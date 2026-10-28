import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CG (call 25, batch 5; her 09:56: fun first): the Prelim and Grade 1 rooms still without a thing to make.
#   Ear Training, Prelim: Be the examiner (the child sets one of the Prelim tests, the app plays it the exam's way, the
#     teacher answers, the child marks it with a stamp)
#   Ear Training, Grade 1: Leave them hanging (a tune that stops before it gets home; three stars: stop on 2, stop on 5,
#     come home; then the listener hums home)
#   Scales: Only the key's notes (a tune in C, G or F major where only the scale's notes play, degree numbers shown; stars:
#     start and end on 1, use all seven, only 1 3 5)
#   Playing scales: Scale remix (one scale, four rhythms: even, long-short, short-long, in threes; play along)
#   6/8: My 6/8 rhythm (two bars of 6/8 from four groups of three: long-short, three quavers, one long, short-long; looped,
#     beats 1 and 4 marked)

CODE = r'''
// ══ Build CG: batch 5, the Prelim and Grade 1 rooms' things to make (call 25; her 09:56: fun first) ══
// ── Ear Training, Prelim: Be the examiner ──
const EX_TESTS = [['echo', 'Echo the rhythm', '리듬 메아리'], ['sing', 'Sing it back', '따라 부르기'], ['updown', 'Higher or lower', '높을까, 낮을까?']];
function ExaminerPad() {
  const ts = useRef([]), clear = () => { ts.current.forEach(clearTimeout); ts.current = []; };
  useEffect(() => () => clear(), []);
  const [test, setTest] = useState('echo'), [cells, setCells] = useState(['w', 'w', 'r', 'w', 'w', 'w', 'w', '.']), [tune, setTune] = useState([1, 2, 3, 2, 1]), [pair, setPair] = useState([]), [msg, setMsg] = useState(null), [stamp, setStamp] = useState(null), [asked, setAsked] = useState(false);
  const flip = (j) => { const n = cells.slice(); n[j] = TK_CYCLE[n[j]]; setCells(n); setStamp(null); setAsked(false); };
  const ask = () => { clear(); setStamp(null); setAsked(true);
    if (test === 'echo') { const spb = 60 / 84; lsBar(cells.slice(0, 4), 0, spb, ts.current); lsBar(cells.slice(4), 4 * spb * 1000, spb, ts.current); }
    else if (test === 'sing') { const ds = tune.map(f => hpFingerD('C', 'R', f)); lsSeq(ds, 650); ds.forEach((d, j) => ts.current.push(setTimeout(() => lsPlay(d, 0.8), ds.length * 650 + 1200 + j * 1700))); }
    else if (pair.length === 2) lsSeq(pair, 900); };
  const tapKey = (f) => { const d = hpFingerD('C', 'R', f); lsPlay(d, 0.5); setStamp(null); setAsked(false);
    if (test === 'sing') { if (tune.length < 6) setTune(tune.concat([f])); return; }
    const p = pair.length >= 2 ? [d] : pair.concat([d]); if (p.length === 2 && Math.abs(p[1] - p[0]) < 2) { setMsg('close'); setPair([p[0]]); return; } setMsg(null); setPair(p); };
  const ready = test === 'echo' || (test === 'sing' && tune.length >= 5) || (test === 'updown' && pair.length === 2);
  return (
    <div className="try-box" style={actBox} data-mk="examiner">
      <div style={actTitle}>{t('Be the examiner', '시험관 되기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>오늘은 내가 시험관! 시험 하나를 골라 <b>문제를 만들어요</b>. 앱이 시험처럼 들려주면, 선생님(이나 가족)이 답해요. 그다음 도장을 찍어 줘요.</> : <>Today <b>you</b> are the examiner! Pick a test and <b>set the question</b>. The app plays it the exam's way; your teacher (or anyone at home) answers. Then you stamp it.</>}</div>
      {spChips(EX_TESTS.map(([id, en, ko]) => [id, t(en, ko)]), test, (x) => { clear(); setTest(x); setStamp(null); setAsked(false); setMsg(null); })}
      {test === 'echo' && <div style={{display:'flex',justifyContent:'center',gap:2,flexWrap:'nowrap',margin:'6px 0'}}>{cells.map((v, j) => <React.Fragment key={j}>{j === 4 && <span style={{width:2,background:BK.ink,margin:'0 3px',flex:'0 0 auto'}}/>}
        <button onClick={() => flip(j)} style={{width:36,minHeight:48,borderRadius:18,border:'2px solid ' + BK.ink,background:'#fff',display:'inline-flex',flexDirection:'column',alignItems:'center',justifyContent:'center',gap:2,cursor:'pointer',fontFamily:'inherit',padding:0}}>
          <span style={{display:'flex',gap:2}}>{v === '.' ? <span style={{width:8,height:8,borderRadius:4,border:'1.5px solid ' + BK.line}}/> : (v === 'r' ? [0, 1] : [0]).map(k => <span key={k} style={{width:v === 'r' ? 7 : 10,height:v === 'r' ? 7 : 10,borderRadius:5,background:BK.coral}}/>)}</span><span style={{fontSize:8.5,fontWeight:800,color:BK.muted,whiteSpace:'nowrap'}}>{tkWord(v)}</span></button></React.Fragment>)}</div>}
      {test !== 'echo' && <><div style={{display:'flex',gap:6,justifyContent:'center',minHeight:38,margin:'4px 0'}}>{(test === 'sing' ? tune.map(f => 'CDEFG'[f - 1]) : pair.map(d => 'CDEFGAB'[(d - 28 + 70) % 7])).map((L, j) => <span key={j} style={{width:34,height:34,borderRadius:17,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,border:'2px solid ' + BK.ink}}>{L}</span>)}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6}}>{[1, 2, 3, 4, 5].map(f => <button key={f} className="choice-btn" onClick={() => tapKey(f)} style={{padding:'10px 0',fontSize:17,fontWeight:900}}>{'CDEFG'[f - 1]}</button>)}</div></>}
      {spMsg(msg === 'close' ? t('In the exam the two notes are at least a 3rd apart: pick another.', '시험에서는 두 음이 3도 이상 떨어져 있어요: 다른 음을 골라요.')
        : asked && test === 'updown' ? t('The answer: ' + (pair[1] > pair[0] ? 'higher, up to the bird.' : 'lower, down to the turtle.'), '정답: ' + (pair[1] > pair[0] ? '더 높아요, 새 쪽으로.' : '더 낮아요, 거북이 쪽으로.'))
        : asked && test === 'sing' ? t('First the whole phrase, then note by note, waiting for each one to be sung, as the examiner does.', '먼저 선율 전체, 그다음 한 음씩, 부를 때까지 기다려 줘요. 시험관처럼.')
        : asked ? t('Two bars, once: now the echo!', '두 마디, 한 번: 이제 메아리!') : test === 'sing' ? t('Five or six notes, one beat each.', '한 박씩 다섯·여섯 음.') : test === 'updown' ? t('Two notes, at least a 3rd apart.', '두 음, 3도 이상 떨어져서.') : t('Tap a circle to change it.', '동그라미를 눌러 바꿔요.'), msg === 'close' ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="primary-btn" style={spBtn} disabled={!ready} onClick={ask}>{t('▶ Ask the question', '▶ 문제 내기')}</button>
        {test === 'sing' && tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setTune(tune.slice(0, -1)); setAsked(false); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
      </div>
      {asked && <div style={{display:'flex',gap:8,justifyContent:'center',marginTop:8}}>{[['pass', t('✓ Pass', '✓ 통과')], ['again', t('↻ Once more', '↻ 한 번 더')]].map(([k, lab]) => <button key={k} className="ghost-btn" style={spBtn} onClick={() => setStamp(k)}>{lab}</button>)}</div>}
      {stamp && <div style={{textAlign:'center',margin:'10px 0 2px'}}><span style={{display:'inline-block',transform:'rotate(-8deg)',border:'3px solid ' + (stamp === 'pass' ? BK.green : BK.coral),color:stamp === 'pass' ? BK.green : BK.coral,borderRadius:8,padding:'4px 16px',fontFamily:LB_SERIF,fontSize:26,fontWeight:900,letterSpacing:'0.08em'}}>{stamp === 'pass' ? t('PASSED!', '통과!') : t('ONCE MORE!', '한 번 더!')}</span></div>}
    </div>
  );
}

// ── Ear Training, Grade 1: Leave them hanging ──
const HG_GOALS = [['two', 'Stop on 2: left hanging', '2에서 멈추기: 매달린 채로'], ['five', 'Stop on 5: left hanging', '5에서 멈추기: 매달린 채로'], ['home', 'Come home on 1', '1에서 집에 오기']];
function HangTune() {
  const T = useSpTimers();
  const [pos, setPos] = useState('C'), [tune, setTune] = useState([1, 2, 3, 4, 5, 4, 3, 2]), [on, setOn] = useState(-1), [played, setPlayed] = useState(false);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_hang')) || {}; } catch (e) { return {}; } });
  const last = tune[tune.length - 1], kind = last === 1 ? 'home' : last === 2 ? 'two' : last === 5 ? 'five' : 'other';
  const play = (withHome) => { T.clear(); const ds = tune.map(f => hpFingerD(pos, 'R', f)), ev = ds.map((d, j) => ({ at: j * 0.6, keys: [hpSemi(d)], len: j === ds.length - 1 ? 1.1 : 0.5, vol: 0.14 }));
    if (withHome) ev.push({ at: ds.length * 0.6 + 1.2, keys: [hpSemi(hpFingerD(pos, 'R', 1))], len: 1.4, vol: 0.16 });
    const r = spPlay(ev, 60); if (!r) return; ev.forEach((e, j) => T.at(r.ms(e.at), () => setOn(j))); T.at(r.ms(ev[ev.length - 1].at + 1.4), () => setOn(-1)); setPlayed(true);
    if (kind !== 'other' && !stars[kind]) { const n = { ...stars, [kind]: 1 }; setStars(n); try { localStorage.setItem('pb_mk_hang', JSON.stringify(n)); } catch (e) {} } };
  const add = (f) => { if (tune.length >= 8) return; setTune(tune.concat([f])); playKey(hpSemi(hpFingerD(pos, 'R', f)), 0.4); setPlayed(false); };
  const home = 'CDEFGAB'[(hpFingerD(pos, 'R', 1) - 28 + 70) % 7];
  return (
    <div className="try-box" style={actBox} data-mk="hang">
      <div style={actTitle}>{t('Leave them hanging', '매달아 두기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>선율을 써요. <b>집(1)에 도착하기 전에</b> 멈추면, 듣는 사람의 귀가 집을 찾아요. 들려주고 집 음을 흥얼거리게 해 봐요! 별 세 개: 2에서 멈추기, 5에서 멈추기, 집에 오기.</> : <>Write a tune. Stop it <b>before it gets home (1)</b> and the listener's ear will go looking for home. Play it to someone: can they hum it? Three stars: stop on 2, stop on 5, come home.</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{HG_GOALS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips([['C', t('C position', 'C 자리')], ['G', t('G position', 'G 자리')]], pos, (p) => { T.clear(); setPos(p); setPlayed(false); })}
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',margin:'4px 0'}}>{tune.map((f, j) => <span key={j} style={{width:32,height:32,borderRadius:16,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:15,border:'2px solid ' + (j === on ? BK.coral : BK.ink),background:j === on ? BK.coral : '#fff',color:j === on ? '#fff' : BK.ink}}>{f}</span>)}</div>
      <HpKeys pos={pos} hands="R" fingers names lit={on >= 0 && on < tune.length ? { [hpFingerD(pos, 'R', tune[on])]: 'cor' } : on === tune.length ? { [hpFingerD(pos, 'R', 1)]: 'cor' } : {}} k={1.5}/>
      <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,marginTop:8}}>{[1, 2, 3, 4, 5].map(f => <button key={f} className="choice-btn" onClick={() => add(f)} style={{padding:'10px 0',fontSize:17,fontWeight:900}}>{f}</button>)}</div>
      {spMsg(!played ? t('Write it, then play it.', '쓰고, 쳐 봐요.') : kind === 'home' ? t('It came home on 1 (' + home + '): it sounds finished.', '1(' + home + ')에서 집에 왔어요: 끝난 소리.') : t('Left hanging on ' + last + '! Hum home: ' + home + '. Tap ▶ with home to check.', last + '에서 매달렸어요! 집 음을 흥얼거려요: ' + home + '. ▶ 집까지를 눌러 확인해요.'), played ? (kind === 'home' ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => play(false)}>{t('▶ Play it', '▶ 쳐 보기')}</button>
        {played && kind !== 'home' && <button className="ghost-btn" style={spBtn} onClick={() => play(true)}>{t('▶ With home', '▶ 집까지')}</button>}
        {tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setTune(tune.slice(0, -1)); setPlayed(false); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
        {tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setTune([]); setPlayed(false); }}>{t('Clear', '처음부터')}</button>}
      </div>
    </div>
  );
}

// ── Scales: Only the key's notes ──
const KT_KEYS = { C: { r: 0, nm: ['C', 'D', 'E', 'F', 'G', 'A', 'B'] }, G: { r: 7, nm: ['G', 'A', 'B', 'C', 'D', 'E', 'F♯'] }, F: { r: 5, nm: ['F', 'G', 'A', 'B♭', 'C', 'D', 'E'] } };
const KT_GOALS = [['ends', 'Start and end on 1', '1에서 시작해서 1에서 끝내기'], ['all', 'Use all seven notes', '일곱 음 모두 쓰기'], ['triad', 'Only 1, 3 and 5', '1, 3, 5만 쓰기']];
function KeyTune() {
  const T = useSpTimers();
  const [key, setKey] = useState('C'), [tune, setTune] = useState([]), [on, setOn] = useState(-1), [msg, setMsg] = useState(null);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_keytune')) || {}; } catch (e) { return {}; } });
  const K = KT_KEYS[key], lo = K.r, sc = [0, 2, 4, 5, 7, 9, 11, 12].map(x => lo + x), degOf = (k) => sc.indexOf(k) % 7 + 1;
  const check = (tn) => { const got = [], dg = tn.map(degOf); if (tn.length >= 3 && dg[0] === 1 && dg[dg.length - 1] === 1) got.push('ends'); if (new Set(dg).size === 7) got.push('all'); if (tn.length >= 4 && dg.every(d => d === 1 || d === 3 || d === 5)) got.push('triad');
    const fresh = got.filter(g => !stars[g]); if (fresh.length) { const n = { ...stars }; fresh.forEach(g => { n[g] = 1; }); setStars(n); setMsg(fresh[0]); try { localStorage.setItem('pb_mk_keytune', JSON.stringify(n)); } catch (e) {} } };
  const tap = (k) => { if (!sc.includes(k)) { playKey(k, 0.3); setMsg('out'); return; } if (tune.length >= 12) return; const n = tune.concat([k]); setTune(n); playKey(k, 0.5); setMsg(null); check(n); };
  const play = () => { T.clear(); const r = spPlay(tune.map((k, j) => ({ at: j * 0.5, keys: [k], len: 0.45, vol: 0.14 })), 60); if (!r) return; tune.forEach((_, j) => T.at(r.ms(j * 0.5), () => setOn(j))); T.at(r.ms(tune.length * 0.5), () => setOn(-1)); };
  const lit = {}, names = {}; sc.forEach((k, j) => { lit[k] = on >= 0 && tune[on] === k ? 'cor' : j === 0 || j === 7 ? 'good' : 'pale'; names[k] = String(j % 7 + 1); });
  return (
    <div className="try-box" style={actBox} data-mk="keytune">
      <div style={actTitle}>{t('Only the key\'s notes', '그 조의 음만')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>조를 고르면 <b>그 음계의 일곱 음</b>만 불이 켜져요. 그 음들로만 선율을 지어요: 어떤 걸 눌러도 어울려요! 별 세 개에 도전.</> : <>Pick a key and only <b>its scale's seven notes</b> light up. Make a tune from those alone: whatever you tap, it fits! Three stars to earn.</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{KT_GOALS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips(Object.keys(KT_KEYS).map(k => [k, t(k + ' major', k + '장조')]), key, (k) => { T.clear(); setKey(k); setTune([]); setMsg(null); })}
      <SpKb lo={lo} hi={lo + 12} W={30} H={86} lit={lit} names={names} onTap={tap} label={t('The scale of ' + key + ' major', key + '장조 음계')}/>
      <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'8px 0 2px',minHeight:30}}>{tune.map((k, j) => <span key={j} style={{minWidth:28,height:28,borderRadius:14,padding:'0 4px',boxSizing:'border-box',display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:13,border:'2px solid ' + (j === on ? BK.coral : BK.ink),background:j === on ? BK.coral : '#fff',color:j === on ? '#fff' : BK.ink}}>{K.nm[sc.indexOf(k) % 7]}</span>)}</div>
      {spMsg(msg === 'out' ? t('That key is not in ' + key + ' major: only the lit ones.', '그 건반은 ' + key + '장조에 없어요: 불 켜진 것만.') : msg ? t('★ ' + KT_GOALS.find(g => g[0] === msg)[1] + '!', '★ ' + KT_GOALS.find(g => g[0] === msg)[2] + '!') : tune.length ? t('Degrees: ' + tune.map(degOf).join(' '), '음계 번호: ' + tune.map(degOf).join(' ')) : t('Tap the lit keys.', '불 켜진 건반을 눌러요.'), msg === 'out' ? BK.coral : msg ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play it', '▶ 들어 보기')}</button>}
        {tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setTune(tune.slice(0, -1)); setMsg(null); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
        {tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setTune([]); setMsg(null); }}>{t('Clear', '처음부터')}</button>}
      </div>
    </div>
  );
}

// ── Playing scales: Scale remix (one scale, four rhythms: a classic way to practise) ──
const RX_RHY = [['even', 'Even', '고르게', [1, 1]], ['ls', 'Long, short', '길게, 짧게', [1.5, 0.5]], ['sl', 'Short, long', '짧게, 길게', [0.5, 1.5]], ['three', 'In threes', '셋씩', [2 / 3, 2 / 3, 2 / 3]]];
function ScaleRemix() {
  const T = useSpTimers();
  const [key, setKey] = useState('C'), [rx, setRx] = useState('ls'), [on, setOn] = useState(-1), [tried, setTried] = useState({});
  const K = KT_KEYS[key], up = [0, 2, 4, 5, 7, 9, 11, 12].map(x => K.r + x), sq = up.concat(up.slice(0, -1).reverse());
  const play = () => { T.clear(); const pat = RX_RHY.find(r => r[0] === rx)[3]; let at = 0; const ev = sq.map((k, j) => { const d = pat[j % pat.length], e = { at, keys: [k, k - 12], len: d * 0.9, vol: 0.12 }; at += d; return e; });
    const r = spPlay(ev, 80, 4); if (!r) return; ev.forEach((e, j) => T.at(r.ms(e.at), () => setOn(sq[j]))); T.at(r.ms(at + 0.5), () => setOn(-1)); setTried(x => ({ ...x, [rx]: 1 })); };
  const lit = {}; up.forEach(k => { lit[k] = k === on ? 'cor' : 'pale'; });
  const n = Object.keys(tried).length;
  return (
    <div className="try-box" style={actBox} data-mk="remix">
      <div style={actTitle}>{t('Scale remix', '스케일 리믹스')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>같은 여덟 음, 네 가지 리듬! 스케일을 여러 리듬으로 연습하는 건 <b>고르게 만드는 오래된 비법</b>이에요: 리듬마다 길게 치는 음이 달라져요. 고르면 앱이 쳐 줘요: 피아노로 같이 쳐요.</> : <>The same eight notes, four rhythms! Practising a scale in different rhythms is <b>an old trick for making it even</b>: each rhythm makes different notes the long ones. Pick one and the app plays it: play along on the piano.</>}</div>
      {spChips(Object.keys(KT_KEYS).filter(k => k !== 'F').map(k => [k, t(k + ' major', k + '장조')]), key, (k) => { T.clear(); setKey(k); })}
      {spChips(RX_RHY.map(([id, en, ko]) => [id, t(en, ko)]), rx, (r) => { T.clear(); setRx(r); })}
      <div style={{display:'flex',gap:3,justifyContent:'center',alignItems:'center',margin:'4px 0 8px',minHeight:24}}>{RX_RHY.find(r => r[0] === rx)[3].concat(RX_RHY.find(r => r[0] === rx)[3]).map((d, j) => <span key={j} style={{width:d * 26,height:14,borderRadius:7,background:BK.coral,opacity:0.85}}/>)}</div>
      <SpKb lo={K.r} hi={K.r + 12} W={30} H={80} lit={lit} names={Object.fromEntries(up.map((k, j) => [k, K.nm[j % 7]]))} label={t(key + ' major', key + '장조')}/>
      {spMsg(n >= 4 ? t('All four remixes! Now play it even again: does it feel smoother?', '리믹스 네 가지 모두! 이제 다시 고르게 쳐 봐요: 더 매끄럽나요?') : t('Remixes tried: ' + n + ' of 4.', '해 본 리믹스: 4개 중 ' + n + '개.'), n >= 4 ? BK.green : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',marginTop:8}}><button className="primary-btn" style={spBtn} onClick={play}>{t('▶ Play the remix', '▶ 리믹스 듣기')}</button></div>
    </div>
  );
}

// ── 6/8: My 6/8 rhythm (the quaver is one beat: two groups of three in a bar, beats 1 and 4 marked) ──
const E8_GR = [['ls', 'Long, short', '길게, 짧게', [0, 2]], ['run', 'Three quavers', '8분음표 셋', [0, 1, 2]], ['hold', 'One long', '하나 길게', [0]], ['sl', 'Short, long', '짧게, 길게', [0, 1]]];
function E8Maker() {
  const [g, setG] = useState(['ls', 'ls', 'run', 'hold']), [bpm, setBpm] = useState(132), [on, setOn] = useState(false), [cur, setCur] = useState(-1);
  const sched = useRef(null), next = useRef(0), step = useRef(0), tms = useRef([]), st = useRef({}); st.current = { g, bpm };
  const stop = () => { clearInterval(sched.current); sched.current = null; tms.current.forEach(clearTimeout); tms.current = []; setOn(false); setCur(-1); };
  useEffect(() => () => { clearInterval(sched.current); tms.current.forEach(clearTimeout); }, []);
  const start = () => { const ctx = getAudio(); if (!ctx) return; stop(); next.current = ctx.currentTime + 0.12; step.current = 0;
    const tick = () => { const S = st.current; while (next.current < ctx.currentTime + 0.3) { const i = step.current % 12, tt = next.current, gi = Math.floor(i / 3), at = E8_GR.find(x => x[0] === S.g[gi])[3];
        if (i % 3 === 0) metroClick(ctx, tt, i % 6 === 0, 0.06); if (at.includes(i % 3)) bodyHit(ctx, tt, 'clap', 0.5);
        tms.current.push(setTimeout(() => setCur(i), Math.max(0, (tt - ctx.currentTime) * 1000))); if (tms.current.length > 64) tms.current = tms.current.slice(-32);
        step.current++; next.current += 60 / S.bpm; } };
    tick(); sched.current = setInterval(tick, 60); setOn(true); };
  const flip = (k) => setG(x => x.map((y, j) => (j === k ? E8_GR[(E8_GR.findIndex(z => z[0] === y) + 1) % 4][0] : y)));
  const cell = (k) => { const G = E8_GR.find(x => x[0] === g[k]), lit = cur >= 0 && Math.floor(cur / 3) === k;
    return <button key={k} onClick={() => flip(k)} style={{flex:1,minWidth:0,padding:'6px 2px',borderRadius:12,border:'2px solid ' + (lit ? BK.coral : BK.ink),background:lit ? '#fbe3da' : '#fff',cursor:'pointer',fontFamily:'inherit'}}>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:2,height:16,alignItems:'center'}}>{[0, 1, 2].map(q => { const startN = G[3].includes(q), held = !startN && G[3].filter(x => x < q).length > 0;
        return <span key={q} style={{height:startN ? 12 : 4,borderRadius:6,background:startN ? BK.coral : held ? 'rgba(228,87,46,0.35)' : 'transparent',outline:cur === k * 3 + q ? '2px solid ' + BK.ink : 'none'}}/>; })}</div>
      <div style={{fontSize:11,fontWeight:900,color:BK.ink,marginTop:4}}>{t(G[1], G[2])}</div><div style={{fontSize:10,fontWeight:800,color:BK.muted}}>{k % 2 === 0 ? t('beats 1 2 3', '박 1 2 3') : t('beats 4 5 6', '박 4 5 6')}</div></button>; };
  return (
    <div className="try-box" style={actBox} data-mk="e8">
      <div style={actTitle}>{t('My 6/8 rhythm', '나의 6/8 리듬')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>6/8은 8분음표가 1박, 한 마디에 여섯 박, 셋씩 두 묶음. 묶음을 누를 때마다 바뀌어요: <b>길게, 짧게</b>, 8분음표 셋, 하나 길게, 짧게, 길게. 두 마디가 계속 돌아요. 1박과 4박에 클릭이 강하게.</> : <>In 6/8 the quaver is one beat: six in a bar, two groups of three. Tap a group to change it: <b>long, short</b>, three quavers, one long, short, long. Two bars go round and round; the click marks beats 1 and 4.</>}</div>
      {[0, 1].map(b => <div key={b} style={{display:'flex',gap:6,margin:'6px 0'}}>{cell(b * 2)}{cell(b * 2 + 1)}</div>)}
      {spChips([[100, t('Slow', '느리게')], [132, t('Moderate', '보통')], [168, t('Fast', '빠르게')]], bpm, setBpm)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {on ? <button className="ghost-btn" style={spBtn} onClick={stop}>{t('■ Stop', '■ 멈추기')}</button> : <button className="primary-btn" style={spBtn} onClick={start}>{t('▶ Play my rhythm', '▶ 나의 리듬 듣기')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={() => setG(['ls', 'ls', 'ls', 'hold'])}>{t('Try: long, short all the way', '해 보기: 계속 길게, 짧게')}</button>
      </div>
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")
rep("""  { id: 'mk-lines', ch: 'staff',""", """  { id: 'mk-exam', ch: 'listen-sing', title: 'Be the examiner', blurb: 'Set a Prelim test yourself; the app plays it the exam way; your teacher answers; you stamp it.', C: () => <ExaminerPad/> },   // Build CG
  { id: 'mk-hang', ch: 'listen-write', title: 'Leave them hanging', blurb: 'A tune that stops before it gets home: can your listener hum home?', C: () => <HangTune/> },
  { id: 'mk-keytune', ch: 'scales', title: 'Only the key\\'s notes', blurb: 'Only the scale\\'s seven notes light up: make a tune where every note fits.', C: () => <KeyTune/> },
  { id: 'mk-remix', ch: 'scale-play', title: 'Scale remix', blurb: 'One scale, four rhythms: even, long-short, short-long, in threes. Play along.', C: () => <ScaleRemix/> },
  { id: 'mk-e8', ch: 'six-eight', title: 'My 6/8 rhythm', blurb: 'Two bars of 6/8 from groups of three, round and round, beats 1 and 4 marked.', C: () => <E8Maker/> },
  { id: 'mk-lines', ch: 'staff',""")
rep("""  'mk-lines': ['나의 오선 선율',""", """  'mk-exam': ['시험관 되기', 'Prelim 시험 문제를 직접 내요. 앱이 시험처럼 들려주고, 선생님이 답하고, 내가 도장을 찍어요.'],
  'mk-hang': ['매달아 두기', '집에 도착하기 전에 멈추는 선율: 듣는 사람이 집 음을 흥얼거릴 수 있을까요?'],
  'mk-keytune': ['그 조의 음만', '그 음계의 일곱 음만 불이 켜져요: 모든 음이 어울리는 선율을 지어요.'],
  'mk-remix': ['스케일 리믹스', '스케일 하나, 리듬 넷: 고르게, 길게 짧게, 짧게 길게, 셋씩. 같이 쳐요.'],
  'mk-e8': ['나의 6/8 리듬', '셋씩 묶은 6/8 두 마디가 계속 돌아요. 1박과 4박에 표시.'],
  'mk-lines': ['나의 오선 선율',""")
rep("""'mk-lines': ['pitch', 0, 1, 'game ear'],""", """'mk-lines': ['pitch', 0, 1, 'game ear'], 'mk-exam': ['rpulse', 0, 1, 'game ear'], 'mk-hang': ['steps', 0, 1, 'game ear'], 'mk-keytune': ['scales', 0, 1, 'game ear'], 'mk-remix': ['scales', 0, 1, 'game ear'], 'mk-e8': ['rpulse', 1, 1, 'game ear'],""")
rep("""'mk-lines': 'p-staff',""", """'mk-lines': 'p-staff', 'mk-exam': 'aural', 'mk-hang': 'aural', 'mk-keytune': 'p-scales', 'mk-remix': 'k-play', 'mk-e8': 'r-beat',""")
rep("""  'mk-lines': () => (\n""", """  'mk-exam': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/><rect x="5" y="6" width="14" height="12" rx="2" fill="none" stroke="#fefbf3" strokeWidth="1.4" transform="rotate(-8 12 12)"/><text x="12" y="14.5" textAnchor="middle" fontFamily="Georgia, serif" fontSize="6" fontWeight="900" fill="#e9a83a" transform="rotate(-8 12 12)">PASS</text></svg>
  ),
  'mk-hang': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#7a4f96"/>{[[5, 15], [9, 12], [13, 10], [17, 8]].map(([x, y]) => <circle key={x} cx={x} cy={y} r="1.7" fill="#fefbf3"/>)}<circle cx="20" cy="17" r="2" fill="none" stroke="#e9a83a" strokeWidth="1.3" strokeDasharray="1.5 1.5"/></svg>
  ),
  'mk-keytune': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/>{[0, 1, 2, 3, 4, 5, 6].map(i => <rect key={i} x={3 + i * 2.6} y="7" width="2.2" height="10" rx="0.6" fill={i === 0 ? '#e9a83a' : '#fefbf3'}/>)}</svg>
  ),
  'mk-remix': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#e4572e"/><rect x="3" y="7" width="7" height="3" rx="1.5" fill="#fefbf3"/><rect x="11" y="7" width="2.5" height="3" rx="1.5" fill="#fefbf3"/><rect x="3" y="14" width="2.5" height="3" rx="1.5" fill="#e9a83a"/><rect x="6.5" y="14" width="7" height="3" rx="1.5" fill="#e9a83a"/><path d="M16 8 L20 12 L16 16" fill="none" stroke="#fefbf3" strokeWidth="1.5"/></svg>
  ),
  'mk-e8': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/><text x="12" y="15" textAnchor="middle" fontFamily="Georgia, serif" fontSize="9" fontWeight="900" fill="#fefbf3">6/8</text><circle cx="5" cy="19" r="1.4" fill="#e9a83a"/><circle cx="14" cy="19" r="1.4" fill="#e9a83a"/></svg>
  ),
  'mk-lines': () => (\n""")
rep("""lessons: ['ls-beat', 'ls-echo', 'ls-updown', 'ls-sing'], check: 'listen-sing' }""", """lessons: ['ls-beat', 'ls-echo', 'ls-updown', 'ls-sing', 'mk-exam'], check: 'listen-sing' }""")
rep("""lessons: ['lw-home', 'lw-clap', 'lw-phrase'], check: 'listen-write' }""", """lessons: ['lw-home', 'lw-clap', 'lw-phrase', 'mk-hang'], check: 'listen-write' }""")
rep("""lessons: ['e8-big', 'e8-dot', 'e8-ls', 'e8-34', 'e8-read'], check: 'six-eight' }""", """lessons: ['e8-big', 'e8-dot', 'e8-ls', 'e8-34', 'e8-read', 'mk-e8'], check: 'six-eight' }""")
rep("""  set('G', 'mk-lines'); set('P1', 'mk-ladders mk-road'); set('1', 'mk-recipe');   // Build CF (P1 becomes Prelim below)""", """  set('G', 'mk-lines'); set('P1', 'mk-ladders mk-road'); set('1', 'mk-recipe');   // Build CF (P1 becomes Prelim below)
  set('P1', 'mk-exam mk-keytune mk-remix'); set('1', 'mk-hang mk-e8');   // Build CG""")
rep("""lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-all', 'sc-chrom'], check: 'scales' }""", """lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-all', 'sc-chrom', 'mk-keytune'], check: 'scales' }""")
rep("""lessons: ['sp-turn', 'sp-beat', 'sp-minor', 'sp-mirror', 'sp-two'], check: 'scale-play' }""", """lessons: ['sp-turn', 'sp-beat', 'sp-minor', 'sp-mirror', 'sp-two', 'mk-remix'], check: 'scale-play' }""")
rep("""  'scales': ['scale-finder', 'major-fingering', 'build-minor', 'minor-fingering', 'modes'],""", """  'scales': ['scale-finder', 'major-fingering', 'build-minor', 'minor-fingering', 'modes', 'mk-keytune'],""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
