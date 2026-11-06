// ─── Phase 461: chapter 8 (Time Signatures): the Lesson Book, draft v1 (?book=lesson&ch=time-signatures; drills.src.html unchanged) ───
// The level plan's scope for room 8 (Level 2): bar lines, the double bar line and the repeat sign; 2/4 3/4 4/4; strong and
// weak beats; filling a bar; rests on the staff; a tie across the bar line. 6/8 and cut time wait for the drill's higher
// levels (and Book rule 13's 2/8 4/8 4/2 6/4 9/4 12/4, 5/8 7/8 7/4). It builds on Notes & Rests (chapter 5: the note values
// and their rests, hearts for beats, the sound line, held beats lighter, 1 + 2 +) and Reading the Staff (chapter 6: the
// treble clef, G on line 2). The rhythms sit on G, so pitch never gets in the way (B3).
// Short and plain (Book rule 7), real names (rule 8), set tasks (rule 3), counting as the time signature counts (rule 12).

// one row on the treble staff, drawn inside SfStaff's extra(yOf). items: [kind, beats] notes and rests ('w' 'hd' 'h' 'q'
// 'p' 'r' 'hr' 'wr'), ['|'] a bar line, ['||'] the double bar line, [':||'] the repeat sign, ['ts', top] a time
// signature, ['C'] common time. o: x0, D (px a beat), ties [[i, j]] (item indexes), counts (true | false), strong
// (beat 1 a big heart), hl (an item index drawn coral), y offsets. Returns the raw SVG and the beats' x.
function tsRaw(yOf, items, o = {}) {
  const D = o.D || 34, G = (d) => yOf(d, 'treble'), col = PEN_N, cor = PEN_C;
  const out = [], beatXs = [], noteX = {}, under = [];
  let x = o.x0 || 46, top = 4, inBar = 0, last = 0;
  const line = (xx, w = 1.5) => '<line x1="' + pFix(xx) + '" x2="' + pFix(xx) + '" y1="' + pFix(G(38)) + '" y2="' + pFix(G(30)) + '" stroke="' + col + '" stroke-width="' + w + '"/>';
  items.forEach((it, i) => {
    const k = it[0];
    if (k === 'ts') { top = it[1];
      [[it[1], G(36), o.topCoral ? cor : col], [4, G(32), col]].forEach(([n, y, c]) => out.push('<text x="' + pFix(x + 8) + '" y="' + pFix(y + 7.6) + '" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="25" font-weight="900" fill="' + c + '">' + n + '</text>'));
      x += 26; return; }
    if (k === 'C') { top = 4; out.push('<text x="' + pFix(x + 9) + '" y="' + pFix(G(34) + 8) + '" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="27" font-weight="900" fill="' + col + '">C</text>'); x += 28; return; }
    if (k === '|') { out.push(line(x + 2)); last = x + 2.8; x += 12; inBar = 0; return; }
    if (k === '||') { out.push(line(x + 1, 1.3), line(x + 6, 4)); last = x + 8; x += 10; return; }
    if (k === ':||') { out.push('<circle cx="' + pFix(x) + '" cy="' + pFix(G(35)) + '" r="2.3" fill="' + col + '"/><circle cx="' + pFix(x) + '" cy="' + pFix(G(33)) + '" r="2.3" fill="' + col + '"/>', line(x + 6, 1.3), line(x + 11, 4)); last = x + 13; x += 16; return; }
    const n = it[1], nx = x + 12, c = o.hl === i ? cor : col;
    if (k === 'p') out.push(nvbPair(nx - 2, nx + D * 0.5 - 2, G(32), { col: c }).svg);
    else if (k === 'r') out.push(nvbRest(nx + 2, G(34), 'q', { k: 0.82, col: c }).svg);
    else if (k === 'hr') out.push('<rect x="' + pFix(nx - 5) + '" y="' + pFix(G(34) - 5) + '" width="16" height="5" fill="' + c + '"/>');
    else if (k === 'wr') out.push('<rect x="' + pFix(x + 12 + (n - 1) * D / 2 - 8) + '" y="' + pFix(G(36)) + '" width="16" height="5" fill="' + c + '"/>');
    else out.push(nvbNote(nx, G(32), k === 'hd' ? 'h' : k, { col: c }).svg + (k === 'hd' ? '<circle cx="' + pFix(nx + 14) + '" cy="' + pFix(G(33)) + '" r="2.6" fill="' + c + '"/>' : ''));
    noteX[i] = nx;
    const tiedIn = (o.ties || []).some(([, tb]) => tb === i);
    for (let b = 0; b < n; b++) beatXs.push({ tied: b === 0 && tiedIn, x: nx + b * D, n: (inBar + b) % top + 1, held: b > 0 && !['r', 'hr', 'wr'].includes(k), rest: ['r', 'hr', 'wr'].includes(k), pair: k === 'p' && b === 0, px: nx + D * 0.5 - 2 });
    inBar += n; x += n * D;
  });
  (o.ties || []).forEach(([a, b]) => { const x1 = noteX[a] + 2, x2 = noteX[b] - 2, y = G(32) + 6.5;
    out.push('<path d="M' + pFix(x1) + ' ' + pFix(y) + ' Q' + pFix((x1 + x2) / 2) + ' ' + pFix(y + 11) + ' ' + pFix(x2) + ' ' + pFix(y) + '" fill="none" stroke="' + cor + '" stroke-width="2.2" stroke-linecap="round"/>'); });
  const yH = G(30) + (o.dyH || 30), yC = yH + (o.strong ? 31 : 26);
  if (o.hearts !== false) beatXs.forEach((bt, j) => {
    const big = o.strong && bt.n === 1, mid = o.strong && o.mid && bt.n === 3, s = big ? 2.3 : mid ? 1.75 : 1.45;
    under.push('<path d="M0 5 Q-7.5 -0.5 -5 -4.2 Q-2.4 -6.8 0 -3 Q2.4 -6.8 5 -4.2 Q7.5 -0.5 0 5 Z" transform="translate(' + pFix(bt.x) + ' ' + pFix(yH) + ') scale(' + s + ')" fill="' + (o.strong && !big && !mid ? '#fff' : cor) + '" stroke="' + cor + '" stroke-width="' + (1.2 / s) + '"/>');
    if (o.counts !== false) {
      const fill = bt.held || bt.tied ? 'rgba(38,41,107,0.38)' : col;
      if (bt.rest) under.push('<circle cx="' + pFix(bt.x) + '" cy="' + pFix(yC - 5.5) + '" r="10.5" fill="#fff" stroke="' + col + '" stroke-width="1.4" stroke-dasharray="3.2 2.6"/>');
      under.push('<text x="' + pFix(bt.x) + '" y="' + pFix(yC) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + (o.strong && bt.n === 1 ? 17 : 15) + '" font-weight="900" fill="' + fill + '">' + bt.n + '</text>');
      if (bt.pair) under.push('<text x="' + pFix(bt.px) + '" y="' + pFix(yC) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="15" font-weight="900" fill="' + col + '">+</text>');
    }
  });
  return { raw: out.join('') + under.join(''), beatXs, end: x, last: last || x };
}
// a staff with one row: SfStaff draws the lines and the clef, tsRaw the rest
// the staff ends at the last bar line; ref: the width that fills the picture, so every staff of a page has one scale
function TsStaff({ items, width = 400, o = {}, label, pad, extra }) {
  const m = tsRaw((d) => dY(d), items, o), vbw = Math.ceil(m.last + 6);
  return <div style={{width:Math.min(100, vbw / width * 100) + '%'}}><SfStaff clef="treble" width={vbw} span={[4, m.last]} pad={pad || [extra ? 34 : 16, 66]} label={label}
    extra={(yOf, layer, txt) => layer === 'over' && <g><g dangerouslySetInnerHTML={{ __html: tsRaw(yOf, items, o).raw }}/>{extra && extra(yOf, txt)}</g>}/></div>;
}
const tsQ = (n) => Array.from({ length: n }, () => ['q', 1]);

function tsLbPages(scr = false) {
  const ch = 'time-signatures';
  const A = (q, kids) => <LbAsk q={q}>{kids}</LbAsk>;
  const pic = (node, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div></LbPic>;
  const stack = (nodes, h, mw = 560) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap:8,width:'100%',maxWidth:mw,margin:'0 auto'}}>{nodes}</div></LbPic>;
  const tag = (x, y, s, c = BK.coral, a = 'middle') => (yOf, txt) => <text x={x} y={typeof y === 'function' ? y(yOf) : y} textAnchor={a} fontSize="11.5" fontWeight="900" fill={c} style={txt}>{s}</text>;
  const tags = (...fs) => (yOf, txt) => <g>{fs.map((f, i) => <g key={i}>{f(yOf, txt)}</g>)}</g>;
  const nvNo = bkChapterNo('note-values'), sfNo = bkChapterNo('staff');
  const C1 = '1 2 3 4';

  // p1: two bars of 4/4 with their hearts and the count, the time signature and the double bar line marked
  const p1 = <TsStaff width={420} items={[['ts', 4], ['q', 1], ['q', 1], ['h', 2], ['|'], ['q', 1], ['q', 1], ['q', 1], ['q', 1], ['||']]} o={{ D: 38 }}
    label={t('The treble staff with the time signature 4 over 4 and two bars of notes on G, a bar line between them and a double bar line at the end. A coral heart under every beat and the count 1 2 3 4 in each bar.', '박자표 4/4와 G 위의 음표 두 마디가 있는 높은음자리표 오선, 마디 사이에 세로줄, 끝에 겹세로줄. 박마다 산호색 심장, 마디마다 1 2 3 4.')}
    extra={tags(tag(62, (yOf) => yOf(40, 'treble') - 6, t('time signature', '박자표')), tag(226, (yOf) => yOf(40, 'treble') - 6, t('bar line', '세로줄')), tag(400, (yOf) => yOf(40, 'treble') - 6, t('double bar line', '끝세로줄'), BK.coral, 'end'))}/>;

  // p2: bars and bar lines: three bars of 3/4; a bar line, then the repeat sign
  const p2a = <TsStaff width={420} items={[['ts', 3], ['q', 1], ['q', 1], ['q', 1], ['|'], ['h', 2], ['q', 1], ['|'], ['hd', 3], ['||']]} o={{ D: 34 }}
    label={t('Three bars of 3/4 on G, with bar lines between them and a double bar line at the end. Under each bar its three hearts and the count 1 2 3.', 'G 위의 3/4 세 마디, 마디 사이에 세로줄, 끝에 겹세로줄. 마디마다 심장 셋과 1 2 3.')}
    extra={tags(tag(122, (yOf) => yOf(40, 'treble') - 6, t('bar 1', '1마디')), tag(236, (yOf) => yOf(40, 'treble') - 6, t('bar 2', '2마디')), tag(350, (yOf) => yOf(40, 'treble') - 6, t('bar 3', '3마디')))}/>;
  const p2b = <TsStaff width={420} items={[['ts', 3], ['q', 1], ['q', 1], ['q', 1], ['|'], ['hd', 3], [':||']]} o={{ D: 34, hearts: false }} pad={[34, 16]}
    label={t('Two bars of 3/4 ending in a repeat sign: two dots before a double bar line. Play it again.', '반복 기호로 끝나는 3/4 두 마디: 겹세로줄 앞의 점 두 개. 한 번 더 쳐요.')}
    extra={tags(tag(300, (yOf) => yOf(40, 'treble') - 6, t('repeat sign: play it again', '도돌이표: 한 번 더'), BK.coral, 'end'))}/>;

  // p3: the two numbers: one bar each of 2/4, 3/4 and 4/4
  const p3 = [2, 3, 4, 'C'].map(n => n === 'C' ? <TsStaff key={n} width={330} items={[['C'], ...tsQ(4), ['||']]} o={{ D: 46 }} pad={[30, 62]}
    label={t('A bar of common time: the sign C instead of 4/4, four crotchets counted 1 2 3 4.', '보통박자 한 마디: 4/4 대신 C, 4분음표 넷을 1 2 3 4로 세요.')}
    extra={(yOf, txt) => <text x="58" y={yOf(40, 'treble') - 6} textAnchor="start" fontSize="11.5" fontWeight="900" fill={BK.coral} style={txt}>{t('C = 4/4, common time', 'C = 4/4, 보통박자')}</text>}/> : <TsStaff key={n} width={330} items={[['ts', n], ...tsQ(n), ['||']]} o={{ D: 46, topCoral: true }} pad={[12, 62]}
    label={t('A bar of ' + n + '/4, the top number ' + n + ' in coral: ' + n + ' crotchets over ' + n + ' hearts, counted ' + Array.from({ length: n }, (_, i) => i + 1).join(' ') + '.', n + '/4 한 마디: 심장 ' + n + '개 위의 4분음표 ' + n + '개, ' + Array.from({ length: n }, (_, i) => i + 1).join(' ') + '로 세요.')}
/>);

  // p4: strong and weak beats: 3/4 and 4/4, beat 1 a big heart (and 3 a middle one in 4/4)
  const p4 = [[3, t('strong, weak, weak', '강, 약, 약')], [4, t('strong, weak, medium, weak', '강, 약, 중간, 약')]].map(([n, w]) => <TsStaff key={n} width={420} items={[['ts', n], ...tsQ(n), ['|'], ...tsQ(n), ['||']]} o={{ D: 36, strong: true, mid: n === 4 }} pad={[34, 68]}
    label={t('Two bars of ' + n + '/4 on G. Beat 1 of each bar has a big coral heart' + (n === 4 ? ', beat 3 a middle one' : '') + ', the other beats small hearts: ' + w + '.', n + '/4 두 마디. 마디마다 1박은 큰 산호색 심장' + (n === 4 ? ', 3박은 중간 심장' : '') + ', 나머지는 작은 심장: ' + w + '.')}
    extra={tags(tag(60, (yOf) => yOf(40, 'treble') - 6, w, BK.coral, 'start'))}/>);

  // p5: fill the bar: notes and rests on the staff, each bar adding up to the top number
  const p5a = <TsStaff width={470} items={[['ts', 4], ['q', 1], ['r', 1], ['h', 2], ['|'], ['hr', 2], ['q', 1], ['q', 1], ['|'], ['wr', 4], ['||']]} o={{ D: 30 }}
    label={t('Three bars of 4/4 on G: a crotchet, a crotchet rest standing in the middle of the staff and a minim; a minim rest sitting on line 3 and two crotchets; a semibreve rest hanging from line 4, a whole bar of silence. The beats of the rests are dashed circles.', '4/4 세 마디: 4분음표, 오선 가운데의 4분쉼표, 2분음표; 3번 줄 위에 앉은 2분쉼표와 4분음표 둘; 4번 줄에 매달린 온쉼표, 한 마디 내내 쉼. 쉼표의 박은 점선 동그라미.')}/>;
  const p5b = <TsStaff width={470} items={[['ts', 3], ['h', 2], ['r', 1], ['|'], ['q', 1], ['p', 1], ['q', 1], ['|'], ['hd', 3], ['||']]} o={{ D: 40 }} pad={[16, 66]}
    label={t('Three bars of 3/4: a minim and a crotchet rest; a crotchet, two quavers and a crotchet; a dotted minim. Each bar adds up to 3.', '3/4 세 마디: 2분음표와 4분쉼표; 4분음표, 8분음표 둘, 4분음표; 점2분음표. 마디마다 3박.')}/>;

  // p6: the tie: a minim tied over the bar line to a crotchet
  const p6a = <TsStaff width={420} items={[['ts', 4], ['q', 1], ['q', 1], ['h', 2], ['|'], ['q', 1], ['q', 1], ['h', 2], ['||']]} o={{ D: 36, ties: [[3, 5]] }}
    label={t('Two bars of 4/4 on G. A coral tie joins the minim at the end of bar 1 to the crotchet at the start of bar 2: play the minim, then hold through beat 1 of bar 2. The held numbers, 4 and the next 1, are lighter.', '4/4 두 마디. 산호색 붙임줄이 1마디 끝의 2분음표와 2마디 첫 4분음표를 이어요: 2분음표를 치고 2마디 1박까지 누르고 있어요. 누르는 박의 숫자는 연하게.')}
    extra={tags(tag(206, (yOf) => yOf(40, 'treble') - 6, t('the tie crosses the bar line', '붙임줄이 세로줄을 건너가요'), BK.coral))}/>;

  const chkArts = {
    bars: [nvbNote(12, 30, 'q', { k: 0.6 }), penLine([28, 10], [28, 40], 1.4, PEN_N), nvbNote(44, 30, 'q', { k: 0.6 }), penLine([62, 10], [62, 40], 1.1, PEN_N), penLine([66, 10], [66, 40], 3, PEN_N), { k: 'raw', svg: '<circle cx="57" cy="21" r="1.6" fill="' + PEN_N + '"/><circle cx="57" cy="29" r="1.6" fill="' + PEN_N + '"/>' }],
    top: [{ ...penText(20, 22, '3', { size: 18, weight: 900, fill: PEN_C, anchor: 'middle' }) }, { ...penText(20, 40, '4', { size: 18, weight: 900, fill: PEN_N, anchor: 'middle' }) }, ...[1, 2, 3].map(n => ({ ...penText(38 + n * 12, 32, String(n), { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' }) }))],
    strong: [{ ...tnHeart(18, 22, 2.4, PEN_C), nw: true }, { ...tnHeart(46, 24, 1.5, PEN_C, true), nw: true }, { ...tnHeart(70, 24, 1.5, PEN_C, true), nw: true }],
    fill: [nvbNote(14, 30, 'h', { k: 0.6 }), nvbRest(40, 24, 'q', { k: 0.55 }), { ...penText(70, 30, '= 3', { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    tie: [nvbNote(16, 26, 'h', { k: 0.6 }), nvbNote(60, 26, 'q', { k: 0.6 }), { k: 'raw', svg: '<path d="M20 33 Q39 41 57 33" fill="none" stroke="' + PEN_C + '" stroke-width="2"/>' }],
  };
  const checksRows = [
    ['bars', [0, 0, 92, 40], t('I can show the bar lines, the double bar line and the repeat sign', '세로줄, 끝세로줄, 도돌이표를 짚을 수 있어요')],
    ['top', [0, 0, 92, 40], t('I can read the top number and count each bar', '위 숫자를 읽고 마디마다 셀 수 있어요')],
    ['strong', [0, 0, 92, 40], t('I can play beat 1 a little stronger', '1박을 조금 더 세게 칠 수 있어요')],
    ['fill', [0, 0, 92, 40], t('I can count the notes and rests in a bar', '마디 안의 음표와 쉼표를 셀 수 있어요')],
    ['tie', [0, 0, 92, 40], t('I can play a tie: once, then hold', '붙임줄을 칠 수 있어요: 한 번 치고 누르기')],
  ];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Time Signatures', '박자표')}</div>
      </div></LbOnly>
      {pic(p1, 220, 640)}
      <LbSay size={17.5}>{LANG === 'ko' ? <>음악은 <b>마디</b>로 나뉘어요. 처음에 있는 <b>박자표</b>가 한 마디에 몇 박이 들어가는지 알려 줘요.</>
        : <>Music is cut into <b>bars</b>. The <b>time signature</b> at the start says how many beats each bar holds.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Bars and bar lines', '마디와 세로줄'), 2], [t('The two numbers', '두 숫자'), 3], [t('Strong and weak beats', '강한 박과 약한 박'), 4], [t('Fill the bar', '마디 채우기'), 5], [t('The tie', '붙임줄'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, , x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkTick(15)}<span>{x.replace(/^I can /, '').replace(/ 수 있어요$/, ' 수 있어요')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. bars and bar lines (and the repeat sign)
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Bars and bar lines', '마디와 세로줄')}>
      {stack([<div key="a">{p2a}</div>, <div key="b">{p2b}</div>], 250, 620)}
      <LbSay>{LANG === 'ko' ? <><b>세로줄</b>이 음악을 <b>마디</b>로 나눠요. 마디마다 같은 수의 박이 들어가요. <b>끝세로줄</b>은 끝이에요. 그 앞에 점이 두 개 있으면 <b>도돌이표</b>예요. 처음으로 돌아가서 한 번 더 쳐요.</>
        : <>A <b>bar line</b> cuts the music into <b>bars</b>. Each bar holds the same number of beats. Its other name is a measure. A <b>double bar line</b> is the end. With two dots before it, it is a <b>repeat sign</b>: go back to the start and play it again.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 3번 손가락, G: 마디마다 1 2 3을 세면서 위의 세 마디를 쳐요.</>,
        <>오른손 3번 손가락, G: 도돌이표가 있는 두 마디를 1 2 3으로 세면서 쳐요. 처음으로 돌아가 한 번 더. 모두 네 마디예요.</>,
      ] : [
        <>Right hand, finger 3 on G: play the three bars, counting 1 2 3 in each bar.</>,
        <>Right hand, finger 3 on G: play the two bars with the repeat sign, counting 1 2 3. Go back and play them again. Four bars in all.</>,
      ]}/>
      <LbRemember>{t('Bar lines make bars. Two dots: play it again.', '세로줄은 마디를 만들어요. 점 두 개: 한 번 더.')}</LbRemember>
    </LbPage>,

    // 3. the two numbers
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The two numbers', '두 숫자')}>
      {stack(p3.map((s, i) => <div key={i}>{s}</div>), 390, 360)}
      <LbSay>{LANG === 'ko' ? <><b>박자표</b>에는 숫자가 둘 있어요. <b>위 숫자</b>: 한 마디의 박 수. <b>아래 숫자</b> 4: 4분음표가 한 박. 4/4는 <b>C</b>로도 써요. {A('B2', <>다른 이름은 보통박자예요.</>)}</>
        : <>A <b>time signature</b> has two numbers. The <b>top number</b>: how many beats in each bar. The <b>bottom number</b> 4: each beat is a crotchet. 4/4 can also be written <b>C</b>. {A('B2', <>Its other name is common time.</>)}</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 3번 손가락, G: 2/4 네 마디, 3/4 네 마디, 4/4 네 마디. 소리 내어 세요: 1 2, 1 2 3, {C1}.</>,
        <>선생님이 박자표 카드를 보여 주면, 위 숫자만큼 무릎을 치고 1로 돌아가요. 두 마디씩.</>,
      ] : [
        <>Right hand, finger 3 on G: four bars of 2/4, four of 3/4, four of 4/4. Count out loud: 1 2, 1 2 3, {C1}.</>,
        <>Your teacher shows a time signature card. Pat your knees up to the top number, then back to 1. Two bars each.</>,
      ]}/>
      <LbRemember>{t('Top: beats in a bar. Bottom 4: a crotchet beat.', '위: 한 마디의 박 수. 아래 4: 4분음표가 한 박.')}</LbRemember>
    </LbPage>,

    // 4. strong and weak beats
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Strong and weak beats', '강한 박과 약한 박')}>
      {stack(p4.map((s, i) => <div key={i}>{s}</div>), 290, 620)}
      <LbSay>{LANG === 'ko' ? <>마디의 <b>1박</b>은 <b>강한 박</b>이에요. 조금 더 세게 쳐요: <b>1</b> 2 3. {A('B4', <>4/4에서는 3박이 중간 박이에요.</>)}</>
        : <>Beat <b>1</b> of every bar is the <b>strong beat</b>. Play it a little louder: <b>1</b> 2 3. {A('B4', <>In 4/4, beat 3 is a medium beat.</>)}</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>{A('B5', <>1에서 무릎을 치고, 나머지 박에서 손뼉을 쳐요. 소리 내어 세요. 2/4, 3/4, 4/4를 네 마디씩.</>)}</>,
        <>오른손 3번 손가락, G: 박마다 4분음표, 1박은 조금 더 세게. 3/4 네 마디, 그다음 4/4 네 마디.</>,
      ] : [
        <>{A('B5', <>Pat your knees on 1 and clap on the other beats. Count out loud. Four bars each of 2/4, 3/4 and 4/4.</>)}</>,
        <>Right hand, finger 3 on G: a crotchet on every beat, beat 1 a little louder. Four bars of 3/4, then four of 4/4.</>,
      ]}/>
      <LbRemember>{t('Beat 1 is strong.', '1박은 강한 박.')}</LbRemember>
    </LbPage>,

    // 5. fill the bar; rests on the staff
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Fill the bar', '마디 채우기')}>
      {stack([<div key="a">{p5a}</div>, <div key="b">{p5b}</div>], 300, 640)}
      <LbSay>{LANG === 'ko' ? <>마디마다 음표와 쉼표를 더하면 <b>위 숫자</b>가 돼요. 4분쉼표는 오선 <b>가운데</b>에 서요. 2분쉼표는 <b>3번 줄 위에 앉아요</b>. 온쉼표는 <b>4번 줄에 매달려요</b>. {A('B6', <>4/4에서 온쉼표는 한 마디 내내 쉬어요.</>)}</>
        : <>In every bar, the notes and rests add up to the <b>top number</b>. The crotchet rest stands in the <b>middle</b> of the staff. The minim rest <b>sits on line 3</b>. The semibreve rest <b>hangs from line 4</b>. {A('B6', <>In 4/4, a semibreve rest is a whole bar of silence.</>)}</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 3번 손가락, G: 위의 4/4 세 마디를 쳐요. 쉼표에서는 손을 건반 바로 위에 띄우고 계속 세요.</>,
        <>오른손 3번 손가락, G: 3/4 세 마디를 소리 내어 세면서 쳐요. 8분음표 둘은 2 +.</>,
      ] : [
        <>Right hand, finger 3 on G: play the three bars of 4/4. In the rests, lift your hand just above the key and keep counting.</>,
        <>Right hand, finger 3 on G: play the three bars of 3/4 and count out loud. Two quavers are 2 +.</>,
      ]}/>
      <LbRemember>{t('Notes and rests fill each bar exactly.', '음표와 쉼표가 마디를 꼭 맞게 채워요.')}</LbRemember>
    </LbPage>,

    // 6. the tie
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('The tie', '붙임줄')}>
      {pic(p6a, 230, 640)}
      <LbSay>{LANG === 'ko' ? <><b>붙임줄</b>은 같은 줄이나 칸의 두 음표를 이어요. 첫 음을 치고, 두 번째 음이 끝날 때까지 누르고 있어요. 붙임줄은 세로줄을 건너갈 수 있어요.</>
        : <>A <b>tie</b> joins two notes on the same line or space. Play the first, then hold it through the second. A tie can cross a bar line.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 3번 손가락, G: 위의 두 마디를 쳐요. 2분음표는 2마디 1박까지 누르고, 연한 숫자도 소리 내어 세요.</>,
        <>오른손 3번 손가락, G: 이번엔 붙임줄 없이 쳐요. 2마디 1박에서 G를 다시 쳐요. 두 소리를 비교해요.</>,
      ] : [
        <>Right hand, finger 3 on G: play the two bars. Hold the minim through beat 1 of bar 2, and count the light numbers out loud too.</>,
        <>Right hand, finger 3 on G: play the two bars again without the tie. Play G again on beat 1 of bar 2. Hear the difference.</>,
      ]}/>
      <LbRemember>{t('A tie: play once, hold for both.', '붙임줄: 한 번 치고, 두 음표만큼 누르고 있어요.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano. Colour a circle: not yet, nearly, or got it! The check-up on paper is in the Workbook.', '피아노 앞에서 하나씩 보여 줘요. 동그라미를 칠해요: 아직, 거의, 됐어요! 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, vb, x]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_ts_v1" rows={checksRows.map(([a, vb, x]) => [{ shapes: chkArts[a], vb }, x])}/>}/>
    </LbPage>,
  ];
}
function TimeSignaturesLessonBook() { return <>{tsLbPages(false)}</>; }
