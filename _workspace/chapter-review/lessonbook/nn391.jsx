// ─── Chapter 3: The Musical Alphabet (was "Note Names") -- Lesson Book DRAFT (Phase 391) ───
// Split agreed with chapter 2 (B3, 2026-10-09): chapter 2 = WHERE the names live (patterns -> houses -> letters ->
// middle C); chapter 3 = naming them FAST: the letter wheel (seven letters round and round, the same letter in every
// octave), forwards up / backwards down, every key's place in its house (doors and insides), skipping a letter, and
// Hot Cross Buns read by letter names. Sharps and flats wait for Tones & Semitones (chapter 6); interval numbers
// (3rd, 5th) wait for Intervals. Same format (Phase 368), same pen engine and inks, straight keyboards, pastel
// membership tints, the turtle (low, under the sea) and the bird (high, up in the sky); middle C is the ground.
// ?draft=1 marks the lines that wait for Sohyun's B answers. Not applied to the app yet.

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
// a straight arrow with a label (the up/forwards and down/backwards lines)
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
// a little door (the doors of a house) and a window (inside), drawn on a white key
function nnDoor(cx, y, w = 12, h = 18, col = PEN_C) {
  return [{ k: 'pa', seg: [['M', [cx - w / 2, y + h]], ['L', [cx - w / 2, y + w / 2]], ['Q', [cx - w / 2, y], [cx, y]], ['Q', [cx + w / 2, y], [cx + w / 2, y + w / 2]], ['L', [cx + w / 2, y + h]], ['Z']], f: '#fffdf7', s: col, w: 1.7, nw: true },
    { k: 'el', c: [cx + w * 0.22, y + h * 0.6], rx: 1.2, ry: 1.2, f: col }];
}
function nnWindow(cx, y, w = 12, col = PEN_N) {
  return [{ k: 'rc', x: cx - w / 2, y, w, h: w, rx: 1.2, f: '#fffdf7', s: col, sw: 1.6 },
    { ...penLine([cx, y], [cx, y + w], 1.1, col), nw: true }, { ...penLine([cx - w / 2, y + w / 2], [cx + w / 2, y + w / 2], 1.1, col), nw: true }];
}

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
  // p2: the wheel (seven letters, round and round) and one octave, C to C = 8
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
  // p3: up = right = forwards (to the bird in the sky); down = left = backwards (to the turtle under the sea)
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
  // p4: every key's place in its house -- doors (C E F B) and insides (D G A)
  const art4 = (() => {
    const s = [];
    const X = 17, Y = 34, W = 38, H = 116;
    const K = fsKeysShapes(X, Y, 7, W, H, { sw: 2.6, tints: true });
    s.push(...K.shapes, ...nnLetters(X, Y, 7, W, H, { size: 15 }));
    const [sm, bg] = K.houses;
    s.push(...fsRoof(sm, 32, 18, { label: t('small house', '작은 집'), labelSize: 10.5 }));
    s.push(...fsRoof(bg, 32, 23, { label: t('big house', '큰 집'), labelSize: 10.5 }));
    const door = [0, 2, 3, 6], iy = Y + H * 0.6 + 4;
    for (let i = 0; i < 7; i++) {
      const cx = X + (i + 0.5) * W;
      s.push(...(door.includes(i) ? nnDoor(cx, iy, 15, 21) : nnWindow(cx, iy + 4, 14)));
    }
    s.push({ ...penText(X + 3.5 * W, Y + H + 18, t('doors: C E F B   ·   inside: D G A', '문: C E F B   ·   집 안: D G A'), { size: 10.5, weight: 900, fill: PEN_N, anchor: 'middle' }), halo: true });
    return s;
  })();
  // p5: skip a letter -- hops over the keys, and the star it draws on the wheel
  const art5 = (() => {
    const s = [];
    // the star: the letters round a ring, joined a skip at a time (A C E G B D F A)
    const cx = 66, cy = 74, R = 50, L = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
    const at = (i) => { const a = -Math.PI / 2 + i * 2 * Math.PI / 7; return [cx + R * Math.cos(a), cy + R * Math.sin(a)]; };
    s.push({ k: 'el', c: [cx, cy], rx: R, ry: R, f: 'none', s: '#cfcbe0', w: 1.4 });
    const order = [2, 4, 6, 1, 3, 5, 0, 2];    // C E G B D F A C
    s.push({ k: 'pl', p: order.map(at), s: PEN_C, w: 1.9 });
    L.forEach((n, i) => { const [x, y] = at(i); s.push({ k: 'el', c: [x, y], rx: 10.5, ry: 10.5, f: n === 'C' ? PEN_C : PEN_P, s: n === 'C' ? PEN_C : PEN_N, w: 1.8 });
      s.push({ ...penText(x, y + 4.6, n, { size: 13, weight: 900, fill: n === 'C' ? '#fffdf7' : PEN_N, anchor: 'middle' }) }); });
    // the keys: C (D) E (F) G (A) B -- skip one white key each hop
    const X = 140, Y = 64, W = 21, H = 76, N = 9;
    const K = fsKeysShapes(X, Y, N, W, H, { sw: 2.2, tints: true });
    s.push(...K.shapes, ...nnLetters(X, Y, N, W, H, { size: 11.5, coralIdx: [0, 2, 4, 6, 8], grey: [1, 3, 5, 7] }));
    [0, 2, 4, 6].forEach(i => s.push(...nnHop(X + (i + 0.5) * W, X + (i + 2.5) * W, Y - 3, 10)));
    s.push({ ...penText(X + 4.5 * W, Y - 36, t('C (D) E (F) G (A) B (C) D', 'C (D) E (F) G (A) B (C) D'), { size: 10.5, weight: 900, fill: PEN_C, anchor: 'middle' }), halo: true });
    s.push({ ...penText(X + 4.5 * W, Y + H + 18, t('a skip jumps over one white key', '건너뛰기: 흰건반 하나를 넘어가요'), { size: 9.5, weight: 800, fill: PEN_N, anchor: 'middle' }), halo: true });
    return s;
  })();
  // p6: right hand 2 3 4 on C D E (the small house's white keys)
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
  // p7 icons
  const chkArts = {
    wheel: [{ ...penText(46, 17, 'C D E →', { size: 13.5, weight: 900, fill: PEN_C, anchor: 'middle' }) }, { ...penText(46, 36, '← C B A', { size: 13.5, weight: 900, fill: PEN_N, anchor: 'middle' }) }],
    glance: (() => { const K = fsKeysShapes(6, 5, 7, 11.4, 30, { sw: 1.6, tints: true }); return [...K.shapes, { k: 'rc', x: 6 + 11.4 + 1.2, y: 23, w: 9, h: 10, rx: 0.8, f: PEN_C }, { ...penText(6 + 1.5 * 11.4, 32, 'D', { size: 7.5, weight: 900, fill: '#fffdf7', anchor: 'middle' }) }]; })(),
    octave: (() => { const K = fsKeysShapes(2, 5, 8, 11, 26, { sw: 1.6 }); return [...K.shapes, { k: 'rc', x: 3, y: 23, w: 9, h: 7, rx: 0.8, f: PEN_C }, { k: 'rc', x: 2 + 7 * 11 + 1, y: 23, w: 9, h: 7, rx: 0.8, f: PEN_C }]; })(),
    skip: [...['C', 'E', 'G'].map((n, i) => ({ ...penText(14 + i * 32, 36, n, { size: 14, weight: 900, fill: PEN_C, anchor: 'middle' }) })), ...nnHop(17, 43, 21, 7), ...nnHop(49, 75, 21, 7)],
    song: ['E', 'D', 'C'].map((n, i) => [{ k: 'el', c: [18 + i * 26, 20], rx: 10, ry: 10, f: PEN_P, s: PEN_N, w: 2 }, { ...penText(18 + i * 26, 24.4, n, { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' }) }]).flat(),
  };
  const checksRows = [
    ['wheel', [0, 0, 92, 40], t('I can say the letters forwards and backwards, from any letter', '어떤 글자에서든 앞으로, 거꾸로 글자를 말할 수 있어요')],
    ['glance', [0, 0, 92, 40], <LbAsk q="B8">{t('I can name any white key at a glance (before you count to two)', '어떤 흰건반이든 보자마자 이름을 댈 수 있어요 (둘 세기 전에)')}</LbAsk>],
    ['octave', [0, 0, 92, 40], t('I can find the same letter in every octave', '모든 옥타브에서 같은 글자를 찾을 수 있어요')],
    ['skip', [0, 0, 92, 40], t('I can skip up and down: C E G B D F A', '건너뛰며 오르내릴 수 있어요: C E G B D F A')],
    ['song', [0, 0, 92, 40], t('I can play Hot Cross Buns from its letters, legato', '핫 크로스 번을 글자를 보고 레가토로 칠 수 있어요')],
  ];
  const hcbL = ['E', 'D', 'C', '-', '|', 'E', 'D', 'C', '-', '|', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', '|', 'E', 'D', 'C', '-'];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Chapter 2 placed the names; this chapter makes them fast. The test is speed without counting: a student who still walks from C to find every key needs more of pages 3 and 4, not more letters. ', '2챕터는 이름의 자리를 잡아 줬고, 이 챕터는 이름을 빠르게 만들어요. 기준은 세지 않고 나오는 속도예요: 아직 건반마다 C부터 걸어가는 학생에게는 글자를 더 주기보다 3, 4쪽을 더 해 주세요. ')}{t('Black keys keep no names yet: sharps and flats arrive with Tones & Semitones.', '검은건반은 아직 이름이 없어요: 샤프와 플랫은 온음과 반음 챕터에서 만나요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}><LbAsk q="B1"><span style={{fontFamily:LB_SERIF}}>{t('The Musical Alphabet', '음악 알파벳')}</span></LbAsk></div>
      </div></LbOnly>
      <LbPic h={225}><div style={{width:'100%'}}><PenArt shapes={art1} vb={[0, 6, 340, 136]} label={t('The letter wheel, a Ferris wheel with seven gondolas A to G, beside a street of keys; the brother points at the wheel', 'A부터 G까지 일곱 칸이 달린 글자 관람차와 건반 거리; 남동생이 관람차를 가리켜요')}/></div></LbPic>
      <LbSay size={17.5}>{t('In Chapter 2 you found where every name lives: C D E at the small house, F G A B at the big one. Now the names come fast -- forwards and backwards, a skip at a time, in every octave -- until any key tells you its name at a glance.', '2챕터에서는 이름들이 어디 사는지 찾았어요: C D E는 작은 집에, F G A B는 큰 집에. 이제는 이름이 빨리 나올 차례예요 -- 앞으로도 거꾸로도, 하나씩 건너뛰면서, 모든 옥타브에서 -- 어떤 건반이든 보자마자 이름이 나올 때까지.')}</LbSay>
      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>
          {[[t('The letter wheel', '글자 관람차'), 2], [t('Forwards up, backwards down', '위로는 앞으로, 아래로는 거꾸로'), 3], [t('Name it at a glance', '보자마자 이름 대기'), 4], [t('Skip a letter', '한 글자 건너뛰기'), 5], [t('Play by letter names', '음이름 보고 연주하기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span>{n}</span><b>{p}</b></div>)}
        </div></LbOnly>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('say the letters forwards and backwards, from any letter', '어떤 글자에서든 앞으로, 거꾸로 글자를 말할 수 있어요'), t('name any white key at a glance', '어떤 흰건반이든 보자마자 이름을 댈 수 있어요'), t('find the same letter in every octave', '모든 옥타브에서 같은 글자를 찾을 수 있어요'), t('skip up and down the keys: C E G B D F A', '건너뛰며 건반을 오르내릴 수 있어요: C E G B D F A'), t('play Hot Cross Buns from its letter names', '음이름을 보고 핫 크로스 번을 칠 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:8,fontSize:14.5,padding:'4px 0'}}><span style={{color:BK.coral,fontWeight:900}}>✓</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><div style={{fontSize:13,color:BK.muted}}>Goes with: the Workbook page beside each lesson page, and the online lesson.</div></LbOnly>
    </LbPage>,

    // 2. the letter wheel
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The letter wheel', '글자 관람차')}
      teacher={<>{t('Start the chain from any letter, not only from A or C: students who only know it from A count up from A every time. Watch for "H". ', '체인은 A나 C에서만이 아니라 아무 글자에서나 시작해요: A부터만 아는 학생은 매번 A부터 세요. "H"가 나오는지 봐 주세요. ')}{t('The word "octave" is planted here as "the same letter, 8 white keys on"; intervals by number wait for their own chapter.', '"옥타브"라는 말은 여기서 "같은 글자, 흰건반 8개 위"로만 심어 둬요; 숫자로 부르는 음정은 음정 챕터에서 만나요.')}</>}>
      <LbLive still={<LbPic h={240}><div style={{width:'100%',maxWidth:600,margin:'0 auto'}}><PenArt shapes={art2} vb={[0, 10, 340, 172]} label={t('The letter wheel with C filled in, and one octave of keys from C to the next C, 8 white keys', 'C가 칠해진 글자 관람차, 그리고 C에서 다음 C까지 흰건반 8개의 한 옥타브')}/></div></LbPic>} live={<NameReveal/>}/>
      <LbSay>{LANG === 'ko' ? <>음악에는 <b>글자 일곱 개</b>만 있어요: A B C D E F G. G 다음엔 관람차가 돌아 다시 <b>A</b>가 와요 -- 요일처럼 돌고 돌아요, H는 없어요. 한 바퀴 돌 때마다 같은 글자가 다시 와요: <LbAsk q="B3">C에서 다음 C까지가 <b>한 옥타브</b> -- 두 C를 모두 세면 흰건반 8개예요. 이름은 같고, 목소리만 더 높아요.</LbAsk></>
        : <>Music uses only <b>seven letters</b>: A B C D E F G. After G, the wheel comes round to <b>A</b> again -- round and round like the days of the week; there is no H. Each time round, the same letter comes back: <LbAsk q="B3">from one C to the next C is <b>an octave</b> -- 8 white keys, counting both Cs. Same name, higher voice.</LbAsk></>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>맨 아래 <b>A</b>부터 맨 위까지 흰건반을 모두 치며 글자를 말해요: A B C D E F G, A B C...</>,
        <><b>가운데 도</b>에서 흰건반 8개를 걸어 올라가 다음 C까지 가요 -- 관람차가 한 바퀴 돌았어요.</>,
        <>누가 아무 글자나 말하면 관람차를 이어 돌려요: "E" -- "F G A B C..."</>,
      ] : [
        <>Start on the lowest <b>A</b> and play every white key to the top, saying the letters: A B C D E F G, A B C...</>,
        <>Play <b>middle C</b>, then walk up 8 white keys to the next C, saying the letters -- the wheel has gone round once.</>,
        <>Someone says any letter; you carry on round the wheel: "E" -- "F G A B C..."</>,
      ]}/>
      <LbRemember>{t('Seven letters, round and round: after G comes A.', '일곱 글자가 돌고 돌아요: G 다음은 A.')}</LbRemember>
    </LbPage>,

    // 3. forwards up, backwards down
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Forwards up, backwards down', '위로는 앞으로, 아래로는 거꾸로')}
      teacher={<>{t('Watch the turn from A back to G going down: students say "H", or restart at the top of the alphabet. Say the backwards chain away from the piano too -- in the car, on the way to school. ', '내려갈 때 A에서 G로 넘어가는 곳을 봐 주세요: "H"라고 하거나 알파벳 처음으로 돌아가요. 거꾸로 체인은 피아노 밖에서도 말해요 -- 차 안에서, 학교 가는 길에. ')}{t('One finger (3) walking is fine here: this page is about the names, not the hand.', '여기서는 손가락 하나(3번)로 걸어도 괜찮아요: 이 쪽은 손이 아니라 이름이 주인공이에요.')}</>}>
      <LbLive still={<LbPic h={225}><div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><PenArt shapes={art3} vb={[0, 2, 340, 146]} label={t('Two octaves of keys: an arrow to the right, up to the bird, reads C D E F G A B C; an arrow to the left, down to the turtle, reads C B A G F E D C', '두 옥타브 건반: 오른쪽 새 쪽 화살표는 C D E F G A B C, 왼쪽 거북이 쪽 화살표는 C B A G F E D C')}/></div></LbPic>} live={<UpDownWalk/>}/>
      <LbSay>{LANG === 'ko' ? <>피아노를 <b>위로</b> -- 오른쪽, 하늘 위 새 쪽으로 -- 올라가면 글자는 <b>앞으로</b> 가요: C D E F G A B C. <b>아래로</b> -- 왼쪽, 바다 아래 거북이 쪽으로 -- 내려가면 관람차가 거꾸로 돌고 글자도 <b>거꾸로</b> 가요: C B A G F E D C. 거꾸로가 어려워요: 앞으로만큼 빨리 나올 때까지 말해 봐요.</>
        : <>Going <b>up</b> the piano -- to the right, towards the bird in the sky -- the letters go <b>forwards</b>: C D E F G A B C. Going <b>down</b> -- to the left, towards the turtle under the sea -- the wheel turns the other way, and the letters go <b>backwards</b>: C B A G F E D C. Backwards is the tricky one: say it until it comes as quickly as forwards.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <><b>가운데 도</b>에서 흰건반을 하나씩 올라가 다음 C까지, 글자를 앞으로 말해요.</>,
        <>다시 가운데 도까지 내려오며 거꾸로 말해요: <b>C B A G F E D C</b>.</>,
        <><b>G</b>에서 아래 G까지 내려가요. A에서 G로 돌아가는 곳을 조심!</>,
      ] : [
        <>From <b>middle C</b>, play up one white key at a time to the next C, saying the letters forwards.</>,
        <>Come back down to middle C, saying them backwards: <b>C B A G F E D C</b>.</>,
        <>Start on <b>G</b> and go down to the G below. Careful where the wheel turns back from A to G!</>,
      ]}/>
      <LbRemember>{t('Up the piano: forwards. Down the piano: backwards.', '피아노 위로는 앞으로, 아래로는 거꾸로.')}</LbRemember>
    </LbPage>,

    // 4. name it at a glance: doors and insides
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Name it at a glance', '보자마자 이름 대기')}
      teacher={<>{t('Doors and insides is a speed tool, not a new fact: the doors (C E F B) each touch a white neighbour with no black key between; the insides (D G A) sit between two black keys. Watch for counting up from C on every key -- ask "Where in the house?" instead. ', '문과 집 안은 새 사실이 아니라 속도를 위한 도구예요: 문(C E F B)은 검은건반 없이 흰건반 이웃과 맞닿아 있고, 집 안(D G A)은 검은건반 두 개 사이에 있어요. 건반마다 C부터 세는지 봐 주세요 -- 대신 "집의 어디야?" 하고 물어요. ')}<LbAsk q="B8">{t('Target: any white key named before you count to two.', '목표: 둘 세기 전에 어떤 흰건반이든 이름 대기.')}</LbAsk></>}>
      <LbLive still={<LbPic h={250}><div style={{width:'100%',maxWidth:540,margin:'0 auto'}}><PenArt shapes={art4} vb={[0, -4, 300, 178]} label={t('One octave under its two roofs: little doors drawn on C, E, F and B, little windows on D, G and A', '두 지붕 아래 한 옥타브: C, E, F, B에는 작은 문, D, G, A에는 작은 창문')}/></div></LbPic>} live={<FindAll/>}/>
      <LbSay>{LANG === 'ko' ? <>매번 C부터 걸어가면 느려요. 대신 그 건반이 <b>집의 어디</b>에 있는지 봐요. <LbAsk q="B4">흰건반은 모두 <b>문</b>이거나 <b>집 안</b>에 살아요: C와 E는 작은 집의 문, D는 집 안. F와 B는 큰 집의 문, G와 A는 집 안 -- G가 왼쪽, A가 오른쪽.</LbAsk></>
        : <>Walking up from C every time is slow. Look at the key’s <b>place in its house</b> instead. <LbAsk q="B4">Every white key is a <b>door</b> or lives <b>inside</b>: C and E are the small house’s doors, and D lives inside. F and B are the big house’s doors, and G and A live inside -- G on the left, A on the right.</LbAsk></>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>피아노의 <b>모든 D</b>를 찾아요: 작은 집마다 집 안에 사는 건반이에요.</>,
        <><b>모든 G와 A</b>를 찾아요: 큰 집 안의 두 건반 -- G가 왼쪽, A가 오른쪽.</>,
        <><b>빨리 대기 게임:</b> 누가 흰건반 하나를 짚으면, 둘 세기 전에 이름을 말해요. 그다음 바꿔서!</>,
      ] : [
        <>Find <b>every D</b> on the piano: the one inside each small house.</>,
        <>Find <b>every G and A</b>: the two inside each big house -- G on the left, A on the right.</>,
        <><b>Fast game:</b> someone touches any white key; name it before they count to two. Then swap!</>,
      ]}/>
      <LbRemember>{t('Don\'t count from C: see the key\'s place in its house.', 'C부터 세지 말고, 집의 어디인지 봐요.')}</LbRemember>
    </LbPage>,

    // 5. skip a letter
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Skip a letter', '한 글자 건너뛰기')}
      teacher={<>{t('Skips are the staff\'s line-to-line and space-to-space, so this page is the bridge to Reading the Staff. Letters only here -- the numbers (3rd, 5th) wait for Intervals. ', '건너뛰기는 오선보에서 줄에서 줄로, 칸에서 칸으로 가는 것이라 이 쪽이 오선보 읽기로 가는 다리예요. 여기서는 글자로만 -- 3도, 5도 같은 숫자는 음정 챕터에서 만나요. ')}{t('The star: C E G B D F A joined round the circle makes a 7-pointed star; the Workbook has the one to draw.', '별: 원 위에서 C E G B D F A를 이으면 꼭짓점 일곱 개짜리 별이 돼요; 워크북에 직접 그리는 쪽이 있어요.')}</>}>
      <LbLive still={<LbPic h={240}><div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><PenArt shapes={art5} vb={[0, 12, 340, 160]} label={t('The seven letters round a circle joined a skip at a time make a star; on the keys, hops from C to E to G to B to D', '원 위의 일곱 글자를 하나씩 건너 이으면 별이 돼요; 건반 위에서는 C에서 E, G, B, D로 깡충')}/></div></LbPic>} live={<LetterChainDrill/>}/>
      <LbSay>{LANG === 'ko' ? <><b>한 걸음</b>은 바로 다음 글자로 가요. <b>건너뛰기</b>는 하나를 넘어가요: C, (D), <b>E</b>, (F), <b>G</b>... 관람차를 건너뛰며 한 바퀴 돌면 -- C E G B D F A, 그리고 다시 C -- 선이 <b>별</b>을 그려요. 피아노에서 건너뛰기는 흰건반 하나를 넘어가는 거예요. <LbAsk q="B5">다음 챕터 오선보에서 건너뛰기를 다시 만나요.</LbAsk></>
        : <>A <b>step</b> goes to the very next letter. A <b>skip</b> jumps over one: C, (D), <b>E</b>, (F), <b>G</b>... Skip all the way round the wheel -- C E G B D F A, and back to C -- and the lines draw a <b>star</b>. On the piano, a skip jumps over one white key. <LbAsk q="B5">You will meet skips again on the staff, in the next chapter.</LbAsk></>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>3번 손가락으로 가운데 도에서 건너뛰며 올라가요: <b>C E G B D F A C</b>. 치는 글자만 말해요.</>,
        <>건너뛰며 내려와요: <b>C A F D B G E C</b>.</>,
        <>누가 글자를 말하면, 한 번 건너뛴 위의 글자를 말해요 (C → E, F → A, A → C).</>,
      ] : [
        <>With finger 3, skip up from middle C: <b>C E G B D F A C</b>. Say only the letters you play.</>,
        <>Skip back down: <b>C A F D B G E C</b>.</>,
        <>Someone says a letter; you say the letter a skip up (C → E, F → A, A → C).</>,
      ]}/>
      <LbRemember>{t('A skip jumps over a friend: C, (D), E.', '건너뛰기는 친구 하나를 넘어가요: C, (D), E.')}</LbRemember>
    </LbPage>,

    // 6. play by letter names
    <LbPage key="6" no={6} chId={ch} kicker={t('Play', '연주')} title={t('Play by letter names', '음이름 보고 연주하기')}
      teacher={<>{t('Same tune, new house: Chapter 2 played it by finger numbers on the black roof; now it is read by letter names on C D E. The legato is still the relay baton. Fingers 2 3 4 only, in both hands -- 1 and 5 wait for C position. ', '같은 노래, 새 집: 2챕터에서는 검은 지붕 위에서 손가락 번호로 쳤고, 이제는 C D E 위에서 음이름을 읽고 쳐요. 레가토는 여전히 릴레이 바통. 양손 모두 2 3 4번만 -- 1번과 5번은 C 포지션에서 만나요. ')}{t('Letter chain out loud: one letter each, turn about, then backwards.', '소리 내어 글자 잇기: 한 글자씩 번갈아, 그다음 거꾸로.')}</>}>
      <LbOnly print><LbPic h={170}><div style={{flex:'1 1 200px',minWidth:0,maxWidth:360}}><PenArt shapes={art6} vb={[0, 0, 258, 126]} label={t('Right-hand fingers 2, 3 and 4 on C, D and E, the small house\'s white keys', '작은 집의 흰건반 C, D, E 위에 오른손 2, 3, 4번 손가락')}/></div><LbFig art="keys-hand-R" h={170}/></LbPic></LbOnly>
      <LbSay>{LANG === 'ko' ? <>지난 챕터에서 핫 크로스 번은 큰 검은 지붕 위에 살았어요. <LbAsk q="B6">이제 <b>작은 집</b>으로 이사해요: 오른손 <b>2 3 4</b>를 <b>C D E</b>에 올리고, 이번에는 손가락 번호가 아니라 <b>글자</b>를 읽어요.</LbAsk> 그다음 왼손으로, 작은 집 하나 아래에서 쳐 봐요.</>
        : <>Last chapter, Hot Cross Buns lived on the big black roof. <LbAsk q="B6">Now it moves into the <b>small house</b>: right-hand <b>2 3 4</b> on <b>C D E</b>, and this time you read the <b>letters</b>, not the finger numbers.</LbAsk> Then try the left hand, one small house lower.</>}</LbSay>
      <div style={{zoom:0.85}}><LbTune name="Hot Cross Buns" how={t('right hand 2 3 4 on C D E; read the letters; one circle = one steady beat', '오른손 2 3 4를 C D E에; 글자를 읽어요; 동그라미 하나 = 일정한 박 하나')} seq={hcbL}/></div>
      <div style={{border:'1px solid #ece6d8',borderRadius:12,padding:'7px 12px',fontSize:13.5,lineHeight:1.5,color:BK.ink}}>
        <b style={{fontFamily:LB_SERIF,fontSize:15.5}}>{t('Spell and play', '단어 치기')}</b> — {t('a word made only of music letters is a tiny tune. Play', '음악 글자로만 된 단어는 작은 노래예요. 쳐 봐요:')} <b>BAG</b>, <b>CAFE</b>, <b>FACE</b>, <b>BEAD</b>, <b>EGG</b>{t(', saying each letter as you play it -- then make up a word of your own.', ' -- 치면서 글자를 하나씩 말하고, 나만의 단어도 만들어 봐요.')}</div>
      <LbPiano steps={LANG === 'ko' ? [
        <>가운데 도 근처의 <b>C D E</b>에 오른손 <b>2, 3, 4</b>. 치면서 글자를 노래해요: <b>E D C...</b></>,
        <>왼손: 작은 집 하나 아래의 C D E에 <b>4, 3, 2</b> -- 같은 글자, 더 낮은 목소리.</>,
        <><b>글자 잇기:</b> 내가 글자 하나, 선생님이 다음 글자 -- 점점 빨리, 그다음 거꾸로!</>,
      ] : [
        <>Right-hand <b>2, 3, 4</b> on <b>C D E</b> near middle C. Sing the letters as you play: <b>E D C...</b></>,
        <>Left hand: <b>4, 3, 2</b> on C D E one small house lower -- the same letters, a lower voice.</>,
        <><b>Letter chain:</b> you say a letter, your teacher says the next -- faster and faster, then backwards!</>,
      ]}/>
      <LbRemember>{t('Read the letter, see its place, play -- no counting from C.', '글자를 읽고, 자리를 보고, 쳐요 -- C부터 세지 않기.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Step 5', '5단계')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Chapter 1\'s five checks still come first at the piano. These five are this chapter\'s own: the student shows each one on the keyboard or says it out loud; you only correct. All five easy? Do the Chapter check-up in the Workbook.', '1챕터의 다섯 가지 확인은 피아노 앞에서 여전히 먼저예요. 이 다섯 가지는 이 챕터만의 확인이에요: 학생이 건반 위에서 보여 주거나 소리 내어 말하고, 선생님은 고쳐 주기만 해요. 다 쉬워지면 워크북의 챕터 점검을 해요.')}</>}>
      <LbSay>{t('Show, don\'t tell! Give yourself a star for each check in each lesson.', '말로 말고, 직접 보여 줘요! 레슨마다 확인 하나에 별 하나씩 칠해요.')}</LbSay>
      <LbLive still={<div style={{display:'flex',flexDirection:'column',gap:9,flex:'1 1 auto'}}>
        <div style={{display:'grid',gridTemplateColumns:'110px 1fr repeat(6, 34px)',gap:8,alignItems:'end',fontSize:11,fontWeight:800,color:BK.muted,textAlign:'center'}}><span/><span style={{textAlign:'right',paddingRight:6}}>{t('Lesson', '레슨')}</span>{[1, 2, 3, 4, 5, 6].map(n => <span key={n}>{n}</span>)}</div>
        {checksRows.map(([a, vb, txt], i) => (
          <div key={i} style={{display:'grid',gridTemplateColumns:'110px 1fr repeat(6, 34px)',gap:8,alignItems:'center',border:'1px solid #ece6d8',borderRadius:12,padding:'6px 8px',flex:'1 1 auto'}}>
            <div style={{display:'flex',justifyContent:'center'}}><PenArt shapes={chkArts[a]} vb={vb} style={{width:92}}/></div>
            <div style={{fontSize:15,fontWeight:800,color:BK.ink}}>{txt}</div>
            {[1, 2, 3, 4, 5, 6].map(n => <span key={n} style={{width:30,height:30,border:'1.5px solid ' + BK.line,borderRadius:8,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center'}}><BkStarG size={14} fill="#ece6d8"/></span>)}
          </div>))}
      </div>} live={<FiveChecks376 storeKey="pb_five_nn_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
      <LbRemember>{t('Seven letters, round and round -- up forwards, down backwards.', '일곱 글자가 돌고 돌아요 -- 위로는 앞으로, 아래로는 거꾸로.')}</LbRemember>
    </LbPage>,
  ];
}
function NoteNamesLessonBook() { return <>{nnLbPages(false)}</>; }
