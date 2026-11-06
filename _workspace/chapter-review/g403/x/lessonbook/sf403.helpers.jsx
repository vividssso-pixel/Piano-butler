// ─── Chapter 4: Reading the Staff (chapter 'staff') -- Lesson Book DRAFT v2 (Phase 402) ───
// v2 (Sohyun 2026-10-09): five notes first -- this chapter reads only the ten notes between the King's F and the Queen's G,
// five each side of Princess Clara (middle C); the whole staff and her rhymes go to a new chapter 5 (The Whole Staff),
// ledger lines to chapter 6. Middle C stands on a little ladder rung (the word 'ledger line' waits for its chapter).
// The chapter teaches the concept only (Phase 399: no songs in a chapter). Built on Sohyun's own clef story (Phase 101c):
// the treble clef began as a G and its curl wraps the Queen's line (G above middle C); the bass clef began as an F and its
// two dots are the King's guards around his line (F below middle C); the two palaces mirror each other round middle C.
// New in this draft (B questions): Princess Clara lives on middle C (chapter 3's Clara at C; middle C is the ground from
// chapter 2), the staff is shown as shapes before names (lines and spaces, steps and skips), and landmarks come before rhymes.
// Ledger lines beyond middle C's own short line wait for chapter 6; sharps and flats for chapter 7.
// ?draft=1 marks the lines that wait for her B answers. Not applied to the app.

// the Queen and the King, small, in pen (characters: hand-drawn)
function sfQueen(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-8.4, -3)], ['Q', P(-11, 8), P(-7.6, 13)], ['L', P(7.6, 13)], ['Q', P(11, 8), P(8.4, -3)], ['Z']], f: PEN_N, s: PEN_N, w: 1.2 });   // long hair
  s.push({ k: 'pa', seg: [['M', P(-11, 14.6)], ['Q', P(-10, 8.4), P(0, 8.8)], ['Q', P(10, 8.4), P(11, 14.6)], ['Z']], f: PEN_C, s: PEN_N, w: 1.5 });   // her gown
  [[-3, 11.2], [0, 11.9], [3, 11.2]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.9 * k, ry: 0.9 * k, f: PEN_P }));   // pearls
  s.push({ k: 'el', c: P(0, -0.4), rx: 6.8 * k, ry: 7.6 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.8, -2)], ['Q', P(-7, -8.4), P(0, -8.6)], ['Q', P(7, -8.4), P(6.8, -2)], ['Q', P(4, -6.2), P(0, -5.2)], ['Q', P(-4, -6.2), P(-6.8, -2)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });
  s.push({ k: 'pa', seg: [['M', P(-6, -7.8)], ['L', P(-7, -15.6)], ['L', P(-3.4, -11.4)], ['L', P(0, -17.6)], ['L', P(3.4, -11.4)], ['L', P(7, -15.6)], ['L', P(6, -7.8)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });   // her tall crown
  [[-7, -15.6], [0, -17.6], [7, -15.6]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 1 * k, ry: 1 * k, f: PEN_P, s: PEN_N, w: 0.8 }));
  s.push({ k: 'el', c: P(-2.5, 0.2), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.5, 0.2), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push(penCurve([['M', P(-1.9, 3.4)], ['Q', P(0, 4.8), P(1.9, 3.4)]], 1.1, PEN_N));
  return nnCh(s);
}
function sfKing(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-11.5, 14.6)], ['Q', P(-10.5, 8), P(0, 8.4)], ['Q', P(10.5, 8), P(11.5, 14.6)], ['Z']], f: PEN_N, s: PEN_N, w: 1.5 });   // his robe
  s.push(penCurve([['M', P(-8, 10.2)], ['Q', P(0, 13.2), P(8, 10.2)]], 2.2, PEN_P));   // the ermine collar
  s.push({ k: 'el', c: P(0, -1), rx: 6.8 * k, ry: 7.4 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.3, 0.6)], ['Q', P(-6.2, 9.8), P(0, 10.8)], ['Q', P(6.2, 9.8), P(6.3, 0.6)], ['Q', P(3.4, 4.6), P(0, 4.2)], ['Q', P(-3.4, 4.6), P(-6.3, 0.6)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });   // his beard
  s.push({ k: 'pa', seg: [['M', P(-6.6, -6.4)], ['L', P(-6.6, -13.6)], ['L', P(-3.3, -10.8)], ['L', P(0, -14.8)], ['L', P(3.3, -10.8)], ['L', P(6.6, -13.6)], ['L', P(6.6, -6.4)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });   // his crown
  s.push({ ...penLine(P(0, -14.8), P(0, -18.4), 1.3), }, { ...penLine(P(-1.6, -16.8), P(1.6, -16.8), 1.3) });   // the cross on top
  s.push({ k: 'el', c: P(-2.5, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.5, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push(penCurve([['M', P(-1.6, 2.4)], ['Q', P(0, 3.4), P(1.6, 2.4)]], 1.1, PEN_P));
  return nnCh(s);
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

