// ─── Phase 432: chapter 7 (Tones & Semitones) Lesson Book -- draft v1 ───
// Built on her standing decisions: her own lesson metaphor -- a semitone is your BEST FRIEND (the very next key,
// nobody in between), a tone is a FRIEND OF A FRIEND (one key in between) -- the keyboard street of chapter 2 (the small
// house and the big house), chapter 3's residents (Princess Clara C, her Dog D, the Exit E, the Front door F, Grandma G,
// her Apple garden A, the Back door B), high = the bird's sky and low = the turtle's sea (chapter 2), chapter 6's 'the
// same key, two ways', the Book rules. The yellow marks (?draft=1) wait for her answers (B codes in the review pack).
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
// a heart: the best friend (coral, filled); a friend of a friend (an outline)
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
  const A = (q, kids) => <LbAsk q={q}>{kids}</LbAsk>;
  const pic = (art, vb, label, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}><PenArt shapes={art} vb={vb} label={label}/></div></LbPic>;
  const W_ = '#fff';

  // p1: Clara at her C on the keyboard street -- her two best friends (a coral heart each: B on her left, the black key on
  // her right) and two friends of a friend (outline hearts: the black key past B, and D)
  const art1 = (() => {
    const K = tnKeys(26, 30, 9, 32, 100, { start: 'A' });
    const s = [...K.shapes, ...K.letters({ size: 13, coral: ['C'] })];
    K.houses.forEach(h => { if (h.kind !== 'lone') s.push(...fsRoof(h, 29, h.kind === 'big' ? 18 : 13, { w: 2.2 })); else s.push({ k: 'pl', p: [[26, 29 - 12], [h.x2, 29]], s: PEN_N, w: 2.2, nw: true }); });   // the big house, cut by the edge
    s.push(K.youW(2), ...sfClara(K.wx(2), 98, 0.7));
    s.push(tnHeart(K.wx(1), 104, 1.35), tnHeart(K.bx(2), 64, 1.25, PEN_C));          // best friends: B, and the black key after C
    s.push(tnHeart(K.bx(0), 64, 1.15, W_, true), tnHeart(K.wx(3), 104, 1.2, PEN_N, true));   // friends of a friend
    s.push(tnHeart(116, 147, 0.95), { ...penText(127, 150.5, t('best friend: a semitone', '베프: 반음'), { size: 9.5, weight: 900, fill: PEN_C }) });
    s.push(tnHeart(116, 161, 0.95, PEN_N, true), { ...penText(127, 164.5, t('friend of a friend: a tone', '친구의 친구: 온음'), { size: 9.5, weight: 900, fill: PEN_N }) });
    return s;
  })();

  // p2: best friends -- the Dog's two are black keys; a black key's two are white keys
  const art2 = (() => {
    const s = [];
    const a = tnKeys(26, 34, 3, 42, 140), b = tnKeys(196, 34, 3, 42, 140);
    s.push(...a.shapes, ...a.letters({ size: 13, coralIdx: [1] }), a.youW(1), ...nnDog(a.wx(1), a.lower + 22, 0.8));
    s.push(tnHeart(a.bx(0), a.lower - 14, 1.3), tnHeart(a.bx(1), a.lower - 14, 1.3));
    s.push(...nnHop(a.wx(1) - 3, a.bx(0) + 2, 30, 7), ...nnHop(a.wx(1) + 3, a.bx(1) - 2, 30, 7));
    s.push(...b.shapes, ...b.letters({ size: 13 }), b.youB(0));
    s.push(tnHeart(b.wx(0), b.lower + 22, 1.5), tnHeart(b.wx(1), b.lower + 22, 1.5));
    s.push(...nnHop(b.bx(0) - 3, b.wx(0) - 2, 30, 7), ...nnHop(b.bx(0) + 3, b.wx(1) + 2, 30, 7));
    [[a.wx(1), t('The Dog\'s best friends:', '강아지 D의 베프:'), t('two black keys', '검은건반 둘')], [b.bx(0), t('A black key\'s best friends:', '검은건반의 베프:'), t('two white keys', '흰건반 둘')]].forEach(([cx, l1, l2]) => {
      s.push({ ...penText(cx, 192, l1, { size: 10, weight: 900, fill: PEN_N, anchor: 'middle' }) }, { ...penText(cx, 205, l2, { size: 10, weight: 900, fill: PEN_C, anchor: 'middle' }) });
    });
    return s;
  })();

  // p3: a friend of a friend -- C to D over the black key; and black to black over one white key; two best-friend hops
  // (hearts) make one tone (the navy arc)
  const art3 = (() => {
    const K = tnKeys(16, 56, 7, 44, 124);
    const s = [...K.shapes, ...K.letters({ size: 13, coralIdx: [0, 1] })];
    s.push(K.youW(0), K.youW(1), K.youB(3), K.youB(4));
    const two = (x1, xm, x2) => {
      s.push(...nnHop(x1 + 2, xm - 2, 52, 8), ...nnHop(xm + 2, x2 - 2, 52, 8), tnHeart((x1 + xm) / 2, 37, 0.95), tnHeart((xm + x2) / 2, 37, 0.95));
      s.push(...nnHop(x1, x2, 28, 9, PEN_N, 1.8), { ...penText((x1 + x2) / 2, 12, t('a tone', '온음'), { size: 11, weight: 900, fill: PEN_N, anchor: 'middle' }), halo: true });
    };
    two(K.wx(0), K.bx(0), K.wx(1));
    two(K.bx(3), K.wx(4), K.bx(4));
    [[(K.wx(0) + K.wx(1)) / 2 + 6, t('C to D:', 'C에서 D:'), t('one black key between', '사이에 검은건반 하나')], [K.wx(4), t('black to black:', '검은건반에서 검은건반:'), t('one white key between', '사이에 흰건반 하나')]].forEach(([cx, l1, l2]) => {
      s.push({ ...penText(cx, 196, l1, { size: 10, weight: 900, fill: PEN_N, anchor: 'middle' }) }, { ...penText(cx, 209, l2, { size: 10, weight: 900, fill: PEN_N, anchor: 'middle' }) });
    });
    return s;
  })();

  // p4: the white best friends -- C to C with who lives there; between the letters a tone, except E F and B C (a heart on
  // their line, where no black key is)
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
      const semi = L === 'E' || L === 'B', bxx = X + (i + 1) * Wk;
      if (semi) s.push(tnHeart(bxx, 52, 1.5));
      s.push({ ...penText(bxx, Y + H + 15, semi ? t('semitone', '반음') : t('tone', '온음'), { size: semi ? 8.4 : 8.6, weight: 900, fill: semi ? PEN_C : PEN_N, anchor: 'middle' }) });
      s.push(penCurve([['M', [K.wx(i) + 3, Y + H + 3]], ['Q', [bxx, Y + H + 8], [K.wx(i + 1) - 3, Y + H + 3]]], 1.3, semi ? PEN_C : '#9a9cc4'));
    });
    return s;
  })();

  // p5: sharp and flat -- C sharp is C's best friend up, D flat is D's best friend down: the same black key; every black
  // key of the small and the big house named both ways
  const art5 = (() => {
    const K = tnKeys(16, 52, 7, 44, 140);
    const s = [...K.shapes, ...K.letters({ size: 14, coral: ['C', 'D'] })];
    s.push(K.youW(0), K.youW(1), K.youB(0));
    const pairs = { 0: ['C', 'D'], 1: ['D', 'E'], 3: ['F', 'G'], 4: ['G', 'A'], 5: ['A', 'B'] };
    Object.entries(pairs).forEach(([i, [lo, hi]]) => {
      const cx = K.bx(+i);
      s.push(tnText(cx, 52 + 24, [lo, '#'], { size: 10.5, fill: W_ }), { ...penLine([cx - 6, 52 + 37], [cx + 6, 52 + 37], 1, 'rgba(255,253,247,0.6)'), nw: true }, tnText(cx, 52 + 56, [hi, 'b'], { size: 10.5, fill: W_ }));
    });
    s.push(...nnHop(K.wx(0) + 1, K.bx(0) - 3, 48, 9, PEN_C, 2), ...nnHop(K.wx(1) - 1, K.bx(0) + 3, 48, 9, PEN_N, 2));
    s.push(tnText(K.wx(0) - 6, 22, ['#', ' ', t('up', '위로')], { size: 12, fill: PEN_C, anchor: 'middle', halo: true }), tnText(K.wx(1) + 8, 22, ['b', ' ', t('down', '아래로')], { size: 12, fill: PEN_N, anchor: 'middle', halo: true }));
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
    semi: (() => { const { K, s } = mini(18); return [...s, K.youW(1), tnHeart(K.bx(0), 19, 0.75), tnHeart(K.bx(1), 19, 0.75)]; })(),
    tone: (() => { const { K, s } = mini(18); return [...s, K.youW(0), K.youW(1), ...nnHop(K.wx(0), K.wx(1), 8, 3, PEN_N, 1.4)]; })(),
    white: [{ k: 'rc', x: 26, y: 6, w: 20, h: 30, rx: 1, f: '#fbe9e2', s: PEN_N, sw: 1.4, nw: true }, { k: 'rc', x: 46, y: 6, w: 20, h: 30, rx: 1, f: '#e9eaf4', s: PEN_N, sw: 1.4, nw: true }, { k: 'rc', x: 20, y: 6, w: 12, h: 18, rx: 1, f: PEN_N, solid: true, nw: true }, { k: 'rc', x: 60, y: 6, w: 12, h: 18, rx: 1, f: PEN_N, solid: true, nw: true },
      tnHeart(46, 14, 0.8), tnText(36, 33, ['E'], { size: 9, fill: PEN_C }), tnText(56, 33, ['F'], { size: 9, fill: PEN_C })],
    names: [{ k: 'rc', x: 32, y: 3, w: 28, h: 34, rx: 2, f: PEN_N, solid: true, nw: true }, tnText(46, 17, ['C', '#'], { size: 10, fill: '#fff' }), { ...penLine([40, 21], [52, 21], 1, 'rgba(255,255,255,0.6)'), nw: true }, tnText(46, 33, ['D', 'b'], { size: 10, fill: '#fff' })],
    signs: [tnText(46, 29, ['#', '   ', 'b'], { size: 22, fill: PEN_C })],
  };
  const checksRows = [
    ['semi', [0, 0, 92, 40], t('I can find both best friends of any key: a semitone up and down', '어떤 건반이든 베프 둘을 찾을 수 있어요: 반음 위, 반음 아래')],
    ['tone', [0, 0, 92, 40], t('I can find a friend of a friend: a tone up and down', '친구의 친구를 찾을 수 있어요: 온음 위, 온음 아래')],
    ['white', [0, 0, 92, 40], t('I can show the white best friends: E F and B C', '흰건반 베프를 보여 줄 수 있어요: E F와 B C')],
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
      {pic(art1, [0, 4, 340, 166], t('The keyboard street with Princess Clara at her C: a coral heart on each of her two best friends, B on her left and the black key on her right -- a semitone away; an outline heart on the black key past B and on D -- friends of a friend, a tone away', '클라라 공주가 C에 서 있는 건반 거리: 두 베프에 산호색 하트 -- 왼쪽 B와 오른쪽 검은건반, 반음 거리; B 너머 검은건반과 D에 테두리 하트 -- 친구의 친구, 온음 거리'), 250, 620)}
      <LbSay size={17.5}>{LANG === 'ko' ? <>피아노의 거의 모든 건반에는 {A('B1', '베프')}가 둘 있어요 -- 바로 옆 건반이요. 베프는 <b>{A('B1', '반음')}</b>, 친구의 친구는 <b>{A('B1', '온음')}</b>. 그리고 검은건반에 이름이 생겨요: <b>샤프</b>와 <b>플랫</b>.</>
        : <>Almost every key on the piano has two {A('B1', 'best friends')} -- the keys right next door. A best friend is a <b>{A('B1', 'semitone')}</b>, a friend of a friend is a <b>{A('B1', 'tone')}</b>, and the black keys get their names: <b>sharps</b> and <b>flats</b>.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Best friends: a semitone', '베프: 반음'), 2], [t('A friend of a friend: a tone', '친구의 친구: 온음'), 3], [t('White best friends', '흰건반 베프'), 4], [t('Sharp and flat', '샤프와 플랫'), 5], [t('Sharps and flats on the staff', '오선 위의 샤프와 플랫'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('find both best friends of any key, a semitone up and down', '어떤 건반이든 베프 둘을 찾을 수 있어요: 반음 위, 반음 아래'), t('find a friend of a friend, a tone up and down', '친구의 친구를 찾을 수 있어요: 온음 위, 온음 아래'), t('show the white best friends: E F and B C', '흰건반 베프를 보여 줄 수 있어요: E F와 B C'), <>{t('name every black key two ways: C', '검은건반마다 이름 두 개를 말할 수 있어요: C')}{tnSign('#')} = D{tnSign('b')}</>, t('read sharps and flats on the staff and play them', '오선의 샤프와 플랫을 읽고 칠 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkTick(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. best friends: a semitone
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Best friends: a semitone', '베프: 반음')}>
      <LbLive still={pic(art2, [0, 4, 340, 206], t('Two pieces of keyboard. On the left, D -- the Dog -- with a coral heart on each black key beside it: both its best friends are black keys. On the right, a black key with a coral heart on the white key on each side: both its best friends are white keys', '건반 두 조각. 왼쪽은 강아지 D, 양옆 검은건반마다 산호색 하트: 베프 둘 다 검은건반. 오른쪽은 검은건반, 양옆 흰건반마다 산호색 하트: 베프 둘 다 흰건반'), 300)} live={<BestFriends/>}/>
      <LbSay>{LANG === 'ko' ? <>내 베프는 누구일까요? 나와 <b>가장 가까운</b> 사람이에요. 피아노에서 건반의 베프는 <b>바로 옆 건반</b>이에요 -- 검은건반이든 흰건반이든, 사이에 아무도 없어요. 이 거리가 <b>반음</b>, 피아노에서 가장 작은 걸음이에요. 건반에는 베프가 둘 있어요: 하나는 오른쪽, 새가 사는 하늘 쪽 위로, 하나는 왼쪽, 거북이 사는 바다 쪽 아래로.</>
        : <>Who is your best friend? The one who is <b>closest</b> to you. On the piano, a key's best friend is the <b>very next key</b> -- black or white, with nobody in between. That distance is a <b>semitone</b>, the smallest step on the piano. A key has two best friends: one on the right, up towards the bird's sky, and one on the left, down towards the turtle's sea.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>강아지 D에 손가락을 올려요. 오른쪽 베프, 그다음 왼쪽 베프를 쳐요 -- 둘 다 검은건반이에요. 칠 때마다 "반음"이라고 말해요.</>,
        <>{A('B8', <><b>베프 걷기:</b> 클라라의 C에서 시작해 오른쪽 베프를 계속 쳐요 -- 검은건반, 흰건반 모두 -- 다음 C까지. 건반 말고 걸음을 세어요: 반음 12개.</>)}</>,
      ] : [
        <>Put a finger on D, the Dog. Play its best friend on the right, then the one on the left -- both black keys. Say "semitone" each time.</>,
        <>{A('B8', <><b>The best-friend walk:</b> start on Clara's C and play the best friend on the right, again and again -- every key, black and white -- up to the next C. Count the steps, not the keys: 12 semitones.</>)}</>,
      ]}/>
      <LbRemember>{t('A semitone is your best friend: the very next key, black or white.', '반음은 베프: 바로 옆 건반, 검은건반이든 흰건반이든.')}</LbRemember>
    </LbPage>,

    // 3. a friend of a friend: a tone
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('A friend of a friend: a tone', '친구의 친구: 온음')}>
      <LbLive still={pic(art3, [0, 0, 340, 214], t('The keys C to B. From C to D: two best-friend hops, each with a little heart, over the black key between them -- together one navy arc, a tone. From the big house\'s first black key to its second: two best-friend hops over the white key G -- one arc, a tone', 'C부터 B까지의 건반. C에서 D: 사이의 검은건반을 지나는 베프 걸음 두 번(작은 하트) -- 합치면 남색 아치 하나, 온음. 큰 집의 첫째 검은건반에서 둘째로: 흰건반 G를 지나는 베프 걸음 두 번 -- 아치 하나, 온음'), 280)} live={<StepExplorer/>}/>
      <LbSay>{LANG === 'ko' ? <>친구의 친구는 한 건반 더 멀리 있어요: 사이에 <b>건반이 하나</b> 끼어 있어요. 이 거리가 <b>온음</b> -- 반음 두 개, 베프의 또 다른 베프예요. C에서 검은건반을 건너뛰면 D가 온음 위예요. 검은건반끼리도 돼요: 흰건반 하나를 사이에 둔 두 검은건반도 온음이에요.</>
        : <>A friend of a friend is one key further away: <b>one key</b> sits in between. That distance is a <b>tone</b> -- two semitones, your best friend's other best friend. From C, skip the black key: D is a tone up. It works for black keys too: two black keys with one white key between them are a tone apart.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>C에서 온음 위로: 검은건반을 건너뛰고 D를 쳐요. 그다음 D에서 온음 위 E를 쳐요.</>,
        <><b>온음일까 반음일까?</b> 이 짝들을 치고 "베프 -- 반음" 또는 "친구의 친구 -- 온음"이라고 말해요: C D, E F, B C, F G, G{tnSign('#')} A{tnSign('#')}, D{tnSign('#')} E.</>,
      ] : [
        <>From C, play a tone up: skip the black key and play D. Then play a tone up from D: E.</>,
        <><b>Tone or semitone?</b> Play each pair and say "best friend -- semitone" or "friend of a friend -- tone": C D, E F, B C, F G, G{tnSign('#')} A{tnSign('#')}, D{tnSign('#')} E.</>,
      ]}/>
      <LbRemember>{t('A tone is a friend of a friend: one key in between -- two semitones.', '온음은 친구의 친구: 사이에 건반 하나 -- 반음 두 개.')}</LbRemember>
    </LbPage>,

    // 4. the white best friends
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('White best friends: E F and B C', '흰건반 베프: E F와 B C')}>
      {pic(art4, [0, -4, 340, 206], t('One octave, C to C, under the small house and the big house, with who lives on each white key. Under each pair of white neighbours: tone, tone, semitone, tone, tone, tone, semitone -- a coral heart on the line between E and F and between B and C, where there is no black key', 'C부터 C까지 한 옥타브, 작은 집과 큰 집 아래, 흰건반마다 사는 이. 흰건반 이웃마다 아래에: 온음, 온음, 반음, 온음, 온음, 온음, 반음 -- 검은건반이 없는 E와 F 사이, B와 C 사이 줄에 산호색 하트'), 300, 590)}
      <LbSay>{LANG === 'ko' ? <>흰건반을 글자 하나씩 걸어가며(3챕터의 걸음) 사이를 봐요. 대부분은 사이에 검은건반이 있어요: <b>온음</b>이에요. 그런데 두 군데는 없어요. {A('B3', <>작은 집의 <b>출구(E)</b>로 나오면 바로 큰 집의 <b>앞문(F)</b>이고, 큰 집의 <b>뒷문(B)</b>으로 나가면 옆 작은 집의 <b>클라라 공주(C)</b>가 있어요</>)}. <b>E F</b>와 <b>B C</b>는 베프: <b>반음</b>이에요.</>
        : <>Walk the white keys letter by letter (Chapter 3's steps) and look between them. Most steps have a black key in between: a <b>tone</b>. But twice there is none. {A('B3', <>Walk out of the small house's <b>Exit (E)</b> and you are at the big house's <b>Front door (F)</b>; go out of the big house's <b>Back door (B)</b> and there is <b>Princess Clara (C)</b> at the next small house</>)}. <b>E F</b> and <b>B C</b> are best friends: <b>semitones</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>피아노의 모든 E와 F, 그다음 모든 B와 C를 찾아요: 사이에 검은건반이 없어요 -- 베프예요.</>,
        <>C에서 다음 C까지 흰건반으로 올라가며 걸음마다 말해요: 온음, 온음, <b>반음</b>, 온음, 온음, 온음, <b>반음</b>.</>,
      ] : [
        <>Find every E and F on the piano, then every B and C: no black key between them -- best friends.</>,
        <>Walk up the white keys from C to the next C, naming each step: tone, tone, <b>semitone</b>, tone, tone, tone, <b>semitone</b>.</>,
      ]}/>
      <LbRemember>{t('No black key between E F and B C: best friends, semitones.', 'E F, B C 사이엔 검은건반이 없어요: 베프, 반음.')}</LbRemember>
    </LbPage>,

    // 5. sharp and flat: one key, two names
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Sharp and flat: one key, two names', '샤프와 플랫: 건반 하나, 이름 둘')}>
      <LbLive still={pic(art5, [0, 6, 340, 192], t('The keys C to B with every black key named two ways: C sharp and D flat, D sharp and E flat, F sharp and G flat, G sharp and A flat, A sharp and B flat. A coral arrow goes from C up to C sharp, a navy arrow from D down to D flat -- the same black key', 'C부터 B까지, 검은건반마다 이름 두 개: C 샤프와 D 플랫, D 샤프와 E 플랫, F 샤프와 G 플랫, G 샤프와 A 플랫, A 샤프와 B 플랫. 산호색 화살표는 C에서 위로 C 샤프로, 남색 화살표는 D에서 아래로 D 플랫으로 -- 같은 검은건반'), 300)} live={<SharpFlatMover/>}/>
      <LbSay>{LANG === 'ko' ? <>이제 검은건반에 이름이 생겨요. {A('B5', <><b>샤프 {tnSign('#')}</b>는 음을 <b>반음 위로</b> 옮겨요 -- 오른쪽 베프에게</>)}. 그래서 C 바로 오른쪽 검은건반은 <b>C 샤프, C{tnSign('#')}</b>예요. {A('B5', <><b>플랫 {tnSign('b')}</b>은 음을 <b>반음 아래로</b> 옮겨요 -- 왼쪽 베프에게</>)}. 그래서 같은 검은건반을 D에서 보면 <b>D 플랫, D{tnSign('b')}</b>이에요. {A('B4', <>건반 하나, 이름 둘: 클라라의 베프이면서 강아지의 베프예요</>)}.</>
        : <>Now the black keys get their names. {A('B5', <>The <b>sharp sign {tnSign('#')}</b> moves a note <b>up a semitone</b> -- to its best friend on the right</>)}. So the black key just right of C is <b>C sharp, C{tnSign('#')}</b>. {A('B5', <>The <b>flat sign {tnSign('b')}</b> moves a note <b>down a semitone</b> -- to its best friend on the left</>)}. So the same black key, seen from D, is <b>D flat, D{tnSign('b')}</b>. {A('B4', <>One key, two names: it is Clara's best friend and the Dog's best friend too</>)}.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>C를 치고 C{tnSign('#')}를 쳐요 -- 위쪽 베프. D를 치고 D{tnSign('b')}을 쳐요 -- 아래쪽 베프. 같은 검은건반이에요!</>,
        <>검은건반마다 이름 두 개를 말해요: 작은 집 C{tnSign('#')} = D{tnSign('b')}, D{tnSign('#')} = E{tnSign('b')}; 큰 집 F{tnSign('#')} = G{tnSign('b')}, G{tnSign('#')} = A{tnSign('b')}, A{tnSign('#')} = B{tnSign('b')}.</>,
      ] : [
        <>Play C, then C{tnSign('#')} -- its best friend up. Play D, then D{tnSign('b')} -- its best friend down. The same black key!</>,
        <>Name every black key both ways: the small house C{tnSign('#')} = D{tnSign('b')}, D{tnSign('#')} = E{tnSign('b')}; the big house F{tnSign('#')} = G{tnSign('b')}, G{tnSign('#')} = A{tnSign('b')}, A{tnSign('#')} = B{tnSign('b')}.</>,
      ]}/>
      <LbRemember><>{tnSign('#')}{t(' up to the best friend on the right, ', '는 오른쪽 베프로 위, ')}{tnSign('b')}{t(' down to the one on the left: one black key, two names.', '은 왼쪽 베프로 아래: 검은건반 하나, 이름 둘.')}</></LbRemember>
    </LbPage>,

    // 6. the signs on the staff
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Sharps and flats on the staff', '오선 위의 샤프와 플랫')}>
      <LbLive still={<LbPic h={330}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{p6}</div></LbPic>} live={<AccidentalCards/>}/>
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
