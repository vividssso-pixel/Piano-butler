// ─── Phase 376: "Set up the stool", drawn as the Lesson Book draws it (page 2), and moving ───
// The same boy on the same stool as the book's picture, in the book's coordinates (stool 46-100 at y 114, keys at
// y 98). Height moves the stool up and down, distance moves it in and out; the hands stay on the keys, so the
// elbows bend to fit (two-bone reach), and the feet reach the floor or swing. A footstool fixes swinging feet.
// The checks are the book's: feet flat; forearm level with the keys; elbows just in front of you, away from your body.
function PenArt({ shapes, vb, shift, label, style, who, inter }) {   // inter: the drawing has its own buttons inside (no img role)
  const id = useMemo(() => 'penh' + (++PEN_UID), []);
  const html = useMemo(() => penSvg(shapes, { vb, shift, id }).replace('<svg ', '<svg width="100%" height="100%" '), [shapes, vb, shift, id]);
  const w = vb ? vb[2] : 220, h = vb ? vb[3] : 172;
  return <div role={label && !inter ? 'img' : undefined} aria-label={inter ? undefined : label} aria-hidden={label || inter ? undefined : true} style={{lineHeight:0,aspectRatio:w + ' / ' + h,width:'100%',...style}} dangerouslySetInnerHTML={{__html: html}}/>;
}
const penWho = (dflt) => (typeof PB_KID !== 'undefined' && PB_KID) || dflt;
function penReach(sh, tg, U, L) {
  const dx = tg[0] - sh[0], dy = tg[1] - sh[1], d = Math.hypot(dx, dy);
  if (d >= U + L - 0.3) return { el: [sh[0] + dx / d * U, sh[1] + dy / d * U], wr: [sh[0] + dx / d * (U + L), sh[1] + dy / d * (U + L)], straight: true };
  const a = (U * U - L * L + d * d) / (2 * d), h = Math.sqrt(Math.max(0, U * U - a * a)), mx = sh[0] + a * dx / d, my = sh[1] + a * dy / d;
  const e1 = [mx + h * dy / d, my - h * dx / d], e2 = [mx - h * dy / d, my + h * dx / d];
  return { el: e1[1] > e2[1] ? e1 : e2, wr: tg, straight: false };
}
// seatY: the stool's top; x2: its front edge; up: a footstool under the feet
function sitPose376(seatY, x2, up) {
  const hip = [x2 - 24, seatY - 4], r = (dx, dy) => [hip[0] + dx, hip[1] + dy], floorY = up ? 143 : 155;
  const sh0 = r(7, -39), sh1 = r(3, -38);
  const a0 = penReach(sh0, [121, 92], 25, 23.02), a1 = penReach(sh1, [116, 94], 25.24, 23.02);
  const leg = (h, k, shin) => { const drop = floorY - k[1]; return drop <= shin + 0.01 ? { ch: [h, k, [k[0] + Math.sqrt(Math.max(0, shin * shin - drop * drop)), floorY]], down: true } : { ch: [h, k, [k[0] + 3, k[1] + shin]], down: false }; };
  const l0 = leg(r(2, 0), r(32, 1), 44), l1 = leg(r(-3, 1), r(25, 3), 42);
  const arm = (sh, A, hv) => A.straight ? [sh, A.el, A.wr] : [sh, A.el, A.wr, [A.wr[0] + hv[0], A.wr[1] + hv[1]]];
  const J = { hip, neck: r(5, -42), head: r(8, -57), arms: [arm(sh0, a0, [7, 6]), arm(sh1, a1, [7, 5])], legs: [l0.ch, l1.ch] };
  return { J, feet: l0.down && l1.down, straight: a0.straight, slope: Math.atan2(a0.wr[1] - a0.el[1], a0.wr[0] - a0.el[0]) * 180 / Math.PI,
    ahead: a0.el[0] - sh0[0], steep: Math.atan2(a0.wr[1] - sh0[1], a0.wr[0] - sh0[0]) * 180 / Math.PI > 31, el: a0.el, wr: a0.wr };
}
function sitChecks376(p) {
  const reach = p.steep ? t('The arm has to stretch down to the keys -- lower the stool.', '팔을 아래로 쭉 뻗어야 건반에 닿아요 -- 의자를 낮춰요.')
    : t('The arm has to stretch out to the keys -- slide the stool closer.', '팔을 앞으로 쭉 뻗어야 건반에 닿아요 -- 의자를 더 가까이 옮겨요.');
  return [
    { id: 'feet', label: t('Feet flat on the floor', '발은 바닥에 평평하게'), ok: p.feet,
      fix: t('The feet can’t reach -- put a footstool or a sturdy box under them.', '발이 닿지 않아요 -- 발판이나 튼튼한 상자를 발밑에 놓아요.') },
    { id: 'level', label: t('Forearm level with the keys', '팔뚝이 건반과 수평'), ok: !p.straight && p.slope > -8 && p.slope < 12,
      fix: p.straight ? reach : p.slope <= -8 ? t('The elbows are below the keys, so the hands reach up -- raise the stool.', '팔꿈치가 건반보다 낮아서 손이 위로 뻗어요 -- 의자를 높여요.')
        : t('The elbows are too high, so the wrists drop to the keys -- lower the stool.', '팔꿈치가 너무 높아서 손목이 건반으로 떨어져요 -- 의자를 낮춰요.') },
    { id: 'ahead', label: t('Elbows just in front of you, away from your body', '팔꿈치는 몸 바로 앞에, 몸에서 떨어지게'), ok: !p.straight && p.ahead >= 8 && p.ahead <= 18,
      fix: p.straight ? reach : p.ahead < 8 ? t('The elbows are squashed in against the body -- slide the stool back.', '팔꿈치가 몸에 눌려 있어요 -- 의자를 뒤로 빼요.')
        : t('The arms reach out ahead of the body -- slide the stool closer.', '팔이 몸 앞으로 멀리 뻗어 있어요 -- 의자를 더 가까이 옮겨요.') },
  ];
}
function penSitShapes(seatY, x2, up, checks) {
  const p = sitPose376(seatY, x2, up), bad = (id) => !checks.find(c => c.id === id).ok;
  const s = [...penFloor(220), ...penKeyLevel(122, t('key level', '건반 높이')), ...penPiano()];
  if (up) s.push({ k: 'rc', x: 102, y: 150, w: 40, h: 12, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2 });
  // the figure moves with the stool; reading its wobble from where it sits keeps its lines steady while it slides
  const shift = [x2 - 100, seatY - 114];
  s.push({ k: 'g', shift, kids: penStool(x2 - 54, x2, seatY) });
  s.push({ k: 'g', shift, kids: [...penKid(p.J, 1, penWho('boy')), ...penJoints(p.J, [bad('level') || bad('ahead') ? 'elbow' : '', bad('level') ? 'wrist' : '', bad('feet') ? 'ankle' : ''].filter(Boolean), ['shoulder', 'hip', 'knee'])] });
  // labels as in the book (elbow above and to the right, wrist above it); the elbow's word stays a line above the wrist's
  // (an elbow squashed back behind the shoulder gets its word on the left, behind the back, so it never sits on the face)
  const lab = (tx, ty, from, to, txt, anchor) => [{ ...penText(tx, ty, txt, { anchor }), halo: true }, { k: 'pa', seg: [['M', from], ['L', to]], f: 'none', s: PEN_C, w: 1.2 }];
  const wy = p.wr[1] - 12, ey = Math.min(p.el[1] - 19, wy - 9), back = p.J.hip[0] - 15;
  if (p.ahead < 6) s.push(...lab(back - 3, p.el[1] + 3, [back - 1, p.el[1]], [p.el[0] - 4, p.el[1]], t('elbow', '팔꿈치'), 'end'));
  else s.push(...lab(p.el[0] + 7, ey, [p.el[0] + 6, ey - 2], [p.el[0] + 1.5, p.el[1] - 4.5], t('elbow', '팔꿈치')));
  s.push(...lab(p.wr[0] + 5, wy, [p.wr[0] + 4.5, wy - 1.5], [p.wr[0] + 2, p.wr[1] - 6], t('wrist', '손목')));
  return s;
}
// the front view: elbows a fist away from the body (the girl, as on the Lesson Book's warm-ups page)
function penFrontShapes(gap, ok) {
  const cx = 75, ex = 2 + gap * 22;
  const j = { hip: [cx, 106], neck: [cx, 64], head: [cx, 49],
    arms: [[[cx + 9, 67], [cx + 9 + ex, 89], [cx + 13, 99], [cx + 10, 105]], [[cx - 9, 67], [cx - 9 - ex, 89], [cx - 13, 99], [cx - 10, 105]]],
    legs: [[[cx + 4, 106], [cx + 5, 132], [cx + 6, 157]], [[cx - 4, 106], [cx - 5, 132], [cx - 6, 157]]] };
  const s = [...penFloor(150), ...penKid(j, 0, penWho('girl'))];
  s.push({ k: 'rc', x: 8, y: 102, w: 134, h: 60, rx: 2, f: PEN_P, s: PEN_N, sw: 2.4 });          // the piano, in front of the lap
  s.push({ k: 'rc', x: 8, y: 102, w: 134, h: 10, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2 });
  for (let i = 1; i < 14; i++) s.push(penLine([8 + i * 134 / 14, 102], [8 + i * 134 / 14, 112], 1.1));
  [1, -1].forEach(sx => {
    s.push(...penLimbPair([[cx + sx * 13, 99], [cx + sx * 10, 105]]));                               // the hands, on the keys
    const side = cx + sx * 11, el = cx + sx * (9 + ex);
    s.push(penLine([side, 89], [el - sx * 4, 89], 1.4, ok ? PEN_N : PEN_C, '2.5 2.5'));
    s.push({ k: 'el', c: [el, 89], rx: 3.2, ry: 3.2, f: ok ? PEN_P : PEN_C, s: PEN_N, w: 1.3 });
  });
  return s;
}
const penLimbPair = (ch) => [{ k: 'pl', p: ch, s: PEN_N, w: 6.8 }, { k: 'pl', p: ch, s: PEN_P, w: 3.6 }];
const SIT_PRESETS_376 = [
  { id: 'good', get label() { return t('Just right', '딱 좋아요'); }, y: 114, x: 100 },
  { id: 'low', get label() { return t('Stool too low', '의자가 너무 낮아요'); }, y: 124, x: 100 },
  { id: 'high', get label() { return t('Stool too high', '의자가 너무 높아요'); }, y: 106, x: 100 },
  { id: 'close', get label() { return t('Too close', '너무 가까워요'); }, y: 114, x: 124 },
  { id: 'far', get label() { return t('Too far', '너무 멀어요'); }, y: 114, x: 90 },
];
function SitCheck() {
  const [seatY, setSeatY] = useState(124);
  const [x2, setX2] = useState(100);
  const [up, setUp] = useState(false);
  const [view, setView] = useState('side');
  const [gap, setGap] = useState(0.05);
  const p = sitPose376(seatY, x2, up), checks = sitChecks376(p), allOk = checks.every(c => c.ok);
  const gapOk = gap >= 0.3 && gap <= 0.65;
  const side = useMemo(() => penSitShapes(seatY, x2, up, checks), [seatY, x2, up, LANG]);
  const front = useMemo(() => penFrontShapes(gap, gapOk), [gap]);
  const lab = {fontSize:13,fontWeight:800,color:'var(--navy)'};
  return (
    <div className="try-box" data-pen-sit style={actBox}>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',flexWrap:'wrap',gap:4}}>
        <div style={actTitle}>{t('Set up the stool', '의자 맞추기')}</div>
        <div style={{display:'flex',gap:3}}>{[['side', t('Side view', '옆에서')], ['front', t('Front view', '앞에서')]].map(([k, l]) => <button key={k} className={'chip' + (view === k ? ' active' : '')} style={{padding:'2px 9px',fontSize:12}} onClick={() => setView(k)}>{l}</button>)}</div>
      </div>
      {view === 'side' ? <>
        <div style={actNote}>{LANG === 'ko' ? <>모든 확인이 맞을 때까지 의자를 옮겨 봐요. <b>높이</b>는 팔뚝을(건반과 수평), <b>거리</b>는 팔꿈치를(몸 바로 앞) 정해요.</> : <>Move the stool until every check is right. The <b>height</b> sets the forearm (level with the keys); the <b>distance</b> sets the elbows (just in front of you).</>}</div>
        <div style={{display:'flex',gap:4,flexWrap:'wrap',marginBottom:6}}>{SIT_PRESETS_376.map(q => <button key={q.id} className={'chip' + (q.y === seatY && q.x === x2 ? ' active' : '')} style={{padding:'2px 8px',fontSize:12}} onClick={() => { setSeatY(q.y); setX2(q.x); }}>{q.label}</button>)}</div>
        <div style={{background:'#faf6ec',borderRadius:12,padding:'6px 4px'}}><PenArt shapes={side} label={t('A child at the piano, seen from the side', '옆에서 본, 피아노 앞에 앉은 아이')} style={{maxWidth:460,margin:'0 auto'}}/></div>
        <div style={{display:'grid',gridTemplateColumns:'auto 1fr',gap:'4px 10px',alignItems:'center',margin:'8px 0 6px'}}>
          <label htmlFor="pen-sit-h" style={lab}>{t('Height', '높이')}</label><input id="pen-sit-h" type="range" min="0" max="30" value={130 - seatY} onChange={e => setSeatY(130 - +e.target.value)} style={{accentColor:'#e4572e'}}/>
          <label htmlFor="pen-sit-d" style={lab}>{t('Distance', '거리')}</label><input id="pen-sit-d" type="range" min="0" max="44" value={132 - x2} onChange={e => setX2(132 - +e.target.value)} style={{accentColor:'#e4572e'}}/>
        </div>
        <label style={{display:'inline-flex',alignItems:'center',gap:7,fontSize:13,fontWeight:700,margin:'0 0 6px',cursor:'pointer'}}><input type="checkbox" checked={up} onChange={e => setUp(e.target.checked)} style={{accentColor:'#26296b',width:16,height:16}}/>{t('Footstool under the feet', '발밑에 발판 놓기')}</label>
        <div style={{display:'flex',flexDirection:'column',gap:3}}>
          {checks.map(c => (
            <div key={c.id} data-check={c.id} data-ok={c.ok ? '1' : '0'} style={{display:'flex',gap:7,alignItems:'flex-start',background:'#faf6ec',borderRadius:8,padding:'5px 8px',fontSize:13.5}}>
              <span style={{fontWeight:900,color:c.ok ? POS_GOOD : POS_BAD,width:14}}>{c.ok ? '✓' : '✗'}</span>
              <span><b>{c.label}</b>{!c.ok && <span style={{color:'#6d6f9c'}}> -- {c.fix}</span>}</span>
            </div>
          ))}
        </div>
        {allOk && <div style={{textAlign:'center',fontWeight:900,color:POS_GOOD,marginTop:6}}>{t('That’s the set-up. Remember this stool height for next time!', '바로 이 자세예요. 다음에도 이 의자 높이를 기억해요!')}</div>}
      </> : <>
        <div style={actNote}>{LANG === 'ko' ? <>앞에서 보면 팔꿈치는 몸에서 <b>주먹 하나만큼</b> 떨어져 있어요. 그래야 팔이 손을 건반 위로 데려갈 수 있어요. 몸에 붙이면 팔이 움직이지 못하고, 너무 벌리면 어깨가 긴장해요.</> : <>From the front, the elbows sit <b>about a fist away</b> from the body, so the arm can carry the hand along the keys. Stuck to the body, the arm can’t move; flapping out, the shoulders tense.</>}</div>
        <div style={{background:'#faf6ec',borderRadius:12,padding:'6px 4px'}}><PenArt shapes={front} vb={[0, 20, 150, 146]} label={t('A child at the piano, seen from the front', '앞에서 본, 피아노 앞에 앉은 아이')} style={{maxWidth:320,margin:'0 auto'}}/></div>
        <input type="range" aria-label={t('Elbows', '팔꿈치')} min="0" max="100" value={Math.round(gap * 100)} onChange={e => setGap(+e.target.value / 100)} style={{width:'100%',accentColor:'#e4572e',marginTop:6}}/>
        <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:gapOk ? POS_GOOD : POS_BAD}}>{gap < 0.3 ? t('✗ Elbows stuck to the body', '✗ 팔꿈치가 몸에 붙었어요') : gap > 0.65 ? t('✗ Chicken wings -- the shoulders lift and tense', '✗ 닭 날개 -- 어깨가 들리고 긴장해요') : t('✓ Elbows away from the body -- room for a fist', '✓ 팔꿈치가 몸에서 떨어졌어요 -- 주먹 하나만큼')}</div>
        <div style={{fontSize:13,color:'#6d6f9c',marginTop:6,background:'#faf6ec',borderRadius:8,padding:'6px 8px'}}>{LANG === 'ko' ? <><b>해 봐요:</b> 팔꿈치와 옆구리 사이에 주먹을 넣었다가 빼고, 그 공간을 그대로 두어요.</> : <><b>Try:</b> put a fist between your elbow and your side, then take it away and keep the space.</>}</div>
      </>}
    </div>
  );
}
