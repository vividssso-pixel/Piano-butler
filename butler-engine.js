// Piano Butler — rotation + coverage engine.
//
// Pure logic, no DOM. Loaded by butler.html in the browser and by the node test
// harness directly, so the rotation rules can be traced against real syllabus data
// without a browser.
//
// Every function that needs "now" takes it as an explicit ISO date argument.
// Nothing in here reads the clock on its own — that's what makes it testable.

(function (root, factory) {
  var api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.ButlerEngine = api;
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // Areas tracked alongside technical work.
  //
  // drillable:false means the butler cannot generate questions for it. Those areas
  // still get a coverage row so they surface as gaps for the teacher to pick up —
  // that display line is the entire feature for theory and general knowledge.
  var AREAS = [
    { id: 'aural',     label: 'Aural',             hint: 'No piano required',                 drillable: true  },
    { id: 'sightread', label: 'Sight-reading',     hint: 'A little each day',                 drillable: true  },
    { id: 'viva',      label: 'Viva voce',         hint: 'Your pieces and their background',  drillable: true  },
    { id: 'theory',    label: 'Theory',            hint: 'With your teacher',                 drillable: false },
    { id: 'gk',        label: 'General knowledge', hint: 'With your teacher',                 drillable: false }
  ];

  var DAILY_TECH_COUNT = 2;    // the fixed daily 3 minutes
  var EXAM_LOCKDOWN_WEEKS = 8; // inside this window rotation stops; the exam tests everything
  var STALE_DAYS = 21;         // the "3+ weeks" threshold shown on the gap map
  var WARN_DAYS = 7;

  // ---------- dates ----------

  function today() {
    var d = new Date();
    return new Date(d.getTime() - d.getTimezoneOffset() * 60000).toISOString().slice(0, 10);
  }

  function daysBetween(fromISO, toISO) {
    if (!fromISO || !toISO) return null;
    var a = new Date(fromISO + 'T00:00:00Z'), b = new Date(toISO + 'T00:00:00Z');
    return Math.round((b - a) / 86400000);
  }

  // Monday-based week id. A weekly module is pinned to this so it can't reshuffle
  // partway through the week.
  function weekOf(iso) {
    var d = new Date(iso + 'T00:00:00Z');
    var dow = (d.getUTCDay() + 6) % 7;
    d.setUTCDate(d.getUTCDate() - dow);
    return d.toISOString().slice(0, 10);
  }

  function weeksUntil(examISO, nowISO) {
    var d = daysBetween(nowISO, examISO);
    return d === null ? null : d / 7;
  }

  // ---------- coverage keys ----------

  // Everything trackable for a grade: named technical exercises, every individual
  // scale/arpeggio/chord line from the syllabus, then the five areas.
  //
  // Comprehensive Piano vs Piano for Leisure — from the PfL Syllabus 2026 itself:
  //   "All technical work is set out in Piano Technical Work Level 1 (Preliminary to
  //    Grade 4) and Piano Technical Work Level 2 (Grade 5 to Grade 8). There is no
  //    specific Piano for Leisure technical work book."
  // So both subjects draw technical work from the same source, and Aural /
  // Sight-Reading / General Knowledge are Section III for both. Only the pieces
  // differ (Series 1-4 + Manual, rather than List A/B/C) — and pieces are out of
  // scope here. That is why one engine serves both.
  //
  // OPEN QUESTION before this branches: does PfL grade N require the *same*
  // scale/arpeggio selection as Comprehensive grade N, or a reduced one? If reduced,
  // add a per-grade Leisure list to data_technical_ameb.js and pick it here from
  // student.syllabus. Until that is confirmed, both show the same (possibly larger)
  // Comprehensive list, which over-serves rather than under-serves a Leisure student.
  function coverageKeys(gradeKey, techData, auralData) {
    var g = (techData || {})[gradeKey];
    var out = [];
    if (g) {
      (g.exercises || []).forEach(function (e) {
        out.push({ key: 'ex:' + e.code, label: e.code, desc: e.purpose || '', group: 'Technical Exercises', kind: 'tech' });
      });
      (g.sections || []).forEach(function (s, si) {
        (s.items || []).forEach(function (it, ii) {
          out.push({ key: 'sc:' + si + ':' + ii, label: it, desc: '', group: s.title, kind: 'tech' });
        });
      });
    }

    // Aural is tracked per test, not as one lump. A grade sets 3-4 separate tests
    // (rhythm, pitch, harmony, memory...) and they slip independently — "aural is
    // behind" is not actionable, "the harmony test hasn't been touched" is.
    var aural = (auralData || {})[gradeKey];
    AREAS.forEach(function (a) {
      if (a.id === 'aural' && aural && aural.tests && aural.tests.length) {
        var seen = {};
        var counts = {};
        aural.tests.forEach(function (t) { counts[t.type] = (counts[t.type] || 0) + 1; });
        aural.tests.forEach(function (t, ti) {
          seen[t.type] = (seen[t.type] || 0) + 1;
          out.push({
            key: 'au:' + ti,
            // Only number a category when the grade sets more than one of it.
            label: counts[t.type] > 1 ? t.type + ' ' + seen[t.type] : t.type,
            desc: t.text, group: 'Aural tests', kind: 'area', areaId: 'aural'
          });
        });
      } else {
        out.push({
          key: 'area:' + a.id, label: a.label, desc: a.hint, group: 'Other components',
          kind: a.drillable ? 'area' : 'manual', areaId: a.id
        });
      }
    });
    return out;
  }

  function lastAt(student, key) {
    var c = student.coverage && student.coverage[key];
    return (c && c.last) || null;
  }

  // Per-student "not required" switches.
  //
  // Piano for Leisure needs a smaller technical selection than Comprehensive at the
  // same grade, and we don't hold the reduced per-grade lists. Rather than quietly
  // over-report, the teacher switches off whatever doesn't apply — once, at setup.
  // Excluded items leave the rotation and drop out of the coverage denominator, so
  // the percentage stays honest. The same switch covers scales not taught yet,
  // exemptions, and injuries.
  function isExcluded(student, key) {
    return !!(student.excluded && student.excluded[key]);
  }

  function toggleExcluded(student, key) {
    student.excluded = student.excluded || {};
    if (student.excluded[key]) delete student.excluded[key];
    else student.excluded[key] = true;
    return student;
  }

  function included(student) {
    return function (k) { return !isExcluded(student, k.key); };
  }

  // ---------- rotation ----------

  // The whole engine is this one rule: least-recently-practiced first, with
  // never-practiced ahead of everything.
  //
  // Never randomise the pick. A random choice can drop an item and never bring it
  // back, which would make the app worse than the paper diary it replaces.
  function stalestFirst(student, nowISO) {
    return function (a, b) {
      var la = lastAt(student, a.key), lb = lastAt(student, b.key);
      if (!la && !lb) return 0;
      if (!la) return -1;
      if (!lb) return 1;
      var da = daysBetween(la, nowISO), db = daysBetween(lb, nowISO);
      if (db !== da) return db - da;
      return 0;
    };
  }

  function examLocked(student, nowISO) {
    var w = weeksUntil(student.examDate, nowISO);
    return w !== null && w <= EXAM_LOCKDOWN_WEEKS && w >= -1;
  }

  // Returns what the student should see today, plus the dayPlan/weekPlan the caller
  // should persist. Does not mutate the student.
  //
  // Both selections are *pinned* — the day's items are chosen once and then stay put
  // even as they get ticked off. Re-deriving them live would make the card infinite:
  // tick one, a fresh one slides in, and the student never reaches "done for today".
  // That completion moment is the whole habit loop, so it has to be reachable.
  function planFor(student, nowISO, techData, auralData) {
    var keys = coverageKeys(student.grade, techData, auralData);
    var cmp = stalestFirst(student, nowISO);
    var byKey = {};
    keys.forEach(function (k) { byKey[k.key] = k; });

    var tech = keys.filter(function (k) { return k.kind === 'tech'; }).filter(included(student));
    var dayPlan = student.dayPlan || null;

    if (!dayPlan || dayPlan.date !== nowISO) {
      dayPlan = {
        date: nowISO,
        keys: tech.slice().sort(cmp).slice(0, DAILY_TECH_COUNT).map(function (k) { return k.key; })
      };
    }

    var daily = dayPlan.keys.map(function (k) { return byKey[k]; })
                            .filter(function (k) {
                              return k && k.kind === 'tech' && !isExcluded(student, k.key);
                            });

    // Grade changed, or an item was switched off, under a pinned plan — top the list
    // back up rather than showing the student a short card.
    if (daily.length < Math.min(DAILY_TECH_COUNT, tech.length)) {
      var have = {};
      daily.forEach(function (k) { have[k.key] = true; });
      tech.slice().sort(cmp).forEach(function (k) {
        if (daily.length < DAILY_TECH_COUNT && !have[k.key]) { daily.push(k); have[k.key] = true; }
      });
      dayPlan = { date: nowISO, keys: daily.map(function (k) { return k.key; }) };
    }

    // Areas rotate as areas, not as individual entries. Aural contributes 3-4 keys
    // (one per test), so ranking raw keys would let it win the weekly slot almost
    // every time and starve sight-reading and viva voce. Rank the areas by their own
    // stalest member, pick one area, then serve that area's stalest test.
    var drillable = keys.filter(function (k) { return k.kind === 'area'; }).filter(included(student));
    var areaIds = [];
    drillable.forEach(function (k) {
      if (areaIds.indexOf(k.areaId) < 0) areaIds.push(k.areaId);
    });
    function stalestIn(areaId) {
      return drillable.filter(function (k) { return k.areaId === areaId; }).sort(cmp)[0];
    }

    // How long since this area was touched at all — the most recent date across its
    // tests. Ranking areas by their *stalest test* instead would hand aural four
    // weeks in a row (it has four tests, only one gets served per day), starving
    // sight-reading for a month. Rotation is between areas; staleness picks the test
    // once an area has won the week.
    function areaLastAt(areaId) {
      var dates = drillable
        .filter(function (k) { return k.areaId === areaId; })
        .map(function (k) { return lastAt(student, k.key); })
        .filter(Boolean)
        .sort();
      return dates.length ? dates[dates.length - 1] : null;
    }

    function leastRecentAreaFirst(a, b) {
      var la = areaLastAt(a), lb = areaLastAt(b);
      if (!la && !lb) return areaIds.indexOf(a) - areaIds.indexOf(b);
      if (!la) return -1;
      if (!lb) return 1;
      return la < lb ? -1 : (la > lb ? 1 : areaIds.indexOf(a) - areaIds.indexOf(b));
    }

    var locked = examLocked(student, nowISO);
    var weekPlan = student.weekPlan || null;
    var chosenAreas;

    if (locked) {
      // Exam inside the lockdown window — every area appears, one test from each.
      chosenAreas = areaIds;
    } else {
      var wk = weekOf(nowISO);
      // `areaId` guard also migrates the older {weekOf, key} shape.
      if (!weekPlan || weekPlan.weekOf !== wk || !weekPlan.areaId ||
          areaIds.indexOf(weekPlan.areaId) < 0) {
        var ranked = areaIds.slice().sort(leastRecentAreaFirst);
        weekPlan = { weekOf: wk, areaId: ranked[0] || null };
      }
      chosenAreas = weekPlan.areaId ? [weekPlan.areaId] : [];
    }

    // Pin the chosen test for the day, same reason as the technical list.
    var pinned = (dayPlan.areaKeys || []).map(function (k) { return byKey[k]; })
      .filter(function (k) { return k && !isExcluded(student, k.key); });
    var weekly = chosenAreas.map(function (id) {
      var held = pinned.filter(function (k) { return k.areaId === id; })[0];
      return held || stalestIn(id);
    }).filter(Boolean);
    dayPlan.areaKeys = weekly.map(function (k) { return k.key; });

    var all = daily.concat(weekly);
    var doneCount = all.filter(function (k) { return lastAt(student, k.key) === nowISO; }).length;

    return {
      daily: daily, weekly: weekly, locked: locked,
      weekPlan: weekPlan, dayPlan: dayPlan,
      total: all.length, done: doneCount, allDone: all.length > 0 && doneCount === all.length
    };
  }

  // Toggle: marking an already-done item undoes it, so a mistap is recoverable.
  function markDone(student, key, nowISO) {
    student.coverage = student.coverage || {};
    var c = student.coverage[key] || { last: null, prev: null, times: 0 };
    if (c.last === nowISO) {
      c.last = c.prev || null;
      c.times = Math.max(0, (c.times || 0) - 1);
    } else {
      c.prev = c.last;
      c.last = nowISO;
      c.times = (c.times || 0) + 1;
    }
    student.coverage[key] = c;
    return student;
  }

  function status(student, key, nowISO) {
    var la = lastAt(student, key);
    if (!la) return 'never';
    var d = daysBetween(la, nowISO);
    if (d >= STALE_DAYS) return 'late';
    if (d >= WARN_DAYS) return 'warn';
    return 'ok';
  }

  // Excluded items are left out of the denominator too, so the percentage reflects
  // what this student is actually required to cover.
  function coverageStats(student, nowISO, techData, auralData) {
    var tech = coverageKeys(student.grade, techData, auralData)
      .filter(function (k) { return k.kind === 'tech'; })
      .filter(included(student));
    var touched = 0, stale = 0;
    tech.forEach(function (k) {
      if (lastAt(student, k.key)) touched++;
      var s = status(student, k.key, nowISO);
      if (s === 'never' || s === 'late') stale++;
    });
    return {
      total: tech.length,
      touched: touched,
      stale: stale,
      pct: tech.length ? Math.round(touched / tech.length * 100) : 0
    };
  }

  return {
    AREAS: AREAS,
    DAILY_TECH_COUNT: DAILY_TECH_COUNT,
    EXAM_LOCKDOWN_WEEKS: EXAM_LOCKDOWN_WEEKS,
    today: today,
    daysBetween: daysBetween,
    weekOf: weekOf,
    weeksUntil: weeksUntil,
    coverageKeys: coverageKeys,
    lastAt: lastAt,
    isExcluded: isExcluded,
    toggleExcluded: toggleExcluded,
    stalestFirst: stalestFirst,
    examLocked: examLocked,
    planFor: planFor,
    markDone: markDone,
    status: status,
    coverageStats: coverageStats
  };
});
