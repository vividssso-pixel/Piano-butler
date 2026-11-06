// ─── Phase 376: the Lesson Book's pen-and-ink drawings, drawn live (so the online lesson can move them) ───
// The book's drawings are baked once in Python (chars/chars8.py: KID -> to_pen -> bake). This is the same recipe in
// JS, so a picture that moves on screen is the book's picture: the same sister and brother, the same hatching, and
// the same hand-drawn wobble (the same noise field, exported from Python as PEN_FIELD).
//   penKid(j, face, who) -> shapes        the two siblings, from a joints dict (hip, neck, head, arms, legs)
//   penSvg(shapes, opts) -> '<svg ...>'   pen-and-ink: hatch the big navy areas, then wobble every outline
const PEN_N = '#26296b', PEN_C = '#e4572e', PEN_P = '#fffdf7';
const PEN_FIELD = __PEN_FIELD__;
function penField(x, y) {
  const f = (cc) => { let v = 0; for (let i = 0; i < cc.length; i++) { const c = cc[i]; v += c[3] * Math.sin(c[0] * x + c[1] * y + c[2]); } return v; };
  return [f(PEN_FIELD[0]), f(PEN_FIELD[1])];
}
const pAdd = (a, b, k = 1) => [a[0] + b[0] * k, a[1] + b[1] * k];
const pSub = (a, b) => [a[0] - b[0], a[1] - b[1]];
const pUnit = (v) => { const l = Math.hypot(v[0], v[1]) || 1; return [v[0] / l, v[1] / l]; };
const pFix = (v) => { const s = (Math.round(v * 10) / 10).toFixed(1); return s === '-0.0' ? '0' : s.endsWith('.0') ? s.slice(0, -2) : s; };

// ---- shapes: plain objects, drawn flat first (like the Python SVG before to_pen) ----
// pl: polyline {p, s, w}  ln: line {p:[a,b], s, w, dash}  el: ellipse {c, rx, ry, f, s, w, m}  pa: path {seg, f, s, w, m}
// hr: a hair-like path drawn rigid {d, f, s, w, m}  rc: rect {x, y, w, h, rx, f, s, sw}  tx: text  g: group {who, hide, kids}
const PEN_HAIR = {
  LONG_SIDE: 'M4.6,-8.6 C-2,-13 -11.6,-9 -11.2,1 C-11,8 -11.8,16 -12.6,23.4 C-9.8,25 -6.2,24.8 -3.6,23.4 C-4.6,15 -4.8,8 -3.8,2.2 C-3,-2.2 0,-5.4 5.8,-5.8 Z',
  LONG_FRONT: 'M-9.6,6 C-11.4,-9 -5,-12.8 0,-12.6 C5,-12.8 11.4,-9 9.6,6 L10.8,18.6 C8.8,20 6.4,19.6 5.4,18 L5.6,4 C5.4,-1 3.6,-4.6 0,-5.4 C-3.6,-4.6 -5.4,-1 -5.6,4 L-5.4,18 C-6.4,19.6 -8.8,20 -10.8,18.6 Z',
  BAND_SIDE: 'M1.9,-10.4 C-0.4,-7.8 -2.4,-4.2 -3.4,0.4 L-5.9,0 C-4.9,-5 -2.6,-8.8 -0.4,-11.6 Z',
  BAND_FRONT: 'M-9.3,-4.2 C-6,-10.6 6,-10.6 9.3,-4.2 L8,-2.2 C5,-7.8 -5,-7.8 -8,-2.2 Z',
  SHORT_SIDE: 'M6.4,-6.4 C3,-12.6 -9,-12 -9.6,-1.6 C-9.4,1.6 -8.6,3 -7.4,3.4 C-6.6,0 -5,-3.4 -1.6,-4.4 C1.6,-5.4 4.4,-5.2 6.4,-6.4 Z',
  SHORT_FRONT: 'M-8.6,-1 C-9.6,-9.6 -4.6,-12.6 0,-12.4 C4.6,-12.6 9.6,-9.6 8.6,-1 C7,-4.4 4,-5.6 0,-5.4 C-4,-5.6 -7,-4.4 -8.6,-1 Z',
};
const PEN_SW = 2.2;
// a limb: navy outline (w + 2*ow), then the fill inside (unless the fill is navy too)
function penLimb(chain, w, fill, out = PEN_N, ow = 2.2) {
  const a = [{ k: 'pl', p: chain, s: out, w: w + 2 * ow }];
  if (fill !== out) a.push({ k: 'pl', p: chain, s: fill, w });
  return a;
}
const penLine = (a, b, w = 3.2, c = PEN_N, dash) => ({ k: 'ln', p: [a, b], s: c, w, dash });
// head group matrix: translate(hc) rotate(ang) [scale(face, 1)]
function penHeadM(hc, u, face) {
  const ang = Math.atan2(u[1], u[0]) - Math.PI / 2, c = Math.cos(ang), s = Math.sin(ang), sx = face ? face : 1;
  return [c * sx, s * sx, -s, c, hc[0], hc[1]];
}
function penTorso(nk, hp) {
  const u = pUnit(pSub(hp, nk)), p = [-u[1], u[0]];
  const sh1 = pAdd(pAdd(nk, p, 10), u, 2), sh2 = pAdd(pAdd(nk, p, -10), u, 2);
  const h1 = pAdd(hp, p, 11.5), h2 = pAdd(hp, p, -11.5);
  const top = pAdd(nk, u, -2.5), c1 = pAdd(sh1, u, 18), c2 = pAdd(sh2, u, 18);
  return { seg: [['M', sh1], ['Q', c1, h1], ['L', h2], ['Q', c2, sh2], ['Q', top, sh1], ['Z']], h: [h1, h2] };
}
function penHull(points) {
  const key = (q) => q[0] + ',' + q[1];
  const seen = {}, ps = [];
  points.forEach(q => { const r = [Math.round(q[0] * 10) / 10, Math.round(q[1] * 10) / 10]; if (!seen[key(r)]) { seen[key(r)] = 1; ps.push(r); } });
  ps.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const cross = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
  const lo = [], up = [];
  for (const q of ps) { while (lo.length >= 2 && cross(lo[lo.length - 2], lo[lo.length - 1], q) <= 0) lo.pop(); lo.push(q); }
  for (let i = ps.length - 1; i >= 0; i--) { const q = ps[i]; while (up.length >= 2 && cross(up[up.length - 2], up[up.length - 1], q) <= 0) up.pop(); up.push(q); }
  return lo.slice(0, -1).concat(up.slice(0, -1));
}
const penShoe = (a, face) => ({ k: 'el', c: [a[0] + 4 * (face || 0), a[1] + 1], rx: face ? 6 : 4.4, ry: 3, f: PEN_N });
// the girl: long hair and a headband, a white blouse under an A-line pinafore, knee socks
function penGirl(j, face) {
  const u = pUnit(pSub(j.hip, j.neck)), legs = j.legs, arms = j.arms, out = [];
  const leg = (ch) => { const [hip, knee, ank] = ch; out.push(...penLimb(ch, 5, PEN_P), ...penLimb([pAdd(knee, pSub(ank, knee), 0.16), ank], 5.4, PEN_N), penShoe(ank, face)); };
  const arm = (ch) => { const [sh, el, wr] = ch; const hand = ch[3] || pAdd(wr, pUnit(pSub(wr, el)), 4); out.push(...penLimb([sh, el, wr], 5.2, PEN_P), ...penLimb([wr, hand], 3.6, PEN_P, PEN_N, 1.6)); };
  if (legs.length > 1) leg(legs[1]);
  if (arms.length > 1 && face !== 0) arm(arms[1]);
  leg(legs[0]);
  out.push({ k: 'pa', seg: penTorso(j.neck, j.hip).seg, f: PEN_P, s: PEN_N, w: PEN_SW });
  // the A-line pinafore: a hull from the shoulders to a short flared hem, with pale pleats
  const nk = j.neck, hp = j.hip, p = [-u[1], u[0]];
  const ps = [pAdd(pAdd(nk, p, 5.6), u, 3), pAdd(pAdd(nk, p, -5.6), u, 3), pAdd(pAdd(nk, p, 10.5), u, 17), pAdd(pAdd(nk, p, -10.5), u, 17), pAdd(hp, p, 12), pAdd(hp, p, -12)];
  const hems = [];
  legs.forEach(lg => { const t = pUnit(pSub(lg[1], lg[0])), n = [-t[1], t[0]], hm = pAdd(lg[0], pSub(lg[1], lg[0]), 0.46); ps.push(pAdd(hm, n, 9), pAdd(hm, n, -9)); hems.push([hm, t, n]); });
  const hull = penHull(ps);
  out.push({ k: 'pa', seg: hull.map((q, i) => [i ? 'L' : 'M', q]).concat([['Z']]), f: PEN_N, s: PEN_N, w: PEN_SW });
  const [hm, t, n] = hems[0];
  [-0.62, -0.2, 0.2, 0.62].forEach(k => { const a = pAdd(pAdd(hm, n, 9 * k), t, -1.6); out.push(penLine(a, pAdd(a, t, -8), 1.3, PEN_P)); });
  if (face === 0 && arms.length > 1) arm(arms[1]);
  arm(arms[0]);
  out.push(penLine(pAdd(j.head, u, 8), j.neck, 3.4, PEN_N));
  // the collar and its little ribbon
  [1, -1].forEach(sx => {
    const a = pAdd(nk, p, sx * 0.8), b = pAdd(pAdd(nk, p, sx * 8.4), u, 0.6), c = pAdd(pAdd(nk, p, sx * 6.6), u, 6.6), d0 = pAdd(pAdd(nk, p, sx * 1.4), u, 5.4);
    out.push({ k: 'pa', seg: [['M', a], ['Q', b, c], ['Q', d0, a], ['Z']], f: PEN_P, s: PEN_N, w: 1.1 });
  });
  const c0 = pAdd(nk, u, 4.6);
  [1, -1].forEach(sx => { const q1 = pAdd(c0, [p[0] * 3.4 * sx + u[0] * -1.8, p[1] * 3.4 * sx + u[1] * -1.8]); out.push({ k: 'pa', seg: [['M', c0], ['L', q1], ['L', pAdd(q1, u, 3.6)], ['Z']], f: PEN_P, s: PEN_N, w: 1 }); });
  const m = penHeadM(j.head, u, face);
  out.push({ k: 'el', c: [0, 0], rx: 8, ry: 9.6, f: PEN_P, s: PEN_N, w: PEN_SW, m });
  out.push({ k: 'hr', d: face === 0 ? PEN_HAIR.LONG_FRONT : PEN_HAIR.LONG_SIDE, f: PEN_N, m });
  out.push({ k: 'hr', d: face === 0 ? PEN_HAIR.BAND_FRONT : PEN_HAIR.BAND_SIDE, f: PEN_P, s: PEN_N, w: 1.1, m });
  return out;
}
// the boy: short hair, a jumper and trousers
function penBoy(j, face) {
  const u = pUnit(pSub(j.hip, j.neck)), legs = j.legs, arms = j.arms, out = [];
  const leg = (ch) => { out.push(...penLimb(ch, 5, PEN_N), penShoe(ch[ch.length - 1], face)); };
  const arm = (ch) => { const [sh, el, wr] = ch; const hand = ch[3] || pAdd(wr, pUnit(pSub(wr, el)), 4); out.push(...penLimb([sh, el, wr], 5.2, PEN_N), ...penLimb([wr, hand], 3.6, PEN_P, PEN_N, 1.6)); };
  if (legs.length > 1) leg(legs[1]);
  if (arms.length > 1 && face !== 0) arm(arms[1]);
  leg(legs[0]);
  out.push({ k: 'pa', seg: penTorso(j.neck, j.hip).seg, f: PEN_N, s: PEN_N, w: PEN_SW });   // the jumper
  if (face === 0 && arms.length > 1) arm(arms[1]);
  arm(arms[0]);
  out.push(penLine(pAdd(j.head, u, 8), j.neck, 3.4, PEN_N));
  const m = penHeadM(j.head, u, face);
  out.push({ k: 'el', c: [0, 0], rx: 8, ry: 9.6, f: PEN_P, s: PEN_N, w: PEN_SW, m });
  out.push({ k: 'hr', d: face === 0 ? PEN_HAIR.SHORT_FRONT : PEN_HAIR.SHORT_SIDE, f: PEN_N, m });
  return out;
}
// both children in one drawing; ?kid=girl|boy (PB_KID_CSS) shows one of them everywhere
function penKid(j, face = 1, who = 'girl') {
  return [{ k: 'g', who: 'girl', hide: who !== 'girl', kids: penGirl(j, face) }, { k: 'g', who: 'boy', hide: who !== 'boy', kids: penBoy(j, face) }];
}
// joint dots (white = fine, coral = this one is wrong or is the thing to look at)
function penJoints(j, coral = [], skip = []) {
  const pts = { shoulder: j.arms[0][0], elbow: j.arms[0][1], wrist: j.arms[0][2], hip: j.legs[0][0], knee: j.legs[0][1], ankle: j.legs[0][2] };
  return Object.keys(pts).filter(k => !skip.includes(k)).map(k => ({ k: 'el', c: pts[k], rx: 3.2, ry: 3.2, f: coral.includes(k) ? PEN_C : PEN_P, s: PEN_N, w: 1.3 }));
}
const penText = (x, y, text, o = {}) => ({ k: 'tx', x, y, text, size: o.size || 8.5, weight: o.weight || 800, fill: o.fill || PEN_C, anchor: o.anchor || 'start', serif: o.serif, italic: o.italic, halo: o.halo });
// shapes drawn smaller somewhere else: every point scaled by k about src and moved to dst, line widths scaled too
function penPlace(list, k, src, dst) {
  const P = (q) => [dst[0] + (q[0] - src[0]) * k, dst[1] + (q[1] - src[1]) * k];
  const M = (m) => m ? [m[0] * k, m[1] * k, m[2] * k, m[3] * k, dst[0] + (m[4] - src[0]) * k, dst[1] + (m[5] - src[1]) * k] : null;
  const sc = (v) => v === 'H' ? 'H@' + (+k.toFixed(2)) : v;
  return penHatch(list).map(e0 => {
    const e = { ...e0, s: sc(e0.s), f: sc(e0.f) };
    if (e.k === 'g') return { ...e, kids: penPlace(e.kids, k, src, dst) };
    if (e.k === 'pl' || e.k === 'ln') return { ...e, p: e.p.map(P), w: e.w * k };
    if (e.k === 'pa') return e.m ? { ...e, m: M(e.m), w: (e.w || 0) * k } : { ...e, seg: e.seg.map(sg => [sg[0], ...sg.slice(1).map(P)]), w: (e.w || 0) * k };
    if (e.k === 'el') return e.m ? { ...e, m: M(e.m), w: e.w != null ? e.w * k : e.w } : { ...e, c: P(e.c), rx: e.rx * k, ry: e.ry * k, w: e.w != null ? e.w * k : e.w };
    if (e.k === 'hr') return { ...e, m: M(e.m), w: e.w != null ? e.w * k : e.w };
    if (e.k === 'rc') return e.m ? { ...e, m: M(e.m), sw: (e.sw || 0) * k } : { ...e, x: P([e.x, e.y])[0], y: P([e.x, e.y])[1], w: e.w * k, h: e.h * k, rx: (e.rx || 0) * k, sw: (e.sw || 0) * k };
    if (e.k === 'tx') return { ...e, x: P([e.x, e.y])[0], y: P([e.x, e.y])[1], size: e.size * k };
    return e;
  });
}
// props, as in chars5.py
const penFloor = (W, y = 162) => [penLine([6, y], [W - 6, y], 1.6, '#bdb7a6')];
function penPiano(x = 150, y = 58, floorY = 162, keyY = 98) {
  const a = [{ k: 'rc', x, y, w: 56, h: floorY - y, rx: 2.5, f: PEN_P, s: PEN_N, sw: 2.4 }, { k: 'rc', x: x - 26, y: keyY, w: 30, h: 8.5, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2 }];
  for (let i = 1; i < 4; i++) a.push(penLine([x - 26 + i * 7.5, keyY], [x - 26 + i * 7.5, keyY + 8.5], 1.2));
  return a;
}
function penStool(x1 = 46, x2 = 100, y = 114, floorY = 162) {
  return [{ k: 'rc', x: x1, y, w: x2 - x1, h: 7, rx: 2, f: PEN_P, s: PEN_N, sw: 2.4 }, penLine([x1 + 7, y + 7], [x1 + 7, floorY], 2.4), penLine([x2 - 7, y + 7], [x2 - 7, floorY], 2.4)];
}
function penKeyrow(x, y, n, w = 9.5, h = 10) {
  const a = [{ k: 'rc', x, y, w: n * w, h, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2 }];
  for (let i = 1; i < n; i++) a.push(penLine([x + i * w, y], [x + i * w, y + h], 1.2));
  return a;
}
// the hand from the side (handside.py): segment angles from the fingertip back to the elbow, the app's HAND_POSES
const PEN_HAND_LENS = [12, 15, 24, 46, 120];
function penHandChain(a, tip = [222, 118]) {
  const pts = [tip]; let x = tip[0], y = tip[1];
  a.forEach((ang, i) => { const r = ang * Math.PI / 180; x -= PEN_HAND_LENS[i] * Math.cos(r); y -= PEN_HAND_LENS[i] * Math.sin(r); pts.push([x, y]); });
  return pts;   // tip, nail joint, middle joint, knuckle, wrist, elbow side
}
function penHandChecks(a, pts) { const [tip, j1, j2, kn, wr] = pts; return { wrist: Math.abs(a[4]) < 6 && a[3] > -14 && a[3] <= 2, knuckle: kn[1] < wr[1] + 1, tip: a[0] > 55 && a[0] > a[1] - 5 }; }
function penHandSide(a, o = {}) {
  const labels = o.labels !== false, faults = o.faults !== false, tipAt = o.tip || [222, 118];
  const pts = penHandChain(a, tipAt), [tip, j1, j2, kn, wr, fa] = pts;
  const ok = faults ? penHandChecks(a, pts) : { wrist: true, knuckle: true, tip: true };
  const s = [{ k: 'rc', x: 150, y: 118 + (o.press || 0), w: 134, h: 16, rx: 0, f: PEN_P, s: PEN_N, sw: 2 }, penLine([206, 118 + (o.press || 0)], [206, 134 + (o.press || 0)], 1.2),
    { k: 'pa', seg: [['M', [120, 134]], ['L', [290, 134]], ['L', [290, 148]], ['L', [120, 148]], ['Z']], f: PEN_N, s: PEN_N, w: 2 },
    penLine([36, 118], [150, 118], 1.4, PEN_C, '4 4')];
  if (o.keylabel !== false && labels) s.push(penText(38, 113, o.keyText || 'key level'));
  if (o.ball) { const bx = (wr[0] + kn[0]) / 2 + 6, by = (wr[1] + kn[1]) / 2 + 16.5;
    s.push({ k: 'el', c: [bx, by], rx: 12, ry: 12, f: 'none', s: PEN_C, w: 2.2 }, { k: 'pa', seg: [['M', [bx - 7, by - 9]], ['Q', [bx - 1.6, by], [bx - 7, by + 9]], ['M', [bx + 7, by - 9]], ['Q', [bx + 1.6, by], [bx + 7, by + 9]]], f: 'none', s: PEN_C, w: 1.2 }); }
  s.push(...penLimb([fa, wr], 17, PEN_P, PEN_N, 1.8));
  const sl = [fa[0] + (wr[0] - fa[0]) * 0.62, fa[1] + (wr[1] - fa[1]) * 0.62];
  s.push(...penLimb([[fa[0] - 4, fa[1]], sl], 21, PEN_N, PEN_N, 0));
  s.push(...penLimb([wr, kn], 14, PEN_P, PEN_N, 1.8), ...penLimb([kn, j2, j1, tip], 7.6, PEN_P, PEN_N, 1.6));
  const u = pUnit(pSub(tip, j1)), n = [-u[1], u[0]];
  s.push(penLine([j1[0] + u[0] * 3 - n[0] * 2.4, j1[1] + u[1] * 3 - n[1] * 2.4], [j1[0] + u[0] * 8 - n[0] * 2.4, j1[1] + u[1] * 8 - n[1] * 2.4], 1.1));
  if (o.car != null) {   // the little car on the knuckle bridge; o.car: 0 at the knuckle, -1 back at the wrist, +1 past the knuckle
    const at = o.car <= 0 ? pAdd(kn, pSub(wr, kn), -o.car) : pAdd(kn, pSub(j2, kn), o.car * 0.6);
    const ang = (-8 + (o.car < 0 ? Math.atan2(kn[1] - wr[1], kn[0] - wr[0]) * 180 / Math.PI + 8 : 0)) * Math.PI / 180, c = Math.cos(ang), sn = Math.sin(ang);
    const m = [c, sn, -sn, c, at[0] - 4, at[1] - 11];
    s.push({ k: 'rc', x: -13, y: -9, w: 26, h: 9, rx: 3.5, f: PEN_C, m }, { k: 'rc', x: -7, y: -15, w: 13, h: 7, rx: 3, f: PEN_C, m },
      { k: 'el', c: [-7, 1], rx: 3.3, ry: 3.3, f: PEN_N, m }, { k: 'el', c: [7, 1], rx: 3.3, ry: 3.3, f: PEN_N, m });
  }
  const dot = (p, good, r = 3.6) => ({ k: 'el', c: p, rx: r, ry: r, f: good ? PEN_P : PEN_C, s: PEN_N, w: 1.5 });
  s.push(dot(j2, true, 2.9), dot(j1, !(o.nail && faults), 2.9), dot(wr, ok.wrist), dot(kn, ok.knuckle), dot(tip, ok.tip));
  if (labels) {
    const lab = (x, y, txt, good, anchor = 'middle') => ({ k: 'tx', x, y, text: txt, size: 9.5, weight: 900, fill: good ? PEN_N : PEN_C, anchor, halo: o.halo });
    s.push(lab(wr[0], wr[1] - 14, o.wristText || 'wrist', ok.wrist), lab(kn[0] + 4, kn[1] - (o.car != null ? 26 : 13), o.knuckleText || 'knuckle', ok.knuckle), lab(tip[0] + 10, tip[1] - 7, o.tipText || 'tip', ok.tip, 'start'));
  }
  return { shapes: s, ok, pts };
}
const penKeyLevel = (x2 = 122, label) => [penText(8, 91, label || 'key level'), penLine([8, 96], [x2, 96], 1.3, PEN_C, '4 4')];

// ---- to_pen: big navy areas hatched, thick navy limbs get an outline and a hatched core ----
function penHatch(list) {
  const out = [];
  list.forEach(e => {
    if (e.k === 'g') { out.push({ ...e, kids: penHatch(e.kids) }); return; }
    if (e.hz) { out.push(e); return; }   // already done (penHatch may meet a shape twice)
    if (e.k === 'pl' && e.s === PEN_N && e.w >= 6) { out.push({ ...e, w: e.w + 0.4, hz: true }, { ...e, s: 'H', w: Math.max(2, e.w - 3.4), hz: true }); return; }
    if (e.k === 'pa' && e.f === PEN_N && !e.solid) {
      const xs = [], ys = []; e.seg.forEach(sg => sg.slice(1).forEach(q => { xs.push(q[0]); ys.push(q[1]); }));
      if ((Math.max(...xs) - Math.min(...xs)) * (Math.max(...ys) - Math.min(...ys)) >= 260) { out.push({ ...e, f: 'H', hz: true }); return; }
    }
    if (e.k === 'rc' && e.f === PEN_N && !e.solid && e.w * e.h >= 400) { out.push({ ...e, f: 'H', hz: true }); return; }
    if (e.k === 'pl' || e.k === 'pa' || e.k === 'rc') { out.push({ ...e, hz: true }); return; }
    out.push(e);
  });
  return out;
}

// ---- bake: resample every outline every 4.6 units and push each point along the noise field ----
const penMul = (m, q) => m ? [m[0] * q[0] + m[2] * q[1] + m[4], m[1] * q[0] + m[3] * q[1] + m[5]] : q;
function penSegPoint(start, sg, t) {
  const u = 1 - t;
  if (sg[0] === 'L') return [start[0] + (sg[1][0] - start[0]) * t, start[1] + (sg[1][1] - start[1]) * t];
  if (sg[0] === 'Q') { const [c, e] = [sg[1], sg[2]]; return [u * u * start[0] + 2 * u * t * c[0] + t * t * e[0], u * u * start[1] + 2 * u * t * c[1] + t * t * e[1]]; }
  if (sg[0] === 'C') { const [c1, c2, e] = [sg[1], sg[2], sg[3]]; return [u * u * u * start[0] + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t * t * t * e[0], u * u * u * start[1] + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t * t * t * e[1]]; }
  if (sg[0] === 'A') { const [c, rx, ry, a0, a1] = sg.slice(1); const a = a0 + (a1 - a0) * t; return [c[0] + rx * Math.cos(a), c[1] + ry * Math.sin(a)]; }
}
function penSegLen(start, sg) {
  if (sg[0] === 'L') return Math.hypot(sg[1][0] - start[0], sg[1][1] - start[1]);
  let l = 0, q = start; for (let i = 1; i <= 24; i++) { const r = penSegPoint(start, sg, i / 24); l += Math.hypot(r[0] - q[0], r[1] - q[1]); q = r; } return l;
}
// a shape as subpaths of segments (local coords), plus whether it is closed
function penGeom(e) {
  if (e.k === 'pl' || e.k === 'ln') return [{ start: e.p[0], seg: e.p.slice(1).map(q => ['L', q]), closed: false }];
  if (e.k === 'pa') {
    const subs = []; let cur = null;
    e.seg.forEach(sg => {
      if (sg[0] === 'M') { cur = { start: sg[1], seg: [], closed: false }; subs.push(cur); }
      else if (sg[0] === 'Z') { const last = cur.seg.length ? cur.seg[cur.seg.length - 1] : null; const end = last ? last[last.length - 1] : cur.start;
        if (Math.hypot(end[0] - cur.start[0], end[1] - cur.start[1]) > 1e-6) cur.seg.push(['L', cur.start]); cur.closed = true; }
      else cur.seg.push(sg);
    });
    return subs;
  }
  if (e.k === 'el') { const [cx, cy] = e.c; return [{ start: [cx - e.rx, cy], seg: [['A', [cx, cy], e.rx, e.ry, Math.PI, 0], ['A', [cx, cy], e.rx, e.ry, 0, -Math.PI]], closed: true }]; }
  if (e.k === 'rc') {
    const { x, y, w, h } = e, rx = Math.min(e.rx || 0, w / 2, h / 2);
    if (rx <= 0) return [{ start: [x, y], seg: [['L', [x + w, y]], ['L', [x + w, y + h]], ['L', [x, y + h]], ['L', [x, y]]], closed: true }];
    const P2 = Math.PI / 2;
    return [{ start: [x + rx, y], closed: true, seg: [['L', [x + w - rx, y]], ['A', [x + w - rx, y + rx], rx, rx, -P2, 0], ['L', [x + w, y + h - rx]], ['A', [x + w - rx, y + h - rx], rx, rx, 0, P2],
      ['L', [x + rx, y + h]], ['A', [x + rx, y + h - rx], rx, rx, P2, Math.PI], ['L', [x, y + rx]], ['A', [x + rx, y + rx], rx, rx, Math.PI, 3 * P2]] }];
  }
  return [];
}
const penSegEnd = (sg) => sg[0] === 'A' ? penSegPoint(null, sg, 1) : sg[sg.length - 1];
let PEN_SCALES = null;   // the hatch sizes one drawing needs (filled while it is baked)
function penPaint(v, hatch) {
  if (v === 'H') return 'url(#' + hatch + ')';
  if (typeof v === 'string' && v.indexOf('H@') === 0) { const k = v.slice(2); if (PEN_SCALES) PEN_SCALES.add(k); return 'url(#' + hatch + '_' + k.replace('.', '') + ')'; }
  return v;
}
function penAttrs(e, hatch) {
  const paint = (v) => penPaint(v, hatch);
  let a = '';
  if (e.k === 'pl' || e.k === 'ln') a += ' fill="none" stroke="' + paint(e.s) + '" stroke-width="' + pFix(e.w) + '" stroke-linecap="round"' + (e.k === 'pl' ? ' stroke-linejoin="round"' : '') + (e.dash ? ' stroke-dasharray="' + e.dash + '"' : '');
  else {
    a += ' fill="' + paint(e.f || 'none') + '"';
    if (e.s) a += ' stroke="' + paint(e.s) + '" stroke-width="' + pFix(e.k === 'rc' ? e.sw : e.w) + '"';
    if (e.k === 'pa' || (e.k === 'hr' && e.s)) a += ' stroke-linejoin="round"';
  }
  if (e.op != null) a += ' opacity="' + e.op + '"';
  return a;
}
// the shape as it is, unwobbled (for the small, rigid ones and the hair)
function penPlain(e, hatch) {
  const tf = e.m ? ' transform="matrix(' + e.m.map(v => +v.toFixed(4)).join(' ') + ')"' : '';
  if (e.k === 'hr') return '<path d="' + e.d + '"' + penAttrs(e, hatch) + tf + '/>';
  if (e.k === 'el') return '<ellipse cx="' + pFix(e.c[0]) + '" cy="' + pFix(e.c[1]) + '" rx="' + e.rx + '" ry="' + e.ry + '"' + penAttrs(e, hatch) + tf + '/>';
  if (e.k === 'ln') return '<line x1="' + pFix(e.p[0][0]) + '" y1="' + pFix(e.p[0][1]) + '" x2="' + pFix(e.p[1][0]) + '" y2="' + pFix(e.p[1][1]) + '"' + penAttrs(e, hatch) + '/>';
  if (e.k === 'pl') return '<polyline points="' + e.p.map(q => pFix(q[0]) + ',' + pFix(q[1])).join(' ') + '"' + penAttrs(e, hatch) + '/>';
  if (e.k === 'rc') return '<rect x="' + pFix(e.x) + '" y="' + pFix(e.y) + '" width="' + pFix(e.w) + '" height="' + pFix(e.h) + '" rx="' + (e.rx || 0) + '"' + penAttrs(e, hatch) + tf + '/>';
  if (e.k === 'pa') return '<path d="' + e.seg.map(sg => sg[0] + (sg[0] === 'Z' ? '' : sg.slice(1).map(q => pFix(q[0]) + ',' + pFix(q[1])).join(' '))).join(' ') + '"' + penAttrs(e, hatch) + tf + '/>';
  return '';
}
function penHrBox(e) {
  const n = (e.d.match(/-?\d*\.?\d+/g) || []).map(Number), q = [];
  for (let i = 0; i + 1 < n.length; i += 2) q.push(penMul(e.m, [n[i], n[i + 1]]));
  return q;
}
function penEsc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
// shift: where this group's noise is read from (so a figure that slides along keeps its own lines instead of boiling)
function penBakeList(list, hatch, shift, step = 4.6, small = 17) {
  let out = '';
  const fld = (x, y) => penField(x - shift[0], y - shift[1]);
  list.forEach(e => {
    if (e.k === 'g') { const sh = e.shift ? [shift[0] + e.shift[0], shift[1] + e.shift[1]] : shift;
      out += '<g' + (e.who ? ' data-who="' + e.who + '"' : '') + (e.hide ? ' display="none"' : '') + (e.testid ? ' data-testid="' + e.testid + '"' : '') + (e.floor != null ? ' data-map-stage="' + e.floor + '"' : '') + '>' + penBakeList(e.kids, hatch, sh, step, small) + '</g>'; return; }
    if (e.k === 'raw') { out += e.svg; return; }   // already drawn (a baked book picture, a small icon): passed through as it is
    if (e.k === 'tx') { out += '<text x="' + pFix(e.x) + '" y="' + pFix(e.y) + '" text-anchor="' + e.anchor + '" font-size="' + e.size + '" font-weight="' + e.weight + '" fill="' + e.fill + '" font-family="Inter,sans-serif"'
      + (e.serif || e.italic ? ' style="' + (e.serif ? "font-family:'Playfair Display',Georgia,serif;" : '') + (e.italic ? 'font-style:italic;' : '') + '"' : '')
      + (e.halo ? ' stroke="#fffdf7" stroke-width="2.4" stroke-linejoin="round" paint-order="stroke"' : '') + '>' + penEsc(e.text) + '</text>'; return; }
    let box;
    const subs = e.k === 'hr' ? null : penGeom(e);
    const sc = e.m ? Math.sqrt(Math.abs(e.m[0] * e.m[3] - e.m[1] * e.m[2])) || 1 : 1;
    // sample every subpath (uniform in each segment's parameter, as svgpathtools does)
    const sampled = subs ? subs.map(sp => {
      const pts = [sp.start]; let st = sp.start;
      sp.seg.forEach(sg => { const n = Math.max(1, Math.ceil(penSegLen(st, sg) * sc / step)); for (let i = 1; i <= n; i++) pts.push(penSegPoint(st, sg, i / n)); st = penSegEnd(sg); });
      if (sp.closed && pts.length > 2) pts.pop();
      return { pts: pts.map(q => penMul(e.m, q)), closed: sp.closed };
    }) : null;
    box = e.k === 'hr' ? penHrBox(e) : [].concat(...sampled.map(s => s.pts));
    const xs = box.map(q => q[0]), ys = box.map(q => q[1]);
    const bw = Math.max(...xs) - Math.min(...xs), bh = Math.max(...ys) - Math.min(...ys);
    if (e.k === 'hr' || Math.max(bw, bh) < small) {
      const d = fld((Math.max(...xs) + Math.min(...xs)) / 2, (Math.max(...ys) + Math.min(...ys)) / 2);
      out += '<g transform="translate(' + pFix(d[0]) + ' ' + pFix(d[1]) + ')">' + penPlain(e, hatch) + '</g>'; return;
    }
    const d = sampled.map(s => { const q = s.pts.map(p => { const v = fld(p[0], p[1]); return [p[0] + v[0], p[1] + v[1]]; });
      return 'M' + q.map(p => pFix(p[0]) + ' ' + pFix(p[1])).join('L') + (s.closed ? 'Z' : ''); }).join('');
    out += '<path d="' + d + '"' + penAttrs(e, hatch) + '/>';
  });
  return out;
}
let PEN_UID = 0;
// opts: vb [x, y, w, h], shift [dx, dy] for the whole drawing, id (hatch pattern id; unique per drawing on a page)
function penSvg(shapes, opts = {}) {
  const vb = opts.vb || [0, 0, 220, 172], hatch = opts.id || ('penh' + (++PEN_UID));
  PEN_SCALES = new Set();
  const body = penBakeList(penHatch(shapes), hatch, opts.shift || [0, 0]);
  const pat = (id, k) => '<pattern id="' + id + '" width="' + 3.2 * k + '" height="' + 3.2 * k + '" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="' + 3.2 * k + '" height="' + 3.2 * k + '" fill="' + PEN_P + '"/><line x1="0" y1="0" x2="0" y2="' + 3.2 * k + '" stroke="' + PEN_N + '" stroke-width="' + 1.15 * k + '"/></pattern>';
  const defs = '<defs>' + pat(hatch, 1) + [...PEN_SCALES].map(k => pat(hatch + '_' + k.replace('.', ''), +k)).join('') + '</defs>';
  PEN_SCALES = null;
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + vb.join(' ') + '">' + defs + body + '</svg>';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { penPlace, penKid, penSvg, penJoints, penText, penFloor, penPiano, penStool, penKeyLevel, penKeyrow, penHandSide, penHandChain, penLine, penLimb, pAdd, pSub, pUnit, PEN_C, PEN_N, PEN_P };
