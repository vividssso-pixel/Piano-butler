// ─── Chapter 4: Reading the Staff (chapter 'staff') -- Lesson Book DRAFT (Phase 401) ───
// The chapter teaches the concept only (Phase 399: no songs in a chapter). Built on Sohyun's own clef story (Phase 101c):
// the treble clef began as a G and its curl wraps the Queen's line (G above middle C); the bass clef began as an F and its
// two dots are the King's guards around his line (F below middle C); the two palaces mirror each other round middle C.
// New in this draft (B questions): Princess Clara lives on middle C (chapter 3's Clara at C; middle C is the ground from
// chapter 2), the staff is shown as shapes before names (lines and spaces, steps and skips), and landmarks come before rhymes.
// Ledger lines beyond middle C's own short line wait for chapter 5; sharps and flats for chapter 6.
// ?draft=1 marks the lines that wait for her B answers. Not applied to the app.

// the Queen and the King, small, in pen (characters: hand-drawn)
function sfQueen(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-8.4, -3)], ['Q', P(-11, 8), P(-7.6, 13)], ['L', P(7.6, 13)], ['Q', P(11, 8), P(8.4, -3)], ['Z']], f: PEN_N, s: PEN_N, w: 1.2 });   // long hair
  s.push({ k: 'pa', seg: [['M', P(-11, 14.6)], ['Q', P(-10, 8.4), P(0, 8.8)], ['Q', P(10, 8.4), P(11, 14.6)], ['Z']], f: PEN_C, s: PEN_N, w: 1.5 });   // her gown
  [[-3, 11.2], [0, 11.9], [3, 11.2]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.9 * k, ry: 0.9 * k, f: PEN_P }));   // pearls
  s.push({ k: 'el', c: P(0, -0.4), rx: 6.8 * k, ry: 7.6 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.8, -2)], ['Q', P(-7, -8.4), P(0, -8.6)], ['Q', P(7, -8.4), P(6.8, -2)], ['Q', P(4, -6.2), P(0, -5.2)], ['Q', P(-4, -6.2), P(-6.8, -2)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });
  s.push({ k: 'pa', seg: [['M', P(-6, -7.8)], ['L', P(-7, -15.6)], ['L', P(-3.4, -11.4)], ['L', P(0, -17.6)], ['L', P(3.4, -11.4)], ['L', P(7, -15.6)], ['L', P(6, -7.8)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });   // her tall crown
  [[-7, -15.6], [0, -17.6], [7, -15.6]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 1 * k, ry: 1 * k, f: PEN_P, s: PEN_N, w: 0.8 }));
  s.push({ k: 'el', c: P(-2.5, 0.2), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.5, 0.2), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push(penCurve([['M', P(-1.9, 3.4)], ['Q', P(0, 4.8), P(1.9, 3.4)]], 1.1, PEN_N));
  return nnCh(s);
}
function sfKing(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-11.5, 14.6)], ['Q', P(-10.5, 8), P(0, 8.4)], ['Q', P(10.5, 8), P(11.5, 14.6)], ['Z']], f: PEN_N, s: PEN_N, w: 1.5 });   // his robe
  s.push(penCurve([['M', P(-8, 10.2)], ['Q', P(0, 13.2), P(8, 10.2)]], 2.2, PEN_P));   // the ermine collar
  s.push({ k: 'el', c: P(0, -1), rx: 6.8 * k, ry: 7.4 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.3, 0.6)], ['Q', P(-6.2, 9.8), P(0, 10.8)], ['Q', P(6.2, 9.8), P(6.3, 0.6)], ['Q', P(3.4, 4.6), P(0, 4.2)], ['Q', P(-3.4, 4.6), P(-6.3, 0.6)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });   // his beard
  s.push({ k: 'pa', seg: [['M', P(-6.6, -6.4)], ['L', P(-6.6, -13.6)], ['L', P(-3.3, -10.8)], ['L', P(0, -14.8)], ['L', P(3.3, -10.8)], ['L', P(6.6, -13.6)], ['L', P(6.6, -6.4)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });   // his crown
  s.push({ ...penLine(P(0, -14.8), P(0, -18.4), 1.3), }, { ...penLine(P(-1.6, -16.8), P(1.6, -16.8), 1.3) });   // the cross on top
  s.push({ k: 'el', c: P(-2.5, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.5, -1.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push(penCurve([['M', P(-1.6, 2.4)], ['Q', P(0, 3.4), P(1.6, 2.4)]], 1.1, PEN_P));
  return nnCh(s);
}
// a staff in the book's two inks: straight lines, the clefs from the music font, open note heads, labels, pen icons
// notes: [{ d, x, staff, color, label, lx, ly, lc, ls }]; extra(yOf, layer) draws more (arrows, numbers); icons: [{ shapes, x, y, k, vb }]
function SfStaff({ clef = 'treble', width = 340, notes = [], gap = 44, pad = [26, 26], extra, icons = [], label }) {
  const grand = clef === 'grand', none = clef === 'none';
  const staves = grand ? ['treble', 'bass'] : [none ? 'treble' : clef];
  const yOf = (d, st) => dY(d) + (grand && st === 'bass' ? gap : 0);
  const staffOf = (n) => n.staff || (grand ? (n.d >= 28 ? 'treble' : 'bass') : staves[0]);
  const ys = []; staves.forEach(st => ys.push(yOf(CLEFS[st].high, st), yOf(CLEFS[st].low, st)));
  notes.forEach(n => ys.push(yOf(n.d, staffOf(n))));
  const y0 = Math.min(...ys) - pad[0], y1 = Math.max(...ys) + pad[1];
  const inner = (shapes, vb) => { const s = penSvg(shapes, { vb }); return s.slice(s.indexOf('>') + 1, s.lastIndexOf('</svg>')); };
  const icn = useMemo(() => icons.map(ic => inner(ic.shapes, ic.vb || [0, 0, 44, 44])), [icons]);
  const txt = { fontFamily: "Inter, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif", paintOrder: 'stroke', stroke: BK.soft, strokeWidth: 3.5, strokeLinejoin: 'round' };
  return (
    <svg viewBox={`0 ${y0} ${width} ${y1 - y0}`} role="img" aria-label={label} style={{width:'100%',display:'block'}}>
      {extra && extra(yOf, 'under', txt)}
      {staves.map(st => CLEFS[st].lines.map(l => <line key={st + l} x1="4" x2={width - 4} y1={yOf(l, st)} y2={yOf(l, st)} stroke={BK.ink} strokeOpacity="0.75" strokeWidth="1.3"/>))}
      {grand && <line x1="4" x2="4" y1={yOf(38, 'treble')} y2={yOf(18, 'bass')} stroke={BK.ink} strokeWidth="1.8"/>}
      {!none && staves.map(st => <ClefGlyph key={'c' + st} clef={st} st={st} yOf={yOf} ink={BK.ink}/>)}
      {notes.map((n, i) => { const st = staffOf(n), y = yOf(n.d, st), x = n.x, c = n.color || BK.ink; return <g key={i}>
        {ledgersFor(n.d, CLEFS[st].low, CLEFS[st].high).map(p => <line key={p} x1={x - 12} x2={x + 12} y1={yOf(p, st)} y2={yOf(p, st)} stroke={BK.ink} strokeWidth="1.4"/>)}
        <ellipse cx={x} cy={y} rx="7.4" ry="5.2" fill={c}/><ellipse cx={x} cy={y} rx="3.4" ry="2.7" transform={`rotate(-38 ${x} ${y})`} fill="#fff"/>
        {n.label && <text x={x + (n.lx || 0)} y={y + (n.ly != null ? n.ly : 19)} textAnchor={n.la || 'middle'} fontSize={n.ls || 9.5} fontWeight="900" fill={n.lc || c} style={txt}>{n.label}</text>}
      </g>; })}
      {extra && extra(yOf, 'over', txt)}
      {icons.map((ic, i) => <g key={'i' + i} transform={`translate(${ic.x} ${ic.y}) scale(${ic.k || 1})`} dangerouslySetInnerHTML={{__html: icn[i]}}/>)}
    </svg>
  );
}
const sfArrowHead = (x, y, dir, c) => <path d={`M${x - 6 * dir} ${y - 4} L${x} ${y} L${x - 6 * dir} ${y + 4}`} fill="none" stroke={c} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"/>;
const sfHop = (x1, x2, y, h, c = BK.coral) => <g><path d={`M${x1} ${y} Q${(x1 + x2) / 2} ${y - h} ${x2} ${y}`} fill="none" stroke={c} strokeWidth="1.7"/><path d={`M${x2 - 5.5 * Math.sign(x2 - x1)} ${y - 5} L${x2} ${y} L${x2 - 7 * Math.sign(x2 - x1)} ${y + 1}`} fill="none" stroke={c} strokeWidth="1.7" strokeLinecap="round"/></g>;
const SF_ICON = (shapes, x, y, k = 1) => ({ shapes, x, y, k });

function sfLbPages(scr = false) {
  const ch = 'staff';
  const queen = sfQueen(22, 24, 1), king = sfKing(22, 24, 1), clara = nnClara(22, 24, 1);
  const turtle = [...fsTurtle(22, 26, 0.8), ...fsWaves(2, 36, 40, 0.8, 3)], bird = [...fsBird(22, 26, 1), ...fsCloud(10, 12, 0.6)];

  // p1: the grand staff as two palaces -- the Queen's G, Princess Clara's middle C, the King's F
  const p1 = <SfStaff clef="grand" width={340} pad={[44, 18]} label={t('The grand staff: the Queen beside her G line in the treble clef, the King beside his F line in the bass clef, and Princess Clara on middle C between them; the bird flies high at the top right, the turtle swims low at the bottom left', '큰보표: 높은음자리표의 G 줄 옆에 여왕, 낮은음자리표의 F 줄 옆에 왕, 그 사이 가운데 도에 클라라 공주; 오른쪽 위에는 새, 왼쪽 아래에는 거북이')}
    notes={[{ d: 24, x: 128, color: PEN_C, label: t('the King\'s F', '왕의 F'), la: 'end', lx: -12, ly: 4 }, { d: 28, x: 196, color: PEN_C, label: t('middle C', '가운데 도'), la: 'end', lx: -12, ly: 4 }, { d: 32, x: 264, color: PEN_C, label: t('the Queen\'s G', '여왕의 G'), la: 'end', lx: -12, ly: 4 }]}
    icons={[SF_ICON(king, 138, 150, 0.95), SF_ICON(clara, 206, 86, 0.85), SF_ICON(queen, 274, 66, 0.95), SF_ICON(bird, 292, 14, 0.95), SF_ICON(turtle, 40, 176, 0.75)]}/>;
  // p2: lines and spaces, counted from the bottom; a line note and a space note
  const p2 = <SfStaff clef="none" width={340} pad={[22, 40]} label={t('A staff with its five lines numbered 1 to 5 from the bottom and its four spaces numbered 1 to 4; a line note with the line through its middle, a space note between two lines', '아래에서부터 1~5번 줄, 1~4번 칸 번호가 붙은 오선; 줄이 가운데를 지나는 줄 음표와 두 줄 사이의 칸 음표')}
    notes={[{ d: 34, x: 136, color: PEN_C }, { d: 33, x: 226, color: PEN_C }]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      {[30, 32, 34, 36, 38].map((d, i) => <text key={d} x="16" y={yOf(d) + 3.5} fontSize="10" fontWeight="900" fill={BK.ink} textAnchor="middle">{i + 1}</text>)}
      {[31, 33, 35, 37].map((d, i) => <text key={d} x="322" y={yOf(d) + 3.5} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{i + 1}</text>)}
      <text x="16" y={yOf(38) - 9} fontSize="8.5" fontWeight="800" fill={BK.ink} textAnchor="middle">{t('lines', '줄')}</text>
      <text x="322" y={yOf(38) - 9} fontSize="8.5" fontWeight="800" fill={BK.coral} textAnchor="middle">{t('spaces', '칸')}</text>
      <text x="136" y={yOf(30) + 20} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('a line note', '줄 음표')}</text>
      <text x="136" y={yOf(30) + 32} fontSize="8.5" fontWeight="700" fill={BK.ink} textAnchor="middle">{t('the line goes through it', '줄이 가운데를 지나요')}</text>
      <text x="226" y={yOf(30) + 20} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('a space note', '칸 음표')}</text>
      <text x="226" y={yOf(30) + 32} fontSize="8.5" fontWeight="700" fill={BK.ink} textAnchor="middle">{t('between two lines', '두 줄 사이에 있어요')}</text>
    </g>}/>;
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
  // p4: the Queen of G -- the treble clef's curl wraps the second line
  const sfNeighbours = (ds, coralIdx, low, high, words) => (yOf, layer, txt) => layer === 'over' && <g style={txt}>{ds.map((d, i) => { const x = 70 + i * 56, up = i > coralIdx, c = i === coralIdx ? BK.coral : BK.ink;
      return <g key={i}><text x={x} y={up ? yOf(high) - 12 : yOf(low) + 19} fontSize={i === coralIdx ? 12 : 10.5} fontWeight="900" fill={c} textAnchor="middle">{dName(d)}</text>
        <text x={x} y={up ? yOf(high) - 24 : yOf(low) + 31} fontSize="8.2" fontWeight={i === coralIdx ? 900 : 700} fill={i === coralIdx ? BK.coral : BK.muted} textAnchor="middle">{words[i]}</text></g>; })}</g>;
  const nbWords = [t('skip down', '건너 아래'), t('step down', '한 걸음 아래'), '', t('step up', '한 걸음 위'), t('skip up', '건너 위')];
  const p4 = <SfStaff clef="treble" width={340} pad={[50, 40]} label={t('The treble clef; its curl wraps the second line, the Queen\'s G line, drawn in coral; the G on it, with F a step down, A a step up, E a skip down and B a skip up', '높은음자리표; 소용돌이가 감싸는 둘째 줄(여왕의 G 줄)이 산호색; 그 위의 G, 한 걸음 아래 F, 한 걸음 위 A, 한 칸 건너 아래 E, 위 B')}
    notes={[30, 31, 32, 33, 34].map((d, i) => ({ d, x: 70 + i * 56, color: i === 2 ? PEN_C : undefined }))}
    icons={[SF_ICON(queen, 108, 14, 0.9)]}
    extra={(yOf, layer, txt) => <g>{layer === 'under' && <line x1="36" x2="332" y1={yOf(32)} y2={yOf(32)} stroke={BK.coral} strokeWidth="3"/>}
      {sfNeighbours([30, 31, 32, 33, 34], 2, 30, 38, [nbWords[0], nbWords[1], t('the Queen\'s line', '여왕의 줄'), nbWords[3], nbWords[4]])(yOf, layer, txt)}</g>}/>;
  // p5: the King of F -- the bass clef's two dots guard the fourth line
  const p5 = <SfStaff clef="bass" width={340} pad={[50, 40]} label={t('The bass clef; its two dots guard the fourth line, the King\'s F line, drawn in coral; the F on it, with E a step down, G a step up, D a skip down and A a skip up', '낮은음자리표; 두 점이 지키는 넷째 줄(왕의 F 줄)이 산호색; 그 위의 F, 한 걸음 아래 E, 위 G, 한 칸 건너 아래 D, 위 A')}
    notes={[22, 23, 24, 25, 26].map((d, i) => ({ d, x: 70 + i * 56, color: i === 2 ? PEN_C : undefined }))}
    icons={[SF_ICON(king, 108, 74, 0.9)]}
    extra={(yOf, layer, txt) => <g>{layer === 'under' && <line x1="36" x2="332" y1={yOf(24)} y2={yOf(24)} stroke={BK.coral} strokeWidth="3"/>}
      {sfNeighbours([22, 23, 24, 25, 26], 2, 18, 26, [nbWords[0], nbWords[1], t('the King\'s line', '왕의 줄'), nbWords[3], nbWords[4]])(yOf, layer, txt)}</g>}/>;
  // p6: the grand staff; middle C on its own short line, under the Queen's staff or over the King's -- the same key; the fold
  const p6 = <SfStaff clef="grand" width={340} pad={[26, 26]} label={t('The grand staff: middle C written just under the treble staff and just over the bass staff, the same key, with Princess Clara between; folded at middle C, the Queen\'s G lands on the King\'s F, five keys each way', '큰보표: 높은음자리표 오선 바로 아래와 낮은음자리표 오선 바로 위에 쓴 가운데 도(같은 건반), 그 사이의 클라라 공주; 가운데 도에서 접으면 여왕의 G가 왕의 F에 겹쳐요, 양쪽으로 다섯 건반씩')}
    notes={[{ d: 28, x: 104, staff: 'treble', color: PEN_C }, { d: 28, x: 104, staff: 'bass', color: PEN_C }, { d: 32, x: 246, color: PEN_C, label: t('G: 5 up', 'G: 5개 위'), ly: -11 }, { d: 24, x: 246, color: PEN_C, label: t('F: 5 down', 'F: 5개 아래'), ly: 21 }]}
    icons={[SF_ICON(clara, 124, 108, 0.8), SF_ICON(queen, 290, 50, 0.85), SF_ICON(king, 290, 140, 0.85)]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <line x1="36" x2="332" y1={(yOf(28, 'treble') + yOf(28, 'bass')) / 2} y2={(yOf(28, 'treble') + yOf(28, 'bass')) / 2} stroke={BK.coral} strokeWidth="1.4" strokeDasharray="5 4"/>
      <text x="200" y={(yOf(28, 'treble') + yOf(28, 'bass')) / 2 + 3.5} fontSize="9" fontWeight="900" fill={BK.coral} textAnchor="middle" style={{paintOrder:'stroke',stroke:'#fff',strokeWidth:4}}>{t('fold here', '여기서 접어요')}</text>
      <text x="74" y={(yOf(28, 'treble') + yOf(28, 'bass')) / 2 + 3.5} fontSize="9.5" fontWeight="900" fill={BK.ink} textAnchor="end">{t('middle C', '가운데 도')}</text>
    </g>}/>;
  // p7: landmarks -- the Queen's G, the King's F, Clara's middle C; step or skip from the nearest one
  const p7 = <SfStaff clef="grand" width={340} pad={[30, 30]} label={t('The grand staff with the landmarks in coral -- the Queen\'s G, middle C and the King\'s F -- and the two space Cs in outline; two black notes read from the nearest landmark: A, a step up from G; D, a skip down from F', '큰보표의 기준 음(산호색): 여왕의 G, 가운데 도, 왕의 F, 그리고 칸의 C 두 개; 가까운 기준 음에서 읽는 검은 음표 둘: G에서 한 걸음 위 A, F에서 건너 아래 D')}
    notes={[{ d: 32, x: 90, color: PEN_C, label: 'G', ly: -11 }, { d: 33, x: 128, label: 'A?', ly: -11 }, { d: 35, x: 196, color: '#9a9cc4', label: 'C', ly: -11, lc: '#6d6f9c' }, { d: 28, x: 252, staff: 'treble', color: PEN_C, label: t('middle C', '가운데 도'), ly: -11 },
      { d: 24, x: 90, color: PEN_C, label: 'F', ly: 21 }, { d: 22, x: 128, label: 'D?', ly: 21 }, { d: 21, x: 196, color: '#9a9cc4', label: 'C', ly: 21, lc: '#6d6f9c' }]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <path d={`M97 ${yOf(32) - 6} Q109 ${yOf(32) - 16} 121 ${yOf(33) - 5}`} fill="none" stroke={BK.ink} strokeWidth="1.4" strokeDasharray="3 3"/>
      <path d={`M97 ${yOf(24, 'bass') + 6} Q109 ${yOf(24, 'bass') + 18} 121 ${yOf(22, 'bass') + 5}`} fill="none" stroke={BK.ink} strokeWidth="1.4" strokeDasharray="3 3"/>
      <text x="300" y={yOf(35) + 3} fontSize="8.5" fontWeight="800" fill="#6d6f9c" textAnchor="middle">{t('an octave up', '한 옥타브 위')}</text>
      <text x="300" y={yOf(21, 'bass') + 3} fontSize="8.5" fontWeight="800" fill="#6d6f9c" textAnchor="middle">{t('an octave down', '한 옥타브 아래')}</text>
    </g>}/>;

  const mini = (dots, extra = []) => { const s = []; for (let i = 0; i < 5; i++) s.push({ ...penLine([6, 8 + i * 6], [86, 8 + i * 6], 1.1), nw: true }); return [...s, ...dots.map(([x, y, c]) => ({ k: 'el', c: [x, y], rx: 4.4, ry: 3.1, f: c || PEN_N })), ...extra]; };
  const chkArts = {
    ls: mini([[34, 20, PEN_C], [58, 23, PEN_N]]),
    ss: mini([[20, 32], [32, 29], [44, 26]], [...nnHop(56, 76, 22, 6)].concat([{ k: 'el', c: [56, 26], rx: 4.4, ry: 3.1, f: PEN_C }, { k: 'el', c: [76, 20], rx: 4.4, ry: 3.1, f: PEN_C }])),
    queen: [...sfQueen(24, 22, 0.8), { ...penText(62, 30, 'G', { size: 18, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    king: [...sfKing(24, 22, 0.8), { ...penText(62, 30, 'F', { size: 18, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
    clara: [...nnClara(24, 22, 0.8), { ...penText(62, 30, 'C', { size: 18, weight: 900, fill: PEN_C, anchor: 'middle' }) }],
  };
  const checksRows = [
    ['ls', [0, 0, 92, 40], t('I can tell a line note from a space note, and count them from the bottom', '줄 음표와 칸 음표를 구별하고, 아래에서부터 셀 수 있어요')],
    ['ss', [0, 0, 92, 40], t('I can see a step or a skip on the staff, and play it', '오선에서 한 걸음과 건너뛰기를 보고 칠 수 있어요')],
    ['queen', [0, 0, 92, 40], t('I can find the Queen\'s G in the treble clef', '높은음자리표에서 여왕의 G를 찾을 수 있어요')],
    ['king', [0, 0, 92, 40], t('I can find the King\'s F in the bass clef', '낮은음자리표에서 왕의 F를 찾을 수 있어요')],
    ['clara', [0, 0, 92, 40], t('I can find middle C on both staves, and name notes from the landmarks', '두 오선에서 가운데 도를 찾고, 기준 음에서 음이름을 댈 수 있어요')],
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
      <LbSay size={17.5}>{t('Music is written on a staff: five lines and the four spaces between them. Every white key you named in Chapter 3 has its own place on it -- a line or a space -- and higher on the staff means higher on the piano. Two royal palaces share the staff: the Queen\'s on top for the high notes, the King\'s underneath for the low ones -- and in between, on middle C, lives Princess Clara.', '음악은 오선 위에 써요: 줄 다섯 개와 그 사이 칸 네 개. 3챕터에서 이름을 붙인 흰건반마다 오선에 제자리가 있어요 -- 줄 아니면 칸 -- 그리고 오선에서 높을수록 피아노에서도 높아요. 오선에는 두 궁전이 있어요: 위에는 높은 음을 맡은 여왕의 궁전, 아래에는 낮은 음을 맡은 왕의 궁전 -- 그리고 그 사이, 가운데 도에 클라라 공주가 살아요.')}</LbSay>
      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>
          {[[t('Lines and spaces', '줄과 칸'), 2], [t('Up the staff, up the piano', '오선 위로, 피아노 위로'), 3], [t('The Queen of G', 'G의 여왕'), 4], [t('The King of F', 'F의 왕'), 5], [t('Middle C: Princess Clara', '가운데 도: 클라라 공주'), 6], [t('Landmarks: read it fast', '기준 음: 빨리 읽기'), 7], [t('My five checks', '나의 다섯 가지 확인'), 8]].map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid #ece6d8'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><b>{'page ' + p}</b></div>)}
        </div></LbOnly>
        <div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('tell a line note from a space note', '줄 음표와 칸 음표를 구별할 수 있어요'), t('see a step or a skip on the staff, and play it', '오선에서 한 걸음과 건너뛰기를 보고 칠 수 있어요'), t('find the Queen\'s G and the King\'s F', '여왕의 G와 왕의 F를 찾을 수 있어요'), t('find middle C on both staves', '두 오선에서 가운데 도를 찾을 수 있어요'), t('name any note on the staff from a landmark', '오선의 어떤 음이든 기준 음에서 이름을 댈 수 있어요'), t('write a note on a line or in a space', '줄이나 칸에 음표를 쓸 수 있어요')].map((x, i) => <div key={i} style={{display:'flex',gap:8,fontSize:14.5,padding:'4px 0'}}><span style={{color:BK.coral,fontWeight:900}}>✓</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    // 2. lines and spaces
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Lines and spaces', '줄과 칸')}>
      {pic(p2, 200, 560)}
      <LbSay>{LANG === 'ko' ? <>오선에는 <b>줄 다섯 개</b>와 <b>칸 네 개</b>가 있어요. <b>아래에서부터</b> 세요: 1번 줄이 가장 낮고 5번 줄이 가장 높아요; 1번 칸은 1번 줄 바로 위예요. 음표는 모두 <b>줄 위</b>에 있거나 -- 줄이 음표 가운데를 지나요 -- <b>칸 안</b>에, 두 줄 사이에 있어요. <LbAsk q="B4">줄 음표는 꼬치: 줄이 가운데를 꿰뚫어요. 칸 음표는 샌드위치 속: 두 줄 사이에 끼어 있어요.</LbAsk></>
        : <>The staff has <b>five lines</b> and <b>four spaces</b>. Count them <b>from the bottom</b>: line 1 is the lowest, line 5 the highest; space 1 sits just above line 1. Every note lives either <b>on a line</b> -- the line goes straight through its middle -- or <b>in a space</b>, between two lines. <LbAsk q="B4">A line note is a kebab: the line goes right through it. A space note is the sandwich filling, between two lines.</LbAsk></>}</LbSay>
      <LbPiano title={t('Try it', '해 봐요')} steps={LANG === 'ko' ? [
        <><LbAsk q="B4"><b>손 오선:</b> 한 손을 옆으로 눕혀 손가락을 벌려요: 손가락 5개 = 줄 5개, 손가락 사이 4개 = 칸 4개.</LbAsk></>,
        <>누가 손가락이나 손가락 사이를 짚으면 말해요: "3번 줄!", "2번 칸!"</>,
        <>진짜 악보 한 쪽을 펴서 줄 음표 하나, 칸 음표 하나를 찾아 짚어요.</>,
      ] : [
        <><LbAsk q="B4"><b>The hand staff:</b> hold one hand out sideways, fingers spread: 5 fingers = 5 lines, the 4 gaps = 4 spaces.</LbAsk></>,
        <>Someone touches a finger or a gap; say which: "line 3!", "space 2!"</>,
        <>Open a page of real music: point to a line note, then a space note.</>,
      ]}/>
      <LbRemember>{t('On a line: the line goes through it. In a space: between two lines.', '줄 위: 줄이 가운데를 지나요. 칸 안: 두 줄 사이에 있어요.')}</LbRemember>
    </LbPage>,

    // 3. up the staff, up the piano: steps and skips
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Up the staff, up the piano', '오선 위로, 피아노 위로')}>
      {pic(p3, 210, 560)}
      <LbSay>{LANG === 'ko' ? <>오선은 건반의 지도예요. 오선에서 <b>위</b>에 있는 음은 <b>높은 소리</b> -- 피아노에서 오른쪽, 하늘 위 새 쪽이에요. <b>아래</b>는 왼쪽, 바다 아래 거북이 쪽이에요. 줄에서 바로 위 칸으로 가면 <b>한 걸음</b>: 다음 글자, 다음 흰건반. 줄에서 다음 줄로(칸에서 다음 칸으로) 가면 <b>건너뛰기</b> -- 3챕터의 그 건너뛰기, 글자 하나를 넘어가요.</>
        : <>The staff is a map of the keys. A note <b>higher</b> on the staff sounds <b>higher</b> -- it is further to the right on the piano, up towards the bird; <b>lower</b> on the staff is further left, down towards the turtle. From a line to the very next space is a <b>step</b>: the next letter, the next white key. From a line to the next line -- or a space to the next space -- is a <b>skip</b>: the same skip as in Chapter 3, one letter jumped over.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>아무 흰건반에서 시작해 그림의 <b>한 걸음</b>들을 쳐요: 위로, 위로, 위로, 위로 -- 이웃 건반으로.</>,
        <>이번엔 <b>건너뛰기</b>: 줄, 줄, 줄 -- 건반 하나씩 넘어가요.</>,
        <>누가 손으로 모양을 그려 줘요("한 걸음 위, 건너 아래..."): 그대로 쳐요.</>,
      ] : [
        <>Start on any white key and play the picture's <b>steps</b>: up, up, up, up -- to the next key each time.</>,
        <>Now the <b>skips</b>: line, line, line -- a key jumped over each time.</>,
        <>Someone draws a shape in the air ("step up, skip down..."); play it.</>,
      ]}/>
      <LbRemember>{t('Line to space: a step. Line to line: a skip.', '줄에서 칸: 한 걸음. 줄에서 줄: 건너뛰기.')}</LbRemember>
    </LbPage>,

    // 4. the Queen of G (treble clef)
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The Queen of G', 'G의 여왕')}>
      {pic(p4, 210, 560)}
      <LbSay>{LANG === 'ko' ? <>이 꼬불꼬불한 기호가 <b>높은음자리표</b>예요. 아주 옛날에는 그냥 글자 <b>G</b>였어요. 소용돌이가 줄 하나 -- 아래에서 <b>둘째 줄</b> -- 를 감싸고 있는데, 그 줄이 <b>여왕의 집</b>이에요: 그 줄 위의 음은 모두 <b>G</b>, 가운데 도 바로 위의 G예요. 여왕은 높은 목소리로 노래해요: 높은음자리표는 높은 음을 맡고, 보통 <b>오른손</b>이 읽어요.</>
        : <>This curly sign is the <b>treble clef</b>. Long ago it was simply a letter <b>G</b>. Its curl wraps round one line -- the <b>second line</b> from the bottom -- and that line is the <b>Queen's house</b>: every note on it is <b>G</b>, the G just above middle C. The Queen sings high: the treble clef is for the high notes, and usually the <b>right hand</b> reads it.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <><b>가운데 도</b>를 찾고, 흰건반 다섯 개를 걸어 올라가요: C D E F <b>G</b> -- 여왕의 G.</>,
        <>오선에서 G 줄(소용돌이가 감싼 줄)을 짚고, 오른손으로 G를 쳐요.</>,
        <>여왕의 G에서: 한 걸음 위(A), 한 걸음 아래(F), 건너 위(B), 건너 아래(E) -- 말하고 쳐요.</>,
      ] : [
        <>Find <b>middle C</b>, then walk up five white keys: C D E F <b>G</b> -- the Queen's G.</>,
        <>Point to the G line on the staff (the one the curl wraps), then play G with your right hand.</>,
        <>From the Queen's G: a step up (A), a step down (F), a skip up (B), a skip down (E) -- say it, then play it.</>,
      ]}/>
      <LbRemember>{t('The treble clef\'s curl wraps round G: the Queen\'s line.', '높은음자리표의 소용돌이는 G를 감싸요: 여왕의 줄.')}</LbRemember>
    </LbPage>,

    // 5. the King of F (bass clef)
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The King of F', 'F의 왕')}>
      {pic(p5, 210, 560)}
      <LbSay>{LANG === 'ko' ? <>이 기호는 <b>낮은음자리표</b>예요. 글자 <b>F</b>에서 시작했어요. 왕의 집은 아래에서 <b>넷째 줄</b>이고, 왕은 절대 혼자 다니지 않아요: 음자리표의 <b>두 점</b>이 경비병이에요 -- 하나는 왕의 줄 바로 위, 하나는 바로 아래. 두 경비병 사이의 줄이 <b>F</b>, 가운데 도 바로 아래의 F예요. 왕은 낮은 목소리로 노래해요: 낮은음자리표는 낮은 음을 맡고, 보통 <b>왼손</b>이 읽어요.</>
        : <>This sign is the <b>bass clef</b>. It began as a letter <b>F</b>. The King's house is the <b>fourth line</b> from the bottom, and he never goes out alone: the clef's <b>two dots</b> are his guards, one just above his line and one just below. The line between the guards is <b>F</b>, the F just below middle C. The King sings low: the bass clef is for the low notes, and usually the <b>left hand</b> reads it.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <><b>가운데 도</b>를 찾고, 흰건반 다섯 개를 걸어 내려가요: C B A G <b>F</b> -- 왕의 F.</>,
        <>오선에서 두 점 사이의 F 줄을 짚고, 왼손으로 F를 쳐요.</>,
        <>왕의 F에서: 한 걸음 위(G), 한 걸음 아래(E), 건너 위(A), 건너 아래(D) -- 말하고 쳐요.</>,
      ] : [
        <>Find <b>middle C</b>, then walk down five white keys: C B A G <b>F</b> -- the King's F.</>,
        <>Point to the F line between the two dots, then play F with your left hand.</>,
        <>From the King's F: a step up (G), a step down (E), a skip up (A), a skip down (D) -- say it, then play it.</>,
      ]}/>
      <LbRemember>{t('The bass clef\'s two dots guard F: the King\'s line.', '낮은음자리표의 두 점은 F를 지켜요: 왕의 줄.')}</LbRemember>
    </LbPage>,

    // 6. middle C: Princess Clara (the grand staff)
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={<LbAsk q="B1">{t('Middle C: Princess Clara', '가운데 도: 클라라 공주')}</LbAsk>}>
      {pic(p6, 230, 560)}
      <LbSay>{LANG === 'ko' ? <>여왕의 오선을 위에, 왕의 오선을 아래에 두고 앞에서 선으로 묶으면 <b>큰보표</b>예요 -- 손마다 오선 하나씩. 두 궁전 사이, <b>가운데 도</b>에는 <LbAsk q="B1"><b>클라라 공주</b>가 살아요</LbAsk> -- 2챕터의 땅이에요. 가운데 도는 <b>자기만의 짧은 줄</b>이 있어요: 여왕의 오선 바로 아래에 쓰든 왕의 오선 바로 위에 쓰든 <b>같은 건반</b>이에요. 두 궁전은 거울처럼 마주 봐요: 여왕의 G는 공주에서 흰건반 다섯 개 위, 왕의 F는 다섯 개 아래 -- 가운데 도에서 접으면 G가 F에 겹쳐요.</>
        : <>Put the Queen's staff on top and the King's underneath, joined by a line at the start: that is the <b>grand staff</b> -- one staff for each hand. Between the two palaces, on <b>middle C</b>, <LbAsk q="B1">lives <b>Princess Clara</b></LbAsk> -- the ground from Chapter 2. Middle C has a <b>short line of its own</b>: written just under the Queen's staff or just over the King's, it is <b>the same key</b>. And the palaces mirror each other: the Queen's G is five white keys above Clara, the King's F five below -- fold the grand staff at middle C, and G lands on F.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <><b>가운데 도</b>를 쳐요: 공주의 자리, 두 손이 다 닿는 단 한 곳.</>,
        <>오른손으로 다섯 개 위의 <b>G</b>, 왼손으로 다섯 개 아래의 <b>F</b>를 쳐요 -- 거울처럼.</>,
        <><b>F, C, G</b> 순서로 쳐요: 왕, 공주, 여왕 -- 낮게, 가운데, 높게.</>,
      ] : [
        <>Play <b>middle C</b>: Clara's place, the one key both hands can reach.</>,
        <>Play <b>G</b> five keys up with your right hand and <b>F</b> five keys down with your left -- a mirror.</>,
        <>Play <b>F, C, G</b>: the King, the Princess, the Queen -- low, middle, high.</>,
      ]}/>
      <LbRemember>{t('Middle C lives between the Queen and the King -- the same key on either staff.', '가운데 도는 여왕과 왕 사이에 살아요 -- 어느 오선에 써도 같은 건반.')}</LbRemember>
    </LbPage>,

    // 7. landmarks: read it fast
    <LbPage key="7" no={7} chId={ch} kicker={t('Step 6', '6단계')} title={t('Landmarks: read it fast', '기준 음: 빨리 읽기')}>
      {pic(p7, 230, 560)}
      <LbSay>{LANG === 'ko' ? <>매번 맨 아래 줄부터 세면 느려요. 대신 가장 가까운 <b>기준 음</b>을 찾아요 -- 여왕의 <b>G</b>, 왕의 <b>F</b>, 공주의 <b>가운데 도</b> -- 그리고 거기서 한 걸음이나 건너뛰기로 가요. G 바로 위 칸? 한 걸음: <b>A</b>. F 아래 줄? 건너뛰기: <b>D</b>. <LbAsk q="B3">각 오선 한가운데의 C도 기준 음이 돼요: 공주보다 한 옥타브 위와 아래.</LbAsk> <LbAsk q="B2">(줄을 외우는 문장도 있어요 -- 높은음자리표 줄 E G B D F "Every Good Boy Deserves Fruit" -- 처음엔 도움이 되지만, 기준 음이 더 빨라요.)</LbAsk></>
        : <>Counting up from the bottom line every time is slow. Instead, find the nearest <b>landmark</b> -- the Queen's <b>G</b>, the King's <b>F</b> or Princess Clara's <b>middle C</b> -- and step or skip from there. The space just above G? A step: <b>A</b>. The line below F? A skip: <b>D</b>. <LbAsk q="B3">The C in the middle of each staff is a landmark too: an octave above Clara, and an octave below.</LbAsk> <LbAsk q="B2">(Some readers learn a rhyme for the treble lines, E G B D F, "Every Good Boy Deserves Fruit" -- it helps at first, but landmarks are faster.)</LbAsk></>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>누가 큰보표의 음 하나를 짚으면: 가장 가까운 기준 음을 찾고, 이름을 말하고, 쳐요.</>,
        <><b>기준 음 게임:</b> "G!" "F!" "가운데 도!" -- 최대한 빨리 건반에서 찾아요.</>,
        <>기준 음에서 출발하는 세 음을 읽고, 이어서 쳐요.</>,
      ] : [
        <>Someone points to a note on the grand staff: find the nearest landmark, say the name, play it.</>,
        <><b>Landmark game:</b> "G!" "F!" "Middle C!" -- find them on the keys as fast as you can.</>,
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
// the check-up on paper (draft), in the order of the five checks
function SfPaperCheck() {
  const C = useMemo(() => withSeed('sf-chk401', () => ({
    ls: shuffle([30, 33, 36, 35]).map(d => ({ d })),
    ss: [[31, 32], [34, 32], [30, 34], [37, 36]].map(([a, b]) => ({ a, b })),
    tr: shuffle([33, 30, 36, 34]),
    ba: shuffle([25, 22, 26, 20]),
    mc: { treble: shuffle([{ d: 28 }, { d: 31 }, { d: 34 }]), bass: shuffle([{ d: 28 }, { d: 23 }, { d: 26 }]) },
  })), [LANG]);
  const cell = (n, kids) => <BkCell key={n} n={n}><div style={{padding:'5px 4px 0'}}>{kids}</div></BkCell>;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column'}}>
    <LbPaperHead/>
    {bkSec('A', 'Line or space? Write L or S.')}
    <BkGrid cols={4} gap="5px 10px">{C.ls.map((it, i) => cell(i + 1, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:72}}><PaperStaff clefOn={false} notes={[{ d: it.d }]} width={90}/></div>{bkBox(28, 24)}</div>))}</BkGrid>
    {bkSec('B', 'Step or skip? Up or down? Write it.')}
    <BkGrid cols={4} gap="5px 10px">{C.ss.map((it, i) => cell(i + 5, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:72}}><PaperStaff clefOn={false} notes={[{ d: it.a }, { d: it.b }]} width={90}/></div>{bkBox(44, 24)}</div>))}</BkGrid>
    {bkSec('C', 'Name the treble notes. Start from the Queen\'s G.')}
    <BkGrid cols={4} gap="5px 10px">{C.tr.map((d, i) => cell(i + 9, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:84}}><PaperStaff clef="treble" notes={[{ d }]} width={110}/></div>{bkBox(28, 24)}</div>))}</BkGrid>
    {bkSec('D', 'Name the bass notes. Start from the King\'s F.')}
    <BkGrid cols={4} gap="5px 10px">{C.ba.map((d, i) => cell(i + 13, <div style={{display:'flex',alignItems:'center',gap:8}}><div style={{flex:1,maxWidth:84}}><PaperStaff clef="bass" notes={[{ d }]} width={110}/></div>{bkBox(28, 24)}</div>))}</BkGrid>
    {bkSec('E', 'Circle every middle C.')}
    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:10}}>{['treble', 'bass'].map(cl => <div key={cl} style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 10px'}}><div style={{maxWidth:200}}><PaperStaff clef={cl} notes={C.mc[cl]} width={220}/></div></div>)}</div>
  </div>;
}
