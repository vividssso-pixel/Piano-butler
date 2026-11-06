// ─── Phases 457-458: chapter 5 (Notes & Rests): the Lesson Book, draft v2 (?book=lesson&ch=note-values; drills.src.html unchanged) ───
// v2 (her 2026-10-13 20:45): walk and running only (no bird / tur-tle); 'its other name is ...', never 'American books';
// every explanation short and plain; the rests show which line they sit on or hang from.
// The level plan's scope for room 5: the semibreve, the minim, the crotchet, the quaver pair, the dotted minim; their
// rests as pictures. Rests on the staff, bars and filling bars wait for Time signatures; the dotted crotchet, single
// quavers and semiquavers for Rhythm patterns and the drill's higher levels. It builds on the pulse chapter (the beat
// as hearts, counting 1 2 3 4, silent beats as dashed circles, bird and tur-tle, finger numbers in coral circles) and
// comes before the staff, so the notes stand over the beats with no staff; the tasks use middle C (chapter 2) and the
// black-key houses, not letter names, since the floor's rooms are free in order (ROOM_AFTER: pulse only).
// Each note has a coral sound line under it, as long as its beats (B6). Her G2 for the pulse chapter: 'walk, running ...
// 1 2 3 4, 1+2+3+4+, 1e+a 2e+a; + is and' (Book rule 12). AMEB: the plan puts these at Preliminary.

const nvbR = (svg) => ({ k: 'raw', svg });
const nvbF = (n) => pFix(n);
// a note head; the semibreve's is wider, rounder and heavier
function nvbHead(x, y, kind, col, k) {
  const w = kind === 'w', hollow = w || kind === 'h';
  const rx = (w ? 9.4 : 7.2) * k, ry = (w ? 6.3 : 5.3) * k, rot = w ? -12 : -20;
  return '<ellipse cx="' + nvbF(x) + '" cy="' + nvbF(y) + '" rx="' + nvbF(rx) + '" ry="' + nvbF(ry) + '" transform="rotate(' + rot + ' ' + nvbF(x) + ' ' + nvbF(y) + ')" fill="' + (hollow ? '#fff' : col) + '" stroke="' + col + '" stroke-width="' + nvbF(w ? 2.9 * k : hollow ? 2.3 * k : 1.2 * k) + '"/>';
}
// one note: kind 'w' semibreve, 'h' minim, 'q' crotchet, 'e' a single quaver; o.dot, o.col, o.k
function nvbNote(x, y, kind, o = {}) {
  const k = o.k || 1, col = o.col || PEN_N, sx = x + 6.4 * k, top = y - 34 * k;
  let s = nvbHead(x, y, kind, col, k);
  if (kind !== 'w') s += '<line x1="' + nvbF(sx) + '" y1="' + nvbF(y - 1.5 * k) + '" x2="' + nvbF(sx) + '" y2="' + nvbF(top) + '" stroke="' + col + '" stroke-width="' + nvbF(1.9 * k) + '" stroke-linecap="round"/>';
  if (kind === 'e') s += '<path d="M' + nvbF(sx) + ' ' + nvbF(top) + ' c ' + nvbF(2 * k) + ' ' + nvbF(9 * k) + ' ' + nvbF(13 * k) + ' ' + nvbF(12 * k) + ' ' + nvbF(8 * k) + ' ' + nvbF(27 * k) + '" fill="none" stroke="' + col + '" stroke-width="' + nvbF(2.6 * k) + '" stroke-linecap="round"/>';
  if (o.dot) s += '<circle cx="' + nvbF(x + 14 * k) + '" cy="' + nvbF(y - 2 * k) + '" r="' + nvbF(2.6 * k) + '" fill="' + col + '"/>';
  return nvbR(s);
}
// two quavers joined by a beam
function nvbPair(x1, x2, y, o = {}) {
  const k = o.k || 1, col = o.col || PEN_N, top = y - 34 * k;
  let s = nvbHead(x1, y, 'q', col, k) + nvbHead(x2, y, 'q', col, k);
  [x1, x2].forEach(x => { s += '<line x1="' + nvbF(x + 6.4 * k) + '" y1="' + nvbF(y - 1.5 * k) + '" x2="' + nvbF(x + 6.4 * k) + '" y2="' + nvbF(top) + '" stroke="' + col + '" stroke-width="' + nvbF(1.9 * k) + '"/>'; });
  s += '<path d="M' + nvbF(x1 + 5.5 * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + 7.3 * k) + ' ' + nvbF(top - 0.2 * k) + ' L' + nvbF(x2 + 7.3 * k) + ' ' + nvbF(top + 5.2 * k) + ' L' + nvbF(x1 + 5.5 * k) + ' ' + nvbF(top + 5.2 * k) + ' Z" fill="' + col + '"/>';
  return nvbR(s);
}
// a rest as a picture: 'q' crotchet rest, 'h' minim rest (sits on its short line), 'w' semibreve rest (hangs under it)
function nvbRest(x, y, kind, o = {}) {
  const k = o.k || 1, col = o.col || PEN_N, P = (a, b) => nvbF(x + a * k) + ' ' + nvbF(y + b * k);
  if (kind === 'q') return nvbR('<path d="M' + P(-3, -19) + ' L' + P(5, -9) + ' L' + P(-2, 0) + ' L' + P(6, 10) + ' C' + P(-4, 4) + ' ' + P(-7, 15) + ' ' + P(1, 19) + '" fill="none" stroke="' + col + '" stroke-width="' + nvbF(3.4 * k) + '" stroke-linecap="round" stroke-linejoin="round"/>');
  const line = '<line x1="' + nvbF(x - 13 * k) + '" y1="' + nvbF(y) + '" x2="' + nvbF(x + 13 * k) + '" y2="' + nvbF(y) + '" stroke="' + col + '" stroke-width="' + nvbF(1.4 * k) + '"/>';
  const by = kind === 'h' ? y - 7 * k : y;
  return nvbR(line + '<rect x="' + nvbF(x - 8 * k) + '" y="' + nvbF(by) + '" width="' + nvbF(16 * k) + '" height="' + nvbF(7 * k) + '" fill="' + col + '"/>');
}
// a piece of the five lines of music (the staff comes in chapter 6), numbered from the bottom; line `hi` coral
function nvbLines(x, y5, gap, w, hi) {   // y5: the bottom line
  const out = [];
  for (let i = 0; i < 5; i++) { const y = y5 - i * gap, on = i + 1 === hi;
    out.push({ ...penLine([x - w / 2, y], [x + w / 2, y], on ? 2.4 : 1.3, on ? PEN_C : PEN_N), nw: true });
    out.push({ ...penText(x - w / 2 - 9, y + 4, String(i + 1), { size: 10.5, weight: 900, fill: on ? PEN_C : PEN_MUTED_NV, anchor: 'middle' }) }); }
  return out;
}
const PEN_MUTED_NV = 'rgba(38,41,107,0.55)';
// the sound line under a note: as long as its beats (B6)
const nvbBar = (x1, x2, y, col = PEN_C) => ({ ...penLine([x1, y], [x2, y], 4, col), nw: true });
// the brother running: two quick steps on each beat
function nvbRunner(who = 'boy') {
  const x = 75;
  const J = { hip: [x, 102], neck: [x + 9, 64], head: [x + 12, 49],
    arms: [[[x + 10, 66], [x + 22, 80], [x + 32, 72]], [[x + 6, 67], [x - 6, 82], [x - 15, 75]]],
    legs: [[[x + 2, 102], [x + 18, 120], [x + 15, 146]], [[x - 2, 102], [x - 13, 124], [x - 30, 134]]] };
  return penKid(J, 1, who);
}
// a row of notes over beats: cells D wide centred on H(i); items [kind, beats], kind 'w' | 'h' | 'hd' (dotted minim) |
// 'q' | 'p' (quaver pair) | 'r' (crotchet rest); each note's sound line under it
function nvbRow(s, H, D, y, items) {
  let b = 0;
  items.forEach(([kd, n]) => {
    const x0 = H(b) - D / 2 + 5, x1 = H(b + n - 1) + D / 2 - 5;
    if (kd === 'p') s.push(nvbPair(H(b) - 13, H(b) + 9, y, { k: 0.92 }), nvbBar(x0, H(b) - 3, y + 16), nvbBar(H(b) + 3, x1, y + 16));
    else if (kd === 'r') s.push(nvbRest(H(b) + 1, y - 12, 'q'));
    else s.push(nvbNote(kd === 'w' ? H(b) - 1 : H(b) - 3, y, kd === 'hd' ? 'h' : kd, { dot: kd === 'hd' }), nvbBar(x0, x1, y + 16));
    b += n;
  });
}

function nvLbPages(scr = false) {
  const ch = 'note-values';
  const A = (q, kids) => <LbAsk q={q}>{kids}</LbAsk>;
  const pic = (art, vb, label, h = 230, mw = 680) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}><PenArt shapes={art} vb={vb} label={label}/></div></LbPic>;
  const heart = (x, y, k = 2.6, col = PEN_C) => ({ ...tnHeart(x, y, k, col), nw: true });
  const txt = (x, y, s, o) => ({ ...penText(x, y, s, o) });
  const N = (n) => String(n);
  const pulseNo = bkChapterNo('pulse'), chP = t('chapter ' + pulseNo, pulseNo + '챕터');
  const C4 = '1 2 3 4', QQ = '1 + 2 +';

  // p1: the note family on four beats: a semibreve, two minims, four crotchets, four quaver pairs, over four hearts
  const art1 = (() => {
    const s = [], D = 62, H = (i) => 162 + i * D, rows = [44, 102, 160, 218];
    [[t('semibreve', '온음표'), t('4 beats', '4박')], [t('minim', '2분음표'), t('2 beats', '2박')], [t('crotchet', '4분음표'), t('1 beat', '1박')], [t('quavers', '8분음표'), t('2 on a beat', '한 박에 둘')]].forEach(([n, b], r) => {
      s.push(txt(8, rows[r] - 2, n, { size: 13, weight: 900, fill: PEN_N, anchor: 'start' }), txt(8, rows[r] + 14, b, { size: 11.5, weight: 800, fill: PEN_C, anchor: 'start' }));
    });
    nvbRow(s, H, D, rows[0], [['w', 4]]);
    nvbRow(s, H, D, rows[1], [['h', 2], ['h', 2]]);
    nvbRow(s, H, D, rows[2], [['q', 1], ['q', 1], ['q', 1], ['q', 1]]);
    nvbRow(s, H, D, rows[3], [['p', 1], ['p', 1], ['p', 1], ['p', 1]]);
    [0, 1, 2, 3].forEach(i => { s.push(heart(H(i), 268, 2.7)); s.push(txt(H(i), 298, N(i + 1), { size: 16, weight: 900, fill: PEN_N, anchor: 'middle' })); });
    s.push(txt(8, 273, t('the beat', '박'), { size: 13, weight: 900, fill: PEN_C, anchor: 'start' }));
    return s;
  })();

  // p2: the crotchet: one beat; the sister walks, one step on each crotchet
  const art2 = (() => {
    const s = [], D = 56, H = (i) => 184 + i * D;
    s.push(...penPlace(plWalker('girl'), 1.02, [75, 156], [70, 226]));
    nvbRow(s, H, D, 84, [['q', 1], ['q', 1], ['q', 1], ['q', 1]]);
    [0, 1, 2, 3].forEach(i => {
      s.push(txt(H(i), 124, t('walk', '걷기'), { size: 13, weight: 900, fill: PEN_N, anchor: 'middle' }));
      s.push(heart(H(i), 150, 2.6));
      s.push(...plFoot(H(i), 184 + (i % 2 ? 7 : -7), 2.2, PEN_N, i % 2 === 0));
      s.push(txt(H(i), 224, N(i + 1), { size: 16, weight: 900, fill: PEN_N, anchor: 'middle' }));
    });
    return s;
  })();

  // p3: the minim: two beats; a crotchet beside a minim; then two minims over four beats, the held beats lighter
  const art3 = (() => {
    const s = [], D = 70, H = (i) => 66 + i * D;
    s.push(txt(H(0), 34, t('crotchet: 1 beat', '4분음표: 1박'), { size: 12.5, weight: 900, fill: PEN_N, anchor: 'middle' }));
    nvbRow(s, H, D, 84, [['q', 1]]); s.push(heart(H(0), 130, 2.4));
    s.push(txt(H(2.5), 34, t('minim: 2 beats', '2분음표: 2박'), { size: 12.5, weight: 900, fill: PEN_N, anchor: 'middle' }));
    nvbRow(s, (i) => H(i + 2), D, 84, [['h', 2]]); s.push(heart(H(2), 130, 2.4), heart(H(3), 130, 2.4));
    nvbRow(s, H, D, 202, [['h', 2], ['h', 2]]);
    [0, 1, 2, 3].forEach(i => { s.push(heart(H(i), 248, 2.4)); s.push(txt(H(i), 280, N(i + 1), { size: 17, weight: 900, fill: i % 2 ? 'rgba(38,41,107,0.42)' : PEN_N, anchor: 'middle' })); });
    s.push(txt(H(1.5), 308, t('play, then hold', '치고, 누르고 있어요'), { size: 12.5, weight: 900, fill: PEN_C, anchor: 'middle' }));
    return s;
  })();

  // p4: longer notes: a dotted minim (3 beats) and a crotchet; a semibreve (4 beats)
  const art4 = (() => {
    const s = [], D = 64, H = (i) => 136 + i * D;
    s.push(txt(8, 68, t('dotted minim', '점2분음표'), { size: 12.5, weight: 900, fill: PEN_N, anchor: 'start' }), txt(8, 84, t('3 beats', '3박'), { size: 12, weight: 800, fill: PEN_C, anchor: 'start' }));
    nvbRow(s, H, D, 76, [['hd', 3], ['q', 1]]);
    s.push(txt(8, 180, t('semibreve', '온음표'), { size: 12.5, weight: 900, fill: PEN_N, anchor: 'start' }), txt(8, 196, t('4 beats', '4박'), { size: 12, weight: 800, fill: PEN_C, anchor: 'start' }));
    nvbRow(s, H, D, 188, [['w', 4]]);
    [122, 234].forEach(y => [0, 1, 2, 3].forEach(i => s.push(heart(H(i), y, 2.3))));
    [0, 1, 2, 3].forEach(i => s.push(txt(H(i), 266, N(i + 1), { size: 16, weight: 900, fill: PEN_N, anchor: 'middle' })));
    return s;
  })();

  // p5: two quavers on one beat: running; counted 1 + 2 +
  const art5 = (() => {
    const s = [], D = 60, H = (i) => 178 + i * D;
    s.push(...penPlace(nvbRunner('boy'), 0.95, [75, 156], [62, 222]));
    nvbRow(s, H, D, 80, [['q', 1], ['p', 1], ['q', 1], ['p', 1]]);
    [0, 1, 2, 3].forEach(i => {
      const pr = i % 2 === 1;
      s.push(txt(H(i), 122, pr ? t('run-ning', '달리기') : t('walk', '걷기'), { size: 13, weight: 900, fill: PEN_N, anchor: 'middle' }));
      s.push(heart(H(i), 148, 2.5));
      s.push(txt(H(i), 180, pr ? N(i + 1) + '  +' : N(i + 1), { size: 16, weight: 900, fill: PEN_N, anchor: 'middle' }));
      if (!pr) s.push(...plFoot(H(i), 210, 2, PEN_N, true));
      else { s.push(...plFoot(H(i) - 11, 204, 1.7, PEN_C, true)); s.push(...plFoot(H(i) + 11, 216, 1.7, PEN_C, false)); }
    });
    return s;
  })();

  // p6: rests: the three signs, then a row with a silent beat (dashed, as in the pulse chapter), the hearts go on
  const art6 = (() => {
    const s = [];
    const G = 13, Y1 = 98;   // the five lines: the bottom line at Y1, 13 apart
    s.push(nvbRest(56, 70, 'q', { k: 1.6 }));
    s.push(...nvbLines(196, Y1, G, 96, 3), nvbR('<rect x="' + nvbF(196 - 15) + '" y="' + nvbF(Y1 - 2 * G - 10) + '" width="30" height="10" fill="' + PEN_N + '"/>'));
    s.push(...nvbLines(332, Y1, G, 96, 4), nvbR('<rect x="' + nvbF(332 - 15) + '" y="' + nvbF(Y1 - 3 * G) + '" width="30" height="10" fill="' + PEN_N + '"/>'));
    [[56, t('crotchet rest', '4분쉼표'), t('1 beat', '1박')], [196, t('minim rest', '2분쉼표'), t('2 beats', '2박')], [332, t('semibreve rest', '온쉼표'), t('4 beats', '4박')]].forEach(([x, n, b]) => {
      s.push(txt(x, 124, n, { size: 13, weight: 900, fill: PEN_N, anchor: 'middle' }), txt(x, 141, b, { size: 12, weight: 800, fill: PEN_C, anchor: 'middle' }));
    });
    s.push(txt(196, 30, t('sits on the middle line', '가운데 줄 위에 앉아요'), { size: 11.5, weight: 900, fill: PEN_C, anchor: 'middle' }), txt(332, 30, t('hangs from line 4', '넷째 줄에 매달려요'), { size: 11.5, weight: 900, fill: PEN_C, anchor: 'middle' }));
    const D = 66, H = (i) => 98 + i * D;
    nvbRow(s, H, D, 212, [['q', 1], ['q', 1], ['r', 1], ['q', 1]]);
    [0, 1, 2, 3].forEach(i => { s.push(heart(H(i), 256, 2.4)); s.push(i === 2 ? plBeat(H(i), 288, 13, N(i + 1), { silent: true, size: 14 }) : txt(H(i), 294, N(i + 1), { size: 16, weight: 900, fill: PEN_N, anchor: 'middle' })); });
    return s;
  })();

  const chkArts = {
    crotchet: [nvbNote(16, 30, 'q', { k: 0.62 }), nvbNote(42, 30, 'q', { k: 0.62 }), nvbNote(68, 30, 'q', { k: 0.62 })],
    hold: [nvbNote(16, 24, 'h', { k: 0.62 }), nvbBar(10, 82, 34)],
    long: [nvbNote(16, 28, 'h', { k: 0.6, dot: true }), nvbNote(64, 30, 'w', { k: 0.7 })],
    pair: [nvbPair(14, 32, 30, { k: 0.62 }), txt(64, 34, '1 +', { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' })],
    rests: [nvbRest(24, 22, 'q', { k: 0.62 }), nvbRest(64, 26, 'h', { k: 0.8 })],
  };
  const checksRows = [
    ['crotchet', [0, 0, 92, 40], t('I can play a crotchet on every beat, counting out loud', '박마다 4분음표를 치면서 소리 내어 셀 수 있어요')],
    ['hold', [0, 0, 92, 40], t('I can hold a minim for two beats and keep counting', '2분음표를 두 박 동안 누르면서 계속 셀 수 있어요')],
    ['long', [0, 0, 92, 40], t('I can hold a dotted minim for 3 beats and a semibreve for 4', '점2분음표는 3박, 온음표는 4박 동안 누를 수 있어요')],
    ['pair', [0, 0, 92, 40], t('I can play two quavers on one beat and count ' + QQ, '한 박에 8분음표 둘을 치고 ' + QQ + '로 셀 수 있어요')],
    ['rests', [0, 0, 92, 40], t('I can count through a crotchet rest and a minim rest', '4분쉼표와 2분쉼표 동안 계속 셀 수 있어요')],
  ];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Notes & Rests', '음표와 쉼표')}</div>
      </div></LbOnly>
      {pic(art1, [0, 0, 410, 310], t('The note family over four beats, four coral hearts numbered 1 2 3 4. One semibreve lasts all four beats; two minims, two beats each; four crotchets, one beat each; four pairs of quavers, two on each beat. Under each note a coral sound line as long as its beats.', '박 네 개, 1 2 3 4 번호가 붙은 산호색 심장 넷 위의 음표 가족. 온음표 하나는 네 박 내내, 2분음표 둘은 두 박씩, 4분음표 넷은 한 박씩, 8분음표 둘씩 네 쌍은 한 박에 둘. 음표마다 아래에 박만큼 긴 산호색 소리 줄.'), 230, 500)}
      <LbSay size={17.5}>{LANG === 'ko' ? <>음표마다 소리 나는 <b>박의 수</b>가 정해져 있어요. <b>모양</b>을 보면 알 수 있어요. <b>쉼표</b>는 몇 박 동안 쉬는지 알려 줘요.</>
        : <>Every note lasts a number of <b>beats</b>. Its <b>shape</b> tells you how many. A <b>rest</b> is a silence that lasts beats too.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('The crotchet: one beat', '4분음표: 한 박'), 2], [t('The minim: two beats', '2분음표: 두 박'), 3], [t('Longer notes: 3 and 4 beats', '더 긴 음표: 3박과 4박'), 4], [t('Two quavers on one beat', '한 박에 8분음표 둘'), 5], [t('Rests: silence you count', '쉼표: 세면서 쉬어요'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, , x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkTick(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. the crotchet
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The crotchet: one beat', '4분음표: 한 박')}>
      {pic(art2, [0, 20, 400, 216], t('The sister walking. Beside her four crotchets, each with a short coral sound line under it, the word walk under each, one coral heart and one footprint for each beat, and the count 1 2 3 4.', '걸어가는 누나. 옆에 4분음표 넷, 음표마다 아래에 짧은 산호색 소리 줄, 그 아래 걷기라는 낱말, 박마다 산호색 심장 하나와 발자국 하나, 세는 숫자 1 2 3 4.'), 230)}
      <LbSay>{LANG === 'ko' ? <><b>4분음표</b>는 꽉 찬 머리에 기둥이 있어요. <b>한 박</b> 동안 소리 나요. 걸어요: 한 박에 한 걸음.</>
        : <>A <b>crotchet</b> has a filled head and a stem. It lasts <b>one beat</b>. Walk: one step on each beat. Its other name is a quarter note.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 1번 손가락, 가운데 도: 박마다 4분음표, {C4}로 세면서. 네 번.</>,
        <>방을 걸어요: 박마다 한 걸음, 소리 내어 세면서. 8걸음.</>,
      ] : [
        <>Right hand, finger 1 on middle C: a crotchet on every beat, counting {C4}. Four times round.</>,
        <>Walk round the room: one step on each beat, counting out loud. 8 steps.</>,
      ]}/>
      <LbRemember>{t('A crotchet: one beat.', '4분음표: 한 박.')}</LbRemember>
    </LbPage>,

    // 3. the minim
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The minim: two beats', '2분음표: 두 박')}>
      {pic(art3, [0, 16, 340, 302], t('A crotchet with a sound line over one heart, beside a minim with a sound line over two hearts. Below, two minims over four hearts, the count 1 2 3 4 under them, 2 and 4 printed lighter: play, then hold.', '심장 하나 위의 4분음표와 소리 줄, 그 옆에 심장 둘 위의 2분음표와 두 박 길이의 소리 줄. 아래에 심장 넷 위의 2분음표 둘, 그 아래 세는 숫자 1 2 3 4, 2와 4는 연하게: 치고, 누르고 있어요.'), 240, 540)}
      <LbSay>{LANG === 'ko' ? <><b>2분음표</b>는 속이 빈 머리에 기둥이 있어요. <b>두 박</b> 동안 소리 나요: 치고, 누르고 있어요. {A('B4', <>누르는 동안에도 계속 세요.</>)}</>
        : <>A <b>minim</b> has a hollow head and a stem. It lasts <b>two beats</b>: play, then hold. {A('B4', <>Keep counting while you hold.</>)} Its other name is a half note.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 1번 손가락, 가운데 도: 1과 3에서 2분음표, 다음 박까지 누르고 있어요. 소리 내어 세면서 네 번.</>,
        <>오른손, 넷째 작은 집에 2번과 3번 손가락: 2번으로 4분음표 둘 (1, 2), 3번으로 2분음표 (3 4). 소리 내어 세면서 네 번.</>,
      ] : [
        <>Right hand, finger 1 on middle C: a minim on 1 and on 3, each held through the next beat. Count out loud, four times round.</>,
        <>Right hand, fingers 2 and 3 on the 4th small house: finger 2 two crotchets (1, 2), finger 3 a minim (3 4). Count out loud, four times round.</>,
      ]}/>
      <LbRemember>{t('A minim: two beats.', '2분음표: 두 박.')}</LbRemember>
    </LbPage>,

    // 4. longer notes
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Longer notes: 3 and 4 beats', '더 긴 음표: 3박과 4박')}>
      {pic(art4, [0, 24, 400, 250], t('Top: a dotted minim with a sound line across three hearts, then a crotchet on the fourth. Bottom: a semibreve, a round hollow head with no stem, its sound line across all four hearts. The count 1 2 3 4 underneath.', '위: 점2분음표, 소리 줄이 심장 셋에 걸쳐 있고, 넷째 심장 위에는 4분음표. 아래: 온음표, 기둥 없는 둥근 속 빈 머리, 소리 줄이 심장 넷 모두에 걸쳐 있어요. 아래에 세는 숫자 1 2 3 4.'), 230)}
      <LbSay>{LANG === 'ko' ? <>2분음표에 점이 붙으면 <b>세 박</b>이에요: {A('B5', <>점은 2분음표의 반을 더해요</>)}. <b>온음표</b>는 기둥 없는 속 빈 머리예요. <b>네 박</b> 동안 소리 나요.</>
        : <>A minim with a dot lasts <b>three beats</b>: {A('B5', <>the dot adds half the minim</>)}. A <b>semibreve</b> has a hollow head and no stem. It lasts <b>four beats</b>. Their other names are dotted half note and whole note.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 1번 손가락, 가운데 도: 점2분음표 (1 2 3), 그다음 4분음표 (4). 소리 내어 세면서 네 번.</>,
        <>오른손 3번 손가락, 넷째 작은 집의 오른쪽 검은건반: 온음표 (1 2 3 4). 소리 내어 세면서 네 번.</>,
      ] : [
        <>Right hand, finger 1 on middle C: a dotted minim (1 2 3), then a crotchet (4). Count out loud, four times round.</>,
        <>Right hand, finger 3 on the right black key of the 4th small house: a semibreve (1 2 3 4). Count out loud, four times round.</>,
      ]}/>
      <LbRemember>{t('Dotted minim: 3 beats. Semibreve: 4 beats.', '점2분음표: 3박. 온음표: 4박.')}</LbRemember>
    </LbPage>,

    // 5. two quavers on one beat
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Two quavers on one beat', '한 박에 8분음표 둘')}>
      {pic(art5, [0, 20, 400, 240], t('The brother running. Beside him, over four hearts: a crotchet (walk), a pair of quavers joined by a beam (run-ning), a crotchet, a pair of quavers, each with its sound line. The count 1, 2 +, 3, 4 +. One footprint for each crotchet, two quick coral footprints for each pair.', '달리는 남동생. 옆에 심장 넷 위로: 4분음표 (걷기), 꼬리가 이어진 8분음표 둘 (달리기), 4분음표, 8분음표 둘, 음표마다 소리 줄. 세는 숫자 1, 2 +, 3, 4 +. 4분음표마다 발자국 하나, 8분음표 둘마다 빠른 산호색 발자국 둘.'), 230)}
      <LbSay>{LANG === 'ko' ? <>꼬리가 이어진 <b>8분음표</b> 둘은 <b>한 박</b>을 나눠요. 달려요: 한 박에 빠른 걸음 둘. <b>{QQ}</b>로 세고, +는 "앤"이라고 읽어요.</>
        : <>Two <b>quavers</b> joined by a beam share <b>one beat</b>. Run: two quick steps on a beat. Count them <b>{QQ}</b> and say "and" for +. Their other name is eighth notes.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>손뼉 쳐요: 한 번, 빠르게 두 번, 한 번, 빠르게 두 번. 그다음 오른손 1번 손가락으로 가운데 도에서 쳐요, 1, 2 +, 3, 4 +로 세면서. 네 번.</>,
        <>이번엔 빠르게 두 번, 빠르게 두 번, 한 번, 한 번: 손뼉 치고, 가운데 도에서 쳐요, 1 +, 2 +, 3, 4로 세면서. 네 번.</>,
      ] : [
        <>Say and clap: walk, run-ning, walk, run-ning. Then play it with right-hand finger 1 on middle C, counting 1, 2 +, 3, 4 +. Four times round.</>,
        <>Now run-ning, run-ning, walk, walk: say it, clap it, then play it on middle C, counting 1 +, 2 +, 3, 4. Four times round.</>,
      ]}/>
      <LbRemember>{t('Two quavers: one beat.', '8분음표 둘: 한 박.')}</LbRemember>
    </LbPage>,

    // 6. rests
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Rests: silence you count', '쉼표: 세면서 쉬어요')}>
      {pic(art6, [0, 14, 400, 294], t('The three rests with their beats: the crotchet rest, a zigzag, 1 beat; the minim rest, a block sitting on the middle of five lines, 2 beats; the semibreve rest, a block hanging from line 4, 4 beats. Below, crotchet, crotchet, crotchet rest, crotchet over four hearts: the third beat is a dashed circle, a silent beat.', '쉼표 셋과 박: 4분쉼표, 지그재그, 1박. 2분쉼표, 다섯 줄의 가운데 줄 위에 앉은 네모, 2박. 온쉼표, 넷째 줄에 매달린 네모, 4박. 아래에 4분음표, 4분음표, 4분쉼표, 4분음표가 심장 넷 위에: 셋째 박은 점선 동그라미, 조용한 박.'), 230)}
      <LbSay>{LANG === 'ko' ? <><b>쉼표</b>는 쉬는 박이에요. 쉬는 동안에도 계속 세요. 4분쉼표는 1박, 2분쉼표는 2박, 온쉼표는 4박. 다섯 줄 위에서 2분쉼표는 <b>가운데 줄 위에 앉고</b>, 온쉼표는 <b>넷째 줄에 매달려요</b>.</>
        : <>A <b>rest</b> is a silent beat. Keep counting while it lasts. A crotchet rest is 1 beat, a minim rest 2 beats, a semibreve rest 4 beats. On the five lines of music, the minim rest <b>sits on the middle line</b> and the semibreve rest <b>hangs from line 4</b>. Their other names are quarter, half and whole rests.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 1번 손가락, 가운데 도: 1, 2, 4에서 쳐요. 3에서는 손을 건반 바로 위에 띄우고 세요. 네 번.</>,
        <>오른손 1번 손가락, 가운데 도: 2분음표 (1 2), 그다음 2분쉼표 (3 4), 손은 건반 바로 위에. 소리 내어 세면서 네 번.</>,
      ] : [
        <>Right hand, finger 1 on middle C: play on 1, 2 and 4. On 3, lift your hand just above the key and count. Four times round.</>,
        <>Right hand, finger 1 on middle C: a minim (1 2), then a minim rest (3 4), your hand just above the key. Count out loud, four times round.</>,
      ]}/>
      <LbRemember>{t('A rest: count the silence.', '쉼표: 쉬면서 세요.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, then colour a circle for how it is going: not yet, nearly, or got it! The check-up on paper is in the Workbook.', '피아노 앞에서 하나씩 보여 주고 어떤지 동그라미를 칠해요: 아직, 거의, 됐어요! 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, vb, x]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_nv_v1" rows={checksRows.map(([a, vb, x]) => [{ shapes: chkArts[a], vb }, x])}/>}/>
    </LbPage>,
  ];
}
function NotesRestsLessonBook() { return <>{nvLbPages(false)}</>; }
