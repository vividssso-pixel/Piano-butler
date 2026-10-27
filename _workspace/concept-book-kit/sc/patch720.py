import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
def rep_in(fn_start, pairs):   # replacements inside one function only
    global s
    assert s.count(fn_start) == 1, fn_start
    a = s.index(fn_start); b = s.index('\n}\n', a) + 3; body = s[a:b]
    for old, new, *k in pairs:
        n = k[0] if k else 1
        assert body.count(old) == n, (body.count(old), old[:80])
        body = body.replace(old, new)
    s = s[:a] + body + s[b:]
def rep_line(prefix, new):   # replace the one whole line that starts with prefix
    global s
    lines = s.split('\n'); hits = [i for i, x in enumerate(lines) if x.startswith(prefix)]
    assert len(hits) == 1, (len(hits), prefix[:80])
    lines[hits[0]] = new; s = '\n'.join(lines)

# Build BA (board call 23, the second Grade 5 room): Scales and Arpeggios, Grade 5. From the technical work book, Grade 5
# (pp19-24, read 27 Oct): scales four octaves, hands separately and together, clear even legato, crotchet 84 four notes a beat,
# in B major, G-sharp harmonic and melodic minor, D-flat major, B-flat harmonic and melodic minor, each prepared (i) all p,
# (ii) all f, (iii) p < f ascending, f > p descending; staccato (D-flat major, B-flat melodic minor) mf at crotchet 60; contrary
# motion two octaves, mf, crotchet 60, in E major, C-sharp harmonic minor, A-flat major, F harmonic minor; chromatic from B and
# from C-sharp/D-flat, four octaves, all p and all f, crotchet 84; arpeggios of B major and minor and D-flat major and minor,
# four octaves, hands separately and together, mf, crotchet 52 four notes a beat. The Grade 4 pads take the keys as props.

# ── registrations ──
rep("""const SCALES_4_DRILL = { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4' };   // Build AS""",
    """const SCALES_4_DRILL = { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4' };   // Build AS
const SCALES_5_DRILL = { id: 'scales-5', label: 'Scales and Arpeggios, Grade 5' };   // Build BA""")
rep("""  { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4', concept: SCALES_4_DRILL, track: 'start' },   // Build AS""",
    """  { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4', concept: SCALES_4_DRILL, track: 'start' },   // Build AS
  { id: 'scales-5', label: 'Scales and Arpeggios, Grade 5', concept: SCALES_5_DRILL, track: 'start' },   // Build BA""")
rep("""'scales-4': '스케일과 아르페지오, Grade 4'""", """'scales-4': '스케일과 아르페지오, Grade 4', 'scales-5': '스케일과 아르페지오, Grade 5'""")
rep("""'scales-4': 'k-play'""", """'scales-4': 'k-play', 'scales-5': 'k-play'""")
rep("""'scales-4': ['scales-23']""", """'scales-4': ['scales-23'], 'scales-5': ['scales-4']""")
rep("""'scales-4': ['Scales 4', '스케일 4']""", """'scales-4': ['Scales 4', '스케일 4'], 'scales-5': ['Scales 5', '스케일 5']""")
rep("""  'scales-4': 'scales arpeggios grade 4""", """  'scales-5': 'scales arpeggios grade 5 four octaves finger 4 dynamics piano forte p f crescendo diminuendo hairpin staccato contrary motion mirror twins chromatic hands together arpeggio four notes a beat thumb technique',
  'scales-4': 'scales arpeggios grade 4""")

# ── the Grade 4 data and pads, opened up for Grade 5 ──
rep("""  Csmel: { en: 'C♯ melodic minor', ko: 'C♯ 가락 단음계', st: S4_MEL, r: 1,""",
    """  Csmel: { en: 'C♯ melodic minor', ko: 'C♯ 가락 단음계', st: S4_MEL, dn: SP_NAT, dn4: { R: ['goes back to D♯', '다시 D♯'] }, r: 1,""")
rep("""const s4Chip = (k) => (k === 'Csmel'""", """const s4Chip = (k) => (S4_SC[k].chip ? t(S4_SC[k].chip[0], S4_SC[k].chip[1]) : k === 'Csmel'""")
rep("""dn = k === 'Csmel' ? SP_NAT : c.st, out = [];""", """dn = c.dn || c.st, out = [];""")
rep_in("function S4FourPad({ fixed, onResult }) {", [
    ("function S4FourPad({ fixed, onResult }) {", "function S4FourPad({ fixed, onResult, keys = S4_KEYS, bpm = 63 }) {"),
    ("useState(fixed ? fixed.k : 'E')", "useState(fixed ? fixed.k : keys[0])"),
    ("0.13 })), 63, 4); if (!run) return;", "0.13 })), bpm, 4); if (!run) return;"),
    ("spChips(S4_KEYS.map(x => [x, s4Chip(x)])", "spChips(keys.map(x => [x, s4Chip(x)])"),
    ("{s4Name(k)}{k === 'Csmel' ? t(', going up', ', 올라갈 때') : ''}", "{s4Name(k)}{c.dn ? t(', going up', ', 올라갈 때') : ''}"),
])
rep_line("  const extra = done ? (k === 'Csmel' && h === 'R'", "  const extra = done ? s4Extra(k, h) : '';")
rep("""function S4FourPad({ fixed, onResult, keys""", """// what else to say once finger 4 is found: the melodic minor's 4 coming down; a first octave without a 4; a first note on 4
const s4Ro = (n) => ([0, 3, 6].includes(n) ? '으로' : '로');
const s4Extra = (k, h) => { const c = S4_SC[k], j4 = s4F4(k, h), first = c[h].slice(0, 7);
  if (c.dn4 && c.dn4[h]) return t(' Coming down (the natural minor) it ' + c.dn4[h][0] + '.', ' 내려올 때(자연 단음계)는 ' + c.dn4[h][1] + '.');
  if (first[j4] !== 4) return t(' The very first octave starts on ' + first[0] + ' ' + first[1] + ', so 4 joins from the second octave.', ' 맨 처음 옥타브는 ' + first[0] + ' ' + first[1] + s4Ro(first[1]) + ' 시작해서, 4는 둘째 옥타브부터.');
  if (first[0] === 4 && j4 !== 0) return t(' The very first note, the bottom ' + c.nm[0] + ', takes 4 as well: only there.', ' 맨 처음 음, 맨 아래 ' + c.nm[0] + '도 4번: 거기서만.');
  return ''; };
function S4FourPad({ fixed, onResult, keys""")
rep_in("function S4MirrorPad({ fixed, onResult }) {", [
    ("function S4MirrorPad({ fixed, onResult }) {", "function S4MirrorPad({ fixed, onResult, keys = S4_CM_KEYS, chip = s4CmChip, bpm = 52, g = 4 }) {"),
    ("useState(fixed || 'A4')", "useState(fixed || keys[0])"),
    ("0.12 })), 52, 4); };", "0.12 })), bpm, 4); };"),
    ("<>4급의 반대 방향: 두 옥타브,", "<>{g}급의 반대 방향: 두 옥타브,"),
    ("<>Grade 4 contrary motion: two octaves,", "<>Grade {g} contrary motion: two octaves,"),
    ("scfKeyChips(S4_CM_KEYS, k, (x) => reset(() => setK(x)), s4CmChip)", "scfKeyChips(keys, k, (x) => reset(() => setK(x)), chip)"),
])
rep_in("function S4ChromPad({ fixed, onResult }) {", [
    ("function S4ChromPad({ fixed, onResult }) {", "function S4ChromPad({ fixed, onResult, set = S4_CH, bpm = 63, g = 4 }) {"),
    ("const s0 = S4_CH[st][1],", "const s0 = set[st][1],"),
    ("0.11 })), 63, 4); if (!run) return;", "0.11 })), bpm, 4); if (!run) return;"),
    ("<>4급 반음계: 네 옥타브, 양손 함께.", "<>{g}급 반음계: 네 옥타브, 양손 함께."),
    ("<>Grade 4 chromatic: four octaves, hands together.", "<>Grade {g} chromatic: four octaves, hands together."),
    ("spChips(S4_CH.map(([n], j)", "spChips(set.map(([n], j)"),
])
rep("""const S4_AR_KEYS = ['E', 'Em', 'Ab', 'Abm'];""", """const S4_AR_KEYS = ['E', 'Em', 'Ab', 'Abm'];
const s4ArChip = (x) => S4_AR[x].nm[0] + (S4_AR[x].q[1] === 3 ? 'm' : '');""")
rep_in("function S4ArpPad({ fixed, onResult }) {", [
    ("function S4ArpPad({ fixed, onResult }) {", "function S4ArpPad({ fixed, onResult, keys = S4_AR_KEYS, per = 2, bpm = 76, note = null }) {"),
    ("useState(fixed ? fixed.k : 'E')", "useState(fixed ? fixed.k : keys[0])"),
    ("const sq = s4ArSeq(k, c.r - 12 - sh), run = spPlay(sq.map((x, n) => ({ at: n / 2, keys: [x], len: n === sq.length - 1 ? 1.5 : 0.5, vol: 0.13 })), 76, 2); if (!run) return;",
     "const sq = s4ArSeq(k, c.r - 12 - (per === 4 ? 0 : sh)), run = spPlay(sq.map((x, n) => ({ at: n / per, keys: per === 4 ? [x, x - 12] : [x], len: n === sq.length - 1 ? 1.5 : 1 / per, vol: 0.13 })), bpm, 2); if (!run) return;"),
    ("sq.forEach((x, n) => T.at(run.ms(n / 2), () => setPl(spPc(x)))); T.at(run.ms(sq.length / 2 + 1), () => setPl(null)); };",
     "sq.forEach((x, n) => T.at(run.ms(n / per), () => setPl(spPc(x)))); T.at(run.ms(sq.length / per + 1), () => setPl(null)); };"),
    ("<div style={actNote}>{LANG === 'ko' ? <>4급 아르페지오", "<div style={actNote}>{note ? note : LANG === 'ko' ? <>4급 아르페지오"),
    ("spChips(S4_AR_KEYS.map(x => [x, x === 'Em' ? 'Em' : x === 'Abm' ? 'A♭m' : S4_AR[x].nm[0]])", "spChips(keys.map(x => [x, s4ArChip(x)])"),
])
rep_in("function S4Question({ q, given, locked, onAnswer, pixel }) {", [
    ("(q.k === 'Csmel' ? ' going up' : '')", "(S4_SC[q.k].dn ? ' going up' : '')"),
    ("(q.k === 'Csmel' ? '(올라갈 때)' : '')", "(S4_SC[q.k].dn ? '(올라갈 때)' : '')"),
    ("const s0 = S4_CH[q.st][1], lit", "const s0 = q.s0 != null ? q.s0 : S4_CH[q.st][1], lit"),
])

# ── the chapter ──
CH = r'''
// ─── Chapter: Scales and Arpeggios, Grade 5 (Build BA, 2026-10-27; board call 23, the second Grade 5 room) ───
// What Grade 5 adds to the Grade 4 room: new keys over the same four octaves (and in all four, the right hand's 4 lands on one
// black key, A♯ = B♭); each scale three ways: all p, all f, louder going up and softer coming down; staccato at mf; contrary
// motion in the Grade 4 keys; the chromatic scale from B and C♯/D♭ in p and in f; arpeggios four notes a beat, hands separately
// and together. The keys, speeds and fingerings are the technical work book's (Grade 5 pp19-24).
Object.assign(S4_SC, {   // four octaves going up, as the book's two printed octaves repeat
  B: { en: 'B major', ko: 'B장조', st: SP_MAJ, r: -1, nm: ['B', 'C♯', 'D♯', 'E', 'F♯', 'G♯', 'A♯'], R: s4Run([1, 2, 3, 1, 2, 3, 4], [1, 2, 3, 1, 2, 3, 4], 5), L: s4Run([4, 3, 2, 1, 4, 3, 2], [1, 3, 2, 1, 4, 3, 2], 1) },
  Gsm: { en: 'G♯ harmonic minor', ko: 'G♯ 화성 단음계', chip: ['G♯m harmonic', 'G♯m 화성'], st: SP_HAR, r: -4, nm: ['G♯', 'A♯', 'B', 'C♯', 'D♯', 'E', 'F𝄪'], R: s4Run([2, 3, 1, 2, 3, 1, 2], [3, 4, 1, 2, 3, 1, 2], 3), L: s4Run([3, 2, 1, 4, 3, 2, 1], [3, 2, 1, 4, 3, 2, 1], 2) },
  Gsmel: { en: 'G♯ melodic minor', ko: 'G♯ 가락 단음계', chip: ['G♯m melodic', 'G♯m 가락'], st: S4_MEL, dn: SP_NAT, r: -4, nm: ['G♯', 'A♯', 'B', 'C♯', 'D♯', 'E♯', 'F𝄪'], R: s4Run([2, 3, 1, 2, 3, 1, 2], [3, 4, 1, 2, 3, 1, 2], 3), L: s4Run([3, 2, 1, 4, 3, 2, 1], [3, 2, 1, 4, 3, 2, 1], 2) },
  Db: { en: 'D♭ major', ko: 'D♭장조', st: SP_MAJ, r: 1, nm: ['D♭', 'E♭', 'F', 'G♭', 'A♭', 'B♭', 'C'], R: s4Run([2, 3, 1, 2, 3, 4, 1], [2, 3, 1, 2, 3, 4, 1], 2), L: s4Run([3, 2, 1, 4, 3, 2, 1], [3, 2, 1, 4, 3, 2, 1], 2) },
  Bbm: { en: 'B♭ harmonic minor', ko: 'B♭ 화성 단음계', chip: ['B♭m harmonic', 'B♭m 화성'], st: SP_HAR, r: -2, nm: ['B♭', 'C', 'D♭', 'E♭', 'F', 'G♭', 'A'], R: s4Run([2, 1, 2, 3, 1, 2, 3], [4, 1, 2, 3, 1, 2, 3], 4), L: s4Run([2, 1, 3, 2, 1, 4, 3], [2, 1, 3, 2, 1, 4, 3], 2) },
  Bbmel: { en: 'B♭ melodic minor', ko: 'B♭ 가락 단음계', chip: ['B♭m melodic', 'B♭m 가락'], st: S4_MEL, dn: SP_NAT, dn4: { L: ['moves to G♭', 'G♭'] }, r: -2, nm: ['B♭', 'C', 'D♭', 'E♭', 'F', 'G', 'A'], R: s4Run([2, 1, 2, 3, 1, 2, 3], [4, 1, 2, 3, 1, 2, 3], 4), L: s4Run([2, 1, 3, 2, 1, 4, 3], [2, 1, 3, 2, 1, 4, 3], 2) },
});
const S5_KEYS = ['B', 'Gsm', 'Gsmel', 'Db', 'Bbm', 'Bbmel'];
Object.assign(S4_ST, {   // the two staccato scales, two octaves up and down
  Db: { en: 'D♭ major', ko: 'D♭장조', r: 1, up: SP_MAJ, dn: SP_MAJ, nmU: ['D♭', 'E♭', 'F', 'G♭', 'A♭', 'B♭', 'C'], nmD: ['D♭', 'E♭', 'F', 'G♭', 'A♭', 'B♭', 'C'] },
  Bbmel: { en: 'B♭ melodic minor', ko: 'B♭ 가락 단음계', r: -2, up: S4_MEL, dn: SP_NAT, nmU: ['B♭', 'C', 'D♭', 'E♭', 'F', 'G', 'A'], nmD: ['B♭', 'C', 'D♭', 'E♭', 'F', 'G♭', 'A♭'] },
});
Object.assign(SCF_CM, {   // contrary motion, the first octave of two (Grade 5 p22): the Grade 4 similar-motion keys
  E5: { g: 5, en: 'E major', ko: 'E장조', st: SP_MAJ, s: 4, nm: ['E', 'F♯', 'G♯', 'A', 'B', 'C♯', 'D♯'], R: [1, 2, 3, 1, 2, 3, 4, 1], L: [1, 2, 3, 1, 2, 3, 4, 1] },
  Csmh: { g: 5, en: 'C♯ harmonic minor', ko: 'C♯ 화성 단음계', st: SP_HAR, s: 1, nm: ['C♯', 'D♯', 'E', 'F♯', 'G♯', 'A', 'B♯'], R: [2, 3, 1, 2, 3, 1, 2, 3], L: [2, 1, 2, 3, 4, 1, 2, 3] },
  Ab5: { g: 5, en: 'A♭ major', ko: 'A♭장조', st: SP_MAJ, s: -4, nm: ['A♭', 'B♭', 'C', 'D♭', 'E♭', 'F', 'G'], R: [2, 3, 1, 2, 3, 1, 2, 3], L: [2, 1, 2, 3, 4, 1, 2, 3] },
  Fmh: { g: 5, en: 'F harmonic minor', ko: 'F 화성 단음계', st: SP_HAR, s: 5, nm: ['F', 'G', 'A♭', 'B♭', 'C', 'D♭', 'E'], R: [1, 2, 3, 4, 1, 2, 3, 1], L: [1, 2, 3, 1, 2, 3, 4, 1] },
});
const S5_CM_KEYS = ['E5', 'Csmh', 'Ab5', 'Fmh'];
const s5CmChip = (k) => ({ E5: 'E', Csmh: 'C♯m', Ab5: 'A♭', Fmh: 'Fm' })[k];
const S5_CH = [['B', -1], ['C♯/D♭', 1]];
Object.assign(S4_AR, {   // two octaves going up, as the book prints them (Grade 5 p24)
  B: { en: 'B major', ko: 'B장조', r: -1, q: [0, 4, 7], nm: ['B', 'D♯', 'F♯'], R: [1, 2, 3, 1, 2, 3, 5], L: [5, 3, 2, 1, 3, 2, 1] },
  Bm: { en: 'B minor', ko: 'B단조', r: -1, q: [0, 3, 7], nm: ['B', 'D', 'F♯'], R: [1, 2, 3, 1, 2, 3, 5], L: [5, 4, 2, 1, 4, 2, 1] },
  Db: { en: 'D♭ major', ko: 'D♭장조', r: 1, q: [0, 4, 7], nm: ['D♭', 'F', 'A♭'], R: [2, 1, 2, 4, 1, 2, 4], L: [2, 1, 4, 2, 1, 4, 2] },
  Dbm: { en: 'D♭ minor', ko: 'D♭단조', r: 1, q: [0, 3, 7], nm: ['D♭', 'F♭', 'A♭'], R: [2, 1, 2, 4, 1, 2, 4], L: [2, 1, 4, 2, 1, 4, 2] },
});
const S5_AR_KEYS = ['B', 'Bm', 'Db', 'Dbm'];
// the Grade 4 pads with the Grade 5 keys and speeds
function S5FourPad(p) { return <S4FourPad keys={S5_KEYS} bpm={84} {...p}/>; }
function S5MirrorPad(p) { return <S4MirrorPad keys={S5_CM_KEYS} chip={s5CmChip} bpm={60} g={5} {...p}/>; }
function S5ChromPad(p) { return <S4ChromPad set={S5_CH} bpm={84} g={5} {...p}/>; }
function S5ArpPad(p) { return <S4ArpPad keys={S5_AR_KEYS} per={4} bpm={52} note={LANG === 'ko' ? <>5급 아르페지오: 네 옥타브, 한 손씩 <b>그리고 양손 함께</b>, <b>한 박에 네 음</b>. 엄지는 흰건반에: B장조와 B단조는 <b>B</b>, D♭에서는 하나뿐인 흰건반 <b>F</b>(단조는 F♭). 빨간 건반의 손가락을 골라요.</>
  : <>Grade 5 arpeggios: four octaves, hands separately <b>and together</b>, <b>four notes a beat</b>. The thumb takes a white key: <b>B</b> in B major and minor; in D♭ the only white key, <b>F</b> (F♭ in the minor). Choose the finger for the coral key.</>} {...p}/>; }

// ── step 2: one scale, four ways: all p, all f, louder going up and softer coming down, and staccato (mf) ──
const S5_WAYS = ['p', 'f', 'cd', 'st'];
const S5_WAY = { p: ['All soft: p', '모두 여리게: p'], f: ['All loud: f', '모두 세게: f'], cd: ['Louder up, softer down', '올라가며 세게, 내려오며 여리게'], st: ['Staccato, mf', '스타카토, mf'] };
const S5_YES = { p: ['Yes: all p, soft from the bottom to the top and back.', '맞아요: 모두 p, 처음부터 끝까지 여리게.'], f: ['Yes: all f, full from the bottom to the top and back.', '맞아요: 모두 f, 처음부터 끝까지 세게.'],
  cd: ['Yes: louder all the way up, softer all the way down.', '맞아요: 꼭대기까지 점점 세게, 내려오며 점점 여리게.'], st: ['Yes: staccato, short and even, mf.', '맞아요: 스타카토, 짧고 고르게, mf.'] };
const s5WayName = (m) => t(S5_WAY[m][0], S5_WAY[m][1]);
const s5Lv = (m, j, n) => { const top = (n - 1) / 2; return m === 'p' ? 0 : m === 'f' ? 1 : m === 'st' ? 0.45 : 1 - Math.abs(j - top) / top; };   // 0 soft … 1 loud
const s5Bpm = (m) => (m === 'st' ? 60 : 84);
// four clicks, the same loudness every time (the yardstick), then the scale two octaves up and down, four notes a beat
const s5PlayWay = (k, m) => { const ctx = getAudio(); if (!ctx) return null; stopClicks();
  const sq = s4Two(k), n = sq.length, spb = 60 / s5Bpm(m), t0 = ctx.currentTime + 0.15;
  for (let b = 0; b < 4; b++) metroClick(ctx, t0 + b * spb, false, 0.25);
  sq.forEach((x, j) => blip(ctx, t0 + (4 + j / 4) * spb, spHz(x.i), m === 'st' ? spb * 0.07 : j === n - 1 ? spb * 1.5 : spb / 4 * 0.98, 0.05 + 0.21 * s5Lv(m, j, n), 'triangle'));
  return { n, ms: (beat) => (0.15 + (4 + beat) * spb) * 1000, end: (0.15 + (4 + n / 4 + 1.5) * spb) * 1000 }; };
// the scale as a hill, two octaves up and down: the thicker the line, the louder; staccato as dots; no way yet: faint dots
function S5Ribbon({ m = null, cur = -1, w = 300, marks = true }) {
  const n = 29, X = (j) => (12 + j * 276 / (n - 1)).toFixed(1), Y = (j) => 62 - (j <= 14 ? j : 28 - j) * 3.2, ink = '#26296b';
  let svg = '';
  if (!m || m === 'st') for (let j = 0; j < n; j++) svg += '<circle cx="' + X(j) + '" cy="' + Y(j).toFixed(1) + '" r="' + (m ? 2.7 : 1.9) + '" fill="' + (m ? ink : 'rgba(38,41,107,0.3)') + '"/>';
  else { const hw = (j) => 1.1 + 5.4 * s5Lv(m, j, n), top = [], bot = [];
    for (let j = 0; j < n; j++) { top.push(X(j) + ',' + (Y(j) - hw(j)).toFixed(1)); bot.unshift(X(j) + ',' + (Y(j) + hw(j)).toFixed(1)); }
    svg += '<polygon points="' + top.concat(bot).join(' ') + '" fill="' + ink + '" stroke="' + ink + '" stroke-width="0.6" stroke-linejoin="round"/>'; }
  if (cur >= 0 && cur < n) svg += '<circle cx="' + X(cur) + '" cy="' + Y(cur).toFixed(1) + '" r="5.2" fill="#e4572e" stroke="#fff" stroke-width="1.5"/>';
  if (marks && m) { const dyn = (x, txt) => '<text x="' + x + '" y="89" text-anchor="middle" font-family="Georgia, \'Times New Roman\', serif" font-style="italic" font-weight="700" font-size="15" fill="' + ink + '">' + txt + '</text>';
    const pin = (x0, x1, open) => '<path d="' + (open ? 'M' + x1 + ' 79 L' + x0 + ' 84 L' + x1 + ' 89' : 'M' + x0 + ' 79 L' + x1 + ' 84 L' + x0 + ' 89') + '" fill="none" stroke="' + ink + '" stroke-width="1.3"/>';
    svg += m === 'cd' ? dyn(14, 'p') + pin(26, 136, true) + dyn(150, 'f') + pin(164, 274, false) + dyn(286, 'p') : dyn(150, m === 'st' ? 'mf' : m); }
  return <svg viewBox="0 0 300 94" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={m ? s5WayName(m) : t('The scale', '스케일')} dangerouslySetInnerHTML={{ __html: svg }}/>;
}
function S5DynPad({ onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState('Db'), [m, setM] = useState('cd'), [cur, setCur] = useState(-1), [quiz, setQuiz] = useState(null), [ans, setAns] = useState(null);
  const last = useRef(null);
  const reset = (fn) => { T.clear(); setCur(-1); setQuiz(null); setAns(null); if (fn) fn(); };
  const hear = (kk, mm) => { T.clear(); setCur(-1); const r = s5PlayWay(kk, mm); if (!r) return; for (let j = 0; j < r.n; j++) T.at(r.ms(j / 4), () => setCur(j)); T.at(r.end, () => setCur(-1)); };
  const way = (x) => { if (quiz) { if (ans) return; T.clear(); setCur(-1); setAns(x); if (onResult) onResult({ ok: x === quiz }); return; } setM(x); hear(k, x); };
  const ask = () => { let x, g = 0; do { x = pick(S5_WAYS); } while (x === last.current && g++ < 10); last.current = x; setQuiz(x); setAns(null); hear(k, x); };
  const shown = quiz ? (ans ? quiz : null) : m, ok = !!ans && ans === quiz;
  return (
    <div className="try-box" style={actBox} data-s5="dyn">
      <div style={actTitle}>{t('One scale, four ways', '한 스케일, 네 가지로')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>5급은 스케일마다 <b>세 가지로</b>: 모두 <b>p</b>, 모두 <b>f</b>, 그리고 <b>올라가며 세게, 내려오며 여리게</b>. D♭장조와 B♭ 가락 단음계는 <b>스타카토</b>도(mf). 손가락은 그대로, 소리만 달라져요. <b>줄이 굵을수록 세게.</b></>
        : <>Grade 5 plays each scale <b>three ways</b>: all <b>p</b>, all <b>f</b>, and <b>louder going up, softer coming down</b>. D♭ major and B♭ melodic minor are also played <b>staccato</b> (mf). The fingers stay the same; only the sound changes. <b>The thicker the line, the louder.</b></>}</div>
      {spChips([['Db', t(S4_ST.Db.en, S4_ST.Db.ko)], ['Bbmel', t(S4_ST.Bbmel.en, S4_ST.Bbmel.ko)]], k, (x) => reset(() => setK(x)))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 0'}}>{t(S4_ST[k].en, S4_ST[k].ko)} · {shown ? <>{s5WayName(shown)} · {spMM(s5Bpm(shown))}</> : '?'}</div>
      <div style={{maxWidth:420,margin:'2px auto 6px'}}><S5Ribbon m={shown} cur={cur}/></div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8}}>{S5_WAYS.map(x => <button key={x} className={'choice-btn' + (quiz && ans ? (x === quiz ? ' good' : x === ans ? ' bad' : '') : '')} aria-pressed={!quiz && x === m}
        style={{padding:'8px 6px 10px',fontSize:13.5,fontWeight:900,display:'grid',gap:2,justifyItems:'center',boxShadow:!quiz && x === m ? 'inset 0 0 0 2px #26296b' : 'none'}} onClick={() => way(x)}><S5Ribbon m={x} w={130} marks={false}/><span>{s5WayName(x)}</span></button>)}</div>
      {spMsg(ans ? (ok ? t(S5_YES[quiz][0], S5_YES[quiz][1]) : t('Not quite: it was “' + S5_WAY[quiz][0] + '”. The four clicks are always the same: compare with them.', '아니에요: “' + S5_WAY[quiz][1] + '”였어요. 클릭 넷은 언제나 같은 크기: 견주어 봐요.'))
        : quiz ? t('Listen: which way? The four clicks are your yardstick.', '들어 봐요: 어느 것? 클릭 넷이 잣대예요.') : t('Tap a way to hear it. Then ▶ Which one?', '하나를 눌러 들어 봐요. 그다음 ▶ 어느 것일까?'), ans ? (ok ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {quiz && !ans ? <button className="ghost-btn" style={spBtn} onClick={() => hear(k, quiz)}>{t('▶ Play it again', '▶ 다시 듣기')}</button>
          : <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which one?', '▶ 어느 것일까?')}</button>}
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('Back to all four', '네 가지 다시 보기')}</button>}
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const s5PicDyn = () => ({ shapes: [{ k: 'raw', svg: '<polygon points="5,22 75,13 75,31" fill="#26296b"/>' }], vb: [0, 0, 80, 44] });
const s5PicChrom = () => { const m = spMiniKeys(-1, 11, { [-1]: 'cor', 0: 'cor', 4: 'cor', 5: 'cor', 11: 'cor' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const s5PicArp = () => { const m = spMiniKeys(1, 25, { 1: 'pale', 5: 'cor', 8: 'pale', 13: 'pale', 17: 'cor', 20: 'pale', 25: 'pale' }, 7); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };

function s5LbPages(scr = false) {
  const ch = 'scales-5', s4n = bkChapterNo('scales-4');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks5 = [[s4PicFour(), t('I play the Grade 5 scales over four octaves and know where finger 4 goes', '5급 스케일을 네 옥타브로 치고, 4번 자리를 알아요')], [s5PicDyn(), t('I play each scale all p, all f, and louder up and softer down; and staccato', '스케일마다 모두 p, 모두 f, 올라가며 세게 내려오며 여리게; 그리고 스타카토')],
    [spPicMirror(), t('I play contrary motion in the Grade 5 keys, each hand with its own fingers', '5급 조의 반대 방향을 손마다 자기 번호로')], [s5PicChrom(), t('I play the chromatic scale from B and C♯, hands together, all p and all f', 'B와 C♯에서 반음계를 양손으로, 모두 p와 모두 f로')],
    [s5PicArp(), t('I play arpeggios four notes a beat, hands separately and together', '아르페지오를 한 박에 네 음으로, 한 손씩 그리고 양손 함께')]];
  const toc = [[t('One 4 in every octave', '옥타브마다 4번 하나'), 2], [t('One scale, four ways', '한 스케일, 네 가지로'), 3], [t('Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?'), 4], [t('Chromatic from B and C♯', 'B와 C♯에서 반음계'), 5], [t('Arpeggios, four notes a beat', '아르페지오, 한 박에 네 음'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const kbW = scr ? 30 : 40, kbH = scr ? 80 : 104;
  const fourStill = (k, h) => { const c = S4_SC[k], K = s4Oct(k), F = s4Mid(k, h), j4 = s4F4(k, h), lit = {}, nums = {}; K.forEach((x, j) => { lit[x] = j === j4 ? 'cor' : 'pale'; nums[x] = F[j]; });
    return <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{s4Name(k)} · {spHand(h)}</div><SpKb lo={c.r} hi={c.r + 12} W={kbW} H={kbH} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, c.nm[j % 7]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}}/></div>; };
  const chromStill = () => { const s0 = -1, K = Array.from({ length: 13 }, (_, j) => s0 + j), up = {}, dn = {}, lit = {}; K.forEach(x => { up[x] = s4ChR(x); dn[x] = s4ChL(x); if (s4ChR(x) !== s4ChL(x)) lit[x] = 'cor'; });
    return <SpKb lo={s0} hi={s0 + 12} W={kbW} H={kbH} lit={lit} names={Object.fromEntries(K.filter(spIsW).map(x => [x, s4ChLet(x)]))} up={up} dn={dn}/>; };
  const arpStill = (k, h) => { const c = S4_AR[k], K = s4ArKeys(k), lit = {}, nums = {}; K.forEach((x, j) => { lit[x] = c[h][j] === 1 ? 'cor' : 'pale'; nums[x] = c[h][j]; });
    return <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{s4ArName(k)} · {spHand(h)}</div><SpKb lo={c.r} hi={c.r + 24} W={scr ? 19 : 24} H={scr ? 66 : 84} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, c.nm[j % 3]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}}/></div>; };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The Grade 5 technical work as skills (chapter ' + s4n + ' has Grade 4). From the technical work book, Grade 5: scales four octaves, hands separately and together, clear even legato, ♩ = 84 four notes a beat, each prepared three ways: all p, all f, and p < f ascending with f > p descending; staccato scales four octaves, mf, ♩ = 60; contrary motion two octaves, mf, ♩ = 60; chromatic scales four octaves, all p and all f, ♩ = 84; arpeggios four octaves, hands separately and together, mf, ♩ = 52 four notes a beat. The book prints two octaves to show the fingering: play four, in most cases starting an octave lower than written. Another fingering is fine if it is logical and systematic. The keys are in the teacher\'s copy.', '5급 테크니컬 워크를 기술로(' + s4n + '장은 4급). 테크니컬 워크 책 5급: 스케일은 네 옥타브, 한 손씩 그리고 양손 함께, 고르고 또렷한 레가토, ♩ = 84 한 박에 네 음, 스케일마다 세 가지로: 모두 p, 모두 f, 올라갈 때 p < f, 내려올 때 f > p; 스타카토 스케일은 네 옥타브, mf, ♩ = 60; 반대 방향은 두 옥타브, mf, ♩ = 60; 반음계는 네 옥타브, 모두 p와 모두 f, ♩ = 84; 아르페지오는 네 옥타브, 한 손씩 그리고 양손 함께, mf, ♩ = 52 한 박에 네 음. 책은 운지를 보여 주려고 두 옥타브만 적어요: 시험에서는 네 옥타브, 대개 적힌 것보다 한 옥타브 아래에서 시작해요. 논리적이고 일관되면 다른 운지도 괜찮아요. 조 목록은 선생님용에 있어요.'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:46,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={150}><div style={{width:'100%',maxWidth:460,margin:'0 auto'}}><S5Ribbon m="cd" w={460}/></div></LbPic>
      <LbSay size={18}>{t('Grade 5 technique: new keys over four octaves, each scale played soft, loud, and louder going up and softer coming down; staccato; contrary motion in the Grade 4 keys; the chromatic scale from B and C♯; and arpeggios four notes a beat, hands together.', '5급 테크닉: 새 조의 네 옥타브 스케일을 여리게, 세게, 올라가며 세게 내려오며 여리게; 스타카토; 4급 조의 반대 방향; B와 C♯에서 반음계; 한 박에 네 음, 양손 아르페지오.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('find finger 4 in every Grade 5 key', '5급 조마다 4번 자리를 찾을 수 있어요'), t('play one scale all p, all f, and louder up and softer down', '한 스케일을 모두 p, 모두 f, 올라가며 세게 내려오며 여리게 칠 수 있어요'), t('play contrary motion in the Grade 4 keys', '4급 조를 반대 방향으로 칠 수 있어요'), t('play arpeggios four notes a beat, hands together', '아르페지오를 한 박에 네 음, 양손으로 칠 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('One 4 in every octave', '옥타브마다 4번 하나')}
      teacher={<>{spTx(t('Four octaves, hands separately and together, ♩ = 84 four notes a beat: B major; G♯ harmonic and melodic minor; D♭ major; B♭ harmonic and melodic minor. Finger 4 plays one note per octave. RH: A♯ in B major and G♯ minor, B♭ in D♭ major and B♭ minor: the same black key in all four. LH: F♯ in B major, G♭ in D♭ major and B♭ harmonic minor, C♯ in G♯ minor, G going up in B♭ melodic minor (G♭ coming down). In G♯ and B♭ minor the RH starts on 2, so the first octave has no 4; in B major the LH starts on 4 on the bottom B.', '네 옥타브, 한 손씩 그리고 양손 함께, ♩ = 84 한 박에 네 음: B장조; G♯ 화성·가락 단음계; D♭장조; B♭ 화성·가락 단음계. 4번은 옥타브에 한 음. 오른손: B장조와 G♯단조에서 A♯, D♭장조와 B♭단조에서 B♭: 넷 모두 같은 검은건반. 왼손: B장조에서 F♯, D♭장조와 B♭ 화성 단음계에서 G♭, G♯단조에서 C♯, B♭ 가락 단음계는 올라갈 때 G(내려올 때 G♭). G♯단조와 B♭단조는 오른손이 2로 시작해서 첫 옥타브에는 4가 없어요; B장조 왼손은 맨 아래 B를 4로 시작해요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{fourStill('B', 'R')}{fourStill('Db', 'R')}</div></LbPic>} live={<S5FourPad/>}/>
      <LbSay>{LANG === 'ko' ? <>5급 조에서는 넷 모두 <b>오른손 4번이 같은 검은건반</b>에: B장조와 G♯단조에서는 A♯, D♭장조와 B♭단조에서는 같은 건반을 B♭라고 불러요. 왼손: B장조는 F♯, D♭장조는 같은 건반 G♭.</>
        : <>In all four Grade 5 keys <b>the right hand's 4 lands on the same black key</b>: A♯ in B major and G♯ minor, and the same key, called B♭, in D♭ major and B♭ minor. The left hand: F♯ in B major, the same key called G♭ in D♭ major.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>오른손, B장조 그다음 D♭장조: 옥타브마다 같은 검은건반 A♯ = B♭에 4번.</>, <>왼손, B장조: 맨 아래 B는 4번으로 시작, 그다음 F♯마다 4번.</>, <>네 옥타브, 한 박에 네 음: 4번이 올 때마다 속으로 "4!". ♩ = 84까지.</>]
        : [<>Right hand, B major then D♭ major: finger 4 on the same black key, A♯ = B♭, in every octave.</>, <>Left hand, B major: start on 4 (the bottom B), then 4 on every F♯.</>, <>Four octaves, four notes a beat: say "4!" inside each time it comes. Up to ♩ = 84.</>]}/>
      <LbRemember>{t('Right hand: 4 on A♯ = B♭ in every Grade 5 key.', '오른손: 5급 조는 모두 A♯ = B♭에 4번.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('One scale, four ways', '한 스케일, 네 가지로')}
      teacher={<>{spTx(t('Every Grade 5 similar-motion scale in three dynamics: (i) all p, (ii) all f, (iii) p < f ascending, f > p descending; four octaves, hands separately and together, clear even legato, ♩ = 84 four notes a beat. Staccato: D♭ major and B♭ melodic minor, four octaves, hands separately and together, mf, ♩ = 60 four notes a beat, the same fingering. Spread the crescendo over all four octaves, the top note the loudest, and the diminuendo over the way down.', '5급 같은 방향 스케일은 모두 세 가지 셈여림으로: (i) 모두 p, (ii) 모두 f, (iii) 올라갈 때 p < f, 내려올 때 f > p; 네 옥타브, 한 손씩 그리고 양손 함께, 고르고 또렷한 레가토, ♩ = 84 한 박에 네 음. 스타카토: D♭장조와 B♭ 가락 단음계, 네 옥타브, 한 손씩 그리고 양손 함께, mf, ♩ = 60 한 박에 네 음, 같은 운지. 크레셴도는 네 옥타브 전체에 나눠서 맨 위 음이 가장 세게, 디미누엔도는 내려오는 길 전체에.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={230}><div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'10px 26px',width:'100%',maxWidth:700,margin:'0 auto'}}>{S5_WAYS.map(x => <div key={x}><div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.ink,marginBottom:2}}>{s5WayName(x)}</div><S5Ribbon m={x} w={330}/></div>)}</div></LbPic>} live={<S5DynPad/>}/>
      <LbSay>{LANG === 'ko' ? <>한 스케일, <b>네 가지로</b>: 모두 <b>p</b>, 모두 <b>f</b>, <b>올라가며 세게, 내려오며 여리게</b>(맨 위 음이 가장 세게), 그리고 <b>스타카토</b>. 손가락은 바뀌지 않아요: 소리만.</>
        : <>One scale, <b>four ways</b>: all <b>p</b>, all <b>f</b>, <b>louder going up and softer coming down</b> (the top note the loudest), and <b>staccato</b>. The fingers never change: only the sound.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>D♭장조 한 옥타브, 모두 p: 여리게, 그래도 음마다 소리 나게.</>, <>똑같이, 모두 f: 꽉 차게, 그래도 고르게.</>, <>네 옥타브: 맨 아래 p에서 맨 위 f까지, 다시 p로. 그다음 스타카토, ♩ = 60.</>]
        : [<>D♭ major, one octave, all p: soft, but every note sounds.</>, <>The same, all f: full, and still even.</>, <>Four octaves: p at the bottom, growing to f at the top, back to p. Then staccato at ♩ = 60.</>]}/>
      <LbRemember>{t('The same fingers; only the sound changes.', '손가락은 그대로, 소리만 달라져요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?')}
      teacher={<>{spTx(t('Contrary motion, two octaves, hands together from one note, mf, clear even legato, ♩ = 60 four notes a beat: E major, C♯ harmonic minor, A♭ major, F harmonic minor (the Grade 4 similar-motion keys). Each hand keeps its own scale fingering: only E major mirrors all the way. C♯ minor and A♭ major: RH 2 3 1 2 3 1 2 3, LH 2 1 2 3 4 1 2 3. F minor: RH 1 2 3 4 1 2 3 1, LH 1 2 3 1 2 3 4 1.', '반대 방향, 두 옥타브, 두 손이 한 음에서, mf, 고르고 또렷한 레가토, ♩ = 60 한 박에 네 음: E장조, C♯ 화성 단음계, A♭장조, F 화성 단음계(4급의 같은 방향 조). 손마다 자기 스케일 번호: 끝까지 같은 번호는 E장조뿐. C♯단조와 A♭장조: 오른손 2 3 1 2 3 1 2 3, 왼손 2 1 2 3 4 1 2 3. F단조: 오른손 1 2 3 4 1 2 3 1, 왼손 1 2 3 1 2 3 4 1.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={160}><div style={{display:'grid',gridTemplateColumns:'1fr',gap:16,width:'100%',maxWidth:scr ? 440 : 560,margin:'0 auto'}}><div><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('E5')} · {t('mirror twins', '거울 쌍둥이')}</div><ScfCmKb k="E5" W={scr ? 20 : 30} H={scr ? 66 : 84}/></div><div><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('Ab5')} · {t('not mirror twins', '거울 쌍둥이 아님')}</div><ScfCmKb k="Ab5" W={scr ? 20 : 30} H={scr ? 66 : 84} mark={scfFirstDiff('Ab5')}/></div></div></LbPic>} live={<S5MirrorPad/>}/>
      <LbSay>{LANG === 'ko' ? <>4급의 조를 이제 반대 방향으로. <b>거울 쌍둥이는 E장조뿐</b>. <b>C♯단조, A♭장조, F단조</b>는 번호가 갈라져요: 손마다 자기 스케일 번호를 지켜요.</>
        : <>The Grade 4 keys, now in contrary motion. <b>Only E major is mirror twins</b>. In <b>C♯ minor, A♭ major and F minor</b> the numbers part: each hand keeps its own scale fingering.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>두 손을 A♭에. 오른손 2 3 1, 왼손 2 1 2.</>, <>번호가 갈라지는 곳에서 멈춰서 확인해요.</>, <>두 옥타브, mf, 한 박에 네 음. ♩ = 60까지.</>]
        : [<>Both hands on A♭. Right hand 2 3 1, left hand 2 1 2.</>, <>Stop where the numbers part, and check.</>, <>Two octaves, mf, four notes a beat. Up to ♩ = 60.</>]}/>
      <LbRemember>{t('Each hand keeps its own numbers.', '손마다 자기 번호를 지켜요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Chromatic from B and C♯', 'B와 C♯에서 반음계')}
      teacher={<>{spTx(t('Chromatic scales from B and from C♯/D♭, four octaves, hands separately and together, all p and all f, clear even legato, ♩ = 84 four notes a beat. The book\'s fingering keeps the rule: 3 on every black key, 1 on white keys, 2 on the right hand\'s F and C and the left hand\'s E and B. From B the right hand starts on 1 and the left hand on 2.', 'B와 C♯/D♭에서 반음계, 네 옥타브, 한 손씩 그리고 양손 함께, 모두 p와 모두 f, 고르고 또렷한 레가토, ♩ = 84 한 박에 네 음. 책의 운지는 규칙 그대로: 검은건반 3, 흰건반 1, 오른손 F와 C, 왼손 E와 B는 2. B에서 시작하면 오른손은 1, 왼손은 2로 시작해요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:600,margin:'0 auto'}}>{chromStill()}</div></LbPic>} live={<S5ChromPad/>}/>
      <LbSay>{LANG === 'ko' ? <>양손 함께면 <b>3번은 언제나 함께</b>. B에서 시작하면 두 손이 처음부터 달라요: 오른손은 1, 왼손은 2. 그다음엔 <b>E–F와 B–C</b> 둘레에서만.</>
        : <>Hands together, <b>the 3s land together</b>. From B the hands differ straight away: the right hand starts on 1, the left on 2. After that, only around <b>E–F and B–C</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>B에서 한 손씩, 한 옥타브: 오른손 1 2 3, 왼손 2 1 3.</>, <>양손 함께, 모두 p. 그다음 모두 f.</>, <>네 옥타브, 한 박에 네 음. ♩ = 84까지.</>]
        : [<>From B, each hand, one octave: right hand 1 2 3, left hand 2 1 3.</>, <>Hands together, all p. Then all f.</>, <>Four octaves, four notes a beat. Up to ♩ = 84.</>]}/>
      <LbRemember>{t('The 3s together; the 2s apart.', '3번은 함께, 2번은 따로.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Arpeggios, four notes a beat', '아르페지오, 한 박에 네 음')}
      teacher={<>{spTx(t('Arpeggios B major and minor, D♭ major and minor, four octaves, hands separately and together, mf, clear even legato, ♩ = 52 four notes a beat. The book\'s fingerings: B major and minor RH 1 2 3 1 2 3 5; LH 5 3 2 1 3 2 1 (major), 5 4 2 1 4 2 1 (minor). D♭ major and minor RH 2 1 2 4 1 2 4, LH 2 1 4 2 1 4 2: the thumb on F (F♭ in the minor), the only white key. Hands together, both thumbs come at the same moment.', '아르페지오 B장조와 단조, D♭장조와 단조, 네 옥타브, 한 손씩 그리고 양손 함께, mf, 고르고 또렷한 레가토, ♩ = 52 한 박에 네 음. 책의 운지: B장조·단조 오른손 1 2 3 1 2 3 5; 왼손 5 3 2 1 3 2 1(장조), 5 4 2 1 4 2 1(단조). D♭장조·단조 오른손 2 1 2 4 1 2 4, 왼손 2 1 4 2 1 4 2: 엄지는 F(단조는 F♭), 하나뿐인 흰건반. 양손 함께면 두 엄지가 같은 순간에 와요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{arpStill('B', 'L')}{arpStill('Db', 'R')}</div></LbPic>} live={<S5ArpPad/>}/>
      <LbSay>{LANG === 'ko' ? <>5급 아르페지오는 <b>한 박에 네 음</b>, 그리고 <b>양손 함께</b>. 엄지는 흰건반: B장조와 단조는 B, D♭에서는 하나뿐인 흰건반 F. D♭단조의 F♭도 흰건반이에요(E와 같은 건반).</>
        : <>Grade 5 arpeggios: <b>four notes a beat</b>, and <b>hands together</b>. The thumb takes a white key: B in B major and minor; in D♭ the only white key, F. In D♭ minor F♭ is a white key too: the same key as E.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>B장조 오른손 두 옥타브: 1 2 3 1 2 3 5. 그다음 왼손: 5 3 2 1 3 2 1.</>, <>D♭장조: 엄지 자리 F를 먼저 찾고, 2 1 2 4.</>, <>양손 함께, 한 박에 네 음. ♩ = 52까지.</>]
        : [<>B major, right hand, two octaves: 1 2 3 1 2 3 5. Then the left hand: 5 3 2 1 3 2 1.</>, <>D♭ major: find the thumb's F first, then 2 1 2 4.</>, <>Hands together, four notes a beat. Up to ♩ = 52.</>]}/>
      <LbRemember>{t('Four to a beat; the thumb on the white key.', '한 박에 넷, 엄지는 흰건반에.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one played to you from memory, in the Grade 5 keys (the teacher\'s copy lists them), four octaves where the book asks for four. Listen for the top of the crescendo, even groups of four in p and in f, the same evenness staccato, and smooth thumbs hands together.', '하나씩 외워서, 5급 조로(선생님용에 목록), 책이 네 옥타브를 요구하는 것은 네 옥타브로 들려줘요. 크레셴도의 꼭대기, p와 f에서 고른 네 음 묶음, 스타카토도 똑같이 고르게, 양손 함께일 때 매끄러운 엄지를 들어 주세요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_s5_five"/>}/>
    </LbPage>,
  ];
}
function Scales5LessonBook() { return <>{s5LbPages(false)}</>; }
function S5Learn({ onStart }) {
  const pages = s5LbPages(true), opener = pages[0];
  return (
    <Lesson id="scales-5" title={bkChapterName('scales-5')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scales-5"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill: the Grade 4 questions with the Grade 5 keys, and one new: which way is it played? ──
const S5_LEVELS = [
  { n: 1, label: 'Grade 5 keys: where does finger 4 go?', kind: 'four', time: 15 },
  { n: 2, label: 'p, f, louder up, or staccato?', kind: 'dyn', time: 25 },
  { n: 3, label: 'Grade 5 contrary motion: mirror twins?', kind: 'mirror', time: 15 },
  { n: 4, label: 'Chromatic from B and C♯: the same finger?', kind: 'chrom', time: 12 },
  { n: 5, label: 'Grade 5 arpeggios: which finger?', kind: 'arp', time: 15 },
];
Object.assign(LEVEL_KO, { 'Grade 5 keys: where does finger 4 go?': '5급 조: 4번은 어디에?', 'p, f, louder up, or staccato?': 'p, f, 올라가며 세게, 스타카토?', 'Grade 5 contrary motion: mirror twins?': '5급 반대 방향: 거울 쌍둥이?', 'Chromatic from B and C♯: the same finger?': 'B와 C♯에서 반음계: 같은 손가락?', 'Grade 5 arpeggios: which finger?': '5급 아르페지오: 몇 번 손가락?' });
const s5CmPick = () => (Math.random() < 0.4 ? 'E5' : pick(['Csmh', 'Ab5', 'Fmh']));   // one twin of four: asked a little more often
function genS5Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'four') { let k, h, g = 0; do { k = pick(S5_KEYS); h = Math.random() < 0.5 ? 'R' : 'L'; } while (prev && prev.key === k + h && g++ < 10);
    return { kind, k, h, answer: s4F4Note(k, h), choices: S4_SC[k].nm.slice(), key: k + h, uid }; }
  if (kind === 'dyn') { let k, m, g = 0; do { k = Math.random() < 0.5 ? 'Db' : 'Bbmel'; m = pick(S5_WAYS); } while (prev && prev.key === 'w' + m && g++ < 10); return { kind, k, m, answer: m, choices: S5_WAYS.slice(), key: 'w' + m, uid }; }
  if (kind === 'mirror') { let k, g = 0; do { k = s5CmPick(); } while (prev && prev.key === 'c' + k && g++ < 10); return { kind, k, answer: scfMirror(k) ? 'yes' : 'no', choices: ['yes', 'no'], key: 'c' + k, uid }; }
  if (kind === 'chrom') { let st, j, g = 0; do { st = Math.floor(Math.random() * 2); j = Math.floor(Math.random() * 12); } while (prev && prev.key === 'h' + st + j && g++ < 10); const s0 = S5_CH[st][1], i = s0 + j;
    return { kind, st, j, i, s0, answer: s4ChAns(i), choices: ['3', '1', 'diff'], key: 'h' + st + j, uid }; }
  let k, h, j, g = 0; do { k = pick(S5_AR_KEYS); h = Math.random() < 0.5 ? 'R' : 'L'; j = Math.floor(Math.random() * 7); } while (prev && prev.key === 'a' + k + h + j && g++ < 10);
  return { kind: 'arp', k, h, j, answer: S4_AR[k][h][j], choices: [1, 2, 3, 4, 5], key: 'a' + k + h + j, uid };
}
const s5AnswerLabel = (q) => (q.kind === 'dyn' ? s5WayName(q.answer) : s4AnswerLabel(q));
function S5DynQuestion({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const play = () => { stopClicks(); s5PlayWay(q.k, q.m); };
  useEffect(() => { const id = setTimeout(play, 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{t('Listen to ' + S4_ST[q.k].en + ': which way is it played?', S4_ST[q.k].ko + '를 들어 봐요: 어떻게 치고 있나요?')}</p>
    <div style={{textAlign:'center'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>
    {!pixel && <div style={{maxWidth:340,margin:'6px auto 0'}}><S5Ribbon m={done ? q.m : null}/></div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:10}}>{S5_WAYS.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:14,fontWeight:900}} onClick={() => pickIt(c)}>{s5WayName(c)}</button>)}</div>
  </div>);
}
function S5Question(props) { return props.q.kind === 'dyn' ? <S5DynQuestion {...props}/> : <S4Question {...props}/>; }
Object.assign(SCALES_5_DRILL, { levels: S5_LEVELS, generate: genS5Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: s5AnswerLabel, Question: S5Question, Learn: S5Learn });
// the teacher's copy: the keys, speeds and fingerings, and what to listen for
function S5Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scales-5" teacher>{content}</WbPage>);
  const mid = (k) => S4_SC[k].en + ': RH ' + s4Mid(k, 'R').join(' ') + ' · LH ' + s4Mid(k, 'L').join(' ') + ' (4: RH ' + s4F4Note(k, 'R') + ', LH ' + s4F4Note(k, 'L') + ')';
  const arp = (k) => S4_AR[k].en + ': RH ' + S4_AR[k].R.join(' ') + ' · LH ' + S4_AR[k].L.join(' ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scales-5')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>{spTx('The keys, speeds and fingerings are the technical work book\'s (Grade 5 pp19–24). Scales and arpeggios four octaves (the book prints two: in most cases start an octave lower than written), from memory. Another fingering is fine if it is logical and systematic.')}</div>
    <TcBlock page={2} title="One 4 in every octave" answers={<>{tcAns(spTx('SIMILAR MOTION, FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, ♩ = 84 FOUR NOTES A BEAT · A MIDDLE OCTAVE'), [mid('B'), mid('Gsm'), mid('Gsmel') + '; coming down as the natural minor', mid('Db'), mid('Bbm'), mid('Bbmel') + '; coming down as the natural minor, LH 4 on G♭'])}</>}
      watch="Losing the place in the third and fourth octaves. In all four keys the RH 4 is the same black key (A♯ = B♭). In G♯ and B♭ minor the RH starts on 2, so its first 4 comes in the second octave; in B major the LH starts on 4."
      say="“Right hand: 4 on A♯ = B♭.”"/>
    <TcBlock page={3} title="One scale, four ways" answers={<>{tcAns(spTx('EVERY SCALE ABOVE, ♩ = 84'), ['all p', 'all f', 'p < f ascending, f > p descending'])}{tcAns(spTx('STACCATO, FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, mf, ♩ = 60 FOUR NOTES A BEAT'), ['D♭ major', 'B♭ melodic minor'], null)}</>}
      watch="A crescendo that peaks in the second octave, or a diminuendo that drops at once: spread each over four octaves, the top note the loudest. All p that loses notes; all f that turns uneven. Staccato that slows down."
      say="“The same fingers; only the sound changes.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Contrary motion: mirror twins?" answers={<>{tcAns('MIRROR TWINS?', S5_CM_KEYS.map(k => SCF_CM[k].en + ': ' + (scfMirror(k) ? 'Y' : 'N')))}{tcAns(spTx('TWO OCTAVES FROM ONE NOTE, mf, ♩ = 60 FOUR NOTES A BEAT'), ['E major (mirror: 1 2 3 1 2 3 4 1)', 'C♯ harmonic minor (not: RH 2 3 1 2 3 1 2 3, LH 2 1 2 3 4 1 2 3)', 'A♭ major (not: RH 2 3 1 2 3 1 2 3, LH 2 1 2 3 4 1 2 3)', 'F harmonic minor (not: RH 1 2 3 4 1 2 3 1, LH 1 2 3 1 2 3 4 1)'], null)}</>}
      watch="The LH copying the RH in C♯ minor, A♭ major or F minor. Each hand keeps its own fingering."
      say="“Each hand keeps its own numbers.”"/>
    <TcBlock page={5} title="Chromatic from B and C♯" answers={<>{tcAns('FROM B', ['RH ' + Array.from({ length: 13 }, (_, j) => s4ChR(-1 + j)).join(' '), 'LH ' + Array.from({ length: 13 }, (_, j) => s4ChL(-1 + j)).join(' ')], null)}{tcAns(spTx('FROM B AND FROM C♯/D♭, FOUR OCTAVES, ALL p AND ALL f, ♩ = 84'), ['RH 3 on black, 1 on white, 2 on F and C', 'LH 3 on black, 1 on white, 2 on E and B (from B the LH starts on 2)', 'Hands together the fingers differ only on E, F, B and C'], null)}</>}
      watch="All p that thins out until notes go missing; the hands drifting apart at E–F and B–C. The 3s land together: listen for one sound."
      say="“The 3s together; the 2s apart.”"/>
    <TcBlock page={6} title="Arpeggios, four notes a beat" answers={<>{tcAns(spTx('FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, mf, ♩ = 52 FOUR NOTES A BEAT'), [arp('B'), arp('Bm'), arp('Db'), arp('Dbm')])}</>}
      watch="A bump each time the thumb passes, now at four notes a beat. Hands together, both thumbs come at the same moment: on B in B major and minor, on F (F♭) in D♭."
      say="“Four to a beat; the thumb on the white key.”"/>
    <TcBlock page={7} title="The check-up" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one at the piano, from memory, in the Grade 5 keys at the book's speeds: every scale all p, all f and with the hairpins; the staccato pair; contrary motion; chromatic in p and in f; arpeggios hands separately and together. Listen for the top of the crescendo, even groups of four, and smooth thumbs.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['scales-5'] = S5Teacher;
'''
rep("""TEACHER_COPIES['scales-4'] = S4Teacher;""", """TEACHER_COPIES['scales-4'] = S4Teacher;""" + CH)

HOME = r'''
// ══ Build BA: Scales and Arpeggios, Grade 5 on the Home (Technique, after Grade 4) ══
LBH_FN['scales-5'] = (s) => s5LbPages(s);
const s5HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('scales-5', i, { make }));
const s5DynQ = (n, prev) => { let k, m, g = 0; do { k = Math.random() < 0.5 ? 'Db' : 'Bbmel'; m = pick(S5_WAYS); } while (prev && prev.key === m && g++ < 10);
  return { kind: 'choice', cols: 2, key: m, prompt: ['Listen: which way is it played?', '들어 봐요: 어떻게 치고 있나요?'], opts: S5_WAYS.map(x => ({ id: x, label: () => s5WayName(x) })), ans: m, ok: (v) => v === m,
    play: () => s5PlayWay(k, m), fig: (c) => ({ mid: <div style={{maxWidth:340,margin:'0 auto'}}><S5Ribbon m={c.res ? m : null}/></div> }), yes: S5_YES[m],
    no: ['It was “' + S5_WAY[m][0] + '”. The four clicks are always the same: compare with them.', '“' + S5_WAY[m][1] + '”였어요. 클릭 넷은 언제나 같은 크기: 견주어 봐요.'] }; };
const s5MirrorQ = (n, prev) => { let k, g = 0; do { k = s5CmPick(); } while (prev && prev.key === k && g++ < 10); const a = scfMirror(k) ? 'yes' : 'no';
  return { kind: 'choice', cols: 2, key: k, prompt: ['Contrary motion, ' + SCF_CM[k].en + ': mirror twins?', '반대 방향, ' + SCF_CM[k].ko + ': 거울 쌍둥이일까?'], opts: [{ id: 'yes', label: () => t('Mirror twins', '거울 쌍둥이') }, { id: 'no', label: () => t('Not mirror twins', '거울 쌍둥이 아님') }], ans: a, ok: (v) => v === a,
    fig: (c) => ({ mid: <ScfCmKb k={k} mark={c.res && a === 'no' ? scfFirstDiff(k) : -1}/> }), yes: a === 'yes' ? ['Yes: the same numbers all the way.', '맞아요: 끝까지 같은 번호.'] : ['Yes: each hand keeps its own numbers.', '맞아요: 손마다 자기 번호.'], no: a === 'yes' ? ['Look again: the numbers match all the way.', '다시 봐요: 끝까지 같은 번호예요.'] : ['Look again: the coral keys have different numbers.', '다시 봐요: 빨간 건반의 번호가 달라요.'] }; };
s5HomeAdd('s5-four', 1, 'One 4 in every octave: Grade 5 keys', '옥타브마다 4번 하나: 5급 조', 'In every Grade 5 key the right hand\'s 4 is the same black key.', '5급 조는 모두 오른손 4번이 같은 검은건반.', lwTapQ(S5FourPad, (n) => ({ fixed: { k: S5_KEYS[(n * 5) % S5_KEYS.length], h: n % 2 ? 'L' : 'R' } }), ['Tap the key finger 4 plays.', '4번이 치는 건반을 눌러요.'], ['Finger 4 found ✓', '4번 자리 찾았어요 ✓']));
s5HomeAdd('s5-dyn', 2, 'One scale, four ways', '한 스케일, 네 가지로', 'All p, all f, louder up and softer down, or staccato.', '모두 p, 모두 f, 올라가며 세게 내려오며 여리게, 또는 스타카토.', s5DynQ);
s5HomeAdd('s5-mirror', 3, 'Contrary motion: the Grade 5 keys', '반대 방향: 5급 조', 'One mirror twin, three not.', '거울 쌍둥이 하나, 아닌 것 셋.', s5MirrorQ);
s5HomeAdd('s5-chrom', 4, 'Chromatic from B and C♯', 'B와 C♯에서 반음계', 'The 3s together; the hands differ only at E–F and B–C.', '3번은 함께, E–F와 B–C에서만 달라요.', lwTapQ(S5ChromPad, (n) => ({ fixed: n % 2 }), ['Tap every key where the hands use different fingers.', '두 손의 번호가 다른 건반을 모두 눌러요.'], ['Found them ✓', '찾았어요 ✓']));
s5HomeAdd('s5-arp', 5, 'Arpeggios, four notes a beat', '아르페지오, 한 박에 네 음', 'B and D♭, major and minor: the thumb on the white key.', 'B와 D♭, 장조와 단조: 엄지는 흰건반에.', lwTapQ(S5ArpPad, (n) => ({ fixed: { k: S5_AR_KEYS[Math.floor(n / 2) % S5_AR_KEYS.length], h: n % 2 ? 'L' : 'R' } }), ['Choose the finger for each coral key.', '빨간 건반마다 손가락을 골라요.'], ['All seven ✓', '일곱 개 모두 ✓']));
'''
lines = s.split('\n'); hits = [i for i, x in enumerate(lines) if x.startswith("s4HomeAdd('s4-arp', 5,")]
assert len(hits) == 1
lines.insert(hits[0] + 1, HOME.rstrip('\n')); s = '\n'.join(lines)   # after the Grade 4 lessons
rep("""    { id: 'kpl-4', en: 'Scales and arpeggios, Grade 4', ko: '스케일과 아르페지오, Grade 4', lessons: ['s4-four', 's4-touch', 's4-mirror', 's4-chrom', 's4-arp'], check: 'scales-4' },   // Build AS""",
    """    { id: 'kpl-4', en: 'Scales and arpeggios, Grade 4', ko: '스케일과 아르페지오, Grade 4', lessons: ['s4-four', 's4-touch', 's4-mirror', 's4-chrom', 's4-arp'], check: 'scales-4' },   // Build AS
    { id: 'kpl-5', en: 'Scales and arpeggios, Grade 5', ko: '스케일과 아르페지오, Grade 5', lessons: ['s5-four', 's5-dyn', 's5-mirror', 's5-chrom', 's5-arp'], check: 'scales-5' },   // Build BA""")
rep("""  set('4', 's4-four s4-touch s4-mirror s4-chrom s4-arp');   // Build AS: Scales and Arpeggios, Grade 4""",
    """  set('4', 's4-four s4-touch s4-mirror s4-chrom s4-arp');   // Build AS: Scales and Arpeggios, Grade 4
  set('5', 's5-four s5-dyn s5-mirror s5-chrom s5-arp');   // Build BA: Scales and Arpeggios, Grade 5""")
rep("""const LESSON_BOOKS = { 'listen-5': Listen5LessonBook,""", """const LESSON_BOOKS = { 'scales-5': Scales5LessonBook, 'listen-5': Listen5LessonBook,""")
rep("""const LB_PAGE_FNS = { 'listen-5': l5LbPages,""", """const LB_PAGE_FNS = { 'scales-5': s5LbPages, 'listen-5': l5LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"scales-5": "<path d=\\"M4 31 H12 V25 H20 V19 H28 V13 H36 V7 H44\\"/><path d=\\"M30 36 L8 40.5 L30 45\\" fill=\\"none\\" stroke=\\"#e4572e\\" stroke-width=\\"2.6\\"/>", """)
# a metronome mark typed as text inside JSX (the font's crotchet leaves a wide gap after it): draw it with spMM, as the pads do
import re
s, nmm = re.subn(r'(?<=[\s,(])♩ = (\d+)(?=(?:까지)?\.?</>)', r'{spMM(\1)}', s)
print('metronome marks drawn:', nmm)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
