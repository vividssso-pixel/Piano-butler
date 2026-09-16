// ---------------------------------------------------------------------------
// Piano Butler - Sight-Reading Generator API + static app server.
//
// Routes:
//   GET  /sight-reading-generator      -> the generator page (SPA)
//   GET  /api/grades                   -> grade taxonomy for the dropdown
//   POST /api/generate-sightreading    -> generate a fresh excerpt
//
// 2026-09-03: Explorer Bank (a separately-curated "famous piece" library)
// was retired -- it ended up doing the same job as Mission Bank ("a place
// to save pieces"), just for manually-typed-in repertoire instead of
// generated excerpts, and Sohyun asked to fold the two into one rather than
// keep maintaining two overlapping "saved pieces" concepts. Its "Generate
// similar sight-reading" idea (nudging the generator toward a tagged
// meter/left-hand feel) survives as the Generator page's own "Style"
// dropdown instead -- see client/public/app.js's STYLE_PRESETS -- so a
// teacher no longer needs a curated piece on file at all to use it.
//
// 2026-09-15: Mission Bank ITSELF then retired too, ahead of finally
// deploying this app publicly ("미션뱅크는 그냥 없애자, 스토리지 쓸데없이 만들
// 필요는 없을 듯"). Two real reasons, not just "simplify the UI": (1) the
// free hosting tier this is headed to (Render's free Web Service, chosen
// specifically to keep this at $0/month) wipes the filesystem on every
// redeploy/restart/spin-down -- a "save for later" feature backed by local
// disk would silently lose everything the very first time the service
// spins down from inactivity, which is worse than not having the feature
// at all. (2) The actual UI need it was serving -- getting a piece OUT of
// the browser and to a student -- is already covered more simply by the
// existing "Download PDF" button plus the new "Share" button (Web Share
// API on the CURRENT excerpt's already-generated PDF, no server-side
// storage involved at all). Old saved records from before this change may
// still sit in storage/mission-bank/ on disk -- left untouched (not this
// session's data to delete), just fully disconnected from the app now.
// ---------------------------------------------------------------------------

const express = require('express');
const path = require('path');
const fs = require('fs');
const { v4: uuidv4 } = require('uuid');

const { generateExcerpt, REALMS } = require('./generator');
const { GRADES } = require('./generator/gradeParams');
const { compileExcerpt, renderLazyView, warmUp } = require('./lilypondCompiler');
const excerptPool = require('./excerptPool');
const { runGated } = require('./compileGate');

const app = express();
const PORT = process.env.PORT || 3000;

const OUTPUT_DIR = path.join(__dirname, 'output');
fs.mkdirSync(OUTPUT_DIR, { recursive: true });

app.use(express.json({ limit: '2mb' }));
app.use('/output', express.static(OUTPUT_DIR));
app.use(express.static(path.join(__dirname, '..', 'client', 'public')));

// ---------------------------------------------------------------------------
// Pages
// ---------------------------------------------------------------------------
app.get('/sight-reading-generator', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'client', 'public', 'index.html'));
});

// ---------------------------------------------------------------------------
// Health check (2026-09-15) -- CORS-open on purpose: this is the one route
// thepianobutler.com's sight-reading-loading.html page (a different origin,
// onrender.com vs. the main GitHub Pages domain) needs to poll from outside
// this app, to tell "our Express app is actually up" apart from Render's
// own "waking up" splash page, which answers every route while the real
// app is still booting but never returns this JSON shape. No sensitive
// data here, so open CORS is fine.
// ---------------------------------------------------------------------------
app.get('/api/health', (req, res) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.json({ ok: true, ts: Date.now() });
});

// ---------------------------------------------------------------------------
// Grade taxonomy
// ---------------------------------------------------------------------------
app.get('/api/grades', (req, res) => {
  const grades = GRADES.map((g) => ({ id: g.id, label: g.label, claraAlias: g.claraAlias }));
  res.json({ grades, realms: REALMS });
});

// ---------------------------------------------------------------------------
// Drill Bank generation (POST /api/generate-sightreading)
// ---------------------------------------------------------------------------
app.post('/api/generate-sightreading', async (req, res) => {
  try {
    const { grade, realm, hands, feel, feelSource } = req.body || {};
    if (!grade) return res.status(400).json({ error: 'grade is required' });

    // 2026-09-16: the generator page always sends the exact same fixed
    // shape (realm 'reading', hands 'auto', no feel) -- only `grade`
    // varies -- so most requests can be served instantly from a small
    // background-refilled pool of already-compiled excerpts instead of
    // paying the ~10-40s+ LilyPond compile live while the visitor waits.
    // See excerptPool.js for the full rationale. Anything outside that
    // fixed shape (a custom feel/hands/realm) always falls through to a
    // live compile below, same as before this change.
    if (excerptPool.isPoolableRequest({ realm, hands, feel, feelSource })) {
      const pooled = excerptPool.takeFromPool(grade);
      if (pooled) {
        res.json(pooled);
        return;
      }
      // Pool empty for this grade (cold boot, or a burst of clicks) --
      // fall through to the normal live-compile path below.
    }

    excerptPool.markLiveRequestStart();
    try {
      // `feel` (optional) is the Generator page's "Style" dropdown hint --
      // { timeSig?, leftHandStyle?, character? }, built client-side from a
      // fixed preset list (see app.js's STYLE_PRESETS -- this used to come
      // from a curated Explorer Bank piece's tags instead; that page was
      // retired 2026-09-03). generateExcerpt only ever applies
      // timeSig/leftHandStyle when they fall within THIS grade's own
      // confirmed pools, so a mismatched hint degrades to the grade's normal
      // random behavior rather than erroring.
      const { lySource, lySourceTreble, lySourceBass, meta } = generateExcerpt({
        gradeId: grade,
        realm,
        hands,
        feel: feel && typeof feel === 'object' ? feel : null,
        feelSource: typeof feelSource === 'string' ? feelSource.slice(0, 120) : null,
      });
      const id = uuidv4();
      const compiled = await runGated(() => compileExcerpt(lySource, OUTPUT_DIR, id, { treble: lySourceTreble, bass: lySourceBass }), 'live');

      res.json({
        id,
        // 2026-09-15: the full-page PDF compile also no longer finishes
        // before this response -- see lilypondCompiler.js's compileExcerpt.
        // pdfUrl is its eventual path; pdfPending tells the client to poll
        // it (app.js's pollForPdf) rather than link it immediately.
        pdfUrl: `/output/${id}.pdf`,
        pdfPending: compiled.pdfPending,
        pngUrl: `/output/${id}.png`,
        // Only set when the piece actually has a second staff (see
        // generator/index.js) -- lets the hands-view toggle hide itself for
        // one-hand grades instead of pointing at a nonexistent image.
        pngUrlTreble: compiled.pngPathTreble ? `/output/${id}.treble.png` : null,
        pngUrlBass: compiled.pngPathBass ? `/output/${id}.bass.png` : null,
        // 2026-09-15: audio is no longer generated before this response goes
        // out (see lilypondCompiler.js's 2026-09-15 note on compileExcerpt).
        // mp3Url is the file's EVENTUAL path even though it doesn't exist
        // yet when audioPending is true -- the client polls exactly this
        // URL until it 200s (see app.js's pollForAudio) rather than needing
        // a separate status route. Null only when this piece never gets
        // audio at all (no \midi block emitted).
        mp3Url: compiled.audioPending ? `/output/${id}.mp3` : null,
        audioPending: compiled.audioPending,
        lySource,
        lySourceTreble,
        lySourceBass,
        meta,
      });
    } finally {
      excerptPool.markLiveRequestEnd();
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
});

// Regenerate is just another call to the same endpoint from the client with
// the same {grade, realm, hands} -- no server-side state needed, since
// generation is cheap/fast/free per spec (no caching required).

// ---------------------------------------------------------------------------
// Lazy hands-view preview (2026-09-15)
// ---------------------------------------------------------------------------
// The original generate call always used to also pre-render the "Right
// hand only" / "Left hand only" preview images, even though most visitors
// never touch that toggle -- wasted LilyPond/compose work on an already
// CPU-starved free-tier instance, on every single excerpt. Now the client
// only asks for one of these when a visitor actually clicks the toggle,
// passing back the treble/bass .ly source text it already received from
// the original generate response (nothing new to remember server-side).
app.post('/api/sightreading-view', async (req, res) => {
  try {
    const { id, view, lySource } = req.body || {};
    if (!id || typeof id !== 'string' || !/^[a-f0-9-]{10,60}$/i.test(id)) {
      return res.status(400).json({ error: 'invalid id' });
    }
    // The id must belong to an excerpt this instance actually generated --
    // cheap guard against using this route to compile arbitrary LilyPond
    // source under a made-up id.
    if (!fs.existsSync(path.join(OUTPUT_DIR, `${id}.ly`))) {
      return res.status(404).json({ error: 'unknown excerpt id' });
    }
    if (view !== 'treble' && view !== 'bass') {
      return res.status(400).json({ error: 'view must be "treble" or "bass"' });
    }
    if (!lySource || typeof lySource !== 'string' || lySource.length > 20000) {
      return res.status(400).json({ error: 'invalid lySource' });
    }
    const pngPath = await runGated(() => renderLazyView(lySource, OUTPUT_DIR, id, view), 'live');
    if (!fs.existsSync(pngPath)) throw new Error('preview render did not produce a PNG');
    res.json({ pngUrl: `/output/${id}.${view}.png` });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Piano Butler Sight-Reading Generator running at http://localhost:${PORT}`);
  console.log(`  -> Generator: http://localhost:${PORT}/sight-reading-generator`);
  // Fire-and-forget: don't delay opening the port (Render's health check
  // needs that promptly) -- see warmUp()'s own comment for what this buys.
  runGated(() => warmUp(), 'background').catch((err) => console.error('LilyPond warm-up failed (non-fatal):', err.message));
  // 2026-09-16: also fire-and-forget -- keeps topping up excerptPool's
  // per-grade pools forever in the background, stepping aside whenever a
  // real visitor's request is in flight. Never resolves; errors inside it
  // are already caught per-iteration (see excerptPool.js), so nothing here
  // should ever actually reject, but we guard anyway.
  excerptPool.refillLoop(OUTPUT_DIR).catch((err) => console.error('excerptPool refill loop crashed:', err.message));
});
