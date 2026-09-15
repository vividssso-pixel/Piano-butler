// ---------------------------------------------------------------------------
// Rhythm generation: fills a single bar with a sequence of note values drawn
// from the grade's allowed set, exactly summing to the bar length.
// ---------------------------------------------------------------------------

const { NOTE_VALUES } = require('./gradeParams');

function weightedPick(candidates) {
  // candidates: [{ key, weight }]
  const total = candidates.reduce((s, c) => s + c.weight, 0);
  let r = Math.random() * total;
  for (const c of candidates) {
    if (r < c.weight) return c.key;
    r -= c.weight;
  }
  return candidates[candidates.length - 1].key;
}

// ---------------------------------------------------------------------------
// 2026-09-09: "이 복잡한 3개 리듬 비스무리한건 없애자" -- direct feedback (3
// cropped screenshots) on a freshly-generated 6/8 "Daintily" excerpt,
// pointing at 3 specific beam shapes that still read as too busy even after
// the subBeatUnits straddle fix above: (1) an alternating eighth-sixteenth-
// eighth-sixteenth run (4 notes, uneven, gapped secondary beam), and (2) a
// 5-note run -- either "eighth + four sixteenths" or "four sixteenths +
// eighth" -- filling a whole 6/8 beat under one continuous beam.
//
// Root cause: the general per-note algorithm below picks one note at a time
// and only checks the short-run cap AFTER the fact. Within a single 6-unit
// 6/8 beat, once a few odd-sized notes (an eighth, some sixteenths) have
// already been placed, the leftover gap is sometimes only 1-2 units with no
// quarter-or-longer duration legally able to start there (mid-beat) --
// so the cap logic's own "prefer a longer note" fallback has nothing to
// fall back to, and it's forced to keep adding sixteenths past the 4-note
// PLAIN_RUN_CAP just to close the beat exactly (a bar-filling algorithm
// can't leave a gap unfilled). That's exactly how "eighth + four sixteenths"
// (2+1+1+1+1=6) and the alternating "eighth-sixteenth-eighth-sixteenth"
// pattern were slipping through.
//
// Rather than patch the generic algorithm further (this is the second
// distinct loophole found in it for 6/8 specifically), compound meters now
// fill each felt beat (one dotted-quarter's worth of units) from a small,
// curated set of the idiomatic groupings actually seen in the book --
// never more than 4 notes, and never the two flagged shapes -- instead of
// letting per-note random choice paint itself into an exact-fill corner.
// Falls back to the general algorithm untouched for any other time
// signature, or if a grade's allowedKeys can't support any curated pattern.
// 2026-09-09 revision: "8분의 6박자는 quaver 3개를 하나의 그룹으로 두개 구성하는데
// 박자 복잡하지 않게 quaver랑 crotchet, dotted crotchet이 주고 간간히 Semiquaver
// 2개 묶어 나오는거 정도만 구성해줘" -- direct spec from the user: quaver (eighth)
// and crotchet (quarter) and dotted crotchet (dottedQuarter) should be the
// MAIN vocabulary, with a semiquaver (sixteenth) PAIR appearing only
// occasionally in place of one quaver. This replaces the previous
// dottedEighth-based patterns above entirely -- the user did not ask for
// that idiom this time, and leaving it in would contradict "quaver, crotchet,
// dotted crotchet -- that's about it".
const COMPOUND_BEAT_PATTERNS = [
  // Held dotted-quarter -- the simplest, most common shape.
  { pattern: ['dottedQuarter'], weight: 3.0 },
  // Crotchet + quaver / quaver + crotchet -- the classic compound-meter
  // "long-short" or "short-long" idiom (4+2=6 units, exactly one beat).
  { pattern: ['quarter', 'eighth'], weight: 2.2 },
  { pattern: ['eighth', 'quarter'], weight: 2.2 },
  // Three plain quavers -- even, simple running motion.
  { pattern: ['eighth', 'eighth', 'eighth'], weight: 1.8 },
  // A semiquaver PAIR standing in for one quaver, in each of the 3 possible
  // slots -- kept at low weight so it's genuinely occasional, not a fourth
  // main option.
  { pattern: ['sixteenth', 'sixteenth', 'eighth', 'eighth'], weight: 0.5 },
  { pattern: ['eighth', 'sixteenth', 'sixteenth', 'eighth'], weight: 0.5 },
  { pattern: ['eighth', 'eighth', 'sixteenth', 'sixteenth'], weight: 0.5 },
];

function fillCompoundBeat(allowedKeys) {
  const allowedSet = new Set(allowedKeys);
  const usable = COMPOUND_BEAT_PATTERNS.filter((p) => p.pattern.every((k) => allowedSet.has(k)));
  if (usable.length === 0) return null;
  const total = usable.reduce((s, p) => s + p.weight, 0);
  let r = Math.random() * total;
  for (const p of usable) {
    if (r < p.weight) return p.pattern;
    r -= p.weight;
  }
  return usable[usable.length - 1].pattern;
}

/**
 * Fill a bar of `barUnits` sixteenth-note-units using only durations whose
 * key is in `allowedKeys`. Guarantees an exact fill by always keeping the
 * smallest available unit as a legal "closer" for the final gap.
 *
 * `beatUnits` (2026-09-04, default 4 = a quarter note, gradeParams.js's
 * BEAT_UNITS table gives the right value per time signature) is the felt
 * beat pulse: a duration lasting a full beat or longer may only START on a
 * beat boundary (`position % beatUnits === 0`), never mid-beat. Without
 * this, e.g. two dotted-quarter notes could land back-to-back in 4/4 (the
 * second one starting on the "and" of beat 2), which reads as an
 * ungrounded, syncopated rhythm with no clear per-beat reference point --
 * see BEAT_UNITS's own comment for the report this fixes. A duration
 * SHORTER than a beat is never restricted this way, which is exactly what
 * lets the standard "dotted-quarter + eighth" (fills 2 beats) idiom through:
 * the dotted quarter starts on-beat, lands mid-beat, and only a
 * shorter-than-beat note can legally follow until the next beat boundary.
 */
function fillBar(barUnits, allowedKeys, beatUnits = 4, subBeatUnits = beatUnits, compoundBeat = false, weightOverrides = null, dottedQuarterEighthChance = null) {
  // Compound-meter curated-pattern path (see COMPOUND_BEAT_PATTERNS' comment
  // above) -- tries to fill every beat in the bar from the idiomatic pool;
  // falls through to the general algorithm below if it can't (e.g. a bucket
  // whose allowedKeys don't support any curated pattern), so nothing else
  // about this function's behaviour changes for non-compound callers.
  if (compoundBeat && beatUnits > 0 && barUnits % beatUnits === 0) {
    const beatsPerBar = barUnits / beatUnits;
    const beats = [];
    let ok = true;
    for (let i = 0; i < beatsPerBar; i++) {
      const beat = fillCompoundBeat(allowedKeys);
      if (!beat) { ok = false; break; }
      beats.push(beat);
    }
    if (ok) return beats.flat();
  }
  const options = allowedKeys
    .map((k) => ({ key: k, units: NOTE_VALUES[k].units }))
    .sort((a, b) => a.units - b.units);
  const smallest = options[0];
  // Every supported duration has an even unit count EXCEPT dottedEighth (3)
  // and sixteenth (1). Picking an odd-unit duration flips the parity of
  // `remaining`; since all other durations are even, an odd `remaining` can
  // only ever be closed by ANOTHER odd-unit duration. A grade whose
  // noteValues include dottedEighth but not sixteenth (e.g. Grade 4) can
  // otherwise strand an unclosable odd remainder and silently overshoot the
  // bar by 1 unit -- see the safety filter below.
  const smallestOdd = options.filter((o) => o.units % 2 === 1).sort((a, b) => a.units - b.units)[0] || null;

  const result = [];
  let remaining = barUnits;
  let position = 0; // units placed so far -- where the NEXT note would start

  // Mild weighting: favour "moving" note values (quarter/eighth) over long
  // held notes so excerpts don't feel static, but still let half/whole notes
  // appear for phrasing.
  // 2026-09-09: dottedEighth dropped 0.8 -> 0.3 -- "아직도 책에 비해 너무 빡빡해...
  // 비중을 좀 낮춰줘 30퍼센트로" (still too packed vs. the book -- bring the
  // proportion down to about 30%), direct feedback after seeing several
  // generated excerpts where a dotted-eighth+sixteenth pair showed up in
  // most bars of the piece. This doesn't change how the pair itself reads
  // once it fires (still a clean 2-note pair, see DOTTED_RUN_CAP/the
  // beat-start restriction below) -- just how often it gets picked over the
  // plain eighth/sixteenth alternatives at each eligible beat.
  const baseWeight = { sixteenth: 1.4, eighth: 1.6, dottedEighth: 0.3, quarter: 2.0, dottedQuarter: 1.0, half: 1.1, dottedHalf: 0.5, whole: 0.3 };

  // 2026-08-27: cap how many consecutive shorter-than-quarter notes (eighths,
  // sixteenths, dotted-eighths) can appear in a row. Each individual pick
  // above was already weighted reasonably, but with nothing tracking history
  // an unlucky run of picks could string together an entire bar of running
  // eighths (e.g. 7-8 in a row) -- reported as "rhythm still looks too
  // complex" even after the pitch-leap fix, since real beginner-grade
  // material (esp. Grade 1, whose noteValues include eighth alongside
  // quarter/half) uses eighths in short isolated pairs, not long runs.
  const QUARTER_UNITS = NOTE_VALUES.quarter.units;
  // 2026-09-09: "끽해야 트리플렛이나 4 세미퀴버 이정도로만" -- direct feedback (with
  // book photos) that even after the previous "taper, don't compound" fix
  // below, generated excerpts still read as harder than the book because
  // the wrong thing was being capped. The real distinction on the page
  // isn't "how many short notes in a row" -- it's UNEVEN vs. EVEN
  // groupings. A plain run of same-length notes (e.g. four sixteenths
  // beamed together) reads simply despite being 4 notes, matching what the
  // user called "4 semiquavers" as an acceptable ceiling; the engine has no
  // triplet support (a separate, already-flagged gap), but a dotted-eighth+
  // sixteenth PAIR is the other explicitly book-confirmed idiom -- and
  // that's exactly the one that reads as "jumpy"/hard once it chains into a
  // second pair (dottedEighth, sixteenth, dottedEighth, sixteenth), because
  // each individual note is a different length from its neighbor. So the
  // cap is now duration-dependent: a run containing a dottedEighth is
  // capped at DOTTED_RUN_CAP (just the one idiomatic pair), while a run of
  // plain eighths/sixteenths only is allowed up to PLAIN_RUN_CAP.
  const DOTTED_RUN_CAP = 2;
  const PLAIN_RUN_CAP = 4;
  let shortRun = 0;
  let shortRunHasDotted = false;
  // 2026-09-11: tracks a run of consecutive PLAIN sixteenth notes
  // specifically (separate from shortRun's general eighth-or-shorter
  // count) -- see its own comment further down, right before the final
  // weighted pick, for why this exists (LilyPond's secondary beam renders
  // a broken/stub look on an ODD-length group of sixteenths).
  let sixteenthRunLen = 0;

  while (remaining > 0) {
    // 2026-09-09: "이 패턴도 넣어줘" -- book photo of the classic "dotted
    // crotchet + quaver" long-short idiom, wanted back in simple meters too
    // (3/4, 4/4 -- excluded earlier today when those meters were narrowed to
    // crotchet/minim/dotted-minim only). A BARE dottedQuarter can't just be
    // added to this meter's vocabulary the way it works in compound time:
    // dottedQuarter is 6 units against a 4-unit felt beat here, so on its
    // own it doesn't return the grid to alignment after it (6 % 4 = 2) --
    // the same class of misalignment the dottedEighth+sixteenth pairing
    // above had to solve with dedicated start/follow restrictions. Simpler
    // fix for this one: inject the pair ATOMICALLY (both notes at once,
    // never just the dottedQuarter alone) at the start of an even beat pair
    // (position a multiple of 2 beats), where 6+2=8 units lands exactly back
    // on the next beat-pair boundary -- guarantees it only ever appears as
    // this clean, book-matching pair. `dottedQuarterEighthChance` (opt-in
    // per bucket, only passed for the meters it should apply to) is the
    // ONLY gate -- deliberately bypassing `options`/`allowedKeys` entirely,
    // so 'dottedQuarter'/'eighth' never need to join this meter's normal
    // vocabulary (and therefore can never be picked bare/standalone by the
    // general algorithm below, only ever as this atomic pair).
    if (dottedQuarterEighthChance && beatUnits > 0 && position % (beatUnits * 2) === 0
      && remaining >= beatUnits * 2 && Math.random() < dottedQuarterEighthChance) {
      result.push('dottedQuarter', 'eighth');
      remaining -= beatUnits * 2;
      position += beatUnits * 2;
      // The pair's last note (the eighth) IS a short note by the run-cap
      // system's own definition (units < QUARTER_UNITS) -- track it as a
      // fresh 1-note run rather than resetting to 0, so a sixteenth run
      // immediately following this pair still gets capped correctly.
      shortRun = 1;
      shortRunHasDotted = false;
      sixteenthRunLen = 0;
      continue;
    }
    let usable = options.filter((o) => o.units <= remaining);
    // Reject any pick that would strand an odd remainder with no odd-unit
    // duration left to close it exactly.
    usable = usable.filter((o) => {
      const after = remaining - o.units;
      if (after === 0 || after % 2 === 0) return true;
      return smallestOdd !== null && smallestOdd.units <= after;
    });
    // Metric alignment (2026-09-04, see this function's doc comment): a
    // beat-or-longer duration may only start ON a beat.
    usable = usable.filter((o) => o.units < beatUnits || position % beatUnits === 0);
    // 2026-09-09: "아직 다 안고쳐졌는데" -- the explicit 6/8 beatStructure
    // fix (index.js's beamGroupingOverride) forces LilyPond's beam to break
    // every 3 eighth-note-units, but nothing here ever stopped a SHORTER-
    // than-beat note from straddling that same 3-unit line -- beatUnits for
    // 6/8 is 6 (the felt dotted-quarter beat), so e.g. an eighth note is
    // "shorter than beat" and was allowed to start anywhere, including
    // position 5 and running to 7, straddling the 3/6/9 sub-beat grid the
    // beam is now forced to break on. LilyPond can't actually split a
    // note's duration to honor that break, so the beam ends up looking
    // wrong/uneven around it regardless of the beatStructure setting.
    // `subBeatUnits` (opt-in via generateRhythm/fillBar's new parameter --
    // index.js passes 3 for 6/8) additionally requires any duration SHORTER
    // than the main beat to fit entirely inside one sub-beat slot without
    // crossing it. Notes a full beat or longer are exempt -- they're
    // already beat-aligned by the filter above and never participate in a
    // beam group anyway.
    // 2026-09-11: BUG FIX -- for every SIMPLE meter (4/4, 3/4, 2/4...),
    // index.js passes `subBeatUnits = beatUnits` (its own default, meaning
    // "no separate sub-beat, the beat IS the slot"), but this filter used to
    // read that as `subBeatUnits >= beatUnits` -> "no restriction configured,
    // skip the check entirely" -- i.e. this straddle guard was silently DEAD
    // CODE for every simple meter, only ever doing anything for the 6/8/9/8
    // fallback path. That let a short note (an eighth, say) start mid-beat
    // and run PAST the beat boundary into the next beat -- which, once the
    // running position drifted off the quarter-note grid this way (e.g.
    // after an ODD number of sixteenths), permanently defeated the
    // PLAIN_RUN_CAP/DOTTED_RUN_CAP logic above (its "force a longer note"
    // fallback only fires when a legal beat-boundary is reached, which
    // could then never happen again for the rest of the bar). Confirmed
    // directly: a 20,000-sample stress test of a plain 4/4 bar under this
    // grade's own tuned weights produced a 10-note-long unbroken run of
    // short notes despite the 4-note cap -- exactly the "still showing"
    // wall-of-eighths screenshot reported after the per-style weight pass.
    // Removing the bypass makes every simple-meter beat its own enforced
    // slot (subBeatUnits defaults to beatUnits precisely so this now
    // applies everywhere, not just 6/8/9/8), which structurally guarantees
    // a short note can never straddle a beat boundary -- so the run-cap's
    // "wait for a beat boundary" fallback can never be permanently defeated
    // again. This is an engine-level fix, not a per-style tuning value, so
    // it protects every grade/timeSig/style at once.
    usable = usable.filter((o) => {
      if (o.units >= beatUnits) return true;
      const startSlot = Math.floor(position / subBeatUnits);
      const endSlot = Math.floor((position + o.units - 1) / subBeatUnits);
      return startSlot === endSlot;
    });
    // 2026-09-09: restrict dottedEighth to the START of a short-note run
    // (shortRun === 0, i.e. the previous note was quarter-or-longer or this
    // is the first note of the bar). Without this, dottedEighth could still
    // get picked mid-run (e.g. sixteenth, eighth, eighth, dottedEighth) --
    // each individual note a different length from its neighbor, which is
    // exactly the "uneven/jumpy" pattern flagged as too hard, even though
    // the DOTTED_RUN_CAP logic below correctly stops anything AFTER a
    // dottedEighth. Restricting where it can START, not just where it must
    // stop, keeps every dottedEighth appearance to a single clean pair
    // (dottedEighth immediately followed by its sixteenth partner, then the
    // run ends) instead of a random uneven note buried in a longer run.
    // 2026-09-09: ALSO require the dottedEighth to start exactly ON a beat
    // boundary, same as a quarter-or-longer note would. dottedEighth +
    // sixteenth sums to exactly one beat (3+1=4 units), so starting the
    // pair on-beat means it lands back on the NEXT beat boundary too --
    // otherwise (e.g. starting right after a dottedQuarter mid-bar) the
    // pair still resolves ITS OWN parity but leaves the bar's overall grid
    // off by the same offset it started with, so the cap logic below can't
    // find a legal spot to stop and has to keep tapering with extra notes.
    if (shortRun === 0 && position % beatUnits !== 0) {
      const withoutDotted = usable.filter((o) => o.key !== 'dottedEighth');
      if (withoutDotted.length > 0) usable = withoutDotted;
    }
    if (shortRun > 0) {
      const withoutDotted = usable.filter((o) => o.key !== 'dottedEighth');
      // Safety: only apply the restriction if it leaves at least one legal
      // option -- a bucket that (hypothetically) allows dottedEighth but not
      // sixteenth could otherwise strand the exact-fill guarantee.
      if (withoutDotted.length > 0) usable = withoutDotted;
    }
    if (usable.length === 0) {
      // Shouldn't happen if smallest unit divides barUnits, but guard anyway.
      result.push(smallest.key);
      remaining -= smallest.units;
      position += smallest.units;
      continue;
    }
    // Once we've already placed SHORT_RUN_CAP short notes in a row, prefer a
    // quarter-or-longer duration to break up the run -- but only if doing so
    // doesn't strand the exact-fill guarantee (e.g. a bar whose only allowed
    // duration is eighth notes has nothing longer to fall back to).
    //
    // 2026-09-09: "리듬은 한박 이하인경우에 이 정도로만" -- direct feedback
    // (with book photos showing sub-beat groupings never busier than a
    // simple 2-note pair: two eighths, or a dotted-eighth+sixteenth) that
    // generated excerpts were sometimes reading busier than that. Root
    // cause: mid-beat, a quarter-or-longer note is illegal (beat-alignment
    // filter above), so the "longer" fallback above was empty and this used
    // to fall through to the FULL unrestricted `usable` list again --
    // meaning once the cap was already hit, the very next pick could still
    // be another sixteenth/dottedEighth, chaining a second short-note pair
    // onto the first (4 short notes total under one beam) instead of
    // actually stopping the run. Now, when no quarter-or-longer can legally
    // break the run, fall back to the LARGEST remaining short duration
    // instead of a random one -- this prefers finishing the beat with a
    // single eighth over extending it with more sixteenths, so a run tapers
    // off (e.g. sixteenth+sixteenth+eighth) rather than compounding
    // (sixteenth+sixteenth+sixteenth+sixteenth).
    //
    // 2026-09-09 correction: picking the raw LARGEST unit-count backfired --
    // dottedEighth (3 units) outranks eighth (2 units) by unit count alone,
    // so the very first version of this fallback ended up preferring
    // dottedEighth over the simpler eighth, occasionally chaining three lone
    // dotted-eighths in a row (each needing an odd-unit partner somewhere
    // to close exactly), which reads as MORE unusual than the plain
    // eighth-note tail this was supposed to produce. Use an explicit
    // simplicity order instead of raw unit count: plain eighth first (the
    // idiomatic "close out the beat" duration), then sixteenth, and only
    // dottedEighth if neither of those is legal here.
    const SIMPLICITY_ORDER = ['eighth', 'sixteenth', 'dottedEighth'];
    // 2026-09-09: the note immediately after a dottedEighth needs to be a
    // sixteenth specifically, not just "something short" -- dottedEighth is
    // 3 (odd) units, so pairing it with an eighth (even) leaves the
    // position permanently off the beat grid (odd+even is always odd,
    // never realigning to a quarter-note boundary), which was letting the
    // DOTTED_RUN_CAP taper below cascade through several more eighths
    // before it could find a legal spot to stop. Only a sixteenth (odd)
    // restores exact beat alignment in one step (3+1=4, a full beat) --
    // which is exactly the classic dottedEighth+sixteenth pairing seen on
    // the actual page. Force it whenever it's legally available.
    // 2026-09-11: this branch's forced sixteenth is the dottedEighth's own
    // PARTNER -- it's beamed together with the dottedEighth it follows, not
    // a standalone plain-sixteenth run needing its own even-count partner
    // (see the parity-guard further below). Flag it so that guard doesn't
    // treat this one sixteenth as starting a fresh odd-length run and force
    // yet another sixteenth after it, which would wrongly extend the pair
    // into a trio.
    let dottedPairSixteenth = false;
    if (shortRunHasDotted && shortRun === 1) {
      const sixteenthOpt = usable.find((o) => o.key === 'sixteenth');
      if (sixteenthOpt) {
        usable = [sixteenthOpt];
        dottedPairSixteenth = true;
      }
    }
    const currentCap = shortRunHasDotted ? DOTTED_RUN_CAP : PLAIN_RUN_CAP;
    // 2026-09-11: forcing only triggers when `shortRun >= currentCap`, but a
    // beat can only be broken with a longer note AT its own boundary
    // (position % beatUnits === 0, see the alignment filter above) -- a run
    // that reaches exactly `currentCap` mid-beat (not AT a boundary) has to
    // wait until the NEXT boundary before this can fire at all, during which
    // an entire extra beat's worth of short notes can be freely chosen,
    // letting the real run length overshoot the cap by up to a whole beat.
    // Confirmed by direct stress-test (20,000 generated 4/4 bars): even
    // after the subBeatUnits straddle fix above (which stops a single note
    // from crossing a boundary), runs of 5-6 notes still slipped through
    // this way against a cap of 4. Fix: evaluate one note EARLY, right AT
    // each beat boundary -- if the run is already one note short of the cap
    // as a fresh beat is about to start, force that beat to open with a
    // longer note too (not just a beat where the cap is already exceeded),
    // so a continuing run can never pick up a whole additional beat's worth
    // of short notes once it's this close to the limit.
    const atBoundary = position % beatUnits === 0;
    const effectiveCap = atBoundary ? Math.max(1, currentCap - 1) : currentCap;
    if (shortRun >= effectiveCap) {
      const longer = usable.filter((o) => o.units >= QUARTER_UNITS);
      if (longer.length > 0) {
        usable = longer;
      } else {
        // Still can't legally break with a quarter-or-longer note (mid-beat).
        // Once a dottedEighth has appeared, exclude it from further
        // consideration entirely -- the goal past DOTTED_RUN_CAP is to stop
        // the uneven pattern, not extend it with a second dotted note.
        const noMoreDotted = usable.filter((o) => o.key !== 'dottedEighth');
        const pool = shortRunHasDotted && noMoreDotted.length > 0 ? noMoreDotted : usable;
        const preferred = SIMPLICITY_ORDER.map((key) => pool.find((o) => o.key === key)).find(Boolean);
        usable = preferred ? [preferred] : pool;
      }
    }
    // 2026-09-11: "16분음표는 4개 한박으로 잘보이게 그룹핑해주고" -- direct
    // screenshot of a beamed group of exactly 3 sixteenths, with LilyPond's
    // secondary beam rendering a visibly broken/stub look on the last note
    // -- reproduced directly: a group of 3 plain sixteenths (an ODD count)
    // always renders this way, regardless of manual vs. automatic beaming
    // (verified both ways), because LilyPond's secondary beam connects
    // sixteenth-level notes in pairs and has nothing to pair the third one
    // with. The run-cap/taper logic above only tracks TOTAL short-note
    // count, with no awareness that a sixteenth run specifically needs to
    // stop at an EVEN count (2 or 4) to beam cleanly -- it was perfectly
    // willing to cut a sixteenth run off at 1 or 3. Fix: if the run of
    // consecutive PLAIN sixteenths so far is odd, and 'sixteenth' is still
    // a legal choice here, force it -- completing the pair -- rather than
    // letting any other duration (even one preferred by the cap/taper logic
    // above) end the run on an odd note. This can extend a run by at most
    // one extra note (to reach the next even count), so it doesn't reopen
    // the long-unbroken-run bug the cap logic above exists to prevent.
    if (!dottedPairSixteenth && sixteenthRunLen % 2 === 1) {
      const sixteenthOpt = usable.find((o) => o.key === 'sixteenth');
      if (sixteenthOpt) usable = [sixteenthOpt];
    }
    // If only the smallest unit can possibly finish the bar exactly given
    // remaining constraints (remaining not a multiple of any larger unit's
    // "fits cleanly" heuristic), prefer it near the end.
    // 2026-09-09: `weightOverrides` (opt-in, per-timeSig, see index.js's
    // simpleMeterWeightOverride) lets a caller rebalance how often each
    // duration is picked without touching the global baseWeight table used
    // by every other grade/timeSig -- e.g. simple-meter grade4 excerpts now
    // want crotchet/minim/dotted-minim to dominate and sixteenth-note runs
    // to be genuinely rare, which the shared baseWeight values (tuned for
    // 4/4's busier eighth/sixteenth mix) don't reflect on their own.
    const candidates = usable.map((o) => ({
      key: o.key,
      weight: (weightOverrides && weightOverrides[o.key] != null) ? weightOverrides[o.key] : (baseWeight[o.key] || 1),
    }));
    const chosen = weightedPick(candidates);
    result.push(chosen);
    remaining -= NOTE_VALUES[chosen].units;
    position += NOTE_VALUES[chosen].units;
    if (NOTE_VALUES[chosen].units < QUARTER_UNITS) {
      shortRun += 1;
      if (chosen === 'dottedEighth') shortRunHasDotted = true;
    } else {
      shortRun = 0;
      shortRunHasDotted = false;
    }
    sixteenthRunLen = chosen === 'sixteenth' && !dottedPairSixteenth ? sixteenthRunLen + 1 : 0;
  }
  return result; // array of NOTE_VALUES keys
}

/** Generate rhythm (array of note-value keys) for every bar in the piece. */
function generateRhythm(barCount, barUnits, allowedKeys, beatUnits = 4, subBeatUnits = beatUnits, compoundBeat = false, weightOverrides = null, dottedQuarterEighthChance = null) {
  const bars = [];
  for (let i = 0; i < barCount; i++) {
    bars.push(fillBar(barUnits, allowedKeys, beatUnits, subBeatUnits, compoundBeat, weightOverrides, dottedQuarterEighthChance));
  }
  return bars;
}

module.exports = { fillBar, generateRhythm };
