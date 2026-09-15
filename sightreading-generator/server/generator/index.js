// ---------------------------------------------------------------------------
// Top-level excerpt generator: looks up grade parameters, runs the rhythm /
// melody / bass generators, and assembles a LilyPond source string.
//
// This is rule-based (constrained random algorithm), not an LLM call --
// deterministic building blocks, seeded only by Math.random(), so it is
// fast, free, and infinitely repeatable per the spec.
// ---------------------------------------------------------------------------

const { getGradeMeta, NOTE_VALUES, TIME_SIG_UNITS, BEAT_UNITS, KEYS, GRADES } = require('./gradeParams');
const { generateRhythm } = require('./rhythm');
const { generateMelody } = require('./melody');
const { generateBass, unitsToLilyDuration } = require('./bass');
const { buildScale, toLilyPitch, raiseBySemitoneLetterAware, pitchClassOf } = require('./scales');

function clampIdx(i, len) {
  return Math.max(0, Math.min(len - 1, i));
}

// KNOWN GAP (2026-08-26): "realm" is currently COSMETIC ONLY. It changes
// the printed subtitle ("... — Reading" / "... — Rhythm" / "... — Technique")
// and is echoed back in `meta.realm`, but every realm runs through the exact
// same generation path with the exact same grade params -- there is no
// realm-specific weighting (e.g. Technique leaning on scale/arpeggio
// patterns, Rhythm leaning on richer rhythm with a narrower pitch range).
// The original build spec named these as three practice modes but the
// engine never grew distinct logic for them. Flagging explicitly rather
// than leaving it silently unimplemented -- revisit if/when realm-specific
// behavior is wanted.
const REALMS = ['reading', 'rhythm', 'technique'];

function pick(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

// 2026-08-31: force a line break every `groupSize` bars instead of letting
// LilyPond's default ragged-right auto-breaking decide -- with indent=0 and
// ragged-right=##t (see headerBlock's \paper block), auto-breaking packs as
// many bars as fit the page width per line, which for a piece like a 10-bar
// excerpt produced a lopsided 6-bars-then-4 split (reported as wanting a
// consistent, "balanced" look instead: "4마디 넘어가면 아래단으로"). `lines`
// is one bar-string per bar (each already ending in ` |`); returns a new
// array with a lone `\break` element inserted after every 4th bar (never
// after the last bar, which would produce a trailing empty system).
function withLineBreaks(lines, groupSize = 4) {
  const out = [];
  lines.forEach((line, i) => {
    out.push(line);
    const barNumber = i + 1;
    const isLast = i === lines.length - 1;
    if (barNumber % groupSize === 0 && !isLast) {
      out.push('\\break');
    }
  });
  return out;
}

// Weighted random pick over parallel `values`/`weights` arrays (used by
// buildAlternatingExcerpt's per-grade segment-count distribution).
function weightedChoice(values, weights) {
  const total = weights.reduce((s, w) => s + w, 0);
  let r = Math.random() * total;
  for (let i = 0; i < values.length; i++) {
    if (r < weights[i]) return values[i];
    r -= weights[i];
  }
  return values[values.length - 1];
}

// Realm-specific parameter overrides (2026-08-27): this is the first real,
// functional difference between Reading/Rhythm/Technique -- previously
// `realm` only changed the printed subtitle (see the KNOWN GAP note above
// REALMS, now partially addressed). Only the melodic-motion weights and the
// hand-position window are touched; bars/keys/timeSigs/noteValues/hands
// stay exactly as the grade bucket defines them, so difficulty level and
// rhythmic vocabulary are unaffected -- only *what kind of reading challenge*
// the excerpt emphasizes changes.
function applyRealmOverrides(params, realm) {
  if (realm === 'technique') {
    // Scale/pattern drilling: heavily stepwise, almost no leaps or repeated
    // notes -- reads like a 5-finger scale or arpeggio run rather than a
    // free melody. Mirrors what "Technique" practice usually means (finger
    // patterns), not sight-reading unfamiliar pitches.
    return { ...params, stepWeight: 0.92, repeatWeight: 0.04 };
  }
  if (realm === 'rhythm') {
    // Keep the grade's rhythmic vocabulary (noteValues) exactly as-is --
    // that's the whole point of this realm -- but shrink the pitch range and
    // lean on repeated notes, so the reading challenge is almost entirely
    // "read this rhythm correctly", not "find this pitch".
    const span = params.position ? params.position.spanScaleDegrees : 5;
    const narrowSpan = Math.max(2, Math.min(span, 3));
    return {
      ...params,
      position: { ...params.position, spanScaleDegrees: narrowSpan },
      repeatWeight: Math.min(0.5, params.repeatWeight + 0.22),
      stepWeight: Math.max(0.3, params.stepWeight - 0.15),
    };
  }
  return params; // 'reading' (default): the grade's calibrated balance, unchanged
}

// 2026-09-14: the local PITCH_CLASS_SEMITONE table (a third hand-copy of
// the same lookup melody.js/bass.js each kept -- see their matching
// comments) is gone. `pitchClassOf` (scales.js) computes any spelling's
// pitch class directly, so widening key coverage can't silently break this
// via a spelling nobody remembered to add to a fixed table.
//
// Parse a LilyPond absolute pitch token like "c'" or "bes,," into a single
// comparable semitone number (octave * 12 + pitch class).
function lyPitchToSemitone(ly, octaveOffset) {
  const pc = pitchClassOf(ly);
  if (pc == null) return null;
  return octaveOffset * 12 + pc;
}

// Smallest semitone gap between the melody's lowest note and the bass's
// highest note across an entire excerpt, or null if either voice is empty.
// `melodyPitches` are toLilyPitch() strings (e.g. "c'"); `bassBars` are
// bass.js's {pitch: {ly, octaveOffset}, durationUnits} event arrays.
function registerGapSemitones(melodyPitches, bassBars) {
  let rhMin = null;
  melodyPitches.forEach((tok) => {
    const m = tok.match(/^([a-g](?:is|es)?)([,']*)$/);
    if (!m) return;
    let oct = 0;
    for (const ch of m[2]) oct += ch === "'" ? 1 : -1;
    const semi = lyPitchToSemitone(m[1], oct);
    if (semi != null && (rhMin === null || semi < rhMin)) rhMin = semi;
  });
  let lhMax = null;
  bassBars.forEach((bar) => {
    bar.forEach((ev) => {
      // 2026-09-09: a rest event (`ev.rest`, see bass.js's bassRestChance)
      // carries no pitch at all -- nothing to compare against the melody's
      // register here, so skip it (falling through to `[ev.pitch]` below
      // would push `undefined` and crash on `.ly`).
      if (ev.rest) return;
      // 2026-09-03: an event may carry a chord (`ev.pitches`, an array --
      // see bass.js's blockChordsEveryBeat) instead of a single `ev.pitch`.
      // Check every chord tone, not just the first, since any of them could
      // be the one that's actually closest to the melody.
      const pitchList = ev.pitches || [ev.pitch];
      pitchList.forEach((p) => {
        const semi = lyPitchToSemitone(p.ly, p.octaveOffset);
        if (semi != null && (lhMax === null || semi > lhMax)) lhMax = semi;
      });
    });
  });
  if (rhMin === null || lhMax === null) return null;
  return rhMin - lhMax;
}

function resolveHands(requested, gradeParams) {
  if (requested === 'one-hand' || requested === 'hands-together') {
    return requested === 'hands-together' ? 'together' : 'one-hand';
  }
  // auto: defer to the grade's authentic default. "alternating" (AMEB
  // Grade 1: a single melodic line that hands off mid-piece between RH and
  // LH, never simultaneous) and "progressive" (pure one-hand, no second
  // staff at all) are both distinct from "together".
  if (gradeParams.hands === 'alternating') return 'alternating';
  if (gradeParams.hands === 'mixed') {
    // AMEB Grade 3 scan evidence: most examples are genuinely hands
    // together, but a real minority (roughly 1 in 3) still use a brief
    // call-and-response alternating device with short 1-2 bar segments --
    // model that as a per-excerpt coin flip rather than picking one texture
    // for the whole grade. `mixedAlternatingChance` is the bucket's tuned
    // probability of landing on the alternating variant.
    const altChance = gradeParams.mixedAlternatingChance != null ? gradeParams.mixedAlternatingChance : 0.3;
    return Math.random() < altChance ? 'alternating' : 'together';
  }
  if (gradeParams.hands === 'progressive') return 'one-hand';
  return 'together';
}

/**
 * @param {{gradeId: string, realm?: string, hands?: string}} opts
 * @returns {{lySource: string, meta: object}}
 */
function generateExcerpt(opts) {
  const gradeMeta = getGradeMeta(opts.gradeId);
  if (!gradeMeta) throw new Error(`Unknown grade: ${opts.gradeId}`);
  const params = gradeMeta.params;
  const realm = REALMS.includes(opts.realm) ? opts.realm : 'reading';
  // Hand configuration is a grade-authenticity question, not a realm one --
  // always resolved from the grade's own (un-overridden) params so e.g.
  // Grade 1's alternating-hands format doesn't change based on realm.
  const handsMode = resolveHands(opts.hands, params);
  // Everything downstream that shapes the actual notes (melody weights,
  // hand-position window) uses the realm-adjusted copy.
  // 2026-09-11: `let`, not `const` -- see the tempoFormRule.rh merge further
  // down (right after tempoFormRule itself is known), which layers a
  // per-style RH musicality profile on top of this.
  let effectiveParams = applyRealmOverrides(params, realm);
  const handsTogether = handsMode === 'together';
  const handsAlternating = handsMode === 'alternating';

  const keyId = pick(params.keys);
  const key = KEYS[keyId];

  // Cosmetic/notational markings confirmed present in the real AMEB books
  // from Grade 3-4 onward: a tempo/character word above the first bar, and
  // a dynamic mark under the first note. Only buckets that define these
  // pools (i.e. grades actually calibrated against scan evidence showing
  // them) will ever produce one -- everything else stays silent as before.
  // Picked BEFORE timeSig/leftHandStyle (2026-09-02) so a tempoFormRules
  // entry (see below) can steer those from the marking that was just drawn.
  //
  // 2026-09-04: tempoMarking is now picked FIRST, dynamic second (was the
  // other way around) -- Grade 3's scan showed the two are never actually
  // independent on the real page: an example either has an above-staff
  // tempo/character word AND a plain dynamic below it (ex.1 "Moderato"/f,
  // ex.2 "Espressivo"/p, ex.3 "Lively"/f, ex.7 "Allegretto"/mf), OR no tempo
  // word at all and a dynamic PAIRED WITH ITS OWN descriptive word instead
  // (ex.6 "p gentle", ex.9 "mp sweetly", ex.10 "f playfully", ex.13 "p
  // lilting", ex.15 "p sadly") -- never both a tempo word and a character
  // word together. Picking them independently (the old order/logic) could
  // land "Espressivo" above a "playfully" dynamic, which reads as a
  // contradiction (a tender, expressive character word over a bouncy one) --
  // reported directly (a generated excerpt paired exactly those two).
  // `params.standaloneDynamics` (opt-in per bucket, only Grade 3 sets it so
  // far) is the pool used when NO tempo marking was drawn this excerpt;
  // `params.dynamics` is used both as the with-tempo-marking pool and, for
  // every other bucket (no standaloneDynamics), the single all-purpose pool
  // exactly as before. `params.tempoMarkingChance` (also opt-in, defaults to
  // "always pick one" -- 1 -- preserving every other bucket's existing
  // 100%-of-the-time behavior) is Grade 3's ~1/3 real-page ratio (5 of 15
  // examples), since always showing a tempo word would leave
  // standaloneDynamics never actually reachable.
  let tempoMarking = null;
  if (params.tempoMarkings) {
    const tempoChance = params.tempoMarkingChance != null ? params.tempoMarkingChance : 1;
    if (Math.random() < tempoChance) tempoMarking = pick(params.tempoMarkings);
  }
  const dynamicPool = tempoMarking || !params.standaloneDynamics ? params.dynamics : params.standaloneDynamics;
  const dynamic = dynamicPool ? pick(dynamicPool) : null;

  // 2026-09-03: "Style" -- opts.feel is an OPTIONAL hint object
  // ({ timeSig?, leftHandStyle?, character? }) coming from the Generator
  // page's "Style" dropdown (see client/public/app.js's STYLE_PRESETS), not
  // from this grade's own calibrated pools. (This used to come from a
  // curated "Explorer Bank" piece's manually-tagged fields instead -- that
  // page was retired in favor of the dropdown, which needs no piece on file
  // at all.) `character` (e.g. "Lyrical and flowing") always wins as the
  // printed marking when given -- even for grades that have no
  // tempoMarkings pool of their own (Prelim/1/2 normally never print one) --
  // since it's an explicit characterization of the requested style, not a
  // random pick that needs to match scan-confirmed vocabulary.
  const feel = opts.feel || null;
  // `character` currently only ever comes from STYLE_PRESETS' own fixed
  // strings, but sanitize anyway rather than trusting the request body --
  // it flows straight into a LilyPond \tempo "..." string literal (see
  // assembleLilyPond/buildAlternatingExcerpt), so strip quote/backslash
  // characters so it can't break out of that string and corrupt the
  // generated .ly source, and cap length so an unexpectedly long value
  // can't blow up the printed excerpt.
  if (feel && feel.character) {
    tempoMarking = String(feel.character).replace(/["\\]/g, '').slice(0, 60).trim() || tempoMarking;
  }

  // 2026-09-02: a handful of tempo/character words are actual DANCE/PIECE
  // FORMS with a real, recognizable meter and accompaniment idiom attached
  // (e.g. "Minuet tempo" is always 3/4; "Waltz time" is 3/4 with an
  // oom-pah-pah LH) -- previously the word was purely cosmetic text and
  // timeSig/leftHandStyle were chosen completely independently, so a
  // "Minuet tempo" excerpt could just as easily land in 4/4, which doesn't
  // read as a minuet at all. `tempoFormRules` (opt-in per bucket -- only
  // grade4 defines it for now) lets a specific marking force a timeSig
  // and/or leftHandStyle for just that excerpt, without changing anything
  // for markings that don't name a real form (Andantino, Allegro, Moderato,
  // Tempo comodo stay exactly as random as before). Scope is deliberately
  // rhythm/meter-only, not full ABA form -- see gradeParams.js's grade4
  // comment.
  const tempoFormRule = tempoMarking && params.tempoFormRules ? params.tempoFormRules[tempoMarking] : null;
  // 2026-09-11: "스타일에 더 맞으면 좋겠어" -- a style marking used to change
  // ONLY the meter and the LH accompaniment idiom (tempoFormRule.timeSig/
  // leftHandStyle above); the RIGHT hand's melody was generated exactly the
  // same way regardless of whether the excerpt was marked "March" or
  // "Sarabande", which is why a generated "March" could still come out
  // legato and rest-free, or a "Sarabande" busy and detached -- neither
  // reads as its named form. `tempoFormRule.rh` (opt-in, only Grade 5's new
  // 8 dance/piece-form rules set it -- see gradeParams.js) is a partial
  // override merged over this grade's own calibrated params, touching only
  // the SAME knobs every bucket already tunes (stepWeight/repeatWeight/
  // leapWeight, allowTriplets, staccatoChance, rest chances, phrase-slur/
  // tie chances, the simple-meter duration-weight table) -- never a new
  // note value or technique outside what this grade already confirmed.
  const rhParams = tempoFormRule && tempoFormRule.rh ? { ...params, ...tempoFormRule.rh } : params;
  if (tempoFormRule && tempoFormRule.rh) {
    effectiveParams = { ...effectiveParams, ...tempoFormRule.rh };
  }
  let timeSig = (tempoFormRule && tempoFormRule.timeSig) || pick(params.timeSigs);
  // A feel.timeSig hint wins over both the tempoFormRule and the random pick
  // -- but ONLY when it's actually in this grade's own confirmed timeSigs
  // pool, so a Style pick (e.g. Waltz's 3/4) can never push a grade into a
  // meter it was never calibrated for. If the requested meter
  // isn't in this grade's pool, silently fall back to the grade's own
  // choice rather than erroring -- the "similar feel" is best-effort, not a
  // hard requirement, and grade-authenticity always wins.
  if (feel && feel.timeSig && params.timeSigs.includes(feel.timeSig)) {
    timeSig = feel.timeSig;
  }
  const barUnits = TIME_SIG_UNITS[timeSig];
  // The felt beat pulse for this time signature (2026-09-04, see
  // gradeParams.js's BEAT_UNITS comment) -- generateRhythm uses this so a
  // beat-or-longer note never starts stranded mid-beat.
  const beatUnits = BEAT_UNITS[timeSig] || 4;
  // 2026-09-09: "아직 다 안고쳐졌는데" -- the 6/8 beamGroupingOverride forces
  // LilyPond to break beams every 3 eighth-note-units, but rhythm.js's
  // beat-alignment only ever protected the COARSE felt beat (6 units for
  // 6/8) from being started mid-beat -- nothing stopped a shorter note
  // (e.g. a plain eighth) from straddling that finer 3-unit beam-break
  // line. `subBeatUnits` (rhythm.js's new optional parameter) closes that
  // gap: 3 for 6/8 and 9/8 (their two/three main pulses, each 3
  // eighth-note-units), otherwise the same as beatUnits (no extra
  // restriction beyond what already existed).
  const subBeatUnits = timeSig === '6/8' || timeSig === '9/8' ? 3 : beatUnits;
  // 2026-09-09: "이 복잡한 3개 리듬 비스무리한건 없애자" -- see rhythm.js's
  // COMPOUND_BEAT_PATTERNS comment. Compound meters (6/8, 9/8) now fill each
  // felt beat from a small curated pool of idiomatic groupings instead of
  // the general per-note algorithm, which had a second (distinct from the
  // straddle bug above) loophole letting a beat's leftover space force extra
  // short notes past the run cap.
  const compoundBeat = timeSig === '6/8' || timeSig === '9/8';
  // 2026-09-09: "2/2일 경우 간단하게 이정도로만" -- direct feedback (with a real
  // book photo, a sparse Andante built almost entirely from half/whole
  // notes) that Grade 4's cut-time excerpts were using the SAME rhythmic
  // vocabulary as its 4/4 material (eighths, dotted-eighth+sixteenth
  // pairs), reading far busier than the actual page. `timeSigNoteValues`
  // (opt-in per bucket) lets one specific timeSig swap in a narrower
  // noteValues list just for rhythm generation, without touching what
  // params.noteValues means for every other timeSig in the same grade.
  const rhythmNoteValues = (rhParams.timeSigNoteValues && rhParams.timeSigNoteValues[timeSig]) || rhParams.noteValues;
  // 2026-09-09: see gradeParams.js's simpleMeterWeightOverride comment --
  // opt-in per bucket, applied only for the two simple meters the user's
  // spec targeted (3/4, 4/4) so it's a no-op for every other grade/timeSig.
  // 2026-09-11: reads from rhParams (not raw params) so a tempoFormRule.rh
  // profile's own simpleMeterWeightOverride (e.g. March's dotted-rhythm
  // emphasis) takes effect -- rhParams falls back to plain params when no
  // rule applies, so every other excerpt is unaffected.
  const rhythmWeightOverrides = rhParams.simpleMeterWeightOverride && (timeSig === '3/4' || timeSig === '4/4')
    ? rhParams.simpleMeterWeightOverride
    : null;
  // 2026-09-09: "이 패턴도 넣어줘" -- see rhythm.js's dottedQuarterEighthChance
  // comment. Same gating as rhythmWeightOverrides above (opt-in per bucket,
  // simple meters only).
  const dottedQuarterEighthChance = rhParams.dottedQuarterEighthChance && (timeSig === '3/4' || timeSig === '4/4')
    ? rhParams.dottedQuarterEighthChance
    : null;
  // Only affects the LH texture picked in the hands-together branch below
  // (generateBass reads params.leftHandStyle); alternating-hands grades
  // never reach a tempoFormRules bucket today, so bassParams is unused there.
  let bassParams = tempoFormRule && tempoFormRule.leftHandStyle
    ? { ...params, leftHandStyle: tempoFormRule.leftHandStyle }
    : params;
  // Same priority as timeSig above: an explicit feel.leftHandStyle wins.
  // Unlike timeSig, there's no grade-specific "allowed pool" to check against
  // here (bass.js's switch already falls back to its default texture for any
  // unrecognised style string), so this is passed through as-is.
  if (feel && feel.leftHandStyle) {
    bassParams = { ...params, leftHandStyle: feel.leftHandStyle };
  }

  // Playback tempo (MIDI only -- never printed on the page, see midiBlock
  // below). A gentle, grade-scaled practice speed so beginners get a slow,
  // clearly-readable playback and advanced grades a bit more brisk; this is
  // for "does this sound right" checking, not a performance tempo.
  const gradeIndex = Math.max(0, GRADES.findIndex((g) => g.id === opts.gradeId));
  const bpm = 76 + gradeIndex * 4;

  let lySource;
  let lySourceTreble = null;
  let lySourceBass = null;
  let barCount;

  if (handsAlternating) {
    const built = buildAlternatingExcerpt({
      gradeLabel: gradeMeta.label,
      claraAlias: gradeMeta.claraAlias,
      realm,
      key,
      keyId,
      timeSig,
      barUnits,
      params: effectiveParams,
      dynamic,
      tempoMarking,
      bpm,
    });
    lySource = built.lySource;
    lySourceTreble = built.lySourceTreble;
    lySourceBass = built.lySourceBass;
    barCount = built.barCount;
  } else {
    barCount = randEvenRange(params.bars[0], params.bars[1]);
    // Rhythm (per-bar arrays of NOTE_VALUES keys) -- melody rhythm is
    // primary; when hands are together the bass uses its own simpler
    // block/broken patterns generated straight from the bar length (see
    // bass.js), so it never needs independent complex rhythm reading.
    const rhythmBars = generateRhythm(barCount, barUnits, rhythmNoteValues, beatUnits, subBeatUnits, compoundBeat, rhythmWeightOverrides, dottedQuarterEighthChance);
    // 2026-09-09: "triplet도 한 두번 나오는 정도" -- closes the "still no tuplet
    // support" gap flagged in grade4's own 2026-09-07 scan comment (ex.13's
    // bracketed triplet). Opt-in per bucket (params.allowTriplets), simple
    // meters only (compound 6/8/9/8 patterns are curated separately and
    // weren't asked to include triplets). Implemented as a POST-PROCESS:
    // pick 0-2 already-placed plain 'quarter' entries (never the very first
    // or very last note of the piece, so the opening and final cadence stay
    // stable) and split each into three 'tripletEighth' entries -- since a
    // tuplet's 3-in-the-time-of-2 notes don't fit the integer sixteenth-unit
    // accounting fillBar relies on, doing this AFTER the bar's exact-fill
    // guarantee already holds keeps that accounting untouched. The melody
    // pitch generator below reads bar.length per bar, so it naturally
    // produces 3 pitches for a tripled entry with no separate wiring.
    // assembleLilyPond's token builder (see mergeTriplets) wraps each
    // resulting run of 3 in `\tuplet 3/2 { ... }`.
    if (rhParams.allowTriplets && !compoundBeat) {
      const eligible = [];
      rhythmBars.forEach((bar, barIdx) => {
        bar.forEach((key, noteIdx) => {
          if (key === 'quarter') eligible.push({ barIdx, noteIdx });
        });
      });
      const lastBarIdx = rhythmBars.length - 1;
      const pool = eligible.filter(({ barIdx, noteIdx }) => !(barIdx === 0 && noteIdx === 0)
        && !(barIdx === lastBarIdx && noteIdx === rhythmBars[lastBarIdx].length - 1));
      if (pool.length > 0) {
        const roll = Math.random();
        const tripletCount = roll < 0.4 ? 0 : roll < 0.8 ? 1 : 2;
        const chosenCount = Math.min(tripletCount, pool.length);
        for (let i = pool.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [pool[i], pool[j]] = [pool[j], pool[i]];
        }
        const byBar = {};
        pool.slice(0, chosenCount).forEach(({ barIdx, noteIdx }) => {
          (byBar[barIdx] = byBar[barIdx] || []).push(noteIdx);
        });
        Object.keys(byBar).forEach((barIdxStr) => {
          const barIdx = Number(barIdxStr);
          const idxsDesc = byBar[barIdx].sort((a, b) => b - a);
          idxsDesc.forEach((noteIdx) => {
            rhythmBars[barIdx].splice(noteIdx, 1, 'tripletEighth', 'tripletEighth', 'tripletEighth');
          });
        });
      }
    }
    const notesPerBar = rhythmBars.map((b) => b.length);
    const totalNotes = notesPerBar.reduce((a, b) => a + b, 0);
    // 2026-08-29: "one-hand" grades (currently just Preliminary, per the
    // real AMEB scan -- separate right-hand-only and left-hand-only
    // exercises, never a second staff at all) pick which single clef to use
    // at random per excerpt, roughly matching the real page's near-even
    // split between its RH and LH exercise lists. Every other hands mode
    // always uses the treble register for its melody line (shift 0), same
    // as before.
    const oneHandClef = handsMode === 'one-hand' ? (Math.random() < 0.5 ? 'treble' : 'bass') : 'treble';
    const oneHandRegisterShift = oneHandClef === 'bass' ? -1 : 0;
    // 2026-08-29: melody.js's REGISTER_GAP_PAD only exists to keep this
    // hand's notes from reading as touching a SIMULTANEOUS second hand (see
    // melody.js's avoidOverlapPad doc comment) -- it has no purpose when
    // there is no second hand at all (one-hand grades, i.e. Preliminary).
    // Left at its true-by-default value, the pad shifted the treble window's
    // floor up while a narrower span (e.g. Preliminary's span=5) meant the
    // trimmed-safe window no longer reached back to any in-window tonic,
    // silently breaking the "every window contains a tonic" guarantee
    // endOnTonic's tail-walk depends on -- its unsafe fallback then landed
    // the final note as high as g'' (2 semitones above TREBLE_SAFE_HI),
    // reproducing the "notes overshoot the staff" regression found via the
    // register-safety regression check. Passing handsTogether here (false
    // for one-hand) restores the tonic guarantee for one-hand excerpts while
    // leaving the hands-together gap padding untouched.
    let melodyResult = generateMelody(totalNotes, effectiveParams, keyId, oneHandRegisterShift, 0, true, null, handsTogether);
    let { pitches, degrees } = melodyResult;

    // 2026-08-31: every melody degree WITHIN each bar (not just its opening
    // note) -- bass.js's chooseChordRoot now fits harmony against the whole
    // bar's line, since scoring on only the first note could pick a chord
    // that clashed with the rest of the bar (see its doc comment for the
    // "make the LH accompaniment actually make sense" fix this feeds).
    const degreesPerBar = (degs) => {
      const out = [];
      let cursor = 0;
      notesPerBar.forEach((n) => {
        out.push(degs.slice(cursor, cursor + n));
        cursor += n;
      });
      return out;
    };
    let melodyDegreesPerBar = degreesPerBar(degrees);

    let chordRootsPerBar = [];
    let bassBars = handsTogether ? generateBass(rhythmBars, melodyDegreesPerBar, bassParams, keyId, timeSig, chordRootsPerBar) : null;

    // Safety net (2026-08-27): melody.js's REGISTER_GAP_PAD and bass.js's
    // chordCeiling both push the two hands apart by scale-degree INDEX, but
    // the actual semitone distance between any two scale degrees depends on
    // where the key's half-steps fall (e.g. in A minor, "b" and "c" sit a
    // single semitone apart regardless of octave) -- so index-based padding
    // alone can't guarantee a safe gap in every key. Belt-and-suspenders:
    // measure the ACTUAL semitone gap for this specific excerpt and, if it's
    // uncomfortably tight, regenerate the melody one octave-block higher
    // (which always restores a clean gap; there's no ceiling on the treble
    // side, see melody.js) rather than trying to prove it analytically for
    // every key/mode combination up front.
    if (handsTogether && bassBars) {
      const MIN_GAP_SEMITONES = 4;
      // Escalate gently: try nudging the melody's floor up a couple of
      // scale-degrees at a time first (barely noticeable) before resorting
      // to a full octave-block jump (which fixes the gap but pushes the
      // melody into a noticeably higher, more ledger-line-heavy register --
      // only worth it if smaller nudges genuinely weren't enough).
      const floorPadSteps = [0, 2, 4];
      for (let attempt = 0; attempt < floorPadSteps.length; attempt++) {
        const gap = registerGapSemitones(pitches, bassBars);
        if (gap === null || gap >= MIN_GAP_SEMITONES) break;
        const isLastAttempt = attempt === floorPadSteps.length - 1;
        melodyResult = isLastAttempt
          ? generateMelody(totalNotes, effectiveParams, keyId, 1, 0, true)
          : generateMelody(totalNotes, effectiveParams, keyId, 0, floorPadSteps[attempt + 1], true);
        pitches = melodyResult.pitches;
        degrees = melodyResult.degrees;
        melodyDegreesPerBar = degreesPerBar(degrees);
        chordRootsPerBar = [];
        bassBars = generateBass(rhythmBars, melodyDegreesPerBar, bassParams, keyId, timeSig, chordRootsPerBar);
      }
    }

    // 2026-09-14: "음악이 쳐보면 어색한데" -- direct follow-up asking why generated
    // excerpts sound off. Root cause: bass.js raises the V chord's third to a
    // proper leading tone in every minor-key V chord (its own 2026-08-31/
    // 2026-09-11 comments), but chooseChordRoot's melody-fit scoring tends to
    // PICK V specifically when the bar's melody sits on the plain natural 7th
    // degree -- that note is literally one of V's raw diatonic chord tones
    // before the raise, so it scores well for V. The LH then raises its
    // third while the RH keeps playing the unraised note in the very same
    // bar: a genuine false relation (e.g. A minor: LH sounds G# while RH
    // sounds G natural at the same time), a real clashing wrong-note moment,
    // not just a plain/simple one. Real harmony raises the leading tone
    // consistently within its harmonic context, not only at the very final
    // cadence (the only place melody.js's own raise already applies) --
    // so wherever the LH's chosen harmony for a bar is V in a minor key, any
    // RH note in that same bar sitting on the natural 7th degree is raised
    // to match, using the same letter-aware raise both hands' existing
    // leading-tone logic already relies on. Read via chordRootsPerBar (see
    // bass.js's matching comment) rather than re-deriving the harmony here.
    if (handsTogether && bassBars && key.mode === 'minor') {
      const melScaleForRaise = buildScale(keyId, 6);
      let noteIdx = 0;
      notesPerBar.forEach((n, barIdx) => {
        if (chordRootsPerBar[barIdx] === 4) {
          for (let k = 0; k < n; k++) {
            const idx = noteIdx + k;
            const deg = degrees[idx];
            const degMod = ((deg % 7) + 7) % 7;
            if (degMod === 6) {
              pitches[idx] = toLilyPitch(
                raiseBySemitoneLetterAware(melScaleForRaise[clampIdx(deg, melScaleForRaise.length)])
              );
            }
          }
        }
        noteIdx += n;
      });
    }

    // 2026-09-03: "RH block chords" (calibrated against the new 15-example
    // Grade 3 scan's ex.5/ex.8, see gradeParams.js's grade3 comment) -- a
    // per-excerpt chance that EVERY right-hand note is thickened with a
    // diatonic third below it, rendered as a LilyPond chord. Deliberately a
    // whole-excerpt toggle (not a per-bar one) since both scan examples are
    // chordal throughout, not just in isolated bars. Only wired up for the
    // hands-together, non-alternating path -- alternating-hands excerpts
    // (buildAlternatingExcerpt) don't read params.rhChordChance at all,
    // flagged as a deferred gap rather than silently ignored.
    let pitchesHarmony = null;
    if (handsTogether && params.rhChordChance && Math.random() < params.rhChordChance) {
      // Mirrors melody.js's own `buildScale(keyId, 6)` call exactly, so
      // `degrees` (absolute indices into THAT array) line up correctly here.
      const melScale = buildScale(keyId, 6);
      pitchesHarmony = degrees.map((deg) => toLilyPitch(melScale[clampIdx(deg - 2, melScale.length)]));
    }

    // 2026-09-03: "mid-piece expressive markings" (ex.2/ex.4/ex.15 in the
    // new 15-example Grade 3 scan show a "rall."/"dim."-type word partway
    // through, not just at the very start) -- a per-excerpt chance of one
    // extra italic marking attached a couple-thirds of the way through the
    // piece. Same hands-together/non-alternating scope as the RH-chord
    // feature above, for the same reason.
    let midMarking = null;
    if (handsTogether && params.midPieceMarkings && params.midPieceMarkingChance && Math.random() < params.midPieceMarkingChance) {
      midMarking = pick(params.midPieceMarkings);
    }

    // 2026-09-03: "staccato" (see gradeParams.js's grade3 comment for the
    // full evidence) -- a per-excerpt, per-HAND toggle, and even when a hand
    // is toggled on, only its quarter-note-or-longer events get dotted;
    // eighth-note-or-shorter runs always stay slurred/legato regardless
    // (assembleLilyPond enforces that duration filter, not this flag alone).
    // lhStaccatoWithRhChance is read only when RH staccato already fired --
    // no scan example showed the LH dotted while the RH wasn't, so this is
    // deliberately a one-way dependency, not two independent rolls.
    // 2026-09-11: staccatoChance/lhStaccatoWithRhChance read from rhParams
    // (not raw params) so a tempoFormRule.rh profile can push a style's
    // articulation either way -- e.g. Grade 5's "March" wants crisp,
    // detached notes (raised staccatoChance) while "Romanze"/"Sarabande"
    // want a smooth singing line (staccatoChance forced to 0, overriding
    // this bucket's own default). rhParams falls back to plain params when
    // no rule applies.
    let rhStaccato = false;
    let lhStaccato = false;
    if (handsTogether && rhParams.staccatoChance && Math.random() < rhParams.staccatoChance) {
      rhStaccato = true;
      if (rhParams.lhStaccatoWithRhChance && Math.random() < rhParams.lhStaccatoWithRhChance) {
        lhStaccato = true;
      }
    }

    // 2026-09-14: "Tier A" musical-expressiveness pass (grades 6-8, per
    // Sohyun's "그레이드 6에서 8까지는... 좀더 가미할 수 있을 요소" request) --
    // five independent, per-excerpt opt-in toggles, all read from rhParams
    // (not raw params) so a tempoFormRule.rh style profile can push any of
    // them either way exactly like staccatoChance/phraseSlurChance already
    // do. Each is its own coin flip (not bundled into one master
    // "expressiveness" toggle) since the real book evidence doesn't show
    // these always co-occurring -- a Nocturne might get tenuto phrasing
    // without ever getting a sudden \sf, for instance.
    let rhAccent = false;
    let rhTenuto = false;
    let fermata = false;
    let sfzMid = false;
    let tempoChangePair = null;
    if (handsTogether) {
      if (rhParams.accentChance && Math.random() < rhParams.accentChance) rhAccent = true;
      if (rhParams.tenutoChance && Math.random() < rhParams.tenutoChance) rhTenuto = true;
      if (rhParams.fermataChance && Math.random() < rhParams.fermataChance) fermata = true;
      if (rhParams.sfzMidChance && Math.random() < rhParams.sfzMidChance) sfzMid = true;
      // Deliberately gated on `!midMarking` -- the plain single-word
      // mid-piece marking and the paired tempo-change markings both anchor
      // near the same 40-75% window of the piece, so letting both fire on
      // the same excerpt risks two markup blocks stacked on nearby/same
      // bars. Skipping the pair when a plain midMarking already landed
      // keeps the piece from getting visually crowded.
      if (!midMarking && rhParams.tempoChangePairs && rhParams.tempoChangePairChance
        && Math.random() < rhParams.tempoChangePairChance) {
        tempoChangePair = pick(rhParams.tempoChangePairs);
      }
    }

    // 2026-09-15: "Tier B" ornamentation (grade6-8, continuing the
    // "순서대로" tier sequence right after Tier A) -- grace notes, trills,
    // and turns/mordents. Unlike Tier A's marks (which just append a
    // postfix articulation to an EXISTING note token), an acciaccatura
    // grace note needs its own real diatonic PITCH to grace with, so it's
    // precomputed here, in the exact same scope/pattern pitchesHarmony
    // already uses (`degrees` + a fresh `buildScale(keyId, 6)` call) --
    // one scale-STEP above each main note (the most common real
    // "upper-neighbour acciaccatura" shape, e.g. a quick grace note a
    // second above landing on the beat). Trill/turn/mordent need no pitch
    // precomputation at all (they're pure postfix marks, `\trill`/`\turn`/
    // `\mordent`), so only `ornamentsEnabled` + the weighted `ornamentPool`
    // get passed down for those; assembleLilyPond does the actual per-note
    // picking (it already owns the per-note eligibility logic Tier A's
    // accent/tenuto marks use, and ornaments need the identical guards:
    // quarter-note-or-longer, not already marked staccato/accent/tenuto,
    // not a rest).
    let ornamentsEnabled = false;
    let graceNotePitches = null;
    if (handsTogether && rhParams.ornamentChance && Math.random() < rhParams.ornamentChance) {
      ornamentsEnabled = true;
      if (rhParams.ornamentPool && rhParams.ornamentPool.includes('grace')) {
        const melScaleForGrace = buildScale(keyId, 6);
        graceNotePitches = degrees.map((deg) => toLilyPitch(melScaleForGrace[clampIdx(deg + 1, melScaleForGrace.length)]));
      }
    }

    const built = assembleLilyPond({
      gradeLabel: gradeMeta.label,
      claraAlias: gradeMeta.claraAlias,
      realm,
      key,
      timeSig,
      rhythmBars,
      pitches,
      pitchesHarmony,
      handsTogether,
      clef: oneHandClef,
      dynamic,
      tempoMarking,
      midMarking,
      rhStaccato,
      lhStaccato,
      bassBars,
      bpm,
      // 2026-09-11: all five read from rhParams (not raw params) so a
      // tempoFormRule.rh profile can shape phrasing/articulation per style
      // -- e.g. "Romanze"/"Sarabande" raise phraseSlurChance/tieAcrossBarChance
      // for a smooth singing line, "March"/"Hymn" zero out rests for a
      // continuous, undecorated texture. Falls back to plain params when no
      // rule applies (rhParams === params in that case), so every other
      // excerpt behaves exactly as before.
      phraseSlurChance: handsTogether ? rhParams.phraseSlurChance : null,
      tieAcrossBarChance: handsTogether ? rhParams.tieAcrossBarChance : null,
      articulationNoteChance: handsTogether ? rhParams.articulationNoteChance : null,
      rhRestChance: handsTogether ? rhParams.rhRestChance : null,
      rhWholeBarRestChance: handsTogether ? rhParams.rhWholeBarRestChance : null,
      rhAccent,
      rhTenuto,
      fermata,
      sfzMid,
      tempoChangePair,
      ornamentsEnabled,
      ornamentNoteChance: handsTogether ? rhParams.ornamentNoteChance : null,
      ornamentPool: handsTogether ? rhParams.ornamentPool : null,
      graceNotePitches,
    });
    lySource = built.lySource;
    lySourceTreble = built.lySourceTreble;
    lySourceBass = built.lySourceBass;
  }

  const meta = {
    gradeId: opts.gradeId,
    gradeLabel: gradeMeta.label,
    claraAlias: gradeMeta.claraAlias,
    realm,
    hands: handsMode,
    key: key.name,
    timeSig,
    barCount,
    generatedAt: new Date().toISOString(),
    // Echoed back (not used internally past this point) so the frontend can
    // show a "🎯 Style: ..." pill on the result -- only set when the
    // request actually carried a feel hint (e.g. from the Style dropdown).
    feelSource: opts.feelSource || null,
  };

  return { lySource, lySourceTreble, lySourceBass, meta };
}

function randRange(min, max) {
  return min + Math.floor(Math.random() * (max - min + 1));
}

// 2026-08-31: "바 넓이 전체가 딱 맞아떨어지게" -- LilyPond's default spacing
// stretches each bar's width mostly by how many noteheads it contains, so
// two bars with the SAME total duration (same time signature) can still end
// up visibly different widths on the page just because one has more, closer
// notes. `uniform-stretching` makes horizontal spacing track duration only,
// so same-duration bars come out close to the same width -- a more even,
// grid-like look, which is what a sight-reading page wants (bars are meant
// to look like consistent "slots" the eye can jump between), rather than
// idiomatic full-score engraving's note-density-aware spacing.
const LAYOUT_BLOCK = `\\layout {
    \\context {
      \\Score
      \\override SpacingSpanner.uniform-stretching = ##t
    }
  }`;

// 2026-08-31: force the excerpt's TOTAL bar count to always be even (paired
// phrases read more naturally, and it keeps the forced-4-bars-per-line
// breaking from ever leaving a lone single bar dangling on its own last
// line) -- picks only even integers within [min, max]. If the range itself
// can't produce an even number in bounds (a single-value range on an odd
// number -- doesn't currently happen for any grade bucket, but guarded
// anyway), falls back to the plain range rather than throwing.
function randEvenRange(min, max) {
  const lo = Math.ceil(min / 2) * 2;
  const hi = Math.floor(max / 2) * 2;
  if (lo > hi) return randRange(min, max);
  const count = (hi - lo) / 2 + 1;
  return lo + 2 * Math.floor(Math.random() * count);
}

// Compound meters (6/8, 9/8) are felt in dotted-quarter beats, not quarter
// beats -- using the same numeric bpm for "4=X" there would sound roughly
// 1.5x too fast. This ONLY affects MIDI playback speed, never the printed
// page: it lives inside \midi {}, a block LilyPond uses purely for audio
// rendering (see lilypondCompiler.js), so a grade with no confirmed tempo
// marking still gets a sensible, silent-on-the-page practice tempo.
const COMPOUND_TIME_SIGS_FOR_MIDI = new Set(['6/8', '9/8']);
function midiBlock(timeSig, bpm) {
  if (COMPOUND_TIME_SIGS_FOR_MIDI.has(timeSig)) {
    return `\n  \\midi { \\tempo 4. = ${Math.round((bpm * 2) / 3)} }`;
  }
  return `\n  \\midi { \\tempo 4 = ${bpm} }`;
}

// Attach a LilyPond dynamic mark (e.g. "\mp") to the very first note token
// of a lines array (skipping any leading full-bar rests), mutating in
// place. No-op if there's no dynamic to attach or every line is a rest.
// LilyPond's builtin dynamic-mark commands (\mp, \f, etc.) -- anything
// outside this set is treated as a descriptive performance-direction WORD
// (see grade2's `dynamics` comment: "smoothly", "loudly", "cheerfully" and
// so on, confirmed under several AMEB Grade 2 examples) and rendered as
// italic text instead, since e.g. "\smoothly" isn't a real LilyPond command.
const STANDARD_DYNAMICS = new Set(['ppp', 'pp', 'p', 'mp', 'mf', 'f', 'ff', 'fff', 'sfz', 'fp']);

// 2026-09-03: turn one bass.js event into its LilyPond note token(s),
// handling BOTH shapes an event can have -- a single `pitch` (every LH style
// except blockChordsEveryBeat) or a `pitches` array (a struck chord, see
// bass.js's blockChordsEveryBeat). A duration that doesn't map to one
// LilyPond token ties across several (unitsToLilyDuration's fallback) --
// for a chord, every note in it gets the same tie treatment so the whole
// chord ties together cleanly.
// `staccato` (2026-09-03): dots the event UNLESS it's shorter than a quarter
// note (STACCATO_MIN_UNITS) -- same rule as the RH side, see its comment.
// `noteChance` (2026-09-05, default 1 -- see articulationNoteChance's own
// comment at its call site): the per-eligible-note chance the dot actually
// gets drawn, so a staccato excerpt doesn't necessarily dot EVERY qualifying
// note.
function bassEventTokens(ev, staccato, noteChance = 1) {
  const durTokens = unitsToLilyDuration(ev.durationUnits);
  // 2026-09-09: "왼손 비중 이정도로 너무 많지 않게" -- see bass.js's
  // bassRestChance comment. A rest event (`ev.rest`) has no pitch at all --
  // skip staccato/ties entirely (neither makes sense on silence).
  //
  // 2026-09-09 (later): "4분쉼표는 가운데 정렬해주고" -- a rest spanning the
  // WHOLE bar (`ev.fullBar`, the only kind produced today) renders as a real
  // LilyPond multi-measure rest (uppercase `R`, from the same FULL_BAR_REST
  // table used elsewhere for this), which LilyPond centers in the bar
  // automatically. A plain lowercase `r` rest -- what this used to always
  // emit -- positions like an ordinary note at the start of the bar instead,
  // which read as stuck off to one side rather than centered.
  if (ev.rest) {
    if (ev.fullBar) {
      return [FULL_BAR_REST[ev.durationUnits] || 'R1'];
    }
    return durTokens.map((d) => `r${d}`);
  }
  const pitchToken = ev.pitches
    ? `<${ev.pitches.map((p) => `${p.ly}${lyOctaveMarks(p)}`).join(' ')}>`
    : `${ev.pitch.ly}${lyOctaveMarks(ev.pitch)}`;
  const staccatoMark = staccato && ev.durationUnits >= STACCATO_MIN_UNITS && Math.random() < noteChance ? '-.' : '';
  return durTokens.map((d, idx) => {
    const tie = durTokens.length > 1 && idx < durTokens.length - 1 ? '~' : '';
    return `${pitchToken}${d}${staccatoMark}${tie}`;
  });
}

// Attach an italic performance-direction word (e.g. "rall.", "dim.") ABOVE
// the first note of a bar roughly two-thirds of the way through the piece
// (2026-09-03, see the "mid-piece expressive markings" feature note at its
// call site) -- distinct from attachDynamic, which always marks the very
// first note. Clamped away from the very first/last bar (a marking on
// either of those would just duplicate what the opening tempo/dynamic or
// the final cadence already conveys) and a no-op for anything shorter than
// 3 bars, where "roughly two-thirds through, not the first or last bar"
// isn't a meaningful position.
function attachMidMarking(lines, marking) {
  if (!marking || lines.length < 3) return lines;
  const idx = Math.max(1, Math.min(lines.length - 2, Math.floor(lines.length * 0.65)));
  const tokens = lines[idx].split(' ');
  tokens[0] = `${tokens[0]}^\\markup { \\italic "${marking}" }`;
  lines[idx] = tokens.join(' ');
  return lines;
}

// 2026-09-14: "Tier A" -- a genuinely PAIRED mid-piece marking, e.g. "rall."
// followed later by "a tempo", rather than the single one-off midMarking
// above. Deliberately a SEPARATE mechanism (not a second call into
// attachMidMarking) so the two never collide on the same bar and so a
// bucket can opt into "paired" phrasing (tempoChangePairChance/
// tempoChangePairs in gradeParams.js) independently of the plain single-
// word midPieceMarkings pool. Anchored at ~40% and ~75% through the piece
// (spaced well apart so the pair reads as two distinct events, not two
// markings crowded together) and clamped away from the first/last two
// bars for the same "wouldn't just duplicate the opening/cadence" reason
// attachMidMarking already documents. No-op under 6 bars, where two
// well-separated anchor points aren't meaningful.
function attachTempoChangePair(lines, pair) {
  if (!pair || lines.length < 6) return lines;
  const [textA, textB] = pair;
  const idxA = Math.max(1, Math.min(lines.length - 4, Math.floor(lines.length * 0.4)));
  const idxB = Math.max(idxA + 2, Math.min(lines.length - 2, Math.floor(lines.length * 0.75)));
  if (idxB <= idxA || idxB >= lines.length) return lines;
  const stamp = (idx, text) => {
    const tokens = lines[idx].split(' ');
    tokens[0] = `${tokens[0]}^\\markup { \\italic "${text}" }`;
    lines[idx] = tokens.join(' ');
  };
  stamp(idxA, textA);
  stamp(idxB, textB);
  return lines;
}

// 2026-09-14: "Tier A" -- a sudden sforzando (\sf) partway through the
// piece, distinct from attachDynamic's OPENING dynamic. Anchored at ~45%
// through the piece (a single fixed point, not a random one, so it reads
// as one deliberate accent-dynamic rather than noise) and skipped
// entirely if that bar happens to be a rest (a \sf on a rest is
// meaningless). No-op under 4 bars, matching attachMidMarking's own
// shortest-piece floor.
function attachSfz(lines, enabled) {
  if (!enabled || lines.length < 4) return lines;
  const idx = Math.max(1, Math.min(lines.length - 2, Math.floor(lines.length * 0.45)));
  if (/^R/.test(lines[idx].trim())) return lines;
  const tokens = lines[idx].split(' ');
  tokens[0] = `${tokens[0]}\\sf`;
  lines[idx] = tokens.join(' ');
  return lines;
}

// 2026-09-14: "Tier A" -- a fermata over the VERY LAST note of the piece
// (the held pause a sight-reading candidate would actually see printed
// over a final cadence chord). Skipped if the final bar is a whole-bar
// rest (can't happen in practice -- bass.js/melody.js always force a real
// tonic-ending note -- but guarded anyway, same defensive style as
// attachDynamic's own no-line-found guard). Finds the last non-barcheck
// token (`|`) in the final line rather than assuming a fixed position,
// since a tied/merged-triplet bar's last real token isn't always the
// line's literal last element.
function attachFermata(lines, enabled) {
  if (!enabled || !lines.length) return lines;
  const lastIdx = lines.length - 1;
  if (/^R/.test(lines[lastIdx].trim())) return lines;
  const tokens = lines[lastIdx].split(' ');
  let ti = tokens.length - 1;
  while (ti >= 0 && tokens[ti] === '|') ti--;
  if (ti < 0) return lines;
  tokens[ti] = `${tokens[ti]}\\fermata`;
  lines[lastIdx] = tokens.join(' ');
  return lines;
}

// 2026-09-03: `dynamic` can now be a two-word combo like "p gentle" (see
// gradeParams.js's grade3 comment) -- a real LilyPond dynamic PLUS a
// descriptive word printed beside it, matching how the actual AMEB page
// pairs them under the first note. Splits on the first space: if the first
// word is a real dynamic command, print `\word1` followed by the rest as
// italic text; otherwise (a bucket like Grade 2's whose whole `dynamics`
// pool is descriptive prose, never a real dynamic) fall back to the old
// single-italic-markup rendering for the whole string.
function attachDynamic(lines, dynamic, fromIdx = 0) {
  if (!dynamic) return lines;
  // fromIdx (2026-09-07, default 0): search for the first non-rest line AT
  // OR AFTER this index instead of from the very start -- lets a SECOND
  // dynamic marking be attached partway through an excerpt (see Grade 2's
  // altSecondDynamicChance in buildAlternatingExcerpt) without re-finding
  // and re-stamping the opening bar's marking.
  const idx = lines.findIndex((l, i) => i >= fromIdx && !/^R/.test(l.trim()));
  if (idx === -1) return lines;
  const tokens = lines[idx].split(' ');
  const parts = dynamic.trim().split(/\s+/);
  const first = parts[0];
  if (STANDARD_DYNAMICS.has(first)) {
    let suffix = `\\${first}`;
    if (parts.length > 1) {
      suffix += `_\\markup { \\italic "${parts.slice(1).join(' ')}" }`;
    }
    tokens[0] = `${tokens[0]}${suffix}`;
  } else {
    tokens[0] = `${tokens[0]}_\\markup { \\italic "${dynamic}" }`;
  }
  lines[idx] = tokens.join(' ');
  return lines;
}

// A note is "quarter-note-or-longer" -- the only durations staccato dots
// ever apply to (see gradeParams.js's grade3 comment: every scan example
// with dots leaves its eighth-note runs slurred/undotted regardless).
const STACCATO_MIN_UNITS = NOTE_VALUES.quarter.units;
// 2026-09-09: "rest도 minim rest, crotchet rest, whole bar rest 섞어서" -- the
// two RH rest sizes this grade's book evidence actually shows.
const HALF_UNITS = NOTE_VALUES.half.units;

// 2026-09-04: mutates `tokens` in place, adding LilyPond slur markers `(`
// / `)` around every run of 2+ consecutive notes shorter than a quarter
// note within one bar (`bar` is the matching array of NOTE_VALUES keys).
// Appended directly onto the token string (no space), same convention as
// the staccato mark already does, so e.g. "d''8" becomes "d''8(" and the
// run's last note becomes "e''8)". A single isolated short note (run length
// 1) is left unslurred -- LilyPond slurs need at least two notes to mean
// anything, and a lone eighth surrounded by quarters reads fine on its own.
// `runChance` (2026-09-05, default 1): the per-ELIGIBLE-run chance the slur
// actually gets drawn -- see articulationNoteChance's comment at its call
// site for why this exists (marking literally every single qualifying run,
// every time, read as over-notated when reported directly).
function applySlurs(bar, tokens, runChance = 1) {
  const QUARTER_UNITS = NOTE_VALUES.quarter.units;
  let runStart = -1;
  for (let i = 0; i <= bar.length; i++) {
    const isShort = i < bar.length && NOTE_VALUES[bar[i]].units < QUARTER_UNITS;
    if (isShort && runStart === -1) {
      runStart = i;
    } else if (!isShort && runStart !== -1) {
      const runEnd = i - 1;
      if (runEnd > runStart && Math.random() < runChance) {
        tokens[runStart] += '(';
        tokens[runEnd] += ')';
      }
      runStart = -1;
    }
  }
}

// 2026-09-09: pairs with generateExcerpt's triplet post-process (which
// splits one 'quarter' rhythm entry into three 'tripletEighth' entries).
// `tokens` is still 1:1 with `bar` at this point (applySlurs, called just
// before this, needs that correspondence) -- this collapses each run of 3
// consecutive tripletEighth entries into a single `\tuplet 3/2 { ... }`
// string so the LilyPond source actually notates a bracketed triplet
// instead of 3 plain eighth notes. No-op (returns tokens unchanged, just a
// new array) for any bar with no tripletEighth entries.
function mergeTriplets(bar, tokens) {
  // 2026-09-09: a whole-bar RH rest (see assembleLilyPond's wholeRestBars)
  // collapses that bar's `tokens` down to a single 'R...' token while `bar`
  // itself still lists every original rhythm-key entry -- without this
  // guard, the while loop below would keep walking `bar.length` steps and
  // read `tokens[1]`/`tokens[2]`/... past the array's real length (1),
  // pushing literal `undefined` into the merged output (the exact class of
  // bug already fixed once this session for the phrase-slur/triplet
  // ordering issue). A rest bar has no tripletEighth entries to merge in the
  // first place, so returning `tokens` untouched is always correct here.
  if (tokens.length !== bar.length) return tokens;
  const merged = [];
  let i = 0;
  while (i < bar.length) {
    if (bar[i] === 'tripletEighth' && bar[i + 1] === 'tripletEighth' && bar[i + 2] === 'tripletEighth') {
      merged.push(`\\tuplet 3/2 { ${tokens[i]} ${tokens[i + 1]} ${tokens[i + 2]} }`);
      i += 3;
    } else {
      merged.push(tokens[i]);
      i += 1;
    }
  }
  return merged;
}

// 2026-09-09: "4분의 2박자와 4분의 3박자의 quaver 그룹은 사진대로 2개를 하나로
// 쪼개주고" -- direct feedback with book photos showing every eighth-note run
// in 2/4 and 3/4 beamed strictly in pairs (never a run of 4+ under one beam).
// Tried the same Timing.beatStructure override trick used for 6/8 below
// first, but it turned out unreliable here: confirmed directly by rendering
// a bare `\time 3/4` eighth run with `Timing.beatStructure = #'(2 2 2)` set --
// it still beamed all 6 notes as one continuous group in this LilyPond
// version, while the exact same technique worked fine for 2/4. Rather than
// chase that inconsistency further, this sidesteps the automatic beaming
// engraver entirely with LilyPond's manual beam operators (`[`/`]`), which
// are guaranteed to win regardless of the context's auto-beam settings.
// Walks each bar's run of consecutive eighth-note-or-shorter entries (same
// run definition as applySlurs' legato-slur grouping above) and brackets
// them two at a time; a run with an odd leftover note at the end is left
// that last note unbracketed (a single note can't be beamed to nothing).
// Deliberately scoped to 2/4 and 3/4 only via its call site in
// assembleLilyPond -- 4/4 keeps LilyPond's own default (confirmed separately
// to already group by a half-note pulse, i.e. a natural MIX of 2- and
// 4-note beams depending on run length), which is exactly what was asked
// for there ("4분의 4박자는 quaver 그룹을 2개 4개 섞어서 써도 좋게").
// 2026-09-10: RE-FIXED -- the pairs-of-2 version above was too blunt: its
// eligibility test (`units < QUARTER_UNITS`) matches sixteenth notes
// (units=1) and tripletEighth (units=1) just as much as plain eighths
// (units=2), so it was pairing THOSE two beat-per-beat instead of leaving
// them alone -- reported directly with two screenshots: a run of 4
// sixteenth notes in a Grade 4 3/4 excerpt came out beamed as two separate
// 2-note beams (a visible gap down the middle) instead of one clean 4-note
// beam, and a bracketed triplet came out with its first two notes joined by
// a manual beam and its third note left as a bare unbeamed flag (forced-2
// pairing hit a run of exactly 3 tripletEighth tokens, bracketed the first
// two, and left the odd one out) -- this ALSO ran before mergeTriplets even
// wraps those tokens in `\tuplet 3/2 { ... }`, so the pairing was silently
// fighting the eventual tuplet notation.
//
// Correct rule: group by BEAT, not by "every 2 notes" -- a plain-eighth beat
// (2 eighths = 4 units) still comes out paired (matches the original
// "2/4·3/4 quaver groups split into pairs" request), but a sixteenth-note
// beat (4 sixteenths = 4 units) now comes out as one beam of 4, and any
// tripletEighth token is skipped entirely (left for LilyPond's own default
// auto-beaming inside the `\tuplet` block mergeTriplets builds afterward,
// which beams a tuplet's notes together with no help needed here).
// Cumulative unit offset from the bar's start decides which beat (0-indexed
// quarter-note slot) each eligible note falls in; consecutive eligible notes
// sharing a beat index are bracketed together as one manual beam, a lone
// note in its own beat is left unbracketed (nothing to beam it to) exactly
// as before.
function forceQuaverBeamPairs(bar, tokens) {
  const QUARTER_UNITS = NOTE_VALUES.quarter.units;
  let offset = 0;
  let i = 0;
  while (i < bar.length) {
    const key = bar[i];
    const units = key === 'tripletEighth' ? NOTE_VALUES.tripletEighth.units : NOTE_VALUES[key].units;
    const eligible = key !== 'tripletEighth' && units < QUARTER_UNITS;
    if (!eligible) {
      offset += units;
      i += 1;
      continue;
    }
    // Walk the run of consecutive eligible (sub-quarter, non-triplet) notes,
    // bracketing each beat's worth as its own beam.
    let chunkStart = i;
    let chunkOffset = offset;
    let p = i;
    while (p < bar.length) {
      const k = bar[p];
      const kUnits = k === 'tripletEighth' ? NOTE_VALUES.tripletEighth.units : NOTE_VALUES[k].units;
      if (k === 'tripletEighth' || kUnits >= QUARTER_UNITS) break;
      const beatOfThis = Math.floor(offset / QUARTER_UNITS);
      const beatOfChunkStart = Math.floor(chunkOffset / QUARTER_UNITS);
      if (beatOfThis !== beatOfChunkStart) {
        if (p - 1 > chunkStart) {
          tokens[chunkStart] += '[';
          tokens[p - 1] += ']';
        }
        chunkStart = p;
        chunkOffset = offset;
      }
      offset += kUnits;
      p += 1;
    }
    if (p - 1 > chunkStart) {
      tokens[chunkStart] += '[';
      tokens[p - 1] += ']';
    }
    i = p;
  }
}

// 2026-09-09 CORRECTION: the paragraph below originally claimed 4/4, 3/4,
// and 2/4 all default to a quarter-note beam pulse already. Direct testing
// while chasing the "quaver 그룹은... 2개를 하나로" report (see
// forceQuaverBeamPairs above) showed that's only true for 4/4 -- 2/4 and 3/4
// both actually default to beaming an ENTIRE run of eighths as one group
// with no break at all in this LilyPond version. 2/4 and 3/4 are now fixed
// separately via forceQuaverBeamPairs's manual beam brackets (more reliable
// than fighting Timing.beatStructure here, see its own comment for why); the
// rest of this function's job is unchanged: 6/8, 9/8 stay on their existing
// compound-grouping override below, and 2/2/3/2 get the half-note-pulse fix
// this function was originally written for.
//
// Original note, still accurate for 6/8/9/8 and the 2/2/3/2 fix below:
// LilyPond's automatic beam grouping defaults to a base pulse of
// `1 / (time signature denominator)`. For 6/8, 9/8 that default is already a
// dotted-quarter-ish compound grouping of 3 eighths -- fine as-is. But for
// cut time (2/2) and 3/2, the default pulse is a HALF NOTE, so LilyPond
// happily beams 4 eighths (or more) together in one run --
// technically correct but much harder to read at a glance than the
// quarter-note-based grouping most beginner/intermediate sight-reading
// editions actually use. Confirmed via direct user feedback on generated
// 2/2 excerpts ("리듬이 어느정도 읽을 수 있게 리듬이 그룹화 되었으면") that this was making
// Grade 4's cut-time excerpts read as harder than intended. Fix: explicitly
// override Timing.baseMoment/beatStructure for 2/2 and 3/2 only, forcing
// beams to break every quarter note, and leave every other time signature on
// LilyPond's already-standard defaults.
function beamGroupingOverride(timeSig) {
  if (timeSig === '2/2') {
    return '  \\set Timing.baseMoment = #(ly:make-moment 1/4)\n  \\set Timing.beatStructure = #\'(1 1 1 1)\n';
  }
  if (timeSig === '3/2') {
    return '  \\set Timing.baseMoment = #(ly:make-moment 1/4)\n  \\set Timing.beatStructure = #\'(1 1 1 1 1 1)\n';
  }
  // 2026-09-09: "8분의 6박자에서 한마디 안에서 3박씩 잘라서 보여줘. 리듬그룹 맞춰서" --
  // direct feedback with a screenshot showing a 7-note beam running straight
  // across an entire 6/8 bar with no break at the halfway point. 6/8's two
  // main pulses are each a dotted quarter (3 eighth-note-units), so the beam
  // should always break into two 3-eighth groups, one per pulse -- but nothing
  // here had ever set that explicitly, so it was riding on LilyPond's
  // built-in default for 6/8, which turned out not to reliably force the
  // break for every note mix this engine produces. Set it explicitly, same
  // pattern as the 2/2/3/2 fix above: base pulse = one eighth note, grouped
  // 3+3.
  if (timeSig === '6/8') {
    return '  \\set Timing.baseMoment = #(ly:make-moment 1/8)\n  \\set Timing.beatStructure = #\'(3 3)\n';
  }
  return '';
}

function assembleLilyPond({ gradeLabel, claraAlias, realm, key, timeSig, rhythmBars, pitches, pitchesHarmony, handsTogether, clef = 'treble', bassBars, dynamic, tempoMarking, midMarking, rhStaccato, lhStaccato, bpm, phraseSlurChance, tieAcrossBarChance, articulationNoteChance, rhRestChance, rhWholeBarRestChance, rhAccent, rhTenuto, fermata, sfzMid, tempoChangePair, ornamentsEnabled, ornamentNoteChance, ornamentPool, graceNotePitches }) {
  const realmLabel = realm.charAt(0).toUpperCase() + realm.slice(1);
  const subtitle = `${gradeLabel} — ${realmLabel}`; // claraAlias intentionally dropped from display (2026-08-27)
  const lyMode = key.mode === 'minor' ? '\\minor' : '\\major';
  const tempoLine = tempoMarking ? `  \\tempo "${tempoMarking}"\n` : '';
  // 2026-09-05: "아티큘레이션이 너무 남용되고있어... 발란스 잡아줘" -- staccato
  // dots and legato slurs were each being applied to LITERALLY EVERY single
  // qualifying note/run once their per-excerpt toggle fired, which read as
  // over-marked ("거의 누르는 족족 스타카토"). `articulationNoteChance`
  // (grade3's own param, default 1 here so a bucket that doesn't set it is
  // unaffected) is the per-note/per-run chance an individual mark actually
  // gets drawn once its hand/run is otherwise eligible -- thins the marks out
  // instead of stamping every single one.
  const artChance = articulationNoteChance != null ? articulationNoteChance : 1;
  // 2026-09-15: "Tier B" ornamentation's own per-note draw chance --
  // DELIBERATELY defaults to 0 (not 1, unlike artChance above) when unset.
  // artChance's "defaults to 1" behaviour exists because articulation
  // (staccato/slurs) is meant to mark EVERY eligible note once its
  // excerpt-level toggle fires, thinned only when a bucket explicitly asks
  // for less. Ornaments are the opposite case -- `ornamentsEnabled` alone
  // just means "this piece is allowed to have ornaments at all"; without
  // an explicit ornamentNoteChance a bucket would otherwise get an
  // ornament stamped on literally every quarter-note-or-longer note,
  // which is absurd for a grace note/trill/turn/mordent (these are meant
  // to punctuate a handful of notes per piece, not decorate the whole
  // line).
  const ornNoteChance = ornamentNoteChance != null ? ornamentNoteChance : 0;

  // 2026-09-04: "타이도 바를 넘는 것도 섞어줘" -- pick which interior bar
  // boundaries get a tie BEFORE building any tokens, since a tie means the
  // next bar's first note must be forced to the SAME pitch (and harmony, if
  // chorded) as the previous bar's last note, not whatever melody.js's
  // random walk originally landed on. Excludes ties into the very last bar
  // (barIdx === rhythmBars.length - 1) so this can never fight the
  // forced-tonic-ending cadence (see bass.js/melody.js), and is skipped
  // entirely when the excerpt is staccato (tie = sustain through the
  // barline, staccato = detach -- contradictory on the same note).
  // barRanges[i] = { start, end } are indices into the flat `pitches` array.
  let idxCursor = 0;
  const barRanges = rhythmBars.map((bar) => {
    const start = idxCursor;
    idxCursor += bar.length;
    return { start, end: idxCursor - 1 };
  });
  // 2026-09-09: "rest도 minim rest, crotchet rest, whole bar rest 섞어서" --
  // book photos show plenty of RH rests (a full-bar rest opening one
  // example, a quarter rest right at the start of another, more scattered
  // through the set) that this engine never modeled for the melody line at
  // all before now (bass.js's LH rest support is a separate mechanism).
  // Picked BEFORE tiedBoundaries below, since a tie can't land on a rest --
  // tiedBoundaries must know which boundaries to skip. `rhWholeBarRestChance`
  // (per bar, never the excerpt's last bar so the cadence is never
  // silenced) replaces an entire bar with one full-bar rest; `rhRestChance`
  // (independent per-bar roll, skipped if the whole-bar chance already fired
  // on that bar) replaces ONE note already sized a crotchet or minim with a
  // rest of that same duration, chosen at random among that bar's eligible
  // notes so both sizes actually mix rather than one dominating. Bars
  // containing a triplet are excluded from both -- rare enough to not matter,
  // and avoids having to reason about resting inside a `\tuplet` group.
  const lastBarIdx = rhythmBars.length - 1;
  const wholeRestBars = new Set();
  const partialRestIdx = new Set();
  if (rhRestChance || rhWholeBarRestChance) {
    rhythmBars.forEach((bar, barIdx) => {
      if (barIdx === lastBarIdx) return;
      if (bar.some((k) => k === 'tripletEighth')) return;
      if (rhWholeBarRestChance && Math.random() < rhWholeBarRestChance) {
        wholeRestBars.add(barIdx);
        return;
      }
      if (rhRestChance && Math.random() < rhRestChance) {
        const eligible = [];
        // 2026-09-10: "2, 3박자에 2분쉼표로 같이 묶일 수 없어 2개의 4분쉼표로
        // 나눠야지" -- flagged directly against a rendered 4/4 sample. A
        // single half-REST is only legible when it starts on a strong beat
        // (beat 1 or, in 4/4, beat 3) -- one starting on beat 2 and spanning
        // beats 2-3 hides beat 3's downbeat, which basic notation practice
        // never allows for a rest (unlike a NOTE, which can freely sustain
        // across that same span). This engine has no way to split one
        // rhythm-slot into two rest tokens without reshaping the whole bar,
        // so rather than build that, a half-duration event starting at
        // beat 2 of a 4/4 bar is simply excluded from eligibility here --
        // the mechanism still produces minim rests everywhere else (beat 1,
        // beat 3, or any position in 2/4/3/4, none of which have this
        // hidden-downbeat problem), just never in this one illegal spot.
        let cumUnits = 0;
        bar.forEach((k, i) => {
          const u = NOTE_VALUES[k].units;
          const offset = cumUnits;
          cumUnits += u;
          if (u !== NOTE_VALUES.quarter.units && u !== HALF_UNITS) return;
          if (u === HALF_UNITS && timeSig === '4/4' && offset === NOTE_VALUES.quarter.units) return;
          eligible.push(barRanges[barIdx].start + i);
        });
        if (eligible.length) {
          partialRestIdx.add(eligible[Math.floor(Math.random() * eligible.length)]);
        }
      }
    });
  }
  // Flat-index helper used both here and by the phrase-slur block further
  // down: true when `idx` lands on a rest, whether from a whole-bar rest or
  // a single partial one.
  const isRestIdx = (idx) => {
    const b = barRanges.findIndex((r) => idx >= r.start && idx <= r.end);
    return wholeRestBars.has(b) || partialRestIdx.has(idx);
  };

  const tiedBoundaries = new Set(); // holds barIdx i, meaning bar i's LAST note ties into bar i+1's FIRST note
  if (!rhStaccato && tieAcrossBarChance) {
    for (let i = 0; i < barRanges.length - 2; i++) {
      if (wholeRestBars.has(i) || wholeRestBars.has(i + 1)) continue;
      if (isRestIdx(barRanges[i].end) || isRestIdx(barRanges[i + 1].start)) continue;
      // 2026-09-10: "타이도 이렇게 긴 호흡 위주로 넣어주고" -- direct follow-up
      // with book photos showing a tie ALWAYS landing on an already-long
      // note (a dotted note / a whole note) and reading as one big sustained
      // "breath" across the barline, often under a long phrase-slur arc too
      // -- never a quick two-short-notes tie. Previously this tied whatever
      // note happened to fall last in the bar, eighth notes included, which
      // reads as a re-attack rather than a breath. Gate to only the LAST
      // note of bar i being half-note-or-longer (half/dottedHalf/a whole-bar
      // note) so every tie this fires extends a genuinely long note, not a
      // short one.
      const lastBarKey = rhythmBars[i][rhythmBars[i].length - 1];
      const lastUnits = lastBarKey === 'tripletEighth' ? 0 : NOTE_VALUES[lastBarKey].units;
      if (lastUnits < HALF_UNITS) continue;
      if (Math.random() < tieAcrossBarChance) tiedBoundaries.add(i);
    }
  }
  const pitchesForRender = pitches.slice();
  const harmonyForRender = pitchesHarmony ? pitchesHarmony.slice() : null;
  tiedBoundaries.forEach((i) => {
    const lastIdx = barRanges[i].end;
    const firstIdxNext = barRanges[i + 1].start;
    pitchesForRender[firstIdxNext] = pitchesForRender[lastIdx];
    if (harmonyForRender) harmonyForRender[firstIdxNext] = harmonyForRender[lastIdx];
  });

  // Right hand: consume pitches in order, one per rhythm event. When
  // `pitchesHarmony` is set (2026-09-03's "RH block chords" feature -- see
  // its call site in generateExcerpt), the matching harmony note is stacked
  // onto the main pitch as a LilyPond chord `<...>` instead of a bare note.
  // `rhStaccato` (also 2026-09-03) dots every note EXCEPT eighth-or-shorter
  // ones, per STACCATO_MIN_UNITS above.
  let pi = 0;
  const rhTokensByBar = rhythmBars.map((bar, barIdx) => {
    // 2026-09-09: a whole-bar rest prints as ONE `R<dur>` token for the
    // entire bar (LilyPond auto-centers it, same FULL_BAR_REST table
    // bass.js's own whole-bar rests use) instead of one token per rhythm
    // event -- still advance `pi` by the bar's full note count first, so
    // every LATER bar's flat pitch-index math (tiedBoundaries, the
    // phrase-slur block below) stays aligned exactly as if this bar had
    // rendered normally.
    if (wholeRestBars.has(barIdx)) {
      const totalUnits = bar.reduce((s, k) => s + NOTE_VALUES[k].units, 0);
      pi += bar.length;
      return [FULL_BAR_REST[totalUnits] || 'R1'];
    }
    const tokens = bar.map((noteKey) => {
      const idx = pi++;
      if (partialRestIdx.has(idx)) {
        return `r${NOTE_VALUES[noteKey].ly}`;
      }
      const pitch = pitchesForRender[idx];
      const harmony = harmonyForRender ? harmonyForRender[idx] : null;
      const pitchToken = harmony ? `<${pitch} ${harmony}>` : pitch;
      const staccatoMark = rhStaccato && NOTE_VALUES[noteKey].units >= STACCATO_MIN_UNITS && Math.random() < artChance ? '-.' : '';
      const tieMark = tiedBoundaries.has(barIdx) && idx === barRanges[barIdx].end ? '~' : '';
      // 2026-09-14: "Tier A" expressive markings (accent/tenuto) -- see
      // gradeParams.js's grade6/7/8 comments for the full rationale. Both
      // are per-excerpt toggles (rhAccent/rhTenuto, mirroring rhStaccato's
      // own on/off + per-note artChance pattern) rather than always-on,
      // and both are mutually exclusive with staccato on the same note
      // (a dot AND an accent/tenuto wedge stacked on one notehead is a
      // real notational contradiction -- staccato says "detach", tenuto
      // says "hold the full value", an accent can still combine with
      // either in real notation but keeping this engine's articulation
      // marks one-per-note avoids visual clutter). An accent lands only on
      // a bar's FIRST note (the natural downbeat stress point) and only if
      // it's quarter-note-or-longer (an accent on a fast eighth-note run
      // reads as noise, same duration floor STACCATO_MIN_UNITS already
      // uses). A tenuto lands only on a bar's LAST note, half-note-or-
      // longer, and never on a note that's already tied into the next bar
      // (a tie already communicates "hold this through" -- a tenuto wedge
      // on top would be redundant).
      const isFirstOfBar = idx === barRanges[barIdx].start;
      const isLastOfBar = idx === barRanges[barIdx].end;
      const accentMark = !staccatoMark && rhAccent && isFirstOfBar
        && NOTE_VALUES[noteKey].units >= STACCATO_MIN_UNITS && Math.random() < artChance ? '->' : '';
      const tenutoMark = !staccatoMark && !accentMark && rhTenuto && isLastOfBar
        && !tiedBoundaries.has(barIdx) && NOTE_VALUES[noteKey].units >= HALF_UNITS && Math.random() < artChance ? '--' : '';
      // 2026-09-15: "Tier B" ornamentation (grace notes / trill / turn /
      // mordent) -- see gradeParams.js's grade6/7/8 comments for the full
      // rationale. Gated OFF any note that already carries a Tier A mark
      // (staccato/accent/tenuto) -- same "one articulation-family mark per
      // note" discipline Tier A itself already follows, avoiding a
      // notehead stacked with e.g. both an accent wedge AND a trill zigzag.
      // Same quarter-note-or-longer floor as accent/staccato (an
      // ornament on a fast eighth-note run has no room to actually sound
      // and just reads as clutter). `ornamentPool` is a weighted array
      // (mirrors mixedStylePool's own weighting convention in
      // gradeParams.js) so a bucket can lean toward trills over grace
      // notes or vice versa; `pick` (module-level, same helper
      // midPieceMarkings/tempoChangePairs already use) draws one entry.
      // Trill/turn/mordent are pure LilyPond postfix marks (`\trill`,
      // `\turn`, `\mordent`) needing no extra data; a grace note instead
      // needs a real precomputed diatonic pitch (graceNotePitches, built
      // in generateExcerpt) rendered as a LilyPond acciaccatura PREFIX
      // (`\acciaccatura { <pitch>8 } `) in front of the main note --
      // skipped gracefully (no mark at all) if that pitch array wasn't
      // built for this excerpt.
      let ornamentPrefix = '';
      let ornamentMark = '';
      const ornamentEligible = !staccatoMark && !accentMark && !tenutoMark
        && NOTE_VALUES[noteKey].units >= STACCATO_MIN_UNITS;
      if (ornamentsEnabled && ornamentEligible && ornamentPool && ornamentPool.length && Math.random() < ornNoteChance) {
        const kind = pick(ornamentPool);
        if (kind === 'trill') ornamentMark = '\\trill';
        else if (kind === 'turn') ornamentMark = '\\turn';
        else if (kind === 'mordent') ornamentMark = '\\mordent';
        else if (kind === 'grace' && graceNotePitches && graceNotePitches[idx]) {
          ornamentPrefix = `\\acciaccatura { ${graceNotePitches[idx]}8 } `;
        }
      }
      return `${ornamentPrefix}${pitchToken}${NOTE_VALUES[noteKey].ly}${staccatoMark}${accentMark}${tenutoMark}${ornamentMark}${tieMark}`;
    });
    // 2026-09-04: "articulation/tie/slur don't show up" -- staccato dots
    // were already wired up (see rhStaccato above), but a slur curve was
    // never actually drawn over the legato runs. The staccato calibration
    // comment (gradeParams.js grade3) already established that eighth-note-
    // or-shorter runs stay legato/slurred on the real page REGARDLESS of
    // whether the excerpt's quarter+ notes are dotted -- this was only ever
    // implemented as "no dot" (implicit legato), never as a drawn slur.
    // Wrap each run of 2+ consecutive shorter-than-quarter notes within a
    // bar in a real LilyPond slur `( )` so it reads as an explicit phrase
    // mark, not just an absence of dots. Scoped to within a single bar
    // (never crosses the `|` bar check) since that's exactly the unit the
    // evidence describes ("every eighth-note run").
    applySlurs(bar, tokens, artChance);
    // 2026-09-09: see forceQuaverBeamPairs's own comment -- 2/4 and 3/4
    // only, forces every consecutive eighth-note run into strict pairs
    // rather than trusting LilyPond's own (here unreliable) auto-beaming.
    if (timeSig === '2/4' || timeSig === '3/4') {
      forceQuaverBeamPairs(bar, tokens);
    }
    return tokens;
  });

  // 2026-09-04: "긴 호흡의 프레이징 성격의 slur" -- a longer, phrase-level
  // slur spanning roughly each half of the piece, layered ON TOP OF the
  // short legato slurs above using LilyPond's separate PHRASING slur symbol
  // (`\( \)`, distinct from the plain `( )` slur) specifically so the two
  // can nest/overlap without colliding. Splits the piece into two halves at
  // the midpoint bar; a no-op for anything shorter than 4 bars, where a
  // "breath in the middle" split isn't a meaningful gesture.
  // 2026-09-05: also skip entirely when rhStaccato is on ("이거 다 뭔가 말이
  // 안되는데" -- a phrase slur that starts or ends ON a dotted/staccato note
  // is a real notational contradiction: the slur says "sustain through this
  // phrase," the dot right under/over the very same notehead says "detach
  // it." tieAcrossBarChance already had this same staccato guard; the
  // phrase slur never did, so a staccato excerpt could still get one drawn
  // squarely across its dotted quarters.
  if (phraseSlurChance && !rhStaccato && rhythmBars.length >= 4 && Math.random() < phraseSlurChance) {
    const totalNotes = pi;
    const midBar = Math.floor(rhythmBars.length / 2);
    const midIdx = barRanges[midBar - 1].end;
    if (totalNotes > midIdx + 1) {
      const tokenAt = (idx) => {
        const b = barRanges.findIndex((r) => idx >= r.start && idx <= r.end);
        return rhTokensByBar[b][idx - barRanges[b].start];
      };
      const setTokenAt = (idx, mark) => {
        const b = barRanges.findIndex((r) => idx >= r.start && idx <= r.end);
        rhTokensByBar[b][idx - barRanges[b].start] += mark;
      };
      // 2026-09-05: "아래 슬러가 중복되지 않게" -- the phrase slur's own
      // start/end note could land on the SAME note that a short legato-run
      // slur (applySlurs, above) already opens or closes on, anchoring two
      // separate curves to the identical notehead -- reads as one doubled/
      // overlapping line rather than two distinct marks. Nudge each
      // endpoint inward, note by note, until it lands on a note with no
      // existing slur boundary mark; skip drawing that half entirely (rare)
      // if the whole span turns out to be nothing but slur-boundary notes.
      // 2026-09-09: a rest (whole-bar or partial, see isRestIdx above) can
      // never anchor a phrase slur -- a slur curve starting or ending on a
      // rest is a notational contradiction, same reasoning as the
      // staccato/tie guards elsewhere in this function. `isRestIdx(s)` is
      // checked BEFORE `tokenAt(s)` in each condition below (JS `||`
      // short-circuits left-to-right) specifically so `tokenAt` is never
      // even called for an index inside a whole-rest bar -- that bar's
      // `rhTokensByBar` entry is a single collapsed token, so indexing it
      // at anything past its start would read past the array's real length.
      const applyPhraseSlur = (startIdx, endIdx) => {
        let s = startIdx;
        while (s <= endIdx && (isRestIdx(s) || /[()]$/.test(tokenAt(s)))) s++;
        let e = endIdx;
        while (e >= s && (isRestIdx(e) || /[()]$/.test(tokenAt(e)))) e--;
        if (e <= s) return;
        setTokenAt(s, '\\(');
        setTokenAt(e, '\\)');
      };
      applyPhraseSlur(0, midIdx);
      applyPhraseSlur(midIdx + 1, totalNotes - 1);
    }
  }

  // 2026-09-09: merging triplet-trio tokens (see mergeTriplets) must happen
  // AFTER the phrase-slur block above, not inside the rhTokensByBar map --
  // that block indexes rhTokensByBar by the ORIGINAL flat pitch position via
  // `barRanges` (built from the unmerged rhythmBars), so merging earlier
  // shrinks each affected bar's token array and desyncs those indices,
  // producing an out-of-bounds `undefined` token (seen as a literal
  // "undefined" string in the LilyPond source, then a barcheck failure).
  rhythmBars.forEach((bar, barIdx) => {
    rhTokensByBar[barIdx] = mergeTriplets(bar, rhTokensByBar[barIdx]);
  });
  const rhLines = rhTokensByBar.map((tokens) => tokens.join(' ') + ' |');
  attachDynamic(rhLines, dynamic);
  attachMidMarking(rhLines, midMarking);
  attachTempoChangePair(rhLines, tempoChangePair);
  attachSfz(rhLines, sfzMid);
  attachFermata(rhLines, fermata);

  let lhLines = null;
  if (handsTogether && bassBars) {
    lhLines = bassBars.map((events) => {
      const tokens = [];
      events.forEach((ev) => {
        tokens.push(...bassEventTokens(ev, lhStaccato, artChance));
      });
      return tokens.join(' ') + ' |';
    });
  }

  // Apply forced line breaks AFTER attachDynamic/attachMidMarking (which scan for the first
  // non-rest bar by content -- a stray `\break` element earlier in the
  // array could otherwise be mistaken for a note line) and to both staves
  // at the SAME bar boundaries, so the two hands stay vertically aligned.
  const rhLinesBroken = withLineBreaks(rhLines);
  const lhLinesBroken = lhLines ? withLineBreaks(lhLines) : null;

  const header = headerBlock(subtitle);

  // NOTE: pitches produced by scales.js/toLilyPitch already carry full
  // absolute-style octave marks (e.g. "c''"), so these blocks are written
  // in LilyPond's default *absolute* pitch mode -- deliberately NOT wrapped
  // in \relative, since relative octave marks would be reinterpreted
  // relative to the previous note and produce wrong registers.
  const melodyDef = `melody = {
  \\key ${key.ly} ${lyMode}
  \\time ${timeSig}
${beamGroupingOverride(timeSig)}${tempoLine}${rhLinesBroken.map((l) => '  ' + l).join('\n')}
  \\bar "|."
}
`;

  if (!handsTogether) {
    return {
      lySource: `${header}
${melodyDef}
${scoreBlock({ view: 'both', hasBass: false, timeSig, bpm, clef })}`,
      lySourceTreble: null,
      lySourceBass: null,
    };
  }

  const bassDef = `bassLine = {
  \\key ${key.ly} ${lyMode}
  \\time ${timeSig}
${beamGroupingOverride(timeSig)}${(lhLinesBroken || []).map((l) => '  ' + l).join('\n')}
  \\bar "|."
}
`;

  const defs = `${melodyDef}\n${bassDef}`;

  return {
    lySource: `${header}\n${defs}\n${scoreBlock({ view: 'both', hasBass: true, timeSig, bpm })}`,
    lySourceTreble: `${header}\n${defs}\n${scoreBlock({ view: 'treble', hasBass: true, timeSig, bpm })}`,
    lySourceBass: `${header}\n${defs}\n${scoreBlock({ view: 'bass', hasBass: true, timeSig, bpm })}`,
  };
}

// 2026-08-27: shared header+paper block for a minimal, uncluttered look --
// a plain sans-serif title (not the heavy default bold serif) with a
// smaller, muted-gray subtitle underneath. `subtitle` is always one of our
// own "<Grade> — <Realm>" strings, never user input, so no escaping is
// needed beyond what already worked for the old plain-string \header
// fields.
//
// 2026-08-27: the title/subtitle font is set with a plain \override
// directly on each markup, NOT via \paper's `#(define fonts
// (make-pango-font-tree ...))` mechanism -- that Scheme function turned out
// to be unbound on at least one real user's LilyPond install (a build
// without the same font-tree API this sandbox's LilyPond has), which made
// EVERY excerpt fail to compile at all. The inline \override achieves the
// same visible font change and doesn't depend on that API, so it works
// across LilyPond builds; the only cost is that a couple of other default
// text elements elsewhere on the page (a one-hand grade's "Piano"
// instrument label, tempo markings) stay in LilyPond's default font
// instead of matching -- a minor cosmetic concession for not breaking
// generation entirely on some installs.
function headerBlock(subtitle) {
  // 2026-09-15: declared as 2.24.1, not this sandbox's 2.24.3, because the
  // Dockerfile's `apt-get install lilypond` on node:20-bookworm-slim only
  // gets Debian bookworm's packaged 2.24.1 -- LilyPond refuses to compile
  // a file declaring a newer \version than the binary running it ("program
  // too old"). See lilypondCompiler.js's matching 2026-09-15 comment.
  return `\\version "2.24.1"

\\header {
  title = \\markup { \\override #'(font-name . "Liberation Sans") \\fontsize #2 \\normal-text "Sight-Reading Excerpt" }
  subtitle = \\markup { \\override #'(font-name . "Liberation Sans") \\fontsize #-1 \\normal-text \\with-color #(x11-color 'gray40) "${subtitle}" }
  tagline = ##f
}

\\paper {
  indent = 0
  ragged-bottom = ##t
  ragged-right = ##t
  top-margin = 6\\mm
  bottom-margin = 6\\mm
  left-margin = 8\\mm
  right-margin = 8\\mm
}
`;
}

// 2026-08-27: the "\\score { ... }" wrapper, parameterized by which staff/
// staves to show -- 'both' (the real piece, used for the download PDF and
// audio), 'treble' (right hand alone), 'bass' (left hand alone). The
// treble/bass single-staff views are for READING PRACTICE ONLY (a student
// isolating one hand's line) -- they reuse the exact same `melody`/
// `bassLine` defs as the full score, so there's no risk of the isolated
// view ever showing different notes than the real piece. Only the 'both'
// view carries a \\midi block, since that's the only view tied to the
// audio player.
function scoreBlock({ view, hasBass, timeSig, bpm, clef = 'treble' }) {
  if (view === 'treble') {
    return `\\score {
  \\new Staff {
    \\clef treble
    \\melody
  }
  ${LAYOUT_BLOCK}
}
`;
  }
  if (view === 'bass') {
    return `\\score {
  \\new Staff {
    \\clef bass
    \\bassLine
  }
  ${LAYOUT_BLOCK}
}
`;
  }
  if (!hasBass) {
    return `\\score {
  \\new Staff \\with { instrumentName = "Piano" } {
    \\clef ${clef}
    \\melody
  }
  ${LAYOUT_BLOCK}${midiBlock(timeSig, bpm)}
}
`;
  }
  return `\\score {
  \\new PianoStaff <<
    \\new Staff = "right" {
      \\clef treble
      \\melody
    }
    \\new Staff = "left" {
      \\clef bass
      \\bassLine
    }
  >>
  ${LAYOUT_BLOCK}${midiBlock(timeSig, bpm)}
}
`;
}

// Full-bar rest / full-bar single-note tokens for each supported time
// signature's total sixteenth-unit length. LilyPond's "R<duration>" is a
// multi-measure rest marker; for a single bar it just needs to match that
// bar's total duration. The note-token table is the same durations without
// the "R" prefix, used for the single-note cadence bar.
// 2026-09-11: BUG FIX -- 9/8 (18 units) had no entry here, so both tables
// silently fell back to their `|| 'R1'` / `|| '1'` default (a PLAIN WHOLE
// NOTE, 16 units), which is 2 units (one eighth note) SHORT of a real 9/8
// bar's 18-unit length. Every whole-bar rest/held-note drawn in a 9/8
// excerpt was therefore under-filling its bar by exactly one eighth note --
// LilyPond's own bar-check then silently resyncs at the next barline,
// which is what produced the broken-looking output reported directly
// (screenshot: a 9/8 "Allegretto" excerpt rendering several near-empty
// systems with just one stray note and no bar number, instead of a normal
// 4-bars-per-line layout) -- NOT a rhythm-complexity issue, a genuine
// under-length-token bug that only 9/8 excerpts could ever trigger (the
// other 4 supported time sigs -- 4/4, 3/4, 2/4, 6/8 -- all already had
// exact entries). `R1*9/8` is LilyPond's own multi-measure-rest scaling
// syntax (a whole rest's duration multiplied by 9/8), which is the
// standard way to notate a rest/note whose length isn't a plain power-of-
// two duration; verified by direct render (a 9/8 excerpt with both a rest
// bar and a held-note bar) showing correct 4-bar systems with no more
// stray fragments.
// 2026-09-14: grade7 uses 3/2 (24 units) and 5/4 (20 units), neither of
// which had an entry here -- the exact same missing-entry bug already fixed
// for grade5's 9/8 (18 units) above, just not yet discovered for grade7
// because it hadn't been individually screenshot-checked yet. Found via a
// proactive audit across all grade buckets rather than waiting for another
// broken-layout report. 24 units = a dotted whole note (16 * 1.5), which
// LilyPond can express directly as a plain duration ('1.'/'R1.'). 20 units
// (16 * 5/4) isn't a plain dotted/double-dotted duration, so it uses the
// same scaled-multiplier syntax as 9/8's 18-unit entry ('1*5/4'/'R1*5/4').
const FULL_BAR_REST = { 16: 'R1', 12: 'R2.', 8: 'R2', 18: 'R1*9/8', 24: 'R1.', 20: 'R1*5/4' };
const FULL_BAR_NOTE_LY = { 16: '1', 12: '2.', 8: '2', 18: '1*9/8', 24: '1.', 20: '1*5/4' };

/**
 * "Hands alternating" sight-reading format: ONE melodic line (not
 * melody+accompaniment) that hands off between clefs -- one hand plays,
 * rests; the other picks up an octave away. Never simultaneous. Calibrated
 * against scanned AMEB sight-reading book pages:
 *   - Grade 1 (2026-09-07 re-scan, 13/13 examples -- supersedes the earlier
 *     8-example scan): within a single excerpt, segments are always the
 *     SAME length as each other (echoed rhythm), but that shared length
 *     varies piece to piece -- 2 bars most often, 3 bars fairly often, 4
 *     bars rarely (params.altSegBars=[[2,2],[3,3],[4,4]] with
 *     altSegBarsWeights). RH leads most often but not always -- 3 of the 11
 *     alternating-hand examples opened with LH (params.altFirstHand='either').
 *     2 of the 13 examples (Ex12, Ex13) weren't alternating at all -- one
 *     hand plays a plain single-hand line for the whole excerpt with the
 *     other tacet throughout; this shape isn't modeled here yet.
 *   - Grade 2 (3/3 examples): looser -- segments run 1-3 bars unevenly, and
 *     either hand may lead (params.altSegBars=[1,3], altFirstHand='either').
 *     Since segment lengths vary, rhythm is generated independently per
 *     segment rather than echoed.
 *   - Shapes seen: 2 segments, 2 segments + a single long cadence note in
 *     the closing hand, or 3 segments (a restatement of the opener).
 */
function buildAlternatingExcerpt({ gradeLabel, claraAlias, realm, key, keyId, timeSig, barUnits, params, dynamic, tempoMarking, bpm }) {
  // 2026-09-04, see gradeParams.js's BEAT_UNITS comment.
  const beatUnits = BEAT_UNITS[timeSig] || 4;
  // 2026-09-07: params.altSegBars now also accepts an ARRAY OF [min,max]
  // pairs (instead of a single pair) so a grade can vary its segment length
  // excerpt-to-excerpt while keeping each individual excerpt's segments
  // symmetric -- e.g. Grade 1's re-scan (13 examples) showed segments are
  // always the same length as each other within one excerpt (2+2, 3+3,
  // 4+4, or 2+2+2), but that shared length itself varies piece to piece
  // (2-bar most common, 3-bar fairly common, 4-bar rare). A plain
  // [minSeg,maxSeg] pair (e.g. [2,3]) can't express this: it would make
  // echoRhythm false below and let segments mismatch in length within a
  // single excerpt, which the evidence never showed. altSegBarsWeights
  // (parallel array) picks among the pairs; omit for uniform odds.
  const segBarsRaw = params.altSegBars || [2, 2];
  const segBarsPair = Array.isArray(segBarsRaw[0])
    ? weightedChoice(segBarsRaw, params.altSegBarsWeights || segBarsRaw.map(() => 1))
    : segBarsRaw;
  const [minSeg, maxSeg] = segBarsPair;
  const echoRhythm = minSeg === maxSeg; // only valid when every segment is the same length
  const firstHand = params.altFirstHand === 'either' ? (Math.random() < 0.5 ? 'treble' : 'bass') : 'treble';
  const otherHand = (h) => (h === 'treble' ? 'bass' : 'treble');

  // 2026-08-27: segment-count distribution and cadence chance are now
  // per-grade params (altSegmentCounts/altSegmentWeights/altCadenceChance)
  // instead of one hardcoded 55%/45% split shared by every alternating-hand
  // grade -- see gradeParams.js's prelim/grade1 comments. Defaults below
  // exactly reproduce the old shared behavior for any bucket that doesn't
  // set these explicitly (e.g. Grade 2+).
  const segmentCounts = params.altSegmentCounts || [2, 3];
  const segmentWeights = params.altSegmentWeights || (segmentCounts.length === 2 ? [0.55, 0.45] : segmentCounts.map(() => 1));
  const numSegments = weightedChoice(segmentCounts, segmentWeights);
  const cadenceChance = params.altCadenceChance != null ? params.altCadenceChance : 0.5;
  const needsCadence = numSegments === 2 && Math.random() < cadenceChance;

  // 2026-09-07: Grade 2's re-scan (SR G2.pdf, 12 clean examples) showed
  // staccato dots used within alternating-hand excerpts, something no
  // earlier calibration had -- 3/12 examples (Ex3, 4, 10), and unlike
  // Grade 3+'s staccato (quarter-note-or-longer only, see
  // STACCATO_MIN_UNITS), Grade 2's dots reached down onto eighth notes too.
  // altStaccatoChance (per-excerpt) gates the whole piece, same shape as
  // rhStaccato/lhStaccato in the hands-together path; altStaccatoMinUnits
  // (defaults to STACCATO_MIN_UNITS if unset) lets a grade lower that floor
  // instead of sharing grade3's quarter-note threshold.
  const staccato = !!(params.altStaccatoChance && Math.random() < params.altStaccatoChance);
  const staccatoMinUnits = params.altStaccatoMinUnits != null ? params.altStaccatoMinUnits : STACCATO_MIN_UNITS;

  const restToken = FULL_BAR_REST[barUnits] || 'R1';
  const trebleLines = [];
  const bassLines = [];
  // Records where each segment's line begins in its hand's array (and which
  // hand), so an optional SECOND dynamic marking (altSecondDynamicChance)
  // can be stamped onto a later segment's opening bar without re-finding
  // the very first (already-marked) bar -- see the attachDynamic fromIdx
  // param this recalibration added.
  const segmentStarts = [];

  // For the echo case (Grade 1), every segment reuses one shared rhythm
  // shape; otherwise each segment gets its own independently-generated
  // rhythm at its own (possibly different) bar length.
  const sharedRhythm = echoRhythm ? generateRhythm(minSeg, barUnits, params.noteValues, beatUnits) : null;

  let barCount = 0;
  let lastHand = firstHand;
  // Absolute scale-degree the PREVIOUS segment actually ended on -- null
  // for the opening segment (which still starts at the window's default
  // "mid", same as before). Every call shares the same flat scale array
  // for this key (see scales.js), so this index is directly comparable
  // across segments/hands even though each hand has its own register
  // window. See melody.js's startDegree doc comment for why this matters:
  // without it, each new hand-off segment restarted from its own fixed
  // middle position regardless of where the melody actually was.
  let lastDegree = null;

  for (let i = 0; i < numSegments; i++) {
    const hand = i % 2 === 0 ? firstHand : otherHand(firstHand);
    segmentStarts.push({ idx: hand === 'treble' ? trebleLines.length : bassLines.length, hand });
    const segBars = echoRhythm ? minSeg : randRange(minSeg, maxSeg);
    const rhythm = echoRhythm ? sharedRhythm : generateRhythm(segBars, barUnits, params.noteValues, beatUnits);
    const noteCount = rhythm.reduce((s, b) => s + b.length, 0);
    const registerShift = hand === 'treble' ? 0 : -1;
    // Only the truly last note of the whole excerpt should be forced onto
    // the tonic (see melody.js's endOnTonic) -- that's this segment's last
    // note only when it's the final segment AND no separate cadence bar
    // follows it (the cadence branch below handles that case instead).
    const isFinalSegment = i === numSegments - 1 && !needsCadence;
    // avoidOverlapPad=false: alternating hands never sound at once, so the
    // hand-overlap-avoidance pad (which can push a narrow window's tonic
    // out of reach for endOnTonic) doesn't apply here -- see melody.js.
    const melody = generateMelody(noteCount, params, keyId, registerShift, 0, isFinalSegment, lastDegree, false);
    lastDegree = melody.degrees[melody.degrees.length - 1];

    let idx = 0;
    rhythm.forEach((bar) => {
      const tokens = bar.map((noteKey) => {
        const mark = staccato && NOTE_VALUES[noteKey].units >= staccatoMinUnits ? '-.' : '';
        return `${melody.pitches[idx++]}${NOTE_VALUES[noteKey].ly}${mark}`;
      });
      const line = tokens.join(' ') + ' |';
      if (hand === 'treble') {
        trebleLines.push(line);
        bassLines.push(restToken + ' |');
      } else {
        bassLines.push(line);
        trebleLines.push(restToken + ' |');
      }
    });

    barCount += segBars;
    lastHand = hand;
  }

  if (needsCadence) {
    // One extra bar: a single long note continuing from whichever hand
    // played last, matching e.g. Grade 1 example 1's closing whole note.
    // Generate it as a single note starting from the previous segment's
    // actual last degree (lastDegree) so it resolves to the tonic from
    // wherever the melody really left off, rather than restarting from a
    // fresh, unrelated phrase and only keeping its final note.
    const cadenceLy = FULL_BAR_NOTE_LY[barUnits] || '1';
    const registerShift = lastHand === 'treble' ? 0 : -1;
    const extended = generateMelody(1, params, keyId, registerShift, 0, true, lastDegree, false);
    const cadencePitch = extended.pitches[0];
    if (lastHand === 'treble') {
      trebleLines.push(`${cadencePitch}${cadenceLy} |`);
      bassLines.push(restToken + ' |');
    } else {
      bassLines.push(`${cadencePitch}${cadenceLy} |`);
      trebleLines.push(restToken + ' |');
    }
    barCount += 1;
  }

  // 2026-08-31: total bar count should always be even (see randEvenRange's
  // doc comment for why) -- but this branch's length comes from summing
  // independently-randomized segment lengths (plus an optional single-bar
  // cadence), so unlike the hands-together branch there's no single range
  // to just pick an even number from. Simplest fix: if the sum came out
  // odd, tack on ONE more bar continuing whichever hand played last, ending
  // (again) on the tonic -- a small harmless cadential echo rather than
  // leaving a lone odd bar dangling on its own line under the forced
  // 4-bars-per-line breaking.
  if (barCount % 2 !== 0) {
    const extraRhythm = generateRhythm(1, barUnits, params.noteValues, beatUnits);
    const extraNoteCount = extraRhythm[0].length;
    const registerShift = lastHand === 'treble' ? 0 : -1;
    const extraMelody = generateMelody(extraNoteCount, params, keyId, registerShift, 0, true, lastDegree, false);
    const tokens = extraRhythm[0].map((noteKey, idx) => `${extraMelody.pitches[idx]}${NOTE_VALUES[noteKey].ly}`);
    const line = tokens.join(' ') + ' |';
    if (lastHand === 'treble') {
      trebleLines.push(line);
      bassLines.push(restToken + ' |');
    } else {
      bassLines.push(line);
      trebleLines.push(restToken + ' |');
    }
    barCount += 1;
  }

  // Attach the dynamic to whichever staff plays the very first note (the
  // other staff's opening bars are all rests, so attachDynamic's
  // rest-skipping search would otherwise land on that hand's later
  // entrance instead of bar 1).
  const dynamicTarget = firstHand === 'treble' ? trebleLines : bassLines;
  attachDynamic(dynamicTarget, dynamic);

  // 2026-09-07: Grade 2's re-scan also showed a dynamic marking sometimes
  // CHANGES partway through a piece (Ex8: "loud" ... later "soft") rather
  // than being set once at the opening note -- altSecondDynamicChance
  // (light evidence, 1/12 examples) optionally stamps a second, independently
  // -picked word onto a later segment's opening bar via attachDynamic's
  // fromIdx param, on the segment's own hand (which may differ from the
  // opening hand).
  if (params.dynamics && params.altSecondDynamicChance && numSegments > 1 && Math.random() < params.altSecondDynamicChance) {
    const laterSegments = segmentStarts.slice(1);
    const target = laterSegments[Math.floor(Math.random() * laterSegments.length)];
    const secondDynamic = pick(params.dynamics);
    const targetLines = target.hand === 'treble' ? trebleLines : bassLines;
    attachDynamic(targetLines, secondDynamic, target.idx);
  }

  // Same forced-line-break treatment as assembleLilyPond (see
  // withLineBreaks' doc comment) -- applied after attachDynamic, at
  // identical bar-index boundaries in both staves so treble/bass stay
  // aligned even though only one of them is actually sounding in most bars.
  const trebleLinesBroken = withLineBreaks(trebleLines);
  const bassLinesBroken = withLineBreaks(bassLines);

  const realmLabel = realm.charAt(0).toUpperCase() + realm.slice(1);
  const subtitle = `${gradeLabel} — ${realmLabel}`; // claraAlias intentionally dropped from display (2026-08-27)
  const lyMode = key.mode === 'minor' ? '\\minor' : '\\major';
  const tempoLine = tempoMarking ? `  \\tempo "${tempoMarking}"\n` : '';

  const header = headerBlock(subtitle);
  const defs = `melody = {
  \\key ${key.ly} ${lyMode}
  \\time ${timeSig}
${beamGroupingOverride(timeSig)}${tempoLine}${trebleLinesBroken.map((l) => '  ' + l).join('\n')}
  \\bar "|."
}

bassLine = {
  \\key ${key.ly} ${lyMode}
  \\time ${timeSig}
${beamGroupingOverride(timeSig)}${bassLinesBroken.map((l) => '  ' + l).join('\n')}
  \\bar "|."
}
`;

  const lySource = `${header}\n${defs}\n${scoreBlock({ view: 'both', hasBass: true, timeSig, bpm })}`;
  const lySourceTreble = `${header}\n${defs}\n${scoreBlock({ view: 'treble', hasBass: true, timeSig, bpm })}`;
  const lySourceBass = `${header}\n${defs}\n${scoreBlock({ view: 'bass', hasBass: true, timeSig, bpm })}`;

  return { lySource, lySourceTreble, lySourceBass, barCount };
}

// Bass pitches from scales.js already come as { ly, octaveOffset } objects;
// bass.js currently stores the *entry* itself under `.pitch`, so we need to
// turn that back into a LilyPond token here in one place.
function lyOctaveMarks(pitchEntry) {
  const rel = pitchEntry.octaveOffset;
  if (rel > 0) return "'".repeat(rel);
  if (rel < 0) return ','.repeat(-rel);
  return '';
}

module.exports = { generateExcerpt, REALMS };
