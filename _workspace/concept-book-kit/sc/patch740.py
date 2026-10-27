import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BU (board call 26, the second Grade 7 room): Scales, Grade 7, from the technical work book (Grade 7 pp48-53, read 28 Oct):
# the abbreviated grand scale in D major, B harmonic minor, A♭ major and F harmonic minor (four octaves, mf, ♩ = 80); polyrhythmic
# scales, three against two, D major and B harmonic minor (right hand three octaves, left hand two, legato, mf, ♩ = 80); contrary
# motion, F♯ major and D♯ harmonic minor (two octaves, ♩ = 80); chromatic scales from D and from G♯/A♭ (four octaves, three
# ways, ♩ = 104) and from E♭ with fingers 3, 4 and 5 (two octaves, hands separately, ♩ = ca 84, two notes a beat); and the skills
# of exercises 7B (two voices played by one hand) and 7C (octaves in the Lydian mode). The thing to make: a mode jam over a drone.

rep("""const SCALES_6_DRILL = {""", """const SCALES_7_DRILL = { id: 'scales-7', label: 'Scales, Grade 7' };   // Build BU
const SCALES_6_DRILL = {""")
rep("""  { id: 'scales-6', label: 'Scales, Grade 6',""", """  { id: 'scales-7', label: 'Scales, Grade 7', concept: SCALES_7_DRILL, track: 'start' },   // Build BU
  { id: 'scales-6', label: 'Scales, Grade 6',""")
rep("""'scales-6': ['scales-5']""", """'scales-6': ['scales-5'], 'scales-7': ['scales-6']""")
rep("""'scales-6': ['Scales 6', '스케일 6']""", """'scales-6': ['Scales 6', '스케일 6'], 'scales-7': ['Scales 7', '스케일 7']""")

CH = r'''
// ─── Chapter: Scales, Grade 7 (Build BU, 2026-10-28; board call 26, the second Grade 7 room) ───
// ── step 1: the grand scale in the four Grade 7 keys (the right hand's first note; the left hand an octave lower) ──
Object.assign(S6_GR, {
  D7: { en: 'D major', ko: 'D장조', st: SP_MAJ, r: -10, nm: ['D', 'E', 'F♯', 'G', 'A', 'B', 'C♯'] },
  Bmh7: { en: 'B harmonic minor', ko: 'B 화성 단음계', st: SP_HAR, r: -13, nm: ['B', 'C♯', 'D', 'E', 'F♯', 'G', 'A♯'] },
  Ab7: { en: 'A♭ major', ko: 'A♭장조', st: SP_MAJ, r: -16, nm: ['A♭', 'B♭', 'C', 'D♭', 'E♭', 'F', 'G'] },
  Fmh7: { en: 'F harmonic minor', ko: 'F 화성 단음계', st: SP_HAR, r: -7, nm: ['F', 'G', 'A♭', 'B♭', 'C', 'D♭', 'E'] },
});
const S7_GR_KEYS = ['D7', 'Bmh7', 'Ab7', 'Fmh7'];
const s7GrMinor = (k) => S6_GR[k].st === SP_HAR;
function S7GrandPad({ onResult, fixed, keys = S7_GR_KEYS, bpm = 80, note, title }) {
  const T = useSpTimers();
  const [k, setK] = useState(fixed ? fixed.k : keys[0]), [cur, setCur] = useState(-1), [quiz, setQuiz] = useState(!!fixed), [ans, setAns] = useState(null);
  const run = (kk, only) => { T.clear(); setCur(-1); const r = grPlay(kk, only, bpm); if (!r.run) return; r.ix.forEach((i, n) => T.at(r.run.ms(n / 4), () => setCur(i))); T.at(r.run.ms(r.ix.length / 4 + 1), () => setCur(-1)); };
  const ask = () => { let x, g = 0; do { x = pick(keys); } while (x === k && g++ < 10); setK(x); setQuiz(true); setAns(null); run(x, 0); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === (s7GrMinor(k) ? 'm' : 'M') }); };
  const show = !quiz || ans, c = S6_GR[k];
  return (
    <div className="try-box" style={actBox} data-s7="grand">
      <div style={actTitle}>{title || t('The grand scale in four new keys', '네 새 조의 그랜드 스케일')}</div>
      <div style={actNote}>{note || (LANG === 'ko' ? <>6급과 같은 길: <b>함께 올라가고, 멀어지고, 다시 모이고, 함께 내려와요</b>. 7급의 조는 넷: D장조와 그 나란한 B 화성 단음계, A♭장조와 그 나란한 F 화성 단음계. {spMM(80)}, 한 박에 네 음, mf. 화성 단음계는 7음을 올려서 <b>위쪽에 넓은 걸음</b>(증2도)이 있어요.</>
        : <>The same route as Grade 6: <b>together up, apart, back together, together down</b>. Grade 7 has four keys: D major and its relative, B harmonic minor; A♭ major and its relative, F harmonic minor. {spMM(80)}, four notes a beat, mf. The harmonic minor raises its 7th, so near the top of each octave there is <b>one wide step</b> (an augmented 2nd).</>)}</div>
      {!quiz && spChips(keys.map(x => [x, t(S6_GR[x].en, S6_GR[x].ko)]), k, (x) => { T.clear(); setCur(-1); setK(x); })}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>{show ? t(c.en, c.ko) + ' · ' + c.nm.join(' ') : t('Major or harmonic minor?', '장조? 화성 단음계?')}</div>
      <GrRoute k={k} cur={cur}/>
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{[['M', t('Major', '장조')], ['m', t('Harmonic minor', '화성 단음계')]].map(([v, lab]) => <button key={v} className="choice-btn" onClick={() => say(v)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}}>{lab}</button>)}</div>}
      {spMsg(ans ? ((ans === 'm') === s7GrMinor(k) ? t('Yes: ' + c.en + '.', '맞아요: ' + c.ko + '.') : t('It was ' + c.en + (s7GrMinor(k) ? ': listen for the wide step near the top.' : ': no wide step, only tones and semitones.'), '정답은 ' + c.ko + (s7GrMinor(k) ? ': 위쪽의 넓은 걸음을 들어 봐요.' : ': 넓은 걸음 없이 온음과 반음만.'))) : quiz ? t('Part 1, together up: major or harmonic minor?', '1부분, 함께 올라가요: 장조? 화성 단음계?') : '', ans ? ((ans === 'm') === s7GrMinor(k) ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => run(k, quiz && !ans ? 0 : null)}>{quiz && !ans ? t('♪ Again', '♪ 다시') : t('▶ The whole grand scale', '▶ 그랜드 스케일 전체')}</button>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Major or minor?', '▶ 장조? 단조?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setCur(-1); setQuiz(false); setAns(null); }}>{t('Back to the four keys', '네 조 다시 보기')}</button>}
      </div>
    </div>
  );
}
// ── step 2: three against two as a scale: the right hand three octaves in triplets, the left hand two octaves in quavers ──
const S7_PS = { D: { en: 'D major', ko: 'D장조', st: SP_MAJ, rh: 2, lh: -10, rO: 3, lO: 2, rP: 3, lP: 2 }, Bmh: { en: 'B harmonic minor', ko: 'B 화성 단음계', st: SP_HAR, rh: -1, lh: -13, rO: 3, lO: 2, rP: 3, lP: 2 } };
const psPer = (k, h) => (h === 'R' ? S7_PS[k].rP : S7_PS[k].lP);
const psSeq = (k, h) => { const c = S7_PS[k], r0 = h === 'R' ? c.rh : c.lh, n = 7 * (h === 'R' ? c.rO : c.lO), deg = (o) => r0 + 12 * Math.floor(o / 7) + c.st[((o % 7) + 7) % 7];
  const up = Array.from({ length: n + 1 }, (_, j) => deg(j)); return up.concat(up.slice(0, -1).reverse()); };
const psPlay = (k, bpm = 80, only = null) => { const ev = []; ['R', 'L'].forEach(h => { if (only && only !== h) return; const S = psSeq(k, h), per = psPer(k, h); S.forEach((x, j) => ev.push({ at: j / per, keys: [x], len: j === S.length - 1 ? 1.4 : 1 / per, vol: 0.12 })); });
  return spPlay(ev, bpm, 2); };
function PsRoute({ k, beat = -1, w = 340 }) {
  const R = psSeq(k, 'R'), L = psSeq(k, 'L'), lo = Math.min(...L), hi = Math.max(...R), X = (b) => 14 + b / 14 * 312, Y = (v) => 100 - (v - lo) / (hi - lo) * 86;
  const path = (A, per, c) => '<path d="' + A.map((v, j) => (j ? 'L' : 'M') + X(j / per).toFixed(1) + ' ' + Y(v).toFixed(1)).join(' ') + '" fill="none" stroke="' + c + '" stroke-width="2.4" stroke-linejoin="round"/>';
  let svg = ''; for (let b = 0; b <= 14; b++) svg += '<path d="M' + X(b).toFixed(1) + ' 112 V116" stroke="#26296b" stroke-width="1.2"/>';
  svg += '<path d="M' + X(7).toFixed(1) + ' 8 V112" stroke="rgba(38,41,107,0.25)" stroke-dasharray="3 3"/>' + path(L, psPer(k, 'L'), '#26296b') + path(R, psPer(k, 'R'), '#e4572e');
  svg += '<text x="' + X(3.5).toFixed(1) + '" y="128" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="900" fill="#26296b">' + t('7 beats up', '7박 올라가요') + '</text><text x="' + X(10.5).toFixed(1) + '" y="128" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="900" fill="#26296b">' + t('7 beats down', '7박 내려와요') + '</text>';
  if (beat >= 0) svg += '<path d="M' + X(beat).toFixed(1) + ' 6 V112" stroke="#e4572e" stroke-width="2"/>';
  return <svg viewBox="0 0 340 132" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t('Three octaves against two', '세 옥타브 대 두 옥타브')} dangerouslySetInnerHTML={{ __html: svg }}/>;
}
function S7PolyScalePad({ onResult, fixed, keys = ['D', 'Bmh'], bpm = 80, note, title }) {
  const T = useSpTimers();
  const [k, setK] = useState(keys[0]), [beat, setBeat] = useState(-1), [guess, setGuess] = useState(null);
  const go = (bpm, only = null) => { T.clear(); setBeat(-1); const r = psPlay(k, bpm, only); if (!r) return; for (let b = 0; b <= 14; b++) T.at(r.ms(b), () => setBeat(b)); T.at(r.ms(15), () => setBeat(-1)); };
  const say = (v) => { if (guess) return; setGuess(v); if (onResult) onResult({ ok: v === 'B' }); go(bpm); };
  return (
    <div className="try-box" style={actBox} data-s7="poly">
      <div style={actTitle}>{title || t('Three against two, as a scale', '3 대 2, 스케일로')}</div>
      <div style={actNote}>{note || (LANG === 'ko' ? <>오른손은 <b>한 박에 셋</b>(셋잇단)으로 <b>세 옥타브</b>, 왼손은 <b>한 박에 둘</b>로 <b>두 옥타브</b>. 위의 줄이 오른손, 아래 줄이 왼손. {spMM(80)}, 레가토, mf.</> : <>The right hand plays <b>three a beat</b> (triplets) over <b>three octaves</b>; the left hand <b>two a beat</b> over <b>two octaves</b>. The top line is the right hand, the bottom the left. {spMM(80)}, legato, mf.</>)}</div>
      {keys.length > 1 && spChips(keys.map(x => [x, t(S7_PS[x].en, S7_PS[x].ko)]), k, (x) => { T.clear(); setBeat(-1); setK(x); setGuess(null); })}
      <PsRoute k={k} beat={beat}/>
      {!guess ? <><div style={{textAlign:'center',fontSize:14.5,fontWeight:900,color:BK.ink,margin:'6px 0 4px'}}>{t('Guess first: which hand reaches the top first?', '먼저 맞혀 봐요: 어느 손이 꼭대기에 먼저 닿을까요?')}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6}}>{[['R', t('Right hand', '오른손')], ['L', t('Left hand', '왼손')], ['B', t('Together', '함께')]].map(([v, lab]) => <button key={v} className="choice-btn" onClick={() => say(v)} style={{padding:'11px 2px',fontSize:14,fontWeight:900}}>{lab}</button>)}</div></>
        : spMsg((guess === 'B' ? t('Yes! ', '맞아요! ') : t('Listen… ', '들어 봐요… ')) + t(S7_PS[k].rO + ' octaves at ' + S7_PS[k].rP + ' a beat and ' + S7_PS[k].lO + ' octaves at ' + S7_PS[k].lP + ' a beat take the same 7 beats: the hands meet at the top, and again at the bottom.', '한 박에 ' + S7_PS[k].rP + '으로 ' + S7_PS[k].rO + '옥타브, 한 박에 ' + S7_PS[k].lP + '로 ' + S7_PS[k].lO + '옥타브: 둘 다 7박이라 두 손이 꼭대기에서, 그리고 맨 아래에서 다시 만나요.'), guess === 'B' ? BK.green : BK.ink)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => go(50)}>{t('▶ Slowly', '▶ 천천히')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => go(bpm)}>{t('▶ At ♩ = ' + bpm, '▶ ♩ = ' + bpm + '으로')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => go(50, 'R')}>{t('▶ Right only', '▶ 오른손만')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => go(50, 'L')}>{t('▶ Left only', '▶ 왼손만')}</button>
      </div>
    </div>
  );
}
// ── step 3: contrary motion in F♯ major and D♯ harmonic minor (the book's first octaves, Grade 7 p51) ──
Object.assign(SCF_CM, {
  Fs7: { g: 7, en: 'F♯ major', ko: 'F♯장조', st: SP_MAJ, s: 6, nm: ['F♯', 'G♯', 'A♯', 'B', 'C♯', 'D♯', 'E♯'], R: [2, 3, 4, 1, 2, 3, 1, 2], L: [2, 1, 2, 3, 1, 2, 3, 4] },
  Dsmh7: { g: 7, en: 'D♯ harmonic minor', ko: 'D♯ 화성 단음계', st: SP_HAR, s: 3, nm: ['D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B', 'C𝄪'], R: [2, 1, 2, 3, 4, 1, 2, 3], L: [2, 3, 1, 2, 3, 4, 1, 2] },
});
const S7_CM_KEYS = ['Fs7', 'Dsmh7'];
const s7CmChip = (k) => ({ Fs7: 'F♯', Dsmh7: 'D♯m' })[k];
function S7MirrorPad(p) { return <S4MirrorPad keys={S7_CM_KEYS} chip={s7CmChip} bpm={80} g={7} {...p}/>; }
// ── step 4: the chromatic scale from D and from G♯/A♭, four octaves, hands together ──
const S7_CH = [['D', 2], ['G♯/A♭', 8]];
function S7ChromPad(p) { return <S4ChromPad set={S7_CH} bpm={104} g={7} {...p}/>; }
// ── step 5: the chromatic scale from E♭ with fingers 3, 4 and 5: every black key 3; the white keys 4, except the outer note of
// each pair of white keys (the right hand's F and C, the left hand's E and B), which takes 5 ──
const c345 = (x, h) => { const pc = spPc(x); if ([1, 3, 6, 8, 10].includes(pc)) return 3; return (h === 'R' ? pc === 5 || pc === 0 : pc === 4 || pc === 11) ? 5 : 4; };
const c345Lo = (h) => (h === 'R' ? 3 : -9);
const c345Play = (h, bpm = 84) => { const a = Array.from({ length: 25 }, (_, j) => (h === 'R' ? 3 + j : -9 - j)), sq = a.concat(a.slice(0, -1).reverse()); return { run: spPlay(sq.map((x, n) => ({ at: n / 2, keys: [x], len: n === sq.length - 1 ? 1.4 : 0.5, vol: 0.13 })), bpm, 2), sq }; };
function S7Ch345Pad({ onResult, fixed }) {
  const T = useSpTimers();
  const [h, setH] = useState(fixed ? fixed.h : 'R'), [found, setFound] = useState([]), [bad, setBad] = useState(null), [miss, setMiss] = useState(0), [pl, setPl] = useState(null);
  const lo = c345Lo(h), K = Array.from({ length: 13 }, (_, j) => lo + j), fives = K.filter(x => c345(x, h) === 5), done = fives.every(x => found.includes(x));
  const reset = (fn) => { T.clear(); setFound([]); setBad(null); setMiss(0); setPl(null); if (fn) fn(); };
  const play = () => { T.clear(); const r = c345Play(h); if (!r.run) return; r.sq.forEach((x, n) => T.at(r.run.ms(n / 2), () => setPl(x))); T.at(r.run.ms(r.sq.length / 2 + 0.5), () => setPl(null)); };
  const tap = (x) => { playKey(x, 0.4); if (done) return; if (fives.includes(x)) { if (found.includes(x)) return; const nf = found.concat([x]); setFound(nf); setBad(null); if (fives.every(y => nf.includes(y))) { if (onResult) onResult({ ok: miss === 0 }); T.at(300, play); } } else { setBad(x); setMiss(m => m + 1); } };
  const nums = {}, lit = {}, act = {}; K.forEach(x => { const f = c345(x, h); if (f !== 5 || found.includes(x) || done) nums[x] = f; if (found.includes(x)) lit[x] = 'good'; });
  if (bad != null) lit[bad] = 'bad'; if (pl != null) { const pp = lo + spPc(pl - lo); if (K.includes(pp)) { lit[pp] = 'cor'; act[pp] = true; act['d' + pp] = true; } }
  return (
    <div className="try-box" style={actBox} data-s7="c345">
      <div style={actTitle}>{t('Chromatic from E♭: fingers 3, 4 and 5', 'E♭ 반음계: 3, 4, 5번')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>엄지 없이! <b>검은건반은 모두 3번</b>, 흰건반은 4번. 그런데 흰건반이 둘 붙은 곳에서는 바깥쪽이 <b>5번</b>. 한 손씩, 두 옥타브, 한 박에 두 음, 약 {spMM(84)}. 고르고 아름다운 소리가 빠르기보다 먼저예요. 5번 자리를 모두 눌러요.</>
        : <>No thumbs! <b>Every black key is 3</b>; the white keys are 4, except where two white keys stand together: the outer one takes <b>5</b>. Hands separately, two octaves, two notes a beat, about {spMM(84)}. An even, lovely tone matters more than speed. Tap every key finger 5 plays.</>}</div>
      {!fixed && spChips([['R', t('Right hand', '오른손')], ['L', t('Left hand', '왼손')]], h, (x) => reset(() => setH(x)))}
      <SpKb lo={lo} hi={lo + 12} W={30} H={84} lit={lit} names={Object.fromEntries(K.filter(spIsW).map(x => [x, lwLet(x)]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}} act={act} onTap={tap} label={t('The chromatic scale from E♭', 'E♭ 반음계')}/>
      {spMsg(done ? (h === 'R' ? t('The right hand\'s 5s: F and C, the top of each white pair.', '오른손 5번: F와 C, 흰건반 짝의 위쪽.') : t('The left hand\'s 5s: E and B, the bottom of each white pair.', '왼손 5번: E와 B, 흰건반 짝의 아래쪽.'))
        : bad != null ? t('That one is ' + c345(bad, h) + '. Find the white keys that stand in pairs.', '거기는 ' + c345(bad, h) + '번. 짝으로 붙은 흰건반을 찾아요.') : t('Where does 5 go? ' + found.length + ' of ' + fives.length, '5번은 어디? ' + fives.length + '개 중 ' + found.length), done ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Two octaves, two a beat', '▶ 두 옥타브, 한 박에 둘')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}
// ── step 6: two voices in one hand: the long note held while the other voice moves (the skill of exercise 7B) ──
const S7_VO = [   // [held note, beats], the moving voice [[note, beats], …]; R in the right hand, L in the left
  { h: 'R', hold: [[0, 4]], move: [[4, 1], [5, 1], [7, 1], [5, 1]] }, { h: 'R', hold: [[4, 2], [2, 2]], move: [[7, 1], [9, 1], [11, 1], [9, 1]] },
  { h: 'R', hold: [[7, 4]], move: [[12, 1], [11, 1], [9, 1], [11, 1]] }, { h: 'L', hold: [[-12, 4]], move: [[-5, 1], [-7, 1], [-8, 1], [-7, 1]] },
  { h: 'L', hold: [[-17, 2], [-15, 2]], move: [[-8, 1], [-10, 1], [-12, 1], [-8, 1]] }, { h: 'R', hold: [[2, 4]], move: [[5, 1], [7, 1], [9, 1], [7, 1]] },
];
const voPlay = (x, held) => { const ev = []; let a = 0; x.hold.forEach(([n, d]) => { ev.push({ at: a, keys: [n], len: held ? d * 0.97 : 0.35, vol: 0.14 }); a += d; }); a = 0; x.move.forEach(([n, d]) => { ev.push({ at: a, keys: [n], len: d * 0.9, vol: 0.12 }); a += d; }); return spPlay(ev, 66); };
function VoBars({ x, held }) {
  const ks = x.hold.concat(x.move).map(p => p[0]), lo = Math.min(...ks), hi = Math.max(...ks), Y = (k) => 70 - (k - lo) / Math.max(1, hi - lo) * 56, X = (b) => 12 + b * 60;
  let a = 0, svg = ''; x.move.forEach(([n, d]) => { svg += '<rect x="' + (X(a) + 2) + '" y="' + (Y(n) - 5) + '" width="' + (d * 60 - 6) + '" height="10" rx="5" fill="#e4572e"/>'; a += d; });
  a = 0; x.hold.forEach(([n, d]) => { svg += '<rect x="' + (X(a) + 2) + '" y="' + (Y(n) - 5) + '" width="' + (held ? d * 60 - 6 : 18) + '" height="10" rx="5" fill="#26296b"/>' + (held ? '' : '<rect x="' + (X(a) + 22) + '" y="' + (Y(n) - 5) + '" width="' + (d * 60 - 26) + '" height="10" rx="5" fill="none" stroke="#26296b" stroke-dasharray="3 3"/>'); a += d; });
  return <svg viewBox="0 0 264 80" style={{width:'100%',maxWidth:300,display:'block',margin:'0 auto'}} role="img" aria-label={t('Two voices in one hand', '한 손의 두 성부')} dangerouslySetInnerHTML={{ __html: svg }}/>;
}
function S7VoicesPad({ onResult, fixed }) {
  const [i, setI] = useState(fixed ? fixed.i : 0), [held, setHeld] = useState(fixed ? fixed.held : true), [quiz, setQuiz] = useState(!!fixed), [ans, setAns] = useState(null);
  const x = S7_VO[i], show = !quiz || ans;
  const ask = () => { let j, g = 0; do { j = Math.floor(Math.random() * S7_VO.length); } while (j === i && g++ < 10); const hh = Math.random() < 0.5; setI(j); setHeld(hh); setQuiz(true); setAns(null); voPlay(S7_VO[j], hh); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === held }); };
  return (
    <div className="try-box" style={actBox} data-s7="voices">
      <div style={actTitle}>{t('Two voices in one hand', '한 손에 두 성부')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>한 손이 두 성부를 쳐요: 한 손가락은 <b>긴 음을 붙잡고</b>, 다른 손가락들은 <b>움직여요</b>. 붙잡은 음이 끝까지 울려야 해요. 들어 보고: 붙잡았나요, 놓쳤나요?</> : <>One hand plays two voices: one finger <b>holds a long note</b> while the others <b>move</b>. The held note must sound to its end. Listen: was it held, or let go?</>}</div>
      {!quiz && spChips(S7_VO.map((y, j) => [j, (y.h === 'R' ? t('RH ', '오 ') : t('LH ', '왼 ')) + (j + 1)]), i, (j) => { setI(j); setAns(null); })}
      {show && <VoBars x={x} held={held}/>}
      {show && <div style={{textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.muted}}>{t('navy: the held voice · coral: the moving voice', '남색: 붙잡는 성부 · 산호색: 움직이는 성부')}</div>}
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{[[true, t('Held to the end', '끝까지 붙잡았어요')], [false, t('Let go too soon', '너무 일찍 놓았어요')]].map(([v, lab]) => <button key={String(v)} className="choice-btn" onClick={() => say(v)} style={{padding:'12px 4px',fontSize:14.5,fontWeight:900}}>{lab}</button>)}</div>}
      {spMsg(ans != null ? (ans === held ? t('Yes.', '맞아요.') : t(held ? 'It was held: the long note sounded under the moving one.' : 'It was let go: the long note stopped after its first moment.', held ? '붙잡았어요: 긴 음이 움직이는 음 아래에서 울렸어요.' : '놓았어요: 긴 음이 처음만 울리고 멈췄어요.')) : quiz ? t('Listen to the long note: held, or let go?', '긴 음을 들어 봐요: 붙잡았나요, 놓았나요?') : '', ans != null ? (ans === held ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setHeld(true); voPlay(x, true); }}>{t('▶ Held', '▶ 붙잡기')}</button>}
        {!quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setHeld(false); voPlay(x, false); }}>{t('▶ Let go', '▶ 놓기')}</button>}
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => voPlay(x, held)}>{t('♪ Again', '♪ 다시')}</button>}
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Held or let go?', '▶ 붙잡았을까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── step 7: the Lydian mode: a major scale with its 4th raised; the white keys from F (the skill of exercise 7C, in octaves) ──
const LYD_KEYS = { F: [5, 'F'], C: [0, 'C'], G: [-5, 'G'], D: [2, 'D'] };
const lydSc = (r, lyd) => [0, 2, 4, lyd ? 6 : 5, 7, 9, 11, 12].map(x => r + x);
const lydPlay = (r, lyd, oct = true) => { const S = lydSc(r, lyd), sq = S.concat(S.slice(0, -1).reverse()); return spPlay(sq.map((x, n) => ({ at: n / 2, keys: oct ? [x, x - 12] : [x], len: n === sq.length - 1 ? 1.4 : 0.42, vol: 0.12 })), 96, 2); };
const lydNames = (k, lyd) => [0, 2, 4, lyd ? 6 : 5, 7, 9, 11, 12].map((x, j) => l6Spell(LYD_KEYS[k][1], x % 12, (j % 7) + 1));
const lydName = (k, lyd) => LYD_KEYS[k][1] + (lyd ? t(' Lydian', ' 리디안') : t(' major', '장조'));
function S7LydianPad({ onResult, fixed }) {
  const [k, setK] = useState(fixed ? fixed.k : 'F'), [lyd, setLyd] = useState(fixed ? fixed.lyd : true), [quiz, setQuiz] = useState(!!fixed), [ans, setAns] = useState(null);
  const r = LYD_KEYS[k][0], S = lydSc(r, lyd), show = !quiz || ans, lit = {}; if (show) S.forEach((x, j) => { lit[x] = j === 3 && lyd ? 'cor' : 'pale'; });
  const ask = () => { const kk = pick(Object.keys(LYD_KEYS)), ll = Math.random() < 0.5; setK(kk); setLyd(ll); setQuiz(true); setAns(null); lydPlay(LYD_KEYS[kk][0], ll); };
  const say = (v) => { if (!quiz || ans != null) return; setAns(v); if (onResult) onResult({ ok: v === lyd }); };
  return (
    <div className="try-box" style={actBox} data-s7="lydian">
      <div style={actTitle}>{t('The Lydian mode, in octaves', '리디안 선법, 옥타브로')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>장음계에서 <b>4음을 반음 올리면</b> 리디안 선법: 장음계보다 더 밝은 소리. 가장 쉬운 리디안은 <b>F에서 F까지 흰건반</b>. 7급 연습곡 7C처럼 양손 옥타브로 가볍고 또렷하게.</> : <>Raise <b>the 4th of a major scale</b> a semitone and you have the Lydian mode: brighter still than major. The simplest Lydian is <b>the white keys from F to F</b>. Play it in octaves, light and clean, as exercise 7C does.</>}</div>
      {!quiz && spChips(Object.keys(LYD_KEYS).map(x => [x, LYD_KEYS[x][1]]), k, (x) => { setK(x); setAns(null); })}
      {!quiz && spChips([[false, t('Major', '장음계')], [true, t('Lydian', '리디안')]], lyd, (v) => { setLyd(v); lydPlay(r, v); })}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 4px'}}>{show ? lydName(k, lyd) + ' · ' + lydNames(k, lyd).join(' ') : t('Major or Lydian?', '장음계? 리디안?')}</div>
      <SpKb lo={Math.min(r, 0) - 1} hi={Math.max(r + 12, 12) + 1} W={20} H={66} lit={lit} names={show ? Object.fromEntries(S.map((x, j) => [x, lydNames(k, lyd)[j]])) : {}} label={t('The scale', '음계')}/>
      {quiz && ans == null && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{[[false, t('Major', '장음계')], [true, t('Lydian', '리디안')]].map(([v, lab]) => <button key={String(v)} className="choice-btn" onClick={() => say(v)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}}>{lab}</button>)}</div>}
      {spMsg(ans != null ? (ans === lyd ? t('Yes: ' + lydName(k, lyd) + '.', '맞아요: ' + lydName(k, lyd) + '.') : t('It was ' + lydName(k, lyd) + (lyd ? ': listen for the raised 4th, a semitone below the 5th.' : ': its 4th sits a semitone above the 3rd.'), '정답은 ' + lydName(k, lyd) + (lyd ? ': 5음 바로 반음 아래의 올린 4음을 들어요.' : ': 4음이 3음 바로 반음 위에 있어요.'))) : quiz ? t('Listen to the 4th note: major or Lydian?', '네 번째 음을 들어요: 장음계? 리디안?') : '', ans != null ? (ans === lyd ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => lydPlay(r, lyd)}>{quiz && ans == null ? t('♪ Again', '♪ 다시') : t('▶ In octaves', '▶ 옥타브로')}</button>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Major or Lydian?', '▶ 장음계? 리디안?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── make: a mode jam: a drone underneath, the white keys from a new home on top ──
const MJ_MODES = [['ion', 0, 'Major (Ionian)', '장음계(이오니안)', 11], ['dor', 2, 'Dorian', '도리안', 11], ['lyd', 5, 'Lydian', '리디안', 11], ['mix', 7, 'Mixolydian', '믹솔리디안', 5], ['aeo', 9, 'Minor (Aeolian)', '단음계(에올리안)', 5]];   // [id, the home key, en, ko, its flavour note]
function ModeJam() {
  const [m, setM] = useState('dor'), [on, setOn] = useState(false), [last, setLast] = useState(null), tm = useRef(null);
  const M = MJ_MODES.find(x => x[0] === m), home = M[1];
  const drone = () => spPlay([{ at: 0, keys: [home - 24, home - 17], len: 3.9, vol: 0.07 }], 80);
  const stop = () => { if (tm.current) { clearInterval(tm.current); tm.current = null; } stopClicks(); setOn(false); };
  const start = () => { stop(); drone(); tm.current = setInterval(drone, 3000); setOn(true); };
  useEffect(() => () => { if (tm.current) clearInterval(tm.current); }, []);
  useEffect(() => { if (on) start(); }, [m]);
  const tap = (k) => { playKey(k, 0.5); setLast(k); };
  const lit = {}; for (let k = home; k <= home + 12; k++) if (spIsW(k)) lit[k] = 'pale'; lit[home] = 'cor'; lit[home + 12] = 'cor'; const fl = home + spPc(M[4] - home); lit[fl] = 'good'; if (fl + 12 <= 19) lit[fl + 12] = 'good';
  return (
    <div className="try-box" style={actBox} data-mk="mode">
      <div style={actTitle}>{t('My mode jam', '나의 선법 잼')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>흰건반만 써요. 그런데 <b>집(빨간 건반)</b>을 바꾸면 소리가 바뀌어요: D에서 도리안, F에서 리디안, G에서 믹솔리디안. 아래에서 집 음이 계속 울려요(드론). 흰건반을 아무거나 눌러 즉흥 연주! 초록 건반이 그 선법의 맛을 내는 음.</>
        : <>White keys only. But move <b>home (the coral key)</b> and the sound changes: Dorian from D, Lydian from F, Mixolydian from G. A drone keeps home sounding underneath. Tap any white keys and make it up as you go! The green key is the note that gives the mode its flavour.</>}</div>
      {spChips(MJ_MODES.map(x => [x[0], t(x[2], x[3])]), m, setM)}
      <SpKb lo={0} hi={19} W={22} H={78} lit={lit} names={{ [home]: lwLet(home) }} onTap={tap} label={t('Play on the white keys', '흰건반에서 연주해요')}/>
      {spMsg(on ? t('The drone is on: home is ' + lwLet(home) + '. Start and end your tune there.', '드론이 울려요: 집은 ' + lwLet(home) + '. 선율을 거기서 시작해 거기서 끝내요.') : t('Turn the drone on, then play.', '드론을 켜고 연주해요.'), on ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={on ? stop : start}>{on ? t('■ Drone off', '■ 드론 끄기') : t('▶ Drone on', '▶ 드론 켜기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => { const W7 = []; for (let k = home; k <= home + 12; k++) if (spIsW(k)) W7.push(k); spPlay(W7.map((x, n) => ({ at: n / 2, keys: [x], len: 0.45, vol: 0.14 })), 96); }}>{t('▶ Hear the mode', '▶ 선법 듣기')}</button>
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const s7PicGrand = () => lsRawPic('<path d="M4 34 L22 18 L40 4 L58 18 L76 4" fill="none" stroke="#e4572e" stroke-width="2.6"/><path d="M4 40 L22 26 L40 40 L58 26 L76 40" fill="none" stroke="#26296b" stroke-width="2.6"/><text x="64" y="30" font-family="Inter, sans-serif" font-size="10" font-weight="900" fill="#e4572e">m</text>', [0, 0, 80, 44]);
const s7PicPs = () => lsRawPic('<path d="M4 38 L40 4 L76 38" fill="none" stroke="#e4572e" stroke-width="2.6"/><path d="M4 42 L40 22 L76 42" fill="none" stroke="#26296b" stroke-width="2.6"/><text x="12" y="16" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#e4572e">3</text><text x="60" y="34" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#26296b">2</text>', [0, 0, 80, 44]);
const s7Pic345 = () => lsRawPic([0, 1, 2].map(i => '<text x="' + (10 + i * 24) + '" y="28" text-anchor="middle" font-family="Inter, sans-serif" font-size="18" font-weight="900" fill="' + (i === 2 ? '#e4572e' : '#26296b') + '">' + (i + 3) + '</text>').join(''), [0, 0, 70, 44]);
const s7PicVo = () => lsRawPic('<rect x="4" y="30" width="70" height="9" rx="4.5" fill="#26296b"/>' + [0, 1, 2, 3].map(i => '<rect x="' + (4 + i * 18) + '" y="' + [14, 10, 6, 10][i] + '" width="15" height="8" rx="4" fill="#e4572e"/>').join(''), [0, 0, 80, 44]);
const s7PicLyd = () => lsRawPic('<text x="8" y="30" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="#26296b">F</text><path d="M24 24 H58" stroke="#26296b" stroke-width="2"/><text x="62" y="30" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="#e4572e">F</text>', [0, 0, 80, 44]);

function s7LbPages(scr = false) {
  const ch = 'scales-7', s6n = bkChapterNo('scales-6');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks = [[s7PicGrand(), t('I play the grand scale in D, B minor, A♭ and F minor', 'D, B단조, A♭, F단조로 그랜드 스케일을 쳐요')], [s7PicPs(), t('I play a scale three against two: three octaves against two', '스케일을 3 대 2로 쳐요: 세 옥타브 대 두 옥타브')],
    [spPicMirror(), t('I play F♯ major and D♯ minor in contrary motion', 'F♯장조와 D♯단조를 반대 방향으로 쳐요')], [s7Pic345(), t('I play the chromatic scale from E♭ with 3, 4 and 5', 'E♭ 반음계를 3, 4, 5번으로 쳐요')], [s7PicVo(), t('I hold one voice while the other moves, in one hand', '한 손에서 한 성부를 붙잡고 다른 성부를 움직여요')], [s7PicLyd(), t('I play the Lydian mode in octaves', '리디안 선법을 옥타브로 쳐요')]];
  const toc = [[t('The grand scale in four new keys', '네 새 조의 그랜드 스케일'), 2], [t('Three against two, as a scale', '3 대 2, 스케일로'), 3], [t('Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?'), 4], [t('Chromatic, hands together', '반음계, 양손 함께'), 5], [t('Chromatic from E♭: fingers 3, 4 and 5', 'E♭ 반음계: 3, 4, 5번'), 6], [t('Two voices in one hand', '한 손에 두 성부'), 7], [t('The Lydian mode, in octaves', '리디안 선법, 옥타브로'), 8], [t('My six checks', '나의 여섯 가지 확인'), 9]];
  const c345Still = (h) => { const lo = c345Lo(h), K = Array.from({ length: 13 }, (_, j) => lo + j), nums = {}, lit = {}; K.forEach(x => { nums[x] = c345(x, h); if (nums[x] === 5) lit[x] = 'cor'; });
    return <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{spHand(h)}</div><SpKb lo={lo} hi={lo + 12} W={scr ? 24 : 34} H={scr ? 70 : 90} lit={lit} names={Object.fromEntries(K.filter(spIsW).map(x => [x, lwLet(x)]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}}/></div>; };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The Grade 7 scales as skills (chapter ' + s6n + ' has Grade 6; the I–IV–V–I progressions and the arpeggios are the next chapter). From the technical work book, Grade 7: the abbreviated grand scale format, D major, B harmonic minor, A♭ major, F harmonic minor, four octaves, mf, clear even legato, ♩ = 80 four notes a beat; polyrhythmic scales, hands together in similar motion, three against two, D major and B harmonic minor, right hand three octaves, left hand two, mf, legato, ♩ = 80; contrary motion, F♯ major and D♯ harmonic minor, two octaves, mf, ♩ = 80 four notes a beat; chromatic scales from D and from G♯/A♭, four octaves, hands separately and together, (i) all p (ii) all f (iii) p < f ascending, f > p descending, ♩ = 104 four notes a beat; the chromatic scale from E♭ with fingers 3, 4 and 5 (every black key 3), two octaves, hands separately, mf, ♩ = ca 84 two notes a beat. Steps 6 and 7 teach the skills behind exercises 7B (two-part retention) and 7C (octaves in the Lydian mode); the exercises themselves stay with the book.', '7급 스케일을 기술로(' + s6n + '장은 6급; I–IV–V–I 진행과 아르페지오는 다음 장). 테크닉 책의 7급: 줄인 그랜드 스케일, D장조, B 화성 단음계, A♭장조, F 화성 단음계, 네 옥타브, mf, 고르고 또렷한 레가토, ♩ = 80 한 박에 네 음; 폴리리듬 스케일, 같은 방향 양손, 3 대 2, D장조와 B 화성 단음계, 오른손 세 옥타브, 왼손 두 옥타브, mf, 레가토, ♩ = 80; 반대 방향, F♯장조와 D♯ 화성 단음계, 두 옥타브, mf, ♩ = 80 한 박에 네 음; D와 G♯/A♭에서 반음계, 네 옥타브, 한 손씩 그리고 양손, (i) 모두 p (ii) 모두 f (iii) 올라가며 p < f, 내려오며 f > p, ♩ = 104 한 박에 네 음; E♭에서 3, 4, 5번 반음계(검은건반은 모두 3), 두 옥타브, 한 손씩, mf, ♩ = 약 84 한 박에 두 음. 6, 7단계는 연습곡 7B(두 성부 유지)와 7C(리디안 선법의 옥타브) 뒤의 기술을 가르쳐요; 연습곡 자체는 책에.'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={150}><div style={{width:'100%',maxWidth:440,margin:'0 auto'}}><PsRoute k="D" w={440}/></div></LbPic>
      <LbSay size={18}>{t('Grade 7 scales: the grand scale in four new keys, three octaves against two, contrary motion on the black keys, chromatic three ways and with 3, 4 and 5, two voices in one hand, and the Lydian mode.', '7급 스케일: 네 새 조의 그랜드 스케일, 세 옥타브 대 두 옥타브, 검은건반의 반대 방향, 세 가지 반음계와 3, 4, 5번 반음계, 한 손에 두 성부, 그리고 리디안 선법.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The grand scale in four new keys', '네 새 조의 그랜드 스케일')}
      teacher={<>{spTx(t('D major, B harmonic minor, A♭ major and F harmonic minor, hands together in the abbreviated grand scale format, four octaves, mf, clear even legato, ♩ = 80 four notes a beat; the same route as Grade 6. The book\'s starting notes (as printed): D major RH D below middle C, LH an octave lower; B minor RH the B below that; A♭ major RH the A♭ an octave and a 3rd below middle C; F minor RH the F below middle C. The ear game: part 1 of a random key, major or harmonic minor?', 'D장조, B 화성 단음계, A♭장조, F 화성 단음계, 줄인 그랜드 스케일 양손, 네 옥타브, mf, 고르고 또렷한 레가토, ♩ = 80 한 박에 네 음; 6급과 같은 길. 책의 시작 음(인쇄된 대로): D장조 오른손은 가운데 도 아래 D, 왼손은 한 옥타브 아래; B단조 오른손은 그 아래 B; A♭장조 오른손은 가운데 도에서 옥타브와 3도 아래 A♭; F단조 오른손은 가운데 도 아래 F. 귀 놀이: 아무 조의 1부분, 장조일까 화성 단음계일까?'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:12,width:'100%',maxWidth:700,margin:'0 auto'}}>{['D7', 'Fmh7'].map(x => <div key={x}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{t(S6_GR[x].en, S6_GR[x].ko)}</div><GrRoute k={x} w={330}/></div>)}</div></LbPic>} live={<S7GrandPad/>}/>
      <LbSay>{LANG === 'ko' ? <>길은 그대로, 조만 넷. 장조와 그 <b>나란한 화성 단음계</b>가 짝: D와 B단조, A♭과 F단조. 단음계는 7음을 올려서 위쪽에 <b>넓은 걸음</b>.</> : <>The same route; four keys. Each major with its <b>relative harmonic minor</b>: D with B minor, A♭ with F minor. The minor raises its 7th: <b>one wide step</b> near the top.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>D장조, 두 손을 한 옥타브 떨어뜨려 1부분만. 그다음 2부분.</>, <>네 부분을 모두, 그다음 B 화성 단음계. A♯이 넓은 걸음.</>, <>A♭장조와 F 화성 단음계. {spMM(80)}까지, 한 박에 네 음.</>]
        : [<>D major, the hands an octave apart: part 1 only. Then part 2.</>, <>All four parts, then B harmonic minor: A♯ makes the wide step.</>, <>A♭ major and F harmonic minor. Up to {spMM(80)}, four notes a beat.</>]}/>
      <LbRemember>{t('The same route, four new keys.', '같은 길, 네 새 조.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Three against two, as a scale', '3 대 2, 스케일로')}
      teacher={<>{spTx(t('Polyrhythmic scales, hands together in similar motion, three against two: D major and B harmonic minor, the right hand three octaves in triplets, the left hand two octaves in quavers, legato, mf, ♩ = 80. As printed, the RH starts on the D (or B) above the LH\'s; both reach the top together after 7 beats and finish together. The book\'s extra for experts (optional): legato in one hand and staccato in the other. The beat pattern is the Grade 6 one: both, right, left, right.', '폴리리듬 스케일, 같은 방향 양손, 3 대 2: D장조와 B 화성 단음계, 오른손은 셋잇단으로 세 옥타브, 왼손은 8분음표로 두 옥타브, 레가토, mf, ♩ = 80. 인쇄된 대로 오른손은 왼손보다 한 옥타브 위 D(또는 B)에서 시작; 7박 뒤 함께 꼭대기에, 함께 끝나요. 책의 전문가용(선택): 한 손은 레가토, 다른 손은 스타카토. 박 안의 무늬는 6급과 같아요: 함께, 오, 왼, 오.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:520,margin:'0 auto'}}><PsRoute k="D" w={520}/></div></LbPic>} live={<S7PolyScalePad/>}/>
      <LbSay>{LANG === 'ko' ? <>오른손 <b>한 박에 셋</b>, 왼손 <b>한 박에 둘</b>. 그래서 같은 7박 동안 오른손은 세 옥타브, 왼손은 두 옥타브: <b>꼭대기에서 함께</b> 만나요.</> : <>The right hand <b>three a beat</b>, the left <b>two a beat</b>. So in the same 7 beats the right hand climbs three octaves and the left two: <b>they meet at the top</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>무릎에서 "함께, 오, 왼, 오"를 말하며 두드려요.</>, <>D장조, 한 옥타브씩: 오른손 셋잇단, 왼손 8분음표, 천천히.</>, <>오른손 세 옥타브, 왼손 두 옥타브. {spMM(80)}까지.</>]
        : [<>On your knees: "both, right, left, right", saying the words.</>, <>D major, one octave at a time: the right hand in triplets, the left in quavers, slowly.</>, <>Right hand three octaves, left hand two. Up to {spMM(80)}.</>]}/>
      <LbRemember>{t('Three a beat against two: they meet at the top.', '한 박에 셋 대 둘: 꼭대기에서 만나요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?')}
      teacher={<>{spTx(t('F♯ major and D♯ harmonic minor, hands together in contrary motion from one note, two octaves, mf, clear even legato, ♩ = 80 four notes a beat. The book\'s first octaves (p51): F♯ major RH 2 3 4 1 2 3 1 2, LH 2 1 2 3 1 2 3 4; D♯ minor RH 2 1 2 3 4 1 2 3, LH 2 3 1 2 3 4 1 2. Neither mirrors.', 'F♯장조와 D♯ 화성 단음계, 한 음에서 반대 방향 양손, 두 옥타브, mf, 고르고 또렷한 레가토, ♩ = 80 한 박에 네 음. 책의 첫 옥타브(51쪽): F♯장조 오른손 2 3 4 1 2 3 1 2, 왼손 2 1 2 3 1 2 3 4; D♯단조 오른손 2 1 2 3 4 1 2 3, 왼손 2 3 1 2 3 4 1 2. 둘 다 거울 쌍둥이가 아니에요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:scr ? 440 : 560,margin:'0 auto'}}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('Fs7')} · {t('not mirror twins', '거울 쌍둥이 아님')}</div><ScfCmKb k="Fs7" W={scr ? 20 : 30} H={scr ? 66 : 84} mark={scfFirstDiff('Fs7')}/></div></LbPic>} live={<S7MirrorPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 손이 F♯(또는 D♯)에서 시작해 멀어져요. 둘째 음부터 번호가 갈라져요: <b>손마다 자기 스케일 번호</b>.</> : <>Both hands start on F♯ (or D♯) and move apart. From the second note the numbers part: <b>each hand keeps its own scale fingering</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>두 손 2번을 F♯에. 오른손 3, 왼손 1로 갈라져요.</>, <>한 옥타브, 천천히. 엄지가 B와 E♯에 오는지 봐요.</>, <>D♯ 화성 단음계도. 두 옥타브, {spMM(80)}까지.</>]
        : [<>Both 2s on F♯. Then the right hand goes on with 3, the left with 1.</>, <>One octave, slowly: watch the thumbs land on B and E♯.</>, <>Then D♯ harmonic minor. Two octaves, up to {spMM(80)}.</>]}/>
      <LbRemember>{t('Each hand keeps its own numbers.', '손마다 자기 번호를 지켜요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Chromatic, hands together', '반음계, 양손 함께')}
      teacher={<>{spTx(t('The chromatic scales from D and from G♯/A♭, four octaves, hands separately and together in similar motion, clear even legato, ♩ = 104 four notes a beat, three ways: (i) all p, (ii) all f, (iii) p < f ascending, f > p descending. The book prints two octaves to show the fingering: 3 on every black key; RH 1 on white keys with 2 on F and C; LH 1 on white keys with 2 on E and B.', 'D와 G♯/A♭에서 반음계, 네 옥타브, 한 손씩 그리고 같은 방향 양손, 고르고 또렷한 레가토, ♩ = 104 한 박에 네 음, 세 가지로: (i) 모두 p, (ii) 모두 f, (iii) 올라가며 p < f, 내려오며 f > p. 책은 운지를 보이려고 두 옥타브만 인쇄해요: 검은건반 3; 오른손은 흰건반 1, F와 C에 2; 왼손은 흰건반 1, E와 B에 2.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><SpKb lo={2} hi={14} W={scr ? 26 : 36} H={scr ? 74 : 92} lit={{}} names={Object.fromEntries(Array.from({ length: 13 }, (_, j) => 2 + j).filter(spIsW).map(x => [x, lwLet(x)]))} up={Object.fromEntries(Array.from({ length: 13 }, (_, j) => [2 + j, s4ChR(2 + j)]))} dn={Object.fromEntries(Array.from({ length: 13 }, (_, j) => [2 + j, s4ChL(2 + j)]))}/></div></LbPic>} live={<S7ChromPad/>}/>
      <LbSay>{LANG === 'ko' ? <>3번은 언제나 함께 검은건반에. 두 손이 다른 곳은 <b>E–F와 B–C 둘레</b>뿐. 세 가지 셈여림으로, 이제 {spMM(104)}.</> : <>The 3s always land together on the black keys. The hands differ only <b>around E–F and B–C</b>. Three dynamics, now at {spMM(104)}.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>D에서 한 손씩, 두 옥타브. 3번이 검은건반에.</>, <>양손 함께, 네 옥타브. 모두 p, 그다음 모두 f.</>, <>올라가며 세게, 내려오며 여리게. G♯에서도. {spMM(104)}까지.</>]
        : [<>From D, hands separately, two octaves: 3 on every black key.</>, <>Hands together, four octaves: all p, then all f.</>, <>Louder up, softer down. Then from G♯. Up to {spMM(104)}.</>]}/>
      <LbRemember>{t('The 3s land together.', '3번은 함께 떨어져요.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Chromatic from E♭: fingers 3, 4 and 5', 'E♭ 반음계: 3, 4, 5번')}
      teacher={<>{spTx(t('The chromatic scale from E♭ using fingers 3, 4 and 5; every black key is played by finger 3. Two octaves, hands separately, mf, clear even legato, ♩ = ca 84 two notes a beat; the written fingering must be observed; quality and evenness of tone matter more than speed (book p53). As printed: RH up E♭3 E4 F5 F♯3 G4 G♯3 A4 A♯3 B4 C5 C♯3 D4; LH down E♭3 D4 D♭3 C4 B5 B♭3 A4 A♭3 G4 G♭3 F4 E5. So the RH\'s 5s are F and C, the LH\'s E and B: the outer note of each white pair.', 'E♭에서 3, 4, 5번만 쓰는 반음계; 검은건반은 모두 3번. 두 옥타브, 한 손씩, mf, 고르고 또렷한 레가토, ♩ = 약 84 한 박에 두 음; 적힌 운지를 지켜야 하고, 빠르기보다 고르고 좋은 소리가 중요해요(53쪽). 인쇄된 대로: 오른손 올라가며 E♭3 E4 F5 F♯3 G4 G♯3 A4 A♯3 B4 C5 C♯3 D4; 왼손 내려가며 E♭3 D4 D♭3 C4 B5 B♭3 A4 A♭3 G4 G♭3 F4 E5. 그래서 오른손 5번은 F와 C, 왼손은 E와 B: 흰건반 짝의 바깥쪽.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:760,margin:'0 auto'}}>{c345Still('R')}{c345Still('L')}</div></LbPic>} live={<S7Ch345Pad/>}/>
      <LbSay>{LANG === 'ko' ? <>엄지 없이 세 손가락만. <b>검은건반 3</b>, <b>흰건반 4</b>, 그리고 흰건반 둘이 붙은 곳의 <b>바깥쪽은 5</b>. 천천히, 고르게.</> : <>Three fingers, no thumb. <b>Black keys 3</b>, <b>white keys 4</b>, and <b>5 on the outer one</b> where two white keys stand together. Slowly and evenly.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>오른손, E♭에서 한 옥타브: 3 4 5 3 4 3 4 3 4 5 3 4.</>, <>왼손, E♭에서 내려가며: 3 4 3 4 5 3 4 3 4 3 4 5.</>, <>두 옥타브, 한 박에 두 음, 약 {spMM(84)}.</>]
        : [<>Right hand, one octave up from E♭: 3 4 5 3 4 3 4 3 4 5 3 4.</>, <>Left hand, down from E♭: 3 4 3 4 5 3 4 3 4 3 4 5.</>, <>Two octaves, two notes a beat, about {spMM(84)}.</>]}/>
      <LbRemember>{t('Black 3, white 4, the outer white 5.', '검은건반 3, 흰건반 4, 바깥 흰건반 5.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Step 6', '6단계')} title={t('Two voices in one hand', '한 손에 두 성부')}
      teacher={<>{t('The skill of exercise 7B (Two-part retention, each hand): one finger holds a long note for its full value while other fingers of the same hand play a moving voice, both voices legato. The ear game: held to the end, or let go? Practise by playing the moving voice alone, then adding the held note and listening for it to last.', '연습곡 7B(두 성부 유지, 손마다)의 기술: 한 손가락이 긴 음을 끝까지 붙잡고, 같은 손의 다른 손가락들이 움직이는 성부를 쳐요. 두 성부 모두 레가토. 귀 놀이: 끝까지 붙잡았나, 놓았나? 연습: 움직이는 성부만 먼저, 그다음 긴 음을 더해 끝까지 울리는지 들어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=6')}>
      <LbLive still={<LbPic h={140}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:640,margin:'0 auto'}}>{[true, false].map(hh => <div key={String(hh)}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:hh ? BK.green : BK.coral}}>{hh ? t('Held to the end', '끝까지 붙잡기') : t('Let go too soon', '너무 일찍 놓기')}</div><VoBars x={S7_VO[0]} held={hh}/></div>)}</div></LbPic>} live={<S7VoicesPad/>}/>
      <LbSay>{LANG === 'ko' ? <>한 손가락은 <b>긴 음을 붙잡고</b>, 나머지는 그 위에서 움직여요. 긴 음이 끝까지 들려야 해요.</> : <>One finger <b>holds a long note</b> while the others move above it. The long note must sound to its end.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>오른손 1번으로 C를 붙잡고, 3 4 5로 E F G F.</>, <>C가 끝까지 울리는지 들어요. 왼손도.</>, <>책의 연습곡 7B를 천천히.</>]
        : [<>Right hand: hold C with 1 while 3 4 5 play E F G F.</>, <>Listen for the C to last to the end. Then the left hand.</>, <>The book's exercise 7B, slowly.</>]}/>
      <LbRemember>{t('One finger holds; the others sing.', '한 손가락은 붙잡고, 나머지는 노래해요.')}</LbRemember>
    </LbPage>,
    <LbPage key="8" no={8} chId={ch} kicker={t('Step 7', '7단계')} title={t('The Lydian mode, in octaves', '리디안 선법, 옥타브로')}
      teacher={<>{t('The skill of exercise 7C (clean, light octaves in the Lydian mode): the Lydian mode is a major scale with a raised 4th, the white keys from F to F in its simplest form; played in octaves, light and clean, from a loose wrist. The ear game: major or Lydian? (The book\'s extra for experts on p53 describes the Dorian the same way: the white keys from D.)', '연습곡 7C(리디안 선법의 깨끗하고 가벼운 옥타브)의 기술: 리디안 선법은 4음을 올린 장음계, 가장 쉬운 꼴은 F에서 F까지 흰건반; 손목을 풀고 가볍고 깨끗한 옥타브로. 귀 놀이: 장음계? 리디안? (53쪽 전문가용은 도리안을 같은 방법으로 설명해요: D에서 흰건반.)')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=7')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:520,margin:'0 auto'}}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{t('F Lydian: the white keys from F; B is the raised 4th', 'F 리디안: F부터 흰건반; B가 올린 4음')}</div><SpKb lo={4} hi={18} W={scr ? 22 : 32} H={scr ? 66 : 86} lit={Object.fromEntries(lydSc(5, true).map((x, j) => [x, j === 3 ? 'cor' : 'pale']))} names={Object.fromEntries(lydSc(5, true).map((x, j) => [x, lydNames('F', true)[j]]))}/></div></LbPic>} live={<S7LydianPad/>}/>
      <LbSay>{LANG === 'ko' ? <>장음계의 <b>4음을 반음 올리면</b> 리디안. F에서 F까지 흰건반이 바로 그것. 양손 옥타브, 가볍게.</> : <><b>Raise the 4th</b> of a major scale and you have the Lydian. The white keys from F to F are exactly that. Octaves in both hands, light.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>F에서 F까지 흰건반, 한 손씩 옥타브로(1번과 5번).</>, <>F장조(B♭)와 번갈아: 무엇이 달라지나요?</>, <>C 리디안(F♯), G 리디안(C♯)도 옥타브로.</>]
        : [<>The white keys from F to F, each hand in octaves (1 and 5).</>, <>Alternate with F major (B♭): what changes?</>, <>C Lydian (F♯) and G Lydian (C♯) in octaves too.</>]}/>
      <LbRemember>{t('Lydian: the 4th raised.', '리디안: 4음을 올려요.')}</LbRemember>
    </LbPage>,
    <LbPage key="9" no={9} chId={ch} kicker={t('Check-up', '점검')} title={t('My six checks', '나의 여섯 가지 확인')}
      teacher={<>{t('Each one played to you from memory, in the Grade 7 keys at the book\'s speeds (the teacher\'s copy lists them). Listen for the turn of the grand scale, an even three against two that meets at the top, the right numbers where contrary motion parts, the 3-4-5 chromatic\'s evenness, a held note that lasts, and light octaves.', '하나씩 외워서, 7급 조와 책의 빠르기로 들려줘요(선생님용에 목록). 그랜드 스케일의 방향 바꾸기, 꼭대기에서 만나는 고른 3 대 2, 반대 방향이 갈라지는 곳의 바른 번호, 3-4-5 반음계의 고름, 끝까지 울리는 긴 음, 가벼운 옥타브를 들어 주세요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey="pb_s7_six"/>}/>
    </LbPage>,
  ];
}
function Scales7LessonBook() { return <>{s7LbPages(false)}</>; }
function S7Learn({ onStart }) {
  const pages = s7LbPages(true), opener = pages[0];
  return (
    <Lesson id="scales-7" title={bkChapterName('scales-7')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scales-7"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const S7_LEVELS = [
  { n: 1, label: 'The grand scale: major or harmonic minor?', kind: 'grand', time: 25 },
  { n: 2, label: 'Three against two: which comes next?', kind: 'poly', time: 15 },
  { n: 3, label: 'Grade 7 contrary motion: mirror twins?', kind: 'mirror', time: 15 },
  { n: 4, label: 'Chromatic from E♭: finger 3, 4 or 5?', kind: 'c345', time: 12 },
  { n: 5, label: 'Two voices: held or let go?', kind: 'held', time: 20 },
  { n: 6, label: 'Major or Lydian?', kind: 'lyd', time: 20 },
];
Object.assign(LEVEL_KO, { 'The grand scale: major or harmonic minor?': '그랜드 스케일: 장조? 화성 단음계?', 'Grade 7 contrary motion: mirror twins?': '7급 반대 방향: 거울 쌍둥이?', 'Chromatic from E♭: finger 3, 4 or 5?': 'E♭ 반음계: 3, 4, 5번 중?', 'Two voices: held or let go?': '두 성부: 붙잡았을까, 놓았을까?', 'Major or Lydian?': '장음계? 리디안?' });
function genS7Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'grand') { let k, g = 0; do { k = pick(S7_GR_KEYS); } while (prev && prev.key === k && g++ < 10); return { kind, k, answer: s7GrMinor(k) ? 'm' : 'M', choices: ['M', 'm'], key: k, uid }; }
  if (kind === 'mirror') { let k, g = 0; do { k = pick(S7_CM_KEYS); } while (prev && prev.key === 'c' + k && g++ < 10); return { kind, k, answer: scfMirror(k) ? 'yes' : 'no', choices: ['yes', 'no'], key: 'c' + k, uid }; }
  if (kind === 'c345') { let h, x, g = 0; do { h = Math.random() < 0.5 ? 'R' : 'L'; x = c345Lo(h) + Math.floor(Math.random() * 12); } while (prev && prev.key === h + x && g++ < 10); return { kind, h, x, answer: c345(x, h), choices: [3, 4, 5], key: h + x, uid }; }
  if (kind === 'held') { let i, hh, g = 0; do { i = Math.floor(Math.random() * S7_VO.length); hh = Math.random() < 0.5; } while (prev && prev.key === i + '' + hh && g++ < 10); return { kind, i, held: hh, answer: hh ? 'yes' : 'no', choices: ['yes', 'no'], key: i + '' + hh, uid }; }
  if (kind === 'lyd') { let k, l, g = 0; do { k = pick(Object.keys(LYD_KEYS)); l = Math.random() < 0.5; } while (prev && prev.key === k + l && g++ < 10); return { kind, k, lyd: l, answer: l ? 'lyd' : 'maj', choices: ['maj', 'lyd'], key: k + l, uid }; }
  let r, sl, g = 0; do { r = '3:2'; sl = pick([2, 3, 4]); } while (prev && prev.key === 'p' + sl && g++ < 10); const x = ppGrid(r)[sl];
  return { kind: 'poly', r, sl, answer: x.R && x.L ? 'B' : x.R ? 'R' : x.L ? 'L' : 'N', choices: ['B', 'R', 'L'], key: 'p' + sl, uid };
}
const s7AnswerLabel = (q) => (q.kind === 'grand' ? (q.answer === 'm' ? t('Harmonic minor', '화성 단음계') : t('Major', '장조')) : q.kind === 'c345' ? String(q.answer) : q.kind === 'held' ? (q.answer === 'yes' ? t('Held', '붙잡았어요') : t('Let go', '놓았어요')) : q.kind === 'lyd' ? (q.answer === 'lyd' ? t('Lydian', '리디안') : t('Major', '장음계')) : q.kind === 'mirror' ? s4AnswerLabel(q) : ({ B: t('both', '함께'), R: t('right', '오'), L: t('left', '왼'), N: t('nothing', '없음') })[q.answer]);
function S7Question(props) {
  const { q, given, locked, onAnswer, pixel } = props;
  if (q.kind === 'mirror') return <S4Question {...props}/>;
  if (q.kind === 'poly') return <S6Question {...props}/>;
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const play = () => { stopClicks(); if (q.kind === 'grand') grPlay(q.k, 0, q.bpm || 80); else if (q.kind === 'held') voPlay(S7_VO[q.i], q.held); else if (q.kind === 'lyd') lydPlay(LYD_KEYS[q.k][0], q.lyd); };
  useEffect(() => { if (q.kind === 'c345') return; const id = setTimeout(play, 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:14.5,fontWeight:900,lineHeight:1.2}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  const again = q.kind === 'c345' ? null : <div style={{textAlign:'center'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>;
  let title, body;
  if (q.kind === 'grand') { title = t('Part 1 of a grand scale: major or harmonic minor?', '그랜드 스케일의 1부분: 장조? 화성 단음계?'); body = <>{!pixel && done && <GrRoute k={q.k} hl={0}/>}{grid(2, [['M', t('Major', '장조')], ['m', t('Harmonic minor', '화성 단음계')]])}</>; }
  else if (q.kind === 'c345') { const lo = c345Lo(q.h); title = t('Chromatic from E♭, ' + spHand(q.h).toLowerCase() + ': which finger plays the coral key?', 'E♭ 반음계, ' + spHand(q.h) + ': 빨간 건반은 몇 번?');
    body = <><SpKb lo={lo} hi={lo + 12} W={26} H={76} lit={{ [q.x]: done ? 'good' : 'cor' }} names={Object.fromEntries(Array.from({ length: 13 }, (_, j) => lo + j).filter(spIsW).map(x => [x, lwLet(x)]))}/>{grid(3, [3, 4, 5].map(f => [f, String(f)]))}</>; }
  else if (q.kind === 'held') { title = t('Two voices in one hand: was the long note held?', '한 손의 두 성부: 긴 음을 붙잡았나요?'); body = <>{!pixel && done && <VoBars x={S7_VO[q.i]} held={q.held}/>}{grid(2, [['yes', t('Held to the end', '끝까지 붙잡았어요')], ['no', t('Let go too soon', '너무 일찍 놓았어요')]])}</>; }
  else { title = t('Listen to the 4th note: major or Lydian?', '네 번째 음을 들어요: 장음계? 리디안?'); body = grid(2, [['maj', t('Major', '장음계')], ['lyd', t('Lydian', '리디안')]]); }
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {again}{body}
  </div>);
}
Object.assign(SCALES_7_DRILL, { levels: S7_LEVELS, generate: genS7Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: s7AnswerLabel, Question: S7Question, Learn: S7Learn });
// ── the teacher's copy and the Workbook ──
const S7_WB = {
  minor: ['Bmh7', 'Fmh7'],
  c345: ['R', 'L'],
  lyd: [['F', 'B'], ['C', 'F♯'], ['G', 'C♯'], ['D', 'G♯']],
  chk: { minor: [['Bmh7', 7], ['Fmh7', 7], ['D7', 7], ['Ab7', 7]], c345: [['R', 5], ['R', 6], ['L', 4], ['L', 9]], mirror: ['Fs7', 'Dsmh7'], lyd: [['F', 'B'], ['C', 'F♯'], ['G', 'C♯'], ['A', 'D♯']] },
};
function S7Teacher() {
  const pages = [], W = S7_WB;
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scales-7" teacher>{content}</WbPage>);
  const row345 = (h) => { const lo = c345Lo(h), K = Array.from({ length: 13 }, (_, j) => (h === 'R' ? lo + j : lo + 12 - j)); return K.map(x => lwLet(x) + ' ' + c345(x, h)).join(' · '); };
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scales-7')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>{spTx('The keys, speeds and fingerings are the technical work book\'s (Grade 7 pp48-53). Scales four octaves where the book asks (it prints two: in most cases start an octave lower than written), from memory. The exercises 7A, 7B and 7C stay with the book; steps 6 and 7 teach the skills behind 7B and 7C.')}</div>
    <TcBlock page={2} title="The grand scale in four new keys" answers={<>{tcAns('TRY IT', W.minor.map(k => S6_GR[k].en + ': ' + S6_GR[k].nm.join(' ') + ' (raised 7th: ' + S6_GR[k].nm[6] + ')'))}{tcAns(spTx('FOUR OCTAVES, mf, ♩ = 80'), S7_GR_KEYS.map(k => S6_GR[k].en), null)}</>}
      watch="The minor keys' raised 7th forgotten at speed (A♯ in B minor, E♮ in F minor). Play part 1 slowly, naming the 7th aloud."
      say="“The same route, four new keys.”"/>
    <TcBlock page={3} title="Three against two, as a scale" answers={<>{tcAns('TRY IT', ['RH 21 notes up in 7 beats', 'LH 14 notes up in 7 beats', 'they meet at the top'], null)}{tcAns(spTx('D MAJOR AND B HARMONIC MINOR, ♩ = 80'), ['RH three octaves, triplets', 'LH two octaves, quavers'], null)}</>}
      watch="The quaver hand speeding up to meet the triplets (a dotted feel). Say “both, right, left, right” inside each beat."
      say="“Three a beat against two: they meet at the top.”"/>
    <TcBlock page={4} title="Contrary motion: mirror twins?" answers={<>{tcAns('TRY IT', S7_CM_KEYS.map(k => SCF_CM[k].en + ': ' + (scfMirror(k) ? 'Y' : 'N')))}{tcAns(spTx('TWO OCTAVES FROM ONE NOTE, mf, ♩ = 80'), S7_CM_KEYS.map(k => SCF_CM[k].en + ': RH ' + SCF_CM[k].R.join(' ') + ', LH ' + SCF_CM[k].L.join(' ')), null)}</>}
      watch="The LH copying the RH's thumb onto a black key. In F♯ major the LH thumb falls on E♯ and B."
      say="“Each hand keeps its own numbers.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Chromatic, hands together" answers={<>{tcAns(spTx('FROM D AND FROM G♯/A♭, FOUR OCTAVES, ♩ = 104'), ['(i) all p', '(ii) all f', '(iii) p < f up, f > p down'], null)}{tcAns('WHERE THE HANDS DIFFER', ['RH 2 on F and C', 'LH 2 on E and B'], null)}</>}
      watch="An uneven crescendo that peaks early; the 2s dropped at ♩ = 104."
      say="“The 3s land together.”"/>
    <TcBlock page={6} title="Chromatic from E♭: fingers 3, 4 and 5" answers={<>{tcAns('TRY IT (RH UP)', [row345('R')], null)}{tcAns('TRY IT (LH DOWN)', [row345('L')], null)}</>}
      watch="A thumb creeping in, or 4 and 5 swapped on the white pairs. The written fingering must be observed; tone before speed."
      say="“Black 3, white 4, the outer white 5.”"/>
    <TcBlock page={7} title="Two voices in one hand" answers={<>{tcAns('LISTEN FOR', ['the long note lasting its full value', 'the moving voice legato above it'], null)}</>}
      watch="The held finger lifting when the moving voice crosses near it. Play the moving voice alone first."
      say="“One finger holds; the others sing.”"/>
    <TcBlock page={8} title="The Lydian mode, in octaves" answers={<>{tcAns('TRY IT', W.lyd.map(([k, n]) => k + ' Lydian: ' + n))}</>}
      watch="Heavy octaves from the arm. A loose wrist, light thumb and 5th finger; the raised 4th clean."
      say="“Lydian: the 4th raised.”"/>
  </>);
  P(<>
    <TcBlock page={9} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', W.chk.minor.map(([k]) => S6_GR[k].nm[6]))}{tcAns('B', W.chk.c345.map(([h, pc]) => String(c345(pc, h))), 5)}{tcAns('C', W.chk.mirror.map(k => (scfMirror(k) ? 'Y' : 'N')), 9)}{tcAns('D', W.chk.lyd.map(([, n]) => n), 11)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (A, B and D: 4 marks each, pass 3+; C: 2 marks, pass 2). Not passed? Go back to that step's page: A p.2 · B p.6 · C p.4 · D p.8. Then hear each one at the piano, from memory, at the book's speeds.</div></>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['scales-7'] = S7Teacher;
function S7Workbook({ startNo = 1 }) {
  const W = S7_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="scales-7">{content}</WbPage>);
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="The raised 7th" how="Write each harmonic minor scale going up, then circle its raised 7th: the note that makes the wide step.">
      <div style={{display:'grid',gap:10}}>{W.minor.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 6px'}}>{s4wLabel(S6_GR[k].en)}{scfwLetters(i === 0 ? S6_GR[k].nm.concat([S6_GR[k].nm[0]]) : Array(8).fill(''), 34, i === 0 ? [6] : [])}</div></ExCell>)}</div>
    </Part>
    <Part kind="home" title="The grand scale this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['D major: parts 1 and 2 slowly, then all four', 'B harmonic minor: name the A♯ as you pass it', 'A♭ major and F harmonic minor, up to ♩ = 80'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Count the notes" how="Seven beats up. The right hand plays three a beat, the left hand two. How many notes does each hand play going up (not counting the first)?">
      <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{[['Right hand: 7 beats × 3 =', '21'], ['Left hand: 7 beats × 2 =', '14'], ['Right hand octaves (7 notes each):', '3'], ['Left hand octaves:', '2']].map(([l, a], i) => <span key={i} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(i + 1)} {l} {nvBox(i === 0, a, 44, 30)}</span>)}</div>
    </Part>
    <Part kind="home" title="Three against two this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['On your knees: “both, right, left, right”', 'D major one octave each hand together, slowly', 'RH three octaves, LH two, up to ♩ = 80'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Fingers 3, 4 and 5" how="Write the finger under (or over) every key: 3 on black keys, 4 on white keys, 5 on the outer white key of each pair.">
      <div style={{display:'grid',gap:10}}>{W.c345.map((h, i) => { const lo = c345Lo(h), K = Array.from({ length: 13 }, (_, j) => lo + j); return <ExCell key={h} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 6px'}}>{s4wLabel(h === 'R' ? 'Right hand, going up from E♭' : 'Left hand (the same keys)')}
        <SpKb lo={lo} hi={lo + 12} W={18} H={54} lit={{}} names={Object.fromEntries(K.filter(spIsW).map(x => [x, lwLet(x)]))} k={1}/>
        <div style={{display:'flex',gap:2,justifyContent:'center'}}>{K.map(x => <span key={x}>{nvBox(i === 0, String(c345(x, h)), 22, 22)}</span>)}</div></div></ExCell>; })}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={7}/>
    <Part kind="together" title="Which note is raised?" how="Each Lydian mode is its major scale with the 4th raised a semitone. Write the raised note.">
      <BkGrid cols={2} gap="6px 10px">{W.lyd.map(([k, n], i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:10,padding:'16px 4px 6px',fontSize:13.5,fontWeight:800,color:BK.ink}}>{k} Lydian: {nvBox(i === 0, n, 50, 28)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Voices and octaves this week" how="Tick a box each day.">
      <PhLog rows={['Hold a long note with 1 while 3 4 5 move above it, each hand', 'F Lydian in octaves, each hand, light and loose', 'The book\'s exercises 7B and 7C, slowly']} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<S7PaperCheck/>);
  return <>{pages}</>;
}
function S7PaperCheck() {
  const C = S7_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the 7th note of each scale (raised in the minor)')}
    <BkGrid cols={4} gap="6px 8px">{C.minor.map(([k], i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>{S6_GR[k].en}{bkBox(44, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'Chromatic from E♭: finger 3, 4 or 5?')}
    <BkGrid cols={4} gap="6px 8px">{C.c345.map(([h, pc], i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>{(h === 'R' ? 'Right hand, ' : 'Left hand, ') + lwLet(pc)}{bkBox(36, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Contrary motion from one note: mirror twins? Y or N')}
    <BkGrid cols={2} gap="6px 8px">{C.mirror.map((k, i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:6,padding:'14px 0 0'}}><div>{s4wLabel(SCF_CM[k].en)}<ScfCmKb k={k} W={12} H={34} kk={1} bare/></div>{bkBox(30, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'The Lydian mode: which note is raised?')}
    <BkGrid cols={4} gap="6px 8px">{C.lyd.map(([k], i) => <BkCell key={i} n={i + 11}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>{k} Lydian{bkBox(44, 24)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['scales-7'] = S7Workbook;
'''
rep("""TEACHER_COPIES['scales-6'] = S6Teacher;""", """TEACHER_COPIES['scales-6'] = S6Teacher;""" + CH)
rep("""'scales-6': '스케일, Grade 6'""", """'scales-6': '스케일, Grade 6', 'scales-7': '스케일, Grade 7'""")
rep("""'scales-6': 'k-play'""", """'scales-6': 'k-play', 'scales-7': 'k-play'""")
rep("""  'scales-6': 'scales grade 6""", """  'scales-7': 'scales grade 7 d major b minor a flat major f minor abbreviated grand scale polyrhythmic three against two triplets contrary motion f sharp d sharp chromatic d g sharp a flat e flat fingers 3 4 5 two voices one hand retention lydian mode octaves dorian mode jam drone',
  'scales-6': 'scales grade 6""")
HOME = r"""
// ══ Build BU: Scales, Grade 7 on the Home (Technique, Playing scales) ══
LBH_FN['scales-7'] = (s) => s7LbPages(s);
const s7HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('scales-7', i, { make }));
const s7EarQ = (kind) => (n, prev) => { const L = { grand: S7_LEVELS[0], held: S7_LEVELS[4], lyd: S7_LEVELS[5] }[kind], q = genS7Question(L, prev);
  const opts = kind === 'grand' ? [['M', t('Major', '장조')], ['m', t('Harmonic minor', '화성 단음계')]] : kind === 'held' ? [['yes', t('Held to the end', '끝까지 붙잡았어요')], ['no', t('Let go too soon', '너무 일찍 놓았어요')]] : [['maj', t('Major', '장음계')], ['lyd', t('Lydian', '리디안')]];
  const play = () => { if (kind === 'grand') grPlay(q.k, 0, q.bpm || 80); else if (kind === 'held') voPlay(S7_VO[q.i], q.held); else lydPlay(LYD_KEYS[q.k][0], q.lyd); };
  return { kind: 'choice', cols: 2, key: q.key, prompt: kind === 'grand' ? ['Part 1 of a grand scale: major or harmonic minor?', '그랜드 스케일의 1부분: 장조? 화성 단음계?'] : kind === 'held' ? ['Two voices in one hand: was the long note held?', '한 손의 두 성부: 긴 음을 붙잡았나요?'] : ['Listen to the 4th note: major or Lydian?', '네 번째 음을 들어요: 장음계? 리디안?'],
    opts: opts.map(([id, lab]) => ({ id, label: () => lab })), ans: q.answer, ok: (v) => v === q.answer, play,
    fig: (c) => ({ mid: kind === 'grand' ? <GrRoute k={q.k} hl={c.res ? 0 : null}/> : kind === 'held' && c.res ? <VoBars x={S7_VO[q.i]} held={q.held}/> : null }),
    yes: ['Yes.', '맞아요.'], no: kind === 'grand' ? ['It was ' + S6_GR[q.k].en + '.', '정답은 ' + S6_GR[q.k].ko + '.'] : kind === 'held' ? [q.held ? 'It was held.' : 'It was let go.', q.held ? '붙잡았어요.' : '놓았어요.'] : ['It was ' + (q.lyd ? 'Lydian: the 4th raised.' : 'major.'), '정답은 ' + (q.lyd ? '리디안: 4음을 올려요.' : '장음계.')] }; };
const s7MirrorQ = (n, prev) => { const k = S7_CM_KEYS[n % 2], a = scfMirror(k) ? 'yes' : 'no';
  return { kind: 'choice', cols: 2, key: k + n, prompt: ['Contrary motion, ' + SCF_CM[k].en + ': mirror twins?', '반대 방향, ' + SCF_CM[k].ko + ': 거울 쌍둥이일까?'], opts: [{ id: 'yes', label: () => t('Mirror twins', '거울 쌍둥이') }, { id: 'no', label: () => t('Not mirror twins', '거울 쌍둥이 아님') }], ans: a, ok: (v) => v === a,
    fig: (c) => ({ mid: <ScfCmKb k={k} mark={c.res && a === 'no' ? scfFirstDiff(k) : -1}/> }), yes: ['Yes: each hand keeps its own numbers.', '맞아요: 손마다 자기 번호.'], no: ['Look again: the numbers part.', '다시 봐요: 번호가 갈라져요.'] }; };
s7HomeAdd('s7-grand', 1, 'The grand scale in four new keys', '네 새 조의 그랜드 스케일', 'D, B minor, A♭ and F minor: major or harmonic minor?', 'D, B단조, A♭, F단조: 장조? 화성 단음계?', s7EarQ('grand'));
s7HomeAdd('s7-poly', 2, 'Three against two, as a scale', '3 대 2, 스케일로', 'Three octaves against two: they meet at the top.', '세 옥타브 대 두 옥타브: 꼭대기에서 만나요.', lwTapQ(S7PolyScalePad, () => ({}), ['Guess first, then listen.', '먼저 맞혀 보고, 들어요.'], ['They meet at the top ✓', '꼭대기에서 만나요 ✓']));
s7HomeAdd('s7-mirror', 3, 'Contrary motion: the Grade 7 keys', '반대 방향: 7급 조', 'F♯ major and D♯ minor: mirror twins?', 'F♯장조와 D♯단조: 거울 쌍둥이?', s7MirrorQ);
s7HomeAdd('s7-chrom', 4, 'Chromatic from D and A♭', 'D와 A♭에서 반음계', 'Where do the hands use different fingers?', '두 손의 번호가 다른 곳은?', lwTapQ(S7ChromPad, (n) => ({ fixed: n % 2 }), ['Tap every key where the fingers differ.', '번호가 다른 건반을 모두 눌러요.'], ['Found them ✓', '찾았어요 ✓']));
s7HomeAdd('s7-345', 5, 'Chromatic from E♭: 3, 4 and 5', 'E♭ 반음계: 3, 4, 5번', 'Black keys 3, white 4, the outer white 5.', '검은건반 3, 흰건반 4, 바깥 흰건반 5.', lwTapQ(S7Ch345Pad, (n) => ({ fixed: { h: n % 2 ? 'L' : 'R' } }), ['Tap every key finger 5 plays.', '5번이 치는 건반을 모두 눌러요.'], ['Found them ✓', '찾았어요 ✓']));
s7HomeAdd('s7-voices', 6, 'Two voices in one hand', '한 손에 두 성부', 'Was the long note held, or let go?', '긴 음을 붙잡았을까, 놓았을까?', s7EarQ('held'));
s7HomeAdd('s7-lyd', 7, 'The Lydian mode', '리디안 선법', 'A major scale with its 4th raised: hear it.', '4음을 올린 장음계: 들어 봐요.', s7EarQ('lyd'));
"""
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""    { id: 'kpl-a6', en: 'Arpeggios and progressions, Grade 6', ko: '아르페지오와 화음 진행, Grade 6', lessons: ['a6-walk', 'a6-arp', 'a6-dom', 'a6-dim', 'mk-wave'], check: 'arps-6' },   // Build BQ""",
    """    { id: 'kpl-a6', en: 'Arpeggios and progressions, Grade 6', ko: '아르페지오와 화음 진행, Grade 6', lessons: ['a6-walk', 'a6-arp', 'a6-dom', 'a6-dim', 'mk-wave'], check: 'arps-6' },   // Build BQ
    { id: 'kpl-7', en: 'Scales, Grade 7', ko: '스케일, Grade 7', lessons: ['s7-grand', 's7-poly', 's7-mirror', 's7-chrom', 's7-345', 's7-voices', 's7-lyd', 'mk-mode'], check: 'scales-7' },   // Build BU""")
rep("""  set('6', 's6-four s6-dyn s6-grand s6-ls s6-mirror s6-poly mk-poly');   // Build BP: Scales, Grade 6""", """  set('6', 's6-four s6-dyn s6-grand s6-ls s6-mirror s6-poly mk-poly');   // Build BP: Scales, Grade 6
  set('7', 's7-grand s7-poly s7-mirror s7-chrom s7-345 s7-voices s7-lyd mk-mode');   // Build BU: Scales, Grade 7""")
rep("""  { id: 'mk-cad', ch: 'listen-6',""", """  { id: 'mk-mode', ch: 'scales-7', title: 'My mode jam', blurb: 'White keys only, a new home on a drone: Dorian, Lydian, Mixolydian; make it up as you go.', C: () => <ModeJam/> },   // Build BU
  { id: 'mk-cad', ch: 'listen-6',""")
rep("""  'mk-cad': ['나만의 끝 만들기',""", """  'mk-mode': ['나의 선법 잼', '흰건반만, 드론 위의 새 집: 도리안, 리디안, 믹솔리디안; 마음대로 즉흥 연주.'],
  'mk-cad': ['나만의 끝 만들기',""")
rep("""'mk-cad': ['chords', 3, 3, 'game ear'],""", """'mk-cad': ['chords', 3, 3, 'game ear'], 'mk-mode': ['scales', 3, 3, 'game ear'],""")
rep("""'mk-cad': 'p-chords',""", """'mk-cad': 'p-chords', 'mk-mode': 'p-scales',""")
rep("""  'mk-cad': () => (\n""", """  'mk-mode': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><rect x="3" y="7" width="18" height="11" rx="1.5" fill="#fefbf3"/>{[6, 9, 12, 15, 18].map(x => <path key={x} d={'M' + x + ' 7 V18'} stroke="#3b4fa8" strokeWidth="0.8"/>)}<rect x="9.2" y="7.4" width="2.6" height="10.2" fill="#e9a83a"/><path d="M3 21 H21" stroke="#e9a83a" strokeWidth="1.6"/></svg>
  ),
  'mk-cad': () => (\n""")
rep("""const LESSON_BOOKS = { 'listen-7': Listen7LessonBook,""", """const LESSON_BOOKS = { 'scales-7': Scales7LessonBook, 'listen-7': Listen7LessonBook,""")
rep("""const LB_PAGE_FNS = { 'listen-7': l7LbPages,""", """const LB_PAGE_FNS = { 'scales-7': s7LbPages, 'listen-7': l7LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"scales-7": "<path d=\\"M4 38 L24 6 L44 38\\" stroke=\\"#e4572e\\" stroke-width=\\"2.6\\"/><path d=\\"M4 42 L24 24 L44 42\\"/><text x=\\"20\\" y=\\"30\\" font-size=\\"11\\" font-weight=\\"900\\" fill=\\"#26296b\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">3</text>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
