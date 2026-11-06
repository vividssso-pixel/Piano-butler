// ─── Phases 432-437: chapter 7 (Tones & Semitones) -- the Lesson Book, on paper and on screen ───
// Phase 437 (her 2026-10-12 12:53 '계속 진행하자'; the B answers as recommended in the v2 pack): the picture is the STEP
// the names already say -- a semitone is a HALF STEP (반음 = 반 걸음), the very next key; a tone is a WHOLE STEP (온음 = 온
// 걸음), two half steps, one key in between (her 09:35). Both pairs of names are taught (Australian/British semitone and
// tone, American half step and whole step); chapter 4's letter steps are whole or half. Built on: chapter 2's keyboard
// street (small house, big house), chapter 4's residents (Princess Clara C, her Dog D, the Exit E, the Front door F,
// Grandma G, her Apple garden A, the Back door B), the bird's sky / the turtle's sea, chapter 15's 'the same key, two
// ways', the Book rules. Out of this chapter (B7): double sharps and flats, writing the chromatic scale, E sharp, B sharp,
// F flat, C flat, the tone-and-a-half; the natural and 'a sign lasts until the bar line' are the Accidentals room's (B6).
// AMEB (2026 Manual): Music Craft Prelim -- recognise and write the sharp and flat; Grade 1 -- the sharp, flat and natural
// signs, the concepts enharmonic and chromatic, tones and semitones marked on scales; Theory of Music Grade 1 -- the
// sharp, flat and natural, the positioning of tones and semitones (C, G, F major). Double sharps and flats: Grade 4.

const TN_ACC = { '#': '♯', b: '♭', n: '♮' };
const tnSign = (c) => <span style={{fontFamily:MUSIC_FONT,fontWeight:400,fontSize:'1.5em',lineHeight:0,verticalAlign:c === '#' ? '0.08em' : '-0.04em'}}>{TN_ACC[c] || c}</span>;   // the music font's signs run small: 1.5x; the sharp lifted
// a text of parts for the pen pictures, the signs in the music font: parts = ['C', '#', ' = D', 'b'] (a lone '#', 'b'
// or 'n' is a sign)
function tnText(x, y, parts, o = {}) {
  const esc = (v) => String(v).replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const body = parts.map(p => TN_ACC[p] ? '<tspan style="font-family:' + MUSIC_FONT.replace(/"/g, '') + ';font-weight:400;font-size:1.5em;baseline-shift:' + (p === '#' ? '0.06em' : '-0.04em') + '">' + TN_ACC[p] + '</tspan>' : esc(p)).join('');
  return { k: 'raw', svg: '<text x="' + pFix(x) + '" y="' + pFix(y) + '" text-anchor="' + (o.anchor || 'middle') + '" font-size="' + (o.size || 10) + '" font-weight="' + (o.weight || 900) + '" fill="' + (o.fill || PEN_N) + '" font-family="Inter,sans-serif"' + (o.halo ? ' paint-order="stroke" stroke="#fff" stroke-width="3" stroke-linejoin="round"' : '') + '>' + body + '</text>' };
}
// a footprint: where a step lands (coral = a half step, navy = a whole step)
function tnFoot(cx, cy, k = 1, col = PEN_C) {   // a bare footprint: the ball, the heel, four toes
  const P = (a, b) => [cx + a * k, cy + b * k];
  return [{ k: 'el', c: P(0, -0.6), rx: 2.7 * k, ry: 3.2 * k, f: col, nw: true }, { k: 'el', c: P(0.5, 4.4), rx: 1.9 * k, ry: 2.3 * k, f: col, nw: true },
    ...[[-2.3, -5.3, 0.95], [-0.7, -6.3, 0.85], [0.9, -6.2, 0.75], [2.3, -5.4, 0.65]].map(([a, b, r]) => ({ k: 'el', c: P(a, b), rx: r * k, ry: r * k, f: col, nw: true }))];
}
// Phase 440 (her 2026-10-12 14:52: the arrows above the keys did not catch the eye): a step drawn ON the keyboard -- a
// dotted line from key to key, a dot at each end, and its name on a little plate in the middle; coral a half step, navy a whole
function tnStepLine(x1, x2, y, label, col = PEN_C, o = {}) {
  const y2 = o.y2 != null ? o.y2 : y;
  const s = [{ ...penLine([x1, y], [x2, y2], o.w || 3.2, col, '0.1 4.4'), nw: true }];
  [[x1, y], [x2, y2]].forEach((c, j) => s.push(j && o.ring2 ? { k: 'el', c, rx: 4.2, ry: 4.2, f: '#fff', s: col, w: 2, nw: true } : { k: 'el', c, rx: 4.2, ry: 4.2, f: col, nw: true }));   // ring2: the far end on a coral key
  if (label) { const mx = o.mx != null ? o.mx : (x1 + x2) / 2, my = o.my != null ? o.my : (y + y2) / 2, z = o.size || 10.5;
    if (o.plate) { const lw = rdWidth(label, 900, z, 'Inter, sans-serif') + 12; s.push({ k: 'rc', x: mx - lw / 2, y: my - 8.5, w: lw, h: 17, rx: 8.5, f: '#fff', s: col, sw: 1.4, nw: true }, penText(mx, my + 3.6, label, { size: z, weight: 900, fill: col, anchor: 'middle' })); }
    else s.push({ ...penText(mx, my + (o.ly != null ? o.ly : -9), label, { size: z, weight: 900, fill: col, anchor: 'middle' }), halo: true }); }
  return s;
}
// a heart (draft v1's best friend; kept for the small icons)
function tnHeart(cx, cy, k = 1, col = PEN_C, outline = false) {
  const P = (a, b) => [cx + a * k, cy + b * k];
  return { k: 'pa', seg: [['M', P(0, 5)], ['Q', P(-7.5, -0.5), P(-5, -4.2)], ['Q', P(-2.4, -6.8), P(0, -3)], ['Q', P(2.4, -6.8), P(5, -4.2)], ['Q', P(7.5, -0.5), P(0, 5)], ['Z']], f: outline ? 'none' : col, s: outline ? col : undefined, w: outline ? 1.5 : undefined, nw: true };
}
// the keyboard of chapter 2 with the helpers this chapter needs: white centres, black centres, 'you' marks
function tnKeys(x, y, nw, W, H, o = {}) {
  const K = fsKeysShapes(x, y, nw, W, H, { tints: true, sw: o.sw || 2.4, start: o.start });
  const off = o.start === 'A' ? 5 : 0;
  const wx = (i) => x + (i + 0.5) * W, bx = (i) => x + (i + 1) * W;           // white key i; the black key after white i
  const lower = y + K.BH;                                                    // where the white keys show below the black ones
  const youW = (i) => ({ k: 'rc', x: x + i * W + 3, y: lower + 3, w: W - 6, h: y + H - lower - 6, rx: 2, f: 'none', s: PEN_C, sw: 2.2, nw: true });
  const youB = (i) => ({ k: 'rc', x: bx(i) - K.BW / 2, y, w: K.BW, h: K.BH, rx: 1, f: PEN_C, solid: true, nw: true });
  const letters = (opts = {}) => nnLetters(x, y, nw, W, H, { start: o.start, size: opts.size || W * 0.36, coral: opts.coral, coralIdx: opts.coralIdx });
  return { ...K, off, wx, bx, lower, youW, youB, letters };
}
// the signs drawn on a staff (SfStaff units: a space is 10): a sharp's box and a flat's belly sit on the note's line or space
function tnAcc(kind, x, cy, col = BK.coral) {
  const bar = (yc, x1, x2) => `M${x1} ${yc + 1.7} L${x2} ${yc - 1.7} L${x2} ${yc + 1.1} L${x1} ${yc + 4.5} Z`;
  if (kind === '#') return <g fill={col} stroke={col}>
    <line x1={x - 2.6} x2={x - 2.6} y1={cy - 12.5} y2={cy + 15} strokeWidth="1.4"/><line x1={x + 2.6} x2={x + 2.6} y1={cy - 15} y2={cy + 12.5} strokeWidth="1.4"/>
    <path d={bar(cy - 6.2, x - 6.4, x + 6.4)} strokeWidth="0.3"/><path d={bar(cy + 2.6, x - 6.4, x + 6.4)} strokeWidth="0.3"/></g>;
  if (kind === 'b') return <g fill="none" stroke={col} strokeLinecap="round">
    <line x1={x - 3.2} x2={x - 3.2} y1={cy - 19} y2={cy + 5} strokeWidth="1.5"/>
    <path d={`M${x - 3.2} ${cy - 0.6} Q${x + 0.8} ${cy - 5.4} ${x + 4.4} ${cy - 3.4} Q${x + 7} ${cy - 0.4} ${x - 3.2} ${cy + 5}`} strokeWidth="2.1"/></g>;
  return <g fill={col} stroke={col}>
    <line x1={x - 3.2} x2={x - 3.2} y1={cy - 14} y2={cy + 4.5} strokeWidth="1.4"/><line x1={x + 3.2} x2={x + 3.2} y1={cy - 4.5} y2={cy + 14} strokeWidth="1.4"/>
    <path d={bar(cy - 6.4, x - 3.2, x + 3.2)} strokeWidth="0.3"/><path d={bar(cy + 2.4, x - 3.2, x + 3.2)} strokeWidth="0.3"/></g>;
}

function tnLbPages(scr = false) {
  const ch = 'tones';
  const pic = (art, vb, label, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}><PenArt shapes={art} vb={vb} label={label}/></div></LbPic>;
  const W_ = '#fff';

  // p1: Clara at her C on the keyboard street: two half steps -- to the black key, then on to D -- make one whole step
  const art1 = (() => {   // Phase 440: the steps dotted on the keys -- a stair of two half steps; the whole step a ruler under them
    const K = tnKeys(40, 50, 6, 46, 124, { start: 'A' });
    const s = [...K.shapes, ...K.letters({ size: 15, coral: ['C'] })];
    s.push(K.youW(2), ...sfClara(K.wx(2), 140, 0.9));
    const c = K.wx(2), cs = K.bx(2), d = K.wx(3);
    s.push(...tnFoot(cs, K.lower - 14, 1.35), ...tnFoot(d, K.lower + 13, 1.5, PEN_N));
    s.push(...tnStepLine(c - 6, cs, 98, t('half', '반'), PEN_C, { ly: -10, size: 11.5 }), ...tnStepLine(cs, d, 72, t('half', '반'), PEN_C, { ly: -10, size: 11.5 }));
    s.push(...tnStepLine(c, d, 190, t('a whole step', '온 걸음'), PEN_N, { ly: 18, size: 11.5 }));
    s.push({ ...penLine([104, 228], [124, 228], 3.2, PEN_C, '0.1 4.4'), nw: true }, penText(132, 232, t('a half step = a semitone', '반 걸음 = 반음'), { size: 11, weight: 900, fill: PEN_C }));
    s.push({ ...penLine([104, 246], [124, 246], 3.2, PEN_N, '0.1 4.4'), nw: true }, penText(132, 250, t('a whole step = a tone', '온 걸음 = 온음'), { size: 11, weight: 900, fill: PEN_N }));
    return s;
  })();

  // p2: a half step -- from the Dog's D both land on black keys; from a black key both land on white keys. The closest
  // keys: a dotted line from your key to each, on the keys
  const art2 = (() => {
    const s = [], W = 52, H = 150;
    const a = tnKeys(12, 26, 3, W, H), b = tnKeys(176, 26, 3, W, H);
    s.push(...a.shapes, ...a.letters({ size: 14, coralIdx: [1] }), a.youW(1), ...nnDog(a.wx(1), a.lower + 26, 0.9));
    s.push(...tnFoot(a.bx(0), a.lower - 16, 1.5), ...tnFoot(a.bx(1), a.lower - 16, 1.5));
    const ya = a.lower - 46;
    s.push(...tnStepLine(a.wx(1), a.bx(0), ya, t('half', '반'), PEN_C, { mx: a.bx(0), my: 26 + 22, ly: 0, size: 12 }).map(e => e.k === 'tx' ? { ...e, fill: '#fff', halo: false } : e));
    s.push(...tnStepLine(a.wx(1), a.bx(1), ya, t('half', '반'), PEN_C, { mx: a.bx(1), my: 26 + 22, ly: 0, size: 12 }).map(e => e.k === 'tx' ? { ...e, fill: '#fff', halo: false } : e));
    s.push(...b.shapes, ...b.letters({ size: 14 }), b.youB(0));
    s.push(...tnFoot(b.wx(0), b.lower + 26, 1.6), ...tnFoot(b.wx(1), b.lower + 26, 1.6));
    const yb = b.lower - 14;
    s.push(...tnStepLine(b.bx(0), b.wx(0) - 4, yb, t('half', '반'), PEN_C, { mx: b.wx(0) - 4, my: b.lower + 4, ly: 0, size: 12 }), ...tnStepLine(b.bx(0), b.wx(1) + 4, yb, t('half', '반'), PEN_C, { mx: b.wx(1) + 4, my: b.lower + 4, ly: 0, size: 12 }));
    [[a.wx(1), t('The Dog\'s closest keys', '강아지 D와 제일 가까운 건반'), t('two black keys', '검은건반 둘')], [b.bx(0), t('A black key\'s closest keys', '검은건반과 제일 가까운 건반'), t('two white keys', '흰건반 둘')]].forEach(([cx, l1, l2]) => {
      s.push({ ...penText(cx, 196, l1, { size: 10, weight: 900, fill: PEN_N, anchor: 'middle' }) }, { ...penText(cx, 210, l2, { size: 10.5, weight: 900, fill: PEN_C, anchor: 'middle' }) });
    });
    return s;
  })();

  // p3: a whole step -- C to D over the black key; and black to black over one white key: two half steps (coral, dotted
  // through the keys) make one whole step (navy, dotted along the top of the keys, named)
  const art3 = (() => {
    const K = tnKeys(16, 56, 7, 44, 124);
    const s = [...K.shapes, ...K.letters({ size: 13, coralIdx: [0, 1] })];
    s.push(K.youW(0), K.youW(1), K.youB(3), K.youB(4));
    const two = (x1, xm, x2) => {
      s.push(...tnStepLine(x1, xm, 108, ''), ...tnStepLine(xm, x2, 108, ''));
      s.push(...tnStepLine(x1, x2, 74, t('a whole step', '온 걸음'), PEN_N, { plate: true, size: 10.5 }));
    };
    two(K.wx(0), K.bx(0), K.wx(1));
    two(K.bx(3), K.wx(4), K.bx(4));
    [[(K.wx(0) + K.wx(1)) / 2 + 6, t('C to D:', 'C에서 D:'), t('one black key between', '사이에 검은건반 하나')], [K.wx(4), t('black to black:', '검은건반에서 검은건반:'), t('one white key between', '사이에 흰건반 하나')]].forEach(([cx, l1, l2]) => {
      s.push({ ...penText(cx, 196, l1, { size: 10, weight: 900, fill: PEN_N, anchor: 'middle' }) }, { ...penText(cx, 209, l2, { size: 10, weight: 900, fill: PEN_N, anchor: 'middle' }) });
    });
    return s;
  })();

  // p4: the white half steps -- C to C with who lives there; between the letters a whole step, except E F and B C: a coral
  // dotted line across their line, on the keys, where no black key is
  const art4 = (() => {
    const X = 10, Y = 38, Wk = 40, H = 138;
    const K = tnKeys(X, Y, 8, Wk, H, { sw: 2.6 });
    const s = [...K.shapes, ...K.letters({ size: 15, coralIdx: [2, 3, 6, 7] })];
    const [sm, bg] = K.houses;
    s.push(...fsRoof(sm, 36, 18, { label: t('small house', '작은 집'), labelSize: 10.5 }));
    s.push(...fsRoof(bg, 36, 23, { label: t('big house', '큰 집'), labelSize: 10.5 }));
    const cy = Y + H * 0.6 + 17;
    'CDEFGABC'.split('').forEach((L, i) => s.push(...nnResident(L, K.wx(i), cy, 1)));
    'CDEFGAB'.split('').forEach((L, i) => {
      const half = L === 'E' || L === 'B', bxx = X + (i + 1) * Wk;
      if (half) s.push(...tnStepLine(K.wx(i) - 6, K.wx(i + 1) + 6, Y + 46, t('half', '반'), PEN_C, { plate: true, size: 10.5 }));
      s.push({ ...penText(bxx, Y + H + 15, half ? t('half', '반') : t('whole', '온'), { size: 9, weight: 900, fill: half ? PEN_C : PEN_N, anchor: 'middle' }) });
      s.push(penCurve([['M', [K.wx(i) + 3, Y + H + 3]], ['Q', [bxx, Y + H + 8], [K.wx(i + 1) - 3, Y + H + 3]]], 1.3, half ? PEN_C : '#9a9cc4'));
    });
    return s;
  })();

  // p5: sharp and flat -- C sharp is a half step up from C, D flat a half step down from D: the same black key, both
  // steps dotted on the keys from a plate on C and on D; every black key of both houses named both ways
  const art5 = (() => {
    const K = tnKeys(16, 52, 7, 44, 164);
    const s = [...K.shapes, ...K.letters({ size: 14, coral: ['C', 'D'] })];
    s.push(K.youB(0));
    const pairs = { 0: ['C', 'D'], 1: ['D', 'E'], 3: ['F', 'G'], 4: ['G', 'A'], 5: ['A', 'B'] };
    Object.entries(pairs).forEach(([i, [lo, hi]]) => {
      const cx = K.bx(+i);
      s.push(tnText(cx, 52 + 24, [lo, '#'], { size: 10.5, fill: W_ }), { ...penLine([cx - 6, 52 + 37], [cx + 6, 52 + 37], 1, 'rgba(255,253,247,0.6)'), nw: true }, tnText(cx, 52 + 56, [hi, 'b'], { size: 10.5, fill: W_ }));
    });
    // a V: from C a half step up, from D a half step down -- both dotted lines meet on the same black key
    const top = K.lower - 6, foot = K.lower + 14;
    s.push(...tnStepLine(K.wx(0) - 4, K.bx(0), foot, '', PEN_C, { y2: top, ring2: true }), ...tnStepLine(K.wx(1) + 4, K.bx(0), foot, '', PEN_N, { y2: top, ring2: true }));
    s.push(tnText(K.wx(0) - 4, foot + 19, ['#', ' ', t('up', '위로')], { size: 12, fill: PEN_C, halo: true }), tnText(K.wx(1) + 4, foot + 19, ['b', ' ', t('down', '아래로')], { size: 12, fill: PEN_N, halo: true }));
    return s;
  })();

  // p6: the signs on the staff -- Queensland: F sharp on the top line, C sharp in the third space, B flat on the middle line,
  // E flat on the bottom line; Kingsland: F sharp on the King's F line, E flat in the third space, B flat on the second
  // line, G sharp on the bottom line
  const N6 = [[38, 98, '#', t('F sharp', 'F 샤프'), t('top line', '맨 윗줄')], [35, 172, '#', t('C sharp', 'C 샤프'), t('third space', '셋째 칸')], [34, 246, 'b', t('B flat', 'B 플랫'), t('middle line', '가운데 줄')], [30, 318, 'b', t('E flat', 'E 플랫'), t('bottom line', '맨 아랫줄')]];
  const N6b = [[24, 98, '#', t('F sharp', 'F 샤프'), t('the King\'s F line', '왕의 F 줄')], [23, 172, 'b', t('E flat', 'E 플랫'), t('third space', '셋째 칸')], [20, 246, 'b', t('B flat', 'B 플랫'), t('second line', '둘째 줄')], [18, 318, '#', t('G sharp', 'G 샤프'), t('bottom line', '맨 아랫줄')]];
  const accRow = (clef, list, low, arrow) => <SfStaff clef={clef} width={360} pad={[clef === 'treble' ? 30 : 26, arrow ? 60 : 46]} span={[4, 354]} label={clef === 'treble'
      ? t('Queensland with four notes, each with its sign just before it on the same line or space: F sharp on the top line, C sharp in the third space, B flat on the middle line, E flat on the bottom line', '네 음이 있는 퀸즈랜드, 기호는 각 음 바로 앞 같은 줄이나 칸에: 맨 윗줄의 F 샤프, 셋째 칸의 C 샤프, 가운데 줄의 B 플랫, 맨 아랫줄의 E 플랫')
      : t('Kingsland with four notes and their signs: F sharp on the King\'s F line, E flat in the third space, B flat on the second line, G sharp on the bottom line', '네 음과 기호가 있는 킹스랜드: 왕의 F 줄의 F 샤프, 셋째 칸의 E 플랫, 둘째 줄의 B 플랫, 맨 아랫줄의 G 샤프')}
    notes={list.map(([d, x]) => ({ d, x }))}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      {list.map(([d, x, k]) => <g key={x}>{tnAcc(k, x - 19, yOf(d))}</g>)}
      {list.map(([d, x, k, name, where]) => <g key={'l' + x}>
        <text x={x - 8} y={yOf(low) + 30} fontSize="12" fontWeight="900" fill={BK.coral} textAnchor="middle">{name}</text>
        <text x={x - 8} y={yOf(low) + 43} fontSize="9" fontWeight="900" fill={BK.muted} textAnchor="middle">{where}</text></g>)}
      {arrow && <><path d={`M${246 - 4} ${yOf(low) + 52} Q${282} ${yOf(low) + 64} ${318 - 12} ${yOf(low) + 52}`} fill="none" stroke={BK.coral} strokeWidth="1.4"/>{sfArrowHead(318 - 12, yOf(low) + 52, 1, BK.coral)}</>}
    </g>}/>;
  const p6 = <div style={{display:'flex',flexDirection:'column',gap:6}}>{accRow('treble', N6, 30, false)}{accRow('bass', N6b, 18, false)}</div>;

  // the check page's little pictures
  const mini = (x, o = {}) => { const K = tnKeys(x, 9, 3, 18, 28, { sw: 1.4 }); return { K, s: K.shapes.map(e => ({ ...e, nw: true })) }; };
  const chkArts = {
    semi: (() => { const { K, s } = mini(18); return [...s, K.youW(1), ...tnFoot(K.bx(0), 18, 0.75), ...tnFoot(K.bx(1), 18, 0.75)]; })(),
    tone: (() => { const { K, s } = mini(18); return [...s, K.youW(0), K.youW(1), ...nnHop(K.wx(0), K.wx(1), 8, 3, PEN_N, 1.4)]; })(),
    white: [{ k: 'rc', x: 26, y: 6, w: 20, h: 30, rx: 1, f: '#fbe9e2', s: PEN_N, sw: 1.4, nw: true }, { k: 'rc', x: 46, y: 6, w: 20, h: 30, rx: 1, f: '#e9eaf4', s: PEN_N, sw: 1.4, nw: true }, { k: 'rc', x: 20, y: 6, w: 12, h: 18, rx: 1, f: PEN_N, solid: true, nw: true }, { k: 'rc', x: 60, y: 6, w: 12, h: 18, rx: 1, f: PEN_N, solid: true, nw: true },
      ...nnHop(38, 54, 16, 4, PEN_C, 1.4), tnText(36, 33, ['E'], { size: 9, fill: PEN_C }), tnText(56, 33, ['F'], { size: 9, fill: PEN_C })],
    names: [{ k: 'rc', x: 32, y: 3, w: 28, h: 34, rx: 2, f: PEN_N, solid: true, nw: true }, tnText(46, 17, ['C', '#'], { size: 10, fill: '#fff' }), { ...penLine([40, 21], [52, 21], 1, 'rgba(255,255,255,0.6)'), nw: true }, tnText(46, 33, ['D', 'b'], { size: 10, fill: '#fff' })],
    signs: [tnText(46, 29, ['#', '   ', 'b'], { size: 22, fill: PEN_C })],
  };
  const checksRows = [
    ['semi', [0, 0, 92, 40], t('I can play a half step (a semitone) up and down from any key', '어떤 건반에서든 반 걸음(반음) 위와 아래를 칠 수 있어요')],
    ['tone', [0, 0, 92, 40], t('I can play a whole step (a tone) up and down from any key', '어떤 건반에서든 온 걸음(온음) 위와 아래를 칠 수 있어요')],
    ['white', [0, 0, 92, 40], t('I can show the white half steps: E F and B C', '흰건반의 반 걸음을 보여 줄 수 있어요: E F와 B C')],
    ['names', [0, 0, 92, 40], <>{t('I can name every black key two ways: C', '검은건반마다 이름 두 개를 말할 수 있어요: C')}{tnSign('#')} = D{tnSign('b')}</>],
    ['signs', [0, 0, 92, 40], t('I can read sharps and flats on the staff and play them', '오선의 샤프와 플랫을 읽고 칠 수 있어요')],
  ];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Tones & Semitones', '온음과 반음')}</div>
      </div></LbOnly>
      {pic(art1, [0, 38, 340, 220], t('The keyboard street with Princess Clara at her C: two coral dotted lines on the keys, each a half step -- to the black key, then up again to D, like a stair -- and under the keys a navy dotted line from C to D, a whole step. Below: a half step is a semitone, a whole step is a tone', '클라라 공주가 C에 서 있는 건반 거리: 건반 위의 산호색 점선 둘, 각각 반 걸음 -- 검은건반으로, 그리고 계단처럼 한 번 더 D로 -- 건반 아래 C에서 D까지 남색 점선은 온 걸음. 아래: 반 걸음은 반음, 온 걸음은 온음'), 250, 620)}
      <LbSay size={17.5}>{LANG === 'ko' ? <>이름이 크기를 알려 줘요. <b>반음</b>은 <b>반 걸음</b> -- 바로 옆 건반까지. <b>온음</b>은 <b>온 걸음</b> -- 반 걸음 두 개. 그리고 두 기호가 음을 반 걸음 옮겨요: <b>샤프</b>는 위로, <b>플랫</b>은 아래로.</>
        : <>The names tell you the size. A <b>semitone</b> is a <b>half step</b> -- to the very next key. A <b>tone</b> is a <b>whole step</b> -- two half steps. And two signs move a note a half step: the <b>sharp</b> up, the <b>flat</b> down.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('A half step: a semitone', '반 걸음: 반음'), 2], [t('A whole step: a tone', '온 걸음: 온음'), 3], [t('White half steps', '흰건반의 반 걸음'), 4], [t('Sharp and flat', '샤프와 플랫'), 5], [t('Sharps and flats on the staff', '오선 위의 샤프와 플랫'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('play a half step up and down from any key', '어떤 건반에서든 반 걸음 위와 아래를 칠 수 있어요'), t('play a whole step up and down from any key', '어떤 건반에서든 온 걸음 위와 아래를 칠 수 있어요'), t('show the white half steps: E F and B C', '흰건반의 반 걸음을 보여 줄 수 있어요: E F와 B C'), <>{t('name every black key two ways: C', '검은건반마다 이름 두 개를 말할 수 있어요: C')}{tnSign('#')} = D{tnSign('b')}</>, t('read sharps and flats on the staff and play them', '오선의 샤프와 플랫을 읽고 칠 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkTick(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. a half step: a semitone
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('A half step: a semitone', '반 걸음: 반음')}>
      <LbLive still={pic(art2, [0, 14, 340, 204], t('Two pieces of keyboard. On the left, D -- the Dog -- with a coral dotted line to each black key beside it, its closest keys: a half step up and a half step down both land on black keys. On the right, a black key with a dotted line to the white key on each side: its half steps land on white keys', '건반 두 조각. 왼쪽은 강아지 D, 양옆 검은건반마다 산호색 점선, 제일 가까운 건반: 반 걸음 위도 아래도 검은건반. 오른쪽은 검은건반, 양옆 흰건반마다 점선: 반 걸음은 흰건반에 닿아요'), 300)} live={<TnHalf/>}/>
      <LbSay>{LANG === 'ko' ? <>피아노에서 가장 작은 걸음은 <b>반 걸음</b>이에요: 한 건반에서 <b>바로 옆 건반</b>까지 -- 검은건반이든 흰건반이든, 사이에 아무것도 없는 <b>가장 가까운 이웃</b>이에요. 이 걸음의 이름이 <b>반음</b>이에요. 영어로는 <b>semitone</b>(호주·영국 책)이라고도, <b>half step</b>(미국 책)이라고도 해요 -- 같은 걸음이에요. 반 걸음은 오른쪽, 새가 사는 하늘 쪽으로 올라가기도 하고, 왼쪽, 거북이 사는 바다 쪽으로 내려가기도 해요.</>
        : <>The smallest step on the piano is a <b>half step</b>: from a key to the <b>very next key</b> -- black or white, nothing in between: its <b>nearest neighbour</b>, the closest key there is. Its other name is a <b>semitone</b> (<i>semi</i> means half): Australian and British books say semitone, American books say half step -- the same step. A half step goes up to the right, towards the bird's sky, or down to the left, towards the turtle's sea.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>강아지 D에 손가락을 올려요. 반 걸음 위, 그다음 반 걸음 아래를 쳐요 -- 둘 다 검은건반이에요. 칠 때마다 "반 걸음"이라고 말해요.</>,
        <><b>반 걸음 걷기:</b> 클라라의 C에서 시작해 반 걸음씩 계속 올라가요 -- 검은건반, 흰건반 모두 -- 다음 C까지. 건반 말고 걸음을 세어요: 반 걸음 12개. 이렇게 반 걸음으로만 걷는 게 <b>반음계(크로마틱 스케일)</b>예요.</>,
      ] : [
        <>Put a finger on D, the Dog. Play a half step up, then a half step down -- both black keys. Say "half step" each time.</>,
        <><b>The half-step walk:</b> start on Clara's C and go up a half step, again and again -- every key, black and white -- to the next C. Count the steps, not the keys: 12 half steps. Walking in half steps like this is the <b>chromatic scale</b>.</>,
      ]}/>
      <LbRemember>{t('A semitone is a half step: the very next key, black or white.', '반음은 반 걸음: 바로 옆 건반, 검은건반이든 흰건반이든.')}</LbRemember>
    </LbPage>,

    // 3. a whole step: a tone
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('A whole step: a tone', '온 걸음: 온음')}>
      <LbLive still={pic(art3, [0, 0, 340, 214], t('The keys C to B. From C to D: two half steps, a coral dotted line through the black key between them -- together one navy dotted line along the top of the keys, a whole step. From the big house\'s first black key to its second: two half steps through the white key G -- one navy line, a whole step', 'C부터 B까지의 건반. C에서 D: 사이의 검은건반을 지나는 반 걸음 둘(산호색 점선) -- 합치면 건반 위쪽의 남색 점선 하나, 온 걸음. 큰 집의 첫째 검은건반에서 둘째로: 흰건반 G를 지나는 반 걸음 둘 -- 남색 점선 하나, 온 걸음'), 280)} live={<TnSteps/>}/>
      <LbSay>{LANG === 'ko' ? <>반 걸음 두 개가 <b>온 걸음</b>이에요: 사이에 <b>건반 하나</b>가 끼어 있어요. 이 걸음의 이름이 <b>온음</b>이에요. 영어로는 <b>tone</b>, 미국 책에서는 <b>whole step</b>이라고 해요. C에서 검은건반을 넘어가면 D가 온 걸음 위예요. 검은건반끼리도 돼요: 흰건반 하나를 사이에 둔 두 검은건반도 온 걸음이에요.</>
        : <>Two half steps make a <b>whole step</b>: <b>one key</b> sits in between. Its other name is a <b>tone</b>; American books say whole step. From C, step over the black key: D is a whole step up. Black keys too: two black keys with one white key between them are a whole step apart.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>C에서 온 걸음 위로: 검은건반을 넘어 D를 쳐요. 그다음 D에서 온 걸음 위 E를 쳐요.</>,
        <><b>반 걸음일까 온 걸음일까?</b> 이 짝들을 치고 "반 걸음 -- 반음" 또는 "온 걸음 -- 온음"이라고 말해요: C D, E F, B C, F G -- 그리고 검은건반 짝 둘: 큰 집의 첫째와 둘째 검은건반, 작은 집의 둘째 검은건반과 E.</>,
      ] : [
        <>From C, play a whole step up: step over the black key and play D. Then play a whole step up from D: E.</>,
        <><b>Half or whole?</b> Play each pair and say "half step -- semitone" or "whole step -- tone": C D, E F, B C, F G -- then two black-key pairs: the big house's first and second black keys, and the small house's second black key with E.</>,
      ]}/>
      <LbRemember>{t('A tone is a whole step: two half steps, one key in between.', '온음은 온 걸음: 반 걸음 두 개, 사이에 건반 하나.')}</LbRemember>
    </LbPage>,

    // 4. the white half steps
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('White half steps: E F and B C', '흰건반의 반 걸음: E F와 B C')}>
      <LbLive still={pic(art4, [0, -4, 340, 206], t('One octave, C to C, under the small house and the big house, with who lives on each white key. Under each pair of white neighbours: whole, whole, half, whole, whole, whole, half -- a coral dotted line on the keys from E to F and from B to C, where there is no black key between', 'C부터 C까지 한 옥타브, 작은 집과 큰 집 아래, 흰건반마다 사는 이. 흰건반 이웃마다 아래에: 온, 온, 반, 온, 온, 온, 반 -- 검은건반이 없는 E에서 F, B에서 C로 건반 위 산호색 점선'), 300, 590)} live={<TnWhites/>}/>
      <LbSay>{LANG === 'ko' ? <>흰건반을 글자 하나씩 걸어가며({bkChapterNo('note-names')}챕터의 걸음) 사이를 봐요. 대부분은 사이에 검은건반이 있어요: <b>온 걸음</b>이에요. 그런데 두 군데는 없어요. 작은 집의 <b>출구(E)</b>로 나오면 바로 큰 집의 <b>앞문(F)</b>이고, 큰 집의 <b>뒷문(B)</b>으로 나가면 옆 작은 집의 <b>클라라 공주(C)</b>가 있어요. <b>E F</b>와 <b>B C</b>는 <b>반 걸음</b>밖에 안 돼요.</>
        : <>Walk the white keys letter by letter (Chapter {bkChapterNo('note-names')}'s steps) and look between them. Most letter steps have a black key in between: a <b>whole step</b>. But twice there is none. Walk out of the small house's <b>Exit (E)</b> and you are at the big house's <b>Front door (F)</b>; go out of the big house's <b>Back door (B)</b> and there is <b>Princess Clara (C)</b> at the next small house. <b>E F</b> and <b>B C</b> are only a <b>half step</b> apart.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>피아노의 모든 E와 F, 그다음 모든 B와 C를 찾아요: 사이에 검은건반이 없어요 -- 반 걸음이에요.</>,
        <>C에서 다음 C까지 흰건반으로 올라가며 걸음마다 말해요: 온, 온, <b>반</b>, 온, 온, 온, <b>반</b>. 이 순서가 장조 스케일의 레시피예요 -- 스케일 방에서 이걸로 스케일을 쌓아요.</>,
      ] : [
        <>Find every E and F on the piano, then every B and C: no black key between them -- a half step.</>,
        <>Walk up the white keys from C to the next C, naming each step: whole, whole, <b>half</b>, whole, whole, whole, <b>half</b>. This order is the major scale's recipe -- in the Scales room you build scales with it.</>,
      ]}/>
      <LbRemember>{t('No black key between E F and B C: only a half step.', 'E F, B C 사이엔 검은건반이 없어요: 반 걸음뿐.')}</LbRemember>
    </LbPage>,

    // 5. sharp and flat: one key, two names
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Sharp and flat: one key, two names', '샤프와 플랫: 건반 하나, 이름 둘')}>
      <LbLive still={pic(art5, [0, 30, 340, 196], t('The keys C to B with every black key named two ways: C sharp and D flat, D sharp and E flat, F sharp and G flat, G sharp and A flat, A sharp and B flat. A coral dotted line goes a half step up from C to C sharp, a navy one a half step down from D to D flat -- the same black key', 'C부터 B까지, 검은건반마다 이름 두 개: C 샤프와 D 플랫, D 샤프와 E 플랫, F 샤프와 G 플랫, G 샤프와 A 플랫, A 샤프와 B 플랫. 산호색 점선은 C에서 반 걸음 위 C 샤프로, 남색 점선은 D에서 반 걸음 아래 D 플랫으로 -- 같은 검은건반'), 300)} live={<TnSharpFlat/>}/>
      <LbSay>{LANG === 'ko' ? <><b>샤프 {tnSign('#')}</b>는 음을 <b>반 걸음 위로</b> 옮겨요 -- 오른쪽 바로 옆 건반으로. 그래서 C 바로 오른쪽 검은건반은 <b>C 샤프, C{tnSign('#')}</b>예요. <b>플랫 {tnSign('b')}</b>은 음을 <b>반 걸음 아래로</b> 옮겨요 -- 왼쪽 바로 옆 건반으로. 그래서 같은 검은건반을 D에서 보면 <b>D 플랫, D{tnSign('b')}</b>이에요. 건반 하나, 이름 둘: 클라라의 C에서 반 걸음 위, 강아지의 D에서 반 걸음 아래예요. 그런데 샤프나 플랫이 늘 검은건반인 건 아니에요: E에서 반 걸음 위는 흰건반 F라서, E 샤프는 F와 같은 건반이에요.</>
        : <>The <b>sharp sign {tnSign('#')}</b> moves a note <b>up a half step</b> -- to the very next key on the right. So the black key just right of C is <b>C sharp, C{tnSign('#')}</b>. The <b>flat sign {tnSign('b')}</b> moves a note <b>down a half step</b> -- to the very next key on the left. So the same black key, seen from D, is <b>D flat, D{tnSign('b')}</b>. One key, two names: a half step up from Clara's C, and a half step down from the Dog's D. But a sharp or a flat is not always a black key: a half step up from E is the white key F, so E sharp is the same key as F.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>C를 치고 C{tnSign('#')}를 쳐요 -- 반 걸음 위. D를 치고 D{tnSign('b')}을 쳐요 -- 반 걸음 아래. 같은 검은건반이에요!</>,
        <>검은건반마다 이름 두 개를 말해요: 작은 집 C{tnSign('#')} = D{tnSign('b')}, D{tnSign('#')} = E{tnSign('b')}; 큰 집 F{tnSign('#')} = G{tnSign('b')}, G{tnSign('#')} = A{tnSign('b')}, A{tnSign('#')} = B{tnSign('b')}.</>,
      ] : [
        <>Play C, then C{tnSign('#')} -- a half step up. Play D, then D{tnSign('b')} -- a half step down. The same black key!</>,
        <>Name every black key both ways: the small house C{tnSign('#')} = D{tnSign('b')}, D{tnSign('#')} = E{tnSign('b')}; the big house F{tnSign('#')} = G{tnSign('b')}, G{tnSign('#')} = A{tnSign('b')}, A{tnSign('#')} = B{tnSign('b')}.</>,
      ]}/>
      <LbRemember><>{tnSign('#')}{t(' up a half step, ', '는 반 걸음 위, ')}{tnSign('b')}{t(' down a half step -- to the very next key, black or white.', '은 반 걸음 아래 -- 바로 옆 건반으로, 검은건반이든 흰건반이든.')}</></LbRemember>
    </LbPage>,

    // 6. the signs on the staff
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Sharps and flats on the staff', '오선 위의 샤프와 플랫')}>
      <LbLive still={<LbPic h={330}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{p6}</div></LbPic>} live={<TnStaffPlay/>}/>
      <LbSay>{LANG === 'ko' ? <>오선에서는 기호를 <b>음표 바로 앞</b>, 음표 머리와 <b>같은 줄이나 칸</b>에 써요: 샤프의 작은 상자와 플랫의 동그란 배가 바로 그 줄이나 칸에 앉아요. 읽을 때는 글자 먼저, 기호는 나중에: "F 샤프", "B 플랫". 쓰는 순서는 반대예요: 기호 먼저, 음표는 그 뒤에.</>
        : <>On the staff, the sign goes <b>just before the note</b>, on <b>the same line or space</b> as its head: the sharp's little box and the flat's round belly sit right on that line or space. Say the letter first, then the sign: "F sharp", "B flat". Write them the other way round: the sign first, then the note.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손으로 퀸즈랜드의 네 음을 읽고 쳐요: F{tnSign('#')}, C{tnSign('#')}, B{tnSign('b')}, E{tnSign('b')}.</>,
        <>왼손으로 킹스랜드의 네 음을 읽고 쳐요: F{tnSign('#')}, E{tnSign('b')}, B{tnSign('b')}, G{tnSign('#')}.</>,
      ] : [
        <>Read and play Queensland's four notes with the right hand: F{tnSign('#')}, C{tnSign('#')}, B{tnSign('b')}, E{tnSign('b')}.</>,
        <>Read and play Kingsland's four with the left hand: F{tnSign('#')}, E{tnSign('b')}, B{tnSign('b')}, G{tnSign('#')}.</>,
      ]}/>
      <LbRemember>{t('The sign goes just before the note, on the note\'s own line or space.', '기호는 음표 바로 앞, 그 음의 줄이나 칸에.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, then tick how it is going -- not yet, nearly, or got it! The check-up on paper is in the Workbook.', '피아노 앞에서 하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요! 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_tn_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
    </LbPage>,
  ];
}
function TonesLessonBook() { return <>{tnLbPages(false)}</>; }
