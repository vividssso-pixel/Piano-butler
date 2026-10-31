// ── Build DX (her 11:31 'the piano's story should have things like the black-key jam; it all feels stiff'): a free-play toy
// in four of the room's steps, under the step's own pad. Played on the app's piano (blip 'triangle' = the sampled piano when
// it is on) or the story's harpsichord and clavichord voices; the facts are the ones the room already teaches (pluck, push,
// strike; long thick strings low; what each pedal does; 88 keys, A to C, eight Cs). ──
const SPS9_WK = (m) => PC_INFO[((m % 12) + 12) % 12].white;
// a keyboard from lo to hi (both white), every key playable; down(m, vel 0..1 from how near the front you tap), up(m);
// lit: keys held (coral), glow: keys still sounding (soft coral)
function Sps9Keys({ lo, hi, lit = [], glow = [], onDown, onUp, h = 96 }) {
  const whites = [], blacks = []; let w = 0;
  for (let m = lo; m <= hi; m++) { if (SPS9_WK(m)) { whites.push({ m, x: w * 24 }); w++; } else blacks.push({ m, x: w * 24 - 7.5 }); }
  const KW = w * 24, BH = h * 0.62;
  const down = (m, e, top) => { e.preventDefault(); try { e.currentTarget.releasePointerCapture(e.pointerId); } catch (x) {}
    const r = e.currentTarget.getBoundingClientRect(), y = Math.max(0, Math.min(1, (e.clientY - r.top) / Math.max(1, r.height)));
    onDown(m, top ? 0.25 + 0.7 * y : 0.15 + 0.8 * y); };
  const handlers = (m, top) => ({ onPointerDown: (e) => down(m, e, top), onPointerUp: () => onUp(m), onPointerLeave: () => onUp(m), onPointerCancel: () => onUp(m), 'data-key': m, style: { cursor: 'pointer' } });
  const fillOf = (m, base) => lit.includes(m) ? PEN_C : glow.includes(m) ? '#f6b9a6' : base;
  return <svg viewBox={'-1 -1 ' + (KW + 2) + ' ' + (h + 2)} style={{width:'100%',display:'block',touchAction:'none',userSelect:'none',WebkitUserSelect:'none'}}>
    {whites.map(k => <rect key={k.m} x={k.x} y="0" width="24" height={h} rx="3" fill={fillOf(k.m, '#fff')} stroke={PEN_N} strokeWidth="1.1" {...handlers(k.m, false)}/>)}
    {blacks.map(k => <rect key={k.m} x={k.x} y="0" width="15" height={BH} rx="2" fill={fillOf(k.m, PEN_N)} stroke={PEN_N} strokeWidth="1" {...handlers(k.m, true)}/>)}
    {whites.filter(k => k.m === 60).map(k => <text key="mc" x={k.x + 12} y={h - 8} textAnchor="middle" fontSize="10" fontWeight="900" fill={lit.includes(60) ? '#fff' : PEN_N} style={{pointerEvents:'none'}}>C</text>)}
  </svg>;
}
const sps9Box = { ...actBox, margin: '4px 0 10px' };

// ── step 1, before the piano: play the three keyboards yourself, over a bass that goes round (C G A E F C F G, all white
// keys fit). Near the front of a key is loud, near the back soft: on the harpsichord it makes no difference ──
const SPS9_BASS = [48, 43, 45, 40, 41, 36, 41, 43];
function SpsTimeKeys() {
  const [inst, setInst] = useState('harpsichord'), [lit, setLit] = useState([]), [lv, setLv] = useState(null), [bass, setBass] = useState(false);
  const sched = useRef(null), next = useRef(0), k = useRef(0), instRef = useRef(inst); instRef.current = inst;
  const stopBass = () => { clearInterval(sched.current); sched.current = null; setBass(false); };
  const me = useRef(() => stopBass()).current;
  useEffect(() => () => { clearInterval(sched.current); spsRelease(me); }, []);
  function startBass() { const ctx = getAudio(); if (!ctx) return; spsTake(me); clearInterval(sched.current); next.current = ctx.currentTime + 0.12; k.current = 0;
    const SPB = 60 / 72;
    const tick = () => { while (next.current < ctx.currentTime + 0.35) { const m = SPS9_BASS[k.current % 8];
      instNote(instRef.current, ctx, next.current, m, SPB * 0.92, 0.42); k.current++; next.current += SPB; } };
    tick(); sched.current = setInterval(tick, 80); setBass(true); }
  const meter = (i, v) => i === 'harpsichord' ? 0.6 : i === 'clavichord' ? 0.08 + 0.18 * v : 0.12 + 0.86 * v;
  function down(m, v) { const ctx = getAudio(); if (!ctx) return; const i = instRef.current;
    instNote(i, ctx, ctx.currentTime + 0.005, m, i === 'piano' ? 1.4 : 0.9, i === 'piano' ? v * 0.75 : v);
    setLv(meter(i, v)); setLit(l => l.concat(m)); }
  const up = (m) => setLit(l => l.filter(x => x !== m));
  return <div className="try-box" style={sps9Box} data-sps9="keys">
    <div style={actTitle}>{t('Play them yourself', '직접 쳐 봐요')}</div>
    <div style={actNote}>{t('Pick a keyboard and play anything. Tap near the front of a key for a strong touch, near the back for a gentle one. Which keyboard gets louder? Start the bass: it goes round and round, and every white key fits over it.', '건반 악기를 골라 마음대로 쳐 봐요. 건반 앞쪽을 누르면 세게, 안쪽을 누르면 살살 친 거예요. 어느 악기가 더 커지나요? 베이스를 켜 봐요: 같은 저음이 빙글빙글 돌고, 흰건반은 무엇이든 어울려요.')}</div>
    {spsGrid(104, SPS_INST.map(i => <button key={i} className={'chip' + (i === inst ? ' active' : '')} style={{padding:'8px 4px',fontSize:15,minHeight:44,wordBreak:'keep-all'}} onClick={() => setInst(i)}>{SPS_IW[i]()}</button>))}
    <div style={{margin:'10px auto 0',maxWidth:460}}><Sps9Keys lo={60} hi={83} lit={lit} onDown={down} onUp={up}/></div>
    <div style={{display:'grid',gridTemplateColumns:'auto 1fr',gap:'4px 10px',alignItems:'center',maxWidth:320,margin:'8px auto 0',fontSize:14,fontWeight:800}}>
      <span>{t('Sound', '소리')}</span><div style={{height:12,borderRadius:6,background:'#fff',border:'1px solid rgba(38,41,107,0.3)',overflow:'hidden'}}><div style={{width:(lv == null ? 0 : lv * 100) + '%',height:'100%',background:PEN_C,transition:'width 0.15s'}}/></div>
    </div>
    {spsRow(<button className={bass ? 'primary-btn' : 'ghost-btn'} style={{...SPS_TAP,width:'auto',padding:'8px 18px'}} data-sps9-bass onClick={() => (bass ? (stopBass(), spsRelease(me)) : startBass())}>{bass ? t('■ Stop the bass', '■ 베이스 멈추기') : t('▶ Start the bass', '▶ 베이스 켜기')}</button>)}
    {inst === 'harpsichord' && <div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.coral,marginTop:6}}>{t('A quill plucks: strong or gentle, the same loudness.', '깃촉이 뜯어요: 세게 쳐도 살살 쳐도 같은 크기.')}</div>}
  </div>;
}

// ── step 3, inside the piano: the strings seen from above, long and thick on the left (low), short and thin on the right
// (high). Tap one, or slide across them all; each string shakes as it sounds ──
const SPS9_STR = []; for (let m = 36; m <= 72; m++) if (SPS9_WK(m)) SPS9_STR.push(m);   // 22 white strings, C2 to C5
function SpsStringHarp() {
  const n = SPS9_STR.length, x0 = 22, dx = 296 / (n - 1), yb = 150, top = (i) => 18 + 112 * Math.pow(i / (n - 1), 0.85), sw = (i) => 3.4 - 2.4 * i / (n - 1);
  const [shake, setShake] = useState({}), last = useRef(-1), T = useRef([]);
  useEffect(() => () => T.current.forEach(clearTimeout), []);
  const ix = (e) => { const r = e.currentTarget.getBoundingClientRect(), x = (e.clientX - r.left) / r.width * 340; return Math.max(0, Math.min(n - 1, Math.round((x - x0) / dx))); };
  function pluck(i) { const ctx = getAudio(); if (!ctx) return; blip(ctx, ctx.currentTime + 0.005, mFreq(SPS9_STR[i]), 1.8, 0.16, 'triangle');
    const id = Math.random(); setShake(s => ({ ...s, [i]: id })); T.current.push(setTimeout(() => setShake(s => (s[i] === id ? (({ [i]: _, ...r }) => r)(s) : s)), 900)); }
  function across(i) { const a = last.current; if (a < 0) { pluck(i); } else if (i !== a) { const st = i > a ? 1 : -1; for (let j = a + st; st > 0 ? j <= i : j >= i; j += st) pluck(j); } last.current = i; }
  return <div className="try-box" style={sps9Box} data-sps9="harp">
    <style>{'@keyframes sps9Ring{0%{opacity:1}100%{opacity:0.25}}.sps9-ring{animation:sps9Ring 0.9s ease-out forwards}.sps9-ring path:first-child{animation:sps9Flick 0.08s steps(2) infinite}@keyframes sps9Flick{0%{opacity:1}100%{opacity:0.35}}@media (prefers-reduced-motion: reduce){.sps9-ring,.sps9-ring path{animation:none}}'}</style>
    <div style={actTitle}>{t('Strum the strings', '현을 쓸어 봐요')}</div>
    <div style={actNote}>{t('The lid is open. Tap a string, or slide your finger across them all. The long, thick strings sing low; the short, thin ones sing high.', '뚜껑이 열렸어요. 현 하나를 톡 치거나, 손가락으로 쭉 쓸어 봐요. 길고 굵은 현은 낮게, 짧고 가는 현은 높게 노래해요.')}</div>
    <svg viewBox="0 0 340 178" style={{width:'100%',maxWidth:460,display:'block',margin:'0 auto',touchAction:'none',userSelect:'none',cursor:'pointer'}}
      onPointerDown={(e) => { e.preventDefault(); try { e.currentTarget.setPointerCapture(e.pointerId); } catch (x) {} last.current = -1; across(ix(e)); }}
      onPointerMove={(e) => { if (last.current >= 0) across(ix(e)); }} onPointerUp={() => { last.current = -1; }} onPointerCancel={() => { last.current = -1; }}>
      <path d={'M8 ' + (yb + 8) + ' L8 12 C120 10 250 70 332 132 L332 ' + (yb + 8) + ' Z'} fill="#fff" stroke={PEN_N} strokeWidth="1.8" strokeLinejoin="round"/>
      <line x1="12" x2="328" y1={yb} y2={yb} stroke={PEN_N} strokeWidth="2.4"/>
      {SPS9_STR.map((m, i) => { const x = x0 + i * dx, on = shake[i] != null;
        const a = Math.min(4, 0.035 * (yb - top(i))), my = (top(i) + yb) / 2;   // a sounding string: the shape it shakes between, a blur
        return <g key={m}>{on ? <g className="sps9-ring"><path d={'M' + x + ' ' + top(i) + ' Q' + (x - 2 * a) + ' ' + my + ' ' + x + ' ' + yb} fill="none" stroke={PEN_C} strokeWidth={sw(i)}/><path d={'M' + x + ' ' + top(i) + ' Q' + (x + 2 * a) + ' ' + my + ' ' + x + ' ' + yb} fill="none" stroke={PEN_C} strokeWidth={sw(i)}/></g>
            : <line x1={x} x2={x} y1={top(i)} y2={yb} stroke={PEN_N} strokeWidth={sw(i)}/>}
          <circle cx={x} cy={top(i)} r="1.6" fill={PEN_N}/></g>; })}
      {spsTx(40, 172, t('long: low', '길다: 낮다'), { size: 12 })}{spsTx(300, 172, t('short: high', '짧다: 높다'), { size: 12 })}
    </svg>
  </div>;
}

// ── step 4, the pedals: two octaves and the three pedals. Right pedal down: the notes ring on and blend; let it up: they
// stop. Left: softer. Middle (on most grands): only the notes you were holding when you pressed it ring on ──
function SpsPedalPlay() {
  const [sus, setSus] = useState(false), [soft, setSoft] = useState(false), [sost, setSost] = useState(false), [lit, setLit] = useState([]), [glow, setGlow] = useState([]);
  const V = useRef({}), held = useRef(new Set()), kept = useRef(new Set()), R = useRef({}); R.current = { sus, sost };
  const stopAll = () => { Object.values(V.current).forEach(v => { try { v.rel && v.rel(); } catch (e) {} clearTimeout(v.tm); }); V.current = {}; held.current.clear(); kept.current.clear(); setLit([]); setGlow([]); };
  useEffect(() => () => stopAll(), []);
  const sync = () => setGlow(Object.keys(V.current).map(Number));
  const end = (m) => { const v = V.current[m]; if (!v) return; try { v.rel && v.rel(); } catch (e) {} clearTimeout(v.tm); delete V.current[m]; sync(); };
  function down(m, vel) { const ctx = getAudio(); if (!ctx) return; end(m);
    const rel = blip(ctx, ctx.currentTime + 0.005, mFreq(m), 5.5, (soft ? 0.09 : 0.2) * (0.6 + 0.6 * vel), 'triangle');
    V.current[m] = { rel, tm: setTimeout(() => { delete V.current[m]; sync(); }, 5600) }; held.current.add(m); setLit([...held.current]); sync(); }
  function up(m) { if (!held.current.has(m)) return; held.current.delete(m); setLit([...held.current]); if (!R.current.sus && !kept.current.has(m)) end(m); }
  function tap(p) {
    if (p === 'soft') { setSoft(x => !x); return; }
    if (p === 'sustain') { const nx = !sus; setSus(nx); if (!nx) Object.keys(V.current).map(Number).forEach(m => { if (!held.current.has(m) && !kept.current.has(m)) end(m); }); return; }
    const nx = !sost; setSost(nx);
    if (nx) kept.current = new Set(held.current); else { const was = kept.current; kept.current = new Set(); if (!sus) [...was].forEach(m => { if (!held.current.has(m)) end(m); }); }
  }
  const status = sus ? t('Right pedal down: every damper is up, so the notes ring on and blend. Let it up: they stop.', '오른쪽 페달을 밟으면 댐퍼가 모두 올라가요: 소리가 계속 울리며 섞여요. 떼면 멈춰요.')
    : sost ? t('Middle pedal (on most grands): only the notes you were holding when you pressed it ring on.', '가운데 페달(대부분의 그랜드): 밟을 때 누르고 있던 음만 계속 울려요.')
    : soft ? t('Left pedal: softer. Now each note still stops when you let go.', '왼쪽 페달: 더 여리게. 손을 떼면 음은 그대로 멈춰요.')
    : t('No pedal: each note stops when you let go. Press a pedal, then play.', '페달 없음: 손을 떼면 음이 멈춰요. 페달을 밟고 쳐 봐요.');
  return <div className="try-box" style={sps9Box} data-sps9="pedals">
    <div style={actTitle}>{t('Pedal playground', '페달 놀이터')}</div>
    <div style={actNote}>{t('Tap a pedal to press it down, tap it again to let it up. Play a few notes with the right pedal down, then let it up.', '페달을 한 번 누르면 밟고, 다시 누르면 떼요. 오른쪽 페달을 밟은 채 몇 음 쳐 보고, 페달을 떼 봐요.')}</div>
    <div style={{maxWidth:460,margin:'0 auto'}}><Sps9Keys lo={60} hi={83} lit={lit} glow={glow} onDown={down} onUp={up}/></div>
    <div style={{maxWidth:300,margin:'6px auto 0'}} data-sps9-pedals><SpsPedals down={[soft && 'soft', sost && 'middle', sus && 'sustain'].filter(Boolean)} onTap={tap} short size={15}/></div>
    <div style={{fontSize:14,color:BK.ink,lineHeight:1.5,margin:'4px auto 0',maxWidth:460,minHeight:42,textAlign:'center',fontWeight:700}} data-sps9-status>{status}</div>
  </div>;
}

// ── step 5, grand and upright: all 88 keys in one strip. Slide along them, bottom to top: every C you pass lights up ──
const SPS9_CS = [24, 36, 48, 60, 72, 84, 96, 108];
function SpsSlide88() {
  const whites = [], blacks = []; let w = 0;
  for (let m = 21; m <= 108; m++) { if (SPS9_WK(m)) { whites.push({ m, x: w }); w++; } else blacks.push({ m, x: w }); }
  const KW = 340 / w, H = 74, BH = 46;
  const [cs, setCs] = useState([]), [cur, setCur] = useState(null), last = useRef(null);
  const keyAt = (e) => { const r = e.currentTarget.getBoundingClientRect(), x = (e.clientX - r.left) / r.width * 340, y = (e.clientY - r.top) / r.height * (H + 18);
    if (y < BH) { const b = blacks.find(k => Math.abs(x - k.x * KW) < KW * 0.34); if (b) return b.m; }
    const wi = Math.max(0, Math.min(w - 1, Math.floor(x / KW))); return whites[wi].m; };
  function hit(m) { if (m === last.current) return; last.current = m; const ctx = getAudio(); if (!ctx) return;
    blip(ctx, ctx.currentTime + 0.005, mFreq(m), 0.7, 0.17, 'triangle'); setCur(m); if (m % 12 === 0) setCs(c => (c.includes(m) ? c : c.concat(m))); }
  const name = (m) => m === 21 ? t('A: the lowest key', 'A: 가장 낮은 건반') : m === 108 ? t('C: the highest key', 'C: 가장 높은 건반') : m === 60 ? t('C: middle C', 'C: 가운데 도') : ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'][m % 12];
  return <div className="try-box" style={sps9Box} data-sps9="slide">
    <div style={actTitle}>{t('Slide along all 88', '88건반 미끄럼틀')}</div>
    <div style={actNote}>{t('Put a finger on the lowest key and slide all the way to the top. Every C you pass lights up: how many are there?', '가장 낮은 건반에 손가락을 대고 맨 위까지 쭉 미끄러져 봐요. 지나가는 C마다 불이 켜져요: 모두 몇 개일까요?')}</div>
    <svg viewBox={'-1 -1 342 ' + (H + 20)} style={{width:'100%',display:'block',touchAction:'none',userSelect:'none',cursor:'pointer'}}
      onPointerDown={(e) => { e.preventDefault(); try { e.currentTarget.setPointerCapture(e.pointerId); } catch (x) {} last.current = null; hit(keyAt(e)); }}
      onPointerMove={(e) => { if (e.buttons || e.pointerType === 'touch') { if (last.current != null) hit(keyAt(e)); } }} onPointerUp={() => { last.current = null; }} onPointerCancel={() => { last.current = null; }}>
      {whites.map(k => <rect key={k.m} x={k.x * KW} y="0" width={KW} height={H} fill={cur === k.m ? PEN_C : cs.includes(k.m) ? '#f6b9a6' : '#fff'} stroke={PEN_N} strokeWidth="0.6"/>)}
      {blacks.map(k => <rect key={k.m} x={k.x * KW - KW * 0.32} y="0" width={KW * 0.64} height={BH} fill={cur === k.m ? PEN_C : PEN_N}/>)}
      <rect x="0" y="0" width={w * KW} height={H} fill="none" stroke={PEN_N} strokeWidth="1.4"/>
      {SPS9_CS.map(m => { const k = whites.find(x => x.m === m); return <text key={m} x={k.x * KW + KW / 2} y={H + 13} textAnchor="middle" fontSize="9.5" fontWeight="900" fill={cs.includes(m) ? PEN_C : BK.muted}>C</text>; })}
    </svg>
    <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:PEN_N,minHeight:24,marginTop:6}} data-sps9-cs>
      {cur == null ? '' : name(cur)}{cs.length ? <span style={{color:PEN_C}}>{'  ·  ' + (cs.length === 8 ? t('all 8 Cs!', 'C 8개 모두!') : t(cs.length + ' C' + (cs.length > 1 ? 's' : '') + ' so far', '지금까지 C ' + cs.length + '개'))}</span> : null}
    </div>
    {cs.length > 0 && spsRow(<button className="ghost-btn" style={SPS_TAP} onClick={() => { setCs([]); setCur(null); }}>{t('Start again', '다시 하기')}</button>)}
  </div>;
}
const SPS9_AT = { 0: SpsTimeKeys, 2: SpsStringHarp, 3: SpsPedalPlay, 4: SpsSlide88 };
const STEP_PLAY = { 'piano-story': SPS9_AT };   // Build DX: a free-play toy in a step, under its own pad
