# Her 16 Nov: the player side of the fine marks (marks.py). Spliced into the Read & listen page by readpage2.py.
CSS = r'''
#ov2{position:absolute;inset:0;pointer-events:none}
.mkhi{position:absolute;border-radius:3px;background:linear-gradient(transparent 30%,rgba(255,206,84,.72) 30%,rgba(255,206,84,.72) 100%);transform-origin:left center;animation:mkpen .5s ease-out both;mix-blend-mode:multiply}
.mkhi.old{opacity:.0;transition:opacity .5s}
.mkkey{position:absolute;border-radius:1px 1px 4px 4px;background:rgba(255,206,84,.5);box-shadow:inset 0 -5px 0 rgba(255,170,0,.75);mix-blend-mode:multiply;animation:mkkey .4s ease-out both}
.mkkey.now{background:rgba(255,196,64,.78);box-shadow:inset 0 -7px 0 #f2a900,0 0 0 2px rgba(242,169,0,.55);animation:mkkey .4s ease-out both,mkpress .5s ease-out}
.mkbadge{position:absolute;transform:translate(-50%,-118%);min-width:1.9em;height:1.9em;padding:0 .35em;border-radius:99px;background:#26296b;color:#fff;font:800 clamp(10px,1.35vw,15px)/1.9em 'Atkinson Hyperlegible',Arial,sans-serif;text-align:center;box-shadow:0 2px 6px rgba(20,22,60,.3);animation:mkbadge .35s cubic-bezier(.3,1.6,.5,1) both}
.mkbadge{display:none} .mkbadge.now{display:block}
.mkblk{position:absolute;border-radius:2px;box-shadow:0 0 0 4px #ffc440,0 0 18px rgba(255,196,64,.95);animation:mkblk 1.1s ease-in-out infinite alternate}
@keyframes mkpen{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
@keyframes mkkey{from{opacity:0}to{opacity:1}} @keyframes mkpress{0%{transform:translateY(0)}35%{transform:translateY(2%)}100%{transform:none}} @keyframes mkbadge{from{transform:translate(-50%,-60%) scale(.4);opacity:0}to{transform:translate(-50%,-118%);opacity:1}}
@keyframes mkblk{from{box-shadow:0 0 0 2px #ffc440,0 0 6px rgba(255,196,64,.5)}to{box-shadow:0 0 0 4px #ffc440,0 0 20px rgba(255,196,64,1)}}
@media (prefers-reduced-motion:reduce){.mkhi,.mkkey,.mkblk{animation:none}}
'''
JS = r'''
// her 16 Nov: the fine marks: the words being said get a highlighter stroke, the keys named or played light up one by one,
// black keys glow when the voice talks about them. On a phone the page follows the marks, close up.
let ov2 = null; const mkOn = new Map();
function popLayer(id) {   // an overlay exactly over the pop-up picture now showing (if it is this example)
  if (!lensEl || !(lensEl.dataset.k || '').includes('pops/' + id)) return null;
  const box = lensEl.querySelector('.popl'), img = box && box.querySelector('img'); if (!img || !img.complete) return null;
  box.style.position = 'relative'; let L = box.querySelector('.mkpop');
  if (!L) { L = document.createElement('div'); L.className = 'mkpop'; box.appendChild(L); }
  Object.assign(L.style, { position: 'absolute', pointerEvents: 'none', left: img.offsetLeft + 'px', top: img.offsetTop + 'px', width: img.offsetWidth + 'px', height: img.offsetHeight + 'px' });
  return L;
}
function drawMarks(ln, t) {
  if (!ov2) { ov2 = document.createElement('div'); ov2.id = 'ov2'; stage.appendChild(ov2); }
  const pg = CH[ci].pages[pi]; const act = (ln && ln.mk || []).filter(m => t >= m.t && t < m.e && (m.pop ? popLayer(m.pop) : m.p === pg));
  const idOf = m => ln.t0 + ':' + m.k + ':' + m.t + ':' + (m.pop || '') + m.r[0].join(',');
  const want = new Set(act.map(idOf));
  for (const [id, el] of mkOn) if (!want.has(id) || !el.isConnected) { el.remove(); mkOn.delete(id); }
  const lastKey = act.filter(m => m.k === 'key').pop();
  act.forEach(m => { const id = idOf(m); let el = mkOn.get(id);
    if (!el) { el = document.createElement('div'); el.className = 'mkg';
      el.innerHTML = m.r.map(([x, y, w, h], i) => m.k === 'hi' ? `<div class="mkhi" style="left:${x * 100 - .3}%;top:${y * 100 - .15}%;width:${w * 100 + .6}%;height:${h * 100 + .3}%;animation-delay:${i * .35}s"></div>`
        : m.k === 'key' ? `<div class="mkkey" style="left:${x * 100}%;top:${y * 100}%;width:${w * 100}%;height:${h * 100}%"></div>` + (m.n ? `<div class="mkbadge" style="left:${(x + w / 2) * 100}%;top:${(y + h) * 100}%">${m.n}</div>` : '')
        : `<div class="mkblk" style="left:${x * 100}%;top:${y * 100}%;width:${w * 100}%;height:${h * 100}%;animation-delay:${i * .12}s"></div>`).join('');
      (m.pop ? popLayer(m.pop) : ov2).appendChild(el); mkOn.set(id, el); }
    el.querySelectorAll('.mkkey,.mkbadge').forEach(k => k.classList.toggle('now', m === lastKey)); });
  return act.filter(m => !m.pop);
}
function clearMarks() { if (ov2) ov2.innerHTML = ''; mkOn.forEach(el => el.remove()); mkOn.clear(); }
function markBox(act) {   // the union of what is lit now: the latest phrase's words, or the keys
  const hi = act.filter(m => m.k === 'hi').pop(); const ks = act.filter(m => m.k !== 'hi'); const use = ks.length ? ks : (hi ? [hi] : []);
  const rs = use.flatMap(m => m.r); if (!rs.length) return null;
  const x0 = Math.min(...rs.map(r => r[0])), y0 = Math.min(...rs.map(r => r[1])), x1 = Math.max(...rs.map(r => r[0] + r[2])), y1 = Math.max(...rs.map(r => r[1] + r[3]));
  return [x0, y0, x1 - x0, y1 - y0];
}
'''
# in tick(): draw the marks; on a narrow screen, frame the marks instead of the whole region
TICK_OLD = "  const c = ln.cue;\n  if (c && follow) {"
TICK_NEW = "  const act = follow ? drawMarks(ln, t) : (clearMarks(), []);\n  const c = ln.cue;\n  if (c && follow) {"
ZOOM_OLD = "      const [x, y, w, h] = reg.b; const S = Math.min(2.2, Math.max(1, 0.94 / w));"
ZOOM_NEW = ("      let [x, y, w, h] = reg.b; let S = Math.min(2.2, Math.max(1, 0.94 / w));\n"
            "      const mb = act.length && act[0].p === c.p ? markBox(act) : null;\n"
            "      if (mb) { const ph = window.innerWidth < 760; const fx = mb[0] + mb[2] / 2, fy = mb[1] + mb[3] / 2; const S2 = ph ? Math.min(2.4, Math.max(1.2, 0.8 / Math.max(mb[2], 0.3))) : Math.min(1.5, Math.max(1.15, 0.75 / Math.max(mb[2], 0.35))); const tx2 = Math.min(0, Math.max(1 - S2, 0.5 - S2 * fx)), ty2 = Math.min(0, Math.max(1 - S2, 0.42 - S2 * fy)); stage.style.transform = `translate(${tx2 * 100}%, ${ty2 * 100}%) scale(${S2})`; }\n"
            "      const zoomed = !!mb;")
TRANS_OLD = "      stage.style.transform = `translate(${tx * 100}%, ${ty * 100}%) scale(${S})`;\n      lensEl"
TRANS_NEW = "      if (!zoomed) stage.style.transform = `translate(${tx * 100}%, ${ty * 100}%) scale(${S})`;\n      lensEl"
SUB_OLD = "if (hit) txt = txt.slice(0, hit[2]) + '<mark>' + txt.slice(hit[2], hit[3]) + '</mark>' + txt.slice(hit[3]);"
SUB_NEW = SUB_OLD + " else if (ln.sp && follow) { const s = ln.sp.filter(x => x[0] <= t).pop(); if (s) txt = txt.slice(0, s[1]) + '<mark>' + txt.slice(s[1], s[2]) + '</mark>' + txt.slice(s[2]); }"
CLEAR_OLD = "function clearFollow() { if (typeof drawLens === 'function') drawLens(null); ov.innerHTML = '';"
CLEAR_NEW = "function clearFollow() { if (typeof drawLens === 'function') drawLens(null); if (typeof clearMarks === 'function') clearMarks(); ov.innerHTML = '';"
def splice(html):
    for a, b in ((SUB_OLD, SUB_NEW), (TICK_OLD, TICK_NEW), (ZOOM_OLD, ZOOM_NEW), (TRANS_OLD, TRANS_NEW), (CLEAR_OLD, CLEAR_NEW)):
        assert html.count(a) == 1, a[:60]
        html = html.replace(a, b)
    html = html.replace('</style>', CSS + '</style>', 1)
    html = html.replace('function tick() {', JS + '\nfunction tick() {', 1)
    return html
