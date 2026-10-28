import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CI (call 25, batch 7; her 09:56: fun first): the Grade 4 rooms' things to make.
#   Ear Training, Grade 4: Interval bingo (make a card of the Grade 4 intervals from the keynote; each call is heard,
#     not read; mark it or say it is not on the card; a line wins; the fewest calls kept)
#   Scales and arpeggios, Grade 4: Catch the 4s (the scale runs four octaves; tap 4! each time finger 4 plays)
#   Keys and intervals, Grade 4: My tune in a new key (a tune in C, moved to B, F♯, D♭ or G♭ major; the key signature, the
#     letters; E♯ and C♭ found)
#   Chords and cadences, Grade 4: My tune, my chords (write six notes, then a chord that holds each one; start on I, end
#     V–I or IV–I)
#   Rhythm, Grade 4: Off the beat (two bars of 4/4: push a pair of beats off the beat; then 3/4 with or without a hemiola)

CODE = r'''
// ══ Build CI: batch 7, the Grade 4 rooms' things to make (call 25; her 09:56: fun first) ══
// ── Ear Training, Grade 4: Interval bingo. The intervals of the room (L4_IV: the major scale's from the keynote); each call
// is played (the keynote, then the note), never named until it is answered ──
const BG_LINES = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];
const bgDeal = () => { const v = shuffle([2, 3, 4, 5, 6, 7, 8]).concat([2 + kqRnd(7)]); return v.slice(0, 4).concat([0], v.slice(4)); };
const bgShort = (n) => t(['', '', 'major 2nd', 'major 3rd', 'perfect 4th', 'perfect 5th', 'major 6th', 'major 7th', 'octave'][n], ['', '', '장2도', '장3도', '완전4도', '완전5도', '장6도', '장7도', '옥타브'][n]);
function IntervalBingo() {
  const [card, setCard] = useState(bgDeal), [marks, setMarks] = useState([4]), [call, setCall] = useState(null), [res, setRes] = useState(null), [calls, setCalls] = useState(0), [win, setWin] = useState(null), [shake, setShake] = useState(-1);
  const [best, setBest] = useState(() => { try { return Number(localStorage.getItem('pb_mk_bingo')) || 0; } catch (e) { return 0; } });
  const play = (c) => { stopClicks(); spPlay([{ at: 0, keys: [c.k], len: 1.3 }, { at: 1.5, keys: [c.k + L4_IV.find(y => y[0] === c.n)[1]], len: 1.8 }], 84); };
  const next = () => { let c, g = 0; do { c = { n: pick(L4_IV)[0], k: pick(L4_KEYS) }; } while (call && c.n === call.n && g++ < 6); setCall(c); setRes(null); setCalls(calls + 1); play(c); };
  const fresh = () => { stopClicks(); setCard(bgDeal()); setMarks([4]); setCall(null); setRes(null); setCalls(0); setWin(null); };
  const done = (mk) => { const line = BG_LINES.find(L => L.every(j => mk.includes(j))); if (!line) return; setWin(line);
    if (!best || calls < best) { setBest(calls); try { localStorage.setItem('pb_mk_bingo', String(calls)); } catch (e) {} } };
  const tap = (j) => { if (j === 4 || win) return;
    if (!calls) { const n = card.slice(); n[j] = n[j] >= 8 ? 2 : n[j] + 1; setCard(n); return; }
    if (!call || res) return;
    if (card[j] === call.n) { const mk = marks.includes(j) ? marks : marks.concat([j]); setMarks(mk); setRes({ ok: true }); done(mk); }
    else { setRes({ ok: false }); setShake(j); setTimeout(() => setShake(-1), 500); } };
  const notOn = () => { if (!call || res) return; setRes({ ok: !card.includes(call.n), off: true }); };
  const cell = (j) => { const free = j === 4, on = marks.includes(j), inWin = win && win.includes(j);
    return <button key={j} onClick={() => tap(j)} style={{aspectRatio:'1 / 1',minWidth:0,borderRadius:12,border:'2px solid ' + (inWin ? BK.coral : BK.ink),background:inWin ? BK.coral : on ? '#fbe3da' : '#fff',color:inWin ? '#fff' : BK.ink,cursor:'pointer',fontFamily:'inherit',
      display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',gap:2,padding:4,transform:shake === j ? 'rotate(-4deg)' : 'none',transition:'transform 0.15s'}}>
      {free ? <><span style={{fontSize:22,color:inWin ? '#fff' : BK.coral}}>★</span><span style={{fontSize:11,fontWeight:900}}>{t('FREE', '보너스')}</span></>
        : <><span style={{fontFamily:LB_SERIF,fontSize:24,fontWeight:900,lineHeight:1,fontVariantNumeric:'lining-nums'}}>{card[j] === 8 ? '8' : card[j]}</span><span style={{fontSize:10.5,fontWeight:800,lineHeight:1.15,textAlign:'center'}}>{bgShort(card[j])}</span>{on && !inWin && <span style={{fontSize:13,fontWeight:900,color:BK.coral}}>✓</span>}</>}</button>; };
  return (
    <div className="try-box" style={actBox} data-mk="bingo">
      <div style={actTitle}>{t('Interval bingo', '음정 빙고')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>먼저 내 카드를 만들어요: 칸을 누르면 음정이 바뀌어요. 그다음 <b>부르기</b>! 앱이 으뜸음과 한 음을 들려주면, 그 음정을 카드에서 찾아 표시해요. 카드에 없으면 <b>내 카드에 없어요</b>. 한 줄이면 빙고!</> : <>First make your card: tap a square to change its interval. Then <b>call</b>! The app plays the keynote and one note; find that interval on your card and mark it. Not there? Say <b>not on my card</b>. A line wins: BINGO!</>}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,maxWidth:300,margin:'6px auto'}}>{[0, 1, 2, 3, 4, 5, 6, 7, 8].map(cell)}</div>
      {win ? <div style={{textAlign:'center',margin:'6px 0'}}><span style={{display:'inline-block',transform:'rotate(-6deg)',border:'3px solid ' + BK.coral,color:BK.coral,borderRadius:8,padding:'4px 16px',fontFamily:LB_SERIF,fontSize:26,fontWeight:900,letterSpacing:'0.06em'}}>{t('BINGO!', '빙고!')}</span>
        <div style={{fontSize:13,fontWeight:800,color:BK.muted,marginTop:6}}>{t('In ' + calls + ' calls.', calls + '번 만에.')}{best ? t(' Best: ' + best + '.', ' 최고: ' + best + '번.') : ''}</div></div>
      : spMsg(!calls ? t('Tap the squares to make your card, then start.', '칸을 눌러 카드를 만들고, 시작해요.')
        : res ? (res.ok ? (res.off ? t('Right: not on your card. It was a ' + bgShort(call.n) + '.', '맞아요: 내 카드에 없어요. ' + bgShort(call.n) + '였어요.') : t('Yes: a ' + bgShort(call.n) + '!', '맞아요: ' + bgShort(call.n) + '!')) : t('It was a ' + bgShort(call.n) + '.', bgShort(call.n) + '였어요.'))
        : t('Call ' + calls + ': which interval from the keynote?', calls + '번째 부르기: 으뜸음에서 몇 도일까요?'), res ? (res.ok ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>
        {!win && (!calls || res) && <button className="primary-btn" style={spBtn} onClick={next}>{!calls ? t('▶ Start: first call', '▶ 시작: 첫 부르기') : t('▶ Next call', '▶ 다음 부르기')}</button>}
        {calls > 0 && !res && !win && <><button className="ghost-btn" style={spBtn} onClick={() => play(call)}>{t('♪ Again', '♪ 다시')}</button><button className="ghost-btn" style={spBtn} onClick={notOn}>{t('Not on my card', '내 카드에 없어요')}</button></>}
        <button className="ghost-btn" style={spBtn} onClick={fresh}>{t('↻ A new card', '↻ 새 카드')}</button>
      </div>
    </div>
  );
}

// ── Scales and arpeggios, Grade 4: Catch the 4s. Four octaves going up (S4_SC, the book's fingers); tap 4! as finger 4 plays ──
function CatchFours() {
  const T = useSpTimers();
  const [k, setK] = useState('E'), [h, setH] = useState('R'), [speed, setSpeed] = useState(0.6), [cur, setCur] = useState(-1), [run, setRun] = useState(null), [flash, setFlash] = useState(false);
  const [got, setGot] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_four4')) || {}; } catch (e) { return {}; } });
  const c = S4_SC[k], fing = c[h], notes = s4Seq(k, c.r - 12, 4).slice(0, 29), fours = fing.map((f, j) => (f === 4 ? j : -1)).filter(j => j >= 0);
  const taps = useRef([]), times = useRef([]), st = useRef({}); st.current = { k, h, fours, speed, got };
  const score = () => { const S = st.current, w = S.speed * 1000 * 0.55, used = new Set(), hit = [];
    S.fours.forEach(j => { const x = taps.current.findIndex((tp, i) => !used.has(i) && Math.abs(tp - times.current[j]) <= w); if (x >= 0) { used.add(x); hit.push(j); } });
    const wrong = taps.current.length - used.size, r = { hit, wrong, all: hit.length === S.fours.length && wrong === 0 }; setRun(r);
    if (r.all && !S.got[S.k + S.h]) { const n = { ...S.got, [S.k + S.h]: 1 }; setGot(n); try { localStorage.setItem('pb_mk_four4', JSON.stringify(n)); } catch (e) {} } };
  const go = () => { T.clear(); taps.current = []; setRun({ live: true }); setCur(-1);
    const r = spPlay(notes.map((x, j) => ({ at: j * speed, keys: [x], len: speed * 0.9, vol: 0.12 })), 60); if (!r) { setRun(null); return; } const t0 = performance.now();
    times.current = notes.map((_, j) => t0 + r.ms(j * speed)); notes.forEach((_, j) => T.at(r.ms(j * speed), () => setCur(j))); T.at(r.ms(notes.length * speed + 0.3), () => { setCur(-1); score(); }); };
  const four = () => { if (!run || !run.live) return; taps.current.push(performance.now()); setFlash(true); setTimeout(() => setFlash(false), 120); };
  const pick2 = (fn) => { T.clear(); setCur(-1); setRun(null); fn(); };
  const done = run && !run.live;
  return (
    <div className="try-box" style={actBox} data-mk="four4">
      <div style={actTitle}>{t('Catch the 4s', '4번을 잡아라')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>스케일이 네 옥타브를 올라가요. <b>4번 손가락이 치는 순간</b>마다 <b>4!</b>를 눌러요. 4번은 옥타브마다 같은 음이에요. 조와 손을 다 모아 봐요!</> : <>The scale runs up four octaves. Tap <b>4!</b> every time <b>finger 4 plays</b>. Finger 4 plays the same note in every octave. Collect every key and both hands!</>}</div>
      {spChips(S4_KEYS.map(x => [x, (got[x + 'R'] && got[x + 'L'] ? '★ ' : '') + s4Chip(x)]), k, (x) => pick2(() => setK(x)))}
      {spChips([['R', t('Right hand', '오른손') + (got[k + 'R'] ? ' ★' : '')], ['L', t('Left hand', '왼손') + (got[k + 'L'] ? ' ★' : '')]], h, (x) => pick2(() => setH(x)))}
      <div style={{display:'flex',flexDirection:'column',gap:3,margin:'6px 0'}}>{[0, 1, 2, 3].map(o => <div key={o} style={{display:'grid',gridTemplateColumns:'repeat(8,minmax(0,1fr))',gap:3}}>{[0, 1, 2, 3, 4, 5, 6, 7].map(x => { const j = o * 7 + x; if (x === 7 && o < 3) return <span key={x}/>;
        const is4 = fing[j] === 4, hit = done && run.hit.includes(j), miss = done && is4 && !hit, now = j === cur;
        return <div key={x} style={{borderRadius:8,border:'1.5px solid ' + (hit ? BK.green : miss ? BK.coral : now ? BK.coral : BK.line),background:now ? BK.coral : hit ? '#e2efe9' : '#fff',color:now ? '#fff' : BK.ink,textAlign:'center',padding:'3px 0',minWidth:0}}>
          <div style={{fontSize:12.5,fontWeight:900}}>{c.nm[j % 7]}</div><div style={{fontSize:10.5,fontWeight:900,color:now ? '#fff' : is4 && done ? (hit ? BK.green : BK.coral) : BK.muted,minHeight:13}}>{done ? fing[j] : ''}</div></div>; })}</div>)}</div>
      {run && run.live ? <button onPointerDown={four} style={{display:'block',width:'100%',maxWidth:360,margin:'6px auto',minHeight:72,borderRadius:16,border:'3px solid ' + BK.coral,background:flash ? BK.coral : '#fbe3da',color:flash ? '#fff' : BK.coral,fontFamily:LB_SERIF,fontSize:34,fontWeight:900,cursor:'pointer',touchAction:'manipulation'}}>4!</button>
        : spMsg(done ? (run.all ? t('All four caught, no wrong taps! ' + c.nm[s4F4(k, h)] + ' every time.', '네 번 모두 잡았어요, 헛손질 없이! 매번 ' + c.nm[s4F4(k, h)] + '.') : t('Caught ' + run.hit.length + ' of ' + fours.length + (run.wrong ? ', ' + run.wrong + ' wrong tap' + (run.wrong > 1 ? 's' : '') : '') + '. The fingers are under the notes now.', fours.length + '번 중 ' + run.hit.length + '번 잡았어요' + (run.wrong ? ', 헛손질 ' + run.wrong + '번' : '') + '. 이제 음 아래에 손가락 번호가 보여요.'))
          : t('Think: which note does finger 4 play? Then start.', '생각해 봐요: 4번은 어느 음을 칠까요? 그다음 시작.'), done ? (run.all ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>
        {!(run && run.live) && <button className="primary-btn" style={spBtn} onClick={go}>{done ? t('▶ Again', '▶ 다시') : t('▶ Start', '▶ 시작')}</button>}
      </div>
      {spChips([[0.6, t('Steady', '보통')], [0.42, t('Faster', '빠르게')], [60 / (S4_BPM * 4), t('Grade 4 speed: ♩ = ' + S4_BPM + ', four a beat', '4급 빠르기: ♩ = ' + S4_BPM + ', 한 박에 넷')]], speed, (x) => pick2(() => setSpeed(x)))}
    </div>
  );
}

// ── Keys and intervals, Grade 4: My tune in a new key. Every letter once in a scale, so F♯ major's 7th is E♯ and G♭ major's
// 4th is C♭ (the room's step 2: the right key, the right letter) ──
const AK_KEYS = ['B', 'Fs', 'Db', 'Gb'];
const akOdd = (nt) => { const L = H3_L[((nt.d % 7) + 7) % 7]; return (nt.acc === 1 && (L === 'E' || L === 'B')) || (nt.acc === -1 && (L === 'C' || L === 'F')); };
const AK_STARS = [['Fs', 'Six sharps: F♯ major', '샵 여섯: F♯장조'], ['Gb', 'Six flats: G♭ major', '플랫 여섯: G♭장조'], ['es', 'Find an E♯', 'E♯ 찾기'], ['cb', 'Find a C♭', 'C♭ 찾기']];
function AnyKeyTune() {
  const T = useSpTimers();
  const [tune, setTune] = useState([1, 3, 5, 4, 3, 2, 7, 8]), [k, setK] = useState('Fs'), [on, setOn] = useState(null);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_anykey')) || {}; } catch (e) { return {}; } });
  const src = tune.map(x => ({ d: 27 + x, acc: 0 })), dst = tune.map(x => k4Note(k, 'treble', x - 1));
  const play = (w) => { T.clear(); const ns = w === 'src' ? src : dst; if (!ns.length) return; const r = spPlay(ns.map((nt, j) => ({ at: j * 0.5, keys: [h3Semi(nt)], len: j === ns.length - 1 ? 1.2 : 0.45, vol: 0.14 })), 66); if (!r) return;
    ns.forEach((_, j) => T.at(r.ms(j * 0.5), () => setOn([w, j]))); T.at(r.ms(ns.length * 0.5 + 0.8), () => setOn(null));
    if (w === 'dst') { const n = { ...stars }; if (k === 'Fs') n.Fs = 1; if (k === 'Gb') n.Gb = 1; dst.forEach(nt => { if (akOdd(nt)) { const L = H3_L[((nt.d % 7) + 7) % 7]; if (L === 'E') n.es = 1; if (L === 'C') n.cb = 1; } });
      if (Object.keys(n).length !== Object.keys(stars).length) { setStars(n); try { localStorage.setItem('pb_mk_anykey', JSON.stringify(n)); } catch (e) {} } } };
  const odd = dst.find(akOdd), oddL = odd ? h3Let(odd) : null;
  const row = (ns, w) => <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'2px 0 4px'}}>{ns.map((nt, j) => { const lit = on && on[0] === w && on[1] === j, o = w === 'dst' && akOdd(nt);
    return <span key={j} style={{minWidth:30,height:28,padding:'0 4px',boxSizing:'border-box',borderRadius:14,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:13,border:'2px solid ' + (o ? BK.coral : BK.ink),background:lit ? (o ? BK.coral : BK.ink) : o ? '#fbe3da' : '#fff',color:lit ? '#fff' : o ? BK.coral : BK.ink}}>{h3Let(nt)}</span>; })}</div>;
  return (
    <div className="try-box" style={actBox} data-mk="anykey">
      <div style={actTitle}>{t('My tune in a new key', '새 조로 옮긴 내 선율')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>C장조로 선율을 쓰고, 4급의 조로 옮겨요: 같은 선율, 새 조표, 새 글자. 음계에는 <b>글자마다 한 번씩</b>이라서, 이상한 음이 숨어 있어요. 찾아봐요!</> : <>Write a tune in C major, then move it into a Grade 4 key: the same tune, a new key signature, new letters. A scale uses <b>every letter once</b>, so some strange notes hide in there. Find them!</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{AK_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      <div style={{fontSize:12,fontWeight:900,color:BK.muted,textAlign:'center'}}>{t('In C major', 'C장조로')}</div>
      <div style={{maxWidth:330,margin:'0 auto'}}><K4Melody notes={src.length ? src : [{ d: 28, acc: 0 }]} width={320} hi={on && on[0] === 'src' ? [on[1]] : []}/></div>
      {row(src, 'src')}
      {spChips(AK_KEYS.map(x => [x, k4Name(x)]), k, (x) => { T.clear(); setOn(null); setK(x); })}
      <div style={{maxWidth:330,margin:'0 auto'}}><K4Melody notes={dst.length ? dst : [k4Note(k, 'treble', 0)]} ks={K4[k].ks} width={320} hi={on && on[0] === 'dst' ? [on[1]] : []}/></div>
      {row(dst, 'dst')}
      <div style={{display:'grid',gridTemplateColumns:'repeat(8,minmax(0,1fr))',gap:4,maxWidth:420,margin:'6px auto 0'}}>{[1, 2, 3, 4, 5, 6, 7, 8].map(g => <button key={g} className="choice-btn" disabled={tune.length >= 8} onClick={() => { T.clear(); setOn(null); setTune(tune.concat([g])); }} style={{padding:'8px 0',fontSize:16,fontWeight:900,minWidth:0}}>{g}</button>)}</div>
      {spMsg(odd ? (H3_L[((odd.d % 7) + 7) % 7] === 'E' || H3_L[((odd.d % 7) + 7) % 7] === 'B' ? t(oddL + ' is played on a white key, but this scale needs that letter, so it is ' + oddL + ', not ' + (oddL[0] === 'E' ? 'F' : 'C') + '.', oddL + ': 흰건반에서 치지만, 이 음계에는 이 글자가 필요해요. 그래서 ' + (oddL[0] === 'E' ? 'F' : 'C') + '가 아니라 ' + oddL + '.')
          : t(oddL + ' is played on a white key, but this scale needs that letter, so it is ' + oddL + ', not ' + (oddL[0] === 'C' ? 'B' : 'E') + '.', oddL + ': 흰건반에서 치지만, 이 음계에는 이 글자가 필요해요. 그래서 ' + (oddL[0] === 'C' ? 'B' : 'E') + '가 아니라 ' + oddL + '.'))
        : t('Tap the scale numbers to write the tune (up to eight notes). 8 is the keynote at the top.', '음계 번호를 눌러 선율을 써요 (여덟 음까지). 8은 꼭대기의 으뜸음.'), odd ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} disabled={!tune.length} onClick={() => play('src')}>{t('▶ In C', '▶ C장조로')}</button>
        <button className="primary-btn" style={spBtn} disabled={!tune.length} onClick={() => play('dst')}>{t('▶ In ' + K4[k].en, '▶ ' + K4[k].ko + '로')}</button>
        {tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setOn(null); setTune(tune.slice(0, -1)); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
      </div>
    </div>
  );
}

// ── Chords and cadences, Grade 4: My tune, my chords. As the room's step 4 (H4HarmPad), with the child's own six notes ──
const TC_KEYS = ['C', 'G', 'F'];
const TC_STARS = [['perfect', 'End V–I: perfect', 'V–I로 끝: 정격'], ['plagal', 'End IV–I: plagal', 'IV–I로 끝: 변격'], ['five', 'All five chords', '다섯 화음 모두']];
function TuneChords() {
  const T = useSpTimers();
  const [k, setK] = useState('C'), [mel, setMel] = useState([5, 6, 4, 3, 2, 1]), [ch, setCh] = useState([null, null, null, null, null, null]), [at, setAt] = useState(0), [on, setOn] = useState(-1);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_tunechords')) || {}; } catch (e) { return {}; } });
  const td = h4Td(k, 4), ns = mel.map(x => h4Note(k, td, x - 1)), degs = H4_DEGS(k), n = ns.length;
  const fit = ns.map((nt, j) => ch[j] != null && h4Has(k, ch[j], nt)), full = ch.every(x => x != null), last = ch[n - 1], pen = ch[n - 2];
  const cad = last === 1 && (pen === 5 || pen === 4), ok = full && fit.every(Boolean) && ch[0] === 1 && cad;
  const setNote = (g) => { T.clear(); setOn(-1); const m = mel.slice(); m[at] = g; setMel(m); playKey(h3Semi(h4Note(k, td, g - 1)), 0.45); };
  const setChord = (d) => { T.clear(); setOn(-1); const c = ch.slice(); c[at] = d; setCh(c); const root = h4Note(k, h4Td(k, 2), d - 1), mid = [2, 4].map(x => h4Note(k, h4Td(k, 3), d - 1 + x));
    spPlay([{ at: 0, keys: [h3Semi(ns[at]), h3Semi(root), ...mid.map(h3Semi)], len: 1, vol: 0.1 }], 72); if (at < n - 1) setAt(at + 1); };
  const play = () => { T.clear(); const ev = ns.map((nt, j) => { const d = ch[j]; if (d == null) return { at: j * 1.2, keys: [h3Semi(nt)], len: 1.1, vol: 0.13 };
      const root = h4Note(k, h4Td(k, 2), d - 1), mid = [2, 4].map(x => h4Note(k, h4Td(k, 3), d - 1 + x)); return { at: j * 1.2, keys: [h3Semi(nt), h3Semi(root), ...mid.map(h3Semi)], len: 1.1, vol: 0.1 }; });
    const r = spPlay(ev, 72); if (!r) return; ev.forEach((e, j) => T.at(r.ms(e.at), () => setOn(j))); T.at(r.ms(n * 1.2 + 0.4), () => setOn(-1));
    if (ok) { const s2 = { ...stars, [pen === 5 ? 'perfect' : 'plagal']: 1 }; if (degs.every(d => ch.includes(d))) s2.five = 1; setStars(s2); try { localStorage.setItem('pb_mk_tunechords', JSON.stringify(s2)); } catch (e) {} } };
  const bad = fit.findIndex((f, j) => ch[j] != null && !f);
  return (
    <div className="try-box" style={actBox} data-mk="tunechords">
      <div style={actTitle}>{t('My tune, my chords', '내 선율, 내 화음')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>여섯 음의 선율을 직접 쓰고, 음마다 그 음이 <b>들어 있는 화음</b>을 골라요. <b>I로 시작</b>, 끝은 V–I나 IV–I. 초록 점이 있는 화음에 그 음이 들어 있어요.</> : <>Write your own six-note tune, then give each note a chord that <b>holds it</b>. <b>Start on I</b>; end V–I or IV–I. A green dot marks the chords that hold the note.</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{TC_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips(TC_KEYS.map(x => [x, h4Name(x)]), k, (x) => { T.clear(); setOn(-1); setK(x); })}
      <div style={{maxWidth:340,margin:'0 auto'}}><K4Melody notes={ns} ks={H4_KEYS[k][2]} hi={on >= 0 ? [on] : [at]} labels={ch.map(d => (d != null ? h4Rom(k, d, 0) : '·'))} width={320}/></div>
      <div style={{display:'flex',gap:4,justifyContent:'center',margin:'4px 0'}}>{ns.map((nt, j) => <button key={j} onClick={() => setAt(j)} className={'chip' + (j === at ? ' active' : '')} style={{minHeight:36,minWidth:40,padding:'2px 6px',color:ch[j] != null && !fit[j] ? BK.coral : undefined}}>{h3Let(nt)}</button>)}</div>
      <div style={{fontSize:11.5,fontWeight:900,color:BK.muted,textAlign:'center',marginTop:4}}>{t('Note', '음')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(8,minmax(0,1fr))',gap:4,maxWidth:420,margin:'2px auto 0'}}>{[1, 2, 3, 4, 5, 6, 7, 8].map(g => <button key={g} className="choice-btn" onClick={() => setNote(g)} style={{padding:'6px 0',fontSize:15,fontWeight:900,minWidth:0}}>{g}</button>)}</div>
      <div style={{fontSize:11.5,fontWeight:900,color:BK.muted,textAlign:'center',marginTop:6}}>{t('Chord', '화음')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(' + degs.length + ',minmax(0,1fr))',gap:6,maxWidth:420,margin:'2px auto 0'}}>{degs.map(d => <button key={d} className="choice-btn" onClick={() => setChord(d)} style={{padding:'8px 2px',fontSize:17,fontWeight:900,fontFamily:LB_SERIF,position:'relative',minWidth:0}}>{h4Rom(k, d, 0)}{h4Has(k, d, ns[at]) && <span style={{position:'absolute',top:4,right:6,width:7,height:7,borderRadius:4,background:BK.green}}/>}</button>)}</div>
      {spMsg(bad >= 0 ? t('Note ' + (bad + 1) + ' (' + h3Let(ns[bad]) + ') is not in ' + h4Rom(k, ch[bad], 0) + '.', (bad + 1) + '번째 음(' + h3Let(ns[bad]) + ')은 ' + h4Rom(k, ch[bad], 0) + '에 없어요.')
        : !full ? t('Note ' + (at + 1) + ': ' + h3Let(ns[at]) + '. Pick its note and its chord.', (at + 1) + '번째 음: ' + h3Let(ns[at]) + '. 음과 화음을 골라요.')
        : ch[0] !== 1 ? t('Start on the tonic chord, I.', '으뜸화음 I로 시작해요.') : !cad ? t('End with V–I or IV–I.', 'V–I나 IV–I로 끝내요.')
        : t('It works: it ends ' + (pen === 5 ? 'V–\u2060I, a perfect cadence.' : 'IV–\u2060I, a plagal cadence.'), '좋아요: ' + (pen === 5 ? 'V–\u2060I, 정격종지로' : 'IV–\u2060I, 변격종지로') + ' 끝나요.'), bad >= 0 ? BK.coral : ok ? BK.green : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="primary-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setOn(-1); setCh([null, null, null, null, null, null]); setAt(0); }}>{t('↻ New chords', '↻ 화음 새로')}</button>
      </div>
    </div>
  );
}

// ── Rhythm, Grade 4: Off the beat. Syncopation as the room has it (quaver, crotchet, quaver: off the beat, held over the
// beat; R2.syncA), and the hemiola (two bars of 3/4 as three minims, the middle one tied; R2.hemA) ──
const OB_STARS = [['push', 'Push a pair of beats', '박 한 쌍 당기기'], ['all4', 'Push all four', '네 쌍 모두 당기기'], ['hem', 'Make a hemiola', '헤미올라 만들기']];
function OffBeat() {
  const [mode, setMode] = useState('sync'), [push, setPush] = useState([false, false, false, false]), [hem, setHem] = useState(false);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_offbeat')) || {}; } catch (e) { return {}; } });
  const give = (ks) => { const n = { ...stars }; ks.forEach(x => { n[x] = 1; }); if (Object.keys(n).length !== Object.keys(stars).length) { setStars(n); try { localStorage.setItem('pb_mk_offbeat', JSON.stringify(n)); } catch (e) {} } };
  const g = (p) => (p ? [['e'], ['q'], ['e']] : [['q'], ['q']]);
  const sync = [['ts', 4]].concat(g(push[0]), g(push[1]), [['|']], g(push[2]), g(push[3]), [['||']]);
  const hemI = [['ts', 3], ['q'], ['q'], ['q'], ['|'], ['h'], ['q'], ['|'], ['h'], ['q'], ['|']].concat(hem ? [['q'], ['h']] : [['h'], ['q']], [['|'], ['hd'], ['||']]);
  const flip = (j) => { const p = push.slice(); p[j] = !p[j]; setPush(p); const ks = []; if (p.some(Boolean)) ks.push('push'); if (p.every(Boolean)) ks.push('all4'); give(ks); };
  const box = (lab, lit, key) => <span key={key} style={{flex:1,minWidth:0,textAlign:'center',fontWeight:900,fontSize:13,padding:'4px 0',borderRadius:8,background:lit ? BK.coral : '#fff',color:lit ? '#fff' : BK.ink,border:'1.5px solid ' + BK.ink}}>{lab}</span>;
  return (
    <div className="try-box" style={actBox} data-mk="offbeat">
      <div style={actTitle}>{t('Off the beat', '박에서 비켜서')}</div>
      <div style={actNote}>{LANG === 'ko' ? <><b>당김음</b>: 박 한 쌍을 당겨요. 4분음표 둘이 8분음표, 4분음표, 8분음표가 되어 박과 박 사이에서 소리가 나요. <b>헤미올라</b>: 3/4 두 마디가 셋씩 둘에서 둘씩 셋으로. 듣고 쳐 봐요!</> : <><b>Syncopation</b>: push a pair of beats. Two crotchets become quaver, crotchet, quaver: the sound lands between the beats and holds over one. <b>Hemiola</b>: two bars of 3/4 change from two threes into three twos. Listen, then tap it!</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{OB_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips([['sync', t('Syncopation', '당김음')], ['hem', t('Hemiola', '헤미올라')]], mode, setMode)}
      {mode === 'sync' ? <>
        <RqStaff key={'s' + push.join()} items={sync} accent={true}/>
        <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6}}>{push.map((p, j) => <button key={j} className="choice-btn" onClick={() => flip(j)} style={{padding:'6px 2px',display:'flex',flexDirection:'column',alignItems:'center',gap:2,minWidth:0,border:p ? '2px solid ' + BK.coral : undefined}}>
          <span style={{fontSize:10.5,fontWeight:800,color:BK.muted}}>{t('bar ' + (j < 2 ? 1 : 2) + ', beats ' + (j % 2 ? '3–4' : '1–2'), (j < 2 ? 1 : 2) + '마디 ' + (j % 2 ? '3–4' : '1–2') + '박')}</span><span style={{fontSize:13.5,fontWeight:900,color:p ? BK.coral : BK.ink}}>{p ? t('pushed', '당김') : t('straight', '그대로')}</span></button>)}</div>
      </> : <>
        <RqStaff key={'h' + hem} items={hemI} ties={hem ? [[9, 11]] : undefined} accent={true} so={hem ? { ties: [[9, 11]] } : {}}/>
        <div style={{fontSize:11.5,fontWeight:900,color:BK.muted,textAlign:'center'}}>{t('Bars 3 and 4: six beats', '3마디와 4마디: 여섯 박')}</div>
        <div style={{display:'flex',gap:6,maxWidth:340,margin:'4px auto'}}>{(hem ? [[0, 1], [2, 3], [4, 5]] : [[0, 1, 2], [3, 4, 5]]).map((grp, gi) => <div key={gi} style={{flex:grp.length,display:'flex',gap:3,padding:3,borderRadius:10,border:'2px solid ' + BK.coral}}>{grp.map(b => box(String(b % 3 + 1), b === grp[0], b))}</div>)}</div>
        <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:18,fontWeight:900,color:BK.coral,fontVariantNumeric:'lining-nums'}}>{hem ? '2 + 2 + 2' : '3 + 3'}</div>
        <div style={{textAlign:'center',marginTop:6}}><button className="primary-btn" style={spBtn} onClick={() => { const h2 = !hem; setHem(h2); if (h2) give(['hem']); }}>{hem ? t('Back to two threes', '셋씩 둘로 돌아가기') : t('Make it a hemiola', '헤미올라로 바꾸기')}</button></div>
      </>}
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")
rep("""  { id: 'mk-pianist', ch: 'posture-hands',""", """  { id: 'mk-bingo', ch: 'listen-4', title: 'Interval bingo', blurb: 'Make a card of the Grade 4 intervals; every call is heard, not read. A line wins.', C: () => <IntervalBingo/> },   // Build CI
  { id: 'mk-four4', ch: 'scales-4', title: 'Catch the 4s', blurb: 'The scale runs up four octaves: tap 4! each time finger 4 plays. Collect every key.', C: () => <CatchFours/> },
  { id: 'mk-anykey', ch: 'keys-4', title: 'My tune in a new key', blurb: 'A tune in C moved into B, F♯, D♭ or G♭ major: new key signature, new letters, strange notes.', C: () => <AnyKeyTune/> },
  { id: 'mk-tunechords', ch: 'harmony-4', title: 'My tune, my chords', blurb: 'Write six notes, then a chord that holds each one. Start on I, end V–I or IV–I.', C: () => <TuneChords/> },
  { id: 'mk-offbeat', ch: 'rhythm-4', title: 'Off the beat', blurb: 'Push pairs of beats into syncopation, or turn two bars of 3/4 into a hemiola.', C: () => <OffBeat/> },
  { id: 'mk-pianist', ch: 'posture-hands',""")
rep("""  'mk-pianist': ['피아니스트 고치기',""", """  'mk-bingo': ['음정 빙고', '4급 음정으로 카드를 만들어요. 부르는 음정은 글자가 아니라 소리로. 한 줄이면 빙고.'],
  'mk-four4': ['4번을 잡아라', '스케일이 네 옥타브를 올라가요: 4번이 칠 때마다 4!를 눌러요. 모든 조를 모아요.'],
  'mk-anykey': ['새 조로 옮긴 내 선율', 'C장조 선율을 B, F♯, D♭, G♭장조로: 새 조표, 새 글자, 이상한 음.'],
  'mk-tunechords': ['내 선율, 내 화음', '여섯 음을 쓰고, 음마다 그 음이 든 화음을. I로 시작, V–I나 IV–I로 끝.'],
  'mk-offbeat': ['박에서 비켜서', '박 한 쌍을 당겨 당김음을, 3/4 두 마디를 헤미올라로.'],
  'mk-pianist': ['피아니스트 고치기',""")
rep("""'mk-pianist': ['body', 0, 1, 'game'],""", """'mk-pianist': ['body', 0, 1, 'game'], 'mk-bingo': ['intervals', 2, 2, 'game ear'], 'mk-four4': ['scales', 2, 2, 'game ear'], 'mk-anykey': ['scales', 2, 2, 'game ear'], 'mk-tunechords': ['chords', 2, 2, 'game ear'], 'mk-offbeat': ['rrhythm', 2, 2, 'game ear'],""")
rep("""'mk-pianist': 'k-posture',""", """'mk-pianist': 'k-posture', 'mk-bingo': 'aural', 'mk-four4': 'k-play', 'mk-anykey': 'p-scales', 'mk-tunechords': 'p-chords', 'mk-offbeat': 'r-beat',""")
rep("""  'mk-pianist': () => (\n""", """  'mk-bingo': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#7a4f96"/>{[0, 1, 2].map(r => [0, 1, 2].map(c => <rect key={r + '' + c} x={4 + c * 5.6} y={4 + r * 5.6} width="4.6" height="4.6" rx="1" fill={r === c ? '#e9a83a' : '#fefbf3'}/>))}</svg>
  ),
  'mk-four4': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/>{[0, 1, 2, 3].map(i => <rect key={i} x={3 + i * 4.6} y={15 - i * 3} width="3.6" height="3" rx="0.8" fill="#fefbf3"/>)}<text x="12" y="10" textAnchor="middle" fontFamily="Georgia, serif" fontSize="8" fontWeight="900" fill="#e9a83a">4!</text></svg>
  ),
  'mk-anykey': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/><text x="7" y="15" textAnchor="middle" fontFamily="Georgia, serif" fontSize="9" fontWeight="900" fill="#fefbf3">C</text><path d="M10.5 12 H14.5 M13 10 L15 12 L13 14" stroke="#e9a83a" strokeWidth="1.3" fill="none"/><text x="18.5" y="15" textAnchor="middle" fontFamily="Georgia, serif" fontSize="8" fontWeight="900" fill="#fefbf3">F♯</text></svg>
  ),
  'mk-tunechords': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#e4572e"/>{[[5, 7], [10, 5], [15, 8], [19, 6]].map(([x, y]) => <circle key={x} cx={x} cy={y} r="1.6" fill="#fefbf3"/>)}{[5, 10, 15, 19].map((x, i) => <g key={'c' + x}><rect x={x - 1.8} y={12} width="3.6" height="8" rx="1" fill={i === 3 ? '#e9a83a' : 'none'} stroke="#fefbf3" strokeWidth="0.9"/></g>)}</svg>
  ),
  'mk-offbeat': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/>{[4, 10, 16].map(x => <line key={x} x1={x} x2={x} y1="15" y2="19" stroke="#fefbf3" strokeWidth="1.2"/>)}<rect x="6" y="7" width="7" height="3" rx="1.5" fill="#e9a83a"/><rect x="14" y="7" width="3" height="3" rx="1.5" fill="#fefbf3"/><rect x="2.5" y="7" width="2.5" height="3" rx="1.25" fill="#fefbf3"/></svg>
  ),
  'mk-pianist': () => (\n""")
rep("""lessons: ['l4-iv', 'l4-two', 'l4-mid', 'l4-clap'], check: 'listen-4' },""", """lessons: ['l4-iv', 'l4-two', 'l4-mid', 'l4-clap', 'mk-bingo'], check: 'listen-4' },""")
rep("""lessons: ['s4-four', 's4-touch', 's4-mirror', 's4-chrom', 's4-arp'], check: 'scales-4' },""", """lessons: ['s4-four', 's4-touch', 's4-mirror', 's4-chrom', 's4-arp', 'mk-four4'], check: 'scales-4' },""")
rep("""lessons: ['k4-sig', 'k4-lead', 'k4-semi', 'k4-below', 'k4-mod', 'k4-tr'], check: 'keys-4' },""", """lessons: ['k4-sig', 'k4-lead', 'k4-semi', 'k4-below', 'k4-mod', 'k4-tr', 'mk-anykey'], check: 'keys-4' },""")
rep("""lessons: ['h4-deg', 'h4-inv', 'h4-cad', 'h4-fit'], check: 'harmony-4' },""", """lessons: ['h4-deg', 'h4-inv', 'h4-cad', 'h4-fit', 'mk-tunechords'], check: 'harmony-4' },""")
rep("""lessons: ['r4-sync', 'r4-hem', 'r4-ts', 'r4-bar'], check: 'rhythm-4' },""", """lessons: ['r4-sync', 'r4-hem', 'r4-ts', 'r4-bar', 'mk-offbeat'], check: 'rhythm-4' },""")
rep("""  set('G', 'mk-pianist mk-ways'); set('23', 'mk-hidden mk-duel mk-melmin mk-choir mk-split');   // Build CH""", """  set('G', 'mk-pianist mk-ways'); set('23', 'mk-hidden mk-duel mk-melmin mk-choir mk-split');   // Build CH
  set('4', 'mk-bingo mk-four4 mk-anykey mk-tunechords mk-offbeat');   // Build CI""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
