const t = (en) => en; const LANG = 'en';
const pEase = (k) => k < 0 ? 0 : k > 1 ? 1 : k * k * (3 - 2 * k);
const PEN_N = '#26296b', PEN_C = '#e4572e', PEN_P = '#fffdf7', PEN_G = '#2e8a6e';
const PEN_FIELD = [[[0.155563, -0.117238, 4.873777, 0.322693], [-0.041694, 0.127865, 5.488698, 0.322693], [0.043848, -0.091346, 5.008135, 0.322693], [-0.055961, 0.161683, 1.7494, 0.322693], [-0.130771, 0.04701, 3.17017, 0.322693], [0.435705, -0.012322, 4.980442, 0.145212], [0.449899, -0.031258, 1.352824, 0.145212], [-0.265623, -0.226978, 0.276096, 0.145212], [-0.320598, -0.030079, 2.929259, 0.145212]], [[-0.164339, -0.173307, 3.230296, 0.322693], [0.00274, 0.175436, 0.074104, 0.322693], [-0.046147, -0.121047, 1.260449, 0.322693], [0.156213, 0.003666, 5.215344, 0.322693], [-0.013664, 0.123067, 5.53129, 0.322693], [0.244339, -0.349289, 4.019462, 0.145212], [0.400563, 0.259517, 3.400107, 0.145212], [0.294099, -0.307948, 2.269889, 0.145212], [0.415175, 0.162125, 2.435562, 0.145212]]];
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
  const a = [{ k: 'pl', p: chain, s: out, w: w + 2 * ow, ch: true }];
  if (fill !== out) a.push({ k: 'pl', p: chain, s: fill, w, ch: true });
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
  return [{ k: 'g', ch: true, who: 'girl', hide: who !== 'girl', kids: penGirl(j, face) }, { k: 'g', ch: true, who: 'boy', hide: who !== 'boy', kids: penBoy(j, face) }];
}
// joint dots (white = fine, coral = this one is wrong or is the thing to look at)
function penJoints(j, coral = [], skip = [], good = []) {
  const pts = { shoulder: j.arms[0][0], elbow: j.arms[0][1], wrist: j.arms[0][2], hip: j.legs[0][0], knee: j.legs[0][1], ankle: j.legs[0][2] };
  return Object.keys(pts).filter(k => !skip.includes(k)).map(k => ({ k: 'el', c: pts[k], rx: 3.2, ry: 3.2, f: coral.includes(k) ? PEN_C : PEN_P, s: good.includes(k) ? PEN_G : PEN_N, w: good.includes(k) ? 2 : 1.3 }));
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
const penFloor = (W, y = 162) => [penLine([6, y], [W - 6, y], 1.6, 'rgba(38,41,107,0.4)')];
function penPiano(x = 150, y = 58, floorY = 162, keyY = 98) {
  const a = [{ k: 'rc', x, y, w: 56, h: floorY - y, rx: 2.5, f: PEN_P, s: PEN_N, sw: 2.4, nw: true }, { k: 'rc', x: x - 26, y: keyY, w: 30, h: 8.5, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2, nw: true }];
  for (let i = 1; i < 4; i++) a.push({ ...penLine([x - 26 + i * 7.5, keyY], [x - 26 + i * 7.5, keyY + 8.5], 1.2), nw: true });
  return a;
}
function penStool(x1 = 46, x2 = 100, y = 114, floorY = 162) {
  return [{ k: 'rc', x: x1, y, w: x2 - x1, h: 7, rx: 2, f: PEN_P, s: PEN_N, sw: 2.4 }, penLine([x1 + 7, y + 7], [x1 + 7, floorY], 2.4), penLine([x2 - 7, y + 7], [x2 - 7, floorY], 2.4)];
}
function penKeyrow(x, y, n, w = 9.5, h = 10) {
  const a = [{ k: 'rc', x, y, w: n * w, h, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2, nw: true }];
  for (let i = 1; i < n; i++) a.push({ ...penLine([x + i * w, y], [x + i * w, y + h], 1.2), nw: true });
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
  const s = [{ k: 'rc', x: 150, y: 118 + (o.press || 0), w: 134, h: 16, rx: 0, f: PEN_P, s: PEN_N, sw: 2, nw: true }, { ...penLine([206, 118 + (o.press || 0)], [206, 134 + (o.press || 0)], 1.2), nw: true },
    { k: 'pa', seg: [['M', [120, 134]], ['L', [290, 134]], ['L', [290, 148]], ['L', [120, 148]], ['Z']], f: PEN_N, s: PEN_N, w: 2, nw: true },
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
  if (o.car != null) {   // the little car; o.car: -1 back at the wrist, 0 on the knuckle bridge, 1 slid down the finger onto the key (Sohyun 2026-10-09)
    let at, dir;
    if (o.car <= 0) { at = pAdd(kn, pSub(wr, kn), -o.car); dir = pSub(kn, wr); }
    else {
      const chain = [kn, j2, j1, tip, [tip[0] + 16, 124 + (o.press || 0)]], lens = chain.slice(1).map((q, i) => Math.hypot(q[0] - chain[i][0], q[1] - chain[i][1]));
      const total = lens.reduce((x, y) => x + y, 0);
      let d = Math.min(o.car, 1) * total, i = 0;
      while (i < lens.length - 1 && d > lens[i]) { d -= lens[i]; i++; }
      at = pAdd(chain[i], pSub(chain[i + 1], chain[i]), d / lens[i]); dir = pSub(chain[i + 1], chain[i]);
    }
    const ang = Math.atan2(dir[1], dir[0]), c = Math.cos(ang), sn = Math.sin(ang);
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
// Sohyun 2026-10-09 (Phase 393): only the characters look hand-drawn -- a shape wobbles only when it (or its group)
// carries ch: true (the siblings, their limbs and hands, the turtle, the bird); frames, houses, props, clouds and
// waves are drawn clean and straight, so a big frame never looks like a mistake.
function penBakeList(list, hatch, shift, step = 4.6, small = 17, chr = false) {
  let out = '';
  const fld = (x, y) => penField(x - shift[0], y - shift[1]);
  list.forEach(e => {
    if (e.k === 'g') { const sh = e.shift ? [shift[0] + e.shift[0], shift[1] + e.shift[1]] : shift;
      out += '<g' + (e.who ? ' data-who="' + e.who + '"' : '') + (e.hide ? ' display="none"' : '') + (e.testid ? ' data-testid="' + e.testid + '"' : '') + (e.floor != null ? ' data-map-stage="' + e.floor + '"' : '') + '>' + penBakeList(e.kids, hatch, sh, step, small, chr || !!e.ch) + '</g>'; return; }
    if (e.k === 'raw') { out += e.svg; return; }   // already drawn (a baked book picture, a small icon): passed through as it is
    if (e.nw) { out += penPlain(e, hatch); return; }   // keyboards: straight, no wobble (Sohyun 2026-10-09)
    if (e.k !== 'tx' && !(chr || e.ch)) { out += penPlain(e, hatch); return; }   // not a character: clean and straight
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
  const reach = p.steep ? t('The arm has to stretch down to the keys. Lower the stool.', '팔을 아래로 쭉 뻗어야 건반에 닿아요. 의자를 낮춰요.')
    : t('The arm has to stretch out to the keys. Slide the stool closer.', '팔을 앞으로 쭉 뻗어야 건반에 닿아요. 의자를 더 가까이 옮겨요.');
  return [
    { id: 'feet', label: t('Feet flat on the floor', '발은 바닥에 평평하게'), ok: p.feet,
      fix: t('The feet can’t reach. Put a footstool or a sturdy box under them.', '발이 닿지 않아요. 발판이나 튼튼한 상자를 발밑에 놓아요.') },
    { id: 'level', label: t('Forearm level with the keys', '팔뚝이 건반과 수평'), ok: !p.straight && p.slope > -8 && p.slope < 12,
      fix: p.straight ? reach : p.slope <= -8 ? t('The elbows are below the keys, so the hands reach up. Raise the stool.', '팔꿈치가 건반보다 낮아서 손이 위로 뻗어요. 의자를 높여요.')
        : t('The elbows are too high, so the wrists drop to the keys. Lower the stool.', '팔꿈치가 너무 높아서 손목이 건반으로 떨어져요. 의자를 낮춰요.') },
    { id: 'ahead', label: t('Elbows just in front of you, away from your body', '팔꿈치는 몸 바로 앞에, 몸에서 떨어지게'), ok: !p.straight && p.ahead >= 8 && p.ahead <= 18,
      fix: p.straight ? reach : p.ahead < 8 ? t('The elbows are squashed in against the body. Slide the stool back.', '팔꿈치가 몸에 눌려 있어요. 의자를 뒤로 빼요.')
        : t('The arms reach out ahead of the body. Slide the stool closer.', '팔이 몸 앞으로 멀리 뻗어 있어요. 의자를 더 가까이 옮겨요.') },
  ];
}
function penSitShapes(seatY, x2, up, checks) {
  const p = sitPose376(seatY, x2, up), bad = (id) => !checks.find(c => c.id === id).ok;
  const elOk = !bad('level') && !bad('ahead'), wrOk = !bad('level');
  const s = [...penFloor(220), ...penKeyLevel(122, t('key level', '건반 높이')), ...penPiano()];
  if (up) s.push({ k: 'rc', x: 102, y: 150, w: 40, h: 12, rx: 1.5, f: PEN_P, s: PEN_N, sw: 2.2 });
  // the figure moves with the stool; reading its wobble from where it sits keeps its lines steady while it slides
  const shift = [x2 - 100, seatY - 114];
  s.push({ k: 'g', shift, kids: penStool(x2 - 54, x2, seatY) });
  s.push({ k: 'g', shift, kids: [...penKid(p.J, 1, penWho('boy')), ...penJoints(p.J, [bad('level') || bad('ahead') ? 'elbow' : '', bad('level') ? 'wrist' : '', bad('feet') ? 'ankle' : ''].filter(Boolean), ['shoulder', 'hip', 'knee'], [elOk ? 'elbow' : '', wrOk ? 'wrist' : ''].filter(Boolean))] });
  // labels as in the book (elbow above and to the right, wrist above it); the elbow's word stays a line above the wrist's
  // (an elbow squashed back behind the shoulder gets its word on the left, behind the back, so it never sits on the face)
  const lab = (tx, ty, from, to, txt, anchor, col) => [{ ...penText(tx, ty, txt, { anchor, fill: col || PEN_C }), halo: true }, { k: 'pa', seg: [['M', from], ['L', to]], f: 'none', s: col || PEN_C, w: 1.2 }];
  const wy = p.wr[1] - 12, ey = Math.min(p.el[1] - 19, wy - 9), back = p.J.hip[0] - 15;
  if (p.ahead < 6) s.push(...lab(back - 3, p.el[1] + 3, [back - 1, p.el[1]], [p.el[0] - 4, p.el[1]], t('elbow', '팔꿈치'), 'end', elOk ? PEN_G : PEN_C));
  else s.push(...lab(p.el[0] + 7, ey, [p.el[0] + 6, ey - 2], [p.el[0] + 1.5, p.el[1] - 4.5], t('elbow', '팔꿈치'), undefined, elOk ? PEN_G : PEN_C));
  s.push(...lab(p.wr[0] + 1, wy, [p.wr[0] + 1.5, wy - 1.5], [p.wr[0] + 1, p.wr[1] - 6], t('wrist', '손목'), undefined, wrOk ? PEN_G : PEN_C));
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
    s.push(penLine([side, 89], [el - sx * 4, 89], 1.4, ok ? PEN_G : PEN_C, '2.5 2.5'));
    s.push({ k: 'el', c: [el, 89], rx: 3.2, ry: 3.2, f: ok ? PEN_P : PEN_C, s: ok ? PEN_G : PEN_N, w: ok ? 2 : 1.3 });
  });
  return s;
}
const penLimbPair = (ch) => [{ k: 'pl', p: ch, s: PEN_N, w: 6.8 }, { k: 'pl', p: ch, s: PEN_P, w: 3.6 }];
const HAND_POSES = {
  good:   { a: [80, 55, 24, -3, -2],  get title() { return t('The good shape', '좋은 모양'); }, get see() { return t('Knuckles make a bridge (the highest point), fingers curve down, you play on the fingertip pad. The wrist sits a little above the keys, level with the forearm, nearly as high as the knuckles.', '마디가 다리를 만들고(가장 높은 곳), 손가락은 아래로 둥글게 굽어, 손끝의 살로 쳐요. 손목은 건반보다 조금 위, 아래팔과 수평, 마디와 거의 같은 높이예요.'); }, get fix() { return t('', ''); } },
  flat:   { a: [22, 16, 10, 4, 2],     get title() { return t('Flat fingers', '납작한 손가락'); }, get see() { return t('Fingers lie flat and the key is played with the soft middle of the finger.', '손가락이 납작하게 누워서 손가락 가운데의 말랑한 부분으로 건반을 쳐요.'); }, get fix() { return t('Hold a small ball (or a mandarin). Keep that round shape and put it on the keys.', '작은 공(또는 귤)을 쥐어 봐요. 그 둥근 모양 그대로 건반 위에 올려요.'); } },
  bridge: { a: [62, 38, 8, 18, 3],     get title() { return t('Knuckles collapsed', '마디가 무너졌어요'); }, get see() { return t('The bridge has fallen in: the knuckles are lower than the wrist.', '다리가 무너졌어요: 마디가 손목보다 낮아요.'); }, get fix() { return t('Knuckle bridge (warm-up 5): press one key slowly and hold for 3. The knuckles stay up like a bridge.', '마디 다리(워밍업 5): 건반 하나를 천천히 누르고 셋을 세는 동안, 마디는 다리처럼 위로 그대로.'); } },
  nail:   { a: [18, 78, 30, -8, 0],    get title() { return t('Tip joint caving in', '손끝 관절이 꺾여요'); }, get see() { return t('The last joint bends backwards when the finger plays.', '건반을 칠 때 마지막 관절이 뒤로 꺾여요.'); }, get fix() { return t('Notice the tip joint: play slowly on the tip, press the key down and hold, and feel it stay firm like a little pillar.', '손끝 관절을 살펴봐요: 손끝으로 천천히, 건반을 끝까지 누르고 기다리며, 작은 기둥처럼 단단한지 느껴 봐요.'); } },
  low:    { a: [80, 55, 22, -40, -18], get title() { return t('Wrist dropped', '손목이 처졌어요'); }, get see() { return t('The wrist sinks below the keys and the hand has to push up.', '손목이 건반 아래로 가라앉아서 손이 위로 밀어 올려야 해요.'); }, get fix() { return t('Wrist balloon (warm-up 6): after each key, the wrist comes straight back up to level.', '손목 풍선(워밍업 6): 건반을 칠 때마다 손목이 바로 같은 높이로 다시 올라와요.'); } },
  high:   { a: [82, 60, 36, 26, 14],   get title() { return t('Wrist too high', '손목이 너무 높아요'); }, get see() { return t('The wrist is hunched up and the fingers poke straight down.', '손목이 구부정하게 솟고 손가락이 꼿꼿이 아래로 찔러요.'); }, get fix() { return t('Let the wrist sink until it’s level with the forearm: a straight line from elbow to knuckle.', '손목이 아래팔과 수평이 될 때까지 내려요: 팔꿈치에서 마디까지 곧은 선.'); } },
};
window.PEN_FING = {"3:left hand finger 2": "<svg style=\"width:100%;height:auto;display:block\" width=\"100%\" height=\"100%\" viewBox=\"0 0 150 176\"><defs><pattern id=\"hpqfingers20\" width=\"3.2\" height=\"3.2\" patternUnits=\"userSpaceOnUse\" patternTransform=\"rotate(40)\"><rect width=\"3.2\" height=\"3.2\" fill=\"#fffdf7\"></rect><line x1=\"0\" y1=\"0\" x2=\"0\" y2=\"3.2\" stroke=\"#26296b\" stroke-width=\"1.15\"></line></pattern></defs><path d=\"M48.7 88.2l4.3 0 3.8-.1 4.1.2 4.2.4 4.2-.3 4.7-.7 4.9-.2 4.5.2 4.5.1 4.5.2 3.9.2 3.6.1 4 .8 3.9 1.8 3.3 2.1 2.7 2.4 2.6 3.5 1.9 4.4 1.1 4.6 .4 4.6-.1 3.5 0 3.3-.1 3.1 0 3-.5 3.7-1.1 4-1.7 4-2 3.5-2.3 3.2-3.1 2.8-3.9 1.9-4 1-4 .3-4.6.4-4.5.1-4.1-.5-4.8-.1-4.8.1-4-.2-4.4-.4-4.9.2-4.1.5-4.3.4-5.2.2-4.6-.3-3.8-1.6-3.9-2.4-3.6-2.4-2.8-2.9-1.8-3.3-1.1-3.4-.6-3.5-.1-4.1 0-3.9-.1-3.8-.3-3.7-.3-3.6-.1-4.2 .6-4.2 1.3-3.8 2.5-3.3 3.7-2.9 4.3-2.3 3.9-1.5 3.8-.9z\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M105.7 33.5l0 0 3.7.5 3 2.2 2 3.2 .6 3.6-.1 4.7-.1 4.3-.1 3.6 0 3.7 0 4.4 .2 5 .2 4.8 .2 4.5-.1 4.6-.3 4.3-.3 3.8-.8 2.8-1.8 2.7-2.6 2.4-3.1 1.1 0 0-3.3-.4-2.7-1.8-2-2.8-.9-3.4-.3-4.6 0-4.2 0-4 .1-4.2-.1-4.6-.2-4.5-.1-4.2 0-4.4 .2-4.9 .1-4.7 0-4.2 .5-3 1.9-2.9 2.8-2.3z\" data-f=\"2\" fill=\"#e4572e\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M84.1 23.7l0 0 3.1 1 2.9 2.5 1.9 3 .7 3.5 .1 4.2 .1 4 0 4.2 .1 4.5 0 4.4-.1 4.7 0 5.1 .2 5.2 .2 4.5 .2 3.7 .1 3.8 .1 4.5 .1 4.6-.5 3.1-2.1 2.5-3.4 1.9-3.8.6 0 0-3.4-.9-2.8-2.1-2.1-2.6-.8-3.2 0-4.1 .3-3.8 .3-3.8 .2-4.8 .1-5.4-.2-5.2-.2-4.7-.3-4.3-.1-4.1 0-4.1 0-4.2 0-4.6 .1-4.7 .9-3.4 2.1-2.9 2.8-2z\" data-f=\"3\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M61.9 32.6l0 0 3.3.2 2.7 1.7 1.8 2.7 .8 3.5 .1 4.6 .3 4.6 .2 4.3 .1 4.1 0 4.3 0 5.2 0 5.5-.2 4.9-.3 4.3-.2 4.3-.1 4.1-.6 2.8-1.9 2.5-2.7 2.1-3.4 1.3 0 0-3.2-.3-2.4-1.9-1.6-3-.8-3.4-.4-4.2-.4-3.8-.2-4.3-.1-4.9 0-5.2 0-4.9 .1-4.7 .2-4.7 .1-4.6 0-4.2-.2-4.2 .4-3.2 1.9-2.6 3.1-1.9z\" data-f=\"4\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M40.1 48l0 0 3.5.4 3 1.4 1.8 2.7 .5 3.7-.2 4.7-.1 4.8 .1 4.8 .3 4.6 .3 4.2 .2 3.9 .2 3.9 .1 3.9-.8 3-2.5 2.4-3.6 1.7-3.6.8 0 0-3.2-.6-3-1.8-2-2.5-.6-3 .3-3.9 .2-4.2 .2-4.5 .2-4.5 0-4.4 0-4.5-.1-4.6-.1-4.3 .7-3.1 2.1-2.6 2.8-1.9z\" data-f=\"5\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><g transform=\"rotate(38 116 118)\"><path d=\"M116 72.7l0 0 4 1 3.2 1.8 2.1 2.8 .8 3.6 .2 4.6 .3 4.5 .2 4.5-.1 4.6-.3 4.7-.5 4.6-.3 4.4-.9 3.7-2.2 3.5-3 2.5-3.4.5 0 0-3.2-.9-3-2.4-2.4-3.5-1-3.8-.7-4.4-.7-4.7 0-4.5 .4-4.4 .3-4.6 .4-4.4 .4-4.1 .7-3.8 1.8-3.5 2.9-2.2z\" data-f=\"1\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path></g><path d=\"M25.9 92.2l5.2-.3 5.4-.3 4.3-.2 4.5.2 5 .3 4.5 0 3.9-.1 4.2.1 4.1 0 4.5-.3 5.1-.4 4.9-.3 4.5 0 4.8.6 4.4.7 4-.1 4.2-.4 4.4-.1 4.3 0 4.4-.2 0 3.5 .1 4 .2 4.5 .2 4.5 0 4.3-3.8-.2-4.2 0-5 0-4.7.3-4.3.6-5.1-.2-5.2-.5-4.7 0-4.6.1-4.3-.4-3.9-.3-4.5.1-4.7.1-4.2.3-4.7.6-5-.2-4.2-.9-4.2-.2-4.8.3-4.1 0-.4-4.5-.3-4.1-.2-3.7 0-3.5z\" fill=\"#fffdf7\"></path><path d=\"M40 142l4.5.5 5.1 0 5-.2 4.2.2 4.8-.1 5.1-1 4.1-.5 4.4.5 5 .4 4.5.2 4.3.6 4.4-.1 4-.8 4.5-.1 3.6.9 2.5 2.1 1 3.1 .1 4.7 0 4.6-.1 4.3-.3 4.3-1.1 3.1-2.7 2.3-3.5 1.1-4.9.4-4.9.2-4.7-.1-3.7-.2-4.3-.6-4.9-.3-3.9.2-4 .3-5.2.1-4.8.5-4.7.3-5-.6-4.1-.8-3.9-.2-3-1-2.5-2.5-1.1-2.9-.6-3.9-.4-3.9-.2-4.8 .1-4.9 1.1-3 2.8-1.9z\" fill=\"url(#hpqfingers20)\"></path><text x=\"72\" y=\"128\" text-anchor=\"middle\" font-size=\"12.5\" font-weight=\"800\" fill=\"#26296b\" font-family=\"Inter,sans-serif\">Left</text></svg>", "3:left hand finger 5": "<svg style=\"width:100%;height:auto;display:block\" width=\"100%\" height=\"100%\" viewBox=\"0 0 150 176\"><defs><pattern id=\"hpqfingers20\" width=\"3.2\" height=\"3.2\" patternUnits=\"userSpaceOnUse\" patternTransform=\"rotate(40)\"><rect width=\"3.2\" height=\"3.2\" fill=\"#fffdf7\"></rect><line x1=\"0\" y1=\"0\" x2=\"0\" y2=\"3.2\" stroke=\"#26296b\" stroke-width=\"1.15\"></line></pattern></defs><path d=\"M48.7 88.2l4.3 0 3.8-.1 4.1.2 4.2.4 4.2-.3 4.7-.7 4.9-.2 4.5.2 4.5.1 4.5.2 3.9.2 3.6.1 4 .8 3.9 1.8 3.3 2.1 2.7 2.4 2.6 3.5 1.9 4.4 1.1 4.6 .4 4.6-.1 3.5 0 3.3-.1 3.1 0 3-.5 3.7-1.1 4-1.7 4-2 3.5-2.3 3.2-3.1 2.8-3.9 1.9-4 1-4 .3-4.6.4-4.5.1-4.1-.5-4.8-.1-4.8.1-4-.2-4.4-.4-4.9.2-4.1.5-4.3.4-5.2.2-4.6-.3-3.8-1.6-3.9-2.4-3.6-2.4-2.8-2.9-1.8-3.3-1.1-3.4-.6-3.5-.1-4.1 0-3.9-.1-3.8-.3-3.7-.3-3.6-.1-4.2 .6-4.2 1.3-3.8 2.5-3.3 3.7-2.9 4.3-2.3 3.9-1.5 3.8-.9z\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M105.7 33.5l0 0 3.7.5 3 2.2 2 3.2 .6 3.6-.1 4.7-.1 4.3-.1 3.6 0 3.7 0 4.4 .2 5 .2 4.8 .2 4.5-.1 4.6-.3 4.3-.3 3.8-.8 2.8-1.8 2.7-2.6 2.4-3.1 1.1 0 0-3.3-.4-2.7-1.8-2-2.8-.9-3.4-.3-4.6 0-4.2 0-4 .1-4.2-.1-4.6-.2-4.5-.1-4.2 0-4.4 .2-4.9 .1-4.7 0-4.2 .5-3 1.9-2.9 2.8-2.3z\" data-f=\"2\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M84.1 23.7l0 0 3.1 1 2.9 2.5 1.9 3 .7 3.5 .1 4.2 .1 4 0 4.2 .1 4.5 0 4.4-.1 4.7 0 5.1 .2 5.2 .2 4.5 .2 3.7 .1 3.8 .1 4.5 .1 4.6-.5 3.1-2.1 2.5-3.4 1.9-3.8.6 0 0-3.4-.9-2.8-2.1-2.1-2.6-.8-3.2 0-4.1 .3-3.8 .3-3.8 .2-4.8 .1-5.4-.2-5.2-.2-4.7-.3-4.3-.1-4.1 0-4.1 0-4.2 0-4.6 .1-4.7 .9-3.4 2.1-2.9 2.8-2z\" data-f=\"3\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M61.9 32.6l0 0 3.3.2 2.7 1.7 1.8 2.7 .8 3.5 .1 4.6 .3 4.6 .2 4.3 .1 4.1 0 4.3 0 5.2 0 5.5-.2 4.9-.3 4.3-.2 4.3-.1 4.1-.6 2.8-1.9 2.5-2.7 2.1-3.4 1.3 0 0-3.2-.3-2.4-1.9-1.6-3-.8-3.4-.4-4.2-.4-3.8-.2-4.3-.1-4.9 0-5.2 0-4.9 .1-4.7 .2-4.7 .1-4.6 0-4.2-.2-4.2 .4-3.2 1.9-2.6 3.1-1.9z\" data-f=\"4\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M40.1 48l0 0 3.5.4 3 1.4 1.8 2.7 .5 3.7-.2 4.7-.1 4.8 .1 4.8 .3 4.6 .3 4.2 .2 3.9 .2 3.9 .1 3.9-.8 3-2.5 2.4-3.6 1.7-3.6.8 0 0-3.2-.6-3-1.8-2-2.5-.6-3 .3-3.9 .2-4.2 .2-4.5 .2-4.5 0-4.4 0-4.5-.1-4.6-.1-4.3 .7-3.1 2.1-2.6 2.8-1.9z\" data-f=\"5\" fill=\"#e4572e\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><g transform=\"rotate(38 116 118)\"><path d=\"M116 72.7l0 0 4 1 3.2 1.8 2.1 2.8 .8 3.6 .2 4.6 .3 4.5 .2 4.5-.1 4.6-.3 4.7-.5 4.6-.3 4.4-.9 3.7-2.2 3.5-3 2.5-3.4.5 0 0-3.2-.9-3-2.4-2.4-3.5-1-3.8-.7-4.4-.7-4.7 0-4.5 .4-4.4 .3-4.6 .4-4.4 .4-4.1 .7-3.8 1.8-3.5 2.9-2.2z\" data-f=\"1\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path></g><path d=\"M25.9 92.2l5.2-.3 5.4-.3 4.3-.2 4.5.2 5 .3 4.5 0 3.9-.1 4.2.1 4.1 0 4.5-.3 5.1-.4 4.9-.3 4.5 0 4.8.6 4.4.7 4-.1 4.2-.4 4.4-.1 4.3 0 4.4-.2 0 3.5 .1 4 .2 4.5 .2 4.5 0 4.3-3.8-.2-4.2 0-5 0-4.7.3-4.3.6-5.1-.2-5.2-.5-4.7 0-4.6.1-4.3-.4-3.9-.3-4.5.1-4.7.1-4.2.3-4.7.6-5-.2-4.2-.9-4.2-.2-4.8.3-4.1 0-.4-4.5-.3-4.1-.2-3.7 0-3.5z\" fill=\"#fffdf7\"></path><path d=\"M40 142l4.5.5 5.1 0 5-.2 4.2.2 4.8-.1 5.1-1 4.1-.5 4.4.5 5 .4 4.5.2 4.3.6 4.4-.1 4-.8 4.5-.1 3.6.9 2.5 2.1 1 3.1 .1 4.7 0 4.6-.1 4.3-.3 4.3-1.1 3.1-2.7 2.3-3.5 1.1-4.9.4-4.9.2-4.7-.1-3.7-.2-4.3-.6-4.9-.3-3.9.2-4 .3-5.2.1-4.8.5-4.7.3-5-.6-4.1-.8-3.9-.2-3-1-2.5-2.5-1.1-2.9-.6-3.9-.4-3.9-.2-4.8 .1-4.9 1.1-3 2.8-1.9z\" fill=\"url(#hpqfingers20)\"></path><text x=\"72\" y=\"128\" text-anchor=\"middle\" font-size=\"12.5\" font-weight=\"800\" fill=\"#26296b\" font-family=\"Inter,sans-serif\">Left</text></svg>", "3:left hand finger 4": "<svg style=\"width:100%;height:auto;display:block\" width=\"100%\" height=\"100%\" viewBox=\"0 0 150 176\"><defs><pattern id=\"hpqfingers20\" width=\"3.2\" height=\"3.2\" patternUnits=\"userSpaceOnUse\" patternTransform=\"rotate(40)\"><rect width=\"3.2\" height=\"3.2\" fill=\"#fffdf7\"></rect><line x1=\"0\" y1=\"0\" x2=\"0\" y2=\"3.2\" stroke=\"#26296b\" stroke-width=\"1.15\"></line></pattern></defs><path d=\"M48.7 88.2l4.3 0 3.8-.1 4.1.2 4.2.4 4.2-.3 4.7-.7 4.9-.2 4.5.2 4.5.1 4.5.2 3.9.2 3.6.1 4 .8 3.9 1.8 3.3 2.1 2.7 2.4 2.6 3.5 1.9 4.4 1.1 4.6 .4 4.6-.1 3.5 0 3.3-.1 3.1 0 3-.5 3.7-1.1 4-1.7 4-2 3.5-2.3 3.2-3.1 2.8-3.9 1.9-4 1-4 .3-4.6.4-4.5.1-4.1-.5-4.8-.1-4.8.1-4-.2-4.4-.4-4.9.2-4.1.5-4.3.4-5.2.2-4.6-.3-3.8-1.6-3.9-2.4-3.6-2.4-2.8-2.9-1.8-3.3-1.1-3.4-.6-3.5-.1-4.1 0-3.9-.1-3.8-.3-3.7-.3-3.6-.1-4.2 .6-4.2 1.3-3.8 2.5-3.3 3.7-2.9 4.3-2.3 3.9-1.5 3.8-.9z\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M105.7 33.5l0 0 3.7.5 3 2.2 2 3.2 .6 3.6-.1 4.7-.1 4.3-.1 3.6 0 3.7 0 4.4 .2 5 .2 4.8 .2 4.5-.1 4.6-.3 4.3-.3 3.8-.8 2.8-1.8 2.7-2.6 2.4-3.1 1.1 0 0-3.3-.4-2.7-1.8-2-2.8-.9-3.4-.3-4.6 0-4.2 0-4 .1-4.2-.1-4.6-.2-4.5-.1-4.2 0-4.4 .2-4.9 .1-4.7 0-4.2 .5-3 1.9-2.9 2.8-2.3z\" data-f=\"2\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M84.1 23.7l0 0 3.1 1 2.9 2.5 1.9 3 .7 3.5 .1 4.2 .1 4 0 4.2 .1 4.5 0 4.4-.1 4.7 0 5.1 .2 5.2 .2 4.5 .2 3.7 .1 3.8 .1 4.5 .1 4.6-.5 3.1-2.1 2.5-3.4 1.9-3.8.6 0 0-3.4-.9-2.8-2.1-2.1-2.6-.8-3.2 0-4.1 .3-3.8 .3-3.8 .2-4.8 .1-5.4-.2-5.2-.2-4.7-.3-4.3-.1-4.1 0-4.1 0-4.2 0-4.6 .1-4.7 .9-3.4 2.1-2.9 2.8-2z\" data-f=\"3\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M61.9 32.6l0 0 3.3.2 2.7 1.7 1.8 2.7 .8 3.5 .1 4.6 .3 4.6 .2 4.3 .1 4.1 0 4.3 0 5.2 0 5.5-.2 4.9-.3 4.3-.2 4.3-.1 4.1-.6 2.8-1.9 2.5-2.7 2.1-3.4 1.3 0 0-3.2-.3-2.4-1.9-1.6-3-.8-3.4-.4-4.2-.4-3.8-.2-4.3-.1-4.9 0-5.2 0-4.9 .1-4.7 .2-4.7 .1-4.6 0-4.2-.2-4.2 .4-3.2 1.9-2.6 3.1-1.9z\" data-f=\"4\" fill=\"#e4572e\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M40.1 48l0 0 3.5.4 3 1.4 1.8 2.7 .5 3.7-.2 4.7-.1 4.8 .1 4.8 .3 4.6 .3 4.2 .2 3.9 .2 3.9 .1 3.9-.8 3-2.5 2.4-3.6 1.7-3.6.8 0 0-3.2-.6-3-1.8-2-2.5-.6-3 .3-3.9 .2-4.2 .2-4.5 .2-4.5 0-4.4 0-4.5-.1-4.6-.1-4.3 .7-3.1 2.1-2.6 2.8-1.9z\" data-f=\"5\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><g transform=\"rotate(38 116 118)\"><path d=\"M116 72.7l0 0 4 1 3.2 1.8 2.1 2.8 .8 3.6 .2 4.6 .3 4.5 .2 4.5-.1 4.6-.3 4.7-.5 4.6-.3 4.4-.9 3.7-2.2 3.5-3 2.5-3.4.5 0 0-3.2-.9-3-2.4-2.4-3.5-1-3.8-.7-4.4-.7-4.7 0-4.5 .4-4.4 .3-4.6 .4-4.4 .4-4.1 .7-3.8 1.8-3.5 2.9-2.2z\" data-f=\"1\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path></g><path d=\"M25.9 92.2l5.2-.3 5.4-.3 4.3-.2 4.5.2 5 .3 4.5 0 3.9-.1 4.2.1 4.1 0 4.5-.3 5.1-.4 4.9-.3 4.5 0 4.8.6 4.4.7 4-.1 4.2-.4 4.4-.1 4.3 0 4.4-.2 0 3.5 .1 4 .2 4.5 .2 4.5 0 4.3-3.8-.2-4.2 0-5 0-4.7.3-4.3.6-5.1-.2-5.2-.5-4.7 0-4.6.1-4.3-.4-3.9-.3-4.5.1-4.7.1-4.2.3-4.7.6-5-.2-4.2-.9-4.2-.2-4.8.3-4.1 0-.4-4.5-.3-4.1-.2-3.7 0-3.5z\" fill=\"#fffdf7\"></path><path d=\"M40 142l4.5.5 5.1 0 5-.2 4.2.2 4.8-.1 5.1-1 4.1-.5 4.4.5 5 .4 4.5.2 4.3.6 4.4-.1 4-.8 4.5-.1 3.6.9 2.5 2.1 1 3.1 .1 4.7 0 4.6-.1 4.3-.3 4.3-1.1 3.1-2.7 2.3-3.5 1.1-4.9.4-4.9.2-4.7-.1-3.7-.2-4.3-.6-4.9-.3-3.9.2-4 .3-5.2.1-4.8.5-4.7.3-5-.6-4.1-.8-3.9-.2-3-1-2.5-2.5-1.1-2.9-.6-3.9-.4-3.9-.2-4.8 .1-4.9 1.1-3 2.8-1.9z\" fill=\"url(#hpqfingers20)\"></path><text x=\"72\" y=\"128\" text-anchor=\"middle\" font-size=\"12.5\" font-weight=\"800\" fill=\"#26296b\" font-family=\"Inter,sans-serif\">Left</text></svg>", "3:1": "<svg style=\"width:100%;height:auto;display:block\" width=\"100%\" height=\"100%\" viewBox=\"0 0 150 176\"><defs><pattern id=\"hpqfingers20\" width=\"3.2\" height=\"3.2\" patternUnits=\"userSpaceOnUse\" patternTransform=\"rotate(40)\"><rect width=\"3.2\" height=\"3.2\" fill=\"#fffdf7\"></rect><line x1=\"0\" y1=\"0\" x2=\"0\" y2=\"3.2\" stroke=\"#26296b\" stroke-width=\"1.15\"></line></pattern></defs><path d=\"M48.7 88.2l4.3 0 3.8-.1 4.1.2 4.2.4 4.2-.3 4.7-.7 4.9-.2 4.5.2 4.5.1 4.5.2 3.9.2 3.6.1 4 .8 3.9 1.8 3.3 2.1 2.7 2.4 2.6 3.5 1.9 4.4 1.1 4.6 .4 4.6-.1 3.5 0 3.3-.1 3.1 0 3-.5 3.7-1.1 4-1.7 4-2 3.5-2.3 3.2-3.1 2.8-3.9 1.9-4 1-4 .3-4.6.4-4.5.1-4.1-.5-4.8-.1-4.8.1-4-.2-4.4-.4-4.9.2-4.1.5-4.3.4-5.2.2-4.6-.3-3.8-1.6-3.9-2.4-3.6-2.4-2.8-2.9-1.8-3.3-1.1-3.4-.6-3.5-.1-4.1 0-3.9-.1-3.8-.3-3.7-.3-3.6-.1-4.2 .6-4.2 1.3-3.8 2.5-3.3 3.7-2.9 4.3-2.3 3.9-1.5 3.8-.9z\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M105.7 33.5l0 0 3.7.5 3 2.2 2 3.2 .6 3.6-.1 4.7-.1 4.3-.1 3.6 0 3.7 0 4.4 .2 5 .2 4.8 .2 4.5-.1 4.6-.3 4.3-.3 3.8-.8 2.8-1.8 2.7-2.6 2.4-3.1 1.1 0 0-3.3-.4-2.7-1.8-2-2.8-.9-3.4-.3-4.6 0-4.2 0-4 .1-4.2-.1-4.6-.2-4.5-.1-4.2 0-4.4 .2-4.9 .1-4.7 0-4.2 .5-3 1.9-2.9 2.8-2.3z\" data-f=\"2\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M84.1 23.7l0 0 3.1 1 2.9 2.5 1.9 3 .7 3.5 .1 4.2 .1 4 0 4.2 .1 4.5 0 4.4-.1 4.7 0 5.1 .2 5.2 .2 4.5 .2 3.7 .1 3.8 .1 4.5 .1 4.6-.5 3.1-2.1 2.5-3.4 1.9-3.8.6 0 0-3.4-.9-2.8-2.1-2.1-2.6-.8-3.2 0-4.1 .3-3.8 .3-3.8 .2-4.8 .1-5.4-.2-5.2-.2-4.7-.3-4.3-.1-4.1 0-4.1 0-4.2 0-4.6 .1-4.7 .9-3.4 2.1-2.9 2.8-2z\" data-f=\"3\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M61.9 32.6l0 0 3.3.2 2.7 1.7 1.8 2.7 .8 3.5 .1 4.6 .3 4.6 .2 4.3 .1 4.1 0 4.3 0 5.2 0 5.5-.2 4.9-.3 4.3-.2 4.3-.1 4.1-.6 2.8-1.9 2.5-2.7 2.1-3.4 1.3 0 0-3.2-.3-2.4-1.9-1.6-3-.8-3.4-.4-4.2-.4-3.8-.2-4.3-.1-4.9 0-5.2 0-4.9 .1-4.7 .2-4.7 .1-4.6 0-4.2-.2-4.2 .4-3.2 1.9-2.6 3.1-1.9z\" data-f=\"4\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M40.1 48l0 0 3.5.4 3 1.4 1.8 2.7 .5 3.7-.2 4.7-.1 4.8 .1 4.8 .3 4.6 .3 4.2 .2 3.9 .2 3.9 .1 3.9-.8 3-2.5 2.4-3.6 1.7-3.6.8 0 0-3.2-.6-3-1.8-2-2.5-.6-3 .3-3.9 .2-4.2 .2-4.5 .2-4.5 0-4.4 0-4.5-.1-4.6-.1-4.3 .7-3.1 2.1-2.6 2.8-1.9z\" data-f=\"5\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><g transform=\"rotate(38 116 118)\"><path d=\"M116 72.7l0 0 4 1 3.2 1.8 2.1 2.8 .8 3.6 .2 4.6 .3 4.5 .2 4.5-.1 4.6-.3 4.7-.5 4.6-.3 4.4-.9 3.7-2.2 3.5-3 2.5-3.4.5 0 0-3.2-.9-3-2.4-2.4-3.5-1-3.8-.7-4.4-.7-4.7 0-4.5 .4-4.4 .3-4.6 .4-4.4 .4-4.1 .7-3.8 1.8-3.5 2.9-2.2z\" data-f=\"1\" fill=\"#e4572e\" stroke=\"#26296b\" stroke-width=\"2.6\"></path></g><path d=\"M25.9 92.2l5.2-.3 5.4-.3 4.3-.2 4.5.2 5 .3 4.5 0 3.9-.1 4.2.1 4.1 0 4.5-.3 5.1-.4 4.9-.3 4.5 0 4.8.6 4.4.7 4-.1 4.2-.4 4.4-.1 4.3 0 4.4-.2 0 3.5 .1 4 .2 4.5 .2 4.5 0 4.3-3.8-.2-4.2 0-5 0-4.7.3-4.3.6-5.1-.2-5.2-.5-4.7 0-4.6.1-4.3-.4-3.9-.3-4.5.1-4.7.1-4.2.3-4.7.6-5-.2-4.2-.9-4.2-.2-4.8.3-4.1 0-.4-4.5-.3-4.1-.2-3.7 0-3.5z\" fill=\"#fffdf7\"></path><path d=\"M40 142l4.5.5 5.1 0 5-.2 4.2.2 4.8-.1 5.1-1 4.1-.5 4.4.5 5 .4 4.5.2 4.3.6 4.4-.1 4-.8 4.5-.1 3.6.9 2.5 2.1 1 3.1 .1 4.7 0 4.6-.1 4.3-.3 4.3-1.1 3.1-2.7 2.3-3.5 1.1-4.9.4-4.9.2-4.7-.1-3.7-.2-4.3-.6-4.9-.3-3.9.2-4 .3-5.2.1-4.8.5-4.7.3-5-.6-4.1-.8-3.9-.2-3-1-2.5-2.5-1.1-2.9-.6-3.9-.4-3.9-.2-4.8 .1-4.9 1.1-3 2.8-1.9z\" fill=\"url(#hpqfingers20)\"></path><text x=\"72\" y=\"128\" text-anchor=\"middle\" font-size=\"12.5\" font-weight=\"800\" fill=\"#26296b\" font-family=\"Inter,sans-serif\">Left</text></svg>", "3:right hand finger 2": "<svg style=\"width:100%;height:auto;display:block\" width=\"100%\" height=\"100%\" viewBox=\"0 0 150 176\"><defs><pattern id=\"hpqfingers20\" width=\"3.2\" height=\"3.2\" patternUnits=\"userSpaceOnUse\" patternTransform=\"rotate(40)\"><rect width=\"3.2\" height=\"3.2\" fill=\"#fffdf7\"></rect><line x1=\"0\" y1=\"0\" x2=\"0\" y2=\"3.2\" stroke=\"#26296b\" stroke-width=\"1.15\"></line></pattern></defs><path d=\"M54.4 88.1l3.9 0 4.2.4 4.1.2 4.3-.6 5-.5 4.7 0 4.4.2 4.6.1 4.4.2 3.7 0 3.9-.2 4.3.3 4.1 1.3 3.6 1.4 3.3 1.9 3.2 3.1 2.5 3.8 1.7 4.2 1 4.4 .4 4.2 .1 3.3 0 3.1 0 3.1-.2 3.3-.6 4.3-1.1 4.2-1.6 4.1-2.3 3.6-2.9 2.7-2.8 2.2-3.1 1.8-4 1.4-4.4.3-4.2-.1-4.4.3-4.7.2-4.1-.3-4.5-.3-5 .1-4.2-.1-4.2-.4-4.8-.1-4.4.5-4 .4-4.7 0-4.8-.8-3.6-2-3-3-3-3.2-2.4-3.1-1.3-3.9-.5-4.2-.1-4.2 0-3.2-.4-3.2-.5-3.5-.6-4-.1-4.9 1-4.2 2.1-3.7 3-3.3 3.4-2.9 3.5-2 4-1.3 4.3-.9z\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M43.8 34.3l0 0 3.2 1 2.9 2.1 2.2 2.6 .9 3.1 .1 4.1 0 4.1-.2 4.4-.1 4.6-.1 4.6 0 4.8 0 4.9 .1 4.6 .3 4.1 .3 3.7 .4 4-.5 3.4-2.1 2.6-3.5 1.4-4.3.4 0 0-3.5-.7-2.5-1.8-1.6-2.6-.4-2.9 .4-3.7 0-4.1 0-4.8 0-4.9 0-4.8-.1-4.6-.1-4.3-.1-4.1-.1-4.1-.1-4.3 0-4.3 .7-3.3 1.8-2.7 2.8-2z\" data-f=\"2\" fill=\"#e4572e\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M66.3 24.6l0 0 3.5.2 2.9 1.7 1.9 2.7 .5 3.4-.1 4.7 0 4.6 0 4.2 0 4.1 .1 4.1 .3 4.3 .2 4.7 .2 5.2-.1 5.4-.2 4.8-.3 3.8-.3 3.8 0 4.1-.8 3.2-2.1 2.5-3 1.8-3.3 1.1 0 0-3.3-.2-2.7-1.6-1.7-2.9-.7-3.5-.4-3.9-.4-3.8-.2-4.1 .1-4.8 .3-4.9 .3-5 .2-4.9 0-4.6-.1-4.2-.1-4.2-.1-4.3-.1-4.1-.2-4 .6-3.4 2.2-3.1 3.2-2z\" data-f=\"3\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M88.1 32.5l0 0 3.2.9 2.8 1.9 2.1 2.7 .8 3.1 .1 4.1-.1 4.7-.1 5.1-.1 4.8 .1 4.4 .1 4.5 .2 4.8-.1 4.5 0 4.1 0 4.5 .3 4.7-.3 3.4-1.6 2.5-3 1.6-4.1.6 0 0-3.8-.9-2.7-2.3-1.8-2.9-.7-3.2 0-3.8 0-3.7 .2-4.4 .2-5 0-5.1-.1-4.8-.4-4.9-.3-4.9-.1-4.4 .1-3.9 .2-4.1 .9-3.5 2.1-3 2.8-1.8z\" data-f=\"4\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M109.4 48.4l0 0 3.8.7 3.1 1.8 1.8 2.5 .5 2.8-.1 3.7 .1 4.5 .3 5.2 .3 5.1 .1 4.2-.1 3.6-.3 3.8-.3 4.1-.8 3.2-2 2.6-2.7 1.9-3.1 1.1 0 0-3.2-.2-2.9-1.7-2-2.9-1-3.5-.3-4.1-.1-3.7 .2-3.9 .2-4.7 .1-4.8-.1-4.3-.2-3.8-.1-4.1 .6-3.7 1.9-3.1 2.7-1.8z\" data-f=\"5\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><g transform=\"rotate(-38 34 118)\"><path d=\"M33.8 72.5l0 0 3.6.6 2.9 1.9 2.5 3.2 .8 4-.2 4.3-.3 4.2 .1 4.3 .5 4.1 .2 4.4 0 4.7-.1 4.8-1 4.2-2.2 3.8-3 2.8-3.2 1.2 0 0-3.3-1.2-3.3-2.3-2.4-2.8-.7-4.1 .1-5-.5-4.1-.4-4.3 .1-5 .1-4.8 .2-4.9 0-5.3 .6-3.9 2-2.8 3.1-1.5z\" data-f=\"1\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path></g><path d=\"M32.9 91.8l5.1-.3 4.2 0 4.7.2 5 .2 4.2 0 4-.1 4.2.1 4.1 0 4.8-.4 5.1-.4 4.7-.3 4.5.2 4.8.8 4.3.5 3.9-.3 4.4-.4 4.4 0 4.2-.1 4.6-.2 4.8.2 0 4.2 0 4.1-.1 4.1-.1 4.4 0 4.3-4.4-.3-3.9-.2-3.9-.1-4.8-.1-4.9.3-4.3.5-4.8.2-5.3-.6-4.9-.2-4.6.2-4.4-.2-4-.5-4.2 0-4.8.2-4.4.2-4.3.6-5.1.1-4.5-.8-4-.5-4.7.2-.4-4.4-.2-4.3 .2-3.9 .4-3.7z\" fill=\"#fffdf7\"></path><path d=\"M46 142.5l5.2-.1 4.7-.1 4.3.3 5.1-.5 4.8-1 3.9-.1 4.7.6 5 .2 4.3.4 4.4.4 4.3-.4 4-.6 4.9.1 4.9-.2 2.7.6 2 2.4 .9 3.5 .3 4.9 .2 4.5 0 3.8-.3 3.8-1 3.1-2.1 2.5-3 1-5.2.3-5 .5-4.8.2-4.9 0-4-.1-3.9-.5-4.9-.5-4.3.1-3.8.3-4.8.1-5.1.4-4.6.5-4.9-.4-4.6-.8-2.4-1.2-2.1-2.3-1-2.9-.7-4.1-.4-4.4-.1-4.4 .4-4.3 1.3-2.8 2.4-2.1z\" fill=\"url(#hpqfingers20)\"></path><text x=\"78\" y=\"128\" text-anchor=\"middle\" font-size=\"12.5\" font-weight=\"800\" fill=\"#26296b\" font-family=\"Inter,sans-serif\">Right</text></svg>", "3:right hand finger 5": "<svg style=\"width:100%;height:auto;display:block\" width=\"100%\" height=\"100%\" viewBox=\"0 0 150 176\"><defs><pattern id=\"hpqfingers20\" width=\"3.2\" height=\"3.2\" patternUnits=\"userSpaceOnUse\" patternTransform=\"rotate(40)\"><rect width=\"3.2\" height=\"3.2\" fill=\"#fffdf7\"></rect><line x1=\"0\" y1=\"0\" x2=\"0\" y2=\"3.2\" stroke=\"#26296b\" stroke-width=\"1.15\"></line></pattern></defs><path d=\"M54.4 88.1l3.9 0 4.2.4 4.1.2 4.3-.6 5-.5 4.7 0 4.4.2 4.6.1 4.4.2 3.7 0 3.9-.2 4.3.3 4.1 1.3 3.6 1.4 3.3 1.9 3.2 3.1 2.5 3.8 1.7 4.2 1 4.4 .4 4.2 .1 3.3 0 3.1 0 3.1-.2 3.3-.6 4.3-1.1 4.2-1.6 4.1-2.3 3.6-2.9 2.7-2.8 2.2-3.1 1.8-4 1.4-4.4.3-4.2-.1-4.4.3-4.7.2-4.1-.3-4.5-.3-5 .1-4.2-.1-4.2-.4-4.8-.1-4.4.5-4 .4-4.7 0-4.8-.8-3.6-2-3-3-3-3.2-2.4-3.1-1.3-3.9-.5-4.2-.1-4.2 0-3.2-.4-3.2-.5-3.5-.6-4-.1-4.9 1-4.2 2.1-3.7 3-3.3 3.4-2.9 3.5-2 4-1.3 4.3-.9z\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M43.8 34.3l0 0 3.2 1 2.9 2.1 2.2 2.6 .9 3.1 .1 4.1 0 4.1-.2 4.4-.1 4.6-.1 4.6 0 4.8 0 4.9 .1 4.6 .3 4.1 .3 3.7 .4 4-.5 3.4-2.1 2.6-3.5 1.4-4.3.4 0 0-3.5-.7-2.5-1.8-1.6-2.6-.4-2.9 .4-3.7 0-4.1 0-4.8 0-4.9 0-4.8-.1-4.6-.1-4.3-.1-4.1-.1-4.1-.1-4.3 0-4.3 .7-3.3 1.8-2.7 2.8-2z\" data-f=\"2\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M66.3 24.6l0 0 3.5.2 2.9 1.7 1.9 2.7 .5 3.4-.1 4.7 0 4.6 0 4.2 0 4.1 .1 4.1 .3 4.3 .2 4.7 .2 5.2-.1 5.4-.2 4.8-.3 3.8-.3 3.8 0 4.1-.8 3.2-2.1 2.5-3 1.8-3.3 1.1 0 0-3.3-.2-2.7-1.6-1.7-2.9-.7-3.5-.4-3.9-.4-3.8-.2-4.1 .1-4.8 .3-4.9 .3-5 .2-4.9 0-4.6-.1-4.2-.1-4.2-.1-4.3-.1-4.1-.2-4 .6-3.4 2.2-3.1 3.2-2z\" data-f=\"3\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M88.1 32.5l0 0 3.2.9 2.8 1.9 2.1 2.7 .8 3.1 .1 4.1-.1 4.7-.1 5.1-.1 4.8 .1 4.4 .1 4.5 .2 4.8-.1 4.5 0 4.1 0 4.5 .3 4.7-.3 3.4-1.6 2.5-3 1.6-4.1.6 0 0-3.8-.9-2.7-2.3-1.8-2.9-.7-3.2 0-3.8 0-3.7 .2-4.4 .2-5 0-5.1-.1-4.8-.4-4.9-.3-4.9-.1-4.4 .1-3.9 .2-4.1 .9-3.5 2.1-3 2.8-1.8z\" data-f=\"4\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M109.4 48.4l0 0 3.8.7 3.1 1.8 1.8 2.5 .5 2.8-.1 3.7 .1 4.5 .3 5.2 .3 5.1 .1 4.2-.1 3.6-.3 3.8-.3 4.1-.8 3.2-2 2.6-2.7 1.9-3.1 1.1 0 0-3.2-.2-2.9-1.7-2-2.9-1-3.5-.3-4.1-.1-3.7 .2-3.9 .2-4.7 .1-4.8-.1-4.3-.2-3.8-.1-4.1 .6-3.7 1.9-3.1 2.7-1.8z\" data-f=\"5\" fill=\"#e4572e\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><g transform=\"rotate(-38 34 118)\"><path d=\"M33.8 72.5l0 0 3.6.6 2.9 1.9 2.5 3.2 .8 4-.2 4.3-.3 4.2 .1 4.3 .5 4.1 .2 4.4 0 4.7-.1 4.8-1 4.2-2.2 3.8-3 2.8-3.2 1.2 0 0-3.3-1.2-3.3-2.3-2.4-2.8-.7-4.1 .1-5-.5-4.1-.4-4.3 .1-5 .1-4.8 .2-4.9 0-5.3 .6-3.9 2-2.8 3.1-1.5z\" data-f=\"1\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path></g><path d=\"M32.9 91.8l5.1-.3 4.2 0 4.7.2 5 .2 4.2 0 4-.1 4.2.1 4.1 0 4.8-.4 5.1-.4 4.7-.3 4.5.2 4.8.8 4.3.5 3.9-.3 4.4-.4 4.4 0 4.2-.1 4.6-.2 4.8.2 0 4.2 0 4.1-.1 4.1-.1 4.4 0 4.3-4.4-.3-3.9-.2-3.9-.1-4.8-.1-4.9.3-4.3.5-4.8.2-5.3-.6-4.9-.2-4.6.2-4.4-.2-4-.5-4.2 0-4.8.2-4.4.2-4.3.6-5.1.1-4.5-.8-4-.5-4.7.2-.4-4.4-.2-4.3 .2-3.9 .4-3.7z\" fill=\"#fffdf7\"></path><path d=\"M46 142.5l5.2-.1 4.7-.1 4.3.3 5.1-.5 4.8-1 3.9-.1 4.7.6 5 .2 4.3.4 4.4.4 4.3-.4 4-.6 4.9.1 4.9-.2 2.7.6 2 2.4 .9 3.5 .3 4.9 .2 4.5 0 3.8-.3 3.8-1 3.1-2.1 2.5-3 1-5.2.3-5 .5-4.8.2-4.9 0-4-.1-3.9-.5-4.9-.5-4.3.1-3.8.3-4.8.1-5.1.4-4.6.5-4.9-.4-4.6-.8-2.4-1.2-2.1-2.3-1-2.9-.7-4.1-.4-4.4-.1-4.4 .4-4.3 1.3-2.8 2.4-2.1z\" fill=\"url(#hpqfingers20)\"></path><text x=\"78\" y=\"128\" text-anchor=\"middle\" font-size=\"12.5\" font-weight=\"800\" fill=\"#26296b\" font-family=\"Inter,sans-serif\">Right</text></svg>", "3:right hand finger 3": "<svg style=\"width:100%;height:auto;display:block\" width=\"100%\" height=\"100%\" viewBox=\"0 0 150 176\"><defs><pattern id=\"hpqfingers20\" width=\"3.2\" height=\"3.2\" patternUnits=\"userSpaceOnUse\" patternTransform=\"rotate(40)\"><rect width=\"3.2\" height=\"3.2\" fill=\"#fffdf7\"></rect><line x1=\"0\" y1=\"0\" x2=\"0\" y2=\"3.2\" stroke=\"#26296b\" stroke-width=\"1.15\"></line></pattern></defs><path d=\"M54.4 88.1l3.9 0 4.2.4 4.1.2 4.3-.6 5-.5 4.7 0 4.4.2 4.6.1 4.4.2 3.7 0 3.9-.2 4.3.3 4.1 1.3 3.6 1.4 3.3 1.9 3.2 3.1 2.5 3.8 1.7 4.2 1 4.4 .4 4.2 .1 3.3 0 3.1 0 3.1-.2 3.3-.6 4.3-1.1 4.2-1.6 4.1-2.3 3.6-2.9 2.7-2.8 2.2-3.1 1.8-4 1.4-4.4.3-4.2-.1-4.4.3-4.7.2-4.1-.3-4.5-.3-5 .1-4.2-.1-4.2-.4-4.8-.1-4.4.5-4 .4-4.7 0-4.8-.8-3.6-2-3-3-3-3.2-2.4-3.1-1.3-3.9-.5-4.2-.1-4.2 0-3.2-.4-3.2-.5-3.5-.6-4-.1-4.9 1-4.2 2.1-3.7 3-3.3 3.4-2.9 3.5-2 4-1.3 4.3-.9z\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M43.8 34.3l0 0 3.2 1 2.9 2.1 2.2 2.6 .9 3.1 .1 4.1 0 4.1-.2 4.4-.1 4.6-.1 4.6 0 4.8 0 4.9 .1 4.6 .3 4.1 .3 3.7 .4 4-.5 3.4-2.1 2.6-3.5 1.4-4.3.4 0 0-3.5-.7-2.5-1.8-1.6-2.6-.4-2.9 .4-3.7 0-4.1 0-4.8 0-4.9 0-4.8-.1-4.6-.1-4.3-.1-4.1-.1-4.1-.1-4.3 0-4.3 .7-3.3 1.8-2.7 2.8-2z\" data-f=\"2\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M66.3 24.6l0 0 3.5.2 2.9 1.7 1.9 2.7 .5 3.4-.1 4.7 0 4.6 0 4.2 0 4.1 .1 4.1 .3 4.3 .2 4.7 .2 5.2-.1 5.4-.2 4.8-.3 3.8-.3 3.8 0 4.1-.8 3.2-2.1 2.5-3 1.8-3.3 1.1 0 0-3.3-.2-2.7-1.6-1.7-2.9-.7-3.5-.4-3.9-.4-3.8-.2-4.1 .1-4.8 .3-4.9 .3-5 .2-4.9 0-4.6-.1-4.2-.1-4.2-.1-4.3-.1-4.1-.2-4 .6-3.4 2.2-3.1 3.2-2z\" data-f=\"3\" fill=\"#e4572e\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M88.1 32.5l0 0 3.2.9 2.8 1.9 2.1 2.7 .8 3.1 .1 4.1-.1 4.7-.1 5.1-.1 4.8 .1 4.4 .1 4.5 .2 4.8-.1 4.5 0 4.1 0 4.5 .3 4.7-.3 3.4-1.6 2.5-3 1.6-4.1.6 0 0-3.8-.9-2.7-2.3-1.8-2.9-.7-3.2 0-3.8 0-3.7 .2-4.4 .2-5 0-5.1-.1-4.8-.4-4.9-.3-4.9-.1-4.4 .1-3.9 .2-4.1 .9-3.5 2.1-3 2.8-1.8z\" data-f=\"4\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M109.4 48.4l0 0 3.8.7 3.1 1.8 1.8 2.5 .5 2.8-.1 3.7 .1 4.5 .3 5.2 .3 5.1 .1 4.2-.1 3.6-.3 3.8-.3 4.1-.8 3.2-2 2.6-2.7 1.9-3.1 1.1 0 0-3.2-.2-2.9-1.7-2-2.9-1-3.5-.3-4.1-.1-3.7 .2-3.9 .2-4.7 .1-4.8-.1-4.3-.2-3.8-.1-4.1 .6-3.7 1.9-3.1 2.7-1.8z\" data-f=\"5\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><g transform=\"rotate(-38 34 118)\"><path d=\"M33.8 72.5l0 0 3.6.6 2.9 1.9 2.5 3.2 .8 4-.2 4.3-.3 4.2 .1 4.3 .5 4.1 .2 4.4 0 4.7-.1 4.8-1 4.2-2.2 3.8-3 2.8-3.2 1.2 0 0-3.3-1.2-3.3-2.3-2.4-2.8-.7-4.1 .1-5-.5-4.1-.4-4.3 .1-5 .1-4.8 .2-4.9 0-5.3 .6-3.9 2-2.8 3.1-1.5z\" data-f=\"1\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path></g><path d=\"M32.9 91.8l5.1-.3 4.2 0 4.7.2 5 .2 4.2 0 4-.1 4.2.1 4.1 0 4.8-.4 5.1-.4 4.7-.3 4.5.2 4.8.8 4.3.5 3.9-.3 4.4-.4 4.4 0 4.2-.1 4.6-.2 4.8.2 0 4.2 0 4.1-.1 4.1-.1 4.4 0 4.3-4.4-.3-3.9-.2-3.9-.1-4.8-.1-4.9.3-4.3.5-4.8.2-5.3-.6-4.9-.2-4.6.2-4.4-.2-4-.5-4.2 0-4.8.2-4.4.2-4.3.6-5.1.1-4.5-.8-4-.5-4.7.2-.4-4.4-.2-4.3 .2-3.9 .4-3.7z\" fill=\"#fffdf7\"></path><path d=\"M46 142.5l5.2-.1 4.7-.1 4.3.3 5.1-.5 4.8-1 3.9-.1 4.7.6 5 .2 4.3.4 4.4.4 4.3-.4 4-.6 4.9.1 4.9-.2 2.7.6 2 2.4 .9 3.5 .3 4.9 .2 4.5 0 3.8-.3 3.8-1 3.1-2.1 2.5-3 1-5.2.3-5 .5-4.8.2-4.9 0-4-.1-3.9-.5-4.9-.5-4.3.1-3.8.3-4.8.1-5.1.4-4.6.5-4.9-.4-4.6-.8-2.4-1.2-2.1-2.3-1-2.9-.7-4.1-.4-4.4-.1-4.4 .4-4.3 1.3-2.8 2.4-2.1z\" fill=\"url(#hpqfingers20)\"></path><text x=\"78\" y=\"128\" text-anchor=\"middle\" font-size=\"12.5\" font-weight=\"800\" fill=\"#26296b\" font-family=\"Inter,sans-serif\">Right</text></svg>", "3:left hand finger 3": "<svg style=\"width:100%;height:auto;display:block\" width=\"100%\" height=\"100%\" viewBox=\"0 0 150 176\"><defs><pattern id=\"hpqfingers20\" width=\"3.2\" height=\"3.2\" patternUnits=\"userSpaceOnUse\" patternTransform=\"rotate(40)\"><rect width=\"3.2\" height=\"3.2\" fill=\"#fffdf7\"></rect><line x1=\"0\" y1=\"0\" x2=\"0\" y2=\"3.2\" stroke=\"#26296b\" stroke-width=\"1.15\"></line></pattern></defs><path d=\"M48.7 88.2l4.3 0 3.8-.1 4.1.2 4.2.4 4.2-.3 4.7-.7 4.9-.2 4.5.2 4.5.1 4.5.2 3.9.2 3.6.1 4 .8 3.9 1.8 3.3 2.1 2.7 2.4 2.6 3.5 1.9 4.4 1.1 4.6 .4 4.6-.1 3.5 0 3.3-.1 3.1 0 3-.5 3.7-1.1 4-1.7 4-2 3.5-2.3 3.2-3.1 2.8-3.9 1.9-4 1-4 .3-4.6.4-4.5.1-4.1-.5-4.8-.1-4.8.1-4-.2-4.4-.4-4.9.2-4.1.5-4.3.4-5.2.2-4.6-.3-3.8-1.6-3.9-2.4-3.6-2.4-2.8-2.9-1.8-3.3-1.1-3.4-.6-3.5-.1-4.1 0-3.9-.1-3.8-.3-3.7-.3-3.6-.1-4.2 .6-4.2 1.3-3.8 2.5-3.3 3.7-2.9 4.3-2.3 3.9-1.5 3.8-.9z\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M105.7 33.5l0 0 3.7.5 3 2.2 2 3.2 .6 3.6-.1 4.7-.1 4.3-.1 3.6 0 3.7 0 4.4 .2 5 .2 4.8 .2 4.5-.1 4.6-.3 4.3-.3 3.8-.8 2.8-1.8 2.7-2.6 2.4-3.1 1.1 0 0-3.3-.4-2.7-1.8-2-2.8-.9-3.4-.3-4.6 0-4.2 0-4 .1-4.2-.1-4.6-.2-4.5-.1-4.2 0-4.4 .2-4.9 .1-4.7 0-4.2 .5-3 1.9-2.9 2.8-2.3z\" data-f=\"2\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M84.1 23.7l0 0 3.1 1 2.9 2.5 1.9 3 .7 3.5 .1 4.2 .1 4 0 4.2 .1 4.5 0 4.4-.1 4.7 0 5.1 .2 5.2 .2 4.5 .2 3.7 .1 3.8 .1 4.5 .1 4.6-.5 3.1-2.1 2.5-3.4 1.9-3.8.6 0 0-3.4-.9-2.8-2.1-2.1-2.6-.8-3.2 0-4.1 .3-3.8 .3-3.8 .2-4.8 .1-5.4-.2-5.2-.2-4.7-.3-4.3-.1-4.1 0-4.1 0-4.2 0-4.6 .1-4.7 .9-3.4 2.1-2.9 2.8-2z\" data-f=\"3\" fill=\"#e4572e\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M61.9 32.6l0 0 3.3.2 2.7 1.7 1.8 2.7 .8 3.5 .1 4.6 .3 4.6 .2 4.3 .1 4.1 0 4.3 0 5.2 0 5.5-.2 4.9-.3 4.3-.2 4.3-.1 4.1-.6 2.8-1.9 2.5-2.7 2.1-3.4 1.3 0 0-3.2-.3-2.4-1.9-1.6-3-.8-3.4-.4-4.2-.4-3.8-.2-4.3-.1-4.9 0-5.2 0-4.9 .1-4.7 .2-4.7 .1-4.6 0-4.2-.2-4.2 .4-3.2 1.9-2.6 3.1-1.9z\" data-f=\"4\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M40.1 48l0 0 3.5.4 3 1.4 1.8 2.7 .5 3.7-.2 4.7-.1 4.8 .1 4.8 .3 4.6 .3 4.2 .2 3.9 .2 3.9 .1 3.9-.8 3-2.5 2.4-3.6 1.7-3.6.8 0 0-3.2-.6-3-1.8-2-2.5-.6-3 .3-3.9 .2-4.2 .2-4.5 .2-4.5 0-4.4 0-4.5-.1-4.6-.1-4.3 .7-3.1 2.1-2.6 2.8-1.9z\" data-f=\"5\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><g transform=\"rotate(38 116 118)\"><path d=\"M116 72.7l0 0 4 1 3.2 1.8 2.1 2.8 .8 3.6 .2 4.6 .3 4.5 .2 4.5-.1 4.6-.3 4.7-.5 4.6-.3 4.4-.9 3.7-2.2 3.5-3 2.5-3.4.5 0 0-3.2-.9-3-2.4-2.4-3.5-1-3.8-.7-4.4-.7-4.7 0-4.5 .4-4.4 .3-4.6 .4-4.4 .4-4.1 .7-3.8 1.8-3.5 2.9-2.2z\" data-f=\"1\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path></g><path d=\"M25.9 92.2l5.2-.3 5.4-.3 4.3-.2 4.5.2 5 .3 4.5 0 3.9-.1 4.2.1 4.1 0 4.5-.3 5.1-.4 4.9-.3 4.5 0 4.8.6 4.4.7 4-.1 4.2-.4 4.4-.1 4.3 0 4.4-.2 0 3.5 .1 4 .2 4.5 .2 4.5 0 4.3-3.8-.2-4.2 0-5 0-4.7.3-4.3.6-5.1-.2-5.2-.5-4.7 0-4.6.1-4.3-.4-3.9-.3-4.5.1-4.7.1-4.2.3-4.7.6-5-.2-4.2-.9-4.2-.2-4.8.3-4.1 0-.4-4.5-.3-4.1-.2-3.7 0-3.5z\" fill=\"#fffdf7\"></path><path d=\"M40 142l4.5.5 5.1 0 5-.2 4.2.2 4.8-.1 5.1-1 4.1-.5 4.4.5 5 .4 4.5.2 4.3.6 4.4-.1 4-.8 4.5-.1 3.6.9 2.5 2.1 1 3.1 .1 4.7 0 4.6-.1 4.3-.3 4.3-1.1 3.1-2.7 2.3-3.5 1.1-4.9.4-4.9.2-4.7-.1-3.7-.2-4.3-.6-4.9-.3-3.9.2-4 .3-5.2.1-4.8.5-4.7.3-5-.6-4.1-.8-3.9-.2-3-1-2.5-2.5-1.1-2.9-.6-3.9-.4-3.9-.2-4.8 .1-4.9 1.1-3 2.8-1.9z\" fill=\"url(#hpqfingers20)\"></path><text x=\"72\" y=\"128\" text-anchor=\"middle\" font-size=\"12.5\" font-weight=\"800\" fill=\"#26296b\" font-family=\"Inter,sans-serif\">Left</text></svg>", "3:right hand finger 4": "<svg style=\"width:100%;height:auto;display:block\" width=\"100%\" height=\"100%\" viewBox=\"0 0 150 176\"><defs><pattern id=\"hpqfingers20\" width=\"3.2\" height=\"3.2\" patternUnits=\"userSpaceOnUse\" patternTransform=\"rotate(40)\"><rect width=\"3.2\" height=\"3.2\" fill=\"#fffdf7\"></rect><line x1=\"0\" y1=\"0\" x2=\"0\" y2=\"3.2\" stroke=\"#26296b\" stroke-width=\"1.15\"></line></pattern></defs><path d=\"M54.4 88.1l3.9 0 4.2.4 4.1.2 4.3-.6 5-.5 4.7 0 4.4.2 4.6.1 4.4.2 3.7 0 3.9-.2 4.3.3 4.1 1.3 3.6 1.4 3.3 1.9 3.2 3.1 2.5 3.8 1.7 4.2 1 4.4 .4 4.2 .1 3.3 0 3.1 0 3.1-.2 3.3-.6 4.3-1.1 4.2-1.6 4.1-2.3 3.6-2.9 2.7-2.8 2.2-3.1 1.8-4 1.4-4.4.3-4.2-.1-4.4.3-4.7.2-4.1-.3-4.5-.3-5 .1-4.2-.1-4.2-.4-4.8-.1-4.4.5-4 .4-4.7 0-4.8-.8-3.6-2-3-3-3-3.2-2.4-3.1-1.3-3.9-.5-4.2-.1-4.2 0-3.2-.4-3.2-.5-3.5-.6-4-.1-4.9 1-4.2 2.1-3.7 3-3.3 3.4-2.9 3.5-2 4-1.3 4.3-.9z\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M43.8 34.3l0 0 3.2 1 2.9 2.1 2.2 2.6 .9 3.1 .1 4.1 0 4.1-.2 4.4-.1 4.6-.1 4.6 0 4.8 0 4.9 .1 4.6 .3 4.1 .3 3.7 .4 4-.5 3.4-2.1 2.6-3.5 1.4-4.3.4 0 0-3.5-.7-2.5-1.8-1.6-2.6-.4-2.9 .4-3.7 0-4.1 0-4.8 0-4.9 0-4.8-.1-4.6-.1-4.3-.1-4.1-.1-4.1-.1-4.3 0-4.3 .7-3.3 1.8-2.7 2.8-2z\" data-f=\"2\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M66.3 24.6l0 0 3.5.2 2.9 1.7 1.9 2.7 .5 3.4-.1 4.7 0 4.6 0 4.2 0 4.1 .1 4.1 .3 4.3 .2 4.7 .2 5.2-.1 5.4-.2 4.8-.3 3.8-.3 3.8 0 4.1-.8 3.2-2.1 2.5-3 1.8-3.3 1.1 0 0-3.3-.2-2.7-1.6-1.7-2.9-.7-3.5-.4-3.9-.4-3.8-.2-4.1 .1-4.8 .3-4.9 .3-5 .2-4.9 0-4.6-.1-4.2-.1-4.2-.1-4.3-.1-4.1-.2-4 .6-3.4 2.2-3.1 3.2-2z\" data-f=\"3\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M88.1 32.5l0 0 3.2.9 2.8 1.9 2.1 2.7 .8 3.1 .1 4.1-.1 4.7-.1 5.1-.1 4.8 .1 4.4 .1 4.5 .2 4.8-.1 4.5 0 4.1 0 4.5 .3 4.7-.3 3.4-1.6 2.5-3 1.6-4.1.6 0 0-3.8-.9-2.7-2.3-1.8-2.9-.7-3.2 0-3.8 0-3.7 .2-4.4 .2-5 0-5.1-.1-4.8-.4-4.9-.3-4.9-.1-4.4 .1-3.9 .2-4.1 .9-3.5 2.1-3 2.8-1.8z\" data-f=\"4\" fill=\"#e4572e\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><path d=\"M109.4 48.4l0 0 3.8.7 3.1 1.8 1.8 2.5 .5 2.8-.1 3.7 .1 4.5 .3 5.2 .3 5.1 .1 4.2-.1 3.6-.3 3.8-.3 4.1-.8 3.2-2 2.6-2.7 1.9-3.1 1.1 0 0-3.2-.2-2.9-1.7-2-2.9-1-3.5-.3-4.1-.1-3.7 .2-3.9 .2-4.7 .1-4.8-.1-4.3-.2-3.8-.1-4.1 .6-3.7 1.9-3.1 2.7-1.8z\" data-f=\"5\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path><g transform=\"rotate(-38 34 118)\"><path d=\"M33.8 72.5l0 0 3.6.6 2.9 1.9 2.5 3.2 .8 4-.2 4.3-.3 4.2 .1 4.3 .5 4.1 .2 4.4 0 4.7-.1 4.8-1 4.2-2.2 3.8-3 2.8-3.2 1.2 0 0-3.3-1.2-3.3-2.3-2.4-2.8-.7-4.1 .1-5-.5-4.1-.4-4.3 .1-5 .1-4.8 .2-4.9 0-5.3 .6-3.9 2-2.8 3.1-1.5z\" data-f=\"1\" fill=\"#fffdf7\" stroke=\"#26296b\" stroke-width=\"2.6\"></path></g><path d=\"M32.9 91.8l5.1-.3 4.2 0 4.7.2 5 .2 4.2 0 4-.1 4.2.1 4.1 0 4.8-.4 5.1-.4 4.7-.3 4.5.2 4.8.8 4.3.5 3.9-.3 4.4-.4 4.4 0 4.2-.1 4.6-.2 4.8.2 0 4.2 0 4.1-.1 4.1-.1 4.4 0 4.3-4.4-.3-3.9-.2-3.9-.1-4.8-.1-4.9.3-4.3.5-4.8.2-5.3-.6-4.9-.2-4.6.2-4.4-.2-4-.5-4.2 0-4.8.2-4.4.2-4.3.6-5.1.1-4.5-.8-4-.5-4.7.2-.4-4.4-.2-4.3 .2-3.9 .4-3.7z\" fill=\"#fffdf7\"></path><path d=\"M46 142.5l5.2-.1 4.7-.1 4.3.3 5.1-.5 4.8-1 3.9-.1 4.7.6 5 .2 4.3.4 4.4.4 4.3-.4 4-.6 4.9.1 4.9-.2 2.7.6 2 2.4 .9 3.5 .3 4.9 .2 4.5 0 3.8-.3 3.8-1 3.1-2.1 2.5-3 1-5.2.3-5 .5-4.8.2-4.9 0-4-.1-3.9-.5-4.9-.5-4.3.1-3.8.3-4.8.1-5.1.4-4.6.5-4.9-.4-4.6-.8-2.4-1.2-2.1-2.3-1-2.9-.7-4.1-.4-4.4-.1-4.4 .4-4.3 1.3-2.8 2.4-2.1z\" fill=\"url(#hpqfingers20)\"></path><text x=\"78\" y=\"128\" text-anchor=\"middle\" font-size=\"12.5\" font-weight=\"800\" fill=\"#26296b\" font-family=\"Inter,sans-serif\">Right</text></svg>"};

// ---- Read & listen: the app's moving posture and hand drawings in the lens (her 12 Nov: "움직이는 것 다 끼워서") ----
// Three widgets, each the app's own drawing: the stool (side view, height and distance), the elbows (front view)
// and the hand (side view, the good shape and five faults). The narration sets the pose; the reader can press or drag.
(function () {
  const SIT = { good: [114, 100], low: [124, 100], high: [106, 100], close: [114, 124], far: [114, 90] };
  const SITL = { good: 'Just right', low: 'Stool too low', high: 'Stool too high', close: 'Too close', far: 'Too far' };
  const HANDS = ['good', 'flat', 'bridge', 'nail', 'low', 'high'];
  const FRONT = { good: 0.45, tight: 0.05, wings: 0.95 };
  const GOOD = [80, 55, 24, -3, -2];
  const W = {};   // kind -> state
  const chip = (on, txt, data, bad) => `<button type="button" class="pch${on ? ' on' : ''}" data-v="${data}">${bad ? '<span class="px">✗</span> ' : on && !bad ? '✓ ' : ''}${txt}</button>`;
  function anim(st, to, draw, ms = 520) {
    cancelAnimationFrame(st.raf); const from = st.v.slice(), t0 = performance.now();
    const step = (now) => { const k = Math.min(1, (now - t0) / ms), e = pEase(k); st.v = from.map((x, i) => x + (to[i] - x) * e); draw(); if (k < 1) st.raf = requestAnimationFrame(step); };
    st.raf = requestAnimationFrame(step);
  }
  function cycle(st, list, go) { clearInterval(st.cyc); let i = 0; go(list[0]); st.cyc = setInterval(() => { if (!st.el.isConnected) return clearInterval(st.cyc); i = (i + 1) % list.length; go(list[i]); }, 1900); }
  // the stool, from the side
  function mountSit(el) {
    const st = W.sit = { el, v: SIT.low.slice(), id: 'low' };
    el.innerHTML = `<div class="pchips">${Object.keys(SIT).map(k => chip(false, SITL[k], k, k !== 'good')).join('')}</div><div class="pdraw"></div>
<div class="psl"><label>Height<input type="range" min="0" max="30" data-s="h"></label><label>Distance<input type="range" min="0" max="44" data-s="d"></label></div><div class="pck"></div>`;
    const draw = () => {
      const [y, x] = st.v, p = sitPose376(y, x, false), cks = sitChecks376(p);
      el.querySelector('.pdraw').innerHTML = penSvg(penSitShapes(y, x, false, cks));
      el.querySelector('.pck').innerHTML = cks.map(c => `<div class="${c.ok ? 'ok' : 'no'}"><b>${c.ok ? '✓' : '✗'}</b> ${c.label}${c.ok ? '' : '<span>: ' + c.fix + '</span>'}</div>`).join('');
      el.querySelector('[data-s=h]').value = 130 - y; el.querySelector('[data-s=d]').value = 132 - x;
      el.querySelectorAll('.pch').forEach(b => b.classList.toggle('on', b.dataset.v === st.id));
    };
    st.draw = draw;
    el.querySelectorAll('.pch').forEach(b => b.onclick = () => { clearInterval(st.cyc); st.id = b.dataset.v; anim(st, SIT[st.id], draw); });
    el.querySelectorAll('input').forEach(r => r.oninput = () => { clearInterval(st.cyc); cancelAnimationFrame(st.raf); st.id = '';
      st.v = [130 - +el.querySelector('[data-s=h]').value, 132 - +el.querySelector('[data-s=d]').value]; draw(); });
    draw();
  }
  // the elbows, from the front
  function mountFront(el) {
    const st = W.front = { el, v: [0.05], id: 'tight' };
    el.innerHTML = `<div class="pdraw pfront"></div><div class="psl"><label>Elbows<input type="range" min="0" max="100" data-s="g"></label></div><div class="pck"></div>`;
    const draw = () => { const g = st.v[0], ok = g >= 0.3 && g <= 0.65;
      el.querySelector('.pdraw').innerHTML = penSvg(penFrontShapes(g, ok), { vb: [0, 20, 150, 146] });
      el.querySelector('.pck').innerHTML = `<div class="${ok ? 'ok' : 'no'}"><b>${ok ? '✓' : '✗'}</b> ${g < 0.3 ? 'Elbows stuck to the body' : g > 0.65 ? 'Chicken wings: elbows too far out' : 'Elbows a fist away from the body'}</div>`;
      el.querySelector('[data-s=g]').value = Math.round(g * 100); };
    st.draw = draw;
    el.querySelector('input').oninput = (e) => { clearInterval(st.cyc); cancelAnimationFrame(st.raf); st.v = [+e.target.value / 100]; draw(); };
    draw();
  }
  // the hand, from the side
  function mountHand(el) {
    const st = W.hand = { el, v: GOOD.slice(), id: 'good' };
    el.innerHTML = `<div class="pchips">${HANDS.map(k => chip(false, k === 'good' ? 'The good shape' : HAND_POSES[k].title, k, k !== 'good')).join('')}</div><div class="pdraw"></div><div class="pck"></div>`;
    const draw = () => {
      const r = penHandSide(st.v, { ball: st.id === 'good', nail: st.id === 'nail', halo: true });
      el.querySelector('.pdraw').innerHTML = penSvg(r.shapes, { vb: [34, 26, 258, 126] });
      const P = st.id === 'good' ? null : HAND_POSES[st.id];
      el.querySelector('.pck').innerHTML = P ? `<div class="no"><b>✗</b> ${P.title}<span>: ${P.see}</span></div>` : `<div class="ok"><b>✓</b> The good shape<span>: knuckles up like a bridge, the wrist level, playing on the fingertip.</span></div>`;
      el.querySelectorAll('.pch').forEach(b => b.classList.toggle('on', b.dataset.v === st.id));
    };
    st.draw = draw;
    el.querySelectorAll('.pch').forEach(b => b.onclick = () => { clearInterval(st.cyc); st.id = b.dataset.v; anim(st, st.id === 'good' ? GOOD : HAND_POSES[st.id].a, draw); });
    draw();
  }
  // finger numbers: the app's two hands from above, each finger lighting with its number (frames from the app)
  const FSEQ = [['3:1', 'Thumbs are 1'], ['3:right hand finger 2', 'Right hand, finger 2'], ['3:right hand finger 3', 'Right hand, finger 3'], ['3:right hand finger 4', 'Right hand, finger 4'], ['3:right hand finger 5', 'Right hand, finger 5'],
    ['3:left hand finger 2', 'Left hand, finger 2'], ['3:left hand finger 3', 'Left hand, finger 3'], ['3:left hand finger 4', 'Left hand, finger 4'], ['3:left hand finger 5', 'Left hand, finger 5']];
  function mountFing(el) {
    const st = W.fing = { el, i: 0 };
    el.innerHTML = `<div class="pchips">${[1, 2, 3, 4, 5].map(n => `<button type="button" class="pch" data-v="${n}">${n}</button>`).join('')}</div><div class="pdraw pfing"></div><div class="pck"></div>`;
    const draw = () => { const [k, lab] = FSEQ[st.i]; el.querySelector('.pdraw').innerHTML = (window.PEN_FING || {})[k] || '';
      el.querySelector('.pck').innerHTML = `<div class="ok"><b>${st.i === 0 ? 1 : (st.i - 1) % 4 + 2}</b> ${lab}</div>`; };
    st.draw = draw;
    el.querySelectorAll('.pch').forEach(b => b.onclick = () => { clearInterval(st.cyc); const n = +b.dataset.v, right = !(st.i >= 5 && n > 1); st.i = n === 1 ? 0 : (right ? n - 1 : n + 3); draw(); });
    draw();
  }
  const MOUNT = { sit: mountSit, front: mountFront, hand: mountHand, fing: mountFing };
  function go(kind, target) {
    const st = W[kind]; if (!st) return; clearInterval(st.cyc);
    if (kind === 'sit') {
      const one = (id) => { st.id = id; anim(st, SIT[id], st.draw); };
      if (target === 'cycle') cycle(st, ['low', 'good', 'high', 'good'], one); else if (SIT[target]) one(target);
    } else if (kind === 'hand') {
      const one = (id) => { st.id = id; anim(st, id === 'good' ? GOOD : HAND_POSES[id].a, st.draw); };
      if (target === 'cycle') cycle(st, ['good', 'flat', 'good', 'bridge', 'good', 'low'], one);
      else if (target === 'cycle-ex') cycle(st, ['flat', 'bridge', 'good'], one); else if (HANDS.includes(target)) one(target);
    } else if (kind === 'fing') {
      st.i = 0; st.draw(); st.cyc = setInterval(() => { if (!st.el.isConnected) return clearInterval(st.cyc); st.i = (st.i + 1) % FSEQ.length; st.draw(); }, 1100);
    } else if (kind === 'front') {
      const one = (id) => { st.id = id; anim(st, [FRONT[id]], st.draw); };
      if (target === 'cycle') cycle(st, ['tight', 'good', 'wings', 'good'], one); else if (FRONT[target] != null) one(target);
    }
  }
  window.PEN = { mount: (kind, el) => { Object.values(W).forEach(s => { clearInterval(s.cyc); cancelAnimationFrame(s.raf); }); MOUNT[kind](el); }, go };
})();
