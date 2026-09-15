// ---------------------------------------------------------------------------
// Diatonic scale construction for LilyPond pitch spelling.
//
// Builds a multi-octave array of correctly-spelled scale degrees (as
// LilyPond pitch names, e.g. "bes" for B-flat) for a given key, so the
// melody/bass generators can walk by *scale degree* (diatonically correct)
// rather than by raw semitone, which keeps everything in-key automatically.
// ---------------------------------------------------------------------------

const { KEYS } = require('./gradeParams');

// 2026-09-14: "이론상 6~7샵/플랫까지 진짜로 다 커버" -- widening key coverage past
// B major/Db major (5 sharps/5 flats) exposed a real ceiling in the OLD
// design here: it picked each scale degree's spelling out of a fixed
// 12-entry pitch-class -> name table (SHARP_NAMES/FLAT_NAMES), one name per
// chromatic pitch. That only works by coincidence for keys up to 5
// sharps/flats, where every accidental the key needs happens to already be
// one of the table's 5 sharped/flatted letters. Past that (F# major's E#,
// Cb major's Fb, ...) the needed spelling simply isn't one of the table's 12
// names -- the pitch is right (enharmonically) but the LETTER is wrong,
// which is a real notation bug: LilyPond positions a note on the staff by
// its LETTER, so "E#" spelled as "f" lands on the wrong line/space and the
// scale silently skips a step visually.
//
// Replaced with the actual rule a key signature encodes: a diatonic scale
// visits each of the 7 staff letters exactly once, in order, starting from
// the tonic's own letter. So degree i's letter is just the tonic letter
// cycled forward by i (mod 7) -- ALWAYS correct, independent of accidental
// count -- and the only thing left to compute is which accidental (if any)
// that letter needs to reach the degree's real pitch class. That computation
// (`buildScale` below) has no table to run out of entries in; it now covers
// any number of sharps/flats a real key can have (0-7 each) for free.
const LETTER_ORDER = ['c', 'd', 'e', 'f', 'g', 'a', 'b'];
const NATURAL_PC = { c: 0, d: 2, e: 4, f: 5, g: 7, a: 9, b: 11 };

// Chromatic pitch class (0-11) of ANY LilyPond letter+accidental spelling,
// computed generically from the letter's natural pitch class plus however
// many 'is'/'es' suffixes it carries -- e.g. "fisis" -> f(5) + 2 -> 7,
// "eses" -> e(4) - 2 -> 2. Replaces the old fixed PITCH_CLASS_INDEX table
// (and its near-duplicates in melody.js/bass.js/index.js -- see each of
// their own 2026-09-14 comments), which could only answer for the ~12-18
// spellings someone had remembered to add by hand. This answers for ANY
// spelling, including ones no key currently in KEYS produces yet, so a
// future key addition can never silently return `undefined` here again.
function pitchClassOf(ly) {
  const letter = ly[0];
  const natural = NATURAL_PC[letter];
  if (natural == null) return null;
  const suffix = ly.slice(1);
  if (!suffix) return natural;
  const sign = suffix[0] === 'i' ? 1 : -1;
  const level = sign * (suffix.length / 2);
  return (((natural + level) % 12) + 12) % 12;
}

const MAJOR_STEPS = [2, 2, 1, 2, 2, 2, 1]; // whole/half pattern from tonic
const NATURAL_MINOR_STEPS = [2, 1, 2, 2, 1, 2, 2];

// 2026-09-11: "더블샵도 보이고" -- Grade 5 book review (SR G5.pdf) flagged
// double-sharp accidentals showing up in the real minor-key examples, and
// separately bass.js's V-chord fix (2026-08-31, raiseBySemitone on the
// third only) already noted that a minor key's UNALTERED natural-minor 7th
// degree gives a weak, non-pulling dominant. The FIRST fix here made the
// whole scale build as harmonic minor (7th degree raised at every octave,
// unconditionally) -- correct in isolated V-chord/cadence contexts, but a
// follow-up report ("이런 박자는 너무많이 넣지말고", with a screenshot of a
// mid-phrase leap to a sharp note) showed the downside: with EVERY occurrence
// of the 7th degree raised, a melody that simply walks stepwise past it
// mid-phrase (not approaching a cadence at all) gets the augmented-2nd
// "leap-like step" (3 semitones between scale degrees 6 and 7) far more
// often than real minor-key writing ever does -- real practice raises the
// leading tone only in the specific contexts that actually need its pull
// (approaching the tonic, or a V chord), and leaves it natural everywhere
// else (descending passages, general stepwise motion).
//
// SUPERSEDED that approach: buildScale below is back to plain, unraised
// NATURAL minor throughout (like before this whole feature). The raise is
// now applied CONTEXTUALLY instead, by the two call sites that actually
// need it -- melody.js's cadential-approach raise and bass.js's V-chord
// third raise (both pre-existing mechanisms, just newly fixed to use the
// letter-aware raise below instead of their own broken pc-lookup one, which
// is what caused the ORIGINAL "더블샵" gap in the first place: G# minor's
// leading tone re-derived from a bare pitch class lands on plain "g",
// losing the "F double-sharp" spelling entirely).

// Parse any LilyPond pitch-name string into { l: letter, n: accidental
// level } -- e.g. "fisis" -> {l:'f', n:2}, "bes" -> {l:'b', n:-1}, "c" ->
// {l:'c', n:0}. Fully generic (any repeat count of 'is'/'es'), unlike the
// old SHARP_LETTER_LEVEL/FLAT_LETTER_LEVEL fixed lookup tables this replaces
// -- those only had entries for single-accidental spellings of a ~12-key
// whitelist, so they had no answer for e.g. "eis" or "fes" once keys past
// 5 sharps/flats made those real scale degrees.
function parseLetterLevel(ly) {
  const l = ly[0];
  const suffix = ly.slice(1);
  if (!suffix) return { l, n: 0 };
  const sign = suffix[0] === 'i' ? 1 : -1;
  return { l, n: sign * (suffix.length / 2) };
}

// Re-spell a {letter, level} entry one semitone higher: level 0 -> 'is'
// (sharp), level 1 -> 'isis' (double sharp), level -1 -> plain letter
// (natural, cancelling a flat), etc.
function raiseLevelByOne(entry) {
  const n = entry.n + 1;
  if (n === 0) return entry.l;
  return n > 0 ? entry.l + 'is'.repeat(n) : entry.l + 'es'.repeat(-n);
}

// Raise a scale-array entry ({ ly, octaveOffset }) by one semitone, letter-
// aware so the result is spelled correctly (including double sharps/flats)
// instead of re-derived from a bare pitch class -- see the module comment
// above. 2026-09-14: no longer takes a `flats` argument -- parseLetterLevel
// reads the letter+level directly off the entry's own spelling, so there's
// no separate table to pick between and every call site simplifies to just
// passing the entry. Exported for melody.js's cadential leading-tone raise
// and bass.js's V-chord third raise -- both apply this CONTEXTUALLY (only
// where a real leading-tone pull belongs), not to every occurrence of the
// degree.
function raiseBySemitoneLetterAware(entry) {
  const parsed = parseLetterLevel(entry.ly);
  const raisedLy = raiseLevelByOne(parsed);
  const octaveBump = pitchClassOf(entry.ly) === 11 ? 1 : 0;
  return { ly: raisedLy, octaveOffset: entry.octaveOffset + octaveBump };
}

/**
 * Build a scale-degree lookup table spanning several octaves.
 * Returns an array of { ly, octaveMarks } where index 0 corresponds to a
 * low anchor octave; the caller picks a starting index near the middle.
 * LilyPond octave marks: c' = middle C (octave 3 in LilyPond's absolute
 * notation where unmarked c is the octave below middle C).
 */
function buildScale(keyId, octaveSpan = 3) {
  const key = KEYS[keyId];
  if (!key) throw new Error(`Unknown key: ${keyId}`);
  const steps = key.mode === 'major' ? MAJOR_STEPS : NATURAL_MINOR_STEPS;
  const tonicIndex = pitchClassOf(key.ly);
  const tonicLetterIdx = LETTER_ORDER.indexOf(key.ly[0]);

  // Build one octave's worth of degree pitch-class indices (0-6 -> chromatic index).
  const degreeClasses = [tonicIndex];
  let cur = tonicIndex;
  for (let i = 0; i < 6; i++) {
    cur = (cur + steps[i]) % 12;
    degreeClasses.push(cur);
  }

  // 2026-08-27 fix: LilyPond's unmarked note names are all pinned to ONE
  // fixed reference octave (c,d,e,f,g,a,b = C3..B3) -- there is no automatic
  // per-letter octave bump. That reference octave starts at C, so it only
  // lines up with a scale block's degree-index boundaries when the KEY's
  // tonic is also C. For any other tonic (e.g. A minor: degree order
  // a,b,c,d,e,f,g), the degrees after the letter wraps back past B into C
  // are actually a full octave HIGHER in real pitch than the unmarked
  // reference, even though they're still within the same "octaveOffset"
  // scale-degree block -- e.g. real A3,B3,C4,D4,E4,F4,G4. Naively giving
  // every degree in a block the same mark count (as this used to do)
  // silently dropped that octave for c/d/e/f/g, producing a spurious ~1
  // octave leap right at the b->c seam (and, symmetrically, an artificial
  // "big leap" whenever a melody/tonic-ending calculation crossed that
  // seam) -- this was the root cause of the register-crossing/big-leap
  // symptoms reported for non-C-tonic keys (A minor, D major, etc).
  //
  // Fix: track cumulative semitones from the tonic (via the same
  // whole/half-step pattern used for spelling) and derive each degree's
  // EXTRA octave mark as how many real 12-semitone boundaries it has
  // crossed relative to the unmarked reference -- so the mark only bumps
  // exactly where the real pitch actually crosses an octave, regardless of
  // which letter that happens to land on.
  const cumulativeSemitones = [0];
  let semitoneAcc = 0;
  for (let i = 0; i < 6; i++) {
    semitoneAcc += steps[i];
    cumulativeSemitones.push(semitoneAcc);
  }

  // 2026-09-14: degree spelling rewritten -- see the module-level comment
  // above for why. Each degree i's LETTER is always the tonic's letter
  // cycled forward i places (guarantees the scale walks the 7 staff
  // letters in order, which is the actual thing a key signature promises);
  // the accidental is whatever's needed to reach that degree's real pitch
  // class from the letter's own natural one, normalized to the smallest
  // same-pitch representative (e.g. +11 semitones off becomes -1, i.e. one
  // flat, not eleven sharps). For every real major/natural-minor scale this
  // always resolves to -1, 0, or +1 -- a key signature never needs a
  // double accidental on its own degrees -- so no clamping beyond the
  // normalization below is needed.
  const degreeLyNames = degreeClasses.map((pc, i) => {
    const letter = LETTER_ORDER[(tonicLetterIdx + i) % 7];
    const raw = pc - NATURAL_PC[letter];
    const diff = (((raw % 12) + 18) % 12) - 6; // normalize to (-6, 6]
    if (diff === 0) return letter;
    return diff > 0 ? letter + 'is'.repeat(diff) : letter + 'es'.repeat(-diff);
  });

  const extraOctave = cumulativeSemitones.map((c) => Math.floor((tonicIndex + c) / 12));

  // Now lay out `octaveSpan` octaves starting a couple below middle, so we
  // have room to walk up/down without hitting the array edge.
  const scale = [];
  // Octave 0 = the unmarked-c octave (C3). Spanning 0..octaveSpan-1 puts the
  // "middle C" block (oct 1) roughly in the middle of a 4-octave build,
  // which melody.js/bass.js use as their position-centering anchor.
  //
  // 2026-08-27: starts at -1, not 0. For a key whose tonic sits high in the
  // fixed reference octave (e.g. A minor: degree0 'a' is already semitone 9
  // of 12), the "octave 0" block's own comfortable low notes (a, b) are
  // followed almost immediately by degrees that cross into octave 1 (c, d,
  // e, f, g -- see the extraOctave fix above) -- so a bass-register window
  // anchored on octave 0 alone doesn't have room to stay low without
  // spilling up past middle C. Building one extra octave below gives every
  // key's bass register somewhere genuinely low to anchor on. Callers that
  // index by absolute octave position (melody.js's block-anchor search,
  // bass.js's bassAnchor) account for this extra low octave.
  const startOctave = -1;
  for (let oct = startOctave; oct < startOctave + octaveSpan; oct++) {
    degreeLyNames.forEach((ly, i) => {
      scale.push({ ly, octaveOffset: oct + extraOctave[i] });
    });
  }
  return scale; // flat array; index = degree count from bottom of range
}

/**
 * Convert a scale-array entry to a LilyPond absolute pitch, e.g. "c'".
 * LilyPond convention: unmarked "c" = C3 (the octave below middle C).
 * octaveOffset 0 => unmarked, positive => that many apostrophes (up an
 * octave each), negative => that many commas (down an octave each). There
 * must be NO discontinuity at 0 -- a jump straight from one comma to one
 * apostrophe would silently skip two octaves.
 */
function toLilyPitch(entry) {
  const rel = entry.octaveOffset;
  let marks = '';
  if (rel > 0) marks = "'".repeat(rel);
  else if (rel < 0) marks = ','.repeat(-rel);
  return `${entry.ly}${marks}`;
}

// pitchClassOf exported so melody.js/bass.js/index.js can share ONE pitch-
// class implementation instead of each keeping its own hand-maintained
// lookup table (see their matching 2026-09-14 comments) -- those tables ran
// out of entries the moment a key needed a spelling nobody had thought to
// add yet, which is exactly the class of bug widening key coverage kept
// tripping over. useFlats/SHARP_NAMES/FLAT_NAMES/PITCH_CLASS_INDEX and the
// old letter-level tables are gone -- nothing downstream needs a `flats`
// flag anymore, since raiseBySemitoneLetterAware now reads letter+level
// straight off the entry it's given.
module.exports = { buildScale, toLilyPitch, raiseBySemitoneLetterAware, pitchClassOf };
