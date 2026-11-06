// ─── Phase 376: the Lesson Book's pages 4, 5 and 7, with the parts that move ───
// Page 4: the hand from the side (the book's drawing), with the roller wrist and the five faults it can turn into.
// Page 5: both hands from above; tap a finger, or play "Which finger?". Page 7: the five checks, starred per lesson.
const RH_GOOD = [80, 55, 24, -3, -2];
const RH_FAULTS = ['flat', 'bridge', 'nail', 'low', 'high'];
function RoundHand376() {
  const [mode, setMode] = useState('good');     // good | roller | one of RH_FAULTS
  const [ang, setAng] = useState(RH_GOOD);
  const [ph, setPh] = useState(0);
  const from = useRef(RH_GOOD);
  // morph to the chosen pose; the roller sways the wrist while the fingertip stays on the key
  useEffect(() => {
    let raf, t0 = null; const a0 = ang.slice(), target = mode === 'good' || mode === 'roller' ? RH_GOOD : HAND_POSES[mode].a;
    const step = (ts) => {
      if (t0 == null) t0 = ts; const k = Math.min(1, (ts - t0) / 450), e = pEase(k);
      if (mode === 'roller') { const w = Math.sin((ts - t0) / 1600 * Math.PI * 2) * Math.min(1, (ts - t0) / 400); setPh(w); setAng([80, 55, 24, -3 + 11 * w, -2 + 5 * w]); raf = requestAnimationFrame(step); return; }
      setAng(a0.map((v, i) => v + (target[i] - v) * e)); if (k < 1) raf = requestAnimationFrame(step);
    };
    raf = requestAnimationFrame(step);
    return () => cancelAnimationFrame(raf);
  }, [mode]);
  const roller = mode === 'roller';
  const shapes = useMemo(() => {
    const r = penHandSide(ang, { ball: mode === 'good', faults: !roller, nail: mode === 'nail', halo: true, keyText: t('key level', '건반 높이'), wristText: t('wrist', '손목'), knuckleText: t('knuckle', '마디'), tipText: t('tip', '손끝') });
    const s = r.shapes;
    if (roller) {   // the roller under the forearm, turning as the wrist sways
      const [, , , , wr, fa] = r.pts, c = pAdd(wr, pSub(fa, wr), 0.22), u = pUnit(pSub(fa, wr)), n = [u[1], -u[0]], o = pAdd(c, n, n[1] > 0 ? 17 : -17);   // below the forearm
      s.splice(4, 0, { k: 'el', c: o, rx: 7, ry: 7, f: PEN_P, s: PEN_C, w: 2 });
      for (let i = 0; i < 3; i++) { const a = ph * 2.4 + i * Math.PI / 3; s.splice(5, 0, penLine([o[0] - 6 * Math.cos(a), o[1] - 6 * Math.sin(a)], [o[0] + 6 * Math.cos(a), o[1] + 6 * Math.sin(a)], 1.2, PEN_C)); }
    }
    return s;
  }, [ang, mode, ph, LANG]);
  const P = mode === 'good' || roller ? null : HAND_POSES[mode];
  return (
    <div className="try-box" data-round-hand style={actBox}>
      <div style={{display:'flex',flexWrap:'wrap',gap:4,marginBottom:8}}>
        <button className={'chip' + (mode === 'good' ? ' active' : '')} style={{padding:'3px 9px',fontSize:12.5}} onClick={() => setMode('good')}>{t('The good shape', '좋은 모양')}</button>
        <button className={'chip' + (roller ? ' active' : '')} style={{padding:'3px 9px',fontSize:12.5}} onClick={() => setMode(roller ? 'good' : 'roller')} aria-pressed={roller}>{roller ? t('■ Roller wrist', '■ 롤러 손목') : t('▶ Roller wrist', '▶ 롤러 손목')}</button>
        {RH_FAULTS.map(f => <button key={f} className={'chip' + (mode === f ? ' active' : '')} style={{padding:'3px 9px',fontSize:12.5}} onClick={() => setMode(f)}><span style={{color:mode === f ? '#fff' : BK.coral}}>✗</span> {HAND_POSES[f].title}</button>)}
      </div>
      <div style={{background:BK.soft,borderRadius:12,padding:'4px 2px'}}><PenArt shapes={shapes} vb={[34, 26, 258, 126]} label={t('A hand on a key, seen from the side', '옆에서 본, 건반 위의 손')} style={{maxWidth:520,margin:'0 auto'}}/></div>
      <div style={{background:'#faf6ec',borderRadius:8,padding:'8px 10px',marginTop:8,fontSize:13.5,lineHeight:1.5,minHeight:44}}>
        {roller ? (LANG === 'ko' ? <><b>롤러 손목:</b> 손끝은 건반에 그대로, 팔뚝 아래 롤러가 있는 것처럼 손목이 위아래로 흔들려요(좌우로도요). 마디와 손끝은 무너지지 않아요.</>
            : <><b>The roller wrist:</b> the fingertip stays on the key while the wrist sways up and down (and side to side), as if a roller sat under the forearm. The knuckles and the tip stay up.</>)
          : P ? <><b style={{color:BK.coral}}>{P.title}.</b> {P.see} {P.fix && <span style={{display:'block',marginTop:3}}><b>{t('Try: ', '해 봐요: ')}</b>{P.fix}</span>}</>
          : <><b>{HAND_POSES.good.title}.</b> {HAND_POSES.good.see}</>}
      </div>
    </div>
  );
}
// page 5: tap a finger to see its number and nickname, or play "Which finger?"
function FingerNumbers376() {
  const [lit, setLit] = useState({ hand: 'R', f: 1 });
  const [ask, setAsk] = useState(null);
  const [res, setRes] = useState(null);
  const [score, setScore] = useState({ right: 0, tries: 0 });
  const next = () => { setAsk({ hand: Math.random() < 0.5 ? 'L' : 'R', f: 1 + Math.floor(Math.random() * 5) }); setRes(null); };
  function tap(hand, f) {
    const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime + 0.01, 262 * Math.pow(2, [0, 2, 4, 5, 7][f - 1] / 12) * (hand === 'L' ? 0.5 : 1), 0.25, 0.15, 'triangle');
    setLit({ hand, f });
    if (!ask) return;
    const ok = hand === ask.hand && f === ask.f; setRes(ok ? 'good' : 'bad');
    setScore(s => ({ right: s.right + (ok ? 1 : 0), tries: s.tries + 1 }));
    if (ok) setTimeout(next, 750);
  }
  const onHand = (hand) => (e) => { const el = e.target.closest && e.target.closest('[data-f]'); if (el) tap(hand, +el.getAttribute('data-f')); };
  const name = FINGER_NAMES[lit.f - 1];
  return (
    <div className="try-box" data-finger-numbers style={actBox}>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <div style={actTitle}>{ask ? t('Which finger?', '어느 손가락?') : t('Tap a finger', '손가락을 눌러 봐요')}</div>
        {ask && <div style={{fontSize:13,fontWeight:800,color:'var(--muted)'}}>{score.right}/{score.tries}</div>}
      </div>
      <div style={{display:'flex',justifyContent:'center',gap:'clamp(10px, 6vw, 40px)',margin:'6px 0'}}>
        {['L', 'R'].map(h => (
          <div key={h} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:2}}>
            <div onClick={onHand(h)} role="group" aria-label={h === 'L' ? t('Left hand', '왼손') : t('Right hand', '오른손')} style={{cursor:'pointer',background:BK.soft,borderRadius:12,padding:'4px 6px'}}>
              <PbArt name={'q-fingers-' + h + '-plain'} h={150} lit={lit.hand === h && (!ask || res) ? lit.f : null} style={{maxWidth:'100%'}}/>
            </div>
            {/* the same five fingers as buttons, in the hand's own order (left: 5 4 3 2 1; right: 1 2 3 4 5); in the game they hide their numbers */}
            <div style={{display:'flex',gap:3}}>{(h === 'L' ? [5, 4, 3, 2, 1] : [1, 2, 3, 4, 5]).map(f => { const on = lit.hand === h && lit.f === f && (!ask || res);
              return <button key={f} onClick={() => tap(h, f)} aria-label={(h === 'L' ? t('Left hand ', '왼손 ') : t('Right hand ', '오른손 ')) + f}
                style={{width:24,height:24,borderRadius:12,border:'1.6px solid ' + (on ? BK.coral : BK.ink),background:on ? BK.coral : '#fff',color:on ? '#fff' : BK.ink,fontSize:12,fontWeight:900,padding:0,cursor:'pointer'}}>{ask && !res ? '' : f}</button>; })}</div>
            <b style={{fontSize:13,color:BK.ink}}>{h === 'L' ? t('Left hand', '왼손') : t('Right hand', '오른손')}</b>
          </div>))}
      </div>
      <div style={{textAlign:'center',minHeight:52}}>
        {ask ? <div style={{fontSize:19,fontWeight:900}}>{LANG === 'ko' ? <>"{ask.hand === 'L' ? '왼손' : '오른손'} <span style={{color:BK.coral}}>{ask.f}</span>번!"</> : <>"{ask.hand === 'L' ? 'Left' : 'Right'} hand, <span style={{color:BK.coral}}>{ask.f}</span>!"</>}
            {res && <div style={{fontSize:14,color:res === 'good' ? POS_GOOD : POS_BAD}}>{res === 'good' ? t('✓ Yes!', '✓ 맞아요!') : (LANG === 'ko' ? '✗ 그건 ' + (lit.hand === 'L' ? '왼손 ' : '오른손 ') + lit.f + '번이에요' : '✗ That’s ' + (lit.hand === 'L' ? 'left' : 'right') + ' hand ' + lit.f)}</div>}</div>
          : <div style={{fontSize:17,fontWeight:900}}>{LANG === 'ko' ? (lit.hand === 'L' ? '왼손 ' : '오른손 ') + lit.f + '번' : (lit.hand === 'L' ? 'Left' : 'Right') + ' hand, ' + lit.f}<div style={{fontSize:14,fontWeight:800,color:BK.coral}}>{t(name.en, name.ko)}</div></div>}
      </div>
      <div style={{textAlign:'center'}}><button className="ghost-btn" style={{fontWeight:800}} onClick={() => { if (ask) { setAsk(null); setRes(null); } else { setScore({ right: 0, tries: 0 }); next(); } }}>{ask ? t('Stop the game', '게임 멈추기') : t('▶ Play “Which finger?”', '▶ "어느 손가락?" 게임')}</button></div>
    </div>
  );
}
// page 7: a star for each check in each lesson (kept on this device)
const FIVE_KEY = 'pb_five_checks_v1';
function FiveChecks376({ rows }) {
  const [st, setSt] = useState(() => { try { return JSON.parse(localStorage.getItem(FIVE_KEY)) || {}; } catch (e) { return {}; } });
  const tog = (r, c) => { const k = r + '-' + c, nx = { ...st, [k]: !st[k] }; if (!nx[k]) delete nx[k]; setSt(nx); try { localStorage.setItem(FIVE_KEY, JSON.stringify(nx)); } catch (e) {} };
  const n = Object.keys(st).length;
  return (
    <div data-five-checks style={{display:'flex',flexDirection:'column',gap:7}}>
      {rows.map(([a, txt], r) => (
        <div key={a} style={{border:'1px solid #ece6d8',borderRadius:12,padding:'6px 8px 8px',display:'flex',flexWrap:'wrap',alignItems:'center',gap:'4px 10px'}}>
          <div style={{flex:'1 1 200px',display:'flex',alignItems:'center',gap:10,minWidth:0}}>
            <div style={{flex:'0 0 64px',display:'flex',justifyContent:'center'}}><PbArt name={a} h={a === 'chk-hand' ? 38 : 52}/></div>
            <div style={{fontSize:14,fontWeight:800,color:BK.ink,lineHeight:1.3}}>{txt}</div>
          </div>
          <div style={{flex:'0 0 auto',display:'flex',gap:4,marginLeft:'auto'}}>{[1, 2, 3, 4, 5, 6].map(c => { const on = !!st[r + '-' + c]; return (
            <button key={c} onClick={() => tog(r, c)} aria-pressed={on} aria-label={txt + ', ' + t('lesson ', '레슨 ') + c} title={t('Lesson ', '레슨 ') + c}
              style={{width:30,height:36,border:'1.5px solid ' + (on ? BK.coral : BK.line),borderRadius:7,background:on ? '#fdeee8' : '#fff',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',gap:1,padding:0,cursor:'pointer'}}>
              <BkStarG size={14} fill={on ? BK.coral : '#ece6d8'}/><span style={{fontSize:9,fontWeight:800,color:BK.muted,lineHeight:1}}>{c}</span></button>); })}</div>
        </div>))}
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:12.5,color:BK.muted}}>
        <span>{t(n + (n === 1 ? ' star' : ' stars') + ' so far (lesson 1 to 6)', '지금까지 별 ' + n + '개 (레슨 1~6)')}</span>
        {n > 0 && <button className="ghost-btn" style={{fontSize:12,padding:'3px 10px'}} onClick={() => { setSt({}); try { localStorage.removeItem(FIVE_KEY); } catch (e) {} }}>{t('Start again', '처음부터')}</button>}
      </div>
    </div>
  );
}
