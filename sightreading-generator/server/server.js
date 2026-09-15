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
const { v4: uuidv4 } = require('uuid');

const { generateExcerpt, REALMS } = require('./generator');
const { GRADES } = require('./generator/gradeParams');
const { compileExcerpt } = require('./lilypondCompiler');

const app = express();
const PORT = process.env.PORT || 3000;

const OUTPUT_DIR = path.join(__dirname, 'output');
require('fs').mkdirSync(OUTPUT_DIR, { recursive: true });

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
    const compiled = await compileExcerpt(lySource, OUTPUT_DIR, id, { treble: lySourceTreble, bass: lySourceBass });

    res.json({
      id,
      pdfUrl: `/output/${id}.pdf`,
      pngUrl: `/output/${id}.png`,
      // Only set when the piece actually has a second staff (see
      // generator/index.js) -- lets the hands-view toggle hide itself for
      // one-hand grades instead of pointing at a nonexistent image.
      pngUrlTreble: compiled.pngPathTreble ? `/output/${id}.treble.png` : null,
      pngUrlBass: compiled.pngPathBass ? `/output/${id}.bass.png` : null,
      // Audio is best-effort (see lilypondCompiler.js) -- null when
      // fluidsynth/ffmpeg rendering didn't succeed, so the frontend can
      // hide the player instead of pointing at a missing file.
      mp3Url: compiled.mp3Path ? `/output/${id}.mp3` : null,
      lySource,
      lySourceTreble,
      lySourceBass,
      meta,
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: err.message });
  }
});

// Regenerate is just another call to the same endpoint from the client with
// the same {grade, realm, hands} -- no server-side state needed, since
// generation is cheap/fast/free per spec (no caching required).

app.listen(PORT, () => {
  console.log(`Piano Butler Sight-Reading Generator running at http://localhost:${PORT}`);
  console.log(`  -> Generator: http://localhost:${PORT}/sight-reading-generator`);
});
