import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CO: Time signatures gets its thing to make (the one room of 59 without one). Guess my time signature: the child
# makes four bars in a secret 2/4, 3/4 or 4/4 (the room's own note values, walk and run-ning), hides it, plays it, and a
# listener guesses how many beats are in a bar. Beat 1 is the strong one (the room's 'strong and weak beats'); the
# harder way plays no clicks, only the notes, beat 1 a little louder. Me : Listener, like Trick your teacher.

CODE = r"""
// ══ Build CO: Time signatures, Guess my time signature ══
const GT_VAL = [['q', 1, 'walk', '타'], ['p', 1, 'run-ning', '티-티'], ['h', 2, '2 beats', '2박'], ['hd', 3, '3 beats', '3박'], ['w', 4, '4 beats', '4박'], ['r', 1, 'rest, 1 beat', '쉼표 1박'], ['hr', 2, 'rest, 2 beats', '쉼표 2박']];
const GT_BPM = 96;
const gtLen = (k) => GT_VAL.find(v => v[0] === k)[1];
const gtSum = (bar) => bar.reduce((a, k) => a + gtLen(k), 0);
function gtRandom(top) {
  return [0, 1, 2, 3].map(() => { const bar = []; let left = top;
    while (left > 0) { const opts = GT_VAL.filter(v => v[1] <= left && !(left === top && v[0][0] !== 'q' && v[0] !== 'h' && v[0] !== 'hd' && v[0] !== 'w') && !(v[0] === 'w' && top !== 4)); const v = opts[Math.floor(Math.random() * opts.length)]; bar.push(v[0]); left -= v[1]; }
    return bar; });
}
function GuessTime() {
  const [top, setTop] = useState(3), [bars, setBars] = useState([[], [], [], []]), [msg, setMsg] = useState(null), [phase, setPhase] = useState('make');
  const [easy, setEasy] = useState(true), [score, setScore] = useState([0, 0]), [last, setLast] = useState(null), [lit, setLit] = useState(-1);
  const [got, setGot] = useState({ fool: false, all: {}, rest: false });
  const T = useSpTimers();
  const cur = bars.findIndex(b => gtSum(b) < top), full = cur < 0;
  const add = (k) => {
    if (phase !== 'make') return;
    if (full) { setMsg([t('All four bars are full. Hide it and play it!', '네 마디가 다 찼어요. 숨기고 들려줘요!'), 0]); return; }
    const left = top - gtSum(bars[cur]);
    if (gtLen(k) > left) { setMsg([t('Only ' + left + (left === 1 ? ' beat' : ' beats') + ' left in bar ' + (cur + 1) + '. Try a shorter one.', (cur + 1) + '번 마디에 ' + left + '박만 남았어요. 더 짧은 걸로.'), 1]); return; }
    setMsg(null); setBars(bs => bs.map((b, j) => (j === cur ? b.concat([k]) : b)));
  };
  const undo = () => { let j = 3; while (j >= 0 && !bars[j].length) j--; if (j < 0) return; setBars(bs => bs.map((b, i) => (i === j ? b.slice(0, -1) : b))); setMsg(null); };
  const reset = (n) => { T.clear(); setLit(-1); setBars([[], [], [], []]); setMsg(null); setPhase('make'); setLast(null); if (n) setTop(n); };
  const items = (all) => { const out = [['ts', top]]; for (let j = 0; j < 4; j++) { if (!bars[j].length) break; bars[j].forEach(k => out.push([k])); if (gtSum(bars[j]) < top) break; out.push([j === 3 ? '||' : '|']); } return out; };
  const play = () => {
    T.clear(); const ctx = getAudio(); if (!ctx) return;
    const spb = 60 / GT_BPM, lead = 0.15, t0 = ctx.currentTime + lead + 2 * spb;
    metroClick(ctx, ctx.currentTime + lead, false, 0.16); metroClick(ctx, ctx.currentTime + lead + spb, false, 0.16);   // ready, go: the same in every metre
    let b = 0;
    bars.forEach((bar, j) => {
      if (easy) for (let i = 0; i < top; i++) metroClick(ctx, t0 + (b + i) * spb, i === 0, i === 0 ? 0.42 : 0.14);
      let pos = 0;
      bar.forEach(k => { const at = t0 + (b + pos) * spb, strong = pos === 0, v = strong ? (easy ? 0.26 : 0.34) : 0.15;
        if (k === 'p') { blip(ctx, at, SRH_HZ, spb * 0.42, v, 'triangle'); blip(ctx, at + spb / 2, SRH_HZ, spb * 0.42, 0.13, 'triangle'); }
        else if (k !== 'r' && k !== 'hr') blip(ctx, at, SRH_HZ, gtLen(k) * spb * 0.9, v, 'triangle');
        pos += gtLen(k); });
      T.at((lead + 2 * spb + b * spb) * 1000, () => setLit(j)); b += top;
    });
    T.at((lead + 2 * spb + b * spb) * 1000 + 150, () => setLit(-1));
  };
  const hide = () => { setPhase('listen'); setTimeout(play, 60); };
  const guess = (n) => {
    const right = n === top; setScore(([a, c]) => (right ? [a, c + 1] : [a + 1, c])); setLast({ n, right }); setPhase('reveal'); T.clear(); setLit(-1);
    setGot(g => ({ fool: g.fool || !right, all: { ...g.all, [top]: true }, rest: g.rest || bars.some(b => b.some(k => k === 'r' || k === 'hr')) }));
  };
  const goals = [[got.fool, t('Fool the listener', '듣는 사람 속이기')], [Object.keys(got.all).length >= 3, t('One in 2/4, 3/4 and 4/4', '2/4, 3/4, 4/4 하나씩')], [got.rest, t('A rest in it', '쉼표 넣기')]];
  const stars = goals.filter(g => g[0]).length;
  const staff = <div style={{position:'relative'}}><SrhStaff items={items()} full o={{}} label={t('Your four bars in ' + top + '/4', top + '/4로 만든 네 마디')}/></div>;
  return (
    <div className="try-box" style={actBox} data-mk="gtime">
      <div style={actTitle}>{t('Guess my time signature', '내 박자표 맞혀 봐')}</div>
      <div style={actNote}>{t('Make four bars in a secret time signature. Then hide it, play it, and let someone guess: how many beats in each bar? Listen for the strong beat 1.', '비밀 박자표로 네 마디를 만들어요. 그다음 숨기고 들려주고, 맞혀 보라고 해요: 한 마디에 몇 박일까? 센박 1을 잘 들어 봐요.')}</div>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',gap:8,margin:'0 0 6px',fontSize:13.5,fontWeight:900,color:BK.ink}}>
        <span>{t('Me ' + score[0] + ' : ' + score[1] + ' Listener', '나 ' + score[0] + ' : ' + score[1] + ' 듣는 사람')}</span>
        <span aria-label={t(stars + ' of 3 stars', '별 3개 중 ' + stars + '개')} style={{color:stars ? BK.green : BK.muted,letterSpacing:2}}>{'★'.repeat(stars)}<span style={{opacity:0.3}}>{'★'.repeat(3 - stars)}</span></span>
      </div>
      {phase === 'make' && <>
        {spChips([[2, '2/4'], [3, '3/4'], [4, '4/4']], top, (n) => reset(n))}
        {staff}
        <div style={{display:'flex',gap:4,justifyContent:'center',margin:'4px 0 6px'}} aria-hidden="true">{[0, 1, 2, 3].map(j => <span key={j} style={{width:46,height:8,borderRadius:4,background:gtSum(bars[j]) >= top ? BK.ink : gtSum(bars[j]) ? 'rgba(38,41,107,0.35)' : 'rgba(38,41,107,0.1)'}}/>)}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6}}>
          {GT_VAL.filter(v => v[1] <= top).map(v => <button key={v[0]} className="choice-btn" onClick={() => add(v[0])} style={{padding:'4px 2px',display:'flex',flexDirection:'column',alignItems:'center',gap:0,minHeight:64}}>
            <NvGlyph kind={v[0]} size={30}/><span style={{fontSize:11.5,fontWeight:800,lineHeight:1.2}}>{t(v[2], v[3])}</span></button>)}
        </div>
        {msg ? spMsg(msg[0], msg[1] ? BK.coral : BK.green) : spMsg(full ? t('Four bars! Now hide it and play it.', '네 마디 완성! 이제 숨기고 들려줘요.') : t('Bar ' + (cur + 1) + ': ' + (top - gtSum(bars[cur])) + ' of ' + top + ' beats left', (cur + 1) + '번 마디: ' + top + '박 중 ' + (top - gtSum(bars[cur])) + '박 남음'))}
        <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>
          <button className="primary-btn" style={spBtn} disabled={!full} onClick={hide}>{t('Hide it and play →', '숨기고 들려주기 →')}</button>
          <button className="ghost-btn" style={spBtn} onClick={undo}>{t('Undo', '되돌리기')}</button>
          <button className="ghost-btn" style={spBtn} onClick={() => { setBars(gtRandom(top)); setMsg(null); }}>{t('Surprise me', '아무거나')}</button>
        </div>
        <label style={{display:'flex',alignItems:'center',justifyContent:'center',gap:6,fontSize:13,fontWeight:700,color:BK.muted,marginTop:8}}><input type="checkbox" checked={!easy} onChange={(e) => setEasy(!e.target.checked)}/>{t('Harder: no clicks, only the notes', '더 어렵게: 클릭 없이 음만')}</label>
      </>}
      {phase !== 'make' && <>
        {phase === 'listen'
          ? <div style={{border:'2px dashed ' + BK.ink,borderRadius:12,padding:'18px 10px',textAlign:'center',margin:'4px 0 8px'}}>
              <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1}}>?<br/><span style={{fontSize:30}}>4</span></div>
              <div style={{display:'flex',gap:4,justifyContent:'center',margin:'10px 0 0'}}>{[0, 1, 2, 3].map(j => <span key={j} style={{width:40,height:10,borderRadius:5,background:lit === j ? BK.coral : 'rgba(38,41,107,0.15)',transition:'background .1s'}}/>)}</div>
              <div style={{fontSize:13.5,fontWeight:700,color:BK.muted,marginTop:8}}>{t('Listener: how many beats in a bar?', '듣는 사람: 한 마디에 몇 박일까요?')}</div>
            </div>
          : <>{staff}{spMsg(last && last.right ? t('The listener got it: ' + top + ' beats in a bar.', '듣는 사람이 맞혔어요: 한 마디에 ' + top + '박.') : t('You fooled them! It was ' + top + '/4, not ' + (last ? last.n : '') + '/4.', '속였어요! ' + (last ? last.n : '') + '/4가 아니라 ' + top + '/4였어요.'), last && last.right ? BK.ink : BK.coral)}</>}
        {phase === 'listen' && <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:8,margin:'0 0 8px'}}>{[2, 3, 4].map(n => <button key={n} className="choice-btn" style={{padding:'12px 4px',fontSize:18,fontWeight:900}} onClick={() => guess(n)}>{n}<span style={{fontSize:12,fontWeight:800,display:'block'}}>{t('beats', '박')}</span></button>)}</div>}
        <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>
          <button className={phase === 'listen' ? 'primary-btn' : 'ghost-btn'} style={spBtn} onClick={play}>{t('▶ Play it again', '▶ 다시 듣기')}</button>
          {phase === 'reveal' && <button className="primary-btn" style={spBtn} onClick={() => reset()}>{t('Make another →', '하나 더 만들기 →')}</button>}
        </div>
      </>}
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:10}}>{goals.map(([ok, lab], i) => <span key={i} style={{fontSize:12,fontWeight:800,padding:'3px 9px',borderRadius:12,border:'1.5px solid ' + (ok ? BK.green : 'rgba(38,41,107,0.2)'),color:ok ? BK.green : BK.muted}}>{(ok ? '★ ' : '☆ ') + lab}</span>)}</div>
    </div>
  );
}

"""
rep("// ══ Build BH: Blues jam ══", CODE + "// ══ Build BH: Blues jam ══")
rep("""  { id: 'mk-surprise', ch: 'piano-story',""", """  { id: 'mk-gtime', ch: 'time-signatures', title: 'Guess my time signature', blurb: 'Four bars in a secret 2/4, 3/4 or 4/4: hide it, play it, and let someone guess.', C: () => <GuessTime/> },   // Build CO
  { id: 'mk-surprise', ch: 'piano-story',""")
rep("""  'mk-surprise': ['깜짝 놀래기!',""", """  'mk-gtime': ['내 박자표 맞혀 봐', '비밀 2/4, 3/4, 4/4로 네 마디: 숨기고 들려주고, 맞혀 보라고 해요.'],
  'mk-surprise': ['깜짝 놀래기!',""")
rep("""'mk-surprise': ['about', 0, 1, 'game ear']""", """'mk-surprise': ['about', 0, 1, 'game ear'], 'mk-gtime': ['rtime', 0, 1, 'game ear']""")
rep("""'mk-surprise': 'about',""", """'mk-surprise': 'about', 'mk-gtime': 'r-beat',""")
rep("""  'mk-surprise': () => (""", """  'mk-gtime': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/><text x="12" y="11" textAnchor="middle" fontFamily="Georgia, serif" fontSize="9" fontWeight="900" fill="#fefbf3">?</text><path d="M7 12.6H17" stroke="#fefbf3" strokeWidth="1"/><text x="12" y="20.5" textAnchor="middle" fontFamily="Georgia, serif" fontSize="8.5" fontWeight="900" fill="#fefbf3">4</text></svg>
  ),
  'mk-surprise': () => (""")
rep("""'rt-bars', 'rt-ts', 'rt-strong', 'rt-fill', 'rt-tie']""", """'rt-bars', 'rt-ts', 'rt-strong', 'rt-fill', 'rt-tie', 'mk-gtime']""")
rep("""set('G', 'mk-word mk-staffword mk-move mk-trick mk-steps');""", """set('G', 'mk-word mk-staffword mk-move mk-trick mk-steps mk-gtime');""")
rep("""'common-cut', 'beat-doubler'],""", """'common-cut', 'beat-doubler', 'mk-gtime'],""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
