// ─── Phase 427: chapter 6 (Ledger Lines) Lesson Book -- draft v1 ───
// Built on her standing decisions: Clara's short line is a 'ladder rung' until this chapter (Book rule 8), the treble
// staff is Queensland and the bass staff Kingsland (chapter 5), high is the bird's sky and low is the turtle's sea
// (chapter 2), the landmarks of chapter 5, the Book rules. The yellow marks (draft=1) wait for her answers (B codes).
// AMEB (2026 Manual): Music Craft Prelim -- one ledger line below the treble staff; Grade 1 -- one above and below both
// staves; Grade 2 -- up to three. Theory of Music Grade 1 -- two; Grade 2 -- three. 'leger' and 'ledger' both accepted.

function llLbPages(scr = false) {
  const ch = 'ledger-lines';
  const queen = sfQueen(22, 24, 1), king = sfKing(22, 24, 1), clara = sfClara(22, 24, 1);
  const bird = [...fsBird(22, 26, 1), ...fsCloud(10, 12, 0.6)], turtle = [...fsTurtle(22, 26, 0.8), ...fsWaves(2, 36, 40, 0.8, 3)];
  const A = (q, kids) => <LbAsk q={q}>{kids}</LbAsk>;
  const pic = (svg, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{svg}</div></LbPic>;
  const stack = (items, h) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:620,margin:'0 auto'}}>{items}</div></LbPic>;
  const landName = (name, d, st, x = 172) => (yOf, layer, txt) => layer === 'under' && <text x={x} y={yOf(d, st) + 7} fontSize="21" fontWeight="900" fill={BK.coral} fillOpacity="0.2" textAnchor="middle" letterSpacing="3" style={{fontFamily:LB_SERIF}}>{name}</text>;
  const both = (...fs) => (yOf, layer, txt) => <g>{fs.map((f, i) => <g key={i}>{f(yOf, layer, txt)}</g>)}</g>;
  const row = (items, y) => (yOf, layer, txt) => layer === 'over' && <g style={txt}>{items.map(([x, top, sub, coral, name], i) => <g key={i}>
    <text x={x} y={y(yOf)} fontSize="13" fontWeight="900" fill={coral ? BK.coral : BK.ink} textAnchor="middle">{top}</text>
    {sub && <text x={x} y={y(yOf) + 12} fontSize="8.6" fontWeight="900" fill={BK.muted} textAnchor="middle">{sub}</text>}
    {name && <text x={x} y={y(yOf) + 24} fontSize="9.6" fontWeight="900" fill={BK.coral} textAnchor="middle">{name}</text>}</g>)}</g>;
  const rungWord = (n) => n ? (LANG === 'ko' ? n + '번 발판' : 'rung ' + n) : (LANG === 'ko' ? '칸' : 'space');

  // p1: the ladder out of both lands -- two rungs up into the bird's sky over Queensland, Clara on her rung between the
  // lands, two rungs down into the turtle's sea under Kingsland
  const p1 = <SfStaff clef="grand" width={360} span={[4, 340]} pad={[30, 30]} label={t('The grand staff with ladders: above Queensland two short ledger lines carry the notes A and C up towards a bird in the sky; between the lands Princess Clara stands by middle C on its short line; below Kingsland two ledger lines carry E and C down towards a turtle in the sea', '큰보표의 사다리: 퀸즈랜드 위로 짧은 덧줄 두 개에 A와 C가 하늘의 새를 향해 올라가고, 두 나라 사이에는 클라라 공주가 가운데 도의 짧은 줄 옆에 서 있고, 킹스랜드 아래로 덧줄 두 개에 E와 C가 바다의 거북을 향해 내려가요')}
    notes={[{ d: 40, x: 214, color: PEN_C }, { d: 42, x: 256, color: PEN_C }, { d: 28, x: 112, color: PEN_C }, { d: 16, x: 214, staff: 'bass', color: PEN_C }, { d: 14, x: 256, staff: 'bass', color: PEN_C }]}
    icons={[SF_ICON(bird, 286, 4, 1), SF_ICON(clara, 124, 84, 0.8), SF_ICON(turtle, 284, 196, 0.95)]}
    extra={both(landName('QUEENSLAND', 34, 'treble', 186), landName('KINGSLAND', 22, 'bass', 186))}/>;

  // p2: Clara's rung is a ledger line -- and how to draw one: as wide as the note, the same distance apart, never one too many
  const p2a = <SfStaff clef="treble" width={340} pad={[24, 42]} span={[4, 336]} label={t('Queensland with two notes on short lines of their own: middle C below the staff on Clara\'s rung, and A above the staff on a rung of its own -- both are ledger lines', '두 음이 자기만의 짧은 줄 위에 있는 퀸즈랜드: 오선 아래 클라라의 발판 위의 가운데 도, 오선 위 자기 발판 위의 A -- 둘 다 덧줄이에요')}
    notes={[{ d: 28, x: 112, color: PEN_C }, { d: 40, x: 226, color: PEN_C }]} icons={[SF_ICON(clara, 99, 116, 0.6)]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <text x="92" y={yOf(28) + 5} fontSize="14" fontWeight="900" fill={BK.coral} textAnchor="end">C</text>
      <text x="226" y={yOf(40) - 11} fontSize="14" fontWeight="900" fill={BK.coral} textAnchor="middle">A</text>
      {[[28, 112], [40, 226]].map(([d, x]) => <g key={d}>
        <line x1={x + 46} x2={x + 18} y1={yOf(d)} y2={yOf(d)} stroke={BK.coral} strokeWidth="1.5"/>{sfArrowHead(x + 17, yOf(d), -1, BK.coral)}
        <text x={x + 51} y={yOf(d) + 4} fontSize="11.5" fontWeight="900" fill={BK.ink}>{t('ledger line', '덧줄')}</text></g>)}
    </g>}/>;
  const howTo = (ok, cap, bad) => <div style={{textAlign:'center'}}>
    <SfStaff clef="treble" width={128} pad={[12, 18]} span={[4, 124]} label={cap} notes={[{ d: 42, x: 66 }]}
      extra={(yOf, layer, txt) => layer === 'under' ? <g>{bad === 'long' && [40, 42].map(d => <line key={d} x1="38" x2="94" y1={yOf(d)} y2={yOf(d)} stroke={BK.ink} strokeWidth="1.4"/>)}{bad === 'extra' && <line x1="54" x2="78" y1={yOf(44)} y2={yOf(44)} stroke={BK.ink} strokeWidth="1.4"/>}</g>
        : <g>{bad === 'gap' && <rect x="50" y={yOf(40) - 3} width="32" height="6" fill={BK.soft}/>}<text x="112" y={yOf(43) + 4} fontSize="17" fontWeight="900" fill={ok ? BK.green : BK.coral} textAnchor="middle">{ok ? '✓' : '✗'}</text></g>}/>
    <div style={{fontSize:11.5,fontWeight:800,color:BK.ink,marginTop:2,lineHeight:1.3}}>{cap}</div></div>;
  const p2b = <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr 1fr',gap:12,alignItems:'start'}}>
    {howTo(true, t('a little wider, the same distance apart', '살짝 넓게, 같은 간격'))}
    {howTo(false, t('not too long', '너무 길면 안 돼요'), 'long')}
    {howTo(false, t('no gap below', '사이가 비면 안 돼요'), 'gap')}
    {howTo(false, t('not one rung too many', '발판 하나 더 그으면 안 돼요'), 'extra')}</div>;

  // p3: up into the sky -- out of Queensland's top line: the space, rung 1, a space, rung 2 (Sky C), a space, rung 3
  const xU = [70, 112, 154, 196, 238, 280, 322];
  const p3 = <SfStaff clef="treble" width={360} pad={[76, 50]} span={[4, 340]} label={t('Up out of Queensland from its top line F: G in the space above, A on rung 1, B, C on rung 2 -- Sky C --, D, E on rung 3, with a bird in the sky', '퀸즈랜드 맨 윗줄 F에서 위로: 위 칸의 G, 1번 발판의 A, B, 2번 발판의 C -- 하늘 C --, D, 3번 발판의 E, 하늘에는 새')}
    notes={[38, 39, 40, 41, 42, 43, 44].map((d, i) => ({ d, x: xU[i], color: i ? PEN_C : undefined }))} icons={[SF_ICON(bird, 282, -44, 1.3)]}
    extra={row([[xU[0], 'F', t('top line', '맨 윗줄')], [xU[1], 'G', rungWord(0), true], [xU[2], 'A', rungWord(1), true], [xU[3], 'B', rungWord(0), true], [xU[4], 'C', rungWord(2), true, t('Sky C', '하늘 C')], [xU[5], 'D', rungWord(0), true], [xU[6], 'E', rungWord(3), true]], (yOf) => yOf(30) + 22)}/>;

  // p4: down into the sea -- out of Kingsland's bottom line: the space, rung 1, a space, rung 2 (Sea C), a space, rung 3
  const p4 = <SfStaff clef="bass" width={360} pad={[60, 74]} span={[4, 340]} label={t('Down out of Kingsland from its bottom line G: F in the space below, E on rung 1, D, C on rung 2 -- Sea C --, B, A on rung 3, with a turtle in the sea', '킹스랜드 맨 아랫줄 G에서 아래로: 아래 칸의 F, 1번 발판의 E, D, 2번 발판의 C -- 바다 C --, B, 3번 발판의 A, 바다에는 거북')}
    notes={[18, 17, 16, 15, 14, 13, 12].map((d, i) => ({ d, x: xU[i], color: i ? PEN_C : undefined }))} icons={[SF_ICON(turtle, 280, 200, 1.3)]}
    extra={row([[xU[0], 'G', t('bottom line', '맨 아랫줄')], [xU[1], 'F', rungWord(0), true], [xU[2], 'E', rungWord(1), true], [xU[3], 'D', rungWord(0), true], [xU[4], 'C', rungWord(2), true, t('Sea C', '바다 C')], [xU[5], 'B', rungWord(0), true], [xU[6], 'A', rungWord(3), true]], (yOf) => yOf(26) - 42)}/>;

  // p5: between the lands -- the rungs there are borrowed: two rungs under Queensland = Kingsland's top line (A); two
  // rungs over Kingsland = Queensland's bottom line (E); Clara's C both ways
  const pairs = [[84, 26, 'A'], [158, 28, 'C'], [232, 30, 'E']];
  const p5 = <SfStaff clef="grand" width={300} gap={64} span={[4, 296]} pad={[18, 22]} label={t('The grand staff with three pairs, each the same key written twice: A on two rungs under Queensland and A on Kingsland\'s top line; middle C on Clara\'s rung under Queensland and over Kingsland; E on Queensland\'s bottom line and E on two rungs over Kingsland', '같은 건반을 두 번 쓴 세 쌍의 큰보표: 퀸즈랜드 아래 두 발판의 A와 킹스랜드 맨 윗줄의 A; 퀸즈랜드 아래와 킹스랜드 위 클라라 발판의 가운데 도; 퀸즈랜드 맨 아랫줄의 E와 킹스랜드 위 두 발판의 E')}
    notes={pairs.flatMap(([x, d]) => [{ d, x, staff: 'treble', color: PEN_C }, { d, x, staff: 'bass', color: PEN_C }])}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>{pairs.map(([x, d, L], i) => <g key={i}>
      <path d={`M${x + 12} ${yOf(d, 'treble') + 3} Q${x + 30} ${(yOf(d, 'treble') + yOf(d, 'bass')) / 2} ${x + 12} ${yOf(d, 'bass') - 3}`} fill="none" stroke={BK.ink} strokeWidth="1.2" strokeDasharray="3 3"/>
      <text x={x + 27} y={(yOf(d, 'treble') + yOf(d, 'bass')) / 2 + 5} fontSize="14" fontWeight="900" fill={BK.ink}>=</text>
      <text x={x - 16} y={yOf(d, 'treble') + 4} fontSize="12" fontWeight="900" fill={BK.coral} textAnchor="end">{L}</text>
      <text x={x - 16} y={yOf(d, 'bass') + 4} fontSize="12" fontWeight="900" fill={BK.coral} textAnchor="end">{L}</text></g>)}</g>}/>;

  // p6: the five Cs, from the sea to the sky -- rungs, space, rung, space, rungs; and a hop from each new C
  // [d, staff, top label, under label, coral] -- the two navy notes are the hops (Sea C a skip up to E, Sky C a step down to B)
  const C5 = [[14, 'bass', 'C', t('Sea', '바다'), t('2 rungs', '발판 2개'), true], [16, 'bass', 'E', t('a skip up', '건너뛰어 위')], [21, 'bass', 'C', t('Kingsland', '킹스랜드'), t('space', '칸'), true], [28, 'treble', 'C', t('Clara\'s', '클라라의'), t('rung', '발판'), true], [35, 'treble', 'C', t('Queensland', '퀸즈랜드'), t('space', '칸'), true], [42, 'treble', 'C', t('Sky', '하늘'), t('2 rungs', '발판 2개'), true], [41, 'treble', 'B', t('a step down', '한 걸음 아래')]];
  const xC = [50, 94, 152, 210, 268, 326, 370];
  const p6 = <SfStaff clef="grand" width={404} span={[4, 400]} pad={[30, 64]} label={t('The five Cs from low to high, an octave apart: Sea C on two rungs below Kingsland, Kingsland C in its second space, Clara\'s C on her rung, Queensland C in its third space, Sky C on two rungs above Queensland; and two hops: from Sea C a skip up to E, from Sky C a step down to B', '낮은 곳부터 한 옥타브씩 떨어진 다섯 C: 킹스랜드 아래 두 발판의 바다 C, 둘째 칸의 킹스랜드 C, 발판 위의 클라라의 C, 셋째 칸의 퀸즈랜드 C, 퀸즈랜드 위 두 발판의 하늘 C; 그리고 두 번 뛰기: 바다 C에서 건너뛰어 위로 E, 하늘 C에서 한 걸음 아래로 B')}
    notes={C5.map(([d, st, , , , c], i) => ({ d, staff: st, x: xC[i], color: c ? PEN_C : undefined }))}
    extra={(yOf, layer, txt) => { const y = yOf(14, 'bass'); return layer === 'over' && <g style={txt}>
      {sfHop(xC[0] + 7, xC[1] - 7, y + 9, -10)}{sfHop(xC[5] + 7, xC[6] - 7, yOf(42) - 9, 10)}
      {C5.map(([d, st, L, name, where, c], i) => <g key={i}>
        <text x={xC[i]} y={y + 31} fontSize="9.4" fontWeight="900" fill={c ? BK.coral : BK.ink} textAnchor="middle">{name}</text>
        <text x={xC[i]} y={y + 45} fontSize="13" fontWeight="900" fill={c ? BK.coral : BK.ink} textAnchor="middle">{L}</text>
        {where && <text x={xC[i]} y={y + 56} fontSize="8.2" fontWeight="900" fill={BK.muted} textAnchor="middle">{where}</text>}</g>)}</g>; }}/>;

  // the check page's little pictures: a rung; out of Queensland under the bird; out of Kingsland over the turtle; the twins; the five Cs
  const st5 = (y0, x0 = 34) => { const s = []; for (let i = 0; i < 5; i++) s.push({ ...penLine([x0, y0 + i * 4], [88, y0 + i * 4], 1.1), nw: true }); return s; };
  const hd = (x, y, c = PEN_C) => ({ k: 'el', c: [x, y], rx: 3.2, ry: 2.3, f: c });
  const rung = (x, y) => ({ ...penLine([x - 5.5, y], [x + 5.5, y], 1.3), nw: true });
  const rungs = (x, ys) => [...ys.map(y => rung(x, y)), hd(x, ys[ys.length - 1])];
  const chkArts = {
    rung: [...st5(18, 6), ...rungs(46, [14])],
    sky: [...fsBird(14, 13, 0.85), ...st5(20), ...rungs(52, [16]), ...rungs(68, [16, 12]), ...rungs(84, [16, 12, 8])],
    sea: [...st5(4), ...fsTurtle(15, 27, 0.6), ...rungs(52, [24]), ...rungs(68, [24, 28]), ...rungs(84, [24, 28, 32])],
    twins: [{ ...penText(46, 27, 'A = A', { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    cs: [0, 1, 2, 3, 4].map(i => ({ ...penText(14 + i * 16, 37 - i * 6.5, 'C', { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) })),
  };
  const checksRows = [
    ['rung', [0, 0, 92, 40], t('I can point to a ledger line and say what it is', '덧줄을 짚고 덧줄이 뭔지 말할 수 있어요')],
    ['sky', [0, 0, 92, 40], t('I can climb out of Queensland: G, A, B, C, D, E', '퀸즈랜드 밖으로 올라갈 수 있어요: G, A, B, C, D, E')],
    ['sea', [0, 0, 92, 40], t('I can climb out of Kingsland: F, E, D, C, B, A', '킹스랜드 밖으로 내려갈 수 있어요: F, E, D, C, B, A')],
    ['twins', [0, 0, 92, 40], t('I can read the rungs between the lands, both ways', '두 나라 사이의 발판을 두 가지로 읽을 수 있어요')],
    ['cs', [0, 0, 92, 40], t('I can find all five Cs fast, from the sea to the sky', '바다에서 하늘까지 다섯 C를 빨리 찾을 수 있어요')],
  ];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Ledger Lines', '덧줄')}</div>
      </div></LbOnly>
      {pic(p1, 250, 620)}
      <LbSay size={17.5}>{LANG === 'ko' ? <>클라라의 짧은 발판 기억나요? 그 줄에는 진짜 이름이 있어요: <b>{A('B1', '덧줄')}</b>. 덧줄은 {A('B2', '사다리의 발판')}이에요 -- 음이 나라 밖으로 나갈 때, 퀸즈랜드 위로는 새가 사는 하늘까지, 킹스랜드 아래로는 거북이 사는 바다까지 올라가고 내려가게 해 줘요.</>
        : <>Remember Clara's short rung? It has a real name: a <b>{A('B1', 'ledger line')}</b>. Ledger lines are the {A('B2', 'rungs of a ladder')} that lets notes climb out of the lands -- up from Queensland into the bird's sky, down from Kingsland into the turtle's sea.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Clara\'s rung is a ledger line', '클라라의 발판은 덧줄'), 2], [t('Up into the sky', '하늘로 올라가기'), 3], [t('Down into the sea', '바다로 내려가기'), 4], [t('Between the lands', '두 나라 사이'), 5], [t('Five Cs', '다섯 C'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('say what a ledger line is and draw one neatly', '덧줄이 뭔지 말하고 깔끔하게 그을 수 있어요'), t('read up to three rungs above Queensland', '퀸즈랜드 위로 발판 세 개까지 읽을 수 있어요'), t('read up to three rungs below Kingsland', '킹스랜드 아래로 발판 세 개까지 읽을 수 있어요'), t('read the rungs between the lands both ways', '두 나라 사이의 발판을 두 가지로 읽을 수 있어요'), t('find the five Cs from the sea to the sky', '바다에서 하늘까지 다섯 C를 찾을 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkTick(15)}{x}</div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. Clara's rung is a ledger line
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Clara\'s rung is a ledger line', '클라라의 발판은 덧줄')}>
      <LbLive still={stack([<div key="a">{p2a}</div>, <div key="b">{p2b}</div>], 330)} live={<LedgerWrite/>}/>
      <LbSay>{LANG === 'ko' ? <>음이 오선 안에 들어가지 못할 만큼 높거나 낮으면, 그 음 하나만을 위해 짧은 줄을 그어요 -- 이게 <b>덧줄</b>이고, 클라라의 발판도 덧줄이에요. 줄-칸-줄-칸 무늬는 오선 밖에서도 그대로 이어져요. 덧줄은 <b>음표보다 살짝 넓게</b>, 오선과 <b>같은 간격</b>으로, 오선까지 <b>빈틈없이</b>, 음표에 필요한 만큼만 그어요.</>
        : <>When a note is too high or too low for the five lines, we draw a short line just for that note -- a <b>ledger line</b>. Clara's rung is one. The pattern carries on outside the staff: line, space, line, space. A ledger line is just <b>a little wider than the note</b>, the <b>same distance apart</b> as the staff lines, with <b>no gaps</b> back to the staff -- and never one more than the note needs.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>클라라의 C를 쳐요. 그 음이 앉은 짧은 줄의 진짜 이름은 <b>덧줄</b>이에요.</>,
        <>덧줄 위의 음을 하나 더 쳐요: 퀸즈랜드 위 발판의 <b>A</b>. 클라라의 C와 A -- 둘 다 덧줄 위에 있어요.</>,
      ] : [
        <>Play Clara's C. The short line it sits on has a real name: a <b>ledger line</b>.</>,
        <>Play one more note on a ledger line: the <b>A</b> on the rung above Queensland. Clara's C and that A both sit on ledger lines.</>,
      ]}/>
      <LbRemember>{t('A ledger line is a rung for one note: line, space, line, space -- the pattern goes on.', '덧줄은 음 하나를 위한 발판: 줄, 칸, 줄, 칸 -- 무늬는 계속돼요.')}</LbRemember>
    </LbPage>,

    // 3. up into the sky
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Up into the sky', '하늘로 올라가기')}>
      <LbLive still={pic(p3, 250, 640)} live={<LedgerClimb/>}/>
      <LbSay>{LANG === 'ko' ? <>퀸즈랜드의 맨 윗줄 <b>F</b>에서 출발해요. 바로 위 칸은 5챕터의 <b>G</b>. 그 위 첫 발판은 <b>A</b>, 그다음 칸은 <b>B</b>, 둘째 발판은 <b>C</b> -- {A('B3', <b>하늘 C</b>)}예요. 줄, 칸, 줄, 칸 -- 오선 안에서처럼 한 걸음에 한 글자씩. {A('B4', <>발판은 <b>세 개</b>까지: 셋째 발판은 <b>E</b>.</>)}</>
        : <>Start on Queensland's top line, <b>F</b>. Just above it, in the space, is Chapter 5's <b>G</b>. Then rung 1 carries <b>A</b>, the next space <b>B</b>, and rung 2 carries <b>C</b> -- {A('B3', <b>Sky C</b>)}. Line, space, line, space: one letter a step, just like inside the staff. {A('B4', <>We go as high as <b>three rungs</b>: rung 3 is <b>E</b>.</>)}</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손으로 F부터 올라가요: <b>F G A B C</b> -- "줄, 칸, 발판 1, 칸, 발판 2."</>,
        <><b>하늘 C</b>를 찾아요: 클라라의 C에서 C를 두 번 더 올라가요.</>,
      ] : [
        <>With your right hand, climb from F: <b>F G A B C</b> -- "line, space, rung 1, space, rung 2".</>,
        <>Find <b>Sky C</b>: from Clara's C, up to the next C, and the next.</>,
      ]}/>
      <LbRemember>{t('Out of Queensland: G in the space, then A, C, E on the rungs.', '퀸즈랜드 밖으로: 칸에 G, 그다음 발판에 A, C, E.')}</LbRemember>
    </LbPage>,

    // 4. down into the sea
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Down into the sea', '바다로 내려가기')}>
      <LbLive still={pic(p4, 250, 640)} live={<LedgerClimb/>}/>
      <LbSay>{LANG === 'ko' ? <>킹스랜드의 맨 아랫줄 <b>G</b>에서 아래로 내려가요. 바로 아래 칸은 5챕터의 <b>F</b>. 첫 발판은 <b>E</b>, 그다음 칸은 <b>D</b>, 둘째 발판은 <b>C</b> -- {A('B3', <b>바다 C</b>)}예요. 거북이 사는 바다까지 한 걸음에 한 글자씩, 거꾸로: G F E D C. {A('B4', <>셋째 발판은 <b>A</b>.</>)}</>
        : <>Now climb down from Kingsland's bottom line, <b>G</b>. Just under it, in the space, is Chapter 5's <b>F</b>. Rung 1 carries <b>E</b>, the next space <b>D</b>, and rung 2 carries <b>C</b> -- {A('B3', <b>Sea C</b>)}, down in the turtle's sea. One letter a step, backwards: G F E D C. {A('B4', <>Rung 3 is <b>A</b>.</>)}</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>왼손으로 G부터 내려가요: <b>G F E D C</b> -- "줄, 칸, 발판 1, 칸, 발판 2."</>,
        <><b>바다 C</b>를 찾아요: 클라라의 C에서 C를 두 번 더 내려가요.</>,
      ] : [
        <>With your left hand, climb down from G: <b>G F E D C</b> -- "line, space, rung 1, space, rung 2".</>,
        <>Find <b>Sea C</b>: from Clara's C, down to the next C, and the next.</>,
      ]}/>
      <LbRemember>{t('Out of Kingsland: F in the space, then E, C, A on the rungs.', '킹스랜드 밖으로: 칸에 F, 그다음 발판에 E, C, A.')}</LbRemember>
    </LbPage>,

    // 5. between the lands (borrowed rungs)
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Between the lands', '두 나라 사이')}>
      <LbLive still={pic(p5, 280, 640)} live={<LedgerTwins/>}/>
      <LbSay>{LANG === 'ko' ? <>{A('B6', <>두 나라 사이의 발판은 <b>빌려 온 줄</b>이에요. 퀸즈랜드 아래 <b>둘째 발판</b>의 A는 킹스랜드의 <b>맨 윗줄 A</b>와 같은 건반이고, 킹스랜드 위 <b>둘째 발판</b>의 E는 퀸즈랜드의 <b>맨 아랫줄 E</b>와 같은 건반이에요. 클라라의 C는 두 나라 모두에서 발판 하나. 같은 건반을 두 가지로 쓸 수 있어서, 두 손이 각자 자기 나라에 머물 수 있어요.</>)}</>
        : <>{A('B6', <>The rungs between the lands are <b>borrowed</b>. The A on <b>rung 2 under Queensland</b> is the same key as Kingsland's <b>top line, A</b>; the E on <b>rung 2 over Kingsland</b> is the same key as Queensland's <b>bottom line, E</b>. Clara's C is one rung from both lands. The same key can be written two ways -- so each hand can stay in its own land.</>)}</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>위 그림의 세 쌍을 쳐요: A, C, E -- 각각 한 번은 오른손, 한 번은 왼손으로. 같은 소리예요!</>,
        <>오른손으로 퀸즈랜드 아래로 내려가요: <b>E D C B A</b> -- "줄, 칸, 발판 1, 칸, 발판 2" -- 그리고 킹스랜드 맨 윗줄 A를 짚어요.</>,
      ] : [
        <>Play the three pairs above: A, C and E -- each once with the right hand, once with the left. The same sound!</>,
        <>With your right hand, climb down out of Queensland: <b>E D C B A</b> -- "line, space, rung 1, space, rung 2" -- then point to Kingsland's top line, A.</>,
      ]}/>
      <LbRemember>{t('Between the lands, the rungs are borrowed: the same key, two ways.', '두 나라 사이의 발판은 빌려 온 줄: 같은 건반, 두 가지로.')}</LbRemember>
    </LbPage>,

    // 6. five Cs
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Five Cs', '다섯 C')}>
      <LbLive still={pic(p6, 300, 680)} live={<LedgerLandmarks/>}/>
      <LbSay>{LANG === 'ko' ? <>바다에서 하늘까지 C가 다섯 개, 한 옥타브씩 떨어져 있어요: {A('B3', <b>바다 C</b>)}, <b>킹스랜드 C</b>, <b>클라라의 C</b>, <b>퀸즈랜드 C</b>, {A('B3', <b>하늘 C</b>)}. 자리는 발판, 칸, 발판, 칸, 발판 -- 번갈아 가요. 이 책의 덧줄 음은 모두 바다 C, 클라라의 C, 하늘 C에서 한 걸음이나 건너뛰기면 닿아요.</>
        : <>From the sea to the sky there are five Cs, an octave apart: {A('B3', <b>Sea C</b>)}, <b>Kingsland C</b>, <b>Clara's C</b>, <b>Queensland C</b> and {A('B3', <b>Sky C</b>)}. They take turns: rungs, space, rung, space, rungs. Every ledger note in this book is a step or a skip from Sea C, Clara's C or Sky C.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>다섯 C를 낮은 데서 높은 데로 쳐요 -- 이름을 말하면서. 바다 C와 킹스랜드 C는 왼손, 나머지는 오른손.</>,
        <><b>C에서 뛰기:</b> 선생님이 덧줄 음 하나를 짚으면: 가장 가까운 C → 한 걸음 또는 건너뛰기 → 이름 → 쳐요.</>,
      ] : [
        <>Play the five Cs from low to high, naming each one -- Sea C and Kingsland C with the left hand, the others with the right.</>,
        <><b>C hop:</b> your teacher points to a ledger note: nearest C → a step or a skip → name it → play it.</>,
      ]}/>
      <LbRemember>{t('Five Cs from the sea to the sky: find the nearest, then step or skip.', '바다에서 하늘까지 다섯 C: 가장 가까운 C를 찾고, 한 걸음 또는 건너뛰기.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, then tick how it is going -- not yet, nearly, or got it! The check-up on paper is in the Workbook.', '피아노 앞에서 하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요! 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_ll_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
    </LbPage>,
  ];
}
function LedgerLessonBook() { return <>{llLbPages(false)}</>; }
