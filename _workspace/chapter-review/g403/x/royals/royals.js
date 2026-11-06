// The Queen and the King, redrawn (Phase 403): the King no longer hides behind a dark beard; the Queen looks like a queen
const LAV = '#dcd9ea';
function kgA(cx, cy, k = 1) {   // King A: a white beard and moustache, bushy brows, a crown with a cross and jewels, an ermine collar
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-11.5, 15)], ['Q', P(-10.5, 8.4), P(0, 8.6)], ['Q', P(10.5, 8.4), P(11.5, 15)], ['Z']], f: PEN_N, s: PEN_N, w: 1.5 });   // robe
  s.push({ k: 'pa', seg: [['M', P(-10.4, 10.6)], ['Q', P(0, 14.4), P(10.4, 10.6)], ['L', P(11, 13.2)], ['Q', P(0, 17), P(-11, 13.2)], ['Z']], f: PEN_P, s: PEN_N, w: 1 });   // ermine collar
  [[-7, 12.4], [-2.4, 13.9], [2.4, 13.9], [7, 12.4]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.7 * k, ry: 1 * k, f: PEN_N }));
  s.push({ k: 'el', c: P(0, -1), rx: 6.8 * k, ry: 7.4 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.6, 0.6)], ['Q', P(-7.2, 10.6), P(0, 11.8)], ['Q', P(7.2, 10.6), P(6.6, 0.6)], ['Q', P(5.4, 6.4), P(2.4, 6.6)], ['Q', P(0, 8), P(-2.4, 6.6)], ['Q', P(-5.4, 6.4), P(-6.6, 0.6)], ['Z']], f: LAV, s: PEN_N, w: 1.1 });   // white beard, the mouth showing
  s.push({ k: 'pa', seg: [['M', P(0, 3.6)], ['Q', P(-2.8, 2.2), P(-5, 4.2)], ['Q', P(-2.4, 5.6), P(0, 4.6)], ['Q', P(2.4, 5.6), P(5, 4.2)], ['Q', P(2.8, 2.2), P(0, 3.6)], ['Z']], f: LAV, s: PEN_N, w: 0.9 });   // moustache
  s.push(penCurve([['M', P(-1.4, 6.4)], ['Q', P(0, 7.2), P(1.4, 6.4)]], 1, PEN_N));
  s.push(penCurve([['M', P(-4.4, -3.4)], ['Q', P(-2.6, -4.6), P(-1, -3.6)]], 1.6, PEN_N), penCurve([['M', P(1, -3.6)], ['Q', P(2.6, -4.6), P(4.4, -3.4)]], 1.6, PEN_N));   // brows
  s.push({ k: 'el', c: P(-2.6, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.6, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'pa', seg: [['M', P(-7.2, -6.2)], ['L', P(-7.4, -14)], ['L', P(-3.6, -10.6)], ['L', P(0, -15.2)], ['L', P(3.6, -10.6)], ['L', P(7.4, -14)], ['L', P(7.2, -6.2)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });   // crown
  s.push(penLine(P(-7.2, -8.2), P(7.2, -8.2), 1));
  [[-4.4, -7.2], [0, -7.2], [4.4, -7.2]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.9 * k, ry: 0.9 * k, f: PEN_P, s: PEN_N, w: 0.5 }));
  s.push(penLine(P(0, -15.2), P(0, -19.2), 1.4), penLine(P(-1.8, -17.3), P(1.8, -17.3), 1.4));   // the cross on top
  return s.map(e => ({ ...e, ch: true }));
}
function kgB(cx, cy, k = 1) {   // King B: no beard, a big curly moustache, round rosy cheeks, the crown and the ermine collar
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-11.5, 15)], ['Q', P(-10.5, 8.4), P(0, 8.6)], ['Q', P(10.5, 8.4), P(11.5, 15)], ['Z']], f: PEN_N, s: PEN_N, w: 1.5 });
  s.push({ k: 'pa', seg: [['M', P(-10.4, 10.6)], ['Q', P(0, 14.4), P(10.4, 10.6)], ['L', P(11, 13.2)], ['Q', P(0, 17), P(-11, 13.2)], ['Z']], f: PEN_P, s: PEN_N, w: 1 });
  [[-7, 12.4], [-2.4, 13.9], [2.4, 13.9], [7, 12.4]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.7 * k, ry: 1 * k, f: PEN_N }));
  s.push({ k: 'el', c: P(0, -0.4), rx: 7 * k, ry: 7.8 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-7, -2.4)], ['Q', P(-7.6, -8.8), P(0, -9)], ['Q', P(7.6, -8.8), P(7, -2.4)], ['Q', P(4.8, -6), P(0, -5.8)], ['Q', P(-4.8, -6), P(-7, -2.4)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });   // short hair under the crown
  s.push({ k: 'pa', seg: [['M', P(0, 3.4)], ['Q', P(-3.4, 1.8), P(-5.4, 3.6)], ['Q', P(-6.6, 4.8), P(-7.2, 2.6)], ['Q', P(-6.6, 6.6), P(-3.6, 5.6)], ['Q', P(-1.6, 5.2), P(0, 4.6)], ['Q', P(1.6, 5.2), P(3.6, 5.6)], ['Q', P(6.6, 6.6), P(7.2, 2.6)], ['Q', P(6.6, 4.8), P(5.4, 3.6)], ['Q', P(3.4, 1.8), P(0, 3.4)], ['Z']], f: PEN_N, s: PEN_N, w: 0.9 });   // curly moustache
  s.push(penCurve([['M', P(-1.8, 6.6)], ['Q', P(0, 7.8), P(1.8, 6.6)]], 1, PEN_N));
  s.push({ k: 'el', c: P(-4.4, 1.6), rx: 1.3 * k, ry: 0.9 * k, f: '#f6c9bb' }, { k: 'el', c: P(4.4, 1.6), rx: 1.3 * k, ry: 0.9 * k, f: '#f6c9bb' });
  s.push(penCurve([['M', P(-4.4, -3.6)], ['Q', P(-2.6, -4.8), P(-1, -3.8)]], 1.5, PEN_N), penCurve([['M', P(1, -3.8)], ['Q', P(2.6, -4.8), P(4.4, -3.6)]], 1.5, PEN_N));
  s.push({ k: 'el', c: P(-2.6, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.6, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'pa', seg: [['M', P(-7.2, -6.2)], ['L', P(-7.4, -14)], ['L', P(-3.6, -10.6)], ['L', P(0, -15.2)], ['L', P(3.6, -10.6)], ['L', P(7.4, -14)], ['L', P(7.2, -6.2)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });
  s.push(penLine(P(-7.2, -8.2), P(7.2, -8.2), 1));
  [[-4.4, -7.2], [0, -7.2], [4.4, -7.2]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.9 * k, ry: 0.9 * k, f: PEN_P, s: PEN_N, w: 0.5 }));
  s.push(penLine(P(0, -15.2), P(0, -19.2), 1.4), penLine(P(-1.8, -17.3), P(1.8, -17.3), 1.4));
  return s.map(e => ({ ...e, ch: true }));
}
function qnCrown(P, k, s) {   // the Queen's tall crown: five points with pearls, a jewelled band
  s.push({ k: 'pa', seg: [['M', P(-6.6, -7.6)], ['L', P(-8, -16.6)], ['L', P(-4.6, -12.2)], ['L', P(-2.6, -18.4)], ['L', P(0, -13)], ['L', P(2.6, -18.4)], ['L', P(4.6, -12.2)], ['L', P(8, -16.6)], ['L', P(6.6, -7.6)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });
  [[-8, -16.6], [-2.6, -18.4], [2.6, -18.4], [8, -16.6]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 1.1 * k, ry: 1.1 * k, f: PEN_P, s: PEN_N, w: 0.7 }));
  s.push(penLine(P(-6.8, -9.6), P(6.8, -9.6), 1));
  s.push({ k: 'el', c: P(0, -8.5), rx: 1.3 * k, ry: 1 * k, f: PEN_N });   // a dark jewel in the middle
}
function qnFace(P, k, s) {
  s.push({ k: 'el', c: P(-2.5, 0.2), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.5, 0.2), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'pa', seg: [['M', P(-1.7, 3.6)], ['Q', P(0, 5.2), P(1.7, 3.6)], ['Q', P(0, 4.2), P(-1.7, 3.6)], ['Z']], f: PEN_C, s: PEN_C, w: 0.6 });   // coral lips
  s.push({ k: 'el', c: P(-6.7, 3.4), rx: 1 * k, ry: 1.3 * k, f: PEN_P, s: PEN_N, w: 0.7 }, { k: 'el', c: P(6.7, 3.4), rx: 1 * k, ry: 1.3 * k, f: PEN_P, s: PEN_N, w: 0.7 });   // pearl earrings
}
function qnA(cx, cy, k = 1) {   // Queen A: hair up, a high lace collar, pearl earrings, a tall crown, a coral gown with a pearl necklace
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-11.8, 15)], ['Q', P(-11, 8.4), P(0, 8.8)], ['Q', P(11, 8.4), P(11.8, 15)], ['Z']], f: PEN_C, s: PEN_N, w: 1.5 });   // gown
  s.push({ k: 'pa', seg: [['M', P(-5.2, 9.4)], ['Q', P(0, 12.6), P(5.2, 9.4)], ['Q', P(0, 10.2), P(-5.2, 9.4)], ['Z']], f: PEN_P, s: PEN_N, w: 1 });   // a scalloped lace collar at the neckline
  [[-3.6, 10.6], [-1.2, 11.4], [1.2, 11.4], [3.6, 10.6]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.95 * k, ry: 0.95 * k, f: PEN_P, s: PEN_N, w: 0.5 }));   // necklace
  s.push({ k: 'el', c: P(0, -0.4), rx: 6.6 * k, ry: 7.6 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.8, 0.4)], ['Q', P(-8.4, -9.4), P(0, -9.8)], ['Q', P(8.4, -9.4), P(6.8, 0.4)], ['Q', P(6, -5.4), P(1.6, -6.4)], ['Q', P(-1, -4.6), P(-3.6, -5.6)], ['Q', P(-6, -5), P(-6.8, 0.4)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });   // swept-up hair
  qnFace(P, k, s); qnCrown(P, k, s);
  return s.map(e => ({ ...e, ch: true }));
}
function qnB(cx, cy, k = 1) {   // Queen B: long wavy hair, the tall crown, pearl earrings, a royal cape with an ermine trim over the coral gown
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-8.6, -3)], ['Q', P(-12, 2), P(-9.4, 6)], ['Q', P(-11.4, 9), P(-8.4, 12)], ['L', P(8.4, 12)], ['Q', P(11.4, 9), P(9.4, 6)], ['Q', P(12, 2), P(8.6, -3)], ['Z']], f: PEN_N, s: PEN_N, w: 1.2 });   // wavy hair
  s.push({ k: 'pa', seg: [['M', P(-12, 15)], ['Q', P(-11, 8.4), P(0, 8.8)], ['Q', P(11, 8.4), P(12, 15)], ['Z']], f: PEN_N, s: PEN_N, w: 1.5 });   // cape
  s.push({ k: 'pa', seg: [['M', P(-4.4, 9)], ['Q', P(0, 8.4), P(4.4, 9)], ['L', P(5.4, 15)], ['L', P(-5.4, 15)], ['Z']], f: PEN_C, s: PEN_N, w: 1 });   // coral gown in front
  s.push({ k: 'pa', seg: [['M', P(-4.4, 9)], ['L', P(-5.4, 15)], ['L', P(-7.4, 15)], ['L', P(-6.2, 8.8)], ['Z'], ['M', P(4.4, 9)], ['L', P(5.4, 15)], ['L', P(7.4, 15)], ['L', P(6.2, 8.8)], ['Z']], f: PEN_P, s: PEN_N, w: 0.9 });   // ermine trim
  [[-6, 11], [-6.4, 13.6], [6, 11], [6.4, 13.6]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.5 * k, ry: 0.8 * k, f: PEN_N }));
  s.push({ k: 'el', c: P(0, -0.4), rx: 6.6 * k, ry: 7.6 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.8, -1)], ['Q', P(-7.6, -9), P(0, -9.2)], ['Q', P(7.6, -9), P(6.8, -1)], ['Q', P(4.6, -6.2), P(0, -6)], ['Q', P(-4.6, -6.2), P(-6.8, -1)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });
  qnFace(P, k, s); qnCrown(P, k, s);
  return s.map(e => ({ ...e, ch: true }));
}
