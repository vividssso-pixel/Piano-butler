// Princess Clara: four redesign options (Phase 403), busts in the cast's box (about x -12..12, y -18..15 at k = 1)
function clA(cx, cy, k = 1) {   // A: two braids down to her shoulders with coral bows at the ends, a small tiara, a collar
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
function clB(cx, cy, k = 1) {   // B: a ballerina bun, a tiara band with three gems, a dress with a coral sash
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-10, 14.6)], ['Q', P(-9.4, 8.2), P(0, 8)], ['Q', P(9.4, 8.2), P(10, 14.6)], ['Z']], f: PEN_P, s: PEN_N, w: 1.5 });   // dress
  s.push({ k: 'pa', seg: [['M', P(-9.4, 11.2)], ['Q', P(0, 13.4), P(9.4, 11.2)], ['L', P(9.8, 13.4)], ['Q', P(0, 15.6), P(-9.8, 13.4)], ['Z']], f: PEN_C, nw: true });   // sash
  s.push({ k: 'el', c: P(0, -11.4), rx: 4.4 * k, ry: 3.6 * k, f: PEN_N, s: PEN_N, w: 1.2 });   // bun
  s.push({ k: 'el', c: P(0, -0.4), rx: 6.4 * k, ry: 7.2 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.6, -0.4)], ['Q', P(-7.2, -8.8), P(0, -8.9)], ['Q', P(7.2, -8.8), P(6.6, -0.4)], ['Q', P(5.8, -5.8), P(0, -6.2)], ['Q', P(-5.8, -5.8), P(-6.6, -0.4)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });   // smooth hair
  s.push(penCurve([['M', P(-5.8, -6.4)], ['Q', P(0, -10.6), P(5.8, -6.4)]], 2.4 * k, PEN_C));   // tiara band
  [[-3, -8.2], [0, -9], [3, -8.2]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.9 * k, ry: 0.9 * k, f: PEN_P, s: PEN_N, w: 0.6 }));
  s.push({ k: 'el', c: P(-2.4, 0.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.4, 0.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'el', c: P(-4, 2.6), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' }, { k: 'el', c: P(4, 2.6), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' });
  s.push(penCurve([['M', P(-1.8, 3.4)], ['Q', P(0, 5), P(1.8, 3.4)]], 1.1, PEN_N));
  return s.map(e => ({ ...e, ch: true }));
}
function clC(cx, cy, k = 1) {   // C: a short bob with blunt bangs, a tiara, a coral bow at the neck (like the butler's bow tie)
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-8.6, 5.4)], ['Q', P(-10.4, -9.6), P(0, -9.6)], ['Q', P(10.4, -9.6), P(8.6, 5.4)], ['Q', P(4, 6.6), P(0, 6.2)], ['Q', P(-4, 6.6), P(-8.6, 5.4)], ['Z']], f: PEN_N, s: PEN_N, w: 1.2 });   // bob
  s.push({ k: 'pa', seg: [['M', P(-10, 14.6)], ['Q', P(-9.4, 8.2), P(0, 8)], ['Q', P(9.4, 8.2), P(10, 14.6)], ['Z']], f: '#fbe9e2', s: PEN_N, w: 1.5 });   // dress
  s.push({ k: 'pa', seg: [['M', P(0, 9.4)], ['L', P(-4.6, 7)], ['L', P(-4.6, 11.8)], ['Z'], ['M', P(0, 9.4)], ['L', P(4.6, 7)], ['L', P(4.6, 11.8)], ['Z']], f: PEN_C, s: PEN_N, w: 0.9 });   // bow
  s.push({ k: 'el', c: P(0, 9.4), rx: 1.3 * k, ry: 1.3 * k, f: PEN_C, s: PEN_N, w: 0.8 });
  s.push({ k: 'el', c: P(0, -0.4), rx: 6.2 * k, ry: 7 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.5, -2.4)], ['Q', P(-6.8, -8.4), P(0, -8.6)], ['Q', P(6.8, -8.4), P(6.5, -2.4)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });   // blunt bangs
  s.push({ k: 'pa', seg: [['M', P(-4, -8.2)], ['Q', P(-3.4, -10), P(-1.8, -9.6)], ['L', P(0, -12)], ['L', P(1.8, -9.6)], ['Q', P(3.4, -10), P(4, -8.2)], ['Z']], f: PEN_C, s: PEN_N, w: 1 });   // tiara
  s.push({ k: 'el', c: P(0, -9.8), rx: 0.8 * k, ry: 0.8 * k, f: PEN_P });
  s.push({ k: 'el', c: P(-2.4, 0.6), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.4, 0.6), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'el', c: P(-3.9, 2.8), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' }, { k: 'el', c: P(3.9, 2.8), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' });
  s.push(penCurve([['M', P(-1.8, 3.6)], ['Q', P(0, 5.2), P(1.8, 3.6)]], 1.1, PEN_N));
  return s.map(e => ({ ...e, ch: true }));
}
function clD(cx, cy, k = 1) {   // D: curly hair, a tiara and a flower clip; a dotted dress
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  [[-7.6, 3.2], [-8.2, -1.6], [-6.6, -6.4], [-3, -9], [1.2, -9.6], [5, -8], [7.6, -4], [8.2, 0.8], [7.4, 4.6]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 3.4 * k, ry: 3.4 * k, f: PEN_N, s: PEN_N, w: 1 }));   // curls
  s.push({ k: 'pa', seg: [['M', P(-10, 14.6)], ['Q', P(-9.4, 8.2), P(0, 8)], ['Q', P(9.4, 8.2), P(10, 14.6)], ['Z']], f: PEN_P, s: PEN_N, w: 1.5 });   // dress
  [[-5.6, 12], [-1, 10.6], [3.4, 12.2], [7, 11]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 1 * k, ry: 1 * k, f: PEN_C }));
  s.push({ k: 'el', c: P(0, -0.2), rx: 6.2 * k, ry: 7 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  [[-4.4, -5.6], [-1.6, -6.6], [1.6, -6.6], [4.4, -5.6]].forEach(([a, b]) => s.push(penCurve([['M', P(a - 1.6, b + 0.8)], ['Q', P(a, b - 1.6), P(a + 1.6, b + 0.8)]], 1.3, PEN_N)));   // curls on the forehead
  s.push({ k: 'pa', seg: [['M', P(-4.2, -7.4)], ['L', P(-3.4, -10.4)], ['L', P(-1.6, -8.8)], ['L', P(0, -11.8)], ['L', P(1.6, -8.8)], ['L', P(3.4, -10.4)], ['L', P(4.2, -7.4)], ['Z']], f: PEN_C, s: PEN_N, w: 1 });   // tiara
  s.push({ k: 'el', c: P(-6.6, -4.6), rx: 1.9 * k, ry: 1.9 * k, f: PEN_C, s: PEN_N, w: 0.7 }, { k: 'el', c: P(-6.6, -4.6), rx: 0.7 * k, ry: 0.7 * k, f: PEN_P });   // a flower clip
  s.push({ k: 'el', c: P(-2.4, 0.6), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.4, 0.6), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'el', c: P(-3.9, 2.8), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' }, { k: 'el', c: P(3.9, 2.8), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' });
  s.push(penCurve([['M', P(-1.8, 3.6)], ['Q', P(0, 5.2), P(1.8, 3.6)]], 1.1, PEN_N));
  return s.map(e => ({ ...e, ch: true }));
}
