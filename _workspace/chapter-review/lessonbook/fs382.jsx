// ─── Chapter 2 -- Lesson Book DRAFT v2 (Phase 385) ───
// Sohyun's re-centre (2026-10-09): the chapter is PATTERN RECOGNITION, not the first song.
// Black-key patterns -> the white keys each group carries (3 + 4) -> the seven letter names ->
// the whole piano and middle C (where the low and high voices meet) -> then play on the patterns.
// High/low folds into the pattern page as a direction line; loud/soft leaves the chapter;
// clefs and the Queen/King wait for the Reading chapter (only the "two voices meet at middle C"
// seed is planted here). Format: Phase 368. Drawings: the Phase 369 pen engine, drawn live.
// ?draft=1 marks the lines that wait for Sohyun's B answers. Not applied to the app yet.
const FS_DRAFT = typeof location !== 'undefined' && /[?&]draft=1/.test(location.search);
function Dft({ children, n }) {
  if (!FS_DRAFT) return <>{children}</>;
  return <span data-draft={n} style={{background:'#fff1a8',borderRadius:3,boxShadow:'0 0 0 3px #fff1a8'}}>{children}</span>;
}

// a keyboard with black keys, in pen (start: 'C' or 'A'; the blacks stay solid navy)
function fsKeysShapes(x, y, nw, W, H, opts = {}) {
  const start = opts.start || 'C', BW = W * 0.62, BH = H * 0.6;
  const off = start === 'C' ? 0 : 5;              // white index of the pattern (C=0 ... A=5)
  const hasBlackAfter = (i) => [0, 1, 3, 4, 5].includes((i + off) % 7);
  const s = [{ k: 'rc', x, y, w: nw * W, h: H, rx: 2, f: PEN_P, s: PEN_N, sw: opts.sw || 2.2 }];
  if (opts.tints) for (let i = 0; i < nw; i++) {
    const m7 = (i + off) % 7;                                   // C D E pale coral, F G A B pale navy
    s.push({ k: 'rc', x: x + i * W + 1, y: y + 2, w: W - 2, h: H - 4, rx: 1.5, f: m7 < 3 ? '#fbe9e2' : '#e9eaf4' });
  }
  for (let i = 1; i < nw; i++) s.push(penLine([x + i * W, y], [x + i * W, y + H], 1.2));
  const blacks = [];
  for (let i = 0; i < nw - 1; i++) if (hasBlackAfter(i)) { blacks.push(i); s.push({ k: 'rc', x: x + (i + 1) * W - BW / 2, y, w: BW, h: BH, rx: 1, f: PEN_N, solid: true }); }
  // the houses: groups of consecutive black keys (2 = small, 3 = big, 1 = the lonely one)
  const houses = [];
  const groups = [];
  blacks.forEach(i => { const g = groups[groups.length - 1]; if (g && i === g[g.length - 1] + 1) g.push(i); else groups.push([i]); });
  groups.forEach(g => houses.push({ kind: g.length >= 3 ? 'big' : g.length === 2 ? 'small' : 'lone',
    x1: x + (g[0] + 1) * W - BW / 2 - W * 0.14, x2: x + (g[g.length - 1] + 1) * W + BW / 2 + W * 0.14 }));
  // letter names on the white keys (C-start octaves): C and F in coral
  if (opts.letters) {
    const L7 = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
    for (let i = 0; i < nw; i++) {
      const n = L7[(i + off) % 7], coral = n === 'C' || n === 'F';
      s.push({ ...penText(x + (i + 0.5) * W, y + H - H * 0.07, n, { size: opts.letterSize || W * 0.48, weight: 900, fill: coral ? PEN_C : PEN_N, anchor: 'middle' }) });
    }
  }
  return { shapes: s, houses, BW, BH };
}
// a roof over a house (the big one gets a chimney)
function fsRoof(h, baseY, peak, opts = {}) {
  const mid = (h.x1 + h.x2) / 2, col = opts.coral ? PEN_C : PEN_N;
  const out = [{ k: 'pl', p: [[h.x1, baseY], [mid, baseY - peak], [h.x2, baseY]], s: col, w: opts.w || 2.6 }];
  if (h.kind === 'big' && opts.chimney !== false) {
    const cx = mid + (h.x2 - mid) * 0.52, cy = baseY - peak * (1 - (cx - mid) / (h.x2 - mid)) - 1;
    out.push({ k: 'rc', x: cx - 2.6, y: cy - 8, w: 5.2, h: 9, rx: 0.8, f: PEN_C });
  }
  if (opts.label) out.push({ ...penText(mid, baseY - peak - 5, opts.label, { size: opts.labelSize || 11, weight: 900, fill: col, anchor: 'middle' }), halo: true });
  return out;
}
// a bracket under a group of white keys, with a count
function fsBrace(x1, x2, y, n, coral) {
  const col = coral ? PEN_C : PEN_N, mid = (x1 + x2) / 2;
  return [
    { k: 'pa', seg: [['M', [x1, y]], ['L', [x1, y + 5]], ['L', [x2, y + 5]], ['L', [x2, y]]], f: 'none', s: col, w: 2 },
    { k: 'el', c: [mid, y + 15], rx: 9.5, ry: 9.5, f: col },
    { ...penText(mid, y + 19, String(n), { size: 12.5, weight: 900, fill: '#fffdf7', anchor: 'middle' }) },
  ];
}
// the bear (low end) and the bird (high end), small, in pen
function fsBear(x, y, k = 1) {
  const s = [];
  const E = (cx, cy, rx, ry, f) => ({ k: 'el', c: [x + cx * k, y + cy * k], rx: rx * k, ry: ry * k, f: f || PEN_P, s: PEN_N, w: 1.8 });
  s.push(E(0, 10, 14, 12));
  s.push(E(-7, -8, 4, 4), E(7, -8, 4, 4));
  s.push(E(0, -4, 10, 9.4));
  s.push(E(0, -1, 4.6, 3.6));
  s.push({ k: 'el', c: [x, y - 2.6], rx: 1.4, ry: 1.1, f: PEN_N });
  s.push({ k: 'el', c: [x - 4 * k, y - 7 * k], rx: 1.1, ry: 1.1, f: PEN_N }, { k: 'el', c: [x + 4 * k, y - 7 * k], rx: 1.1, ry: 1.1, f: PEN_N });
  s.push(E(-10, 18, 3.6, 2.6), E(10, 18, 3.6, 2.6));
  return s;
}
function fsBird(x, y, k = 1) {
  const s = [];
  s.push({ k: 'el', c: [x, y], rx: 7 * k, ry: 5.4 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'el', c: [x + 6 * k, y - 4 * k], rx: 3.8 * k, ry: 3.4 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', [x + 9.4 * k, y - 4.6 * k]], ['L', [x + 13 * k, y - 3.6 * k]], ['L', [x + 9.4 * k, y - 2.6 * k]], ['Z']], f: PEN_C });
  s.push({ k: 'el', c: [x + 6.6 * k, y - 5 * k], rx: 0.9 * k, ry: 0.9 * k, f: PEN_N });
  s.push(penCurve([['M', [x - 2 * k, y - 1.5 * k]], ['Q', [x - 7 * k, y - 6 * k], [x - 10 * k, y - 1 * k]]], 1.6, PEN_N));
  s.push(penCurve([['M', [x - 6.6 * k, y + 1.4 * k]], ['L', [x - 11 * k, y + 3.4 * k]], ['M', [x - 6.6 * k, y + 2.8 * k]], ['L', [x - 11 * k, y + 5 * k]]], 1.4, PEN_N));
  s.push({ ...penText(x + 13 * k, y - 10 * k, '♪', { size: 9 * k, weight: 800, fill: PEN_C }), halo: true });
  return s;
}
// a standing child, posed (scaled via penPlace)
function fsKid(who, pose, face = 1) {
  const x = 75;
  const arms = pose === 'point'
    ? [[[x + 4, 66], [x + 15, 56], [x + 26, 48], [x + 31, 45]], [[x - 3, 67], [x - 6, 87], [x - 4, 103]]]
    : [[[x + 4, 66], [x + 8, 86], [x + 7, 103]], [[x - 3, 66], [x - 7, 86], [x - 6, 103]]];
  const J = { hip: [x, 104], neck: [x + 1, 64], head: [x + 2, 49],
    arms, legs: [[[x + 2, 104], [x + 3, 130], [x + 4, 156]], [[x - 2, 104], [x - 3, 130], [x - 4, 156]]] };
  return penKid(J, face, who);
}

// ─── the seven pages ───
function fsLbPages(scr = false) {
  const ch = 'first-steps';
  const P_W = 560;

  // p1: the street of keys with its houses, letters on the doors, the siblings
  const art1 = (() => {
    const s = [penLine([8, 136], [332, 136], 1.6, '#bdb7a6')];
    const K = fsKeysShapes(62, 68, 14, 15.6, 68, { letters: true, letterSize: 8, tints: true });
    s.push(...K.shapes);
    K.houses.forEach((h, i) => s.push(...fsRoof(h, 66, h.kind === 'big' ? 22 : 16, { coral: i === 0 })));
    s.push(...penPlace(fsKid('girl', 'point', 1), 0.58, [75, 156], [34, 136]));
    s.push(...penPlace(fsKid('boy', 'stand', -1), 0.58, [75, 156], [312, 136]));
    return s;
  })();
  // p2: the two patterns, plus the low -> high direction strip (bear and bird)
  const art2 = (() => {
    const s = [];
    const K = fsKeysShapes(17, 44, 7, 38, 92, { sw: 2.6, tints: true });
    s.push(...K.shapes);
    const [sm, bg] = K.houses;
    s.push(...fsRoof(sm, 42, 20, { label: t('small house', '작은 집'), labelSize: 11.5 }));
    s.push(...fsRoof(bg, 42, 26, { label: t('big house', '큰 집'), labelSize: 11.5 }));
    [[sm, '2'], [bg, '3']].forEach(([h, n]) => {
      const mx = (h.x1 + h.x2) / 2;
      s.push({ k: 'el', c: [mx, 148], rx: 9.5, ry: 9.5, f: PEN_C });
      s.push({ ...penText(mx, 152, n, { size: 12.5, weight: 900, fill: '#fffdf7', anchor: 'middle' }) });
    });
    return s;
  })();
  const art2b = (() => {
    const s = [];
    const K = fsKeysShapes(46, 16, 21, 12.2, 44);
    s.push(...K.shapes);
    s.push(...fsBear(22, 44, 0.9));
    s.push(...fsBird(320, 12, 0.95));
    s.push({ k: 'pa', seg: [['M', [60, 76]], ['L', [290, 76]]], f: 'none', s: PEN_C, w: 2 });
    s.push({ k: 'pa', seg: [['M', [284, 72]], ['L', [292, 76]], ['L', [284, 80]], ['Z']], f: PEN_C });
    s.push({ ...penText(62, 88, t('low voices', '낮은 소리'), { size: 9.5, weight: 900, fill: PEN_N }), halo: true });
    s.push({ ...penText(288, 88, t('high voices', '높은 소리'), { size: 9.5, weight: 900, fill: PEN_C, anchor: 'end' }), halo: true });
    return s;
  })();
  // p3: each house carries its white keys -- 3 at the small house, 4 at the big one
  const art3 = (() => {
    const s = [];
    const K = fsKeysShapes(17, 36, 7, 38, 88, { sw: 2.6, tints: true });
    s.push(...K.shapes);
    const [sm, bg] = K.houses;
    s.push(...fsRoof(sm, 34, 18, { label: t('small house', '작은 집'), labelSize: 10.5 }));
    s.push(...fsRoof(bg, 34, 23, { label: t('big house', '큰 집'), labelSize: 10.5 }));
    s.push(...fsBrace(17 + 2, 17 + 3 * 38 - 2, 130, 3, true));
    s.push(...fsBrace(17 + 3 * 38 + 2, 17 + 7 * 38 - 2, 130, 4, false));
    return s;
  })();
  // p4: the seven letter names on the doors (C and F in coral)
  const art4 = (() => {
    const s = [];
    const K = fsKeysShapes(17, 40, 7, 38, 96, { sw: 2.6, letters: true, letterSize: 15, tints: true });
    s.push(...K.shapes);
    const [sm, bg] = K.houses;
    s.push(...fsRoof(sm, 38, 18, { w: 2.2 }));
    s.push(...fsRoof(bg, 38, 23, { w: 2.2 }));
    // the doors: C at the small house's left door, F at the big house's
    s.push(penCurve([['M', [17 + 0.5 * 38, 34]], ['L', [17 + 0.5 * 38, 24]]], 1.4, PEN_C));
    s.push({ ...penText(17 + 0.5 * 38, 19, t('C -- the left door', 'C -- 왼쪽 문'), { size: 9.5, weight: 900, fill: PEN_C, anchor: 'start' }), halo: true });
    s.push(penCurve([['M', [17 + 3.5 * 38, 34]], ['L', [17 + 3.5 * 38, 10]]], 1.4, PEN_C));
    s.push({ ...penText(17 + 3.5 * 38, 7, t('F -- the big house\'s left door', 'F -- 큰 집의 왼쪽 문'), { size: 9.5, weight: 900, fill: PEN_C, anchor: 'start' }), halo: true });
    return s;
  })();
  // p5: the whole piano -- 7+7 houses, the kennel, middle C where the two voices meet
  const art5 = (() => {
    const s = [];
    const X = 24, W = 9.85, H = 64, Y = 56;
    const K = fsKeysShapes(X, Y, 52, W, H, { start: 'A', sw: 2 });
    s.push(...K.shapes);
    let nS = 0;
    K.houses.forEach(h => {
      if (h.kind === 'lone') {
        s.push(...fsRoof({ ...h, kind: 'small' }, 54, 10));
        s.push({ ...penText((h.x1 + h.x2) / 2, 36, t('the kennel', '개집'), { size: 8.5, weight: 900, fill: PEN_C, anchor: 'start' }), halo: true });
        s.push(penCurve([['M', [(h.x1 + h.x2) / 2 + 2, 38]], ['L', [(h.x1 + h.x2) / 2, 46]]], 1.2, PEN_C));
      } else {
        s.push(...fsRoof(h, 54, h.kind === 'small' ? 9 : 12, { w: 1.8, chimney: false }));
        if (h.kind === 'small') { nS++; s.push({ ...penText((h.x1 + h.x2) / 2, 42, String(nS), { size: 8.5, weight: 900, fill: PEN_N, anchor: 'middle' }), halo: true }); }
      }
    });
    const mcX = X + 23 * W;
    s.push({ k: 'rc', x: mcX + 1.2, y: Y + H - 20, w: W - 2.4, h: 17, rx: 1, f: PEN_C });
    s.push(penCurve([['M', [mcX + W / 2, Y + H + 14]], ['L', [mcX + W / 2, Y + H + 3]]], 1.6, PEN_C));
    s.push({ k: 'pa', seg: [['M', [mcX + W / 2 - 3, Y + H + 7]], ['L', [mcX + W / 2, Y + H + 2]], ['L', [mcX + W / 2 + 3, Y + H + 7]], ['Z']], f: PEN_C });
    s.push({ ...penText(mcX + W / 2, Y + H + 24, t('middle C', '가운데 도'), { size: 10, weight: 900, fill: PEN_C, anchor: 'middle' }), halo: true });
    s.push({ ...penText(mcX - 14, Y + H + 15, t('← low voices', '← 낮은 목소리'), { size: 8.5, weight: 800, fill: PEN_N, anchor: 'end' }), halo: true });
    s.push({ ...penText(mcX + W + 14, Y + H + 15, t('high voices →', '높은 목소리 →'), { size: 8.5, weight: 800, fill: PEN_N, anchor: 'start' }), halo: true });
    s.push(...penPlace(fsBear(0, 0, 1), 0.72, [0, 0], [10, 38]));
    s.push(...penPlace(fsBird(0, 0, 1), 0.9, [0, 0], [548, 26]));
    return s;
  })();
  // p6: right hand 2 3 4 on the big house (the play page)
  const art6 = (() => {
    const s = [];
    const K = fsKeysShapes(10, 30, 7, 34, 86, { sw: 2.4, tints: true });
    s.push(...K.shapes);
    const bg = K.houses[1];
    s.push(...fsRoof(bg, 28, 22));
    [3, 4, 5].forEach((wi, i) => {
      const cx = 10 + (wi + 1) * 34;
      s.push({ k: 'el', c: [cx, 44], rx: 8.6, ry: 8.6, f: PEN_C });
      s.push({ ...penText(cx, 47.6, String(i + 2), { size: 11, weight: 900, fill: '#fffdf7', anchor: 'middle' }) });
    });
    return s;
  })();
  // p7 icons
  const chkArts = {
    house: [...fsRoof({ kind: 'small', x1: 10, x2: 34 }, 30, 12), ...fsRoof({ kind: 'big', x1: 44, x2: 80 }, 30, 16), penLine([6, 31], [86, 31], 1.8)],
    brace: [penLine([6, 10], [86, 10], 1.8), ...fsBrace(8, 38, 14, 3, true), ...fsBrace(44, 84, 14, 4, false)],
    letters: 'CDEFGAB'.split('').map((n, i) => ({ ...penText(8 + i * 12.6, 26, n, { size: 11, weight: 900, fill: n === 'C' || n === 'F' ? PEN_C : PEN_N, anchor: 'middle' }) })),
    midc: (() => { const K = fsKeysShapes(6, 6, 7, 11.4, 26, { sw: 1.6 }); return [...K.shapes, { k: 'rc', x: 7, y: 24, w: 9.4, h: 7, rx: 0.8, f: PEN_C }]; })(),
    song: ['4', '3', '2'].map((n, i) => [{ k: 'el', c: [18 + i * 26, 20], rx: 10, ry: 10, f: PEN_P, s: PEN_N, w: 2 }, { ...penText(18 + i * 26, 24.4, n, { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' }) }]).flat(),
  };
  const checksRows = [
    ['house', [0, 0, 92, 40], t('I can find a small house and a big house anywhere', '어디서든 작은 집과 큰 집을 찾을 수 있어요')],
    ['brace', [0, 0, 92, 40], t('I can say each house\'s white keys: 3 and 4', '집마다 딸린 흰건반을 말할 수 있어요: 3개와 4개')],
    ['letters', [0, 0, 92, 40], t('I can name any white key (C at the small house\'s left door)', '어떤 흰건반이든 이름을 댈 수 있어요 (C는 작은 집 왼쪽 문)')],
    ['midc', [0, 0, 92, 40], t('I can find middle C (just left of the 4th small house)', '가운데 도를 찾을 수 있어요 (4번째 작은 집 바로 왼쪽)')],
    ['song', [0, 0, 92, 40], t('I can play Hot Cross Buns legato with 2 3 4', '2 3 4로 핫 크로스 번을 레가토로 칠 수 있어요')],
  ];

  const hcb = ['4', '3', '2', '-', '|', '4', '3', '2', '-', '|', '2', '2', '2', '2', '3', '3', '3', '3', '|', '4', '3', '2', '-'];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Pattern first, names second -- the same order at every age. Older beginners take this chapter in one sitting; younger ones live in the patterns for a while before the names stick. ', '어느 나이든 순서는 같아요: 패턴 먼저, 이름은 그다음. 나이가 있는 학습자는 이 챕터를 한 번에 지나가고, 어린 친구들은 패턴 속에서 한동안 지내다가 이름이 붙어요. ')}<Dft n="B7">{t('No staff yet: the Queen of G and the King of F wait for the Reading chapter -- here we only plant "the low and high voices meet at middle C".', '오선보는 아직이에요: 솔의 여왕과 파의 왕은 악보 읽기 챕터에서 등장해요 -- 여기서는 "낮은 목소리와 높은 목소리가 가운데 도에서 만난다"만 심어 둬요.')}</Dft></>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Keyboard Patterns & Note Names', '건반 패턴과 음이름')}</div>
      </div></LbOnly>
      <LbPic h={225}><div style={{width:'100%'}}><PenArt shapes={art1} vb={[0, 14, 340, 128]} label={t('A keyboard street with roofed black-key houses and letters on the doors; the sister points at a small house', '지붕 얹은 검은건반 집들과 문마다 글자가 있는 건반 거리; 누나가 작은 집을 가리켜요')}/></div></LbPic>
      <LbSay size={17.5}>{t('The piano looks like 88 different keys -- but it is one small pattern, repeated: a small house of 2 black keys that carries 3 white keys, and a big house of 3 black keys that carries 4. Learn the pattern, and every key on the piano tells you its own name.', '피아노는 건반 88개처럼 보이지만, 사실은 작은 패턴 하나가 반복되는 거예요: 흰건반 3개를 거느린 검은건반 2개짜리 작은 집, 그리고 흰건반 4개를 거느린 3개짜리 큰 집. 이 패턴을 알면 피아노의 모든 건반이 자기 이름을 알려 줘요.')}</LbSay>
      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>
          {[[t('Small house, big house', '작은 집, 큰 집'), 2], [t('The white keys of each house', '집마다 딸린 흰건반'), 3], [t('The seven letter names', '일곱 글자 음이름'), 4], [t('The whole piano & middle C', '피아노 전체와 가운데 도'), 5], [t('Play on the patterns', '패턴 위에서 연주'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span>{n}</span><b>{p}</b></div>)}
        </div></LbOnly>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('find any small house or big house', '어떤 작은 집, 큰 집이든 찾을 수 있어요'), t('say which white keys belong to each house', '집마다 어떤 흰건반이 딸려 있는지 말할 수 있어요'), t('name every white key, C to B', '모든 흰건반의 이름을 댈 수 있어요'), t('find middle C on a real piano', '진짜 피아노에서 가운데 도를 찾을 수 있어요'), t('play your first tune on the black keys', '검은건반으로 첫 튠을 칠 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:8,fontSize:14.5,padding:'4px 0'}}><span style={{color:BK.coral,fontWeight:900}}>✓</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><div style={{fontSize:13,color:BK.muted}}>Goes with: the Workbook page beside each lesson page, and the online lesson (scan the code below).</div></LbOnly>
    </LbPage>,

    // 2. small house, big house (+ the low -> high direction)
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Small house, big house', '작은 집, 큰 집')}
      teacher={<>{t('Watch for counting black keys one by one instead of seeing the groups. Say: "Look for the shapes, not the keys -- two together, three together." ', '검은건반을 하나씩 세고 무리를 못 보는지 봐 주세요. 이렇게 말해요: "건반 말고 모양을 봐요 -- 둘이 함께, 셋이 함께." ')}{t('The bear (low end) and the bird (high end) carry the direction; loud/soft stays out of this chapter (her call).', '곰(낮은 쪽)과 새(높은 쪽)가 방향을 맡아요; 크고 작게는 이 챕터에서 뺐어요(소현님 결정).')}</>}>
      <LbPic h={225}><div style={{width:'100%',maxWidth:440,margin:'0 auto'}}><PenArt shapes={art2} vb={[0, 0, 300, 162]} label={t('One octave: a small house over the two black keys, a big house with a chimney over the three', '한 옥타브: 검은건반 두 개 위에 작은 집, 세 개 위에 굴뚝 달린 큰 집')}/></div>
      <div style={{width:'100%',maxWidth:470,margin:'0 auto'}}><PenArt shapes={art2b} vb={[0, 0, 340, 94]} label={t('The street runs from the bear\'s low end to the bird\'s high end', '거리는 곰의 낮은 쪽 끝에서 새의 높은 쪽 끝으로 이어져요')}/></div></LbPic>
      <LbSay>{LANG === 'ko' ? <>검은건반은 집의 <b>지붕</b>이에요. <b>검은건반 2개</b> = 작은 집의 지붕, <b>3개</b> = 큰 집의 지붕. 작은 집, 큰 집, 작은 집, 큰 집... 피아노 끝까지 같은 두 집이 반복돼요. 그리고 거리는 <b>왼쪽(낮은 소리)에서 오른쪽(높은 소리)</b>으로 올라가요.</> : <>The black keys are the <b>roofs</b> of the houses. <b>Two black keys</b> = the small house's roof; <b>three</b> = the big house's. Small, big, small, big... the same two houses repeat all the way up the piano. And the street climbs from <b>left (low sounds) to right (high sounds)</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>피아노 가운데쯤에서 <b>작은 집</b>과 <b>큰 집</b>을 하나씩 찾아요.</>,
        <>맨 아래부터 맨 위까지 올라가며 소리 내어 말해요: "작은 집... 큰 집... 작은 집..."</>,
        <>눈을 감아요. 누가 높거나 낮은 소리를 하나 치면, 그 소리가 사는 쪽을 가리켜요.</>,
      ] : [
        <>Find a <b>small house</b> and a <b>big house</b> near the middle of the piano.</>,
        <>Travel from the very bottom to the very top, saying it out loud: "small house... big house... small house..."</>,
        <>Close your eyes. Someone plays one high or one low sound -- point to the end of the street where it lives.</>,
      ]}/>
      <LbRemember>{t('A 2-key roof = the small house. A 3-key roof = the big one. Low left, high right.', '검은건반 2개 지붕 = 작은 집, 3개 지붕 = 큰 집. 왼쪽은 낮게, 오른쪽은 높게.')}</LbRemember>
    </LbPage>,

    // 3. the white keys of each house
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The white keys of each house', '집마다 딸린 흰건반')}
      teacher={<>{t('This is the chapter\'s key idea: the white keys belong to a house. 3 at the small house, 4 at the big one -- 3 + 4 = 7, then the street repeats. A student who sees this grouping finds every note name (and later every scale fingering) from the pattern, not by counting from the bottom.', '이 챕터의 핵심이에요: 흰건반은 집에 딸려 있어요. 작은 집에 3개, 큰 집에 4개 -- 3 + 4 = 7, 그리고 거리가 반복돼요. 이 묶음이 보이는 학생은 모든 음이름을 (나중에는 스케일 손가락 번호까지) 맨 아래부터 세지 않고 패턴에서 찾아요.')}</>}>
      <LbPic h={235}><div style={{width:'100%',maxWidth:470,margin:'0 auto'}}><PenArt shapes={art3} vb={[0, -10, 300, 172]} label={t('One octave: a bracket under the small house\'s 3 white keys and the big house\'s 4', '한 옥타브: 작은 집의 흰건반 3개와 큰 집의 4개 아래에 묶음 표시')}/></div></LbPic>
      <LbSay>{LANG === 'ko' ? <>흰건반은 아무 데나 있는 게 아니라 <b>어느 지붕 아래</b>에 살아요. 작은 지붕 아래에는 흰건반 <b>3개</b>(왼쪽 문, 집 안, 오른쪽 문), 큰 지붕 아래에는 <b>4개</b>가 살아요. 그림의 연한 색이 누가 어느 집 식구인지 보여 줘요. 3 + 4 = <b>7</b> -- 일곱 개가 지나면 거리가 처음부터 반복돼요.</> : <>A white key is never just anywhere -- each one lives <b>under a roof</b>. Under the small roof live <b>3</b> white keys (left door, inside, right door); under the big roof live <b>4</b>. The faint colours in the picture show who belongs to which house. 3 + 4 = <b>7</b> -- after seven, the street starts again.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>작은 집을 찾아 그 흰건반 <b>3개</b>를 차례로 쳐요: 왼쪽 문, 집 안, 오른쪽 문.</>,
        <>옆의 큰 집에서 흰건반 <b>4개</b>를 차례로 쳐요.</>,
        <>"3개... 4개... 3개... 4개..." 하고 말하면서 피아노 끝까지 올라가요.</>,
      ] : [
        <>Find a small house and play its <b>3</b> white keys in turn: left door, inside, right door.</>,
        <>Move to the big house next door and play its <b>4</b> white keys in turn.</>,
        <>Travel up the whole piano saying "three... four... three... four..."</>,
      ]}/>
      <LbRemember>{t('Every white key lives under a roof: 3 under the small one, 4 under the big.', '흰건반은 모두 지붕 아래 살아요: 작은 지붕에 3개, 큰 지붕에 4개.')}</LbRemember>
    </LbPage>,

    // 4. the seven letter names
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The seven letter names', '일곱 글자 음이름')}
      teacher={<>{t('Anchor C and F at their doors; the rest follow by walking. Watch for "H" (there is none -- after G comes A again) and for counting from A at the bottom. ', 'C와 F를 각자의 문에 닻으로 내려요; 나머지는 걸어가며 따라와요. "H"를 찾거나(없어요 -- G 다음은 다시 A) 맨 아래 A부터 세는 습관을 봐 주세요. ')}<Dft n="B4">{t('Letters only here; 도레미 alongside (Korean mode) is an open choice.', '여기서는 알파벳만; 한국어 모드의 도레미 병기는 아직 열린 선택이에요.')}</Dft></>}>
      <LbPic h={235}><div style={{width:'100%',maxWidth:470,margin:'0 auto'}}><PenArt shapes={art4} vb={[0, 0, 300, 150]} label={t('One octave with its letter names; C at the small house\'s left door and F at the big house\'s, both in coral', '음이름이 적힌 한 옥타브; 작은 집 왼쪽 문의 C와 큰 집 왼쪽 문의 F가 코랄색이에요')}/></div></LbPic>
      <LbSay>{LANG === 'ko' ? <>음악은 글자 <b>일곱 개</b>만 써요: <b>C D E</b>는 작은 집에, <b>F G A B</b>는 큰 집에 살아요. <b>C는 작은 집의 왼쪽 문</b>, <b>F는 큰 집의 왼쪽 문</b> -- 문 두 개만 외우면 나머지는 걸어가며 읽을 수 있어요. G 다음은? 다시 A예요.</> : <>Music uses just <b>seven letters</b>: <b>C D E</b> live at the small house and <b>F G A B</b> at the big one. <b>C is the small house’s left door</b> and <b>F is the big house’s</b> -- learn the two doors, and you can walk to every other name. After G? A again.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>맨 아래부터 맨 위까지, <b>모든 C</b>를 찾아 쳐요 -- 작은 집의 왼쪽 문마다 하나씩이에요.</>,
        <>이제 <b>모든 F</b>를 찾아 쳐요 -- 큰 집의 왼쪽 문이에요.</>,
        <>누가 글자를 하나 말하면(예: D, G, B), 두 집을 보고 그 건반을 찾아 쳐요.</>,
      ] : [
        <>From the bottom to the top, find and play <b>every C</b> -- one at each small house’s left door.</>,
        <>Now find and play <b>every F</b> -- the big house’s left door.</>,
        <>Someone says a letter (D, G, B...); use the two houses to find that key and play it.</>,
      ]}/>
      <LbRemember>{t('C D E at the small house, F G A B at the big -- and after G comes A.', 'C D E는 작은 집에, F G A B는 큰 집에 -- G 다음은 다시 A.')}</LbRemember>
    </LbPage>,

    // 5. the whole piano & middle C
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The whole piano & middle C', '피아노 전체와 가운데 도')}
      teacher={<>{t('Tick each house while counting so none is counted twice. The lonely black key is A♯0/B♭0, the second key from the bottom. ', '세면서 집마다 표시하면 두 번 세지 않아요. 외로운 검은건반은 맨 아래에서 두 번째 건반(A♯0/B♭0)이에요. ')}<Dft n="B5">{t('"Kennel" for the lonely key -- your call.', '외로운 건반의 "개집" -- 선생님이 정해 주세요.')}</Dft></>}>
      <LbPic h={210} pad="14px 8px"><div style={{width:'100%'}}><PenArt shapes={art5} vb={[0, 14, P_W, 140]} label={t('All 88 keys: 7 small and 7 big houses, the kennel, and middle C where the low and high voices meet', '88개 건반 전체: 작은 집 7채와 큰 집 7채, 개집, 그리고 낮은 목소리와 높은 목소리가 만나는 가운데 도')}/></div></LbPic>
      <LbSay>{LANG === 'ko' ? <>진짜 피아노는 건반 <b>88개</b> -- 그래도 작은 집 7채, 큰 집 7채뿐이에요. <b>4번째 작은 집</b>까지 세면 그 왼쪽 문이 <b>가운데 도(middle C)</b>: 왼쪽은 낮은 목소리 나라, 오른쪽은 높은 목소리 나라, 가운데 도는 <b>둘이 만나는 문</b>이에요.</> : <>A real piano has <b>88 keys</b> -- yet still only 7 small houses and 7 big ones. Count to the <b>4th small house</b>: its left door is <b>middle C</b>. To its left live the low voices, to its right the high voices -- middle C is <b>the door where they meet</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>맨 아래부터 <b>작은 집</b>을 세어요: 1... 7까지, 집마다 짚으면서.</>,
        <>맨 아래의 <b>외로운 검은건반</b>을 찾아요 -- 바로 옆이 가장 낮은 건반이에요.</>,
        <><b>가운데 도</b>를 치고, 한 집 아래의 C(더 낮은 목소리)와 한 집 위의 C(더 높은 목소리)도 쳐 봐요.</>,
      ] : [
        <>Count the <b>small houses</b> from the bottom: 1 up to 7, touching each one.</>,
        <>Find the <b>lonely black key</b> at the very bottom -- right beside it is the lowest key of all.</>,
        <>Play <b>middle C</b>; then the C one house lower (a lower voice) and one house higher (a higher one).</>,
      ]}/>
      <LbRemember>{t('Middle C: just left of the 4th small house -- where low and high meet.', '가운데 도: 4번째 작은 집 바로 왼쪽 -- 낮음과 높음이 만나는 곳.')}</LbRemember>
    </LbPage>,

    // 6. play on the patterns
    <LbPage key="6" no={6} chId={ch} kicker={t('Play', '연주')} title={t('Play on the patterns', '패턴 위에서 연주')}
      teacher={<>{t('Fingers 2 3 4 only, in both hands -- 1 and 5 wait for C position. The legato tip: like a relay baton -- hold the key until the next one plays, and the moment it sounds, release the old one. No gap between the two sounds. ', '양손 모두 2 3 4번만 써요 -- 1번과 5번은 C 포지션에서 만나요. 레가토 팁: 릴레이 바통처럼 -- 다음 음을 누를 때까지 손을 떼지 않고, 다음 음이 울리는 순간 잡고 있던 음을 놓아요. 두 소리 사이에 틈이 없게. ')}<Dft n="B6">{t('Echo: 2-3 black keys, straight back; grow to 4-5.', '에코: 검은건반 2-3개를 바로 따라 치고, 쉬워지면 4-5개로.')}</Dft></>}>
      <LbPic h={175}><div style={{flex:'1 1 200px',minWidth:0,maxWidth:300}}><PenArt shapes={art6} vb={[0, 0, 258, 126]} label={t('Right-hand fingers 2, 3 and 4 on the big roof\'s three black keys', '큰 지붕의 검은건반 세 개 위에 오른손 2, 3, 4번 손가락')}/></div><LbFig art="keys-hand-R" h={142}/></LbPic>
      <LbSay>{LANG === 'ko' ? <>이제 지도가 보답할 차례예요. 첫 튠에는 악보가 필요 없어요: <b>검은건반 지붕</b>과 양손의 <b>2, 3, 4번</b> 손가락이면 돼요. <b>꿀처럼 매끄럽게</b>(레가토) -- 바통 터치하듯, 다음 음이 울리는 순간 앞의 손가락이 놓아요.</> : <>Now the map pays you back. Your first tunes need no written notes: just the <b>black-key roofs</b> and fingers <b>2, 3, 4</b> of both hands. Play <b>smooth as honey</b> (legato) -- like a relay baton, the old finger lets go the moment the new note sounds.</>}</LbSay>
      <div style={{zoom:0.85}}><LbTune name="Hot Cross Buns" how={t('right hand 2 3 4 on the big roof; one circle = one steady beat', '오른손 2 3 4를 큰 지붕에; 동그라미 하나 = 일정한 박 하나')} seq={hcb}/></div>
      <div style={{border:'1px solid #ece6d8',borderRadius:12,padding:'7px 12px',fontSize:13.5,lineHeight:1.5,color:BK.ink}}>
        <b style={{fontFamily:LB_SERIF,fontSize:15.5}}>{t('More tunes that live on the black keys', '검은건반에 사는 다른 노래들')}</b> — {t('left hand 2 3 on the small roof, right hand 2 3 4 on the big one:', '왼손 2 3은 작은 지붕에, 오른손 2 3 4는 큰 지붕에:')} <b>Mary Had a Little Lamb</b>{t(' (떴다 떴다 비행기)', ' (떴다 떴다 비행기)')}, <b>Old MacDonald</b>, <b>Merrily We Roll Along</b>, <b>Rain Rain Go Away</b>{LANG === 'ko' ? <>, <b>아리랑</b></> : <>, <b>Arirang</b></>}. {t('All famous, all free to use -- the Workbook and the app carry their finger rows.', '모두 유명하고 저작권 걱정 없는 곡이에요 -- 손가락 번호 악보는 워크북과 앱에 있어요.')}</div>
      <LbPiano steps={LANG === 'ko' ? [
        <>가운데쯤의 큰 지붕에 오른손 <b>2, 3, 4</b>를 올리고, 노래하면서 천천히: <b>4 - 3 - 2...</b></>,
        <>왼손 <b>2, 3</b>을 작은 지붕에 올리고, 두 손을 번갈아 써서 다른 노래도 쳐 봐요.</>,
        <><b>에코:</b> 누가 검은건반 두세 개를 치면 똑같이 바로 따라 쳐요. 그다음 나만의 튠!</>,
      ] : [
        <>Right-hand <b>2, 3, 4</b> on a big roof near the middle; sing and play slowly: <b>4 - 3 - 2...</b></>,
        <>Put left-hand <b>2, 3</b> on the small roof and try the other tunes, hands taking turns.</>,
        <><b>Echo:</b> someone plays two or three black keys; you play them straight back. Then make up your own tune!</>,
      ]}/>
      <LbRemember>{t('Legato: a relay baton -- the old finger lets go as the new note sounds.', '레가토: 릴레이 바통 -- 새 음이 울리는 순간 앞 손가락이 놓아요.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Step 5', '5단계')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Chapter 1\'s five checks still come first, every time at the piano. These five are this chapter\'s own: the student shows you each one on the keyboard; you only correct. All five easy? Do the Chapter check-up in the Workbook.', '1챕터의 다섯 가지 확인은 여전히 피아노 앞에서 늘 먼저예요. 이 다섯 가지는 이 챕터만의 확인이에요: 학생이 건반 위에서 직접 보여 주고, 선생님은 고쳐 주기만 해요. 다 쉬워지면 워크북의 챕터 점검을 해요.')}</>}>
      <LbSay>{t('Show, don\'t tell! Give yourself a star for each check in each lesson.', '말로 말고, 직접 보여 줘요! 레슨마다 확인 하나에 별 하나씩 칠해요.')}</LbSay>
      <div style={{display:'flex',flexDirection:'column',gap:9,flex:'1 1 auto'}}>
        <div style={{display:'grid',gridTemplateColumns:'110px 1fr repeat(6, 34px)',gap:8,alignItems:'end',fontSize:11,fontWeight:800,color:BK.muted,textAlign:'center'}}><span/><span style={{textAlign:'right',paddingRight:6}}>{t('Lesson', '레슨')}</span>{[1, 2, 3, 4, 5, 6].map(n => <span key={n}>{n}</span>)}</div>
        {checksRows.map(([a, vb, txt], i) => (
          <div key={i} style={{display:'grid',gridTemplateColumns:'110px 1fr repeat(6, 34px)',gap:8,alignItems:'center',border:'1px solid #ece6d8',borderRadius:12,padding:'6px 8px',flex:'1 1 auto'}}>
            <div style={{display:'flex',justifyContent:'center'}}><PenArt shapes={chkArts[a]} vb={vb} style={{width:92}}/></div>
            <div style={{fontSize:15,fontWeight:800,color:BK.ink}}>{txt}</div>
            {[1, 2, 3, 4, 5, 6].map(n => <span key={n} style={{width:30,height:30,border:'1.5px solid ' + BK.line,borderRadius:8,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center'}}><BkStarG size={14} fill="#ece6d8"/></span>)}
          </div>))}
      </div>
      <LbRemember>{t('Pattern first, names second -- the keyboard is a map you can read.', '패턴 먼저, 이름은 그다음 -- 건반은 읽을 수 있는 지도예요.')}</LbRemember>
    </LbPage>,
  ];
}
function FirstStepsLessonBook() { return <>{fsLbPages(false)}</>; }
