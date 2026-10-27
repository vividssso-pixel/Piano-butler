import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BY (board call 26, the second Grade 8 room): Scales, Grade 8, from the technical work book (Grade 8 pp68-75, read 28 Oct):
# the abbreviated grand scale in E major, C♯ harmonic minor, B♭ major and G harmonic minor (four octaves, all p and all f,
# ♩ = 92); the polyrhythmic scale two against three, E major, commencing two octaves apart (right hand two octaves, left hand
# three, ♩ = 100); hands together a third apart (the left hand on the tonic) and a sixth apart (the right hand on the tonic), the
# same four keys, four octaves, ♩ = 100; chromatic scales from E and from A♯/B♭ grouped in sixes, three octaves, ♩ = 70 six notes
# a beat, felt as three pairs; the chromatic scale in double minor thirds from C and E♭, hands separately, two octaves,
# ♩ = ca 80 two thirds a beat. The thing to make: a tune in thirds or sixths.

rep("""const SCALES_7_DRILL = { id: 'scales-7', label: 'Scales, Grade 7' };   // Build BU""", """const SCALES_7_DRILL = { id: 'scales-7', label: 'Scales, Grade 7' };   // Build BU
const SCALES_8_DRILL = { id: 'scales-8', label: 'Scales, Grade 8' };   // Build BY""")
rep("""  { id: 'scales-7', label: 'Scales, Grade 7', concept: SCALES_7_DRILL, track: 'start' },   // Build BU""", """  { id: 'scales-7', label: 'Scales, Grade 7', concept: SCALES_7_DRILL, track: 'start' },   // Build BU
  { id: 'scales-8', label: 'Scales, Grade 8', concept: SCALES_8_DRILL, track: 'start' },   // Build BY""")
rep("""'scales-7': ['scales-6']""", """'scales-7': ['scales-6'], 'scales-8': ['scales-7']""")
rep("""'scales-7': ['Scales 7', '스케일 7']""", """'scales-7': ['Scales 7', '스케일 7'], 'scales-8': ['Scales 8', '스케일 8']""")
rep("""'scales-7': '스케일, Grade 7'""", """'scales-7': '스케일, Grade 7', 'scales-8': '스케일, Grade 8'""")
rep("""'scales-7': 'k-play'""", """'scales-7': 'k-play', 'scales-8': 'k-play'""")
rep("""  'scales-7': 'scales grade 7""", """  'scales-8': 'scales grade 8 e major c sharp minor b flat g minor abbreviated grand scale two against three polyrhythmic third apart sixth apart chromatic sixes groups of six pairs double thirds minor thirds fingering',
  'scales-7': 'scales grade 7""")

CH = r'''
// ─── Chapter: Scales, Grade 8 (Build BY, 2026-10-28; board call 26, the second Grade 8 room) ───
Object.assign(S6_GR, {
  E8: { en: 'E major', ko: 'E장조', st: SP_MAJ, r: -8, nm: ['E', 'F♯', 'G♯', 'A', 'B', 'C♯', 'D♯'] },
  Csmh8: { en: 'C♯ harmonic minor', ko: 'C♯ 화성 단음계', st: SP_HAR, r: -11, nm: ['C♯', 'D♯', 'E', 'F♯', 'G♯', 'A', 'B♯'] },
  Bb8: { en: 'B♭ major', ko: 'B♭장조', st: SP_MAJ, r: -14, nm: ['B♭', 'C', 'D', 'E♭', 'F', 'G', 'A'] },
  Gmh8: { en: 'G harmonic minor', ko: 'G 화성 단음계', st: SP_HAR, r: -17, nm: ['G', 'A', 'B♭', 'C', 'D', 'E♭', 'F♯'] },
});
const S8_GR_KEYS = ['E8', 'Csmh8', 'Bb8', 'Gmh8'];
const S8GrandNote = () => (LANG === 'ko' ? <>같은 길, 8급의 네 조: E장조와 그 나란한 C♯ 화성 단음계, B♭장조와 그 나란한 G 화성 단음계. 이번엔 <b>모두 p</b>, 그리고 <b>모두 f</b>로. {spMM(92)}, 한 박에 네 음.</> : <>The same route in Grade 8's four keys: E major with its relative, C♯ harmonic minor; B♭ major with its relative, G harmonic minor. Now <b>all p</b>, and <b>all f</b>. {spMM(92)}, four notes a beat.</>);
function S8GrandPad(p) { return <S7GrandPad keys={S8_GR_KEYS} bpm={92} note={<S8GrandNote/>} title={t('The grand scale, Grade 8', '그랜드 스케일, 8급')} {...p}/>; }
Object.assign(S7_PS, { E8: { en: 'E major', ko: 'E장조', st: SP_MAJ, rh: 4, lh: -20, rO: 2, lO: 3, rP: 2, lP: 3 } });
const S8PolyNote = () => (LANG === 'ko' ? <>이번엔 거꾸로: <b>오른손이 둘</b>, <b>왼손이 셋</b>. E장조, 두 손이 <b>두 옥타브 떨어져</b> 시작해요. 오른손은 두 옥타브, 왼손은 세 옥타브. {spMM(100)}, 레가토, mf.</> : <>Now the other way round: <b>the right hand two</b> a beat, <b>the left hand three</b>. E major, the hands starting <b>two octaves apart</b>; the right hand two octaves, the left hand three. {spMM(100)}, legato, mf.</>);
function S8PolyScalePad(p) { return <S7PolyScalePad keys={['E8']} bpm={100} note={<S8PolyNote/>} title={t('Two against three, as a scale', '2 대 3, 스케일로')} {...p}/>; }
// ── step 3: a third apart (the left hand on the tonic) and a sixth apart (the right hand on the tonic): either way the other hand starts on the 3rd ──
const S8_AP = { E8: [4, 'E'], Csmh8: [1, 'C♯'], Bb8: [-2, 'B♭'], Gmh8: [-5, 'G'] };
const apStart = (k, kind) => { const c = S6_GR[k], t0 = S8_AP[k][0], med = c.st[2]; return kind === 'third' ? { L: t0 - 12, R: t0 - 12 + med } : { R: t0, L: t0 - 12 + med }; };
const apartPlay = (k, kind, bpm = 100) => { const c = S6_GR[k], S = apStart(k, kind), deg = (r0, o) => r0 + 12 * Math.floor(o / 7) + c.st[((o % 7) + 7) % 7] - c.st[0];
  const lD = kind === 'third' ? 0 : 2, rD = kind === 'third' ? 2 : 0, up = Array.from({ length: 8 }, (_, j) => j), sq = up.concat(up.slice(0, -1).reverse());
  const base = (start, d0) => start - c.st[d0]; return spPlay(sq.map((j, n) => ({ at: n / 4, keys: [base(S.R, rD) + 12 * Math.floor((rD + j) / 7) + c.st[(rD + j) % 7], base(S.L, lD) + 12 * Math.floor((lD + j) / 7) + c.st[(lD + j) % 7]], len: n === sq.length - 1 ? 1.4 : 0.25, vol: 0.12 })), bpm, 2); };
function S8ApartPad({ onResult, fixed }) {
  const [k, setK] = useState(fixed ? fixed.k : 'E8'), [kind, setKind] = useState(fixed ? fixed.kind : 'third'), [hit, setHit] = useState(false), [bad, setBad] = useState(null), [miss, setMiss] = useState(0);
  const S = apStart(k, kind), given = kind === 'third' ? 'L' : 'R', want = kind === 'third' ? S.R : S.L, c = S6_GR[k];
  const reset = (fn) => { setHit(false); setBad(null); setMiss(0); if (fn) fn(); };
  const tap = (x) => { playKey(x, 0.4); if (hit) return; if (x === want) { setHit(true); setBad(null); if (onResult) onResult({ ok: miss === 0 }); setTimeout(() => apartPlay(k, kind), 300); } else { setBad(x); setMiss(m => m + 1); } };
  const lit = { [S[given]]: 'cor' }; if (hit) lit[want] = 'good'; if (bad != null) lit[bad] = 'bad';
  return (
    <div className="try-box" style={actBox} data-s8="apart">
      <div style={actTitle}>{t('A third apart, a sixth apart', '3도 떨어져, 6도 떨어져')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 손이 같은 스케일을 다른 음에서 함께. <b>3도 떨어져</b>: 왼손이 으뜸음, 오른손은 3도 위. <b>6도 떨어져</b>: 오른손이 으뜸음, 왼손은 6도 아래. 비밀: 어느 쪽이든 다른 손은 <b>3음</b>에서 시작해요! 그 건반을 눌러요. 네 옥타브, {spMM(100)}.</> : <>Both hands play the same scale from different notes. <b>A third apart</b>: the left hand on the tonic, the right hand a 3rd above. <b>A sixth apart</b>: the right hand on the tonic, the left hand a 6th below. The secret: either way, the other hand starts on <b>the 3rd</b>! Tap that key. Four octaves, {spMM(100)}.</>}</div>
      {!fixed && spChips(S8_GR_KEYS.map(x => [x, t(S6_GR[x].en, S6_GR[x].ko)]), k, (x) => reset(() => setK(x)))}
      {!fixed && spChips([['third', t('A third apart', '3도 떨어져')], ['sixth', t('A sixth apart', '6도 떨어져')]], kind, (x) => reset(() => setKind(x)))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 4px'}}>{t(c.en, c.ko)} · {given === 'L' ? t('the left hand on ' + c.nm[0], '왼손은 ' + c.nm[0]) : t('the right hand on ' + c.nm[0], '오른손은 ' + c.nm[0])}</div>
      <SpKb lo={-17} hi={12} W={14} H={70} lit={lit} names={Object.fromEntries([[S[given], c.nm[0]]].concat(hit ? [[want, c.nm[2]]] : []))} onTap={tap} label={t('Where does the other hand start?', '다른 손은 어디서 시작할까요?')}/>
      {spMsg(hit ? t((given === 'L' ? 'The right hand' : 'The left hand') + ' starts on ' + c.nm[2] + ', the 3rd: ' + (kind === 'third' ? 'a 3rd above.' : 'a 6th below.'), (given === 'L' ? '오른손은 ' : '왼손은 ') + c.nm[2] + '(3음)에서: ' + (kind === 'third' ? '3도 위.' : '6도 아래.')) : bad != null ? t('Not there: find the 3rd note of the scale, ' + (kind === 'third' ? 'above' : 'below') + ' the coral key.', '거기가 아니에요: 빨간 건반 ' + (kind === 'third' ? '위' : '아래') + '의 3음을 찾아요.') : t('Where does the ' + (given === 'L' ? 'right' : 'left') + ' hand start?', (given === 'L' ? '오른손' : '왼손') + '은 어디서 시작할까요?'), hit ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => apartPlay(k, kind)}>{t('▶ Hear it, one octave', '▶ 한 옥타브 듣기')}</button>
      </div>
    </div>
  );
}
// ── step 4: the chromatic scale in sixes: six notes a beat, felt as three pairs, played evenly ──
const sxPlay = (start, group, bpm = 70) => { const up = Array.from({ length: 37 }, (_, j) => start + j), sq = up.concat(up.slice(0, -1).reverse()).slice(0, 48);
  return spPlay(sq.map((x, n) => ({ at: n / 6, keys: [x, x - 12], len: 1 / 6, vol: group === 'pairs' ? (n % 2 === 0 ? 0.16 : 0.08) : group === 'threes' ? (n % 3 === 0 ? 0.16 : 0.08) : (n % 6 === 0 ? 0.13 : 0.11) })), bpm, 2); };
const SX_START = { E: -8, Bb: -14 };
function S8SixesPad({ onResult, fixed }) {
  const [st, setSt] = useState('E'), [quiz, setQuiz] = useState(fixed ? fixed.g : null), [ans, setAns] = useState(null);
  const ask = () => { const g = Math.random() < 0.5 ? 'pairs' : 'threes'; setQuiz(g); setAns(null); sxPlay(SX_START[st], g, 50); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === quiz }); };
  const dots = (g) => <div style={{display:'flex',justifyContent:'center',gap:2,margin:'4px 0'}}>{[0, 1, 2, 3, 4, 5].map(i => <span key={i} style={{flex:'0 0 auto',width:16,height:16,borderRadius:8,border:'2px solid ' + BK.ink,background:(g === 'pairs' ? i % 2 === 0 : i % 3 === 0) ? BK.coral : '#fff',marginRight:(g === 'pairs' ? i % 2 === 1 : i % 3 === 2) && i < 5 ? 6 : 0}}/>)}</div>;
  return (
    <div className="try-box" style={actBox} data-s8="sixes">
      <div style={actTitle}>{t('Chromatic in sixes', '여섯 음씩 반음계')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>E와 B♭에서 반음계, 세 옥타브, 양손 같은 방향, <b>한 박에 여섯 음</b>({spMM(70)}). 여섯 음은 셋씩 둘이 아니라 <b>둘씩 셋</b>으로 느껴요. 그래도 소리는 고르게, 강세 없이! 먼저 과장된 강세로 들어 보고 알아맞혀요.</> : <>Chromatic from E and from B♭, three octaves, hands together in similar motion, <b>six notes a beat</b> ({spMM(70)}). Feel the six as <b>three pairs</b>, not two threes; yet play them evenly, without accents! First hear exaggerated accents and tell them apart.</>}</div>
      {!quiz && spChips([['E', t('From E', 'E에서')], ['Bb', t('From B♭', 'B♭에서')]], st, setSt)}
      {(!quiz || ans) && <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10,margin:'4px 0'}}>{['pairs', 'threes'].map(g => <div key={g} style={{textAlign:'center'}}><div style={{fontSize:13,fontWeight:900,color:g === 'pairs' ? BK.ink : BK.muted}}>{g === 'pairs' ? t('Three pairs ✓', '둘씩 셋 ✓') : t('Two threes', '셋씩 둘')}</div>{dots(g)}</div>)}</div>}
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{[['pairs', t('Pairs', '둘씩')], ['threes', t('Threes', '셋씩')]].map(([v, lab]) => <button key={v} className="choice-btn" onClick={() => say(v)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}}>{lab}</button>)}</div>}
      {spMsg(ans ? (ans === quiz ? t('Yes: ' + quiz + '.', '맞아요: ' + (quiz === 'pairs' ? '둘씩' : '셋씩') + '.') : t('It was in ' + quiz + '.', '정답은 ' + (quiz === 'pairs' ? '둘씩' : '셋씩') + '.')) : quiz ? t('Listen to the accents: pairs or threes?', '강세를 들어요: 둘씩? 셋씩?') : '', ans ? (ans === quiz ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!quiz && <button className="ghost-btn" style={spBtn} onClick={() => sxPlay(SX_START[st], 'pairs', 50)}>{t('▶ Pairs, slowly', '▶ 둘씩, 천천히')}</button>}
        {!quiz && <button className="ghost-btn" style={spBtn} onClick={() => sxPlay(SX_START[st], 'even', 70)}>{t('▶ Even, at ♩ = 70', '▶ 고르게, ♩ = 70')}</button>}
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => sxPlay(SX_START[st], quiz, 50)}>{t('♪ Again', '♪ 다시')}</button>}
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Pairs or threes?', '▶ 둘씩? 셋씩?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(null); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── step 5: the chromatic scale in double minor thirds: the right hand's fingers for each third (bottom/top), going up ──
const DT_F = [[1, 3], [2, 4], [1, 5], [2, 3], [1, 4], [1, 3], [2, 4], [1, 3], [2, 4], [1, 5], [2, 3], [1, 4]];   // bottom note C, C♯, … B (book p75)
const DT_OPTS = ['1 3', '2 4', '1 5', '2 3', '1 4'];
const dtTop = (x) => l6Spell(lwLet(x), 3, 3);   // the top of a minor 3rd, spelled as a 3rd (E♭–G♭, not E♭–F♯)
const dtPlay = (start = 0, bpm = 80) => { const up = Array.from({ length: 25 }, (_, j) => start + j), sq = up.concat(up.slice(0, -1).reverse()); return spPlay(sq.map((x, n) => ({ at: n / 2, keys: [x, x + 3], len: n === sq.length - 1 ? 1.4 : 0.48, vol: 0.11 })), bpm, 2); };
function S8DThirdsPad({ onResult, fixed }) {
  const [at, setAt] = useState(fixed ? fixed.at : 0), [ans, setAns] = useState(null), [run, setRun] = useState(fixed ? 0 : 0), [miss, setMiss] = useState(0);
  const f = DT_F[at], right = f.join(' '), done = !fixed && at >= 12;
  const say = (v) => { if (ans) return; setAns(v); const ok = v === right; if (!ok) setMiss(m => m + 1); if (fixed && onResult) onResult({ ok }); spPlay([{ at: 0, keys: [at, at + 3], len: 0.8, vol: 0.13 }], 80); };
  const next = () => { setAns(null); if (at + 1 >= 12) { setAt(12); if (onResult) onResult({ ok: miss === 0 }); setTimeout(() => dtPlay(0), 400); } else setAt(at + 1); };
  const lit = {}; if (!done) { lit[at] = ans ? (ans === right ? 'good' : 'cor') : 'cor'; lit[at + 3] = lit[at]; }
  const up = {}, dn = {}; DT_F.forEach((ff, j) => { if (j < at || done) { dn[j] = ff[0]; } }); if (ans && !done) { dn[at] = f[0]; up[at + 3] = f[1]; }
  return (
    <div className="try-box" style={actBox} data-s8="dthirds">
      <div style={actTitle}>{t('Chromatic in double minor thirds', '반음계 겹단3도')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>두 음(단3도)을 함께, 반음씩 올라가요: C와 E♭에서. 오른손 운지는 무늬가 있어요: 아랫음은 <b>1과 2가 번갈아</b>, 윗음은 <b>3, 4, 5</b>를 돌려요. <b>5번은 F와 C</b>에(3-4-5 반음계의 오른손처럼!). 한 손씩, 두 옥타브, 약 {spMM(80)}, 한 박에 두 쌍. 빠르기보다 고른 소리.</> : <>Two notes together (a minor 3rd), climbing a semitone at a time: from C and E♭. The right hand's fingering has a pattern: the bottom notes <b>take turns with 1 and 2</b>; the top notes cycle <b>3, 4, 5</b>. <b>Finger 5 lands on F and C</b> (just as in the 3-4-5 chromatic!). Hands separately, two octaves, about {spMM(80)}, two thirds a beat. Evenness before speed.</>}</div>
      <SpKb lo={0} hi={15} W={24} H={80} lit={lit} names={{ 0: 'C', 3: 'E♭', 12: 'C' }} up={up} dn={dn} label={t('The right hand, going up', '오른손, 올라가며')}/>
      {!done ? <><div style={{textAlign:'center',fontSize:14.5,fontWeight:900,color:BK.ink,margin:'4px 0'}}>{t('Third ' + (at + 1) + ' of 12: ' + lwLet(at) + ' + ' + dtTop(at) + '. Which fingers (bottom, top)?', '12개 중 ' + (at + 1) + '번째: ' + lwLet(at) + ' + ' + dtTop(at) + '. 손가락은(아래, 위)?')}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:5}}>{DT_OPTS.map(o => <button key={o} className={'choice-btn' + (!ans ? '' : o === right ? ' good' : o === ans ? ' bad' : '')} onClick={() => say(o)} style={{padding:'10px 2px',fontSize:14,fontWeight:900}}>{o}</button>)}</div></> : null}
      {spMsg(done ? t('One octave: bottom 1 2 1 2 1 1 2 1 2 1 2 1, top 3 4 5 3 4 3 4 3 4 5 3 4.' + (miss ? '' : ' First time!'), '한 옥타브: 아래 1 2 1 2 1 1 2 1 2 1 2 1, 위 3 4 5 3 4 3 4 3 4 5 3 4.' + (miss ? '' : ' 한 번에!')) : ans ? (ans === right ? t('Yes: ' + right + '.', '맞아요: ' + right + '.') : t('It is ' + right + '.', '정답은 ' + right + '.')) : '', done ? BK.green : ans ? (ans === right ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {ans && !done && !fixed && <button className="ghost-btn" style={spBtn} onClick={next}>{at < 11 ? t('Next third →', '다음 3도 →') : t('Finish', '끝내기')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={() => dtPlay(0)}>{t('▶ Two octaves from C', '▶ C에서 두 옥타브')}</button>
        {done && <button className="ghost-btn" style={spBtn} onClick={() => { setAt(0); setAns(null); setMiss(0); }}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}
// ── make: a tune in thirds or sixths: tap the tune, a second voice follows a 3rd or a 6th below, in the key ──
function ThirdsMaker() {
  const [key, setKey] = useState(0), [iv, setIv] = useState(3), [last, setLast] = useState(null);
  const sc = [0, 2, 4, 5, 7, 9, 11].map(x => spPc(x + key)), inKey = (x) => sc.includes(spPc(x));
  const below = (x) => { const i = sc.indexOf(spPc(x)), j = ((i - (iv - 1)) % 7 + 7) % 7; let y = x - 1; while (spPc(y) !== sc[j]) y--; return y; };
  const tap = (x) => { if (!inKey(x)) { playKey(x, 0.5); setLast([x]); return; } const y = below(x); spPlay([{ at: 0, keys: [x, y], len: 0.9, vol: 0.14 }], 90); setLast([x, y]); };
  const lit = {}; for (let x = -12; x <= 19; x++) if (inKey(x)) lit[x] = 'pale'; if (last) last.forEach((x, j) => { lit[x] = j === 0 ? 'cor' : 'good'; });
  return (
    <div className="try-box" style={actBox} data-mk="thirds">
      <div style={actTitle}>{t('My tune in thirds and sixths', '3도와 6도로 내 선율')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>위쪽 건반으로 선율을 쳐요. 둘째 성부가 그 조 안에서 <b>3도 아래</b>나 <b>6도 아래</b>로 따라와요: 8급의 '3도 떨어져', '6도 떨어져' 스케일, 그리고 겹3도의 소리. 흐린 건반이 그 조의 음.</> : <>Play a tune on the upper keys. A second voice follows <b>a 3rd below</b> or <b>a 6th below</b>, inside the key: the sound of Grade 8's scales a third and a sixth apart, and of double thirds. The pale keys are the key's notes.</>}</div>
      {spChips([[0, t('C major', 'C장조')], [7, t('G major', 'G장조')], [5, t('F major', 'F장조')]], key, setKey)}
      {spChips([[3, t('A 3rd below', '3도 아래')], [6, t('A 6th below', '6도 아래')]], iv, setIv)}
      <SpKb lo={-12} hi={19} W={14} H={74} lit={lit} names={last ? Object.fromEntries(last.map(x => [x, lwLet(x)])) : {}} onTap={tap} label={t('Play your tune', '선율 치기')}/>
      {spMsg(last && last.length === 2 ? t(lwLet(last[0]) + ' with ' + lwLet(last[1]) + ' below: a ' + (iv === 3 ? '3rd' : '6th') + '.', lwLet(last[0]) + ' 아래 ' + lwLet(last[1]) + ': ' + (iv === 3 ? '3도' : '6도') + '.') : t('Tap a pale key.', '흐린 건반을 눌러요.'))}
    </div>
  );
}

const s8PicApart = () => lsRawPic('<path d="M4 30 L40 12 L76 30" fill="none" stroke="#e4572e" stroke-width="2.6"/><path d="M4 38 L40 20 L76 38" fill="none" stroke="#26296b" stroke-width="2.6"/><text x="36" y="44" font-family="Inter, sans-serif" font-size="9" font-weight="900" fill="#26296b">3 · 6</text>', [0, 0, 80, 46]);
const s8PicSix = () => lsRawPic([0, 1, 2, 3, 4, 5].map(i => '<circle cx="' + (8 + i * 12 + Math.floor(i / 2) * 4) + '" cy="22" r="5" fill="' + (i % 2 === 0 ? '#e4572e' : '#fff') + '" stroke="#26296b" stroke-width="2"/>').join(''), [0, 0, 92, 44]);
const s8PicDt = () => lsRawPic([0, 1, 2, 3].map(i => '<ellipse cx="' + (14 + i * 16) + '" cy="' + (34 - i * 5) + '" rx="5" ry="3.7" fill="#26296b"/><ellipse cx="' + (14 + i * 16) + '" cy="' + (24 - i * 5) + '" rx="5" ry="3.7" fill="#e4572e"/>').join(''), [0, 0, 80, 44]);

function s8LbPages(scr = false) {
  const ch = 'scales-8', s7n = bkChapterNo('scales-7');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks = [[s7PicGrand(), t('I play the grand scale in E, C♯ minor, B♭ and G minor, all p and all f', 'E, C♯단조, B♭, G단조로 그랜드 스케일을 모두 p, 모두 f로 쳐요')], [s7PicPs(), t('I play E major two against three', 'E장조를 2 대 3으로 쳐요')],
    [s8PicApart(), t('I play scales a third apart and a sixth apart', '스케일을 3도 떨어져, 6도 떨어져 쳐요')], [s8PicSix(), t('I play the chromatic scale in even sixes', '반음계를 고른 여섯 음씩 쳐요')], [s8PicDt(), t('I play the chromatic scale in double minor thirds', '반음계를 겹단3도로 쳐요')]];
  const toc = [[t('The grand scale, Grade 8', '그랜드 스케일, 8급'), 2], [t('Two against three, as a scale', '2 대 3, 스케일로'), 3], [t('A third apart, a sixth apart', '3도 떨어져, 6도 떨어져'), 4], [t('Chromatic in sixes', '여섯 음씩 반음계'), 5], [t('Chromatic in double minor thirds', '반음계 겹단3도'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const apartStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:700,margin:'0 auto'}}>{['third', 'sixth'].map(kd => { const S = apStart('E8', kd);
    return <div key={kd}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{kd === 'third' ? t('A third apart: LH E, RH G♯', '3도 떨어져: 왼손 E, 오른손 G♯') : t('A sixth apart: RH E, LH G♯', '6도 떨어져: 오른손 E, 왼손 G♯')}</div><SpKb lo={-17} hi={12} W={scr ? 9 : 17} H={scr ? 50 : 84} lit={{ [S.L]: 'cor', [S.R]: 'cor' }} names={{ [S.L]: kd === 'third' ? 'E' : 'G♯', [S.R]: kd === 'third' ? 'G♯' : 'E' }} k={1}/></div>; })}</div>;
  const dtStill = <div style={{width:'100%',maxWidth:600,margin:'0 auto'}}><SpKb lo={0} hi={15} W={scr ? 20 : 30} H={scr ? 64 : 84} lit={{ 2: 'cor', 5: 'cor', 9: 'cor', 12: 'cor' }} names={{ 0: 'C', 5: 'F', 12: 'C' }} dn={Object.fromEntries(DT_F.map((f, j) => [j, f[0]]))} up={Object.fromEntries(DT_F.map((f, j) => [j + 3, f[1]]).filter(([x]) => x <= 15))}/></div>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The Grade 8 scales as skills (chapter ' + s7n + ' has Grade 7; the I–IV–I⁶₄–V–I progressions and the arpeggios are the next chapter). From the technical work book, Grade 8: the abbreviated grand scale, E major, C♯ harmonic minor, B♭ major, G harmonic minor, four octaves, (i) all p (ii) all f, clear even legato, ♩ = 92 four notes a beat; the polyrhythmic scale, two against three, E major, commencing two octaves apart, right hand two octaves, left hand three, mf, legato, ♩ = 100; hands together a third apart (the left hand on the tonic) and a sixth apart (the right hand on the tonic), the same four keys, four octaves, mf, ♩ = 100 four notes a beat; chromatic scales from E and from A♯/B♭, hands separately and together, grouped in sixes, three octaves, mf, legato, ♩ = 70 six notes a beat (felt as three pairs, played evenly, without accents); the chromatic scale in double minor thirds from C and E♭, hands separately, two octaves, mf, legato, ♩ = ca 80 two notes a beat (quality before speed). The exercises 8A, 8B and 8C stay with the book; step 5 (page 6) practises the legato double notes of 8A.', '8급 스케일을 기술로(' + s7n + '장은 7급; I–IV–I⁶₄–V–I 진행과 아르페지오는 다음 장). 테크닉 책의 8급: 줄인 그랜드 스케일, E장조, C♯ 화성 단음계, B♭장조, G 화성 단음계, 네 옥타브, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 92 한 박에 네 음; 폴리리듬 스케일 2 대 3, E장조, 두 옥타브 떨어져 시작, 오른손 두 옥타브, 왼손 세 옥타브, mf, 레가토, ♩ = 100; 3도 떨어진 양손(왼손이 으뜸음)과 6도 떨어진 양손(오른손이 으뜸음), 같은 네 조, 네 옥타브, mf, ♩ = 100 한 박에 네 음; E와 A♯/B♭에서 여섯 음씩 반음계, 한 손씩 그리고 양손, 세 옥타브, mf, 레가토, ♩ = 70 한 박에 여섯 음(둘씩 셋으로 느끼되 강세 없이 고르게); C와 E♭에서 겹단3도 반음계, 한 손씩, 두 옥타브, mf, 레가토, ♩ = 약 80 한 박에 두 음(빠르기보다 소리). 연습곡 8A, 8B, 8C는 책에; 5단계(6쪽)가 8A의 레가토 겹음을 연습해요.'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={150}><div style={{width:'100%',maxWidth:440,margin:'0 auto'}}><PsRoute k="E8" w={440}/></div></LbPic>
      <LbSay size={18}>{t('Grade 8 scales, the top floor: the grand scale all p and all f, two against three, hands a third and a sixth apart, chromatic in sixes, and double thirds.', '맨 위층 8급 스케일: 모두 p와 모두 f의 그랜드 스케일, 2 대 3, 3도와 6도 떨어진 양손, 여섯 음씩 반음계, 그리고 겹3도.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The grand scale, Grade 8', '그랜드 스케일, 8급')}
      teacher={<>{spTx(t('E major, C♯ harmonic minor, B♭ major and G harmonic minor in the abbreviated grand scale format, four octaves, (i) all p (ii) all f, clear even legato, ♩ = 92 four notes a beat. The same route as Grades 6 and 7. The ear game: major or harmonic minor?', 'E장조, C♯ 화성 단음계, B♭장조, G 화성 단음계, 줄인 그랜드 스케일, 네 옥타브, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 92 한 박에 네 음. 6, 7급과 같은 길. 귀 놀이: 장조? 화성 단음계?'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:12,width:'100%',maxWidth:700,margin:'0 auto'}}>{['E8', 'Gmh8'].map(x => <div key={x}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{t(S6_GR[x].en, S6_GR[x].ko)}</div><GrRoute k={x} w={330}/></div>)}</div></LbPic>} live={<S8GrandPad/>}/>
      <LbSay>{LANG === 'ko' ? <>세 번째 그랜드 스케일. 이제 <b>셈여림</b>이 일: 처음부터 끝까지 <b>모두 p</b>, 그다음 <b>모두 f</b>. 방향이 바뀌는 곳에서도 크기가 그대로.</> : <>Your third grand scale. Now the work is <b>the dynamic</b>: <b>all p</b> from start to finish, then <b>all f</b>, the same level through every turn.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E장조, 1·2부분을 모두 p로.</>, <>네 부분 모두, 모두 f로. 그다음 C♯ 화성 단음계.</>, <>B♭장조와 G 화성 단음계. {spMM(92)}까지.</>]
        : [<>E major, parts 1 and 2, all p.</>, <>All four parts, all f. Then C♯ harmonic minor.</>, <>B♭ major and G harmonic minor. Up to {spMM(92)}.</>]}/>
      <LbRemember>{t('The same level through every turn.', '방향이 바뀌어도 같은 크기.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Two against three, as a scale', '2 대 3, 스케일로')}
      teacher={<>{spTx(t('The polyrhythmic scale, hands together in similar motion, two against three, E major, commencing two octaves apart: the right hand two octaves in quavers, the left hand three octaves in triplets, mf, legato, ♩ = 100. Grade 7 was the other way round. Inside each beat: both, left, right, left.', '폴리리듬 스케일, 같은 방향 양손, 2 대 3, E장조, 두 옥타브 떨어져 시작: 오른손은 8분음표로 두 옥타브, 왼손은 셋잇단으로 세 옥타브, mf, 레가토, ♩ = 100. 7급은 그 반대였어요. 박 안에서: 함께, 왼, 오, 왼.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:520,margin:'0 auto'}}><PsRoute k="E8" w={520}/></div></LbPic>} live={<S8PolyScalePad/>}/>
      <LbSay>{LANG === 'ko' ? <>7급을 뒤집어요: 이제 <b>왼손이 셋</b>, 오른손이 둘. 박 안에서 <b>함께, 왼, 오, 왼</b>.</> : <>Grade 7 turned over: now <b>the left hand has three</b>, the right hand two. Inside each beat: <b>both, left, right, left</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>무릎에서 "함께, 왼, 오, 왼".</>, <>E장조 한 옥타브씩, 천천히. 두 손을 두 옥타브 떨어뜨려요.</>, <>오른손 두 옥타브, 왼손 세 옥타브. {spMM(100)}까지.</>]
        : [<>On your knees: "both, left, right, left".</>, <>E major, one octave at a time, slowly, the hands two octaves apart.</>, <>Right hand two octaves, left hand three. Up to {spMM(100)}.</>]}/>
      <LbRemember>{t('Both, left, right, left.', '함께, 왼, 오, 왼.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('A third apart, a sixth apart', '3도 떨어져, 6도 떨어져')}
      teacher={<>{spTx(t('Hands together a third apart (the left hand commencing on the tonic) and a sixth apart (the right hand commencing on the tonic): E major, C♯ harmonic minor, B♭ major, G harmonic minor, four octaves, mf, clear even legato, ♩ = 100 four notes a beat. Each hand keeps its own fingering for the notes it plays; either way the other hand starts on the 3rd of the scale.', '3도 떨어진 양손(왼손이 으뜸음에서)과 6도 떨어진 양손(오른손이 으뜸음에서): E장조, C♯ 화성 단음계, B♭장조, G 화성 단음계, 네 옥타브, mf, 고르고 또렷한 레가토, ♩ = 100 한 박에 네 음. 손마다 자기가 치는 음의 운지를 지켜요; 어느 쪽이든 다른 손은 스케일의 3음에서 시작해요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}>{apartStill}</LbPic>} live={<S8ApartPad/>}/>
      <LbSay>{LANG === 'ko' ? <>3도 떨어져: 왼손 으뜸음, 오른손 <b>3음</b>. 6도 떨어져: 오른손 으뜸음, 왼손 <b>3음</b>. 두 손이 나란히 노래해요.</> : <>A third apart: the left hand on the tonic, the right on <b>the 3rd</b>. A sixth apart: the right hand on the tonic, the left on <b>the 3rd</b>. The hands sing together in parallel.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E장조: 왼손 E, 오른손 G♯에서 한 옥타브.</>, <>6도: 오른손 E, 왼손 그 아래 G♯에서.</>, <>네 조 모두, 네 옥타브. {spMM(100)}까지.</>]
        : [<>E major: the left hand from E, the right from G♯, one octave.</>, <>Sixths: the right hand from E, the left from the G♯ below.</>, <>All four keys, four octaves. Up to {spMM(100)}.</>]}/>
      <LbRemember>{t('Either way, the other hand starts on the 3rd.', '어느 쪽이든 다른 손은 3음에서.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Chromatic in sixes', '여섯 음씩 반음계')}
      teacher={<>{spTx(t('Chromatic scales from E and from A♯/B♭, hands separately and together in similar motion, grouped in sixes, three octaves, mf, legato, ♩ = 70 six notes a beat. The book: each group of six should be felt as three pairs rather than two groups of three; played evenly and without accents. The ear game exaggerates the accents to make the grouping audible.', 'E와 A♯/B♭에서 반음계, 한 손씩 그리고 같은 방향 양손, 여섯 음씩, 세 옥타브, mf, 레가토, ♩ = 70 한 박에 여섯 음. 책: 여섯 음 묶음은 셋씩 둘이 아니라 둘씩 셋으로 느끼고, 강세 없이 고르게. 귀 놀이는 묶음이 들리도록 강세를 과장해요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={120}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:16,width:'100%',maxWidth:620,margin:'0 auto'}}>{['pairs', 'threes'].map(g => <div key={g} style={{textAlign:'center'}}><div style={{fontSize:13.5,fontWeight:900,color:g === 'pairs' ? BK.ink : BK.muted}}>{g === 'pairs' ? t('Three pairs ✓', '둘씩 셋 ✓') : t('Not two threes', '셋씩 둘이 아니라')}</div><div style={{display:'flex',justifyContent:'center',gap:3,marginTop:6}}>{[0, 1, 2, 3, 4, 5].map(i => <span key={i} style={{flex:'0 0 auto',width:scr ? 18 : 30,height:scr ? 18 : 30,borderRadius:15,border:'2px solid ' + BK.ink,background:(g === 'pairs' ? i % 2 === 0 : i % 3 === 0) ? BK.coral : '#fff',marginRight:(g === 'pairs' ? i % 2 === 1 : i % 3 === 2) && i < 5 ? (scr ? 7 : 14) : 0}}/>)}</div></div>)}</div></LbPic>} live={<S8SixesPad/>}/>
      <LbSay>{LANG === 'ko' ? <>한 박에 여섯. 속으로는 <b>둘, 둘, 둘</b>; 소리는 <b>강세 없이 고르게</b>.</> : <>Six to a beat. Inside, feel <b>two, two, two</b>; outside, play <b>evenly, no accents</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E에서 한 옥타브, 둘씩 살짝 강세를 주며 천천히.</>, <>강세를 빼고 고르게.</>, <>B♭에서도, 세 옥타브, {spMM(70)}까지.</>]
        : [<>From E, one octave, slowly, with a little accent on each pair.</>, <>Take the accents away: even.</>, <>From B♭ too, three octaves, up to {spMM(70)}.</>]}/>
      <LbRemember>{t('Feel pairs, play even.', '둘씩 느끼고, 고르게 쳐요.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Chromatic in double minor thirds', '반음계 겹단3도')}
      teacher={<>{spTx(t('The chromatic scale in double minor thirds from C and E♭, hands separately, two octaves, mf, legato, ♩ = ca 80 two notes a beat; quality and evenness of tone matter more than speed (book p75). The book\'s right-hand fingering going up, bottom/top, from C: 1/3, 2/4, 1/5, 2/3, 1/4, 1/3, 2/4, 1/3, 2/4, 1/5, 2/3, 1/4 (then again); the left hand\'s is in the book. The skill of exercise 8A (legato double notes) in a scale.', 'C와 E♭에서 겹단3도 반음계, 한 손씩, 두 옥타브, mf, 레가토, ♩ = 약 80 한 박에 두 음; 빠르기보다 고르고 좋은 소리(75쪽). 책의 오른손 운지(올라가며, 아래/위), C부터: 1/3, 2/4, 1/5, 2/3, 1/4, 1/3, 2/4, 1/3, 2/4, 1/5, 2/3, 1/4(그다음 반복); 왼손은 책에. 연습곡 8A(레가토 겹음)의 기술을 스케일로.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={150}>{dtStill}</LbPic>} live={<S8DThirdsPad/>}/>
      <LbSay>{LANG === 'ko' ? <>아랫음은 1과 2가 <b>번갈아</b>, 윗음은 <b>3 4 5</b>를 돌아요. 5번은 <b>F와 C</b>에: 7급 3-4-5 반음계와 같은 자리!</> : <>The bottom notes <b>take turns, 1 and 2</b>; the top notes go round <b>3 4 5</b>. Finger 5 lands on <b>F and C</b>: the same places as Grade 7's 3-4-5 chromatic!</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>오른손, C와 E♭에서 셋만: 1/3, 2/4, 1/5.</>, <>한 옥타브, 아주 천천히, 이어서.</>, <>두 옥타브, 약 {spMM(80)}. 왼손은 책의 운지로.</>]
        : [<>Right hand, from C and E♭, just three: 1/3, 2/4, 1/5.</>, <>One octave, very slowly, joined.</>, <>Two octaves, about {spMM(80)}. The left hand with the book's fingering.</>]}/>
      <LbRemember>{t('1 and 2 take turns; 3 4 5 go round.', '1과 2는 번갈아; 3 4 5는 돌아요.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one played to you from memory at the book\'s speeds (the teacher\'s copy lists the keys). Listen for an even all p and all f through the grand scale\'s turns, a steady two against three, the right starting notes a third and a sixth apart, even sixes, and legato double thirds.', '하나씩 외워서 책의 빠르기로 들려줘요(선생님용에 조 목록). 그랜드 스케일의 방향 바꾸기에서도 고른 모두 p와 모두 f, 고른 2 대 3, 3도와 6도 떨어진 바른 시작 음, 고른 여섯 음, 레가토 겹3도를 들어 주세요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey="pb_s8_five"/>}/>
    </LbPage>,
  ];
}
function Scales8LessonBook() { return <>{s8LbPages(false)}</>; }
function S8Learn({ onStart }) {
  const pages = s8LbPages(true), opener = pages[0];
  return (
    <Lesson id="scales-8" title={bkChapterName('scales-8')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scales-8"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
const S8_LEVELS = [
  { n: 1, label: 'Grade 8 grand scale: major or harmonic minor?', kind: 'grand', time: 25 },
  { n: 2, label: 'Two against three: which comes next?', kind: 'poly', time: 15 },
  { n: 3, label: 'A third or a sixth apart: where does the other hand start?', kind: 'apart', time: 15 },
  { n: 4, label: 'Sixes: pairs or threes?', kind: 'sixes', time: 20 },
  { n: 5, label: 'Double thirds: which fingers?', kind: 'dt', time: 15 },
];
Object.assign(LEVEL_KO, { 'Grade 8 grand scale: major or harmonic minor?': '8급 그랜드 스케일: 장조? 화성 단음계?', 'Two against three: which comes next?': '2 대 3: 다음은?', 'A third or a sixth apart: where does the other hand start?': '3도·6도 떨어져: 다른 손은 어디서?', 'Sixes: pairs or threes?': '여섯 음: 둘씩? 셋씩?', 'Double thirds: which fingers?': '겹3도: 어떤 손가락?' });
function genS8Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'grand') { let k, g = 0; do { k = pick(S8_GR_KEYS); } while (prev && prev.key === k && g++ < 10); return { kind, k, bpm: 92, answer: s7GrMinor(k) ? 'm' : 'M', choices: ['M', 'm'], key: k, uid }; }
  if (kind === 'apart') { let k, kd, g = 0; do { k = pick(S8_GR_KEYS); kd = pick(['third', 'sixth']); } while (prev && prev.key === k + kd && g++ < 10); const c = S6_GR[k], opts = [c.nm[2], c.nm[4], c.nm[5], c.nm[1]];
    return { kind, k, kd, answer: c.nm[2], choices: shuffle(opts), key: k + kd, uid }; }
  if (kind === 'sixes') { let gq, st, g = 0; do { gq = pick(['pairs', 'threes']); st = pick(['E', 'Bb']); } while (prev && prev.key === gq + st && g++ < 10); return { kind, g: gq, st, answer: gq, choices: ['pairs', 'threes'], key: gq + st, uid }; }
  if (kind === 'dt') { let at, g = 0; do { at = Math.floor(Math.random() * 12); } while (prev && prev.key === 'd' + at && g++ < 10); return { kind, at, answer: DT_F[at].join(' '), choices: DT_OPTS.slice(), key: 'd' + at, uid }; }
  let sl, g = 0; do { sl = pick([2, 3, 4]); } while (prev && prev.key === 'p' + sl && g++ < 10); const x = ppGrid('2:3')[sl];
  return { kind: 'poly', r: '2:3', sl, answer: x.R && x.L ? 'B' : x.R ? 'R' : x.L ? 'L' : 'N', choices: ['B', 'R', 'L'], key: 'p' + sl, uid };
}
function S8Question(props) {
  const { q, given, locked, onAnswer, pixel } = props;
  if (q.kind === 'poly') return <S6Question {...props}/>;
  if (q.kind === 'grand') return <S7Question {...props} q={{ ...q }}/>;
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  const play = () => { stopClicks(); if (q.kind === 'sixes') sxPlay(SX_START[q.st], q.g, 50); else if (q.kind === 'dt') spPlay([{ at: 0, keys: [q.at, q.at + 3], len: 1, vol: 0.13 }], 80); else if (q.kind === 'apart') apartPlay(q.k, q.kd); };
  useEffect(() => { if (q.kind !== 'sixes') return; const id = setTimeout(play, 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:14.5,fontWeight:900,lineHeight:1.2}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  let title, body;
  if (q.kind === 'apart') { const c = S6_GR[q.k]; title = q.kd === 'third' ? t(c.en + ', a third apart: the left hand starts on ' + c.nm[0] + '. Where does the right hand start?', c.ko + ', 3도 떨어져: 왼손은 ' + c.nm[0] + '. 오른손은?') : t(c.en + ', a sixth apart: the right hand starts on ' + c.nm[0] + '. Where does the left hand start?', c.ko + ', 6도 떨어져: 오른손은 ' + c.nm[0] + '. 왼손은?'); body = grid(4, q.choices.map(x => [x, x])); }
  else if (q.kind === 'sixes') { title = t('Six notes a beat, with exaggerated accents: pairs or threes?', '한 박에 여섯, 과장된 강세: 둘씩? 셋씩?'); body = <><div style={{textAlign:'center'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>{grid(2, [['pairs', t('Pairs', '둘씩')], ['threes', t('Threes', '셋씩')]])}</>; }
  else { title = t('Double minor thirds, right hand going up: which fingers play ' + lwLet(q.at) + ' + ' + dtTop(q.at) + ' (bottom, top)?', '겹단3도, 오른손 올라가며: ' + lwLet(q.at) + ' + ' + dtTop(q.at) + '은 몇 번(아래, 위)?');
    body = <><SpKb lo={0} hi={15} W={22} H={70} lit={{ [q.at]: 'cor', [q.at + 3]: 'cor' }} names={{ [q.at]: lwLet(q.at), [q.at + 3]: dtTop(q.at) }}/>{grid(5, q.choices.map(x => [x, x]))}</>; }
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
  </div>);
}
const s8AnswerLabel = (q) => (q.kind === 'grand' ? (q.answer === 'm' ? t('Harmonic minor', '화성 단음계') : t('Major', '장조')) : q.kind === 'sixes' ? (q.answer === 'pairs' ? t('Pairs', '둘씩') : t('Threes', '셋씩')) : q.kind === 'poly' ? ({ B: t('both', '함께'), R: t('right', '오'), L: t('left', '왼'), N: t('nothing', '없음') })[q.answer] : String(q.answer));
Object.assign(SCALES_8_DRILL, { levels: S8_LEVELS, generate: genS8Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: s8AnswerLabel, Question: S8Question, Learn: S8Learn });
const S8_WB = {
  apart: [['E8', 'third'], ['E8', 'sixth'], ['Bb8', 'third'], ['Gmh8', 'sixth']],
  chk: { minor: ['Csmh8', 'Gmh8'], apart: [['Csmh8', 'third'], ['Bb8', 'sixth'], ['Gmh8', 'third'], ['E8', 'sixth']], dt: [0, 2, 5, 9] },
};
function S8Teacher() {
  const pages = [], W = S8_WB;
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scales-8" teacher>{content}</WbPage>);
  const startOf = ([k, kd]) => S6_GR[k].en + ', ' + kd + ' apart: ' + (kd === 'third' ? 'LH ' + S6_GR[k].nm[0] + ', RH ' + S6_GR[k].nm[2] : 'RH ' + S6_GR[k].nm[0] + ', LH ' + S6_GR[k].nm[2]);
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scales-8')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>{spTx('The keys, speeds and fingerings are the technical work book\'s (Grade 8 pp68-75). Scales at the book\'s compass, from memory; the book prints two octaves (in most cases start an octave lower). The exercises 8A, 8B and 8C stay with the book.')}</div>
    <TcBlock page={2} title="The grand scale, Grade 8" answers={<>{tcAns(spTx('FOUR OCTAVES, (i) ALL p (ii) ALL f, ♩ = 92'), S8_GR_KEYS.map(k => S6_GR[k].en + ': ' + S6_GR[k].nm.join(' ')), null)}</>}
      watch="The dynamic creeping up in all p, or a bump where the hands turn. Record it and listen back."
      say="“The same level through every turn.”"/>
    <TcBlock page={3} title="Two against three, as a scale" answers={<>{tcAns(spTx('E MAJOR, TWO OCTAVES APART, ♩ = 100'), ['RH 2 octaves, two a beat', 'LH 3 octaves, three a beat', 'both, left, right, left'], null)}</>}
      watch="The right hand's quavers pulled into the triplets. Say the words; slow first."
      say="“Both, left, right, left.”"/>
    <TcBlock page={4} title="A third apart, a sixth apart" answers={<>{tcAns('TRY IT', W.apart.map(startOf))}</>}
      watch="The second hand copying the first hand's fingering. Each hand plays its own notes with that scale's fingering from where it starts."
      say="“Either way, the other hand starts on the 3rd.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Chromatic in sixes" answers={<>{tcAns(spTx('FROM E AND A♯/B♭, THREE OCTAVES, ♩ = 70 SIX A BEAT'), ['felt as three pairs', 'played evenly, no accents'], null)}</>}
      watch="Accents on every third note (two threes) or audible pairs at speed. Feel the pairs; let the sound be even."
      say="“Feel pairs, play even.”"/>
    <TcBlock page={6} title="Chromatic in double minor thirds" answers={<>{tcAns('RH UP FROM C (BOTTOM/TOP)', DT_F.map((f, j) => lwLet(j) + ': ' + f.join('/')), null)}</>}
      watch="The top line broken (fingers lifted early). Legato in the upper line matters most; quality before speed."
      say="“1 and 2 take turns; 3 4 5 go round.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', W.chk.minor.map(k => S6_GR[k].nm[6]))}{tcAns('B', W.chk.apart.map(([k]) => S6_GR[k].nm[2]), 3)}{tcAns('C', W.chk.dt.map(a => DT_F[a].join('/')), 7)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (A: 2 marks, pass 2; B and C: 4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.4 · C p.6.</div></>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['scales-8'] = S8Teacher;
function S8Workbook({ startNo = 1 }) {
  const W = S8_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="scales-8">{content}</WbPage>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Where does the other hand start?" how="Write the note the other hand starts on. A third apart: the left hand is on the tonic. A sixth apart: the right hand is.">
      <BkGrid cols={2} gap="6px 10px">{W.apart.map(([k, kd], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 6px',justifyItems:'center',fontSize:12,fontWeight:800,color:BK.ink,textAlign:'center'}}>{S6_GR[k].en + ', a ' + kd + ' apart'}<span>{kd === 'third' ? 'LH ' + S6_GR[k].nm[0] + ' · RH ' : 'RH ' + S6_GR[k].nm[0] + ' · LH '}{nvBox(i === 0, S6_GR[k].nm[2], 44, 26)}</span></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Grade 8 scales this week" how="Tick a box each day.">
      <PhLog rows={spTxRows(['The grand scale in E, all p then all f', 'E major a third apart, then a sixth apart', 'E major two against three, slowly, then up to ♩ = 100'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Fingers for double thirds" how="The right hand going up from C. Write the fingers for each third: bottom, then top.">
      <BkGrid cols={4} gap="6px 8px">{[0, 1, 2, 3, 4, 5, 6, 7].map((a, i) => <ExCell key={a} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 2px 4px',justifyItems:'center',fontSize:12,fontWeight:800,color:BK.ink}}>{lwLet(a) + ' + ' + dtTop(a)}{nvBox(i === 0, DT_F[a].join('/'), 50, 26)}</div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Sixes and thirds this week" how="Tick a box each day.">
      <PhLog rows={spTxRows(['Chromatic from E in sixes, a little accent on each pair, slowly', 'The same, even, then from B♭; up to ♩ = 70', 'Double minor thirds from C, one octave, very slowly'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<S8PaperCheck/>);
  return <>{pages}</>;
}
function S8PaperCheck() {
  const C = S8_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Write the raised 7th of each harmonic minor')}
    <BkGrid cols={2} gap="6px 8px">{C.minor.map((k, i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11.5,fontWeight:800,color:BK.ink}}>{S6_GR[k].en}{bkBox(44, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'Where does the other hand start?')}
    <BkGrid cols={2} gap="6px 8px">{C.apart.map(([k, kd], i) => <BkCell key={i} n={i + 3}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>{S6_GR[k].en + ', a ' + kd + ' apart (' + (kd === 'third' ? 'LH' : 'RH') + ' on ' + S6_GR[k].nm[0] + ')'}{bkBox(44, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Double minor thirds, right hand going up: which fingers? (bottom/top)')}
    <BkGrid cols={4} gap="6px 8px">{C.dt.map((a, i) => <BkCell key={i} n={i + 7}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11.5,fontWeight:800,color:BK.ink}}>{lwLet(a) + ' + ' + dtTop(a)}{bkBox(50, 24)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['scales-8'] = S8Workbook;
'''
rep("""WORKBOOKS['scales-7'] = S7Workbook;""", """WORKBOOKS['scales-7'] = S7Workbook;""" + CH)

HOME = r'''
// ══ Build BY: Scales, Grade 8 on the Home (Technique, Playing scales) ══
LBH_FN['scales-8'] = (s) => s8LbPages(s);
const s8HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('scales-8', i, { make }));
const s8GrandQ = (n, prev) => { const q = genS8Question(S8_LEVELS[0], prev);
  return { kind: 'choice', cols: 2, key: q.key, prompt: ['Part 1 of a grand scale: major or harmonic minor?', '그랜드 스케일의 1부분: 장조? 화성 단음계?'], opts: [{ id: 'M', label: () => t('Major', '장조') }, { id: 'm', label: () => t('Harmonic minor', '화성 단음계') }], ans: q.answer, ok: (v) => v === q.answer,
    play: () => grPlay(q.k, 0, 92), fig: (c) => ({ mid: <GrRoute k={q.k} hl={c.res ? 0 : null}/> }), yes: ['Yes.', '맞아요.'], no: ['It was ' + S6_GR[q.k].en + '.', '정답은 ' + S6_GR[q.k].ko + '.'] }; };
const s8ApartQ = (n, prev) => { const q = genS8Question(S8_LEVELS[2], prev), c = S6_GR[q.k];
  return { kind: 'choice', cols: 4, key: q.key, prompt: q.kd === 'third' ? [c.en + ', a third apart: LH on ' + c.nm[0] + '. The RH starts on…', c.ko + ', 3도 떨어져: 왼손 ' + c.nm[0] + '. 오른손은…'] : [c.en + ', a sixth apart: RH on ' + c.nm[0] + '. The LH starts on…', c.ko + ', 6도 떨어져: 오른손 ' + c.nm[0] + '. 왼손은…'], opts: q.choices.map(x => ({ id: x, label: () => x })), ans: q.answer, ok: (v) => v === q.answer,
    play: () => apartPlay(q.k, q.kd), fig: () => ({ mid: null }), yes: ['Yes: the 3rd, ' + q.answer + '.', '맞아요: 3음, ' + q.answer + '.'], no: ['It is the 3rd, ' + q.answer + '.', '정답은 3음, ' + q.answer + '.'] }; };
const s8SixesQ = (n, prev) => { const q = genS8Question(S8_LEVELS[3], prev);
  return { kind: 'choice', cols: 2, key: q.key, prompt: ['Six a beat, accents exaggerated: pairs or threes?', '한 박에 여섯, 과장된 강세: 둘씩? 셋씩?'], opts: [{ id: 'pairs', label: () => t('Pairs', '둘씩') }, { id: 'threes', label: () => t('Threes', '셋씩') }], ans: q.answer, ok: (v) => v === q.answer,
    play: () => sxPlay(SX_START[q.st], q.g, 50), fig: () => ({ mid: null }), yes: ['Yes.', '맞아요.'], no: ['It was ' + q.answer + '.', '정답은 ' + (q.answer === 'pairs' ? '둘씩' : '셋씩') + '.'] }; };
s8HomeAdd('s8-grand', 1, 'The grand scale, Grade 8', '그랜드 스케일, 8급', 'E, C♯ minor, B♭ and G minor: major or harmonic minor?', 'E, C♯단조, B♭, G단조: 장조? 화성 단음계?', s8GrandQ);
s8HomeAdd('s8-poly', 2, 'Two against three, as a scale', '2 대 3, 스케일로', 'Two octaves against three: they meet at the top.', '두 옥타브 대 세 옥타브: 꼭대기에서 만나요.', lwTapQ(S8PolyScalePad, () => ({}), ['Guess first, then listen.', '먼저 맞혀 보고, 들어요.'], ['They meet at the top ✓', '꼭대기에서 만나요 ✓']));
s8HomeAdd('s8-apart', 3, 'A third apart, a sixth apart', '3도 떨어져, 6도 떨어져', 'The other hand always starts on the 3rd.', '다른 손은 언제나 3음에서.', s8ApartQ);
s8HomeAdd('s8-sixes', 4, 'Chromatic in sixes', '여섯 음씩 반음계', 'Feel three pairs; play even.', '둘씩 셋으로 느끼고, 고르게.', s8SixesQ);
s8HomeAdd('s8-dt', 5, 'Chromatic in double minor thirds', '반음계 겹단3도', '1 and 2 take turns; 3 4 5 go round.', '1과 2는 번갈아; 3 4 5는 돌아요.', lwTapQ(S8DThirdsPad, (n) => ({ fixed: { at: (n * 5) % 12 } }), ['Which fingers play this third?', '이 3도는 몇 번?'], ['Right fingers ✓', '맞는 손가락 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""check: 'arps-7' },   // Build BV""", """check: 'arps-7' },   // Build BV
    { id: 'kpl-8', en: 'Scales, Grade 8', ko: '스케일, Grade 8', lessons: ['s8-grand', 's8-poly', 's8-apart', 's8-sixes', 's8-dt', 'mk-thirds'], check: 'scales-8' },   // Build BY""")
rep("""  set('7', 'p78-form p78-tonal p78-mvt p78-genre mk-map');   // Build BW: Knowing Your Pieces, Grades 7 and 8""", """  set('7', 'p78-form p78-tonal p78-mvt p78-genre mk-map');   // Build BW: Knowing Your Pieces, Grades 7 and 8
  set('8', 's8-grand s8-poly s8-apart s8-sixes s8-dt mk-thirds');   // Build BY: Scales, Grade 8""")
rep("""  { id: 'mk-cad', ch: 'listen-6',""", """  { id: 'mk-thirds', ch: 'scales-8', title: 'My tune in thirds and sixths', blurb: 'Play a tune; a second voice follows a 3rd or a 6th below, in the key.', C: () => <ThirdsMaker/> },   // Build BY
  { id: 'mk-cad', ch: 'listen-6',""")
rep("""  'mk-cad': ['나만의 끝 만들기',""", """  'mk-thirds': ['3도와 6도로 내 선율', '선율을 치면 둘째 성부가 그 조 안에서 3도나 6도 아래로 따라와요.'],
  'mk-cad': ['나만의 끝 만들기',""")
rep("""'mk-cad': ['chords', 3, 3, 'game ear'],""", """'mk-cad': ['chords', 3, 3, 'game ear'], 'mk-thirds': ['scales', 3, 3, 'game ear'],""")
rep("""'mk-cad': 'p-chords',""", """'mk-cad': 'p-chords', 'mk-thirds': 'p-scales',""")
rep("""  'mk-cad': () => (\n""", """  'mk-thirds': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><path d="M3 10 L9 7 L15 9 L21 5" fill="none" stroke="#e9a83a" strokeWidth="2"/><path d="M3 15 L9 12 L15 14 L21 10" fill="none" stroke="#fefbf3" strokeWidth="2"/></svg>
  ),
  'mk-cad': () => (\n""")
rep("""const LESSON_BOOKS = { 'listen-8': Listen8LessonBook,""", """const LESSON_BOOKS = { 'scales-8': Scales8LessonBook, 'listen-8': Listen8LessonBook,""")
rep("""const LB_PAGE_FNS = { 'listen-8': l8LbPages,""", """const LB_PAGE_FNS = { 'scales-8': s8LbPages, 'listen-8': l8LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"scales-8": "<path d=\\"M4 30 L24 10 L44 30\\" stroke=\\"#e4572e\\" stroke-width=\\"2.6\\"/><path d=\\"M4 38 L24 18 L44 38\\"/><text x=\\"20\\" y=\\"44\\" font-size=\\"9\\" font-weight=\\"900\\" fill=\\"#26296b\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">8</text>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
