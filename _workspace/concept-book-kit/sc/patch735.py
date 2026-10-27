import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BP (board call 26, the second Grade 6 room): Scales, Grade 6. From the technical work book, Grade 6 (pp25-41, read 28
# Oct): scales four octaves, hands separately and together, clear even legato, crotchet 92 four notes a beat, F-sharp major, D-sharp
# harmonic and melodic minor, each (i) all p, (ii) all f, (iii) p < f ascending, f > p descending; the chromatic scale from
# F-sharp/G-flat the same; the ABBREVIATED GRAND SCALE FORMAT (hands together an octave apart: similar motion up two octaves,
# contrary motion out and back, similar motion down; the footnote's definition, p32) in E-flat major and C harmonic minor, four
# octaves, mf, crotchet 76; the LEGATO AND STACCATO COMBINATION (one hand staccato, the other legato, then swapped) in F-sharp major
# and D-sharp melodic minor, mf, crotchet 72; contrary motion two octaves in B major, G-sharp harmonic minor, D-flat major and
# B-flat harmonic minor, mf, crotchet 72; exercise 6B's skill, three against two (the book's own way in: "both right-left-right").
# The I-V-I progressions and the arpeggios are the next room (Arpeggios and Progressions, Grade 6).

rep("""const SCALES_5_DRILL = { id: 'scales-5', label: 'Scales and Arpeggios, Grade 5' };   // Build BA""",
    """const SCALES_5_DRILL = { id: 'scales-5', label: 'Scales and Arpeggios, Grade 5' };   // Build BA
const SCALES_6_DRILL = { id: 'scales-6', label: 'Scales, Grade 6' };   // Build BP""")
rep("""  { id: 'scales-5', label: 'Scales and Arpeggios, Grade 5', concept: SCALES_5_DRILL, track: 'start' },   // Build BA""",
    """  { id: 'scales-5', label: 'Scales and Arpeggios, Grade 5', concept: SCALES_5_DRILL, track: 'start' },   // Build BA
  { id: 'scales-6', label: 'Scales, Grade 6', concept: SCALES_6_DRILL, track: 'start' },   // Build BP""")
rep("""'scales-5': '스케일과 아르페지오, Grade 5'""", """'scales-5': '스케일과 아르페지오, Grade 5', 'scales-6': '스케일, Grade 6'""")
rep("""'scales-5': 'k-play'""", """'scales-5': 'k-play', 'scales-6': 'k-play'""")
rep("""'scales-5': ['scales-4']""", """'scales-5': ['scales-4'], 'scales-6': ['scales-5']""")
rep("""  'scales-5': 'scales arpeggios grade 5""", """  'scales-6': 'scales grade 6 f sharp major d sharp minor four octaves finger 4 dynamics p f crescendo diminuendo abbreviated grand scale format russian legato staccato combination contrary motion mirror twins chromatic three against two polyrhythm triplets duplets',
  'scales-5': 'scales arpeggios grade 5""")
rep("""'scales-5': ['Scales 5', '스케일 5']""", """'scales-5': ['Scales 5', '스케일 5'], 'scales-6': ['Scales 6', '스케일 6']""")

CH = r'''
// ─── Chapter: Scales, Grade 6 (Build BP, 2026-10-28; board call 26, the second Grade 6 room) ───
// What Grade 6 adds: F♯ major and D♯ minor (in all three, the right hand's 4 is A♯ and the left hand's 4 is F♯); the same three
// dynamics at ♩ = 92; the abbreviated grand scale (together up, apart, back together, together down); one hand legato and the
// other staccato; contrary motion in the Grade 5 keys; and three against two, the skill of exercise 6B. The keys, speeds and
// fingerings are the technical work book's (Grade 6 pp25-41).
Object.assign(S4_SC, {   // four octaves going up, as the book's two printed octaves repeat (Grade 6 p31)
  Fs: { en: 'F♯ major', ko: 'F♯장조', st: SP_MAJ, r: 6, nm: ['F♯', 'G♯', 'A♯', 'B', 'C♯', 'D♯', 'E♯'], R: s4Run([2, 3, 4, 1, 2, 3, 1], [2, 3, 4, 1, 2, 3, 1], 2), L: s4Run([4, 3, 2, 1, 3, 2, 1], [4, 3, 2, 1, 3, 2, 1], 2) },
  Dsm: { en: 'D♯ harmonic minor', ko: 'D♯ 화성 단음계', chip: ['D♯m harmonic', 'D♯m 화성'], st: SP_HAR, r: 3, nm: ['D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B', 'C𝄪'], R: s4Run([2, 1, 2, 3, 4, 1, 2], [3, 1, 2, 3, 4, 1, 2], 3), L: s4Run([2, 1, 4, 3, 2, 1, 3], [2, 1, 4, 3, 2, 1, 3], 2) },
  Dsmel: { en: 'D♯ melodic minor', ko: 'D♯ 가락 단음계', chip: ['D♯m melodic', 'D♯m 가락'], st: S4_MEL, dn: SP_NAT, r: 3, nm: ['D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B♯', 'C𝄪'], R: s4Run([2, 1, 2, 3, 4, 1, 2], [3, 1, 2, 3, 4, 1, 2], 3), L: s4Run([2, 1, 4, 3, 2, 1, 3], [2, 1, 4, 3, 2, 1, 3], 2) },
});
const S6_KEYS = ['Fs', 'Dsm', 'Dsmel'];
Object.assign(S4_ST, {   // two octaves up and down, for the three ways and for legato with staccato
  Fs: { en: 'F♯ major', ko: 'F♯장조', r: -6, up: SP_MAJ, dn: SP_MAJ, nmU: ['F♯', 'G♯', 'A♯', 'B', 'C♯', 'D♯', 'E♯'], nmD: ['F♯', 'G♯', 'A♯', 'B', 'C♯', 'D♯', 'E♯'] },
  Dsm: { en: 'D♯ harmonic minor', ko: 'D♯ 화성 단음계', r: -9, up: SP_HAR, dn: SP_HAR, nmU: ['D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B', 'C𝄪'], nmD: ['D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B', 'C𝄪'] },
  Dsmel: { en: 'D♯ melodic minor', ko: 'D♯ 가락 단음계', r: -9, up: S4_MEL, dn: SP_NAT, nmU: ['D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B♯', 'C𝄪'], nmD: ['D♯', 'E♯', 'F♯', 'G♯', 'A♯', 'B', 'C♯'] },
});
Object.assign(SCF_CM, {   // contrary motion, the first octave of two (Grade 6 p34): the Grade 5 similar-motion keys
  B6: { g: 6, en: 'B major', ko: 'B장조', st: SP_MAJ, s: -1, nm: ['B', 'C♯', 'D♯', 'E', 'F♯', 'G♯', 'A♯'], R: [1, 2, 3, 1, 2, 3, 4, 1], L: [1, 2, 3, 4, 1, 2, 3, 1] },
  Gsmh6: { g: 6, en: 'G♯ harmonic minor', ko: 'G♯ 화성 단음계', st: SP_HAR, s: 8, nm: ['G♯', 'A♯', 'B', 'C♯', 'D♯', 'E', 'F𝄪'], R: [2, 3, 1, 2, 3, 1, 2, 3], L: [2, 1, 2, 3, 4, 1, 2, 3] },
  Db6: { g: 6, en: 'D♭ major', ko: 'D♭장조', st: SP_MAJ, s: 1, nm: ['D♭', 'E♭', 'F', 'G♭', 'A♭', 'B♭', 'C'], R: [2, 3, 1, 2, 3, 4, 1, 2], L: [2, 1, 2, 3, 4, 1, 2, 3] },
  Bbmh6: { g: 6, en: 'B♭ harmonic minor', ko: 'B♭ 화성 단음계', st: SP_HAR, s: -2, nm: ['B♭', 'C', 'D♭', 'E♭', 'F', 'G♭', 'A'], R: [2, 1, 2, 3, 1, 2, 3, 4], L: [2, 3, 4, 1, 2, 3, 1, 2] },
});
const S6_CM_KEYS = ['B6', 'Gsmh6', 'Db6', 'Bbmh6'];
const s6CmChip = (k) => ({ B6: 'B', Gsmh6: 'G♯m', Db6: 'D♭', Bbmh6: 'B♭m' })[k];
function S6FourPad(p) { return <S4FourPad keys={S6_KEYS} bpm={92} {...p}/>; }
function S6MirrorPad(p) { return <S4MirrorPad keys={S6_CM_KEYS} chip={s6CmChip} bpm={72} g={6} {...p}/>; }

// ── step 2: three ways at ♩ = 92: all p, all f, louder up and softer down ──
const S6_WAYS = ['p', 'f', 'cd'];
const s6PlayWay = (k, m, bpm = 92) => { const ctx = getAudio(); if (!ctx) return null; stopClicks();
  const sq = s4Two(k), n = sq.length, spb = 60 / bpm, t0 = ctx.currentTime + 0.15;
  for (let b = 0; b < 4; b++) metroClick(ctx, t0 + b * spb, false, 0.25);
  sq.forEach((x, j) => blip(ctx, t0 + (4 + j / 4) * spb, spHz(x.i), j === n - 1 ? spb * 1.5 : spb / 4 * 0.98, 0.05 + 0.21 * s5Lv(m, j, n), 'triangle'));
  return { n, ms: (beat) => (0.15 + (4 + beat) * spb) * 1000, end: (0.15 + (4 + n / 4 + 1.5) * spb) * 1000 }; };
function S6WaysPad({ onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState('Fs'), [m, setM] = useState('cd'), [cur, setCur] = useState(-1), [quiz, setQuiz] = useState(null), [ans, setAns] = useState(null);
  const last = useRef(null);
  const reset = (fn) => { T.clear(); setCur(-1); setQuiz(null); setAns(null); if (fn) fn(); };
  const hear = (kk, mm) => { T.clear(); setCur(-1); const r = s6PlayWay(kk, mm); if (!r) return; for (let j = 0; j < r.n; j++) T.at(r.ms(j / 4), () => setCur(j)); T.at(r.end, () => setCur(-1)); };
  const way = (x) => { if (quiz) { if (ans) return; T.clear(); setCur(-1); setAns(x); if (onResult) onResult({ ok: x === quiz }); return; } setM(x); hear(k, x); };
  const ask = () => { let x, g = 0; do { x = pick(S6_WAYS); } while (x === last.current && g++ < 10); last.current = x; setQuiz(x); setAns(null); hear(k, x); };
  const shown = quiz ? (ans ? quiz : null) : m, ok = !!ans && ans === quiz;
  return (
    <div className="try-box" style={actBox} data-s6="ways">
      <div style={actTitle}>{t('Three ways, four octaves', '세 가지로, 네 옥타브')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>6급 스케일도 <b>세 가지로</b>: 모두 <b>p</b>, 모두 <b>f</b>, 그리고 <b>올라가며 세게, 내려오며 여리게</b>, 이제 {spMM(92)}. F♯에서 시작하는 반음계도 똑같이 세 가지로. <b>줄이 굵을수록 세게.</b></>
        : <>Grade 6 scales are played <b>three ways</b> too: all <b>p</b>, all <b>f</b>, and <b>louder going up, softer coming down</b>, now at {spMM(92)}. The chromatic scale from F♯ is played the same three ways. <b>The thicker the line, the louder.</b></>}</div>
      {spChips(S6_KEYS.map(x => [x, s4Chip(x)]), k, (x) => reset(() => setK(x)))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 0'}}>{t(S4_ST[k].en, S4_ST[k].ko)} · {shown ? <>{s5WayName(shown)} · {spMM(92)}</> : '?'}</div>
      <div style={{maxWidth:420,margin:'2px auto 6px'}}><S5Ribbon m={shown} cur={cur}/></div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6}}>{S6_WAYS.map(x => <button key={x} className={'choice-btn' + (quiz && ans ? (x === quiz ? ' good' : x === ans ? ' bad' : '') : '')} aria-pressed={!quiz && x === m}
        style={{padding:'8px 4px 10px',fontSize:12.5,fontWeight:900,display:'grid',gap:2,justifyItems:'center',lineHeight:1.2,boxShadow:!quiz && x === m ? 'inset 0 0 0 2px #26296b' : 'none'}} onClick={() => way(x)}><S5Ribbon m={x} w={100} marks={false}/><span>{s5WayName(x)}</span></button>)}</div>
      {spMsg(ans ? (ok ? t(S5_YES[quiz][0], S5_YES[quiz][1]) : t('Not quite: it was “' + S5_WAY[quiz][0] + '”. The four clicks are always the same: compare with them.', '아니에요: “' + S5_WAY[quiz][1] + '”였어요. 클릭 넷은 언제나 같은 크기: 견주어 봐요.'))
        : quiz ? t('Listen: which way? The four clicks are your yardstick.', '들어 봐요: 어느 것? 클릭 넷이 잣대예요.') : t('Tap a way to hear it. Then ▶ Which one?', '하나를 눌러 들어 봐요. 그다음 ▶ 어느 것일까?'), ans ? (ok ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {quiz && !ans ? <button className="ghost-btn" style={spBtn} onClick={() => hear(k, quiz)}>{t('▶ Play it again', '▶ 다시 듣기')}</button>
          : <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which one?', '▶ 어느 것일까?')}</button>}
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('Back to all three', '세 가지 다시 보기')}</button>}
      </div>
    </div>
  );
}

// ── step 3: the abbreviated grand scale: together up, apart, back together, together down ──
// hands an octave apart, the right hand starting an octave above the left; each leg two octaves, the turning note shared
const S6_GR = {
  Eb: { en: 'E♭ major', ko: 'E♭장조', st: SP_MAJ, r: -9, nm: ['E♭', 'F', 'G', 'A♭', 'B♭', 'C', 'D'] },
  Cmh: { en: 'C harmonic minor', ko: 'C 화성 단음계', st: SP_HAR, r: -12, nm: ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B'] },
};
const GR_LEGS = [['Together, up', '함께 올라가요'], ['Apart', '멀어져요'], ['Back together', '다시 모여요'], ['Together, down', '함께 내려와요']];
const GR_ARROWS = [['↗', '↗'], ['↗', '↘'], ['↘', '↗'], ['↘', '↘']];   // [right hand, left hand]
const grSeq = (k) => { const c = S6_GR[k], deg = (o) => c.r + 12 * Math.floor(o / 7) + c.st[((o % 7) + 7) % 7];
  const LR = [[0, 1], [14, 1], [28, -1], [14, -1]], LL = [[-7, 1], [7, -1], [-7, 1], [7, -1]], R = [], L = [], leg = [];
  for (let g = 0; g < 4; g++) for (let j = g ? 1 : 0; j <= 14; j++) { R.push(deg(LR[g][0] + LR[g][1] * j)); L.push(deg(LL[g][0] + LL[g][1] * j)); leg.push(g); }
  return { R, L, leg }; };
const grPlay = (k, only = null, bpm = 76) => { const S = grSeq(k), ix = S.R.map((_, i) => i).filter(i => only == null || S.leg[i] === only || (i === only * 14 && only > 0));
  return { run: spPlay(ix.map((i, n) => ({ at: n / 4, keys: [S.R[i], S.L[i]], len: n === ix.length - 1 ? 1.5 : 0.25, vol: 0.12 })), bpm, only == null ? 4 : 0), ix }; };
function GrRoute({ k, cur = -1, hl = null, w = 340 }) {   // the two hands' paths: the right hand coral, the left navy
  const S = grSeq(k), lo = Math.min(...S.L), hi = Math.max(...S.R), X = (i) => 14 + i / 56 * 312, Y = (v) => 104 - (v - lo) / (hi - lo) * 88;
  let svg = '';
  [14, 28, 42].forEach(i => { svg += '<path d="M' + X(i).toFixed(1) + ' 10 V114" stroke="rgba(38,41,107,0.25)" stroke-width="1" stroke-dasharray="3 3"/>'; });
  if (hl != null) svg += '<rect x="' + X(hl * 14).toFixed(1) + '" y="8" width="' + (X(14) - X(0)).toFixed(1) + '" height="108" fill="#fbe3da"/>';
  const path = (A, c) => '<path d="' + A.map((v, i) => (i ? 'L' : 'M') + X(i).toFixed(1) + ' ' + Y(v).toFixed(1)).join(' ') + '" fill="none" stroke="' + c + '" stroke-width="2.6" stroke-linejoin="round"/>';
  svg += path(S.L, '#26296b') + path(S.R, '#e4572e');
  [0, 1, 2, 3].forEach(g => { svg += '<text x="' + X(g * 14 + 7).toFixed(1) + '" y="126" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#26296b">' + (g + 1) + '</text>'; });
  if (cur >= 0) svg += '<circle cx="' + X(cur).toFixed(1) + '" cy="' + Y(S.R[cur]).toFixed(1) + '" r="5" fill="#e4572e" stroke="#fff" stroke-width="1.5"/><circle cx="' + X(cur).toFixed(1) + '" cy="' + Y(S.L[cur]).toFixed(1) + '" r="5" fill="#26296b" stroke="#fff" stroke-width="1.5"/>';
  return <svg viewBox="0 0 340 132" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t('The grand scale: the right hand above, the left hand below', '그랜드 스케일: 위는 오른손, 아래는 왼손')} dangerouslySetInnerHTML={{ __html: svg }}/>;
}
const grLegLab = (g) => <span style={{display:'grid',gap:1,justifyItems:'center'}}><span style={{fontSize:15,letterSpacing:2}}><span style={{color:BK.coral}}>{GR_ARROWS[g][0]}</span><span style={{color:BK.ink}}>{GR_ARROWS[g][1]}</span></span><span>{t(GR_LEGS[g][0], GR_LEGS[g][1])}</span></span>;
function S6GrandPad({ onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState('Eb'), [cur, setCur] = useState(-1), [hl, setHl] = useState(null), [deck, setDeck] = useState(() => shuffle([0, 1, 2, 3])), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [bad, setBad] = useState(null);
  const done = got >= 4;
  const run = (only) => { T.clear(); setCur(-1); setHl(only); const r = grPlay(k, only); if (!r.run) return; r.ix.forEach((i, n) => T.at(r.run.ms(n / 4), () => setCur(i))); T.at(r.run.ms(r.ix.length / 4 + 1), () => { setCur(-1); setHl(null); }); };
  const card = (g) => { if (done) return; if (g === got) { const ng = got + 1; setGot(ng); setBad(null); run(g); if (ng >= 4 && onResult) onResult({ ok: miss === 0 }); } else { setBad(g); setMiss(m => m + 1); } };
  const again = () => { T.clear(); setCur(-1); setHl(null); setDeck(shuffle([0, 1, 2, 3])); setGot(0); setMiss(0); setBad(null); };
  return (
    <div className="try-box" style={actBox} data-s6="grand">
      <div style={actTitle}>{t('The abbreviated grand scale', '줄인 그랜드 스케일')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>양손이 한 옥타브 떨어져서. <b>1</b> 함께 두 옥타브 올라가요. <b>2</b> 오른손은 계속 올라가고 왼손은 내려와요: 멀어져요(반대 방향). <b>3</b> 다시 모여요. <b>4</b> 함께 내려와요. 위의 줄이 오른손, 아래 줄이 왼손. {spMM(76)}, mf.</>
        : <>Hands an octave apart. <b>1</b> Together up two octaves. <b>2</b> The right hand carries on up while the left comes down: apart (contrary motion). <b>3</b> Back together. <b>4</b> Together down. The top line is the right hand, the bottom the left. {spMM(76)}, mf.</>}</div>
      {spChips(Object.keys(S6_GR).map(x => [x, t(S6_GR[x].en, S6_GR[x].ko)]), k, (x) => { T.clear(); setCur(-1); setHl(null); setK(x); })}
      <GrRoute k={k} cur={cur} hl={hl}/>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:5,marginTop:6}}>{[0, 1, 2, 3].map(g => <button key={g} className="chip" onClick={() => run(g)} style={{padding:'6px 2px',fontSize:11.5,fontWeight:800,lineHeight:1.15,minHeight:52,whiteSpace:'normal',borderRadius:10}}>{grLegLab(g)}</button>)}</div>
      <div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink,margin:'12px 0 4px'}}>{t('Your turn: put the four parts in order', '내 차례: 네 부분을 순서대로')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:5}}>{[0, 1, 2, 3].map(g => <div key={g} style={{minHeight:52,border:'1.5px dashed rgba(38,41,107,0.35)',borderRadius:8,display:'flex',alignItems:'center',justifyContent:'center',fontSize:11.5,fontWeight:800,color:g < got ? BK.green : BK.muted,background:g < got ? '#fff' : 'transparent',textAlign:'center',padding:2}}>{g < got ? grLegLab(g) : g + 1}</div>)}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:5,marginTop:6}}>{deck.map(g => <button key={g} className={'choice-btn' + (bad === g ? ' bad' : '')} disabled={g < got} onClick={() => card(g)} style={{padding:'6px 2px',fontSize:11.5,fontWeight:800,lineHeight:1.15,minHeight:52,opacity:g < got ? 0.25 : 1}}>{grLegLab(g)}</button>)}</div>
      {spMsg(done ? t(miss ? 'In order: together up, apart, back together, together down.' : 'First time! Together up, apart, back together, together down.', miss ? '순서대로: 함께 올라가고, 멀어지고, 다시 모이고, 함께 내려와요.' : '한 번에! 함께 올라가고, 멀어지고, 다시 모이고, 함께 내려와요.') : bad != null ? t('Not yet: which comes ' + ['first', 'second', 'third', 'last'][got] + '?', '아직이에요: ' + ['첫째', '둘째', '셋째', '마지막'][got] + '는?') : t('Which comes ' + ['first', 'second', 'third', 'last'][got] + '?', ['첫째', '둘째', '셋째', '마지막'][got] + '는?'), done ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => run(null)}>{t('▶ The whole grand scale', '▶ 그랜드 스케일 전체')}</button>
        {done && <button className="ghost-btn" style={spBtn} onClick={again}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── step 4: one hand legato, the other staccato (and then swapped) ──
const S6_LS_KEYS = ['Fs', 'Dsmel'];
const s6LsPlay = (k, stac, bpm = 72) => { const ctx = getAudio(); if (!ctx) return null; stopClicks();
  const sq = s4Two(k), n = sq.length, spb = 60 / bpm, t0 = ctx.currentTime + 0.15;
  for (let b = 0; b < 4; b++) metroClick(ctx, t0 + b * spb, false, 0.25);
  sq.forEach((x, j) => ['R', 'L'].forEach(h => { const st = stac === h, len = st ? spb * 0.07 : j === n - 1 ? spb * 1.5 : spb / 4 * 0.98; blip(ctx, t0 + (4 + j / 4) * spb, spHz(x.i + (h === 'L' ? -12 : 0)), len, st ? 0.2 : 0.12, 'triangle'); }));
  return { n, ms: (beat) => (0.15 + (4 + beat) * spb) * 1000, end: (0.15 + (4 + n / 4 + 1.5) * spb) * 1000 }; };
function S6LsRows({ stac, cur = -1, w = 320 }) {   // the right hand on top, the left below; a joined line is legato, loose dots are staccato
  const n = 29, X = (j) => (14 + j * 292 / (n - 1)).toFixed(1), H = (j) => (j <= 14 ? j : 28 - j) * 1.7;
  let svg = '';
  [['R', 40, '#e4572e'], ['L', 98, '#26296b']].forEach(([h, y0, c]) => { const Y = (j) => (y0 - H(j)).toFixed(1);
    if (stac !== h) svg += '<path d="' + Array.from({ length: n }, (_, j) => (j ? 'L' : 'M') + X(j) + ' ' + Y(j)).join(' ') + '" fill="none" stroke="' + c + '" stroke-width="2.6" stroke-linejoin="round"/>';
    for (let j = 0; j < n; j++) svg += '<circle cx="' + X(j) + '" cy="' + Y(j) + '" r="' + (stac === h ? 2.6 : 2.2) + '" fill="' + c + '"/>';
    svg += '<text x="4" y="' + (y0 + 14) + '" font-family="Inter, sans-serif" font-size="10.5" font-weight="900" fill="' + c + '">' + (h === 'R' ? t('RH', '오른손') : t('LH', '왼손')) + ' · ' + (stac === h ? 'stacc.' : 'legato') + '</text>';
    if (cur >= 0) svg += '<circle cx="' + X(cur) + '" cy="' + Y(cur) + '" r="5" fill="' + c + '" stroke="#fff" stroke-width="1.5"/>'; });
  return <svg viewBox="0 0 320 120" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t('Two hands: legato and staccato', '두 손: 레가토와 스타카토')} dangerouslySetInnerHTML={{ __html: svg }}/>;
}
function S6LsPad({ onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState('Fs'), [stac, setStac] = useState('R'), [cur, setCur] = useState(-1), [quiz, setQuiz] = useState(null), [ans, setAns] = useState(null);
  const reset = (fn) => { T.clear(); setCur(-1); setQuiz(null); setAns(null); if (fn) fn(); };
  const hear = (kk, st) => { T.clear(); setCur(-1); const r = s6LsPlay(kk, st); if (!r) return; for (let j = 0; j < r.n; j++) T.at(r.ms(j / 4), () => setCur(j)); T.at(r.end, () => setCur(-1)); };
  const ask = () => { const x = Math.random() < 0.5 ? 'R' : 'L'; setQuiz(x); setAns(null); hear(k, x); };
  const say = (h) => { if (!quiz || ans) return; T.clear(); setCur(-1); setAns(h); if (onResult) onResult({ ok: h === quiz }); };
  const shown = quiz ? (ans ? quiz : null) : stac, ok = !!ans && ans === quiz;
  return (
    <div className="try-box" style={actBox} data-s6="ls">
      <div style={actTitle}>{t('One hand legato, the other staccato', '한 손은 레가토, 다른 손은 스타카토')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>F♯장조와 D♯ 가락 단음계, 네 옥타브, mf, {spMM(72)}. (i) <b>오른손 스타카토, 왼손 레가토</b>, 그다음 (ii) 바꿔서. 손가락은 같고, 한 손은 짧게 튀고 다른 손은 이어서 노래해요. 이어진 줄은 레가토, 떨어진 점은 스타카토.</>
        : <>F♯ major and D♯ melodic minor, four octaves, mf, {spMM(72)}. (i) <b>Right hand staccato, left hand legato</b>, then (ii) swapped. The same fingers: one hand bounces short while the other sings joined. A joined line is legato; loose dots are staccato.</>}</div>
      {spChips(S6_LS_KEYS.map(x => [x, t(S4_ST[x].en, S4_ST[x].ko)]), k, (x) => reset(() => setK(x)))}
      {!quiz && spChips([['R', t('(i) Right hand staccato', '(i) 오른손 스타카토')], ['L', t('(ii) Left hand staccato', '(ii) 왼손 스타카토')]], stac, (x) => { reset(() => setStac(x)); hear(k, x); })}
      {shown ? <S6LsRows stac={shown} cur={cur}/> : <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.muted,margin:'18px 0'}}>{t('Listen: which hand is short?', '들어 봐요: 어느 손이 짧을까요?')}</div>}
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{[['R', t('Right hand staccato', '오른손 스타카토')], ['L', t('Left hand staccato', '왼손 스타카토')]].map(([h, lab]) => <button key={h} className="choice-btn" onClick={() => say(h)} style={{padding:'12px 4px',fontSize:14.5,fontWeight:900}}>{lab}</button>)}</div>}
      {spMsg(ans ? (ok ? t('Yes: the ' + (quiz === 'R' ? 'right' : 'left') + ' hand short, the ' + (quiz === 'R' ? 'left' : 'right') + ' hand joined.', '맞아요: ' + (quiz === 'R' ? '오른손' : '왼손') + '은 짧게, ' + (quiz === 'R' ? '왼손' : '오른손') + '은 이어서.') : t('It was the ' + (quiz === 'R' ? 'right' : 'left') + ' hand: listen to the ' + (quiz === 'R' ? 'high' : 'low') + ' notes.', (quiz === 'R' ? '오른손' : '왼손') + '이었어요: ' + (quiz === 'R' ? '높은' : '낮은') + ' 음을 들어 봐요.'))
        : quiz ? t('The high line is the right hand, the low line the left.', '높은 줄이 오른손, 낮은 줄이 왼손.') : t('Tap (i) or (ii) to hear it. Then ▶ Which hand?', '(i)이나 (ii)를 눌러 들어 봐요. 그다음 ▶ 어느 손?'), ans ? (ok ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {quiz && !ans ? <button className="ghost-btn" style={spBtn} onClick={() => hear(k, quiz)}>{t('▶ Play it again', '▶ 다시 듣기')}</button>
          : <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which hand?', '▶ 어느 손?')}</button>}
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('Back to (i) and (ii)', '(i)과 (ii) 다시 보기')}</button>}
      </div>
    </div>
  );
}

// ── step 6: three against two (exercise 6B's skill): "both, right, left, right" ──
const PP_RAT = { '3:2': [3, 2], '2:3': [2, 3], '4:3': [4, 3] };   // notes a beat: [right hand, left hand]
const ppGcd = (a, b) => (b ? ppGcd(b, a % b) : a);
const ppGrid = (r) => { const [a, b] = PP_RAT[r], n = a * b / ppGcd(a, b); return Array.from({ length: n }, (_, sl) => ({ R: sl % (n / a) === 0, L: sl % (n / b) === 0 })).map(x => ({ ...x, on: x.R || x.L })); };
const ppWord = (x) => (x.R && x.L ? t('both', '함께') : x.R ? t('right', '오') : t('left', '왼'));
const ppLet = (x) => (x.R && x.L ? t('B', '양') : x.R ? t('R', '오') : t('L', '왼'));   // the grid's letters, as the book writes them (B = both)
const PP_SND = { piano: ['Piano', '피아노'], drums: ['Drums', '드럼'], bells: ['Bells', '종'] };
const ppHit = (ctx, at, h, snd) => { if (snd === 'drums') bodyHit(ctx, at, h === 'R' ? 'clap' : 'stamp', 0.55); else if (snd === 'bells') blip(ctx, at, h === 'R' ? 1568 : 523, 0.35, 0.14, 'sine'); else blip(ctx, at, spHz(h === 'R' ? 19 : -12), 0.22, 0.17, 'triangle'); };
function PolyPad({ ratios = ['3:2', '2:3'], toy = false, onResult, startOwn = false }) {
  const T = useSpTimers();
  const [rat, setRat] = useState(ratios[0]), [bpm, setBpm] = useState(toy ? 70 : 50), [snd, setSnd] = useState('piano'), [phase, setPhase] = useState('ready'), [slot, setSlot] = useState(-1), [res, setRes] = useState(null), [guide, setGuide] = useState(!startOwn);
  const taps = useRef({ R: [], L: [] }), t0 = useRef(0), G = ppGrid(rat), n = G.length, beats = 4;
  const reset = (fn) => { T.clear(); setPhase('ready'); setSlot(-1); setRes(null); if (fn) fn(); };
  const sched = (lead, sound) => { const ctx = getAudio(); if (!ctx) return null; stopClicks(); const spb = 60 / bpm, start = ctx.currentTime + 0.15 + lead * spb;
    for (let b = 0; b < lead; b++) metroClick(ctx, ctx.currentTime + 0.15 + b * spb, b === 0, 0.3);
    for (let b = 0; b < beats; b++) { metroClick(ctx, start + b * spb, b === 0, sound ? 0.12 : 0.22); G.forEach((x, sl) => { const at = start + (b + sl / n) * spb; if (sound) { if (x.R) ppHit(ctx, at, 'R', snd); if (x.L) ppHit(ctx, at, 'L', snd); } }); }
    for (let i = 0; i < beats * n; i++) T.at((start - ctx.currentTime + i / n * spb) * 1000, () => setSlot(i % (2 * n)));
    T.at((start - ctx.currentTime + beats * spb) * 1000 + 150, () => setSlot(-1));
    return { ctx, start, spb }; };
  const listen = () => { reset(); const r = sched(0, true); if (!r) return; setPhase('listen'); T.at((r.start - r.ctx.currentTime + beats * r.spb) * 1000 + 200, () => setPhase('ready')); };
  const go = () => { reset(); taps.current = { R: [], L: [] }; const r = sched(4, guide); if (!r) return; t0.current = r.start; setPhase('tap');
    T.at((r.start - r.ctx.currentTime + beats * r.spb) * 1000 + 250, () => { const exp = { R: [], L: [] };
      for (let b = 0; b < beats; b++) G.forEach((x, sl) => { if (x.R) exp.R.push(r.start + (b + sl / n) * r.spb); if (x.L) exp.L.push(r.start + (b + sl / n) * r.spb); });
      const tol = Math.min(PL_TOL, r.spb / n * 0.9 + 0.03), mR = plMatch(exp.R, taps.current.R, tol), mL = plMatch(exp.L, taps.current.L, tol);
      const ok = mR.hits >= mR.total - 1 && mL.hits >= mL.total - 1 && mR.extra + mL.extra <= 2; setRes({ R: mR, L: mL, ok }); setPhase('done'); if (ok && onResult && !guide) onResult({ ok: true }); else if (onResult && !guide) onResult({ ok: false }); }); };
  const hit = (h) => { const ctx = getAudio(); if (!ctx) return; ppHit(ctx, ctx.currentTime, h, snd); if (phase === 'tap') taps.current[h].push(ctx.currentTime); };
  const cell = (x, i, row) => { const on = row === 'R' ? x.R : x.L, now = slot === i; return <div key={i} style={{display:'flex',justifyContent:'center',alignItems:'center',height:26}}>{on ? <span style={{width:(now ? 22 : 18) / (n > 6 ? 2 : 1),height:(now ? 22 : 18) / (n > 6 ? 2 : 1),borderRadius:11,background:row === 'R' ? BK.coral : BK.ink,boxShadow:now ? '0 0 0 3px #fbe3da' : 'none',transition:'all .08s'}}/> : <span style={{width:5,height:5,borderRadius:3,background:'rgba(38,41,107,0.2)'}}/>}</div>; };
  const two = G.concat(G);
  const pad = (h) => <button onPointerDown={(e) => { e.preventDefault(); hit(h); }} style={{flex:1,minHeight:84,borderRadius:14,border:'none',background:h === 'R' ? BK.coral : BK.ink,color:'#fff',fontSize:17,fontWeight:900,touchAction:'manipulation',cursor:'pointer'}}>{h === 'L' ? t('Left', '왼손') : t('Right', '오른손')}<div style={{fontSize:12,fontWeight:800,opacity:0.85}}>{PP_RAT[rat][h === 'R' ? 0 : 1] + t(' a beat', '개 한 박에')}</div></button>;
  return (
    <div className="try-box" style={actBox} data-pp={toy ? 'toy' : 'pad'}>
      <div style={actTitle}>{toy ? t('My polyrhythm band', '나의 폴리리듬 밴드') : t('Three against two', '3 대 2')}</div>
      <div style={actNote}>{toy ? (LANG === 'ko' ? <>두 손이 다른 수로 한 박을 나눠요. 비율과 소리를 고르고 ▶로 들은 다음, 아래 두 패드로 같이 쳐 봐요.</> : <>Two hands split one beat into different numbers. Pick the ratio and the sounds, tap ▶ to hear it, then play along on the two pads.</>)
        : (LANG === 'ko' ? <>한 손은 한 박에 <b>셋</b>, 다른 손은 <b>둘</b>. 둘을 합치면 언제나 같은 무늬: <b>"함께, 오, 왼, 오"</b>(오른손이 셋일 때). 책의 방법대로, 먼저 무릎을 두드리며 말해요. 그다음 아래 두 패드로. 처음엔 소리와 함께, 그다음 혼자.</>
          : <>One hand plays <b>three</b> in a beat, the other <b>two</b>. Put together they always make the same pattern: <b>"both, right, left, right"</b> (with three in the right hand). As the book suggests, first tap it on your knees, saying the words. Then on the two pads below: first with the sound, then on your own.</>)}</div>
      {spChips(ratios.map(r => [r, r === '3:2' ? t('3 right, 2 left', '오른손 3, 왼손 2') : r === '2:3' ? t('2 right, 3 left', '오른손 2, 왼손 3') : t('4 right, 3 left', '오른손 4, 왼손 3')]), rat, (x) => reset(() => setRat(x)))}
      <div style={{display:'grid',gridTemplateColumns:'48px repeat(' + (2 * n) + ',minmax(0,1fr))',alignItems:'center',margin:'4px 0',background:'#fffefa',border:'1.5px solid rgba(38,41,107,0.2)',borderRadius:8,padding:'4px 6px'}}>
        <span style={{fontSize:11,fontWeight:900,color:BK.coral}}>{t('Right', '오른손')}</span>{two.map((x, i) => cell(x, i, 'R'))}
        <span style={{fontSize:11,fontWeight:900,color:BK.ink}}>{t('Left', '왼손')}</span>{two.map((x, i) => cell(x, i, 'L'))}
        <span/>{two.map((x, i) => <span key={i} style={{textAlign:'center',fontSize:n > 6 ? 9.5 : 12,fontWeight:900,color:x.on ? BK.ink : 'transparent',borderLeft:i % n === 0 ? '1.5px solid #26296b' : 'none'}}>{x.on ? ppLet(x) : '·'}</span>)}
      </div>
      {spChips([[50, spMM(50)], [70, spMM(70)], [100, spMM(100)]], bpm, (x) => reset(() => setBpm(x)))}
      {toy && spChips(Object.keys(PP_SND).map(x => [x, t(PP_SND[x][0], PP_SND[x][1])]), snd, (x) => setSnd(x))}
      {!toy && spChips([[true, t('With the sound', '소리와 함께')], [false, t('On your own', '혼자서')]], guide, (x) => reset(() => setGuide(x)))}
      <div style={{display:'flex',gap:10,margin:'8px 0 4px'}}>{pad('L')}{pad('R')}</div>
      {spMsg(phase === 'listen' ? t('Listen…', '들어요…') : phase === 'tap' ? t('Four clicks, then play along on the pads.', '클릭 넷, 그다음 패드로 같이 쳐요.') : res ? t('Right: ' + res.R.hits + ' of ' + res.R.total + ' · Left: ' + res.L.hits + ' of ' + res.L.total + (res.ok ? (guide ? ' ✓ Now on your own.' : ' ✓') : '. Say the words, then again.'), '오른손: ' + res.R.total + '개 중 ' + res.R.hits + ' · 왼손: ' + res.L.total + '개 중 ' + res.L.hits + (res.ok ? (guide ? ' ✓ 이제 혼자서.' : ' ✓') : '. 말로 해 보고 다시.')) : toy ? t('Tap ▶ to hear the band.', '▶를 눌러 밴드를 들어 봐요.') : t('Tap ▶ to hear it, then Play along.', '▶로 듣고, 같이 치기.'), res ? (res.ok ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={go}>{t('Play along', '같이 치기')}</button>
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const s6PicGrand = () => lsRawPic('<path d="M4 34 L22 18 L40 4 L58 18 L76 4" fill="none" stroke="#e4572e" stroke-width="2.6"/><path d="M4 42 L22 30 L40 42 L58 30 L76 42" fill="none" stroke="#26296b" stroke-width="2.6"/>', [0, 0, 80, 46]);
const s6PicLs = () => lsRawPic('<path d="M4 16 L40 6 L76 16" fill="none" stroke="#e4572e" stroke-width="2.6"/>' + [4, 13, 22, 31, 40, 49, 58, 67, 76].map((x, i) => '<circle cx="' + x + '" cy="' + (40 - (i <= 4 ? i : 8 - i) * 2.5) + '" r="2.6" fill="#26296b"/>').join(''), [0, 0, 80, 46]);
const s6PicPoly = () => lsRawPic([0, 1, 2].map(i => '<circle cx="' + (8 + i * 24) + '" cy="12" r="6" fill="#e4572e"/>').join('') + [0, 1].map(i => '<circle cx="' + (8 + i * 36) + '" cy="34" r="6" fill="#26296b"/>').join(''), [0, 0, 80, 46]);
const s6PicWays = () => ({ shapes: [{ k: 'raw', svg: '<polygon points="5,22 40,13 75,22 40,31" fill="#26296b"/>' }], vb: [0, 0, 80, 44] });

function s6LbPages(scr = false) {
  const ch = 'scales-6', s5n = bkChapterNo('scales-5');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks6 = [[s4PicFour(), t('I play F♯ major and D♯ minor over four octaves and know where finger 4 goes', 'F♯장조와 D♯단조를 네 옥타브로 치고, 4번 자리를 알아요')], [s6PicWays(), t('I play every scale all p, all f, and louder up and softer down', '스케일마다 모두 p, 모두 f, 올라가며 세게 내려오며 여리게 쳐요')],
    [s6PicGrand(), t('I play the abbreviated grand scale: together up, apart, back together, together down', '줄인 그랜드 스케일을 쳐요: 함께 올라가고, 멀어지고, 다시 모이고, 함께 내려와요')], [s6PicLs(), t('I play one hand legato and the other staccato, both ways', '한 손은 레가토, 다른 손은 스타카토로, 두 가지 모두')],
    [spPicMirror(), t('I play contrary motion in the Grade 5 keys', '5급 조를 반대 방향으로 쳐요')], [s6PicPoly(), t('I play three against two, steady', '3 대 2를 고르게 쳐요')]];
  const toc = [[t('One 4 in every octave', '옥타브마다 4번 하나'), 2], [t('Three ways, four octaves', '세 가지로, 네 옥타브'), 3], [t('The abbreviated grand scale', '줄인 그랜드 스케일'), 4], [t('One hand legato, the other staccato', '한 손은 레가토, 다른 손은 스타카토'), 5], [t('Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?'), 6], [t('Three against two', '3 대 2'), 7], [t('My six checks', '나의 여섯 가지 확인'), 8]];
  const kbW = scr ? 30 : 40, kbH = scr ? 80 : 104;
  const fourStill = (k, h) => { const c = S4_SC[k], K = s4Oct(k), F = s4Mid(k, h), j4 = s4F4(k, h), lit = {}, nums = {}; K.forEach((x, j) => { lit[x] = j === j4 ? 'cor' : 'pale'; nums[x] = F[j]; });
    return <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{s4Name(k)} · {spHand(h)}</div><SpKb lo={c.r} hi={c.r + 12} W={kbW} H={kbH} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, c.nm[j % 7]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}}/></div>; };
  const ppStill = <LbPic h={130}><div style={{display:'grid',gridTemplateColumns:'60px repeat(6,1fr)',alignItems:'center',rowGap:6,width:'100%',maxWidth:420,margin:'0 auto',fontWeight:900}}>
    <span style={{fontSize:13,color:BK.coral}}>{t('Right', '오른손')}</span>{ppGrid('3:2').map((x, i) => <span key={i} style={{display:'flex',justifyContent:'center'}}>{x.R ? <span style={{width:20,height:20,borderRadius:10,background:BK.coral}}/> : '·'}</span>)}
    <span style={{fontSize:13,color:BK.ink}}>{t('Left', '왼손')}</span>{ppGrid('3:2').map((x, i) => <span key={i} style={{display:'flex',justifyContent:'center'}}>{x.L ? <span style={{width:20,height:20,borderRadius:10,background:BK.ink}}/> : '·'}</span>)}
    <span/>{ppGrid('3:2').map((x, i) => <span key={i} style={{textAlign:'center',fontSize:13,color:BK.ink}}>{x.on ? ppWord(x) : ''}</span>)}</div></LbPic>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The Grade 6 scales as skills (chapter ' + s5n + ' has Grade 5; the I–V–I progressions and the arpeggios are the next chapter). From the technical work book, Grade 6: scales four octaves, hands separately and together, clear even legato, ♩ = 92 four notes a beat, each three ways: all p, all f, p < f ascending with f > p descending (F♯ major, D♯ harmonic and melodic minor; the chromatic scale from F♯/G♭ the same); the abbreviated grand scale format, E♭ major and C harmonic minor, four octaves, mf, ♩ = 76; legato and staccato combined, F♯ major and D♯ melodic minor, four octaves, mf, ♩ = 72: (i) RH staccato, LH legato, (ii) RH legato, LH staccato; contrary motion, two octaves, mf, ♩ = 72: B major, G♯ harmonic minor, D♭ major, B♭ harmonic minor. Exercise 6B (three against two) stays with the book; its skill is step 6. The book prints two octaves to show the fingering: play four. Another fingering is fine if it is logical and systematic.', '6급 스케일을 기술로(' + s5n + '장은 5급; I–V–I 진행과 아르페지오는 다음 챕터). 테크니컬 워크 책 6급: 스케일 네 옥타브, 한 손씩 그리고 양손 함께, 고르고 또렷한 레가토, ♩ = 92 한 박에 네 음, 세 가지로: 모두 p, 모두 f, 올라갈 때 p < f, 내려올 때 f > p(F♯장조, D♯ 화성·가락 단음계; F♯/G♭ 반음계도 같게); 줄인 그랜드 스케일, E♭장조와 C 화성 단음계, 네 옥타브, mf, ♩ = 76; 레가토와 스타카토 함께, F♯장조와 D♯ 가락 단음계, 네 옥타브, mf, ♩ = 72: (i) 오른손 스타카토, 왼손 레가토, (ii) 오른손 레가토, 왼손 스타카토; 반대 방향, 두 옥타브, mf, ♩ = 72: B장조, G♯ 화성 단음계, D♭장조, B♭ 화성 단음계. 연습곡 6B(3 대 2)는 책으로; 그 기술은 6단계. 책은 운지를 보여 주려고 두 옥타브만 적어요: 네 옥타브로 쳐요. 논리적이고 체계적이면 다른 운지도 괜찮아요.'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={150}><div style={{width:'100%',maxWidth:440,margin:'0 auto'}}><GrRoute k="Eb" w={440}/></div></LbPic>
      <LbSay size={18}>{t('Grade 6 scales: F♯ and D♯ minor three ways, the grand scale that comes apart and back together, one hand short while the other sings, contrary motion, and three against two.', '6급 스케일: F♯과 D♯단조를 세 가지로, 멀어졌다 다시 모이는 그랜드 스케일, 한 손은 짧게 다른 손은 노래하듯, 반대 방향, 그리고 3 대 2.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('find finger 4 in F♯ major and D♯ minor', 'F♯장조와 D♯단조에서 4번 자리를 찾을 수 있어요'), t('play the abbreviated grand scale from memory', '줄인 그랜드 스케일을 외워서 칠 수 있어요'), t('keep one hand legato while the other plays staccato', '한 손은 스타카토, 다른 손은 레가토를 지킬 수 있어요'), t('play three against two, steady', '3 대 2를 고르게 칠 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('One 4 in every octave', '옥타브마다 4번 하나')}
      teacher={<>{spTx(t('F♯ major, D♯ harmonic and melodic minor, four octaves, hands separately and together, ♩ = 92 four notes a beat. The book\'s fingerings: F♯ major RH 2 3 4 1 2 3 1 (2 at the top), LH 4 3 2 1 3 2 1 (2 at the top); D♯ minor RH 2 1 2 3 4 1 2, then 3 1 2 3 4 1 2 (3 at the top), LH 2 1 4 3 2 1 3 (2 at the top). In all three the RH 4 plays A♯ and the LH 4 plays F♯.', 'F♯장조, D♯ 화성·가락 단음계, 네 옥타브, 한 손씩 그리고 양손 함께, ♩ = 92 한 박에 네 음. 책의 운지: F♯장조 오른손 2 3 4 1 2 3 1(맨 위 2), 왼손 4 3 2 1 3 2 1(맨 위 2); D♯단조 오른손 2 1 2 3 4 1 2, 그다음 3 1 2 3 4 1 2(맨 위 3), 왼손 2 1 4 3 2 1 3(맨 위 2). 셋 모두 오른손 4번은 A♯, 왼손 4번은 F♯.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{fourStill('Fs', 'R')}{fourStill('Dsm', 'L')}</div></LbPic>} live={<S6FourPad/>}/>
      <LbSay>{LANG === 'ko' ? <>6급의 세 스케일은 모두 <b>오른손 4번이 A♯</b>, <b>왼손 4번이 F♯</b>에 와요. 옥타브마다 한 번, 언제나 같은 건반.</> : <>In all three Grade 6 scales <b>the right hand's 4 lands on A♯</b> and <b>the left hand's 4 on F♯</b>: once an octave, always the same key.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>오른손, F♯장조: 2 3 4 1 2 3 1. A♯마다 4번.</>, <>왼손, D♯단조: 2 1 4 3 2 1 3. F♯마다 4번.</>, <>네 옥타브, 한 박에 네 음, 양손 함께. {spMM(92)}까지.</>]
        : [<>Right hand, F♯ major: 2 3 4 1 2 3 1. Finger 4 on every A♯.</>, <>Left hand, D♯ minor: 2 1 4 3 2 1 3. Finger 4 on every F♯.</>, <>Four octaves, four notes a beat, hands together. Up to {spMM(92)}.</>]}/>
      <LbRemember>{t('Right hand 4 on A♯, left hand 4 on F♯.', '오른손 4번은 A♯, 왼손 4번은 F♯.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Three ways, four octaves', '세 가지로, 네 옥타브')}
      teacher={<>{spTx(t('Every Grade 6 similar-motion scale, and the chromatic scale from F♯/G♭, in three dynamics: (i) all p, (ii) all f, (iii) p < f ascending, f > p descending; four octaves, hands separately and together, clear even legato, ♩ = 92 four notes a beat. The chromatic scale: 3 on every black key, 1 on white keys, 2 on the RH\'s F and C and the LH\'s E and B.', '6급 같은 방향 스케일과 F♯/G♭ 반음계를 모두 세 가지 셈여림으로: (i) 모두 p, (ii) 모두 f, (iii) 올라갈 때 p < f, 내려올 때 f > p; 네 옥타브, 한 손씩 그리고 양손 함께, 고르고 또렷한 레가토, ♩ = 92 한 박에 네 음. 반음계: 검은건반 3, 흰건반 1, 오른손 F와 C, 왼손 E와 B는 2.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={150}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:'10px 18px',width:'100%',maxWidth:700,margin:'0 auto'}}>{S6_WAYS.map(x => <div key={x}><div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.ink,marginBottom:2}}>{s5WayName(x)}</div><S5Ribbon m={x} w={220}/></div>)}</div></LbPic>} live={<S6WaysPad/>}/>
      <LbSay>{LANG === 'ko' ? <>5급과 같은 세 가지, 이제 더 빠르게. 맨 위 음이 가장 세게, 그리고 내려오는 길 내내 여리게.</> : <>The same three ways as Grade 5, now faster. The top note the loudest, then softer all the way down.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>F♯장조 한 옥타브, 모두 p. 그다음 모두 f.</>, <>네 옥타브: 맨 아래 p, 맨 위 f, 다시 p.</>, <>F♯에서 반음계도 세 가지로. {spMM(92)}까지.</>]
        : [<>F♯ major, one octave, all p. Then all f.</>, <>Four octaves: p at the bottom, f at the top, p again.</>, <>The chromatic scale from F♯, the same three ways. Up to {spMM(92)}.</>]}/>
      <LbRemember>{t('The same fingers; only the sound changes.', '손가락은 그대로, 소리만 달라져요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The abbreviated grand scale', '줄인 그랜드 스케일')}
      teacher={<>{spTx(t('E♭ major and C harmonic minor, hands together in the abbreviated grand scale format, four octaves, mf, clear even legato, ♩ = 76 four notes a beat. The book (p32): the format combines similar and contrary motion. As printed: the hands an octave apart; similar motion up two octaves; the right hand carries on up while the left comes down (contrary motion, two octaves); back together; similar motion down to the start. In the full grand scale (the "Russian cross") the hands go on in similar motion for two more octaves after the contrary motion, and repeat the contrary motion midway down; Grade 6 asks only for the abbreviated one. The game puts the four parts in order.', 'E♭장조와 C 화성 단음계, 줄인 그랜드 스케일 형식으로 양손 함께, 네 옥타브, mf, 고르고 또렷한 레가토, ♩ = 76 한 박에 네 음. 책(32쪽): 같은 방향과 반대 방향을 합친 형식. 인쇄된 대로: 두 손은 한 옥타브 떨어져서; 같은 방향으로 두 옥타브 올라가고; 오른손은 계속 올라가고 왼손은 내려와요(반대 방향 두 옥타브); 다시 모이고; 같은 방향으로 처음 자리까지 내려와요. 줄이지 않은 그랜드 스케일(\'러시안 크로스\')은 반대 방향 다음에 같은 방향으로 두 옥타브 더 가고, 내려오는 중간에 반대 방향을 한 번 더 해요; 6급은 줄인 것만. 게임은 네 부분을 순서대로 놓아요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={190}><div style={{display:'grid',gap:8,width:'100%',maxWidth:520,margin:'0 auto'}}><GrRoute k="Eb" w={520}/><div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:6,fontSize:12.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>{[0, 1, 2, 3].map(g => <div key={g}>{g + 1}. {grLegLab(g)}</div>)}</div></div></LbPic>} live={<S6GrandPad/>}/>
      <LbSay>{LANG === 'ko' ? <>한 옥타브 떨어져서 <b>함께 올라가고</b>, <b>멀어졌다가</b>, <b>다시 모이고</b>, <b>함께 내려와요</b>. 가운데는 반대 방향이에요.</> : <><b>Together up</b>, <b>apart</b>, <b>back together</b>, <b>together down</b>, an octave apart. The middle is contrary motion.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E♭장조, 두 손을 한 옥타브 떨어뜨려요. 두 옥타브 함께 올라가서 멈춰요.</>, <>거기서 오른손은 계속 위로, 왼손은 아래로. 두 옥타브 뒤 다시 모여요.</>, <>함께 내려와서 끝. 그다음 C 화성 단음계. {spMM(76)}까지.</>]
        : [<>E♭ major, the hands an octave apart. Up two octaves together, then stop.</>, <>From there the right hand goes on up and the left goes down. Come back together.</>, <>Together down to the end. Then C harmonic minor. Up to {spMM(76)}.</>]}/>
      <LbRemember>{t('Together up, apart, back together, together down.', '함께 위로, 멀어지고, 다시 모이고, 함께 아래로.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('One hand legato, the other staccato', '한 손은 레가토, 다른 손은 스타카토')}
      teacher={<>{spTx(t('F♯ major and D♯ melodic minor, hands together in similar motion, four octaves, mf, ♩ = 72 four notes a beat: (i) RH staccato, LH legato; (ii) RH legato, LH staccato. The same fingering as the legato scales. Practise one octave slowly first; the legato hand must stay joined while the other lifts.', 'F♯장조와 D♯ 가락 단음계, 같은 방향 양손, 네 옥타브, mf, ♩ = 72 한 박에 네 음: (i) 오른손 스타카토, 왼손 레가토; (ii) 오른손 레가토, 왼손 스타카토. 운지는 레가토 스케일과 같아요. 먼저 한 옥타브를 천천히; 다른 손이 떨어질 때도 레가토 손은 이어져야 해요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:16,width:'100%',maxWidth:680,margin:'0 auto'}}><div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{t('(i) Right hand staccato', '(i) 오른손 스타카토')}</div><S6LsRows stac="R" w={300}/></div><div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{t('(ii) Left hand staccato', '(ii) 왼손 스타카토')}</div><S6LsRows stac="L" w={300}/></div></div></LbPic>} live={<S6LsPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 손이 같은 음을 같은 번호로, 그런데 <b>한 손은 짧게</b>, <b>한 손은 이어서</b>. 그다음 바꿔요.</> : <>Both hands play the same notes with the same fingers, but <b>one hand short</b> and <b>one hand joined</b>. Then swap.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>F♯장조 한 옥타브, 오른손만 스타카토. 그다음 왼손만 레가토.</>, <>함께 천천히: 오른손은 튀고, 왼손은 노래해요.</>, <>바꿔서 (ii). 그다음 네 옥타브, {spMM(72)}까지.</>]
        : [<>F♯ major, one octave, the right hand alone staccato. Then the left hand alone legato.</>, <>Together, slowly: the right hand bounces, the left hand sings.</>, <>Swap for (ii). Then four octaves, up to {spMM(72)}.</>]}/>
      <LbRemember>{t('One hand short, one hand joined; then swap.', '한 손은 짧게, 한 손은 이어서; 그다음 바꿔요.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?')}
      teacher={<>{spTx(t('Contrary motion, two octaves, hands together from one note, mf, clear even legato, ♩ = 72 four notes a beat: B major, G♯ harmonic minor, D♭ major, B♭ harmonic minor (the Grade 5 similar-motion keys). The book\'s first octaves: B major RH 1 2 3 1 2 3 4 1, LH 1 2 3 4 1 2 3 1; G♯ minor RH 2 3 1 2 3 1 2 3, LH 2 1 2 3 4 1 2 3; D♭ major RH 2 3 1 2 3 4 1 2, LH 2 1 2 3 4 1 2 3; B♭ minor RH 2 1 2 3 1 2 3 4, LH 2 3 4 1 2 3 1 2. None mirrors all the way.', '반대 방향, 두 옥타브, 두 손이 한 음에서, mf, 고르고 또렷한 레가토, ♩ = 72 한 박에 네 음: B장조, G♯ 화성 단음계, D♭장조, B♭ 화성 단음계(5급의 같은 방향 조). 책의 첫 옥타브: B장조 오른손 1 2 3 1 2 3 4 1, 왼손 1 2 3 4 1 2 3 1; G♯단조 오른손 2 3 1 2 3 1 2 3, 왼손 2 1 2 3 4 1 2 3; D♭장조 오른손 2 3 1 2 3 4 1 2, 왼손 2 1 2 3 4 1 2 3; B♭단조 오른손 2 1 2 3 1 2 3 4, 왼손 2 3 4 1 2 3 1 2. 끝까지 같은 것은 없어요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={160}><div style={{display:'grid',gridTemplateColumns:'1fr',gap:16,width:'100%',maxWidth:scr ? 440 : 560,margin:'0 auto'}}><div><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('B6')} · {t('not mirror twins', '거울 쌍둥이 아님')}</div><ScfCmKb k="B6" W={scr ? 20 : 30} H={scr ? 66 : 84} mark={scfFirstDiff('B6')}/></div></div></LbPic>} live={<S6MirrorPad/>}/>
      <LbSay>{LANG === 'ko' ? <>5급의 조를 이제 반대 방향으로. 이번엔 <b>넷 모두 거울 쌍둥이가 아니에요</b>: 손마다 자기 스케일 번호를 지켜요.</> : <>The Grade 5 keys, now in contrary motion. This time <b>none of the four are mirror twins</b>: each hand keeps its own scale fingering.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>두 손을 B에. 오른손 1 2 3, 왼손 1 2 3 4.</>, <>번호가 갈라지는 곳에서 멈춰서 확인해요.</>, <>두 옥타브, mf, 한 박에 네 음. {spMM(72)}까지.</>]
        : [<>Both hands on B. Right hand 1 2 3, left hand 1 2 3 4.</>, <>Stop where the numbers part, and check.</>, <>Two octaves, mf, four notes a beat. Up to {spMM(72)}.</>]}/>
      <LbRemember>{t('Each hand keeps its own numbers.', '손마다 자기 번호를 지켜요.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Step 6', '6단계')} title={t('Three against two', '3 대 2')}
      teacher={<>{t('The skill of exercise 6B (Perfect polyrhythms): triplets in one hand against duplets in the other, at a steady pulse. The book\'s own way in: clap, then tap on the knees, saying "both right-left-right" (three in the right hand), then reversed, "both left-right-left"; then the exercise, at about ♩ = 100. Grade 7 brings polyrhythmic scales (three against two) and Grade 8 two against three, so this pattern returns. Below the pad in the toolbox: My polyrhythm band, the same pattern with drums or bells, and four against three.', '연습곡 6B(Perfect polyrhythms)의 기술: 한 손은 셋잇단, 다른 손은 둘, 고른 박으로. 책의 방법: 손뼉, 그다음 무릎을 두드리며 "both right-left-right"(오른손이 셋)라고 말하고, 그다음 반대로 "both left-right-left"; 그다음 연습곡, 대략 ♩ = 100. 7급에 3 대 2 스케일, 8급에 2 대 3 스케일이 나와서 이 무늬가 다시 와요. 툴박스에는 \'나의 폴리리듬 밴드\': 같은 무늬를 드럼이나 종으로, 4 대 3까지.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=6')}>
      <LbLive still={ppStill} live={<PolyPad/>}/>
      <LbSay>{LANG === 'ko' ? <>오른손 셋, 왼손 둘을 한 박에. 합치면 언제나 <b>함께, 오, 왼, 오</b>. 말로 먼저, 그다음 손으로.</> : <>Three in the right hand, two in the left, in one beat. Together they always make <b>both, right, left, right</b>. Say it first, then play it.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>무릎에 두 손을 얹고 "함께, 오, 왼, 오"를 말하며 두드려요.</>, <>바꿔서: 왼손 셋, 오른손 둘. "함께, 왼, 오, 왼".</>, <>건반에서: 오른손은 C E G, 왼손은 C G로. 점점 빠르게.</>]
        : [<>Hands on your knees: tap "both, right, left, right", saying the words.</>, <>Swap: three in the left, two in the right. "Both, left, right, left".</>, <>At the keys: the right hand C E G, the left hand C G. Then faster.</>]}/>
      <LbRemember>{t('Both, right, left, right.', '함께, 오, 왼, 오.')}</LbRemember>
    </LbPage>,
    <LbPage key="8" no={8} chId={ch} kicker={t('Check-up', '점검')} title={t('My six checks', '나의 여섯 가지 확인')}
      teacher={<>{t('Each one played to you from memory, in the Grade 6 keys (the teacher\'s copy lists them), four octaves where the book asks for four. Listen for the crescendo\'s top, the turn of the grand scale at the top and the bottom, a legato hand that stays joined, and an even three against two.', '하나씩 외워서, 6급 조로(선생님용에 목록), 책이 네 옥타브를 요구하는 것은 네 옥타브로 들려줘요. 크레셴도의 꼭대기, 그랜드 스케일의 위와 아래에서 방향 바꾸기, 끊기지 않는 레가토 손, 고른 3 대 2를 들어 주세요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks6.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks6} storeKey="pb_s6_six"/>}/>
    </LbPage>,
  ];
}
function Scales6LessonBook() { return <>{s6LbPages(false)}</>; }
function S6Learn({ onStart }) {
  const pages = s6LbPages(true), opener = pages[0];
  return (
    <Lesson id="scales-6" title={bkChapterName('scales-6')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scales-6"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const S6_LEVELS = [
  { n: 1, label: 'F♯ and D♯ minor: where does finger 4 go?', kind: 'four', time: 15 },
  { n: 2, label: 'All p, all f, or louder up?', kind: 'dyn', time: 25 },
  { n: 3, label: 'The grand scale: which part is this?', kind: 'grand', time: 20 },
  { n: 4, label: 'Which hand is staccato?', kind: 'ls', time: 25 },
  { n: 5, label: 'Grade 6 contrary motion: mirror twins?', kind: 'mirror', time: 15 },
  { n: 6, label: 'Three against two: which comes next?', kind: 'poly', time: 15 },
];
Object.assign(LEVEL_KO, { 'F♯ and D♯ minor: where does finger 4 go?': 'F♯과 D♯단조: 4번은 어디에?', 'All p, all f, or louder up?': '모두 p, 모두 f, 올라가며 세게?', 'The grand scale: which part is this?': '그랜드 스케일: 지금은 어느 부분?', 'Which hand is staccato?': '어느 손이 스타카토?', 'Grade 6 contrary motion: mirror twins?': '6급 반대 방향: 거울 쌍둥이?', 'Three against two: which comes next?': '3 대 2: 다음은?' });
function genS6Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'four') { let k, h, g = 0; do { k = pick(S6_KEYS); h = Math.random() < 0.5 ? 'R' : 'L'; } while (prev && prev.key === k + h && g++ < 10); return { kind, k, h, answer: s4F4Note(k, h), choices: S4_SC[k].nm.slice(), key: k + h, uid }; }
  if (kind === 'dyn') { let k, m, g = 0; do { k = pick(S6_KEYS); m = pick(S6_WAYS); } while (prev && prev.key === 'w' + m && g++ < 10); return { kind, k, m, answer: m, choices: S6_WAYS.slice(), key: 'w' + m, uid }; }
  if (kind === 'grand') { let k, leg, g = 0; do { k = pick(['Eb', 'Cmh']); leg = Math.floor(Math.random() * 4); } while (prev && prev.key === 'g' + leg && g++ < 10); return { kind, k, leg, answer: leg, choices: [0, 1, 2, 3], key: 'g' + leg, uid }; }
  if (kind === 'ls') { let k, h, g = 0; do { k = pick(S6_LS_KEYS); h = Math.random() < 0.5 ? 'R' : 'L'; } while (prev && prev.key === 'l' + h + k && g++ < 10); return { kind, k, h, answer: h, choices: ['R', 'L'], key: 'l' + h + k, uid }; }
  if (kind === 'mirror') { let k, g = 0; do { k = pick(S6_CM_KEYS); } while (prev && prev.key === 'c' + k && g++ < 10); return { kind, k, answer: scfMirror(k) ? 'yes' : 'no', choices: ['yes', 'no'], key: 'c' + k, uid }; }
  let r, sl, g = 0; do { r = pick(['3:2', '2:3']); sl = pick([2, 3, 4]); } while (prev && prev.key === 'p' + r + sl && g++ < 10); const x = ppGrid(r)[sl];
  return { kind: 'poly', r, sl, answer: x.R && x.L ? 'B' : x.R ? 'R' : 'L', choices: ['B', 'R', 'L'], key: 'p' + r + sl, uid };
}
const s6AnswerLabel = (q) => (q.kind === 'dyn' ? s5WayName(q.answer) : q.kind === 'grand' ? t(GR_LEGS[q.answer][0], GR_LEGS[q.answer][1]) : q.kind === 'ls' ? (q.answer === 'R' ? t('Right hand', '오른손') : t('Left hand', '왼손')) : q.kind === 'poly' ? ({ B: t('both', '함께'), R: t('right', '오'), L: t('left', '왼') })[q.answer] : s4AnswerLabel(q));
function S6Question(props) {
  const { q, given, locked, onAnswer, pixel } = props;
  if (q.kind === 'four' || q.kind === 'mirror') return <S4Question {...props}/>;
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const play = () => { stopClicks(); if (q.kind === 'dyn') s6PlayWay(q.k, q.m); else if (q.kind === 'grand') grPlay(q.k, q.leg); else if (q.kind === 'ls') s6LsPlay(q.k, q.h); };
  useEffect(() => { if (q.kind === 'poly') return; const id = setTimeout(play, 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:14,fontWeight:900,lineHeight:1.2}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  const again = q.kind === 'poly' ? null : <div style={{textAlign:'center'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>;
  let title, body;
  if (q.kind === 'dyn') { title = t('Listen to ' + S4_ST[q.k].en + ': which way is it played?', S4_ST[q.k].ko + '를 들어 봐요: 어떻게 치고 있나요?'); body = <>{!pixel && <div style={{maxWidth:340,margin:'6px auto 0'}}><S5Ribbon m={done ? q.m : null}/></div>}{grid(3, S6_WAYS.map(c => [c, s5WayName(c)]))}</>; }
  else if (q.kind === 'grand') { title = t('Part of the grand scale in ' + S6_GR[q.k].en + ': which part is it?', S6_GR[q.k].ko + ' 그랜드 스케일의 한 부분: 어느 부분일까요?'); body = <>{!pixel && done && <GrRoute k={q.k} hl={q.leg}/>}{grid(2, [0, 1, 2, 3].map(g => [g, grLegLab(g)]))}</>; }
  else if (q.kind === 'ls') { title = t(S4_ST[q.k].en + ', hands together: which hand is staccato?', S4_ST[q.k].ko + ', 양손: 어느 손이 스타카토?'); body = <>{!pixel && done && <S6LsRows stac={q.h}/>}{grid(2, [['R', t('Right hand', '오른손')], ['L', t('Left hand', '왼손')]])}</>; }
  else { const G = ppGrid(q.r); title = t((q.r === '3:2' ? 'Three in the right hand, two in the left' : 'Two in the right hand, three in the left') + ': what comes on the coral slot?', (q.r === '3:2' ? '오른손 셋, 왼손 둘' : '오른손 둘, 왼손 셋') + ': 빨간 칸에는?');
    body = <><div style={{display:'grid',gridTemplateColumns:'repeat(6,1fr)',gap:4,maxWidth:340,margin:'6px auto 0'}}>{G.map((x, i) => <div key={i} style={{textAlign:'center',padding:'10px 0',borderRadius:8,border:'1.5px solid ' + (i === q.sl ? BK.coral : 'rgba(38,41,107,0.2)'),background:i === q.sl ? '#fbe3da' : '#fff',fontWeight:900,fontSize:13,color:BK.ink}}>{i < q.sl || (done && i === q.sl) ? (x.on ? ppWord(x) : '·') : i === q.sl ? '?' : ''}</div>)}</div>{grid(3, [['B', t('both', '함께')], ['R', t('right', '오')], ['L', t('left', '왼')]])}</>; }
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {again}{body}
  </div>);
}
Object.assign(SCALES_6_DRILL, { levels: S6_LEVELS, generate: genS6Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: s6AnswerLabel, Question: S6Question, Learn: S6Learn });
// the teacher's copy
function S6Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scales-6" teacher>{content}</WbPage>);
  const mid = (k) => S4_SC[k].en + ': RH ' + s4Mid(k, 'R').join(' ') + ' · LH ' + s4Mid(k, 'L').join(' ') + ' (4: RH ' + s4F4Note(k, 'R') + ', LH ' + s4F4Note(k, 'L') + ')';
  const W = S6_WB;
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scales-6')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>{spTx('The keys, speeds and fingerings are the technical work book\'s (Grade 6 pp25–41). Scales four octaves (the book prints two: in most cases start an octave lower than written), from memory. Another fingering is fine if it is logical and systematic. The I–V–I progressions and the arpeggios are in the next chapter.')}</div>
    <TcBlock page={2} title="One 4 in every octave" answers={<>{tcAns('TRY IT', W.four.map(([k, h]) => s4wName(k) + ', ' + scfwHand(h) + ': ' + s4F4Note(k, h)))}{tcAns('PLAY', ['F♯ major RH, a middle octave: ' + s4Mid('Fs', 'R').join(' ')], null)}{tcAns(spTx('FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, ♩ = 92 FOUR NOTES A BEAT · A MIDDLE OCTAVE'), [mid('Fs'), mid('Dsm'), mid('Dsmel') + '; coming down as the natural minor'])}</>}
      watch="Losing the place on the black keys. In all three keys the RH 4 is A♯ and the LH 4 is F♯; in D♯ minor the RH starts on 2, its first 4 on the first A♯."
      say="“Right hand 4 on A♯, left hand 4 on F♯.”"/>
    <TcBlock page={3} title="Three ways, four octaves" answers={<>{tcAns('TRY IT', W.ways.map(m => S5_WAY_AB[m]))}{tcAns(spTx('EVERY SCALE ABOVE AND THE CHROMATIC FROM F♯/G♭, ♩ = 92'), ['all p', 'all f', 'p < f ascending, f > p descending'])}</>}
      watch="A crescendo that peaks too early; all p that loses notes on the black keys; the chromatic scale's 2s (RH F and C, LH E and B) dropped at speed."
      say="“The same fingers; only the sound changes.”"/>
    <TcBlock page={4} title="The abbreviated grand scale" answers={<>{tcAns('TRY IT', W.grand.map(g => String(g + 1)))}{tcAns('PLAY', ['L', '2'], 5)}{tcAns(spTx('E♭ MAJOR AND C HARMONIC MINOR, FOUR OCTAVES, mf, ♩ = 76'), ['the hands an octave apart', 'up two octaves together', 'RH up, LH down two octaves (contrary)', 'back together', 'down two octaves together'], null)}</>}
      watch="Stopping at the turn into contrary motion, or the LH starting down a note late. Practise each turning point as a pair: the top of part 1 into part 2, the bottom of part 2 into part 3."
      say="“Together up, apart, back together, together down.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="One hand legato, the other staccato" answers={<>{tcAns('TRY IT', W.ls.map(h => (h === 'R' ? 'right hand staccato' : 'left hand staccato')))}{tcAns(spTx('F♯ MAJOR AND D♯ MELODIC MINOR, FOUR OCTAVES, mf, ♩ = 72'), ['(i) RH staccato, LH legato', '(ii) RH legato, LH staccato'], null)}</>}
      watch="The legato hand catching the staccato (both short), or the staccato hand lengthening. Slow and one octave first; then four."
      say="“One hand short, one hand joined; then swap.”"/>
    <TcBlock page={6} title="Contrary motion: mirror twins?" answers={<>{tcAns('TRY IT', S6_CM_KEYS.map(k => SCF_CM[k].en + ': ' + (scfMirror(k) ? 'Y' : 'N')))}{tcAns(spTx('TWO OCTAVES FROM ONE NOTE, mf, ♩ = 72 FOUR NOTES A BEAT'), S6_CM_KEYS.map(k => SCF_CM[k].en + ': RH ' + SCF_CM[k].R.join(' ') + ', LH ' + SCF_CM[k].L.join(' ')), null)}</>}
      watch="The LH copying the RH's numbers. None of the four mirrors all the way."
      say="“Each hand keeps its own numbers.”"/>
    <TcBlock page={7} title="Three against two" answers={<>{tcAns('TRY IT', ['3:2', '2:3'].map(r => r + ': ' + ppGrid(r).map(x => (x.R && x.L ? 'B' : x.R ? 'R' : x.L ? 'L' : '_')).join(' ')))}{tcAns('THE PATTERN', ['3 right, 2 left: both, right, left, right', '2 right, 3 left: both, left, right, left'], null)}</>}
      watch="The duplet hand drifting onto the triplet's notes (a dotted rhythm). Say the words aloud, slowly, then let them go."
      say="“Both, right, left, right.”"/>
    <TcBlock page={8} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', W.chk.four.map(([k, h]) => s4F4Note(k, h)))}{tcAns('B', W.chk.grand.map(([g, h]) => GR_ARROWS[g][h === 'R' ? 0 : 1] === '↗' ? 'up' : 'down'), 5)}{tcAns('C', W.chk.mirror.map(k => (scfMirror(k) ? 'Y' : 'N')), 9)}{tcAns('D', W.chk.poly.map(([r, sl]) => { const x = ppGrid(r)[sl]; return x.R && x.L ? 'B' : x.R ? 'R' : x.L ? 'L' : '—'; }), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.4 · C p.6 · D p.7. Then hear each one at the piano, from memory, in the Grade 6 keys at the book's speeds.</div></>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['scales-6'] = S6Teacher;
// ─── Scales, Grade 6: the Workbook ───
const S6_WB = {
  four: [['Fs', 'R'], ['Fs', 'L'], ['Dsm', 'R'], ['Dsm', 'L'], ['Dsmel', 'R'], ['Dsmel', 'L']],
  ways: ['cd', 'p', 'f'],
  grand: [2, 0, 3, 1],   // the order the four pictures stand in
  ls: ['R', 'L', 'L', 'R'],
  chk: { four: [['Fs', 'R'], ['Dsm', 'L'], ['Dsmel', 'R'], ['Fs', 'L']], grand: [[1, 'R'], [1, 'L'], [2, 'R'], [3, 'L']], mirror: ['B6', 'Gsmh6', 'Db6', 'Bbmh6'], poly: [['3:2', 4], ['3:2', 0], ['2:3', 4], ['2:3', 3]] },
};
function S6Workbook({ startNo = 1 }) {
  const W = S6_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="scales-6">{content}</WbPage>);
  const quiz = (rows) => <div style={{display:'grid',gap:8,padding:'6px 0',fontSize:13.5,fontWeight:800,color:BK.ink}}>{rows.map(([l, n, w]) => <span key={l} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'center'}}>{nvNum(n)} {l} {bkBox(w || 44, 30)}</span>)}</div>;
  const order = W.grand;
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Which note does finger 4 play?" how="One octave of each scale, the thumbs shown. Finger 4 plays once an octave, always the same note: write it.">
      <BkGrid cols={3} gap="6px 10px">{W.four.map((it, i) => <S4wFourCell key={i} item={it} n={i + 1} ex={i === 0}/>)}</BkGrid>
    </Part>
    <Part kind="home" title="Four octaves this week" how="Do each one at the piano and tick a box each day. Find the 4s before you start.">
      <PhLog rows={s4wRows(['F♯ major, each hand: RH 4 on A♯, LH 4 on F♯', 'D♯ harmonic and melodic minor: RH starts on 2, LH starts on 2', 'Hands together, four notes a beat, up to ♩ = 92'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Which way?" how="The thicker the line, the louder. Write the way under each picture: p, f, or &lt; &gt; (louder up, softer down).">
      <BkGrid cols={3} gap="6px 10px">{W.ways.map((m, i) => <ExCell key={m} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}><S5Ribbon m={m} w={200} marks={false}/>
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, S5_WAY_AB[m], 60, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Three ways this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['F♯ major, one octave: all p, then all f', 'Four octaves: p at the bottom, f at the top, p again at the end', 'The chromatic scale from F♯, the same three ways, up to ♩ = 92'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="The four parts in order" how="Each picture is one part of the abbreviated grand scale: the coral line is the right hand, the navy the left. Number them 1 to 4.">
      <BkGrid cols={4} gap="6px 8px">{order.map((g, i) => <ExCell key={g} n={i + 1} ex={g === 0}><div style={{display:'grid',gap:4,padding:'16px 2px 2px',justifyItems:'center'}}>
        <svg viewBox="0 0 60 44" style={{width:'100%',maxWidth:90}}><path d={g === 0 || g === 1 ? 'M6 22 L54 4' : 'M6 4 L54 22'} stroke="#e4572e" strokeWidth="3" fill="none"/><path d={g === 0 ? 'M6 40 L54 24' : g === 1 ? 'M6 24 L54 40' : g === 2 ? 'M6 40 L54 26' : 'M6 26 L54 42'} stroke="#26296b" strokeWidth="3" fill="none"/></svg>
        {nvBox(g === 0, String(g + 1), 34, 26)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="The grand scale this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['E♭ major, hands an octave apart: parts 1 and 2 only, slowly', 'All four parts, mf, then C harmonic minor', 'From memory, four notes a beat, up to ♩ = 76'])} label={300}/>
    </Part>
    <Part kind="play" title="Where the hands turn" how="Write the answers, then draw the whole grand scale as two lines, the right hand above, the left hand below.">
      {quiz([['In part 2, which hand goes down? (R or L)', 5], ['How many octaves is each part?', 6]])}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Which hand is staccato?" how="A joined line is legato; loose dots are staccato. The top is the right hand. Write R or L for the staccato hand.">
      <BkGrid cols={2} gap="6px 10px">{W.ls.map((h, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}><S6LsRows stac={h} w={240}/>
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, h, 40, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Legato and staccato this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['F♯ major, one octave: (i) RH staccato, LH legato, slowly', '(ii) swapped: RH legato, LH staccato', 'D♯ melodic minor both ways, four octaves, up to ♩ = 72'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Mirror twins, or not?" how="Contrary motion from one note: the right hand's fingers above, the left hand's below. Same numbers all the way? Write Y. Not? Write N.">
      <BkGrid cols={2} gap="6px 10px">{S6_CM_KEYS.map((k, i) => <ExCell key={k} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:3,padding:'16px 2px 2px'}}>
        {s4wLabel(SCF_CM[k].en)}<ScfCmKb k={k} W={11} H={40} kk={1.1}/>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>mirror twins? {nvBox(i === 0, scfMirror(k) ? 'Y' : 'N', 34, 26)}</div></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Contrary motion this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['B major: RH 1 2 3 1, LH 1 2 3 4', 'G♯ minor and D♭ major: both hands start on 2', 'All four, two octaves, up to ♩ = 72'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={6}/>
    <Part kind="together" title="Both, right or left?" how="One beat split into six. Write B (both), R (right) or L (left) under each slot that plays; leave the others empty.">
      <div style={{display:'grid',gap:10}}>{['3:2', '2:3'].map((r, i) => { const G = ppGrid(r); return <ExCell key={r} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>
        {s4wLabel(r === '3:2' ? 'Three in the right hand, two in the left' : 'Two in the right hand, three in the left')}
        {s4wRow('RH', <div style={{display:'flex',gap:3}}>{G.map((x, j) => <span key={j} style={{width:34,display:'flex',justifyContent:'center'}}>{x.R ? <span style={{width:16,height:16,borderRadius:8,background:BK.coral}}/> : ''}</span>)}</div>)}
        {s4wRow('LH', <div style={{display:'flex',gap:3}}>{G.map((x, j) => <span key={j} style={{width:34,display:'flex',justifyContent:'center'}}>{x.L ? <span style={{width:16,height:16,borderRadius:8,background:BK.ink}}/> : ''}</span>)}</div>)}
        {s4wRow('', <div style={{display:'flex',gap:3}}>{G.map((x, j) => <span key={j}>{nvBox(i === 0 && x.on, x.R && x.L ? 'B' : x.R ? 'R' : 'L', 34, 26)}</span>)}</div>)}</div></ExCell>; })}</div>
    </Part>
    <Part kind="home" title="Three against two this week" how="Tick a box each day.">
      <PhLog rows={s4wRows(['On your knees: "both, right, left, right", slowly, saying the words', 'Swapped: "both, left, right, left"', 'At the keys, then faster, up to about ♩ = 100'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<S6PaperCheck/>);
  return <>{pages}</>;
}
function S6PaperCheck() {
  const C = S6_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Which note does finger 4 play in every octave?')}
    <BkGrid cols={4} gap="6px 8px">{C.four.map((it, i) => <S4wFourCell key={i} item={it} n={i + 1} small/>)}</BkGrid>
    {bkSec('B', 'The grand scale: in this part, does this hand go up or down?')}
    <BkGrid cols={4} gap="6px 8px">{C.grand.map(([g, h], i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink,textAlign:'center'}}>Part {g + 1}, {h === 'R' ? 'right hand' : 'left hand'}{bkBox(60, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Contrary motion from one note: mirror twins? Y or N')}
    <BkGrid cols={2} gap="6px 8px">{C.mirror.map((k, i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gridTemplateColumns:'1fr auto',alignItems:'center',gap:6,padding:'14px 0 0'}}><div>{s4wLabel(SCF_CM[k].en)}<ScfCmKb k={k} W={9} H={24} kk={1} bare/></div>{bkBox(30, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Three against two: B, R or L on the slot?')}
    <BkGrid cols={4} gap="6px 8px">{C.poly.map(([r, sl], i) => <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink,textAlign:'center'}}>{r === '3:2' ? '3 right, 2 left' : '2 right, 3 left'}, slot {sl + 1} of 6{bkBox(40, 24)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['scales-6'] = S6Workbook;
'''
rep("""TEACHER_COPIES['scales-5'] = S5Teacher;""", """TEACHER_COPIES['scales-5'] = S5Teacher;""" + CH)

HOME = r'''
// ══ Build BP: Scales, Grade 6 on the Home (Technique, Playing scales) ══
LBH_FN['scales-6'] = (s) => s6LbPages(s);
const s6HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('scales-6', i, { make }));
const s6DynQ = (n, prev) => { let k, m, g = 0; do { k = pick(S6_KEYS); m = pick(S6_WAYS); } while (prev && prev.key === m && g++ < 10);
  return { kind: 'choice', cols: 3, key: m, prompt: ['Listen: which way is it played?', '들어 봐요: 어떻게 치고 있나요?'], opts: S6_WAYS.map(x => ({ id: x, label: () => s5WayName(x) })), ans: m, ok: (v) => v === m,
    play: () => s6PlayWay(k, m), fig: (c) => ({ mid: <div style={{maxWidth:340,margin:'0 auto'}}><S5Ribbon m={c.res ? m : null}/></div> }), yes: S5_YES[m],
    no: ['It was “' + S5_WAY[m][0] + '”. The four clicks are always the same: compare with them.', '“' + S5_WAY[m][1] + '”였어요. 클릭 넷은 언제나 같은 크기: 견주어 봐요.'] }; };
const s6GrandQ = (n, prev) => { let k, leg, g = 0; do { k = n % 2 ? 'Cmh' : 'Eb'; leg = Math.floor(Math.random() * 4); } while (prev && prev.key === k + leg && g++ < 10);
  return { kind: 'choice', cols: 2, key: k + leg, prompt: ['Listen: which part of the grand scale is this?', '들어 봐요: 그랜드 스케일의 어느 부분일까요?'], opts: [0, 1, 2, 3].map(x => ({ id: x, label: () => grLegLab(x) })), ans: leg, ok: (v) => v === leg,
    play: () => grPlay(k, leg), fig: (c) => ({ mid: <GrRoute k={k} hl={c.res ? leg : null}/> }), yes: ['Yes: ' + GR_LEGS[leg][0].toLowerCase() + '.', '맞아요: ' + GR_LEGS[leg][1] + '.'],
    no: ['It was part ' + (leg + 1) + ': ' + GR_LEGS[leg][0].toLowerCase() + '. Listen: do the two hands move the same way?', (leg + 1) + '번 부분이었어요: ' + GR_LEGS[leg][1] + '. 두 손이 같은 쪽으로 가나요?'] }; };
const s6LsQ = (n, prev) => { let k, h, g = 0; do { k = pick(S6_LS_KEYS); h = n % 2 ? 'L' : 'R'; } while (prev && prev.key === k + h && g++ < 10);
  return { kind: 'choice', cols: 2, key: k + h, prompt: ['Hands together: which hand is staccato?', '양손: 어느 손이 스타카토?'], opts: [{ id: 'R', label: () => t('Right hand', '오른손') }, { id: 'L', label: () => t('Left hand', '왼손') }], ans: h, ok: (v) => v === h,
    play: () => s6LsPlay(k, h), fig: (c) => ({ mid: c.res ? <S6LsRows stac={h}/> : null }), yes: ['Yes: the ' + (h === 'R' ? 'right' : 'left') + ' hand short.', '맞아요: ' + (h === 'R' ? '오른손' : '왼손') + '이 짧게.'], no: ['It was the ' + (h === 'R' ? 'right hand: the high notes.' : 'left hand: the low notes.'), (h === 'R' ? '오른손: 높은 음' : '왼손: 낮은 음') + '이었어요.'] }; };
const s6MirrorQ = (n, prev) => { let k, g = 0; do { k = pick(S6_CM_KEYS); } while (prev && prev.key === k && g++ < 10); const a = scfMirror(k) ? 'yes' : 'no';
  return { kind: 'choice', cols: 2, key: k, prompt: ['Contrary motion, ' + SCF_CM[k].en + ': mirror twins?', '반대 방향, ' + SCF_CM[k].ko + ': 거울 쌍둥이일까?'], opts: [{ id: 'yes', label: () => t('Mirror twins', '거울 쌍둥이') }, { id: 'no', label: () => t('Not mirror twins', '거울 쌍둥이 아님') }], ans: a, ok: (v) => v === a,
    fig: (c) => ({ mid: <ScfCmKb k={k} mark={c.res && a === 'no' ? scfFirstDiff(k) : -1}/> }), yes: ['Yes: each hand keeps its own numbers.', '맞아요: 손마다 자기 번호.'], no: ['Look again: the numbers part.', '다시 봐요: 번호가 갈라져요.'] }; };
s6HomeAdd('s6-four', 1, 'One 4 in every octave: Grade 6 keys', '옥타브마다 4번 하나: 6급 조', 'F♯ major and D♯ minor: the right hand\'s 4 on A♯, the left hand\'s on F♯.', 'F♯장조와 D♯단조: 오른손 4번은 A♯, 왼손은 F♯.', lwTapQ(S6FourPad, (n) => ({ fixed: { k: S6_KEYS[n % 3], h: n % 2 ? 'L' : 'R' } }), ['Tap the key finger 4 plays.', '4번이 치는 건반을 눌러요.'], ['Found it ✓', '찾았어요 ✓']));
s6HomeAdd('s6-dyn', 2, 'Three ways, four octaves', '세 가지로, 네 옥타브', 'All p, all f, or louder up and softer down, at ♩ = 92.', '모두 p, 모두 f, 또는 올라가며 세게 내려오며 여리게, ♩ = 92.', s6DynQ);
s6HomeAdd('s6-grand', 3, 'The abbreviated grand scale', '줄인 그랜드 스케일', 'Together up, apart, back together, together down.', '함께 올라가고, 멀어지고, 다시 모이고, 함께 내려와요.', s6GrandQ);
s6HomeAdd('s6-ls', 4, 'One hand legato, the other staccato', '한 손은 레가토, 다른 손은 스타카토', 'Hear which hand is short.', '어느 손이 짧은지 들어요.', s6LsQ);
s6HomeAdd('s6-mirror', 5, 'Contrary motion: the Grade 6 keys', '반대 방향: 6급 조', 'B, G♯ minor, D♭ and B♭ minor: none are mirror twins.', 'B, G♯단조, D♭, B♭단조: 거울 쌍둥이는 없어요.', s6MirrorQ);
s6HomeAdd('s6-poly', 6, 'Three against two', '3 대 2', 'Both, right, left, right: on the pads.', '함께, 오, 왼, 오: 패드로.', lwTapQ(PolyPad, () => ({ startOwn: true }), ['Listen, then play along on your own.', '듣고, 혼자서 같이 쳐요.'], ['Steady ✓', '고르게 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""    { id: 'kpl-5', en: 'Scales and arpeggios, Grade 5', ko: '스케일과 아르페지오, Grade 5', lessons: ['s5-four', 's5-dyn', 's5-mirror', 's5-chrom', 's5-arp'], check: 'scales-5' },   // Build BA""",
    """    { id: 'kpl-5', en: 'Scales and arpeggios, Grade 5', ko: '스케일과 아르페지오, Grade 5', lessons: ['s5-four', 's5-dyn', 's5-mirror', 's5-chrom', 's5-arp'], check: 'scales-5' },   // Build BA
    { id: 'kpl-6', en: 'Scales, Grade 6', ko: '스케일, Grade 6', lessons: ['s6-four', 's6-dyn', 's6-grand', 's6-ls', 's6-mirror', 's6-poly', 'mk-poly'], check: 'scales-6' },   // Build BP""")
rep("""  set('5', 's5-four s5-dyn s5-mirror s5-chrom s5-arp');   // Build BA: Scales and Arpeggios, Grade 5""", """  set('5', 's5-four s5-dyn s5-mirror s5-chrom s5-arp');   // Build BA: Scales and Arpeggios, Grade 5
  set('6', 's6-four s6-dyn s6-grand s6-ls s6-mirror s6-poly mk-poly');   // Build BP: Scales, Grade 6""")
# the make-toy
rep("""  { id: 'mk-cad', ch: 'listen-6',""", """  { id: 'mk-poly', ch: 'scales-6', title: 'My polyrhythm band', blurb: 'Three against two, two against three or four against three, on piano, drums or bells; play along on two pads.', C: () => <PolyPad ratios={['3:2', '2:3', '4:3']} toy/> },   // Build BP
  { id: 'mk-cad', ch: 'listen-6',""")
rep("""  'mk-cad': ['나만의 끝 만들기',""", """  'mk-poly': ['나의 폴리리듬 밴드', '3 대 2, 2 대 3, 4 대 3을 피아노, 드럼, 종으로; 두 패드로 같이 쳐요.'],
  'mk-cad': ['나만의 끝 만들기',""")
rep("""'mk-cad': ['chords', 3, 3, 'game ear'],""", """'mk-cad': ['chords', 3, 3, 'game ear'], 'mk-poly': ['rrhythm', 3, 3, 'game ear'],""")
rep("""  'mk-cad': () => (\n""", """  'mk-poly': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#b85068"/>{[0, 1, 2].map(i => <circle key={'r' + i} cx={5 + i * 7} cy="8" r="2.4" fill="#fefbf3"/>)}{[0, 1].map(i => <circle key={'l' + i} cx={5 + i * 10.5} cy="16.5" r="2.4" fill="#e9a83a"/>)}</svg>
  ),
  'mk-cad': () => (\n""")
# the books and the house
rep("""const LESSON_BOOKS = { 'listen-6': Listen6LessonBook,""", """const LESSON_BOOKS = { 'scales-6': Scales6LessonBook, 'listen-6': Listen6LessonBook,""")
rep("""const LB_PAGE_FNS = { 'listen-6': l6LbPages,""", """const LB_PAGE_FNS = { 'scales-6': s6LbPages, 'listen-6': l6LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"scales-6": "<path d=\\"M4 30 L14 20 L24 10 L34 20 L44 10\\" stroke=\\"#e4572e\\" stroke-width=\\"2.6\\"/><path d=\\"M4 40 L14 32 L24 40 L34 32 L44 40\\"/>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
