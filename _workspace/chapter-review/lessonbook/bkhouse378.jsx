// ─── Phase 378: the house in the books ───
// A small house (one line per floor, every room with its number and short name, your chapter's room in coral) takes
// the place of "The whole path" list; the Workbook's opening pages get the whole house to colour in, a room per chapter.
function houseMiniShapes(current, W = 600) {
  const s = [], X0 = 4, HW = W - 8, SC = 120, FH = 19, ROOF = 26, TOP = ROOF + 4;
  const stages = PATH_STAGES.map((st, i) => ({ st, i, ids: pathStageIds(st) }));
  let n = 0; const nums = {}; stages.forEach(x => x.ids.forEach(id => { nums[id] = ++n; }));
  s.push({ k: 'pa', seg: [['M', [X0, TOP]], ['L', [X0 + 26, TOP - ROOF + 4]], ['L', [X0 + HW - 26, TOP - ROOF + 4]], ['L', [X0 + HW, TOP]], ['Z']], f: 'H@0.7', s: PEN_N, w: 2 });
  const cx = W / 2; s.push({ k: 'rc', x: cx - 58, y: TOP - ROOF + 7, w: 116, h: 15, rx: 4, f: PEN_P, s: PEN_N, sw: 1.4 }, penText(cx, TOP - ROOF + 18, 'Piano Butler', { size: 10, weight: 700, fill: PEN_N, anchor: 'middle', serif: true, italic: true }));
  let y = TOP;
  [...stages].reverse().forEach(x => {
    const has = x.ids.includes(current), rw = (HW - SC) / x.ids.length;
    s.push({ k: 'rc', x: X0, y, w: HW, h: FH, rx: 0, f: PEN_P, s: PEN_N, sw: 1.4 }, penLine([X0 + SC, y], [X0 + SC, y + FH], 1.2));
    s.push(penText(X0 + 6, y + 13, (x.i + 1) + ' · ' + x.st.en[0], { size: 10, weight: 800, fill: has ? PEN_C : PEN_N, serif: true }));
    x.ids.forEach((id, j) => {
      const rx = X0 + SC + j * rw, on = id === current;
      if (j) s.push(penLine([rx, y], [rx, y + FH], 1));
      if (on) s.push({ k: 'rc', x: rx + 1.2, y: y + 1.2, w: rw - 2.4, h: FH - 2.4, rx: 0, f: '#fde9e1' });
      const nm = (CH_SHORT[id] || [bkChapterName(id)])[0];
      s.push(penText(rx + 5, y + 13, nums[id] + ' ' + nm, { size: 9.5, weight: on ? 800 : 600, fill: on ? PEN_C : PEN_N }));
    });
    y += FH;
  });
  s.push(penLine([0, y + 1.5], [W, y + 1.5], 1.4));
  return { shapes: s, W, H: y + 6 };
}
function BkHouse({ current, compact }) {
  const h = useMemo(() => houseMiniShapes(current), [current]);
  return (
    <div data-bk-house style={{border:'1.5px solid ' + BK.line,borderRadius:12,padding:compact ? '8px 12px 6px' : '10px 14px 8px'}}>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',marginBottom:4}}><div style={bkH(compact ? 15 : 17, 4)}>The Piano Butler’s house</div><span style={{fontSize:10.5,color:BK.muted}}>every floor a stage, every room a chapter -- the same order as the app</span></div>
      <PenArt shapes={h.shapes} vb={[0, 0, h.W, h.H]} label="The Piano Butler’s house: the chapter map"/>
    </div>
  );
}
// the whole house to colour in (the Workbook's opening pages)
function BkHousePage() {
  const stages = PATH_STAGES.map((s, i) => { const ids = pathStageIds(s); return { s, i, ids, st: ids.map(() => 'print') }; });
  const nums = {}; stages.flatMap(x => x.ids).forEach((id, k) => { nums[id] = k + 1; });
  const house = useMemo(() => houseShapes({ stages, here: null, nums, print: true }, true), []);
  return <>
    <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em',marginTop:4}}>YOUR MAP</div>
    <h1 style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:32,fontWeight:900,color:BK.ink,margin:'2px 0 4px',lineHeight:1.05}}>The Piano Butler’s house</h1>
    <p style={{fontSize:13.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Every floor is a stage and every room is a chapter, from the front door up to the attic. When you finish a chapter, <b style={{color:BK.ink}}>colour in its room</b>. Draw yourself on the stairs of the floor you are on.</p>
    <div style={{flex:1,minHeight:0,display:'flex',alignItems:'center',justifyContent:'center'}}><PenArt shapes={house.shapes} vb={[0, 0, house.W, house.H]} label="The Piano Butler’s house" style={{maxHeight:'100%'}}/></div>
  </>;
}
