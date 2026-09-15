// ---------------------------------------------------------------------------
// Grade -> generation-parameter mapping (Piano Butler Sight-Reading Generator)
//
// This is the "Difficulty Mapping" table from the build spec, expressed as
// data so the generator engine can look up constraints for any grade/level.
// AMEB/ABRSM/Trinity grade numbers are the primary keys; the Clara Music
// level names (Spark/Ember/Flame/Blaze/Beacon) are provided as aliases that
// resolve to the same parameter bucket.
//
// NOTE: these ranges are a *starting point*, per the spec ("Teacher should
// review and adjust these ranges based on real testing"). Tweak freely.
// ---------------------------------------------------------------------------

// Duration "units" are expressed in sixteenth-note units so every bar length
// (in any supported time signature) is an integer, which keeps bar-filling
// arithmetic exact regardless of which note values are allowed.
const NOTE_VALUES = {
  sixteenth: { units: 1, ly: '16', label: 'sixteenth note' },
  eighth: { units: 2, ly: '8', label: 'eighth note' },
  dottedEighth: { units: 3, ly: '8.', label: 'dotted eighth note' },
  quarter: { units: 4, ly: '4', label: 'quarter note' },
  dottedQuarter: { units: 6, ly: '4.', label: 'dotted quarter note' },
  half: { units: 8, ly: '2', label: 'half note' },
  dottedHalf: { units: 12, ly: '2.', label: 'dotted half note' },
  whole: { units: 16, ly: '1', label: 'whole note' },
  // 2026-09-09: "triplet도 한 두번 나오는 정도" -- one note of a triplet group (3
  // notes filling one quarter-beat's worth of time). NOT used by rhythm.js's
  // fillBar/generateRhythm directly (a tuplet's 3-in-the-time-of-2 notes
  // don't fit the integer sixteenth-unit accounting the rest of the engine
  // relies on) -- index.js's generateExcerpt splits an already-placed
  // 'quarter' entry into three of these as a POST-PROCESS step, after the
  // bar's exact-fill guarantee already holds, and assembleLilyPond's token
  // builder wraps 3 consecutive ones in `\tuplet 3/2 { ... }`. `units: 1`
  // just marks it "short" for staccato/slur classification -- its real
  // notated duration comes from the eighth-note `ly` token living inside
  // the tuplet bracket, not from this units value.
  tripletEighth: { units: 1, ly: '8', label: 'triplet eighth note' },
};

// Bar length in sixteenth-note units for each supported time signature.
const TIME_SIG_UNITS = {
  '4/4': 16,
  '3/4': 12,
  '2/4': 8,
  '6/8': 12,
  // Cut time (alla breve) -- confirmed in the AMEB "Fourth Grade" scan
  // (example 3, "Allegro"). Same total bar duration as 4/4 (4 quarter-note
  // beats' worth of units); LilyPond accepts "2/2" directly as \time 2/2.
  '2/2': 16,
  // Compound triple meter (3 groups of 3 eighths = 9 eighths = 18 units).
  // Confirmed in the AMEB "Fifth Grade" scan (example 6, "Allegretto").
  '9/8': 18,
  // 3 half notes per bar (3 x 8 units). Confirmed in the AMEB "Seventh
  // Grade" scan (example 1, "Allegretto").
  '3/2': 24,
  // 2026-09-10: 5 quarter-note beats per bar (5 x 4 units). Confirmed in the
  // fresh, bigger AMEB "Seventh Grade" scan (SR G7.pdf, example 1) -- a
  // brand-new meter for this app, not seen in any earlier grade's scan.
  // rhythm.js's fillBar/generateRhythm are fully table-driven off
  // TIME_SIG_UNITS/BEAT_UNITS (no per-timeSig branching), so adding this
  // entry is low-risk -- it's treated exactly like 4/4 with an extra beat.
  '5/4': 20,
};

// 2026-09-04: the "felt beat" pulse (in the same sixteenth-note units) for
// each supported time signature -- simple meters pulse in quarter notes,
// compound meters (6/8, 9/8) pulse in DOTTED quarters (3 eighths as one
// felt beat), and the two half-note-beat meters (2/2 cut time, 3/2) pulse in
// half notes. rhythm.js's fillBar uses this so a quarter-note-or-longer
// duration only ever STARTS on a real beat, never stranded mid-beat --
// without it, nothing stopped e.g. two dotted-quarter notes from landing
// back-to-back in 4/4 (positions 0 and 6, the second one starting on the
// "and" of beat 2 instead of a beat), which reads as an ungrounded,
// syncopated-feeling rhythm with no clear per-beat reference point. Reported
// directly against a generated Grade 3 excerpt, and confirmed against the
// scan: the real book's dotted-quarter bars are always the standard
// "dotted-quarter + eighth" (fills exactly 2 beats) or "dotted-quarter on
// beat 1, quarter notes after" shapes -- never two dotted-quarters chained.
const BEAT_UNITS = {
  '4/4': 4,
  '3/4': 4,
  '2/4': 4,
  '6/8': 6,
  '9/8': 6,
  '2/2': 8,
  '3/2': 8,
  '5/4': 4, // simple quintuple meter, quarter-note felt beat -- see TIME_SIG_UNITS
};

// Keys: tonic pitch class + mode. `ly` is the LilyPond \key tonic spelling.
const KEYS = {
  cMajor: { name: 'C major', ly: 'c', mode: 'major' },
  aMinor: { name: 'A minor', ly: 'a', mode: 'minor' },
  gMajor: { name: 'G major', ly: 'g', mode: 'major' },
  fMajor: { name: 'F major', ly: 'f', mode: 'major' },
  dMajor: { name: 'D major', ly: 'd', mode: 'major' },
  bbMajor: { name: 'B flat major', ly: 'bes', mode: 'major' },
  dMinor: { name: 'D minor', ly: 'd', mode: 'minor' },
  eMinor: { name: 'E minor', ly: 'e', mode: 'minor' },
  ebMajor: { name: 'E flat major', ly: 'ees', mode: 'major' },
  bMinor: { name: 'B minor', ly: 'b', mode: 'minor' },
  aMajor: { name: 'A major', ly: 'a', mode: 'major' },
  gMinor: { name: 'G minor', ly: 'g', mode: 'minor' },
  // 2026-09-07: added for Grade 4's re-scan (SR G4.pdf) -- E major (4
  // sharps, ex.3/4) and Ab major (4 flats, ex.2) both appeared and had no
  // existing entry here.
  eMajor: { name: 'E major', ly: 'e', mode: 'major' },
  abMajor: { name: 'A flat major', ly: 'aes', mode: 'major' },
  // 2026-09-10: added during the Grade 5-8 recalibration against the fresh,
  // much bigger SR G5-G8.pdf scans (13/12/13/13 examples respectively,
  // superseding the older 6/6/5/5-example 2026-08 scans those buckets were
  // originally built from). Every one of these five keys was read directly
  // off a confirmed key signature in at least one grade5-8 example -- see
  // each bucket's own comment below for which example(s).
  dbMajor: { name: 'D flat major', ly: 'des', mode: 'major' }, // 5 flats
  fMinor: { name: 'F minor', ly: 'f', mode: 'minor' }, // 4 flats
  // scales.js's FLAT_MINOR_TONICS already covers 'des'/'f' (D flat major and
  // F minor spell with flats automatically); 'bes' (Bb minor) needed adding
  // there too -- see that file's own comment.
  bbMinor: { name: 'B flat minor', ly: 'bes', mode: 'minor' }, // 5 flats
  fsMinor: { name: 'F sharp minor', ly: 'fis', mode: 'minor' }, // 3 sharps
  csMinor: { name: 'C sharp minor', ly: 'cis', mode: 'minor' }, // 4 sharps
  gsMinor: { name: 'G sharp minor', ly: 'gis', mode: 'minor' }, // 5 sharps
  // 2026-09-14: "그레이드마다 샵/플랫 늘어감에 맞춰 이론상 허용되는 major/minor를 다
  // 깔기" -- widening each grade's key pool to the FULL major+minor set within
  // that grade's actual sharp/flat-count ceiling (Sohyun's own stated AMEB
  // rule: grade2=2, grade3=3, grade4=4, grade5=5, grade6=6, grade7=6,
  // grade8=7), not just whichever keys happened to appear in the scanned
  // book examples. That widening needs every key up to 5 sharps/5 flats
  // (already had all of those) AND now 6-7 sharps/flats too, which is what
  // required scales.js's spelling rewrite (see its own 2026-09-14 comment --
  // the old fixed pitch-class table physically couldn't spell these
  // correctly; the new letter-cycling algorithm can, verified directly
  // against real music theory for every one of these before adding them
  // here).
  bMajor: { name: 'B major', ly: 'b', mode: 'major' }, // 5 sharps
  fsMajor: { name: 'F sharp major', ly: 'fis', mode: 'major' }, // 6 sharps
  dsMinor: { name: 'D sharp minor', ly: 'dis', mode: 'minor' }, // 6 sharps
  csMajor: { name: 'C sharp major', ly: 'cis', mode: 'major' }, // 7 sharps
  asMinor: { name: 'A sharp minor', ly: 'ais', mode: 'minor' }, // 7 sharps
  cMinor: { name: 'C minor', ly: 'c', mode: 'minor' }, // 3 flats
  gbMajor: { name: 'G flat major', ly: 'ges', mode: 'major' }, // 6 flats
  ebMinor: { name: 'E flat minor', ly: 'ees', mode: 'minor' }, // 6 flats
  cbMajor: { name: 'C flat major', ly: 'ces', mode: 'major' }, // 7 flats
  abMinor: { name: 'A flat minor', ly: 'aes', mode: 'minor' }, // 7 flats
};

// Each bucket is the actual difficulty definition; multiple grade labels can
// point at the same bucket (mirrors the spec's grouped rows, e.g. 2-3, 4-5, 6-8).
const BUCKETS = {
  prelim: {
    // 2026-08-29: NOW scan-calibrated -- the user supplied real photos of
    // the official AMEB Preliminary sight-reading page (this book's
    // Preliminary section, unlike the "First Grade"-starting scan used for
    // grade1, DOES exist and was previously just unavailable). Findings
    // completely changed this bucket's shape:
    //   - There is NO two-staff/hand-off format at all here. The page is
    //     literally two separate lists: "Right hand" (13 -> actually 6
    //     numbered single-line treble-clef exercises) and "Left hand" (7
    //     numbered single-line bass-clef exercises), each its OWN staff
    //     with nothing on the other stave -- not even a rest. Every
    //     previous Preliminary design (both the old hands:'progressive'
    //     single-hand format AND the more recent hands:'alternating'
    //     grand-staff format) was a guess; this is the first real evidence,
    //     and it says: single hand, single staff, chosen once per exercise
    //     (never both in the same excerpt).
    //   - Every exercise is exactly 4 bars.
    //   - 2026-08-31 re-verification (user asked "does D major really show up
    //     in Prelim?" then "was there really no minor key?"): went back to
    //     both scan photos and read every one of the 13 examples' key
    //     signatures individually (RH: 6 examples, page 7; LH: 7 examples,
    //     page 8). Result: ONLY 0-sharp and 1-sharp signatures appear --
    //     RH exx 1/3/4/5 and LH exx 7/9/10/13 have no sharps/flats; RH ex 6
    //     and LH exx 8/11/12 have exactly 1 sharp. NO example anywhere in
    //     Prelim (either hand) has a 2-sharp signature -- the old "D major
    //     turns up" claim above was wrong (most likely a mis-read of one of
    //     the 1-sharp examples) and dMajor has been removed from keys[].
    //   - On the minor-key question: a 0-sharp signature is inherently
    //     ambiguous between C major/A minor, and 1-sharp between G major/E
    //     minor, so key signature alone can't settle it. Went note-by-note
    //     looking for the strongest possible tell (an incidental raised
    //     leading tone, e.g. G# in an A-minor piece). Found only one
    //     incidental accidental in the whole Prelim section -- RH example 2
    //     uses a natural-then-sharp F/F# pair (an "introducing accidentals"
    //     teaching device) -- which is NOT a minor-key leading tone, so it
    //     doesn't indicate a minor key. No other incidentals turned up on
    //     either page. Traced a couple of the plain 0-sharp melodies
    //     (e.g. LH ex 7) by ear/pixel-position and found nothing that reads
    //     as a clear minor-key cadence either. So: no legible evidence of an
    //     actual minor-key exercise was found -- A minor (a pure guess in an
    //     earlier, non-scan-calibrated version of this bucket) stays dropped.
    //     Caveat: these are simple 4-bar phone-photographed exercises with
    //     no fully conclusive cadence in several of them, so this is "no
    //     evidence found for minor" rather than ironclad proof none exists.
    //   - 2026-09-02 cross-check: the official AMEB Piano Syllabus 2026 +
    //     Technical Work (Pre-4) documents (in the user's "Piano Butler"
    //     project folder) show A minor and E minor ARE required Preliminary
    //     scales, and confirm sight-reading tests are only bound by "the
    //     technical standard of the Grade" -- i.e. minor keys are technically
    //     allowed at Preliminary. Sohyun's explicit decision: keep this
    //     bucket keyed off the actual sight-reading book's photographed
    //     examples (major-only), not the technical scale ceiling -- the
    //     sight-reading book deliberately runs easier than the full
    //     technical standard, and that's the more relevant ground truth for
    //     what excerpts should look like. Do not add minor keys here based
    //     on the technical scale list alone.
    //   - Confirmed time sigs: 4/4 (majority) and 2/4; one LH exercise
    //     uses alla breve "c" (same total length as 4/4, so no new
    //     TIME_SIG_UNITS entry needed).
    //   - Note values: quarter and half notes only, confirmed -- matches
    //     what this bucket already had.
    //   - Motion: overwhelmingly stepwise with only occasional small
    //     skips, consistent with this bucket's existing step/repeat/leap
    //     weights -- left those as-is.
    // hands:'progressive' reuses index.js's existing single-staff "one-hand"
    // rendering path (resolveHands -> 'one-hand'), extended (2026-08-29) to
    // pick treble or bass clef at random per excerpt rather than always
    // treble, so both the RH-only and LH-only halves of the real page are
    // represented. altSegBars/altFirstHand/altSegmentCounts/altCadenceChance
    // are gone -- those only mattered for the old hands:'alternating' shape.
    label: 'Preliminary',
    bars: [4, 4],
    noteValues: ['quarter', 'half'],
    hands: 'progressive',
    // 2026-09-14: widened from the book-scanned majors alone (cMajor,
    // gMajor -- 0-1 sharps, 0 flats) to also include their relative minors,
    // per Sohyun's explicit call: cover every major+minor within the
    // grade's real sharp/flat ceiling, not just what the scanned examples
    // happened to show. Prelim's own ceiling stays asymmetric (1 sharp, 0
    // flats) -- that's the actual confirmed range from the book scan (see
    // this bucket's 2026-08-29/08-31 comments), just now including aMinor/
    // eMinor alongside it instead of only their major counterparts.
    keys: ['cMajor', 'aMinor', 'gMajor', 'eMinor'],
    timeSigs: ['4/4', '2/4'],
    position: { spanScaleDegrees: 5 }, // strict 5-finger position
    maxLeapInterval: 3, // 3rd -- melody.js's leap-size formula for this
    // interval already only ever produces steps or exact-3rd leaps (never a
    // bigger "leap"), so maxLeapsPerExcerpt is mostly a formality here.
    maxLeapsPerExcerpt: 1,
    stepWeight: 0.85,
    repeatWeight: 0.12,
    leapWeight: 0.03,
    leftHandStyle: 'wholeBarRoot', // unused now that hands is 'progressive'; harmless if left in place
  },
  grade1: {
    // 2026-09-07: RECALIBRATED against a much bigger/cleaner source -- a
    // 13-example photographed AMEB "Grade 1" section (3 pages, SR G1.pdf)
    // that SUPERSEDES the earlier 8-example CamScanner scan this bucket was
    // built from. Every alternating example is still a SINGLE melodic line
    // on a grand staff that hands off between RH and LH, never
    // simultaneous -- see index.js's buildAlternatingExcerpt for the
    // segment structure this drives. New findings vs. the old 8-example
    // scan:
    //   - G major (1 sharp) appeared 4/13 times (Ex3, 6, 9, 12) -- added
    //     back to keys[]. Bb major (2 flats) appeared once (Ex13, a
    //     single-hand-only example) -- added too, but on lighter evidence.
    //   - 3/4 appeared 7/13 times (Ex2,4,5,8,9,11,12) -- this is a real gap
    //     the old 8-example scan simply didn't happen to sample; added.
    //   - Segment length is NOT fixed at 2 bars: within any one excerpt
    //     both/all segments always match each other, but that shared
    //     length varies piece to piece -- 2 bars (Ex1,2,3,6, ~5/11), 3 bars
    //     (Ex4,5,8, ~3/11), 4 bars (Ex7, 1/11), or three 2-bar segments
    //     (Ex11). See index.js's altSegBars array-of-pairs support (added
    //     alongside this recalibration) and altSegmentCounts below for the
    //     3-segment shape.
    //   - RH does NOT always lead: Ex3, Ex10, and Ex11's opening segment
    //     all start with LH. altFirstHand switched from 'rh' to 'either'.
    //   - Ex12 and Ex13 (2/13) are single-hand-only for the whole excerpt
    //     (no hand-off at all) -- NOT modeled here; buildAlternatingExcerpt
    //     has no single-hand mode yet, so this shape is still missing.
    //     Flagged for a future pass rather than guessed at.
    // Range: phrases regularly span a 6th-7th within one slur, well past a
    // strict 5-note "5-finger position" -- span stays at 6 (unchanged,
    // still consistent with the new examples).
    label: 'Grade 1',
    bars: [4, 6],
    noteValues: ['quarter', 'half', 'eighth'],
    hands: 'alternating',
    // 2026-09-14: widened to the full major+minor set within this grade's
    // real ceiling (2 sharps, 2 flats -- the scanned majors here already
    // topped out there: dMajor=2 sharps, bbMajor=2 flats), adding the
    // relative minors the book examples themselves didn't happen to show.
    keys: ['cMajor', 'aMinor', 'gMajor', 'eMinor', 'dMajor', 'bMinor', 'fMajor', 'dMinor', 'bbMajor', 'gMinor'],
    timeSigs: ['4/4', '2/4', '3/4'],
    position: { spanScaleDegrees: 6 },
    maxLeapInterval: 3,
    maxLeapsPerExcerpt: 2,
    stepWeight: 0.75,
    repeatWeight: 0.13,
    leapWeight: 0.12,
    leftHandStyle: 'halfBarRootFifth', // used only if a user forces "hands together" override
    // Per-excerpt shared segment length, weighted roughly to the 13-example
    // distribution above (2-bar most common, 3-bar fairly common, 4-bar
    // rare). See index.js buildAlternatingExcerpt's array-of-pairs support.
    altSegBars: [[2, 2], [3, 3], [4, 4]],
    altSegBarsWeights: [0.55, 0.35, 0.1],
    altFirstHand: 'either', // RH leads more often but not always -- 3/11 examples opened LH
    // 2026-09-07: REVERTED the 2026-08-27 user-directed bias toward the
    // longer 3-segment (6-bar) shape, per explicit request to match the
    // book's actual frequency instead -- the 13-example re-scan shows
    // 3-segment excerpts are rare (1/11 alternating examples, Ex11 only),
    // so the weighting now reflects that ~9%/91% split rather than the
    // earlier stylistic 70%/30% preference.
    altSegmentCounts: [2, 3],
    altSegmentWeights: [0.91, 0.09],
  },
  grade2: {
    // Calibrated against the AMEB "Second Grade" page (3 examples, same
    // 2026-08 scan). Grade 2 is a TRANSITIONAL step, not yet full
    // hands-together: it still alternates RH/LH with rests, like Grade 1,
    // but looser -- segments run 1-3 bars (not a fixed 2), and either hand
    // can lead (one example opens with LH, unlike Grade 1's RH-always-first).
    // Keys confirmed: F major (1 flat), G major (1 sharp), and a flat key
    // that reads as Bb major. Time sigs confirmed: 4/4, 3/4.
    //
    // 2026-08-29: a fuller scan (13 examples across 3 pages, not just 3)
    // confirmed the alternating/either-leads shape above and additionally
    // showed a descriptive performance-direction WORD ("smoothly", "loudly",
    // "cheerfully", "soft", "loud", "brightly") printed under the first
    // note of several examples -- NOT a standard mp/mf/f abbreviation like
    // Grade 3+ uses. Modeled as its own `dynamics` pool; index.js's
    // attachDynamic now renders anything outside the standard dynamic set
    // as italic text under the note instead of a \mp-style builtin.
    //
    // 2026-09-07: that fuller scan (SR G2.pdf, 12 clean examples) was
    // finally re-transcribed at usable resolution and SUPERSEDES the
    // earlier small-sample key/timeSig calibration below. Findings:
    //   - D major (2 sharps) was actually the SINGLE MOST COMMON key, 4/12
    //     examples (Ex1, 2, 8, 12) -- previously missing entirely. Eb major
    //     (3 flats) appeared once (Ex11) -- added on lighter evidence.
    //   - 2/4 appeared 2/12 times (Ex3, 4) -- previously missing.
    //   - Staccato dots appear within alternating-hand excerpts in 3/12
    //     examples (Ex3, 4, 10), reaching down onto EIGHTH notes too
    //     (unlike Grade 3+'s quarter-note-or-longer floor) -- see
    //     altStaccatoChance/altStaccatoMinUnits and index.js's
    //     buildAlternatingExcerpt, which had no staccato support at all
    //     before this pass.
    //   - The dynamics word sometimes CHANGES partway through one excerpt
    //     (Ex8: "loud" then later "soft") rather than being set once at the
    //     opening note -- light evidence (1/12), see altSecondDynamicChance.
    label: 'Grade 2',
    bars: [4, 8],
    noteValues: ['quarter', 'half', 'eighth', 'dottedQuarter'],
    hands: 'alternating',
    // 2026-09-14: widened to the full major+minor set within this grade's
    // stated ceiling (2 sharps/2 flats). An earlier pass on this same date
    // kept ebMajor/cMinor here too (3 flats) to preserve a scanned-example
    // hit, but Sohyun asked why a 2/2-grade had a 3-flat key and, once
    // asked directly, chose the strict symmetric 2/2 reading -- ebMajor and
    // cMinor were removed from THIS bucket. They still surface starting at
    // grade3, whose ceiling already reaches 3 flats, so no real coverage is
    // lost, only pushed one grade later.
    keys: [
      'cMajor', 'aMinor', 'gMajor', 'eMinor', 'dMajor', 'bMinor',
      'fMajor', 'dMinor', 'bbMajor', 'gMinor',
    ],
    timeSigs: ['4/4', '3/4', '2/4'],
    position: { spanScaleDegrees: 7 },
    maxLeapInterval: 4,
    maxLeapsPerExcerpt: 3,
    stepWeight: 0.72,
    repeatWeight: 0.12,
    leapWeight: 0.16,
    leftHandStyle: 'brokenRootFifth', // used only if a user forces "hands together" override
    altSegBars: [1, 3], // variable segment length, looser than Grade 1
    altFirstHand: 'either', // either hand may lead
    dynamics: ['smoothly', 'loudly', 'cheerfully', 'soft', 'loud', 'brightly'],
    altStaccatoChance: 0.25, // ~3/12 examples had staccato
    altStaccatoMinUnits: NOTE_VALUES.eighth.units, // dots reach eighth notes here, unlike grade3+
    altSecondDynamicChance: 0.15, // light evidence (1/12) of a mid-piece word change
  },
  grade3: {
    // Calibrated against a bar-by-bar read of all 9 examples on the AMEB
    // "Third Grade" pages (2026-08 scan, pages 4-5). Findings:
    //   - 6 of 9 examples (ex. 1, 2, 6, 7, 8, 9) are genuinely hands
    //     TOGETHER and continuous -- confirms the AMEB manual's note that
    //     "Grade 3-8 are examined in the normal way." LH textures actually
    //     seen across these: whole-bar block chords (ex.1's dotted-half
    //     chords), a sustained pedal tone held almost the whole excerpt
    //     (ex.2), and a broken/independent answering figure (ex.6, 7) --
    //     i.e. NOT one fixed LH pattern the way Grade 1-2's accompaniment
    //     was. Modeled via a new 'mixed' leftHandStyle (bass.js) that picks
    //     one concrete texture per excerpt from {wholeBarRoot,
    //     halfBarRootFifth, brokenRootFifth} rather than always the same one.
    //   - 3 of 9 (ex. 3, 4, and the top-of-page-5 continuation) still use a
    //     brief alternating/call-and-response device -- but with much
    //     SHORTER segments than Grade 1-2 (as short as a single bar,
    //     hocket-style in ex.4), sometimes with a sustained final note
    //     rather than a clean hand-off. Modeled as a per-excerpt ~1-in-3
    //     chance of the alternating path via hands:'mixed' +
    //     mixedAlternatingChance (see index.js resolveHands), reusing
    //     buildAlternatingExcerpt with tighter altSegBars:[1,2].
    //   - 2026-08-31: RE-VERIFIED directly against the scan page images
    //     (not just this comment's prior notes) after a user question about
    //     Preliminary prompted a full grade-by-grade re-check. Reading each
    //     of the ~8 examples' actual key signatures: F major x4 (1 flat),
    //     D major x2 (2 sharps), Bb major x1 (2 flats), and C major x1 (no
    //     sharps/flats, ex.8) -- NO example shows a 1-sharp signature. The
    //     bucket previously had 'gMajor' here with no supporting example
    //     anywhere in the scan (an undocumented leftover, unlike aMinor/
    //     eMinor below which were always honestly flagged as unconfirmed) --
    //     removed, and cMajor added in its place since that one genuinely IS
    //     in the scan (ex.8) but had been missing from this list. No minor
    //     key directly confirmed in this sample -- aMinor/eMinor kept as a
    //     reasonable estimate per general AMEB Grade 3 syllabus scope, NOT
    //     scan-confirmed; flag for removal if that turns out wrong.
    //   - Confirmed time sigs: 3/4, 4/4, 2/4. No 6/8 seen at this grade.
    //   - NOT modeled yet (deferred, bigger engine changes): example 1 opens
    //     with a bracketed eighth-note TRIPLET (no tuplet support in
    //     rhythm.js yet), and example 6 has chromatic passing tones outside
    //     the diatonic scale (melody.js only ever walks in-key). Flagging
    //     both as known gaps rather than guessing at an implementation.
    //   - 2026-09-03: RECALIBRATED against a DIFFERENT/NEWER copy of the
    //     Grade 3 book -- 15 examples (pages "AMEB 15" through "AMEB 19"),
    //     not the 9-example scan the comment above documents. This is very
    //     likely a different print edition of the same AMEB "Piano
    //     Sight-reading" book (its examples are renumbered/reselected
    //     between editions), so its evidence supersedes the 2026-08 scan's
    //     KEY findings above rather than averaging with them -- keeping
    //     whichever book is most recently in hand, per the session's
    //     standing approach to conflicting scan evidence.
    //       - Key signatures, all 15 read bar-by-bar: C major x1 (ex.10),
    //         G major x2 (ex.2, ex.13), Eb major x3 (ex.5, ex.9, ex.15), A
    //         major x2 (ex.6, ex.11), Bb major x4 (ex.1, ex.4, ex.8, ex.12),
    //         D major x2 (ex.3, ex.14... wait ex.14 is discussed below) --
    //         NO F major and NO minor key anywhere in this set, a genuinely
    //         different distribution from the old scan. `keys` below
    //         replaces the old list entirely rather than merging with it;
    //         fMajor/aMinor/eMinor dropped (fMajor was scan-confirmed in the
    //         OLD book, but 0/15 in this one -- kept out until a scan shows
    //         it again, same caution as the old aMinor/eMinor estimate).
    //       - Time sigs: 2/4, 3/4, 4/4 again -- no 6/8, consistent with the
    //         old scan.
    //       - Structural findings new to this scan, now modeled:
    //         * ex.14: LH moves in stepwise crotchets outlining the harmony
    //           ("walking bass") rather than repeating fixed chord tones --
    //           new bass.js style `walkingBass`.
    //         * ex.15: LH strikes a full root-third-fifth chord on every
    //           beat -- new bass.js style `blockChordsEveryBeat` (this
    //           file's one genuinely polyphonic LH texture; every other
    //           style stays single-note).
    //         * ex.10 and ex.12: true imitation -- the LH echoes the RH's
    //           previous bar's exact rhythm and contour down an octave, a
    //           real (if simple) canon, not the existing hocket-style
    //           alternating device. New bass.js style `canonImitation`.
    //         * ex.5 and ex.8: the RH itself is chordal (block chords, not a
    //           single melodic line) for the whole excerpt. New
    //           generateExcerpt feature `rhChordChance` (index.js) --
    //           thickens every RH note with a diatonic third below it.
    //         * ex.2, ex.4, ex.15: a second expressive word ("rall.",
    //           "dim.", "slowing") appears partway through the piece, not
    //           just at the very start. New generateExcerpt feature
    //           `midPieceMarkingChance`/`midPieceMarkings`.
    //         All four are wired into the 'mixed' leftHandStyle pool
    //         (mixedStylePool below) and the two generateExcerpt-level
    //         chances, so they show up as a genuine MINORITY of generated
    //         excerpts (roughly matching how rare they are on the actual
    //         page: 2-3 examples each out of 15), not as the default.
    //       - Still NOT modeled (same class of gap as the triplet/chromatic
    //         notes above): none of the 15 examples showed anything beyond
    //         what's now covered.
    //       - Bar length: counted every one of the 15 examples' bars
    //         individually (barline-by-barline, not just eyeballing the
    //         system length) -- EVERY single one is exactly 8 bars, with no
    //         exceptions (ex.1-9 confirmed one page at a time, ex.10-15
    //         likewise). That's a much tighter, more consistent standard
    //         than the old 9-example scan's `bars: [6, 10]` range, so
    //         narrowed to exactly 8 rather than kept as a wider guess --
    //         this only governs the hands-together (70%) majority branch;
    //         see below re: the alternating branch, which this scan can't
    //         speak to.
    //       - 2026-09-04 RE-CHECKED specifically for the hocket-style
    //         hands-alternating format the OLD scan's
    //         `mixedAlternatingChance: 0.3` was calibrated from (previously
    //         only flagged, not acted on -- asked to confirm one way or the
    //         other against this book). Went back through all 15 examples
    //         looking specifically at every bar where one hand rests: ex.1,
    //         9, and 13 all have LH rest bars, but in every one of them the
    //         RH keeps playing straight through -- that's a sparser/echoing
    //         LH accompaniment, not the hocket format (which requires BOTH
    //         hands to trade off carrying ONE melodic line, the other
    //         silent). No example anywhere in this 15 has the RH rest while
    //         the LH carries the line. Conclusion: this printing's Grade 3
    //         page does not use the alternating format at all --
    //         `mixedAlternatingChance` dropped to 0 to match. altSegBars/
    //         altFirstHand/altSegmentCounts/altSegmentWeights are left in
    //         place (dead while the chance is 0) rather than deleted, in
    //         case a future scan finds real alternating examples again.
    //       - 2026-09-04: LH texture variety -- a generated batch looked too
    //         dominated by the two-note-per-bar "root/fifth zigzag" styles
    //         (halfBarRootFifth, brokenRootFifth). Re-tallying which of the
    //         13 hands-together-with-real-accompaniment examples (excludes
    //         ex.3, whose LH is too sparse/independent to read as a
    //         "style") match which texture: sustained/pedal-tone
    //         (wholeBarRoot) is actually the SINGLE MOST common one on the
    //         page (ex.1, 2, 6, 9, 11 -- roughly 5 of 13), and a flowing
    //         arpeggiated broken-chord bass (ex.4, ex.8's legato ascending
    //         line) appears too, which the pool never drew from at all --
    //         added 'triadPattern' and re-weighted wholeBarRoot up / the two
    //         zigzag styles down accordingly (mixedStylePool below).
    label: 'Grade 3',
    bars: [8, 8],
    // 2026-09-09: "grade 3 다시 폴더 검색해서 다시 재점검 해서 평준화 좋게 하자" --
    // re-scanned the same 15-example AMEB Grade 3 pages this bucket's other
    // comments were calibrated from (freshly re-photographed, same book/
    // edition -- key signatures, tempo words, and dynamics all line up
    // bar-for-bar with what's already documented below). One genuine gap
    // turned up on this re-check: 'dottedHalf' was never in this list even
    // though a real dotted-half notehead (not a tied half+quarter) appears
    // in a full quarter of the set -- ex.9's LH holds one every single bar,
    // ex.13/ex.15's RH phrases end on one, and ex.14's RH pairs one with a
    // beamed eighth-eighth ("2." + two 8ths = 12+2+2 = 16 units, landing
    // exactly on a 4/4 bar's own quarter-note grid, so no special alignment
    // handling is needed the way grade4's dottedQuarter-in-a-4-unit-beat
    // idiom required -- see rhythm.js's dottedQuarterEighthChance comment
    // for that contrast). Added directly to the shared vocabulary; its
    // existing global baseWeight (rhythm.js, 0.5 -- already tuned lower than
    // quarter/half/eighth/dottedQuarter) keeps it an occasional "sustain"
    // note rather than a co-equal duration, matching how it reads on the
    // page (never more than one per bar, never back-to-back).
    // 2026-09-09: "dotted rhythm은 dotted minim만" -- direct follow-up
    // instruction dropping 'dottedQuarter' (dotted crotchet) back out again:
    // the only dotted duration this bucket should ever produce is dottedHalf
    // (dotted minim), just added above. dottedQuarter had been in this list
    // since the bucket's very first calibration pass, well before either of
    // today's two re-checks -- removing it now on explicit instruction
    // rather than scan evidence.
    noteValues: ['quarter', 'half', 'eighth', 'dottedHalf'],
    hands: 'mixed',
    mixedAlternatingChance: 0,
    altSegBars: [1, 2],
    altFirstHand: 'either',
    // 2026-09-14: widened to the full major+minor set within this grade's
    // ceiling (3 sharps, 3 flats).
    keys: [
      'cMajor', 'aMinor', 'gMajor', 'eMinor', 'dMajor', 'bMinor', 'aMajor', 'fsMinor',
      'fMajor', 'dMinor', 'bbMajor', 'gMinor', 'ebMajor', 'cMinor',
    ],
    timeSigs: ['4/4', '3/4', '2/4'],
    position: { spanScaleDegrees: 7 },
    maxLeapInterval: 4,
    maxLeapsPerExcerpt: 3,
    stepWeight: 0.68,
    repeatWeight: 0.12,
    leapWeight: 0.20,
    allowContraryMotion: true,
    leftHandStyle: 'mixed',
    // 2026-09-05 RE-WEIGHTED A THIRD TIME: reported AGAIN as still too busy
    // ("왼손비중이 아직도 좀 많네") even after the previous rebalance (4
    // wholeBarRoot + 2 triadPatternCalm vs 5 busy styles out of 11, ~45%
    // busy). The evidence tally (wholeBarRoot 5/13, triadPatternCalm-type
    // 2/13) was already close to fully spent last time without satisfying
    // the density complaint, so this pass leans further calm than a strict
    // evidence-proportion match would justify -- every style stays present
    // (nothing dropped to 0, still matches SOME real page evidence), but the
    // calm pair's combined share goes from 6/11 (~55%) to 8/13 (~62%): one
    // more triadPatternCalm slot on top of last time's increase, one more
    // wholeBarRoot slot. The five busier styles (halfBarRootFifth/
    // brokenRootFifth/walkingBass/blockChordsEveryBeat/canonImitation) stay
    // at 1 slot each, same as before -- only the calm end grew, so their
    // combined share drops from ~45% to ~38%.
    // 2026-09-10: "그레이드 3이 그레이드 4보다 쉬워야하는데 더 복잡하게 느껴지는데" --
    // direct cross-grade comparison. Two features were unique to THIS bucket
    // and absent from grade4 entirely, each a genuinely harder reading skill
    // than anything grade4 asks for: 'blockChordsEveryBeat' (a full
    // root-third-fifth triad struck on every beat -- this file's one truly
    // polyphonic LH texture) and rhChordChance (thickens every RH melody
    // note into a 2-note chord for the whole excerpt). Grade4's own
    // mixedStylePool has no chord-heavy LH style at all, and grade4 has no
    // RH-chording feature whatsoever -- so grade3 was asking students to
    // read chords in BOTH hands in ways grade4 never does, despite being the
    // easier grade. Dropped blockChordsEveryBeat from the pool entirely
    // (its slot folded into wholeBarRoot, the calmest texture) and
    // rhChordChance to 0 below.
    mixedStylePool: [
      'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot',
      'halfBarRootFifth',
      'brokenRootFifth',
      'triadPatternCalm', 'triadPatternCalm', 'triadPatternCalm',
      'walkingBass', 'canonImitation',
    ],
    // 2026-09-10: dropped 0.10 -> 0 -- see the mixedStylePool comment just
    // above. A chorded RH is a harder reading skill (two noteheads read as
    // one interval, every single note) that grade4 never asks for at all;
    // keeping it on in the supposedly-easier grade3 was a direct
    // contributor to "그레이드 3이 그레이드 4보다... 더 복잡하게 느껴지는데".
    rhChordChance: 0,
    // ex.2/ex.4/ex.15 out of 15 had a second expressive word partway through
    // -- see generateExcerpt's midMarking handling (index.js).
    // 2026-09-09: re-read the actual words directly off the fresh re-scan --
    // ex.2 carries BOTH "rall." (above the staff) and "dim." (as a dynamic,
    // same spot) together; ex.4 and ex.15 each end with "slowing" instead
    // (never "poco rall.", which doesn't appear anywhere in the 15 examples
    // and looks like it was invented rather than read off the page). Swapped
    // the unconfirmed word out for the one actually seen -- twice, the most
    // common of the three -- so the pool now matches every confirmed
    // instance instead of 2 of 3.
    midPieceMarkings: ['rall.', 'dim.', 'slowing', 'slowing'],
    midPieceMarkingChance: 0.2,
    // 2026-08-27: the alternating (hocket-style) ~30% minority branch was
    // defaulting to the same 2-3-segment count as Grade 1/2, which with
    // this grade's much shorter altSegBars:[1,2] segments (~1.5 bars each
    // on average) produced excerpts as short as 2-3 bars total -- nowhere
    // near this bucket's declared `bars: [6, 10]` (which only the
    // hands-together 70% majority branch actually reads; alternating
    // excerpts get their length from altSegBars/altSegmentCounts instead,
    // see index.js buildAlternatingExcerpt). Bumped segment count so the
    // alternating branch's total length lands in roughly the same 6-9 bar
    // range as the hands-together branch, keeping a full-length excerpt
    // even though only some of it is hocket-style per the real scan.
    altSegmentCounts: [4, 5, 6],
    altSegmentWeights: [0.3, 0.4, 0.3],
    // 2026-09-03: articulation + dynamics/tempo pass against the same
    // 15-example scan the bar-length/textures above came from -- every
    // example carries SOME below-staff dynamic mark, 5 of the 15 (ex.1,2,3,
    // 4,7) additionally carry an above-staff tempo/character word, and a
    // genuine minority use STACCATO dots.
    //   - Tempo words (above-staff, separate from the dynamic): "Moderato"
    //     (ex.1), "Espressivo" (ex.2), "Lively" (ex.3), "Adagio" (ex.4),
    //     "Allegretto" (ex.7). Grade3 never had a tempoMarkings pool before
    //     this -- 0% of generated excerpts showed one even though ~1/3 of
    //     the real page does.
    //   - Dynamics (below-staff, under the first note): plain f/p/mf/mp
    //     (ex.1,3,5,7,8,11,12) AND, just as often, a dynamic paired with a
    //     descriptive word right beside it -- "p gentle" (ex.6), "mp
    //     sweetly" (ex.9, ex.14), "f playfully" (ex.10), "p lilting"
    //     (ex.13), "p sadly" (ex.15). attachDynamic (index.js) now parses a
    //     dynamics-pool entry as "<standardDynamic> <word>" and prints BOTH
    //     (the real \dynamic command plus the word in italics beside it),
    //     falling back to its old word-only rendering for a bucket (like
    //     Grade 2's) whose entries aren't a real dynamic at all.
    //   - 2026-09-04: CORRECTED -- tempo word and character-word dynamic are
    //     NOT independent on the real page. Every example with a tempo word
    //     (ex.1,2,3,7) has only a PLAIN dynamic under it; every
    //     character-word dynamic ("p gentle" etc.) shows up ONLY on an
    //     example with no tempo word at all. Reported directly: an
    //     independently-random draw had landed "Espressivo" (a tender,
    //     lyrical character) over "f playfully" (a bouncy one), which reads
    //     as a contradiction. Split into `dynamics` (plain -- used whenever
    //     a tempo marking is also printed) and `standaloneDynamics` (the
    //     character-word combos plus a few plain ones too -- used when no
    //     tempo marking was drawn); index.js now picks tempoMarking FIRST
    //     and chooses the dynamic pool based on that result, so the two
    //     never clash. `tempoMarkingChance` (~5/15) keeps tempo markings a
    //     genuine minority so standaloneDynamics is actually reachable most
    //     of the time, matching the real page's ratio.
    //   - Staccato: NOT a whole-piece toggle -- on close inspection, dots
    //     only ever land on quarter-note-or-longer notes (chords included);
    //     every eighth-note run stays slurred/legato regardless. Genuinely
    //     staccato examples: ex.3, ex.5, ex.7 (both hands' quarters dotted)
    //     and ex.8 (RH chords dotted, LH stays legato/slurred underneath --
    //     confirms this can differ per hand, not just per excerpt).
    //     staccatoChance is the per-excerpt chance the RH goes staccato (its
    //     quarter+ notes only); lhStaccatoWithRhChance is, GIVEN that, the
    //     chance the LH's quarter+ notes are dotted too, rather than staying
    //     legato -- no example showed LH-staccato-without-RH, so this is
    //     deliberately a one-way dependency, not two independent coin flips.
    tempoMarkings: ['Moderato', 'Espressivo', 'Lively', 'Adagio', 'Allegretto'],
    tempoMarkingChance: 0.33,
    dynamics: ['f', 'p', 'mf'],
    standaloneDynamics: ['f', 'mp', 'mf', 'p', 'p gentle', 'mp sweetly', 'f playfully', 'p lilting', 'p sadly'],
    // 2026-09-09: direct follow-up re-check against the Grade 3 folder --
    // "스타카토는 양손 같이칠 때 넣지말고 손이 교차하거나 할 때 진짜 가끔 작은
    // 비율로 만들어줘, 얼터네이션 일 때도 아주 작은 비율로": staccato should
    // NEVER appear while both hands play together (this bucket's normal
    // hands-together path), only very rarely when the hands alternate/cross.
    // staccatoChance -> 0 turns off the hands-together mechanism entirely;
    // lhStaccatoWithRhChance is left in place below but is now dormant dead
    // code (it only ever fires when rhStaccato is already true, which can no
    // longer happen) -- kept rather than deleted so the "no LH-staccato-
    // without-RH" documentation/finding above stays intact if staccatoChance
    // is ever raised again.
    staccatoChance: 0,
    lhStaccatoWithRhChance: 0.45, // dormant -- see staccatoChance note above
    // altStaccatoChance is the ALTERNATING-hands path's own independent
    // staccato toggle (see index.js's buildAlternatingExcerpt, gated
    // separately from staccatoChance above). Grade 3 never had this set at
    // all until now; added at a small value per "진짜 가끔 작은 비율로...
    // 얼터네이션 일 때도 아주 작은 비율로" (rare, small ratio). Currently
    // dormant in practice since this bucket's mixedAlternatingChance is 0
    // (see that param's own comment -- no true alternating/hocket examples
    // found in this book edition), kept here for the same reason the other
    // now-dormant alt* params (altSegBars, altFirstHand, altSegmentCounts,
    // altSegmentWeights) are: in case a future scan finds real alternating
    // examples again, this is ready rather than needing to be re-derived.
    altStaccatoChance: 0.1,
    altStaccatoMinUnits: NOTE_VALUES.quarter.units,
    // 2026-09-05: "아티큘레이션이 너무 남용되고있어... 거의 누르는 족족
    // 스타카토 슬러" -- staccato dots and legato slurs were each applied to
    // LITERALLY EVERY qualifying note/run, every time their toggle fired.
    // articulationNoteChance is the per-note/per-run chance an individual
    // mark actually gets drawn (see index.js) -- 0.6 means roughly 3 in 5 of
    // the eligible quarter+ notes get dotted in a staccato excerpt (not all
    // of them), and roughly 3 in 5 of eligible short-note runs get slurred
    // (this applies to every grade3 excerpt's slurring, not just staccato
    // ones, since slur marking was never gated by rhStaccato to begin with).
    // staccatoChance/lhStaccatoWithRhChance also brought down (0.3->0.22,
    // 0.65->0.45) so a fully-staccato, both-hands-dotted excerpt is itself
    // less common on top of being less densely marked when it does happen.
    articulationNoteChance: 0.6,
    // 2026-09-04, requested directly ("긴 호흡의 프레이징 성격의 slur도 넣어주고
    // 타이도 바를 넘는 것도 섞어줘") -- unlike every other grade3 param above,
    // these two are NOT tallied against the 15-photo scan (no bar-by-bar
    // phrase-mark or tie count was taken the way staccato/keys/bars were).
    // Reasonable, adjustable defaults instead -- see index.js for what each
    // actually draws.
    //   - phraseSlurChance: a long phrasing slur (LilyPond `\( \)`, visually
    //     distinct from the short legato `( )` slur already drawn over
    //     eighth-note runs) spanning each half of the piece -- reads as a
    //     "breath" phrase mark over the whole opening/closing gesture, layered
    //     ON TOP OF (not replacing) the short slurs.
    //     2026-09-05: dropped 0.6 -> 0.4 and (index.js) now hard-gated off
    //     whenever rhStaccato is on -- reported directly as "말이 안되는데"
    //     against an excerpt where the long slur started/ended squarely ON a
    //     dotted/staccato note, a real contradiction (slur = sustain through
    //     the phrase, dot = detach that exact note). The staccato gate fixes
    //     the contradiction outright; the chance was also brought down since
    //     0.6 combined with staccatoChance/rhChordChance/midPieceMarkingChance
    //     all independently rolling made a single excerpt likely to stack
    //     several unrelated decorations at once, reading as over-notated --
    //     the real scan shows each of these as a feature of a DIFFERENT
    //     individual example, never all five stacked on one page.
    //     2026-09-07: dropped again, 0.4 -> 0.15, per direct feedback
    //     ("타이 슬러 빈도가 너무 높은데") after seeing generated pages where the
    //     long phrase slur -- which spans a full HALF of the 8-bar excerpt
    //     each time it fires, i.e. basically the whole visible system --
    //     showed up on multiple pages in a row. Since this was never
    //     scan-evidence in the first place (see the note above), there's no
    //     "correct" frequency to defend; lowered further to read as a
    //     genuine occasional feature rather than a piece's default look.
    //   - tieAcrossBarChance: per ELIGIBLE bar boundary (not per excerpt,
    //     see index.js), the chance that boundary's two notes get forced to
    //     the same pitch and tied across the barline instead of re-struck.
    //     2026-09-07: dropped 0.15 -> 0.08 alongside phraseSlurChance above,
    //     same feedback ("타이 슬러 빈도가 너무 높은데") -- still per-boundary
    //     rather than per-excerpt so it stays a rare accent, not a per-piece
    //     guarantee, on top of the piece already firing an actual tie
    //     less than half as often as before.
    phraseSlurChance: 0.15,
    tieAcrossBarChance: 0.08,
    // 2026-09-09: "rest 도 minim rest, crotchet rest, whole bar rest 섞어서"
    // -- this bucket had NO rest mechanism at all for the RH/melody line
    // before today (only the LH's own separate bass rest params, added just
    // below). New index.js support (assembleLilyPond's wholeRestBars /
    // partialRestIdx) lets a bar be replaced entirely with a whole-bar rest,
    // or a single quarter- or half-duration note within a bar be replaced
    // with a matching rest -- exactly the "minim rest, crotchet rest, whole
    // bar rest" mix requested. Values kept modest (never the excerpt's final
    // bar, see index.js) so rests read as an occasional real feature rather
    // than emptying out the melody.
    rhRestChance: 0.15,
    rhWholeBarRestChance: 0.1,
    // Mirrors rhRestChance/rhWholeBarRestChance above but for the LH, using
    // the mechanism already built and calibrated for grade4 (see that
    // bucket's own bassRestChance/bassSmallRestChance comments) -- same
    // request ("rest 도... 섞어서") applies to both hands, and the book scan's
    // ex.1 already showed LH rest bars at this grade too. bassSmallRestChance
    // now also covers HALF_UNITS-duration events, not just QUARTER_UNITS (see
    // bass.js), so "minim rest" is available on the LH side as well as RH.
    bassRestChance: 0.15,
    bassSmallRestChance: 0.12,
  },
  grade4: {
    // Calibrated against all 6 examples on the AMEB "Fourth Grade" pages
    // (2026-08 scan, pages 6-7). Findings:
    //   - Every example is hands together and continuous -- no alternating
    //     device at this grade (unlike Grade 3's ~30% minority case).
    //   - NEW at this grade: every example carries a TEMPO/CHARACTER
    //     marking above the first bar (Andantino, Minuet tempo, Allegro,
    //     Waltz time, Moderato, Tempo comodo) and a DYNAMIC under the first
    //     note (mp/mf/p seen). Both are now modeled generically (see
    //     index.js: params.tempoMarkings / params.dynamics, rendered as
    //     LilyPond \tempo text + a dynamic mark on the first note) rather
    //     than grade-4-specific code.
    //   - NEW time signature: cut time (2/2), confirmed in example 3
    //     ("Allegro") -- added to TIME_SIG_UNITS.
    //   - Bar counts observed: 8 (ex.1,2,4,5), ~9-10 (ex.3,6) -- shorter
    //     than the old placeholder grade4to5 range of [12,16], which was
    //     evidently sized for the upper end of that merged bucket, not
    //     Grade 4 itself.
    //   - No sixteenth notes seen in this sample (removed from noteValues
    //     vs. the old shared bucket); eighth/dotted-quarter/dotted-eighth
    //     patterns are the finest rhythm used.
    //   - Keys confirmed: Bb major, G major, C major, Eb major, D major (ex.6
    //     had no accidentals -- read as C major/A minor, ambiguous from the
    //     scan). A minor kept in the list as a reasonable estimate per
    //     general AMEB Grade 4 syllabus scope, not directly scan-confirmed.
    //     2026-08-31 correction: this comment previously also listed F major
    //     as an unconfirmed estimate -- wrong. Re-checking the actual scan
    //     page during a full grade-by-grade re-verification, example 1
    //     ("Andantino") clearly has a 1-flat key signature, i.e. F major IS
    //     directly confirmed, same as the other five keys.
    //   - Confirmed time sigs: 4/4, 3/4, 2/2.
    //   - NOT modeled (deferred): example 6 ("Tempo comodo") has accented,
    //     syncopation-flavored eighth-note groupings (">" accents on
    //     repeated notes) -- accent marks and true syncopation are left for
    //     a later grade where they're more central to the texture (Grade 6
    //     per the earlier high-level read).
    //
    // 2026-09-07: RECALIBRATED against a much bigger source -- 13 examples
    // (SR G4.pdf, AMEB pages 20-25) that SUPERSEDES the 6-example 2026-08
    // scan above. Findings:
    //   - Bar length: every one of the 13 examples is exactly 8 bars (two
    //     4-bar systems) -- narrowed from the old placeholder [8,11] range,
    //     same tightening Grade 3 got from its own bigger re-scan.
    //   - Keys, all 13 read directly: Bb major x2 (ex.1, 6), Ab major x1
    //     (ex.2 -- NEW, added to the KEYS table), E major x2 (ex.3, 4 --
    //     NEW, added to KEYS), A major x2 (ex.5, 8), Eb major x1 (ex.7), D
    //     major x1 (ex.9), G major x2 (ex.10, 12), F major x1 (ex.13).
    //     Neither C major nor A minor showed up anywhere in this set (the
    //     old scan's C-major/A-minor read was itself flagged ambiguous) --
    //     replaces the old key list entirely rather than merging, same
    //     supersede approach as Grade 3's key-list rewrite.
    //   - NEW time signature: 6/8, in 3 of 13 examples (ex.4, 7, 9) --
    //     already had a TIME_SIG_UNITS/BEAT_UNITS entry from other grades,
    //     just missing from this bucket's timeSigs.
    //   - Sixteenth notes DO appear here after all (ex.12 "Allegretto" has
    //     plain sixteenth-note runs, ex.9 "Sweetly" has dotted-eighth+
    //     sixteenth pairs) -- the old scan's "no sixteenths" finding doesn't
    //     hold up against the bigger sample; added back to noteValues.
    //   - Dynamics seen: mp, p, mf, f, pp -- f and pp are new (old pool was
    //     mp/mf/p only).
    //   - Tempo/character words, all 13 read directly: Moderato (ex.1, 10),
    //     Daintily (ex.2), Andante (ex.3, 6, 11), "Not too fast" (ex.4),
    //     Cheekily (ex.5), Cantabile (ex.7), Dolce (ex.8), Sweetly (ex.9),
    //     Allegretto (ex.12), Legato (ex.13). NONE of the old pool's six
    //     words (Andantino, Minuet tempo, Allegro, Waltz time, Tempo
    //     comodo) appear anywhere in this set except "Moderato" -- replaces
    //     the old pool entirely. tempoFormRules below is left in place for
    //     'Minuet tempo'/'Waltz time' in case a future scan brings those
    //     words back, but is effectively dormant now that neither word is
    //     in the active pool.
    //   - ex.1 ("Moderato", titled "Waltz" above the system) IS a genuine
    //     waltz -- 3/4 with a clear oom-pah-pah LH -- just under a
    //     "Moderato" tempo word rather than "Waltz time", so the existing
    //     tempoFormRules hook can't catch it. Folded 'waltzOomPah' into
    //     mixedStylePool instead, at low weight, so the texture still shows
    //     up sometimes without being tied to one specific word.
    //   - ex.3 is explicitly titled "Canon" and its LH echoes the RH exactly
    //     like Grade 3's canonImitation device -- added to mixedStylePool.
    //   - NOT modeled (deferred, higher engine cost than this pass covers):
    //     ex.6 ("Bass arioso") carries the melody in the LEFT hand with
    //     both staves in bass clef -- a genuinely different clef/register
    //     layout the engine doesn't support. ex.10 ("Echoes") alternates
    //     f/p across several short phrases rather than once at the start or
    //     mid-piece. ex.11 uses an unusual 4/2-look meter alongside chordal
    //     writing. ex.13 has a bracketed triplet (still no tuplet support,
    //     same known gap as Grade 3). Flagging all four rather than
    //     guessing at implementations.
    label: 'Grade 4',
    bars: [8, 8],
    noteValues: ['quarter', 'half', 'eighth', 'dottedQuarter', 'dottedEighth', 'sixteenth'],
    // 2026-09-09: direct feedback with a real book photo (an "Andante" cut-
    // time example built almost entirely from half notes, dotted-half, and
    // whole notes, with the bass moving in plain quarters -- no eighths,
    // dotted-eighths, or sixteenths anywhere) -- cut time's rhythmic
    // vocabulary in this book reads much simpler/sparser than 4/4's does,
    // matching how a half-note-felt beat is usually written (longer note
    // values relative to the beat, not the same busy 8th/16th mix). See
    // index.js's `rhythmNoteValues` -- this only swaps the vocabulary used
    // for RHYTHM GENERATION when timeSig is exactly '2/2'; every other
    // timeSig in this grade keeps the noteValues list above untouched.
    timeSigNoteValues: {
      '2/2': ['quarter', 'half', 'dottedHalf', 'whole'],
      // 2026-09-09 revision: "quaver랑 crotchet, dotted crotchet이 주고 간간히
      // Semiquaver 2개 묶어 나오는거 정도만" -- rhythm.js's COMPOUND_BEAT_PATTERNS
      // now fills 6/8 beats from a curated pool built ONLY from these four
      // durations (quarter is safe here despite not dividing 6 evenly,
      // because the curated patterns place it explicitly at a beat
      // boundary rather than letting the general algorithm's weaker
      // "shorter than one felt beat" rule wave it through anywhere --
      // dottedEighth dropped, since the user's new spec doesn't call for it).
      '6/8': ['eighth', 'sixteenth', 'quarter', 'dottedQuarter'],
      // 2026-09-09: "4분의 2박자, 4분의 3박자, 4분의 4박자는 crotchet, minim, dotted
      // minim이 주이고, 간간히 4semiquaver 한그룹... 정도가 다" -- direct spec:
      // crotchet/minim/dotted-minim should dominate these meters, with only
      // an occasional group of 4 semiquavers (never a bare/odd number of
      // them -- see simpleMeterWeightOverride below, which keeps sixteenth's
      // pick-weight low so it stays rare, and rhythm.js's proof that with
      // eighth/dottedEighth excluded here, a sixteenth run can only ever
      // start on a beat boundary and therefore always closes at exactly 4).
      // Plain eighth and dottedEighth are deliberately NOT in this list --
      // the user's spec doesn't mention quavers at all for these meters,
      // unlike 6/8 above.
      '3/4': ['quarter', 'half', 'dottedHalf', 'sixteenth'],
      '4/4': ['quarter', 'half', 'dottedHalf', 'sixteenth'],
    },
    // 2026-09-09: see timeSigNoteValues['3/4']/['4/4'] above -- keeps
    // sixteenth-note runs genuinely occasional (not a 3rd/4th co-equal
    // duration) by weighting it far below quarter/half/dottedHalf, only for
    // the two simple meters the user's spec targeted. rhythm.js's fillBar
    // merges this over the shared baseWeight table instead of replacing it
    // globally, so every other grade/timeSig is unaffected.
    simpleMeterWeightOverride: { quarter: 3.0, half: 2.2, dottedHalf: 1.4, sixteenth: 0.35 },
    // 2026-09-09: "triplet도 한 두번 나오는 정도" -- opt-in flag read by
    // generateExcerpt's triplet post-process (see index.js). Closes the
    // "still no tuplet support" gap flagged in this bucket's own 2026-09-07
    // scan comment (ex.13's bracketed triplet).
    allowTriplets: true,
    // 2026-09-09: "이 패턴도 넣어줘" -- book photo of the classic "dotted
    // crotchet + quaver" long-short idiom. Excluded outright when '3/4'/'4/4'
    // were narrowed to crotchet/minim/dotted-minim/sixteenth above, but the
    // user wants it back as an occasional idiom (not a co-equal duration --
    // hence a small chance, not a vocabulary entry). See rhythm.js's
    // dottedQuarterEighthChance param: injects the pair atomically so it
    // only ever appears as this exact beat-aligned pair, never as a bare
    // dottedQuarter or eighth.
    dottedQuarterEighthChance: 0.12,
    hands: 'together',
    // 2026-09-14: widened to the full major+minor set within this grade's
    // ceiling (4 sharps, 4 flats).
    keys: [
      'cMajor', 'aMinor', 'gMajor', 'eMinor', 'dMajor', 'bMinor', 'aMajor', 'fsMinor',
      'eMajor', 'csMinor', 'fMajor', 'dMinor', 'bbMajor', 'gMinor', 'ebMajor', 'cMinor',
      'abMajor', 'fMinor',
    ],
    timeSigs: ['4/4', '3/4', '2/2', '6/8'],
    position: { spanScaleDegrees: 8 },
    maxLeapInterval: 5, // up to a 6th
    maxLeapsPerExcerpt: 4,
    stepWeight: 0.63,
    repeatWeight: 0.11,
    leapWeight: 0.26,
    allowContraryMotion: true,
    leftHandStyle: 'mixed',
    // canonImitation and waltzOomPah added 2026-09-07 (see comment above);
    // weighted so together they're a genuine minority (~2/9 slots each get
    // ~1 in 9), matching how rare they are on the actual page (1/13 each).
    //
    // 2026-09-09: rebalanced again -- "왼손반주 좀 느슨하게" (loosen up the left
    // hand accompaniment too), same "비중을 30퍼센트로" feedback as the
    // dottedEighth change above. brokenRootFifth moves at a full quarter-
    // note pulse every beat and canonImitation exactly mirrors whatever
    // rhythm the RH rolled (so a busy melody made the LH equally busy,
    // doubling the visual density) -- those two are this pool's "active"
    // textures. wholeBarRoot (one note per bar) and halfBarRootFifth (two
    // notes per bar) are the "sparse" ones, matching the book's mostly
    // whole/half-note bass. Rebalanced so active textures land around 30%
    // of picks (was ~36%) and sparse ones make up the rest.
    //
    // 2026-09-09 (later same day): "왼손 비중 이정도로 너무 많지 않게" -- another
    // direct pass, after seeing more generated pages against more book
    // photos. Two changes together: (1) brokenRootFifth thinned from 2 slots
    // to 1 (active textures now ~13% instead of ~29%), and (2) bassRestChance
    // below adds genuine SILENCE to sparse bars too -- the book photos this
    // round showed several examples with a fully rest bar in the LH (not
    // just a held whole-bar note), which no style in this pool could
    // previously produce at all.
    //
    // 2026-09-09 (even later): "왼손이... 너무 지그재그 패턴만 보이는데 책에 나온
    // 것처럼 다양하지만 비중 너무 크지 않게" -- correctly diagnosed: with only
    // wholeBarRoot (one held note) and halfBarRootFifth (root-then-fifth, the
    // literal "zigzag" shape) making up ~85% of picks, a whole piece tends to
    // repeat just those two silhouettes over and over. Added two more
    // textures that were already implemented in this file but never in this
    // bucket's pool: 'triadPatternCalm' (root-then-THIRD, same 2-notes-a-bar
    // density as halfBarRootFifth but a visually different shape/color) and
    // a low-weight touch of 'walkingBass' (stepwise diatonic motion toward
    // the next bar's chord -- genuinely different contour, kept rare since
    // its steady quarter-note pulse is busier than the other sparse styles).
    // wholeBarRoot/halfBarRootFifth trimmed to make room so total weight
    // (and therefore average note density) doesn't rise.
    mixedStylePool: [
      'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot',
      'halfBarRootFifth', 'halfBarRootFifth', 'halfBarRootFifth', 'halfBarRootFifth',
      'triadPatternCalm', 'triadPatternCalm', 'triadPatternCalm',
      'walkingBass',
      'brokenRootFifth',
      'canonImitation',
      'waltzOomPah',
    ],
    // 2026-09-09: "왼손 비중 이정도로 너무 많지 않게" -- see bass.js's
    // bassRestChance comment. ~1 in 5 eligible bars (never the final bar,
    // never under canonImitation) plays a genuine full-bar rest instead of
    // its style's usual note(s) -- roughly matching how often the book
    // photos showed a silent LH bar.
    bassRestChance: 0.2,
    // 2026-09-09: "왼손 8분의 6박자에는 Quaver rest도 살짝만 포함해주고, 다른
    // 나머지 박자표에는 Crotchet rest도 포함해줄래" -- opt-in chance (per
    // qualifying bar, see bass.js's bassSmallRestChance handling) of ONE
    // small single-beat rest (an eighth/quaver in 6/8, a quarter/crotchet in
    // every other timeSig this grade uses) standing in for one of the LH's
    // usual pulse notes, distinct from bassRestChance above (whole-bar
    // silence). Kept low ("살짝만" -- just a little) so it reads as an
    // occasional breath, not a habit.
    bassSmallRestChance: 0.12,
    // 2026-09-14: "왼손의 다양성이 아직 부족해... 왼손 음역대가 좀 넓어지지 않나" -- see
    // bass.js's own comment on this param. A modest, grade-appropriate chance
    // (this is the first hands-together grade it's turned on for) of the
    // whole excerpt's LH sitting one octave lower than usual, for real
    // piece-to-piece register variety instead of every excerpt anchoring the
    // LH in the exact same spot.
    bassLowVarietyChance: 0.15,
    dynamics: ['mp', 'mf', 'p', 'f', 'pp'],
    tempoMarkings: ['Moderato', 'Daintily', 'Andante', 'Not too fast', 'Cheekily', 'Cantabile', 'Dolce', 'Sweetly', 'Allegretto', 'Legato'],
    // 2026-09-02: user asked to actually build out the dance/piece-FORM
    // implications of these tempo words, scoped (per user direction) to
    // rhythm/meter characteristics only -- not a full ABA structure -- and
    // to Grade 4 first. Of this grade's 6 markings, only two name a real
    // form with an unambiguous, well-known meter/idiom: a minuet is always
    // in 3/4, and a waltz is always in 3/4 with an oom-pah-pah LH. The other
    // four (Andantino, Allegro, Moderato, Tempo comodo) are generic
    // tempo/mood words with no single meter or accompaniment tied to them,
    // so they're deliberately left out of this map and stay exactly as
    // random as before (see index.js's tempoFormRules handling). Note:
    // the scan comment above records "Allegro" example 3 as confirmed
    // cut time (2/2) specifically -- that's one example, not "Allegro is
    // always 2/2" the way minuet/waltz are unambiguous by definition, so it
    // was NOT added here; worth another look if more Allegro examples turn
    // up. leftHandStyle 'waltzOomPah' is a new bass.js case (root then the
    // 5th twice, i.e. bass-chord-chord).
    tempoFormRules: {
      'Minuet tempo': { timeSig: '3/4' },
      'Waltz time': { timeSig: '3/4', leftHandStyle: 'waltzOomPah' },
    },
    // 2026-09-09: direct user feedback on generated pages ("타이는 대부분 넓은
    // 밀도로 바랑 바로 이어지거나 하면 더 좋을 듯" -- ties would read better if they
    // mostly connected sparsely, directly across a barline), not new book
    // evidence -- same "tune from screenshots" pattern already used for
    // Grade 3's phraseSlurChance/tieAcrossBarChance.
    //   - articulationNoteChance had never been set for this grade, so it
    //     was silently defaulting to 1 (index.js's assembleLilyPond: `const
    //     artChance = articulationNoteChance != null ? articulationNoteChance
    //     : 1`) -- meaning EVERY eligible run of 2+ eighth-or-shorter notes
    //     within a bar was getting the automatic short legato slur (
    //     applySlurs), 100% of the time. That's the "짧은 슬러" the user saw
    //     drawn over nearly every fast run. Thinned to 0.5 so only about
    //     half of eligible runs actually get the drawn slur -- the same
    //     mechanism already used to de-clutter Grade 3's staccato dots.
    //   - tieAcrossBarChance also didn't exist for this grade (no bar-
    //     crossing ties were possible at all). Added at a low 0.1 per-
    //     eligible-boundary chance so a genuine tie across the barline shows
    //     up occasionally, sparsely, rather than never or constantly.
    // 2026-09-09: "전체적으로 책에 나온것 기준으로 쉼표도 슬러 타이 빈도수도 너무 높지 않게
    // 설정해줘" -- another across-the-board thinning pass, same direction as
    // the original 2026-09-09 calibration above (0.5/0.1) but the user's
    // now looked at several more generated pages and wants it lower still.
    // (Mid-melody rests aren't a lever here: this grade's hands:'together'
    // format has no rest-insertion mechanism at all -- see grade5's own
    // "NOT modeled" comment below -- so rest frequency is already at its
    // floor of zero, nothing to thin.)
    articulationNoteChance: 0.35,
    tieAcrossBarChance: 0.07,
    // 2026-09-09: user then sent 4 direct photos of real Grade 4 book pages
    // in reply, pointing out the big picture I'd missed -- most of what
    // reads as "타이" (tie) to the eye on these pages is actually a LONG
    // PHRASE SLUR (LilyPond's separate `\( \)` phrasing-slur symbol),
    // sweeping over an entire system/line at a time (confirmed clearly on
    // the "Echoes" example, which has one continuous slur over every single
    // line), sometimes with a real same-pitch tie nested at its tail end
    // (the short connecting curve visible right at a barline in two of the
    // photos, e.g. dotted-half tied to dotted-half). That's exactly what
    // Grade 3's existing `phraseSlurChance` mechanism already draws (a
    // phrasing slur over each half of the piece, i.e. roughly one system
    // each for this grade's 4+4-bar layout) -- it just had never been
    // turned on for Grade 4. Enabling it here, at a higher rate than Grade
    // 3's already-tuned-down 0.15, since multiple different Grade 4
    // examples across the photos show it (not a rare accent the way it was
    // for Grade 3).
    // 2026-09-09: thinned 0.4 -> 0.25 alongside the articulation/tie changes
    // above, same "책 기준으로 너무 높지 않게" feedback.
    phraseSlurChance: 0.25,
  },
  grade5: {
    // 2026-09-11: SECOND follow-up pass, direct user review ("Waltz, canon,
    // romanze, sarabande, hymn, gigue, march, corrente 이런 스타일이
    // 추가된것, 더블샵도 보이고, 4성부 3성부도 보인다") on top of the
    // 2026-09-10 recalibration below. Two real engine changes, not just
    // parameter tuning:
    //   - scales.js now builds every minor key as HARMONIC minor (raised
    //     7th/leading-tone degree, correctly re-spelled including double
    //     sharps) instead of plain natural minor -- this is what makes G#
    //     minor's leading tone spell as F double-sharp (Fx) like the book
    //     shows, and gives every minor-key V chord a real dominant pull
    //     instead of a weak minor-v. Global fix (scales.js is shared by
    //     every grade), not grade5-only, but grade5 is where minor keys
    //     with 2+ sharps first appear so it's most visible here.
    //   - The 8 named dance/piece-form styles are now wired to a real
    //     meter+LH-idiom via tempoMarkings/tempoFormRules below (same
    //     mechanism Grade 4 introduced), not just cosmetic text -- see the
    //     tempoFormRules comment.
    // "4성부/3성부" (4-part/3-part texture): NOT modeled as genuine
    // independent voice-leading -- this engine's RH stays monophonic and
    // its LH stays a single chosen chord shape, the same architectural gap
    // already flagged at Grade 6 ("the melody generator is monophonic
    // throughout... making it polyphonic is a real architecture change").
    // 'Hymn' below gets as close as this engine can: a full 3-note LH
    // triad on every beat under a monophonic RH line reads as a dense,
    // chordal, hymn-like texture (up to 4 simultaneous pitches) even though
    // it's not real SATB writing. Flagged here rather than silently
    // claimed as "4-part."
    //
    // 2026-09-10: RECALIBRATED against a much bigger source -- 13 examples
    // on SR G5.pdf, superseding the 6-example 2026-08 scan whose findings
    // are kept below for history. This scan confirmed the old bucket's
    // basic shape (keys, timeSigs, LH textures) but surfaced how much MORE
    // is going on in the real book than a parameter-tuning pass can reach:
    //   - RH/LH block chords and double-stops are already common at this
    //     grade, not something that first appears at Grade 6 as the old
    //     Grade 6 comment below assumed -- several of the 13 examples stack
    //     2-3 note chords in one or both hands for a passage at a time.
    //   - Both TRIPLETS and DUPLETS (2-against-3-feeling groupings) appear,
    //     sometimes in the same example -- allowTriplets (Grade 4's
    //     mechanism, see that bucket) is turned on below, but duplets have
    //     no engine mechanism at all (deferred, same class of gap as
    //     mixed-tuplet writing generally).
    //   - Remote/chromatic keys are more common than the old 6-example scan
    //     suggested: confirmed signatures up to 5 sharps/flats, including
    //     F# minor, C# minor, G# minor, Bb minor, and Db major -- all five
    //     added to gradeParams.js's KEYS table and to `keys` below (none of
    //     the old bucket's 6 keys are dropped; this widens the pool).
    //   - A brief canon/imitation passage confined to ONE clef/hand (the RH
    //     echoes its own previous phrase an octave down, staying in treble
    //     clef throughout) appears in one example -- distinct from
    //     bass.js's existing canonImitation (which always echoes RH into
    //     the LH/bass clef); not modeled, since a same-clef self-echo needs
    //     new melody-generation logic, not just a new bass.js case.
    //   - Light ornamentation (a single grace note or turn ahead of a
    //     cadential note) appears in a couple of examples -- no ornament
    //     support anywhere in this engine; deferred.
    // Calibrated below: widened `keys` (5 new remote keys), turned on
    // allowTriplets (already-built Grade 4 mechanism) and a modest
    // rhRestChance/staccatoChance (already-built Grade 3/4 mechanisms,
    // previously unused here) to reflect the chords-and-rests texture even
    // though true polyphonic chords themselves stay out of scope. Left
    // untouched: bars/position/leap/rhythm-vocabulary ranges, which the new
    // scan didn't contradict.
    //
    // Superseded 2026-08 comment (6-example scan) kept for history:
    // Calibrated against all 6 examples on the AMEB "Fifth Grade" pages
    // (2026-08 scan, pages 8-10). Findings:
    //   - All 6 examples are hands together and continuous, same as Grade 4
    //     -- no alternating device at this grade.
    //   - Compound meters are now a MAJOR feature, not a rarity: 2 of 6
    //     examples use 6/8 (ex.3 "Moderato Pastorale", ex.4 "Gently
    //     rocking") and 1 uses 9/8 (ex.6 "Allegretto", new time sig, added
    //     to TIME_SIG_UNITS). bass.js's pulse-based LH textures now use a
    //     dotted-quarter (6-unit) pulse for compound bars instead of always
    //     forcing a quarter-note pulse, so the broken/arpeggiated LH
    //     patterns actually match the 3-eighths feel in 6/8 and 9/8.
    //   - Dotted "march" rhythm (dotted-eighth + sixteenth pairs) appears in
    //     ex.2 ("Slow march", f non legato) -- sixteenth added back to
    //     noteValues (removed at Grade 4) specifically for this pattern; the
    //     rhythm.js odd/even fix from the Grade 4 pass makes this safe.
    //   - LH textures are noticeably richer than Grade 3-4: compound-meter
    //     arpeggiation (ex.3, ex.4) and syncopated chordal support (ex.5,
    //     ex.6), beyond the plain root/fifth/broken patterns 'mixed' picks
    //     from by default. Added params.mixedStylePool so a bucket can widen
    //     the 'mixed' leftHandStyle's pool -- Grade 5 adds 'triadPattern'
    //     (the root-fifth-third-fifth arpeggiation) alongside the existing
    //     halfBarRootFifth/brokenRootFifth options.
    //   - Confirmed keys: A major, Eb major, D major, E minor (ex.4's flat
    //     key read as Bb major, less certain from the scan quality).
    //     2026-08-31: also naming ex.6 ("Allegretto", 9/8) explicitly here --
    //     its 1-sharp signature is G major, which is where 'gMajor' in this
    //     bucket's keys list actually comes from (previously in the array
    //     but never named in this comment; re-verified against the scan
    //     during a full grade-by-grade re-check and confirmed correct).
    //   - Confirmed time sigs: 3/4, 4/4, 6/8, 2/4, 9/8.
    //   - Bar counts are hard to compare directly across this sample since
    //     shorter-bar meters (2/4) naturally need more bars for the same
    //     musical length (ex.5 ran to ~15 short bars) while compound-meter
    //     examples stayed around 7-8 bars -- bars range widened accordingly
    //     rather than picked from a single example.
    //   - NOT modeled (deferred, bigger engine changes): ex.1 is heavily
    //     chromatic (near-constant accidentals outside the diatonic scale --
    //     melody.js only ever walks in-key); ex.3/ex.4 use mid-piece dynamic
    //     changes and hairpins (<, dim., più f) where this engine only ever
    //     places one dynamic at the very start; ex.5/ex.6 use accents,
    //     staccato dots, and genuine syncopation/off-beat rests within the
    //     "hands together" texture, which the current rhythm generator
    //     can't insert (it only ever fills a bar with sounding notes, never
    //     a mid-melody rest, outside the alternating-hands device). Flagging
    //     all three as known gaps rather than guessing at partial fixes.
    label: 'Grade 5',
    bars: [7, 15],
    noteValues: ['quarter', 'half', 'eighth', 'dottedQuarter', 'dottedEighth', 'sixteenth'],
    hands: 'together',
    // 2026-09-10: widened with 5 remote keys confirmed in the fresh 13-example
    // scan -- see the bucket-level comment above. Old 6 keys kept as-is.
    // 2026-09-14: widened to the full major+minor set within this grade's
    // ceiling (5 sharps, 5 flats).
    keys: [
      'cMajor', 'aMinor', 'gMajor', 'eMinor', 'dMajor', 'bMinor', 'aMajor', 'fsMinor',
      'eMajor', 'csMinor', 'bMajor', 'gsMinor', 'fMajor', 'dMinor', 'bbMajor', 'gMinor',
      'ebMajor', 'cMinor', 'abMajor', 'fMinor', 'dbMajor', 'bbMinor',
    ],
    timeSigs: ['4/4', '3/4', '2/4', '6/8', '9/8'],
    position: { spanScaleDegrees: 9 },
    maxLeapInterval: 6, // up to a 6th
    maxLeapsPerExcerpt: 5,
    stepWeight: 0.6,
    repeatWeight: 0.1,
    leapWeight: 0.3,
    allowContraryMotion: true,
    allowTies: true,
    // 2026-09-11 (third pass): bucket-LEVEL default, not just a per-style
    // one -- the beat-alignment-cascade fix (see the 'Waltz' tempoFormRule
    // comment below for the full mechanical explanation) had only ever been
    // added to each NAMED style's own `rh` block, one at a time, as each got
    // separately screenshotted. That left every plain tempo-word marking
    // with NO tempoFormRule.rh at all (e.g. 'Allegretto', 'Moderato,
    // flowing', 'Not fast but sharp') falling through to rhythm.js's own
    // un-tuned baseWeight table whenever it landed in 3/4 or 4/4 -- still
    // exposed to the exact same cascade. Setting it here, at the bucket
    // level, means it's the DEFAULT every style inherits unless its own
    // `rh` block overrides it (index.js's `rhParams = {...params,
    // ...tempoFormRule.rh}` merge already does this correctly) -- so no
    // style, named or plain, can silently miss this fix again.
    simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
    leftHandStyle: 'mixed',
    // 2026-09-11: 'canonImitation' added -- see the tempoMarkings/
    // tempoFormRules comment below (Grade 5's book review named "Canon" as
    // a real style seen in the source). It was already a proven mechanism
    // (Grade 3/6/8 all draw from it) but hadn't been offered at Grade 5.
    // 2026-09-14: RE-TALLIED against the actual SR G5.pdf scan page-by-page
    // (13 examples) at Sohyun's request ("텍스쳐도 책보고 분석해서 그레이드마다
    // 각각 적용해줘"). Excluding the 8 examples already wired to their own
    // named tempoFormRule (Waltz/Canon/Romanze/Sarabande/Hymn/Gigue/March/
    // Corrente), the remaining 5 GENERIC-tempo examples' actual LH textures
    // are: ex.2 ("With vigour", F# minor) and ex.7 ("Not too fast", C#
    // minor) both hold a single sustained chord per bar or half-bar --
    // wholeBarRoot; ex.3 ("Allegretto", G# minor, 3/8) and the untitled
    // ex.13 (Eb major, 6/8) both arpeggiate a chorded dotted-quarter pulse
    // -- triadPattern; ex.5 ("Andante, Walking pace", G minor) is a genuine
    // continuous stepwise bass line -- walkingBass (the tempo word itself
    // says "walking"). That's 2 wholeBarRoot : 2 triadPattern : 1
    // walkingBass, and NEITHER halfBarRootFifth's nor brokenRootFifth's
    // "boom-chick" zigzag actually appears in any of the 5 -- both dropped
    // in favour of the textures the page really shows. canonImitation also
    // dropped from this generic pool (it stays exclusive to the dedicated
    // 'Canon' tempoFormRule below, matching that it never showed up
    // OUTSIDE the one example literally titled "Canon").
    mixedStylePool: ['wholeBarRoot', 'wholeBarRoot', 'triadPattern', 'triadPattern', 'walkingBass'],
    // 2026-09-14: see bass.js's bassLowVarietyChance comment and grade4's
    // matching entry above -- a touch higher here than grade4's 0.15 since
    // Grade 5's LH textures (triadPattern in particular) are already richer
    // and can comfortably carry a lower register some of the time.
    bassLowVarietyChance: 0.2,
    dynamics: ['mp', 'mf', 'f', 'p'],
    // 2026-09-11: widened with 8 dance/piece-form names the Grade 5 book
    // review flagged as visibly present in the source ("Waltz, canon,
    // romanze, sarabande, hymn, gigue, march, corrente 이런 스타일이
    // 추가된것") -- each is wired to a real timeSig+leftHandStyle via
    // tempoFormRules below, same mechanism Grade 4 introduced for "Waltz
    // time"/"Minuet tempo", rather than staying purely cosmetic text. The
    // pre-existing 6 markings (Moderato flowing / Slow march / Moderato
    // Pastorale / Gently rocking / Not fast but sharp / Allegretto) are
    // kept exactly as before -- this only adds to the pool.
    // 2026-09-14: "그레이드 5,6,7은 스타일 추가되잖아, 다 체크해서 책에나온건
    // 최소한으로 넣고 다른 관련성 있는 스타일도 넣었으면해" -- the 8 names above
    // already ARE the book-confirmed minimum, so nothing to add on that side.
    // Added 2 more relevant forms not already covered by Grade 6/7's new
    // sets (see those buckets' own 2026-09-14 comments): 'Siciliana' (the
    // only named form using this bucket's own 9/8 meter, which nothing else
    // here uses) and 'Bourrée', distinct from 'Slow march' despite sharing
    // 2/4 -- see tempoFormRules below for how.
    tempoMarkings: [
      'Moderato, flowing', 'Slow march', 'Moderato Pastorale', 'Gently rocking',
      'Not fast but sharp', 'Allegretto',
      'Waltz', 'Canon', 'Romanze', 'Sarabande', 'Hymn', 'Gigue', 'March', 'Corrente',
      'Siciliana', 'Bourrée',
    ],
    // 2026-09-10: reuses Grade 4's already-built triplet post-process (see
    // that bucket's own allowTriplets comment) -- the fresh scan confirmed
    // triplets appear here too, not just from Grade 4 on. Duplets (the
    // other tuplet shape seen in the same scan) have no engine mechanism at
    // all and are NOT modeled -- see the bucket-level comment above.
    allowTriplets: true,
    // 2026-09-10: modest rest/staccato -- reuses the Grade 3/4 mechanisms
    // (rhRestChance/rhWholeBarRestChance/staccatoChance, all already wired
    // for any hands:'together' bucket, see index.js) which this bucket never
    // turned on before. Kept low: these stand in for the "occasional rest or
    // detached note" flavor of the real page's busier passages, not for the
    // chords/double-stops themselves, which stay out of scope (see comment
    // above).
    rhRestChance: 0.1,
    rhWholeBarRestChance: 0.05,
    staccatoChance: 0.15,
    lhStaccatoWithRhChance: 0.3,
    // 2026-09-11 (third pass): BUG, not a tuning choice -- this bucket never
    // set articulationNoteChance, and index.js's own fallback for a missing
    // value is `articulationNoteChance != null ? articulationNoteChance : 1`
    // -- i.e. UNSET silently means "100% of eligible notes get a staccato
    // dot" whenever rhStaccato triggers for the piece, not "no extra
    // marking" as the name might suggest. That's exactly the "거의 누르는
    // 족족 스타카토" (near enough every note dotted) over-marking bug
    // index.js's own comment already describes as fixed elsewhere -- it was
    // simply never wired up for Grade 5, so any style here WITHOUT its own
    // `rh.articulationNoteChance` (the plain 'Allegretto'/'Moderato, flowing'
    // etc. markings with no tempoFormRule at all, and several of the 8 new
    // named styles whose `rh` blocks never set this field either) fell all
    // the way back to 1 and dotted literally every quarter-or-longer note --
    // confirmed directly from two screenshots (a 9/8 "Allegretto" and a
    // "March" excerpt) where every single eligible notehead carried a dot.
    // Set to a real per-note probability here so the bucket-wide default
    // is sane for every style that doesn't override it; this is the same
    // 0.35-0.6 range already used at other grades for this field.
    articulationNoteChance: 0.4,
    // 2026-09-02: same tempoFormRules idea introduced at Grade 4 (see that
    // bucket's comment), now extended here per user request to keep going
    // grade by grade, informed by general music-form research (marches,
    // pastorales) cross-checked against what this bucket's own scan
    // comment above already confirmed, rather than overriding it:
    //   - 'Slow march': marches are fundamentally simple DUPLE meter (2/4
    //     or 4/4) -- 3/4 or a compound meter would never read as a march.
    //     2/4 is already in this bucket's confirmed timeSigs pool, so
    //     forcing it here doesn't add an unconfirmed meter, just removes
    //     the chance of this specific excerpt accidentally landing in 3/4
    //     or 6/8, which would contradict its own tempo marking. Paired with
    //     leftHandStyle 'brokenRootFifth' (root-fifth alternating on every
    //     beat) for the steady on-the-beat "boom-chick" march feel --
    //     'triadPattern' or 'halfBarRootFifth' both read too soft/static
    //     for a march.
    //   - 'Moderato Pastorale' / 'Gently rocking': the comment above already
    //     scan-confirms BOTH of these exact examples (ex.3, ex.4) as 6/8,
    //     so timeSig here is a direct restatement of that finding, not a
    //     new guess -- it just makes sure these two specific markings can
    //     never land anywhere else. leftHandStyle 'triadPattern' likewise
    //     restates the same comment's "compound-meter arpeggiation (ex.3,
    //     ex.4)" finding for these two examples specifically.
    //   - The other three markings (Moderato flowing / Not fast but sharp /
    //     Allegretto) are generic tempo words with no single meter tied to
    //     them, left untouched as before.
    // 2026-09-11: the 8 new style markings above, each tied to the meter +
    // LH idiom that actually makes it read as that dance/piece form rather
    // than generic text (same reasoning as the 3 existing rules just above
    // -- a "Waltz" that lands in 4/4 doesn't read as a waltz):
    //   - 'Waltz': the classic oom-pah-pah, 3/4 only (same device Grade 4's
    //     "Waltz time" already uses).
    //   - 'March': duple meter is non-negotiable for a march -- paired with
    //     'brokenRootFifth' for the steady on-the-beat "boom-chick" feel,
    //     same idiom as 'Slow march' just at a normal (4/4, not 2/4) pace,
    //     so the two markings read as related but distinct.
    //   - 'Canon': imitation between the hands is the entire point of a
    //     canon, regardless of meter -- leftHandStyle only, timeSig stays
    //     whatever the excerpt would otherwise draw from the grade's own
    //     pool. Uses the same canonImitation mechanism now also in this
    //     bucket's mixedStylePool (see above) -- named here so an excerpt
    //     actually marked "Canon" is GUARANTEED to get it, not just
    //     possible.
    //   - 'Romanze': a lyrical, singing character -- paired with the
    //     gentler 'triadPatternCalm' arpeggiation (half the note rate of
    //     plain 'triadPattern') so the LH never competes with a "singing"
    //     RH line, in 4/4 for a flowing, unhurried pulse.
    //   - 'Sarabande': slow triple meter with the stress on beat 2 is what
    //     DEFINES this Baroque dance -- see bass.js's new 'sarabandeStress'
    //     case (added specifically for this marking) for how that's
    //     modeled; 3/4 is not optional here, it's the form.
    //   - 'Hymn': the closest this monophonic-bass engine gets to a real
    //     chorale/hymn texture is 'blockChordsEveryBeat' (full root-third-
    //     fifth triad struck together every beat) -- combined with the RH
    //     melody that's up to 4 simultaneous pitches, which reads as a
    //     hymn's chordal density even though it's NOT genuine independent
    //     4-part (SATB) voice-leading -- true polyphonic voice-leading is
    //     the same class of deferred engine gap already flagged at Grade 6
    //     (see that bucket's "RH chords" comment). 4/4, the standard hymn
    //     meter.
    //   - 'Gigue': a fast, lilting compound-meter Baroque dance -- 6/8 with
    //     the existing arpeggiated 'triadPattern' (its dotted-quarter pulse
    //     already gives the rolling broken-chord feel a gigue wants) rather
    //     than inventing a new style for it.
    //   - 'Corrente': a fast, continuously-running Baroque triple-meter
    //     dance -- paired with 'walkingBass' (continuous diatonic quarter-
    //     note motion) for the sense of perpetual forward motion, in 3/4.
    //     Simplification, documented rather than silently assumed: a real
    //     corrente's bass often runs in continuous EIGHTHS, busier than
    //     this engine's quarter-note walking pulse -- kept at the walking-
    //     bass's normal rate rather than inventing a faster LH pulse, since
    //     this engine's own design principle is the LH should never read
    //     harder than the RH (see this file's header comment).
    tempoFormRules: {
      'Slow march': { timeSig: '2/4', leftHandStyle: 'brokenRootFifth' },
      'Moderato Pastorale': { timeSig: '6/8', leftHandStyle: 'triadPattern' },
      'Gently rocking': { timeSig: '6/8', leftHandStyle: 'triadPattern' },
      // 2026-09-11 follow-up: "스타일에 더 맞으면 좋겠어" -- each rule below now
      // also carries an `rh` block (see index.js's tempoFormRule.rh comment),
      // a partial override of this bucket's own RH params so the melody
      // itself, not just the LH accompaniment, reads as its named style.
      // Every value stays within knobs this grade already tunes elsewhere
      // (stepWeight/repeatWeight/leapWeight, allowTriplets, staccatoChance,
      // rest/slur/tie chances, the simple-meter duration-weight table) and
      // this grade's own confirmed noteValues -- no new note value or
      // technique is introduced for any single style.
      'Waltz': {
        timeSig: '3/4', leftHandStyle: 'waltzOomPah',
        // A singing, legato waltz tune: mostly stepwise, phrase-slurred,
        // no staccato/triplets to muddy the lilting 3/4 flow.
        // 2026-09-11: phraseSlurChance/tieAcrossBarChance pulled back down
        // (were 0.5/0.15) -- see the "당김음" note on 'March' below. At the
        // old values, the same big slur-into-a-leap shape was landing in
        // roughly half of every Waltz excerpt generated, which reads as
        // that ONE gesture being the style's whole personality rather than
        // an occasional expressive touch.
        // 2026-09-11 (THIRD pass, applied to every 3/4-or-4/4 style at
        // once): "corrente 이런곳에는 고쳐졌는데 romanze에서 계속 보이네
        // 전체적용을 해줘야지... 계속 같은 걸로 몇 번 말하게 하지 말아줘" --
        // direct, and fair, feedback that the beat-alignment-cascade fix
        // (see Sarabande's comment below for the full mechanical
        // explanation: a beat that opens with a short note forces the rest
        // of that beat short too, since a beat-or-longer duration can only
        // START on a beat boundary) had only been applied one style at a
        // time as each one got separately screenshotted, instead of once to
        // every style sharing the exact same underlying weight shape. Fixed
        // properly this time: EVERY 3/4-or-4/4 named style's
        // simpleMeterWeightOverride now shares the same target shape already
        // proven out on March/Corrente (quarter/half raised to plurality,
        // eighth/sixteenth/dottedEighth pushed down near the floor) --
        // Waltz, Canon (newly given one -- it had none before, so it fell
        // through to no override at all whenever it landed in 3/4/4/4), and
        // Romanze below. Sarabande keeps its own even-more-extreme values
        // (near-zero short notes fits that dance specifically) and March
        // keeps slightly more dottedEighth/sixteenth than the others
        // (its dotted-rhythm character genuinely needs some) -- both left
        // as already tuned, not touched again.
        rh: {
          stepWeight: 0.72, repeatWeight: 0.08, leapWeight: 0.15,
          allowTriplets: false, staccatoChance: 0, rhRestChance: 0.03,
          phraseSlurChance: 0.28, tieAcrossBarChance: 0.08,
          simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
        },
      },
      'March': {
        // 2026-09-14: leftHandStyle corrected 'brokenRootFifth' ->
        // 'halfBarRootFifth' against the actual scan page (ex.11, "Tempo di
        // marcia") -- its LH is sustained half-note/dotted-half chords, not
        // an alternating on-the-beat zigzag. 'brokenRootFifth' was a generic
        // march-convention guess made before this page was checked directly;
        // the RH's own staccato/no-legato treatment below still carries the
        // crisp march character, so this only changes the LH accompaniment.
        timeSig: '4/4', leftHandStyle: 'halfBarRootFifth',
        // Crisp, detached, on-the-beat march character: staccato turned
        // WAY up (opposite of every lyrical style below), no legato
        // slurs/ties, near-continuous (a march doesn't pause).
        // 2026-09-11: "당김음이 압도적으로 많이" -- direct report (with a
        // screenshot of a beamed run leaping up into an accidental) that
        // one rhythmic shape was showing up in nearly every bar and reading
        // as an overused "pushed"/syncopated feel. Root cause: dottedEighth
        // and sixteenth were BOTH weighted at 1.6 -- more than 5x
        // rhythm.js's own baseline weight for dottedEighth (0.3) -- so the
        // dotted-eighth+sixteenth "long-short" figure that creates exactly
        // that pushed feeling was winning the weighted pick almost every
        // time a short note was called for, instead of being one flavor
        // among several. Brought back down closer to a normal spread --
        // the march's dotted-rhythm character still comes through (these
        // values are still well above rhythm.js's 0.3/1.4 baseline), it just
        // no longer dominates literally every bar. Quarter raised to be the
        // clear plurality, matching a march's actual steady-footfall feel.
        // 2026-09-11 (again): "아직도... 비중이 많아서 최소로" -- named alongside
        // Sarabande in the same follow-up report. Same mechanical cascade
        // issue as Sarabande's own comment below (a beat that happens to
        // open with a short note forces the rest of that beat short too,
        // since longer durations can't start off-beat) -- eighth pulled
        // down further so a beat opens with one much less often. Kept
        // higher than Sarabande's, though, since a march's dotted-rhythm
        // character genuinely depends on SOME dottedEighth/sixteenth
        // presence -- reducing it to Sarabande's near-zero level would
        // erase the style entirely, not just its overuse.
        rh: {
          allowTriplets: false, staccatoChance: 0.5, rhRestChance: 0.02,
          phraseSlurChance: 0, tieAcrossBarChance: 0,
          simpleMeterWeightOverride: { quarter: 2.6, dottedEighth: 0.5, sixteenth: 0.5, eighth: 0.9, half: 1.1, dottedHalf: 0.55 },
        },
      },
      'Canon': {
        leftHandStyle: 'canonImitation',
        // A canon's whole point is a clean, recognizable phrase the LH can
        // echo a bar later -- keep the RH simple and mostly stepwise
        // (nothing the ear loses track of before the echo lands) and skip
        // triplets (canonImitation already collapses a triplet's 3 notes to
        // one plain quarter when echoing, so avoiding them in the first
        // place keeps the echo an exact, not approximate, copy).
        // 2026-09-11 (third pass): given the same simpleMeterWeightOverride
        // as every other 3/4-or-4/4 style below (see Waltz's comment above)
        // -- Canon previously had NONE at all, so whenever it happened to
        // land in 3/4 or 4/4 (its timeSig is unset, drawn from the grade's
        // whole pool) it got no cascade protection whatsoever.
        rh: {
          stepWeight: 0.68, repeatWeight: 0.08, leapWeight: 0.24, allowTriplets: false,
          simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
        },
      },
      'Romanze': {
        timeSig: '4/4', leftHandStyle: 'triadPatternCalm',
        // Lyrical, singing "Romance" character: strongly stepwise, long
        // slurred phrases, zero staccato -- the melodic mirror of the LH's
        // already-calm arpeggiation.
        // 2026-09-11: phraseSlurChance/tieAcrossBarChance pulled back (were
        // 0.6/0.2) -- same "당김음" overuse fix as 'Waltz'/'March' above.
        // 2026-09-11 (third pass): eighth/sixteenth/dottedEighth pushed down
        // to the same shared target as every other style -- see Waltz's
        // comment above ("corrente에는 고쳐졌는데 romanze에서 계속 보이네").
        rh: {
          stepWeight: 0.75, repeatWeight: 0.05, leapWeight: 0.15,
          allowTriplets: false, staccatoChance: 0, rhRestChance: 0.03,
          phraseSlurChance: 0.32, tieAcrossBarChance: 0.1,
          simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
        },
      },
      'Sarabande': {
        timeSig: '3/4', leftHandStyle: 'sarabandeStress',
        // Slow and weighty, favoring sustained half/dotted-half values over
        // busy short notes, tied through the beat-2 stress the LH already
        // creates (see bass.js's sarabandeStress) -- a fast, note-heavy
        // melody here would fight the dance's whole character.
        // 2026-09-11: phraseSlurChance/tieAcrossBarChance pulled back (were
        // 0.55/0.25) -- same "당김음" overuse fix as the other styles above;
        // the long half/dotted-half notes this style already favors were
        // ALSO the exact durations tieAcrossBarChance's gate requires
        // (half-note-or-longer), so the two features compounded, making a
        // tied "breath" across the barline show up unusually often.
        // 2026-09-11 (again): "아직도... 이 박자들 비중이 많아서 최소로" -- still
        // too many short-note runs even after the first pullback above.
        // Root cause is mechanical, not just a weight-tuning miss: half/
        // dottedHalf/quarter are all "beat-or-longer" durations, which
        // rhythm.js only allows to START on an actual beat boundary (see
        // fillBar's own comment) -- so the INSTANT the very first pick
        // within a beat happens to be an eighth (even at a modest weight),
        // every long duration becomes illegal for the rest of that beat
        // (they can't start off-beat), forcing a cascade of more short
        // notes just to reach the next beat boundary. eighth's old weight
        // (1.0) was low relative to the long durations but still high
        // enough to trigger that cascade fairly often. Pushed eighth/
        // sixteenth/dottedEighth down much further (near the floor) so a
        // beat essentially only opens with a short note by rare chance --
        // this is the only lever that actually prevents the cascade, since
        // the existing hard cap in rhythm.js (max 4 plain short notes in a
        // row) still permits what the screenshot showed.
        rh: {
          stepWeight: 0.65, repeatWeight: 0.1, leapWeight: 0.2,
          allowTriplets: false, staccatoChance: 0, rhRestChance: 0.02,
          phraseSlurChance: 0.3, tieAcrossBarChance: 0.1,
          simpleMeterWeightOverride: { quarter: 1.6, half: 2.2, dottedHalf: 1.8, eighth: 0.35, sixteenth: 0.08, dottedEighth: 0.08 },
        },
      },
      'Hymn': {
        timeSig: '4/4', leftHandStyle: 'blockChordsEveryBeat',
        // Homophonic chorale motion: the RH should move WITH the LH's
        // block chords (mostly quarters/halves, almost no leaps or fast
        // decoration) rather than dancing an independent melodic line over
        // them -- that's what makes struck chords read as a hymn instead of
        // just "a chordal accompaniment under an ordinary tune".
        // 2026-09-11 (third pass): already close to the shared target shape
        // (see Waltz's comment above) -- nudged the rest of the way to
        // match it exactly, for consistency across every style rather than
        // each one drifting slightly differently.
        rh: {
          stepWeight: 0.8, repeatWeight: 0.1, leapWeight: 0.1,
          allowTriplets: false, staccatoChance: 0, rhRestChance: 0, rhWholeBarRestChance: 0,
          phraseSlurChance: 0.2, tieAcrossBarChance: 0.1,
          simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
        },
      },
      'Gigue': {
        timeSig: '6/8', leftHandStyle: 'triadPattern',
        // A gigue's perpetual lilting motion -- mostly stepwise running
        // notes, light slurring, almost never silent. (simpleMeterWeightOverride
        // is 3/4-or-4/4-only -- see index.js -- so 6/8's rhythm still comes
        // from rhythm.js's own curated compound-meter pattern pool; only the
        // pitch-motion/phrasing knobs below actually apply here.)
        // 2026-09-11: phraseSlurChance pulled back (was 0.4) -- same
        // "당김음" overuse fix as the other styles above.
        rh: { stepWeight: 0.7, repeatWeight: 0.05, leapWeight: 0.2, staccatoChance: 0.1, rhRestChance: 0.02, phraseSlurChance: 0.2 },
      },
      'Corrente': {
        timeSig: '3/4', leftHandStyle: 'walkingBass',
        // 2026-09-11 (second pass): user flagged that the SAME beat-
        // alignment-cascade pattern already fixed for Sarabande/March
        // (see those two styles' comments above) was also dominating
        // Corrente -- a whole-bar run of eighths beamed/slurred together,
        // screenshotted directly ("corrente에도 나오네, 이 리듬비중을
        // 전체적으로 확 줄여줘"). Original design intent here was "eighths
        // dominate" (continuously-running Baroque motion) -- that intent is
        // what's being walked back: eighth/sixteenth/dottedEighth weights
        // pushed down hard (same lever as Sarabande/March, since raising a
        // beat with a short note forces the rest of that beat short too)
        // and quarter/half raised to take over as the plurality durations,
        // so Corrente still has SOME running-eighths flavor but no longer
        // reads as continuous quaver motion bar after bar.
        // Beam grouping was separately re-verified after this change --
        // forceQuaverBeamPairs (index.js) groups strictly per-beat
        // regardless of these weights, so pairs of eighths within a beat
        // still beam correctly together and never straddle a beat
        // boundary; nothing here needed changing for that.
        rh: {
          stepWeight: 0.78, repeatWeight: 0.04, leapWeight: 0.15,
          allowTriplets: false, staccatoChance: 0.05, rhRestChance: 0.01, rhWholeBarRestChance: 0,
          phraseSlurChance: 0.12,
          simpleMeterWeightOverride: { quarter: 2.4, eighth: 0.75, sixteenth: 0.2, half: 1.4, dottedHalf: 0.5, dottedEighth: 0.15 },
        },
      },
      // 2026-09-14: two more relevant forms (see the tempoMarkings comment
      // above) --
      //   - 'Siciliana': a slow, lilting pastoral dance in a gently
      //     dotted/lilting compound meter -- this bucket's own 9/8 (used by
      //     nothing else here) fits its lilting long-short-short compound
      //     pulse better than 6/8, paired with the calm 'triadPatternCalm'
      //     arpeggiation for its wistful, unhurried character.
      //   - 'Bourrée': a brisk, upbeat-driven Baroque duple dance -- 2/4,
      //     'halfBarRootFifth' (sustained root/fifth every half bar) rather
      //     than 'Slow march''s on-the-beat 'brokenRootFifth', with the RH
      //     pushed toward quick continuous stepwise motion so it reads as
      //     lively/dancing rather than a march's steady tread.
      'Siciliana': {
        timeSig: '9/8', leftHandStyle: 'triadPatternCalm',
        rh: { stepWeight: 0.72, repeatWeight: 0.08, leapWeight: 0.16, staccatoChance: 0, rhRestChance: 0.02, phraseSlurChance: 0.3 },
      },
      // Note: no simpleMeterWeightOverride here -- that knob only takes
      // effect at 3/4/4/4 (see index.js's rhythmWeightOverrides), so it
      // would be dead weight at 2/4 (same reason 'Slow march' above never
      // set one either).
      'Bourrée': {
        timeSig: '2/4', leftHandStyle: 'halfBarRootFifth',
        rh: {
          stepWeight: 0.74, repeatWeight: 0.06, leapWeight: 0.18,
          allowTriplets: false, staccatoChance: 0.15, rhRestChance: 0.02,
          phraseSlurChance: 0.1, tieAcrossBarChance: 0,
        },
      },
    },
  },
  grade6: {
    // 2026-09-10: RECALIBRATED against a much bigger source -- 12 examples
    // on SR G6.pdf, superseding the 6-example 2026-08 scan below (kept for
    // history). Confirmed timeSigs match exactly (4/4, 3/4, 2/2, 6/8 -- no
    // new meter to add). New findings from the bigger sample:
    //   - Both TRIPLETS and DUPLETS appear (same pairing as the fresh Grade
    //     5 scan) -- allowTriplets turned on below; duplets stay deferred,
    //     same reasoning as Grade 5.
    //   - Chromaticism is heavier than the old 6-example scan suggested --
    //     several examples lean on secondary-dominant-flavored accidentals
    //     outside the diatonic scale for a phrase at a time. melody.js only
    //     ever walks in-key, so this stays deferred (same class of gap
    //     flagged since Grade 3's chromatic-passing-tone note).
    //   - RH/LH chords and double-stops are, if anything, MORE pervasive
    //     than the old scan's already-flagged finding -- confirms rather
    //     than changes that deferred item.
    //   - A canon+staccato idiom recurs: a short staccato RH phrase
    //     immediately echoed by the LH an octave down. This IS reachable
    //     with existing mechanisms -- bass.js's canonImitation (already in
    //     this bucket's mixedStylePool) plus staccatoChance (not previously
    //     turned on here) -- so staccatoChance is added below rather than
    //     deferred.
    // Keys/bars/range/dynamics/tempo pools below are left as the old scan
    // calibrated them; the fresh scan didn't contradict any of those.
    //
    // Superseded 2026-08 comment (6-example scan) kept for history:
    // Calibrated against all 6 examples on the AMEB "Sixth Grade" pages
    // (2026-08 scan, pages 11-13). Findings:
    //   - All 6 examples hands together and continuous.
    //   - Pieces are noticeably longer -- ex.1 runs ~12 bars, ex.3 ~16,
    //     ex.6 ~20 -- so bars widened well past Grade 5's range.
    //   - Melodic range widens too: arpeggiated figures spanning close to
    //     an octave appear repeatedly, so position span and max leap size
    //     both increased from Grade 5.
    //   - Confirmed time sigs: 3/4 (ex.1), 4/4 (ex.2, ex.4), cut time
    //     (ex.5, "Moderato scherzoso"), 6/8 (ex.6, "Allegretto").
    //   - Confirmed keys: G major (ex.1, ex.2), A major (ex.3), Bb major
    //     (ex.4), F major (ex.6); ex.5's key was hard to pin down from the
    //     scan (heavy chromatic alteration) -- read as G minor, kept as an
    //     estimate. A couple of AMEB-typical minors (D minor) added for
    //     syllabus coverage, not directly scan-confirmed.
    //   - NOT modeled (deferred, MAJOR engine changes, bigger than anything
    //     deferred so far): this is the first grade where the right hand
    //     itself plays genuine CHORDS/double-stops, not a single melodic
    //     line (ex.1, ex.2, ex.3, ex.5 all have stacked-notehead chords in
    //     the RH) -- the melody generator is monophonic throughout this
    //     engine and making it polyphonic is a real architecture change,
    //     not a parameter tweak. Also not modeled: grace-note ornaments
    //     (ex.5), rapid terraced dynamics changing mid-piece (ex.2, f/p
    //     alternating within a few bars), and triplets (ex.4, same gap
    //     flagged at Grade 3). Calibrating everything ELSE (keys, time
    //     sigs, range, bar length, LH texture, tempo/dynamic pools) below
    //     while being upfront that the RH texture itself is simpler than
    //     the real book at this grade.
    label: 'Grade 6',
    bars: [12, 20],
    noteValues: ['quarter', 'half', 'eighth', 'dottedQuarter', 'dottedEighth', 'sixteenth', 'dottedHalf'],
    hands: 'together',
    // 2026-09-14: widened to the full major+minor set within this grade's
    // ceiling (6 sharps, 6 flats) -- the point this grade jumps past grade5
    // is exactly the 6th sharp/flat (F#/Gb major, D#/Eb minor), only
    // reachable now that scales.js can spell them correctly (see its own
    // 2026-09-14 comment).
    keys: [
      'cMajor', 'aMinor', 'gMajor', 'eMinor', 'dMajor', 'bMinor', 'aMajor', 'fsMinor',
      'eMajor', 'csMinor', 'bMajor', 'gsMinor', 'fsMajor', 'dsMinor',
      'fMajor', 'dMinor', 'bbMajor', 'gMinor', 'ebMajor', 'cMinor', 'abMajor', 'fMinor',
      'dbMajor', 'bbMinor', 'gbMajor', 'ebMinor',
    ],
    timeSigs: ['4/4', '3/4', '2/2', '6/8'],
    position: { spanScaleDegrees: 10 },
    maxLeapInterval: 7, // up to an octave-ish
    maxLeapsPerExcerpt: 6,
    stepWeight: 0.57,
    repeatWeight: 0.09,
    leapWeight: 0.34,
    allowContraryMotion: true,
    allowTies: true,
    leftHandStyle: 'mixed',
    // 2026-09-14: RE-TALLIED against the actual SR G6.pdf scan (12
    // examples, page by page) at Sohyun's request ("텍스쳐도 책보고 분석해서
    // 그레이드마다 각각 적용해줘"). Two real findings:
    //   - 'fullTexture' is a NO-OP here -- bass.js's switch has no distinct
    //     'fullTexture' case at all; it falls into the exact same
    //     default/'triadPattern' arpeggiation code (see bass.js's own
    //     2026-09-XX comment on that case). Keeping it in a pool never
    //     added real variety, only an illusion of a 4th option. Dropped.
    //   - Excluding ex.4 ("Canon", already its own tempoFormRule) and ex.5
    //     ("Scherzetto", -> the 'Scherzo' rule), the other 10 examples'
    //     actual LH textures: ex.1/3/8/12 hold sustained chords for a
    //     half-bar or whole bar (wholeBarRoot, 4/10 -- the single most
    //     common texture on the page, and one this pool never offered at
    //     all); ex.6/7/11 play a detached single note against a rest every
    //     beat (brokenRootFifth-with-rest, 3/10); ex.9/10 arpeggiate a
    //     running chorded figure (triadPattern, 2/10, ex.10 is itself
    //     titled "Gigue"); ex.2 is a genuine continuous stepwise bass
    //     (walkingBass, 1/10). Rebuilt the pool to roughly that 4:3:2:1
    //     proportion instead of the old flat 4-way split that was missing
    //     wholeBarRoot -- the actual most common texture -- entirely.
    mixedStylePool: [
      'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot',
      'brokenRootFifth', 'brokenRootFifth', 'brokenRootFifth',
      'triadPattern', 'triadPattern',
      'walkingBass',
    ],
    // 2026-09-14: see bass.js's bassLowVarietyChance comment and grade4/5's
    // matching entries above.
    bassLowVarietyChance: 0.25,
    dynamics: ['p', 'mp', 'mf', 'f'],
    // 2026-09-14: "그레이드 5,6,7은 스타일 추가되잖아, 다 체크해서 책에나온건
    // 최소한으로 넣고 다른 관련성 있는 스타일도 넣었으면해" -- audited this
    // bucket's own scan comments above: only 'Moderato scherzoso' (ex.5) and
    // 'Allegretto' (ex.6) are actually named IN the source scan; 'Valse
    // lente'/'Risoluto'/'Flowing'/'Moderato grazioso' were generic tempo/mood
    // words added earlier for pool variety, not scan citations -- kept as-is
    // (still plausible AMEB tempo words, just not form-specific) rather than
    // removed, since the ask is to ADD coverage, not delete anything real.
    // Added 5 new named dance/piece-form markings below, one grade harder
    // than Grade 5's set (Waltz/Canon/Romanze/Sarabande/Hymn/Gigue/March/
    // Corrente) so Grade 6 doesn't just repeat Grade 5's forms: Minuet,
    // Scherzo, Nocturne, Barcarolle, Tarantella. Each is wired via
    // tempoFormRules below to a timeSig already in THIS bucket's own
    // confirmed pool (4/4/3/4/2/2/6/8) and a leftHandStyle mechanism that
    // already exists in bass.js (no new engine code) -- same discipline as
    // Grade 5's rules.
    tempoMarkings: [
      'Valse lente', 'Risoluto', 'Flowing', 'Moderato grazioso', 'Moderato scherzoso', 'Allegretto',
      'Minuet', 'Scherzo', 'Nocturne', 'Barcarolle', 'Tarantella',
    ],
    // 2026-09-10: see the bucket-level comment above -- reuses Grade 4/5's
    // triplet mechanism, and turns on staccato (paired with canonImitation,
    // now in mixedStylePool just above) for the canon+staccato idiom the
    // fresh 12-example scan showed recurring.
    allowTriplets: true,
    staccatoChance: 0.15,
    // 2026-09-14: this bucket had staccatoChance turned on (above) but never
    // set articulationNoteChance -- the exact same gap already root-caused
    // and fixed for grade5 (index.js's `articulationNoteChance != null ?
    // articulationNoteChance : 1` silently defaults to 1.0 / 100% of
    // eligible notes marked staccato whenever staccato triggers at all).
    // Found via a proactive audit of every bucket rather than waiting for
    // another over-staccato screenshot. Same 0.4 value used for grade5.
    articulationNoteChance: 0.4,
    lhStaccatoWithRhChance: 0.35,
    // 2026-09-14: same systemic rhythm-weight rebalance already applied to
    // every grade5 style plus a grade5 bucket-level default, per the user's
    // explicit "apply this globally" feedback -- grade6 can land in 3/4 or
    // 4/4 (directly, or via 'Valse lente' below) and had no such protection
    // at all, leaving it exposed to the same overused-rhythm/long-run
    // cascade already fixed everywhere else. Only gates 3/4 and 4/4 (see
    // index.js's rhythmWeightOverrides), same as every other bucket.
    simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
    // 2026-09-02: 'Valse lente' ("slow waltz") is the same 3/4 oom-pah-pah
    // idiom as Grade 4's 'Waltz time' -- just a slower tempo word, not a
    // different form -- so it reuses bass.js's 'waltzOomPah' style rather
    // than inventing a near-duplicate. 3/4 is already scan-confirmed for
    // this bucket (ex.1). The other five markings here are generic
    // tempo/mood words, left untouched.
    // 2026-09-14: the 5 new dance/piece-form markings, each tied to the
    // meter + LH idiom that makes it read as that form rather than generic
    // text (same reasoning as Grade 5's rules above):
    //   - 'Minuet': a courtly, measured triple-meter dance -- more sustained
    //     and elegant than a Waltz's continuous oom-pah, so paired with
    //     'halfBarRootFifth' (root then fifth every HALF bar, not every
    //     beat) instead of reusing 'waltzOomPah'. Mostly stepwise, moderate
    //     phrasing, no staccato.
    //   - 'Scherzo': literally "joke" -- brisk, light, playful triple meter,
    //     the opposite temperament from Minuet in the same meter. Paired
    //     with 'brokenRootFifth' for a quicker, lighter LH pulse; RH raised
    //     staccato/leap, no slurs/ties (nothing sustained about a scherzo).
    //   - 'Nocturne': a lyrical, dreamy night-piece -- gentle arpeggiated LH
    //     ('triadPatternCalm', the same half-rate arpeggiation Grade 5's
    //     Romanze uses) under a singing, mostly-stepwise, heavily-slurred RH
    //     with zero staccato, in 4/4 for an unhurried pulse.
    //   - 'Barcarolle': a gently rocking boat-song, traditionally compound
    //     meter -- 6/8, paired with the same calm 'triadPatternCalm'
    //     arpeggiation as Nocturne (a barcarolle's LH is a lulling swell, not
    //     Gigue's brisker running 'triadPattern'), legato, minimal rest.
    //   - 'Tarantella': a fast, whirling, driving compound-meter dance -- 6/8
    //     with the brisker 'triadPattern' (Gigue's LH), but RH pushed toward
    //     near-continuous stepwise motion with almost no rests/slurs/ties, so
    //     it reads as breathless drive rather than Gigue's lilting flow.
    tempoFormRules: {
      'Valse lente': { timeSig: '3/4', leftHandStyle: 'waltzOomPah' },
      'Minuet': {
        timeSig: '3/4', leftHandStyle: 'halfBarRootFifth',
        rh: {
          stepWeight: 0.72, repeatWeight: 0.1, leapWeight: 0.14,
          allowTriplets: false, staccatoChance: 0, rhRestChance: 0.03,
          phraseSlurChance: 0.25, tieAcrossBarChance: 0.08,
          simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
        },
      },
      'Scherzo': {
        timeSig: '3/4', leftHandStyle: 'brokenRootFifth',
        rh: {
          stepWeight: 0.62, repeatWeight: 0.06, leapWeight: 0.3,
          allowTriplets: false, staccatoChance: 0.5, rhRestChance: 0.05,
          phraseSlurChance: 0, tieAcrossBarChance: 0,
          simpleMeterWeightOverride: { quarter: 2.6, half: 1.1, dottedHalf: 0.5, eighth: 0.9, sixteenth: 0.35, dottedEighth: 0.2 },
        },
      },
      'Nocturne': {
        timeSig: '4/4', leftHandStyle: 'triadPatternCalm',
        rh: {
          stepWeight: 0.76, repeatWeight: 0.05, leapWeight: 0.15,
          allowTriplets: false, staccatoChance: 0, rhRestChance: 0.02,
          phraseSlurChance: 0.35, tieAcrossBarChance: 0.12,
          simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
        },
      },
      'Barcarolle': {
        timeSig: '6/8', leftHandStyle: 'triadPatternCalm',
        rh: { stepWeight: 0.72, repeatWeight: 0.06, leapWeight: 0.18, staccatoChance: 0, rhRestChance: 0.02, phraseSlurChance: 0.3 },
      },
      'Tarantella': {
        timeSig: '6/8', leftHandStyle: 'triadPattern',
        rh: { stepWeight: 0.68, repeatWeight: 0.04, leapWeight: 0.22, staccatoChance: 0.05, rhRestChance: 0.01, rhWholeBarRestChance: 0, phraseSlurChance: 0.05 },
      },
    },
    // 2026-09-14: "Tier A" musical-expressiveness pass (grades 6-8, per
    // Sohyun's "그레이드 6에서 8까지는 최소한 음악적요소가 더 디테일하게
    // 표현되고 언어적으로 들려야하는데 좀더 가미할 수 있을 요소" request,
    // implemented in the "순서대로" (in order) sequence she asked for,
    // starting with Tier A -- see the tiered spec proposed earlier this
    // session: hairpins/accents/tenuto/fermata/sf-subito dynamics/paired
    // mid-piece tempo changes. Hairpins are deferred to a later pass (they
    // need a start+end anchor spanning several notes, closer in shape to
    // the phrase-slur mechanism than a single-note mark -- want to design
    // that properly rather than bolt it on quickly); the other five below
    // are new opt-in per-excerpt toggles, all consumed via rhParams in
    // index.js's generateExcerpt/assembleLilyPond so a tempoFormRule.rh
    // style profile above can still override any of them per-style (none
    // of grade6's own rules above set these, so every named style here
    // just inherits these bucket-level defaults). Values kept modest --
    // these are ADDITIONS meant to occasionally punctuate a piece, not a
    // replacement for the existing staccato/slur/tie/rest mechanisms, so
    // not every excerpt should carry all five at once.
    accentChance: 0.18,
    tenutoChance: 0.15,
    fermataChance: 0.2,
    sfzMidChance: 0.12,
    // 2026-09-14: gated off whenever the plain midPieceMarkings pool
    // already fired for that excerpt (see index.js's generateExcerpt --
    // `!midMarking` guard) so a piece never gets both a single italic
    // marking AND a paired rall./a-tempo pair crowding the same 40-75%
    // window. "Tempo I" (Italian convention: "back to the first tempo",
    // distinct from the more generic "a tempo") mixed in as a second pair
    // option so the pool isn't just one phrase repeated.
    tempoChangePairs: [
      ['rall.', 'a tempo'],
      ['rit.', 'Tempo I'],
      ['poco rall.', 'a tempo'],
    ],
    tempoChangePairChance: 0.15,
    // 2026-09-15: "Tier B" ornamentation, continuing the "순서대로" tier
    // sequence right after Tier A -- grace notes, trills, turns, mordents.
    // ornamentChance is the per-EXCERPT gate (does this piece get any
    // ornamentation at all); ornamentNoteChance is the per-ELIGIBLE-note
    // draw chance once that gate is open (kept low -- these are meant to
    // punctuate a couple of notes per piece, not decorate the whole line,
    // same over-marking lesson already learned from Tier A's
    // articulationNoteChance audit). ornamentPool is weighted like
    // mixedStylePool: trill leans heaviest (the single most idiomatic,
    // least visually disruptive ornament at this grade), turn/mordent
    // next, grace notes lightest (the only one requiring a whole extra
    // acciaccatura note printed before the beat, the most visually
    // "busy" of the four).
    ornamentChance: 0.25,
    ornamentNoteChance: 0.08,
    ornamentPool: ['trill', 'trill', 'trill', 'turn', 'turn', 'mordent', 'grace'],
  },
  grade7: {
    // 2026-09-10: RECALIBRATED against a much bigger source -- 13 examples
    // across SR G7.pdf's book pages 36-44 (the file itself has reversed page
    // order and duplicate pages -- deduplicated by the printed "Grade N"
    // header on each page, not by file order; 2 examples that bled into this
    // file actually belong to Grade 8 and were excluded). Supersedes the
    // 5-example 2026-08 scan below (kept for history). New findings:
    //   - Two new time signatures: 5/4 (ex.1 -- brand new to this app, added
    //     to TIME_SIG_UNITS/BEAT_UNITS above) and 2/4 (already
    //     engine-supported, just not previously in this bucket's list). 3/8
    //     also appeared once but is NOT added -- a genuinely odd meter this
    //     engine has never generated before, and unlike 5/4 (a simple
    //     extension of the existing quarter-beat machinery) 3/8 is compound-
    //     ish in a way the engine's COMPOUND_TIME_SIGS/pulse logic has never
    //     been tested against; deferred rather than guessed at.
    //   - One example changes time signature MID-PIECE (4/4 to 3/4 partway
    //     through) -- this engine picks exactly one timeSig per excerpt with
    //     no mechanism for a mid-piece change; deferred, a bigger engine
    //     change than this pass covers.
    //   - Genuine FUGATO/imitative counterpoint (one voice enters, a second
    //     voice imitates it a few beats later, both continuing
    //     independently) appears in one example, titled "Fugato" outright --
    //     categorically different from bass.js's canonImitation (which only
    //     ever echoes a single already-finished bar, not an overlapping
    //     independent line); deferred.
    //   - Full chorale-style chords in both hands recur (confirms, doesn't
    //     change, the old scan's ex.3 "Andante religioso" finding below).
    //   - Cut time (2/2)'s status here is less certain than the old scan
    //     suggested -- kept in timeSigs since it's still represented, but
    //     flagging the uncertainty rather than treating it as fully solid.
    // Calibrated below: widened timeSigs (added 5/4, 2/4), left keys/bars/
    // range/dynamics/tempo pools as the old scan calibrated them since the
    // fresh scan didn't contradict those specifically.
    //
    // Superseded 2026-08 comment (5-example scan) kept for history:
    // Calibrated against all 5 examples on the AMEB "Seventh Grade" pages
    // (2026-08 scan, pages 14-17). This is a bigger difficulty jump than
    // Grade 6: 3 of 5 examples (ex.2, ex.3, ex.5) go well beyond what this
    // engine can generate --
    //   - ex.3 ("Andante religioso") is a full chorale: block CHORDS in
    //     BOTH hands throughout, not melody-plus-accompaniment at all.
    //   - ex.2 and ex.5 both use mid-staff CLEF CHANGES (the LH borrows
    //     treble clef for a high passage, or vice versa) plus extensive
    //     triplets, syncopated rests, and fermatas.
    //   - All 5 examples are far more chromatic than Grade 6.
    // None of that is modeled (same deferred list as Grade 6, plus clef
    // changes and a genuinely chordal-not-accompanied texture, which is a
    // bigger gap than anything flagged so far). Calibration below leans on
    // the two more tractable examples (ex.1 "Allegretto", ex.4 "Tempo di
    // Gavotte" -- both a single flowing melodic line over a simpler LH) for
    // range/rhythm/LH texture, while keys/time-sigs/bar-length draw on all 5
    // where they could be read confidently.
    //   - Confirmed time sigs: 3/2 (ex.1 -- new, added to TIME_SIG_UNITS),
    //     4/4 (ex.2, ex.3), cut time (ex.4), 3/4 (ex.5).
    //   - Confirmed keys: F major (ex.1, ex.2), D major (ex.3), Bb major
    //     (ex.4, estimate); ex.5's key was uncertain from the scan (heavy
    //     chromatic alteration) -- read as A major. A minor kept for
    //     syllabus coverage, not scan-confirmed.
    //   - 2026-08-31: re-checked the scan page during a full grade-by-grade
    //     re-verification -- this bucket's keys list also had 'gMinor' in
    //     it, which is not supported by ANY of the 5 examples (their key
    //     signatures are 1 flat/2 sharps/2 flats/3 sharps/unclear, per the
    //     line above -- none read as G minor's 2 flats with no major-key
    //     match) and wasn't mentioned in this comment at all, unlike A minor
    //     which was always honestly flagged as a syllabus estimate. Removed
    //     as an undocumented leftover rather than a real finding.
    //   - Bar counts ran long across the sample (10-24) -- range widened
    //     again vs. Grade 6, but capped below ex.2's ~24-bar outlier since
    //     that example is also the most atypically virtuosic one being
    //     deferred most heavily.
    label: 'Grade 7',
    bars: [14, 22],
    noteValues: ['quarter', 'half', 'eighth', 'dottedQuarter', 'dottedEighth', 'sixteenth', 'dottedHalf'],
    hands: 'together',
    // 2026-09-14: widened to the full major+minor set within this grade's
    // ceiling (6 sharps, 6 flats -- same ceiling as grade6; the distinction
    // between the two grades lives in rhythm/texture params, not key range).
    keys: [
      'cMajor', 'aMinor', 'gMajor', 'eMinor', 'dMajor', 'bMinor', 'aMajor', 'fsMinor',
      'eMajor', 'csMinor', 'bMajor', 'gsMinor', 'fsMajor', 'dsMinor',
      'fMajor', 'dMinor', 'bbMajor', 'gMinor', 'ebMajor', 'cMinor', 'abMajor', 'fMinor',
      'dbMajor', 'bbMinor', 'gbMajor', 'ebMinor',
    ],
    // 2026-09-10: added 5/4 (brand new) and 2/4 (already engine-supported)
    // per the fresh 13-example scan -- see bucket-level comment above.
    timeSigs: ['4/4', '2/2', '3/2', '3/4', '5/4', '2/4'],
    position: { spanScaleDegrees: 11 },
    maxLeapInterval: 7,
    maxLeapsPerExcerpt: 6,
    stepWeight: 0.56,
    repeatWeight: 0.08,
    leapWeight: 0.36,
    allowContraryMotion: true,
    allowTies: true,
    leftHandStyle: 'mixed',
    // 2026-09-14: RE-TALLIED against the actual SR G7.pdf scan at Sohyun's
    // request ("텍스쳐도 책보고 분석해서 그레이드마다 각각 적용해줘"). Same
    // 'fullTexture' finding as grade6 (it's a no-op duplicate of
    // 'triadPattern' in bass.js -- dropped). Excluding the examples already
    // wired to their own named tempoFormRule ('Minuet', 'Tempo di Gavotte'),
    // the remaining generic-tempo examples' LH textures: 6 of 10 (ex.6
    // "Allegretto", ex.7 "Hymnus", ex.9 "Allegro ma non troppo", ex.10 "The
    // secret", ex.12 "Allegro e ritmico", ex.13 "Unhurried") hold long
    // sustained chords for a half-bar or more -- wholeBarRoot, by far the
    // dominant texture at this grade, and completely missing from the old
    // 3-way pool; ex.1/ex.2 walk in continuous chorded motion -- triadPattern/
    // walkingBass; ex.11 ("Adagio") is a busy running figure with rests --
    // walkingBass; ex.5 ("Valse") is a broken ascending bass -- kept as the
    // one brokenRootFifth-ish slot. Rebuilt to roughly that 6:2:2:1 shape.
    mixedStylePool: [
      'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot', 'wholeBarRoot',
      'triadPattern', 'triadPattern',
      'walkingBass', 'walkingBass',
      'brokenRootFifth',
    ],
    // 2026-09-14: see bass.js's bassLowVarietyChance comment and grade4-6's
    // matching entries above.
    bassLowVarietyChance: 0.3,
    dynamics: ['pp', 'p', 'mp', 'mf', 'f'],
    // 2026-09-14: "그레이드 5,6,7은 스타일 추가되잖아, 다 체크해서 책에나온건
    // 최소한으로 넣고 다른 관련성 있는 스타일도 넣었으면해" -- audited this
    // bucket's own scan comments above: 'Andante religioso' (ex.3), 'Tempo di
    // Gavotte' (ex.4), and 'Allegretto' (ex.1) are the actual scan-confirmed
    // names; 'Moderato' and 'Dreamily' are generic mood/tempo words, not
    // specific scan citations -- kept, not removed (the ask is to add
    // coverage, not delete what's already there). Added 5 new named
    // dance/piece-form markings below, distinct from Grade 5's and Grade 6's
    // sets so no grade just repeats another's forms: Polonaise, Pavane,
    // Rondo, Musette, Toccata. Each timeSig used is already in THIS bucket's
    // own confirmed pool (4/4, 2/2, 3/2, 3/4, 5/4, 2/4) and each leftHandStyle
    // is an existing bass.js mechanism -- same discipline as Grade 5/6.
    tempoMarkings: [
      'Allegretto', 'Moderato', 'Andante religioso', 'Tempo di Gavotte', 'Dreamily',
      'Polonaise', 'Pavane', 'Rondo', 'Musette', 'Toccata',
    ],
    // 2026-09-02: 'Tempo di Gavotte' -- forced to cut time (2/2), which the
    // comment above already scan-confirms specifically for ex.4, the
    // gavotte example. PARTIAL implementation, flagged deliberately: a real
    // gavotte's single most identifying feature (per general music-form
    // research, e.g. Vaia's "Gavotte" entry) is that the phrase starts on a
    // HALF-BAR ANACRUSIS -- an upbeat entering halfway through the bar,
    // with the final bar correspondingly shortened to balance it -- not
    // just its time signature. This engine's rhythm generator only ever
    // fills complete bars from beat 1 (no partial/pickup bar concept
    // anywhere in generateRhythm/assembleLilyPond), so the anacrusis itself
    // is NOT modeled here, same as this bucket's other documented gaps
    // above (chords, clef changes, triplets). Forcing the confirmed meter
    // is a real improvement on its own (a "gavotte" that could previously
    // land in 3/4 or 3/2 was actively wrong) but this is not yet a genuine
    // gavotte rhythm -- worth a real pickup-bar feature later if it's worth
    // the engine change.
    // 2026-09-14: the 5 new dance/piece-form markings, each tied to the
    // meter + LH idiom that makes it read as that form:
    //   - 'Polonaise': a stately Polish triple-meter processional with a
    //     characteristic dotted-rhythm lilt -- 3/4, 'brokenRootFifth' for a
    //     steady on-the-beat LH, RH's dotted-eighth/sixteenth weights raised
    //     (same lever as Grade 5's March) so the dotted character actually
    //     comes through rather than defaulting to plain quarters/halves.
    //   - 'Pavane': a slow, stately duple processional -- cut time (2/2,
    //     already this bucket's own confirmed meter, and where Grade 8's
    //     chorale writing lives too), 'blockChordsEveryBeat' for the
    //     sustained homophonic tread, RH heavily weighted toward long notes
    //     with near-zero staccato/rests (a processional doesn't hurry or
    //     pause). No simpleMeterWeightOverride -- that knob only applies at
    //     3/4/4/4 (see index.js), so 2/2 always draws from rhythm.js's own
    //     pattern pool regardless.
    //   - 'Rondo': a lively, recurring-theme form -- this engine can't
    //     actually repeat a theme, but the bright, energetic CHARACTER a
    //     rondo's main theme has is reachable: 2/4 (brisk, already this
    //     bucket's pool), 'brokenRootFifth', RH biased toward leaps and
    //     lighter staccato touches rather than a smooth singing line.
    //   - 'Musette': a pastoral dance built over a sustained drone bass --
    //     'wholeBarRoot' (a single held root per bar) is the closest this
    //     engine gets to a drone, under a light, dance-like, mostly-stepwise
    //     RH with a little staccato, in 4/4.
    //   - 'Toccata': a fast, continuously-running virtuosic showpiece --
    //     DELIBERATE exception to the "cascade fix" pattern used everywhere
    //     else (which pushes eighth/sixteenth weights DOWN to avoid
    //     over-syncopation): a toccata's whole identity is unbroken fast
    //     motion, so eighth/sixteenth are pushed UP instead, paired with
    //     'walkingBass' for continuous quarter-note drive underneath and
    //     zero rests/slurs/ties (nothing sustained interrupts a toccata).
    tempoFormRules: {
      'Tempo di Gavotte': { timeSig: '2/2' },
      'Polonaise': {
        timeSig: '3/4', leftHandStyle: 'brokenRootFifth',
        rh: {
          stepWeight: 0.62, repeatWeight: 0.08, leapWeight: 0.3,
          allowTriplets: false, staccatoChance: 0.1, rhRestChance: 0.02,
          phraseSlurChance: 0.1, tieAcrossBarChance: 0,
          simpleMeterWeightOverride: { quarter: 2.2, half: 1.1, dottedHalf: 0.5, eighth: 0.9, sixteenth: 0.5, dottedEighth: 0.55 },
        },
      },
      'Pavane': {
        timeSig: '2/2', leftHandStyle: 'blockChordsEveryBeat',
        rh: {
          stepWeight: 0.8, repeatWeight: 0.12, leapWeight: 0.08,
          allowTriplets: false, staccatoChance: 0, rhRestChance: 0, rhWholeBarRestChance: 0,
          phraseSlurChance: 0.25, tieAcrossBarChance: 0.15,
        },
      },
      'Rondo': {
        timeSig: '2/4', leftHandStyle: 'brokenRootFifth',
        rh: { stepWeight: 0.55, repeatWeight: 0.08, leapWeight: 0.37, staccatoChance: 0.25, rhRestChance: 0.03, phraseSlurChance: 0.05 },
      },
      'Musette': {
        timeSig: '4/4', leftHandStyle: 'wholeBarRoot',
        rh: {
          stepWeight: 0.68, repeatWeight: 0.1, leapWeight: 0.22,
          allowTriplets: false, staccatoChance: 0.2, rhRestChance: 0.03,
          phraseSlurChance: 0.1, tieAcrossBarChance: 0,
          simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
        },
      },
      'Toccata': {
        timeSig: '4/4', leftHandStyle: 'walkingBass',
        rh: {
          stepWeight: 0.7, repeatWeight: 0.05, leapWeight: 0.25,
          allowTriplets: false, staccatoChance: 0, rhRestChance: 0, rhWholeBarRestChance: 0,
          phraseSlurChance: 0, tieAcrossBarChance: 0,
          simpleMeterWeightOverride: { quarter: 1.2, half: 0.5, dottedHalf: 0.2, eighth: 2.4, sixteenth: 1.8, dottedEighth: 0.3 },
        },
      },
    },
    // 2026-09-10: reuses the Grade 4-6 triplet mechanism -- the fresh scan's
    // examples use triplets freely (this bucket's own 2026-08 comment above
    // already flagged the gap; now closed the same way Grade 5/6 were).
    allowTriplets: true,
    // 2026-09-14: same cascade protection now applied to every other grade
    // bucket that can land in 3/4 or 4/4 -- grade7's timeSigs list includes
    // both directly, and had no simpleMeterWeightOverride at all. Found via
    // proactive audit rather than a per-style screenshot report.
    simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
    // 2026-09-14: "Tier A" musical-expressiveness pass -- see grade6's
    // matching comment for the full rationale (hairpins deferred, these
    // five wired as opt-in rhParams toggles). Chances nudged up slightly
    // from grade6's, matching this grade's own generally busier/more
    // detailed real scan pages (see this bucket's tally comments above).
    accentChance: 0.22,
    tenutoChance: 0.18,
    fermataChance: 0.25,
    sfzMidChance: 0.15,
    tempoChangePairs: [
      ['rall.', 'a tempo'],
      ['rit.', 'Tempo I'],
      ['poco rall.', 'a tempo'],
      ['meno mosso', 'Tempo I'],
    ],
    tempoChangePairChance: 0.18,
    // 2026-09-15: "Tier B" ornamentation -- see grade6's matching comment
    // for the full rationale. Slightly busier pool/chances than grade6,
    // and mordent/turn given a bit more weight relative to trill (a
    // more advanced grade can carry a bit more ornament variety).
    ornamentChance: 0.3,
    ornamentNoteChance: 0.1,
    ornamentPool: ['trill', 'trill', 'turn', 'turn', 'mordent', 'mordent', 'grace'],
  },
  grade8: {
    // 2026-09-10: RECALIBRATED against a much bigger source -- all 13
    // examples on SR G8.pdf (AMEB book pages 44-55), superseding the
    // 5-example 2026-08 scan below (kept for history). This is the deepest
    // gap between engine and book of any grade -- every single example is
    // built from continuous chords in one or both hands (block chords,
    // arpeggiated broken chords spanning close to two octaves with sustain
    // pedal, chorale-style harmony), several use genuine two-voice
    // counterpoint (ex.4 "Two-part invention", clearly Bach-invention-style
    // imitative writing in 16th notes), one uses explicit hand-crossing with
    // a clef swap and an 8va/8vb register shift (ex.11 "Romanza", ex.12
    // "Etude"), and one example (ex.12 "Etude") changes time signature FIVE
    // times within one piece (4/4 -> 3/4 -> 4/4 -> 2/4 -> 4/4). None of this
    // is newly discovered -- the old 5-example scan already documented the
    // same class of gap -- but the bigger sample shows it's not a few
    // outlier examples, it's the norm for every example at this grade.
    //
    // What's newly calibrated from the bigger sample (all still text-only/
    // parameter-level, same "safely extractable" scope as the old scan):
    //   - Key signatures read directly off all 13: Db major/Bb minor (5
    //     flats, ex.4 Arioso, ex.6 Elegy), Ab major/F minor (4 flats, ex.2
    //     Agitato, ex.6 Triple time tango), Eb major (3 flats, ex.10
    //     Romanza), Bb major (2 flats, ex.9 March), E major (4 sharps, ex.5
    //     Springtime, ex.9 Passacaglia, ex.11 Etude), A major (3 sharps,
    //     ex.12 Sentimentale), D major (2 sharps, ex.3 Two-part invention).
    //     dbMajor/bbMinor/fMinor are new to this app (added to
    //     gradeParams.js's KEYS and scales.js's flat-spelling set, see those
    //     comments); abMajor/eMajor/dMajor/bbMajor/ebMajor already existed.
    //     Replaces the old key list entirely (same supersede approach as
    //     every other grade's re-scan in this file) -- the old scan's
    //     unconfirmed "Ab/Db major aren't supported, Eb/Bb major stand in
    //     instead" workaround is no longer needed now that the real keys are
    //     supported outright.
    //   - Time signatures: 3/4 is the clear majority (ex.2, 6, 7, 10, 13),
    //     plus 4/4 (ex.3, 9), 2/4 (ex.7 interlude, ex.8), and 9/8 (ex.9
    //     Passacaglia). Neither cut time (2/2) nor 6/8 -- both in the old
    //     bucket's timeSigs -- showed up anywhere in this 13-example set;
    //     replaced rather than merged, per this file's standing approach to
    //     conflicting scan evidence (most-recent/biggest scan wins). The
    //     mid-piece meter change (ex.12) stays unmodeled -- one timeSig per
    //     excerpt is a hard engine limit, not a parameter.
    //   - Bar counts stayed in roughly the same long range as the old scan;
    //     `bars` below is unchanged.
    label: 'Grade 8',
    bars: [15, 24],
    noteValues: ['quarter', 'half', 'eighth', 'dottedQuarter', 'dottedEighth', 'sixteenth', 'dottedHalf'],
    hands: 'together',
    // 2026-09-14: widened to the full major+minor set within this grade's
    // ceiling (7 sharps, 7 flats -- the top grade, so it gets every key:
    // C#/Cb major and A#/Ab minor round out the circle of fifths).
    keys: [
      'cMajor', 'aMinor', 'gMajor', 'eMinor', 'dMajor', 'bMinor', 'aMajor', 'fsMinor',
      'eMajor', 'csMinor', 'bMajor', 'gsMinor', 'fsMajor', 'dsMinor', 'csMajor', 'asMinor',
      'fMajor', 'dMinor', 'bbMajor', 'gMinor', 'ebMajor', 'cMinor', 'abMajor', 'fMinor',
      'dbMajor', 'bbMinor', 'gbMajor', 'ebMinor', 'cbMajor', 'abMinor',
    ],
    timeSigs: ['3/4', '4/4', '2/4', '9/8'],
    position: { spanScaleDegrees: 12 },
    maxLeapInterval: 8, // octave leaps possible
    maxLeapsPerExcerpt: 7,
    stepWeight: 0.54,
    repeatWeight: 0.08,
    leapWeight: 0.38,
    allowContraryMotion: true,
    allowTies: true,
    leftHandStyle: 'mixed',
    // 2026-09-14: RE-CHECKED against the actual SR G8.pdf scan at Sohyun's
    // request ("텍스쳐도 책보고 분석해서 그레이드마다 각각 적용해줘"). Same
    // 'fullTexture' no-op finding as grade6/7 (dropped -- see those
    // buckets' own comments). Grade 8's real LH is, as the bucket-level
    // comment below already documents at length, mostly full CHORDS this
    // engine can't genuinely produce -- but of the mechanisms that DO
    // exist, the closest approximations actually seen on the page are
    // 'blockChordsEveryBeat' (struck-chord density, e.g. "Call of the
    // bush"/"Allegretto"'s repeated chorded figures) and sustained
    // 'wholeBarRoot' (e.g. "Arioso"'s held bass under a chordal RH),
    // neither of which the old pool offered at all -- it was 100%
    // triadPattern/canonImitation, textures this scan doesn't actually
    // show much of. Rebuilt to weight the two chord-adjacent textures
    // highest, consistent with "every single example uses full chords".
    mixedStylePool: [
      'blockChordsEveryBeat', 'blockChordsEveryBeat', 'blockChordsEveryBeat',
      'wholeBarRoot', 'wholeBarRoot',
      'triadPattern',
      'canonImitation',
    ],
    // 2026-09-14: see bass.js's bassLowVarietyChance comment and grade4-7's
    // matching entries above -- highest here since Grade 8's LH textures are
    // this engine's richest and a lower register reads as appropriately more
    // "advanced" for the final grade.
    bassLowVarietyChance: 0.35,
    dynamics: ['pp', 'p', 'mp', 'mf', 'f', 'ff'],
    tempoMarkings: ['Moderato cantabile', 'Allegro giocoso', 'Grazioso', 'Moderato, hard and brassy', 'Andante (in 2)', 'Agitato', 'Maestoso', 'Sentimentale', 'Solemn', 'Con moto'],
    // 2026-09-10: same reasoning as Grade 5-7 -- reuses already-built
    // mechanisms rather than guessing at the chords/counterpoint/clef-swap
    // textures themselves, which stay deferred (see comment above).
    allowTriplets: true,
    staccatoChance: 0.1,
    // 2026-09-14: same over-staccato gap as grade5/grade6 -- staccatoChance
    // was on but articulationNoteChance was never set, so index.js's default
    // (100% of eligible notes marked staccato whenever staccato triggers at
    // all) was silently in effect here too. Found via proactive audit.
    articulationNoteChance: 0.4,
    lhStaccatoWithRhChance: 0.3,
    rhRestChance: 0.08,
    phraseSlurChance: 0.2,
    tieAcrossBarChance: 0.1,
    // 2026-09-14: same cascade protection applied to every other grade
    // bucket -- grade8's timeSigs list includes 3/4 and 4/4, and had none.
    simpleMeterWeightOverride: { quarter: 2.4, half: 1.6, dottedHalf: 0.6, eighth: 0.75, sixteenth: 0.2, dottedEighth: 0.15 },
    // 2026-09-14: "Tier A" musical-expressiveness pass -- see grade6's
    // matching comment for the full rationale (hairpins deferred, these
    // five wired as opt-in rhParams toggles). Highest chances of the three
    // grade6-8 buckets: this is the final, most advanced grade, and per
    // this bucket's own comment above it already leans on the most
    // dramatic real-book contrasts (full chords, clef changes, hand-
    // crossing) that the engine can't reproduce directly -- these five
    // per-note/per-excerpt marks are the closest available stand-in for
    // "more musically detailed and expressive" at this grade.
    accentChance: 0.28,
    tenutoChance: 0.22,
    fermataChance: 0.3,
    sfzMidChance: 0.2,
    tempoChangePairs: [
      ['rall.', 'a tempo'],
      ['rit.', 'Tempo I'],
      ['poco rall.', 'a tempo'],
      ['meno mosso', 'Tempo I'],
      ['stringendo', 'a tempo'],
    ],
    tempoChangePairChance: 0.22,
    // 2026-09-15: "Tier B" ornamentation -- see grade6's matching comment
    // for the full rationale. Highest chances/most even weighting of the
    // three grade6-8 buckets, matching this bucket's own "final, most
    // advanced grade" framing already established by Tier A's params.
    ornamentChance: 0.35,
    ornamentNoteChance: 0.12,
    ornamentPool: ['trill', 'trill', 'turn', 'turn', 'mordent', 'mordent', 'grace', 'grace'],
    //
    // Superseded 2026-08 comment (5-example scan) kept for history:
    // Calibrated against all 5 examples on the AMEB "Eighth Grade" pages
    // (2026-08 scan, pages 18-21) -- the final grade, and the one where the
    // gap between this engine's texture and the real book is widest.
    //
    // Every single one of the 5 examples uses at least one of: full CHORDS
    // in the right hand (all 5), mid-staff CLEF CHANGES so a hand can reach
    // an extreme register (ex.2, ex.5), or genuine HAND-CROSSING with an
    // explicit "l.h." marking plus an 8va octave-transposition sign (ex.3).
    // Unlike every earlier grade, there was no "more tractable" example to
    // lean on here -- the whole grade is built around textures this engine
    // cannot produce (it generates one monophonic RH line plus a simple LH
    // accompaniment, full stop). This bucket is therefore an intentional
    // simplification of real Grade 8 sight-reading, not a close match --
    // documented here rather than glossed over.
    //
    // What WAS safely extractable and is calibrated below: keys, time
    // signatures, note values, bar-length range, and the tempo/dynamic
    // text pools (all still text-only markings, unaffected by the texture
    // gap). Two keys seen in the scan -- Ab major (ex.1, 2) and Db major
    // (ex.2) -- are NOT in this app's KEYS table; adding them would also
    // require updating scales.js's flat/sharp spelling heuristic, which
    // felt like too large a change to make sight-unseen this late in the
    // pass, so Eb/Bb major stand in as the nearest already-supported flat
    // keys instead. Confirmed time sigs: cut time (ex.1), 3/4 (ex.3), 6/8
    // (ex.2, ex.4, ex.5 -- read as 6/8 rather than the less-common 3/8,
    // given the character markings and to stay on already-supported
    // meters). Bar counts stayed in the same long range as Grade 7.
    //
    // 2026-08-31: re-checked the scan page during a full grade-by-grade
    // re-verification. dMajor and aMajor were already in this list but
    // never actually named in the paragraph above as scan-confirmed --
    // they are: ex.3 ("Grazioso") has a clean 2-sharp signature (D major)
    // and ex.5 ("Andante (in 2)") has a clean 3-sharp signature (A major).
    // ex.3's 2 sharps is technically ambiguous between D major and its
    // relative B minor without a full harmonic reading, so bMinor is kept
    // alongside dMajor to cover that ambiguity rather than guessing one way.
    // 'gMinor', however, had no example to point to at all (ex.4's heavy
    // multi-flat signature doesn't match G minor's 2 flats, and nothing
    // else is unaccidented/2-flat) -- removed as an undocumented leftover.
    // (End of superseded 2026-08 comment; the live params are above.)
  },
};

// Grade selector -> bucket, plus display metadata + Clara alias.
const GRADES = [
  { id: 'prelim', label: 'Preliminary', claraAlias: 'Spark', bucket: 'prelim' },
  { id: 'grade1', label: 'Grade 1', claraAlias: 'Ember', bucket: 'grade1' },
  { id: 'grade2', label: 'Grade 2', claraAlias: 'Flame', bucket: 'grade2' },
  { id: 'grade3', label: 'Grade 3', claraAlias: 'Flame', bucket: 'grade3' },
  { id: 'grade4', label: 'Grade 4', claraAlias: 'Blaze', bucket: 'grade4' },
  { id: 'grade5', label: 'Grade 5', claraAlias: 'Blaze', bucket: 'grade5' },
  { id: 'grade6', label: 'Grade 6', claraAlias: 'Beacon', bucket: 'grade6' },
  { id: 'grade7', label: 'Grade 7', claraAlias: 'Beacon', bucket: 'grade7' },
  { id: 'grade8', label: 'Grade 8', claraAlias: 'Beacon', bucket: 'grade8' },
];

function getGradeMeta(gradeId) {
  const g = GRADES.find((x) => x.id === gradeId);
  if (!g) return null;
  return { ...g, params: BUCKETS[g.bucket] };
}

module.exports = { NOTE_VALUES, TIME_SIG_UNITS, BEAT_UNITS, KEYS, BUCKETS, GRADES, getGradeMeta };
