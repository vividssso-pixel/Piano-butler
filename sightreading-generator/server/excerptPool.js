// ---------------------------------------------------------------------------
// Piano Butler - Sight-Reading Generator "warm pool" (2026-09-16).
//
// The generator page always requests the exact same fixed shape --
// { realm: 'reading', hands: 'auto', feel: null, feelSource: null }, only
// `grade` varies (see client/public/app.js: REALM is hardcoded, the old
// Style/"feel" picker was disabled, and hands is always 'auto') -- so
// instead of compiling a brand-new excerpt live for every visitor (the
// ~10-40s+ LilyPond compile that's the real bottleneck on Render's free
// 0.1 vCPU tier), we keep a small pool of already-compiled excerpts ready
// per grade, topped up quietly in the background between requests, and
// hand one out instantly when a visitor clicks Generate.
//
// This does NOT reduce how long any single compile takes -- it just moves
// the wait from "while the visitor is staring at a spinner" to "before
// anyone asked", using idle time the free instance already has between
// visitors. A live compile is still the fallback whenever the pool for a
// grade happens to be empty (e.g. right after a burst of clicks, or right
// after a cold boot before the pool has filled).
// ---------------------------------------------------------------------------

const { v4: uuidv4 } = require('uuid');
const { generateExcerpt } = require('./generator');
const { compileExcerpt } = require('./lilypondCompiler');
const { runGated } = require('./compileGate');
const { GRADES } = require('./generator/gradeParams');

const GRADE_IDS = GRADES.map((g) => g.id);
const TARGET_PER_GRADE = 2; // small on purpose -- weak CPU, keep the standing footprint modest
const REFILL_PAUSE_MS = 3000; // breathing room between background compiles

const pools = Object.fromEntries(GRADE_IDS.map((id) => [id, []]));
let liveRequestsInFlight = 0;

function markLiveRequestStart() {
  liveRequestsInFlight++;
}
function markLiveRequestEnd() {
  liveRequestsInFlight = Math.max(0, liveRequestsInFlight - 1);
}

// Only the generator page's exact, fixed request shape is poolable -- a
// custom `feel`/`feelSource` or a non-default `hands`/`realm` always falls
// through to a live, on-demand compile instead.
function isPoolableRequest({ realm, hands, feel, feelSource }) {
  return (!realm || realm === 'reading') && (!hands || hands === 'auto') && !feel && !feelSource;
}

function takeFromPool(gradeId) {
  const pool = pools[gradeId];
  if (!pool || pool.length === 0) return null;
  const item = pool.shift();
  const { _pooledAt, ...payload } = item;
  return payload;
}

function poolStatus() {
  return Object.fromEntries(Object.entries(pools).map(([id, list]) => [id, list.length]));
}

async function buildOne(gradeId, outputDir) {
  const { lySource, lySourceTreble, lySourceBass, meta } = generateExcerpt({
    gradeId,
    realm: 'reading',
    hands: 'auto',
    feel: null,
    feelSource: null,
  });
  const id = uuidv4();
  const compiled = await runGated(() => compileExcerpt(lySource, outputDir, id, { treble: lySourceTreble, bass: lySourceBass }), 'background');
  return {
    id,
    pdfUrl: `/output/${id}.pdf`,
    pdfPending: compiled.pdfPending,
    pngUrl: `/output/${id}.png`,
    pngUrlTreble: compiled.pngPathTreble ? `/output/${id}.treble.png` : null,
    pngUrlBass: compiled.pngPathBass ? `/output/${id}.bass.png` : null,
    mp3Url: compiled.audioPending ? `/output/${id}.mp3` : null,
    audioPending: compiled.audioPending,
    lySource,
    lySourceTreble,
    lySourceBass,
    meta,
    _pooledAt: Date.now(),
  };
}

// Runs forever once started (fire-and-forget from server.js). Deliberately
// serial, one excerpt at a time, and steps aside completely whenever a real
// visitor's request is in flight -- background pool-filling must never
// compete with, and slow down, someone actually waiting on the page.
async function refillLoop(outputDir) {
  for (;;) {
    try {
      if (liveRequestsInFlight === 0) {
        const needy = GRADE_IDS.find((id) => pools[id].length < TARGET_PER_GRADE);
        if (needy) {
          const item = await buildOne(needy, outputDir);
          pools[needy].push(item);
          console.log(`[excerptPool] refilled "${needy}" (${pools[needy].length}/${TARGET_PER_GRADE})`);
        }
      }
    } catch (err) {
      console.error('[excerptPool] background refill failed (non-fatal):', err.message);
    }
    await new Promise((r) => setTimeout(r, REFILL_PAUSE_MS));
  }
}

module.exports = {
  isPoolableRequest,
  takeFromPool,
  poolStatus,
  refillLoop,
  markLiveRequestStart,
  markLiveRequestEnd,
};
