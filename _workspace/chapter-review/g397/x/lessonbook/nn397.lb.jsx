// ─── Chapter 3: The Musical Alphabet (chapter 'note-names') -- the Lesson Book, applied (Phase 397) ───
// Sohyun 2026-10-09: the seven letter names are introduced HERE, properly, as A B C D E F G (chapter 2 showed the keyboard
// by its pattern only). Her notes on draft v2: naming at a glance is "who lives there" -- the big house has a Front door (F)
// and a Back door (B), Grandma (G) inside, who loves apples, so her Apple garden (A) is right next to her; the small house's
// D is the Dog in his doghouse between the two black keys, with the Cat (C) and the Elephant (E) either side (her C/E
// words were left to Claude: alphabet-book words, see the Phase 397 row); the word "octave" is used, simply explained;
// no "you will meet skips again on the staff"; no hand picture on the play page; no "before you count to two".
// Her three answers: the alphabet backwards IN YOUR HEAD, without the keyboard pattern, matters -- practise it on its own;
// note names rarely hold children up, skips are the harder part (a whisper for the letter jumped over).
// One page function (nnLbPages): printed it is the A4 Lesson Book, on screen each page after the opener is one step of the
// online lesson (LbLive swaps a still picture for its moving part). Sharps and flats wait for Tones & Semitones
// (chapter 6, whose drill now has the black-key naming level); interval numbers wait for Intervals.

const NN_L7 = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
// letters on a pen keyboard (fsKeysShapes, C start); coral: the letters to colour, grey: the letters to fade
function nnLetters(x, y, nw, W, H, opts = {}) {
  const out = [], off = opts.start === 'A' ? 5 : 0;
  for (let i = 0; i < nw; i++) {
    const n = NN_L7[(i + off) % 7];
    if (opts.only && !opts.only.includes(i)) continue;
    const col = (opts.coralIdx && opts.coralIdx.includes(i)) || (opts.coral && opts.coral.includes(n)) ? PEN_C : (opts.grey && opts.grey.includes(i)) ? '#b9b6d0' : PEN_N;
    out.push({ ...penText(x + (i + 0.5) * W, y + H - H * 0.08, n, { size: opts.size || W * 0.5, weight: 900, fill: col, anchor: 'middle' }) });
  }
  return out;
}
// the letter wheel: a Ferris wheel with seven gondolas, A at the top, turning clockwise = forwards
function nnWheel(cx, cy, R, opts = {}) {
  const s = [], g = opts.g || R * 0.24;
  const at = (i, r = R) => { const a = -Math.PI / 2 + i * 2 * Math.PI / 7; return [cx + r * Math.cos(a), cy + r * Math.sin(a)]; };
  if (opts.legs !== false) {
    const fy = opts.groundY || cy + R + g + 12;
    s.push({ k: 'pl', p: [[cx - R * 0.62, fy], [cx, cy], [cx + R * 0.62, fy]], s: PEN_N, w: 2.4 });
    s.push(penLine([cx - R * 0.42, cy + R * 0.66], [cx + R * 0.42, cy + R * 0.66], 1.6));
    if (!opts.groundY) s.push(penLine([cx - R * 0.9, fy], [cx + R * 0.9, fy], 1.6, '#bdb7a6'));
  }
  s.push({ k: 'el', c: [cx, cy], rx: R, ry: R, f: 'none', s: PEN_N, w: 2.2 });
  for (let i = 0; i < 7; i++) s.push(penLine([cx, cy], at(i), 1.2));
  s.push({ k: 'el', c: [cx, cy], rx: 3.4, ry: 3.4, f: PEN_C });
  const L = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
  L.forEach((n, i) => {
    const [x, y] = at(i), on = opts.coral && opts.coral.includes(n), fill = opts.fill && opts.fill.includes(n);
    s.push({ k: 'rc', x: x - g, y: y - g * 0.55, w: g * 2, h: g * 1.9, rx: g * 0.5, f: fill ? PEN_C : PEN_P, s: on || fill ? PEN_C : PEN_N, sw: 1.8 });
    s.push({ ...penText(x, y + g * 0.85, n, { size: g * 1.25, weight: 900, fill: fill ? '#fffdf7' : on ? PEN_C : PEN_N, anchor: 'middle' }) });
  });
  if (opts.arrow) {   // a curved arrow outside the rim: clockwise (forwards) or anticlockwise (backwards)
    const r = R + g + 7, cw = opts.arrow === 'cw', a0 = cw ? -1.25 : -1.9, a1 = cw ? -0.55 : -2.6;
    const p = (a) => [cx + r * Math.cos(a), cy + r * Math.sin(a)];
    const seg = [['M', p(a0)]]; for (let i = 1; i <= 8; i++) seg.push(['L', p(a0 + (a1 - a0) * i / 8)]);
    s.push({ k: 'pa', seg, f: 'none', s: opts.arrowCol || PEN_C, w: 2 });
    const e = p(a1), d = cw ? 1 : -1, tg = [-Math.sin(a1) * d, Math.cos(a1) * d], nn = [Math.cos(a1), Math.sin(a1)];
    s.push({ k: 'pa', seg: [['M', [e[0] + tg[0] * 6, e[1] + tg[1] * 6]], ['L', [e[0] + nn[0] * 4, e[1] + nn[1] * 4]], ['L', [e[0] - nn[0] * 4, e[1] - nn[1] * 4]], ['Z']], f: opts.arrowCol || PEN_C });
  }
  return s;
}
// a straight arrow (the up/forwards and down/backwards lines)
function nnArrow(x1, x2, y, col, w = 2.2) {
  const d = x2 > x1 ? 1 : -1;
  return [{ k: 'pa', seg: [['M', [x1, y]], ['L', [x2 - d * 4, y]]], f: 'none', s: col, w, nw: true },
    { k: 'pa', seg: [['M', [x2 - d * 8, y - 4.5]], ['L', [x2, y]], ['L', [x2 - d * 8, y + 4.5]], ['Z']], f: col }];
}
// a hop arc over the keys (a skip), with an arrowhead
function nnHop(x1, x2, y, h, col = PEN_C, w = 1.8) {
  const mx = (x1 + x2) / 2, d = x2 > x1 ? 1 : -1;
  return [penCurve([['M', [x1, y]], ['Q', [mx, y - h * 2], [x2, y]]], w, col),
    { k: 'pa', seg: [['M', [x2 - d * 6.5, y - 4.5]], ['L', [x2, y + 0.5]], ['L', [x2 - d * 1, y - 7.5]], ['Z']], f: col }];
}
// a little door, drawn on a white key (the big house's Front door and Back door)
function nnDoor(cx, y, w = 12, h = 18, col = PEN_C) {
  return [{ k: 'pa', seg: [['M', [cx - w / 2, y + h]], ['L', [cx - w / 2, y + w / 2]], ['Q', [cx - w / 2, y], [cx, y]], ['Q', [cx + w / 2, y], [cx + w / 2, y + w / 2]], ['L', [cx + w / 2, y + h]], ['Z']], f: '#fffdf7', s: col, w: 1.7, nw: true },
    { k: 'el', c: [cx + w * 0.22, y + h * 0.6], rx: 1.3, ry: 1.3, f: col }];
}

// ─── who lives at each white key (Sohyun 2026-10-09): naming at a glance ───
// the words start with their key's letter; English in both languages (the Korean words are only a gloss)
const NN_RES = { C: ['Cat', '고양이'], D: ['Dog', '강아지'], E: ['Elephant', '코끼리'], F: ['Front door', '앞문'], G: ['Grandma', '할머니'], A: ['Apple garden', '사과 정원'], B: ['Back door', '뒷문'] };
const nnCh = (list) => list.map(e => ({ ...e, ch: true }));
function nnCat(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-8.4, -3)], ['L', P(-9.2, -13)], ['L', P(-2.6, -7.6)], ['Z']], f: PEN_P, s: PEN_N, w: 1.6 });
  s.push({ k: 'pa', seg: [['M', P(8.4, -3)], ['L', P(9.2, -13)], ['L', P(2.6, -7.6)], ['Z']], f: PEN_P, s: PEN_N, w: 1.6 });
  s.push({ k: 'el', c: P(0, 0), rx: 9.2 * k, ry: 7.6 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'el', c: P(-3.3, -1.2), rx: 1 * k, ry: 1.4 * k, f: PEN_N }, { k: 'el', c: P(3.3, -1.2), rx: 1 * k, ry: 1.4 * k, f: PEN_N });
  s.push({ k: 'pa', seg: [['M', P(-1.4, 1.4)], ['L', P(1.4, 1.4)], ['L', P(0, 2.9)], ['Z']], f: PEN_C });
  s.push(penCurve([['M', P(0, 2.9)], ['Q', P(-1.2, 4.8), P(-2.8, 4)], ['M', P(0, 2.9)], ['Q', P(1.2, 4.8), P(2.8, 4)]], 1.1, PEN_N));
  [[-4, 2.2, -12.5, 1], [-4, 3.4, -12.5, 4.6], [4, 2.2, 12.5, 1], [4, 3.4, 12.5, 4.6]].forEach(([a, b, c, d]) => s.push(penLine(P(a, b), P(c, d), 0.9)));
  return nnCh(s);
}
function nnDog(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [], d = [];
  // the doghouse (a prop: straight lines), its coral roof and dark doorway
  s.push({ k: 'pa', seg: [['M', P(-12, 12)], ['L', P(-12, -2)], ['L', P(0, -12.5)], ['L', P(12, -2)], ['L', P(12, 12)], ['Z']], f: PEN_P, s: PEN_N, w: 1.6, nw: true });
  s.push({ k: 'pl', p: [P(-14, -0.4), P(0, -13.8), P(14, -0.4)], s: PEN_C, w: 2.2, nw: true });
  s.push({ k: 'pa', seg: [['M', P(-7.5, 12)], ['L', P(-7.5, 3)], ['Q', P(-7.5, -3.5), P(0, -3.5)], ['Q', P(7.5, -3.5), P(7.5, 3)], ['L', P(7.5, 12)], ['Z']], f: PEN_N, nw: true });
  // the dog, looking out
  d.push({ k: 'pa', seg: [['M', P(-4.2, 1)], ['Q', P(-9.4, 1.4), P(-8.2, 8.4)], ['Q', P(-6, 9.6), P(-4.4, 5.6)], ['Z']], f: PEN_P, s: PEN_N, w: 1.3 });
  d.push({ k: 'pa', seg: [['M', P(4.2, 1)], ['Q', P(9.4, 1.4), P(8.2, 8.4)], ['Q', P(6, 9.6), P(4.4, 5.6)], ['Z']], f: PEN_P, s: PEN_N, w: 1.3 });
  d.push({ k: 'el', c: P(0, 4.6), rx: 5.4 * k, ry: 5 * k, f: PEN_P, s: PEN_N, w: 1.6 });
  d.push({ k: 'el', c: P(-2, 3.4), rx: 0.85 * k, ry: 0.85 * k, f: PEN_N }, { k: 'el', c: P(2, 3.4), rx: 0.85 * k, ry: 0.85 * k, f: PEN_N });
  d.push({ k: 'el', c: P(0, 6), rx: 1.5 * k, ry: 1.1 * k, f: PEN_N });
  d.push(penCurve([['M', P(-1.6, 7.6)], ['Q', P(0, 8.8), P(1.6, 7.6)]], 0.9, PEN_N));
  return [...s, ...nnCh(d)];
}
function nnElephant(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'el', c: P(-8.6, -1), rx: 6.2 * k, ry: 7.6 * k, f: PEN_P, s: PEN_N, w: 1.7 }, { k: 'el', c: P(8.6, -1), rx: 6.2 * k, ry: 7.6 * k, f: PEN_P, s: PEN_N, w: 1.7 });
  s.push(penCurve([['M', P(-7, -5.4)], ['Q', P(-12.4, -2), P(-7.8, 4)]], 1, PEN_N), penCurve([['M', P(7, -5.4)], ['Q', P(12.4, -2), P(7.8, 4)]], 1, PEN_N));
  s.push({ k: 'pa', seg: [['M', P(-2.5, 0)], ['C', P(-2.8, 8), P(-1.6, 12.6), P(2.6, 13.2)], ['L', P(3.8, 11.2)], ['C', P(1.2, 10.8), P(2.4, 7), P(2.5, 0)], ['Z']], f: PEN_P, s: PEN_N, w: 1.5 });   // the trunk, under the head
  s.push({ k: 'el', c: P(0, -2), rx: 6.4 * k, ry: 6.8 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'el', c: P(-2.7, -3.2), rx: 0.95 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.7, -3.2), rx: 0.95 * k, ry: 0.95 * k, f: PEN_N });
  return nnCh(s);
}
function nnGrandma(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [], HAIR = '#dcd9ea';
  s.push({ k: 'pa', seg: [['M', P(-10, 13)], ['Q', P(-9, 6.4), P(0, 6.8)], ['Q', P(9, 6.4), P(10, 13)], ['Z']], f: PEN_C, s: PEN_N, w: 1.5 });   // her shawl
  s.push({ k: 'el', c: P(0, -10.6), rx: 3.6 * k, ry: 3 * k, f: HAIR, s: PEN_N, w: 1.4 });                                                         // the bun
  s.push({ k: 'el', c: P(0, -1), rx: 7.4 * k, ry: 8.2 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-7.4, -1.5)], ['Q', P(-7.8, -9.4), P(0, -9.4)], ['Q', P(7.8, -9.4), P(7.4, -1.5)], ['Q', P(4.5, -6), P(0, -5.6)], ['Q', P(-4.5, -6), P(-7.4, -1.5)], ['Z']], f: HAIR, s: PEN_N, w: 1.3 });
  s.push({ k: 'el', c: P(-3, 0), rx: 2.3 * k, ry: 2.3 * k, f: 'none', s: PEN_N, w: 1.1 }, { k: 'el', c: P(3, 0), rx: 2.3 * k, ry: 2.3 * k, f: 'none', s: PEN_N, w: 1.1 });   // glasses
  s.push(penLine(P(-0.7, -0.2), P(0.7, -0.2), 1));
  s.push({ k: 'el', c: P(-3, 0.2), rx: 0.7 * k, ry: 0.7 * k, f: PEN_N }, { k: 'el', c: P(3, 0.2), rx: 0.7 * k, ry: 0.7 * k, f: PEN_N });
  s.push(penCurve([['M', P(-2.4, 4)], ['Q', P(0, 5.8), P(2.4, 4)]], 1.1, PEN_N));
  return nnCh(s);
}
function nnAppleTree(cx, cy, k = 1) {   // a prop: straight lines
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'rc', x: cx - 1.8 * k, y: cy + 1 * k, w: 3.6 * k, h: 12 * k, rx: 0.6, f: PEN_N, nw: true });
  s.push({ k: 'pa', seg: [['M', P(-8, 3)], ['Q', P(-12.5, 1), P(-10, -4)], ['Q', P(-11, -10.5), P(-4, -10.5)], ['Q', P(0, -14.5), P(4.5, -10.5)], ['Q', P(11.5, -10), P(10, -3.5)], ['Q', P(12.5, 1.5), P(7.5, 3.5)], ['Q', P(0, 6), P(-8, 3)], ['Z']], f: PEN_P, s: PEN_N, w: 1.6, nw: true });
  [[-5, -5.5], [2.5, -7.5], [-1, -1], [5.6, -1.6], [-6.4, 0.4]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 1.8 * k, ry: 1.8 * k, f: PEN_C, nw: true }));
  s.push({ ...penLine(P(-11, 13), P(11, 13), 1.2, '#bdb7a6'), nw: true });
  return s;
}
function nnResident(L, cx, cy, k = 1) {
  if (L === 'C') return nnCat(cx, cy + 1 * k, k);
  if (L === 'D') return nnDog(cx, cy, k);
  if (L === 'E') return nnElephant(cx, cy - 1 * k, k);
  if (L === 'G') return nnGrandma(cx, cy, k * 0.95);
  if (L === 'A') return nnAppleTree(cx, cy, k);
  return nnDoor(cx, cy - 11.5 * k, 15 * k, 23 * k, L === 'F' ? PEN_C : PEN_N);
}
const nnResIcon = (L, w = 44) => <div style={{width:w,flex:'0 0 auto'}}><PenArt shapes={nnResident(L, 22, 22, 1.05)} vb={[0, 0, 44, 44]} label={NN_RES[L][0]}/></div>;

function nnLbPages(scr = false) {
  const ch = 'note-names';

  // p1: the letter wheel beside the keyboard street; the brother points at the wheel
  const art1 = (() => {
    const s = [penLine([4, 138], [336, 138], 1.6, '#bdb7a6')];
    s.push(...nnWheel(104, 62, 42, { arrow: 'cw', coral: ['C', 'F'], legs: true, groundY: 138 }));
    const K = fsKeysShapes(178, 70, 10, 15.6, 68, { tints: true });
    s.push(...K.shapes, ...nnLetters(178, 70, 10, 15.6, 68, { size: 8.5, coral: ['C', 'F'] }));
    K.houses.forEach(h => s.push(...fsRoof(h, 68, h.kind === 'big' ? 18 : 13, { w: 2.2 })));
    s.push(...penPlace(fsKid('boy', 'point', 1), 0.58, [75, 156], [24, 138]));
    return s;
  })();
  // p2: A to G on the keys -- the alphabet written along the white keys from the bottom A, the houses above
  const art0 = (() => {
    const s = [];
    const X = 22, Y = 62, W = 33, H = 88, N = 9;
    const K = fsKeysShapes(X, Y, N, W, H, { start: 'A', sw: 2.4, tints: true });
    s.push(...K.shapes, ...nnLetters(X, Y, N, W, H, { start: 'A', size: 15, coralIdx: [0, 7] }));
    K.houses.forEach(h => { if (h.kind !== 'lone') s.push(...fsRoof(h, Y - 1, h.kind === 'big' ? 18 : 13, { w: 2.2 })); });
    'ABCDEFG'.split('').forEach((l, i) => {
      const cx = X + (i + 0.5) * W;
      s.push({ k: 'rc', x: cx - 12, y: 6, w: 24, h: 24, rx: 5, f: i === 0 ? PEN_C : PEN_P, s: i === 0 ? PEN_C : PEN_N, sw: 1.8, nw: true });
      s.push({ ...penText(cx, 23.5, l, { size: 15, weight: 900, fill: i === 0 ? '#fffdf7' : PEN_N, anchor: 'middle' }) });
      s.push({ ...penLine([cx, 32], [cx, 40], 1.2, '#b9b6d0', '2 3'), nw: true });
    });
    s.push(...nnArrow(X + 6.5 * W + 16, X + 7.5 * W - 8, 18, PEN_C));
    s.push({ ...penText(X + 7.5 * W - 4, 22, t('A again', '다시 A'), { size: 10.5, weight: 900, fill: PEN_C, anchor: 'start' }), halo: true });
    s.push({ ...penText(X + 4 * W, Y + H + 16, t('C D E: the small house  ·  F G A B: the big house', 'C D E: 작은 집  ·  F G A B: 큰 집'), { size: 10, weight: 800, fill: PEN_N, anchor: 'middle' }), halo: true });
    return s;
  })();
  // p3: the wheel (seven letters, round and round) and one octave, C to C = 8
  const art2 = (() => {
    const s = [];
    s.push(...nnWheel(64, 68, 46, { arrow: 'cw', fill: ['C'], legs: true }));
    const X = 138, Y = 34, W = 24.5, H = 92;
    const K = fsKeysShapes(X, Y, 8, W, H, { sw: 2.4, tints: true });
    s.push(...K.shapes, ...nnLetters(X, Y, 8, W, H, { size: 13, coralIdx: [0, 7] }));
    s.push(...fsBrace(X + 3, X + 8 * W - 3, Y + H + 6, 8, true));
    s.push({ ...penText(X + 4 * W, Y + H + 40, t('C to the next C: one octave', 'C에서 다음 C까지: 한 옥타브'), { size: 10, weight: 900, fill: PEN_C, anchor: 'middle' }), halo: true });
    s.push({ ...penText(X + 4 * W, Y - 10, t('C D E F G A B -- and C again', 'C D E F G A B -- 그리고 다시 C'), { size: 10, weight: 900, fill: PEN_N, anchor: 'middle' }), halo: true });
    return s;
  })();
  // p4: up = right = forwards (to the bird in the sky); down = left = backwards (to the turtle under the sea)
  const art3 = (() => {
    const s = [];
    const X = 34, Y = 44, W = 18.2, H = 66, N = 15;
    const K = fsKeysShapes(X, Y, N, W, H, { sw: 2.2, tints: true });
    s.push(...K.shapes, ...nnLetters(X, Y, N, W, H, { size: 10, coralIdx: [0, 7, 14] }));
    s.push(...nnArrow(X + 4, X + N * W - 4, 26, PEN_C));
    s.push({ ...penText(X + 4, 18, t('up: forwards  C D E F G A B C', '위로: 앞으로  C D E F G A B C'), { size: 9.5, weight: 900, fill: PEN_C }), halo: true });
    s.push(...nnArrow(X + N * W - 4, X + 4, Y + H + 18, PEN_N));
    s.push({ ...penText(X + N * W - 4, Y + H + 34, t('down: backwards  C B A G F E D C', '아래로: 거꾸로  C B A G F E D C'), { size: 9.5, weight: 900, fill: PEN_N, anchor: 'end' }), halo: true });
    s.push(...fsCloud(X + N * W + 19, 12, 0.78), ...fsBird(X + N * W + 16, 34, 1));
    s.push(...fsTurtle(17, Y + H + 25, 0.72), ...fsWaves(0, Y + H + 37, 34, 1, 2));
    return s;
  })();
  // p5: who lives there -- Cat, Dog (in his doghouse), Elephant; Front door, Grandma, Apple garden, Back door
  const art4 = (() => {
    const s = [];
    const X = 10, Y = 38, W = 40, H = 138;
    const K = fsKeysShapes(X, Y, 7, W, H, { sw: 2.6, tints: true });
    s.push(...K.shapes, ...nnLetters(X, Y, 7, W, H, { size: 15 }));
    const [sm, bg] = K.houses;
    s.push(...fsRoof(sm, 36, 18, { label: t('small house', '작은 집'), labelSize: 10.5 }));
    s.push(...fsRoof(bg, 36, 23, { label: t('big house', '큰 집'), labelSize: 10.5 }));
    const cy = Y + H * 0.6 + 17;
    NN_L7.forEach((L, i) => {
      const cx = X + (i + 0.5) * W;
      s.push(...nnResident(L, cx, cy, 1));
      NN_RES[L][0].split(' ').forEach((wd, j) => s.push({ ...penText(cx, Y + H + 13 + j * 9.5, wd, { size: 8.5, weight: 900, fill: PEN_N, anchor: 'middle' }) }));
    });
    return s;
  })();
  // p6: skip a letter -- hops over the keys, and the star it draws on the wheel
  const art5 = (() => {
    const s = [];
    const cx = 66, cy = 74, R = 50, L = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
    const at = (i) => { const a = -Math.PI / 2 + i * 2 * Math.PI / 7; return [cx + R * Math.cos(a), cy + R * Math.sin(a)]; };
    s.push({ k: 'el', c: [cx, cy], rx: R, ry: R, f: 'none', s: '#cfcbe0', w: 1.4 });
    const order = [2, 4, 6, 1, 3, 5, 0, 2];    // C E G B D F A C
    s.push({ k: 'pl', p: order.map(at), s: PEN_C, w: 1.9 });
    L.forEach((n, i) => { const [x, y] = at(i); s.push({ k: 'el', c: [x, y], rx: 10.5, ry: 10.5, f: n === 'C' ? PEN_C : PEN_P, s: n === 'C' ? PEN_C : PEN_N, w: 1.8 });
      s.push({ ...penText(x, y + 4.6, n, { size: 13, weight: 900, fill: n === 'C' ? '#fffdf7' : PEN_N, anchor: 'middle' }) }); });
    const X = 140, Y = 64, W = 21, H = 76, N = 9;
    const K = fsKeysShapes(X, Y, N, W, H, { sw: 2.2, tints: true });
    s.push(...K.shapes, ...nnLetters(X, Y, N, W, H, { size: 11.5, coralIdx: [0, 2, 4, 6, 8], grey: [1, 3, 5, 7] }));
    [0, 2, 4, 6].forEach(i => s.push(...nnHop(X + (i + 0.5) * W, X + (i + 2.5) * W, Y - 3, 10)));
    s.push({ ...penText(X + 4.5 * W, Y - 36, t('C (d) E (f) G (a) B (c) D', 'C (d) E (f) G (a) B (c) D'), { size: 10.5, weight: 900, fill: PEN_C, anchor: 'middle' }), halo: true });
    s.push({ ...penText(X + 4.5 * W, Y + H + 18, t('a skip jumps over one white key', '건너뛰기: 흰건반 하나를 넘어가요'), { size: 9.5, weight: 800, fill: PEN_N, anchor: 'middle' }), halo: true });
    return s;
  })();
  // p7: right hand 2 3 4 on C D E (the small house's white keys)
  const art6 = (() => {
    const s = [];
    const X = 10, Y = 26, W = 34, H = 92;
    const K = fsKeysShapes(X, Y, 7, W, H, { sw: 2.4, tints: true });
    s.push(...K.shapes, ...nnLetters(X, Y, 7, W, H, { size: 13, coral: ['C', 'D', 'E'], only: [0, 1, 2] }));
    s.push(...fsRoof(K.houses[0], 24, 16));
    [0, 1, 2].forEach((wi, i) => {
      const cx = X + (wi + 0.5) * W;
      s.push({ k: 'el', c: [cx, Y + H * 0.62 + 6], rx: 9, ry: 9, f: PEN_C });
      s.push({ ...penText(cx, Y + H * 0.62 + 10, String(i + 2), { size: 11.5, weight: 900, fill: '#fffdf7', anchor: 'middle' }) });
    });
    return s;
  })();
  // p8 icons
  const chkArts = {
    atog: 'ABCDEFG'.split('').map((n, i) => ({ ...penText(8 + i * 12.6, 26, n, { size: 11, weight: 900, fill: n === 'C' || n === 'F' ? PEN_C : PEN_N, anchor: 'middle' }) })),
    wheel: [{ ...penText(46, 17, 'C D E →', { size: 13.5, weight: 900, fill: PEN_C, anchor: 'middle' }) }, { ...penText(46, 36, '← C B A', { size: 13.5, weight: 900, fill: PEN_N, anchor: 'middle' }) }],
    glance: [...nnDog(30, 21, 1.1), { ...penText(62, 29, 'D', { size: 17, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    skip: [...['C', 'E', 'G'].map((n, i) => ({ ...penText(14 + i * 32, 36, n, { size: 14, weight: 900, fill: PEN_C, anchor: 'middle' }) })), ...nnHop(17, 43, 21, 7), ...nnHop(49, 75, 21, 7)],
    song: ['E', 'D', 'C'].map((n, i) => [{ k: 'el', c: [18 + i * 26, 20], rx: 10, ry: 10, f: PEN_P, s: PEN_N, w: 2 }, { ...penText(18 + i * 26, 24.4, n, { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' }) }]).flat(),
  };
  const checksRows = [
    ['atog', [0, 0, 92, 40], t('I can find A to G on the keys (C and F at the left doors)', '건반에서 A부터 G까지 찾을 수 있어요 (C와 F는 왼쪽 문)')],
    ['wheel', [0, 0, 92, 40], t('I can say the letters forwards and backwards, from any letter', '어떤 글자에서든 앞으로, 거꾸로 글자를 말할 수 있어요')],
    ['glance', [0, 0, 92, 40], t('I can name any white key at a glance: who lives there?', '어떤 흰건반이든 보자마자 이름을 댈 수 있어요: 누가 살지?')],
    ['skip', [0, 0, 92, 40], t('I can skip up and down: C E G B D F A', '건너뛰며 오르내릴 수 있어요: C E G B D F A')],
    ['song', [0, 0, 92, 40], t('I can play Hot Cross Buns from its letters, legato', '핫 크로스 번을 글자를 보고 레가토로 칠 수 있어요')],
  ];
  const hcbL = ['E', 'D', 'C', '-', '|', 'E', 'D', 'C', '-', '|', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', '|', 'E', 'D', 'C', '-'];

  return [
    // 1. opener (also the Workbook's map)
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Chapter 2 gave the keyboard its pattern; this chapter gives every white key its name, A to G, and then makes the names fast. The test is speed without counting: a student who still walks from C to find every key needs more of pages 4 and 5, not more letters. ', '2챕터는 건반에 패턴을 줬고, 이 챕터는 흰건반마다 A부터 G까지 이름을 주고, 그 이름을 빠르게 만들어요. 기준은 세지 않고 나오는 속도예요: 아직 건반마다 C부터 걸어가는 학생에게는 글자를 더 주기보다 4, 5쪽을 더 해 주세요. ')}{t('Black keys keep no names yet: sharps and flats arrive with Tones & Semitones.', '검은건반은 아직 이름이 없어요: 샤프와 플랫은 온음과 반음 챕터에서 만나요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('The Musical Alphabet', '음악 알파벳')}</div>
      </div></LbOnly>
      <LbPic h={200}><div style={{width:'100%'}}><PenArt shapes={art1} vb={[0, 6, 340, 136]} label={t('The letter wheel, a Ferris wheel with seven gondolas A to G, beside a street of keys; the brother points at the wheel', 'A부터 G까지 일곱 칸이 달린 글자 관람차와 건반 거리; 남동생이 관람차를 가리켜요')}/></div></LbPic>
      <LbSay size={17.5}>{t('Every white key has a name: a letter from A to G, the first seven letters of the alphabet. In Chapter 2 you learned the houses; now each house gets its names -- and then the names come fast: forwards and backwards, a skip at a time, all over the piano, until any key tells you its name at a glance.', '흰건반에는 모두 이름이 있어요: 알파벳 처음 일곱 글자, A부터 G까지. 2챕터에서 집을 배웠으니, 이제 집마다 이름이 생겨요 -- 그리고 이름이 빨리 나오게 해요: 앞으로도 거꾸로도, 하나씩 건너뛰면서, 피아노 어디에서든, 어떤 건반이든 보자마자 이름이 나올 때까지.')}</LbSay>
      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>
          {[[t('A to G on the keys', '건반 위의 A부터 G'), 2], [t('The letter wheel', '글자 관람차'), 3], [t('Forwards up, backwards down', '위로는 앞으로, 아래로는 거꾸로'), 4], [t('Name it at a glance', '보자마자 이름 대기'), 5], [t('Skip a letter', '한 글자 건너뛰기'), 6], [t('Play by letter names', '음이름 보고 연주하기'), 7], [t('My five checks', '나의 다섯 가지 확인'), 8]].map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid #ece6d8'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><b>{'page ' + p}</b></div>)}
        </div></LbOnly>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('find A to G on the keys', '건반에서 A부터 G까지 찾을 수 있어요'), t('say the letters forwards and backwards, from any letter', '어떤 글자에서든 앞으로, 거꾸로 글자를 말할 수 있어요'), t('name any white key at a glance', '어떤 흰건반이든 보자마자 이름을 댈 수 있어요'), t('find the same letter in every octave', '모든 옥타브에서 같은 글자를 찾을 수 있어요'), t('skip up and down the keys: C E G B D F A', '건너뛰며 건반을 오르내릴 수 있어요: C E G B D F A'), t('play Hot Cross Buns from its letter names', '음이름을 보고 핫 크로스 번을 칠 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:8,fontSize:14.5,padding:'4px 0'}}><span style={{color:BK.coral,fontWeight:900}}>✓</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. A to G on the keys
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('A to G on the keys', '건반 위의 A부터 G')}
      teacher={<>{t('The names arrive in alphabet order, A to G, laid along the white keys from the bottom A of the piano; the houses from Chapter 2 tell where each one lives. The most common stumble is crossing into F G A at the three-black-key roof: anchor C and F at their left doors and walk from there. Watch for an "H".', '이름은 알파벳 순서대로, A부터 G까지, 피아노 맨 아래 A부터 흰건반 위에 놓여요; 2챕터의 집이 각 글자가 사는 곳을 알려 줘요. 가장 흔한 실수는 검은건반 세 개짜리 지붕에서 F G A로 넘어가는 곳이에요: C와 F를 왼쪽 문에 닻으로 내리고 거기서 걸어가요. "H"가 나오는지 봐 주세요.')}</>}>
      <LbLive still={<LbPic h={230}><div style={{width:'100%',maxWidth:600,margin:'0 auto'}}><PenArt shapes={art0} vb={[0, 0, 340, 172]} label={t('The alphabet A to G written along the white keys from the bottom A; then A again; C D E under the small house, F G A B under the big house', '맨 아래 A부터 흰건반을 따라 쓴 알파벳 A부터 G, 그리고 다시 A; 작은 집 아래 C D E, 큰 집 아래 F G A B')}/></div></LbPic>} live={<><KeyHouses/><WhichLetter/></>}/>
      <LbSay>{LANG === 'ko' ? <>음악은 알파벳 <b>처음 일곱 글자</b>만 써요: <b>A B C D E F G</b>. 피아노 맨 아래 건반이 바로 <b>A</b>예요 -- 거기서부터 흰건반을 하나씩 올라가며 알파벳 순서대로: A B C D E F G, 그리고 <b>다시 A</b>. 집이 자리를 알려 줘요: <b>C D E</b>는 작은 집에, <b>F G A B</b>는 큰 집에 살아요. <b>C</b>와 <b>F</b>는 각 집의 왼쪽 문이에요. (도레미로는 C가 도, D가 레, E가 미...)</>
        : <>Music uses just the <b>first seven letters</b> of the alphabet: <b>A B C D E F G</b>. The very lowest key on the piano is an <b>A</b> -- from there, the white keys go up in alphabet order: A B C D E F G, and then <b>A again</b>. The houses tell you where each one lives: <b>C D E</b> in the small house, <b>F G A B</b> in the big one, with <b>C</b> and <b>F</b> at the left doors. (In Do Re Mi, C is Do, D is Re, E is Mi...)</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>피아노 <b>맨 아래 건반</b>을 찾아요: A예요. 흰건반을 올라가며 말해요: A B C D E F G, 그리고 다시 A.</>,
        <>모든 <b>C</b>(작은 집의 왼쪽 문)와 모든 <b>F</b>(큰 집의 왼쪽 문)를 찾아 쳐요.</>,
        <>누가 글자를 하나 말하면, 집을 보고 그 건반을 찾아요 -- 세 군데에서 쳐 봐요.</>,
      ] : [
        <>Find the <b>lowest key</b> on the piano: it is A. Walk up the white keys saying A B C D E F G -- and A again.</>,
        <>Find and play every <b>C</b> (the small house's left door) and every <b>F</b> (the big house's left door).</>,
        <>Someone says a letter; use the houses to find it -- then play it in three different places.</>,
      ]}/>
      <LbRemember>{t('A B C D E F G: C D E in the small house, F G A B in the big.', 'A B C D E F G: C D E는 작은 집에, F G A B는 큰 집에.')}</LbRemember>
    </LbPage>,

    // 3. the letter wheel (and the word "octave")
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The letter wheel', '글자 관람차')}
      teacher={<>{t('Start the chain from any letter, not only from A or C: students who only know it from A count up from A every time. Watch for "H". ', '체인은 A나 C에서만이 아니라 아무 글자에서나 시작해요: A부터만 아는 학생은 매번 A부터 세요. "H"가 나오는지 봐 주세요. ')}{t('The word "octave" is used plainly here -- the same letter, 8 white keys on; intervals by number come in their own chapter.', '"옥타브"라는 말은 여기서 쉽게만 써요 -- 같은 글자, 흰건반 8개 위; 숫자로 부르는 음정은 음정 챕터에서 만나요.')}</>}>
      <LbLive still={<LbPic h={240}><div style={{width:'100%',maxWidth:600,margin:'0 auto'}}><PenArt shapes={art2} vb={[0, 10, 340, 172]} label={t('The letter wheel with C filled in, and one octave of keys from C to the next C, 8 white keys', 'C가 칠해진 글자 관람차, 그리고 C에서 다음 C까지 흰건반 8개의 한 옥타브')}/></div></LbPic>} live={<NameReveal/>}/>
      <LbSay>{LANG === 'ko' ? <>음악에는 <b>글자 일곱 개</b>만 있어요: A B C D E F G. G 다음엔 관람차가 돌아 다시 <b>A</b>가 와요 -- 요일처럼 돌고 돌아요, H는 없어요. 한 바퀴 돌 때마다 같은 글자가 다시 와요. C에서 다음 C까지를 <b>옥타브</b>라고 해요 -- '옥트(oct)'는 8이라는 뜻, 문어(octopus)의 다리 여덟 개처럼요: 두 C를 모두 세면 흰건반 8개. 이름은 같고, 목소리만 더 높아요.</>
        : <>Music uses only <b>seven letters</b>: A B C D E F G. After G, the wheel comes round to <b>A</b> again -- round and round like the days of the week; there is no H. Each time round, the same letter comes back. From one C up to the next C is called an <b>octave</b> -- <i>oct</i> means eight, like the eight legs of an octopus: 8 white keys, counting both Cs. Same name, higher voice.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>맨 아래 <b>A</b>부터 맨 위까지 흰건반을 모두 치며 글자를 말해요: A B C D E F G, A B C...</>,
        <><b>가운데 도</b>에서 흰건반 8개를 걸어 올라가 다음 C까지 가요 -- 한 옥타브, 관람차가 한 바퀴 돌았어요.</>,
        <>누가 아무 글자나 말하면 관람차를 이어 돌려요: "E" -- "F G A B C..."</>,
      ] : [
        <>Start on the lowest <b>A</b> and play every white key to the top, saying the letters: A B C D E F G, A B C...</>,
        <>Play <b>middle C</b>, then walk up 8 white keys to the next C, saying the letters -- one octave: the wheel has gone round once.</>,
        <>Someone says any letter; you carry on round the wheel: "E" -- "F G A B C..."</>,
      ]}/>
      <LbRemember>{t('Seven letters, round and round: after G comes A.', '일곱 글자가 돌고 돌아요: G 다음은 A.')}</LbRemember>
    </LbPage>,

    // 4. forwards up, backwards down (and backwards in your head, away from the piano)
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Forwards up, backwards down', '위로는 앞으로, 아래로는 거꾸로')}
      teacher={<>{t('Watch the turn from A back to G going down: students say "H", or restart at the top of the alphabet. Saying the alphabet backwards in your head, without the keyboard pattern, matters as much as finding it on the keys: practise it on its own, away from the piano, a little every day. ', '내려갈 때 A에서 G로 넘어가는 곳을 봐 주세요: "H"라고 하거나 알파벳 처음으로 돌아가요. 건반 패턴 없이 머릿속으로 알파벳을 거꾸로 말하는 것도 건반에서 찾는 것만큼 중요해요: 피아노 밖에서, 따로, 날마다 조금씩 연습해요. ')}{t('One finger (3) walking is fine here: this page is about the names, not the hand.', '여기서는 손가락 하나(3번)로 걸어도 괜찮아요: 이 쪽은 손이 아니라 이름이 주인공이에요.')}</>}>
      <LbLive still={<LbPic h={205}><div style={{width:'100%',maxWidth:600,margin:'0 auto'}}><PenArt shapes={art3} vb={[0, 2, 340, 146]} label={t('Two octaves of keys: an arrow to the right, up to the bird, reads C D E F G A B C; an arrow to the left, down to the turtle, reads C B A G F E D C', '두 옥타브 건반: 오른쪽 새 쪽 화살표는 C D E F G A B C, 왼쪽 거북이 쪽 화살표는 C B A G F E D C')}/></div></LbPic>} live={<UpDownWalk/>}/>
      <LbSay>{LANG === 'ko' ? <>피아노를 <b>위로</b> -- 오른쪽, 하늘 위 새 쪽으로 -- 올라가면 글자는 <b>앞으로</b> 가요: C D E F G A B C. <b>아래로</b> -- 왼쪽, 바다 아래 거북이 쪽으로 -- 내려가면 관람차가 거꾸로 돌고 글자도 <b>거꾸로</b> 가요: C B A G F E D C. 거꾸로가 어려워요: 건반 위에서도, 머릿속으로도, 앞으로만큼 빨리 나올 때까지 말해 봐요.</>
        : <>Going <b>up</b> the piano -- to the right, towards the bird in the sky -- the letters go <b>forwards</b>: C D E F G A B C. Going <b>down</b> -- to the left, towards the turtle under the sea -- the wheel turns the other way, and the letters go <b>backwards</b>: C B A G F E D C. Backwards is the tricky one: say it until it comes as quickly as forwards -- on the keys, and in your head.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <><b>가운데 도</b>에서 흰건반을 하나씩 올라가 다음 C까지, 글자를 앞으로 말해요.</>,
        <>다시 가운데 도까지 내려오며 거꾸로 말해요: <b>C B A G F E D C</b>.</>,
        <><b>G</b>에서 아래 G까지 내려가요. A에서 G로 돌아가는 곳을 조심!</>,
      ] : [
        <>From <b>middle C</b>, play up one white key at a time to the next C, saying the letters forwards.</>,
        <>Come back down to middle C, saying them backwards: <b>C B A G F E D C</b>.</>,
        <>Start on <b>G</b> and go down to the G below. Careful where the wheel turns back from A to G!</>,
      ]}/>
      <LbPiano title={t('Away from the piano', '피아노 밖에서')} icon={<LbHeadIcon/>} steps={LANG === 'ko' ? [
        <>피아노도 건반도 없이: <b>머릿속으로 거꾸로</b> 말해요 -- G F E D C B A -- 그다음 E에서, B에서, 아무 글자에서나 시작해요.</>,
        <>차 안에서, 목욕하면서, 학교 가는 길에 -- 거꾸로가 앞으로만큼 빨리 나올 때까지.</>,
      ] : [
        <>No piano, no keys: say the letters <b>backwards in your head</b> -- G F E D C B A -- then start from E, from B, from any letter.</>,
        <>In the car, in the bath, on the way to school -- until backwards comes as fast as forwards.</>,
      ]}/>
      <LbRemember>{t('Up the piano: forwards. Down the piano: backwards.', '피아노 위로는 앞으로, 아래로는 거꾸로.')}</LbRemember>
    </LbPage>,

    // 5. name it at a glance: who lives there
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Name it at a glance', '보자마자 이름 대기')}
      teacher={<>{t('Who lives there is a speed tool, not a new fact: each one sits in its key\'s place in the house -- the Dog between the two black keys, Grandma and her Apple garden between the three -- and each word starts with its key\'s letter. Watch for counting up from C on every key: ask "Who lives there?" instead.', '누가 사는지는 새 사실이 아니라 속도를 위한 도구예요: 모두 집 안의 제자리에 살아요 -- 강아지는 검은건반 두 개 사이, 할머니와 사과 정원은 세 개 사이 -- 그리고 단어마다 그 건반의 글자로 시작해요. 건반마다 C부터 세는지 봐 주세요: 대신 "거기 누가 살지?" 하고 물어요.')}</>}>
      <LbLive still={<LbPic h={300}><div style={{width:'100%',maxWidth:590,margin:'0 auto'}}><PenArt shapes={art4} vb={[0, -4, 300, 208]} label={t('One octave under its two roofs, with who lives on each white key: the Cat on C, the Dog in his doghouse on D, the Elephant on E; the Front door on F, Grandma on G, her Apple garden on A, the Back door on B', '두 지붕 아래 한 옥타브, 흰건반마다 사는 이: C에 고양이, D에 개집 속 강아지, E에 코끼리; F에 앞문, G에 할머니, A에 사과 정원, B에 뒷문')}/></div></LbPic>} live={<><WhoLivesHere/><FindAll/></>}/>
      <LbSay>{LANG === 'ko' ? <>매번 C부터 걸어가면 느려요. 대신 <b>누가 사는지</b> 봐요. 작은 집 한가운데, 검은건반 두 개 사이 개집에는 <b>강아지(Dog)</b>가 살아요: <b>D</b>. 왼쪽 문에는 <b>고양이(Cat)</b>, <b>C</b>. 오른쪽 문에는 <b>코끼리(Elephant)</b>, <b>E</b>. 큰 집에는 <b>앞문(Front door)</b> <b>F</b>와 <b>뒷문(Back door)</b> <b>B</b>가 있고, 그 안에는 사과를 좋아하는 <b>할머니(Grandma)</b> <b>G</b>가 살아요 -- 그래서 바로 옆이 할머니의 <b>사과 정원(Apple garden)</b>, <b>A</b>예요.</>
        : <>Walking up from C every time is slow. Instead, look at <b>who lives there</b>. In the small house, the <b>Dog</b> lives in the middle, in his doghouse between the two black keys: that is <b>D</b>. The <b>Cat</b> sits at the left door (<b>C</b>) and the <b>Elephant</b> at the right door (<b>E</b>). The big house has a <b>Front door</b> (<b>F</b>) and a <b>Back door</b> (<b>B</b>); inside lives <b>Grandma</b> (<b>G</b>), who loves apples -- so right next to her is her <b>Apple garden</b> (<b>A</b>).</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>피아노의 <b>모든 D</b>를 찾아요: 검은건반 두 개 사이, 개집의 강아지예요.</>,
        <><b>모든 G와 A</b>를 찾아요: 큰 집 안의 할머니와 사과 정원.</>,
        <><b>빨리 대기 게임:</b> 누가 흰건반 하나를 짚으면, 누가 사는지와 글자를 말해요 -- "코끼리: E!" 그다음 바꿔서!</>,
      ] : [
        <>Find <b>every D</b> on the piano: the Dog in his doghouse, between the two black keys.</>,
        <>Find <b>every G and A</b>: Grandma and her Apple garden, inside the big house.</>,
        <><b>Fast game:</b> someone touches any white key; say who lives there and its letter -- "Elephant: E!" Then swap.</>,
      ]}/>
      <LbRemember>{t('Don\'t count from C: ask who lives there.', 'C부터 세지 말고, 누가 사는지 봐요.')}</LbRemember>
    </LbPage>,

    // 6. skip a letter
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Skip a letter', '한 글자 건너뛰기')}
      teacher={<>{t('Skips are the hardest part of this chapter for most children: go slowly with the whispered letter first, then drop the whisper. Letters only here -- the numbers (3rd, 5th) wait for Intervals. ', '건너뛰기는 대부분의 아이들에게 이 챕터에서 가장 어려운 부분이에요: 처음에는 넘어가는 글자를 속삭이며 천천히, 그다음 속삭임을 빼요. 여기서는 글자로만 -- 3도, 5도 같은 숫자는 음정 챕터에서 만나요. ')}{t('The star: C E G B D F A joined round the circle makes a 7-pointed star; the Workbook has the one to draw.', '별: 원 위에서 C E G B D F A를 이으면 꼭짓점 일곱 개짜리 별이 돼요; 워크북에 직접 그리는 쪽이 있어요.')}</>}>
      <LbLive still={<LbPic h={230}><div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><PenArt shapes={art5} vb={[0, 12, 340, 160]} label={t('The seven letters round a circle joined a skip at a time make a star; on the keys, hops from C to E to G to B to D', '원 위의 일곱 글자를 하나씩 건너 이으면 별이 돼요; 건반 위에서는 C에서 E, G, B, D로 깡충')}/></div></LbPic>} live={<LetterChainDrill sizes={[2, 3]} noStaff/>}/>
      <LbSay>{LANG === 'ko' ? <><b>한 걸음</b>은 바로 다음 글자로 가요. <b>건너뛰기</b>는 하나를 넘어가요: C, (D), <b>E</b>, (F), <b>G</b>... 관람차를 건너뛰며 한 바퀴 돌면 -- C E G B D F A, 그리고 다시 C -- 선이 <b>별</b>을 그려요. 피아노에서 건너뛰기는 흰건반 하나를 넘어가는 거예요. 처음에는 넘어가는 글자를 <b>속삭여요</b> -- C (d) E (f) G -- 그다음 속삭임을 빼요.</>
        : <>A <b>step</b> goes to the very next letter. A <b>skip</b> jumps over one: C, (D), <b>E</b>, (F), <b>G</b>... Skip all the way round the wheel -- C E G B D F A, and back to C -- and the lines draw a <b>star</b>. On the piano, a skip jumps over one white key. At first, <b>whisper</b> the letter you jump over -- C (d) E (f) G -- then leave the whisper out.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>3번 손가락으로 가운데 도에서 건너뛰며 올라가요: <b>C E G B D F A C</b>. 처음엔 사이 글자를 속삭이고, 그다음 치는 글자만 말해요.</>,
        <>건너뛰며 내려와요: <b>C A F D B G E C</b>.</>,
        <>누가 글자를 말하면, 한 번 건너뛴 위의 글자를 말해요 (C → E, F → A, A → C).</>,
      ] : [
        <>With finger 3, skip up from middle C: <b>C E G B D F A C</b>. Whisper the letters in between at first; then say only the ones you play.</>,
        <>Skip back down: <b>C A F D B G E C</b>.</>,
        <>Someone says a letter; you say the letter a skip up (C → E, F → A, A → C).</>,
      ]}/>
      <LbRemember>{t('A skip jumps over a friend: C, (D), E.', '건너뛰기는 친구 하나를 넘어가요: C, (D), E.')}</LbRemember>
    </LbPage>,

    // 7. play by letter names
    <LbPage key="7" no={7} chId={ch} kicker={t('Play', '연주')} title={t('Play by letter names', '음이름 보고 연주하기')}
      teacher={<>{t('Same tune, new house: Chapter 2 played it by finger numbers on the black roof; now it is read by letter names on C D E. The legato is still the relay baton. Fingers 2 3 4 only, in both hands -- 1 and 5 wait for C position. ', '같은 노래, 새 집: 2챕터에서는 검은 지붕 위에서 손가락 번호로 쳤고, 이제는 C D E 위에서 음이름을 읽고 쳐요. 레가토는 여전히 릴레이 바통. 양손 모두 2 3 4번만 -- 1번과 5번은 C 포지션에서 만나요. ')}{t('Letter chain out loud: one letter each, turn about, then backwards.', '소리 내어 글자 잇기: 한 글자씩 번갈아, 그다음 거꾸로.')}</>}>
      <LbOnly print><LbPic h={160}><div style={{width:'100%',maxWidth:470,margin:'0 auto'}}><PenArt shapes={art6} vb={[0, 0, 258, 126]} label={t('Right-hand fingers 2, 3 and 4 on C, D and E, the small house\'s white keys', '작은 집의 흰건반 C, D, E 위에 오른손 2, 3, 4번 손가락')}/></div></LbPic></LbOnly>
      <LbSay>{LANG === 'ko' ? <>지난 챕터에서 핫 크로스 번은 큰 검은 지붕 위에 살았어요. 이제 <b>작은 집</b>으로 이사해요: 오른손 <b>2 3 4</b>를 <b>C D E</b>에 올리고, 이번에는 손가락 번호가 아니라 <b>글자</b>를 읽어요. 그다음 왼손으로, 작은 집 하나 아래에서 쳐 봐요.</>
        : <>Last chapter, Hot Cross Buns lived on the big black roof. Now it moves into the <b>small house</b>: right-hand <b>2 3 4</b> on <b>C D E</b>, and this time you read the <b>letters</b>, not the finger numbers. Then try the left hand, one small house lower.</>}</LbSay>
      <LbOnly print><div style={{zoom:0.85}}><LbTune name="Hot Cross Buns" how={t('right hand 2 3 4 on C D E; read the letters; one circle = one steady beat', '오른손 2 3 4를 C D E에; 글자를 읽어요; 동그라미 하나 = 일정한 박 하나')} seq={hcbL}/></div></LbOnly>
      <LbOnly screen><LetterSong/></LbOnly>
      <div style={{border:'1px solid #ece6d8',borderRadius:12,padding:'7px 12px',fontSize:13.5,lineHeight:1.5,color:BK.ink}}>
        <b style={{fontFamily:LB_SERIF,fontSize:15.5}}>{t('Spell and play', '단어 치기')}</b> — {t('a word made only of music letters is a tiny tune. Play', '음악 글자로만 된 단어는 작은 노래예요. 쳐 봐요:')} <b>BAG</b>, <b>CAFE</b>, <b>FACE</b>, <b>BEAD</b>, <b>EGG</b>{t(', saying each letter as you play it -- then make up a word of your own.', ' -- 치면서 글자를 하나씩 말하고, 나만의 단어도 만들어 봐요.')}</div>
      <LbPiano steps={LANG === 'ko' ? [
        <>가운데 도 근처의 <b>C D E</b>에 오른손 <b>2, 3, 4</b>. 치면서 글자를 노래해요: <b>E D C...</b></>,
        <>왼손: 작은 집 하나 아래의 C D E에 <b>4, 3, 2</b> -- 같은 글자, 더 낮은 목소리.</>,
        <><b>글자 잇기:</b> 내가 글자 하나, 상대가 다음 글자 -- 점점 빨리, 그다음 거꾸로!</>,
      ] : [
        <>Right-hand <b>2, 3, 4</b> on <b>C D E</b> near middle C. Sing the letters as you play: <b>E D C...</b></>,
        <>Left hand: <b>4, 3, 2</b> on C D E one small house lower -- the same letters, a lower voice.</>,
        <><b>Letter chain:</b> you say a letter, someone says the next -- faster and faster, then backwards!</>,
      ]}/>
      <LbRemember>{t('Read the letter, see its place, play -- no counting from C.', '글자를 읽고, 자리를 보고, 쳐요 -- C부터 세지 않기.')}</LbRemember>
    </LbPage>,

    // 8. my five checks + the check-up on paper
    <LbPage key="8" no={8} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Chapter 1\'s five checks still come first at the piano. These five are this chapter\'s own: the student shows each one on the keyboard or says it out loud; you only correct. All five "got it"? Then the paper part on the same page.', '1챕터의 다섯 가지 확인은 피아노 앞에서 여전히 먼저예요. 이 다섯 가지는 이 챕터만의 확인이에요: 학생이 건반 위에서 보여 주거나 소리 내어 말하고, 선생님은 고쳐 주기만 해요. 다섯 가지 다 "됐어요!"가 되면 같은 쪽의 종이 점검을 해요.')}</>}>
      <LbSay>{t('At the piano: show each one, then tick how it is going -- not yet, nearly, or got it! On paper: do the check-up below.', '피아노 앞에서: 하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요! 종이에서: 아래 점검을 풀어요.')}</LbSay>
      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_nn_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
      <LbOnly print><NnPaperCheck/></LbOnly>
    </LbPage>,
  ];
}
function NoteNamesLessonBook() { return <>{nnLbPages(false)}</>; }
// a head with a thought bubble: the "Away from the piano" box
function LbHeadIcon() {
  return <svg width="33" height="28" viewBox="0 0 26 22" aria-hidden="true" style={{display:'block'}}>
    <circle cx="8" cy="13" r="6.2" fill="#fff" stroke={BK.ink} strokeWidth="1.6"/><circle cx="6" cy="12.4" r="0.9" fill={BK.ink}/><path d="M5.6 15.6 Q8 17.2 10.4 15.6" fill="none" stroke={BK.ink} strokeWidth="1.2" strokeLinecap="round"/>
    <circle cx="15.4" cy="6.6" r="1.3" fill={BK.coral}/><path d="M17.4 1.5 h6.2 a1.8 1.8 0 0 1 1.8 1.8 v3.2 a1.8 1.8 0 0 1 -1.8 1.8 h-6.2 a1.8 1.8 0 0 1 -1.8 -1.8 v-3.2 a1.8 1.8 0 0 1 1.8 -1.8 z" fill="#fff" stroke={BK.coral} strokeWidth="1.3"/>
    <text x="20.5" y="7" textAnchor="middle" fontSize="5" fontWeight="900" fill={BK.coral}>GFE</text>
  </svg>;
}
// the check-up on paper, in the order of the five checks
function NnPaperCheck() {
  const W = useMemo(() => nnWorkbook(), [LANG]);
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column'}}>
    <LbPaperHead/>
    {bkSec('A', 'Name the dotted keys.')}
    <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 10px',width:'62%'}}><PaperKeys start="G" whites={10} w={30} h={66} dots={W.chk.nm} boxes={W.chk.nm} boxNos={Object.fromEntries([...W.chk.nm].sort((a, b) => a - b).map((d, j) => [d, j + 1]))}/></div>
    {bkSec('B', 'Fill in the missing letters.')}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{W.chk.ab.map((r, i) => <LetterRow key={i} n={(5 + 2 * i) + '-' + (6 + 2 * i)} cells={rowCells(r, false)}/>)}</div>
    {bkSec('C', 'One step up or down.')}
    <BkGrid cols={4} gap="6px 10px">{W.chk.ud.map((it, i) => <UpDownCell key={i} it={it} n={i + 9}/>)}</BkGrid>
    {bkSec('D', 'Row 1 goes backwards. Row 2 skips a letter.')}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8}}>{W.chk.ch.map((r, i) => <LetterRow key={i} n={(13 + 2 * i) + '-' + (14 + 2 * i)} cells={rowCells(r, false)}/>)}</div>
    {bkSec('E', 'Hot Cross Buns: write the letters under the beats.')}
    <NnTuneRow seq={NN_CHK_SONG} n0={17}/>
  </div>;
}
// a tune by letter names, with boxes for the missing letters (ex: the first box shows its answer in coral)
const NN_SONG_L = ['E', 'D', 'C', '-', '|', 'E', 'D', 'C', '-', '|', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', '|', 'E', 'D', 'C', '-'];
const NN_SONG_GAPS = [1, 7, 12, 15, 19, 21];
const NN_CHK_SONG = ['E', 'D', '?C', '-', '|', 'E', '?D', 'C', '-'];
function NnTuneRow({ seq, ex, n0 }) {
  let g = 0;
  const cell = (x, i) => {
    if (x === '-') return <span key={i} style={{width:28,height:28,borderRadius:14,border:'1.6px dashed ' + BK.line}}/>;
    if (x[0] === '?') { const first = g === 0; g++; return <span key={i} style={{position:'relative',display:'inline-flex'}}>{ex && first ? bkHand(x.slice(1), 30, 28) : bkBox(30, 28)}{n0 && <span style={{position:'absolute',top:-11,left:1,fontSize:8.5,fontWeight:900,color:BK.coral}}>{n0 + g - 1}</span>}</span>; }
    return <span key={i} style={{width:28,height:28,borderRadius:14,border:'2px solid ' + BK.ink,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{x}</span>;
  };
  const bars = [[]]; seq.forEach((x, i) => { if (x === '|') bars.push([]); else bars[bars.length - 1].push([x, i]); });
  return <div style={{display:'flex',flexWrap:'wrap',gap:'10px 0',alignItems:'center',padding:n0 ? '10px 4px 2px' : '2px 4px'}}>{bars.map((b, k) => <span key={k} style={{display:'inline-flex',alignItems:'center',gap:6,whiteSpace:'nowrap'}}>
    {k > 0 && <span style={{width:1.6,height:28,background:BK.ink,opacity:0.5,margin:'0 8px 0 4px'}}/>}{b.map(([x, i]) => cell(x, i))}</span>)}</div>;
}
// ─── the chapter's own small moving parts (screen only) ───
// Who lives here? tap a white key: who lives there, and its letter
function WhoLivesHere() {
  const PCS = [0, 2, 4, 5, 7, 9, 11];
  const [pick, setPick] = useState(null);
  const L = pick == null ? null : NN_L7[PCS.indexOf(pick % 12)];
  const marks = {}, names = {};
  if (pick != null) { marks[pick] = 'good'; names[pick] = L; }
  const say = LANG === 'ko'
    ? { C: 'C -- 고양이(Cat): 작은 집의 왼쪽 문.', D: 'D -- 강아지(Dog): 검은건반 두 개 사이, 개집에 살아요.', E: 'E -- 코끼리(Elephant): 작은 집의 오른쪽 문.', F: 'F -- 큰 집의 앞문(Front door).', G: 'G -- 할머니(Grandma): 큰 집 안에 살아요.', A: 'A -- 할머니의 사과 정원(Apple garden): 할머니 바로 옆.', B: 'B -- 큰 집의 뒷문(Back door).' }
    : { C: 'C -- the Cat, at the small house\'s left door.', D: 'D -- the Dog, in his doghouse between the two black keys.', E: 'E -- the Elephant, at the small house\'s right door.', F: 'F -- the big house\'s Front door.', G: 'G -- Grandma, inside the big house.', A: 'A -- Grandma\'s Apple garden, right next to her.', B: 'B -- the big house\'s Back door.' };
  return (
    <div className="try-box" data-who-lives style={actBox}>
      <div style={actTitle}>{t('Who lives here?', '누가 살까?')}</div>
      <div style={actNote}>{t('Tap any white key: see who lives there -- then say its letter before you look.', '흰건반을 아무거나 눌러 봐요: 누가 사는지 보고 -- 다음엔 보기 전에 글자를 먼저 말해요.')}</div>
      <TapKeyboard octaves={2} tint marks={marks} names={names} onTap={(k) => { playKey(k); if (PC_INFO[k % 12].white) setPick(k); }}/>
      <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:12,minHeight:58,marginTop:8}}>
        {L ? <>{nnResIcon(L, 52)}<div style={{fontSize:15,fontWeight:800,color:'var(--navy)',lineHeight:1.35}}>{say[L]}</div></>
          : <div style={{fontSize:14,fontWeight:700,color:'var(--muted)'}}>{t('Cat · Dog · Elephant -- Front door · Grandma · Apple garden · Back door', '고양이 · 강아지 · 코끼리 -- 앞문 · 할머니 · 사과 정원 · 뒷문')}</div>}
      </div>
    </div>
  );
}
// Hot Cross Buns read by letter names: right hand 2 3 4 on C D E (watch, then your turn)
const NN_SONG = { keys: [16, 14, 12, 16, 14, 12, 12, 12, 12, 12, 14, 14, 14, 14, 16, 14, 12], durs: [1, 1, 2, 1, 1, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, 2] };
function LetterSong() {
  const song = NN_SONG;
  const [mode, setMode] = useState('watch');
  const [i, setI] = useState(-1);
  const [bad, setBad] = useState(null);
  const timers = useRef([]);
  useEffect(() => () => timers.current.forEach(clearTimeout), []);
  function watch() {
    timers.current.forEach(clearTimeout); timers.current = [];
    let tt = 0;
    song.keys.forEach((k, j) => { timers.current.push(setTimeout(() => { setI(j); playKey(k, song.durs[j] * 0.45); }, 150 + tt * 480)); tt += song.durs[j]; });
    timers.current.push(setTimeout(() => setI(-1), 150 + tt * 480 + 300));
  }
  function tap(k) {
    playKey(k, 0.35);
    if (mode !== 'turn') return;
    if (k === song.keys[i + 1]) { setI(i + 1); setBad(null); } else { setBad(k); setTimeout(() => setBad(b => (b === k ? null : b)), 500); }
  }
  const done = mode === 'turn' && i === song.keys.length - 1;
  const cur = mode === 'watch' ? (i >= 0 ? song.keys[i] : null) : (i + 1 < song.keys.length ? song.keys[i + 1] : null);
  const marks = {}; if (cur !== null) marks[cur] = mode === 'watch' ? 'good' : 'target'; if (bad !== null) marks[bad] = 'bad';
  const nm = (k) => PC_INFO[k % 12].names[0];
  return (
    <div className="try-box" data-letter-song style={actBox}>
      <div style={actTitle}>{t('Hot Cross Buns by letter names', '음이름으로 치는 핫 크로스 번')}</div>
      <div style={actNote}>{t('Right hand 2 3 4 on C D E. Read the letters, not the finger numbers. First Watch, then Your turn: the orange key plays next.', '오른손 2 3 4를 C D E에. 손가락 번호 말고 글자를 읽어요. 먼저 보기, 그다음 내 차례: 주황색 건반이 다음 차례예요.')}</div>
      <TapKeyboard octaves={2} marks={marks} names={{ 12: 'C', 14: 'D', 16: 'E' }} onTap={tap}/>
      <div style={{display:'flex',flexWrap:'wrap',gap:4,justifyContent:'center',margin:'8px 0',fontSize:15,fontWeight:900}}>
        {song.keys.map((k, j) => { const on = mode === 'watch' ? j === i : j <= i; return <span key={j} style={{minWidth:15,textAlign:'center',color:on ? '#e4572e' : '#26296b'}}>{nm(k)}</span>; })}
      </div>
      {done && <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:'#2e8a6e',marginBottom:6}}>{t('You played Hot Cross Buns by its letters!', '글자를 보고 핫 크로스 번을 끝까지 쳤어요!')}</div>}
      <div style={{display:'flex',gap:6,justifyContent:'center'}}>
        <button className="ghost-btn" style={mode === 'watch' ? {borderColor:'var(--text)'} : {}} onClick={() => { setMode('watch'); setI(-1); setTimeout(watch, 60); }}>{t('▶ Watch', '▶ 보기')}</button>
        <button className="ghost-btn" style={mode === 'turn' ? {borderColor:'var(--text)'} : {}} onClick={() => { timers.current.forEach(clearTimeout); setMode('turn'); setI(-1); }}>{t('Your turn', '내 차례')}</button>
      </div>
    </div>
  );
}
// the online lesson: the book's pages 2-8 as its seven steps (the old four steps' ticks stay where their content went:
// 0 the black-key map -> A to G on the keys, 1 seven letters -> the wheel, 2 up and down -> forwards/backwards, 3 the letter chain -> play)
const NN_STORE = [0, 1, 2, 4, 5, 3, 6];
function NoteNamesLearn({ onStart }) {
  const pages = nnLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="note-names" title={t('The Musical Alphabet', '음악 알파벳')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="note-names"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={NN_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}
