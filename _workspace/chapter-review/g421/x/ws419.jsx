// ─── Phase 419: chapter 5 (The Whole Staff) Lesson Book, DRAFT v1 for Sohyun's review ───
// Built on her decisions: d2 (Queensland = the treble staff, Kingsland = the bass staff), the rhymes with an owner and
// 'crown check first' (her guide Q1: children mix up the four sentences and do not look at the clef first), w4 (the fold
// at middle C, with the three Cs), landmarks moved here from chapter 4 ('랜드마크는 다음 챕터에서'), and the Book rules.
// Ledger lines beyond Clara's rung wait for chapter 6. LbAsk marks (?draft=1) are the B questions of the review pack.

// the King's dragon (flies along his lines) and one of his cows (eats the grass in his spaces) -- pen characters
function wsDragon(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push(penCurve([['M', P(-8, 2)], ['Q', P(-16, 6), P(-19, -2)]], 2.2, PEN_N));                                     // tail
  s.push({ k: 'pa', seg: [['M', P(-19, -2)], ['L', P(-22.5, -4.6)], ['L', P(-18, -5.8)], ['Z']], f: PEN_C, s: PEN_N, w: 1 });   // tail tip
  s.push({ k: 'el', c: P(0, 0), rx: 9.6 * k, ry: 6 * k, f: '#e8f1e6', s: PEN_N, w: 1.8 });                          // body
  [[-5, -5.2], [-1, -6], [3, -5.6]].forEach(([a, b]) => s.push({ k: 'pa', seg: [['M', P(a - 1.6, b + 0.8)], ['L', P(a, b - 2.6)], ['L', P(a + 1.6, b + 0.8)], ['Z']], f: PEN_C, s: PEN_N, w: 0.8 }));   // back spikes
  s.push({ k: 'pa', seg: [['M', P(-3, -4)], ['L', P(-8, -17)], ['L', P(-1, -12)], ['L', P(2, -18)], ['L', P(5, -5)], ['Z']], f: PEN_C, s: PEN_N, w: 1.3 });   // wing
  s.push(penLine(P(-4, 5.2), P(-5, 8.6), 1.6), penLine(P(4, 5.2), P(5, 8.6), 1.6));                                   // legs
  s.push({ k: 'el', c: P(11.5, -5.5), rx: 5.4 * k, ry: 4.6 * k, f: '#e8f1e6', s: PEN_N, w: 1.8 });                   // head
  s.push({ k: 'el', c: P(16, -4.2), rx: 2.8 * k, ry: 2.2 * k, f: '#e8f1e6', s: PEN_N, w: 1.3 });                     // snout
  s.push({ k: 'el', c: P(12, -6.8), rx: 0.95 * k, ry: 1.05 * k, f: PEN_N });                                           // eye
  s.push(penLine(P(9.6, -9.4), P(8.4, -12.6), 1.4), penLine(P(12.6, -9.8), P(13.4, -13), 1.4));                      // horns
  s.push({ k: 'el', c: P(17.4, -4.6), rx: 0.5 * k, ry: 0.5 * k, f: PEN_N });                                           // nostril
  return s.map(e => ({ ...e, ch: true }));
}
function wsCow(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push(penCurve([['M', P(-3.4, -6.4)], ['Q', P(-5, -10.6), P(-8.4, -11)]], 1.4, PEN_N), penCurve([['M', P(3.4, -6.4)], ['Q', P(5, -10.6), P(8.4, -11)]], 1.4, PEN_N));   // horns
  s.push({ k: 'pa', seg: [['M', P(-6, -4.4)], ['Q', P(-11.6, -6), P(-11, -2.6)], ['Q', P(-8.4, -1.4), P(-5.6, -2)], ['Z']], f: PEN_P, s: PEN_N, w: 1.2 });   // ears
  s.push({ k: 'pa', seg: [['M', P(6, -4.4)], ['Q', P(11.6, -6), P(11, -2.6)], ['Q', P(8.4, -1.4), P(5.6, -2)], ['Z']], f: PEN_P, s: PEN_N, w: 1.2 });
  s.push({ k: 'el', c: P(0, 0), rx: 6.6 * k, ry: 8 * k, f: PEN_P, s: PEN_N, w: 1.8 });                                // head
  s.push({ k: 'pa', seg: [['M', P(-2.6, -7.4)], ['Q', P(1.6, -9), P(3.6, -5.6)], ['Q', P(2, -2.4), P(-1, -3.4)], ['Q', P(-3.6, -4.6), P(-2.6, -7.4)], ['Z']], f: PEN_N });   // patch
  s.push({ k: 'el', c: P(-2.6, -0.6), rx: 0.9 * k, ry: 1 * k, f: PEN_N }, { k: 'el', c: P(2.6, -0.6), rx: 0.9 * k, ry: 1 * k, f: PEN_N });   // eyes
  s.push({ k: 'el', c: P(0, 5), rx: 5.2 * k, ry: 3.4 * k, f: '#fbe9e2', s: PEN_N, w: 1.3 });                          // muzzle
  s.push({ k: 'el', c: P(-1.8, 5), rx: 0.7 * k, ry: 0.9 * k, f: PEN_N }, { k: 'el', c: P(1.8, 5), rx: 0.7 * k, ry: 0.9 * k, f: PEN_N });   // nostrils
  return s.map(e => ({ ...e, ch: true }));
}

function wsLbPages(scr = false) {
  const ch = 'whole-staff';
  const queen = sfQueen(22, 24, 1), king = sfKing(22, 24, 1), clara = sfClara(22, 24, 1);
  const A = (q, kids) => <LbAsk q={q}>{kids}</LbAsk>;
  const pic = (svg, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{svg}</div></LbPic>;
  const stack = (items, h) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:620,margin:'0 auto'}}>{items}</div></LbPic>;
  const under = (xs, letters, words, y, coral) => (yOf, layer, txt) => layer === 'over' && <g style={txt}>{xs.map((x, i) => <g key={i}>
    <text x={x} y={y(yOf)} fontSize="12" fontWeight="900" fill={coral ? BK.coral : BK.ink} textAnchor="middle">{letters[i]}</text>
    {words && <text x={x} y={y(yOf) + 12} fontSize="8.6" fontWeight="900" fill={BK.muted} textAnchor="middle">{words[i]}</text>}</g>)}</g>;
  const landName = (name, d, st, x = 172) => (yOf, layer, txt) => layer === 'under' && <text x={x} y={yOf(d, st) + 7} fontSize="21" fontWeight="900" fill={BK.coral} fillOpacity="0.24" textAnchor="middle" letterSpacing="3" style={{fontFamily:LB_SERIF}}>{name}</text>;
  const both = (...fs) => (yOf, layer, txt) => <g>{fs.map((f, i) => <g key={i}>{f(yOf, layer, txt)}</g>)}</g>;

  // p1: two lands on one map -- Queensland (the Queen's staff) over Kingsland (the King's); the family stands at the end
  const p1 = <SfStaff clef="grand" width={360} span={[4, 288]} pad={[22, 22]} label={t('The grand staff as a map of two lands: QUEENSLAND is the top staff, with the Queen beside it; KINGSLAND is the bottom staff, with the King beside it; Princess Clara stands between them', '큰보표는 두 나라의 지도: 위 오선은 퀸즈랜드, 옆에 여왕; 아래 오선은 킹스랜드, 옆에 왕; 그 사이에 클라라 공주')}
    icons={[SF_ICON(queen, 304, 46, 1), SF_ICON(clara, 308, 108, 0.82), SF_ICON(king, 304, 148, 1)]}
    extra={both(landName('QUEENSLAND', 34, 'treble', 160), landName('KINGSLAND', 22, 'bass', 160))}/>;

  // p2: crown check first -- the same line in each land, two names
  const crown = (clef, d, head, where) => { const L = dName(d), who = clef === 'treble' ? queen : king;
    return <SfStaff clef={clef} width={170} span={[4, 166]} pad={[head ? 58 : 20, 30]} label={clef === 'treble' ? t('In Queensland (treble clef) the note on line 2 is G', '퀸즈랜드(높은음자리표)에서 2번 줄 음표는 G') : t('In Kingsland (bass clef) the note on line 2 is B', '킹스랜드(낮은음자리표)에서 2번 줄 음표는 B')}
      notes={[{ d, x: 108, color: PEN_C }]} icons={head ? [SF_ICON(who, 6, dY(CLEFS[clef].high) - 56, 0.95)] : []}
      extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
        {head && <text x="62" y={yOf(CLEFS[clef].high) - 30} fontSize="11" fontWeight="900" fill={BK.ink}>{clef === 'treble' ? t('Queensland', '퀸즈랜드') : t('Kingsland', '킹스랜드')}</text>}
        <text x="128" y={yOf(d) + 5} fontSize="16" fontWeight="900" fill={BK.coral}>{L}</text>
        <text x="86" y={yOf(CLEFS[clef].low) + 22} fontSize="9" fontWeight="800" fill={BK.muted} textAnchor="middle">{where}</text>
      </g>}/>; };
  const p2 = <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'10px 22px',alignItems:'end'}}>
    {crown('treble', 32, true, t('line 2', '2번 줄'))}{crown('bass', 20, true, t('line 2', '2번 줄'))}
    {crown('treble', 31, false, t('space 1', '1번 칸'))}{crown('bass', 19, false, t('space 1', '1번 칸'))}</div>;

  // p3: Queensland -- the lines (Every Good Boy Deserves Fun) and the Queen's FACE in the spaces
  const xL = [92, 146, 200, 254, 308], xS = [112, 168, 224, 280];
  const p3a = <SfStaff clef="treble" width={340} pad={[18, 34]} label={t('Queensland\'s five lines from the bottom: E G B D F -- Every Good Boy Deserves Fun', '퀸즈랜드의 다섯 줄, 아래에서부터: E G B D F -- Every Good Boy Deserves Fun')}
    notes={[30, 32, 34, 36, 38].map((d, i) => ({ d, x: xL[i] }))}
    extra={under(xL, ['E', 'G', 'B', 'D', 'F'], ['Every', 'Good', 'Boy', 'Deserves', 'Fun'], (yOf) => yOf(30) + 20)}/>;
  const p3b = <SfStaff clef="treble" width={340} pad={[18, 30]} label={t('Queensland\'s four spaces from the bottom: F A C E -- the Queen\'s FACE, with the Queen beside them', '퀸즈랜드의 네 칸, 아래에서부터: F A C E -- 여왕의 얼굴(FACE), 옆에 여왕')}
    notes={[31, 33, 35, 37].map((d, i) => ({ d, x: xS[i] - 20, color: PEN_C }))} span={[4, 284]} icons={[SF_ICON(queen, 290, 42, 1.05)]}
    extra={under(xS.map(x => x - 20), ['F', 'A', 'C', 'E'], null, (yOf) => yOf(30) + 20, true)}/>;

  // p4: Kingsland -- the King's Great Big Dragon Flies Away on the lines, All Cows Eat Grass in the spaces
  const dragon = wsDragon(24, 26, 1), cow = wsCow(22, 22, 1.25);
  const p4a = <SfStaff clef="bass" width={340} pad={[62, 34]} span={[4, 284]} label={t('Kingsland\'s five lines from the bottom: G B D F A -- Great Big Dragon Flies Away, with the King\'s dragon flying above', '킹스랜드의 다섯 줄, 아래에서부터: G B D F A -- Great Big Dragon Flies Away, 위로 왕의 용이 날아가요')}
    notes={[18, 20, 22, 24, 26].map((d, i) => ({ d, x: xL[i] - 12 }))} icons={[SF_ICON(dragon, 282, 60, 1.2)]}
    extra={under(xL.map(x => x - 12), ['G', 'B', 'D', 'F', 'A'], ['Great', 'Big', 'Dragon', 'Flies', 'Away'], (yOf) => yOf(18) + 20)}/>;
  const p4b = <SfStaff clef="bass" width={340} pad={[18, 34]} span={[4, 284]} label={t('Kingsland\'s four spaces from the bottom: A C E G -- All Cows Eat Grass, with one of the King\'s cows beside them', '킹스랜드의 네 칸, 아래에서부터: A C E G -- All Cows Eat Grass, 옆에 왕의 소')}
    notes={[19, 21, 23, 25].map((d, i) => ({ d, x: xS[i] - 20, color: PEN_C }))} icons={[SF_ICON(cow, 290, 106, 1.05)]}
    extra={under(xS.map(x => x - 20), ['A', 'C', 'E', 'G'], ['All', 'Cows', 'Eat', 'Grass'], (yOf) => yOf(18) + 20, true)}/>;

  // p5 (w4): fold the grand staff at Clara's rung -- the Queen's G meets the King's F, the two space Cs meet, Clara meets Clara
  const p5 = <SfStaff clef="grand" width={360} span={[4, 300]} pad={[24, 24]} label={t('The grand staff with a dashed fold line between the staves, at Clara\'s rung: folded, the Queen\'s G lands on the King\'s F, the C in Queensland\'s third space lands on the C in Kingsland\'s second space, and middle C lands on middle C', '오선 사이, 클라라의 발판 자리에 접는 점선: 접으면 여왕의 G가 왕의 F에, 퀸즈랜드 셋째 칸의 C가 킹스랜드 둘째 칸의 C에, 가운데 도가 가운데 도에 겹쳐요')}
    notes={[{ d: 28, x: 92, staff: 'treble', color: PEN_C }, { d: 28, x: 92, staff: 'bass', color: PEN_C }, { d: 32, x: 168, color: PEN_C }, { d: 24, x: 168, staff: 'bass', color: PEN_C }, { d: 35, x: 244, color: PEN_C }, { d: 21, x: 244, staff: 'bass', color: PEN_C }]}
    icons={[SF_ICON(clara, 304, 110, 0.7)]}
    extra={(yOf, layer, txt) => { const mid = (yOf(30, 'treble') + yOf(26, 'bass')) / 2;
      return layer === 'under' ? <line x1="4" x2="300" y1={mid} y2={mid} stroke={BK.coral} strokeWidth="1.6" strokeDasharray="6 5"/>
      : <g style={txt}>
        {[[92, 28, 28, ''], [168, 32, 24, ''], [244, 35, 21, '']].map(([x, a, b], i) => <path key={i} d={`M${x + 12} ${yOf(a, 'treble')} Q${x + 34} ${mid} ${x + 12} ${yOf(b, 'bass')}`} fill="none" stroke={BK.ink} strokeWidth="1.2" strokeDasharray="3 3"/>)}
        <text x="104" y={yOf(28, 'treble') - 9} fontSize="10" fontWeight="900" fill={BK.coral}>C</text>
        <text x="180" y={yOf(32, 'treble') - 9} fontSize="10" fontWeight="900" fill={BK.coral}>{t('G', 'G')}</text>
        <text x="180" y={yOf(24, 'bass') + 16} fontSize="10" fontWeight="900" fill={BK.coral}>F</text>
        <text x="256" y={yOf(35, 'treble') - 9} fontSize="10" fontWeight="900" fill={BK.coral}>C</text>
        <text x="256" y={yOf(21, 'bass') + 16} fontSize="10" fontWeight="900" fill={BK.coral}>C</text>
        <text x="300" y={mid - 6} fontSize="9" fontWeight="900" fill={BK.coral} textAnchor="end">{t('fold here', '여기서 접어요')}</text>
      </g>; }}/>;

  // p6: five landmarks -- and read from the nearest one, a step or a skip away
  const LM = [[21, 'bass', 'C', t('Kingsland C', '킹스랜드 C')], [24, 'bass', 'F', t('the King\'s F', '왕의 F')], [28, 'treble', 'C', t('Clara\'s C', '클라라의 C')], [32, 'treble', 'G', t('the Queen\'s G', '여왕의 G')], [35, 'treble', 'C', t('Queensland C', '퀸즈랜드 C')]];
  const xM = [64, 124, 184, 244, 304];
  const p6a = <SfStaff clef="grand" width={360} pad={[24, 44]} label={t('The five landmarks from low to high: Kingsland C in the bass staff\'s second space, the King\'s F on its fourth line, Clara\'s middle C, the Queen\'s G on the treble staff\'s second line, Queensland C in its third space', '낮은 곳부터 다섯 랜드마크: 낮은음자리표 둘째 칸의 킹스랜드 C, 넷째 줄의 왕의 F, 클라라의 가운데 도, 높은음자리표 둘째 줄의 여왕의 G, 셋째 칸의 퀸즈랜드 C')}
    notes={LM.map(([d, st], i) => ({ d, staff: st, x: xM[i], color: PEN_C }))}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>{LM.map(([d, st, L, name], i) => <g key={i}>
      <text x={xM[i]} y={st === 'treble' ? yOf(38, 'treble') - 12 : yOf(18, 'bass') + 18} fontSize="11" fontWeight="900" fill={BK.coral} textAnchor="middle">{L}</text>
      <text x={xM[i]} y={st === 'treble' ? yOf(38, 'treble') - 2 : yOf(18, 'bass') + 28} fontSize="7.6" fontWeight="900" fill={BK.muted} textAnchor="middle">{name}</text></g>)}</g>}/>;
  const hop = (clef, from, to, txt0) => <SfStaff clef={clef} width={180} pad={[20, 30]} label={txt0}
    notes={[{ d: from, x: 90, color: PEN_C }, { d: to, x: 140 }]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>{sfHop(96, 134, Math.min(yOf(from), yOf(to)) - 8, 10)}<text x="115" y={yOf(CLEFS[clef].low) + 24} fontSize="9" fontWeight="900" fill={BK.ink} textAnchor="middle">{txt0}</text></g>}/>;
  const p6b = <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16}}>{hop('treble', 32, 33, t('G, a step up: A', 'G에서 한 걸음 위: A'))}{hop('bass', 24, 22, t('F, a skip down: D', 'F에서 건너뛰어 아래: D'))}</div>;

  const mini = (dots, extra = []) => { const s = []; for (let i = 0; i < 5; i++) s.push({ ...penLine([6, 8 + i * 6], [86, 8 + i * 6], 1.1), nw: true }); return [...s, ...dots.map(([x, y, c]) => ({ k: 'el', c: [x, y], rx: 4.4, ry: 3.1, f: c || PEN_N })), ...extra]; };
  const chkArts = {
    crown: [...sfQueen(18, 22, 0.75), ...sfKing(52, 22, 0.75), { ...penText(80, 30, '?', { size: 16, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    queens: [...sfQueen(18, 22, 0.75), { ...penText(58, 28, 'FACE', { size: 11, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    kings: [...wsCow(18, 22, 0.9), { ...penText(58, 28, 'ACEG', { size: 11, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    fold: mini([[30, 14, PEN_C], [30, 26, PEN_C]], [{ ...penLine([6, 20], [86, 20], 1.6, PEN_C), nw: true }]),
    marks: mini([[22, 26, PEN_C], [46, 20, PEN_C], [70, 14, PEN_C]]),
  };
  const checksRows = [
    ['crown', [0, 0, 92, 40], t('Crown check first: I say whose land it is before I name a note', '왕관 확인 먼저: 음 이름을 말하기 전에 어느 나라인지 말해요')],
    ['queens', [0, 0, 92, 40], t('I can read every line and space in Queensland', '퀸즈랜드의 모든 줄과 칸을 읽을 수 있어요')],
    ['kings', [0, 0, 92, 40], t('I can read every line and space in Kingsland', '킹스랜드의 모든 줄과 칸을 읽을 수 있어요')],
    ['fold', [0, 0, 92, 40], t('I can fold the staff in my head: G meets F, C meets C', '머릿속으로 오선을 접을 수 있어요: G는 F와, C는 C와 만나요')],
    ['marks', [0, 0, 92, 40], t('I can read any note fast from its nearest landmark', '어떤 음이든 가장 가까운 랜드마크에서 빨리 읽을 수 있어요')],
  ];

  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('The Whole Staff', '오선 전체 읽기')}</div>
      </div></LbOnly>
      {pic(p1, 230, 620)}
      <LbSay size={17.5}>{t('The staff is a map of two lands. The top staff is Queensland, the Queen\'s land; the bottom staff is Kingsland, the King\'s. Chapter 4 read the nine notes round Princess Clara. Now you can read every line and space in both lands.', '오선은 두 나라의 지도예요. 위 오선은 여왕의 나라 퀸즈랜드, 아래 오선은 왕의 나라 킹스랜드예요. 4챕터에서는 클라라 공주 둘레의 아홉 음을 읽었어요. 이제 두 나라의 모든 줄과 칸을 읽어요.')}</LbSay>
      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>
          {[[t('Crown check first', '왕관 확인 먼저'), 2], [t('Queensland', '퀸즈랜드'), 3], [t('Kingsland', '킹스랜드'), 4], [t('Fold at Clara\'s rung', '클라라의 발판에서 접기'), 5], [t('Five landmarks', '다섯 랜드마크'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid #ece6d8'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('check the crown before you read', '읽기 전에 왕관부터 확인할 수 있어요'), t('read every line and space in Queensland', '퀸즈랜드의 모든 줄과 칸을 읽을 수 있어요'), t('read every line and space in Kingsland', '킹스랜드의 모든 줄과 칸을 읽을 수 있어요'), t('find the partner note across the fold', '접는 선 건너편의 짝 음을 찾을 수 있어요'), t('read fast from five landmarks', '다섯 랜드마크에서 빨리 읽을 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid #ece6d8'}}>{bkTick(15)}{x}</div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. crown check first
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Crown check first', '왕관 확인 먼저')}>
      {pic(p2, 220, 560)}
      <LbSay>{LANG === 'ko' ? <>두 나라는 줄과 칸이 똑같이 생겼지만, 이름은 달라요. <b>2번 줄</b>은 퀸즈랜드에서는 <b>G</b>, 킹스랜드에서는 <b>B</b>; <b>1번 칸</b>은 <b>F</b>와 <b>A</b>예요. 그래서 음을 읽기 전에 늘 줄 맨 앞의 <b>왕관</b> -- 음자리표 -- 부터 봐요: 여왕의 소용돌이면 퀸즈랜드, 왕의 두 점이면 킹스랜드.</>
        : <>The two lands have the same lines and spaces, but different names. <b>Line 2</b> is <b>G</b> in Queensland and <b>B</b> in Kingsland; <b>space 1</b> is <b>F</b> in one and <b>A</b> in the other. So before you read any note, look at the <b>crown</b> at the start of the line -- the clef: the Queen's curl means Queensland, the King's two dots mean Kingsland.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <><b>왕관 확인 놀이:</b> 선생님이 음표 카드를 보여 주면, 이름보다 먼저 "퀸즈랜드!" 또는 "킹스랜드!"를 외쳐요. 그다음에 이름을 말하고 쳐요.</>,
        <>같은 자리, 다른 이름: 2번 줄을 오른손으로 G, 왼손으로 B -- 두 나라에서 한 번씩 쳐요.</>,
      ] : [
        <><b>Crown check game:</b> your teacher shows a note card -- call out "Queensland!" or "Kingsland!" before anything else. Then name the note and play it.</>,
        <>Same place, two names: play line 2 in both lands -- G with the right hand, B with the left.</>,
      ]}/>
      <LbRemember>{t('Crown check first: whose land is it?', '왕관 확인 먼저: 어느 나라예요?')}</LbRemember>
    </LbPage>,

    // 3. Queensland
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Queensland', '퀸즈랜드')}>
      {stack([<div key="a">{p3a}</div>, <div key="b">{p3b}</div>], 300)}
      <LbSay>{LANG === 'ko' ? <>여왕의 나라에는 문장이 두 개 있어요. 다섯 <b>줄</b>은 아래에서부터 <b>E G B D F</b> -- 여왕이 좋아하는 말 <b>{A('B1', 'Every Good Boy Deserves Fun')}</b>. 네 <b>칸</b>은 <b>F A C E</b> -- 여왕의 <b>얼굴(FACE)</b>이 칸 속에 숨어 있어요. 줄에서 줄은 건너뛰기라서, 줄 글자도 칸 글자도 하나씩 건너뛰며 가요.</>
        : <>The Queen's land has two sayings. Her five <b>lines</b>, from the bottom, are <b>E G B D F</b> -- her favourite saying, <b>{A('B1', 'Every Good Boy Deserves Fun')}</b>. Her four <b>spaces</b> are <b>F A C E</b>: the Queen's <b>FACE</b> is hiding in her spaces. Line to line is a skip, so both sayings skip a letter each time.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손으로 줄 음을 건너뛰며 올라가요: <b>E G B D F</b> -- 문장을 말하면서.</>,
        <>이번엔 칸 음: <b>F A C E</b> -- "여왕의 얼굴!"</>,
        <>{A('B3', <>꼭대기 줄 바로 위는 <b>G</b>, 맨 아래 줄 바로 아래는 4챕터의 <b>D</b>예요.</>)}</>,
      ] : [
        <>With your right hand, skip up the lines: <b>E G B D F</b> -- saying the words as you go.</>,
        <>Now the spaces: <b>F A C E</b> -- "the Queen's FACE!"</>,
        <>{A('B3', <>Just over the top line sits <b>G</b>; just under the bottom line is Chapter 4's <b>D</b>.</>)}</>,
      ]}/>
      <LbRemember>{t('Queensland: Every Good Boy Deserves Fun on the lines, the Queen\'s FACE in the spaces.', '퀸즈랜드: 줄에는 Every Good Boy Deserves Fun, 칸에는 여왕의 FACE.')}</LbRemember>
    </LbPage>,

    // 4. Kingsland
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Kingsland', '킹스랜드')}>
      {stack([<div key="a">{p4a}</div>, <div key="b">{p4b}</div>], 300)}
      <LbSay>{LANG === 'ko' ? <>왕의 나라에도 문장이 두 개 있어요. 다섯 <b>줄</b>은 <b>G B D F A</b> -- 왕의 용이 줄을 따라 날아가요: <b>Great Big Dragon Flies Away</b>. 네 <b>칸</b>은 <b>A C E G</b> -- 왕의 소들이 칸의 풀밭에서 풀을 먹어요: <b>All Cows Eat Grass</b>. 여왕의 문장은 여왕의 나라에서만, 왕의 문장은 왕의 나라에서만 써요.</>
        : <>The King's land has two sayings too. His five <b>lines</b> are <b>G B D F A</b> -- the King's dragon flies along them: <b>Great Big Dragon Flies Away</b>. His four <b>spaces</b> are <b>A C E G</b> -- his cows graze in the green spaces: <b>All Cows Eat Grass</b>. The Queen's sayings only work in her land, the King's only in his.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>왼손으로 줄 음을 건너뛰며 올라가요: <b>G B D F A</b> -- "용이 날아가요!"</>,
        <>이번엔 칸 음: <b>A C E G</b> -- "소들이 풀을 먹어요."</>,
        <>{A('B3', <>꼭대기 줄 바로 위는 4챕터의 <b>B</b>, 맨 아래 줄 바로 아래는 <b>F</b>예요.</>)}</>,
      ] : [
        <>With your left hand, skip up the lines: <b>G B D F A</b> -- "the dragon flies away!"</>,
        <>Now the spaces: <b>A C E G</b> -- "all cows eat grass".</>,
        <>{A('B3', <>Just over the top line is Chapter 4's <b>B</b>; just under the bottom line sits <b>F</b>.</>)}</>,
      ]}/>
      <LbRemember>{t('Kingsland: the King\'s dragon flies on the lines, his cows eat grass in the spaces.', '킹스랜드: 왕의 용은 줄 위를 날고, 소들은 칸에서 풀을 먹어요.')}</LbRemember>
    </LbPage>,

    // 5. fold at Clara's rung (w4)
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Fold at Clara\'s rung', '클라라의 발판에서 접기')}>
      {pic(p5, 250, 640)}
      <LbSay>{LANG === 'ko' ? <>큰보표를 두 오선 사이, <b>클라라의 발판</b> 자리에서 반으로 접어 봐요. 줄은 줄에, 칸은 칸에 딱 겹쳐요. <b>여왕의 G</b>는 <b>왕의 F</b>에 닿고 -- 공주에서 위로 다섯, 아래로 다섯 -- 퀸즈랜드 칸의 <b>C</b>는 킹스랜드 칸의 <b>C</b>에 닿아요. 공주는 공주끼리. 이렇게 <b>C가 세 개</b>: 위에 하나, 가운데 클라라, 아래에 하나.</>
        : <>Fold the grand staff in half between the staves, at <b>Clara's rung</b>. Lines land on lines, spaces on spaces. <b>The Queen's G</b> lands on <b>the King's F</b> -- five up from Clara, five down -- and the <b>C</b> in Queensland's spaces lands on the <b>C</b> in Kingsland's. Clara lands on Clara. That makes <b>three Cs</b>: one up, Clara in the middle, one down.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>{A('B5', <><b>거울 걷기:</b> 두 엄지를 가운데 도에 같이 올려요. 오른손은 C D E F G 위로, 왼손은 C B A G F 아래로 -- 같은 손가락 번호로, 동시에. 마지막 음 G와 F가 접으면 만나는 짝이에요.</>)}</>,
        <><b>세 개의 C:</b> 왼손으로 킹스랜드 C, 두 손 엄지로 클라라의 C, 오른손으로 퀸즈랜드 C -- 낮은 데서 높은 데로.</>,
      ] : [
        <>{A('B5', <><b>The mirror walk:</b> both thumbs on middle C. The right hand walks up C D E F G while the left walks down C B A G F -- the same finger numbers, at the same time. The last two, G and F, are the partners that meet in the fold.</>)}</>,
        <><b>Three Cs:</b> play Kingsland C with the left hand, Clara's C with both thumbs, Queensland C with the right -- low to high.</>,
      ]}/>
      <LbRemember>{t('Fold at Clara: G meets F, C meets C.', '클라라에서 접으면: G는 F와, C는 C와 만나요.')}</LbRemember>
    </LbPage>,

    // 6. five landmarks: read fast
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Five landmarks', '다섯 랜드마크')}>
      {stack([<div key="a">{p6a}</div>, <div key="b">{p6b}</div>], 300)}
      <LbSay>{LANG === 'ko' ? <>빨리 읽는 사람은 매번 문장을 처음부터 외우지 않아요. 가장 가까운 <b>랜드마크</b>에서 한 걸음이나 건너뛰기로 가요. 다섯 랜드마크: <b>{A('B2', '킹스랜드 C')}</b>, <b>왕의 F</b>, <b>클라라의 C</b>, <b>여왕의 G</b>, <b>{A('B2', '퀸즈랜드 C')}</b> -- 앞의 쪽에서 접어서 만났던 바로 그 음들이에요.</>
        : <>Fast readers don't say the whole saying every time. They jump from the nearest <b>landmark</b>, a step or a skip away. The five landmarks: <b>{A('B2', 'Kingsland C')}</b>, <b>the King's F</b>, <b>Clara's C</b>, <b>the Queen's G</b> and <b>{A('B2', 'Queensland C')}</b> -- the very notes that met in the fold.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>다섯 랜드마크를 낮은 데서 높은 데로 쳐요: C, F, C, G, C -- 이름을 말하면서.</>,
        <><b>랜드마크 뛰기:</b> 선생님이 음표 하나를 짚으면: 왕관 확인 → 가장 가까운 랜드마크 → 한 걸음 또는 건너뛰기 → 이름 → 쳐요.</>,
      ] : [
        <>Play the five landmarks from low to high: C, F, C, G, C -- naming each one.</>,
        <><b>Landmark hop:</b> your teacher points to a note: crown check → nearest landmark → a step or a skip → name it → play it.</>,
      ]}/>
      <LbRemember>{t('Find the nearest landmark, then step or skip.', '가장 가까운 랜드마크를 찾고, 한 걸음 또는 건너뛰기.')}</LbRemember>
    </LbPage>,

    // 7. my five checks
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, then tick how it is going -- not yet, nearly, or got it! The check-up on paper is in the Workbook.', '피아노 앞에서 하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요! 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_ws_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
    </LbPage>,
  ];
}
function WholeStaffLessonBook() { return <>{wsLbPages(false)}</>; }
