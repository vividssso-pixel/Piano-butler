// ─── Phase 376: the six warm-ups of the Lesson Book's page 3, moving ───
// Each card is the book's card (same picture, same words). Tap the picture and that drawing moves: the same child
// in the same pen and ink, joint by joint. At rest each scene is exactly the book's picture (phase null).
const pLerp = (a, b, k) => [a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k];
function pLerpJ(A, B, k) {
  return { hip: pLerp(A.hip, B.hip, k), neck: pLerp(A.neck, B.neck, k), head: pLerp(A.head, B.head, k),
    arms: A.arms.map((ch, i) => ch.map((q, n) => pLerp(q, B.arms[i][n] || q, k))), legs: A.legs.map((ch, i) => ch.map((q, n) => pLerp(q, B.legs[i][n] || q, k))) };
}
const pEase = (k) => k < 0 ? 0 : k > 1 ? 1 : k * k * (3 - 2 * k);
// the joints dict moved/turned as one piece (turn around o by ang radians, then shift by d)
function pMoveJ(J, o, ang, d) {
  const c = Math.cos(ang), s = Math.sin(ang), f = (q) => [o[0] + (q[0] - o[0]) * c - (q[1] - o[1]) * s + d[0], o[1] + (q[0] - o[0]) * s + (q[1] - o[1]) * c + d[1]];
  return { hip: f(J.hip), neck: f(J.neck), head: f(J.head), arms: J.arms.map(ch => ch.map(f)), legs: J.legs.map(ch => ch.map(f)) };
}
const pQuad = (a, c, b, k) => { const u = 1 - k; return [u * u * a[0] + 2 * u * k * c[0] + k * k * b[0], u * u * a[1] + 2 * u * k * c[1] + k * k * b[1]]; };
const penPoly = (pts, w, c = PEN_N) => ({ k: 'pl', p: pts, s: c, w });
const penCurve = (seg, w, c, extra) => ({ k: 'pa', seg, f: 'none', s: c, w, ...extra });

// 1. rag doll: flop and shake, rise, float the hands up, flop again (the girl)
const WU_RAG = { hip: [70, 104], neck: [90, 72], head: [100, 63], arms: [[[89, 75], [90, 97], [89, 117], [89, 123]], [[85, 77], [84, 99], [83, 119]]], legs: [[[72, 104], [73, 131], [74, 157]], [[68, 104], [66, 131], [64, 157]]] };
const WU_RAG_UP = { hip: [70, 104], neck: [73, 63], head: [75, 49], arms: [[[75, 66], [80, 86], [100, 88], [107, 92]], [[71, 66], [75, 87], [95, 89], [101, 93]]], legs: WU_RAG.legs };
function wuRagdoll(ph, who) {
  let J = WU_RAG, marks = true;
  if (ph != null) {
    if (ph < 0.42) { const w = Math.sin(ph / 0.42 * Math.PI * 6) * 5;
      J = { ...WU_RAG, arms: WU_RAG.arms.map(ch => ch.map((q, n) => n === 0 ? q : [q[0] + w * (n / 3), q[1] - Math.abs(w) * 0.15 * n])) }; }
    else if (ph < 0.66) { J = pLerpJ(WU_RAG, WU_RAG_UP, pEase((ph - 0.42) / 0.24)); marks = false; }
    else if (ph < 0.84) { J = WU_RAG_UP; marks = false; }
    else { J = pLerpJ(WU_RAG_UP, WU_RAG, pEase((ph - 0.84) / 0.16)); marks = false; }
  }
  const s = [...penFloor(150), ...penKid(J, 1, who)];
  if (marks) s.push(penPoly([[80, 128], [76, 132], [80, 136], [76, 140]], 1.6, PEN_C), penPoly([[98, 128], [102, 132], [98, 136], [102, 140]], 1.6, PEN_C));
  if (ph != null && ph >= 0.6 && ph < 0.9) s.push(...penKeyrow(96, 95, 4, 9.5, 8).map(e => ({ ...e, op: 0.9 })));
  return s;
}
// 2. elbow wings: the hands rest; the elbows float in, out like wings, and stop in the middle (the girl, from the front)
const WU_WINGS = { hip: [75, 106], neck: [75, 64], head: [75, 49], arms: [[[84, 67], [104, 76], [92, 90], [87, 92]], [[66, 67], [46, 76], [58, 90], [63, 92]]], legs: [[[79, 106], [80, 132], [81, 157]], [[71, 106], [70, 132], [69, 157]]] };
function wuWings(ph, who) {
  let out = 1;   // 0 = stuck to the body, 1 = wings out (the book's picture), 0.55 = the middle
  if (ph != null) out = ph < 0.25 ? 1 - pEase(ph / 0.25) : ph < 0.5 ? pEase((ph - 0.25) / 0.25) : ph < 0.65 ? 1 : ph < 0.85 ? 1 - 0.45 * pEase((ph - 0.65) / 0.2) : 0.55;
  const el = (sx) => [75 + sx * (13 + 16 * out), 88 - 12 * out];
  const J = { ...WU_WINGS, arms: [[WU_WINGS.arms[0][0], el(1), WU_WINGS.arms[0][2], WU_WINGS.arms[0][3]], [WU_WINGS.arms[1][0], el(-1), WU_WINGS.arms[1][2], WU_WINGS.arms[1][3]]] };
  const s = [...penFloor(150), ...penKid(J, 0, who)];
  if (ph == null || out > 0.9) s.push(penCurve([['M', [108, 66]], ['Q', [113, 70], [112, 78]], ['M', [112, 62]], ['Q', [120, 68], [118, 80]], ['M', [42, 66]], ['Q', [37, 70], [38, 78]], ['M', [38, 62]], ['Q', [30, 68], [32, 80]]], 1.6, PEN_C));
  if (ph != null && ph >= 0.85) s.push(penLine([86, 88], [75 + 13 + 16 * out - 4, 82], 1.4, PEN_C, '2.5 2.5'), penLine([64, 88], [75 - 13 - 16 * out + 4, 82], 1.4, PEN_C, '2.5 2.5'));
  s.push(penCurve([['M', [112, 24]], ['Q', [118, 18], [124, 24]], ['Q', [130, 18], [136, 24]]], 2, PEN_N));
  return s;
}
// 3. arm glide: the boy skates along the keys; the round hand rides on the arm (the fingers don't walk)
const WU_GLIDE = { hip: [64, 100], neck: [74, 60], head: [79, 46], arms: [[[76, 64], [98, 74], [120, 75], [127, 79]], [[72, 64], [56, 78], [44, 90]]], legs: [[[66, 100], [82, 120], [84, 140]], [[62, 100], [48, 119], [34, 133]]] };
function wuSkate(ank, ang) {
  const c = Math.cos(ang), s = Math.sin(ang), m = [c, s, -s, c, ank[0], ank[1]];
  return [{ k: 'rc', x: -8, y: -2, w: 17, h: 6, rx: 3, f: PEN_N, m }, { k: 'el', c: [-5, 7], rx: 3, ry: 3, f: PEN_C, m }, { k: 'el', c: [6, 7], rx: 3, ry: 3, f: PEN_C, m }];
}
function wuGlide(ph, who) {
  let J = WU_GLIDE, dx = 0, st = 0;
  if (ph != null) { dx = 46 * (0.5 - 0.5 * Math.cos(ph * Math.PI * 2)); st = Math.sin(ph * Math.PI * 4);
    const legA = [[66, 100], [74 + 8 * st, 120], [70 + 14 * st, 140]], legB = [[62, 100], [56 - 8 * st, 120], [48 - 14 * st, 136 + 3 * Math.abs(st)]];
    J = { ...WU_GLIDE, legs: st >= 0 ? [legA, legB] : [legB.map(q => q), legA] };
    J = pMoveJ(J, [0, 0], 0, [dx, 0]); }
  const s = [penLine([6, 152], [214, 152], 1.6, '#bdb7a6'), ...penKeyrow(112, 80, 10)];
  if (ph == null || Math.abs(Math.sin(ph * Math.PI * 2)) > 0.3) [[8, 60], [14, 72], [8, 84]].forEach(([x, y]) => s.push(penLine([x + dx * 0.6, y], [x + 18 + dx * 0.6, y], 1.8)));
  s.push(...penKid(J, 1, who));
  if (ph == null) s.push(...wuSkate([84.5, 140], 0), ...wuSkate([34.5, 133], -22 * Math.PI / 180));
  else J.legs.forEach(lg => { const a = lg[2]; s.push(...wuSkate([a[0] + 0.5, a[1]], a[1] < 138 ? -18 * Math.PI / 180 : 0)); });
  return s;
}
// 4. arm drop: the girl dives off the board along the dashed arc into the water -- splash (the arm drops into the key)
function wuDivePose() {
  const dv = [0.62, 0.78], pp = [-dv[1], dv[0]], hip = [96, 60], nk = pAdd(hip, dv, 36), hd = pAdd(nk, dv, 13);
  const A = (b, k1, k2) => pAdd(pAdd(b, dv, k1), pp, k2);
  return { hip, neck: nk, head: hd,
    arms: [[pAdd(nk, pp, 3), A(nk, 20, 5), A(nk, 38, 4), A(nk, 44, 4)], [pAdd(nk, pp, -3), A(nk, 20, -2), A(nk, 38, -1), A(nk, 44, -1)]],
    legs: [[pAdd(hip, pp, 3), A(hip, -24, 4), A(hip, -46, 4)], [pAdd(hip, pp, -3), A(hip, -24, -3), A(hip, -46, -6)]] };
}
const WU_DIVE = wuDivePose();
function wuDive(ph, who) {
  let J = WU_DIVE, under = false, splash = 1;
  if (ph != null) {
    const k = Math.min(1, ph / 0.62), at = pQuad([62, 50], [94, 12], [150, 128], pEase(k) * 0.82 + k * 0.18), ang = (-38 + 58 * k) * Math.PI / 180;
    J = pMoveJ(WU_DIVE, WU_DIVE.hip, ang, pSub(at, WU_DIVE.hip));
    under = ph > 0.45; splash = ph < 0.5 ? 0 : ph < 0.62 ? (ph - 0.5) / 0.12 : ph < 0.85 ? 1 : 1 - (ph - 0.85) / 0.15;
    if (ph >= 0.62) J = null;
  }
  const s = [{ k: 'rc', x: 6, y: 70, w: 62, h: 7, rx: 2, f: PEN_P, s: PEN_N, sw: 2.6 }, penLine([18, 77], [18, 162], 2.6), penLine([6, 162], [214, 162], 1.6, '#bdb7a6'),
    penCurve([['M', [64, 60]], ['Q', [92, 24], [124, 64]]], 1.4, PEN_N, { dash: '3 5', op: 0.6 })];
  if (J) s.push(...penKid(J, 1, who));
  if (under) s.push({ k: 'rc', x: 86, y: 143, w: 134, h: 29, rx: 0, f: BK.soft }, penLine([86, 162], [214, 162], 1.6, '#bdb7a6'));   // the water hides her (the card's own paper colour)
  const wave = [['M', [90, 142]]]; for (let i = 0; i < 6; i++) wave.push(['Q', [100 + i * 20, i % 2 ? 149 : 135], [110 + i * 20, 142]]);
  s.push(penCurve(wave, 2.4, PEN_N));
  if (splash > 0) [[156, 130, 3.2], [166, 122, 2.6], [146, 123, 2.4], [174, 132, 2], [138, 133, 2]].forEach(([x, y, r]) => s.push({ k: 'el', c: [156 + (x - 156) * (0.4 + 0.6 * splash), 142 + (y - 142) * splash], rx: r * Math.max(0.3, splash), ry: r * Math.max(0.3, splash), f: PEN_C }));
  return s;
}
// 5. knuckle bridge: a little car drives over the knuckles; the bridge stays up (the hand from the side)
function wuBridge(ph) {
  const car = ph == null ? 0 : ph < 0.7 ? -1 + 2 * pEase(ph / 0.7) : 1;
  return penHandSide([80, 55, 24, -3, -2], { labels: false, faults: false, car: ph != null && ph >= 0.85 ? null : car, press: ph != null && ph > 0.3 && ph < 0.7 ? 2 : 0 }).shapes;
}
// 6. wrist balloon: the key goes down, and a balloon lifts the wrist straight back up to level (the boy)
const WU_BAL = { hip: [80, 106], neck: [80, 64], head: [82, 50], arms: [[[82, 67], [103, 86], [124, 80], [130, 102]], [[78, 68], [74, 88], [75, 106]]], legs: [[[82, 106], [85, 132], [87, 157]], [[78, 106], [74, 132], [71, 157]]] };
function wuBalloon(ph, who) {
  let dip = 0, press = 0;
  if (ph != null) { dip = ph < 0.18 ? pEase(ph / 0.18) * 8 : ph < 0.5 ? 8 * (1 - pEase((ph - 0.18) / 0.32)) : 0; press = ph < 0.5 ? 1.6 : 0; }
  const wr = [124, 80 + dip], el = [103, 86 + dip * 0.45];
  const J = { ...WU_BAL, arms: [[WU_BAL.arms[0][0], el, wr, [130, 102 + press]], WU_BAL.arms[1]] };
  const by = 25 + (ph == null ? 0 : Math.sin(ph * Math.PI * 2) * 2 + dip * 0.6);
  const s = [...penFloor(220), ...penKeyrow(112, 104, 8)];
  if (press) s.push({ k: 'rc', x: 126.5, y: 104 + press, w: 9.5, h: 10, rx: 0, f: PEN_P, s: PEN_N, sw: 1.6 });
  s.push(penCurve([['M', wr], ['C', [wr[0] + 6, wr[1] - 22], [148, by + 25], [151, by + 15]]], 1.6, PEN_N),
    { k: 'el', c: [153, by], rx: 13, ry: 16, f: PEN_C }, { k: 'pa', seg: [['M', [150, by + 16]], ['L', [153, by + 12]], ['L', [156, by + 16]], ['Z']], f: PEN_C },
    { k: 'el', c: [148, by - 6], rx: 3, ry: 5, f: '#fff', op: 0.45 });
  s.push(...penKid(J, 1, who));
  return s;
}
const WARM_UPS = [
  { id: 'ragdoll', who: 'girl', vb: [0, 0, 150, 172], ms: 4200, f: wuRagdoll },
  { id: 'wings', who: 'girl', vb: [0, 0, 150, 172], ms: 3600, f: wuWings },
  { id: 'glide', who: 'boy', vb: [0, 0, 220, 160], ms: 4400, f: wuGlide },
  { id: 'dive', who: 'girl', vb: [0, 0, 220, 172], ms: 2600, f: wuDive },
  { id: 'bridge', who: '', vb: [34, 26, 258, 126], ms: 3000, f: wuBridge },
  { id: 'balloon', who: 'boy', vb: [0, 0, 220, 172], ms: 3200, f: wuBalloon },
];
// plays one scene for a few rounds, then comes back to the book's still picture
function useWarmPlay(ms, rounds, on, onEnd) {
  const [ph, setPh] = useState(null);
  useEffect(() => {
    if (!on) { setPh(null); return; }
    let raf, t0 = null;
    const step = (ts) => { if (t0 == null) t0 = ts; const k = (ts - t0) / ms; if (k >= rounds) { setPh(null); onEnd && onEnd(); return; } setPh(k % 1); raf = requestAnimationFrame(step); };
    raf = requestAnimationFrame(step);
    return () => cancelAnimationFrame(raf);
  }, [on]);
  return ph;
}
function WarmPic({ w, playing, onEnd, h }) {
  const ph = useWarmPlay(w.ms, 2, playing, onEnd);
  const who = penWho(w.who);
  const shapes = useMemo(() => w.f(ph, who), [ph, who]);
  return <PenArt shapes={shapes} vb={w.vb} style={{height:h,width:'auto',maxWidth:'100%'}}/>;
}
function WarmUps376({ cards }) {
  const [on, setOn] = useState(-1);
  const [all, setAll] = useState(false);
  const next = (i) => { if (all && i < WARM_UPS.length - 1) setOn(i + 1); else { setOn(-1); setAll(false); } };
  return (
    <div data-warmups>
      <div style={{display:'flex',justifyContent:'flex-end',marginBottom:8}}>
        <button className="ghost-btn" style={{padding:'5px 12px',fontWeight:800,fontSize:13}} onClick={() => { if (on >= 0) { setOn(-1); setAll(false); } else { setAll(true); setOn(0); } }}>{on >= 0 ? t('■ Stop', '■ 멈추기') : t('▶ Watch all six, in order', '▶ 여섯 가지를 순서대로 보기')}</button>
      </div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill, minmax(min(100%, 170px), 1fr))',gap:14}}>
        {WARM_UPS.map((w, i) => { const [name, how] = cards[i]; return (
          <div key={w.id} data-warm={w.id} style={{border:'1px solid ' + (on === i ? BK.coral : '#ece6d8'),borderRadius:12,padding:'8px 10px 10px',display:'flex',flexDirection:'column',gap:5,transition:'border-color 0.2s'}}>
            <button onClick={() => { setAll(false); setOn(on === i ? -1 : i); }} aria-pressed={on === i} aria-label={t('Watch it move: ', '움직이는 모습 보기: ') + name}
              style={{position:'relative',background:BK.soft,border:'none',borderRadius:8,height:150,display:'flex',alignItems:'center',justifyContent:'center',overflow:'hidden',padding:0,cursor:'pointer'}}>
              <WarmPic w={w} playing={on === i} onEnd={() => next(i)} h={134}/>
              {on !== i && <span aria-hidden="true" style={{position:'absolute',right:6,bottom:6,width:26,height:26,borderRadius:13,background:'#fff',border:'1.5px solid ' + BK.ink,color:BK.ink,fontSize:11,display:'flex',alignItems:'center',justifyContent:'center',paddingLeft:2}}>▶</span>}
            </button>
            <div style={{display:'flex',alignItems:'center',gap:7}}>
              <span style={{flex:'0 0 22px',height:22,borderRadius:11,background:on === i ? BK.coral : BK.ink,color:'#fff',fontWeight:900,fontSize:12.5,display:'flex',alignItems:'center',justifyContent:'center'}}>{i + 1}</span>
              <span style={{fontFamily:LB_SERIF,fontSize:16.5,fontWeight:800,color:BK.ink}}>{name}</span>
            </div>
            <div style={{fontSize:13.5,color:BK.ink,lineHeight:1.4}}>{how}</div>
          </div>); })}
      </div>
    </div>
  );
}
