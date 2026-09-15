// ---------------------------------------------------------------------------
// Left-hand (bass) generation for "hands together" excerpts.
//
// Deliberately simple, per spec: "generate a left-hand part using simple
// intervals/block patterns (avoid independent complex rhythms at early
// grades)". A tonic/subdominant/dominant triad is chosen per bar from the
// melody's first scale degree in that bar, then rendered in one of a few
// textures that get richer as grade increases (leftHandStyle).
//
// 2026-09-03: three more textures added (walkingBass, blockChordsEveryBeat,
// canonImitation), calibrated against the newer 15-example AMEB Grade 3
// sight-reading book scan (see gradeParams.js's grade3 comment) -- ex.14's
// stepwise moving bass, ex.15's struck-every-beat solid chords, and ex.10/12's
// true rhythmic-echo imitation between the hands. blockChordsEveryBeat is the
// one exception to "deliberately monophonic" above: its events carry a
// `pitches` array (multiple simultaneous notes) instead of a single `pitch`,
// rendered as a LilyPond chord `<...>` by index.js's assembleLilyPond.
// ---------------------------------------------------------------------------

const { buildScale, toLilyPitch, raiseBySemitoneLetterAware, pitchClassOf } = require('./scales');
const { NOTE_VALUES, KEYS } = require('./gradeParams');

const QUARTER_UNITS = NOTE_VALUES.quarter.units;
// 2026-09-09: grade3's "rest 도 minim rest, crotchet rest... 섞어서" needs the
// simple-meter bassSmallRestChance branch below to also recognize a
// half/minim-duration event (not just quarter/crotchet), so the LH's small
// rest can be a minim rest too, matching whichever event it happened to pick.
const HALF_UNITS = NOTE_VALUES.half.units;
const EIGHTH_UNITS = NOTE_VALUES.eighth.units;

// 2026-09-09: a triplet ('tripletEighth' x3 -- see gradeParams.js/index.js's
// triplet post-process) collectively occupies exactly one quarter-beat's
// worth of TIME despite each individual entry's placeholder `units: 1`
// (that placeholder only classifies it as "short" for staccato/slur
// purposes upstream in index.js). Summing raw NOTE_VALUES units naively
// undercounts any bar containing one by 1 unit (3 vs. the true 4), which
// broke every LH style below that sizes itself off the RH bar's total
// length -- caught as a LilyPond barcheck failure (LH bar 1 unit short)
// right after triplets were added. Walks a rhythm-key array and returns the
// real total, folding each run of 3 consecutive tripletEighth entries back
// into QUARTER_UNITS.
function effectiveBarUnits(bar) {
  let total = 0;
  let i = 0;
  while (i < bar.length) {
    if (bar[i] === 'tripletEighth' && bar[i + 1] === 'tripletEighth' && bar[i + 2] === 'tripletEighth') {
      total += QUARTER_UNITS;
      i += 3;
    } else {
      total += NOTE_VALUES[bar[i]].units;
      i += 1;
    }
  }
  return total;
}

// 2026-09-11: the local raiseBySemitone() that used to live here (a
// PITCH_CLASS_INDEX/SHARP_NAMES pc-lookup mirroring melody.js's old one) is
// gone -- it patched the V chord's third up to a proper major third
// ON TOP OF a scale built from plain natural minor. Now that scales.js
// builds every minor key as harmonic minor (the 7th/leading-tone degree is
// raised at the SOURCE, correctly re-spelled letter-by-letter -- see its
// 2026-09-11 comment), the V chord's third already lands on that raised
// degree directly (V's third is exactly the scale's 7th-degree slot -- see
// the chooseChordRoot call site below), so re-raising it here would raise
// the same note a second time. See the third assignment below.

// 2026-08-31: choose a harmony root degree (0=I, 3=IV, 4=V) by fitting the
// WHOLE bar's melody, not just its opening note. Scoring on the first note
// alone (the old behavior) could pick a harmony that clashed with the rest
// of the bar's line whenever the opening note happened to be a common tone
// shared by more than one triad, and had no memory of the previous bar's
// chord -- so the accompaniment could hop I-V-IV-I-V with no relationship
// to what the melody was actually doing, reading as "notes stacked under
// the melody" rather than a real bass line. Weighting every degree in the
// bar (opening note counted double, since it lands on the strong beat) and
// preferring the previous bar's root on a tie (real progressions don't
// change chord every single bar when the melody doesn't demand it) both
// push toward a harmony that actually tracks the tune and moves with some
// logic bar-to-bar. Reported as "grade 2로부터 make sense" scope --
// this bucket only ever runs for hands-together grades (4+), Grade 2/3's
// alternating device never reaches this function.
// 2026-09-10: "왼손도 [멜로디처럼] 적용... 기능화성 경향" -- direct follow-up to
// the RH phrase-arc work, applied to harmony instead of contour. Before this,
// chooseChordRoot picked purely by how well each candidate root's triad
// matched the bar's melody notes -- a real bass line, but with no sense that
// IV tends to move to V and V tends to resolve to I (the two strongest pulls
// in tonal harmony, "predominant -> dominant -> tonic"). A bar whose melody
// was genuinely ambiguous between two chords (a common case -- lots of scale
// degrees are shared between I/IV/V) previously broke that tie arbitrarily
// (favoring only a flat repeat of the previous chord); now it breaks toward
// the functionally expected next chord instead, which is what makes a real
// progression sound like it's "going somewhere" rather than just sitting on
// whatever chord best fits each bar in isolation. FUNCTIONAL_BONUS is added
// to the melody-fit score, not a replacement for it -- a bar whose melody
// clearly implies a different chord still wins on fit; the bonus only tips
// genuinely close calls, so this stays "the same I/IV/V vocabulary already
// calibrated per grade, just a smarter order to choose it in."
const FUNCTIONAL_BONUS = 0.75;

// 2026-09-10: "반종지 넣고 하는거" -- the half-cadence option from the earlier
// LH-musicality menu, now added. Real classical-era phrases very commonly
// split into two halves -- an antecedent ending on a HALF cadence (landing
// on V, "comma" -- the phrase pauses but clearly isn't over) and a
// consequent ending on a full authentic cadence (V->I, "period" -- see
// FUNCTIONAL_BONUS above, which already gives that resolution its pull).
// This engine already forces the very LAST bar to I; it never had anything
// marking the phrase's MIDPOINT as a place harmony gravitates toward V.
// `midCadenceBonus` is passed into chooseChordRoot only for the one bar
// index generateBass computes as the phrase midpoint (see its own comment)
// -- everywhere else it's 0, a no-op.
const MID_CADENCE_BONUS = 0.85;

// 2026-09-14: "화성학 공부시켜서 적용할 수 없나" -- direct ask to actually apply real
// harmony theory here rather than leave the accompaniment limited to I/IV/V.
// Real tonal harmony's other two commonly-used diatonic triads are ii
// (supertonic) and vi (submediant) -- ubiquitous in real practice (the
// "circle progression" vi-ii-V-I, and vi/ii as richer substitutes for I/IV
// in a predominant role) and, unlike a secondary dominant or borrowed chord,
// still built entirely from the SAME diatonic scale this engine already
// walks -- no new accidentals, no new reading burden for the student, only
// a more varied and idiomatic-sounding progression under the same notes.
// Root degree 5 (vi in a major key, VI in natural minor) is added
// unconditionally: built the same generic diatonic-thirds way as I/IV/V
// (see chordTones below), it comes out as a correctly consonant triad in
// EITHER mode without needing any alteration -- minor in a major key (the
// standard vi), and, perhaps less obviously, MAJOR in natural minor (a
// natural-minor scale's 6th-degree triad lands a major third + perfect
// fifth above its root purely from the scale's own whole/half-step pattern
// -- e.g. A minor's VI is F major -- real music theory, not a guess).
// Root degree 1 (ii) is added ONLY for major keys -- built the same way from
// a NATURAL minor scale, degree1's triad comes out diminished (ii°), which
// this engine has no diminished-triad handling for (no established
// dissonance-resolution convention here, unlike the V-chord's leading-tone
// fix) and would just read as an odd clashing chord, so it's deliberately
// left out for minor keys rather than guessed at.
const SECONDARY_BONUS = 0.6; // slightly gentler than FUNCTIONAL_BONUS -- vi/ii are a genuine functional pull but shouldn't out-compete the strong V->I/IV->V resolutions on a close call.

// 2026-09-14: "같은바면 여러번 안그리는걸로 이론에 맞게" -- investigated as a
// literal same-bar accidental-suppression bug first (repeated notes, tuplets,
// slurred groups, block chords struck every beat -- rendered and inspected
// each one directly). LilyPond's own default engraving already suppresses
// every one of those correctly; the actual generator has no such bug.
// The real source of what read as "the same accidental drawn over and over":
// whenever a bar's harmony lands on V in a minor key (which needs the raised
// leading tone -- a double sharp in sharp-heavy keys like G#/D# minor),
// `preferPrevOnTie` above has no cost for staying there bar after bar, and
// once a melody genuinely fits V for 2+ bars running (common -- V's tones
// overlap heavily with I's), the chosen root simply doesn't move. Each of
// those bars is individually correct (a NEW bar always needs its own
// accidental, LilyPond isn't wrong to print it), but several in a row reads
// visually as "the same double-sharp, again and again." STALENESS_PENALTY
// makes a candidate that's ALREADY held the previous 2+ bars mildly less
// attractive than moving on, so the harmony still parks on a chord when the
// melody genuinely calls for it (a real close-fit score beats this penalty),
// but doesn't linger there purely by tie-break default.
const STALENESS_PENALTY = 0.55;

function chooseChordRoot(degreesInBar, prevRoot, midCadenceBonus = 0, mode = 'major', rootStreak = 0) {
  // Generic diatonic triad built by stacking every-other scale degree
  // starting at `root` (e.g. root=4 -> [4,6,1], root=5 -> [5,0,2]) -- the
  // same construction I/IV/V already used, just no longer hardcoded to only
  // those three roots.
  const chordTones = (root) => [root, (root + 2) % 7, (root + 4) % 7];
  const candidates = mode === 'major' ? [0, 1, 3, 4, 5] : [0, 3, 4, 5];
  let best = 0;
  let bestScore = -1;
  for (const root of candidates) {
    let score = 0;
    const tones = chordTones(root);
    degreesInBar.forEach((deg, i) => {
      const degreeInOctave = ((deg % 7) + 7) % 7;
      const weight = i === 0 ? 2 : 1;
      if (tones.includes(degreeInOctave)) score += weight;
    });
    // Predominant -> dominant (IV -> V, and ii -> V, the same functional
    // role) and dominant -> tonic (V -> I) are the progressions that
    // actually define tonal "pull" -- nudging toward them (not toward I ->
    // IV or I -> V, which have no comparable strong pull either way) is
    // what reads as functional rather than arbitrary. See FUNCTIONAL_BONUS
    // comment above for why this only tips close calls instead of
    // overriding the melody-fit score. vi -> IV and vi -> ii (both real,
    // common "circle progression" links -- vi substitutes for I as a
    // springboard into the same predominants) get the gentler
    // SECONDARY_BONUS, same reasoning.
    if (prevRoot === 3 && root === 4) score += FUNCTIONAL_BONUS;
    if (prevRoot === 1 && root === 4) score += FUNCTIONAL_BONUS;
    if (prevRoot === 4 && root === 0) score += FUNCTIONAL_BONUS;
    if (prevRoot === 5 && root === 3) score += SECONDARY_BONUS;
    if (prevRoot === 5 && root === 1) score += SECONDARY_BONUS;
    // Half-cadence nudge -- see MID_CADENCE_BONUS comment above. Only
    // nonzero for the one bar generateBass marks as the phrase midpoint.
    if (root === 4) score += midCadenceBonus;
    // Only bites once the chord has ALREADY held for 2+ bars running --
    // a fresh repeat (streak 0 or 1) is untouched, so a normal 2-bar sit
    // (e.g. a half-cadence approach) is unaffected.
    if (root === prevRoot && rootStreak >= 2) score -= STALENESS_PENALTY;
    const preferPrevOnTie = score === bestScore && root === prevRoot && best !== prevRoot;
    if (score > bestScore || preferPrevOnTie) {
      bestScore = score;
      best = root;
    }
  }
  return best;
}

// Compound meters (3 eighths per beat-group) want a dotted-quarter pulse for
// the LH, not a quarter-note one, or the accompaniment reads like it's in a
// simple meter. Only the meters actually supported this way; extend if more
// compound time sigs are added.
const COMPOUND_TIME_SIGS = new Set(['6/8', '9/8']);

// 2026-09-14: `chordRootsOut`, when passed, gets each bar's chosen root
// degree offset (0=I, 3=IV, 4=V) pushed onto it in bar order -- lets
// index.js see which bars landed on V without duplicating chooseChordRoot's
// own logic, so it can keep the RH's leading tone consistent with the LH's
// (see index.js's own comment on this, next to where it reads this array).
function generateBass(barsRhythm, melodyDegreesPerBar, params, keyId, timeSig, chordRootsOut) {
  // Bass gets its own scale build (independent of melody.js's array) so its
  // register anchor can't drift into treble range: anchor the chord root
  // squarely in the octave-0 block ("unmarked c" register, ~C3), which
  // sits comfortably in the bass clef regardless of grade.
  const scale = buildScale(keyId, 6);
  const keyMeta = KEYS[keyId];
  const scaleLen7 = 7;
  const isCompound = COMPOUND_TIME_SIGS.has(timeSig);

  // 'mixed' (Grade 3+) means the real books don't commit to one LH texture
  // per grade -- block chords, sustained pedal tones, and broken patterns
  // all appear across different examples. Pick one concrete texture ONCE
  // per excerpt (not per bar) so a single piece stays internally consistent.
  // params.mixedStylePool lets a bucket widen/narrow which concrete
  // textures 'mixed' draws from (e.g. Grade 5 adds the richer
  // 'triadPattern' arpeggiation, seen in its compound-meter examples).
  let style = params.leftHandStyle || 'halfBarRootFifth';
  if (style === 'mixed') {
    let pool = params.mixedStylePool || ['wholeBarRoot', 'halfBarRootFifth', 'brokenRootFifth'];
    // 2026-09-09: "이런건 안나오면 좋겠다" -- reported with a screenshot of a
    // 4/4 G major excerpt whose LH repeated "g4~g16 d'4~d'16 d'4." IDENTICALLY
    // every single bar. Root cause: waltzOomPah's "oom-pah-pah" split (root
    // on beat 1, the chord's 5th on beats 2 and 3 -- see its own comment
    // below) does `Math.floor(barUnitsTotal / 3)`, which only divides evenly
    // when there really are 3 quarter-note beats in the bar (3/4, 12 units).
    // grade4's mixedStylePool includes waltzOomPah so it can surface outside
    // the dedicated "Waltz time" tempoFormRules path too (ex.1's "Moderato"-
    // titled waltz -- see this bucket's own 2026-09-09 comment on
    // mixedStylePool) -- but the pool is drawn regardless of the excerpt's
    // ACTUAL timeSig, so it could just as easily land on a 4/4 (16 units) or
    // 2/2 (also 16) excerpt: floor(16/3)=5, remainder=16-10=6, and
    // unitsToLilyDuration(5) doesn't map to one token -- it falls back to a
    // split-and-tie (4+1 -> "4~16"), producing exactly the ugly repeating
    // tied-quarter-into-sixteenth artifact reported. Filtering waltzOomPah
    // out of the pool whenever this excerpt's timeSig isn't actually 3/4
    // keeps the texture confined to bars where its 3-beat math is valid.
    if (timeSig !== '3/4') pool = pool.filter((s) => s !== 'waltzOomPah');
    if (pool.length === 0) pool = ['halfBarRootFifth'];
    style = pool[Math.floor(Math.random() * pool.length)];
  }
  // 2026-09-14: "왼손의 다양성이 아직 부족해... 왼손 음역대가 좀 넓어지지 않나" -- direct
  // feedback that every generated excerpt's LH sits in the exact same fixed
  // register (bassAnchor was a hardcoded constant, unrelated to grade), so a
  // whole batch of excerpts at any one grade all looked/sounded alike, AND
  // the LH register never widened as the RH's already does (see
  // gradeParams.js's position.spanScaleDegrees, which climbs 5->12 across
  // grades -- bassAnchor had no equivalent). Real piano writing at these
  // grades does vary which octave the LH sits in piece to piece (a piece in
  // a lower, richer register vs. one in a lighter, higher one), so this adds
  // exactly that: once per excerpt (not per bar, so a single piece stays
  // internally consistent), a grade-configurable chance
  // (params.bassLowVarietyChance) to drop the whole LH's register down one
  // full octave block. Deliberately DOWN only, never up -- widening upward is
  // exactly what caused the over-ledger-lined chord just fixed below (the
  // `third` chord-tone clamp bug), so more upward headroom is the wrong
  // direction; buildScale's array has genuine spare room below the default
  // anchor (see its startOctave comment) for this to draw on safely.
  // Excluded for 'canonImitation', which already computes its own register
  // (one octave below the chord-root block, echoing the RH's own pitches --
  // see its case below) independent of bassAnchor's block-tone math; shifting
  // bassAnchor under it too would double-lower it well past any safe range.
  const bassLowVariety =
    style !== 'canonImitation' && params.bassLowVarietyChance
      ? Math.random() < params.bassLowVarietyChance
      : false;
  // 2026-08-27: scales.js's buildScale now starts one octave lower than it
  // used to (see its startOctave comment) so every key has genuine
  // low-register headroom -- what used to be "the octave-0 block" at index
  // 0 is now at index 7. bassLowVariety (just above) can drop this a further
  // full block, to index 0.
  const bassAnchor = bassLowVariety ? 0 : 7;
  const bassBars = [];
  // Tracks the previous bar's chosen root so chooseChordRoot can prefer
  // staying put on a tie instead of restarting the search cold every bar
  // (see its 2026-08-31 doc comment).
  let prevRoot = null;
  // Companion to STALENESS_PENALTY above -- how many bars IN A ROW (ending
  // at the bar just processed) have shared the same root, so
  // chooseChordRoot knows when a repeat has already run long enough to
  // start discouraging another one.
  let rootStreak = 0;
  // 2026-09-11: "왼손 반주가 너무 지그재그" -- the arpeggio cursor for
  // 'triadPattern'/'fullTexture' below used to be a LOCAL `let i = 0`
  // re-declared fresh at the top of every bar, so it always started the
  // [root, fifth, third, fifth] cycle back at index 0 each time. That's
  // invisible in 4/4 (4 pulses/bar happens to walk the whole 4-entry cycle
  // every bar, so it looks fine by coincidence) but in any meter with only
  // 2 pulses/bar -- every compound meter (6/8, 9/8), which is exactly where
  // Grade 5's newer styles (Gigue, and the general compound-meter pool)
  // draw from this same default case -- it NEVER got past index 1, so the
  // LH played root-fifth-root-fifth identically every single bar for the
  // whole excerpt: a static back-and-forth "zigzag" instead of an actual
  // rotating arpeggio. Tracked here instead, OUTSIDE the bar loop, so the
  // cursor keeps advancing across bars -- bar 2 might pick up at "third",
  // bar 3 at "fifth" again, etc. Each bar still builds its arpeggio from
  // ITS OWN freshly-chosen root/third/fifth (harmony correctness is
  // untouched); only which chord tone the bar STARTS on now varies.
  let arpeggioCursor = 0;

  // 2026-09-10: see chooseChordRoot's MID_CADENCE_BONUS comment -- the bar
  // ending the excerpt's first "half" is where a half cadence (landing on V)
  // belongs. Only meaningful for excerpts with a real two-phrase shape (at
  // least 6 bars -- anything shorter has a midpoint too close to either end
  // to read as a real phrase break, so this is skipped there entirely).
  // Never the excerpt's own final bar (already hard-forced to I above) and
  // never bar 0 (a "half cadence" one bar in isn't a phrase boundary).
  const midCadenceBarIdx =
    barsRhythm.length >= 6 ? Math.max(1, Math.floor(barsRhythm.length / 2) - 1) : -1;

  barsRhythm.forEach((bar, barIdx) => {
    const degreesInBar = melodyDegreesPerBar[barIdx] || [];
    const isFinalBar = barIdx === barsRhythm.length - 1;
    // 2026-09-04: the LAST bar's harmony is always forced to the tonic (I),
    // never left to chooseChordRoot's melody-fit scoring -- every real
    // scanned example cadences on I at the end, but scoring purely against
    // the final bar's melody notes could land on IV or V instead (e.g. a
    // melody that ends on the 5th scale degree scores just as well against
    // V as I), which reads as an unresolved, "wrong key" ending even though
    // the melody itself correctly ends on the tonic (see melody.js's
    // endOnTonic). Reported directly against a generated excerpt.
    const midCadenceBonus = !isFinalBar && barIdx === midCadenceBarIdx ? MID_CADENCE_BONUS : 0;
    const rootOffset = isFinalBar
      ? 0
      : chooseChordRoot(degreesInBar, prevRoot, midCadenceBonus, keyMeta.mode, rootStreak);
    rootStreak = rootOffset === prevRoot ? rootStreak + 1 : 0;
    prevRoot = rootOffset;
    if (chordRootsOut) chordRootsOut.push(rootOffset);
    const rootIdx = bassAnchor - (bassAnchor % scaleLen7) + rootOffset;
    // 2026-09-14: the degree-index-based `chordCeiling` clamp that used to
    // sit here (and on `third`/`fifth` below) is GONE -- see
    // foldChordToneSafe's own comment further down for why a plain index
    // cutoff can't be trusted (it silently assumed every key's degrees sit
    // in the same real octave within a block, which is false for keys like
    // B minor). Root/third/fifth now rely solely on foldChordToneSafe's
    // real-PITCH safety fold, which handles every root this function can
    // produce -- including 2026-09-14's new ii/vi roots (see
    // chooseChordRoot's own comment), which the old degree-based ceiling
    // actively broke: ii's fifth (rootIdx+4, one degree above where the old
    // ceiling capped out) got clamped DOWN a whole scale-degree, silently
    // turning a correct perfect fifth into a wrong perfect fourth in every
    // major key. foldChordToneSafe has no such blind spot since it checks
    // the tone's actual sounding pitch, not its position within one
    // arbitrarily-sized block.
    const root = scale[clampIdx(foldChordToneSafe(scale, rootIdx), scale.length)];
    let third = scale[clampIdx(foldChordToneSafe(scale, chordToneIndex(rootIdx, 2, scaleLen7)), scale.length)];
    const fifth = scale[clampIdx(foldChordToneSafe(scale, chordToneIndex(rootIdx, 4, scaleLen7)), scale.length)];
    // 2026-08-31 (re-fixed 2026-09-11): bass.js builds every triad straight
    // from the scale's own (natural minor) tones, so a minor-key V chord
    // came out as a MINOR triad (e.g. A minor's V, built on E, landed as
    // E-G-B instead of the real dominant E-G#-B) -- a minor v doesn't pull
    // the ear back to the tonic the way a real dominant does. Raise just the
    // third to make the V a proper major dominant triad; root and fifth
    // stay diatonic. Same idea as melody.js's cadential leading-tone raise,
    // kept independent since the two hands build their harmony separately.
    // 2026-09-11: this briefly moved to scales.js raising the leading tone
    // unconditionally (harmonic minor throughout) instead of only here --
    // reverted after a direct report that it made the augmented-2nd interval
    // show up far more often than real minor-key writing does (see scales.js's
    // 2026-09-11 comment) -- back to this narrow, V-chord-only context, now
    // calling scales.js's letter-aware raise so double sharps (e.g. G#
    // minor's V chord third, F double-sharp) still spell correctly.
    if (keyMeta.mode === 'minor' && rootOffset === 4) {
      third = raiseBySemitoneLetterAware(third);
    }

    const barUnitsTotal = effectiveBarUnits(bar);

    let events; // [{ ly, durationKey }]
    switch (style) {
      case 'wholeBarRoot':
        events = [{ pitch: root, durationUnits: barUnitsTotal }];
        break;
      case 'halfBarRootFifth': {
        // 2026-09-10: "grade 3에 점 4분음표는 안나오니 빼줘" -- flagged directly
        // against a rendered 3/4 sample. Root cause: this style always splits
        // the bar into two EQUAL halves, which works cleanly in 2/4 (half of
        // 8 units = a plain quarter) and 4/4 (half of 16 = a plain half note)
        // but not 3/4, where the bar totals 12 units and an even split lands
        // on 6+6 -- neither half is a plain note value, so both get rendered
        // as a dotted quarter (exactly the "점 4분음표" the user is pointing
        // at). Special-cased 3/4 to split 4+8 instead (a plain quarter for
        // the root, a dotted half for the fifth) -- still two LH notes per
        // bar like every other timeSig, just using durations that don't
        // require a dotted quarter. Dotted half is fine here since it's
        // already the one dotted duration this grade explicitly allows (see
        // gradeParams.js's noteValues/"dotted rhythm은 dotted minim만").
        const half = timeSig === '3/4' ? QUARTER_UNITS : Math.floor(barUnitsTotal / 2);
        events = [
          { pitch: root, durationUnits: half },
          { pitch: fifth, durationUnits: barUnitsTotal - half },
        ];
        break;
      }
      case 'brokenRootFifth': {
        // Fixed quarter-note pulse (4 sixteenth-units), not a fraction of
        // the bar -- dividing the bar itself into quarters produces
        // ever-smaller (and busier) note values as bars get shorter.
        const pulse = pulseUnitsFor(barUnitsTotal, isCompound);
        events = [];
        let remaining = barUnitsTotal;
        let toggle = 0;
        while (remaining > 0) {
          const d = Math.min(pulse, remaining);
          events.push({ pitch: toggle % 2 === 0 ? root : fifth, durationUnits: d });
          remaining -= d;
          toggle += 1;
        }
        break;
      }
      case 'waltzOomPah': {
        // 2026-09-02: the classic "oom-pah-pah" waltz LH -- low root on beat
        // 1 ("oom"), then the chord's 5th repeated on beats 2 and 3
        // ("pah-pah"). Only ever selected via a bucket's tempoFormRules
        // (see index.js) when the excerpt's tempo marking is "Waltz time",
        // which also forces 3/4 -- so barUnitsTotal is always 12 units here
        // (3 quarter-note beats), splitting evenly. Kept single-note (no
        // real stacked chord) like every other LH style in this file, since
        // this codebase's bass line is deliberately monophonic throughout.
        const beat = Math.floor(barUnitsTotal / 3);
        const remainder = barUnitsTotal - beat * 2;
        events = [
          { pitch: root, durationUnits: beat },
          { pitch: fifth, durationUnits: beat },
          { pitch: fifth, durationUnits: remainder },
        ];
        break;
      }
      case 'walkingBass': {
        // 2026-09-03: stepwise crotchet motion that walks diatonically from
        // THIS bar's chord root toward the NEXT bar's chord root (or holds
        // near this bar's own root if it's the excerpt's last bar) --
        // outlines the harmony the way a real walking bass does, distinct
        // from every other style here which either repeats a fixed set of
        // chord tones or arpeggiates in place. Diatonic scale steps only
        // (index-adjacent entries in `scale`), never chromatic passing
        // tones, matching this codebase's in-key-only convention.
        const pulse = pulseUnitsFor(barUnitsTotal, isCompound);
        const stepsCount = Math.max(1, Math.round(barUnitsTotal / pulse));
        const nextBarIdx = barIdx + 1 < barsRhythm.length ? barIdx + 1 : null;
        const nextDegreesInBar = nextBarIdx != null ? (melodyDegreesPerBar[nextBarIdx] || []) : [];
        const nextRootOffset = nextDegreesInBar.length ? chooseChordRoot(nextDegreesInBar, rootOffset, 0, keyMeta.mode) : rootOffset;
        const nextRootIdx = bassAnchor - (bassAnchor % scaleLen7) + nextRootOffset;
        // 2026-09-14: same real-pitch safety fold as root/third/fifth above
        // (see foldChordToneSafe's comment) -- walkingBass interpolates
        // between these two ROOT indices directly rather than going through
        // the already-folded `root` variable, so it needs its own fold on
        // both endpoints to stay clear of the same key-distortion issue.
        const safeRootIdx = foldChordToneSafe(scale, rootIdx);
        const safeNextRootIdx = foldChordToneSafe(scale, nextRootIdx);
        events = [];
        for (let s = 0; s < stepsCount; s++) {
          const t = stepsCount === 1 ? 0 : s / (stepsCount - 1);
          const idx = Math.round(safeRootIdx + (safeNextRootIdx - safeRootIdx) * t);
          events.push({ pitch: scale[clampIdx(idx, scale.length)], durationUnits: pulse });
        }
        break;
      }
      case 'blockChordsEveryBeat': {
        // 2026-09-03: full root-third-fifth triad struck TOGETHER on every
        // beat -- this codebase's one genuinely polyphonic LH texture (see
        // this file's header comment). `pitches` (an array) replaces the
        // usual single `pitch`; index.js's assembleLilyPond renders that as
        // a LilyPond chord `<...>`.
        const pulse = pulseUnitsFor(barUnitsTotal, isCompound);
        events = [];
        let remaining = barUnitsTotal;
        while (remaining > 0) {
          const d = Math.min(pulse, remaining);
          events.push({ pitches: [root, third, fifth], durationUnits: d });
          remaining -= d;
        }
        break;
      }
      case 'triadPatternCalm': {
        // 2026-09-04: a gentler, half-bar-pulse cousin of 'triadPattern'
        // below -- root then third, TWO notes per bar instead of four.
        // Grade3's own scan evidence for a flowing arpeggiated LH (ex.4,
        // ex.8) always pairs it with a comparatively calm/sparse RH, but
        // this engine picks the RH's rhythm independently of which LH style
        // gets drawn -- so plain 'triadPattern' (borrowed as-is from higher
        // grades) could land under an energetic, note-heavy RH and read as
        // the LH competing with or dominating the melody, reported directly
        // against a "Lively"-tempo generated excerpt. Halving the note rate
        // keeps the arpeggiated color (a real, different quality from flat
        // root-fifth) while being far less likely to ever outbusy the RH,
        // regardless of what the RH happened to roll.
        // 2026-09-10: same even-split bug as halfBarRootFifth above ("grade
        // 3에 점 4분음표는 안나오니 빼줘") -- 3/4's 12 units split evenly into
        // 6+6, both dotted quarters. Same fix: quarter + dotted half in 3/4.
        const half = timeSig === '3/4' ? QUARTER_UNITS : Math.floor(barUnitsTotal / 2);
        events = [
          { pitch: root, durationUnits: half },
          { pitch: third, durationUnits: barUnitsTotal - half },
        ];
        break;
      }
      case 'sarabandeStress': {
        // 2026-09-11: added for Grade 5's "Sarabande" style marking (SR
        // G5.pdf book review flagged this dance form by name -- see
        // gradeParams.js's grade5 tempoFormRules). A sarabande's defining
        // rhythmic trait, unlike every other triple-meter dance in this
        // engine, is that the METRIC WEIGHT falls on beat 2, not beat 1 --
        // traditionally notated as a long note (or tied/dotted value)
        // landing there. Modeled here as a light single root on beat 1
        // (the "up" gesture) followed by a full root-third-fifth chord
        // struck on beat 2 and held through beat 3 -- the chord's harmonic
        // "arrival" plus its extra duration is what reads as the stress
        // landing on beat 2 rather than beat 1. Only meaningful in 3/4 (see
        // tempoFormRules, which forces that meter for this marking) --
        // barUnitsTotal is always 12 units (3 quarter-note beats) here.
        const beat = Math.floor(barUnitsTotal / 3);
        events = [
          { pitch: root, durationUnits: beat },
          { pitches: [root, third, fifth], durationUnits: barUnitsTotal - beat },
        ];
        break;
      }
      case 'canonImitation': {
        // 2026-09-03: true canon -- the LH echoes the RH's PREVIOUS bar
        // (same rhythm, same scale degrees) transposed down an octave. The
        // one-bar delay is what makes this a canon rather than plain
        // parallel octaves; the very first bar has no previous RH material
        // to echo yet, so it holds a plain tonic pedal instead. Ignores the
        // root/third/fifth harmony computed above entirely -- the LH's
        // pitches here come straight from the melody, not from a chosen
        // chord.
        const prevBarRhythm = barIdx > 0 ? barsRhythm[barIdx - 1] : null;
        const prevDegrees = barIdx > 0 ? (melodyDegreesPerBar[barIdx - 1] || []) : [];
        // 2026-09-04: the final bar never echoes, even when previous material
        // exists. Straight canon imitation reproduces whatever scale degree
        // the RH happened to land on a bar ago, with no regard for harmony --
        // fine everywhere else (echoing IS the point of a canon), but on the
        // very last bar that could land on any degree, not the tonic, which
        // is exactly the "ending key doesn't match" report this style's own
        // final-bar exemption should have already prevented. Falls back to
        // the same plain tonic pedal used when there's no previous bar to
        // echo, so canonImitation cadences on I like every other LH style.
        if (!prevBarRhythm || !prevDegrees.length || isFinalBar) {
          events = [{ pitch: root, durationUnits: barUnitsTotal }];
        } else {
          events = [];
          // 2026-09-09: a triplet trio in the echoed RH bar needs the same
          // collapse-to-one-quarter treatment as effectiveBarUnits above --
          // echoing 3 separate 1-unit LH events would both mis-total the bar
          // AND try to render a canon voice that itself needs tuplet
          // notation, which this style was never meant to produce. Echo just
          // the triplet's first pitch/degree as a plain quarter instead.
          let i = 0;
          while (i < prevBarRhythm.length) {
            const noteKey = prevBarRhythm[i];
            const isTripletStart = noteKey === 'tripletEighth'
              && prevBarRhythm[i + 1] === 'tripletEighth' && prevBarRhythm[i + 2] === 'tripletEighth';
            const deg = prevDegrees[i] != null ? prevDegrees[i] : prevDegrees[prevDegrees.length - 1];
            const degMod = ((deg % scaleLen7) + scaleLen7) % scaleLen7;
            // One octave below the usual chord-root block (bassAnchor's own
            // block minus a full 7-degree octave) so the echo reads clearly
            // as a low accompaniment voice, not a doubling of the melody.
            const idx = bassAnchor - (bassAnchor % scaleLen7) + degMod - scaleLen7;
            const durationUnits = isTripletStart ? QUARTER_UNITS : NOTE_VALUES[noteKey].units;
            events.push({ pitch: scale[clampIdx(idx, scale.length)], durationUnits });
            i += isTripletStart ? 3 : 1;
          }
        }
        break;
      }
      case 'triadPattern':
      case 'fullTexture':
      default: {
        // Both the "richer" left-hand textures use the same gentle
        // root-fifth-third-fifth arpeggiation at a steady quarter-note
        // pulse -- kept deliberately unfussy so the left hand never reads
        // harder than the melody, per spec ("avoid independent complex
        // rhythms").
        const pulse = pulseUnitsFor(barUnitsTotal, isCompound);
        const seq = [root, fifth, third, fifth];
        events = [];
        let remaining = barUnitsTotal;
        while (remaining > 0) {
          const d = Math.min(pulse, remaining);
          events.push({ pitch: seq[arpeggioCursor % seq.length], durationUnits: d });
          remaining -= d;
          arpeggioCursor += 1;
        }
        break;
      }
    }
    // 2026-09-09: "왼손 8분의 6박자에는 Quaver rest도 살짝만 포함해주고, 다른
    // 나머지 박자표에는 Crotchet rest도 포함해줄래" -- a SMALL, single-beat rest
    // dropped into an otherwise-sounding bar (distinct from bassRestChance
    // just below, which silences the WHOLE bar).
    //
    // Simple meters: this only ever targets an event whose duration already
    // happens to be exactly one quarter/crotchet unit (brokenRootFifth's
    // alternating pulse, walkingBass's steps, blockChordsEveryBeat's struck
    // chords, the default arpeggiation's quarter pulse) -- never a style
    // like wholeBarRoot or halfBarRootFifth whose events are bigger than that
    // and would need splitting to fit a rest in. Skipped rather than forced,
    // keeping this additive and low-risk.
    //
    // Compound (6/8, 9/8): the LH's felt pulse there is the DOTTED quarter
    // (6 units -- see pulseUnitsFor), never a bare eighth on its own, so
    // there's no existing eighth-duration event to just swap for a rest the
    // way the simple-meter branch does. Instead, carve a quaver (eighth, 2
    // units) rest off the FRONT of one dotted-quarter pulse-note, leaving a
    // plain crotchet (4 units) to fill out the remainder of that pulse --
    // this is exactly what the user asked for ("Quaver rest도... 포함해") and
    // keeps the bar's total units untouched (2 + 4 = 6, same as before).
    //
    // Same isFinalBar/canonImitation exclusions as bassRestChance (never
    // rest out the cadence; canonImitation's echo needs next bar's material
    // intact).
    if (params.bassSmallRestChance && !isFinalBar && style !== 'canonImitation') {
      if (isCompound) {
        const candidates = [];
        events.forEach((ev, idx) => {
          if (!ev.rest && !ev.pitches && ev.durationUnits === 6) candidates.push(idx);
        });
        if (candidates.length && Math.random() < params.bassSmallRestChance) {
          const pickIdx = candidates[Math.floor(Math.random() * candidates.length)];
          const picked = events[pickIdx];
          events.splice(pickIdx, 1,
            { rest: true, durationUnits: EIGHTH_UNITS },
            { pitch: picked.pitch, durationUnits: QUARTER_UNITS });
        }
      } else {
        // 2026-09-09: extended from QUARTER_UNITS-only to also match
        // HALF_UNITS-duration events, so styles like wholeBarRoot/
        // halfBarRootFifth (whose events ARE minim-length) can now also
        // contribute a small rest -- picked event's OWN duration is reused
        // for the replacement rest (read before reassignment below) rather
        // than hardcoding QUARTER_UNITS, so a minim-length event becomes a
        // minim rest and a crotchet-length event becomes a crotchet rest.
        const candidates = [];
        events.forEach((ev, idx) => {
          if (!ev.rest && !ev.pitches && (ev.durationUnits === QUARTER_UNITS || ev.durationUnits === HALF_UNITS)) candidates.push(idx);
        });
        if (candidates.length && Math.random() < params.bassSmallRestChance) {
          const pickIdx = candidates[Math.floor(Math.random() * candidates.length)];
          events[pickIdx] = { rest: true, durationUnits: events[pickIdx].durationUnits };
        }
      }
    }
    // 2026-09-09: "왼손 비중 이정도로 너무 많지 않게" -- direct feedback with real
    // book photos showing the LH is often genuinely SILENT for a whole bar
    // (e.g. "Cheekily"'s and "Dolce"'s own bar 1), not just playing sparser
    // note VALUES. bass.js had no rest concept at all until now -- every bar
    // always sounded something, which reads as more LH presence overall than
    // the book actually has even once note density per sounding bar was
    // already tuned down. Opt-in per bucket (params.bassRestChance). Book
    // evidence (two of the photographed examples) shows the very FIRST bar
    // of a piece can be silent in the LH, so that's not excluded here --
    // only the last bar (keeps the final cadence's resolution audible) and
    // canonImitation (a silent bar there would also erase the RH material
    // the NEXT bar's echo needs to copy) are.
    if (params.bassRestChance && !isFinalBar && style !== 'canonImitation'
      && Math.random() < params.bassRestChance) {
      // 2026-09-09: "4분쉼표는 가운데 정렬해주고" -- a rest that spans the WHOLE
      // bar (this is the only kind bassRestChance ever produces today) needs
      // `fullBar: true` so index.js's bassEventTokens renders it as a real
      // LilyPond multi-measure rest (uppercase `R`), which LilyPond
      // automatically centers in the bar -- a plain lowercase `r` rest (what
      // it was rendering as before) is positioned like an ordinary note at
      // the start of the bar instead, which is what read as "off to one
      // side" rather than centered.
      events = [{ rest: true, fullBar: true, durationUnits: barUnitsTotal }];
    }
    bassBars.push(events);
  });

  return bassBars;
}

// A compound-meter bar (6/8, 9/8) wants a dotted-quarter pulse (6 units --
// one "group of 3 eighths") so the LH pattern matches the beat feel;
// simple meters use a quarter-note pulse (4 units). All supported time
// signatures divide evenly by whichever of these applies (4/4=16, 3/4=12,
// 2/4=8 by 4; 6/8=12, 9/8=18 by 6), so this never leaves an awkward
// remainder. Falls back to the whole bar as one pulse if neither divides
// evenly (shouldn't happen for any currently supported time signature).
function pulseUnitsFor(barUnitsTotal, isCompound) {
  if (isCompound && barUnitsTotal % 6 === 0) return 6;
  if (barUnitsTotal % 4 === 0) return 4;
  return barUnitsTotal;
}

// Pick a compact voicing for a chord tone `stepsUp` scale-degrees above the
// root: if going straight up would cross into the next 7-note (octave)
// block, fold it down an octave instead (same pitch class, played below the
// root). Without this, a root sitting in the upper half of its block (e.g.
// the IV or V chord's root) sends its 5th shooting into the next octave --
// which is fine harmonically, but on the page it reads as a bass note
// stranded 2+ ledger lines above the staff, in what looks like it should
// have been the right hand's register.
function chordToneIndex(rootIdx, stepsUp, scaleLen7) {
  const rootBlock = Math.floor(rootIdx / scaleLen7);
  const rootPos = rootIdx % scaleLen7;
  const pos = rootPos + stepsUp;
  if (pos >= scaleLen7) {
    return rootBlock * scaleLen7 + (pos - scaleLen7); // fold down an octave
  }
  return rootIdx + stepsUp;
}

function clampIdx(i, len) {
  return Math.max(0, Math.min(len - 1, i));
}

// 2026-09-14: "이렇게 덧줄이 많이 쓰이지는 않게" -- direct follow-up after the
// `third`-clamp fix above (see its comment) turned out NOT to fully explain
// the reported over-ledger-lined chord. Root cause, found by checking every
// grade4-8 key's actual chord-tone PITCHES (not just scale-degree indices):
// chordCeiling above is a plain scale-degree-index cutoff, which silently
// assumes every degree within one 7-degree block sits in the same real
// octave. That's true for C major (where this file's degree math was
// originally tuned) but NOT true in general -- scales.js's buildScale
// necessarily gives some keys' degrees an extra octave bump mid-block (see
// its own extraOctave comment: a tonic that starts high in the fixed
// per-letter reference octave, e.g. B/Bb/A, crosses a real octave boundary
// partway through its own 7-degree block even though the degree-index count
// doesn't reflect it). Measured directly: B minor's V chord (a "#" on the
// raised third, matching the reported screenshot) reached real semitone 18
// -- 11 semitones above what the SAME chordCeiling produces in C major (7)
// -- because the block's 4th/5th degrees for that key land a full octave
// higher than its 0th/1st degrees do. B major/minor, Bb major/minor, and A
// major/minor (all real keys used from Grade 5 on) share this same
// distortion to varying degrees. A degree-index cap alone can never catch
// this, since the index never actually left its intended 0-4 range -- only
// checking the chord tone's REAL pitch can. `foldChordToneSafe` does exactly
// that: given a candidate scale-array index, walks it down a full octave
// block (index -= 7, which this array's per-octave layout guarantees is
// always exactly 12 semitones lower for the same degree -- see buildScale's
// loop) for as long as its real pitch sits above BASS_CHORD_SAFE_HI, the
// safe ceiling C major's own (undistorted) chord tones top out at. Mirrors
// melody.js's real-semitone BASS_SAFE_HI trim for the same class of problem
// on the melodic (alternating-hands) side.
const BASS_CHORD_SAFE_HI = 11; // real semitone ceiling (unmarked c = 0); C major's own chordCeiling tops out at 7, so this leaves a little headroom without letting any key's distortion through.
// 2026-09-14: the local PITCH_CLASS_BASS table (a hand-copy of melody.js's
// own, same problem) is gone -- see melody.js's matching comment. Any
// spelling nobody had added to it yet returned `undefined` here, and
// widening key coverage guarantees new spellings keep showing up.
// `pitchClassOf` (scales.js) computes any spelling's pitch class directly.
function absoluteSemitoneBass(entry) {
  return entry.octaveOffset * 12 + pitchClassOf(entry.ly);
}
function foldChordToneSafe(scale, idx) {
  let i = idx;
  while (i - 7 >= 0 && absoluteSemitoneBass(scale[i]) > BASS_CHORD_SAFE_HI) i -= 7;
  return i;
}

/** Convert an arbitrary units value to the closest single LilyPond duration
 * string (with a tie to a second note if it doesn't map to one token). */
function unitsToLilyDuration(units) {
  const table = [
    [16, '1'], [12, '2.'], [8, '2'], [6, '4.'], [4, '4'], [3, '8.'], [2, '8'], [1, '16'],
  ];
  for (const [u, ly] of table) {
    if (units === u) return [ly];
  }
  // Fallback: split into two tied tokens (largest-first greedy).
  const parts = [];
  let remaining = units;
  for (const [u, ly] of table) {
    while (remaining >= u) {
      parts.push(ly);
      remaining -= u;
    }
  }
  return parts.length ? parts : ['4'];
}

module.exports = { generateBass, unitsToLilyDuration };
