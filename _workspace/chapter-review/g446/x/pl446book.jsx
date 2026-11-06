// ─── Phase 446: chapter 3 (Pulse & Counting) Lesson Book, draft v1 ───
// Built on her own words for the pulse ("Music has a heartbeat: the pulse. It keeps going, steady, even when the notes
// stop."), the level plan's scope for room 3 (a steady beat, counting out loud, the beat and the rhythm are not the same;
// strong and weak beats wait for Time signatures, note values for Notes & rests), the cast of chapters 1 and 2 (the
// sister and the brother, the small house and the big house, the bird's sky and the turtle's sea, the lighthouse) and
// the Book rules. Chapter 3 comes before the letter names (chapter 4): the keys are named by their house and the fingers
// by their numbers. The yellow marks (?draft=1) wait for her answers (the B codes in the review pack).
// AMEB (2026 Manual): practical; the groundwork for 2/4 and 3/4 (Preliminary). No grade asks for "pulse" on paper.

const plRaw = (svg) => ({ k: 'raw', svg });
// a beat circle: white with a navy ring (a beat), navy filled (a beat you play), dashed (a silent beat: count, don't play)
function plBeat(cx, cy, r, label, o = {}) {
  const col = o.col || PEN_N, fill = o.fill ? col : '#fff';
  let s = '<circle cx="' + pFix(cx) + '" cy="' + pFix(cy) + '" r="' + pFix(r) + '" fill="' + fill + '" stroke="' + col + '" stroke-width="' + (o.sw || 2.2) + '"' + (o.silent ? ' stroke-dasharray="4.2 3.4"' : '') + '/>';
  if (label != null && label !== '') s += '<text x="' + pFix(cx) + '" y="' + pFix(cy + r * 0.38) + '" text-anchor="middle" font-size="' + pFix(o.size || r * 1.08) + '" font-weight="900" fill="' + (o.fill ? '#fff' : col) + '" font-family="Inter,sans-serif">' + penEsc(label) + '</text>';
  return plRaw(s);
}
// a bracket under two neighbours: the gap between two beats
function plGap(x1, x2, y, col = PEN_C) {
  return { k: 'pl', p: [[x1, y - 4], [x1, y], [x2, y], [x2, y - 4]], s: col, w: 1.6, nw: true };
}
// a small curved arrow (back to 1)
function plArc(x1, x2, y, h, col = PEN_C) {
  const m = (x1 + x2) / 2;
  return [penCurve([['M', [x1, y]], ['Q', [m, y - h], [x2, y]]], 1.8, col), { k: 'pa', seg: [['M', [x2 - 5.5, y - 5]], ['L', [x2, y]], ['L', [x2 + 1, y - 7]]], f: 'none', s: col, w: 1.8, nw: true }];
}
// a bare footprint pointing right (the way she walks); left: the left foot (its big toe on the other side)
function plFoot(cx, cy, k = 1, col = PEN_N, left = false) {
  const m = left ? -1 : 1, P = (a, b) => [cx + a * k, cy + b * m * k];
  return [{ k: 'el', c: P(0.6, 0), rx: 3.2 * k, ry: 2.7 * k, f: col, nw: true }, { k: 'el', c: P(-4.4, 0.5), rx: 2.3 * k, ry: 1.9 * k, f: col, nw: true },
    ...[[4.8, -2.3, 0.95], [5.8, -0.7, 0.85], [5.7, 0.9, 0.75], [4.9, 2.3, 0.65]].map(([a, b, r]) => ({ k: 'el', c: P(a, b), rx: r * k, ry: r * k, f: col, nw: true }))];
}
const plBird = (x, y, k) => fsBird(x, y, k).filter(e => !(e.k === 'tx' && e.text === '♪'));   // no note: a quaver is chapter 5's
// the sister walking: a stride (her joints, as fsKid's, legs and arms swinging)
function plWalker(who = 'girl') {
  const x = 75;
  const J = { hip: [x, 104], neck: [x + 2, 64], head: [x + 3, 49],
    arms: [[[x + 4, 66], [x + 13, 84], [x + 18, 99]], [[x - 2, 67], [x - 10, 85], [x - 15, 99]]],
    legs: [[[x + 2, 104], [x + 12, 129], [x + 18, 155]], [[x - 2, 104], [x - 9, 130], [x - 18, 152]]] };
  return penKid(J, 1, who);
}

function plLbPages(scr = false) {
  const ch = 'pulse';
  const A = (q, kids) => <LbAsk q={q}>{kids}</LbAsk>;
  const pic = (art, vb, label, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}><PenArt shapes={art} vb={vb} label={label}/></div></LbPic>;

  // p1: the heart, and the beat it makes: steady circles, 1 2 3 4, 1 2 3 4, the same gap every time
  const art1 = (() => {
    const s = [];
    s.push({ ...tnHeart(66, 112, 7.4), ch: true });
    s.push({ ...penText(66, 176, t('your heartbeat', '내 심장 박동'), { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) });
    [10, 20, 30].forEach((d, i) => s.push(penCurve([['M', [120 + d, 112 - 12 - i * 6]], ['Q', [128 + d + i * 3, 112], [120 + d, 112 + 12 + i * 6]]], 2, PEN_C)));   // the beat going out of the heart
    const x0 = 172, dx = 44, r = 17;
    [[84, '1234'], [148, '1234']].forEach(([cy, ns]) => {
      ns.split('').forEach((n, i) => s.push(plBeat(x0 + i * dx, cy, r, n, { size: 17 })));
      for (let i = 0; i < 3; i++) s.push(plGap(x0 + i * dx, x0 + (i + 1) * dx, cy + r + 9));
    });
    s.push({ ...penText(x0 + 1.5 * dx, 46, t('the pulse: steady, it never stops', '박: 꾸준하고, 멈추지 않아요'), { size: 12.5, weight: 900, fill: PEN_N, anchor: 'middle' }) });
    s.push({ ...penText(x0 + 1.5 * dx, 198, t('the same gap every time', '매번 똑같은 간격'), { size: 12.5, weight: 900, fill: PEN_C, anchor: 'middle' }) });
    return s;
  })();

  // p2: a steady beat: footprints with the same gap every time (a tick) and footprints with gaps that change (a cross)
  const art2 = (() => {
    const s = [];
    s.push(...penPlace(plWalker('girl'), 1.12, [75, 156], [48, 226]));
    const row = (y, xs, ok) => {
      xs.forEach((x, i) => s.push(...plFoot(x, y + (i % 2 ? 9 : -9), 2.5, ok ? PEN_N : PEN_C, i % 2 === 0)));
      if (ok) for (let i = 0; i < xs.length - 1; i++) s.push(plGap(xs[i], xs[i + 1], y + 36, PEN_N));
      const mid = (xs[0] + xs[xs.length - 1]) / 2;
      s.push({ ...penText(mid, y - (ok ? 34 : 32), (ok ? '✓  ' : '✗  ') + (ok ? t('steady', '꾸준해요') : t('not steady', '들쭉날쭉')), { size: 14, weight: 900, fill: ok ? PEN_G : PEN_C, anchor: 'middle' }) });
    };
    row(80, [128, 168, 208, 248, 288, 328], true);
    row(208, [128, 146, 196, 268, 290, 328], false);
    s.push({ ...penText(228, 136, t('the same gap every time', '매번 똑같은 간격'), { size: 11.5, weight: 900, fill: PEN_N, anchor: 'middle' }) });
    return s;
  })();

  // p3: count out loud: the brother says the numbers, one on each beat; the count goes round: 4, then back to 1
  const art3 = (() => {
    const s = [];
    s.push(...penPlace(fsKid('boy', 'stand', 1), 1.15, [75, 156], [62, 232]));
    s.push({ k: 'rc', x: 36, y: 34, w: 96, h: 40, rx: 16, f: '#fff', s: PEN_N, sw: 1.8, nw: true }, { k: 'pl', p: [[62, 73], [70, 92], [80, 73]], s: PEN_N, w: 1.8, nw: true }, { k: 'rc', x: 63, y: 71, w: 16, h: 5, f: '#fff', nw: true });
    s.push({ ...penText(84, 60, '1, 2, 3, 4!', { size: 16, weight: 900, fill: PEN_C, anchor: 'middle' }) });
    const cx = 258, cy = 142, R = 58, r = 20;
    const at = (i) => { const a = -Math.PI / 2 + i * Math.PI / 2; return [cx + R * Math.cos(a), cy + R * Math.sin(a)]; };
    for (let i = 0; i < 4; i++) {   // the arrows between the circles, round the ring
      const a1 = -Math.PI / 2 + i * Math.PI / 2 + 0.42, a2 = -Math.PI / 2 + (i + 1) * Math.PI / 2 - 0.42, am = (a1 + a2) / 2, k2 = R / Math.cos((a2 - a1) / 2);
      const p1 = [cx + R * Math.cos(a1), cy + R * Math.sin(a1)], p2 = [cx + R * Math.cos(a2), cy + R * Math.sin(a2)], pm = [cx + k2 * Math.cos(am), cy + k2 * Math.sin(am)];
      const col = i === 3 ? PEN_C : PEN_N;
      s.push(penCurve([['M', p1], ['Q', pm, p2]], 2, col));
      const tang = [-Math.sin(a2), Math.cos(a2)], nrm = [Math.cos(a2), Math.sin(a2)];
      s.push({ k: 'pl', p: [[p2[0] - tang[0] * 7 + nrm[0] * 4, p2[1] - tang[1] * 7 + nrm[1] * 4], p2, [p2[0] - tang[0] * 7 - nrm[0] * 4, p2[1] - tang[1] * 7 - nrm[1] * 4]], s: col, w: 2, nw: true });
    }
    ['1', '2', '3', '4'].forEach((n, i) => { const [x, y] = at(i); s.push(plBeat(x, y, r, n, { size: 19 })); });
    s.push({ ...penText(cx - R - 12, cy - R + 2, t('back to 1', '다시 1'), { size: 12, weight: 900, fill: PEN_C, anchor: 'end' }) });
    s.push({ ...penText(cx, cy + R + r + 22, t('one number on each beat', '박마다 숫자 하나'), { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' }) });
    return s;
  })();

  // p4: when the notes stop: play on 1 and 2, count only on 3 and 4, and the count goes on; under it the heart keeps beating
  const art4 = (() => {
    const s = [];
    const dx = 46, cy = 104, r = 20, X = (i) => 34 + i * dx + (i >= 4 ? 18 : 0), x0 = X(0);
    for (let i = 0; i < 8; i++) {
      const play = i % 4 < 2, n = String(i % 4 + 1);
      s.push(plBeat(X(i), cy, r, n, { fill: play, silent: !play, size: 19 }));
      s.push({ ...tnHeart(X(i), cy + 60, 3), nw: true });
    }
    [[0, 1], [4, 5]].forEach(([a, b]) => s.push({ ...penText((X(a) + X(b)) / 2, cy - 34, t('play', '치기'), { size: 13, weight: 900, fill: PEN_N, anchor: 'middle' }) }));
    [[2, 3], [6, 7]].forEach(([a, b]) => s.push({ ...penText((X(a) + X(b)) / 2, cy - 34, t('count only', '세기만'), { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) }));
    s.push({ ...penLine([x0 - 8, cy + 94], [X(7) + 12, cy + 94], 2, PEN_C), nw: true }, { k: 'pl', p: [[X(7) + 5, cy + 89], [X(7) + 12, cy + 94], [X(7) + 5, cy + 99]], s: PEN_C, w: 2, nw: true });
    s.push({ ...penText((X(3) + X(4)) / 2, cy + 118, t('the pulse goes on', '박은 계속돼요'), { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) });
    return s;
  })();

  // p5: beat or rhythm: four beats (hearts) under four words; one dot for each sound on top: bird (one), tur-tle (two)
  const art5 = (() => {
    const s = [];
    const x0 = 104, dx = 78, words = [1, 2, 1, 2];
    words.forEach((n, i) => {
      const cx = x0 + i * dx;
      if (n === 1) s.push(...plBird(cx - 4, 40, 2.1)); else s.push(...fsTurtle(cx - 3, 46, 1.55));
      s.push({ ...penText(cx, 92, n === 1 ? t('bird', '새') : t('tur-tle', '거-북'), { size: 15, weight: 900, fill: PEN_N, anchor: 'middle' }) });
      (n === 1 ? [cx] : [cx - 12, cx + 12]).forEach(x => s.push({ k: 'el', c: [x, 124], rx: 7.5, ry: 7.5, f: PEN_C, nw: true }));
      s.push({ ...tnHeart(cx, 170, 2.6), nw: true });
    });
    s.push({ ...penText(10, 128, t('rhythm', '리듬'), { size: 13, weight: 900, fill: PEN_C, anchor: 'start' }) });
    s.push({ ...penText(10, 144, t('the sounds', '소리들'), { size: 10, weight: 800, fill: PEN_C, anchor: 'start' }) });
    s.push({ ...penText(10, 172, t('beat', '박'), { size: 13, weight: 900, fill: PEN_N, anchor: 'start' }) });
    s.push({ ...penText(10, 188, t('steady', '꾸준해요'), { size: 10, weight: 800, fill: PEN_N, anchor: 'start' }) });
    return s;
  })();

  // p6: the pulse in the fingers: the small house's two black keys under fingers 2 and 3, one note on each beat
  const art6 = (() => {
    const s = [];
    const KX = 20, KY = 52, KW = 36;
    const K = fsKeysShapes(KX, KY, 7, KW, 118, { tints: true, sw: 2.4 });
    s.push(...K.shapes);
    const [sm, bg] = K.houses;
    s.push(...fsRoof(sm, KY - 2, 16, { label: t('small house', '작은 집'), labelSize: 11 }), ...fsRoof(bg, KY - 2, 21, { label: t('big house', '큰 집'), labelSize: 11 }));
    [[1, '2'], [2, '3']].forEach(([i, f]) => { const cx = KX + i * KW; s.push({ k: 'el', c: [cx, KY + K.BH - 16], rx: 11, ry: 11, f: PEN_C, nw: true }, { ...penText(cx, KY + K.BH - 11.5, f, { size: 13, weight: 900, fill: '#fff', anchor: 'middle' }) }); });
    const x0 = 300, dx = 30, cy = 112;
    s.push({ ...penText(x0 + 1.5 * dx, cy - 50, t('fingers', '손가락'), { size: 12, weight: 900, fill: PEN_C, anchor: 'middle' }) });
    ['2', '3', '2', '3'].forEach((f, i) => s.push(plBeat(x0 + i * dx, cy - 24, 12.5, f, { fill: true, col: PEN_C, size: 14 })));
    ['1', '2', '3', '4'].forEach((n, i) => s.push({ ...penText(x0 + i * dx, cy + 18, n, { size: 16, weight: 900, fill: PEN_N, anchor: 'middle' }) }));
    s.push({ ...penText(x0 + 1.5 * dx, cy + 44, t('say: 1 2 3 4', '말해요: 1 2 3 4'), { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' }) });
    return s;
  })();

  // the check rows' small pictures
  const chkArts = {
    steady: [...[0, 1, 2, 3].map(i => ({ k: 'el', c: [16 + i * 20, 15], rx: 5.5, ry: 5.5, f: PEN_N, nw: true })), ...[0, 1, 2].map(i => plGap(16 + i * 20, 36 + i * 20, 32, PEN_C))],
    count: ['1', '2', '3', '4'].map((n, i) => plBeat(16 + i * 20, 20, 9, n, { size: 10.5, sw: 1.7 })),
    silent: [0, 1, 2, 3].map(i => plBeat(16 + i * 20, 20, 9, String(i + 1), { fill: i < 2, silent: i >= 2, size: 10.5, sw: 1.7 })),
    rhythm: [{ k: 'el', c: [26, 10], rx: 4, ry: 4, f: PEN_C, nw: true }, { k: 'el', c: [58, 10], rx: 4, ry: 4, f: PEN_C, nw: true }, { k: 'el', c: [70, 10], rx: 4, ry: 4, f: PEN_C, nw: true }, { ...tnHeart(26, 30, 1.2), nw: true }, { ...tnHeart(64, 30, 1.2), nw: true }],
    piano: [{ k: 'rc', x: 18, y: 4, w: 56, h: 32, rx: 2, f: '#fff', s: PEN_N, sw: 1.4, nw: true }, ...[1, 2, 3].map(i => ({ ...penLine([18 + i * 14, 4], [18 + i * 14, 36], 1), nw: true })), { k: 'rc', x: 28, y: 4, w: 8, h: 19, f: PEN_N, nw: true }, { k: 'rc', x: 42, y: 4, w: 8, h: 19, f: PEN_C, nw: true }],
  };
  const checksRows = [
    ['steady', [0, 0, 92, 40], t('I can pat a steady beat: the same gap every time', '무릎을 치며 꾸준한 박을 지킬 수 있어요: 매번 똑같은 간격')],
    ['count', [0, 0, 92, 40], t('I can count out loud, 1 2 3 4, while I pat', '무릎을 치면서 소리 내어 셀 수 있어요: 1 2 3 4')],
    ['silent', [0, 0, 92, 40], t('I can keep counting through silent beats', '조용한 박에서도 계속 셀 수 있어요')],
    ['rhythm', [0, 0, 92, 40], t('I can tell the beat from the rhythm: my foot keeps the beat, my hands clap the words', '박과 리듬을 구별할 수 있어요: 발로 박을 지키며 낱말에 손뼉을 쳐요')],
    ['piano', [0, 0, 92, 40], t('I can play a new finger on each beat and count out loud', '박마다 다른 손가락으로 치면서 소리 내어 셀 수 있어요')],
  ];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Pulse & Counting', '박과 세기')}</div>
      </div></LbOnly>
      {pic(art1, [0, 26, 340, 190], t('A coral heart, your heartbeat, and beside it two rows of four beat circles, 1 2 3 4 and 1 2 3 4, with the same gap between every two: the pulse, steady, it never stops', '산호색 심장, 내 심장 박동. 그 옆에 박 동그라미 네 개씩 두 줄: 1 2 3 4, 1 2 3 4, 둘 사이마다 똑같은 간격. 박은 꾸준하고 멈추지 않아요'), 200)}
      <LbSay size={17.5}>{LANG === 'ko' ? <>음악에는 심장 박동이 있어요: <b>박</b>이에요. 박은 <b>매번 똑같은 간격</b>으로 꾸준히 이어지고, 음이 멈춰도 계속돼요. 이 챕터에서는 박을 느끼고, 소리 내어 세고, 피아노에서 계속 이어 가요.</>
        : <>Music has a heartbeat: the <b>pulse</b>. It keeps going, steady, with <b>the same gap every time</b>, even when the notes stop. In this chapter you feel it, count it out loud, and keep it going at the piano.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('A steady beat', '꾸준한 박'), 2], [t('Count out loud', '소리 내어 세기'), 3], [t('When the notes stop', '음이 멈출 때'), 4], [t('Beat or rhythm?', '박일까, 리듬일까?'), 5], [t('The pulse in your fingers', '손가락으로 박 치기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('pat a steady beat, the same gap every time', '매번 똑같은 간격으로 꾸준한 박을 칠 수 있어요'), t('count out loud, 1 2 3 4, while you pat', '무릎을 치면서 소리 내어 셀 수 있어요: 1 2 3 4'), t('keep counting through silent beats', '조용한 박에서도 계속 셀 수 있어요'), t('tell the beat from the rhythm', '박과 리듬을 구별할 수 있어요'), t('play a new finger on each beat and count out loud', '박마다 다른 손가락으로 치면서 소리 내어 셀 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkTick(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. a steady beat
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('A steady beat', '꾸준한 박')}>
      {pic(art2, [0, 30, 352, 210], t('The sister walking to the right. Beside her two trails of footprints: in the top one the same gap every time, steady, with a green tick; in the bottom one the gaps change, not steady, with a coral cross', '오른쪽으로 걸어가는 누나. 옆에 발자국 두 줄: 윗줄은 매번 똑같은 간격으로 꾸준해요, 초록 체크. 아랫줄은 간격이 바뀌어 들쭉날쭉해요, 산호색 엑스'), 230)}
      <LbSay>{LANG === 'ko' ? <><b>꾸준한 박</b>은 <b>간격이 매번 똑같아요</b>. 심장 박동처럼, 똑딱거리는 시계처럼, 걸어갈 때 내 발걸음처럼요. 꾸준하지 않으면 간격이 바뀌어요: 빨라졌다, 느려졌다, 멈췄다, 다시 가요. 음악의 박은 꾸준해요.</>
        : <>A <b>steady beat</b> has <b>the same gap every time</b>, like your heartbeat, a ticking clock, or your feet when you walk. Not steady means the gaps change: faster, slower, stop, go. The pulse of music is steady.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>두 손으로 무릎을 꾸준하게 8번 쳐요: 매번 똑같은 간격으로, 시계처럼.</>,
        <>방을 가로질러 8걸음 걸어요: 박 하나에 한 걸음, 매번 똑같은 간격으로.{A('B3', <> 그다음 8걸음 더 천천히, 그래도 꾸준하게.</>)}</>,
      ] : [
        <>Pat your knees with both hands, 8 times, steady: the same gap every time, like a clock.</>,
        <>Walk 8 steps across the room: one step on each beat, the same gap every time.{A('B3', <> Then 8 more, slower, still steady.</>)}</>,
      ]}/>
      <LbRemember>{t('A steady beat: the same gap every time.', '꾸준한 박: 매번 똑같은 간격.')}</LbRemember>
    </LbPage>,

    // 3. count out loud
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Count out loud', '소리 내어 세기')}>
      {pic(art3, [0, 28, 340, 222], t('The brother says 1, 2, 3, 4! Beside him four beat circles in a ring, 1 2 3 4, with arrows round the ring: from 4 a coral arrow goes back to 1', '남동생이 1, 2, 3, 4! 하고 말해요. 옆에 박 동그라미 네 개가 동그랗게: 1 2 3 4, 화살표가 돌아가고 4에서 산호색 화살표가 다시 1로'), 210)}
      <LbSay>{LANG === 'ko' ? <>박마다 번호를 붙여요: <b>1 2 3 4</b>, 그리고 다시 1부터. 소리 내어, 박 하나에 숫자 하나씩, 빠르지도 느리지도 않게 말해요. 소리 내어 세면 박이 꾸준해지고, 나중에는 음이 어디에 오는지도 알려 줘요.</>
        : <>Give every beat a number: <b>1 2 3 4</b>, then start again at 1. Say it out loud, one number on each beat, not faster and not slower. Counting out loud keeps the beat steady, and later it tells you where every note goes.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>무릎을 치면서 소리 내어 세요: 1 2 3 4를 네 번, 멈추지 않고.</>,
        <>오른손 3번 손가락을 넷째 작은 집의 오른쪽 검은건반에 올려요. 박마다 한 번씩 치면서 세요: 1 2 3 4를 네 번.</>,
      ] : [
        <>Pat your knees and count out loud: 1 2 3 4, four times round, without stopping.</>,
        <>Right hand: finger 3 on the right black key of the 4th small house. Play it on every beat and count: 1 2 3 4, four times round.</>,
      ]}/>
      <LbRemember>{t('Count out loud: 1 2 3 4, then 1 again.', '소리 내어 세기: 1 2 3 4, 그리고 다시 1.')}</LbRemember>
    </LbPage>,

    // 4. when the notes stop
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('When the notes stop', '음이 멈출 때')}>
      {pic(art4, [0, 52, 396, 196], t('Eight beat circles in two groups, 1 2 3 4 and 1 2 3 4: on 1 and 2 navy, play; on 3 and 4 dashed, count only. Under every circle a coral heart: the pulse goes on', '박 동그라미 여덟 개, 1 2 3 4와 1 2 3 4: 1과 2는 남색, 치기. 3과 4는 점선, 세기만. 동그라미마다 아래에 산호색 심장: 박은 계속돼요'), 190)}
      <LbSay>{LANG === 'ko' ? <>치는 걸 멈춰도 박은 멈추지 않아요. 1과 2에서 치고, 3과 4에서는 손을 들고 계속 세요: <b>조용한 박에서도 계속 세요</b>. 그래야 제때 다시 들어가요.</>
        : <>The pulse does not stop when you stop playing. Play on 1 and 2, lift your hand on 3 and 4, and keep counting: <b>the silent beats still count</b>. Then you come back in at the right time.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 3번 손가락, 넷째 작은 집의 오른쪽 검은건반: 1과 2에서 치고, 3과 4에서는 손을 들고, 계속 소리 내어 세요. 네 번.</>,
        <>이번에는 1에서만 쳐요. 2 3 4는 손을 건반 바로 위에 띄우고 세요. 네 번.</>,
      ] : [
        <>Right hand, finger 3 on the right black key of the 4th small house: play on 1 and 2, lift on 3 and 4, and keep counting out loud. Four times round.</>,
        <>Now play only on 1, and count 2 3 4 with your hand just above the key. Four times round.</>,
      ]}/>
      <LbRemember>{t('Silent beats still count.', '조용한 박에서도 계속 세요.')}</LbRemember>
    </LbPage>,

    // 5. beat or rhythm?
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Beat or rhythm?', '박일까, 리듬일까?')}>
      {pic(art5, [0, 14, 380, 190], t('Four beats, four coral hearts in a row. Over them four words: bird, tur-tle, bird, tur-tle, with the bird and the turtle drawn above them. One coral dot for each sound: one over bird, two over tur-tle', '박 넷, 산호색 심장 네 개가 한 줄로. 그 위에 낱말 넷: 새, 거-북, 새, 거-북, 그 위에 새와 거북 그림. 소리마다 산호색 점 하나: 새 위에 하나, 거-북 위에 둘'), 230)}
      <LbSay>{LANG === 'ko' ? <><b>박</b>은 아래에서 꾸준하게 이어져요. <b>리듬</b>은 그 위에 있는 소리들의 모양이에요: 낱말 소리처럼 길기도 하고 짧기도 해요. 박 하나에 {A('B7', <><b>새</b>라고 말하면 소리 하나, <b>거-북</b>이라고 말하면 소리 둘</>)}. 박은 그대로, 리듬은 바뀌어요.</>
        : <>The <b>beat</b> is the steady pulse underneath. The <b>rhythm</b> is the pattern of sounds on top, long and short, like the sounds of words. {A('B7', <>Say <b>bird</b> on one beat: one sound. Say <b>tur-tle</b> on one beat: two sounds.</>)} The beat stays the same; the rhythm changes.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>발로 바닥을 톡톡 치며 박을 지키고 말해요: 새, 거-북, 새, 거-북. 박마다 낱말 하나. 그다음 발은 박을 지키고, 낱말 소리마다 손뼉을 쳐요.</>,
        <>이번엔: 거-북, 거-북, 새, 새. 그리고: 등-대, 새, 등-대, 새.</>,
      ] : [
        <>Tap the beat with your foot and say: bird, tur-tle, bird, tur-tle, one word on each beat. Then clap the words while your foot keeps the beat.</>,
        <>Now: tur-tle, tur-tle, bird, bird. And: light-house, bird, light-house, bird.</>,
      ]}/>
      <LbRemember>{t('The beat stays steady; the rhythm is the sounds on top.', '박은 꾸준하게, 리듬은 그 위의 소리.')}</LbRemember>
    </LbPage>,

    // 6. the pulse in your fingers
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('The pulse in your fingers', '손가락으로 박 치기')}>
      {pic(art6, [0, 14, 440, 170], t('The small house and the big house of black keys. Fingers 2 and 3 on the small house\'s two black keys. Beside it, the coral finger circles 2 3 2 3 over the count 1 2 3 4: a new finger on each beat, counted out loud', '검은건반의 작은 집과 큰 집. 작은 집의 검은건반 두 개에 2번과 3번 손가락. 옆에 산호색 손가락 동그라미 2 3 2 3, 그 아래 세는 숫자 1 2 3 4: 박마다 다른 손가락, 소리 내어 세요'), 200)}
      <LbSay>{LANG === 'ko' ? <>이제 손가락이 번갈아 쳐요: 박마다 다른 손가락. 소리 내어 세면서 쳐요: 1 2 3 4. 산호색 동그라미 안의 숫자는 손가락 번호예요.</>
        : <>Now your fingers take turns: a new finger on each beat. Count out loud as you play: 1 2 3 4. The numbers in the coral circles are finger numbers.</>}</LbSay>
      <LbTune name={t('Small-house beat', '작은 집 박')} coral how={t('right hand, fingers 2 and 3 on the 4th small house; play the row twice, counting 1 2 3 4', '오른손, 넷째 작은 집에 2번과 3번 손가락; 1 2 3 4를 세면서 줄을 두 번')} seq={['2', '3', '2', '3', '2', '3', '2', '3']}/>
      <LbTune name={t('Big-house beat', '큰 집 박')} coral how={t('right hand, fingers 2 3 4 on the big house next to it; play the row twice, counting 1 2 3 4', '오른손, 바로 옆 큰 집에 2번 3번 4번 손가락; 1 2 3 4를 세면서 줄을 두 번')} seq={['2', '3', '4', '3', '2', '3', '4', '3']}/>
      <LbTune name={t('Left-hand beat', '왼손 박')} coral how={t('left hand, fingers 3 and 2 on the 3rd small house; play the row twice, counting 1 2 3 4', '왼손, 셋째 작은 집에 3번과 2번 손가락; 1 2 3 4를 세면서 줄을 두 번')} seq={['3', '2', '3', '2', '3', '2', '3', '2']}/>
      <LbRemember>{t('A new finger on each beat; keep counting.', '박마다 다른 손가락, 계속 세면서.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, then tick how it is going: not yet, nearly, or got it! The check-up on paper is in the Workbook.', '피아노 앞에서 하나씩 보여 주고 어떤지 표시해요: 아직, 거의, 됐어요! 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_pl_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
    </LbPage>,
  ];
}
function PulseLessonBook() { return <>{plLbPages(false)}</>; }
