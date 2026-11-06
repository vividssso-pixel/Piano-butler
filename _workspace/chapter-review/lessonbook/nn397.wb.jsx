function nnWorkbook() {
  // Phase 397: the chapter 3 Workbook follows the Lesson Book page by page (The Musical Alphabet)
  const k = (s) => 'nn-wb397-' + s;
  // n keys spread across the keyboard (one per stretch), all different letters
  const dotSet = (whites, start, n, avoid = []) => { for (let g = 0; g < 200; g++) { const out = [], seen = new Set(avoid); let ok = true; for (let q = 0; q < n; q++) { const lo = Math.floor(q * whites / n), hi = Math.floor((q + 1) * whites / n) - 1; const i = lo + Math.floor(Math.random() * (hi - lo + 1)); const l = nnLet(start, i); if (seen.has(l) || (out.length && i - out[out.length - 1] < 2)) { ok = false; break; } seen.add(l); out.push(i); } if (ok) return out; } return Array.from({ length: n }, (_, q) => Math.floor((q + 0.5) * whites / n)); };
  const mk = (l, up) => ({ l, up, a: azStep(l, up ? 1 : -1) });
  const s1 = withSeed(k('s1'), () => { const a = dotSet(10, 'C', 4); const al = a.map(i => nnLet('C', i)); const b = dotSet(10, 'A', 4, al.slice(0, 1)); return { kb: [{ start: 'C', dots: a }, { start: 'A', dots: b }] }; });
  const s2 = withSeed(k('s2'), () => ({ tog: [nnRow(1, 8, 3), nnRow(1, 8, 3), nnRow(1, 8, 3)], home: Array.from({ length: 6 }, () => nnRow(1, 7, 3)) }));
  const s3 = withSeed(k('s3'), () => ({ tog: [mk('D', true), mk(pick(['E', 'F', 'B']), false), mk(pick(['C', 'A']), true), mk(pick(['G', 'D']), false)], back: [nnRow(-1, 7, 3), nnRow(-1, 7, 3), nnRow(-1, 7, 3), nnRow(-1, 7, 3)] }));
  const hunt = withSeed(k('hunt'), () => { let pos = 3; const moves = []; while (moves.length < 6) { const m = pick([2, 3, 4, -1, -2, -3]); if (pos + m >= 0 && pos + m <= 14) { pos += m; moves.push({ m, land: pos }); } } return { start: 3, moves }; });
  const gl = withSeed(k('gl'), () => { const rest = shuffle(['C', 'E', 'F', 'G', 'A', 'B']); return { tog: ['D', ...rest.slice(0, 3)], home: rest.slice(3), kb: dotSet(14, 'C', 6) }; });
  const sk = withSeed(k('sk'), () => ({ tog: [nnRow(2, 8, 3), nnRow(2, 8, 3), nnRow(2, 8, 3)], home: [nnRow(2, 7, 3), nnRow(2, 7, 3), nnRow(-2, 7, 3), nnRow(-2, 7, 3)] }));
  const search = withSeed(k('ws'), () => nnSearch());
  const chk = withSeed(k('chk'), () => ({
    nm: dotSet(10, 'G', 4),
    ab: [nnRow(1, 7, 2), nnRow(1, 7, 2)],
    ud: [{ l: 'G', up: true }, { l: pick(['C', 'D']), up: false }, { l: 'A', up: false }, { l: pick(['E', 'B']), up: true }].map(o => ({ ...o, a: azStep(o.l, o.up ? 1 : -1) })),
    ch: [nnRow(-1, 7, 2), nnRow(2, 7, 2)],
  }));
  return { s1, s2, s3, hunt, gl, sk, search, chk };
}
function nnConcepts() {
  return [
    { id: 'ag', name: 'A to G on the keys', step: '1', page: '2' },
    { id: 'wh', name: 'The letter wheel', step: '2', page: '3' },
    { id: 'ud', name: 'Forwards and backwards', step: '3', page: '4' },
    { id: 'gl', name: 'Name it at a glance', step: '4', page: '5' },
    { id: 'sk', name: 'Skip a letter', step: '5', page: '6' },
    { id: 'pl', name: 'Hot Cross Buns by letters', step: '6', page: '7' },
    { id: 'ck', name: 'My five checks', step: '7', page: '8', chk: false },
  ];
}
