// ─── Phase 464: chapter 8 (Time Signatures): the Lesson Book, built in full with B1-B12 as recommended (her 2026-10-13
// 23:51 '지금부터 추천대로 다 가줘'; Book rule 15), every explanation like a dictionary (Book rule 14). Draft v1: Phase 461.
// The level plan's scope for room 8 (Level 2): bar lines, the double bar line and the repeat sign; 2/4 3/4 4/4 and C;
// strong and weak beats; filling a bar; rests on the staff; a tie across the bar line. 6/8, cut time and the bottom
// number are the drill's higher levels (B1, Book rule 13). It builds on Notes & Rests (chapter 5: the note values and
// their rests, hearts for beats, held beats lighter, 1 + 2 +) and Reading the Staff (chapter 6: the treble clef, G on
// line 2). The rhythms sit on G, so pitch never gets in the way (B3). AMEB Theory: 2/4 3/4 4/4 C, the tie, the bar line
// and the double bar line at Grade 1, the repeat sign and the whole-bar rest at Grade 2; ABRSM: 2/4 3/4 4/4 and ties at
// Grade 1.

// Book rule 14 (her 2026-10-13 23:51 '모든 설명을 사전처럼 깔끔하게'): the lesson's words as dictionary entries, the term
// in bold first, then what it is. lead: one plain sentence before the entries.
function LbDefs({ lead, items }) {
  const scr = lbScreen(), fs = 18;
  return <div className="lb-say lb-defs" style={{display:'flex',flexDirection:'column',gap:scr ? 9 : 6,margin:'2px 0',color:BK.ink}}>
    {lead && <p style={{fontSize:fs,lineHeight:1.5,fontWeight:500,margin:0}}>{lead}</p>}
    <dl style={{margin:0,display:'flex',flexDirection:'column',gap:scr ? 8 : 5}}>
      {items.map(([term, def], i) => <div key={i} data-lb-def={i} style={{paddingLeft:20,textIndent:-20,fontSize:fs,lineHeight:1.5}}>
        <dt style={{display:'inline',fontFamily:LANG === 'ko' ? 'inherit' : LB_SERIF,fontWeight:900,fontSize:LANG === 'ko' ? fs + 0.5 : fs + 1.5,marginRight:9}}>{term}</dt>
        <dd style={{display:'inline',margin:0,fontWeight:500}}>{def}</dd>
      </div>)}
    </dl>
  </div>;
}

// one row on the treble staff, drawn inside SfStaff's extra(yOf). items: [kind, beats] notes and rests ('w' 'hd' 'h' 'q'
// 'p' 'r' 'hr' 'wr'), ['box', beats] an empty dashed box (a note or rest to find), ['|'] a bar line, ['||'] the double
// bar line, [':||'] the repeat sign, ['ts', top] a time signature (['ts', top, 'blank']: two boxes to write it in),
// ['C'] common time, ['sp', px] a gap. o: x0, D (px a beat), ink, ties [[i, j]] (item indexes), noBars (bar lines neither drawn nor
// spaced: the child draws them), hearts (true | 'outline' | false), strong (beat 1 a big heart), mid (4/4: beat 3 a
// middle one), counts (true | false | 'boxes' | 'ans'), lit (the beat sounding), marks (under each beat: '✓' '?' '·'),
// hl (an item index drawn coral), topCoral, dyH; on paper: ['ts', top, 'ans'] a worked time signature, fill (beats whose
// outline hearts are coloured, a worked example), exBars (with noBars: the first bar lines drawn in coral). Returns the raw SVG, the beats, the bar lines' x and the end.
const tsIsRest = (k) => k === 'r' || k === 'hr' || k === 'wr';
function tsRaw(yOf, items, o = {}) {
  const D = o.D || 34, G = (d) => yOf(d, 'treble'), col = o.ink || PEN_N, cor = PEN_C;
  const out = [], beatXs = [], noteX = {}, bars = [], under = [];
  let x = o.x0 || 46, top = 4, inBar = 0, last = 0;
  const line = (xx, w = 1.5) => '<line x1="' + pFix(xx) + '" x2="' + pFix(xx) + '" y1="' + pFix(G(38)) + '" y2="' + pFix(G(30)) + '" stroke="' + col + '" stroke-width="' + w + '"/>';
  items.forEach((it, i) => {
    const k = it[0];
    if (k === 'ts') { top = it[1];
      if (it[2] === 'blank' || it[2] === 'ans') [[G(36), it[1]], [G(32), 4]].forEach(([y, num]) => { out.push('<rect x="' + pFix(x - 1) + '" y="' + pFix(y - 9.5) + '" width="18" height="19" rx="2" fill="#fff" stroke="' + (it[2] === 'ans' ? cor : col) + '" stroke-width="1.2" stroke-dasharray="3 2.4"/>');
        if (it[2] === 'ans') out.push('<text x="' + pFix(x + 8) + '" y="' + pFix(y + 6.4) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="16" font-weight="900" font-style="italic" fill="' + cor + '">' + num + '</text>'); });
      else [[it[1], G(36), o.topCoral ? cor : col], [4, G(32), col]].forEach(([n, y, c]) => out.push('<text x="' + pFix(x + 8) + '" y="' + pFix(y + 7.6) + '" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="25" font-weight="900" fill="' + c + '">' + n + '</text>'));
      x += 26; return; }
    if (k === 'sp') { x += it[1]; last = x; return; }   // a gap (a time signature on its own)
    if (k === 'C') { top = 4; out.push('<text x="' + pFix(x + 9) + '" y="' + pFix(G(34) + 8) + '" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="27" font-weight="900" fill="' + col + '">C</text>'); x += 28; return; }
    if (k === '|') { if (o.noBars) { if (bars.length < (o.exBars || 0)) out.push('<line x1="' + pFix(x - 6) + '" x2="' + pFix(x - 6) + '" y1="' + pFix(G(38)) + '" y2="' + pFix(G(30)) + '" stroke="' + cor + '" stroke-width="1.8"/>'); bars.push(x - 6); inBar = 0; return; } out.push(line(x + 2)); bars.push(x + 2); last = x + 2.8; x += 12; inBar = 0; return; }
    if (k === '||') { out.push(line(x + 1, 1.3), line(x + 6, 4)); last = x + 8; x += 10; return; }
    if (k === ':||') { out.push('<circle cx="' + pFix(x) + '" cy="' + pFix(G(35)) + '" r="2.3" fill="' + col + '"/><circle cx="' + pFix(x) + '" cy="' + pFix(G(33)) + '" r="2.3" fill="' + col + '"/>', line(x + 6, 1.3), line(x + 11, 4)); last = x + 13; x += 16; return; }
    const n = it[1], nx = x + 12, c = o.hl === i ? cor : col, w = k === 'p' ? n * D * 1.3 : n * D;   // a quaver pair a little wider, so its heads never touch
    if (k === 'box') out.push('<rect x="' + pFix(x + 4) + '" y="' + pFix(G(39.4)) + '" width="' + pFix(n * D - 10) + '" height="' + pFix(G(28.6) - G(39.4)) + '" rx="3" fill="#fff" fill-opacity="0.7" stroke="' + cor + '" stroke-width="1.6" stroke-dasharray="4 3"/>');
    else if (k === 'p') out.push(nvbPair(nx - 2, nx + D * 0.65 - 2, G(32), { col: c }).svg);
    else if (k === 'r') out.push(nvbRest(nx + 2, G(34), 'q', { k: 0.82, col: c }).svg);
    else if (k === 'hr') out.push('<rect x="' + pFix(nx - 5) + '" y="' + pFix(G(34) - 5) + '" width="16" height="5" fill="' + c + '"/>');
    else if (k === 'wr') out.push('<rect x="' + pFix(x + 12 + (n - 1) * D / 2 - 8) + '" y="' + pFix(G(36)) + '" width="16" height="5" fill="' + c + '"/>');
    else out.push(nvbNote(nx, G(32), k === 'hd' ? 'h' : k, { col: c }).svg + (k === 'hd' ? '<circle cx="' + pFix(nx + 14) + '" cy="' + pFix(G(33)) + '" r="2.6" fill="' + c + '"/>' : ''));
    noteX[i] = nx;
    const tiedIn = (o.ties || []).some(([, tb]) => tb === i);
    for (let b = 0; b < n; b++) beatXs.push({ tied: b === 0 && tiedIn, x: nx + b * D, n: (inBar + b) % top + 1, held: b > 0 && !tsIsRest(k) && k !== 'box', rest: tsIsRest(k), box: k === 'box', pair: k === 'p' && b === 0, px: nx + D * 0.65 - 2, item: i });
    inBar += n; x += w + (o.noBars ? (o.G || 12) : 0);   // noBars: the same gap after every note, room for a bar line anywhere
  });
  (o.ties || []).forEach(([a, b]) => { const x1 = noteX[a] + 4, x2 = noteX[b] - 4, y = G(32) + 7.5;   // under the heads, a clear curve below line 1
    out.push('<path d="M' + pFix(x1) + ' ' + pFix(y) + ' Q' + pFix((x1 + x2) / 2) + ' ' + pFix(y + 15) + ' ' + pFix(x2) + ' ' + pFix(y) + '" fill="none" stroke="' + cor + '" stroke-width="2.2" stroke-linecap="round"/>'); });
  const boxes = o.counts === 'boxes' || o.counts === 'ans', yH = G(30) + (o.dyH || 30), yC = yH + (o.strong ? 31 : 26) + (boxes ? 6 : 0);   // boxes start below the hearts' tips
  if (o.hearts !== false) beatXs.forEach((bt, j) => {
    const big = o.strong && bt.n === 1, mid = o.strong && o.mid && bt.n === 3, on = o.lit === j, s = (big ? 2.3 : mid ? 1.75 : 1.45) * (on ? 1.18 : 1);
    const solid = on || (o.fill || []).includes(j) || (o.hearts === 'outline' ? false : o.strong ? big || mid : true);
    under.push('<path d="M0 5 Q-7.5 -0.5 -5 -4.2 Q-2.4 -6.8 0 -3 Q2.4 -6.8 5 -4.2 Q7.5 -0.5 0 5 Z" transform="translate(' + pFix(bt.x) + ' ' + pFix(yH) + ') scale(' + pFix(s * 100) / 100 + ')" fill="' + (solid ? cor : '#fff') + '" stroke="' + cor + '" stroke-width="' + pFix(120 / s) / 100 + '"/>');
    if (o.counts !== false) {
      const light = bt.held || bt.tied, fill = on ? cor : light ? 'rgba(38,41,107,0.38)' : col;
      const cells = bt.pair ? [[bt.x, String(bt.n)], [bt.px, '+']] : [[bt.x, String(bt.n)]];
      if (boxes) {
        const bw = bt.pair ? Math.min(22, D * 0.5 - 3) : Math.min(28, D - 6);
        cells.forEach(([cx, tx]) => {
          under.push('<rect x="' + pFix(cx - bw / 2) + '" y="' + pFix(yC - 20) + '" width="' + pFix(bw) + '" height="27" rx="3" fill="' + (light ? 'rgba(38,41,107,0.11)' : '#fff') + '" stroke="' + (o.counts === 'ans' ? cor : 'rgba(38,41,107,0.45)') + '" stroke-width="1.3"' + (bt.rest ? ' stroke-dasharray="3.4 2.8"' : '') + '/>');
          if (o.counts === 'ans') under.push('<text x="' + pFix(cx) + '" y="' + pFix(yC) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="15" font-weight="900" font-style="italic" fill="' + (light ? 'rgba(228,87,46,0.55)' : cor) + '">' + tx + '</text>');
        });
      } else {
        if (bt.rest) under.push('<circle cx="' + pFix(bt.x) + '" cy="' + pFix(yC - 5.5) + '" r="10.5" fill="#fff" stroke="' + col + '" stroke-width="1.4" stroke-dasharray="3.2 2.6"/>');
        cells.forEach(([cx, tx], c) => under.push('<text x="' + pFix(cx) + '" y="' + pFix(yC) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + (o.strong && bt.n === 1 && !c ? 17 : 15) + '" font-weight="900" fill="' + (c ? (on ? cor : col) : fill) + '">' + tx + '</text>'));
      }
    }
    const m = o.marks && o.marks[j];
    if (m) under.push('<text x="' + pFix(bt.x) + '" y="' + pFix(yC + 22) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="15" font-weight="900" fill="' + (m === '✓' ? PEN_G : m === '·' ? 'rgba(38,41,107,0.4)' : cor) + '">' + m + '</text>');
  });
  return { raw: out.join('') + under.join(''), beatXs, bars, end: x, last: last || x, noteX };
}
// the room a row needs under the staff: hearts, the count (or its boxes) and the marks
function tsPadBottom(o = {}) {
  if (o.hearts === false) return 22;
  if (o.counts === false) return (o.dyH || 30) + 20;
  return (o.dyH || 30) + (o.strong ? 31 : 26) + (o.counts === 'boxes' || o.counts === 'ans' ? 20 : 10) + (o.marks ? 24 : 0);
}
// a staff with one row: SfStaff draws the lines and the clef, tsRaw the rest. The staff ends at its last bar line
// (or the end); width: the width that fills the picture, so every staff of a page has one scale.
function TsStaff({ items, width = 400, o = {}, label, pad, extra, full }) {
  const m = tsRaw((d) => dY(d), items, o), vbw = Math.ceil(m.last + 6);
  return <div style={{width:full ? '100%' : Math.min(100, vbw / width * 100) + '%'}}><SfStaff clef="treble" width={vbw} span={[4, m.last]} pad={pad || [extra ? 34 : 16, tsPadBottom(o)]} label={label}
    extra={(yOf, layer, txt) => layer === 'over' && <g><g dangerouslySetInnerHTML={{ __html: tsRaw(yOf, items, o).raw }}/>{extra && extra(yOf, txt, m)}</g>}/></div>;
}
const tsQ = (n) => Array.from({ length: n }, () => ['q', 1]);

function tsLbPages(scr = false) {
  const ch = 'time-signatures';
  const live = (still, comp) => <LbLive still={still} live={<>{still}{comp}</>}/>;   // on screen: the picture, then what moves (B12)
  const pic = (node, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div></LbPic>;
  const stack = (nodes, h, mw = 560) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap:8,width:'100%',maxWidth:mw,margin:'0 auto'}}>{nodes}</div></LbPic>;
  const tag = (x, y, s, c = BK.coral, a = 'middle') => (yOf, txt) => <text x={x} y={typeof y === 'function' ? y(yOf) : y} textAnchor={a} fontSize="11.5" fontWeight="900" fill={c} style={txt}>{s}</text>;
  const tags = (...fs) => (yOf, txt) => <g>{fs.map((f, i) => <g key={i}>{f(yOf, txt)}</g>)}</g>;
  const above = (yOf) => yOf(40, 'treble') - 6;
  const nb = (x) => x.replace(/ /g, '\u00a0');   // a count never breaks across lines
  const C1 = nb('1 2 3 4');

  // p1: two bars of 4/4 with their hearts and the count; the time signature, a bar line and the double bar line named
  const p1 = <TsStaff width={420} items={[['ts', 4], ['q', 1], ['q', 1], ['h', 2], ['|'], ['q', 1], ['q', 1], ['q', 1], ['q', 1], ['||']]} o={{ D: 38 }}
    label={t('The treble staff with the time signature 4 over 4 and two bars of notes on G, a bar line between them and a double bar line at the end. A coral heart under every beat and the count 1 2 3 4 in each bar.', '박자표 4/4와 G 위의 음표 두 마디가 있는 높은음자리표 오선, 마디 사이에 세로줄, 끝에 끝세로줄. 박마다 산호색 심장, 마디마다 1 2 3 4.')}
    extra={tags(tag(62, above, t('time signature', '박자표')), tag(226, above, t('bar line', '세로줄')), tag(400, above, t('double bar line', '끝세로줄'), BK.coral, 'end'))}/>;

  // p2: three bars of 3/4; then two bars with the repeat sign
  const p2a = <TsStaff width={420} items={TS_ROWS.bars3} o={{ D: 34 }}
    label={t('Three bars of 3/4 on G, with bar lines between them and a double bar line at the end. Under each bar its three hearts and the count 1 2 3.', 'G 위의 3/4 세 마디, 마디 사이에 세로줄, 끝에 끝세로줄. 마디마다 심장 셋과 1 2 3.')}
    extra={tags(tag(122, above, t('bar 1', '1마디')), tag(236, above, t('bar 2', '2마디')), tag(350, above, t('bar 3', '3마디')))}/>;
  const p2b = <TsStaff width={420} items={TS_ROWS.repeat} o={{ D: 34, hearts: false }} pad={[34, 16]}
    label={t('Two bars of 3/4 ending in a repeat sign: two dots before a double bar line. Play them again.', '도돌이표로 끝나는 3/4 두 마디: 끝세로줄 앞의 점 두 개. 한 번 더 쳐요.')}
    extra={tags(tag(300, above, t('repeat sign: play it again', '도돌이표: 한 번 더'), BK.coral, 'end'))}/>;

  // p3: the two numbers: a bar each of 2/4, 3/4 and 4/4, the top number coral; and C
  const W3 = scr ? 330 : 250, D3 = scr ? 46 : 40;   // printed two by two, each bar as large as its half allows
  const p3 = [2, 3, 4, 'C'].map(n => n === 'C' ? <TsStaff key={n} width={W3} items={[['C'], ...tsQ(4), ['||']]} o={{ D: D3 }} pad={[30, 62]}
    label={t('A bar of common time: the sign C instead of 4/4, four crotchets counted 1 2 3 4.', '보통박자 한 마디: 4/4 대신 C, 4분음표 넷을 1 2 3 4로 세요.')}
    extra={(yOf, txt) => <text x="58" y={above(yOf)} textAnchor="start" fontSize="11.5" fontWeight="900" fill={BK.coral} style={txt}>{t('C = 4/4, common time', 'C = 4/4, 보통박자')}</text>}/> : <TsStaff key={n} width={W3} items={[['ts', n], ...tsQ(n), ['||']]} o={{ D: D3, topCoral: true }} pad={[30, 62]}
    label={t('A bar of ' + n + '/4, the top number ' + n + ' in coral: ' + n + ' crotchets over ' + n + ' hearts, counted ' + Array.from({ length: n }, (_, i) => i + 1).join(' ') + '.', n + '/4 한 마디, 위 숫자 ' + n + '는 산호색: 심장 ' + n + '개 위의 4분음표 ' + n + '개, ' + Array.from({ length: n }, (_, i) => i + 1).join(' ') + '로 세요.')}/>);

  // p4: strong and weak beats: 3/4 and 4/4, beat 1 a big heart (and 3 a middle one in 4/4)
  const p4 = [[3, t('strong, weak, weak', '센박, 여린박, 여린박')], [4, t('strong, weak, medium, weak', '센박, 여린박, 중간 센박, 여린박')]].map(([n, w]) => <TsStaff key={n} width={420} items={[['ts', n], ...tsQ(n), ['|'], ...tsQ(n), ['||']]} o={{ D: 36, strong: true, mid: n === 4 }} pad={[34, 68]}
    label={t('Two bars of ' + n + '/4 on G. Beat 1 of each bar has a big coral heart' + (n === 4 ? ', beat 3 a middle one' : '') + ', the other beats small white hearts: ' + w + '.', n + '/4 두 마디. 마디마다 1박은 큰 산호색 심장' + (n === 4 ? ', 3박은 중간 심장' : '') + ', 나머지는 작은 흰 심장: ' + w + '.')}
    extra={tags(tag(60, above, w, BK.coral, 'start'))}/>);

  // p5: fill the bar: notes and rests on the staff, each bar adding up to the top number
  const p5a = <TsStaff width={470} items={TS_ROWS.fill4} o={{ D: 30 }}
    label={t('Three bars of 4/4 on G: a crotchet, a crotchet rest standing in the middle of the staff and a minim; a minim rest sitting on line 3 and two crotchets; a semibreve rest hanging from line 4, a whole bar of silence. The beats of the rests are dashed circles.', '4/4 세 마디: 4분음표, 오선 가운데에 선 4분쉼표, 2분음표; 3번 줄 위에 앉은 2분쉼표와 4분음표 둘; 4번 줄에 매달린 온쉼표, 한 마디 내내 쉼. 쉼표의 박은 점선 동그라미.')}/>;
  const p5b = <TsStaff width={470} items={TS_ROWS.fill3} o={{ D: 40 }} pad={[16, 66]}
    label={t('Three bars of 3/4: a minim and a crotchet rest; a crotchet, two quavers and a crotchet; a dotted minim. Each bar adds up to 3.', '3/4 세 마디: 2분음표와 4분쉼표; 4분음표, 8분음표 둘, 4분음표; 점2분음표. 마디마다 3박.')}/>;

  // p6: the tie: a minim tied over the bar line to a crotchet
  const p6b = <TsStaff width={420} items={TS_ROWS.tie} o={{ D: 36 }}
    label={t('The same two bars without the tie: G plays again on beat 1 of bar 2, so that 1 is dark.', '붙임줄 없는 같은 두 마디: 2마디 1박에서 G를 다시 쳐요. 그래서 그 1은 진하게.')}
    extra={tags(tag(206, above, t('without the tie: play G again', '붙임줄 없이: G를 다시 쳐요'), BK.ink))}/>;
  const p6a = <TsStaff width={420} items={TS_ROWS.tie} o={{ D: 36, ties: [[3, 5]] }}
    label={t('Two bars of 4/4 on G. A coral tie joins the minim at the end of bar 1 to the crotchet at the start of bar 2: play the minim, then hold it through beat 1 of bar 2. The held numbers, 4 and the next 1, are lighter.', '4/4 두 마디. 산호색 붙임줄이 1마디 끝의 2분음표와 2마디 첫 4분음표를 이어요: 2분음표를 치고 2마디 1박까지 누르고 있어요. 누르는 박의 숫자 4와 다음 1은 연하게.')}
    extra={tags(tag(206, above, t('the tie crosses the bar line', '붙임줄이 세로줄을 건너가요'), BK.coral))}/>;

  const chkArts = {
    bars: [nvbNote(12, 30, 'q', { k: 0.6 }), penLine([28, 10], [28, 40], 1.4, PEN_N), nvbNote(44, 30, 'q', { k: 0.6 }), penLine([62, 10], [62, 40], 1.1, PEN_N), penLine([66, 10], [66, 40], 3, PEN_N), { k: 'raw', svg: '<circle cx="57" cy="21" r="1.6" fill="' + PEN_N + '"/><circle cx="57" cy="29" r="1.6" fill="' + PEN_N + '"/>' }],
    top: [{ ...penText(20, 22, '3', { size: 18, weight: 900, fill: PEN_C, anchor: 'middle' }) }, { ...penText(20, 40, '4', { size: 18, weight: 900, fill: PEN_N, anchor: 'middle' }) }, ...[1, 2, 3].map(n => ({ ...penText(38 + n * 12, 32, String(n), { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' }) }))],
    strong: [{ ...tnHeart(18, 22, 2.4, PEN_C), nw: true }, { ...tnHeart(46, 24, 1.5, PEN_C, true), nw: true }, { ...tnHeart(70, 24, 1.5, PEN_C, true), nw: true }],
    fill: [nvbNote(14, 30, 'h', { k: 0.6 }), nvbRest(40, 24, 'q', { k: 0.55 }), { ...penText(70, 30, '= 3', { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    tie: [nvbNote(16, 26, 'h', { k: 0.6 }), nvbNote(60, 26, 'q', { k: 0.6 }), { k: 'raw', svg: '<path d="M20 33 Q39 41 57 33" fill="none" stroke="' + PEN_C + '" stroke-width="2"/>' }],
  };
  const checksRows = [
    ['bars', [0, 0, 92, 40], t('I can point to the bar lines, the double bar line and the repeat sign', '세로줄, 끝세로줄, 도돌이표를 짚을 수 있어요')],
    ['top', [0, 0, 92, 40], t('I can read the top number and count each bar', '위 숫자를 읽고 마디마다 셀 수 있어요')],
    ['strong', [0, 0, 92, 40], t('I can play beat 1 a little louder', '1박을 조금 더 세게 칠 수 있어요')],
    ['fill', [0, 0, 92, 40], t('I can add up the notes and rests in a bar', '마디 안의 음표와 쉼표를 더할 수 있어요')],
    ['tie', [0, 0, 92, 40], t('I can play a tie: once, then hold', '붙임줄을 칠 수 있어요: 한 번 치고 누르기')],
  ];
  const G3 = t('Right hand, finger 3 on G', '오른손 3번 손가락, G');

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Time Signatures', '박자표')}</div>
      </div></LbOnly>
      {pic(p1, 220, 640)}
      <LbSay size={17.5}>{LANG === 'ko' ? <>음악은 <b>마디</b>로 나뉘어요. 악보 맨 앞의 <b>박자표</b>는 마디를 어떻게 세는지 알려 줘요.</>
        : <>Music is divided into <b>bars</b>. The <b>time signature</b> at the start tells you how to count them.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Bars and bar lines', '마디와 세로줄'), 2], [t('The two numbers', '두 숫자'), 3], [t('Strong and weak beats', '센박과 여린박'), 4], [t('Fill the bar', '마디 채우기'), 5], [t('The tie', '붙임줄'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, , x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. bars and bar lines (and the repeat sign)
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Bars and bar lines', '마디와 세로줄')}>
      {live(stack([<div key="a">{p2a}</div>, <div key="b">{p2b}</div>], 250, 620), <TsPad page={2}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['세로줄', '음악을 마디로 나누는 줄.'],
        ['마디', '세로줄로 나뉜 음악의 한 부분. 마디마다 박의 수가 같아요.'],
        ['끝세로줄', '음악 끝의 가는 줄과 굵은 줄.'],
        ['도돌이표', '끝세로줄 앞의 점 두 개. 처음으로 돌아가 한 번 더 쳐요.'],
      ] : [
        ['bar line', 'A line that divides the music into bars.'],
        ['bar', 'A part of the music marked off by bar lines. Every bar has the same number of beats. Its other name is a measure.'],
        ['double bar line', 'A thin line and a thick line at the end of the music.'],
        ['repeat sign', 'Two dots before a double bar line. Go back to the start and play the music again.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{G3}: 위의 세 마디를 마디마다 1 2 3으로 세면서 쳐요.</>,
        <>{G3}: 도돌이표가 있는 두 마디를 1 2 3으로 세면서 쳐요. 처음으로 돌아가 한 번 더 쳐요. 모두 네 마디예요.</>,
      ] : [
        <>{G3}: play the three bars, counting 1 2 3 in each bar.</>,
        <>{G3}: play the two bars with the repeat sign, counting 1 2 3. Go back and play them again. Four bars in all.</>,
      ]}/>
      <LbRemember>{t('Bar lines make bars. Two dots: play it again.', '세로줄은 마디를 만들어요. 점 두 개: 한 번 더.')}</LbRemember>
    </LbPage>,

    // 3. the two numbers
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The two numbers', '두 숫자')}>
      {live(<LbPic h={300}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:'14px 30px',width:'100%',maxWidth:scr ? 360 : 680,margin:'0 auto',alignItems:'end'}}>{p3.map((s, i) => <div key={i}>{s}</div>)}</div></LbPic>, <TsPad page={3}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['박자표', '악보 맨 앞의 두 숫자. 마디를 어떻게 세는지 알려 줘요.'],
        ['위 숫자', '한 마디의 박 수.'],
        ['아래 숫자', '한 박이 되는 음표. 4는 4분음표예요.'],
        ['C', '4/4를 쓰는 다른 방법. 다른 이름은 보통박자예요.'],
      ] : [
        ['time signature', 'The two numbers at the start of the music. They show how to count each bar.'],
        ['top number', 'The number of beats in each bar.'],
        ['bottom number', 'The note that is one beat. 4 means a crotchet.'],
        ['C', 'Another way to write 4/4. Its other name is common time.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>무릎을 치면서 위의 박자표를 두 마디씩 세요: {nb('1 2')}, {nb('1 2 3')}, {C1}, 그리고 C는 {C1}.</>,
        <>{G3}: 위의 네 오선을 이 차례로 두 마디씩, 소리 내어 세면서 쳐요: 3/4, C, 2/4, 4/4.</>,
      ] : [
        <>Pat your knees and count each time signature above, two bars each: {nb('1 2')}, {nb('1 2 3')}, {C1}, and C: {C1}.</>,
        <>{G3}: play the four staves in this order, two bars each, counting out loud: 3/4, C, 2/4, 4/4.</>,
      ]}/>
      <LbRemember>{t('Top: beats in a bar. Bottom 4: a crotchet beat.', '위: 한 마디의 박 수. 아래 4: 4분음표가 한 박.')}</LbRemember>
    </LbPage>,

    // 4. strong and weak beats
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Strong and weak beats', '센박과 여린박')}>
      {live(stack(p4.map((s, i) => <div key={i}>{s}</div>), 290, 620), <TsStrongPad/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['센박', '마디의 1박. 조금 더 세게 쳐요.'],
        ['중간 센박', '4/4의 3박. 1박보다 조금 여리게 쳐요.'],
        ['여린박', '나머지 박.'],
      ] : [
        ['strong beat', 'Beat 1 of every bar. Play it a little louder.'],
        ['medium beat', 'Beat 3 in 4/4. Play it a little softer than beat 1.'],
        ['weak beat', 'All the other beats.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>1에서 무릎을 치고, 나머지 박에서 손뼉을 쳐요. 소리 내어 세요. 2/4, 3/4, 4/4를 네{'\u00a0'}마디씩.</>,
        <>{G3}: 박마다 4분음표, 1박은 조금 더 세게. 3/4 네{'\u00a0'}마디, 그다음 4/4 네{'\u00a0'}마디.</>,
      ] : [
        <>Pat your knees on 1 and clap on the other beats. Count out loud. Four bars each of 2/4, 3/4 and 4/4.</>,
        <>{G3}: a crotchet on every beat, beat 1 a little louder. Four bars of 3/4, then four of 4/4.</>,
      ]}/>
      <LbRemember>{t('Beat 1 is strong.', '1박은 센박.')}</LbRemember>
    </LbPage>,

    // 5. fill the bar; rests on the staff
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Fill the bar', '마디 채우기')}>
      {live(stack([<div key="a">{p5a}</div>, <div key="b">{p5b}</div>], 300, 640), <TsBuildBar/>)}
      <LbDefs lead={LANG === 'ko' ? <>마디마다 음표와 쉼표를 더하면 <b>위 숫자</b>가 돼요.</> : <>In every bar, the notes and rests add up to the <b>top number</b>.</>} items={LANG === 'ko' ? [
        ['4분쉼표', '1박 쉬는 쉼표. 오선 가운데에 서 있어요.'],
        ['2분쉼표', '2박 쉬는 쉼표. 3번 줄 위에 앉아요.'],
        ['온쉼표', '4박 쉬는 쉼표. 4번 줄에 매달려요. 4/4에서는 한 마디 내내 쉬어요.'],
      ] : [
        ['crotchet rest', 'A silence of 1 beat. It stands in the middle of the staff.'],
        ['minim rest', 'A silence of 2 beats. It sits on line 3.'],
        ['semibreve rest', 'A silence of 4 beats. It hangs from line 4. In 4/4 it fills a whole bar.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{G3}: 위의 4/4 세 마디를 소리 내어 세면서 쳐요. 쉼표에서는 손을 건반 바로 위에 띄우고 계속 세요.</>,
        <>{G3}: 3/4 세 마디를 소리 내어 세면서 쳐요. 8분음표 둘은 2 +: “2 앤”이라고 세요.</>,
      ] : [
        <>{G3}: play the three bars of 4/4, counting out loud. In the rests, lift your hand just above the key and keep counting.</>,
        <>{G3}: play the three bars of 3/4, counting out loud. Two quavers are 2 +: say “2 and”.</>,
      ]}/>
      <LbRemember>{t('Notes and rests fill each bar exactly.', '음표와 쉼표가 마디를 꼭 맞게 채워요.')}</LbRemember>
    </LbPage>,

    // 6. the tie
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('The tie', '붙임줄')}>
      {live(stack([<div key="a">{p6a}</div>, <div key="b">{p6b}</div>], 300, 640), <TsTiePad/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['붙임줄', '같은 음 두 개를 잇는 곡선. 첫 음표를 치고, 두 번째 음표가 끝날 때까지 누르고 있어요. 붙임줄은 세로줄을 건너갈 수 있어요.'],
      ] : [
        ['tie', 'A curved line that joins two of the same note. Play the first note, then hold it through the second. A tie can cross a bar line.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>{G3}: 위쪽 두 마디를 쳐요. 2분음표는 2마디 1박까지 누르고, 연한 숫자도 소리 내어 세요.</>,
        <>{G3}: 아래쪽 두 마디를 붙임줄 없이 쳐요. 2마디 1박에서 G를 다시 쳐요. 두 소리를 비교해요.</>,
      ] : [
        <>{G3}: play the top two bars. Hold the minim through beat 1 of bar{'\u00a0'}2, and count the light numbers out loud too.</>,
        <>{G3}: play the bottom two bars, without the tie. Play G again on beat 1 of bar{'\u00a0'}2. Hear the difference.</>,
      ]}/>
      <LbRemember>{t('A tie: play once, hold for both.', '붙임줄: 한 번 치고, 두 음표만큼 누르기.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '피아노 앞에서 그 쪽(2-6쪽)을 펴고 하나씩 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, vb, x]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_ts_v1" rows={checksRows.map(([a, vb, x]) => [{ shapes: chkArts[a], vb }, x])}/>}/>
    </LbPage>,
  ];
}
// the book's rows, shared with what moves on screen
const TS_ROWS = {
  bars3: [['ts', 3], ['q', 1], ['q', 1], ['q', 1], ['|'], ['h', 2], ['q', 1], ['|'], ['hd', 3], ['||']],
  repeat: [['ts', 3], ['q', 1], ['q', 1], ['q', 1], ['|'], ['hd', 3], [':||']],
  fill4: [['ts', 4], ['q', 1], ['r', 1], ['h', 2], ['|'], ['hr', 2], ['q', 1], ['q', 1], ['|'], ['wr', 4], ['||']],
  fill3: [['ts', 3], ['h', 2], ['r', 1], ['|'], ['q', 1], ['p', 1], ['q', 1], ['|'], ['hd', 3], ['||']],
  tie: [['ts', 4], ['q', 1], ['q', 1], ['h', 2], ['|'], ['q', 1], ['q', 1], ['h', 2], ['||']],
};
function TimeSignaturesLessonBook() { return <>{tsLbPages(false)}</>; }
