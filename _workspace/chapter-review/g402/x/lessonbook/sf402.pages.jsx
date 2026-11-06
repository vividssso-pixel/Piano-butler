function sfLbPages(scr = false) {
  const ch = 'staff';
  const queen = sfQueen(22, 24, 1), king = sfKing(22, 24, 1), clara = nnClara(22, 24, 1);
  const turtle = [...fsTurtle(22, 26, 0.8), ...fsWaves(2, 36, 40, 0.8, 3)], bird = [...fsBird(22, 26, 1), ...fsCloud(10, 12, 0.6)];
  // letters (and a word) under or over a row of notes, on one baseline
  const rowLabels = (items, y, wordDy) => (yOf, layer, txt) => layer === 'over' && <g style={txt}>{items.map(([x, letter, word, coral], i) => <g key={i}>
    <text x={x} y={y(yOf)} fontSize={coral ? 12 : 10.5} fontWeight="900" fill={coral ? BK.coral : BK.ink} textAnchor="middle">{letter}</text>
    {word && <text x={x} y={y(yOf) + wordDy} fontSize="8.2" fontWeight="900" fill={coral ? BK.coral : BK.muted} textAnchor="middle">{word}</text>}</g>)}</g>;

  // p1: the grand staff as two palaces -- the Queen's G, Princess Clara's middle C, the King's F
  const p1 = <SfStaff clef="grand" width={340} pad={[44, 18]} label={t('The grand staff: the Queen beside her G line in the treble clef, the King beside his F line in the bass clef, and Princess Clara on middle C between them; the bird flies high at the top right, the turtle swims low at the bottom left', '큰보표: 높은음자리표의 G 줄 옆에 여왕, 낮은음자리표의 F 줄 옆에 왕, 그 사이 가운데 도에 클라라 공주; 오른쪽 위에는 새, 왼쪽 아래에는 거북이')}
    notes={[{ d: 24, x: 128, color: PEN_C, label: t('the King\'s F', '왕의 F'), la: 'end', lx: -12, ly: 4 }, { d: 28, x: 196, color: PEN_C, label: t('middle C', '가운데 도'), la: 'end', lx: -12, ly: 4 }, { d: 32, x: 264, color: PEN_C, label: t('the Queen\'s G', '여왕의 G'), la: 'end', lx: -12, ly: 4 }]}
    icons={[SF_ICON(king, 138, 150, 0.95), SF_ICON(clara, 206, 86, 0.85), SF_ICON(queen, 274, 66, 0.95), SF_ICON(bird, 292, 14, 0.95), SF_ICON(turtle, 40, 176, 0.75)]}/>;
  // p2 (B4): the staff, lines and spaces numbered from the bottom; two magnifiers show a line note (the line runs through its
  // middle) and a space note (it fills the space and touches the lines above and below)
  const mag = (cx, cy, r, line, id) => <g>
    <defs><clipPath id={id}><circle cx={cx} cy={cy} r={r}/></clipPath></defs>
    <circle cx={cx} cy={cy} r={r} fill="#fffdf7"/>
    <g clipPath={`url(#${id})`}>{(line ? [-24, 0, 24] : [-12, 12]).map(o => <line key={o} x1={cx - r} x2={cx + r} y1={cy + o} y2={cy + o} stroke={BK.ink} strokeOpacity="0.75" strokeWidth="2.2"/>)}</g>
    <ellipse cx={cx} cy={cy} rx="17" ry="12" fill={BK.coral}/><ellipse cx={cx} cy={cy} rx="7.8" ry="6.2" transform={`rotate(-38 ${cx} ${cy})`} fill="#fff"/>
    {line && <line x1={cx - 9} x2={cx + 9} y1={cy} y2={cy} stroke={BK.ink} strokeOpacity="0.75" strokeWidth="2.2"/>}
    <circle cx={cx} cy={cy} r={r} fill="none" stroke={BK.ink} strokeWidth="1.6"/>
  </g>;
  const p2 = <SfStaff clef="none" width={320} span={[42, 278]} pad={[30, 132]} label={t('The staff, lines numbered 1 to 5 from the bottom and spaces 1 to 4; under it, two magnifiers: a line note with the line running through its middle, and a space note filling the space and touching the line above and the line below', '오선, 아래에서부터 1~5번 줄과 1~4번 칸; 그 아래 돋보기 둘: 줄이 한가운데를 지나는 줄 음표, 칸을 꽉 채워 위 줄과 아래 줄에 닿는 칸 음표')}
    notes={[{ d: 34, x: 100, color: PEN_C }, { d: 33, x: 220, color: PEN_C }]}
    extra={(yOf, layer, txt) => { if (layer !== 'over') return null; const cy = yOf(30) + 66, r = 38; return <g>
      {[[100, yOf(34)], [220, yOf(33)]].map(([x, y], i) => <g key={i}><circle cx={x} cy={y} r="11" fill="none" stroke={BK.ink} strokeWidth="1.2"/><line x1={x} x2={x} y1={y + 11} y2={cy - r} stroke={BK.ink} strokeWidth="1.2" strokeDasharray="3 3"/></g>)}
      {mag(100, cy, r, true, 'sf402m1')}{mag(220, cy, r, false, 'sf402m2')}
      <g style={txt}>
        {[30, 32, 34, 36, 38].map((d, i) => <text key={d} x="28" y={yOf(d) + 3.4} fontSize="9" fontWeight="900" fill={BK.ink} textAnchor="middle">{i + 1}</text>)}
        {[31, 33, 35, 37].map((d, i) => <text key={d} x="292" y={yOf(d) + 3.4} fontSize="9" fontWeight="900" fill={BK.coral} textAnchor="middle">{i + 1}</text>)}
        <text x="28" y={yOf(38) - 10} fontSize="8" fontWeight="800" fill={BK.ink} textAnchor="middle">{t('lines', '줄')}</text>
        <text x="292" y={yOf(38) - 10} fontSize="8" fontWeight="800" fill={BK.coral} textAnchor="middle">{t('spaces', '칸')}</text>
        <text x="100" y={cy + r + 15} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('a line note', '줄 음표')}</text>
        <text x="100" y={cy + r + 27} fontSize="8" fontWeight="700" fill={BK.ink} textAnchor="middle">{t('the line runs through it', '줄이 가운데를 지나요')}</text>
        <text x="220" y={cy + r + 15} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('a space note', '칸 음표')}</text>
        <text x="220" y={cy + r + 27} fontSize="8" fontWeight="700" fill={BK.ink} textAnchor="middle">{t('it touches both lines', '위아래 줄에 닿아요')}</text>
      </g></g>; }}/>;
  // p3: up the staff = up the piano; steps (line, space) and skips (line, line)
  const p3 = <SfStaff clef="none" width={340} pad={[46, 40]} label={t('Notes climbing the staff: steps go line, space, line, space; skips go line, line, line; the bird is up at the high end, the turtle down at the low end', '오선을 오르는 음표: 한 걸음은 줄, 칸, 줄, 칸; 건너뛰기는 줄, 줄, 줄; 높은 쪽엔 새, 낮은 쪽엔 거북이')}
    notes={[30, 31, 32, 33, 34].map((d, i) => ({ d, x: 66 + i * 22 })).concat([30, 32, 34, 36].map((d, i) => ({ d, x: 204 + i * 30, color: PEN_C })))}
    icons={[SF_ICON(bird, 300, 6, 0.85), SF_ICON(turtle, 0, 112, 0.75)]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <text x="110" y={yOf(38) - 14} fontSize="10" fontWeight="900" fill={BK.ink} textAnchor="middle">{t('steps: line, space, line...', '한 걸음: 줄, 칸, 줄...')}</text>
      <text x="249" y={yOf(38) - 14} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('skips: line, line, line', '건너뛰기: 줄, 줄, 줄')}</text>
      {[0, 1, 2].map(i => <g key={i}>{sfHop(204 + i * 30 + 3, 204 + (i + 1) * 30 - 3, yOf(32 + 2 * i) - 9, 12)}</g>)}
      <path d={`M60 ${yOf(30) + 22} L292 ${yOf(30) + 22}`} stroke={BK.coral} strokeWidth="1.8"/>{sfArrowHead(296, yOf(30) + 22, 1, BK.coral)}
      <text x="176" y={yOf(30) + 35} fontSize="9" fontWeight="800" fill={BK.ink} textAnchor="middle">{t('higher on the staff = higher on the piano, further to the right', '오선에서 위로 = 피아노에서 높이, 오른쪽으로')}</text>
    </g>}/>;
  // p4: the Queen's five -- C D E F G, from Clara up to the Queen's G; the curl wraps the second line
  const xs5 = [70, 126, 182, 238, 294];
  const p4 = <SfStaff clef="treble" width={340} pad={[50, 40]} label={t('The treble clef; its curl wraps the second line, the Queen\'s G line, in coral; five notes climb from middle C on its little ladder rung: C D E F G', '높은음자리표; 소용돌이가 감싸는 둘째 줄(여왕의 G 줄)이 산호색; 작은 사다리 발판 위의 가운데 도에서 다섯 음이 올라가요: C D E F G')}
    notes={[28, 29, 30, 31, 32].map((d, i) => ({ d, x: xs5[i], color: i === 4 || i === 0 ? PEN_C : undefined }))}
    icons={[SF_ICON(queen, 268, 10, 0.9), SF_ICON(clara, 22, 112, 0.72)]}
    extra={(yOf, layer, txt) => <g>{layer === 'under' && <line x1="36" x2="332" y1={yOf(32)} y2={yOf(32)} stroke={BK.coral} strokeOpacity="0.55" strokeWidth="3.4"/>}
      {rowLabels([[xs5[0], 'C', t('Clara', '클라라'), true], [xs5[1], 'D'], [xs5[2], 'E'], [xs5[3], 'F'], [xs5[4], 'G', t('the Queen\'s G', '여왕의 G'), true]], (yOf) => yOf(28) + 19, 12)(yOf, layer, txt)}</g>}/>;
  // p5: the King's five -- F G A B C, from the King's F up to Clara; the two dots guard the fourth line
  const p5 = <SfStaff clef="bass" width={340} pad={[56, 50]} label={t('The bass clef; its two dots guard the fourth line, the King\'s F line, in coral; five notes climb from the King\'s F to middle C on its little ladder rung: F G A B C', '낮은음자리표; 두 점이 지키는 넷째 줄(왕의 F 줄)이 산호색; 왕의 F에서 작은 사다리 발판 위의 가운데 도까지 다섯 음: F G A B C')}
    notes={[24, 25, 26, 27, 28].map((d, i) => ({ d, x: xs5[i], color: i === 0 || i === 4 ? PEN_C : undefined }))}
    icons={[SF_ICON(king, 51, 166, 0.9), SF_ICON(clara, 304, 66, 0.62)]}
    extra={(yOf, layer, txt) => <g>{layer === 'under' && <line x1="36" x2="332" y1={yOf(24)} y2={yOf(24)} stroke={BK.coral} strokeOpacity="0.55" strokeWidth="3.4"/>}
      {rowLabels([[xs5[0], 'F', t('the King\'s F', '왕의 F'), true], [xs5[1], 'G'], [xs5[2], 'A'], [xs5[3], 'B'], [xs5[4], 'C', t('Clara', '클라라'), true]], (yOf) => yOf(28) - 16, -12)(yOf, layer, txt)}</g>}/>;
  // p6: the grand staff; middle C on its own ladder rung, under the Queen's staff or over the King's -- the same key; the fold
  const p6 = <SfStaff clef="grand" width={340} pad={[26, 26]} label={t('The grand staff: middle C written on a little ladder rung just under the treble staff and just over the bass staff, the same key, with Princess Clara between; folded at middle C, the Queen\'s G lands on the King\'s F, five keys each way', '큰보표: 높은음자리표 오선 바로 아래와 낮은음자리표 오선 바로 위, 작은 사다리 발판에 쓴 가운데 도(같은 건반)와 그 사이의 클라라 공주; 가운데 도에서 접으면 여왕의 G가 왕의 F에 겹쳐요, 양쪽으로 다섯 건반씩')}
    notes={[{ d: 28, x: 104, staff: 'treble', color: PEN_C }, { d: 28, x: 104, staff: 'bass', color: PEN_C }, { d: 32, x: 236, color: PEN_C, label: t('G: 5 up', 'G: 5개 위'), la: 'start', lx: 12, ly: 3.5 }, { d: 24, x: 236, color: PEN_C, label: t('F: 5 down', 'F: 5개 아래'), la: 'start', lx: 12, ly: 3.5 }]}
    icons={[SF_ICON(clara, 124, 108, 0.8), SF_ICON(queen, 300, 50, 0.85), SF_ICON(king, 300, 140, 0.85)]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <line x1="80" x2="332" y1={(yOf(28, 'treble') + yOf(28, 'bass')) / 2} y2={(yOf(28, 'treble') + yOf(28, 'bass')) / 2} stroke={BK.coral} strokeWidth="1.4" strokeDasharray="5 4"/>
      <text x="200" y={(yOf(28, 'treble') + yOf(28, 'bass')) / 2 + 3.5} fontSize="9" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('fold here', '여기서 접어요')}</text>
      <text x="74" y={(yOf(28, 'treble') + yOf(28, 'bass')) / 2 + 3.5} fontSize="9.5" fontWeight="900" fill={BK.ink} textAnchor="end">{t('middle C', '가운데 도')}</text>
      <text x="118" y={yOf(28, 'treble') + 3} fontSize="7.5" fontWeight="800" fill={BK.muted} textAnchor="start">{t('her ladder rung', '공주의 사다리 발판')}</text>
    </g>}/>;
  // p7: landmarks -- the Queen's G, the King's F, Clara's middle C; the nine notes between, read by step or skip
  const p7 = <SfStaff clef="grand" width={340} pad={[28, 28]} label={t('The grand staff with the three landmarks in coral -- the Queen\'s G, middle C and the King\'s F -- and four black notes read from the nearest landmark: E, a skip down from G; D, a step up from middle C; B, a step down from middle C; A, a skip up from F', '큰보표의 기준 음 셋(산호색): 여왕의 G, 가운데 도, 왕의 F; 가장 가까운 기준 음에서 읽는 검은 음표 넷: G에서 건너 아래 E, 가운데 도에서 한 걸음 위 D, 한 걸음 아래 B, F에서 건너 위 A')}
    notes={[{ d: 32, x: 74, color: PEN_C, label: 'G', la: 'end', lx: -12, ly: 3.5 }, { d: 30, x: 116, label: 'E?', ly: 19 }, { d: 28, x: 190, staff: 'treble', color: PEN_C, label: t('middle C', '가운데 도'), la: 'end', lx: -15, ly: 3.5 }, { d: 29, x: 232, label: 'D?', ly: -11 },
      { d: 24, x: 74, color: PEN_C, label: 'F', la: 'end', lx: -12, ly: 3.5 }, { d: 26, x: 116, label: 'A?', ly: -11 }, { d: 28, x: 190, staff: 'bass', color: PEN_C }, { d: 27, x: 232, staff: 'bass', label: 'B?', ly: 19 }]}
    icons={[SF_ICON(queen, 290, 44, 0.8), SF_ICON(clara, 290, 108, 0.75), SF_ICON(king, 290, 160, 0.8)]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <path d={`M81 ${yOf(32) + 3} Q96 ${yOf(32) + 18} 110 ${yOf(30) + 4}`} fill="none" stroke={BK.ink} strokeWidth="1.3" strokeDasharray="3 3"/>
      <path d={`M197 ${yOf(28) - 4} Q212 ${yOf(28) - 14} 226 ${yOf(29) - 4}`} fill="none" stroke={BK.ink} strokeWidth="1.3" strokeDasharray="3 3"/>
      <path d={`M81 ${yOf(24, 'bass') - 3} Q96 ${yOf(24, 'bass') - 18} 110 ${yOf(26, 'bass') - 4}`} fill="none" stroke={BK.ink} strokeWidth="1.3" strokeDasharray="3 3"/>
      <path d={`M197 ${yOf(28, 'bass') + 4} Q212 ${yOf(28, 'bass') + 14} 226 ${yOf(27, 'bass') + 4}`} fill="none" stroke={BK.ink} strokeWidth="1.3" strokeDasharray="3 3"/>
    </g>}/>;

  const mini = (dots, extra = []) => { const s = []; for (let i = 0; i < 5; i++) s.push({ ...penLine([6, 8 + i * 6], [86, 8 + i * 6], 1.1), nw: true }); return [...s, ...dots.map(([x, y, c]) => ({ k: 'el', c: [x, y], rx: 4.4, ry: 3.1, f: c || PEN_N })), ...extra]; };
  const chkArts = {
    ls: mini([[34, 20, PEN_C], [58, 23, PEN_N]]),
    ss: mini([[20, 32], [32, 29], [44, 26]], [...nnHop(56, 76, 22, 6)].concat([{ k: 'el', c: [56, 26], rx: 4.4, ry: 3.1, f: PEN_C }, { k: 'el', c: [76, 20], rx: 4.4, ry: 3.1, f: PEN_C }])),
    queen: [...sfQueen(20, 22, 0.8), { ...penText(60, 28, 'C–G', { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    king: [...sfKing(20, 22, 0.8), { ...penText(60, 28, 'F–C', { size: 13, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    clara: [...nnClara(24, 22, 0.8), { ...penText(62, 30, 'C', { size: 18, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
  };
  const checksRows = [
    ['ls', [0, 0, 92, 40], t('I can tell a line note from a space note, and count them from the bottom', '줄 음표와 칸 음표를 구별하고, 아래에서부터 셀 수 있어요')],
    ['ss', [0, 0, 92, 40], t('I can see a step or a skip on the staff, and play it', '오선에서 한 걸음과 건너뛰기를 보고 칠 수 있어요')],
    ['queen', [0, 0, 92, 40], t('I can read the Queen\'s five: C D E F G in the treble clef', '여왕의 다섯 음 C D E F G를 읽을 수 있어요')],
    ['king', [0, 0, 92, 40], t('I can read the King\'s five: F G A B C in the bass clef', '왕의 다섯 음 F G A B C를 읽을 수 있어요')],
    ['clara', [0, 0, 92, 40], t('I can find middle C on both staves, and name notes from the landmarks', '두 오선에서 가운데 도를 찾고, 기준 음에서 읽을 수 있어요')],
  ];
  const pic = (svg, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{svg}</div></LbPic>;

  return [
    // 1. opener (also the Workbook's map)
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Reading the Staff', '오선보 읽기')}</div>
      </div></LbOnly>
      {pic(p1, 220, 560)}
      <LbSay size={17.5}>{t('Music is written on a staff: five lines and the four spaces between them, and higher on the staff means higher on the piano. Two royal palaces share it: the Queen\'s on top for the high notes, the King\'s underneath for the low ones -- and in between, on middle C, lives Princess Clara. This chapter reads the notes around her: five from Clara up to the Queen\'s G, five from Clara down to the King\'s F -- nine notes in all, Clara in the middle. The whole staff comes next.', '음악은 오선 위에 써요: 줄 다섯 개와 그 사이 칸 네 개, 그리고 오선에서 높을수록 피아노에서도 높아요. 오선에는 두 궁전이 있어요: 위에는 높은 음을 맡은 여왕의 궁전, 아래에는 낮은 음을 맡은 왕의 궁전 -- 그리고 그 사이, 가운데 도에 클라라 공주가 살아요. 이 챕터에서는 공주 둘레의 음을 읽어요: 공주에서 위로 여왕의 G까지 다섯, 아래로 왕의 F까지 다섯 -- 공주가 가운데, 모두 아홉 음. 오선 전체는 다음 챕터예요.')}</LbSay>
      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>
          {[[t('Lines and spaces', '줄과 칸'), 2], [t('Up the staff, up the piano', '오선 위로, 피아노 위로'), 3], [t('The Queen\'s five', '여왕의 다섯 음'), 4], [t('The King\'s five', '왕의 다섯 음'), 5], [t('Middle C: Princess Clara', '가운데 도: 클라라 공주'), 6], [t('Landmarks: read it fast', '기준 음: 빨리 읽기'), 7], [t('My five checks', '나의 다섯 가지 확인'), 8]].map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid #ece6d8'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><b>{'page ' + p}</b></div>)}
        </div></LbOnly>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('tell a line note from a space note', '줄 음표와 칸 음표를 구별할 수 있어요'), t('see a step or a skip on the staff, and play it', '오선에서 한 걸음과 건너뛰기를 보고 칠 수 있어요'), t('read C D E F G in the treble clef', '높은음자리표에서 C D E F G를 읽을 수 있어요'), t('read F G A B C in the bass clef', '낮은음자리표에서 F G A B C를 읽을 수 있어요'), t('find middle C on both staves', '두 오선에서 가운데 도를 찾을 수 있어요'), t('name these nine notes from a landmark', '이 아홉 음을 기준 음에서 바로 읽을 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:8,fontSize:14.5,padding:'4px 0'}}><span style={{color:BK.coral,fontWeight:900}}>✓</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. lines and spaces
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Lines and spaces', '줄과 칸')}>
      {pic(p2, 210, 600)}
      <LbSay>{LANG === 'ko' ? <>오선에는 <b>줄 다섯 개</b>와 <b>칸 네 개</b>가 있어요. <b>아래에서부터</b> 세요: 1번 줄이 가장 낮고 5번 줄이 가장 높아요; 1번 칸은 1번 줄 바로 위예요. 음표는 모두 <b>줄 위</b>에 있거나 -- 줄이 음표 한가운데를 꿰뚫어요, 꼬치처럼 -- <b>칸 안</b>에 있어요: 칸을 꽉 채워서 위아래 줄에 닿아요, 샌드위치 속처럼.</>
        : <>The staff has <b>five lines</b> and <b>four spaces</b>. Count them <b>from the bottom</b>: line 1 is the lowest, line 5 the highest; space 1 sits just above line 1. Every note lives either <b>on a line</b> -- the line runs straight through its middle, like a kebab -- or <b>in a space</b>: it fills the space and touches the line above and the line below, like a sandwich filling.</>}</LbSay>
      <LbPiano title={t('Try it', '해 봐요')} steps={LANG === 'ko' ? [
        <><LbAsk q="N1"><b>엄지 시험:</b> 음표를 엄지로 가려요. 엄지 양옆으로 줄이 한가운데에서 삐져나오면 줄 음표, 엄지 위아래로 줄이 보이면 칸 음표.</LbAsk></>,
        <><LbAsk q="N2"><b>바닥 오선:</b> 바닥에 테이프로 줄 다섯 개를 붙여요. 누가 "3번 줄!", "2번 칸!" 하면 줄 <b>위에</b> 또는 칸 <b>안에</b> 뛰어 서요.</LbAsk></>,
        <><b>손 오선:</b> 한 손을 옆으로 눕혀 손가락을 벌려요: 손가락 5개 = 줄 5개, 손가락 사이 4개 = 칸 4개. 누가 짚으면 줄인지 칸인지, 몇 번인지 말해요.</>,
      ] : [
        <><LbAsk q="N1"><b>The thumb test:</b> cover a note with your thumb. A line poking out on both sides, right at its middle? A line note. Lines peeping out above and below? A space note.</LbAsk></>,
        <><LbAsk q="N2"><b>The floor staff:</b> five lines of tape on the floor. Someone calls "line 3!" or "space 2!" -- jump <b>onto</b> the line or <b>into</b> the space.</LbAsk></>,
        <><b>The hand staff:</b> hold one hand out sideways, fingers spread: 5 fingers = 5 lines, the 4 gaps = 4 spaces. Someone touches one; say line or space, and which number.</>,
      ]}/>
      <LbRemember>{t('On a line: the line runs through it. In a space: it touches both lines.', '줄 위: 줄이 가운데를 지나요. 칸 안: 위아래 줄에 닿아요.')}</LbRemember>
    </LbPage>,

    // 3. up the staff, up the piano: steps and skips
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Up the staff, up the piano', '오선 위로, 피아노 위로')}>
      {pic(p3, 210, 680)}
      <LbSay>{LANG === 'ko' ? <>오선은 건반의 지도예요. 오선에서 <b>위</b>에 있는 음은 <b>높은 소리</b> -- 피아노에서 오른쪽, 하늘 위 새 쪽이에요. <b>아래</b>는 왼쪽, 바다 아래 거북이 쪽이에요. 줄에서 바로 위 칸으로 가면 <b>한 걸음</b>: 다음 글자, 다음 흰건반. 줄에서 다음 줄로(칸에서 다음 칸으로) 가면 <b>건너뛰기</b> -- 3챕터의 그 건너뛰기, 글자 하나를 넘어가요.</>
        : <>The staff is a map of the keys. A note <b>higher</b> on the staff sounds <b>higher</b> -- it is further to the right on the piano, up towards the bird; <b>lower</b> on the staff is further left, down towards the turtle. From a line to the very next space is a <b>step</b>: the next letter, the next white key. From a line to the next line -- or a space to the next space -- is a <b>skip</b>: the same skip as in Chapter 3, one letter jumped over.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>아무 흰건반에서 시작해 그림의 <b>한 걸음</b>들을 쳐요: 위로, 위로, 위로, 위로 -- 이웃 건반으로.</>,
        <>이번엔 <b>건너뛰기</b>: 줄, 줄, 줄 -- 건반 하나씩 넘어가요.</>,
        <><LbAsk q="N3"><b>오선 사방치기:</b> 바닥 오선 위에서 한 걸음은 바로 옆 줄이나 칸으로, 건너뛰기는 줄에서 줄로 깡충 -- 그리고 피아노에서 똑같이 쳐요.</LbAsk></>,
      ] : [
        <>Start on any white key and play the picture's <b>steps</b>: up, up, up, up -- to the next key each time.</>,
        <>Now the <b>skips</b>: line, line, line -- a key jumped over each time.</>,
        <><LbAsk q="N3"><b>Staff hopscotch:</b> on the floor staff, a step goes to the very next line or space, a skip hops line to line -- then play the same moves on the piano.</LbAsk></>,
      ]}/>
      <LbRemember>{t('Line to space: a step. Line to line: a skip.', '줄에서 칸: 한 걸음. 줄에서 줄: 건너뛰기.')}</LbRemember>
    </LbPage>,

    // 4. the Queen's five (treble clef)
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The Queen\'s five', '여왕의 다섯 음')}>
      {pic(p4, 210, 680)}
      <LbSay>{LANG === 'ko' ? <>이 꼬불꼬불한 기호가 <b>높은음자리표</b>예요. 아주 옛날에는 그냥 글자 <b>G</b>였어요. 소용돌이가 아래에서 <b>둘째 줄</b>을 감싸는데, 그 줄이 <b>여왕의 집</b>이에요: 그 줄 위의 음은 모두 <b>G</b>. 여왕은 높은 목소리로 노래하고, 보통 <b>오른손</b>이 읽어요. 클라라 공주(가운데 도)에서 여왕의 G까지는 딱 <b>다섯 음</b>: C D E F G -- 공주는 오선 아래 작은 사다리 발판 위, D는 1번 줄 바로 아래, E는 1번 줄, F는 1번 칸, G는 여왕의 줄.</>
        : <>This curly sign is the <b>treble clef</b>. Long ago it was simply a letter <b>G</b>. Its curl wraps round the <b>second line</b> from the bottom, and that line is the <b>Queen's house</b>: every note on it is <b>G</b>. The Queen sings high, and usually the <b>right hand</b> reads her staff. From Princess Clara (middle C) up to the Queen's G is exactly <b>five notes</b>: C D E F G -- Clara on her little ladder rung under the staff, D just under line 1, E on line 1, F in space 1, G on the Queen's line.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손으로 <b>가운데 도</b>에서 <b>G</b>까지 걸어 올라가요: C D E F G -- 오선의 그림을 보면서, 글자를 말하면서.</>,
        <>누가 다섯 음 중 하나를 짚으면: 여왕의 G에서 세어 내려오거나, 공주의 C에서 세어 올라가 이름을 대고 쳐요.</>,
        <><LbAsk q="N4"><b>여왕의 소용돌이 그리기:</b> 높은음자리표는 <b>G 줄에서 시작</b>해 밖으로 감아 나가요 -- 여왕의 집에서 출발! (워크북에 따라 그리는 쪽이 있어요.)</LbAsk></>,
      ] : [
        <>With your right hand, walk up from <b>middle C</b> to <b>G</b>: C D E F G -- looking at the staff picture, saying the letters.</>,
        <>Someone points to one of the five: count down from the Queen's G or up from Clara's C, name it, play it.</>,
        <><LbAsk q="N4"><b>Draw the Queen's curl:</b> a treble clef <b>starts on the G line</b> and spirals out -- it begins at the Queen's house! (The Workbook has one to trace.)</LbAsk></>,
      ]}/>
      <LbRemember>{t('The curl wraps round G: the Queen\'s line. Clara to the Queen: C D E F G.', '소용돌이는 G를 감싸요: 여왕의 줄. 공주에서 여왕까지: C D E F G.')}</LbRemember>
    </LbPage>,

    // 5. the King's five (bass clef)
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The King\'s five', '왕의 다섯 음')}>
      {pic(p5, 220, 680)}
      <LbSay>{LANG === 'ko' ? <>이 기호는 <b>낮은음자리표</b>예요. 글자 <b>F</b>에서 시작했어요. 왕의 집은 아래에서 <b>넷째 줄</b>이고, 음자리표의 <b>두 점</b>이 경비병이에요 -- 하나는 왕의 줄 바로 위, 하나는 바로 아래. 두 경비병 사이의 줄이 <b>F</b>예요. 왕은 낮은 목소리로 노래하고, 보통 <b>왼손</b>이 읽어요. 왕의 F에서 공주까지도 딱 <b>다섯 음</b>: F G A B C -- F는 왕의 줄, G는 그 위 칸, A는 맨 윗줄, B는 그 위, C는 오선 위 작은 사다리 발판의 공주.</>
        : <>This sign is the <b>bass clef</b>. It began as a letter <b>F</b>. The King's house is the <b>fourth line</b> from the bottom, and the clef's <b>two dots</b> are his guards, one just above his line and one just below. The line between the guards is <b>F</b>. The King sings low, and usually the <b>left hand</b> reads his staff. From the King's F up to Princess Clara is <b>five notes</b> too: F G A B C -- F on the King's line, G in the space above, A on the top line, B just over it, and Clara on her little ladder rung above the staff.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>왼손으로 <b>가운데 도</b>에서 <b>F</b>까지 걸어 내려가요: C B A G F -- 그다음 F에서 다시 올라와요: F G A B C.</>,
        <>누가 다섯 음 중 하나를 짚으면: 왕의 F나 공주의 C에서 세어 이름을 대고 쳐요.</>,
        <><LbAsk q="N5"><b>왕의 경비병 그리기:</b> 낮은음자리표는 <b>F 줄 위의 점</b>에서 시작해 동그랗게 내려가요 -- 그리고 F 줄 위아래에 경비병 두 점! (워크북에 따라 그리는 쪽이 있어요.)</LbAsk></>,
      ] : [
        <>With your left hand, walk down from <b>middle C</b> to <b>F</b>: C B A G F -- then back up from F: F G A B C.</>,
        <>Someone points to one of the five: count from the King's F or from Clara's C, name it, play it.</>,
        <><LbAsk q="N5"><b>Draw the King's guards:</b> a bass clef <b>starts with a dot on the F line</b> and curls down -- then the two guards, one above the F line and one below. (The Workbook has one to trace.)</LbAsk></>,
      ]}/>
      <LbRemember>{t('The two dots guard F: the King\'s line. The King to Clara: F G A B C.', '두 점은 F를 지켜요: 왕의 줄. 왕에서 공주까지: F G A B C.')}</LbRemember>
    </LbPage>,

    // 6. middle C: Princess Clara (the grand staff)
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Middle C: Princess Clara', '가운데 도: 클라라 공주')}>
      {pic(p6, 230, 680)}
      <LbSay>{LANG === 'ko' ? <>여왕의 오선을 위에, 왕의 오선을 아래에 두고 앞에서 선으로 묶으면 <b>큰보표</b>예요 -- 손마다 오선 하나씩. 두 궁전 사이, <b>가운데 도</b>에 <b>클라라 공주</b>가 살아요 -- 2챕터의 땅이에요. 공주는 <b>자기만의 작은 사다리 발판</b>에 서 있어요: 여왕의 오선 바로 아래에 쓰든 왕의 오선 바로 위에 쓰든 <b>같은 건반</b>이에요. 두 궁전은 거울처럼 마주 봐요: 여왕의 G는 공주에서 다섯 음 위, 왕의 F는 다섯 음 아래 -- 가운데 도에서 접으면 G가 F에 겹쳐요.</>
        : <>Put the Queen's staff on top and the King's underneath, joined by a line at the start: that is the <b>grand staff</b> -- one staff for each hand. Between the two palaces, on <b>middle C</b>, lives <b>Princess Clara</b> -- the ground from Chapter 2. She stands on <b>a little ladder rung of her own</b>: written just under the Queen's staff or just over the King's, it is <b>the same key</b>. And the palaces mirror each other: the Queen's G is five notes above Clara, the King's F five below -- fold the grand staff at middle C, and G lands on F.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <><b>가운데 도</b>를 쳐요: 공주의 자리, 두 손이 다 닿는 단 한 곳.</>,
        <>오른손으로 다섯 음 위의 <b>G</b>, 왼손으로 다섯 음 아래의 <b>F</b>를 쳐요 -- 거울처럼.</>,
        <><LbAsk q="N6"><b>어느 궁전?</b> 누가 공주를 위 오선 아래에 쓰거나 아래 오선 위에 써요: 어디에 있든 같은 건반 -- 매번 가운데 도를 쳐요. 그다음 <b>F, C, G</b>: 왕, 공주, 여왕.</LbAsk></>,
      ] : [
        <>Play <b>middle C</b>: Clara's place, the one key both hands can reach.</>,
        <>Play <b>G</b> five notes up with your right hand and <b>F</b> five notes down with your left -- a mirror.</>,
        <><LbAsk q="N6"><b>Which palace?</b> Someone writes Clara under the top staff or over the bottom one: wherever she is, it is the same key -- play middle C each time. Then <b>F, C, G</b>: the King, the Princess, the Queen.</LbAsk></>,
      ]}/>
      <LbRemember>{t('Clara lives between the Queen and the King -- the same key on either staff.', '클라라는 여왕과 왕 사이에 살아요 -- 어느 오선에 써도 같은 건반.')}</LbRemember>
    </LbPage>,

    // 7. landmarks: read it fast
    <LbPage key="7" no={7} chId={ch} kicker={t('Step 6', '6단계')} title={t('Landmarks: read it fast', '기준 음: 빨리 읽기')}>
      {pic(p7, 230, 680)}
      <LbSay>{LANG === 'ko' ? <>아홉 음을 매번 하나씩 세면 느려요. 대신 가장 가까운 <b>기준 음</b>을 찾아요 -- 여왕의 <b>G</b>, 공주의 <b>가운데 도</b>, 왕의 <b>F</b> -- 그리고 거기서 한 걸음이나 건너뛰기로 가요. G에서 건너 아래? <b>E</b>. 가운데 도에서 한 걸음 위? <b>D</b>. 한 걸음 아래? <b>B</b>. F에서 건너 위? <b>A</b>. 날마다 조금씩, 드릴이 계속 섞어서 내 줘요. 다음 챕터에서는 오선이 더 넓어져요.</>
        : <>Counting the nine notes one by one is slow. Instead, find the nearest <b>landmark</b> -- the Queen's <b>G</b>, Clara's <b>middle C</b> or the King's <b>F</b> -- and step or skip from there. A skip down from G? <b>E</b>. A step up from middle C? <b>D</b>. A step down? <b>B</b>. A skip up from F? <b>A</b>. A little every day: the drill keeps mixing them up for you. In the next chapter, the staff opens up.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>누가 큰보표의 음 하나를 짚으면: 가장 가까운 기준 음을 찾고, 이름을 말하고, 쳐요.</>,
        <><LbAsk q="N7"><b>깃발 게임:</b> 건반 위 G, 가운데 도, F에 작은 깃발(포스트잇)을 붙여요. 누가 오선의 음을 짚으면 가장 가까운 깃발에서 출발해 그 건반을 쳐요 -- 빨리!</LbAsk></>,
        <>기준 음에서 출발하는 세 음을 읽고, 이어서 쳐요.</>,
      ] : [
        <>Someone points to a note on the grand staff: find the nearest landmark, say the name, play it.</>,
        <><LbAsk q="N7"><b>Flag game:</b> stick little flags (sticky notes) on G, middle C and F on the keys. Someone points to a note on the staff: run from the nearest flag to its key -- fast!</LbAsk></>,
        <>Read three notes in a row from a landmark, then play them.</>,
      ]}/>
      <LbRemember>{t('Find the nearest landmark, then step or skip.', '가장 가까운 기준 음을 찾고, 한 걸음이나 건너뛰기로.')}</LbRemember>
    </LbPage>,

    // 8. my five checks + the check-up on paper
    <LbPage key="8" no={8} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('At the piano: show each one, then tick how it is going -- not yet, nearly, or got it! On paper: do the check-up below.', '피아노 앞에서: 하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요! 종이에서: 아래 점검을 풀어요.')}</LbSay>
      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_sf_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
      <LbOnly print><SfPaperCheck/></LbOnly>
    </LbPage>,
  ];
}
function StaffLessonBook() { return <>{sfLbPages(false)}</>; }
// the check-up on paper (draft), in the order of the five checks; only the nine notes from the King's F to the Queen's G
function SfPaperCheck() {
  const C = useMemo(() => withSeed('sf-chk402', () => ({
    ls: shuffle([30, 33, 36, 35]).map(d => ({ d })),
    ss: [[31, 32], [34, 32], [30, 34], [37, 36]].map(([a, b]) => ({ a, b })),
    tr: shuffle([29, 30, 31, 32]),
    ba: shuffle([25, 26, 27, 24]),
    mc: { treble: shuffle([{ d: 28 }, { d: 31 }, { d: 29 }]), bass: shuffle([{ d: 28 }, { d: 25 }, { d: 27 }]) },
  })), [LANG]);
  const cell = (n, kids) => <BkCell key={n} n={n}><div style={{padding:'5px 4px 0'}}>{kids}</div></BkCell>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column'}}>
    <LbPaperHead/>
    {bkSec('A', 'Line or space? Write L or S.')}
    <BkGrid cols={4} gap="5px 10px">{C.ls.map((it, i) => cell(i + 1, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:72}}><PaperStaff clefOn={false} notes={[{ d: it.d }]} width={90}/></div>{bkBox(28, 24)}</div>))}</BkGrid>
    {bkSec('B', 'Step or skip? Up or down? Write it.')}
    <BkGrid cols={4} gap="5px 10px">{C.ss.map((it, i) => cell(i + 5, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:72}}><PaperStaff clefOn={false} notes={[{ d: it.a }, { d: it.b }]} width={90}/></div>{bkBox(44, 24)}</div>))}</BkGrid>
    {bkSec('C', 'The Queen\'s five: name the notes.')}
    <BkGrid cols={4} gap="5px 10px">{C.tr.map((d, i) => cell(i + 9, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:84}}><PaperStaff clef="treble" notes={[{ d }]} width={110}/></div>{bkBox(28, 24)}</div>))}</BkGrid>
    {bkSec('D', 'The King\'s five: name the notes.')}
    <BkGrid cols={4} gap="5px 10px">{C.ba.map((d, i) => cell(i + 13, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:84}}><PaperStaff clef="bass" notes={[{ d }]} width={110}/></div>{bkBox(28, 24)}</div>))}</BkGrid>
    {bkSec('E', 'Circle every middle C.')}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10}}>{['treble', 'bass'].map(cl => <div key={cl} style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 10px'}}><div style={{maxWidth:200}}><PaperStaff clef={cl} notes={C.mc[cl]} width={220}/></div></div>)}</div>
  </div>;
}
