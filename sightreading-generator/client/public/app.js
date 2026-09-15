// Sight-Reading Generator front-end (vanilla JS, no build step).

const gradeSelect = document.getElementById('grade');
const generateBtn = document.getElementById('generateBtn');
const previewArea = document.getElementById('previewArea');

// "Realm focus" (Reading/Rhythm/Technique) is no longer a user-facing
// toggle (2026-08-27) -- the three realms don't yet produce a visibly
// different excerpt (see generator/index.js's KNOWN GAP note: only the
// melodic-motion weights/hand-position window differ, which reads as noise
// rather than a meaningful choice), so showing three options that don't
// clearly do different things was just confusing. Always generate as
// 'reading' for now; the backend still fully supports all three realms, so
// this can come back as a real toggle once the realms actually diverge.
const REALM = 'reading';

let current = null; // last generated { id, pdfUrl, pngUrl, lySource, meta }

// 2026-09-10: the "Style" dropdown (waltz/minuet/march/lyrical/pastorale/
// gavotte presets, added 2026-09-03) is removed from the UI for now, per
// direct request ("이 스타일 그냥 없애자 지금은, 나중에 더 디테일하게 가더라도" --
// drop it for now, even if it comes back more fully built out later). The
// backend (generator/index.js's opts.feel: { timeSig?, leftHandStyle?,
// character? }) still fully supports this -- nothing removed there -- so a
// future pass can reintroduce a style picker without touching the API.
// generate() below now always sends feel: null.

// "Hands" is no longer a user-facing toggle (2026-08-27) -- every grade now
// always renders in its own authentic format (one melodic line handing off
// between clefs for Preliminary/Grade 1/2, a real "hands together" texture
// from Grade 4 on, etc; see gradeParams.js/index.js resolveHands). Forcing
// an override like "Hands together" onto a grade that never actually uses
// that texture produced results that didn't match any real sight-reading
// book, which is why the option was removed rather than just relabeled.
const HANDS_LABELS = {
  together: 'Hands together',
  alternating: 'Hands alternating',
  'one-hand': 'One hand',
};

async function loadGrades() {
  const res = await fetch('/api/grades');
  const data = await res.json();
  gradeSelect.innerHTML = data.grades
    .map((g) => `<option value="${g.id}">${g.label}</option>`)
    .join('');
}

function renderPlaceholder(text) {
  previewArea.innerHTML = `<div class="placeholder">${text}</div>`;
}

function renderSpinner() {
  previewArea.innerHTML = `<div class="spinner">Engraving your excerpt…<br><span class="spinner-note">This can take up to a minute the first time — thanks for waiting.</span></div>`;
}

function renderError(msg) {
  previewArea.innerHTML = `<div class="error-box">Couldn't generate an excerpt: ${escapeHtml(msg)}</div>`;
}

// Which hands-view is currently showing ('both' | 'treble' | 'bass') --
// reset to 'both' on every fresh generate/regenerate.
let currentView = 'both';

function pngUrlForView(data, view) {
  if (view === 'treble') return data.pngUrlTreble;
  if (view === 'bass') return data.pngUrlBass;
  return data.pngUrl;
}

function renderResult(data) {
  current = data;
  currentView = 'both';
  const { pdfUrl, mp3Url, meta, pngUrlTreble, pngUrlBass } = data;
  const hasHandsView = !!(pngUrlTreble && pngUrlBass);

  previewArea.innerHTML = `
    ${hasHandsView ? `
    <div class="hands-toggle" id="handsViewToggle" style="margin-bottom:12px">
      <button data-view="both" class="selected">Both hands</button>
      <button data-view="treble">Right hand</button>
      <button data-view="bass">Left hand</button>
    </div>` : ''}
    <div class="sheet-wrap"><img id="previewImg" src="${pngUrlForView(data, 'both')}?t=${Date.now()}" alt="Generated sight-reading excerpt" /></div>
    <div class="meta-row">
      <span class="pill">${meta.gradeLabel}</span>
      <span class="pill">${capitalize(meta.realm)}</span>
      <span class="pill">${meta.key}</span>
      <span class="pill">${meta.timeSig}</span>
      <span class="pill">${meta.barCount} bars</span>
      <span class="pill">${HANDS_LABELS[meta.hands] || 'One hand'}</span>
      ${meta.feelSource ? `<span class="pill">🎯 ${escapeHtml(meta.feelSource)}</span>` : ''}
    </div>
    ${mp3Url ? `
    <div class="player-row">
      <span class="player-label">Listen back (practice tempo)</span>
      <audio controls src="${mp3Url}?t=${Date.now()}" style="width:100%"></audio>
    </div>` : ''}
    <div class="action-row">
      <a class="secondary" style="text-decoration:none;display:inline-block;text-align:center" href="${pdfUrl}" download>Download PDF</a>
      <button class="secondary" id="shareBtn">Share</button>
      <button class="secondary" id="regenerateBtn">Regenerate</button>
      <span id="shareStatus" style="margin-left:2px;font-size:13px;color:#1f9d63;align-self:center"></span>
    </div>
  `;

  if (hasHandsView) {
    const toggle = document.getElementById('handsViewToggle');
    toggle.addEventListener('click', (e) => {
      const btn = e.target.closest('button[data-view]');
      if (!btn) return;
      currentView = btn.dataset.view;
      toggle.querySelectorAll('button').forEach((b) => b.classList.toggle('selected', b === btn));
      document.getElementById('previewImg').src = `${pngUrlForView(current, currentView)}?t=${Date.now()}`;
    });
  }

  document.getElementById('regenerateBtn').addEventListener('click', generate);
  document.getElementById('shareBtn').addEventListener('click', shareExcerpt);
}

// 2026-09-15: replaces the old "Save to Mission Bank" flow (removed --
// see server.js's 2026-09-15 comment for why: no server-side storage at
// all now, so this shares the CURRENT excerpt's already-generated PDF
// directly, right now, from the browser -- nothing to keep alive on a
// free hosting tier that wipes disk on every spin-down). Prefers the Web
// Share API with an actual attached FILE (works on iOS/Android/most
// modern desktop browsers over HTTPS) so the recipient gets the real PDF,
// not just a link that stops working once this server instance restarts.
// Falls back to the Web Share API's link-only form, then to copying the
// (session-lifetime-only) PDF link to the clipboard, for browsers with no
// Web Share support at all (most desktop browsers as of this writing).
async function shareExcerpt() {
  if (!current) return;
  const statusEl = document.getElementById('shareStatus');
  const setStatus = (text, color) => { if (statusEl) { statusEl.textContent = text; statusEl.style.color = color; } };
  const fileName = `sight-reading-${(current.meta.gradeLabel || 'excerpt').replace(/\s+/g, '-')}.pdf`;
  const shareText = `${current.meta.gradeLabel} sight-reading excerpt (${current.meta.key}, ${current.meta.timeSig}) — Piano Butler`;
  try {
    const res = await fetch(current.pdfUrl);
    const blob = await res.blob();
    const file = new File([blob], fileName, { type: 'application/pdf' });
    if (navigator.canShare && navigator.canShare({ files: [file] })) {
      await navigator.share({ files: [file], title: 'Sight-Reading Excerpt', text: shareText });
      setStatus('Shared ✓', '#1f9d63');
      return;
    }
    if (navigator.share) {
      await navigator.share({ title: 'Sight-Reading Excerpt', text: shareText, url: new URL(current.pdfUrl, window.location.href).href });
      setStatus('Shared ✓', '#1f9d63');
      return;
    }
    await navigator.clipboard.writeText(new URL(current.pdfUrl, window.location.href).href);
    setStatus('Link copied (works while this page stays open)', '#6b7280');
  } catch (err) {
    if (err.name === 'AbortError') return; // user cancelled the native share sheet -- not an error
    setStatus(`Couldn't share: ${err.message}`, '#a3271a');
  }
}

// A "gateway-style" failure is what we see when Render's proxy answers
// before the app itself is ready to (or the app briefly restarts) --
// the body is an HTML error page ("<!DOCTYPE ...") instead of JSON, so
// res.json() throws a generic "Unexpected token '<'... is not valid
// JSON" parse error. That message is technically true but meaningless to
// a teacher/student seeing it, and -- unlike a real generation failure --
// it's usually gone if you just wait a few seconds and try again (2026-09-15,
// after Sohyun reported this happening live). We detect it and retry once
// automatically before ever showing the person an error.
function isGatewayStyleError(err) {
  return err instanceof SyntaxError || /Unexpected token|is not valid JSON/i.test(err.message || '');
}

async function requestExcerpt(grade) {
  const res = await fetch('/api/generate-sightreading', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      grade,
      realm: REALM,
      hands: 'auto',
      feel: null,
      feelSource: null,
    }),
  });
  if (!res.ok) {
    let serverMsg = 'generation failed';
    try { serverMsg = (await res.json()).error || serverMsg; } catch (_) { /* non-JSON error body -- fall through */ }
    throw new Error(serverMsg);
  }
  return res.json();
}

async function generate() {
  const grade = gradeSelect.value;
  generateBtn.disabled = true;
  renderSpinner();
  try {
    let data;
    try {
      data = await requestExcerpt(grade);
    } catch (err) {
      if (!isGatewayStyleError(err)) throw err;
      // One silent retry after a short pause -- this is almost always the
      // service finishing its boot, not a real problem with the excerpt.
      previewArea.innerHTML = `<div class="spinner">Still warming up — trying again…<br><span class="spinner-note">This only happens right after the generator has been idle.</span></div>`;
      await new Promise((r) => setTimeout(r, 4000));
      data = await requestExcerpt(grade);
    }
    renderResult(data);
  } catch (err) {
    if (isGatewayStyleError(err)) {
      renderError("the generator is still waking up. Please wait a few seconds and click Generate again.");
    } else {
      renderError(err.message);
    }
  } finally {
    generateBtn.disabled = false;
  }
}

generateBtn.addEventListener('click', generate);

function capitalize(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
function escapeHtml(s) { return s.replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }

loadGrades();
