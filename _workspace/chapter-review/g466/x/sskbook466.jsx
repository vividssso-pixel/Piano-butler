// ─── Phase 466: chapter 9 (Steps & Skips): the Lesson Book, built in full under Book rules 14 and 15 (her 2026-10-13
// 23:51 '지금부터 추천대로 다 가줘 ... 사전처럼 깔끔하게', and 2026-10-14 06:54 '계속 가줘'). The level plan's scope for room 9
// (Level 2): pitch and rhythm together: tiny tunes, up / down / the same, a step and a skip, the C and G five-finger
// positions. It builds on the staff (chapter 6: lines and spaces, a first look at steps and skips, C D E F G in the
// treble clef, F G A B C in the bass clef, middle C on its little ladder), Line and Space Names (chapter 7), Notes &
// Rests (chapter 5) and Time Signatures (chapter 8: bars, 2/4 3/4 4/4). Every tune is new (no songs inside the
// chapters, Book rule 8). The interval numbers (2nd, 3rd ...) are given once, as the other names of a step and a skip;
// intervals themselves wait for their chapter.

// a tune on one staff, drawn inside SfStaff's extra(yOf). items: ['ts', top], ['|'], ['||'], ['sp', px], notes
// [kind, beats, d] (kind 'w' 'hd' 'h' 'q'), a quaver pair ['p', 1, [d1, d2]], rests ['r', 1] ['hr', 2] ['wr', 4].
// o: clef, D (px a beat), x0, ink, minW, lit / hl (note indexes drawn coral), fingers (by note index: a number, '' an
// empty circle; o.fingerAt 'above' | 'below'; o.fingerR), under (by note index: a word under the staff, null an empty
// box; o.boxS its size, o.underBoxed the word in a box, o.underCoral the worked ones),
// moves ('arrow' | 'box' | 'word' | 'bracket' | 'circ'; o.moveOn: which moves, by index; o.moveAns: worked ones),
// contour (a dashed line through the heads), noTail (no end line). Returns the raw SVG, the notes, the bar lines,
// the end and the drawing's top and bottom.
const sskIsRest = (k) => k === 'r' || k === 'hr' || k === 'wr';
const sskMove = (a, b) => b === a ? 'same' : Math.abs(b - a) === 1 ? 'step' : Math.abs(b - a) === 2 ? 'skip' : 'leap';
const SSK_WORD = { step: () => t('step', '한 걸음'), skip: () => t('skip', '건너뛰기'), same: () => t('same', '같은 음'), leap: () => t('leap', '크게 뛰기') };
function sskArrow(x, y, dir, col, s = 1) {   // up, down or the same (=), drawn in lines so it prints alike everywhere
  const w = 2.2 * s, h = 8 * s;
  if (dir === 0) return '<line x1="' + pFix(x - 6 * s) + '" x2="' + pFix(x + 6 * s) + '" y1="' + pFix(y - 3 * s) + '" y2="' + pFix(y - 3 * s) + '" stroke="' + col + '" stroke-width="' + pFix(w) + '" stroke-linecap="round"/><line x1="' + pFix(x - 6 * s) + '" x2="' + pFix(x + 6 * s) + '" y1="' + pFix(y + 3 * s) + '" y2="' + pFix(y + 3 * s) + '" stroke="' + col + '" stroke-width="' + pFix(w) + '" stroke-linecap="round"/>';
  const tip = y - dir * h, tail = y + dir * h;
  return '<line x1="' + pFix(x) + '" x2="' + pFix(x) + '" y1="' + pFix(tail) + '" y2="' + pFix(tip) + '" stroke="' + col + '" stroke-width="' + pFix(w) + '" stroke-linecap="round"/><path d="M' + pFix(x - 5 * s) + ' ' + pFix(tip + dir * 5 * s) + ' L' + pFix(x) + ' ' + pFix(tip) + ' L' + pFix(x + 5 * s) + ' ' + pFix(tip + dir * 5 * s) + '" fill="none" stroke="' + col + '" stroke-width="' + pFix(w) + '" stroke-linecap="round" stroke-linejoin="round"/>';
}
function sskRaw(yOf, items, o = {}) {
  const clef = o.clef || 'treble', low = CLEFS[clef].low, high = CLEFS[clef].high, mid = low + 4;
  const D = o.D || 34, col = o.ink || PEN_N, cor = PEN_C, Y = (d) => yOf(d);
  const yTop = Y(high), yBot = Y(low), out = [], over = [], notes = [], bars = [];
  let x = o.x0 || 46, last = 0;
  const bar = (xx, w = 1.5) => '<line x1="' + pFix(xx) + '" x2="' + pFix(xx) + '" y1="' + pFix(yTop) + '" y2="' + pFix(yBot) + '" stroke="' + col + '" stroke-width="' + w + '"/>';
  const coral = (j) => o.lit === j || (o.hl || []).includes(j);
  const stem = (nx, y, up, c) => '<line x1="' + pFix(up ? nx + 6.4 : nx - 6.4) + '" x2="' + pFix(up ? nx + 6.4 : nx - 6.4) + '" y1="' + pFix(up ? y - 1.5 : y + 1.5) + '" y2="' + pFix(up ? y - 34 : y + 34) + '" stroke="' + c + '" stroke-width="1.9" stroke-linecap="round"/>';
  const ledgers = (nx, d) => ledgersFor(d, low, high).map(p => '<line x1="' + pFix(nx - 12) + '" x2="' + pFix(nx + 12) + '" y1="' + pFix(Y(p)) + '" y2="' + pFix(Y(p)) + '" stroke="' + col + '" stroke-width="1.4"/>').join('');
  items.forEach((it) => {
    const k = it[0];
    if (k === 'ts') { [[it[1], Y(low + 6)], [4, Y(low + 2)]].forEach(([n, y]) => out.push('<text x="' + pFix(x + 8) + '" y="' + pFix(y + 7.6) + '" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="25" font-weight="900" fill="' + col + '">' + n + '</text>')); x += 26; return; }
    if (k === 'sp') { x += it[1]; last = x; return; }
    if (k === '|') { out.push(bar(x + 2)); bars.push(x + 2); last = x + 2.8; x += 12; return; }
    if (k === '||') { out.push(bar(x + 1, 1.3), bar(x + 6, 4)); last = x + 8; x += 10; return; }
    const n = it[1], nx = x + 12;
    if (sskIsRest(k)) {
      if (k === 'r') out.push(nvbRest(nx + 2, Y(mid), 'q', { k: 0.82, col }).svg);
      else if (k === 'hr') out.push('<rect x="' + pFix(nx - 5) + '" y="' + pFix(Y(mid) - 5) + '" width="16" height="5" fill="' + col + '"/>');
      else out.push('<rect x="' + pFix(x + 12 + (n - 1) * D / 2 - 8) + '" y="' + pFix(Y(mid + 2)) + '" width="16" height="5" fill="' + col + '"/>');
      x += Math.max(n * D, o.minW || 0); return;
    }
    if (k === 'p') {   // two quavers, beamed: the stems go the way most of the pair would
      const [d1, d2] = it[2], x2 = nx + D * 0.65, up = d1 + d2 < 2 * mid, y1 = Y(d1), y2 = Y(d2);
      const by = up ? Math.min(y1, y2) - 32 : Math.max(y1, y2) + 32;
      [[nx, d1, y1], [x2, d2, y2]].forEach(([xx, d, y]) => { const c = coral(notes.length) ? cor : col;
        out.push(ledgers(xx, d), nvbHead(xx, y, 'q', c, 1), '<line x1="' + pFix(up ? xx + 6.4 : xx - 6.4) + '" x2="' + pFix(up ? xx + 6.4 : xx - 6.4) + '" y1="' + pFix(up ? y - 1.5 : y + 1.5) + '" y2="' + pFix(by) + '" stroke="' + c + '" stroke-width="1.9"/>');
        notes.push({ x: xx, y, d, up, end: by }); });
      const xa = (up ? nx + 6.4 : nx - 6.4) - 0.9, xb = (up ? x2 + 6.4 : x2 - 6.4) + 0.9;
      out.push('<rect x="' + pFix(xa) + '" y="' + pFix(up ? by : by - 5) + '" width="' + pFix(xb - xa) + '" height="5" fill="' + col + '"/>');
      x += Math.max(n * D * 1.3, o.minW || 0); return;
    }
    const d = it[2], y = Y(d), up = d < mid, kind = k === 'hd' ? 'h' : k, c = coral(notes.length) ? cor : col;
    out.push(ledgers(nx, d), nvbHead(nx, y, kind, c, 1));
    if (kind !== 'w') out.push(stem(nx, y, up, c));
    if (k === 'hd') out.push('<circle cx="' + pFix(nx + 14) + '" cy="' + pFix((d - low) % 2 === 0 ? y - 5 : y) + '" r="2.6" fill="' + c + '"/>');
    notes.push({ x: nx, y, d, up, end: kind === 'w' ? y : up ? y - 34 : y + 34 });
    x += Math.max(n * D, o.minW || 0);
  });
  if (!last) last = x;
  // what sits above and below: the moves, then the finger numbers (above); the words or boxes (below)
  const topOf = (nt) => Math.min(nt.y - 7, nt.up ? nt.end : nt.y - 7), botOf = (nt) => Math.max(nt.y + 7, nt.up ? nt.y + 7 : nt.end);
  let top = Math.min(yTop, ...notes.map(topOf)), bottom = Math.max(yBot, ...notes.map(botOf));
  const under = [];
  if (o.contour && notes.length > 1) under.push('<polyline points="' + notes.map(nt => pFix(nt.x) + ',' + pFix(nt.y)).join(' ') + '" fill="none" stroke="' + cor + '" stroke-width="1.6" stroke-dasharray="4 3" opacity="0.8"/>');
  if (o.moves) {   // over each move: an arrow, a box for one, the word, the word over a straight bracket, or three words to circle
    const on = (j) => !o.moveOn || o.moveOn[j], M = o.moves;
    const my = M === 'circ' ? top - 39 : M === 'bracket' ? top - 8 : M === 'box' ? top - 16 : top - 13;
    const word = (x, y, w, c, fs) => '<text x="' + pFix(x) + '" y="' + pFix(y) + '" text-anchor="middle" font-family="Inter, \'Apple SD Gothic Neo\', sans-serif" font-size="' + fs + '" font-weight="900" fill="' + c + '" paint-order="stroke" stroke="#fff" stroke-width="3" stroke-linejoin="round">' + w + '</text>';
    if (M === 'arrow' && o.moveIn != null && notes.length) over.push(sskArrow(notes[0].x - 22, my, o.moveIn, cor));
    for (let j = 0; j < notes.length - 1; j++) {
      if (!on(j)) continue;
      const a = notes[j], b = notes[j + 1], mx = (a.x + b.x) / 2, dir = Math.sign(b.d - a.d), mv = sskMove(a.d, b.d);
      if (M === 'arrow') over.push(sskArrow(mx, my, dir, cor));
      else if (M === 'box') {   // moveAns: filled in; moveCol: its colour (green right, coral not yet); moveCur: the one to answer now
        const shown = o.moveAns && o.moveAns[j], mc = (o.moveCol && o.moveCol[j]) || cor, now = o.moveCur === j;
        over.push('<rect x="' + pFix(mx - 11) + '" y="' + pFix(my - 11) + '" width="22" height="22" rx="3" fill="' + (now ? '#fbe3da' : '#fff') + '" stroke="' + (now ? cor : shown ? mc : 'rgba(38,41,107,0.45)') + '" stroke-width="' + (now ? 2.2 : 1.3) + '"/>');
        if (shown) over.push(sskArrow(mx, my, dir, mc, 0.8));
      } else if (M === 'circ') {   // step, skip, same stacked, to circle (moveAns: the worked one ringed)
        ['step', 'skip', 'same'].forEach((w, r) => { const y = my - 15 + r * 15, ring = o.moveAns && o.moveAns[j] && w === mv;
          if (ring) over.push('<rect x="' + pFix(mx - 15) + '" y="' + pFix(y - 9.5) + '" width="30" height="13" rx="6.5" fill="none" stroke="' + cor + '" stroke-width="1.4"/>');
          over.push('<text x="' + pFix(mx) + '" y="' + pFix(y) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="800" fill="' + (ring ? cor : col) + '">' + w + '</text>'); });
      } else if (M === 'word') over.push(word(mx, my + 4, SSK_WORD[mv](), cor, 10.5));
      else {   // a straight bracket over the two notes, the word over it: never a curve, which would read as a tie or a slur
        const x1 = a.x + 2, x2 = b.x + (b.up ? 6.4 : 2);
        over.push('<path d="M' + pFix(x1) + ' ' + pFix(my + 5) + ' L' + pFix(x1) + ' ' + pFix(my) + ' L' + pFix(x2) + ' ' + pFix(my) + ' L' + pFix(x2) + ' ' + pFix(my + 5) + '" fill="none" stroke="' + cor + '" stroke-width="1.6" stroke-linejoin="round"/>');
        over.push(word((x1 + x2) / 2, my - 5, SSK_WORD[mv](), cor, 12));
      }
    }
    top = M === 'circ' ? my - 26 : M === 'bracket' ? my - 19 : my - 14;
  }
  const R = o.fingerR || 9;
  const fing = (fy, j, v) => '<circle cx="' + pFix(notes[j].x) + '" cy="' + pFix(fy) + '" r="' + R + '" fill="#fff" stroke="' + cor + '" stroke-width="1.5"/>' + (v === '' ? '' : '<text x="' + pFix(notes[j].x) + '" y="' + pFix(fy + R * 0.5) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + pFix(R * 1.45) + '" font-weight="900" fill="' + cor + '">' + v + '</text>');
  if (o.fingers) {
    const has = notes.map((_, j) => o.fingers[j] != null);
    if (o.fingerAt === 'below') { const fy = bottom + 6 + R; notes.forEach((_, j) => { if (has[j]) over.push(fing(fy, j, o.fingers[j])); }); bottom = fy + R + 1; }
    else { const fy = top - 5 - R; notes.forEach((_, j) => { if (has[j]) over.push(fing(fy, j, o.fingers[j])); }); top = fy - R - 1; }
  }
  if (o.under) {   // a word under each note, or an empty box (null) to write it in; never touching a stem
    const BX = o.boxS || 24, bt = bottom + 8;
    notes.forEach((nt, j) => { const v = o.under[j]; if (v === undefined) return;
      if (v === null) over.push('<rect x="' + pFix(nt.x - BX / 2) + '" y="' + pFix(bt) + '" width="' + BX + '" height="' + BX + '" rx="3" fill="#fff" stroke="rgba(38,41,107,0.45)" stroke-width="1.3"/>');
      else { const cr = (o.underCoral || []).includes(j); if (o.underBoxed) over.push('<rect x="' + pFix(nt.x - BX / 2) + '" y="' + pFix(bt) + '" width="' + BX + '" height="' + BX + '" rx="3" fill="#fff" stroke="' + (cr ? cor : 'rgba(38,41,107,0.45)') + '" stroke-width="1.3"/>');
        over.push('<text x="' + pFix(nt.x) + '" y="' + pFix(bt + BX * 0.5 + 5) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + pFix(Math.max(13, BX * 0.55)) + '" font-weight="900" fill="' + (cr ? cor : col) + '"' + (cr ? ' font-style="italic"' : '') + '>' + v + '</text>'); } });
    bottom = bt + BX + 2;
  }
  return { raw: under.join('') + out.join('') + over.join(''), notes, bars, last, end: x, top, bottom };
}
// a tune on one staff: SfStaff draws the lines and the clef, sskRaw the rest; the staff ends at its last line
function SskStaff({ items, clef = 'treble', width = 400, o = {}, label, extra, full, pad }) {
  const oo = { ...o, clef }, m = sskRaw((d) => dY(d), items, oo), vbw = Math.ceil(m.last + 6);
  const hi = dY(CLEFS[clef].high), lo = dY(CLEFS[clef].low);
  const p = pad || [Math.max(12, hi - m.top + 6), Math.max(12, m.bottom - lo + 6)];
  return <div style={{width:full ? '100%' : Math.min(100, vbw / width * 100) + '%'}}><SfStaff clef={clef} width={vbw} span={[4, m.last]} pad={p} label={label}
    extra={(yOf, layer, txt) => layer === 'over' && <g><g dangerouslySetInnerHTML={{ __html: sskRaw((d) => yOf(d, clef), items, oo).raw }}/>{extra && extra(yOf, txt, m)}</g>}/></div>;
}
// a piece of the keyboard as raw SVG: nw white keys from the diatonic note d0; on { d: 'ink' | 'cor' | 'pale' };
// fingers { d: n } in coral circles; letters on every white key
function sskKeysRaw(x, y, d0, nw, W, H, o = {}) {
  const out = ['<rect x="' + pFix(x) + '" y="' + pFix(y) + '" width="' + pFix(nw * W) + '" height="' + pFix(H) + '" rx="2" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.6"/>'];
  const on = o.on || {}, BW = W * 0.6, BH = H * 0.58;
  for (let i = 0; i < nw; i++) { const d = d0 + i, m = on[d];
    if (m && m !== 'dash') out.push('<rect x="' + pFix(x + i * W + 1) + '" y="' + pFix(y + 1) + '" width="' + pFix(W - 2) + '" height="' + pFix(H - 2) + '" fill="' + (m === 'ink' ? PEN_N : m === 'cor' ? PEN_C : '#fbe3da') + '"/>');
    if (i) out.push('<line x1="' + pFix(x + i * W) + '" x2="' + pFix(x + i * W) + '" y1="' + pFix(y) + '" y2="' + pFix(y + H) + '" stroke="' + PEN_N + '" stroke-width="1.1"/>');
  }
  for (let i = 0; i < nw - 1; i++) if ([0, 1, 3, 4, 5].includes(((d0 + i) % 7 + 7) % 7)) out.push('<rect x="' + pFix(x + (i + 1) * W - BW / 2) + '" y="' + pFix(y) + '" width="' + pFix(BW) + '" height="' + pFix(BH) + '" rx="1" fill="' + PEN_N + '"/>');
  for (let i = 0; i < nw; i++) { const d = d0 + i, m = on[d], cx = x + (i + 0.5) * W;
    if (m === 'out' || m === 'dash') out.push('<rect x="' + pFix(x + i * W + 1.5) + '" y="' + pFix(y + H * 0.6) + '" width="' + pFix(W - 3) + '" height="' + pFix(H * 0.4 - 1.5) + '" rx="1.5" fill="none" stroke="' + (m === 'out' ? PEN_N : PEN_C) + '" stroke-width="' + (m === 'out' ? 2.4 : 1.6) + '"' + (m === 'dash' ? ' stroke-dasharray="3 2.5"' : '') + '/>');
    if (o.letters !== false) out.push('<text x="' + pFix(cx) + '" y="' + pFix(y + H - 6) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + pFix(Math.min(13, W * 0.5)) + '" font-weight="900" fill="' + (m === 'ink' || m === 'cor' ? '#fff' : PEN_N) + '">' + dName(d) + '</text>');
    const f = (o.fingers || {})[d];
    if (f != null) { const r = Math.min(9, W * 0.4), fy = y - r - 3; out.push('<circle cx="' + pFix(cx) + '" cy="' + pFix(fy) + '" r="' + pFix(r) + '" fill="#fff" stroke="' + PEN_C + '" stroke-width="1.4"/><text x="' + pFix(cx) + '" y="' + pFix(fy + r * 0.47) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + pFix(r * 1.35) + '" font-weight="900" fill="' + PEN_C + '">' + f + '</text>'); }
  }
  return out.join('');
}
const sskKeyX = (x, d0, W, d) => x + (d - d0 + 0.5) * W;

// a five-finger position: the grand staff over the keyboard, each note straight over its key; the left hand's five
// notes on the bass staff with their fingers below, the right hand's on the treble staff with theirs above
const SSK_POS = { C: { lh: [21, 22, 23, 24, 25], rh: [28, 29, 30, 31, 32], d0: 21, nw: 12 }, G: { lh: [18, 19, 20, 21, 22], rh: [32, 33, 34, 35, 36], d0: 18, nw: 19 } };
function SskPosPic({ pos, label, W = 26, hand }) {
  const P = SSK_POS[pos], x0 = 46, width = x0 + P.nw * W + 8, kx = (d) => sskKeyX(x0, P.d0, W, d), r = Math.min(9, W * 0.38);
  const showL = hand !== 'rh', showR = hand !== 'lh';
  const on = {}; if (showL) P.lh.forEach(d => { on[d] = 'pale'; }); if (showR) P.rh.forEach(d => { on[d] = 'pale'; });
  return <SfStaff clef="grand" width={width} pad={[44, 140]} label={label}
    extra={(yOf, layer, txt) => { if (layer !== 'over') return null;
      const head = (d, st) => { const x = kx(d), y = yOf(d, st), cl = CLEFS[st];
        return ledgersFor(d, cl.low, cl.high).map(p => '<line x1="' + pFix(x - 12) + '" x2="' + pFix(x + 12) + '" y1="' + pFix(yOf(p, st)) + '" y2="' + pFix(yOf(p, st)) + '" stroke="' + PEN_N + '" stroke-width="1.4"/>').join('') + nvbHead(x, y, 'w', PEN_N, 0.9); };
      const circ = (x, y, n) => '<circle cx="' + pFix(x) + '" cy="' + pFix(y) + '" r="' + pFix(r) + '" fill="#fff" stroke="' + PEN_C + '" stroke-width="1.4"/><text x="' + pFix(x) + '" y="' + pFix(y + r * 0.5) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + pFix(r * 1.4) + '" font-weight="900" fill="' + PEN_C + '">' + n + '</text>';
      const yT = Math.min(yOf(38, 'treble'), ...P.rh.map(d => yOf(d, 'treble') - 8)) - 16, yB = Math.max(yOf(18, 'bass'), ...P.lh.map(d => yOf(d, 'bass') + 8)) + 16;
      const ky = yB + 22, s = [];
      if (showR) P.rh.forEach((d, i) => s.push(head(d, 'treble'), circ(kx(d), yT, i + 1)));
      if (showL) P.lh.forEach((d, i) => s.push(head(d, 'bass'), circ(kx(d), yB, 5 - i)));
      s.push(sskKeysRaw(x0, ky, P.d0, P.nw, W, 62, { on }));
      return <g><g dangerouslySetInnerHTML={{ __html: s.join('') }}/>
        {showL && <text x={(kx(P.lh[0]) + kx(P.lh[4])) / 2} y={ky + 80} textAnchor="middle" fontSize="11" fontWeight="900" fill={BK.ink} style={txt}>{t('left hand', '왼손')}</text>}
        {showR && <text x={(kx(P.rh[0]) + kx(P.rh[4])) / 2} y={ky + 80} textAnchor="middle" fontSize="11" fontWeight="900" fill={BK.ink} style={txt}>{t('right hand', '오른손')}</text>}
      </g>; }}/>;
}
// a step or a skip: the two notes on the staff, each over its key; the first key framed in navy, the second coral; a
// skip's jumped key dashed; a straight bracket and the word over the notes (a curve would read as a tie or a slur)
function SskStepPic({ a, b, label }) {
  const x0 = 40, W = 36, d0 = 28, nw = 6, kx = (d) => sskKeyX(x0, d0, W, d), width = x0 + nw * W + 8;
  const word = sskMove(a, b), between = word === 'skip' ? (a + b) / 2 : null;
  return <SfStaff clef="treble" width={width} pad={[56, 118]} label={label}
    extra={(yOf, layer, txt) => { if (layer !== 'over') return null;
      const y1 = yOf(a), y2 = yOf(b), xa = kx(a), xb = kx(b), ky = yOf(28) + 22;
      const on = { [a]: 'out', [b]: 'cor' }; if (between) on[between] = 'dash';
      const by = Math.min(y1, y2) - 14, ty = yOf(38) - 26;
      return <g><g dangerouslySetInnerHTML={{ __html: nvbHead(xa, y1, 'w', PEN_N, 0.9) + nvbHead(xb, y2, 'w', PEN_C, 0.9) + '<path d="M' + pFix(xa) + ' ' + pFix(by + 5) + ' L' + pFix(xa) + ' ' + pFix(by) + ' L' + pFix(xb) + ' ' + pFix(by) + ' L' + pFix(xb) + ' ' + pFix(by + 5) + '" fill="none" stroke="' + PEN_C + '" stroke-width="1.7" stroke-linejoin="round"/>' + sskKeysRaw(x0, ky, d0, nw, W, 58, { on }) }}/>
        <text x={(xa + xb) / 2} y={ty} textAnchor="middle" fontSize="14" fontWeight="900" fill={BK.coral} style={txt}>{SSK_WORD[word]()}</text>
        <text x={(xa + xb) / 2} y={ty + 14} textAnchor="middle" fontSize="11" fontWeight="800" fill={BK.ink} style={txt}>{word === 'step' ? t('line to space', '줄에서 칸으로') : t('line to line', '줄에서 줄로')}</text>
        <text x={(xa + xb) / 2} y={ky + 76} textAnchor="middle" fontSize="12" fontWeight="900" fill={BK.ink} style={txt}>{word === 'step' ? t('the next white key', '바로 옆 흰 건반') : t('jump over one white key', '흰 건반 하나 건너')}</text>
      </g>; }}/>;
}
// a tune in systems (one staff under another), every system at one scale; o: one option set for each
const sskVbw = (items, o, clef) => Math.ceil(sskRaw((d) => dY(d), items, { ...o, clef }).last + 6);
function SskSystems({ rows, clef = 'treble', os = [], labels = [], extras = [], pads = [], gap = 10 }) {
  const w = Math.max(...rows.map((r, i) => sskVbw(r, os[i] || {}, clef)));
  return <div style={{display:'flex',flexDirection:'column',gap,width:'100%'}}>{rows.map((r, i) => <SskStaff key={i} width={w} clef={clef} items={r} o={os[i] || {}} label={labels[i]} extra={extras[i]} pad={pads[i]}/>)}</div>;
}

// the book's tunes, shared with what moves on screen and the Workbook (open and read in two systems on paper)
const SSK_ROWS = {
  open1: [['ts', 4], ['q', 1, 28], ['q', 1, 29], ['q', 1, 30], ['q', 1, 28], ['|']], open2: [['q', 1, 30], ['q', 1, 30], ['h', 2, 32], ['||']],
  shape1: [['ts', 4], ['q', 1, 28], ['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['|'], ['q', 1, 32], ['q', 1, 32], ['q', 1, 31], ['q', 1, 30], ['|']], shape2: [['q', 1, 29], ['q', 1, 29], ['h', 2, 28], ['||']],
  read1: [['ts', 3], ['q', 1, 32], ['q', 1, 33], ['q', 1, 34], ['|'], ['h', 2, 36], ['q', 1, 34], ['|']], read2: [['q', 1, 35], ['q', 1, 34], ['q', 1, 33], ['|'], ['hd', 3, 32], ['||']],
};
SSK_ROWS.open = [...SSK_ROWS.open1, ...SSK_ROWS.open2];
SSK_ROWS.shape = [...SSK_ROWS.shape1, ...SSK_ROWS.shape2];
SSK_ROWS.read = [...SSK_ROWS.read1, ...SSK_ROWS.read2];
// the tunes to read on screen (page 6): each hand in each position
const SSK_TUNES = [
  { id: 'rc', pos: 'C', hand: 'rh', clef: 'treble', name: () => t('C position, right hand', 'C 자리, 오른손'), items: [['ts', 4], ['q', 1, 28], ['q', 1, 29], ['q', 1, 30], ['q', 1, 28], ['|'], ['q', 1, 30], ['q', 1, 31], ['h', 2, 32], ['|'], ['q', 1, 32], ['q', 1, 31], ['q', 1, 30], ['q', 1, 29], ['|'], ['w', 4, 28], ['||']] },
  { id: 'lc', pos: 'C', hand: 'lh', clef: 'bass', name: () => t('C position, left hand', 'C 자리, 왼손'), items: [['ts', 4], ['q', 1, 21], ['q', 1, 23], ['h', 2, 25], ['|'], ['q', 1, 24], ['q', 1, 23], ['h', 2, 22], ['|'], ['q', 1, 23], ['q', 1, 22], ['h', 2, 21], ['||']] },
  { id: 'rg', pos: 'G', hand: 'rh', clef: 'treble', name: () => t('G position, right hand', 'G 자리, 오른손'), items: SSK_ROWS.read },
  { id: 'lg', pos: 'G', hand: 'lh', clef: 'bass', name: () => t('G position, left hand', 'G 자리, 왼손'), items: [['ts', 4], ['q', 1, 18], ['q', 1, 19], ['q', 1, 20], ['q', 1, 18], ['|'], ['h', 2, 20], ['h', 2, 22], ['|'], ['q', 1, 21], ['q', 1, 20], ['q', 1, 19], ['q', 1, 20], ['|'], ['w', 4, 18], ['||']] },
];
// a tune's notes, in order (the quaver pair as two)
const sskNotesOf = (items) => items.flatMap(it => it[0] === 'p' ? it[2].map(d => ({ d, b: 0.5 })) : (it.length > 2 && !sskIsRest(it[0]) ? [{ d: it[2], b: it[1] }] : []));
const sskFingerOf = (pos, hand, d) => { const P = SSK_POS[pos][hand], i = P.indexOf(d); return i < 0 ? null : hand === 'rh' ? i + 1 : 5 - i; };

function sskLbPages(scr = false) {
  const ch = 'reading-steps';
  const live = (still, comp) => <LbLive still={still} live={<>{still}{comp}</>}/>;   // on screen: the picture, then what moves
  const pic = (node, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div></LbPic>;
  const nb = (x) => x.replace(/ /g, ' ');
  const RHC = t('Right hand, thumb on middle C', '오른손 엄지를 가운데 도에 두고');

  const p1 = <SskSystems rows={[SSK_ROWS.open1, SSK_ROWS.open2]} gap={4} os={[{ D: 40, moves: 'bracket', moveOn: [true, false, true] }, { D: 40, moves: 'bracket', moveOn: [true, false] }]}
    labels={[t('Bar 1 of a tune in 4/4 in the treble clef: C D E C. Coral brackets over the notes: C to D, a step; E down to C, a skip.', '높은음자리표, 4/4 선율의 1마디: C D E C. 음표 위의 산호색 괄호: C에서 D는 한 걸음, E에서 C로 내려가는 건너뛰기.'),
      t('Bar 2: E E and a minim G. A coral bracket over E to E: the same note.', '2마디: E E와 2분음표 G. E에서 E 위의 산호색 괄호: 같은 음.')]}/>;
  const p2 = <SskSystems rows={[SSK_ROWS.shape1, SSK_ROWS.shape2]} gap={6} os={[{ D: 32, moves: 'arrow', contour: true }, { D: 32, moves: 'arrow', contour: true, moveIn: -1 }]}
    labels={[t('Bars 1 and 2 of a tune in 4/4: C D E F, G G F E. A dashed coral line joins the note heads, and a coral arrow over each move shows its way: up, up, up, up, the same, down, down.', '4/4 선율의 1~2마디: C D E F, G G F E. 산호색 점선이 음표 머리를 잇고, 움직임마다 산호색 화살표: 위로, 위로, 위로, 위로, 같은 음, 아래로, 아래로.'),
      t('Bar 3: D D and a minim C. An arrow before the first D: down from E. Then the same, down.', '3마디: D D와 2분음표 C. 첫 D 앞의 화살표: E에서 아래로. 그다음 같은 음, 아래로.')]}/>;
  const p3 = [[30, 31], [30, 32]].map(([a, b]) => <SskStepPic key={b} a={a} b={b} label={b - a === 1
    ? t('A step: E on line 1 goes to F in space 1. Under the staff, E and F are white keys side by side, F in coral.', '한 걸음: 1번 줄의 E에서 1번 칸의 F로. 오선 아래 건반에서 E와 F는 바로 옆 흰 건반, F는 산호색.')
    : t('A skip: E on line 1 goes to G on line 2. Under the staff, the keys E and G, and F between them, jumped over.', '건너뛰기: 1번 줄의 E에서 2번 줄의 G로. 오선 아래 건반에서 E와 G, 그 사이의 F는 건너뛰어요.')}/>);
  const p4 = <SskPosPic pos="C" label={t('C position on the grand staff over the keyboard. Left hand: C D E F G on the bass staff, fingers 5 4 3 2 1. Right hand: C D E F G from middle C on the treble staff, fingers 1 2 3 4 5. Each note sits over its key.', '건반 위의 큰보표에 C 자리. 왼손: 낮은음자리표 오선의 C D E F G, 손가락 5 4 3 2 1. 오른손: 가운데 도부터 높은음자리표 오선의 C D E F G, 손가락 1 2 3 4 5. 음표마다 자기 건반 바로 위에 있어요.')}/>;
  const p5 = <SskPosPic pos="G" W={22} label={t('G position on the grand staff over the keyboard. Left hand: G on line 1 of the bass staff up to D, fingers 5 4 3 2 1. Right hand: G on line 2 of the treble staff up to D, fingers 1 2 3 4 5.', '건반 위의 큰보표에 G 자리. 왼손: 낮은음자리표 오선 1번 줄의 G부터 D까지, 손가락 5 4 3 2 1. 오른손: 높은음자리표 오선 2번 줄의 G부터 D까지, 손가락 1 2 3 4 5.')}/>;
  const p6 = <SskSystems rows={[SSK_ROWS.read1, SSK_ROWS.read2]} gap={2} os={[{ D: 34, fingers: [1], hl: [0] }, { D: 34 }]} pads={[[44, 26], null]}
    labels={[t('A new tune in 3/4, bars 1 and 2: G A B, then a minim D and B. The first note, G on line 2, is coral, with finger 1 over it.', '3/4의 새 선율, 1~2마디: G A B, 그다음 2분음표 D와 B. 첫 음인 2번 줄의 G는 산호색, 그 위에 1번 손가락.'),
      t('Bars 3 and 4: C B A, then a dotted minim G.', '3~4마디: C B A, 그다음 점2분음표 G.')]}
    extras={[(yOf, txt, m) => <text x={m.notes[0].x - 10} y={yOf(30) + 17} textAnchor="start" fontSize="12" fontWeight="900" fill={BK.coral} style={txt}>{t('the first note: G', '첫 음: G')}</text>]}/>;

  const mini = (heads, extra = '') => { let s = ''; for (let i = 0; i < 5; i++) s += '<line x1="6" x2="86" y1="' + (8 + i * 6) + '" y2="' + (8 + i * 6) + '" stroke="' + PEN_N + '" stroke-width="1.1"/>';
    return [{ k: 'raw', svg: s + heads.map(([x, y, c]) => '<ellipse cx="' + x + '" cy="' + y + '" rx="4.4" ry="3.1" fill="' + (c || PEN_N) + '" transform="rotate(-20 ' + x + ' ' + y + ')"/>').join('') + extra }]; };
  const posIcon = (d0, L) => [{ k: 'raw', svg: sskKeysRaw(4, 5, d0, 5, 13, 30, { letters: false, on: { [d0]: 'pale', [d0 + 1]: 'pale', [d0 + 2]: 'pale', [d0 + 3]: 'pale', [d0 + 4]: 'pale' } }) + '<text x="84" y="28" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="22" font-weight="900" fill="' + PEN_N + '">' + L + '</text>' }];
  const chkArts = {
    dir: [{ k: 'raw', svg: sskArrow(18, 22, 1, PEN_C, 1.2) + sskArrow(46, 22, 0, PEN_C, 1.2) + sskArrow(74, 22, -1, PEN_C, 1.2) }],
    ss: mini([[24, 32], [44, 29], [70, 23, PEN_C]], '<path d="M44 21 L44 15 L70 15 L70 19" fill="none" stroke="' + PEN_C + '" stroke-width="1.6" stroke-linejoin="round"/>'),
    cpos: posIcon(0, 'C'), gpos: posIcon(4, 'G'),
    read: mini([[18, 26, PEN_C], [34, 23], [50, 20], [66, 26]]),
  };
  const checksRows = [
    ['dir', [0, 0, 92, 40], t('I can say if a note goes up, down or stays the same', '음이 위로 가는지, 아래로 가는지, 같은 음인지 말할 수 있어요')],
    ['ss', [0, 0, 92, 40], t('I can see a step or a skip and play it', '한 걸음과 건너뛰기를 보고 칠 수 있어요')],
    ['cpos', [0, 0, 92, 40], t('I can play in C position with each hand', '양손 각각 C 자리에서 칠 수 있어요')],
    ['gpos', [0, 0, 92, 40], t('I can play in G position with each hand', '양손 각각 G 자리에서 칠 수 있어요')],
    ['read', [0, 0, 92, 40], t('I can read a new tune: first note, rhythm, moves, then play', '새 선율을 읽을 수 있어요: 첫 음, 리듬, 움직임, 그리고 연주')],
  ];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Steps & Skips', '차례가기와 건너뛰기')}</div>
      </div></LbOnly>
      {pic(p1, 220, 520)}
      <LbSay size={17.5}>{LANG === 'ko' ? <><b>선율</b>은 위로 가거나, 아래로 가거나, 같은 음에 머물러요. 앞 음에서 얼마나 움직이는지 읽어요: <b>한{'\u00a0'}걸음</b>, <b>건너뛰기</b>, 같은{'\u00a0'}음.</>
        : <>A <b>tune</b> goes up, goes down or stays on the same note. Read how far each note moves from the one before: a <b>step</b>, a <b>skip</b> or the same note.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Up, down or the same', '위로, 아래로, 같은 음'), 2], [t('Steps and skips', '한 걸음과 건너뛰기'), 3], [t('C position', 'C 자리'), 4], [t('G position', 'G 자리'), 5], [t('Read a tune', '선율 읽기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, , x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. up, down or the same
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Up, down or the same', '위로, 아래로, 같은 음')}>
      {live(pic(p2, 250, 560), <SskShapePad/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['선율', '음이 하나씩 이어져 만드는 음악. 다른 이름은 멜로디예요.'],
        ['위로', '앞 음보다 높은 음. 오선에서는 위쪽, 건반에서는 오른쪽이에요.'],
        ['아래로', '앞 음보다 낮은 음. 오선에서는 아래쪽, 건반에서는 왼쪽이에요.'],
        ['같은 음', '앞 음을 한 번 더. 같은 줄이나 칸, 같은 건반이에요. 다른 이름은 동음 반복이에요.'],
      ] : [
        ['tune', 'Notes one after another that make music. Its other name is a melody.'],
        ['up', 'Higher than the note before: higher on the staff, to the right on the keys.'],
        ['down', 'Lower than the note before: lower on the staff, to the left on the keys.'],
        ['same note', 'The note before, played again: the same line or space, the same key. Its other name is a repeated note.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{RHC}, 손가락 하나에 건반 하나씩 G까지 올려요. 위의 선율을 {nb('1 2 3 4')}로 세면서 쳐요.</>,
        <>음마다 어디로 가는지 말해요: 위로, 위로, 위로, 위로, 같은 음, 아래로… 그다음 움직임을 말하면서 한 번 더 쳐요.</>,
      ] : [
        <>{RHC}, one finger on each key up to G: play the tune above, counting {nb('1 2 3 4')}.</>,
        <>Say how each note moves: up, up, up, up, the same, down… Then play it again, saying the moves.</>,
      ]}/>
      <LbRemember>{t('Higher on the staff, further right on the keys.', '오선에서 높을수록 건반에서 오른쪽.')}</LbRemember>
    </LbPage>,

    // 3. steps and skips
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Steps and skips', '한 걸음과 건너뛰기')}>
      {live(<LbPic h={250}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:'14px 24px',width:'100%',maxWidth:scr ? 360 : 680,margin:'0 auto'}}>{p3.map((s, i) => <div key={i}>{s}</div>)}</div></LbPic>, <SskStepPad/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['한 걸음', '줄에서 바로 옆 칸으로, 또는 칸에서 바로 옆 줄로 가요: 바로 다음 음이름. C 자리와 G 자리에서는 바로 옆 흰 건반이에요. 다른 이름은 2도예요.'],
        ['건너뛰기', '줄에서 다음 줄로, 또는 칸에서 다음 칸으로 가요: 음이름 하나를 건너뛰어요. C 자리와 G 자리에서는 흰 건반 하나를 건너뛰어요. 다른 이름은 3도예요.'],
      ] : [
        ['step', 'From a line to the next space, or from a space to the next line: the next letter. In C and G position, the next white key. Its other name is a 2nd.'],
        ['skip', 'From a line to the next line, or from a space to the next space: one letter jumped over. In C and G position, jump over one white key. Its other name is a 3rd.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{RHC} C{'\u00a0'}E{'\u00a0'}G를 위로 건너뛰며 쳐요. 그다음 G{'\u00a0'}F{'\u00a0'}E{'\u00a0'}D{'\u00a0'}C를 한{'\u00a0'}걸음씩 내려와요.</>,
        <>왼손 5번{'\u00a0'}손가락을 가운데 도 아래의 C에 두고 C{'\u00a0'}D{'\u00a0'}E를 한{'\u00a0'}걸음씩 올라가요. 그다음 E에서 C로 건너뛰어 내려와요.</>,
      ] : [
        <>Right hand, thumb on middle C: play C E G, skips up. Then G F E D C, steps down.</>,
        <>Left hand, finger 5 on the C below middle C: play C D E, steps up. Then E C, a skip down.</>,
      ]}/>
      <LbRemember>{t('The next white key: a step. Jump one: a skip.', '바로 옆 흰 건반: 한 걸음. 흰 건반 하나 건너: 건너뛰기.')}</LbRemember>
    </LbPage>,

    // 4. C position
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('C position', 'C 자리')}>
      {live(pic(p4, 300, 560), <SskPosPad pos="C"/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['다섯 손가락 자리', '한 걸음씩 이웃한 다섯 음에 손가락을 하나씩 올린 자리.'],
        ['C 자리', 'C\u00a0D\u00a0E\u00a0F\u00a0G에 놓는 다섯 손가락 자리. 오른손: 엄지를 가운데 도에. 왼손: 5번\u00a0손가락을 낮은음자리표 오선 2번 칸의 C에.'],
      ] : [
        ['five-finger position', 'Five fingers on five notes a step apart, one finger for each note.'],
        ['C position', 'The five-finger position on C D E F G. Right hand: thumb on middle C. Left hand: finger 5 on the C below middle C, in space 2 of the bass staff.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 C 자리: C{'\u00a0'}D{'\u00a0'}E{'\u00a0'}F{'\u00a0'}G를 치고 다시 내려와요. 손가락 번호를 말해요: {nb('1 2 3 4 5 4 3 2 1')}.</>,
        <>왼손 C 자리: C{'\u00a0'}D{'\u00a0'}E{'\u00a0'}F{'\u00a0'}G를 치고 다시 내려와요. 손가락 번호를 말해요: {nb('5 4 3 2 1 2 3 4 5')}.</>,
      ] : [
        <>Right hand in C position: play C D E F G and back down, saying the finger numbers: {nb('1 2 3 4 5 4 3 2 1')}.</>,
        <>Left hand in C position: play C D E F G and back down, saying the finger numbers: {nb('5 4 3 2 1 2 3 4 5')}.</>,
      ]}/>
      <LbRemember>{t('In a position, a step is the next finger; a skip jumps one finger.', '자리 안에서 한 걸음은 바로 옆 손가락, 건너뛰기는 손가락 하나 건너.')}</LbRemember>
    </LbPage>,

    // 5. G position
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('G position', 'G 자리')}>
      {live(pic(p5, 300, 620), <SskPosPad pos="G"/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['G 자리', 'G\u00a0A\u00a0B\u00a0C\u00a0D에 놓는 다섯 손가락 자리. 오른손: 엄지를 높은음자리표 오선 2번 줄의 G에. 왼손: 5번\u00a0손가락을 낮은음자리표 오선 1번 줄의 G에.'],
      ] : [
        ['G position', 'The five-finger position on G A B C D. Right hand: thumb on G, line 2 of the treble staff. Left hand: finger 5 on G, line 1 of the bass staff.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 G 자리: G{'\u00a0'}A{'\u00a0'}B{'\u00a0'}C{'\u00a0'}D를 치고 다시 내려와요. 음이름을 말해요.</>,
        <>왼손 G 자리: G{'\u00a0'}A{'\u00a0'}B{'\u00a0'}C{'\u00a0'}D를 치고 다시 내려와요. 손가락 번호를 말해요: {nb('5 4 3 2 1 2 3 4 5')}.</>,
        <>오른손 손가락 번호 {nb('1 2 3 1 3 5 3 1')}로 쳐요. C 자리에서 한 번, G 자리에서 한 번.</>,
      ] : [
        <>Right hand in G position: play G A B C D and back down, saying the note names.</>,
        <>Left hand in G position: play G A B C D and back down, saying the finger numbers: {nb('5 4 3 2 1 2 3 4 5')}.</>,
        <>Right hand, play the finger numbers {nb('1 2 3 1 3 5 3 1')}: once in C position, once in G position.</>,
      ]}/>
      <LbRemember>{t('Same fingers, same shape, a new place.', '같은 손가락, 같은 모양, 새 자리.')}</LbRemember>
    </LbPage>,

    // 6. read a tune
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Read a tune', '선율 읽기')}>
      {live(pic(p6, 240, 520), <SskReadPad/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['초견', '처음 보는 악보를 바로 치는 것.'],
      ] : [
        ['sight-reading', 'Playing music you have not seen before.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>첫 음을 찾아요: 2번 줄의 G. 오른손 G 자리, 엄지를 G에.</>,
        <>{nb('1 2 3')}으로 세면서 리듬에 맞춰 손뼉을 쳐요.</>,
        <>움직임을 말해요: 위로 한{'\u00a0'}걸음, 위로 한{'\u00a0'}걸음, 위로 건너뛰기, 아래로 건너뛰기… 그다음 소리 내어 세면서 쳐요.</>,
      ] : [
        <>Find the first note: G, line 2. Right hand in G position, thumb on G.</>,
        <>Clap the rhythm, counting {nb('1 2 3')}.</>,
        <>Say the moves: step up, step up, skip up, skip down… Then play it, counting out loud.</>,
      ]}/>
      <LbRemember>{t('First note, rhythm, moves, then play.', '첫 음, 리듬, 움직임, 그리고 연주.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, vb, x]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_ssk_v1" rows={checksRows.map(([a, vb, x]) => [{ shapes: chkArts[a], vb }, x])}/>}/>
    </LbPage>,
  ];
}
function ReadingStepsLessonBook() { return <>{sskLbPages(false)}</>; }
