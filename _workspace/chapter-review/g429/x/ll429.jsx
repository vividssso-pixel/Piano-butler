// ─── Phases 427-429: chapter 6 (Ledger Lines) Lesson Book -- draft v1 (Phase 427), applied after her answers (Phase 428:
// 'G1-3 너가 말한거 다 해당 / 너가 검토한거 책 바탕으로 최적으로 만들어줘' = every B as recommended); Phase 429 (her 22:22):
// 'ladder', not 'rung', in English; guide lines to draw on; the lid on a space note is a mistake to check ───
// Built on her standing decisions: Clara's short line is a 'ladder rung' until this chapter (Book rule 8), the treble
// staff is Queensland and the bass staff Kingsland (chapter 5), high is the bird's sky and low is the turtle's sea
// (chapter 2), the landmarks of chapter 5, the Book rules. B1 ledger line (also spelled leger), B2 the ladder into the
// sky and the sea, B3 Sky C and Sea C, B4 up to three rungs, B5 no A C E lists in the book, B6 Between the lands kept, B9 a minimal opener.
// AMEB (2026 Manual): Music Craft Prelim -- one ledger line below the treble staff; Grade 1 -- one above and below both
// staves; Grade 2 -- up to three. Theory of Music Grade 1 -- two; Grade 2 -- three. 'leger' and 'ledger' both accepted.

function llLbPages(scr = false) {
  const ch = 'ledger-lines';
  const queen = sfQueen(22, 24, 1), king = sfKing(22, 24, 1), clara = sfClara(22, 24, 1);
  const bird = [...fsBird(22, 26, 1), ...fsCloud(10, 12, 0.6)], turtle = [...fsTurtle(22, 26, 0.8), ...fsWaves(2, 36, 40, 0.8, 3)];
  const A = (q, kids) => kids;   // her answers are in (Phase 428): no draft marks left
  const pic = (svg, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{svg}</div></LbPic>;
  const stack = (items, h) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:620,margin:'0 auto'}}>{items}</div></LbPic>;
  const landName = (name, d, st, x = 172) => (yOf, layer, txt) => layer === 'under' && <text x={x} y={yOf(d, st) + 7} fontSize="21" fontWeight="900" fill={BK.coral} fillOpacity="0.2" textAnchor="middle" letterSpacing="3" style={{fontFamily:LB_SERIF}}>{name}</text>;
  const both = (...fs) => (yOf, layer, txt) => <g>{fs.map((f, i) => <g key={i}>{f(yOf, layer, txt)}</g>)}</g>;
  const row = (items, y) => (yOf, layer, txt) => layer === 'over' && <g style={txt}>{items.map(([x, top, sub, coral, name], i) => <g key={i}>
    <text x={x} y={y(yOf)} fontSize="13" fontWeight="900" fill={coral ? BK.coral : BK.ink} textAnchor="middle">{top}</text>
    {sub && <text x={x} y={y(yOf) + 12} fontSize="8.6" fontWeight="900" fill={BK.muted} textAnchor="middle">{sub}</text>}
    {name && <text x={x} y={y(yOf) + 24} fontSize="9.6" fontWeight="900" fill={BK.coral} textAnchor="middle">{name}</text>}</g>)}</g>;
  const rungWord = (n) => n ? (LANG === 'ko' ? n + '번 발판' : 'ladder ' + n) : (LANG === 'ko' ? '칸' : 'space');

  // p1: the ladder out of both lands -- two rungs up into the bird's sky over Queensland, Clara on her rung between the
  // lands, two rungs down into the turtle's sea under Kingsland
  const p1 = <SfStaff clef="grand" width={360} span={[4, 340]} pad={[30, 30]} label={t('The grand staff with ladders: above Queensland two short ledger lines carry the notes A and C up towards a bird in the sky; between the lands Princess Clara stands by middle C on its short line; below Kingsland two ledger lines carry E and C down towards a turtle in the sea', '큰보표의 사다리: 퀸즈랜드 위로 짧은 덧줄 두 개에 A와 C가 하늘의 새를 향해 올라가고, 두 나라 사이에는 클라라 공주가 가운데 도의 짧은 줄 옆에 서 있고, 킹스랜드 아래로 덧줄 두 개에 E와 C가 바다의 거북을 향해 내려가요')}
    notes={[{ d: 40, x: 214, color: PEN_C }, { d: 42, x: 256, color: PEN_C }, { d: 28, x: 112, color: PEN_C }, { d: 16, x: 214, staff: 'bass', color: PEN_C }, { d: 14, x: 256, staff: 'bass', color: PEN_C }]}
    icons={[SF_ICON(bird, 286, 4, 1), SF_ICON(clara, 124, 84, 0.8), SF_ICON(turtle, 284, 196, 0.95)]}
    extra={both(landName(t('QUEENSLAND', '퀸즈랜드'), 34, 'treble', 186), landName(t('KINGSLAND', '킹스랜드'), 22, 'bass', 186))}/>;

  // p2: Clara's rung is a ledger line -- and how to draw one: as wide as the note, the same distance apart, never one too many
  const p2a = <SfStaff clef="treble" width={340} pad={[24, 42]} span={[4, 336]} label={t('Queensland with two notes on short lines of their own: middle C below the staff on Clara\'s ladder, and A above the staff on a ladder of its own -- both are ledger lines', '두 음이 자기만의 짧은 줄 위에 있는 퀸즈랜드: 오선 아래 클라라의 발판 위의 가운데 도, 오선 위 자기 발판 위의 A -- 둘 다 덧줄이에요')}
    notes={[{ d: 28, x: 112, color: PEN_C }, { d: 40, x: 226, color: PEN_C }]} icons={[SF_ICON(clara, 99, 116, 0.6)]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <text x="92" y={yOf(28) + 5} fontSize="14" fontWeight="900" fill={BK.coral} textAnchor="end">C</text>
      <text x="226" y={yOf(40) - 11} fontSize="14" fontWeight="900" fill={BK.coral} textAnchor="middle">A</text>
      {[[28, 112], [40, 226]].map(([d, x]) => <g key={d}>
        <line x1={x + 46} x2={x + 18} y1={yOf(d)} y2={yOf(d)} stroke={BK.coral} strokeWidth="1.5"/>{sfArrowHead(x + 17, yOf(d), -1, BK.coral)}
        <text x={x + 51} y={yOf(d) + 4} fontSize="11.5" fontWeight="900" fill={BK.ink}>{t('ledger line', '덧줄')}</text></g>)}
    </g>}/>;
  const howTo = (ok, cap, bad) => <div style={{textAlign:'center'}}>
    <SfStaff clef="treble" width={128} pad={[12, 18]} span={[4, 124]} label={cap} notes={[{ d: bad === 'lid' ? 41 : 42, x: 66 }]}
      extra={(yOf, layer, txt) => layer === 'under' ? <g>{bad === 'long' && [40, 42].map(d => <line key={d} x1="38" x2="94" y1={yOf(d)} y2={yOf(d)} stroke={BK.ink} strokeWidth="1.4"/>)}{bad === 'lid' && <line x1="54" x2="78" y1={yOf(42)} y2={yOf(42)} stroke={BK.ink} strokeWidth="1.4"/>}</g>
        : <g>{bad === 'gap' && <rect x="50" y={yOf(40) - 3} width="32" height="6" fill={BK.soft}/>}<text x="112" y={yOf(43) + 4} fontSize="17" fontWeight="900" fill={ok ? BK.green : BK.coral} textAnchor="middle">{ok ? '✓' : '✗'}</text></g>}/>
    <div style={{fontSize:11.5,fontWeight:800,color:BK.ink,marginTop:2,lineHeight:1.3}}>{cap}</div></div>;
  const p2b = <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr 1fr',gap:12,alignItems:'start'}}>
    {howTo(true, t('a little wider, the same distance apart', '살짝 넓게, 같은 간격'))}
    {howTo(false, t('not too long', '너무 길면 안 돼요'), 'long')}
    {howTo(false, t('no gap below', '사이가 비면 안 돼요'), 'gap')}
    {howTo(false, t('no lid on a note in a space', '칸 음 위에 뚜껑은 안 돼요'), 'lid')}</div>;

  // p3: up into the sky -- out of Queensland's top line: the space, rung 1, a space, rung 2 (Sky C), a space, rung 3
  const xU = [70, 112, 154, 196, 238, 280, 322];
  const p3 = <SfStaff clef="treble" width={360} pad={[76, 50]} span={[4, 340]} label={t('Up out of Queensland from its top line F: G in the space above, A on ladder 1, B, C on ladder 2 -- Sky C --, D, E on ladder 3, with a bird in the sky', '퀸즈랜드 맨 윗줄 F에서 위로: 위 칸의 G, 1번 발판의 A, B, 2번 발판의 C -- 하늘 C --, D, 3번 발판의 E, 하늘에는 새')}
    notes={[38, 39, 40, 41, 42, 43, 44].map((d, i) => ({ d, x: xU[i], color: i ? PEN_C : undefined }))} icons={[SF_ICON(bird, 282, -44, 1.3)]}
    extra={row([[xU[0], 'F', t('top line', '맨 윗줄')], [xU[1], 'G', rungWord(0), true], [xU[2], 'A', rungWord(1), true], [xU[3], 'B', rungWord(0), true], [xU[4], 'C', rungWord(2), true, t('Sky C', '하늘 C')], [xU[5], 'D', rungWord(0), true], [xU[6], 'E', rungWord(3), true]], (yOf) => yOf(30) + 22)}/>;

  // p4: down into the sea -- out of Kingsland's bottom line: the space, rung 1, a space, rung 2 (Sea C), a space, rung 3
  const p4 = <SfStaff clef="bass" width={360} pad={[60, 74]} span={[4, 340]} label={t('Down out of Kingsland from its bottom line G: F in the space below, E on ladder 1, D, C on ladder 2 -- Sea C --, B, A on ladder 3, with a turtle in the sea', '킹스랜드 맨 아랫줄 G에서 아래로: 아래 칸의 F, 1번 발판의 E, D, 2번 발판의 C -- 바다 C --, B, 3번 발판의 A, 바다에는 거북')}
    notes={[18, 17, 16, 15, 14, 13, 12].map((d, i) => ({ d, x: xU[i], color: i ? PEN_C : undefined }))} icons={[SF_ICON(turtle, 280, 200, 1.3)]}
    extra={row([[xU[0], 'G', t('bottom line', '맨 아랫줄')], [xU[1], 'F', rungWord(0), true], [xU[2], 'E', rungWord(1), true], [xU[3], 'D', rungWord(0), true], [xU[4], 'C', rungWord(2), true, t('Sea C', '바다 C')], [xU[5], 'B', rungWord(0), true], [xU[6], 'A', rungWord(3), true]], (yOf) => yOf(26) - 42)}/>;

  // p5: between the lands -- the rungs there are borrowed: two rungs under Queensland = Kingsland's top line (A); two
  // rungs over Kingsland = Queensland's bottom line (E); Clara's C both ways
  const pairs = [[84, 26, 'A'], [158, 28, 'C'], [232, 30, 'E']];
  const p5 = <SfStaff clef="grand" width={300} gap={64} span={[4, 296]} pad={[18, 22]} label={t('The grand staff with three pairs, each the same key written twice: A on two ladders under Queensland and A on Kingsland\'s top line; middle C on Clara\'s ladder under Queensland and over Kingsland; E on Queensland\'s bottom line and E on two ladders over Kingsland', '같은 건반을 두 번 쓴 세 쌍의 큰보표: 퀸즈랜드 아래 두 발판의 A와 킹스랜드 맨 윗줄의 A; 퀸즈랜드 아래와 킹스랜드 위 클라라 발판의 가운데 도; 퀸즈랜드 맨 아랫줄의 E와 킹스랜드 위 두 발판의 E')}
    notes={pairs.flatMap(([x, d]) => [{ d, x, staff: 'treble', color: PEN_C }, { d, x, staff: 'bass', color: PEN_C }])}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>{pairs.map(([x, d, L], i) => <g key={i}>
      <path d={`M${x + 12} ${yOf(d, 'treble') + 3} Q${x + 30} ${(yOf(d, 'treble') + yOf(d, 'bass')) / 2} ${x + 12} ${yOf(d, 'bass') - 3}`} fill="none" stroke={BK.ink} strokeWidth="1.2" strokeDasharray="3 3"/>
      <text x={x + 27} y={(yOf(d, 'treble') + yOf(d, 'bass')) / 2 + 5} fontSize="14" fontWeight="900" fill={BK.ink}>=</text>
      <text x={x - 16} y={yOf(d, 'treble') + 4} fontSize="12" fontWeight="900" fill={BK.coral} textAnchor="end">{L}</text>
      <text x={x - 16} y={yOf(d, 'bass') + 4} fontSize="12" fontWeight="900" fill={BK.coral} textAnchor="end">{L}</text></g>)}</g>}/>;

  // p6: the five Cs, from the sea to the sky -- rungs, space, rung, space, rungs; and a hop from each new C
  // [d, staff, top label, under label, coral] -- the two navy notes are the hops (Sea C a skip up to E, Sky C a step down to B)
  const C5 = [[14, 'bass', 'C', t('Sea', '바다'), t('2 ladders', '발판 2개'), true], [16, 'bass', 'E', t('a skip up', '건너뛰어 위')], [21, 'bass', 'C', t('Kingsland', '킹스랜드'), t('space', '칸'), true], [28, 'treble', 'C', t('Clara\'s', '클라라의'), t('ladder', '발판'), true], [35, 'treble', 'C', t('Queensland', '퀸즈랜드'), t('space', '칸'), true], [42, 'treble', 'C', t('Sky', '하늘'), t('2 ladders', '발판 2개'), true], [41, 'treble', 'B', t('a step down', '한 걸음 아래')]];
  const xC = [50, 94, 152, 210, 268, 326, 370];
  const p6 = <SfStaff clef="grand" width={404} span={[4, 400]} pad={[30, 64]} label={t('The five Cs from low to high, an octave apart: Sea C on two ladders below Kingsland, Kingsland C in its second space, Clara\'s C on her ladder, Queensland C in its third space, Sky C on two ladders above Queensland; and two hops: from Sea C a skip up to E, from Sky C a step down to B', '낮은 곳부터 한 옥타브씩 떨어진 다섯 C: 킹스랜드 아래 두 발판의 바다 C, 둘째 칸의 킹스랜드 C, 발판 위의 클라라의 C, 셋째 칸의 퀸즈랜드 C, 퀸즈랜드 위 두 발판의 하늘 C; 그리고 두 번 뛰기: 바다 C에서 건너뛰어 위로 E, 하늘 C에서 한 걸음 아래로 B')}
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
    ['twins', [0, 0, 92, 40], t('I can read the ladders between the lands, both ways', '두 나라 사이의 발판을 두 가지로 읽을 수 있어요')],
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
        : <>Remember Clara's little ladder? It has a real name: a <b>{A('B1', 'ledger line')}</b>. Ledger lines are {A('B2', 'little ladders')} that let notes climb out of the lands -- up from Queensland into the bird's sky, down from Kingsland into the turtle's sea.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Clara\'s ladder is a ledger line', '클라라의 발판은 덧줄'), 2], [t('Up into the sky', '하늘로 올라가기'), 3], [t('Down into the sea', '바다로 내려가기'), 4], [t('Between the lands', '두 나라 사이'), 5], [t('Five Cs', '다섯 C'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('say what a ledger line is and draw one neatly', '덧줄이 뭔지 말하고 깔끔하게 그을 수 있어요'), t('read up to three ladders above Queensland', '퀸즈랜드 위로 발판 세 개까지 읽을 수 있어요'), t('read up to three ladders below Kingsland', '킹스랜드 아래로 발판 세 개까지 읽을 수 있어요'), t('read the ladders between the lands both ways', '두 나라 사이의 발판을 두 가지로 읽을 수 있어요'), t('find the five Cs from the sea to the sky', '바다에서 하늘까지 다섯 C를 찾을 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkTick(15)}{x}</div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. Clara's rung is a ledger line
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Clara\'s ladder is a ledger line', '클라라의 발판은 덧줄')}>
      <LbLive still={stack([<div key="a">{p2a}</div>, <div key="b">{p2b}</div>], 330)} live={<LlRungs/>}/>
      <LbSay>{LANG === 'ko' ? <>음이 오선 안에 들어가지 못할 만큼 높거나 낮으면, 그 음 하나만을 위해 짧은 줄을 그어요 -- 이게 <b>덧줄</b>이고, 클라라의 발판도 덧줄이에요. 줄-칸-줄-칸 무늬는 오선 밖에서도 그대로 이어져요. 덧줄은 <b>음표보다 살짝 넓게</b>, 오선과 <b>같은 간격</b>으로, 오선까지 <b>빈틈없이</b>, 음표에 필요한 만큼만 그어요. 칸에 있는 음 위에는 <b>뚜껑</b>처럼 한 줄 더 긋지 않아요.</>
        : <>When a note is too high or too low for the five lines, we draw a short line just for that note -- a <b>ledger line</b>. Clara's ladder is one. The pattern carries on outside the staff: line, space, line, space. A ledger line is just <b>a little wider than the note</b>, the <b>same distance apart</b> as the staff lines, with <b>no gaps</b> back to the staff -- and never one more than the note needs: a note in a space gets <b>no lid</b> on top.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>클라라의 C를 쳐요. 그 음이 앉은 짧은 줄의 진짜 이름은 <b>덧줄</b>이에요.</>,
        <>덧줄 위의 음을 하나 더 쳐요: 퀸즈랜드 위 발판의 <b>A</b>. 클라라의 C와 A -- 둘 다 덧줄 위에 있어요.</>,
      ] : [
        <>Play Clara's C. The short line it sits on has a real name: a <b>ledger line</b>.</>,
        <>Play one more note on a ledger line: the <b>A</b> on the ladder above Queensland. Clara's C and that A both sit on ledger lines.</>,
      ]}/>
      <LbRemember>{t('A ledger line is a little ladder for one note: line, space, line, space -- the pattern goes on.', '덧줄은 음 하나를 위한 발판: 줄, 칸, 줄, 칸 -- 무늬는 계속돼요.')}</LbRemember>
    </LbPage>,

    // 3. up into the sky
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Up into the sky', '하늘로 올라가기')}>
      <LbLive still={pic(p3, 250, 640)} live={<LlClimb clef="treble"/>}/>
      <LbSay>{LANG === 'ko' ? <>퀸즈랜드의 맨 윗줄 <b>F</b>에서 출발해요. 바로 위 칸은 5챕터의 <b>G</b>. 그 위 1번 발판은 <b>A</b>, 그다음 칸은 <b>B</b>, 2번 발판은 <b>C</b> -- {A('B3', <b>하늘 C</b>)}예요. 줄, 칸, 줄, 칸 -- 오선 안에서처럼 한 걸음에 한 글자씩. {A('B4', <>발판은 <b>세 개</b>까지: 3번 발판은 <b>E</b>.</>)}</>
        : <>Start on Queensland's top line, <b>F</b>. Just above it, in the space, is Chapter 5's <b>G</b>. Then ladder 1 carries <b>A</b>, the next space <b>B</b>, and ladder 2 carries <b>C</b> -- {A('B3', <b>Sky C</b>)}. Line, space, line, space: one letter a step, just like inside the staff. {A('B4', <>We go as high as <b>three ladders</b>: ladder 3 is <b>E</b>.</>)}</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손으로 F부터 올라가요: <b>F G A B C</b> -- "줄, 칸, 발판 1, 칸, 발판 2."</>,
        <><b>하늘 C</b>를 찾아요: 클라라의 C에서 C를 두 번 더 올라가요.</>,
      ] : [
        <>With your right hand, climb from F: <b>F G A B C</b> -- "line, space, ladder 1, space, ladder 2".</>,
        <>Find <b>Sky C</b>: from Clara's C, up to the next C, and the next.</>,
      ]}/>
      <LbRemember>{t('Out of Queensland: G in the space, then A, C, E on the ladders.', '퀸즈랜드 밖으로: 칸에 G, 그다음 발판에 A, C, E.')}</LbRemember>
    </LbPage>,

    // 4. down into the sea
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Down into the sea', '바다로 내려가기')}>
      <LbLive still={pic(p4, 250, 640)} live={<LlClimb clef="bass"/>}/>
      <LbSay>{LANG === 'ko' ? <>킹스랜드의 맨 아랫줄 <b>G</b>에서 아래로 내려가요. 바로 아래 칸은 5챕터의 <b>F</b>. 1번 발판은 <b>E</b>, 그다음 칸은 <b>D</b>, 2번 발판은 <b>C</b> -- {A('B3', <b>바다 C</b>)}예요. 거북이 사는 바다까지 한 걸음에 한 글자씩, 거꾸로: G F E D C. {A('B4', <>3번 발판은 <b>A</b>.</>)}</>
        : <>Now climb down from Kingsland's bottom line, <b>G</b>. Just under it, in the space, is Chapter 5's <b>F</b>. Ladder 1 carries <b>E</b>, the next space <b>D</b>, and ladder 2 carries <b>C</b> -- {A('B3', <b>Sea C</b>)}, down in the turtle's sea. One letter a step, backwards: G F E D C. {A('B4', <>Ladder 3 is <b>A</b>.</>)}</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>왼손으로 G부터 내려가요: <b>G F E D C</b> -- "줄, 칸, 발판 1, 칸, 발판 2."</>,
        <><b>바다 C</b>를 찾아요: 클라라의 C에서 C를 두 번 더 내려가요.</>,
      ] : [
        <>With your left hand, climb down from G: <b>G F E D C</b> -- "line, space, ladder 1, space, ladder 2".</>,
        <>Find <b>Sea C</b>: from Clara's C, down to the next C, and the next.</>,
      ]}/>
      <LbRemember>{t('Out of Kingsland: F in the space, then E, C, A on the ladders.', '킹스랜드 밖으로: 칸에 F, 그다음 발판에 E, C, A.')}</LbRemember>
    </LbPage>,

    // 5. between the lands (borrowed rungs)
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Between the lands', '두 나라 사이')}>
      <LbLive still={pic(p5, 280, 640)} live={<LlTwins/>}/>
      <LbSay>{LANG === 'ko' ? <>{A('B6', <>두 나라 사이의 발판은 <b>빌려 온 줄</b>이에요. 퀸즈랜드 아래 <b>2번 발판</b>의 A는 킹스랜드의 <b>맨 윗줄 A</b>와 같은 건반이고, 킹스랜드 위 <b>2번 발판</b>의 E는 퀸즈랜드의 <b>맨 아랫줄 E</b>와 같은 건반이에요. 클라라의 C는 어느 나라에서 봐도 발판 하나 위에 있어요. 같은 건반을 두 가지로 쓸 수 있어서, 두 손이 각자 자기 나라에 머물 수 있어요.</>)}</>
        : <>{A('B6', <>The ladders between the lands are <b>borrowed</b>. The A on <b>ladder 2 under Queensland</b> is the same key as Kingsland's <b>top line, A</b>; the E on <b>ladder 2 over Kingsland</b> is the same key as Queensland's <b>bottom line, E</b>. Clara's C sits on one ladder, seen from either land. The same key can be written two ways -- so each hand can stay in its own land.</>)}</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>위 그림의 세 쌍을 쳐요: A, C, E -- 각각 한 번은 오른손, 한 번은 왼손으로. 같은 소리예요!</>,
        <>오른손으로 퀸즈랜드 아래로 내려가요: <b>E D C B A</b> -- "줄, 칸, 발판 1, 칸, 발판 2" -- 그리고 킹스랜드 맨 윗줄 A를 짚어요.</>,
      ] : [
        <>Play the three pairs above: A, C and E -- each once with the right hand, once with the left. The same sound!</>,
        <>With your right hand, climb down out of Queensland: <b>E D C B A</b> -- "line, space, ladder 1, space, ladder 2" -- then point to Kingsland's top line, A.</>,
      ]}/>
      <LbRemember>{t('Between the lands, the ladders are borrowed: the same key, two ways.', '두 나라 사이의 발판은 빌려 온 줄: 같은 건반, 두 가지로.')}</LbRemember>
    </LbPage>,

    // 6. five Cs
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Five Cs', '다섯 C')}>
      <LbLive still={pic(p6, 300, 680)} live={<LlFiveCs/>}/>
      <LbSay>{LANG === 'ko' ? <>바다에서 하늘까지 C가 다섯 개, 한 옥타브씩 떨어져 있어요: {A('B3', <b>바다 C</b>)}, <b>킹스랜드 C</b>, <b>클라라의 C</b>, <b>퀸즈랜드 C</b>, {A('B3', <b>하늘 C</b>)}. 자리는 발판, 칸, 발판, 칸, 발판 -- 번갈아 가요. 이 책의 덧줄 음은 모두 바다 C, 클라라의 C, 하늘 C에서 한 걸음이나 건너뛰기면 닿아요.</>
        : <>From the sea to the sky there are five Cs, an octave apart: {A('B3', <b>Sea C</b>)}, <b>Kingsland C</b>, <b>Clara's C</b>, <b>Queensland C</b> and {A('B3', <b>Sky C</b>)}. They take turns: ladders, space, ladder, space, ladders. Every ledger note in this book is a step or a skip from Sea C, Clara's C or Sky C.</>}</LbSay>
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

// ─── Phase 428: chapter 6 applied -- the moving parts (one per book page), the drill's words, the Workbook, the Teacher copy ───
const llLand = (clef) => clef === 'treble' ? t('Queensland', '퀸즈랜드') : t('Kingsland', '킹스랜드');
const LL_C = { 14: () => t('Sea C', '바다 C'), 21: () => t('Kingsland C', '킹스랜드 C'), 28: () => t('Clara\'s C', '클라라의 C'), 35: () => t('Queensland C', '퀸즈랜드 C'), 42: () => t('Sky C', '하늘 C') };
const llRungCount = (clef, d) => ledgersFor(d, CLEFS[clef].low, CLEFS[clef].high).length;
// where a note sits, in the lands' words: 'on rung 2 over Queensland', 'just under Kingsland's bottom line', 'Kingsland's top line'
function llPlace(clef, d) {
  const c = CLEFS[clef], L = llLand(clef), ko = LANG === 'ko';
  if (d >= c.low && d <= c.high) {
    if (d === c.high) return ko ? L + ' 맨 윗줄' : L + '\'s top line';
    if (d === c.low) return ko ? L + ' 맨 아랫줄' : L + '\'s bottom line';
    const k = d - c.low;
    return k % 2 === 0 ? (ko ? L + ' ' + (k / 2 + 1) + '번 줄' : L + ' line ' + (k / 2 + 1)) : (ko ? L + ' ' + ((k + 1) / 2) + '번 칸' : L + ' space ' + ((k + 1) / 2));
  }
  const up = d > c.high, k = up ? d - c.high : c.low - d, r = Math.floor(k / 2);
  if (k === 1) return up ? (ko ? L + ' 맨 윗줄 바로 위 칸' : 'just over ' + L + '\'s top line') : (ko ? L + ' 맨 아랫줄 바로 아래 칸' : 'just under ' + L + '\'s bottom line');
  if (k % 2 === 0) return up ? (ko ? L + ' 위 ' + r + '번 발판' : 'on ladder ' + r + ' over ' + L) : (ko ? L + ' 아래 ' + r + '번 발판' : 'on ladder ' + r + ' under ' + L);
  return up ? (ko ? L + ' 위 ' + r + '번 발판 위 칸' : 'above ladder ' + r + ' over ' + L) : (ko ? L + ' 아래 ' + r + '번 발판 아래 칸' : 'below ladder ' + r + ' under ' + L);
}
const llBtnRow = (kids) => <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>{kids}</div>;

// page 2's moving part: draw the rungs -- add them one at a time, out from the staff, then check (no gaps, none too many)
const LL_RUNG_TASKS = [['treble', 40], ['bass', 14], ['treble', 28], ['treble', 39], ['bass', 16], ['treble', 42], ['bass', 30], ['treble', 41], ['bass', 12], ['treble', 26], ['bass', 17], ['treble', 44], ['bass', 15], ['bass', 28]];
function LlRungs() {
  const [i, setI] = useState(0);
  const [n, setN] = useState(0);
  const [v, setV] = useState(null);   // null | 'ok' | 'gap' | 'many'
  const [clef, d] = LL_RUNG_TASKS[i % LL_RUNG_TASKS.length], c = CLEFS[clef];
  const up = d > c.high, need = llRungCount(clef, d);
  const rungAt = (j) => up ? c.high + 2 * (j + 1) : c.low - 2 * (j + 1);   // ladder j + 1, counted out from the staff
  const add = (k) => { setV(null); setN(x => Math.max(0, Math.min(4, x + k))); };
  const check = () => { const r = n === need ? 'ok' : n < need ? 'gap' : 'many'; setV(r); if (r === 'ok') playKey(dMidiKey(d), 0.4); };
  const next = () => { setI(x => x + 1); setN(0); setV(null); };
  const X = 170, col = v === 'ok' ? BK.green : PEN_C;
  const msg = v === 'ok' ? (need === 0 ? t('Right -- no ladder at all: ' + dName(d) + ' sits ' + llPlace(clef, d) + '.', '맞아요 -- 발판이 필요 없어요: ' + dName(d) + '는 ' + llPlace(clef, d) + '에 있어요.')
      : t('Neat! ' + need + (need > 1 ? ' ladders' : ' ladder') + ': ' + dName(d) + ' sits ' + llPlace(clef, d) + '.', '깔끔해요! 발판 ' + need + '개: ' + dName(d) + '는 ' + llPlace(clef, d) + '에 있어요.'))
    : v === 'gap' ? t('There is a gap -- the note is floating. Add a ladder.', '사이가 비었어요 -- 음이 떠 있어요. 발판을 하나 더 그어요.')
    : v === 'many' ? ((up ? d - c.high : c.low - d) % 2 && n === need + 1 ? t('That is a lid -- a note in a space gets no line ' + (up ? 'on top of it.' : 'under it.'), '뚜껑이에요 -- 칸에 있는 음 ' + (up ? '위' : '아래') + '에는 줄을 긋지 않아요.')
      : t('One ladder too many -- the note doesn\'t reach it.', '발판이 하나 더 있어요 -- 음이 거기까지 가지 않아요.'))
    : t('How many ladders does this note need? Add them one at a time, out from the staff.', '이 음에는 발판이 몇 개 필요할까요? 오선에서부터 하나씩 그어 봐요.');
  return (
    <div className="try-box" style={actBox}>
      <div style={actTitle}>{t('Draw the ladders', '발판 그리기')}</div>
      <div style={actNote}>{t('A ledger line is a little wider than the note, the same distance apart as the staff lines -- no gaps, and never one too many.', '덧줄은 음표보다 살짝 넓게, 오선과 같은 간격으로 -- 빈틈없이, 필요한 만큼만.')}</div>
      <div style={{maxWidth:420,margin:'0 auto'}}>
        <SfStaff clef={clef} width={300} span={[4, 296]} pad={up ? [52, 16] : [16, 52]} label={t('A note ' + (up ? 'above' : 'below') + ' ' + llLand(clef) + ' with ' + n + ' ladders drawn', llLand(clef) + (up ? ' 위' : ' 아래') + '의 음, 발판 ' + n + '개')}
          extra={(yOf, layer, txt) => layer === 'over' && <g>
            {Array.from({ length: n }, (_, j) => <line key={j} x1={X - 13} x2={X + 13} y1={yOf(rungAt(j))} y2={yOf(rungAt(j))} stroke={v === 'many' && j >= need ? BK.coral : BK.ink} strokeWidth="1.6"/>)}
            <ellipse cx={X} cy={yOf(d)} rx="7.4" ry="5.2" fill={col}/><ellipse cx={X} cy={yOf(d)} rx="3.4" ry="2.7" transform={`rotate(-38 ${X} ${yOf(d)})`} fill="#fff"/>
            <text x={X + 24} y={yOf(d) + 5} fontSize="15" fontWeight="900" fill={col} style={txt}>{dName(d)}</text>
          </g>}/>
      </div>
      <div style={{textAlign:'center',fontSize:14,fontWeight:800,minHeight:40,color:v === 'ok' ? BK.green : v ? BK.coral : BK.ink,margin:'4px 0 0',lineHeight:1.4}}>{msg}</div>
      {llBtnRow(v === 'ok' ? [<button key="n" className="chip active" onClick={next}>{t('Next note →', '다음 음 →')}</button>]
        : [<button key="m" className="ghost-btn" disabled={n === 0} onClick={() => add(-1)}>{t('− ladder', '− 발판')}</button>, <button key="p" className="ghost-btn" disabled={n >= 4} onClick={() => add(1)}>{t('+ ladder', '+ 발판')}</button>, <button key="c" className="chip active" onClick={check}>{t('Check', '확인')}</button>])}
    </div>
  );
}

// pages 3 and 4's moving part: climb out of the land a step at a time -- the ladder stays drawn behind you
function LlClimb({ clef = 'treble' }) {
  const c = CLEFS[clef], up = clef === 'treble';
  const start = up ? c.high : c.low, end = up ? c.high + 6 : c.low - 6;
  const [d, setD] = useState(start);
  const go = (k) => { const nd = d + k; if (up ? (nd < start || nd > end) : (nd > start || nd < end)) return; playKey(dMidiKey(nd), 0.3); setD(nd); };
  const path = []; for (let x = start; up ? x <= d : x >= d; x += up ? 1 : -1) path.push(x);
  const xs = (j) => 62 + j * 40;
  const bird = [...fsBird(22, 26, 1), ...fsCloud(10, 12, 0.6)], turtle = [...fsTurtle(22, 26, 0.8), ...fsWaves(2, 36, 40, 0.8, 3)];
  const steps = up ? Math.abs(end - d) : Math.abs(d - end);
  const where = llPlace(clef, d), cn = LL_C[d];
  return (
    <div className="try-box" style={actBox}>
      <div style={actTitle}>{up ? t('Climb up into the sky', '하늘로 올라가기') : t('Climb down into the sea', '바다로 내려가기')}</div>
      <div style={actNote}>{up ? t('Start on Queensland\'s top line, F. Step up: line, space, ladder -- one letter a step.', '퀸즈랜드 맨 윗줄 F에서 출발해요. 한 걸음씩 위로: 줄, 칸, 발판 -- 한 걸음에 한 글자.')
        : t('Start on Kingsland\'s bottom line, G. Step down: line, space, ladder -- one letter a step, backwards.', '킹스랜드 맨 아랫줄 G에서 출발해요. 한 걸음씩 아래로: 줄, 칸, 발판 -- 한 걸음에 한 글자, 거꾸로.')}</div>
      <div style={{maxWidth:460,margin:'0 auto'}}>
        <SfStaff clef={clef} width={340} span={[4, 336]} pad={up ? [56 + 5 * steps, 26] : [26, 52 + 5 * steps]} label={t(dName(d) + ', ' + where, dName(d) + ', ' + where)}
          notes={path.map((x, j) => ({ d: x, x: xs(j), color: x === d ? PEN_C : undefined }))}
          icons={[SF_ICON(up ? bird : turtle, 290, up ? dY(end) - 52 : dY(end) + 6, 1)]}
          extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>{path.map((x, j) => <text key={j} x={xs(j)} y={up ? yOf(c.low) + 22 : yOf(c.high) - 14} fontSize="13" fontWeight="900" fill={x === d ? BK.coral : BK.ink} textAnchor="middle">{dName(x)}</text>)}</g>}/>
      </div>
      <div style={{textAlign:'center',fontSize:16,fontWeight:900,marginTop:4}}>{dName(d)} <span style={{fontWeight:700,color:BK.muted,fontSize:14}}>-- {where}</span>{cn && <b style={{color:BK.coral}}> · {cn()}</b>}</div>
      {llBtnRow([<button key="a" className="ghost-btn" disabled={up ? d <= start : d >= start} onClick={() => go(up ? -1 : 1)}>{up ? t('↓ Back down', '↓ 다시 아래로') : t('↑ Back up', '↑ 다시 위로')}</button>,
        <button key="b" className="ghost-btn" style={{color:BK.coral}} disabled={up ? d >= end : d <= end} onClick={() => go(up ? 1 : -1)}>{up ? t('Step up ↑', '한 걸음 위로 ↑') : t('Step down ↓', '한 걸음 아래로 ↓')}</button>])}
    </div>
  );
}
function LlClimbBoth() {   // the toolbox: either ladder
  const [c, setC] = useState('treble');
  return <div>
    <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'0 0 -2px'}}>{[['treble', t('Up out of Queensland', '퀸즈랜드 위로')], ['bass', t('Down out of Kingsland', '킹스랜드 아래로')]].map(([k, l]) => <button key={k} className={'chip' + (c === k ? ' active' : '')} style={{padding:'3px 10px',fontSize:13}} onClick={() => setC(k)}>{l}</button>)}</div>
    <LlClimb key={c} clef={c}/>
  </div>;
}

// page 5's moving part: a note between the lands, seen from both lands -- one key on the piano
const LL_BETWEEN = [26, 27, 28, 29, 30];
function LlTwins() {
  const [d, setD] = useState(26);
  const pick = (x) => { setD(x); playKey(dMidiKey(x), 0.4); };
  return (
    <div className="try-box" style={actBox}>
      <div style={actTitle}>{t('The same key, two ways', '같은 건반, 두 가지로')}</div>
      <div style={actNote}>{t('Tap a note between the lands: see it in Queensland and in Kingsland -- one key on the piano.', '두 나라 사이의 음을 눌러 봐요: 퀸즈랜드에서도, 킹스랜드에서도 -- 피아노에서는 건반 하나예요.')}</div>
      <div style={{display:'flex',gap:5,justifyContent:'center',margin:'0 0 6px'}}>{LL_BETWEEN.map(x => <button key={x} className={'chip' + (x === d ? ' active' : '')} style={{padding:'3px 12px',fontSize:14}} onClick={() => pick(x)}>{dName(x)}</button>)}</div>
      <div style={{maxWidth:420,margin:'0 auto'}}>
        <SfStaff clef="grand" width={340} gap={64} span={[4, 336]} pad={[14, 18]} label={t(dName(d) + ': ' + llPlace('treble', d) + ', the same key as ' + llPlace('bass', d), dName(d) + ': ' + llPlace('treble', d) + ', ' + llPlace('bass', d) + '과 같은 건반')}
          notes={[{ d, x: 96, staff: 'treble', color: PEN_C }, { d, x: 96, staff: 'bass', color: PEN_C }]}
          extra={(yOf, layer, txt) => { const a = yOf(d, 'treble'), b = yOf(d, 'bass'); return layer === 'over' && <g style={txt}>
            <path d={`M108 ${a + 3} Q126 ${(a + b) / 2} 108 ${b - 3}`} fill="none" stroke={BK.ink} strokeWidth="1.2" strokeDasharray="3 3"/>
            <text x="123" y={(a + b) / 2 + 5} fontSize="15" fontWeight="900" fill={BK.ink}>=</text>
            <text x="134" y={a + 4} fontSize="11" fontWeight="900" fill={BK.coral}>{llPlace('treble', d)}</text>
            <text x="134" y={b + 4} fontSize="11" fontWeight="900" fill={BK.coral}>{llPlace('bass', d)}</text></g>; }}/>
      </div>
      <div style={{marginTop:6}}><TapKeyboard octaves={3} labels="white" marks={{ [dToKey(d)]: 'good' }} onTap={(k) => playKey(k - 12)}/></div>
    </div>
  );
}

// page 6's moving part: the five Cs (tap to hear and see where each one lives), then the C hop -- name a ledger note from the nearest C
const LL_FIVE = [[14, 'bass'], [21, 'bass'], [28, 'treble'], [35, 'treble'], [42, 'treble']];
const LL_HOPS = [[41, 'treble', 42], [43, 'treble', 42], [40, 'treble', 42], [44, 'treble', 42], [27, 'treble', 28], [29, 'bass', 28], [26, 'treble', 28], [30, 'bass', 28], [15, 'bass', 14], [13, 'bass', 14], [16, 'bass', 14], [12, 'bass', 14]];
const llHopWord = (from, to) => { const k = to - from; return Math.abs(k) === 1 ? (k > 0 ? t('a step up', '한 걸음 위') : t('a step down', '한 걸음 아래')) : (k > 0 ? t('a skip up', '건너뛰어 위') : t('a skip down', '건너뛰어 아래')); };
function LlFiveCs() {
  const [mode, setMode] = useState('cs');
  const [c, setC] = useState(2);
  const [h, setH] = useState(0);
  const [ans, setAns] = useState(null);
  const tapC = (i) => { setC(i); playKey(dMidiKey(LL_FIVE[i][0]), 0.4); };
  const [hd, hst, hc] = LL_HOPS[h % LL_HOPS.length];
  const answer = (L) => { if (ans) return; setAns(L); playKey(dMidiKey(hd), 0.35); };
  const next = () => { setAns(null); setH(x => (x + 5) % LL_HOPS.length); };
  const ok = ans === dName(hd);
  const xC = [64, 118, 172, 226, 280];
  return (
    <div className="try-box" style={actBox}>
      <div style={{display:'flex',gap:6,justifyContent:'center',margin:'0 0 8px'}}>{[['cs', t('The five Cs', '다섯 C')], ['hop', t('C hop', 'C에서 뛰기')]].map(([k, l]) => <button key={k} className={'chip' + (mode === k ? ' active' : '')} style={{padding:'3px 12px',fontSize:13.5}} onClick={() => setMode(k)}>{l}</button>)}</div>
      {mode === 'cs' ? <>
        <div style={actNote}>{t('Tap a C, from the sea to the sky: hear it, see where it lives.', '바다에서 하늘까지, C를 눌러 봐요: 소리를 듣고, 어디 사는지 봐요.')}</div>
        <div style={{maxWidth:440,margin:'0 auto'}}>
          <SfStaff clef="grand" width={340} span={[4, 336]} pad={[14, 22]} label={t('The five Cs on the grand staff', '큰보표 위의 다섯 C')}
            notes={LL_FIVE.map(([d, st], i) => ({ d, staff: st, x: xC[i], color: i === c ? PEN_C : undefined }))}/>
        </div>
        <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',margin:'6px 0 4px'}}>{LL_FIVE.map(([d], i) => <button key={d} className={'chip' + (i === c ? ' active' : '')} style={{padding:'3px 9px',fontSize:13}} onClick={() => tapC(i)}>{LL_C[d]()}</button>)}</div>
        <div style={{textAlign:'center',fontSize:14.5,fontWeight:800,color:BK.ink}}><b style={{color:BK.coral}}>{LL_C[LL_FIVE[c][0]]()}</b> -- {llPlace(LL_FIVE[c][1], LL_FIVE[c][0])}</div>
      </> : <>
        <div style={actNote}>{t('Find the nearest C first -- Sea C, Clara\'s C or Sky C. Then a step or a skip: which note is it?', '먼저 가장 가까운 C를 찾아요 -- 바다 C, 클라라의 C, 하늘 C. 그다음 한 걸음이나 건너뛰기: 무슨 음일까요?')}</div>
        <div style={{maxWidth:440,margin:'0 auto'}}>
          <SfStaff clef="grand" width={340} span={[4, 336]} pad={[14, 22]} label={t('A ledger note to name', '이름을 맞힐 덧줄 음')}
            notes={[{ d: hd, staff: hst, x: 200, color: ans ? (ok ? BK.green : PEN_C) : undefined }, ...(ans ? [{ d: hc, staff: hst, x: 150, color: PEN_C }] : [])]}
            extra={(yOf, layer, txt) => ans && layer === 'over' && <g style={txt}>{hd > hc ? sfHop(156, 194, Math.min(yOf(hc, hst), yOf(hd, hst)) - 9, 10) : sfHop(156, 194, Math.max(yOf(hc, hst), yOf(hd, hst)) + 9, -10)}</g>}/>
        </div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(7,1fr)',gap:5,marginTop:6}}>{STAFF_LETTERS.map(L => <button key={L} className={'choice-btn' + (!ans ? '' : L === dName(hd) ? ' good' : L === ans ? ' bad' : '')} onClick={() => answer(L)}>{L}</button>)}</div>
        {ans && <div style={{textAlign:'center',fontSize:14,fontWeight:800,marginTop:8,color:ok ? BK.green : BK.coral}}>{ok ? t('Yes! ', '맞아요! ') : t('Not quite. ', '아쉬워요. ')}<span style={{color:BK.ink}}>{t('From ' + LL_C[hc]() + ', ' + llHopWord(hc, hd) + ': ' + dName(hd) + '.', LL_C[hc]() + '에서 ' + llHopWord(hc, hd) + ': ' + dName(hd) + '.')}</span></div>}
        {ans && llBtnRow([<button key="n" className="chip active" onClick={next}>{t('Next note →', '다음 음 →')}</button>])}
      </>}
    </div>
  );
}

// ── the Workbook (Phase 428): faces the Lesson Book page by page; set tasks, solo, big staves, full pages ──
// a note may carry its own rungs on paper: rungs = [[d, half-width], ...] (none = []): the neat-or-not pictures and the bare notes to draw on
const llNeat = (clef, d, flaw) => { const c = CLEFS[clef], L = ledgersFor(d, c.low, c.high), out = d > c.high ? 2 : -2;
  return flaw === 'gap' ? L.slice(1).map(p => [p, 11]) : flaw === 'long' ? L.map(p => [p, 25]) : flaw === 'many' || flaw === 'lid' ? [...L, L[L.length - 1] + out].map(p => [p, 11]) : L.map(p => [p, 11]); };
function llWorkbook() {
  const k = (s) => 'll-wb428-' + s;
  const neat = withSeed(k('neat'), () => [['treble', 40, null], ...shuffle([['bass', 14, 'gap'], ['treble', 26, null], ['treble', 41, 'lid'], ['treble', 42, 'long']])]);
  const draw = [['treble', 40], ['treble', 42], ['bass', 16], ['treble', 39], ['treble', 44], ['bass', 15], ['treble', 26], ['treble', 41]];   // ladders: (1) 2 1 0 3 1 2 1
  return {
    neat, draw,
    count: [39, 43, 28, 44, 29, 41, 26, 27],                                  // ladders: 0 2 1 3 0 1 2 1
    sky: { tog: [38, 39, 40, 41, 42, 43, 44], given: [0, 3, 5], ex: 1, home: [42, 40, 44, 39, 43, 41, 38, 40] },   // fill the ladder: F, B, D printed, G drawn as the example
    sea: { tog: [18, 17, 16, 15, 14, 13, 12], given: [0, 3, 5], ex: 1, home: [14, 16, 12, 17, 13, 15, 18, 16] },
    twins: [[27, 'treble'], [29, 'treble'], [26, 'treble'], [29, 'bass'], [30, 'bass'], [27, 'bass']],   // B D A into Kingsland, D E B into Queensland
    between: { tre: [26, 28, 29, 27], bas: [30, 28, 27, 29] },   // under Queensland: A C D B; over Kingsland: E C B D
    same: [[26, 26], [27, 26], [30, 29], [30, 30]],   // [Queensland's note, Kingsland's note]: yes, no, no, yes
    hop: [[41, 'treble'], [16, 'bass'], [29, 'bass'], [12, 'bass']],   // B (Sky C), E (Sea C), D (Clara's C), A (Sea C)
    fast: { tre: [43, 27, 44, 40], bas: [13, 30, 15, 28] },
  };
}
const LL_WORDS_SKY = [{ word: 'BADGE', notes: [41, 40, 43, 39, 44] }, { word: 'CAGE', notes: [42, 40, 39, 44] }];
const LL_WORDS_SEA = [{ word: 'BEAD', notes: [13, 16, 12, 15] }, { word: 'CAFE', notes: [14, 12, 17, 16] }];
const LL_MSG = { word: 'CABBAGE', notes: [[42, 'treble'], [40, 'treble'], [13, 'bass'], [27, 'treble'], [12, 'bass'], [39, 'treble'], [16, 'bass']] };
const llNearC = (d) => [14, 28, 42].reduce((b, m) => Math.abs(m - d) < Math.abs(b - d) ? m : b, 14);
const LL_C_WORD = { 14: 'Sea', 28: 'Clara\'s', 42: 'Sky' };
// the Teacher copy's short place words (English only): 'rung 1', 'above rung 1', 'just over the top line'
function llShort(clef, d) {
  const c = CLEFS[clef];
  if (d === c.high) return 'top line'; if (d === c.low) return 'bottom line';
  if (d > c.low && d < c.high) return (d - c.low) % 2 === 0 ? 'line ' + ((d - c.low) / 2 + 1) : 'space ' + ((d - c.low + 1) / 2);
  const up = d > c.high, k = up ? d - c.high : c.low - d, r = Math.floor(k / 2);
  if (k === 1) return up ? 'just over the top line' : 'just under the bottom line';
  return k % 2 === 0 ? 'ladder ' + r : (up ? 'above ladder ' : 'below ladder ') + r;
}
// the three Cs a ledger note hops from, as pictures to circle: the turtle (Sea C), Clara (her C), the bird (Sky C)
const llCPick = (on) => <span style={{display:'inline-flex',gap:3}}>{[[14, [...fsTurtle(22, 26, 0.8)]], [28, sfClara(22, 24, 1)], [42, [...fsBird(22, 26, 1)]]].map(([c, sh]) => <span key={c} style={{width:40,height:40,borderRadius:20,border:'1.6px solid ' + (on === c ? BK.coral : 'transparent'),display:'inline-flex',alignItems:'center',justifyContent:'center'}}><PenArt shapes={sh} vb={[0, 0, 44, 44]} style={{width:34}}/></span>)}</span>;

function LedgerWorkbook({ startNo = 1 }) {
  const W = useMemo(() => llWorkbook(), [LANG]);
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="ledger-lines">{content}</WbPage>);
  const cellStaff = (clef, notes, w = 104, ms) => <PaperStaff clef={clef} notes={notes} width={w} minSpan={ms}/>;
  const names = (list, width, clef, exFirst, from = 1, ms) => { const xs = sfXs(list.length, width, true);
    return <SfRow clef={clef} width={width} notes={list.map((d, i) => ({ d, x: xs[i] }))} minSpan={ms}
      items={list.map((d, i) => ({ x: xs[i], n: from + i, ex: exFirst && i === 0, ans: dName(d) }))}/>; };
  const words = (list, clef, n0, W0 = 510) => list.map((w, j) => { const xs = sfXs(w.word.length, W0, true); return <div key={j} style={{marginTop:j ? 6 : 0}}>
    <div style={{fontSize:13.5,fontWeight:800,color:BK.ink,margin:'0 0 2px'}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700}}>{n0 + j}</span> · {w.word}</div>
    <SfRow clef={clef} width={W0} notes={[]} guides={clef === 'treble' ? [3, 0] : [0, 3]} minSpan={clef === 'treble' ? [30, 45] : [8, 26]} items={xs.map((x, i) => ({ x, ex: true, ans: w.word[i], w: 32 }))}/>
  </div>; });

  // a ladder out of a land with some notes printed: the child draws the others over their letters (the first one drawn in coral)
  const ladder = (L, clef, ms) => { const xs = sfXs(L.tog.length, 470, true);
    return <SfRow clef={clef} width={470} guides={clef === 'treble' ? [3, 0] : [0, 3]} notes={L.tog.map((d, i) => ({ d, x: xs[i], i })).filter(n => L.given.includes(n.i) || n.i === L.ex).map(n => ({ d: n.d, x: n.x, color: n.i === L.ex ? BK.coral : undefined, rungC: n.i === L.ex ? BK.coral : undefined }))} minSpan={ms}
      items={L.tog.map((d, i) => ({ x: xs[i], label: dName(d) }))}/>; };

  // 2 (faces "Clara's rung is a ledger line")
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Neat or not?" how="Circle ✓ if the ladders are drawn right, ✗ if they are not: too long, a gap, or a lid on top.">
      <BkGrid cols={5} gap="8px 8px">{W.neat.map(([cl, d, flaw], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'12px 2px 3px'}}>
        {cellStaff(cl, [{ d, rungs: llNeat(cl, d, flaw) }], 104)}
        <div style={{display:'flex',justifyContent:'center',marginTop:3}}>{wsChoose(['✓', '✗'], i === 0 ? (flaw ? '✗' : '✓') : null)}</div>
      </div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Draw the ladders" how="Draw the ladders each note needs on the dotted lines. Some need none.">
      <BkGrid cols={4} gap="8px 10px">{W.draw.map(([cl, d], i) => <ExCell key={i} n={i + 6} ex={i === 0}><div style={{padding:'12px 4px 3px'}}>
        <PaperStaff clef={cl} notes={[{ d, rungs: i === 0 ? null : [], rungC: BK.coral, color: i === 0 ? BK.coral : undefined }]} width={92} guides={d > CLEFS[cl].high ? [3, 0] : [0, 3]}/>
      </div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="play" title="How many ladders?" how="The ladders are missing. Count the dotted lines out to each note: how many does it need? 0, 1, 2 or 3.">
      {(() => { const xs = sfXs(W.count.length, 440, true); return <SfRow clef="treble" width={440} notes={W.count.map((d, i) => ({ d, x: xs[i], rungs: [] }))} guides={[3, 2]}
        items={W.count.map((d, i) => ({ x: xs[i], n: 14 + i, ex: i === 0, ans: String(llRungCount('treble', d)) }))}/>; })()}
    </Part>
    <Faces/>
  </>);

  // 3 (faces "Up into the sky")
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="The missing notes" how="Some notes are missing. Draw each one above its letter, one step up from the last, with its ladders.">
      {ladder(W.sky, 'treble', [30, 45])}
    </Part>
    <Part kind="home" title="Name the sky notes" how="Count up from Queensland's top line, F, and write each letter.">
      {names(W.sky.home, 470, 'treble', false, 1, [30, 45])}
    </Part>
    <Part kind="play" title="Words in the sky" how="Draw each note above its letter, with its ladders. Then play the words with your right hand.">
      {words(LL_WORDS_SKY, 'treble', 9)}
    </Part>
    <Faces/>
  </>);

  // 4 (faces "Down into the sea")
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="The missing notes" how="Some notes are missing. Draw each one above its letter, one step down from the last, with its ladders.">
      {ladder(W.sea, 'bass', [10, 26])}
    </Part>
    <Part kind="home" title="Name the sea notes" how="Count down from Kingsland's bottom line, G, and write each letter.">
      {names(W.sea.home, 470, 'bass', false, 1, [11, 26])}
    </Part>
    <Part kind="play" title="Words in the sea" how="Draw each note above its letter, with its ladders. Then play the words with your left hand.">
      {words(LL_WORDS_SEA, 'bass', 9, 584)}
    </Part>
    <Faces/>
  </>);

  // 5 (faces "Between the lands")
  const twinRow = () => { const xs = sfXs(6, 440, true);
    return <SfRow clef="grand" width={440} notes={W.twins.map(([d, st], i) => ({ d, staff: st, x: xs[i] })).concat([{ d: W.twins[0][0], staff: 'bass', x: xs[0], color: BK.coral }])}
      items={W.twins.map(([d], i) => ({ x: xs[i], n: i + 1, ex: i === 0, ans: dName(d) }))}/>; };
  P(<>
    <WbTop step={4}/>
    <Part kind="together" title="The same key in the other land" how="1-3: draw the same key in Kingsland. 4-6: draw it in Queensland. Write the letter.">
      {twinRow()}
    </Part>
    <Part kind="home" title="Read the borrowed ladders" how="Whose land is the note in? Count out from that land, then write the letter.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:18}}>{names(W.between.tre, 232, 'treble', false, 7, [26, 38])}{names(W.between.bas, 232, 'bass', false, 11, [18, 30])}</div>
    </Part>
    <Part kind="play" title="Same key?" how="Each picture has a note in each land. Is it the same key on the piano? Circle yes or no.">
      <BkGrid cols={4} gap="8px 10px">{W.same.map(([a, b], i) => <BkCell key={i} n={i + 15}><div style={{padding:'12px 4px 3px'}}>
        <PaperStaff clef="grand" notes={[{ d: a, staff: 'treble', x: 92 }, { d: b, staff: 'bass', x: 92 }]} width={140}/>
        <div style={{display:'flex',justifyContent:'center',marginTop:3}}>{wsChoose(['yes', 'no'])}</div>
      </div></BkCell>)}</BkGrid>
    </Part>
    <Faces/>
  </>);

  // 6 (faces "Five Cs")
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="Hop from a C" how="Circle the nearest C: the turtle's Sea C, Clara's C or the bird's Sky C. Then hop a step or a skip and write the letter.">
      <BkGrid cols={4} gap="8px 10px">{W.hop.map(([d, cl], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{padding:'12px 2px 3px'}}>
        {cellStaff(cl, [{ d }], 116, cl === 'treble' ? [27, 44] : [12, 29])}
        <div style={{display:'grid',justifyItems:'center',gap:4,marginTop:3}}>{llCPick(i === 0 ? llNearC(d) : null)}{nvBox(i === 0, dName(d), 40, 30)}</div>
      </div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Read them fast" how="Hop from the nearest C and write each letter.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:18}}>{names(W.fast.tre, 232, 'treble', false, 5, [25, 45])}{names(W.fast.bas, 232, 'bass', false, 9, [11, 31])}</div>
    </Part>
    <Part kind="play" title="The secret message" how="Write each note's letter, left to right. The word tells you what the turtle likes to eat.">
      {(() => { const xs = sfXs(7, 556, true); return <SfRow clef="grand" width={556} notes={LL_MSG.notes.map(([d, st], j) => ({ d, staff: st, x: xs[j] }))} items={xs.map((x, j) => ({ x, ex: j === 0, ans: LL_MSG.word[j], w: 32 }))}/>; })()}
    </Part>
    <Faces/>
  </>);

  // 7. the check-up on paper (the Workbook's last page)
  P(<LlPaperCheck/>);
  return <>{pages}</>;
}

const llChkData = () => ({
  draw: [['treble', 42], ['bass', 16], ['treble', 26], ['treble', 39]],
  sky: [41, 44, 39, 42], sea: [15, 12, 17, 14],
  between: [['treble', 26], ['bass', 30], ['treble', 27], ['bass', 29]],
  hop: [['treble', 43], ['bass', 13], ['treble', 28], ['bass', 16]],
});
function LlPaperCheck() {
  const C = llChkData();
  const xs4 = sfXs(4, 510, true);
  const cells = (list, n0, kids) => <BkGrid cols={4} gap="6px 10px">{list.map(([cl, d], i) => <BkCell key={i} n={n0 + i}><div style={{padding:'11px 4px 2px'}}>
    <PaperStaff clef={cl} notes={[{ d, rungs: kids ? [] : undefined }]} width={kids ? 124 : 136} guides={kids ? (d > CLEFS[cl].high ? [3, 0] : [0, 3]) : undefined}/>
    {!kids && <div style={{display:'flex',justifyContent:'center',marginTop:3}}>{bkBox(34, 30)}</div>}
  </div></BkCell>)}</BkGrid>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Draw the ladders each note needs on the dotted lines. Some need none.')}
    {cells(C.draw, 1, true)}
    {bkSec('B', 'Up into the sky: name the notes.')}
    <SfRow clef="treble" width={510} notes={C.sky.map((d, i) => ({ d, x: xs4[i] }))} minSpan={[30, 45]} items={xs4.map((x, i) => ({ x, n: i + 5 }))}/>
    {bkSec('C', 'Down into the sea: name the notes.')}
    <SfRow clef="bass" width={510} notes={C.sea.map((d, i) => ({ d, x: xs4[i] }))} minSpan={[11, 26]} items={xs4.map((x, i) => ({ x, n: i + 9 }))}/>
    {bkSec('D', 'Between the lands: count out from the note\'s land, then name it.')}
    {cells(C.between, 13, false)}
    {bkSec('E', 'Hop from the nearest C: name the notes.')}
    {cells(C.hop, 17, false)}
  </div>;
}

function LedgerTeacher() {
  const W = useMemo(() => llWorkbook(), [LANG]);
  const C = llChkData();
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="ledger-lines" teacher>{content}</WbPage>);
  const yn = (a, b) => a === b ? 'yes' : 'no';
  P(<>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('ledger-lines')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Answers for every workbook page, the mistakes students make most, and a line to say when they get stuck. A ledger line is also spelled leger line (AMEB accepts both). Some books teach the ledger notes as four lists -- A C E above the treble staff, C A F below it, C E G above the bass staff, E C A below it; this book counts out of each land and reads from the five Cs instead. The lists' third notes between the lands (F three ladders under Queensland, G three ladders over Kingsland) come later. AMEB: Preliminary needs one ladder below Queensland; Grade 1 one ladder above and below both lands; Grade 2 up to three.</div>
    <TcBlock page={2} title="Clara's ladder is a ledger line" answers={<>{tcAns('TRY IT', W.neat.map(([, , f]) => f ? '✗ (' + (f === 'gap' ? 'a gap' : f === 'long' ? 'too long' : 'a lid on top') + ')' : '✓'))}{tcAns('YOUR TURN', W.draw.map(([cl, d]) => dName(d) + ': ' + llRungCount(cl, d)), 6)}{tcAns('PLAY', W.count.map(d => String(llRungCount('treble', d))), 14)}</>}
      watch="Ladders drawn as one long line, a gap between the staff and the note, a lid on a note in a space (one line too many on top), ladders further apart than the staff lines. The notes just outside the staff (G over Queensland, F under Kingsland) need no ladder."
      say="“Count the ladders out from the staff: line, space, ladder…”"/>
    <TcBlock page={3} title="Up into the sky" answers={<>{tcAns('TRY IT', W.sky.tog.map((d, i) => W.sky.given.includes(i) || i === W.sky.ex ? null : dName(d) + ' ' + llShort('treble', d)).filter(Boolean), null)}{tcAns('YOUR TURN', W.sky.home.map(dName))}{tcAns('PLAY', LL_WORDS_SKY.map(w => w.word + ': ' + w.notes.map(d => dName(d) + ' ' + llShort('treble', d)).join(', ')), 9)}</>}
      watch="Counting the ladders wrong: starting from the wrong line (start on the top line, F), or calling the space just over the staff a ladder. Sky C is on ladder 2, not ladder 3."
      say="“Line F, space G, ladder A, space B, ladder C -- Sky C.”"/>
    <TcBlock page={4} title="Down into the sea" answers={<>{tcAns('TRY IT', W.sea.tog.map((d, i) => W.sea.given.includes(i) || i === W.sea.ex ? null : dName(d) + ' ' + llShort('bass', d)).filter(Boolean), null)}{tcAns('YOUR TURN', W.sea.home.map(dName))}{tcAns('PLAY', LL_WORDS_SEA.map(w => w.word + ': ' + w.notes.map(d => dName(d) + ' ' + llShort('bass', d)).join(', ')), 9)}</>}
      watch="Reading upwards by habit: below Kingsland the letters go backwards. Sea C is on ladder 2 under Kingsland."
      say="“Line G, space F, ladder E, space D, ladder C -- Sea C.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Between the lands" answers={<>{tcAns('TRY IT', W.twins.map(([d, st]) => dName(d) + ' → ' + (st === 'treble' ? 'Kingsland ' : 'Queensland ') + llShort(st === 'treble' ? 'bass' : 'treble', d)))}{tcAns('YOUR TURN', [...W.between.tre, ...W.between.bas].map(dName), 7)}{tcAns('PLAY', W.same.map(([a, b]) => yn(a, b)), 15)}</>}
      watch="Reading a note under Queensland as a Kingsland note: it belongs to the land it hangs from, so count out from Queensland. The same key in the other land is written another way."
      say="“Whose land is it in? Count out from that land.”"/>
    <TcBlock page={6} title="Five Cs" answers={<>{tcAns('TRY IT', W.hop.map(([d]) => LL_C_WORD[llNearC(d)] + ' C → ' + dName(d)))}{tcAns('YOUR TURN', [...W.fast.tre, ...W.fast.bas].map(dName), 5)}{tcAns('PLAY', [LL_MSG.word])}</>}
      watch="Counting every ladder from the staff instead of hopping from the nearest C. Every ledger note in the book is a step or a skip from Sea C, Clara's C or Sky C."
      say="“Find the nearest C -- then a step or a skip.”"/>
    <TcBlock page={7} title="The check-up on paper (the Workbook's last page)" answers={<>
      {tcAns('A', C.draw.map(([cl, d]) => dName(d) + ': ' + llRungCount(cl, d) + (llRungCount(cl, d) === 1 ? ' ladder' : ' ladders')))}
      {tcAns('B', C.sky.map(dName), 5)}
      {tcAns('C', C.sea.map(dName), 9)}
      {tcAns('D', C.between.map(([, d]) => dName(d)), 13)}
      {tcAns('E', C.hop.map(([, d]) => dName(d)), 17)}
    </>}
      watch="Score each part on its own (4 marks, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5 · E p.6."
      say="“Count out from the land -- or hop from the nearest C.”"/>
    <div style={{fontSize:12.5,color:BK.ink,lineHeight:1.6,marginTop:6}}>
      <b style={{color:BK.muted,fontSize:10.5,letterSpacing:'0.06em'}}>LESSON TIME</b> The C hop needs only note cards. Short lessons: set the drill levels as the week's practice -- a little every day, tracked on the student page. A Preliminary student can stop after level 1.
    </div>
  </>);
  return <>{pages}</>;
}
