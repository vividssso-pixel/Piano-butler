// ─── Phase 425: the map is a street ───
// Sohyun 2026-10-10: "B가 좋다 ... 다른 집으로 들어가서 하는 거는 필요할 때마다 거기에 방문을 해서 할 수 있는 거잖아. 그리고 C를
//같이 써서 ... 어디에 있는지 위치만 파악할 수 있도록" and "색은 단순하게 두고 ... 단순하지만 그 쉐입으로 조금 클래식함을 표현".
// Every stage is a building on one street and every chapter a window: the Lodge at the foot of the street, then the
// Library, the Clock Tower, the Conservatory, the Academy, the Theatre and the Museum at the top. Lines only, navy on
// white; the classicism is in the shapes (cornices with dentils, friezes with the building's name, arched windows with
// keystones and bracketed sills, quoins, pilasters, columns, balustrades, pediments, a dome). Coral marks where you are,
// green what is done; Clara (the pink pawn) stands in your window. Above it, "Clara's journey" -- the same 26 chapters as
// squares on a chessboard -- shows at a glance where you are. Drawn from maps/streetc.py (_workspace/chapter-review).
const ST = { N: '#26296b', C: '#e4572e', G: '#2b6e56', NEW: '#8a8cb0', M: '#6d6f9c', LW: 1.6, MW: 0.9, FW: 0.55, CW: 360, BX0: 28, BX1: 332 };
const ST_SANS = "Inter,'Pretendard',sans-serif", ST_SERIF = "'Playfair Display',Georgia,serif";
const ST_NAMES = [['The Lodge', '버틀러의 집'], ['Library', '도서관'], ['The Clock Tower', '시계탑'], ['Conservatory', '온실'], ['Academy', '아카데미'], ['Theatre', '극장'], ['Museum', '박물관']];
const ST_AT = ['at the Lodge', 'at the Library', 'at the Clock Tower', 'in the Conservatory', 'at the Academy', 'at the Theatre', 'at the Museum'];
// the drawing's parts sit inside ST_G (white fill, navy line), so each part names only what differs
const ST_G = '<g fill="#fff" stroke="#26296b" stroke-linejoin="round">', stG = (svg) => ST_G + svg + '</g>';
const stL = (x1, y1, x2, y2, w = ST.MW) => '<line x1="' + pFix(x1) + '" y1="' + pFix(y1) + '" x2="' + pFix(x2) + '" y2="' + pFix(y2) + '" stroke-width="' + w + '"/>';
const stR = (x, y, w, h, sw = ST.MW, fill = '#fff') => '<rect x="' + pFix(x) + '" y="' + pFix(y) + '" width="' + pFix(w) + '" height="' + pFix(h) + '"' + (fill === '#fff' ? '' : ' fill="' + fill + '"') + ' stroke-width="' + sw + '"/>';
const stP = (d, sw = ST.MW, fill = '#fff') => '<path d="' + d + '"' + (fill === '#fff' ? '' : ' fill="' + fill + '"') + ' stroke-width="' + sw + '"/>';
const stD = (...a) => a.map(v => typeof v === 'number' ? pFix(v) : v).join(' ');   // a path's d: numbers rounded, letters kept
const stC = (cx, cy, r, sw = ST.MW, fill = '#fff') => '<circle cx="' + pFix(cx) + '" cy="' + pFix(cy) + '" r="' + pFix(r) + '"' + (fill === '#fff' ? '' : ' fill="' + fill + '"') + (fill === 'none' || fill === '#fff' ? '' : ' stroke="' + fill + '"') + ' stroke-width="' + sw + '"/>';
function stT(x, y, s, o = {}) {
  const st = (o.serif ? 'font-family:' + ST_SERIF + ';font-variant-numeric:lining-nums;' : '') + (o.italic ? 'font-style:italic;' : '') + (o.ls ? 'letter-spacing:' + o.ls + ';' : '');
  return '<text x="' + pFix(x) + '" y="' + pFix(y) + '" font-size="' + (o.size || 11) + '" font-weight="' + (o.weight || 600) + '" fill="' + (o.fill || ST.N) + '" stroke="none" text-anchor="' + (o.anchor || 'start') + '" font-family="' + ST_SANS + '"' + (st ? ' style="' + st + '"' : '') + (o.op ? ' opacity="' + o.op + '"' : '') + '>' + penEsc(s) + '</text>';
}
// the classical vocabulary
function stCornice(x0, x1, y, dent = true, proj = 6) {   // a projecting cornice: a fascia, a moulding, a dentil course
  let s = stR(x0 - proj, y, x1 - x0 + 2 * proj, 4) + stR(x0 - proj + 2, y + 4, x1 - x0 + 2 * proj - 4, 2.5, ST.FW);
  if (dent) { const a = Math.ceil((x0 - proj + 4) / 5.2) * 5.2, n = Math.floor((x1 + proj - 4 - a) / 5.2);
    s += '<defs><pattern id="stdn" width="5.2" height="3" patternUnits="userSpaceOnUse"><rect width="2.6" height="3" fill="' + ST.N + '" stroke="none"/></pattern></defs><rect x="' + pFix(a) + '" y="' + pFix(y + 7) + '" width="' + pFix(n * 5.2 - 2.6) + '" height="3" fill="url(#stdn)"/>'; }
  return [s + stL(x0 - proj + 3, y + 11, x1 + proj - 3, y + 11, ST.FW), 12];
}
const stPlinth = (x0, x1, y, h = 10) => stR(x0 - 3, y, x1 - x0 + 6, h) + stL(x0 - 3, y + 3, x1 + 3, y + 3, ST.FW);
function stQuoins(x, y0, y1, left) {   // the stepped corner stones, long and short in turn
  let s = '', y = y0, k = 0;
  while (y < y1 - 2) { const h = Math.min(9, y1 - y), w = k % 2 === 0 ? 12 : 8; s += stR(left ? x : x - w, y, w, h, ST.FW); y += h; k++; }
  return s;
}
const stPilaster = (x, y0, y1, w = 8) => stR(x - w / 2, y0 + 4, w, y1 - y0 - 8, ST.FW) + stR(x - w / 2 - 1.5, y0, w + 3, 4, ST.FW) + stR(x - w / 2 - 1.5, y1 - 4, w + 3, 4, ST.FW);
function stColumn(x, y0, y1, r = 5, ionic = false) {   // a base of two rings, a tapering fluted shaft, a capital
  const top = y0 + (ionic ? 6 : 5);
  let s = stR(x - r - 2.5, y1 - 3, 2 * r + 5, 3, ST.FW) + stR(x - r - 1.5, y1 - 5.5, 2 * r + 3, 2.5, ST.FW);
  s += stP(stD('M', x - r, y1 - 5.5, 'L', x - r * 0.84, top, 'L', x + r * 0.84, top, 'L', x + r, y1 - 5.5, 'Z'));
  s += stL(x - r * 0.35, top + 2, x - r * 0.4, y1 - 7, ST.FW * 0.8) + stL(x + r * 0.35, top + 2, x + r * 0.4, y1 - 7, ST.FW * 0.8);
  if (ionic) s += stR(x - r - 3, y0, 2 * r + 6, 2.5, ST.FW) + stC(x - r - 0.5, y0 + 4.2, 2, ST.FW) + stC(x + r + 0.5, y0 + 4.2, 2, ST.FW);
  else s += stR(x - r - 2, y0, 2 * r + 4, 2.5, ST.FW) + stR(x - r, y0 + 2.5, 2 * r, 2.5, ST.FW);
  return s;
}
function stBaluster(x, y, h) {   // a turned baluster: a cap, a narrow neck, a bulb low down, a foot
  return stR(x - 3, y, 6, 1.6, ST.FW) + stP(stD('M', x - 1.1, y + 1.6, 'C', x - 1.1, y + h * 0.3, x - 3, y + h * 0.5, x - 3, y + h * 0.7, 'C', x - 3, y + h - 3, x - 1.4, y + h - 2.2, x - 1.4, y + h - 1.6,
    'L', x + 1.4, y + h - 1.6, 'C', x + 1.4, y + h - 2.2, x + 3, y + h - 3, x + 3, y + h * 0.7, 'C', x + 3, y + h * 0.5, x + 1.1, y + h * 0.3, x + 1.1, y + 1.6, 'Z'), ST.FW) + stR(x - 3, y + h - 1.6, 6, 1.6, ST.FW);
}
const stUrn = (x, y) => stP(stD('M', x - 3, y, 'L', x - 2, y - 2, 'C', x - 6, y - 4, x - 5, y - 10, x, y - 11, 'C', x + 5, y - 10, x + 6, y - 4, x + 2, y - 2, 'L', x + 3, y, 'Z'), ST.FW) + stC(x, y - 12.5, 1.4, 0, ST.N);
function stBalustrade(x0, x1, y, h = 18) {
  let s = stR(x0, y, x1 - x0, 2.5) + stR(x0, y + h - 2.5, x1 - x0, 2.5);
  const n = Math.floor((x1 - x0 - 16) / 10), step = (x1 - x0 - 22) / Math.max(1, n - 1), id = 'stbl' + Math.round(x0) + '_' + Math.round(y);
  s += '<defs><pattern id="' + id + '" x="' + pFix(x0 + 11 - step / 2) + '" y="' + pFix(y + 2.5) + '" width="' + step.toFixed(3) + '" height="' + (h - 5) + '" patternUnits="userSpaceOnUse">' + stBaluster(step / 2, 0, h - 5) + '</pattern></defs>'
    + '<rect x="' + pFix(x0 + 11 - step / 2) + '" y="' + pFix(y + 2.5) + '" width="' + pFix(n * step) + '" height="' + (h - 5) + '" fill="url(#' + id + ')"/>';
  [x0, x1].forEach(x => { s += stR(x - 4, y - 1, 8, h + 1) + stUrn(x, y - 1); });
  return s;
}
const stFinial = (x, y, h = 10) => stL(x, y, x, y - h) + stC(x, y - h - 1.5, 1.8, 0, ST.N) + stP(stD('M', x - 3, y - 3, 'l', 3, -4, 'l', 3, 4, 'Z'), ST.FW, ST.N);
function stPediment(x0, x1, y, h) {   // a triangular pediment with an inner moulding, an oculus, urns and a finial
  const cx = (x0 + x1) / 2;
  return stP(stD('M', x0 - 6, y, 'L', cx, y - h, 'L', x1 + 6, y, 'Z'), ST.LW) + stP(stD('M', x0 + 4, y - 3, 'L', cx, y - h + 5, 'L', x1 - 4, y - 3), ST.FW, 'none')
    + stC(cx, y - h * 0.4, h * 0.22) + stC(cx, y - h * 0.4, h * 0.22 - 2, ST.FW, 'none') + stUrn(x0 - 4, y) + stUrn(x1 + 4, y) + stFinial(cx, y - h, 6);
}
const stSteps = (cx, y, w, n = 2) => Array.from({ length: n }, (_, k) => stR(cx - w / 2 - k * 6, y + k * 4, w + k * 12, 4)).join('');
const stChimney = (x, y, h = 26) => stR(x, y - h, 14, h) + stR(x - 2, y - h - 4, 18, 4) + stR(x + 2, y - h - 9, 4, 5, ST.FW) + stR(x + 8, y - h - 9, 4, 5, ST.FW);
function stFrame(x, y, w, h, arch, stroke = ST.N, sw = ST.LW) {   // an architrave: the opening, a band, a keystone (or a little cornice); a sill on brackets
  const r = w / 2, o = 3.2; let inner, outer, key;
  if (arch) {
    inner = stD('M', x, y + h, 'L', x, y + r, 'A', r, r, 0, 0, 1, x + w, y + r, 'L', x + w, y + h, 'Z');
    outer = stD('M', x - o, y + h, 'L', x - o, y + r, 'A', r + o, r + o, 0, 0, 1, x + w + o, y + r, 'L', x + w + o, y + h);
    key = stP(stD('M', x + r - 3, y - o - 2.5, 'L', x + r + 3, y - o - 2.5, 'L', x + r + 2, y + 3, 'L', x + r - 2, y + 3, 'Z'));
  } else {
    inner = stD('M', x, y, 'H', x + w, 'V', y + h, 'H', x, 'Z');
    outer = stD('M', x - o, y + h, 'V', y - o, 'H', x + w + o, 'V', y + h);
    key = stR(x - o - 3, y - o - 4, w + 2 * o + 6, 3);
  }
  return stP(outer, ST.FW, 'none') + '<path d="' + inner + '" fill="#fff" stroke="' + stroke + '" stroke-width="' + sw + '" stroke-linejoin="round"/>' + key
    + stR(x - o - 3, y + h, w + 2 * o + 6, 3) + stP(stD('M', x - o, y + h + 3, 'l', 2, 0, 'l', 0, 3, 'l', -1, 1, 'Z', 'M', x + w + o, y + h + 3, 'l', -2, 0, 'l', 0, 3, 'l', 1, 1, 'Z'), ST.FW, ST.N);
}
const stPawn = (x, y, k) => '<g transform="translate(' + pFix(x) + ' ' + pFix(y) + ') scale(' + k + ')">' + VIC_PAWN + '</g>';
const stPiece = (svg, x, y, k) => '<g transform="translate(' + pFix(x) + ' ' + pFix(y) + ') scale(' + k + ')">' + svg + '</g>';
// a chess square with a number (dark when the number is odd, as on the street's windows); green when done
function stSquare(x, y, s, num, fill, size) {
  const dark = fill || (num % 2 === 1 ? ST.N : '#fff');
  return '<rect x="' + pFix(x) + '" y="' + pFix(y) + '" width="' + s + '" height="' + s + '" fill="' + dark + '" stroke="' + (fill || ST.N) + '" stroke-width="1.1"/>'
    + stT(x + s / 2, y + s * 0.72, String(num), { size: size || s * 0.62, weight: 800, fill: dark === '#fff' ? ST.N : '#fff', anchor: 'middle', serif: true });
}
const WIN_TOP = 36, WIN_LAB = 60, WIN_PL = 10;   // a hall: the plaque, the chapter windows (ctx.winH tall: taller on paper, to colour in), their numbers and names, the plinth
// one chapter window: its frame, its picture, its number on a chess square, its name; the button and Clara go to ctx
function stWindow(ctx, id, x, y, w, h, slot, arch) {
  const v = ctx.view, st = ctx.state[id], on = id === v.here, done = st === 'done', print = st === 'print', num = v.nums[id];
  let s = stFrame(x, y, w, h, arch, on ? ST.C : ST.N, on ? 2.4 : ST.LW);
  const ic = HOUSE_ICONS[id];
  if (ic) s += '<g transform="translate(' + pFix(x + w / 2 - 15) + ' ' + pFix(y + h * (arch ? (on ? 0.2 : 0.42) : (on ? 0.12 : 0.3))) + ') scale(0.62)" fill="none" stroke="' + ST.N + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"' + (st === 'new' && !on ? ' opacity="0.5"' : '') + '>' + ic + '</g>';
  const sq = x + w / 2 - 8;
  s += stSquare(sq, y + h + 12, 16, num, done ? ST.G : null, 10.5);
  if (st === 'started' && !on) s += stC(sq + 16, y + h + 12, 3, 0, ST.C);
  const nm = CH_SHORT[id] || [(DRILLS.find(d => d.id === id) || {}).label || id, ''];
  const name = (done ? '✓ ' : '') + (print ? nm[0] : t(nm[0], nm[1] || nm[0]));
  houseWrap(name, slot - 6, 10.5).forEach((ln, k) => { s += stT(x + w / 2, y + h + 41 + k * 12, ln, { size: 10.5, weight: on || done ? 800 : print ? 700 : 600, fill: on ? ST.C : st === 'new' ? ST.NEW : ST.N, anchor: 'middle' }); });
  if (on) ctx.fig = stPawn(x + w - 9, y + h - 1.5, 0.3);
  const label = num + '. ' + t(nm[0], nm[1] || nm[0]) + (done ? t(', done', ', 완료') : on ? t(', you are here', ', 지금 여기') : '');
  ctx.btns.push({ num, html: '<g data-chapter="' + id + '" data-status="' + st + '" data-here="' + (on ? '1' : '0') + '" role="button" tabindex="0" aria-label="' + penEsc(label).replace(/"/g, '&quot;') + '" style="cursor:pointer"><rect x="' + pFix(x + w / 2 - slot / 2 + 1) + '" y="' + pFix(y - 8) + '" width="' + pFix(slot - 2) + '" height="' + pFix(h + 66) + '" fill="transparent"/></g>' });
  return s;
}
function stRow(ctx, ids, y, x0, x1, arch = true, wmax = 44) {
  const n = ids.length, gap = (x1 - x0) / n, w = Math.min(gap - 20, wmax);
  return ids.map((id, k) => stWindow(ctx, id, x0 + k * gap + (gap - w) / 2, y, w, ctx.winH, gap, arch)).join('');
}
function stPlaque(cx, y, txt) {
  const w = rdWidth(txt, 700, 11.5, true) + 26;
  return stR(cx - w / 2, y, w, 18) + stR(cx - w / 2 + 2, y + 2, w - 4, 14, ST.FW, 'none') + stT(cx, y + 13, txt, { size: 11.5, weight: 700, anchor: 'middle', serif: true, italic: true });
}
function stEntab(x0, x1, y, name, proj = 6) {   // cornice (with dentils), frieze (the building's name in spaced capitals), architrave
  const [c, ch] = stCornice(x0, x1, y, true, proj), f = y + ch;
  return [c + stR(x0 - 1, f, x1 - x0 + 2, 14) + (name ? stT((x0 + x1) / 2, f + 10.2, name.toUpperCase(), { size: 7.6, weight: 800, anchor: 'middle', ls: '0.32em' }) : '')
    + stR(x0 + 1, f + 14, x1 - x0 - 2, 3, ST.FW) + stR(x0 + 3, f + 17, x1 - x0 - 6, 2.5, ST.FW), ch + 19.5];
}
// the storey every building shares: the stage's plaque, the chapter windows, their numbers and names, the plinth
function stHall(ctx, k, body, x0, x1, o = {}) {
  const pad = o.pad != null ? o.pad : 16, arch = o.arch !== false, cols = o.cols, extra = cols ? 8 : 0, cx = (x0 + x1) / 2;
  const WH = ctx.winH, bh = WIN_TOP + extra + WH + WIN_LAB + WIN_PL, base = body + bh, wy = body + WIN_TOP + extra, ids = ctx.view.stages[k].ids;
  let s = stR(x0, body, x1 - x0, bh, ST.LW);
  if (o.glass) {   // glazing above a low stone wall that carries the numbers and names
    const sill = wy + WH + 7.5;
    for (let j = 1; j < 12; j++) s += stL(x0 + j * (x1 - x0) / 12, body + 3, x0 + j * (x1 - x0) / 12, sill, ST.FW);
    s += stL(x0, body + 30, x1, body + 30, ST.FW) + stR(x0 - 2, sill, x1 - x0 + 4, 3.5);
  }
  if (o.quoin) s += stQuoins(x0, body, base - WIN_PL, true) + stQuoins(x1, body, base - WIN_PL, false);
  if (o.pil) s += stPilaster(x0 + 9, body + 2, base - WIN_PL, 9) + stPilaster(x1 - 9, body + 2, base - WIN_PL, 9);
  const stg = ctx.view.stages[k].s;
  s += stPlaque(cx, body + 8, (k + 1) + ' · ' + (ctx.print ? stg.en[0] : t(stg.en[0], stg.ko[0])));
  if (cols) {   // a colonnade standing on a ledge at the sills, carrying a beam over the windows
    const n = ids.length, gap = (x1 - x0 - 2 * pad) / n;
    s += stR(x0 + pad - 8, wy + WH + 7.5, x1 - x0 - 2 * pad + 16, 3) + stR(x0 + pad - 8, wy - (arch ? 13 : 14), x1 - x0 - 2 * pad + 16, 3);
    for (let j = 0; j <= n; j++) s += stColumn(x0 + pad + j * gap, wy - (arch ? 10 : 11), wy + WH + 7.5, cols, !arch);
  }
  s += stRow(ctx, ids, wy, x0 + pad, x1 - pad, arch, o.wmax || 44) + stPlinth(x0, x1, base - WIN_PL, WIN_PL);
  return [s, base];
}
const stName = (ctx, k) => ctx.print ? ST_NAMES[k][0] : t(ST_NAMES[k][0], ST_NAMES[k][1]);
// the seven buildings: each draws itself in a 360-wide cell at ox, from y0 down, and returns [svg, height]
const ST_BUILD = [
  function lodge(ctx, ox, y0) {   // a gabled cottage: carved bargeboards, a finial, the butler's portrait in a roundel, chimneys, quoins
    const X0 = ox + ST.BX0, X1 = ox + ST.BX1, BW = X1 - X0, CX = (X0 + X1) / 2, top = y0 + 14, eave = top + 72;
    let s = stChimney(X0 + 40, eave - 24) + stChimney(X1 - 54, eave - 24) + stP(stD('M', X0 - 10, eave, 'L', CX, top, 'L', X1 + 10, eave, 'Z'), ST.LW);
    [-1, 1].forEach(side => { for (let k = 1; k < 14; k++) {
      const t0 = (k - 1) / 13, t1 = k / 13, xa = CX + side * t0 * (BW / 2 + 10), ya = top + t0 * (eave - top), xb = CX + side * t1 * (BW / 2 + 10), yb = top + t1 * (eave - top);
      s += stP(stD('M', xa, ya + 3, 'Q', (xa + xb) / 2, (ya + yb) / 2 + 8, xb, yb + 3), ST.FW, 'none'); } });
    s += stFinial(CX, top, 12) + stC(CX, top + 42, 20, ST.LW) + stC(CX, top + 42, 23, ST.FW, 'none')
      + '<image href="' + VIC_CAMEO + '" x="' + pFix(CX - 13.5) + '" y="' + pFix(top + 25) + '" height="34" width="27"/>';
    s += stR(X0, eave, BW, 14) + stT(CX, eave + 10.2, stName(ctx, 0).toUpperCase(), { size: 7.6, weight: 800, anchor: 'middle', ls: '0.32em' }) + stR(X0 + 2, eave + 14, BW - 4, 3, ST.FW);
    const [h, base] = stHall(ctx, 0, eave + 17, X0, X1, { quoin: true, pad: 14 });
    return [s + h, base - y0];
  },
  function library(ctx, ox, y0) {   // a balustrade with urns over a full entablature; pilasters at the corners
    const X0 = ox + ST.BX0, X1 = ox + ST.BX1, bt = y0 + 22;
    const [e, eh] = stEntab(X0, X1, bt + 18, stName(ctx, 1)), [h, base] = stHall(ctx, 1, bt + 18 + eh, X0, X1, { pil: true, pad: 20 });
    return [stBalustrade(X0 + 4, X1 - 4, bt, 18) + e + h, base - y0];
  },
  function clocktower(ctx, ox, y0) {   // a spire with a finial, an arcaded belfry, a clock stage between pilasters, over a quoined hall
    const X0 = ox + ST.BX0, X1 = ox + ST.BX1, CX = (X0 + X1) / 2, tw = 62, tx = CX - tw / 2, rt = y0 + 20;
    let s = stP(stD('M', tx - 6, rt + 36, 'L', CX, rt, 'L', tx + tw + 6, rt + 36, 'Z'), ST.LW) + [-22, -11, 11, 22].map(d => stL(CX, rt + 5, CX + d, rt + 36, ST.FW)).join('') + stFinial(CX, rt, 14);
    const bel = rt + 36; s += stR(tx, bel, tw, 30, ST.LW);
    for (let k = 0; k < 3; k++) { const x = tx + 9 + k * 16.5; s += stP(stD('M', x, bel + 26, 'L', x, bel + 13, 'A', 6, 6, 0, 0, 1, x + 12, bel + 13, 'L', x + 12, bel + 26, 'Z')); }
    const [c, ch] = stCornice(tx, tx + tw, bel + 30, false, 4), cs = bel + 30 + ch, cy = cs + 30; s += c;
    s += stR(tx, cs, tw, 60, ST.LW) + stPilaster(tx + 5, cs, cs + 60, 6) + stPilaster(tx + tw - 5, cs, cs + 60, 6) + stC(CX, cy, 21, ST.LW) + stC(CX, cy, 17, ST.FW, 'none');
    for (let k = 0; k < 12; k++) { const a = k * Math.PI / 6; s += stL(CX + 14 * Math.cos(a), cy + 14 * Math.sin(a), CX + 17 * Math.cos(a), cy + 17 * Math.sin(a)); }
    s += stL(CX, cy, CX, cy - 12, 1.6) + stL(CX, cy, CX + 8, cy + 4, 1.6);
    const [e, eh] = stEntab(X0, X1, cs + 60, stName(ctx, 2)), [h, base] = stHall(ctx, 2, cs + 60 + eh, X0, X1, { quoin: true });
    return [s + e + h, base - y0];
  },
  function conservatory(ctx, ox, y0) {   // a palm house: a glass roof with curved shoulders on iron ribs, a raised lantern with a finial
    const X0 = ox + ST.BX0, X1 = ox + ST.BX1, CX = (X0 + X1) / 2, lt = y0 + 30;
    const roof = (x0, x1, ridge, eave, r, ribs) => {
      let s = stP(stD('M', x0, eave, 'Q', x0, ridge, x0 + r, ridge, 'L', x1 - r, ridge, 'Q', x1, ridge, x1, eave), ST.LW)
        + stP(stD('M', x0 + 5, eave, 'Q', x0 + 5, ridge + 5, x0 + r, ridge + 5, 'L', x1 - r, ridge + 5, 'Q', x1 - 5, ridge + 5, x1 - 5, eave), ST.FW, 'none');
      for (let j = 1; j < ribs; j++) {   // each rib stands from the eave to the glass (inverting the quadratic shoulder)
        const x = x0 + j * (x1 - x0) / ribs, d = Math.min(x - x0, x1 - x);
        let y = ridge; if (d < r) { const tt = 1 - Math.sqrt(1 - d / r); y = (1 - tt) * (1 - tt) * eave + 2 * tt * (1 - tt) * ridge + tt * tt * ridge; }
        s += stL(x, eave, x, y, ST.FW);
      }
      return s;
    };
    let s = stFinial(CX, lt, 10) + roof(CX - 46, CX + 46, lt, lt + 22, 16, 10) + stR(CX - 46, lt + 22, 92, 18);
    for (let j = 1; j < 10; j++) s += stL(CX - 46 + j * 9.2, lt + 22, CX - 46 + j * 9.2, lt + 40, ST.FW);
    const ridge = lt + 43, eave = ridge + 44;
    s += stR(CX - 50, lt + 40, 100, 3) + roof(X0, X1, ridge, eave, 50, 24);
    s += stR(X0 - 4, eave, X1 - X0 + 8, 3.5) + stR(X0, eave + 3.5, X1 - X0, 13) + stT(CX, eave + 13.2, stName(ctx, 3).toUpperCase(), { size: 7.6, weight: 800, anchor: 'middle', ls: '0.32em' });
    const [h, base] = stHall(ctx, 3, eave + 16.5, X0, X1, { glass: true, pad: 58, wmax: 50 });
    return [s + h, base - y0];
  },
  function academy(ctx, ox, y0) {   // a temple front: a pediment, a full entablature, Ionic columns between the windows, steps
    const X0 = ox + ST.BX0, X1 = ox + ST.BX1, ped = y0 + 56;
    const [e, eh] = stEntab(X0, X1, ped, stName(ctx, 4), 4), [h, base] = stHall(ctx, 4, ped + eh, X0, X1, { arch: false, wmax: 38, pad: 12, cols: 4.6 });
    return [stPediment(X0 + 6, X1 - 6, ped, 46) + e + h + stSteps((X0 + X1) / 2, base, X1 - X0 - 16, 2), base + 8 - y0];
  },
  function theatre(ctx, ox, y0) {   // a mansard roof with round dormers, an arched attic with a lyre, an arcade on columns
    const X0 = ox + ST.BX0, X1 = ox + ST.BX1, CX = (X0 + X1) / 2, top = y0 + 34, eave = top + 42, ly = top - 1;
    let s = stP(stD('M', CX - 32, top + 2, 'A', 30, 26, 0, 0, 1, CX + 32, top + 2, 'Z'), ST.LW) + stP(stD('M', CX - 26, top + 2, 'A', 25, 21, 0, 0, 1, CX + 26, top + 2), ST.FW, 'none');
    s += '<path d="' + stD('M', CX - 4, ly - 2, 'C', CX - 13, ly - 6, CX - 11, ly - 16, CX - 6, ly - 19, 'M', CX + 4, ly - 2, 'C', CX + 13, ly - 6, CX + 11, ly - 16, CX + 6, ly - 19) + '" fill="none" stroke="' + ST.N + '" stroke-width="1.3" stroke-linecap="round"/>';
    s += stL(CX - 8.5, ly - 14, CX + 8.5, ly - 14) + stR(CX - 5, ly - 2.5, 10, 2.5, ST.FW, ST.N) + [-3, -1, 1, 3].map(d => stL(CX + d, ly - 14, CX + d, ly - 2.5, ST.FW)).join('') + stFinial(CX, top - 24, 8);
    s += stP(stD('M', X0 - 2, eave, 'L', X0 + 16, top + 2, 'L', X1 - 16, top + 2, 'L', X1 + 2, eave, 'Z'), ST.LW) + stR(X0 + 12, top - 1, X1 - X0 - 24, 3);
    [X0 + 58, X1 - 58].forEach(x => { s += stC(x, top + 21, 9) + stC(x, top + 21, 6, ST.FW, 'none') + stL(x - 6, top + 21, x + 6, top + 21, ST.FW) + stL(x, top + 15, x, top + 27, ST.FW) + stR(x - 12, top + 31, 24, 3, ST.FW); });
    const [e, eh] = stEntab(X0, X1, eave, stName(ctx, 5)), [h, base] = stHall(ctx, 5, eave + eh, X0, X1, { wmax: 38, pad: 8, cols: 3.4 });
    return [s + e + h, base - y0];
  },
  function museum(ctx, ox, y0) {   // a ribbed dome on an arcaded drum with a lantern, over a balustrade, an entablature and a quoined hall
    const X0 = ox + ST.BX0, X1 = ox + ST.BX1, CX = (X0 + X1) / 2, lt = y0 + 14, dt = lt + 18, drum = dt + 44, bt = drum + 27;
    let s = stFinial(CX, lt + 4, 8) + stR(CX - 7, lt + 4, 14, 14) + stP(stD('M', CX - 9, lt + 5, 'L', CX, lt - 2, 'L', CX + 9, lt + 5, 'Z'), ST.FW);
    s += stP(stD('M', CX - 52, dt + 44, 'A', 52, 44, 0, 0, 1, CX + 52, dt + 44, 'Z'), ST.LW) + [-36, -18, 18, 36].map(d => stP(stD('M', CX + d, dt + 44, 'Q', CX + d * 0.55, dt + 10, CX, dt + 1), ST.FW, 'none')).join('');
    s += stR(CX - 60, drum, 120, 3) + stR(CX - 58, drum + 3, 116, 24, ST.LW);
    for (let k = 0; k < 6; k++) { const x = CX - 49 + k * 18; s += stP(stD('M', x, drum + 23, 'L', x, drum + 10, 'A', 4, 4, 0, 0, 1, x + 8, drum + 10, 'L', x + 8, drum + 23, 'Z'), ST.FW); }
    const [e, eh] = stEntab(X0, X1, bt + 18, stName(ctx, 6)), [h, base] = stHall(ctx, 6, bt + 18 + eh, X0, X1, { quoin: true });
    return [s + stBalustrade(X0 + 4, X1 - 4, bt, 18) + e + h, base - y0];
  },
];
function stLamp(x, y) {
  return stR(x - 4, y - 4, 8, 4) + stL(x, y - 4, x, y - 50, 1.8) + stL(x - 2, y - 30, x + 2, y - 30) + stP(stD('M', x - 6, y - 52, 'L', x + 6, y - 52, 'L', x + 4, y - 64, 'L', x - 4, y - 64, 'Z'))
    + '<path d="' + stD('M', x, y - 54, 'q', 3, -5, 0, -9, 'q', -3, 4, 0, 9, 'z') + '" fill="' + ST.C + '" stroke="none"/>' + stP(stD('M', x - 6, y - 64, 'L', x, y - 70, 'L', x + 6, y - 64, 'Z'), ST.MW, ST.N);
}
function stPavement(x0, x1, y) {
  const id = 'stpv' + Math.round(x0) + '_' + Math.round(y);
  return '<defs><pattern id="' + id + '" x="' + pFix(x0) + '" y="' + pFix(y) + '" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="' + ST.N + '" stroke="none"/><rect x="7" y="7" width="7" height="7" fill="' + ST.N + '" stroke="none"/></pattern></defs>'
    + '<rect x="' + pFix(x0) + '" y="' + pFix(y) + '" width="' + pFix(x1 - x0) + '" height="14" fill="url(#' + id + ')" stroke="' + ST.N + '" stroke-width="0.8"/>';
}
// The street. layout: false or 'tall' -- one street, the Lodge at the foot, the Museum at the top (phones, the app);
// true or 'wide' -- three stretches of street, one above another (stages 1-3, 4-5, 6-7), for the guide's front page;
// 'og' -- two stretches (1-4, 5-7), the guide's sharing picture; 'print1' / 'print2' -- the Workbook's two pages to
// colour in (1-2 then 3-4; 5-6 then 7). Each stretch is read left to right, and the street climbs from stretch to
// stretch, bottom to top. view: { stages, here, nums, print }.
function houseShapes(view, layout) {
  const L = layout === true ? 'wide' : layout || 'tall';
  const ROWS = { tall: [[0], [1], [2], [3], [4], [5], [6]], wide: [[0, 1, 2], [3, 4], [5, 6]], og: [[0, 1, 2, 3], [4, 5, 6]], print1: [[0, 1], [2, 3]], print2: [[4, 5], [6]] }[L];
  const state = {}; view.stages.forEach(x => x.ids.forEach((id, j) => { state[id] = x.st[j]; }));
  const ctx = { view, state, btns: [], fig: null, print: !!view.print, winH: L === 'print1' || L === 'print2' ? 72 : 58 };
  // measure each building (drawn once off-page), then stand every stretch's buildings on its own pavement
  const BH = {}; ROWS.flat().forEach(k => { BH[k] = ST_BUILD[k](ctx, 0, 0)[1]; });
  ctx.btns = []; ctx.fig = null;
  const W = ST.CW * Math.max(...ROWS.map(r => r.length)), shapes = [], grounds = [];
  let y = 18;
  [...ROWS].reverse().forEach(row => {   // the top stretch first
    const ground = y + Math.max(...row.map(k => BH[k])), ox0 = L === 'print2' && row.length === 1 ? 0 : (W - row.length * ST.CW) / 2;
    row.forEach((k, j) => {
      const ox = ox0 + j * ST.CW, [svg] = ST_BUILD[k](ctx, ox, ground - BH[k]);
      shapes.push({ k: 'g', floor: k, kids: [{ k: 'raw', svg: stG(svg) }] });
    });
    let pav = stPavement(ox0 + 4, ox0 + row.length * ST.CW - 4, ground + 4);
    if (row.length === 1) pav += stLamp(ox0 + (row[0] % 2 ? 14 : ST.CW - 14), ground + 4);
    else for (let j = 0; j <= row.length; j++) pav += stLamp(ox0 + j * ST.CW + (j === 0 ? 14 : j === row.length ? -14 : 0), ground + 4);
    shapes.push({ k: 'raw', svg: stG(pav) });
    grounds.push(ground); y = ground + 44;
  });
  const ground = grounds[grounds.length - 1];
  if (L === 'print2') {   // the King and the Queen wait beside the Museum, at the top of the street
    const cx = ST.CW * 1.5, y = grounds[0] - 70;
    shapes.push({ k: 'raw', svg: stPiece(VIC_KING, cx - 34, y, 0.62) + stPiece(VIC_QUEEN, cx + 34, y, 0.62)
      + stT(cx, y + 26, 'The King and the Queen', { size: 15, weight: 700, anchor: 'middle', serif: true, italic: true }) + stT(cx, y + 44, 'wait at the top of the street.', { size: 15, weight: 700, anchor: 'middle', serif: true, italic: true }) });
  }
  if (ctx.fig) shapes.push({ k: 'g', testid: 'map-figure', kids: [{ k: 'raw', svg: ctx.fig }] });
  ctx.btns.sort((a, b) => a.num - b.num).forEach(b => shapes.push({ k: 'raw', svg: b.html }));   // the buttons in chapter order, 1 to 26
  let foot = ground + 14;
  if (L === 'print1') {   // the butler welcomes you at the foot of the street
    shapes.push({ k: 'raw', svg: '<image href="' + VIC_CAMEO + '" x="40" y="' + pFix(ground + 22) + '" height="84" width="66.6"/>'
      + stT(122, ground + 58, 'Your butler welcomes you at the Lodge.', { size: 17, weight: 700, serif: true, italic: true }) + stT(122, ground + 80, 'Start here, then walk along the street and up: one window at a time.', { size: 13, weight: 600, fill: ST.M }) });
    foot = ground + 112;
  }
  if (L === 'print2') {   // and Clara at the end of her walk
    shapes.push({ k: 'raw', svg: stPawn(76, ground + 100, 1.25)
      + stT(122, ground + 58, 'Every window coloured in?', { size: 17, weight: 700, serif: true, italic: true }) + stT(122, ground + 80, 'Then Clara has walked the whole street --', { size: 13, weight: 600, fill: ST.M }) + stT(122, ground + 97, 'and a pawn that crosses the board becomes a queen.', { size: 13, weight: 600, fill: ST.M }) });
    foot = ground + 112;
  }
  if (L === 'tall' || L === 'wide') {
    const cap = L === 'wide' ? 'Start at the Lodge, bottom left: walk along the street, then up.' : 'Start at the Lodge and walk up the street.';
    shapes.push({ k: 'raw', svg: stT(W / 2, foot, view.print ? cap : t(cap, '버틀러의 집에서 출발해 거리를 따라 올라가요.'), { size: 11.5, weight: 600, fill: ST.M, anchor: 'middle' }) });
    foot += 8;
  }
  return { shapes, W, H: foot };
}
// "Clara's journey": the 26 chapters as squares on a chessboard, seven ranks (one a stage), walked from the bottom up and
// back and forth; Clara stands on your square, the King and Queen wait at the far end; the words beside the board.
// btn: the squares are the chapters' buttons (the student page, where the board is the whole map); otherwise a tap finds
// the chapter on the street.
function boardSvg(view, btn) {
  const SQ = 30, N = 5, state = {}; view.stages.forEach(x => x.ids.forEach((id, j) => { state[id] = x.st[j]; }));
  const here = view.here;
  const W = 360, bx = 14, by = 46, bh = 7 * SQ;
  let s = '', btns = [], fig = '';
  s += stR(bx - 7, by - 7, N * SQ + 14, bh + 14, 1.6) + stR(bx - 3.5, by - 3.5, N * SQ + 7, bh + 7, 0.55, 'none');
  view.stages.forEach((x, k) => {
    const ry = by + (6 - k) * SQ, ltr = k % 2 === 0;
    for (let c = 0; c < N; c++) {
      const sx = bx + c * SQ, dark = (c + k) % 2 === 0, slot = ltr ? c : N - 1 - c, id = x.ids[slot];
      const st = id ? state[id] : null, on = id && id === here;
      s += '<rect x="' + pFix(sx) + '" y="' + pFix(ry) + '" width="' + SQ + '" height="' + SQ + '" fill="' + (st === 'done' ? ST.G : dark ? ST.N : '#fff') + '"' + (dark || st === 'done' ? ' stroke="none"' : ' stroke-width="0.4"') + '/>';
      if (!id) continue;
      const fg = st === 'done' || dark ? '#fff' : ST.N;
      if (on) s += '<rect x="' + pFix(sx + 1.5) + '" y="' + pFix(ry + 1.5) + '" width="' + (SQ - 3) + '" height="' + (SQ - 3) + '" fill="#fff" stroke="' + ST.C + '" stroke-width="2.4"/>';
      s += stT(sx + 4, ry + 12, String(view.nums[id]), { size: 10, weight: 800, fill: on ? ST.C : fg, serif: true });
      if (on) fig = stPawn(sx + SQ / 2 + 6, ry + SQ - 3, 0.38);
      const nm = CH_SHORT[id] || [id, ''];
      btns.push({ num: view.nums[id], id, st, on, x: sx, y: ry, label: view.nums[id] + '. ' + t(nm[0], nm[1] || nm[0]) + (st === 'done' ? t(', done', ', 완료') : on ? t(', you are here', ', 지금 여기') : '') });
    }
  });
  // the King and the Queen at the far end of the board
  const kx = bx + N * SQ / 2, ky = by - 12;
  s += stPiece(VIC_KING, kx - 13, ky, 0.32) + stPiece(VIC_QUEEN, kx + 13, ky, 0.32);
  // the words
  const cur = here ? CH_SHORT[here] || [here, ''] : null, stage = here ? view.stages.findIndex(x => x.ids.includes(here)) : -1;
  const lines = [];
  if (here) lines.push([view.nums[here] + ' · ' + t(cur[0], cur[1] || cur[0]), { size: 14, weight: 800, fill: ST.C }], [t(ST_AT[stage], ST_NAMES[stage][1] + '에서'), { size: 11.5, weight: 600, fill: ST.M }]);
  else lines.push([t('The board is crossed!', '체스판을 다 건넜어요!'), { size: 14, weight: 800, fill: ST.G }]);
  const note = t('A pawn that crosses the board becomes a queen.', '폰이 체스판 끝까지 가면 퀸이 돼요.');
  const tx = bx + N * SQ + 20, tw = W - tx - 6;
  s += stT(tx, 30, t('Clara’s journey', '클라라의 여행'), { size: 18, weight: 800, serif: true, italic: true });
  lines.forEach(([txt, o], j) => houseWrap(txt, tw, o.size).forEach((ln, i) => { s += stT(tx, 64 + j * 22 + i * 15, ln, o); }));
  houseWrap(note, tw, 10.5).forEach((ln, j) => { s += stT(tx, by + bh - 26 + j * 13, ln, { size: 10.5, weight: 600, fill: ST.M }); });
  const H = by + bh + 16;
  if (fig) s += '<g data-testid="board-clara">' + fig + '</g>';
  s += btns.sort((a, b) => a.num - b.num).map(b => btn
    ? '<g data-chapter="' + b.id + '" data-status="' + b.st + '" data-here="' + (b.on ? '1' : '0') + '" role="button" tabindex="0" aria-label="' + penEsc(b.label).replace(/"/g, '&quot;') + '" style="cursor:pointer"><rect x="' + pFix(b.x) + '" y="' + pFix(b.y) + '" width="' + SQ + '" height="' + SQ + '" fill="transparent"/></g>'
    : '<g data-goto="' + b.id + '" style="cursor:pointer"><rect x="' + pFix(b.x) + '" y="' + pFix(b.y) + '" width="' + SQ + '" height="' + SQ + '" fill="transparent"/></g>').join('');
  return { svg: stG(s), W, H };
}
function HouseMap({ onOpen, compact, noIntro }) {
  const box = useRef(null);
  const [, setFontTick] = useState(0);
  useEffect(() => { try { document.fonts && document.fonts.ready.then(() => { rdCtx = null; setFontTick(n => n + 1); }); } catch (e) {} }, []);
  const stages = PATH_STAGES.map((s, i) => { const ids = pathStageIds(s); return { s, i, ids, st: ids.map(id => chapterState(id).status) }; });
  const all = stages.flatMap(x => x.ids), nums = {}; all.forEach((id, k) => { nums[id] = k + 1; });
  const finished = stages.reduce((a, x) => a + x.st.filter(v => v === 'done').length, 0);
  let last = null; try { last = localStorage.getItem(LAST_CHAPTER_KEY); } catch (e) {}
  const here = last && all.includes(last) && chapterState(last).status !== 'done' ? last : all.find(id => chapterState(id).status !== 'done');
  const sig = stages.map(x => x.st.join(',')).join('|') + here + LANG + compact;
  const view = { stages, here, nums };
  const house = useMemo(() => compact ? null : houseShapes(view, 'tall'), [sig]);
  const board = useMemo(() => boardSvg(view, !!compact), [sig]);
  const open = (e) => {
    const g = e.target.closest && e.target.closest('[data-chapter]'); if (g) { onOpen(g.getAttribute('data-chapter')); return; }
    const q = e.target.closest && e.target.closest('[data-goto]');   // a square on the board: find that window on the street
    if (q && box.current) { const w = box.current.querySelector('[data-street] [data-chapter="' + q.getAttribute('data-goto') + '"]'); if (w) { try { w.scrollIntoView({ block: 'center', behavior: 'smooth' }); } catch (x) { w.scrollIntoView(); } try { w.focus({ preventScroll: true }); } catch (x) {} } }
  };
  const key = (e) => { if ((e.key === 'Enter' || e.key === ' ') && e.target.getAttribute && e.target.getAttribute('data-chapter')) { e.preventDefault(); onOpen(e.target.getAttribute('data-chapter')); } };
  const boardEl = <div data-testid="map-board" aria-hidden={compact ? undefined : true} style={{lineHeight:0}} dangerouslySetInnerHTML={{__html: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + board.W + ' ' + board.H + '" width="100%" role="group" aria-label="' + penEsc(t('Clara’s journey: the chapter map', '클라라의 여행: 챕터 지도')) + '">' + board.svg + '</svg>'}}/>;
  return (
    <div data-testid="music-map" data-layout="tall" data-house ref={box} className={compact ? '' : 'fade-up'} onClick={open} onKeyDown={key}>
      <style>{'[data-house] [data-chapter]:focus-visible{outline:none}[data-house] [data-chapter]:focus-visible rect{stroke:#e4572e;stroke-width:3}'}</style>
      {!compact && !noIntro && <PageIntro title={UI_TEACHER ? t('Music map', '음악 지도') : t('My music map', '나의 음악 지도')} text={t('The Piano Butler’s street: every building is a stage, every window is a chapter. Tap a window to open it.', '피아노 버틀러의 거리: 건물마다 단계 하나, 창문마다 챕터 하나. 창문을 누르면 열려요.')}/>}
      <div data-testid="map-count" style={{fontSize:12.5,fontWeight:600,color:'#6d6f9c',maxWidth:440,margin:'0 auto 4px',paddingLeft:'2%',boxSizing:'border-box'}}>{t(finished + ' of ' + all.length + ' chapters done', all.length + '개 챕터 중 ' + finished + '개 완료')}</div>
      {compact ? <div style={{maxWidth:440,margin:'0 auto'}}>{boardEl}</div>
        : <div style={{maxWidth:440,margin:'0 auto'}}>
          <div style={{marginBottom:14}}>{boardEl}</div>
          <div data-street role="group" aria-label={t('The Piano Butler’s street: the chapter map', '피아노 버틀러의 거리: 챕터 지도')}>
            <PenArt shapes={house.shapes} vb={[0, 0, house.W, house.H]} inter/>
          </div>
        </div>}
    </div>
  );
}
// ─── the street in the books ───
// The small map at the foot of a chapter's map page: one row per stage, a chess square with each chapter's number,
// your chapter in coral -- the same order as the app's street.
function houseMiniShapes(current, W = 600) {
  const s = [], X0 = 4, HW = W - 8, SC = 118, FH = 19, TOP = 4;
  const stages = PATH_STAGES.map((st, i) => ({ st, i, ids: pathStageIds(st) }));
  let n = 0; const nums = {}; stages.forEach(x => x.ids.forEach(id => { nums[id] = ++n; }));
  let y = TOP, svg = '';
  [...stages].reverse().forEach(x => {
    const has = x.ids.includes(current), rw = (HW - SC) / 5;
    svg += stL(X0, y + FH, X0 + HW, y + FH, 0.6);
    svg += stT(X0 + 2, y + 13, (x.i + 1) + ' · ' + x.st.en[0], { size: 10, weight: 800, fill: has ? ST.C : ST.N, serif: true, italic: true });
    x.ids.forEach((id, j) => {
      const rx = X0 + SC + j * rw, on = id === current, nm = (CH_SHORT[id] || [bkChapterName(id)])[0];
      if (on) svg += '<rect x="' + pFix(rx) + '" y="' + pFix(y + 1.5) + '" width="' + pFix(rw - 3) + '" height="' + (FH - 3) + '" fill="#fff" stroke="' + ST.C + '" stroke-width="1.3"/>';
      svg += stSquare(rx + 2.5, y + 3.5, 12, nums[id], null, 8.5) + stT(rx + 18.5, y + 13, nm, { size: 9.2, weight: on ? 800 : 600, fill: on ? ST.C : ST.N });
    });
    y += FH;
  });
  s.push({ k: 'raw', svg: stG(stL(X0, TOP, X0 + HW, TOP, 1.2) + svg + stL(X0, y + 1.5, X0 + HW, y + 1.5, 1.2)) });
  return { shapes: s, W, H: y + 4 };
}
function BkHouse({ current, compact }) {
  const h = useMemo(() => houseMiniShapes(current), [current]);
  return (
    <div data-bk-house style={{border:'1.5px solid ' + BK.line,borderRadius:3,padding:compact ? '8px 12px 6px' : '10px 14px 8px'}}>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',marginBottom:4}}><div style={bkH(compact ? 15 : 17, 4)}>The Piano Butler’s street</div><span style={{fontSize:10.5,color:BK.muted}}>every building a stage, every window a chapter -- the same order as the app</span></div>
      <PenArt shapes={h.shapes} vb={[0, 0, h.W, h.H]} label="The Piano Butler’s street: the chapter map"/>
    </div>
  );
}
// the whole street to colour in (the Workbook's opening pages): stages 1-4 on the first page, 5-7 on the second
function BkHousePage({ part = 1 }) {
  const stages = PATH_STAGES.map((s, i) => { const ids = pathStageIds(s); return { s, i, ids, st: ids.map(() => 'print') }; });
  const nums = {}; stages.flatMap(x => x.ids).forEach((id, k) => { nums[id] = k + 1; });
  const street = useMemo(() => houseShapes({ stages, here: null, nums, print: true }, part === 1 ? 'print1' : 'print2'), [part]);
  return <>
    <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em',marginTop:4}}>{part === 1 ? 'YOUR MAP' : 'YOUR MAP, GOING UP'}</div>
    <h1 style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:32,fontWeight:900,color:BK.ink,margin:'2px 0 4px',lineHeight:1.05}}>{part === 1 ? 'The Piano Butler’s street' : 'The top of the street'}</h1>
    <p style={{fontSize:13.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>{part === 1
      ? <>Every building is a stage and every window is a chapter. Start at the Lodge, bottom left, and go along to the Library; then up to the Clock Tower and the Conservatory. When you finish a chapter, <b style={{color:BK.ink}}>colour in its window</b>. Draw a little pawn -- that’s you -- in the window you are working on.</>
      : <>Next come the Academy and the Theatre, and at the very top of the street, the Museum. <b style={{color:BK.ink}}>Colour in each window</b> when you finish its chapter.</>}</p>
    <div style={{flex:1,minHeight:0,display:'flex',alignItems:'center',justifyContent:'center'}}><PenArt shapes={street.shapes} vb={[0, 0, street.W, street.H]} label="The Piano Butler’s street" style={{maxHeight:'100%'}}/></div>
  </>;
}
