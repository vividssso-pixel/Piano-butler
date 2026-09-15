// ---------------------------------------------------------------------------
// Melody (right-hand) generation: a constrained random walk over scale
// degrees, weighted toward stepwise motion, that respects a hand-position
// range and a per-excerpt cap on "large" leaps -- per the build spec:
//   - stepwise motion weighted higher than leaps
//   - stay within a defined hand-position range (5-finger position early on)
//   - no more than 1-2 leaps larger than a 3rd per excerpt at beginner grades
// ---------------------------------------------------------------------------

const { buildScale, toLilyPitch, raiseBySemitoneLetterAware, pitchClassOf } = require('./scales');
const { KEYS } = require('./gradeParams');

// 2026-09-14: the local PITCH_CLASS lookup table this used to keep (a
// hand-maintained copy of scales.js's own internal table, extended by hand
// each time a new raised spelling showed up -- cisis/disis/fisis/gisis/
// aisis/eis/bis) is gone. Widening key coverage past 5 sharps/flats made
// that whole approach a liability: any spelling nobody had thought to add
// yet (e.g. "fes", or the double-sharps a 6-7 sharp key's own leading-tone
// raise can produce) would silently return `undefined` here, corrupting
// register-window/anchor math with a NaN. `pitchClassOf`, imported from
// scales.js, computes any letter+accidental spelling's pitch class directly
// instead of looking it up, so there's nothing left to run out of entries.
//
// A scale-array entry's real absolute pitch as a single semitone number
// (octaveOffset*12 + pitch class) -- used to anchor register windows by
// REAL pitch rather than by scale-degree-index alone (see the register
// window anchor comment in generateMelody for why that distinction matters
// for keys whose tonic isn't C).
function absoluteSemitone(entry) {
  return entry.octaveOffset * 12 + pitchClassOf(entry.ly);
}

// Middle C's absolute semitone value under this same reckoning (unmarked
// "c" = 0, one apostrophe = +12) -- the one ledger-line note the treble
// clef is allowed to touch per the build spec.
const MIDDLE_C_SEMITONE = 12;

// Ledger-line-free semitone ranges for each clef under this same reckoning
// (established empirically this session: bass G2-A3, treble D4-F5 with
// middle C as the one allowed exception) -- used to keep a hand-off's
// CONTINUATION target (see the startDegree handling above) from ever
// pulling a window outside its clef's comfortable range, even when the
// previous note sat right at the far edge of the other clef.
const BASS_SAFE_LO = -5;
const BASS_SAFE_HI = 9;
const TREBLE_SAFE_HI = 29;

/**
 * @param {number} totalNotes total melody note-events needed (sum across bars)
 * @param {object} params grade bucket params (position, maxLeapInterval, weights, maxLeapsPerExcerpt)
 * @param {string} keyId key id from gradeParams.KEYS
 * @param {number} [registerBlockShift] shift the center position by this many
 *   full 7-degree octave blocks -- e.g. -1 to generate a left-hand-register
 *   phrase (used for "hands alternating" grades where a single melodic line
 *   hands off between clefs rather than a chordal accompaniment).
 * @param {number} [extraFloorPad] extra scale-degree steps added on top of
 *   the default hand-separation floor pad (see REGISTER_GAP_PAD below) --
 *   used by index.js's register-safety retry to nudge the melody's floor up
 *   a little further when the default pad wasn't enough for a given key,
 *   without jumping a full octave block the way a bigger registerBlockShift
 *   would (which reads as an unnecessarily high-flying melody).
 * @param {boolean} [endOnTonic] snap the LAST generated note to the nearest
 *   tonic scale degree (2026-08-27: a plain random walk has no reason to
 *   land on the tonic, and a piece/phrase that doesn't resolve to "home"
 *   sounds unfinished -- especially noticeable at beginner grades). Pass
 *   true only for the call that produces the excerpt's actual final note;
 *   mid-piece calls (e.g. an alternating excerpt's earlier segments) should
 *   leave this false.
 * @param {number|null} [startDegree] absolute scale-degree index (into the
 *   SAME flat scale array every call for this key shares) to start this
 *   walk from, instead of the window's default "mid" position. 2026-08-27:
 *   "hands alternating" excerpts generate each hand-off segment with an
 *   independent generateMelody() call; without this, every new segment
 *   restarted at its own register's fixed middle regardless of where the
 *   previous segment actually left off, which reads as the melody making a
 *   large (often ~octave) unmotivated jump right at the hand-off -- exactly
 *   the "big leap" a real alternating-hands piece doesn't have (the line is
 *   conceived as ONE continuous melody that simply changes which hand plays
 *   it). Passing the previous segment's final degree here keeps the new
 *   hand's opening note close to where the line actually was. Clamped into
 *   this call's own [low, high] window like every other step, so it never
 *   breaks the hand's register safety guarantees.
 * @returns {{pitches: string[], degrees: number[]}}
 */
function generateMelody(totalNotes, params, keyId, registerBlockShift = 0, extraFloorPad = 0, endOnTonic = false, startDegree = null, avoidOverlapPad = true) {
  const scale = buildScale(keyId, 6);
  const span = params.position.spanScaleDegrees;
  // Anchor the melody's hand-position window by REAL pitch, not by a fixed
  // scale-degree-index formula (2026-08-27) -- scales.js correctly spells
  // each key's degrees using LilyPond's fixed per-letter reference octave
  // (see its own 2026-08-27 fix), which means a tonic far from C (e.g. A
  // minor) has its block's later degrees (c/d/e/f/g) cross into the next
  // real octave partway through. A fixed index formula tuned for C major
  // would land a 9th or more too high for a key like that.
  let targetSemitone = (1 + registerBlockShift) * 12;
  // 2026-08-27: when this call is continuing a hand-off from a previous
  // segment (startDegree given -- see "hands alternating" excerpts in
  // index.js), pull the window's target toward where the melody actually
  // left off, instead of always the generic register-block center. Without
  // this, a hand-off's target was fixed regardless of context -- e.g. the
  // bass hand always targeted the CENTER of its comfortable register block,
  // even when the treble line had just ended right at the boundary between
  // the two clefs. Since the two hands' comfortable windows rarely overlap
  // (that's inherent to switching staves), clamping the previous absolute
  // scale-degree straight into the new window (the old behavior) often
  // landed on whichever edge of the new window was nearest -- which could
  // still be an octave or more from the previous note if that edge wasn't
  // actually close to it. Clamping the CONTINUATION PITCH itself into the
  // safe register range first, then using that as the search target, makes
  // the new hand pick up as close as it comfortably can to where the line
  // actually was, while still never leaving its clef's ledger-line-safe
  // range (verified via the register-violation regression check).
  if (startDegree != null) {
    const clampedStartDegree = Math.max(0, Math.min(scale.length - 1, startDegree));
    const continuationSemitone = absoluteSemitone(scale[clampedStartDegree]);
    targetSemitone =
      registerBlockShift < 0
        ? Math.max(BASS_SAFE_LO, Math.min(BASS_SAFE_HI, continuationSemitone))
        : Math.max(MIDDLE_C_SEMITONE, Math.min(TREBLE_SAFE_HI, continuationSemitone));
  }
  // +1 block vs. the naive "7*(1+shift)" formula -- scales.js's buildScale
  // starts one octave lower than a naive reading would suggest (see its
  // startOctave comment), so what reads as "block 0" is actually index 7.
  const nominalBlockStart = 7 * (2 + registerBlockShift);
  const searchLo = Math.max(0, nominalBlockStart - 14);
  const searchHi = Math.min(scale.length - 1, nominalBlockStart + 14);

  // Nearest TONIC (index a multiple of 7) to the target -- used to anchor
  // the window so it always contains an in-window tonic for endOnTonic to
  // land on (see below for why that's not automatic).
  //
  // 2026-08-27: restricted to candidates at or above middle C (semitone 12).
  // A plain nearest-by-distance search can pick a tonic that sits BELOW
  // middle C (e.g. A minor's tonic pitch classes are semitone 9 or 21 --
  // neither equals the target of 12, and 9 is numerically closer even
  // though it reads a 3rd below middle C, needing a ledger line). Since the
  // treble branch below anchors the window's FLOOR directly on this tonic,
  // picking the below-middle-C option put the window's bottom note (and
  // often its neighbor) below the staff. Requiring >= middle C guarantees
  // the floor is always in-staff (or exactly middle C, the one allowed
  // exception) regardless of how far the key's tonic sits from C.
  let tonicAnchor = null;
  let bestTonicDist = Infinity;
  for (let idx = searchLo; idx <= searchHi; idx += 7) {
    const abs = absoluteSemitone(scale[idx]);
    if (abs < MIDDLE_C_SEMITONE) continue;
    const dist = Math.abs(abs - targetSemitone);
    if (dist < bestTonicDist) {
      bestTonicDist = dist;
      tonicAnchor = idx;
    }
  }
  if (tonicAnchor == null) {
    // Fallback (shouldn't happen given the search range comfortably spans
    // several octaves either side of the target): walk forward from the
    // nominal block start until we find any in-range, at-or-above-middle-C
    // tonic index.
    tonicAnchor = nominalBlockStart;
    while (tonicAnchor < scale.length && absoluteSemitone(scale[tonicAnchor]) < MIDDLE_C_SEMITONE) {
      tonicAnchor += 7;
    }
    tonicAnchor = Math.min(tonicAnchor, scale.length - 1 - ((scale.length - 1) % 7));
  }

  let low;
  let high;
  let mid;
  if (registerBlockShift < 0) {
    // Bass/left-hand register: anchor on whichever SCALE DEGREE (not
    // necessarily the tonic) is closest to the target pitch, centered with
    // room both directions, then clamp so the window can never cross UP
    // out of its anchor octave block -- unlike the treble register, there
    // is no headroom above it before notes read as stranded many ledger
    // lines above the bass staff (the same failure mode the bass-chord
    // octave-crossing bug had).
    let bestDist = Infinity;
    mid = nominalBlockStart;
    for (let idx = searchLo; idx <= searchHi; idx++) {
      const dist = Math.abs(absoluteSemitone(scale[idx]) - targetSemitone);
      if (dist < bestDist) {
        bestDist = dist;
        mid = idx;
      }
    }
    low = mid - Math.floor(span / 2);
    high = low + span;
    // Floor safety: index 0 is the bottom of the built scale array -- for a
    // key whose tonic sits high in the fixed reference octave (e.g. A
    // minor), the closest available real-pitch anchor for the lowest
    // register can itself be index 0 (nothing lower to anchor on), which
    // would otherwise push `low` negative and walk off the front of the
    // array.
    if (low < 0) {
      high -= low; // shift the whole window up by the same amount, keep its width
      low = 0;
    }
    const blockStart = Math.floor(mid / 7) * 7;
    const blockEnd = blockStart + 6;
    high = Math.min(high, blockEnd);
    low = Math.min(low, high);
    // 2026-08-27: hard real-pitch safety trim. The block-based clamp above
    // keeps the window from crossing into the NEXT octave block, but a
    // block's own top degree can still sit above the bass clef's
    // ledger-line-free ceiling (BASS_SAFE_HI) depending on the key's step
    // pattern -- normally harmless when `mid` sits near the block's usual
    // center, but the continuation-pitch target above can push `mid` (and
    // so the whole window) much closer to that ceiling than usual, e.g.
    // right after a treble segment that ended high. Trim from the top
    // (and, symmetrically, the bottom) until every degree in range is
    // actually safe, rather than trusting the block boundary alone.
    while (high > low && absoluteSemitone(scale[high]) > BASS_SAFE_HI) high -= 1;
    while (low < high && absoluteSemitone(scale[low]) < BASS_SAFE_LO) low += 1;
    // The trim above can shrink the window past its block's tonic entirely
    // (e.g. a continuation target sitting well above the block's own
    // center), which would silently break endOnTonic's tail-walk later --
    // its own tonic search is scoped to [low, high], and finding nothing
    // there falls back to a plain nearest-by-index tonic that ignores this
    // window's safety bounds. Pull `low` back down to include the nearest
    // tonic at-or-below `high`, but only when that tonic is itself safe --
    // widening the window a little is preferable to losing the in-window
    // tonic guarantee.
    // 2026-09-14 (same day, second pass): "그레이드별로 다 확인해줘" -- a direct
    // report (Preliminary, one-hand bass clef, E minor: excerpt ended on a
    // non-tonic note) plus a follow-up sweep across every grade/key/hands
    // combination found this branch never got the equivalent fix the
    // TREBLE branch received earlier the same day (see its own 2026-09-14
    // comment below). An first attempt at a fix here only ever shifted the
    // window DOWN a block on the reasoning that "no headroom above" (see
    // this branch's own opening comment) -- wrong for e.g. E minor
    // Preliminary: `mid` there anchors right at the bottom of the array
    // (index 5, real pitch c0), so the tonic at-or-below it (index 0, a
    // full block down) is BELOW BASS_SAFE_LO and unusable, while shifting
    // DOWN further isn't even possible (nothing below index 0) -- the only
    // actually-safe tonic sits one block ABOVE `mid` (index 7, e0, well
    // inside [BASS_SAFE_LO, BASS_SAFE_HI]). "No headroom above" is about
    // not letting the window's CENTER float upward by default, not a rule
    // against ever widening a couple of degrees to reach an otherwise-safe
    // tonic. Correct fix: search outward from `mid` (both directions) for
    // the nearest tonic whose own real pitch is safety-clamped, then widen
    // [low, high] just enough to include it (extend low down if it sits
    // below the window, high up if above) -- minimal, always safe, and
    // does not require the window to have been centered exactly right in
    // the first place.
    let safeTonicIdx = null;
    let bestSafeTonicDist = Infinity;
    for (let t = 0; t < scale.length; t += 7) {
      const abs = absoluteSemitone(scale[t]);
      if (abs < BASS_SAFE_LO || abs > BASS_SAFE_HI) continue;
      const dist = Math.abs(t - mid);
      if (dist < bestSafeTonicDist) {
        bestSafeTonicDist = dist;
        safeTonicIdx = t;
      }
    }
    if (safeTonicIdx != null) {
      if (safeTonicIdx < low) low = safeTonicIdx;
      else if (safeTonicIdx > high) high = safeTonicIdx;
    }
  } else {
    // Treble/right-hand register (2026-08-27 rewrite): anchor the window's
    // FLOOR at the nearest tonic, extending upward by `span` -- a genuine
    // "hand position starting on the tonic" (thumb on doh), same shape as
    // real beginner sight-reading material. This guarantees the tonic is
    // always in [low, high] for endOnTonic to land on: centering the
    // window on the nearest scale DEGREE (as this used to, and as the bass
    // branch above still does) can pick a non-tonic degree whose window
    // doesn't happen to reach back to any tonic, forcing the final note to
    // break out of the comfortable register right at the end -- reported
    // as an otherwise-clean Preliminary excerpt suddenly growing ledger
    // lines only on its very last note.
    // 2026-08-27: this pad exists to stop the two hands' noteheads reading
    // as almost touching when they sound AT THE SAME TIME (see index.js's
    // "hands together" register-safety retry) -- it doesn't apply to
    // "hands alternating" excerpts, where only one hand ever plays at once
    // (see index.js's buildAlternatingExcerpt). Callers pass
    // avoidOverlapPad=false for alternating-mode calls to skip it, since
    // padding there only pushes the tonic further from the window without
    // preventing any real overlap.
    const REGISTER_GAP_PAD = 2;
    const floorPad = avoidOverlapPad ? REGISTER_GAP_PAD + extraFloorPad : 0;
    low = tonicAnchor + floorPad;
    high = low + span;
    // Same real-pitch safety trim as the bass branch above, for the same
    // reason: a continuation target can legitimately push `low` (anchored
    // on a tonic near that target) close to the treble ceiling, and `span`
    // could then carry `high` past it.
    while (high > low && absoluteSemitone(scale[high]) > TREBLE_SAFE_HI) high -= 1;
    // 2026-09-14: "음악이 어색한데" -- traced to a genuinely major bug, not a
    // subtlety: the trim above can (and, for a lot of real grade/key
    // combinations -- G major at EVERY grade including Preliminary, A major,
    // Bb major, and several minors from Grade 5 up, measured directly) cut
    // `high` back so far that it falls BELOW the next tonic up from `low`
    // (`tonicAnchor` itself sits 2+ degrees below `low` because of
    // REGISTER_GAP_PAD, so the window's only remaining in-range tonic is a
    // full octave above `tonicAnchor`, at `tonicAnchor + 7`). When that
    // happens the window this function returns has NO tonic in it at all,
    // even though every comment above (and endOnTonic's whole design) assumes
    // one always exists: endOnTonic's own tonic search then silently falls
    // through to its "not a true tonic, but register-safe" fallback, so the
    // excerpt's LAST note doesn't actually land on the stated key's tonic --
    // an unresolved ending, which is a large, audible part of why a piece
    // can read as "off." It also shrinks the usable window itself down to as
    // few as 3-4 scale degrees regardless of the grade's intended `span`
    // (verified directly: A minor Grade 7, intended span 11, collapsed to
    // span 3), which is why the melody can sound stuck circling the same
    // handful of notes even mid-phrase, not just at the cadence. Root cause
    // is `tonicAnchor` itself sometimes landing high enough (the "nearest
    // tonic at or above middle C" search below can only go up, never down,
    // even when up is a 6th or more away) that GAP_PAD + span reliably
    // overshoots the treble ceiling for that key. Fix: if the trim ate the
    // window's only guaranteed tonic, retry with the whole window shifted
    // down a full octave block (bounded -- verified this always resolves in
    // exactly one shift for every currently affected grade/key combination,
    // landing the floor comfortably within a 3rd of middle C either way) --
    // far better than leaving a phrase that structurally can't resolve.
    // 2026-09-14 (third pass, same day): the original fix here only ever
    // shifted `tonicAnchor` DOWN a block and re-tried. That resolved every
    // grade/key combination measured at the time, but a later, wider sweep
    // ("그레이드별로 다 확인해줘") found a case it can't ever fix: realm
    // 'rhythm' narrows `span` to 2-3, and floorPad is at least
    // REGISTER_GAP_PAD (2) -- whenever floorPad + span < 7, the window
    // [low, high] sits entirely BETWEEN two tonics no matter which block
    // `tonicAnchor` points at (shifting by a full block moves the window
    // and its anchor together, so their relative position never changes).
    // Reproduced directly: Grade 4, realm 'rhythm', hands together, C/G/Bb
    // major. General fix, same shape as the bass branch's equivalent fix
    // just above (see its own 2026-09-14 comment): search outward from
    // `tonicAnchor` for the nearest TREBLE_SAFE_HI-safe tonic in EITHER
    // direction and widen [low, high] just enough to include it, instead of
    // assuming a same-relative-position block shift will eventually find
    // one.
    const nextTonicUp = Math.ceil(low / 7) * 7;
    if (!(nextTonicUp <= high && nextTonicUp >= low)) {
      let safeTonicIdx = null;
      let bestSafeTonicDist = Infinity;
      for (let t = 0; t < scale.length; t += 7) {
        if (absoluteSemitone(scale[t]) > TREBLE_SAFE_HI) continue;
        const dist = Math.abs(t - tonicAnchor);
        if (dist < bestSafeTonicDist) {
          bestSafeTonicDist = dist;
          safeTonicIdx = t;
        }
      }
      if (safeTonicIdx != null) {
        if (safeTonicIdx < low) low = safeTonicIdx;
        else if (safeTonicIdx > high) high = safeTonicIdx;
        tonicAnchor = safeTonicIdx;
      }
    }
    mid = tonicAnchor;
  }

  const maxLeapDegrees = intervalToDegrees(params.maxLeapInterval);
  let bigLeapsUsed = 0;
  const bigLeapCap = params.maxLeapsPerExcerpt;

  // 2026-08-27: pick the FIRST segment's opening note from the tonic TRIAD
  // (1st/3rd/5th of the hand position) rather than always hardcoding the
  // tonic itself. Every previous version started every fresh segment at
  // exactly `mid` (the tonic for the treble branch, since low=tonicAnchor
  // there) -- reported as "even though it's e.g. C major, the excerpt
  // doesn't have to always START on C." Real beginner sight-reading pieces
  // vary which chord tone they open on. Only applies when this call ISN'T
  // continuing a hand-off (startDegree == null, i.e. it's the very first
  // segment of the excerpt) -- a continuing segment must still start
  // exactly where the previous one left off, handled below.
  let degree = mid;
  if (startDegree == null) {
    let openTonicIdx = null;
    let bestOpenTonicDist = Infinity;
    for (let idx = Math.ceil(low / 7) * 7; idx <= high; idx += 7) {
      const dist = Math.abs(idx - mid);
      if (dist < bestOpenTonicDist) {
        bestOpenTonicDist = dist;
        openTonicIdx = idx;
      }
    }
    if (openTonicIdx != null) {
      const openCandidates = [openTonicIdx, openTonicIdx + 2, openTonicIdx + 4].filter(
        (d) => d >= low && d <= high
      );
      degree = openCandidates[Math.floor(Math.random() * openCandidates.length)];
    } else {
      // 2026-08-29: safety fallback. No in-window tonic means `degree`
      // would otherwise stay at its outer initializer (`mid`), which for
      // the treble branch is `tonicAnchor` -- NOT guaranteed to sit inside
      // [low, high] once REGISTER_GAP_PAD/extraFloorPad have shifted the
      // window's floor past it (see index.js's one-hand register-safety
      // fix for how this was first triggered). [low, high] are themselves
      // always kept within the clef-safe range by the trims above, so
      // clamping here is always safe even though it isn't a true tonic.
      degree = Math.max(low, Math.min(high, mid));
    }
  }
  // Tracks whether the PREVIOUS move was a leap (>= a 3rd), so pickMove can
  // refuse to stack a second leap right on top of it (see pickMove's
  // prevWasLeap handling below) -- added 2026-08-27 after a Grade 1 D major
  // sample chained two upward 3rd-leaps back to back (d-f#-a style, outlining
  // a broken chord) which read as noticeably harder than the rest of the
  // batch despite neither leap alone exceeding maxLeapInterval. Real
  // beginner-grade material keeps leaps as isolated events recovered by a
  // step, never chained into an arpeggio shape.
  let prevWasLeap = false;
  if (startDegree != null) {
    // Continue from the previous segment's ending note (see the
    // startDegree doc comment above) -- clamp into this call's own window
    // so a hand-off can never land the new hand outside its safe register.
    degree = Math.max(low, Math.min(high, startDegree));
  }
  const pitches = [];
  const degrees = [];

  // 2026-09-10: phrase-arch setup -- see the pickMove/ARC_STRENGTH comments
  // above for the "why". `arcPeakFrac` is WHERE in this call's note sequence
  // (as a 0-1 fraction) the melody's high point tends to land -- randomized
  // per call, not fixed at dead-center, so a batch of generated excerpts
  // doesn't all peak at exactly the same beat. Kept away from the very
  // edges (0.3-0.7) so both the rising approach and the falling tail
  // actually have room to read as a real climb/descent rather than being
  // clipped by the phrase boundary.
  const arcPeakFrac = 0.3 + Math.random() * 0.4;

  for (let i = 0; i < totalNotes; i++) {
    if (i === 0) {
      pitches.push(toLilyPitch(scale[degree]));
      degrees.push(degree);
      continue;
    }
    // phraseFrac: this note's position through the call, 0 (first note)
    // to 1 (last note). distFromPeak is +1 at the very start (full "rising"
    // bias), 0 exactly at the arch's peak, and -1 at the very end (full
    // "falling" bias) -- a straight linear taper either side of the peak,
    // not a hard switch, so the bias fades smoothly through the high point
    // instead of flipping abruptly right at it.
    const phraseFrac = totalNotes > 1 ? i / (totalNotes - 1) : 0;
    const distFromPeak =
      phraseFrac <= arcPeakFrac
        ? (arcPeakFrac - phraseFrac) / Math.max(arcPeakFrac, 1e-6)
        : -(phraseFrac - arcPeakFrac) / Math.max(1 - arcPeakFrac, 1e-6);
    const upProb = 0.5 + ARC_STRENGTH * distFromPeak;
    const move = pickMove(params, maxLeapDegrees, bigLeapsUsed < bigLeapCap, prevWasLeap, upProb);
    let next = degree + move.delta;

    // Clamp to hand-position window; if clamped, reflect direction so the
    // line doesn't just stick to the boundary repeatedly.
    if (next < low) next = low + (low - next);
    if (next > high) next = high - (next - high);
    next = Math.max(low, Math.min(high, next));

    if (move.isBigLeap) bigLeapsUsed += 1;
    prevWasLeap = move.isLeap;
    degree = next;
    pitches.push(toLilyPitch(scale[degree]));
    degrees.push(degree);
  }

  if (endOnTonic && degrees.length > 0) {
    // Every 7th scale-degree index is a tonic (scales.js lays out each
    // octave block as 7 consecutive degrees starting on the tonic). The
    // nearest tonic to any given degree is at most 3 scale-degrees away
    // (7 degrees per block, so worst case sits exactly between two
    // tonics). Snapping only the very last note to that tonic in one jump
    // could still mean a leap as large as a 4th right at the cadence --
    // too big for grades like Preliminary, which should have almost no
    // leaps at all, including the ending. Instead, re-walk the last few
    // notes (up to 3) as a smooth STEPWISE approach (one scale-degree per
    // note, never more) from an anchor note back from the end, landing
    // exactly on the tonic on the final note. (2026-08-27)
    const lastPos = degrees.length - 1;
    const maxTail = 3;
    const tailLen = Math.min(maxTail, lastPos);
    const anchorPos = lastPos - tailLen;
    const anchorDegree = degrees[anchorPos];
    // 2026-08-27: pick the nearest tonic that's actually reachable INSIDE
    // this call's own [low, high] hand-position window, not just the
    // nearest tonic by raw degree-index distance. A plain round-to-nearest
    // could pick a tonic one block above the window (e.g. anchorDegree
    // sitting near the window's ceiling, with the closer tonic being just
    // outside it) -- landing there means the tail-walk marches the melody
    // straight out of its comfortable register on the very last notes,
    // undoing everything the window anchoring above guarantees.
    let tonicIdx = null;
    let bestTonicDist = Infinity;
    for (let idx = Math.ceil(low / 7) * 7; idx <= high; idx += 7) {
      const dist = Math.abs(idx - anchorDegree);
      if (dist < bestTonicDist) {
        bestTonicDist = dist;
        tonicIdx = idx;
      }
    }
    if (tonicIdx == null) {
      // Fallback: shouldn't happen (every window this function builds is
      // supposed to contain at least one in-range tonic), but a narrow
      // span combined with the treble register-gap pad can still trim the
      // window down past its only tonic (see index.js's one-hand
      // register-safety fix for a concrete case). The old fallback here --
      // `Math.round(anchorDegree / 7) * 7` -- ignored [low, high] entirely
      // and could land a full block above the window's ceiling (reproduced
      // as a final note 2 semitones over TREBLE_SAFE_HI). [low, high] are
      // always kept within the clef-safe range by the trims above, so
      // clamp into that range instead -- not a true tonic, but guaranteed
      // register-safe, which matters more than a perfect cadence.
      tonicIdx = Math.max(low, Math.min(high, Math.round(anchorDegree / 7) * 7));
    }
    const keyMeta = KEYS[keyId];
    let remaining = tonicIdx - anchorDegree;
    let cur = anchorDegree;
    for (let i = 1; i <= tailLen; i++) {
      let stepDir = 0;
      if (remaining !== 0) {
        stepDir = remaining > 0 ? 1 : -1;
        cur += stepDir;
        remaining -= stepDir;
      }
      degrees[anchorPos + i] = cur;
      // 2026-08-31 (re-fixed 2026-09-11): melody.js walks a plain NATURAL
      // minor scale (see scales.js), whose 7th degree sits a WHOLE step
      // below the tonic rather than the half-step "pull" of a real leading
      // tone. Fine for general melodic motion, but the piece's very last
      // cadential approach to the tonic needs that half-step pull -- without
      // it, a minor-key excerpt's ending sounds like it resolved in the
      // RELATIVE MAJOR rather than confirming the stated minor tonic.
      // Only the single note stepping UP into the tonic gets raised
      // (melodic-minor convention: the 7th -- and 6th -- are only raised
      // ascending; descending motion and every other degree stays natural).
      // 2026-09-11: this briefly moved to raising the leading tone
      // UNCONDITIONALLY at the scale-build level (harmonic minor throughout)
      // instead of just here -- reverted (see scales.js's 2026-09-11
      // comment) after a direct report that it made the augmented-2nd
      // "leap-like step" between scale degrees 6-7 show up far more often
      // than real minor-key writing does, since every ordinary stepwise
      // pass through the 7th degree got raised too, not just the cadential
      // one. Back to this single, deliberately narrow context -- but now
      // calling scales.js's letter-aware raise (raiseBySemitoneLetterAware)
      // instead of the old broken pc-lookup one, so the ORIGINAL "더블샵"
      // ask still works correctly right here (e.g. G# minor's cadential
      // leading tone still spells as F double-sharp, not a wrong "g").
      const pitchEntry =
        keyMeta.mode === 'minor' && stepDir === 1 && cur === tonicIdx - 1
          ? raiseBySemitoneLetterAware(scale[cur])
          : scale[cur];
      pitches[anchorPos + i] = toLilyPitch(pitchEntry);
    }
    // Guard: guarantee the exact landing regardless of any rounding edge case above.
    degrees[lastPos] = tonicIdx;
    pitches[lastPos] = toLilyPitch(scale[tonicIdx]);
  }

  return { pitches, degrees };
}

function intervalToDegrees(interval) {
  // interval expressed as "3rd", "4th" etc via numeric size (3,4,6,8...);
  // scale-degree distance = interval - 1 (e.g. a 3rd spans 2 scale degrees).
  return Math.max(1, interval - 1);
}

// 2026-09-10: "선율처럼 나오게 할 수 있는 방법" -- direct request to make
// generated excerpts read more like an actual composed classical melody
// rather than a pure per-note random walk, which is exactly what this
// engine was doing: every step/leap direction was a flat 50/50 coin flip
// with zero awareness of where the note sat within the phrase. Real tonal
// melodies (and AMEB sight-reading excerpts specifically) very commonly
// trace an ARCH shape -- rising toward a melodic high point somewhere in
// the phrase, then descending back down -- rather than wandering with no
// net direction. `upProb` is the probability THIS note moves up rather
// than down; it's computed once per note in generateMelody's main loop
// from that note's position relative to the phrase's (randomized, so not
// every excerpt peaks at exactly the same spot) high-point target, and
// threaded through here instead of a flat 0.5. Deliberately a BIAS, not a
// rule -- the max deviation (see ARC_STRENGTH below) still leaves plenty of
// room for the melody to dip before the peak or rise after it, which is
// what keeps this reading as "tends to arch" rather than a robotic ramp
// up-then-down.
function pickMove(params, maxLeapDegrees, bigLeapAllowed, prevWasLeap, upProb = 0.5) {
  const r = Math.random();
  if (r < params.repeatWeight) {
    return { delta: 0, isBigLeap: false, isLeap: false };
  }
  if (r < params.repeatWeight + params.stepWeight) {
    const dir = Math.random() < upProb ? 1 : -1;
    return { delta: dir, isBigLeap: false, isLeap: false };
  }
  // Leap: size between 2 and maxLeapDegrees scale-degrees.
  if (prevWasLeap) {
    // 2026-08-27: never stack two leaps back-to-back -- chaining leaps (even
    // ones each individually within maxLeapInterval) outlines a broken chord
    // and reads as noticeably harder than an isolated leap recovered by a
    // step, which is what beginner-grade material actually looks like.
    // Fall back to a step so every leap stays a single, isolated skip.
    const dir = Math.random() < upProb ? 1 : -1;
    return { delta: dir, isBigLeap: false, isLeap: false };
  }
  const dir = Math.random() < upProb ? 1 : -1;
  const size = 2 + Math.floor(Math.random() * Math.max(1, maxLeapDegrees - 1));
  const isBig = size > 2; // bigger than a 3rd (2 scale-degree span)
  if (isBig && !bigLeapAllowed) {
    // Fall back to a step instead of exceeding the beginner leap cap.
    return { delta: dir, isBigLeap: false, isLeap: false };
  }
  return { delta: dir * size, isBigLeap: isBig, isLeap: true };
}

// 2026-09-10: max probability swing away from 0.5 the arch shape is allowed
// to apply (e.g. 0.18 means direction bias ranges from 32%-up/68%-down at
// the phrase's lowest-bias point to 68%-up/32%-down at its most biased) --
// see the pickMove comment above and generateMelody's per-note upProb calc.
// Kept modest deliberately: this is a tendency the ear picks up over a
// whole phrase, not a per-note guarantee -- a stronger value started
// reading as a mechanical ramp instead of a natural-sounding arch.
const ARC_STRENGTH = 0.18;

module.exports = { generateMelody };
