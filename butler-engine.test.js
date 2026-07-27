// Traces butler-engine.js against the real AMEB syllabus data.
// Run: node butler-engine.test.js
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const ROOT = __dirname;
const sandbox = { module: undefined, self: undefined };
vm.createContext(sandbox);
// The data file uses `const`, so it never lands on the context's global object.
// Re-export it explicitly — the browser has the same quirk, which is why butler.html
// probes with typeof rather than window.*
vm.runInContext(
  fs.readFileSync(path.join(ROOT, 'data_technical_ameb.js'), 'utf8') +
  '\nglobalThis.__TECH = DATA_TECHNICAL_AMEB;', sandbox);
vm.runInContext(
  fs.readFileSync(path.join(ROOT, 'data_aural_ameb.js'), 'utf8') +
  '\nglobalThis.__AURAL = DATA_AURAL_AMEB;', sandbox);
const TECH = sandbox.__TECH;
const AURAL = sandbox.__AURAL;

const E = require(path.join(ROOT, 'butler-engine.js'));

let pass = 0, fail = 0;
function ok(name, cond, extra) {
  if (cond) { pass++; console.log('  PASS  ' + name); }
  else { fail++; console.log('  FAIL  ' + name + (extra ? '  -> ' + extra : '')); }
}
function h(t) { console.log('\n' + t); }
const clone = o => JSON.parse(JSON.stringify(o));

// ---------------------------------------------------------------- data
h('Syllabus data');
ok('all grades load', Object.keys(TECH).length === 9, Object.keys(TECH).join(','));
const g5keys = E.coverageKeys('G5', TECH, AURAL);
const g5tech = g5keys.filter(k => k.kind === 'tech');
const g5areas = g5keys.filter(k => k.kind !== 'tech');
console.log('        G5: ' + g5tech.length + ' technical items, ' + g5areas.length + ' areas');
console.log('        sections: ' + [...new Set(g5tech.map(k => k.group))].join(' / '));
ok('G5 has a real technical list', g5tech.length > 20, String(g5tech.length));
// Aural is expanded into one row per test, so G5 = 4 aural + sight-reading + viva
// + theory + general knowledge.
const g5aural = g5areas.filter(k => k.areaId === 'aural');
ok('aural expands to one row per test', g5aural.length === AURAL.G5.tests.length,
  g5aural.length + ' vs ' + AURAL.G5.tests.length);
ok('6 drillable / 2 teacher-led',
  g5areas.filter(k => k.kind === 'area').length === 6 &&
  g5areas.filter(k => k.kind === 'manual').length === 2,
  g5areas.filter(k => k.kind === 'area').length + '/' + g5areas.filter(k => k.kind === 'manual').length);
ok('aural rows carry the full test wording',
  g5aural.every(k => k.desc && k.desc.length > 40));
ok('repeated categories get numbered',
  g5aural.filter(k => /^PITCH \d$/.test(k.label)).length === 2,
  g5aural.map(k => k.label).join(', '));
ok('a single-category test is not numbered',
  g5aural.some(k => k.label === 'RHYTHM'));
console.log('        G5 aural: ' + g5aural.map(k => k.label).join(', '));

// Diploma grades have no technical list and no aural table — aural falls back to one row.
const dip = E.coverageKeys('AMusA', TECH, AURAL);
ok('diploma falls back to a single aural row',
  dip.length === 5 && dip.filter(k => k.key === 'area:aural').length === 1,
  String(dip.length));

// ---------------------------------------------------------------- dates
h('Dates');
ok('weekOf(Monday) is itself', E.weekOf('2026-07-27') === '2026-07-27', E.weekOf('2026-07-27'));
ok('same week shares a weekOf', E.weekOf('2026-07-27') === E.weekOf('2026-08-02'));
ok('next week differs', E.weekOf('2026-08-03') !== E.weekOf('2026-08-02'));
ok('daysBetween is exact', E.daysBetween('2026-07-01', '2026-07-25') === 24);

// ---------------------------------------------------------------- fresh student
h('Fresh student, nothing practised');
const s = { id: 't1', name: 'Test', grade: 'G5', examDate: null, coverage: {}, weekPlan: null, dayPlan: null };
const p = E.planFor(s, '2026-07-27', TECH, AURAL);
ok('two daily technical items', p.daily.length === 2, String(p.daily.length));
ok('one weekly module', p.weekly.length === 1, String(p.weekly.length));
ok('no exam means no lockdown', p.locked === false);
console.log('        today: ' + p.daily.map(k => k.label).join(' | '));
console.log('        this week: ' + p.weekly.map(k => k.label).join(', '));

// ---------------------------------------------------------------- stalest first
h('Least-recently-practised first');
const s2 = clone(s);
g5tech.forEach(k => E.markDone(s2, k.key, '2026-07-27'));
E.markDone(s2, g5tech[10].key, '2026-07-27'); // toggle back off -> never practised
const stale1 = g5tech[3].key;
s2.coverage[stale1] = { last: '2026-06-01', prev: null, times: 1 };
s2.coverage[g5tech[17].key] = { last: '2026-06-10', prev: null, times: 1 };
const p2 = E.planFor(s2, '2026-07-27', TECH, AURAL);
ok('never-practised wins', p2.daily[0].key === g5tech[10].key, p2.daily[0].key);
ok('then the oldest date', p2.daily[1].key === stale1, p2.daily[1].key);
console.log('        picked: ' + p2.daily.map(k => k.label).join(' | '));

h('Deterministic, never random');
const runs = new Set();
for (let i = 0; i < 30; i++) {
  runs.add(E.planFor(clone(s2), '2026-07-27', TECH, AURAL).daily.map(k => k.key).join(','));
}
ok('30 runs give one result', runs.size === 1, runs.size + ' variants');

// ---------------------------------------------------------------- week pinning
h('Weekly module stays pinned');
const s3 = clone(s);
const wkA = E.planFor(s3, '2026-07-27', TECH, AURAL);
s3.weekPlan = wkA.weekPlan; s3.dayPlan = wkA.dayPlan;
const wkA2 = E.planFor(s3, '2026-07-30', TECH, AURAL);
ok('does not change mid-week', wkA.weekly[0].key === wkA2.weekly[0].key,
  wkA.weekly[0].label + ' -> ' + wkA2.weekly[0].label);

E.markDone(s3, wkA.weekly[0].key, '2026-07-30');
s3.weekPlan = wkA2.weekPlan;
const wkB = E.planFor(s3, '2026-08-03', TECH, AURAL);
ok('next week brings a different module', wkB.weekly[0].key !== wkA.weekly[0].key,
  wkA.weekly[0].label + ' -> ' + wkB.weekly[0].label);

const s4 = clone(s);
const seen = [];
['2026-07-27', '2026-08-03', '2026-08-10'].forEach(d => {
  const pp = E.planFor(s4, d, TECH, AURAL);
  s4.weekPlan = pp.weekPlan; s4.dayPlan = pp.dayPlan;
  seen.push(pp.weekly[0].label);
  E.markDone(s4, pp.weekly[0].key, d);
});
ok('three weeks cover all three drillable areas', new Set(seen).size === 3, seen.join(' -> '));

// ---------------------------------------------------------------- exam lockdown
h('Exam lockdown at 8 weeks');
const far = Object.assign(clone(s), { examDate: '2026-12-01' });
const near = Object.assign(clone(s), { examDate: '2026-09-01' });
const pFar = E.planFor(far, '2026-07-27', TECH, AURAL);
const pNear = E.planFor(near, '2026-07-27', TECH, AURAL);
ok('18 weeks out: normal rotation', pFar.locked === false && pFar.weekly.length === 1);
ok('5 weeks out: locked', pNear.locked === true);
ok('locked shows every drillable area', pNear.weekly.length === 3, String(pNear.weekly.length));
ok('exactly 8 weeks still locks',
  E.planFor(Object.assign(clone(s), { examDate: '2026-09-21' }), '2026-07-27', TECH, AURAL).locked === true);
ok('long-past exam unlocks',
  E.planFor(Object.assign(clone(s), { examDate: '2026-06-01' }), '2026-07-27', TECH, AURAL).locked === false);

// ---------------------------------------------------------------- toggle
h('Tick toggling');
const s5 = clone(s);
E.markDone(s5, 'ex:5A', '2026-07-20');
E.markDone(s5, 'ex:5A', '2026-07-27');
ok('second tick updates the date', E.lastAt(s5, 'ex:5A') === '2026-07-27');
E.markDone(s5, 'ex:5A', '2026-07-27');
ok('tapping again restores the previous date', E.lastAt(s5, 'ex:5A') === '2026-07-20',
  String(E.lastAt(s5, 'ex:5A')));
ok('times never goes negative', s5.coverage['ex:5A'].times >= 0);

// ---------------------------------------------------------------- stats
h('Coverage stats');
const s6 = clone(s);
g5tech.slice(0, 10).forEach(k => E.markDone(s6, k.key, '2026-07-27'));
const st = E.coverageStats(s6, '2026-07-27', TECH, AURAL);
ok('touched count', st.touched === 10, String(st.touched));
ok('total equals technical item count', st.total === g5tech.length);
ok('the rest are stale', st.stale === g5tech.length - 10, String(st.stale));
console.log('        coverage ' + st.pct + '% (' + st.touched + '/' + st.total + '), ' +
  st.stale + ' untouched for 3+ weeks');

// ---------------------------------------------------------------- day pinning
h("Today's list is pinned — ticking must not replace items");
const d1 = clone(s);
const pd = E.planFor(d1, '2026-07-27', TECH, AURAL);
d1.dayPlan = pd.dayPlan; d1.weekPlan = pd.weekPlan;
const firstKeys = pd.daily.map(k => k.key);
console.log('        assigned: ' + pd.daily.map(k => k.label).join(' | '));

E.markDone(d1, firstKeys[0], '2026-07-27');
const pd2 = E.planFor(d1, '2026-07-27', TECH, AURAL);
ok('same items after ticking one',
  pd2.daily.map(k => k.key).join(',') === firstKeys.join(','),
  pd2.daily.map(k => k.label).join(' | '));
ok('done count reflects it', pd2.done === 1, String(pd2.done));
ok('not allDone yet', pd2.allDone === false);

E.markDone(d1, firstKeys[1], '2026-07-27');
E.markDone(d1, pd2.weekly[0].key, '2026-07-27');
const pd3 = E.planFor(d1, '2026-07-27', TECH, AURAL);
ok('everything ticked gives allDone', pd3.allDone === true, pd3.done + '/' + pd3.total);

h('Next day brings new items');
d1.dayPlan = pd3.dayPlan;
const pd4 = E.planFor(d1, '2026-07-28', TECH, AURAL);
ok("yesterday's items drop out", pd4.daily.every(k => !firstKeys.includes(k.key)),
  pd4.daily.map(k => k.label).join(' | '));
ok('back to not done', pd4.done === 0 && pd4.allDone === false);
console.log('        next day: ' + pd4.daily.map(k => k.label).join(' | '));

h('Pinned list is topped up if a key disappears');
const d2 = clone(s);
d2.dayPlan = { date: '2026-07-27', keys: ['sc:99:99', 'ex:5A'] }; // one key no longer exists
const pd5 = E.planFor(d2, '2026-07-27', TECH, AURAL);
ok('refilled back to two', pd5.daily.length === 2, String(pd5.daily.length));
ok('the still-valid key is kept', pd5.daily.some(k => k.key === 'ex:5A'));

// ---------------------------------------------------------------- aural rotation
h('Aural does not dominate the weekly rotation');
// Aural contributes 4 keys against sight-reading's and viva's 1 each. Ranking raw
// keys would hand aural the weekly slot almost every week.
const a1 = clone(s);
const weeks = ['2026-07-27', '2026-08-03', '2026-08-10', '2026-08-17', '2026-08-24', '2026-08-31'];
const picked = [];
weeks.forEach(d => {
  const pp = E.planFor(a1, d, TECH, AURAL);
  a1.weekPlan = pp.weekPlan; a1.dayPlan = pp.dayPlan;
  picked.push(pp.weekly[0].areaId);
  pp.weekly.forEach(k => E.markDone(a1, k.key, d));
});
ok('all three areas appear across six weeks', new Set(picked).size === 3, picked.join(' -> '));
ok('each area gets exactly two of the six weeks',
  [...new Set(picked)].every(a => picked.filter(x => x === a).length === 2),
  picked.join(' -> '));
ok('no area runs two weeks back to back',
  picked.every((a, i) => i === 0 || a !== picked[i - 1]), picked.join(' -> '));
console.log('        rotation: ' + picked.join(' -> '));

h('An aural week serves one test at a time, stalest first');
const a2 = clone(s);
// force aural to be the week's area by making the others fresh
E.markDone(a2, 'area:sightread', '2026-07-27');
E.markDone(a2, 'area:viva', '2026-07-27');
const pa = E.planFor(a2, '2026-07-27', TECH, AURAL);
ok('the week lands on aural', pa.weekly[0].areaId === 'aural', pa.weekly[0].areaId);
ok('exactly one aural test on the card', pa.weekly.length === 1, String(pa.weekly.length));
a2.dayPlan = pa.dayPlan; a2.weekPlan = pa.weekPlan;
E.markDone(a2, pa.weekly[0].key, '2026-07-27');
const pa2 = E.planFor(a2, '2026-07-27', TECH, AURAL);
ok('ticking it does not swap in another test the same day',
  pa2.weekly[0].key === pa.weekly[0].key, pa2.weekly[0].label);
a2.dayPlan = pa2.dayPlan;
const pa3 = E.planFor(a2, '2026-07-28', TECH, AURAL);
ok('the next day moves to a different aural test',
  pa3.weekly[0].key !== pa.weekly[0].key,
  pa.weekly[0].label + ' -> ' + pa3.weekly[0].label);

h('Exam lockdown serves one test from every area');
const a3 = Object.assign(clone(s), { examDate: '2026-09-01' });
const pa4 = E.planFor(a3, '2026-07-27', TECH, AURAL);
ok('three rows, one per area', pa4.weekly.length === 3, String(pa4.weekly.length));
ok('one of them is an aural test',
  pa4.weekly.filter(k => k.areaId === 'aural').length === 1,
  pa4.weekly.map(k => k.areaId).join(','));

// ---------------------------------------------------------------- exclusions
h('Switching items off (Piano for Leisure, untaught scales, exemptions)');
const x1 = clone(s);
const statsBefore = E.coverageStats(x1, '2026-07-27', TECH, AURAL);
E.toggleExcluded(x1, g5tech[0].key);
E.toggleExcluded(x1, g5tech[1].key);
E.toggleExcluded(x1, g5tech[2].key);
const statsAfter = E.coverageStats(x1, '2026-07-27', TECH, AURAL);
ok('denominator shrinks by the number switched off',
  statsAfter.total === statsBefore.total - 3,
  statsBefore.total + ' -> ' + statsAfter.total);
ok('isExcluded reports it', E.isExcluded(x1, g5tech[0].key) === true);
ok('toggling again switches it back on',
  E.toggleExcluded(x1, g5tech[0].key) && E.isExcluded(x1, g5tech[0].key) === false);

h('Excluded items leave the rotation');
const x2 = clone(s);
const before = E.planFor(x2, '2026-07-27', TECH, AURAL).daily.map(k => k.key);
before.forEach(k => E.toggleExcluded(x2, k));
const after = E.planFor(x2, '2026-07-27', TECH, AURAL);
ok('the switched-off picks are replaced',
  after.daily.every(k => !before.includes(k.key)) && after.daily.length === 2,
  after.daily.map(k => k.label).join(' | '));

h('A pinned day plan drops items switched off mid-day');
const x3 = clone(s);
const px = E.planFor(x3, '2026-07-27', TECH, AURAL);
x3.dayPlan = px.dayPlan; x3.weekPlan = px.weekPlan;
E.toggleExcluded(x3, px.daily[0].key);
const px2 = E.planFor(x3, '2026-07-27', TECH, AURAL);
ok('still two items, the excluded one gone',
  px2.daily.length === 2 && !px2.daily.some(k => k.key === px.daily[0].key),
  px2.daily.map(k => k.label).join(' | '));

h('Areas can be switched off too');
const x4 = clone(s);
g5aural.forEach(k => E.toggleExcluded(x4, k.key));   // the whole aural area
E.toggleExcluded(x4, 'area:sightread');
const px4 = E.planFor(x4, '2026-07-27', TECH, AURAL);
ok('weekly module skips excluded areas',
  px4.weekly.length === 1 && px4.weekly[0].key === 'area:viva',
  px4.weekly.map(k => k.key).join(','));

h('Individual aural tests can be switched off');
const x6 = clone(s);
E.toggleExcluded(x6, g5aural[0].key);
const remaining = E.coverageKeys('G5', TECH, AURAL)
  .filter(k => k.areaId === 'aural' && !E.isExcluded(x6, k.key));
ok('one aural test off, the rest stay', remaining.length === g5aural.length - 1);
const px6 = E.planFor(x6, '2026-07-27', TECH, AURAL);
ok('the switched-off test is never served',
  px6.weekly.every(k => k.key !== g5aural[0].key));

h('Everything switched off does not crash');
const x5 = clone(s);
E.coverageKeys('G5', TECH, AURAL).forEach(k => E.toggleExcluded(x5, k.key));
const px5 = E.planFor(x5, '2026-07-27', TECH, AURAL);
ok('empty plan, no throw', px5.daily.length === 0 && px5.weekly.length === 0);
ok('allDone is false on an empty plan', px5.allDone === false);
ok('stats read 0 of 0 without dividing by zero',
  E.coverageStats(x5, '2026-07-27', TECH, AURAL).pct === 0);

// ---------------------------------------------------------------- status
h('Status thresholds');
const s7 = { grade: 'G5', coverage: { a: { last: '2026-07-27' }, b: { last: '2026-07-20' }, c: { last: '2026-07-06' } } };
ok('today -> ok', E.status(s7, 'a', '2026-07-27') === 'ok');
ok('7 days -> warn', E.status(s7, 'b', '2026-07-27') === 'warn');
ok('21 days -> late', E.status(s7, 'c', '2026-07-27') === 'late');
ok('no record -> never', E.status(s7, 'zzz', '2026-07-27') === 'never');

// ---------------------------------------------------------------- language rule
// CLAUDE.md: "All code, file outputs, comments: English only."
h('English-only check');
// Escaped ranges (compatibility jamo + syllables) so this file stays ASCII itself.
const hangul = /[\u3131-\u318E\uAC00-\uD7A3]/;
['butler.html', 'butler-engine.js', 'butler-engine.test.js'].forEach(f => {
  const lines = fs.readFileSync(path.join(ROOT, f), 'utf8').split('\n');
  const bad = lines.map((l, i) => ({ n: i + 1, l })).filter(x => hangul.test(x.l));
  ok(f + ' has no Korean', bad.length === 0,
    bad.slice(0, 3).map(x => 'line ' + x.n + ': ' + x.l.trim().slice(0, 50)).join(' // '));
});

console.log('\n' + pass + ' passed, ' + fail + ' failed\n');
process.exit(fail ? 1 : 0);
