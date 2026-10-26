import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AK (board call 14, the second Grades 2-3 room): Scales Further. Technique follows the practical syllabus and is
# "comparable, not a copy of the exam" (her 10:19): the room teaches the skill each scale group is for; the key lists and the
# speeds live in the teacher's copy. Every fingering below was read off the technical work book (Level 1, Grade 2 pp36-39,
# Grade 3 pp47-50; transcribed 26 Oct, pages 37, 47 and 48 checked by eye): two octaves, mf, clear even legato, two notes a
# beat (Grade 2 crotchet 84, Grade 3 92; contrary motion 66 and 80); melodic minor hands separately at Grade 2 (G), hands
# together too at Grade 3 (C); the chromatic scale from D (Grade 2, hands separately), from A and from D#/Eb (Grade 3, hands
# separately and together). Her rule for a scale that starts on a black key (2026-09-19): the right hand starts on 2 and the
# thumb takes the first white key.

rep("""const LISTEN_23_DRILL = { id: 'listen-23', label: 'Hear and Sing Further', noPrint: true };   // Build AJ: Grades 2-3 aural""",
    """const LISTEN_23_DRILL = { id: 'listen-23', label: 'Hear and Sing Further', noPrint: true };   // Build AJ: Grades 2-3 aural
const SCALES_23_DRILL = { id: 'scales-23', label: 'Scales Further' };   // Build AK: Grades 2-3 scales""")
rep("""  { id: 'listen-23', label: 'Hear and Sing Further', concept: LISTEN_23_DRILL, track: 'start' },   // Build AJ""",
    """  { id: 'listen-23', label: 'Hear and Sing Further', concept: LISTEN_23_DRILL, track: 'start' },   // Build AJ
  { id: 'scales-23', label: 'Scales Further', concept: SCALES_23_DRILL, track: 'start' },   // Build AK""")
rep("""'listen-23': '더 듣고 부르기'""", """'listen-23': '더 듣고 부르기', 'scales-23': '스케일 한 걸음 더'""")
rep("""'listen-23': ['listen-write']""", """'listen-23': ['listen-write'], 'scales-23': ['scale-play', 'minor-scales']""")
rep("""'listen-23': ['Hear & sing', '듣고 부르기']""", """'listen-23': ['Hear & sing', '듣고 부르기'], 'scales-23': ['Scales further', '스케일 더']""")
rep("""  'scale-play': 'playing scales technique""", """  'scales-23': 'scales grade 2 grade 3 black key start finger 2 thumb white key hands together thumbs meet melodic minor contrary motion mirror twins chromatic any note two octaves two notes a beat technique',
  'scale-play': 'playing scales technique""")
rep("""'scale-play': 'k-play', 'key-signatures': 'p-scales',""", """'scale-play': 'k-play', 'scales-23': 'k-play', 'key-signatures': 'p-scales',""")
rep("""  { ids: ['melody', 'listen-23', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, your ears a step further, and more scales.'], ko: ['Grade 2–3', '선율의 모양, 귀를 한 걸음 더, 그리고 더 많은 음계.'] },""",
    """  { ids: ['melody', 'listen-23', 'scales-23', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, your ears a step further, and scales a step further.'], ko: ['Grade 2–3', '선율의 모양, 귀를 한 걸음 더, 그리고 스케일 한 걸음 더.'] },   // Build AK: Scales Further""")
rep("""    { id: 'kpl-scales', en: 'Playing scales', ko: '스케일 치기', lessons: ['sp-turn', 'sp-beat', 'sp-minor', 'sp-mirror', 'sp-two'], check: 'scale-play' },""",
    """    { id: 'kpl-scales', en: 'Playing scales', ko: '스케일 치기', lessons: ['sp-turn', 'sp-beat', 'sp-minor', 'sp-mirror', 'sp-two'], check: 'scale-play' },
    { id: 'kpl-23', en: 'Scales further', ko: '스케일 한 걸음 더', lessons: ['scf-thumb', 'scf-meet', 'scf-mel', 'scf-mirror', 'scf-chrom'], check: 'scales-23' },   // Build AK""")
rep("""  set('23', 'l2-dyad l2-any l2-deg l2-clap l2-sing');""", """  set('23', 'l2-dyad l2-any l2-deg l2-clap l2-sing');
  set('23', 'scf-thumb scf-meet scf-mel scf-mirror scf-chrom');   // Build AK: Scales Further""")
# the book prints the left hand's top note of B-flat and E-flat major (two octaves) with finger 2 (Grade 2 p37, Grade 3 p48)
rep("""  Bb: { rootPc: 10, octaves: {
    1: { offsets: majorOffsets(1), RH: [2,1,2,3,1,2,3,4], LH: [3,2,1,4,3,2,1,3], label: '1 octave' },
    2: { offsets: majorOffsets(2), RH: [2,1,2,3,1,2,3,4,1,2,3,1,2,3,4], LH: [3,2,1,4,3,2,1,3,2,1,4,3,2,1,3], label: '2 octaves' } } },
  Eb: { rootPc: 3, octaves: {
    1: { offsets: majorOffsets(1), RH: [2,1,2,3,4,1,2,3], LH: [3,2,1,4,3,2,1,3], label: '1 octave' },
    2: { offsets: majorOffsets(2), RH: [2,1,2,3,4,1,2,3,1,2,3,4,1,2,3], LH: [3,2,1,4,3,2,1,3,2,1,4,3,2,1,3], label: '2 octaves' } } },""",
    """  Bb: { rootPc: 10, octaves: {
    1: { offsets: majorOffsets(1), RH: [2,1,2,3,1,2,3,4], LH: [3,2,1,4,3,2,1,3], label: '1 octave' },
    2: { offsets: majorOffsets(2), RH: [2,1,2,3,1,2,3,4,1,2,3,1,2,3,4], LH: [3,2,1,4,3,2,1,3,2,1,4,3,2,1,2], label: '2 octaves' } } },   // Build AK: LH top note 2, as the book prints it (Grade 2 p37)
  Eb: { rootPc: 3, octaves: {
    1: { offsets: majorOffsets(1), RH: [2,1,2,3,4,1,2,3], LH: [3,2,1,4,3,2,1,3], label: '1 octave' },
    2: { offsets: majorOffsets(2), RH: [2,1,2,3,4,1,2,3,1,2,3,4,1,2,3], LH: [3,2,1,4,3,2,1,3,2,1,4,3,2,1,2], label: '2 octaves' } } },   // Build AK: LH top note 2 (Grade 3 p48)""")

CH = r'''
// ─── Chapter: Scales Further (Build AK, 2026-10-26; board call 14, the second Grades 2-3 room) ───
// The skills the Grade 2 and 3 scales add to Playing Scales: a scale that starts on a black key (her rule: the right hand starts on
// 2, the thumb takes the first white key; the thumb plays only white keys here); two octaves hands together where the thumbs
// meet on the keynote, in two places, or never; the melodic minor (up with the 6th and 7th raised, down as the natural minor);
// contrary motion from one note, where each hand keeps its own fingering (mirror twins in some keys, not in others); the chromatic
// scale from any note (3 on every black key, 1 on white keys, 2 where two white keys sit together: the right hand's F and C, the
// left hand's E and B). The keys are the book's; the fingerings are the book's, read 26 Oct.
const SCF_R = [1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 5], SCF_L = [5, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1];
const SCF = {   // r: the keynote the strip starts on (semitones from middle C); R and L: two octaves going up
  D: { g: 2, en: 'D major', ko: 'D장조', st: SP_MAJ, r: 2, nm: ['D', 'E', 'F♯', 'G', 'A', 'B', 'C♯'], R: SCF_R, L: SCF_L },
  Bm: { g: 2, en: 'B minor', ko: 'B단조', st: SP_NAT, r: -1, nm: ['B', 'C♯', 'D', 'E', 'F♯', 'G', 'A'], R: SCF_R, L: [4, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1] },
  Bb: { g: 2, en: 'B♭ major', ko: 'B♭장조', st: SP_MAJ, r: -2, nm: ['B♭', 'C', 'D', 'E♭', 'F', 'G', 'A'], R: [2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4], L: [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 2] },
  Gm: { g: 2, en: 'G minor', ko: 'G단조', st: SP_NAT, r: -5, nm: ['G', 'A', 'B♭', 'C', 'D', 'E♭', 'F'], R: SCF_R, L: SCF_L },
  A: { g: 3, en: 'A major', ko: 'A장조', st: SP_MAJ, r: -3, nm: ['A', 'B', 'C♯', 'D', 'E', 'F♯', 'G♯'], R: SCF_R, L: SCF_L },
  Fsm: { g: 3, en: 'F♯ minor', ko: 'F♯단조', st: SP_NAT, r: -6, nm: ['F♯', 'G♯', 'A', 'B', 'C♯', 'D', 'E'], R: [2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3], L: [4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 2] },
  Eb: { g: 3, en: 'E♭ major', ko: 'E♭장조', st: SP_MAJ, r: 3, nm: ['E♭', 'F', 'G', 'A♭', 'B♭', 'C', 'D'], R: [2, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3], L: [3, 2, 1, 4, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 2] },
  Cm: { g: 3, en: 'C minor', ko: 'C단조', st: SP_NAT, r: 0, nm: ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B♭'], R: SCF_R, L: SCF_L },
};
const SCF_KEYS = ['D', 'Bm', 'Bb', 'Gm', 'A', 'Fsm', 'Eb', 'Cm'];
const scfName = (k) => t(SCF[k].en, SCF[k].ko);
const scfKeys = (k, n = 2) => { const c = SCF[k], out = []; for (let o = 0; o < n; o++) c.st.forEach(x => out.push(c.r + 12 * o + x)); out.push(c.r + 12 * n); return out; };
const scfNames = (k, n = 2) => { const c = SCF[k], out = []; for (let o = 0; o < n; o++) out.push(...c.nm); out.push(c.nm[0]); return out; };
const scfThumbPcs = (k, h) => { const K = scfKeys(k, 1), out = []; K.forEach((x, j) => { if (SCF[k][h][j] === 1 && !out.includes(spPc(x))) out.push(spPc(x)); }); return out; };
const scfBlackStart = (k) => !spIsW(SCF[k].r);
const scfMeet = (k) => SCF[k].R.map((f, j) => (f === 1 && SCF[k].L[j] === 1 ? j : -1)).filter(j => j >= 0);
const scfMeetKind = (k) => { const m = scfMeet(k); if (!m.length) return 'never'; return new Set(m.map(j => j % 7)).size === 1 ? 'tonic' : 'tonic4'; };
const SCF_MEET_LAB = { tonic: ['Only on the middle keynote', '가운데 으뜸음에서만'], tonic4: ['On the keynote and the 4th', '으뜸음과 4도에서'], never: ['Never: each hand turns on its own', '한 번도 안 만나요: 손마다 따로 넘어가요'] };
// contrary motion from one note: one octave each way, the fingers as the book prints them (the first octave of two)
const SCF_CM_STD = [1, 2, 3, 1, 2, 3, 4, 1];
const SCF_CM = {
  G: { g: 2, en: 'G major', ko: 'G장조', st: SP_MAJ, s: 7, nm: ['G', 'A', 'B', 'C', 'D', 'E', 'F♯'], R: SCF_CM_STD, L: SCF_CM_STD },
  Emh: { g: 2, en: 'E harmonic minor', ko: 'E 화성 단음계', st: SP_HAR, s: 4, nm: ['E', 'F♯', 'G', 'A', 'B', 'C', 'D♯'], R: SCF_CM_STD, L: SCF_CM_STD },
  F: { g: 2, en: 'F major', ko: 'F장조', st: SP_MAJ, s: 5, nm: ['F', 'G', 'A', 'B♭', 'C', 'D', 'E'], R: [1, 2, 3, 4, 1, 2, 3, 1], L: SCF_CM_STD },
  Dmh: { g: 2, en: 'D harmonic minor', ko: 'D 화성 단음계', st: SP_HAR, s: 2, nm: ['D', 'E', 'F', 'G', 'A', 'B♭', 'C♯'], R: SCF_CM_STD, L: SCF_CM_STD },
  D: { g: 3, en: 'D major', ko: 'D장조', st: SP_MAJ, s: 2, nm: ['D', 'E', 'F♯', 'G', 'A', 'B', 'C♯'], R: SCF_CM_STD, L: SCF_CM_STD },
  Bmh: { g: 3, en: 'B harmonic minor', ko: 'B 화성 단음계', st: SP_HAR, s: -1, nm: ['B', 'C♯', 'D', 'E', 'F♯', 'G', 'A♯'], R: SCF_CM_STD, L: [1, 2, 3, 4, 1, 2, 3, 1] },
  Bb: { g: 3, en: 'B♭ major', ko: 'B♭장조', st: SP_MAJ, s: -2, nm: ['B♭', 'C', 'D', 'E♭', 'F', 'G', 'A'], R: [2, 1, 2, 3, 1, 2, 3, 4], L: [2, 1, 2, 3, 4, 1, 2, 3] },
  Gmh: { g: 3, en: 'G harmonic minor', ko: 'G 화성 단음계', st: SP_HAR, s: 7, nm: ['G', 'A', 'B♭', 'C', 'D', 'E♭', 'F♯'], R: SCF_CM_STD, L: SCF_CM_STD },
};
const SCF_CM_KEYS = ['G', 'Emh', 'F', 'Dmh', 'D', 'Bmh', 'Bb', 'Gmh'];
const scfCm = (k) => { const c = SCF_CM[k], R = c.st.map(x => c.s + x).concat([c.s + 12]), L = [c.s].concat([6, 5, 4, 3, 2, 1, 0].map(d => c.s - 12 + c.st[d]));
  const nmR = c.nm.concat([c.nm[0]]), nmL = [c.nm[0]].concat([6, 5, 4, 3, 2, 1, 0].map(d => c.nm[d])); return { R, L, nmR, nmL, fR: c.R, fL: c.L }; };
const scfMirror = (k) => SCF_CM[k].R.every((f, j) => f === SCF_CM[k].L[j]);
const scfCmName = (k) => t(SCF_CM[k].en, SCF_CM[k].ko);
// the melodic minor: up with the 6th and 7th raised, down as the natural minor
const SCF_MEL = { Gm: { g: 2, s: 7, en: 'G melodic minor', ko: 'G 가락 단음계', up: ['G', 'A', 'B♭', 'C', 'D', 'E', 'F♯', 'G'], dn: ['G', 'F', 'E♭', 'D', 'C', 'B♭', 'A', 'G'] },
  Cm: { g: 3, s: 0, en: 'C melodic minor', ko: 'C 가락 단음계', up: ['C', 'D', 'E♭', 'F', 'G', 'A', 'B', 'C'], dn: ['C', 'B♭', 'A♭', 'G', 'F', 'E♭', 'D', 'C'] } };
const SCF_MEL_UP = [0, 2, 3, 5, 7, 9, 11, 12], SCF_MEL_DN = [12, 10, 8, 7, 5, 3, 2, 0];
// the chromatic scale: the book's starting notes; fingers by the book's own pattern (chromFinger, as in the Scales room)
const SCF_CHROM = [['D', 2, 2], ['A', -3, 3], ['E♭', 3, 3]];
const scfChF = (i, h, edge) => chromFinger(spPc(i), h === 'R' ? 'RH' : 'LH', edge);
const SCF_CH_NM = ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];
const scfChLet = (i) => (spPc(i) === 3 ? 'D♯/E♭' : SCF_CH_NM[spPc(i)]);
const scfKeyChips = (keys, val, set, nameOf) => spChips(keys.map(k => [k, nameOf(k)]), val, set);

// ── step 1: start on a black key: where do the thumbs go? ──
function ScfThumbPad({ fixed, onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState(fixed ? fixed.k : 'Bb'), [h, setH] = useState(fixed ? fixed.h : 'R'), [found, setFound] = useState([]), [bad, setBad] = useState(null), [miss, setMiss] = useState(0), [at, setAt] = useState(-1);
  const K = scfKeys(k, 1), F = SCF[k][h].slice(0, 8), targets = scfThumbPcs(k, h), done = found.length === targets.length, lo = SCF[k].r, N = scfNames(k, 1);
  const reset = (fn) => { T.clear(); setFound([]); setBad(null); setMiss(0); setAt(-1); if (fn) fn(); };
  const play = () => { T.clear(); const ix = spUpDown(8), run = spPlay(ix.map((j, n) => ({ at: n * 0.5, keys: [K[j] - (h === 'L' ? 12 : 0)], len: n === ix.length - 1 ? 2 : 0.5 })), 80); if (!run) return; ix.forEach((j, n) => T.at(run.ms(n * 0.5), () => setAt(j))); T.at(run.ms(ix.length * 0.5 + 1.2), () => setAt(-1)); };
  const tap = (i) => { playKey(i - (h === 'L' ? 12 : 0), 0.5); if (done) return; if (!K.includes(i)) { setBad(i); setMiss(m => m + 1); return; }
    const pc = spPc(i); if (targets.includes(pc)) { if (found.includes(pc)) return; const nf = found.concat([pc]); setFound(nf); setBad(null); if (nf.length === targets.length) { if (onResult) onResult({ ok: miss === 0 }); T.at(300, play); } }
    else { setBad(i); setMiss(m => m + 1); } };
  const lit = {}; K.forEach(x => { lit[x] = found.includes(spPc(x)) ? 'good' : 'pale'; }); if (bad != null) lit[bad] = 'bad'; if (at >= 0) lit[K[at]] = 'cor';
  const nums = {}; if (done) K.forEach((x, j) => { nums[x] = F[j]; });
  const act = {}; if (at >= 0) act[(h === 'L' ? 'd' : '') + K[at]] = true;
  const thumbsTxt = targets.map(pc => N[K.findIndex(x => spPc(x) === pc)]).join(t(' and ', '와 '));
  return (
    <div className="try-box" style={actBox} data-scf="thumb">
      <div style={actTitle}>{t('Where do the thumbs go?', '엄지는 어디에?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>이 스케일들에서 <b>엄지는 흰건반만</b> 쳐요. 검은건반에서 시작하는 스케일이면 <b>오른손은 2번으로 시작하고, 처음 나오는 흰건반에 엄지</b>가 와요. 한 옥타브에서 엄지가 치는 건반을 모두 눌러요.</>
        : <>In these scales <b>the thumb plays only white keys</b>. When a scale starts on a black key, <b>the right hand starts on 2 and the thumb takes the first white key</b>. Tap every key the thumb plays in one octave.</>}</div>
      {!fixed && scfKeyChips(SCF_KEYS, k, (x) => reset(() => setK(x)), (x) => SCF[x].nm[0] + (SCF[x].st === SP_MAJ ? '' : 'm'))}
      {!fixed && spChips([['R', spHand('R')], ['L', spHand('L')]], h, (x) => reset(() => setH(x)))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 4px'}}>{scfName(k)} · {spHand(h)}</div>
      <SpKb lo={lo} hi={lo + 12} W={30} H={84} lit={lit} names={done ? Object.fromEntries(K.map((x, j) => [x, N[j]])) : { [K[0]]: N[0] }} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}} act={act} onTap={tap} label={scfName(k)}/>
      {spMsg(done ? t('Thumbs on ' + thumbsTxt + '. Fingers: ' + F.join(' ') + '.', '엄지는 ' + thumbsTxt + '. 손가락: ' + F.join(' ') + '.') : bad != null ? (K.includes(bad) ? t('Not the thumb there: count the fingers up from the first note.', '거기는 엄지가 아니에요: 첫 음부터 손가락을 세어 봐요.') : t('That key is not in the scale.', '그 건반은 이 스케일에 없어요.'))
        : scfBlackStart(k) && h === 'R' ? t('Starts on a black key: finger 2 first, then the thumb on the first white key.', '검은건반에서 시작: 먼저 2번, 그다음 첫 흰건반에 엄지.') : t('Find the thumb’s keys: ' + found.length + ' of ' + targets.length, '엄지가 치는 건반 찾기: ' + targets.length + '개 중 ' + found.length + '개'), done ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── step 2: two octaves hands together: where do both thumbs play together? ──
function ScfStrip({ k, cur = -1, found = [], bad = null, onTap, mw = 460 }) {
  const N = scfNames(k), R = SCF[k].R, L = SCF[k].L, n = N.length;
  const cell = (j, txt, row, col) => <div key={row + '-' + j} style={{gridRow:row,gridColumn:j + 2,textAlign:'center',fontWeight:900,fontSize:13,lineHeight:'26px',height:26,color:col,borderRadius:13,
    background:found.includes(j) ? '#d9efe7' : j === cur ? '#fbe3da' : 'transparent',border:'1.5px solid ' + (found.includes(j) ? PEN_G : j === bad ? '#c8361b' : j === cur ? PEN_C : 'transparent')}}>{txt}</div>;
  const nameSt = (j, x) => ({gridRow:2,gridColumn:j + 2,height:30,padding:0,minWidth:0,boxSizing:'border-box',display:'flex',alignItems:'center',justifyContent:'center',border:'1.5px solid ' + (j === bad ? '#c8361b' : PEN_N),borderRadius:6,background:found.includes(j) ? PEN_G : '#fff',color:found.includes(j) ? '#fff' : PEN_N,fontWeight:900,fontSize:x.length > 1 ? 10 : 12.5,cursor:onTap ? 'pointer' : 'default',fontFamily:'Inter, sans-serif'});
  return <div style={{maxWidth:mw,margin:'0 auto'}}><div style={{display:'grid',gridTemplateColumns:'30px repeat(' + n + ',minmax(0,1fr))',gap:1,rowGap:4,alignItems:'center'}}>
    {Array.from({ length: Math.ceil(n / 2) }, (_, b) => <div key={'bg' + b} style={{gridRow:'1 / 4',gridColumn:(2 * b + 2) + ' / span ' + Math.min(2, n - 2 * b),background:b % 2 ? 'transparent' : 'rgba(38,41,107,0.06)',borderRadius:8,alignSelf:'stretch'}}/>)}
    <div style={{gridRow:1,gridColumn:1,fontSize:10.5,fontWeight:800,color:BK.muted}}>{t('right', '오른손')}</div>
    {R.map((f, j) => cell(j, f, 1, PEN_C))}
    <div style={{gridRow:2,gridColumn:1}}/>
    {N.map((x, j) => onTap ? <button key={'n' + j} onClick={() => onTap(j)} aria-label={x} style={nameSt(j, x)}>{x}</button> : <div key={'n' + j} style={nameSt(j, x)}>{x}</div>)}
    <div style={{gridRow:3,gridColumn:1,fontSize:10.5,fontWeight:800,color:BK.muted}}>{t('left', '왼손')}</div>
    {L.map((f, j) => cell(j, f, 3, PEN_N))}
  </div>
  <div style={{display:'flex',justifyContent:'center',gap:8,marginTop:6,fontSize:12,fontWeight:800,color:BK.muted}}><span style={{display:'inline-block',width:22,height:12,borderRadius:4,background:'rgba(38,41,107,0.10)',verticalAlign:'middle'}}/>{t('one beat: run-ning, two notes', '한 박: 티-티, 두 음')}</div></div>;
}
function ScfMeetPad({ fixed, onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState(fixed || 'D'), [bpm, setBpm] = useState(60), [cur, setCur] = useState(-1), [found, setFound] = useState([]), [bad, setBad] = useState(null), [never, setNever] = useState(null), [miss, setMiss] = useState(0);
  const targets = scfMeet(k), N = scfNames(k), done = targets.length ? found.length === targets.length : never === 'ok';
  const reset = (fn) => { T.clear(); setCur(-1); setFound([]); setBad(null); setNever(null); setMiss(0); if (fn) fn(); };
  const play = () => { T.clear(); setCur(-1); const KR = scfKeys(k), ix = spUpDown(15);
    const run = spPlay(ix.map((j, n) => ({ at: n / 2, keys: [KR[j], KR[j] - 12], len: n === ix.length - 1 ? 2 : 0.5, vol: 0.12 })), bpm, 4); if (!run) return;
    ix.forEach((j, n) => T.at(run.ms(n / 2), () => setCur(j))); T.at(run.ms(ix.length / 2 + 1.5), () => setCur(-1)); };
  const finish = (m) => { if (onResult) onResult({ ok: m === 0 }); };
  const tap = (j) => { playKey(scfKeys(k)[j], 0.5); if (done) return; if (targets.includes(j)) { if (found.includes(j)) return; const nf = found.concat([j]); setFound(nf); setBad(null); if (nf.length === targets.length) finish(miss); }
    else { setBad(j); setMiss(m => m + 1); T.at(1100, () => setBad(null)); } };
  const sayNever = () => { if (done) return; if (!targets.length) { setNever('ok'); finish(miss); } else { setNever('no'); setMiss(m => m + 1); } };
  const kind = scfMeetKind(k);
  return (
    <div className="try-box" style={actBox} data-scf="meet">
      <div style={actTitle}>{t('Where do the thumbs meet?', '엄지는 어디서 만날까?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 옥타브, <b>양손 함께</b>, 한 옥타브 떨어져서. 오른손 번호는 위, 왼손은 아래. 두 엄지가 함께 치는 음을 모두 눌러요. <b>한 번도 안 만나는</b> 스케일도 있어요.</>
        : <>Two octaves, <b>hands together</b>, an octave apart. The right hand's fingers above, the left hand's below. Tap every note where both thumbs play. In some scales they <b>never meet</b>.</>}</div>
      {!fixed && scfKeyChips(SCF_KEYS, k, (x) => reset(() => setK(x)), (x) => SCF[x].nm[0] + (SCF[x].st === SP_MAJ ? '' : 'm'))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 6px'}}>{scfName(k)}</div>
      <ScfStrip k={k} cur={cur} found={found} bad={bad} onTap={tap}/>
      {spMsg(done ? t(SCF_MEET_LAB[kind][0] + (kind === 'tonic4' ? ': ' + targets.map(j => N[j]).join(', ') : '') + '.' + (kind === 'never' ? ' Keep the run-ning even through every turn.' : ''), SCF_MEET_LAB[kind][1] + (kind === 'tonic4' ? ': ' + targets.map(j => N[j]).join(', ') : '') + '.' + (kind === 'never' ? ' 넘어갈 때마다 티-티를 고르게.' : ''))
        : never === 'no' ? t('They do meet somewhere: look for a 1 above and a 1 below.', '어딘가에서 만나요: 위에도 1, 아래에도 1인 곳.') : bad != null ? t('Not there: look for a 1 above and a 1 below.', '거기가 아니에요: 위에도 1, 아래에도 1인 곳.')
        : cur >= 0 ? t('run-ning, run-ning…', '티-티, 티-티…') : t('Tap where both thumbs play, or say they never meet.', '두 엄지가 함께 치는 곳을 누르거나, 안 만난다고 해요.'), done ? BK.green : bad != null || never === 'no' ? BK.coral : undefined)}
      {!done && <div style={{textAlign:'center',marginTop:6}}><button className="choice-btn" style={{padding:'10px 16px',fontSize:14.5,fontWeight:900}} onClick={sayNever}>{t('They never meet', '한 번도 안 만나요')}</button></div>}
      {spChips([[60, spMM(60)], [84, spMM(84)], [92, spMM(92)]], bpm, (x) => { T.clear(); setCur(-1); setBpm(x); })}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hands together', '▶ 양손 함께 듣기')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── step 3: the melodic minor: going up, which two notes rise? ──
function ScfMelRow({ m, dir, show = true }) {
  const c = SCF_MEL[m], row = dir === 'up' ? c.up : c.dn, ch = dir === 'up' ? [5, 6] : [1, 2];
  return <div style={{display:'flex',alignItems:'center',gap:3,justifyContent:'center',flexWrap:'wrap',margin:'3px 0'}}>
    <span style={{width:48,fontSize:12,fontWeight:900,color:BK.muted,textAlign:'right',lineHeight:1.15}}>{dir === 'up' ? t('up ↗', '올라갈 때') : t('down ↘', '내려올 때')}</span>
    {row.map((x, j) => <span key={j} style={{minWidth:27,height:27,padding:'0 3px',boxSizing:'border-box',borderRadius:14,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:13,fontWeight:900,
      background:show && ch.includes(j) ? (dir === 'up' ? BK.coral : '#fff') : '#fff',color:show && ch.includes(j) && dir === 'up' ? '#fff' : BK.ink,border:'1.5px solid ' + (show && ch.includes(j) ? BK.coral : BK.ink)}}>{show || !ch.includes(j) ? x : '?'}</span>)}
  </div>;
}
function ScfMelPad({ fixed, onResult }) {
  const T = useSpTimers();
  const [m, setM] = useState(fixed || 'Gm'), [found, setFound] = useState([]), [bad, setBad] = useState(null), [miss, setMiss] = useState(0), [at, setAt] = useState(null);
  const c = SCF_MEL[m], lo = c.s, nat = SP_NAT.map(x => lo + x).concat([lo + 12]), targets = [lo + 9, lo + 11], done = found.length === 2;
  const reset = (fn) => { T.clear(); setFound([]); setBad(null); setMiss(0); setAt(null); if (fn) fn(); };
  const play = () => { T.clear(); const ev = SCF_MEL_UP.concat(SCF_MEL_DN.slice(1)); const run = spPlay(ev.map((x, n) => ({ at: n * 0.5, keys: [lo + x], len: n === ev.length - 1 ? 2 : 0.5 })), 80); if (!run) return;
    ev.forEach((x, n) => T.at(run.ms(n * 0.5), () => setAt(lo + x))); T.at(run.ms(ev.length * 0.5 + 1.2), () => setAt(null)); };
  const tap = (i) => { playKey(i, 0.5); if (done) return; if (targets.includes(i)) { if (found.includes(i)) return; const nf = found.concat([i]); setFound(nf); setBad(null); if (nf.length === 2) { if (onResult) onResult({ ok: miss === 0 }); T.at(300, play); } }
    else { setBad(i); setMiss(x => x + 1); } };
  const lit = {}; nat.forEach(x => { lit[x] = 'pale'; }); found.forEach(x => { lit[x] = 'good'; }); if (bad != null) lit[bad] = 'bad'; if (at != null) lit[at] = 'cor';
  const nm = {}, natNm = c.dn.slice().reverse(); nat.forEach((x, j) => { nm[x] = natNm[j]; }); found.forEach(x => { nm[x] = x === lo + 9 ? c.up[5] : c.up[6]; });
  return (
    <div className="try-box" style={actBox} data-scf="mel">
      <div style={actTitle}>{t('The melodic minor', '가락 단음계')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>가락 단음계는 <b>올라갈 때 6도와 7도를 반음 올리고</b>, <b>내려올 때는 자연 단음계</b>로 돌아와요. 건반은 자연 단음계예요. 올라갈 때 바뀌는 두 음을 눌러요.</>
        : <>The melodic minor <b>raises the 6th and the 7th going up</b> and <b>comes down as the natural minor</b>. The keys show the natural minor. Tap the two notes that change going up.</>}</div>
      {!fixed && spChips([['Gm', t('G minor', 'G단조')], ['Cm', t('C minor', 'C단조')]], m, (x) => reset(() => setM(x)))}
      <SpKb lo={lo} hi={lo + 12} W={30} H={84} lit={lit} names={nm} onTap={tap} label={t(c.en, c.ko)}/>
      <ScfMelRow m={m} dir="up" show={done}/>
      <ScfMelRow m={m} dir="down"/>
      {spMsg(done ? t('Up: ' + c.up[5] + ' and ' + c.up[6] + '. Down: ' + c.dn[1] + ' and ' + c.dn[2] + ' again.', '올라갈 때: ' + c.up[5] + ', ' + c.up[6] + '. 내려올 때: 다시 ' + c.dn[1] + ', ' + c.dn[2] + '.') : bad != null ? t('Not that one: it is the 6th and 7th that rise, one semitone each.', '그 음이 아니에요: 6도와 7도가 반음씩 올라가요.') : t('Tap the two notes going up: ' + found.length + ' of 2', '올라갈 때 바뀌는 두 음: 2개 중 ' + found.length + '개'), done ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Up and down', '▶ 올라갔다 내려오기')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── step 4: contrary motion from one note: mirror twins, or not? ──
function ScfCmKb({ k, mark = -1, W = 22, H = 70 }) {
  const c = scfCm(k), up = {}, dn = {}, lit = {}, nm = {};
  c.R.forEach((x, j) => { up[x] = c.fR[j]; lit[x] = 'pale'; nm[x] = c.nmR[j]; }); c.L.forEach((x, j) => { dn[x] = c.fL[j]; lit[x] = 'pale'; nm[x] = c.nmL[j]; });
  if (mark >= 0) { lit[c.R[mark]] = 'cor'; lit[c.L[mark]] = 'cor'; }
  return <><SpKb lo={c.L[7]} hi={c.R[7]} W={W} H={H} lit={lit} names={nm} up={up} dn={dn} label={scfCmName(k)} k={1.5}/>
    <div style={{display:'flex',justifyContent:'space-between',fontSize:12,fontWeight:800,color:BK.muted,margin:'2px 4px 0'}}><span>{t('← left hand: down', '← 왼손: 아래로')}</span><span>{t('right hand: up →', '오른손: 위로 →')}</span></div></>;
}
const scfFirstDiff = (k) => SCF_CM[k].R.findIndex((f, j) => f !== SCF_CM[k].L[j]);
function ScfMirrorPad({ fixed, onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState(fixed || 'G'), [ans, setAns] = useState(null);
  const yes = scfMirror(k), d = scfFirstDiff(k), c = scfCm(k), ok = ans != null && ans === yes;
  const reset = (fn) => { T.clear(); setAns(null); if (fn) fn(); };
  const play = () => { T.clear(); const ix = spUpDown(8); spPlay(ix.map((j, n) => ({ at: n * 0.5, keys: [c.R[j], c.L[j]], len: n === ix.length - 1 ? 2 : 0.5, vol: 0.13 })), 66, 4); };
  const say = (v) => { if (ans != null) return; setAns(v); if (onResult) onResult({ ok: v === yes }); };
  return (
    <div className="try-box" style={actBox} data-scf="mirror">
      <div style={actTitle}>{t('Mirror twins, or not?', '거울 쌍둥이일까, 아닐까?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>반대 방향: 두 손이 <b>한 음</b>에서 시작해서 멀어졌다가 돌아와요. <b>손마다 자기 스케일 번호</b>를 써요. 어떤 조에서는 번호가 똑같아서 거울 쌍둥이, 어떤 조에서는 달라요. 번호를 비교해 봐요.</>
        : <>Contrary motion: both hands start on <b>one note</b>, move apart and come back. <b>Each hand keeps its own scale fingering</b>. In some keys the numbers match all the way (mirror twins); in others they don't. Compare the numbers.</>}</div>
      {!fixed && scfKeyChips(SCF_CM_KEYS, k, (x) => reset(() => setK(x)), (x) => SCF_CM[x].nm[0] + (SCF_CM[x].st === SP_MAJ ? '' : 'm'))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 4px'}}>{scfCmName(k)}</div>
      <ScfCmKb k={k} mark={ans != null && !yes ? d : -1}/>
      {ans == null ? <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:10}}>
        <button className="choice-btn" style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => say(true)}>{t('Mirror twins', '거울 쌍둥이')}</button>
        <button className="choice-btn" style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => say(false)}>{t('Not mirror twins', '거울 쌍둥이 아님')}</button></div>
        : spMsg((ok ? t('Yes. ', '맞아요. ') : t('Look again. ', '다시 봐요. ')) + (yes ? t('The same numbers all the way: mirror twins.', '끝까지 같은 번호: 거울 쌍둥이.') : t('Note ' + (d + 1) + ': the right hand plays ' + c.nmR[d] + ' with ' + c.fR[d] + ', the left hand ' + c.nmL[d] + ' with ' + c.fL[d] + '. Each hand keeps its own fingering.', (d + 1) + '번째 음: 오른손은 ' + c.nmR[d] + '에 ' + c.fR[d] + '번, 왼손은 ' + c.nmL[d] + '에 ' + c.fL[d] + '번. 손마다 자기 번호를 지켜요.')), ok ? BK.green : BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {ans != null && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── step 5: the chromatic scale from any note: which finger? ──
function ScfChromPad({ fixed, onResult }) {
  const T = useSpTimers();
  const [st, setSt] = useState(fixed ? fixed.st : 0), [h, setH] = useState(fixed ? fixed.h : 'R'), [at, setAt] = useState(0), [wrong, setWrong] = useState(null), [miss, setMiss] = useState(0), [pl, setPl] = useState(-1);
  const s0 = SCF_CHROM[st][1], K = Array.from({ length: 13 }, (_, j) => s0 + j), F = K.map((x, j) => scfChF(x, h, j === 0 || j === 12)), done = at >= 13;
  const reset = (fn) => { T.clear(); setAt(0); setWrong(null); setMiss(0); setPl(-1); if (fn) fn(); };
  const play = () => { T.clear(); const ix = Array.from({ length: 13 }, (_, j) => j).concat(Array.from({ length: 12 }, (_, j) => 11 - j)); const run = spPlay(ix.map((j, n) => ({ at: n * 0.5, keys: [K[j] - (h === 'L' ? 12 : 0)], len: n === ix.length - 1 ? 2 : 0.5 })), 84); if (!run) return;
    ix.forEach((j, n) => T.at(run.ms(n * 0.5), () => setPl(j))); T.at(run.ms(ix.length * 0.5 + 1.2), () => setPl(-1)); };
  const say = (f) => { if (done) return; if (f === F[at]) { const n = at + 1; setAt(n); setWrong(null); playKey(K[at] - (h === 'L' ? 12 : 0), 0.4); if (n >= 13) { if (onResult) onResult({ ok: miss === 0 }); T.at(300, play); } } else { setWrong(f); setMiss(x => x + 1); } };
  const lit = {}, nums = {}, act = {}; K.forEach((x, j) => { if (j < at) { nums[x] = F[j]; lit[x] = 'pale'; } }); if (!done) lit[K[at]] = wrong != null ? 'bad' : 'cor'; if (pl >= 0) { lit[K[pl]] = 'cor'; act[(h === 'L' ? 'd' : '') + K[pl]] = true; }
  return (
    <div className="try-box" style={actBox} data-scf="chrom">
      <div style={actTitle}>{t('Chromatic from any note', '어느 음에서든 반음계')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>규칙 하나면 어느 음에서든 시작해요: <b>검은건반은 3번</b>, <b>흰건반은 1번</b>, 그리고 <b>흰건반 둘이 붙어 있는 곳은 2번</b>(오른손은 F와 C, 왼손은 E와 B). 빨간 건반의 손가락을 골라요.</>
        : <>One rule starts it from any note: <b>3 on every black key</b>, <b>1 on white keys</b>, and <b>2 where two white keys sit together</b> (the right hand's F and C, the left hand's E and B). Choose the finger for the coral key.</>}</div>
      {!fixed && spChips(SCF_CHROM.map(([n], j) => [j, t('From ' + n, n + '에서')]), st, (x) => reset(() => setSt(x)))}
      {!fixed && spChips([['R', spHand('R')], ['L', spHand('L')]], h, (x) => reset(() => setH(x)))}
      <SpKb lo={s0} hi={s0 + 12} W={30} H={84} lit={lit} names={done ? Object.fromEntries(K.map(x => [x, scfChLet(x).split('/')[0]])) : { [K[0]]: scfChLet(K[0]).split('/')[0] }} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}} act={act} label={t('Chromatic scale', '반음계')}/>
      {!done && <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:8,marginTop:10}}>{[1, 2, 3].map(f => <button key={f} className={'choice-btn' + (wrong === f ? ' bad' : '')} onClick={() => say(f)} style={{padding:'12px 4px',fontSize:18,fontWeight:900}}>{f}</button>)}</div>}
      {spMsg(done ? t('All 13 ✓ ' + (h === 'R' ? 'Right hand: 2 on F and C.' : 'Left hand: 2 on E and B.') + (miss ? '' : ' First time!'), '13개 모두 ✓ ' + (h === 'R' ? '오른손: F와 C는 2번.' : '왼손: E와 B는 2번.') + (miss ? '' : ' 한 번에!'))
        : wrong != null ? (spIsW(K[at]) ? t('A white key: 1, unless two white keys sit together here.', '흰건반: 1번, 흰건반 둘이 붙어 있는 곳만 2번.') : t('A black key: always 3.', '검은건반: 언제나 3번.')) : t(spHand(h) + ': note ' + (at + 1) + ' of 13', spHand(h) + ': 13개 중 ' + (at + 1) + '번째'), done ? BK.green : wrong != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const scfPicThumb = () => { const m = spMiniKeys(-2, 10, { [-2]: 'pale', 0: 'cor', 2: 'pale', 3: 'pale', 5: 'cor', 7: 'pale', 9: 'pale', 10: 'pale' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const scfPicMeet = () => spPicTwo();
const scfPicMel = () => ({ shapes: [{ k: 'raw', svg: '<path d="M6 36 L36 10 L66 36" fill="none" stroke="#26296b" stroke-width="2"/>' + lsCircleSvg(26, 19, 6, 'play', '6') + lsCircleSvg(36, 10, 6, 'play', '7') + lsCircleSvg(56, 27, 6, 'beat', '') }], vb: [0, 0, 72, 44] });
const scfPicMirror = () => spPicMirror();
const scfPicChrom = () => { const m = spMiniKeys(2, 14, { 3: 'cor', 6: 'cor', 8: 'cor', 10: 'cor', 13: 'cor' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };

function scfLbPages(scr = false) {
  const ch = 'scales-23', sp = bkChapterNo('scale-play');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks5 = [[scfPicThumb(), t('I start a black-key scale on finger 2, with my thumbs on white keys', '검은건반 스케일을 2번으로 시작하고, 엄지는 흰건반에')], [scfPicMeet(), t('I play two octaves hands together, two notes a beat, even where the thumbs never meet', '두 옥타브 양손 함께, 한 박에 두 음, 엄지가 안 만나는 스케일도 고르게')],
    [scfPicMel(), t('I play the melodic minor: up with the 6th and 7th raised, down as the natural minor', '가락 단음계: 올라갈 때 6도와 7도를 올리고, 내려올 때는 자연 단음계')], [scfPicMirror(), t('I play contrary motion from one note, each hand with its own fingers', '한 음에서 반대 방향으로, 손마다 자기 번호로')],
    [scfPicChrom(), t('I play the chromatic scale from any note: 3 on black, 1 on white, 2 where two white keys sit together', '어느 음에서든 반음계: 검은건반 3, 흰건반 1, 흰건반 둘이 붙은 곳은 2')]];
  const toc = [[t('Start on a black key', '검은건반에서 시작'), 2], [t('Where the thumbs meet', '엄지가 만나는 곳'), 3], [t('The melodic minor', '가락 단음계'), 4], [t('Mirror twins, or not?', '거울 쌍둥이일까, 아닐까?'), 5], [t('Chromatic from any note', '어느 음에서든 반음계'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const kbW = scr ? 30 : 40, kbH = scr ? 80 : 104;
  const thumbStill = (k, h) => { const K = scfKeys(k, 1), F = SCF[k][h].slice(0, 8), lit = {}, nums = {}; K.forEach((x, j) => { lit[x] = F[j] === 1 ? 'cor' : 'pale'; nums[x] = F[j]; });
    return <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{scfName(k)} · {spHand(h)}</div><SpKb lo={SCF[k].r} hi={SCF[k].r + 12} W={kbW} H={kbH} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, scfNames(k, 1)[j]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}}/></div>; };
  const chromStill = () => { const s0 = 2, K = Array.from({ length: 13 }, (_, j) => s0 + j), up = {}, dn = {}, lit = {}; K.forEach((x, j) => { up[x] = scfChF(x, 'R', j === 0 || j === 12); dn[x] = scfChF(x, 'L', j === 0 || j === 12); if (spIsW(x)) lit[x] = 'pale'; });
    [5, 12].forEach(x => { lit[x] = 'cor'; }); return <SpKb lo={s0} hi={s0 + 12} W={kbW} H={kbH} lit={lit} names={{ 2: 'D', 5: 'F', 12: 'C', 4: 'E', 11: 'B' }} up={up} dn={dn}/>; };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The Grade 2 and 3 scales, as skills (chapter ' + sp + ' has the Grade 1 ones). Two octaves, mf, clear even legato, from memory, two notes a beat: ♩ = 84 at Grade 2 and 92 at Grade 3; contrary motion ♩ = 66 and 80. Fingerings are the technical work book\'s; another fingering is fine if it is logical and systematic. The keys for each grade are in the teacher\'s copy.', '2·3급 스케일을 기술로(' + sp + '장은 1급). 두 옥타브, mf, 고르고 또렷한 레가토, 외워서, 한 박에 두 음: 2급 ♩ = 84, 3급 92; 반대 방향은 ♩ = 66과 80. 손가락 번호는 테크니컬 워크 책 그대로이고, 논리적이고 일관되면 다른 번호도 괜찮아요. 급마다의 조는 선생님용에 있어요.'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Scales Further', '스케일 한 걸음 더')}</div>
      </div></LbOnly>
      <LbPic h={170}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{thumbStill('Bb', 'R')}</div></LbPic>
      <LbSay size={18}>{t('Scales for Grades 2 and 3: black-key starts, two hands that turn at different times, the melodic minor, contrary motion in new keys, and the chromatic scale from any note.', '2·3급 스케일: 검은건반에서 시작하기, 따로 넘어가는 두 손, 가락 단음계, 새 조의 반대 방향, 어느 음에서든 반음계.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('start a scale on a black key, with the thumbs on white keys', '검은건반에서 스케일을 시작하고, 엄지는 흰건반에 둘 수 있어요'), t('play two octaves hands together, even when the thumbs never meet', '엄지가 만나지 않아도 두 옥타브를 양손으로 칠 수 있어요'), t('play the melodic minor up and down', '가락 단음계를 올라갔다 내려올 수 있어요'), t('play the chromatic scale from any note', '어느 음에서든 반음계를 칠 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Start on a black key', '검은건반에서 시작')}
      teacher={<>{t('Your rule: a scale that starts on a black key starts on finger 2 in the right hand, and the thumb takes the first white key (B♭ major: 2 1 2 3 1 2 3 4; E♭ major: 2 1 2 3 4 1 2 3; F♯ minor: 2 3 1 2 3 1 2 3). The left hand starts on 3 in B♭ and E♭, on 4 in F♯ minor. In every Grade 2 and 3 scale the thumb plays only white keys: finding the thumbs first is the quickest way to learn a new fingering.', '선생님 규칙: 검은건반에서 시작하는 스케일은 오른손 2번으로 시작하고, 처음 나오는 흰건반에 엄지(B♭장조 2 1 2 3 1 2 3 4, E♭장조 2 1 2 3 4 1 2 3, F♯단조 2 3 1 2 3 1 2 3). 왼손은 B♭과 E♭에서 3번, F♯단조에서 4번으로 시작해요. 2·3급 스케일은 모두 엄지가 흰건반만 쳐요: 엄지 자리를 먼저 찾는 게 새 운지를 익히는 가장 빠른 길이에요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{thumbStill('Bb', 'R')}{thumbStill('Eb', 'R')}</div></LbPic>} live={<ScfThumbPad/>}/>
      <LbSay>{LANG === 'ko' ? <>검은건반에서 시작하면 <b>오른손은 2번</b>으로 시작해요. <b>엄지는 처음 나오는 흰건반</b>에. 이 스케일들에서 엄지는 <b>흰건반만</b> 쳐요.</> : <>Starting on a black key? The <b>right hand starts on 2</b>, and <b>the thumb takes the first white key</b>. In these scales the thumb plays <b>only white keys</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>B♭장조 오른손: 엄지 자리 C와 F를 먼저 찾아요. 그다음 2 1 2 3 1 2 3 4.</>, <>왼손: 3 2 1 4 3 2 1 3. 엄지는 D와 A.</>, <>한 옥타브씩, 그다음 두 옥타브. 한 박에 두 음, 메트로놈 60부터.</>]
        : [<>B♭ major, right hand: find the thumb's keys first, C and F. Then 2 1 2 3 1 2 3 4.</>, <>Left hand: 3 2 1 4 3 2 1 3. The thumb plays D and A.</>, <>One octave, then two. Two notes a beat, from metronome 60.</>]}/>
      <LbRemember>{t('Black key first? Finger 2, then the thumb on the first white key.', '검은건반이 먼저? 2번, 그다음 첫 흰건반에 엄지.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Where the thumbs meet', '엄지가 만나는 곳')}
      teacher={<>{spTx(t('Two octaves, hands separately and together, an octave apart, two notes a beat: Grade 2 at ♩ = 84, Grade 3 at 92. In D and A major, G and C minor the thumbs play together only on the middle keynote; in B minor on B and E; in B♭ and E♭ major and F♯ minor never, so each hand turns on its own and an uneven turn shows at once. Practise hands together around each turn, slowly, then join them up. The melodic minor is hands separately at Grade 2.', '두 옥타브, 한 손씩 그리고 한 옥타브 떨어져 양손 함께, 한 박에 두 음: 2급 ♩ = 84, 3급 92. D장조, A장조, G단조, C단조는 가운데 으뜸음에서만 두 엄지가 함께; B단조는 B와 E에서; B♭장조, E♭장조, F♯단조는 한 번도 안 만나요. 그래서 손마다 따로 넘어가고, 고르지 않은 넘기기가 바로 들려요. 넘기는 곳마다 천천히 양손으로 연습하고, 그다음 이어요. 2급의 가락 단음계는 한 손씩만.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><ScfStrip k="Bb" mw={660}/></div></LbPic>} live={<ScfMeetPad/>}/>
      <LbSay>{LANG === 'ko' ? <>양손 함께 두 옥타브. 두 엄지가 <b>가운데 으뜸음에서만</b> 만나는 스케일, <b>두 군데</b>에서 만나는 스케일, 그리고 <b>한 번도 안 만나는</b> 스케일이 있어요. B♭장조는 한 번도 안 만나요.</> : <>Two octaves, hands together. In some scales the thumbs meet <b>only on the middle keynote</b>, in one <b>in two places</b>, and in some <b>never</b>. In B♭ major they never meet.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>한 손씩 두 옥타브. 그다음 양손 함께, 아주 천천히.</>, <>엄지가 안 만나는 곳: 넘어가는 곳 두세 음만 양손으로 여러 번.</>, <>티-티를 고르게: 메트로놈 60, 그다음 84(2급), 92(3급).</>]
        : [<>Two octaves, each hand. Then hands together, very slowly.</>, <>Where the thumbs don't meet: just the two or three notes around each turn, hands together, several times.</>, <>Even run-ning: metronome 60, then 84 (Grade 2), 92 (Grade 3).</>]}/>
      <LbRemember>{t('The thumbs never meet? Each hand turns on its own: keep it even.', '엄지가 안 만나요? 손마다 따로 넘어가요: 고르게.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The melodic minor', '가락 단음계')}
      teacher={<>{t('The melodic minor raises the 6th and 7th going up and comes down as the natural minor. Grade 2: G melodic minor, hands separately only. Grade 3: C melodic minor, hands separately and together. The fingering is the same as the natural minor\'s.', '가락 단음계는 올라갈 때 6도와 7도를 올리고, 내려올 때는 자연 단음계예요. 2급: G 가락 단음계, 한 손씩만. 3급: C 가락 단음계, 한 손씩 그리고 양손 함께. 손가락 번호는 자연 단음계와 같아요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:6,width:'100%',maxWidth:520,margin:'0 auto'}}><ScfMelRow m="Gm" dir="up"/><ScfMelRow m="Gm" dir="down"/></div></LbPic>} live={<ScfMelPad/>}/>
      <LbSay>{LANG === 'ko' ? <>올라갈 때는 <b>6도와 7도를 반음씩 올려요</b>: G단조에서 E와 F♯. 내려올 때는 <b>자연 단음계</b>: F와 E♭.</> : <>Going up, <b>the 6th and 7th rise a semitone</b>: in G minor, E and F♯. Coming down, <b>the natural minor</b>: F and E♭.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>G 자연 단음계를 한 옥타브 쳐요.</>, <>올라갈 때 E와 F♯로 바꿔요. 내려올 때는 F와 E♭.</>, <>두 옥타브, 한 손씩. 3급은 C 가락 단음계를 양손 함께.</>]
        : [<>Play G natural minor, one octave.</>, <>Going up, change to E and F♯. Coming down, F and E♭.</>, <>Two octaves, each hand. Grade 3: C melodic minor hands together.</>]}/>
      <LbRemember>{t('Up: 6 and 7 rise. Down: natural.', '올라갈 때: 6과 7이 올라가요. 내려올 때: 자연.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Mirror twins, or not?', '거울 쌍둥이일까, 아닐까?')}
      teacher={<>{spTx(t('Contrary motion, two octaves, both hands from one note (the book prints them in unison). Grade 2 at ♩ = 66: G major, E harmonic minor, F major, D harmonic minor. Grade 3 at 80: D major, B harmonic minor, B♭ major, G harmonic minor. Each hand keeps its own scale fingering: in G, D, E minor, D minor and G minor the numbers mirror all the way (mirror twins); in F, B♭ and B minor they don\'t, and the hands turn at different times.', '반대 방향, 두 옥타브, 두 손이 한 음에서(책은 같은 음에서 시작). 2급 ♩ = 66: G장조, E 화성 단음계, F장조, D 화성 단음계. 3급 80: D장조, B 화성 단음계, B♭장조, G 화성 단음계. 손마다 자기 스케일 번호를 지켜요: G, D, E단조, D단조, G단조는 끝까지 같은 번호(거울 쌍둥이); F, B♭, B단조는 달라서 두 손이 다른 때에 넘어가요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={160}><div style={{display:'grid',gridTemplateColumns:'1fr',gap:16,width:'100%',maxWidth:scr ? 440 : 560,margin:'0 auto'}}><div><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('D')} · {t('mirror twins', '거울 쌍둥이')}</div><ScfCmKb k="D" W={scr ? 20 : 30} H={scr ? 66 : 84}/></div><div><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('Bb')} · {t('not mirror twins', '거울 쌍둥이 아님')}</div><ScfCmKb k="Bb" W={scr ? 20 : 30} H={scr ? 66 : 84} mark={scfFirstDiff('Bb')}/></div></div></LbPic>} live={<ScfMirrorPad/>}/>
      <LbSay>{LANG === 'ko' ? <>반대 방향에서 <b>손마다 자기 번호</b>를 써요. D장조는 번호가 끝까지 같아서 <b>거울 쌍둥이</b>. B♭장조는 다섯째 음부터 달라요.</> : <>In contrary motion <b>each hand uses its own numbers</b>. In D major they match all the way: <b>mirror twins</b>. In B♭ major they part at the fifth note.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>두 손을 같은 음에 놓아요. 오른손은 위로, 왼손은 아래로.</>, <>번호가 달라지는 곳에서 멈춰서 확인해요.</>, <>메트로놈 66(2급), 80(3급). 한 박에 두 음.</>]
        : [<>Both hands on the same note. The right hand goes up, the left hand down.</>, <>Stop where the numbers part, and check.</>, <>Metronome 66 (Grade 2), 80 (Grade 3). Two notes a beat.</>]}/>
      <LbRemember>{t('Each hand keeps its own numbers.', '손마다 자기 번호를 지켜요.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Chromatic from any note', '어느 음에서든 반음계')}
      teacher={<>{spTx(t('Two octaves, ♩ = 84 two notes a beat: Grade 2 from D, hands separately; Grade 3 from A and from D♯/E♭ at 92, hands separately and together (written with sharps going up, flats coming down). The book\'s fingering follows one pattern: 3 on every black key, 1 on white keys, 2 on the right hand\'s F and C and the left hand\'s E and B; the left hand may start and end on 4. Hands together, the 3s always land together.', '두 옥타브, ♩ = 84에 한 박에 두 음: 2급은 D에서 한 손씩; 3급은 A와 D♯/E♭에서 92로 한 손씩 그리고 양손 함께(올라갈 때 샵, 내려올 때 플랫). 책의 운지는 한 가지 규칙: 검은건반 3, 흰건반 1, 오른손 F와 C, 왼손 E와 B는 2. 왼손은 처음과 끝을 4번으로 해도 돼요. 양손 함께면 3번은 언제나 같이 떨어져요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:600,margin:'0 auto'}}>{chromStill()}</div></LbPic>} live={<ScfChromPad/>}/>
      <LbSay>{LANG === 'ko' ? <><b>검은건반은 3번</b>, <b>흰건반은 1번</b>, <b>흰건반 둘이 붙은 곳은 2번</b>: 오른손은 F와 C, 왼손은 E와 B. 이 규칙이면 어느 음에서든 시작해요.</> : <><b>3 on black</b>, <b>1 on white</b>, <b>2 where two white keys sit together</b>: the right hand's F and C, the left hand's E and B. With this rule you can start anywhere.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>D에서 오른손, 한 옥타브. 3번이 검은건반에만 가는지 봐요.</>, <>왼손도. E와 B에서 2번.</>, <>두 옥타브. 3급은 A와 E♭에서, 양손 함께: 3번이 같이 떨어져요.</>]
        : [<>From D, right hand, one octave. Check that 3 only ever plays black keys.</>, <>Left hand too: 2 on E and B.</>, <>Two octaves. Grade 3: from A and E♭, hands together: the 3s land together.</>]}/>
      <LbRemember>{t('3 on black, 1 on white, 2 where two whites sit together.', '검은건반 3, 흰건반 1, 흰건반 둘이 붙은 곳 2.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one played to you, from memory, in the keys of the child\'s grade (the teacher\'s copy lists them). Listen for the turns: an even run-ning through every thumb.', '하나씩 외워서, 아이의 급의 조로 들려줘요(선생님용에 목록). 넘기는 곳을 들어 주세요: 엄지마다 티-티가 고르게.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_scf_five"/>}/>
    </LbPage>,
  ];
}
function Scales23LessonBook() { return <>{scfLbPages(false)}</>; }
function ScfLearn({ onStart }) {
  const pages = scfLbPages(true), opener = pages[0];
  return (
    <Lesson id="scales-23" title={t('Scales Further', '스케일 한 걸음 더')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scales-23"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const SCF_LEVELS = [
  { n: 1, label: 'Which finger? Grades 2–3 scales', kind: 'thumb', time: 15 },
  { n: 2, label: 'Hands together: where do the thumbs meet?', kind: 'meet', time: 15 },
  { n: 3, label: 'The melodic minor, up and down', kind: 'mel', time: 15 },
  { n: 4, label: 'Contrary motion: mirror twins or not?', kind: 'mirror', time: 15 },
  { n: 5, label: 'Chromatic from any note: which finger?', kind: 'chrom', time: 12 },
];
Object.assign(LEVEL_KO, { 'Which finger? Grades 2–3 scales': '몇 번 손가락? 2·3급 스케일', 'Hands together: where do the thumbs meet?': '양손 함께: 엄지는 어디서 만날까?', 'The melodic minor, up and down': '가락 단음계, 올라갈 때와 내려올 때', 'Contrary motion: mirror twins or not?': '반대 방향: 거울 쌍둥이일까?', 'Chromatic from any note: which finger?': '어느 음에서든 반음계: 몇 번 손가락?' });
function genScfQuestion(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'thumb') { let k, h, j, g = 0; do { k = pick(SCF_KEYS); h = Math.random() < 0.5 ? 'R' : 'L'; j = Math.floor(Math.random() * 7); } while (prev && prev.key === k + h + j && g++ < 10);
    return { kind, k, h, j, answer: SCF[k][h][j], choices: [1, 2, 3, 4, 5], key: k + h + j, uid }; }
  if (kind === 'meet') { let k, g = 0; do { k = pick(SCF_KEYS); } while (prev && prev.key === 'm' + k && g++ < 10); return { kind, k, answer: scfMeetKind(k), choices: ['tonic', 'tonic4', 'never'], key: 'm' + k, uid }; }
  if (kind === 'mel') { let m, dir, g = 0; do { m = Math.random() < 0.5 ? 'Gm' : 'Cm'; dir = Math.random() < 0.6 ? 'up' : 'down'; } while (prev && prev.key === m + dir && g++ < 10);
    return { kind, m, dir, answer: dir === 'up' ? 'mel' : 'nat', choices: ['mel', 'nat', 'har'], key: m + dir, uid }; }
  if (kind === 'mirror') { let k, g = 0; do { k = pick(SCF_CM_KEYS); } while (prev && prev.key === 'c' + k && g++ < 10); return { kind, k, answer: scfMirror(k) ? 'yes' : 'no', choices: ['yes', 'no'], key: 'c' + k, uid }; }
  let st, h, j, g = 0; do { st = Math.floor(Math.random() * 3); h = Math.random() < 0.5 ? 'R' : 'L'; j = 1 + Math.floor(Math.random() * 11); } while (prev && prev.key === 'h' + st + h + j && g++ < 10);
  const i = SCF_CHROM[st][1] + j; return { kind: 'chrom', st, h, j, i, answer: scfChF(i, h, false), choices: [1, 2, 3], key: 'h' + st + h + j, uid };
}
const scfMelPair = (m, c) => { const x = SCF_MEL[m]; return c === 'mel' ? x.up[5] + ' ' + x.up[6] : c === 'nat' ? x.dn[2] + ' ' + x.dn[1] : x.dn[2] + ' ' + x.up[6]; };
function scfAnswerLabel(q) {
  if (q.kind === 'meet') return t(SCF_MEET_LAB[q.answer][0], SCF_MEET_LAB[q.answer][1]);
  if (q.kind === 'mel') return scfMelPair(q.m, q.answer);
  if (q.kind === 'mirror') return q.answer === 'yes' ? t('mirror twins', '거울 쌍둥이') : t('not mirror twins', '거울 쌍둥이 아님');
  return t('finger ' + q.answer, q.answer + '번');
}
function ScfQuestion({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; onAnswer(c); };
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  let title, body;
  if (q.kind === 'thumb') { const K = scfKeys(q.k, 1), F = SCF[q.k][q.h], nums = {}; K.forEach((x, j) => { if (j !== q.j) nums[x] = F[j]; }); const lit = {}; K.forEach(x => { lit[x] = 'pale'; }); lit[K[q.j]] = done ? (given.ans === q.answer ? 'good' : 'bad') : 'cor'; if (done) nums[K[q.j]] = F[q.j];
    title = t(scfName(q.k) + ', ' + spHand(q.h).toLowerCase() + ': which finger plays ' + scfNames(q.k, 1)[q.j] + '?', scfName(q.k) + ', ' + spHand(q.h) + ': ' + scfNames(q.k, 1)[q.j] + '은 몇 번?');
    body = <><SpKb lo={SCF[q.k].r} hi={SCF[q.k].r + 12} W={28} H={78} lit={lit} names={{ [K[q.j]]: scfNames(q.k, 1)[q.j] }} up={q.h === 'R' ? nums : {}} dn={q.h === 'L' ? nums : {}}/>{grid(5, [1, 2, 3, 4, 5].map(c => [c, String(c)]))}</>; }
  else if (q.kind === 'meet') { title = t(scfName(q.k) + ', two octaves hands together: where do both thumbs play together?', scfName(q.k) + ', 두 옥타브 양손 함께: 두 엄지가 함께 치는 곳은?');
    body = <>{done && <ScfStrip k={q.k} found={scfMeet(q.k)}/>}{grid(1, q.choices.map(c => [c, t(SCF_MEET_LAB[c][0], SCF_MEET_LAB[c][1])]))}</>; }
  else if (q.kind === 'mel') { const x = SCF_MEL[q.m]; title = t(x.en + ', going ' + q.dir + ': the 6th and the 7th are…', x.ko + ', ' + (q.dir === 'up' ? '올라갈 때' : '내려올 때') + ': 6도와 7도는…');
    body = <>{done && <><ScfMelRow m={q.m} dir="up"/><ScfMelRow m={q.m} dir="down"/></>}{grid(3, q.choices.map(c => [c, scfMelPair(q.m, c)]))}</>; }
  else if (q.kind === 'mirror') { title = t('Contrary motion, ' + scfCmName(q.k) + ': mirror twins?', '반대 방향, ' + scfCmName(q.k) + ': 거울 쌍둥이일까?');
    body = <><ScfCmKb k={q.k} mark={done && q.answer === 'no' ? scfFirstDiff(q.k) : -1}/>{grid(2, [['yes', t('Mirror twins', '거울 쌍둥이')], ['no', t('Not mirror twins', '거울 쌍둥이 아님')]])}</>; }
  else { const s0 = SCF_CHROM[q.st][1], K = Array.from({ length: 13 }, (_, j) => s0 + j), nums = {}, lit = {}; K.forEach((x, j) => { if (j < q.j) nums[x] = scfChF(x, q.h, j === 0); }); lit[q.i] = done ? (given.ans === q.answer ? 'good' : 'bad') : 'cor'; if (done) nums[q.i] = q.answer;
    title = t('Chromatic from ' + SCF_CHROM[q.st][0] + ', ' + spHand(q.h).toLowerCase() + ': which finger plays ' + scfChLet(q.i) + '?', SCF_CHROM[q.st][0] + '에서 반음계, ' + spHand(q.h) + ': ' + scfChLet(q.i) + '은 몇 번?');
    body = <><SpKb lo={s0} hi={s0 + 12} W={28} H={78} lit={lit} names={{ [K[0]]: scfChLet(K[0]).split('/')[0] }} up={q.h === 'R' ? nums : {}} dn={q.h === 'L' ? nums : {}}/>{grid(3, [1, 2, 3].map(c => [c, String(c)]))}</>; }
  const why = !done || pixel ? null : q.kind === 'thumb' ? t(spHand(q.h) + ': ' + SCF[q.k][q.h].slice(0, 8).join(' ') + '. The thumb plays only white keys.', spHand(q.h) + ': ' + SCF[q.k][q.h].slice(0, 8).join(' ') + '. 엄지는 흰건반만.')
    : q.kind === 'chrom' ? (spIsW(q.i) ? t(q.answer === 2 ? 'Two white keys sit together here: 2.' : 'A white key: 1.', q.answer === 2 ? '흰건반 둘이 붙은 곳: 2번.' : '흰건반: 1번.') : t('A black key: always 3.', '검은건반: 언제나 3번.'))
    : q.kind === 'mel' ? t(q.dir === 'up' ? 'Going up, the 6th and 7th rise.' : 'Coming down, the natural minor.', q.dir === 'up' ? '올라갈 때는 6도와 7도가 올라가요.' : '내려올 때는 자연 단음계.') : null;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
    {why && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(SCALES_23_DRILL, { levels: SCF_LEVELS, generate: genScfQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: scfAnswerLabel, Question: ScfQuestion, Learn: ScfLearn });
// the teacher's copy: the keys and speeds for each grade, and what to listen for (the Workbook comes in the next build)
function ScfTeacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scales-23" teacher>{content}</WbPage>);
  const fing = (k) => SCF[k].en + ': RH ' + SCF[k].R.slice(0, 8).join(' ') + ' · LH ' + SCF[k].L.slice(0, 8).join(' ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scales-23')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>{spTx('The keys, speeds and fingerings are the technical work book\'s (Grade 2 pp36–39, Grade 3 pp47–50). All scales two octaves, mf, clear even legato, from memory, two notes a beat. Another fingering is fine if it is logical and systematic.')}</div>
    <TcBlock page={2} title="Start on a black key" answers={<>{tcAns('GRADE 2', [fing('D'), fing('Bm'), fing('Bb'), fing('Gm')])}{tcAns('GRADE 3', [fing('A'), fing('Fsm'), fing('Eb'), fing('Cm')])}</>}
      watch="A thumb on a black key, or B♭ and E♭ started on the thumb. Find the two thumb keys first, then fill in the rest."
      say="“Black key first? Finger 2, then the thumb on the first white key.”"/>
    <TcBlock page={3} title="Where the thumbs meet" answers={<>{tcAns(spTx('SIMILAR MOTION, HANDS SEPARATELY AND TOGETHER: GRADE 2 ♩ = 84, GRADE 3 ♩ = 92'), ['Grade 2: D major; B natural and harmonic minor; B♭ major; G natural and harmonic minor; G melodic minor (hands separately only)', 'Grade 3: A major; F♯ natural and harmonic minor; E♭ major; C natural, harmonic and melodic minor', 'Thumbs together: middle keynote only in D, A, G minor, C minor · B and E in B minor · never in B♭, E♭, F♯ minor'])}</>}
      watch="A bump at each turn where the thumbs don't meet. Practise the three notes around each turn, hands together."
      say="“The thumbs never meet? Each hand turns on its own: keep it even.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="The melodic minor" answers={<>{tcAns('UP / DOWN', ['G: G A B♭ C D E F♯ G / G F E♭ D C B♭ A G (Grade 2, hands separately)', 'C: C D E♭ F G A B C / C B♭ A♭ G F E♭ D C (Grade 3, hands separately and together)'])}</>}
      watch="The raised notes kept on the way down, or the 6th forgotten going up (that is the harmonic minor)."
      say="“Up: 6 and 7 rise. Down: natural.”"/>
    <TcBlock page={5} title="Mirror twins, or not?" answers={<>{tcAns(spTx('CONTRARY MOTION FROM ONE NOTE: GRADE 2 ♩ = 66, GRADE 3 ♩ = 80'), ['Grade 2: G major (mirror), E harmonic minor (mirror), F major (not: RH 1 2 3 4 1 2 3 1, LH 1 2 3 1 2 3 4 1), D harmonic minor (mirror)', 'Grade 3: D major (mirror), B harmonic minor (not: LH 1 2 3 4 1 2 3 1), B♭ major (not: RH 2 1 2 3 1 2 3 4, LH 2 1 2 3 4 1 2 3), G harmonic minor (mirror)'])}</>}
      watch="The left hand copying the right hand's numbers in F, B♭ or B minor. Each hand keeps its own scale fingering."
      say="“Each hand keeps its own numbers.”"/>
    <TcBlock page={6} title="Chromatic from any note" answers={<>{tcAns(spTx('TWO OCTAVES, TWO NOTES A BEAT'), ['Grade 2: from D, hands separately, ♩ = 84', 'Grade 3: from A and from D♯/E♭, hands separately and together, ♩ = 92', 'RH 3 on black, 1 on white, 2 on F and C · LH 3 on black, 1 on white, 2 on E and B; the LH may start and end on 4'])}</>}
      watch="2 and 3 swapped on the white keys either side of E–F or B–C. Hands together: the 3s land together."
      say="“3 on black, 1 on white, 2 where two whites sit together.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one played to you from memory, in the keys of the child's grade, at the grade's speed. Listen for an even run-ning through every turn.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['scales-23'] = ScfTeacher;
'''
rep("""TEACHER_COPIES['listen-23'] = L2Teacher;""", """TEACHER_COPIES['listen-23'] = L2Teacher;""" + CH)

HOME = r'''
// ══ Build AK: Scales Further on the Home (Technique, after Playing scales) ══
LBH_FN['scales-23'] = (s) => scfLbPages(s);
const scfHomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('scales-23', i, { make }));
const scfMeetQ = (n, prev) => { let k, g = 0; do { k = pick(SCF_KEYS); } while (prev && prev.key === k && g++ < 10); const a = scfMeetKind(k);
  return { kind: 'choice', cols: 1, key: k, prompt: [SCF[k].en + ', hands together: where do both thumbs play together?', SCF[k].ko + ', 양손 함께: 두 엄지가 함께 치는 곳은?'], opts: ['tonic', 'tonic4', 'never'].map(x => ({ id: x, label: () => t(SCF_MEET_LAB[x][0], SCF_MEET_LAB[x][1]) })), ans: a, ok: (v) => v === a,
    fig: (c) => ({ mid: c.res ? <ScfStrip k={k} found={scfMeet(k)}/> : null }), yes: ['Yes: ' + SCF_MEET_LAB[a][0].toLowerCase() + '.', '맞아요: ' + SCF_MEET_LAB[a][1] + '.'], no: [SCF_MEET_LAB[a][0] + ': look for a 1 above and a 1 below.', SCF_MEET_LAB[a][1] + ': 위에도 1, 아래에도 1인 곳.'] }; };
const scfMirrorQ = (n, prev) => { let k, g = 0; do { k = pick(SCF_CM_KEYS); } while (prev && prev.key === k && g++ < 10); const a = scfMirror(k) ? 'yes' : 'no';
  return { kind: 'choice', cols: 2, key: k, prompt: ['Contrary motion, ' + SCF_CM[k].en + ': mirror twins?', '반대 방향, ' + SCF_CM[k].ko + ': 거울 쌍둥이일까?'], opts: [{ id: 'yes', label: () => t('Mirror twins', '거울 쌍둥이') }, { id: 'no', label: () => t('Not mirror twins', '거울 쌍둥이 아님') }], ans: a, ok: (v) => v === a,
    fig: (c) => ({ mid: <ScfCmKb k={k} mark={c.res && a === 'no' ? scfFirstDiff(k) : -1}/> }), yes: a === 'yes' ? ['Yes: the same numbers all the way.', '맞아요: 끝까지 같은 번호.'] : ['Yes: each hand keeps its own numbers.', '맞아요: 손마다 자기 번호.'], no: a === 'yes' ? ['Look again: the numbers match all the way.', '다시 봐요: 끝까지 같은 번호예요.'] : ['Look again: the coral keys have different numbers.', '다시 봐요: 빨간 건반의 번호가 달라요.'] }; };
scfHomeAdd('scf-thumb', 1, 'Start on a black key', '검은건반에서 시작', 'Finger 2 first; the thumb on the first white key.', '먼저 2번, 첫 흰건반에 엄지.', lwTapQ(ScfThumbPad, (n) => ({ fixed: { k: SCF_KEYS[(n * 3) % SCF_KEYS.length], h: n % 2 ? 'L' : 'R' } }), ['Tap every key the thumb plays in one octave.', '한 옥타브에서 엄지가 치는 건반을 모두 눌러요.'], ['Thumbs found ✓', '엄지 자리 찾았어요 ✓']));
scfHomeAdd('scf-meet', 2, 'Where the thumbs meet', '엄지가 만나는 곳', 'On the keynote, in two places, or never.', '으뜸음에서, 두 곳에서, 아니면 한 번도.', scfMeetQ);
scfHomeAdd('scf-mel', 3, 'The melodic minor', '가락 단음계', 'Up: the 6th and 7th rise. Down: natural.', '올라갈 때 6도와 7도가 올라가요. 내려올 때는 자연.', lwTapQ(ScfMelPad, (n) => ({ fixed: n % 2 ? 'Cm' : 'Gm' }), ['Tap the two notes that change going up.', '올라갈 때 바뀌는 두 음을 눌러요.'], ['Up and down ✓', '올라갔다 내려오기 ✓']));
scfHomeAdd('scf-mirror', 4, 'Mirror twins, or not?', '거울 쌍둥이일까, 아닐까?', 'Contrary motion: each hand keeps its own numbers.', '반대 방향: 손마다 자기 번호.', scfMirrorQ);
scfHomeAdd('scf-chrom', 5, 'Chromatic from any note', '어느 음에서든 반음계', '3 on black, 1 on white, 2 where two whites sit together.', '검은건반 3, 흰건반 1, 흰건반 둘이 붙은 곳 2.', lwTapQ(ScfChromPad, (n) => ({ fixed: { st: n % 3, h: n % 2 ? 'L' : 'R' } }), ['Choose the finger for each coral key.', '빨간 건반마다 손가락을 골라요.'], ['All 13 ✓', '13개 모두 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""const LESSON_BOOKS = { 'listen-23': Listen23LessonBook,""", """const LESSON_BOOKS = { 'scales-23': Scales23LessonBook, 'listen-23': Listen23LessonBook,""")
rep("""const LB_PAGE_FNS = { 'listen-23': l2LbPages,""", """const LB_PAGE_FNS = { 'scales-23': scfLbPages, 'listen-23': l2LbPages,""")
rep("""const HOUSE_ICONS = {"listen-23": """, """const HOUSE_ICONS = {"scales-23": "<path d=\\"M4 31 H12 V25 H20 V19 H28 V13 H36 V7 H44\\"/><rect x=\\"9\\" y=\\"30\\" width=\\"7\\" height=\\"11\\" rx=\\"1.5\\" fill=\\"#26296b\\"/><text x=\\"30\\" y=\\"41\\" font-size=\\"12\\" font-weight=\\"900\\" fill=\\"#e4572e\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">2</text>", "listen-23": """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
