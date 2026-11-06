// ─── Chapter 4: Reading the Staff (chapter 'staff') -- APPLIED (Phase 405) ───
// v4 (Sohyun 2026-10-09 evening): her characters (King A, Clara A, Queen A); the hand staff is her real lesson activity
// (the kebab test is out); page 3 goes up AND down; page 6 shows where the written C attaches (no fold here -- folding
// waits for chapter 5's three Cs); the landmarks page moves to chapter 5. v2: five notes first -- this chapter reads only the ten notes between the King's F and the Queen's G,
// five each side of Princess Clara (middle C); the whole staff and her rhymes go to a new chapter 5 (The Whole Staff),
// ledger lines to chapter 6. Middle C stands on a little ladder rung (the word 'ledger line' waits for its chapter).
// The chapter teaches the concept only (Phase 399: no songs in a chapter). Built on Sohyun's own clef story (Phase 101c):
// the treble clef began as a G and its curl wraps the Queen's line (G above middle C); the bass clef began as an F and its
// two dots are the King's guards around his line (F below middle C); the two palaces mirror each other round middle C.
// New in this draft (B questions): Princess Clara lives on middle C (chapter 3's Clara at C; middle C is the ground from
// chapter 2), the staff is shown as shapes before names (lines and spaces, steps and skips), and landmarks come before rhymes.
// Ledger lines beyond middle C's own short line wait for chapter 6; sharps and flats for chapter 7.

// the royal family, her picks from Royals-new-looks (Phase 404): King A, Clara A, Queen A
const SF_LAV = '#dcd9ea';
function qnCrown(P, k, s) {   // the Queen's tall crown: five points with pearls, a jewelled band
  s.push({ k: 'pa', seg: [['M', P(-6.6, -7.6)], ['L', P(-8, -16.6)], ['L', P(-4.6, -12.2)], ['L', P(-2.6, -18.4)], ['L', P(0, -13)], ['L', P(2.6, -18.4)], ['L', P(4.6, -12.2)], ['L', P(8, -16.6)], ['L', P(6.6, -7.6)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });
  [[-8, -16.6], [-2.6, -18.4], [2.6, -18.4], [8, -16.6]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 1.1 * k, ry: 1.1 * k, f: PEN_P, s: PEN_N, w: 0.7 }));
  s.push(penLine(P(-6.8, -9.6), P(6.8, -9.6), 1));
  s.push({ k: 'el', c: P(0, -8.5), rx: 1.3 * k, ry: 1 * k, f: PEN_N });   // a dark jewel in the middle
}
function qnFace(P, k, s) {
  s.push({ k: 'el', c: P(-2.5, 0.2), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.5, 0.2), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'pa', seg: [['M', P(-1.7, 3.6)], ['Q', P(0, 5.2), P(1.7, 3.6)], ['Q', P(0, 4.2), P(-1.7, 3.6)], ['Z']], f: PEN_C, s: PEN_C, w: 0.6 });   // coral lips
  s.push({ k: 'el', c: P(-5.9, 2.9), rx: 0.95 * k, ry: 1.2 * k, f: PEN_P, s: PEN_N, w: 0.7 }, { k: 'el', c: P(5.9, 2.9), rx: 0.95 * k, ry: 1.2 * k, f: PEN_P, s: PEN_N, w: 0.7 });   // pearl earrings, at the jaw
}
function sfQueen(cx, cy, k = 1) {   // Phase 404, her pick (Queen A): hair up, a high lace collar, pearl earrings, a tall crown, a coral gown with a pearl necklace
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-11.8, 15)], ['Q', P(-11, 8.4), P(0, 8.8)], ['Q', P(11, 8.4), P(11.8, 15)], ['Z']], f: PEN_C, s: PEN_N, w: 1.5 });   // gown
  s.push({ k: 'pa', seg: [['M', P(-5.2, 9.4)], ['Q', P(0, 12.6), P(5.2, 9.4)], ['Q', P(0, 10.2), P(-5.2, 9.4)], ['Z']], f: PEN_P, s: PEN_N, w: 1 });   // a scalloped lace collar at the neckline
  [[-3.6, 10.6], [-1.2, 11.4], [1.2, 11.4], [3.6, 10.6]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.95 * k, ry: 0.95 * k, f: PEN_P, s: PEN_N, w: 0.5 }));   // necklace
  s.push({ k: 'el', c: P(0, -0.4), rx: 6.6 * k, ry: 7.6 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.8, 0.4)], ['Q', P(-8.4, -9.4), P(0, -9.8)], ['Q', P(8.4, -9.4), P(6.8, 0.4)], ['Q', P(6, -5.4), P(1.6, -6.4)], ['Q', P(-1, -4.6), P(-3.6, -5.6)], ['Q', P(-6, -5), P(-6.8, 0.4)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });   // swept-up hair
  qnFace(P, k, s); qnCrown(P, k, s);
  return s.map(e => ({ ...e, ch: true }));
}
function sfKing(cx, cy, k = 1) {   // Phase 404, her pick (King A): a white beard and moustache, bushy brows, a crown with a cross and jewels, an ermine collar
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-11.5, 15)], ['Q', P(-10.5, 8.4), P(0, 8.6)], ['Q', P(10.5, 8.4), P(11.5, 15)], ['Z']], f: PEN_N, s: PEN_N, w: 1.5 });   // robe
  s.push({ k: 'pa', seg: [['M', P(-10.4, 10.6)], ['Q', P(0, 14.4), P(10.4, 10.6)], ['L', P(11, 13.2)], ['Q', P(0, 17), P(-11, 13.2)], ['Z']], f: PEN_P, s: PEN_N, w: 1 });   // ermine collar
  [[-7, 12.4], [-2.4, 13.9], [2.4, 13.9], [7, 12.4]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.7 * k, ry: 1 * k, f: PEN_N }));
  s.push({ k: 'el', c: P(0, -1), rx: 6.8 * k, ry: 7.4 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.6, 0.6)], ['Q', P(-7.2, 10.6), P(0, 11.8)], ['Q', P(7.2, 10.6), P(6.6, 0.6)], ['Q', P(5.4, 6.4), P(2.4, 6.6)], ['Q', P(0, 8), P(-2.4, 6.6)], ['Q', P(-5.4, 6.4), P(-6.6, 0.6)], ['Z']], f: SF_LAV, s: PEN_N, w: 1.1 });   // white beard, the mouth showing
  s.push({ k: 'pa', seg: [['M', P(0, 3.6)], ['Q', P(-2.8, 2.2), P(-5, 4.2)], ['Q', P(-2.4, 5.6), P(0, 4.6)], ['Q', P(2.4, 5.6), P(5, 4.2)], ['Q', P(2.8, 2.2), P(0, 3.6)], ['Z']], f: SF_LAV, s: PEN_N, w: 0.9 });   // moustache
  s.push(penCurve([['M', P(-1.4, 6.4)], ['Q', P(0, 7.2), P(1.4, 6.4)]], 1, PEN_N));
  s.push(penCurve([['M', P(-4.4, -3.4)], ['Q', P(-2.6, -4.6), P(-1, -3.6)]], 1.6, PEN_N), penCurve([['M', P(1, -3.6)], ['Q', P(2.6, -4.6), P(4.4, -3.4)]], 1.6, PEN_N));   // brows
  s.push({ k: 'el', c: P(-2.6, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.6, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'pa', seg: [['M', P(-7.2, -6.2)], ['L', P(-7.4, -14)], ['L', P(-3.6, -10.6)], ['L', P(0, -15.2)], ['L', P(3.6, -10.6)], ['L', P(7.4, -14)], ['L', P(7.2, -6.2)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });   // crown
  s.push(penLine(P(-7.2, -8.2), P(7.2, -8.2), 1));
  [[-4.4, -7.2], [0, -7.2], [4.4, -7.2]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.9 * k, ry: 0.9 * k, f: PEN_P, s: PEN_N, w: 0.5 }));
  s.push(penLine(P(0, -15.2), P(0, -19.2), 1.4), penLine(P(-1.8, -17.3), P(1.8, -17.3), 1.4));   // the cross on top
  return s.map(e => ({ ...e, ch: true }));
}
function sfClara(cx, cy, k = 1) {   // Phase 404, her pick (Clara A): two braids down to her shoulders with coral bows at the ends, a small tiara, a collar
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-10, 14.6)], ['Q', P(-9.4, 8.2), P(0, 8)], ['Q', P(9.4, 8.2), P(10, 14.6)], ['Z']], f: '#fbe9e2', s: PEN_N, w: 1.5 });   // dress
  [-1, 1].forEach(sx => {   // braids: three little loops down each side, a bow at the end
    [[6.6, 2.6], [7.4, 6], [7.8, 9.4]].forEach(([a, b]) => s.push({ k: 'el', c: P(a * sx, b), rx: 2.1 * k, ry: 2 * k, f: PEN_N, s: PEN_N, w: 0.9 }));
    s.push({ k: 'pa', seg: [['M', P(7.9 * sx, 11.6)], ['L', P(5.2 * sx, 10.2)], ['L', P(5.4 * sx, 13.6)], ['Z'], ['M', P(7.9 * sx, 11.6)], ['L', P(10.6 * sx, 10.2)], ['L', P(10.4 * sx, 13.6)], ['Z']], f: PEN_C, s: PEN_N, w: 0.8 });
  });
  s.push(penCurve([['M', P(-3.6, 8.1)], ['Q', P(0, 11.2), P(3.6, 8.1)]], 1.7, PEN_C));   // collar
  s.push({ k: 'el', c: P(0, -0.4), rx: 6.3 * k, ry: 7 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.6, 1.2)], ['Q', P(-7.1, -8.3), P(0, -8.4)], ['Q', P(7.1, -8.3), P(6.6, 1.2)], ['Q', P(5.6, -4.6), P(0.8, -5.4)], ['Q', P(-1.2, -3.6), P(-3.2, -4.6)], ['Q', P(-5.6, -4), P(-6.6, 1.2)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });   // hair, side part
  s.push({ k: 'pa', seg: [['M', P(-3.8, -7.6)], ['L', P(-3.2, -10.2)], ['L', P(-1.5, -8.8)], ['L', P(0, -11.6)], ['L', P(1.5, -8.8)], ['L', P(3.2, -10.2)], ['L', P(3.8, -7.6)], ['Z']], f: PEN_C, s: PEN_N, w: 1 });   // tiara
  s.push({ k: 'el', c: P(0, -8.9), rx: 0.9 * k, ry: 0.9 * k, f: PEN_P });
  s.push({ k: 'el', c: P(-2.4, 0.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.4, 0.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'el', c: P(-4, 2.6), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' }, { k: 'el', c: P(4, 2.6), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' });
  s.push(penCurve([['M', P(-1.8, 3.4)], ['Q', P(0, 5), P(1.8, 3.4)]], 1.1, PEN_N));
  return s.map(e => ({ ...e, ch: true }));
}
// a staff in the book's two inks: straight lines, the clefs from the music font, open note heads, labels, pen icons
// notes: [{ d, x, staff, color, label, lx, ly, lc, ls }]; extra(yOf, layer) draws more (arrows, numbers); icons: [{ shapes, x, y, k, vb }]
function SfStaff({ clef = 'treble', width = 340, notes = [], gap = 44, pad = [26, 26], extra, icons = [], label, span }) {
  const [lx1, lx2] = span || [4, width - 4];
  const grand = clef === 'grand', none = clef === 'none';
  const staves = grand ? ['treble', 'bass'] : [none ? 'treble' : clef];
  const yOf = (d, st) => dY(d) + (grand && st === 'bass' ? gap : 0);
  const staffOf = (n) => n.staff || (grand ? (n.d >= 28 ? 'treble' : 'bass') : staves[0]);
  const ys = []; staves.forEach(st => ys.push(yOf(CLEFS[st].high, st), yOf(CLEFS[st].low, st)));
  notes.forEach(n => ys.push(yOf(n.d, staffOf(n))));
  const y0 = Math.min(...ys) - pad[0], y1 = Math.max(...ys) + pad[1];
  const inner = (shapes, vb) => { const s = penSvg(shapes, { vb }); return s.slice(s.indexOf('>') + 1, s.lastIndexOf('</svg>')); };
  const icn = useMemo(() => icons.map(ic => inner(ic.shapes, ic.vb || [0, 0, 44, 44])), [icons]);
  const txt = { fontFamily: "Inter, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif", paintOrder: 'stroke', stroke: BK.soft, strokeWidth: 3.5, strokeLinejoin: 'round' };
  return (
    <svg viewBox={`0 ${y0} ${width} ${y1 - y0}`} role="img" aria-label={label} style={{width:'100%',display:'block'}}>
      {extra && extra(yOf, 'under', txt)}
      {staves.map(st => CLEFS[st].lines.map(l => <line key={st + l} x1={lx1} x2={lx2} y1={yOf(l, st)} y2={yOf(l, st)} stroke={BK.ink} strokeOpacity="0.75" strokeWidth="1.3"/>))}
      {grand && <line x1="4" x2="4" y1={yOf(38, 'treble')} y2={yOf(18, 'bass')} stroke={BK.ink} strokeWidth="1.8"/>}
      {!none && staves.map(st => <ClefGlyph key={'c' + st} clef={st} st={st} yOf={yOf} ink={BK.ink}/>)}
      {notes.map((n, i) => { const st = staffOf(n), y = yOf(n.d, st), x = n.x, c = n.color || BK.ink; return <g key={i}>
        {ledgersFor(n.d, CLEFS[st].low, CLEFS[st].high).map(p => <line key={p} x1={x - 12} x2={x + 12} y1={yOf(p, st)} y2={yOf(p, st)} stroke={BK.ink} strokeWidth="1.4"/>)}
        <ellipse cx={x} cy={y} rx="7.4" ry="5.2" fill={c}/><ellipse cx={x} cy={y} rx="3.4" ry="2.7" transform={`rotate(-38 ${x} ${y})`} fill="#fff"/>
        {(n.d - CLEFS[st].low) % 2 === 0 && <line x1={x - 4} x2={x + 4} y1={y} y2={y} stroke={BK.ink} strokeOpacity="0.75" strokeWidth="1.3"/>/* a line note: the line shows through its hole (Sohyun B4) */}
        {n.label && <text x={x + (n.lx || 0)} y={y + (n.ly != null ? n.ly : 19)} textAnchor={n.la || 'middle'} fontSize={n.ls || 9.5} fontWeight="900" fill={n.lc || c} style={txt}>{n.label}</text>}
      </g>; })}
      {extra && extra(yOf, 'over', txt)}
      {icons.map((ic, i) => <g key={'i' + i} transform={`translate(${ic.x} ${ic.y}) scale(${ic.k || 1})`} dangerouslySetInnerHTML={{__html: icn[i]}}/>)}
    </svg>
  );
}
const sfArrowHead = (x, y, dir, c) => <path d={`M${x - 6 * dir} ${y - 4} L${x} ${y} L${x - 6 * dir} ${y + 4}`} fill="none" stroke={c} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"/>;
const sfHop = (x1, x2, y, h, c = BK.coral) => <g><path d={`M${x1} ${y} Q${(x1 + x2) / 2} ${y - h} ${x2} ${y}`} fill="none" stroke={c} strokeWidth="1.7"/><path d={`M${x2 - 5.5 * Math.sign(x2 - x1)} ${y - 5} L${x2} ${y} L${x2 - 7 * Math.sign(x2 - x1)} ${y + 1}`} fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round"/></g>;
const SF_ICON = (shapes, x, y, k = 1) => ({ shapes, x, y, k });


function sfLbPages(scr = false) {
  const ch = 'staff';
  const queen = sfQueen(22, 24, 1), king = sfKing(22, 24, 1), clara = sfClara(22, 24, 1);
  const turtle = [...fsTurtle(22, 26, 0.8), ...fsWaves(2, 36, 40, 0.8, 3)], bird = [...fsBird(22, 26, 1), ...fsCloud(10, 12, 0.6)];
  // letters (and a word) under or over a row of notes, on one baseline
  const rowLabels = (items, y, wordDy) => (yOf, layer, txt) => layer === 'over' && <g style={txt}>{items.map(([x, letter, word, coral], i) => <g key={i}>
    <text x={x} y={y(yOf)} fontSize={coral ? 12 : 10.5} fontWeight="900" fill={coral ? BK.coral : BK.ink} textAnchor="middle">{letter}</text>
    {word && <text x={x} y={y(yOf) + wordDy} fontSize="8.2" fontWeight="900" fill={coral ? BK.coral : BK.muted} textAnchor="middle">{word}</text>}</g>)}</g>;

  // p1 (v3, Sohyun n2 + "minimal"): the royal family on the keyboard first -- no staff, no clefs yet. The King low, the
  // Queen high, Princess Clara on middle C; the turtle's sea on the low side, the bird's sky on the high side (chapter 2).
  const art1 = (() => {
    const X = 56, W = 16.4, s1 = [];
    const K = fsKeysShapes(X, 44, 15, W, 60);
    s1.push(...K.shapes);
    const mcx = X + 7.5 * W;
    s1.push({ k: 'el', c: [mcx, 96], rx: 3.6, ry: 3.6, f: PEN_C, nw: true });
    s1.push(...sfKing(24, 22, 1), ...sfClara(mcx, 23, 0.95), ...sfQueen(352, 22, 1));
    s1.push({ ...penText(24, 52, t('the King', '왕'), { size: 9, weight: 900, fill: PEN_N, anchor: 'middle' }), halo: true });
    s1.push({ ...penText(24, 63, t('sings low', '낮은 목소리'), { size: 8, weight: 800, fill: '#6d6f9c', anchor: 'middle' }), halo: true });
    s1.push({ ...penText(352, 52, t('the Queen', '여왕'), { size: 9, weight: 900, fill: PEN_N, anchor: 'middle' }), halo: true });
    s1.push({ ...penText(352, 63, t('sings high', '높은 목소리'), { size: 8, weight: 800, fill: '#6d6f9c', anchor: 'middle' }), halo: true });
    s1.push({ ...penText(mcx, 116, t('Princess Clara · middle C', '클라라 공주 · 가운데 도'), { size: 9, weight: 900, fill: PEN_C, anchor: 'middle' }), halo: true });
    return s1;
  })();
  const p1 = <PenArt shapes={art1} vb={[0, -4, 376, 128]} label={t('The piano: the King stands at the low end, the Queen at the high end, and Princess Clara in the middle, on middle C', '피아노: 낮은 쪽 끝에 왕, 높은 쪽 끝에 여왕, 그리고 한가운데, 가운데 도 위에 클라라 공주')}/>;
  // p2 (B4): the staff, lines and spaces numbered from the bottom; two magnifiers show a line note (the line runs through its
  // middle) and a space note (it fills the space and touches the lines above and below)
  const mag = (cx, cy, r, line, id) => <g>
    <defs><clipPath id={id}><circle cx={cx} cy={cy} r={r}/></clipPath></defs>
    <circle cx={cx} cy={cy} r={r} fill="#fffdf7"/>
    <g clipPath={`url(#${id})`}>{(line ? [-24, 0, 24] : [-12, 12]).map(o => <line key={o} x1={cx - r} x2={cx + r} y1={cy + o} y2={cy + o} stroke={BK.ink} strokeOpacity="0.75" strokeWidth="2.2"/>)}</g>
    <ellipse cx={cx} cy={cy} rx="17" ry="12" fill={BK.coral}/><ellipse cx={cx} cy={cy} rx="7.8" ry="6.2" transform={`rotate(-38 ${cx} ${cy})`} fill="#fff"/>
    {line && <line x1={cx - 9} x2={cx + 9} y1={cy} y2={cy} stroke={BK.ink} strokeOpacity="0.75" strokeWidth="2.2"/>}
    <circle cx={cx} cy={cy} r={r} fill="none" stroke={BK.ink} strokeWidth="1.6"/>
  </g>;
  const p2 = <SfStaff clef="none" width={320} span={[42, 278]} pad={[30, 132]} label={t('The staff, lines numbered 1 to 5 from the bottom and spaces 1 to 4; under it, two magnifiers: a line note with the line running through its middle, and a space note filling the space and touching the line above and the line below', '오선, 아래에서부터 1~5번 줄과 1~4번 칸; 그 아래 돋보기 둘: 줄이 한가운데를 지나는 줄 음표, 칸을 꽉 채워 위 줄과 아래 줄에 닿는 칸 음표')}
    notes={[{ d: 34, x: 100, color: PEN_C }, { d: 33, x: 220, color: PEN_C }]}
    extra={(yOf, layer, txt) => { if (layer !== 'over') return null; const cy = yOf(30) + 66, r = 38; return <g>
      {[[100, yOf(34)], [220, yOf(33)]].map(([x, y], i) => <g key={i}><circle cx={x} cy={y} r="11" fill="none" stroke={BK.ink} strokeWidth="1.2"/><line x1={x} x2={x} y1={y + 11} y2={cy - r} stroke={BK.ink} strokeWidth="1.2" strokeDasharray="3 3"/></g>)}
      {mag(100, cy, r, true, 'sf402m1')}{mag(220, cy, r, false, 'sf402m2')}
      <g style={txt}>
        {[30, 32, 34, 36, 38].map((d, i) => <text key={d} x="28" y={yOf(d) + 3.4} fontSize="9" fontWeight="900" fill={BK.ink} textAnchor="middle">{i + 1}</text>)}
        {[31, 33, 35, 37].map((d, i) => <text key={d} x="292" y={yOf(d) + 3.4} fontSize="9" fontWeight="900" fill={BK.coral} textAnchor="middle">{i + 1}</text>)}
        <text x="28" y={yOf(38) - 10} fontSize="8" fontWeight="800" fill={BK.ink} textAnchor="middle">{t('lines', '줄')}</text>
        <text x="292" y={yOf(38) - 10} fontSize="8" fontWeight="800" fill={BK.coral} textAnchor="middle">{t('spaces', '칸')}</text>
        <text x="100" y={cy + r + 15} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('a line note', '줄 음표')}</text>
        <text x="100" y={cy + r + 27} fontSize="8" fontWeight="700" fill={BK.ink} textAnchor="middle">{t('the line runs through it', '줄이 가운데를 지나요')}</text>
        <text x="220" y={cy + r + 15} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('a space note', '칸 음표')}</text>
        <text x="220" y={cy + r + 27} fontSize="8" fontWeight="700" fill={BK.ink} textAnchor="middle">{t('it touches both lines', '위아래 줄에 닿아요')}</text>
      </g></g>; }}/>;
  // p3: up the staff = up the piano, and back down (Sohyun v3 review: "내려가는건?") -- the steps climb a hill and
  // come down again; the skips go up; the arrow under it points both ways
  const p3 = <SfStaff clef="none" width={340} pad={[46, 44]} label={t('Notes on the staff: steps climb line, space, line, space to the top and walk back down; skips go line, line, line; the bird is up at the high end, the turtle down at the low end, and an arrow under the staff points both ways', '오선 위의 음표: 한 걸음은 줄, 칸, 줄, 칸 꼭대기까지 올라갔다가 다시 내려와요; 건너뛰기는 줄, 줄, 줄; 높은 쪽엔 새, 낮은 쪽엔 거북이, 오선 아래 화살표는 양쪽을 가리켜요')}
    notes={[30, 31, 32, 33, 34, 33, 32].map((d, i) => ({ d, x: 56 + i * 21 })).concat([30, 32, 34, 36].map((d, i) => ({ d, x: 216 + i * 27, color: PEN_C })))}
    icons={[SF_ICON(bird, 300, 6, 0.85), SF_ICON(turtle, 0, 116, 0.75)]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <text x="119" y={yOf(38) - 14} fontSize="10" fontWeight="900" fill={BK.ink} textAnchor="middle">{t('steps: up... and down', '한 걸음: 위로... 그리고 아래로')}</text>
      <text x="257" y={yOf(38) - 14} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('skips: line, line, line', '건너뛰기: 줄, 줄, 줄')}</text>
      {[0, 1, 2].map(i => <g key={i}>{sfHop(216 + i * 27 + 3, 216 + (i + 1) * 27 - 3, yOf(32 + 2 * i) - 9, 11)}</g>)}
      <path d={`M64 ${yOf(30) + 24} L292 ${yOf(30) + 24}`} stroke={BK.coral} strokeWidth="1.8"/>{sfArrowHead(296, yOf(30) + 24, 1, BK.coral)}{sfArrowHead(60, yOf(30) + 24, -1, BK.coral)}
      <text x="178" y={yOf(30) + 37} fontSize="9" fontWeight="800" fill={BK.ink} textAnchor="middle">{t('up = higher, to the right · down = lower, to the left', '위로 = 높게, 오른쪽으로 · 아래로 = 낮게, 왼쪽으로')}</text>
    </g>}/>;
  // p4: the Queen's five -- C D E F G, from Clara up to the Queen's G; the curl wraps the second line
  const xs5 = [70, 126, 182, 238, 294];
  const p4 = <SfStaff clef="treble" width={340} pad={[50, 40]} label={t('The treble clef; its curl wraps the second line, the Queen\'s G line, in coral; five notes climb from middle C on its little ladder rung: C D E F G', '높은음자리표; 소용돌이가 감싸는 둘째 줄(여왕의 G 줄)이 산호색; 작은 사다리 발판 위의 가운데 도에서 다섯 음이 올라가요: C D E F G')}
    notes={[28, 29, 30, 31, 32].map((d, i) => ({ d, x: xs5[i], color: i === 4 || i === 0 ? PEN_C : undefined }))}
    icons={[SF_ICON(queen, 268, 10, 0.9), SF_ICON(clara, 28, 92, 0.72)]}
    extra={(yOf, layer, txt) => <g>{layer === 'under' && <line x1="36" x2="332" y1={yOf(32)} y2={yOf(32)} stroke={BK.coral} strokeOpacity="0.55" strokeWidth="3.4"/>}
      {rowLabels([[xs5[0], 'C', t('Clara', '클라라'), true], [xs5[1], 'D'], [xs5[2], 'E'], [xs5[3], 'F'], [xs5[4], 'G', t('the Queen\'s G', '여왕의 G'), true]], (yOf) => yOf(28) + 19, 12)(yOf, layer, txt)}</g>}/>;
  // p5: the King's five -- F G A B C, from the King's F up to Clara; the two dots guard the fourth line
  const p5 = <SfStaff clef="bass" width={340} pad={[56, 50]} label={t('The bass clef; its two dots guard the fourth line, the King\'s F line, in coral; five notes climb from the King\'s F to middle C on its little ladder rung: F G A B C', '낮은음자리표; 두 점이 지키는 넷째 줄(왕의 F 줄)이 산호색; 왕의 F에서 작은 사다리 발판 위의 가운데 도까지 다섯 음: F G A B C')}
    notes={[24, 25, 26, 27, 28].map((d, i) => ({ d, x: xs5[i], color: i === 0 || i === 4 ? PEN_C : undefined }))}
    icons={[SF_ICON(king, 51, 166, 0.9), SF_ICON(clara, 304, 94, 0.62)]}
    extra={(yOf, layer, txt) => <g>{layer === 'under' && <line x1="36" x2="332" y1={yOf(24)} y2={yOf(24)} stroke={BK.coral} strokeOpacity="0.55" strokeWidth="3.4"/>}
      {rowLabels([[xs5[0], 'F', t('the King\'s F', '왕의 F'), true], [xs5[1], 'G'], [xs5[2], 'A'], [xs5[3], 'B'], [xs5[4], 'C', t('Clara', '클라라'), true]], (yOf) => yOf(28) - 16, -12)(yOf, layer, txt)}</g>}/>;
  // p6 (v4): the grand staff; the written middle C attaches just under the Queen's staff or just over the King's --
  // two places on paper, one key. No folding here (Sohyun: the fold waits for chapter 5's three Cs).
  const p6 = <SfStaff clef="grand" width={340} pad={[26, 30]} label={t('The grand staff: middle C written twice on its little ladder rung, once just under the Queen\'s staff and once just over the King\'s, in the same column, joined by a dotted line saying they are the same key; Princess Clara stands by both', '큰보표: 작은 사다리 발판 위의 가운데 도가 두 번 써 있어요 -- 한 번은 여왕의 오선 바로 아래, 한 번은 왕의 오선 바로 위, 같은 세로줄에; 점선이 둘을 이으며 같은 건반이라고 말해요; 클라라 공주가 양쪽에 서 있어요')}
    notes={[{ d: 28, x: 96, staff: 'treble', color: PEN_C }, { d: 28, x: 96, staff: 'bass', color: PEN_C }]}
    icons={[SF_ICON(clara, 60, 96, 0.55), SF_ICON(clara, 60, 140, 0.55), SF_ICON(queen, 300, 50, 0.85), SF_ICON(king, 300, 140, 0.85)]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <line x1="96" x2="96" y1={yOf(28, 'treble') + 9} y2={yOf(28, 'bass') - 9} stroke={BK.coral} strokeWidth="1.4" strokeDasharray="4 3.5"/>
      <text x="108" y={(yOf(28, 'treble') + yOf(28, 'bass')) / 2 + 3.5} fontSize="9.5" fontWeight="900" fill={BK.coral} textAnchor="start">{t('the same key!', '같은 건반!')}</text>
      <text x="116" y={yOf(28, 'treble') + 3.5} fontSize="8.5" fontWeight="800" fill={BK.ink} textAnchor="start">{t("just under the Queen's staff", '여왕의 오선 바로 아래')}</text>
      <text x="116" y={yOf(28, 'bass') + 3.5} fontSize="8.5" fontWeight="800" fill={BK.ink} textAnchor="start">{t("just over the King's staff", '왕의 오선 바로 위')}</text>
    </g>}/>;

  const mini = (dots, extra = []) => { const s = []; for (let i = 0; i < 5; i++) s.push({ ...penLine([6, 8 + i * 6], [86, 8 + i * 6], 1.1), nw: true }); return [...s, ...dots.map(([x, y, c]) => ({ k: 'el', c: [x, y], rx: 4.4, ry: 3.1, f: c || PEN_N })), ...extra]; };
  const chkArts = {
    ls: mini([[34, 20, PEN_C], [58, 23, PEN_N]]),
    ss: mini([[20, 32], [32, 29], [44, 26]], [...nnHop(56, 76, 22, 6)].concat([{ k: 'el', c: [56, 26], rx: 4.4, ry: 3.1, f: PEN_C }, { k: 'el', c: [76, 20], rx: 4.4, ry: 3.1, f: PEN_C }])),
    queen: [...sfQueen(20, 22, 0.8), { ...penText(60, 28, 'C–G', { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    king: [...sfKing(20, 22, 0.8), { ...penText(60, 28, 'F–C', { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    clara: [...sfClara(24, 22, 0.8), { ...penText(62, 30, 'C', { size: 18, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
  };
  const checksRows = [
    ['ls', [0, 0, 92, 40], t('I can tell a line note from a space note, and count them from the bottom', '줄 음표와 칸 음표를 구별하고, 아래에서부터 셀 수 있어요')],
    ['ss', [0, 0, 92, 40], t('I can see a step or a skip on the staff, and play it', '오선에서 한 걸음과 건너뛰기를 보고 칠 수 있어요')],
    ['queen', [0, 0, 92, 40], t('I can read the Queen\'s five: C D E F G in the treble clef', '여왕의 다섯 음 C D E F G를 읽을 수 있어요')],
    ['king', [0, 0, 92, 40], t('I can read the King\'s five: F G A B C in the bass clef', '왕의 다섯 음 F G A B C를 읽을 수 있어요')],
    ['clara', [0, 0, 92, 40], t('I can find middle C on both staves -- attached up or down, the same key', '두 오선에서 가운데 도를 찾을 수 있어요 -- 위에 붙어도 아래에 붙어도 같은 건반')],
  ];
  const pic = (svg, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{svg}</div></LbPic>;

  return [
    // 1. opener (also the Workbook's map)
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Reading the Staff', '오선보 읽기')}</div>
      </div></LbOnly>
      {pic(p1, 220, 600)}
      <LbSay size={17.5}>{t('Meet the royal family of the keys. The King sings low, the Queen sings high, and Princess Clara lives between them on middle C. This chapter writes their notes down, so your eyes can read what your hands play.', '건반의 왕실 가족을 만나요. 왕은 낮은 목소리로, 여왕은 높은 목소리로 노래하고, 클라라 공주는 그 사이 가운데 도에 살아요. 이 챕터에서는 이들의 음을 종이에 써요 -- 손이 치는 것을 눈으로 읽을 수 있게요.')}</LbSay>
      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>
          {[[t('Lines and spaces', '줄과 칸'), 2], [t('Up the staff, up the piano', '오선 위로, 피아노 위로'), 3], [t('The Queen\'s five', '여왕의 다섯 음'), 4], [t('The King\'s five', '왕의 다섯 음'), 5], [t('Middle C: Princess Clara', '가운데 도: 클라라 공주'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid #ece6d8'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><b>{'page ' + p}</b></div>)}
        </div></LbOnly>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('tell a line note from a space note', '줄 음표와 칸 음표를 구별할 수 있어요'), t('see a step or a skip on the staff, and play it', '오선에서 한 걸음과 건너뛰기를 보고 칠 수 있어요'), t('read C D E F G in the treble clef', '높은음자리표에서 C D E F G를 읽을 수 있어요'), t('read F G A B C in the bass clef', '낮은음자리표에서 F G A B C를 읽을 수 있어요'), t('find middle C on both staves -- attached up or down, the same key', '두 오선에서 가운데 도를 찾을 수 있어요 -- 위에 붙어도 아래에 붙어도 같은 건반')].map((x, i) => <div key={i} style={{display:'flex',gap:8,fontSize:14.5,padding:'4px 0'}}><span style={{color:BK.coral,fontWeight:900}}>✓</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. lines and spaces
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Lines and spaces', '줄과 칸')}>
      {pic(p2, 210, 600)}
      <LbSay>{LANG === 'ko' ? <>오선에는 <b>줄 다섯 개</b>와 <b>칸 네 개</b>가 있어요. <b>아래에서부터</b> 세요: 1번 줄이 가장 낮고 5번 줄이 가장 높아요; 1번 칸은 1번 줄 바로 위예요. 음표는 모두 <b>줄 위</b>에 있거나 -- 줄이 음표 한가운데를 꿰뚫어요, 꼬치처럼 -- <b>칸 안</b>에 있어요: 칸을 꽉 채워서 위아래 줄에 닿아요, 샌드위치 속처럼.</>
        : <>The staff has <b>five lines</b> and <b>four spaces</b>. Count them <b>from the bottom</b>: line 1 is the lowest, line 5 the highest; space 1 sits just above line 1. Every note lives either <b>on a line</b> -- the line runs straight through its middle, like a kebab -- or <b>in a space</b>: it fills the space and touches the line above and the line below, like a sandwich filling.</>}</LbSay>
      <LbPiano title={t('Try it', '해 봐요')} steps={LANG === 'ko' ? [
        <><b>손 오선:</b> 한 손을 옆으로 눕혀 손가락을 벌려요: 손가락 5개 = 줄 5개, 손가락 사이 4개 = 칸 4개. 누가 짚으면 줄인지 칸인지, 몇 번인지 말해요.</>,
      ] : [
        <><b>The hand staff:</b> hold one hand out sideways, fingers spread: 5 fingers = 5 lines, the 4 gaps = 4 spaces. Someone touches one; say line or space, and which number.</>,
      ]}/>
      <LbRemember>{t('On a line: the line runs through it. In a space: it touches both lines.', '줄 위: 줄이 가운데를 지나요. 칸 안: 위아래 줄에 닿아요.')}</LbRemember>
    </LbPage>,

    // 3. up the staff, up the piano: steps and skips
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Up the staff, up the piano', '오선 위로, 피아노 위로')}>
      {pic(p3, 210, 680)}
      <LbSay>{LANG === 'ko' ? <>오선은 건반의 지도예요. 오선에서 <b>위</b>에 있는 음은 <b>높은 소리</b> -- 피아노에서 오른쪽, 하늘 위 새 쪽이에요. <b>아래</b>는 왼쪽, 바다 아래 거북이 쪽이에요. 줄에서 바로 위 칸으로 가면 <b>한 걸음</b>: 다음 글자, 다음 흰건반. 줄에서 다음 줄로(칸에서 다음 칸으로) 가면 <b>건너뛰기</b> -- 3챕터의 그 건너뛰기, 글자 하나를 넘어가요.</>
        : <>The staff is a map of the keys. A note <b>higher</b> on the staff sounds <b>higher</b> -- it is further to the right on the piano, up towards the bird; <b>lower</b> on the staff is further left, down towards the turtle. From a line to the very next space is a <b>step</b>: the next letter, the next white key. From a line to the next line -- or a space to the next space -- is a <b>skip</b>: the same skip as in Chapter 3, one letter jumped over.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>아무 흰건반에서 시작해 그림처럼 <b>한 걸음</b>으로 꼭대기까지 올라갔다가 <b>다시 내려와요</b> -- 매번 이웃 건반으로.</>,
        <>이번엔 <b>건너뛰기</b>: 줄, 줄, 줄 위로 -- 건반 하나씩 넘어가요. 그리고 건너뛰기로 다시 내려와요.</>,
      ] : [
        <>Start on any white key and play the picture's <b>steps</b>: up to the top of the hill and <b>back down</b> -- the next key each time.</>,
        <>Now the <b>skips</b>: line, line, line going up -- a key jumped over each time. Then skip your way back down.</>,
      ]}/>
      <LbRemember>{t('Line to space: a step. Line to line: a skip. Up or down.', '줄에서 칸: 한 걸음. 줄에서 줄: 건너뛰기. 위로도, 아래로도.')}</LbRemember>
    </LbPage>,

    // 4. the Queen's five (treble clef)
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The Queen\'s five', '여왕의 다섯 음')}>
      {pic(p4, 210, 680)}
      <LbSay>{LANG === 'ko' ? <>이 꼬불꼬불한 기호가 <b>높은음자리표</b>예요. 아주 옛날에는 그냥 글자 <b>G</b>였어요. 소용돌이가 아래에서 <b>둘째 줄</b>을 감싸는데, 그 줄이 <b>여왕의 집</b>이에요: 그 줄 위의 음은 모두 <b>G</b>. 여왕은 높은 목소리로 노래하고, 보통 <b>오른손</b>이 읽어요. 클라라 공주(가운데 도)에서 여왕의 G까지는 딱 <b>다섯 음</b>: C D E F G -- 공주는 오선 아래 작은 사다리 발판 위, D는 1번 줄 바로 아래, E는 1번 줄, F는 1번 칸, G는 여왕의 줄.</>
        : <>This curly sign is the <b>treble clef</b>. Long ago it was simply a letter <b>G</b>. Its curl wraps round the <b>second line</b> from the bottom, and that line is the <b>Queen's house</b>: every note on it is <b>G</b>. The Queen sings high, and usually the <b>right hand</b> reads her staff. From Princess Clara (middle C) up to the Queen's G is exactly <b>five notes</b>: C D E F G -- Clara on her little ladder rung under the staff, D just under line 1, E on line 1, F in space 1, G on the Queen's line.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손으로 <b>가운데 도</b>에서 <b>G</b>까지 걸어 올라가요: C D E F G -- 오선의 그림을 보면서, 글자를 말하면서.</>,
        <>누가 다섯 음 중 하나를 짚으면: 여왕의 G에서 세어 내려오거나, 공주의 C에서 세어 올라가 이름을 대고 쳐요.</>,
        <><b>여왕의 소용돌이 그리기:</b> 높은음자리표는 <b>G 줄에서 시작</b>해 밖으로 감아 나가요 -- 여왕의 집에서 출발! (워크북에 따라 그리는 쪽이 있어요.)</>,
      ] : [
        <>With your right hand, walk up from <b>middle C</b> to <b>G</b>: C D E F G -- looking at the staff picture, saying the letters.</>,
        <>Someone points to one of the five: count down from the Queen's G or up from Clara's C, name it, play it.</>,
        <><b>Draw the Queen's curl:</b> a treble clef <b>starts on the G line</b> and spirals out -- it begins at the Queen's house! (The Workbook has one to trace.)</>,
      ]}/>
      <LbRemember>{t('The curl wraps round G: the Queen\'s line. Clara to the Queen: C D E F G.', '소용돌이는 G를 감싸요: 여왕의 줄. 공주에서 여왕까지: C D E F G.')}</LbRemember>
    </LbPage>,

    // 5. the King's five (bass clef)
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The King\'s five', '왕의 다섯 음')}>
      {pic(p5, 220, 680)}
      <LbSay>{LANG === 'ko' ? <>이 기호는 <b>낮은음자리표</b>예요. 글자 <b>F</b>에서 시작했어요. 왕의 집은 아래에서 <b>넷째 줄</b>이고, 음자리표의 <b>두 점</b>이 경비병이에요 -- 하나는 왕의 줄 바로 위, 하나는 바로 아래. 두 경비병 사이의 줄이 <b>F</b>예요. 왕은 낮은 목소리로 노래하고, 보통 <b>왼손</b>이 읽어요. 왕의 F에서 공주까지도 딱 <b>다섯 음</b>: F G A B C -- F는 왕의 줄, G는 그 위 칸, A는 맨 윗줄, B는 그 위, C는 오선 위 작은 사다리 발판의 공주.</>
        : <>This sign is the <b>bass clef</b>. It began as a letter <b>F</b>. The King's house is the <b>fourth line</b> from the bottom, and the clef's <b>two dots</b> are his guards, one just above his line and one just below. The line between the guards is <b>F</b>. The King sings low, and usually the <b>left hand</b> reads his staff. From the King's F up to Princess Clara is <b>five notes</b> too: F G A B C -- F on the King's line, G in the space above, A on the top line, B just over it, and Clara on her little ladder rung above the staff.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>왼손으로 <b>가운데 도</b>에서 <b>F</b>까지 걸어 내려가요: C B A G F -- 그다음 F에서 다시 올라와요: F G A B C.</>,
        <>누가 다섯 음 중 하나를 짚으면: 왕의 F나 공주의 C에서 세어 이름을 대고 쳐요.</>,
        <><b>왕의 경비병 그리기:</b> 낮은음자리표는 <b>F 줄 위의 점</b>에서 시작해 동그랗게 내려가요 -- 그리고 F 줄 위아래에 경비병 두 점! (워크북에 따라 그리는 쪽이 있어요.)</>,
      ] : [
        <>With your left hand, walk down from <b>middle C</b> to <b>F</b>: C B A G F -- then back up from F: F G A B C.</>,
        <>Someone points to one of the five: count from the King's F or from Clara's C, name it, play it.</>,
        <><b>Draw the King's guards:</b> a bass clef <b>starts with a dot on the F line</b> and curls down -- then the two guards, one above the F line and one below. (The Workbook has one to trace.)</>,
      ]}/>
      <LbRemember>{t('The two dots guard F: the King\'s line. The King to Clara: F G A B C.', '두 점은 F를 지켜요: 왕의 줄. 왕에서 공주까지: F G A B C.')}</LbRemember>
    </LbPage>,

    // 6. middle C: Princess Clara (the grand staff)
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Middle C: Princess Clara', '가운데 도: 클라라 공주')}>
      {pic(p6, 230, 680)}
      <LbSay>{LANG === 'ko' ? <>여왕의 오선을 위에, 왕의 오선을 아래에 두고 앞에서 선으로 묶으면 <b>큰보표</b>예요 -- 손마다 오선 하나씩. 두 궁전 사이, <b>가운데 도</b>에 <b>클라라 공주</b>가 살아요 -- 2챕터의 땅이에요. 공주의 음은 자기만의 <b>작은 사다리 발판</b>에 써요: 여왕의 오선에 붙을 땐 <b>바로 아래</b>, 왕의 오선에 붙을 땐 <b>바로 위</b>. 종이에서는 두 자리처럼 보여도 피아노에서는 <b>한 건반</b> -- 그래서 클라라가 양쪽에 서 있어요.</>
        : <>Put the Queen's staff on top and the King's underneath, joined by a line at the start: that is the <b>grand staff</b> -- one staff for each hand. Between the two palaces, on <b>middle C</b>, lives <b>Princess Clara</b> -- the ground from Chapter 2. Her note is written on <b>a little ladder rung of its own</b>: <b>just under</b> the Queen's staff when it belongs up there, <b>just over</b> the King's when it belongs down. Two places on paper, <b>one key</b> on the piano -- that is why Clara stands by both.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <><b>가운데 도</b>를 쳐요: 공주의 자리, 두 손이 다 닿는 단 한 곳.</>,
        <><b>어느 궁전?</b> 누가 공주의 음을 위 오선 아래에 쓰거나 아래 오선 위에 써요: 위에 붙어도 아래에 붙어도 <b>같은 건반</b> -- 매번 가운데 도를 쳐요. 오른손으로도, 왼손으로도.</>,
      ] : [
        <>Play <b>middle C</b>: Clara's place, the one key both hands can reach.</>,
        <><b>Which palace?</b> Someone writes Clara's note under the top staff or over the bottom one: attached up or attached down, it is <b>the same key</b> -- play middle C each time, with the right hand and with the left.</>,
      ]}/>
      <LbRemember>{t('Clara lives between the Queen and the King -- the same key on either staff.', '클라라는 여왕과 왕 사이에 살아요 -- 어느 오선에 써도 같은 건반.')}</LbRemember>
    </LbPage>,

    // 8. my five checks + the check-up on paper
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('At the piano: show each one, then tick how it is going -- not yet, nearly, or got it! On paper: do the check-up below.', '피아노 앞에서: 하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요! 종이에서: 아래 점검을 풀어요.')}</LbSay>
      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_sf_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
      <LbOnly print><SfPaperCheck/></LbOnly>
    </LbPage>,
  ];
}
function StaffLessonBook() { return <>{sfLbPages(false)}</>; }
// the check-up on paper, in the order of the five checks; only the nine notes from the King's F to the Queen's G
const sfChkData = () => withSeed('sf-chk405', () => ({
    ls: shuffle([30, 33, 36, 35]).map(d => ({ d })),
    ss: [[31, 32], [34, 32], [30, 34], [37, 36]].map(([a, b]) => ({ a, b })),
    tr: shuffle([29, 30, 31, 32]),
    ba: shuffle([25, 26, 27, 24]),
    mc: { treble: shuffle([{ d: 28 }, { d: 31 }, { d: 29 }]), bass: shuffle([{ d: 28 }, { d: 25 }, { d: 27 }]) },
  }));
function SfPaperCheck() {
  const C = useMemo(() => sfChkData(), [LANG]);
  const cell = (n, kids) => <BkCell key={n} n={n}><div style={{padding:'5px 4px 0'}}>{kids}</div></BkCell>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column'}}>
    <LbPaperHead/>
    {bkSec('A', 'Line or space? Write L or S.')}
    <BkGrid cols={4} gap="5px 10px">{C.ls.map((it, i) => cell(i + 1, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:72}}><PaperStaff clefOn={false} notes={[{ d: it.d }]} width={90}/></div>{bkBox(28, 24)}</div>))}</BkGrid>
    {bkSec('B', 'Step or skip? Up or down? Write it.')}
    <BkGrid cols={4} gap="5px 10px">{C.ss.map((it, i) => cell(i + 5, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:72}}><PaperStaff clefOn={false} notes={[{ d: it.a }, { d: it.b }]} width={90}/></div>{bkBox(44, 24)}</div>))}</BkGrid>
    {bkSec('C', 'The Queen\'s five: name the notes.')}
    <BkGrid cols={4} gap="5px 10px">{C.tr.map((d, i) => cell(i + 9, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:84}}><PaperStaff clef="treble" notes={[{ d }]} width={110}/></div>{bkBox(28, 24)}</div>))}</BkGrid>
    {bkSec('D', 'The King\'s five: name the notes.')}
    <BkGrid cols={4} gap="5px 10px">{C.ba.map((d, i) => cell(i + 13, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:84}}><PaperStaff clef="bass" notes={[{ d }]} width={110}/></div>{bkBox(28, 24)}</div>))}</BkGrid>
    {bkSec('E', 'Circle every middle C.')}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10}}>{['treble', 'bass'].map(cl => <div key={cl} style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 10px'}}><div style={{maxWidth:200}}><PaperStaff clef={cl} notes={C.mc[cl]} width={220}/></div></div>)}</div>
  </div>;
}

// ─── Phase 405, part 2: the chapter 4 app lesson (the book on screen), the drill's new question kinds, ───
// ─── the Workbook that faces the Lesson Book, and the Teacher copy ───

// the online lesson is the Lesson Book opened on screen (Phase 376 pattern), one step per book page
const SF_STORE = [0, 1, 2, 3, 4, 5];
function StaffLearn({ onStart }) {
  const pages = sfLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="staff" title={t('Reading the Staff', '오선보 읽기')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="staff"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={SF_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ─ the drill's new question kinds (Phase 405): 'ls' line or space, 'ss' step or skip up or down, 'write' tap where it goes ─
function SfLsQuestion({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const ink = pixel ? '#faf6ec' : '#26296b';
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const c = CLEFS[q.clef], off = q.d - c.low, isLine = q.answer === 'line';
  const num = isLine ? off / 2 + 1 : (off + 1) / 2;
  return (
    <div>
      <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 8px'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)'}}>{pixel ? t('LINE OR SPACE?', '줄? 칸?') : t('Is this a line note or a space note?', '줄 음표일까요, 칸 음표일까요?')}</p>
      <div style={{background:pixel ? 'transparent' : '#fff',borderRadius:8,margin:'0 0 12px'}}>
        <StaffView clef={q.clef} ink={ink} notes={[{ d: q.d, color: done ? (given.ok ? '#2e8a6e' : '#c8361b') : ink }]}/>
      </div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>
        {[['line', t('On a line', '줄 위')], ['space', t('In a space', '칸 안')]].map(([v, lbl]) => <button key={v} disabled={locked} onClick={() => onAnswer(v)} className={btnCls + (!done ? '' : v === q.answer ? ' good' : given.ans === v ? ' bad' : '')}>{lbl}</button>)}
      </div>
      {done && <div style={{textAlign:'center',fontSize:13,fontWeight:700,marginTop:8,color:'var(--muted)'}}>{isLine ? t('Line ' + num + ' runs right through its middle.', num + '번 줄이 한가운데를 지나요.') : t('Space ' + num + ': it touches the lines above and below.', num + '번 칸: 위아래 줄에 닿아요.')}</div>}
    </div>
  );
}
function SfSsQuestion({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const ink = pixel ? '#faf6ec' : '#26296b';
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  return (
    <div>
      <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 8px'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)'}}>{pixel ? t('STEP OR SKIP? UP OR DOWN?', '한 걸음? 건너뛰기?') : t('From the first note to the second: step or skip? Up or down?', '첫 음에서 둘째 음으로: 한 걸음일까요, 건너뛰기일까요? 위로? 아래로?')}</p>
      <div style={{background:pixel ? 'transparent' : '#fff',borderRadius:8,margin:'0 0 12px'}}>
        <StaffView clef={q.clef} ink={ink} spread notes={[{ d: q.a, color: done ? '#6d6f9c' : ink }, { d: q.b, color: done ? (given.ok ? '#2e8a6e' : '#c8361b') : ink }]}/>
      </div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>
        {[['step-up', t('Step up', '한 걸음 위로')], ['skip-up', t('Skip up', '건너뛰기 위로')], ['step-down', t('Step down', '한 걸음 아래로')], ['skip-down', t('Skip down', '건너뛰기 아래로')]].map(([v, lbl]) =>
          <button key={v} disabled={locked} onClick={() => onAnswer(v)} className={btnCls + (!done ? '' : v === q.answer ? ' good' : given.ans === v ? ' bad' : '')}>{lbl}</button>)}
      </div>
    </div>
  );
}
function SfWriteQuestion({ q, level, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const ink = pixel ? '#faf6ec' : '#26296b';
  const [tap, setTap] = useState(null);
  useEffect(() => { setTap(null); }, [q.uid]);
  const rows = []; for (let d = level.range[0]; d <= level.range[1]; d++) rows.push(d);
  return (
    <div>
      <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 8px'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)'}}>{pixel ? t('TAP WHERE IT GOES', '들어갈 자리를 탭') : t('Tap the line or space where this note goes -- either staff counts', '이 음이 들어갈 줄이나 칸을 눌러요 -- 위 오선이든 아래 오선이든 괜찮아요')}</p>
      <div style={{textAlign:'center',fontSize:34,fontWeight:900,lineHeight:1.05,margin:'0 0 2px',color:pixel ? '#faf6ec' : 'var(--text)'}}><NoteName n={q.answer}/></div>
      <div style={{background:pixel ? 'transparent' : '#fff',borderRadius:8,margin:'0 0 8px'}}>
        <StaffFrame clef={q.clef} lo={level.range[0]} hi={level.range[1]} width={280} ink={ink} rows={done || locked ? null : rows} onRow={(d) => { setTap(d); onAnswer(dName(d)); }} guideX={150}>
          {(yOf) => done && <>
            {tap !== null && !given.ok && <g><Ledgers clef={q.clef} d={tap} x={150} yOf={yOf}/><ellipse cx={150} cy={yOf(tap)} rx="7" ry="5" transform={`rotate(-20 150 ${yOf(tap)})`} fill="#c8361b"/></g>}
            {rows.filter(d => dName(d) === q.answer).map(d => <g key={d} opacity={tap === d ? 1 : 0.45}><Ledgers clef={q.clef} d={d} x={tap === d ? 150 : 200} yOf={yOf}/><ellipse cx={tap === d ? 150 : 200} cy={yOf(d)} rx="7" ry="5" transform={`rotate(-20 ${tap === d ? 150 : 200} ${yOf(d)})`} fill="#2e8a6e"/></g>)}
          </>}
        </StaffFrame>
      </div>
    </div>
  );
}

// ─── the Workbook (Phase 405): one page facing each Lesson Book page, in the two inks ───
function sfWorkbook() {
  const k = (s) => 'sf-wb405-' + s;
  const rnd = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
  const run = (n, lo, hi) => { const out = []; for (let i = 0; i < n; i++) { let d; do { d = rnd(lo, hi); } while (out.length && out[out.length - 1].d === d); out.push({ d }); } return out; };
  const mkSS = (lo, hi) => { for (;;) { const a = rnd(lo, hi), gap = Math.random() < 0.5 ? 1 : 2, dir = Math.random() < 0.5 ? 1 : -1, b = a + gap * dir; if (b >= lo && b <= hi) return { a, b }; } };
  const s1 = withSeed(k('s1'), () => ({ tog: run(4, 30, 38), home: run(6, 30, 38), sort: run(6, 30, 38) }));
  const s2 = withSeed(k('s2'), () => ({ tog: Array.from({ length: 4 }, () => mkSS(30, 38)), home: Array.from({ length: 4 }, () => mkSS(30, 38)), hi: Array.from({ length: 4 }, () => mkSS(30, 38)) }));
  const s3 = withSeed(k('s3'), () => ({ tog: shuffle([28, 29, 30, 31, 32]).slice(0, 4).map(d => ({ d })), home: run(6, 28, 32), draw: shuffle(['D', 'E', 'F', 'G']) }));
  const s4 = withSeed(k('s4'), () => {
    let r = rnd(0, 2); const path = [[r, 0]];
    for (let c = 1; c < 5; c++) { r = Math.max(0, Math.min(2, r + rnd(-1, 1))); path.push([r, c]); }
    const grid = Array.from({ length: 3 }, () => Array.from({ length: 5 }, () => rnd(25, 28)));
    path.forEach(([pr, pc]) => { grid[pr][pc] = 24; });
    return { tog: shuffle([24, 25, 26, 27, 28]).slice(0, 4).map(d => ({ d })), home: run(6, 24, 28), draw: shuffle(['G', 'A', 'B', 'C']), grid, path };
  });
  const s5 = withSeed(k('s5'), () => ({
    mid: [0, 1].map(() => { const cs = shuffle([0, 1, 2, 3, 4]).slice(0, 2); const rest = [24, 25, 26, 27, 29, 30, 31, 32]; return [0, 1, 2, 3, 4].map(i => cs.includes(i) ? { d: 28, staff: Math.random() < 0.5 ? 'treble' : 'bass' } : { d: rest[Math.floor(Math.random() * rest.length)] }); }),
    bingo: shuffle([24, 25, 26, 27, 28, 29, 30, 31, 32]),
  }));
  return { s1, s2, s3, s4, s5 };
}
const sfLS = (d, clef = 'treble') => (d - CLEFS[clef].low) % 2 === 0 ? 'L' : 'S';
const sfSSName = (it) => (Math.abs(it.b - it.a) === 1 ? 'step ' : 'skip ') + (it.b > it.a ? 'up' : 'down');
// the secret words, spelled with the nine notes round Clara (w3; CABBAGE is the long one)
const SF_MSG = [
  { word: 'BAG', clef: 'bass', notes: [27, 26, 25] },
  { word: 'FED', clef: 'treble', notes: [31, 30, 29] },
  { word: 'EGG', clef: 'treble', notes: [30, 32, 32] },
  { word: 'CABBAGE', clef: 'grand', notes: [28, 26, 27, 27, 26, 25, 30] },
];
// a row of faint clefs to trace (N4/N5), the first one solid as the example
function SfTraceRow({ clef }) {
  return <BkGrid cols={4} gap="5px 8px">{[0, 1, 2, 3].map(i => <div key={i} style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 6px'}}>
    <PaperStaff clef={clef} notes={[]} width={92} ink={i === 0 ? BK.ink : '#c9c4de'} minSpan={clef === 'treble' ? [29, 39] : [17, 27]}/>
  </div>)}</BkGrid>;
}
function SfWorkbook({ startNo = 1, frames = true }) {
  const W = useMemo(() => sfWorkbook(), [LANG]);
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="staff">{content}</WbPage>);
  const lsCell = (it, n, ex) => <ExCell key={n} n={n} ex={ex}><div style={{display:'flex',alignItems:'center',gap:8,padding:'8px 4px 2px'}}><div style={{flex:1,maxWidth:76}}><PaperStaff clefOn={false} notes={[{ d: it.d }]} width={92}/></div><span style={{fontSize:16,fontWeight:900,color:ex ? BK.coral : 'transparent',border:ex ? 'none' : '1.4px solid ' + BK.ink,borderRadius:6,minWidth:28,minHeight:26,display:'inline-flex',alignItems:'center',justifyContent:'center'}}>{ex ? sfLS(it.d) : '?'}</span></div></ExCell>;
  const nmCell = (it, n, ex, clef) => <ExCell key={n} n={n} ex={ex}><div style={{display:'flex',alignItems:'center',gap:8,padding:'8px 4px 2px'}}><div style={{flex:1,maxWidth:86}}><PaperStaff clef={clef} notes={[{ d: it.d }]} width={110}/></div><span style={{fontSize:16,fontWeight:900,color:ex ? BK.coral : 'transparent',border:ex ? 'none' : '1.4px solid ' + BK.ink,borderRadius:6,minWidth:28,minHeight:26,display:'inline-flex',alignItems:'center',justifyContent:'center'}}>{ex ? dName(it.d) : '?'}</span></div></ExCell>;
  const ssCell = (it, n, ex) => <ExCell key={n} n={n} ex={ex}><div style={{display:'flex',alignItems:'center',gap:6,padding:'8px 4px 2px'}}><div style={{flex:1,maxWidth:76}}><PaperStaff clefOn={false} notes={[{ d: it.a }, { d: it.b }]} width={92}/></div><span style={{fontSize:11.5,fontWeight:900,color:ex ? BK.coral : 'transparent',border:ex ? 'none' : '1.4px solid ' + BK.ink,borderRadius:6,minWidth:52,minHeight:26,display:'inline-flex',alignItems:'center',justifyContent:'center',textAlign:'center'}}>{ex ? sfSSName(it) : '?'}</span></div></ExCell>;
  const drawD = (L, clef) => clef === 'treble' ? 28 + ['C', 'D', 'E', 'F', 'G'].indexOf(L) : 24 + ['F', 'G', 'A', 'B', 'C'].indexOf(L);
  const drawCell = (L, n, clef, ex) => <ExCell key={n} n={n} ex={ex}><div style={{padding:'6px 4px 2px',textAlign:'center'}}><div style={{fontSize:20,fontWeight:900,color:BK.coral,lineHeight:1}}>{L}</div><PaperStaff clef={clef} notes={ex ? [{ d: drawD(L, clef), color: BK.coral }] : []} width={100} minSpan={clef === 'treble' ? [27, 33] : [23, 29]}/></div></ExCell>;

  // 2 (faces "Lines and spaces")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Line or space?" how="Kebab = on a line, write L. Sandwich = in a space, write S. Count from the bottom.">
      <Lead><KebabSandwich/></Lead>
      <BkGrid cols={4} gap="5px 8px">{W.s1.tog.map((it, i) => lsCell(it, i + 1, i === 0))}</BkGrid>
    </Part>
    <Part kind="home" title="Your turn" how="L on a line, S in a space -- then write the line or space number next to it if you can.">
      <BkGrid cols={3} gap="5px 8px">{W.s1.home.map((it, i) => lsCell(it, i + 5))}</BkGrid>
    </Part>
    <Part kind="play" style={{justifyContent:'center'}} title="Kebab plate, sandwich plate" how="Sort the six notes: write each number on its plate.">
      <BkGrid cols={6} gap="4px 6px">{W.s1.sort.map((it, i) => <BkCell key={i} n={i + 1}><div style={{padding:'8px 4px 2px'}}><PaperStaff clefOn={false} notes={[{ d: it.d }]} width={70}/></div></BkCell>)}</BkGrid>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10,marginTop:8}}>
        {[['Kebab plate (line notes)', true], ['Sandwich plate (space notes)', false]].map(([lbl]) => <div key={lbl} style={{border:'1.6px solid ' + BK.ink,borderRadius:40,minHeight:44,display:'flex',alignItems:'center',justifyContent:'center',fontSize:12,fontWeight:800,color:BK.muted}}>{lbl}</div>)}
      </div>
    </Part>
  </>);
  // 3 (faces "Up the staff, up the piano")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Step or skip? Up or down?" how="From the first note to the second. Write it, like “step up” or “skip down”.">
      <BkGrid cols={4} gap="5px 8px">{W.s2.tog.map((it, i) => ssCell(it, i + 1, i === 0))}</BkGrid>
    </Part>
    <Part kind="home" title="Your turn">
      <BkGrid cols={4} gap="5px 8px">{W.s2.home.map((it, i) => ssCell(it, i + 5))}</BkGrid>
    </Part>
    <Part kind="play" style={{justifyContent:'center'}} title="Which is higher?" how="Circle the higher note in each pair -- then play both, low one first, and check with your ears.">
      <BkGrid cols={4} gap="5px 8px">{W.s2.hi.map((it, i) => <BkCell key={i} n={i + 1}><div style={{padding:'8px 4px 2px'}}><PaperStaff clefOn={false} notes={[{ d: it.a }, { d: it.b }]} width={92}/></div></BkCell>)}</BkGrid>
    </Part>
  </>);
  // 4 (faces "The Queen's five")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Trace the Queen's curl" how="A treble clef starts on the G line -- the Queen's house -- and spirals out. Trace the faint ones.">
      <SfTraceRow clef="treble"/>
    </Part>
    <Part kind="home" title="The Queen's five: name the notes" how="Count up from Clara's C or down from the Queen's G.">
      <BkGrid cols={3} gap="5px 8px">{W.s3.home.map((it, i) => nmCell(it, i + 1, i === 0, 'treble'))}</BkGrid>
    </Part>
    <Part kind="play" style={{justifyContent:'center'}} title="Draw the Queen's notes" how="Draw a note head where each letter lives. On a line, the line runs through it; in a space, it fills the space.">
      <BkGrid cols={4} gap="5px 8px">{W.s3.draw.map((L, i) => drawCell(L, i + 1, 'treble', i === 0))}</BkGrid>
    </Part>
  </>);
  // 5 (faces "The King's five")
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="Trace the King's guards" how="A bass clef starts with a dot on the F line and curls down -- then the two guards, one above the F line and one below.">
      <SfTraceRow clef="bass"/>
    </Part>
    <Part kind="home" title="The King's five: name the notes" how="Start from the King's F -- the line between the two guards -- or from Clara's C.">
      <BkGrid cols={3} gap="5px 8px">{W.s4.home.map((it, i) => nmCell(it, i + 1, i === 0, 'bass'))}</BkGrid>
    </Part>
    <Part kind="play" style={{justifyContent:'center'}} title="Help the King get home" how="Colour every F. The F stones touching each other make the road from the King to his castle.">
      <div style={{display:'flex',alignItems:'center',gap:8}}>
        <PenArt shapes={sfKing(22, 26, 1)} vb={[4, 0, 36, 48]} style={{width:36,flex:'0 0 auto'}} label="the King"/>
        <div style={{flex:1}}><BkGrid cols={5} gap="4px 5px">{W.s4.grid.flatMap((row, r) => row.map((d, c) => <div key={r + '-' + c} style={{border:'1px solid #ece6d8',borderRadius:7,padding:'2px 4px'}}><PaperStaff clef="bass" notes={[{ d }]} width={120}/></div>))}</BkGrid></div>
        <svg viewBox="0 0 36 48" style={{width:36,flex:'0 0 auto'}} aria-label="his castle"><path d="M6 44 V20 H10 V15 H14 V20 H16 V15 H20 V20 H22 V15 H26 V20 H30 V44 Z" fill={BK.soft} stroke={BK.ink} strokeWidth="1.8" strokeLinejoin="round"/><path d="M15 44 V32 Q18 28 21 32 V44" fill={BK.coral} stroke={BK.ink} strokeWidth="1.4"/></svg>
      </div>
    </Part>
  </>);
  // 6 (faces "Middle C: Princess Clara")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Circle every middle C" how="Clara's note sits on its own little ladder rung -- just under the Queen's staff, or just over the King's. Same key!">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10}}>{W.s5.mid.map((row, i) => <div key={i} style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 10px'}}><PaperStaff clef="grand" notes={row} width={330}/></div>)}</div>
    </Part>
    <Part kind="home" title="The secret message" how="Write each note's letter in its box -- every row spells a word. The last one is seven notes long!">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:'2px 10px'}}>
        {SF_MSG.slice(0, 3).map((m, i) => <div key={i} style={{display:'flex',flexDirection:'column',gap:2}}>
          <PaperStaff clef={m.clef} notes={m.notes.map(d => ({ d }))} width={150}/>
          <div style={{display:'flex',gap:4,justifyContent:'center'}}>{m.word.split('').map((L, j) => <span key={j} style={{width:24,height:26,border:'1.4px solid ' + BK.ink,borderRadius:5,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14,fontWeight:900,color:i === 0 ? BK.coral : 'transparent'}}>{i === 0 ? L : ''}</span>)}</div>
        </div>)}
      </div>
      {SF_MSG.slice(3).map((m) => <div key={m.word} style={{display:'flex',alignItems:'center',gap:12,margin:'6px 0 0'}}>
        <div style={{flex:'1 1 auto',maxWidth:330}}><PaperStaff clef={m.clef} notes={m.notes.map(d => ({ d }))} width={330}/></div>
        <div style={{display:'flex',gap:4}}>{m.word.split('').map((L, j) => <span key={j} style={{width:24,height:26,border:'1.4px solid ' + BK.ink,borderRadius:5,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14,fontWeight:900,color:'transparent'}}/>)}</div>
      </div>)}
    </Part>
    <Part kind="play" style={{justifyContent:'center'}} title="Note bingo" how="Someone names (or plays) one of the nine notes. Find it and colour it. Three in a row -- any direction -- wins!">
      <BkGrid cols={9} gap="4px 5px">{W.s5.bingo.map((d, i) => <div key={i} style={{border:'1px solid #ece6d8',borderRadius:7,padding:'2px 3px'}}><PaperStaff clef={d >= 28 ? 'treble' : 'bass'} notes={[{ d }]} width={56}/></div>)}</BkGrid>
    </Part>
  </>);
  return <>{frames ? lbFramed('staff', pages, startNo) : pages}</>;
}

// ─── the Teacher copy (Phase 405): answers, what to watch for, what to say -- her own lines ───
function SfTeacher() {
  const W = useMemo(() => sfWorkbook(), [LANG]);
  const C = useMemo(() => sfChkData(), [LANG]);
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="staff" teacher>{content}</WbPage>);
  const path = W.s4.path.map(([r, c]) => 'row ' + (r + 1) + ' col ' + (c + 1));
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('staff')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Answers for every workbook page, the mistakes students make most, and a line to say when they get stuck. This chapter reads only the nine notes round middle C; the whole staff, the rhymes and fast reading from landmarks come in the next chapter.</div>
    <TcBlock page={2} title="Lines and spaces" answers={<>{tcAns('TRY IT', W.s1.tog.map(it => sfLS(it.d)))}{tcAns('YOUR TURN', W.s1.home.map(it => sfLS(it.d) + (sfLS(it.d) === 'L' ? (it.d - 30) / 2 + 1 : (it.d - 29) / 2)))}{tcAns('PLATES', ['kebab: ' + W.s1.sort.map((it, i) => sfLS(it.d) === 'L' ? i + 1 : null).filter(Boolean).join(' ') , 'sandwich: ' + W.s1.sort.map((it, i) => sfLS(it.d) === 'S' ? i + 1 : null).filter(Boolean).join(' ')])}</>}
      watch="Counting from the top line down, and space notes drawn leaning on a line so they look like line notes."
      say="“Count like climbing a ladder -- from the floor up. Line 1 is the bottom one.”"/>
    <TcBlock page={3} title="Up the staff, up the piano" answers={<>{tcAns('TRY IT', W.s2.tog.map(sfSSName))}{tcAns('YOUR TURN', W.s2.home.map(sfSSName))}{tcAns('HIGHER', W.s2.hi.map(it => it.a > it.b ? '1st' : '2nd'))}</>}
      watch="Circling the note that comes later in time instead of the higher one, and calling every move “up”."
      say="“Higher on the page is higher on the piano -- which one would your right hand reach for?”"/>
    <TcBlock page={4} title="The Queen's five" answers={<>{tcAns('YOUR TURN', W.s3.home.map(it => withSolfa(dName(it.d))))}{tcAns('DRAW', W.s3.draw.map(L => L + ': ' + { C: 'her ladder rung', D: 'just under line 1', E: 'line 1', F: 'space 1', G: 'line 2, the Queen\u2019s' }[L]))}</>}
      watch="Starting to count without looking at the clef first -- most children grab whatever they remember."
      say="“Crown check first: whose palace is this? The curl holds the Queen's G -- start from her line, or from Clara's C.”"/>
    <TcBlock page={5} title="The King's five" answers={<>{tcAns('YOUR TURN', W.s4.home.map(it => withSolfa(dName(it.d))))}{tcAns('DRAW', W.s4.draw.map(L => L + ': ' + { F: 'line 4, the King\u2019s', G: 'space 4', A: 'line 5, the top line', B: 'just over the top line', C: 'her ladder rung above' }[L]))}{tcAns('MAZE', ['the F road: ' + path.join(' \u203a ')])}</>}
      watch="Reading bass notes with treble names -- the answer comes out two letters too high."
      say="“Crown check: this is the King's staff. His two dots guard F -- find F first, then walk from there.”"/>
  </>);
  P(<>
    <TcBlock page={6} title="Middle C: Princess Clara" answers={<>{tcAns('CIRCLE', W.s5.mid.map((row, i) => 'staff ' + (i + 1) + ': notes ' + row.map((n, j) => n.d === 28 ? j + 1 : null).filter(Boolean).join(' & ')))}{tcAns('MESSAGE', SF_MSG.map(m => m.word))}{tcAns('BINGO', W.s5.bingo.map(d => withSolfa(dName(d))))}</>}
      watch="Thinking the C under the treble staff and the C over the bass staff are two different keys."
      say="“Same key, written from the Queen's side or the King's side -- that is why Clara stands by both.”"/>
    <TcBlock page={7} title="Check-up (in the Lesson Book)" goBack={[{ id: 'ls', step: 1, page: 2 }, { id: 'ss', step: 2, page: 3 }, { id: 'tr', step: 3, page: 4 }, { id: 'ba', step: 4, page: 5 }, { id: 'mc', step: 5, page: 6 }]} answers={<>
      {tcAns('A', C.ls.map(it => sfLS(it.d)))}
      {tcAns('B', C.ss.map(it => sfSSName({ a: it.a, b: it.b })))}
      {tcAns('C', C.tr.map(d => withSolfa(dName(d))))}
      {tcAns('D', C.ba.map(d => withSolfa(dName(d))))}
      {tcAns('E', ['treble staff: note ' + (C.mc.treble.findIndex(n => n.d === 28) + 1) + ' · bass staff: note ' + (C.mc.bass.findIndex(n => n.d === 28) + 1)])}
    </>}
      watch="A wobbly B: step down from Clara's C. And F and G living in both palaces -- on the Queen's staff they are high, on the King's they are low."
      say="“Crown check, then count from the nearest friend: the Queen's G, Clara's C or the King's F.”"/>
    <div style={{fontSize:12.5,color:BK.ink,lineHeight:1.6,marginTop:6}}>
      <b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>LESSON TIME</b> The hand staff (page 2 of the book) is the one prop this chapter needs: five fingers are the five lines. Short lessons: set the drill levels as the week's practice -- random notes, a little every day, tracked on the student page.
    </div>
  </>);
  return <>{pages}</>;
}
