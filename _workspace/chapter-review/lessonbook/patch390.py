# Phase 390 (Sohyun 2026-10-09): the low sounds are a TURTLE, not a bear; and middle C is the ground --
# going up climbs into the sky (the bird), going down dives under the sea (the turtle).
# Lesson Book, Workbook, Teacher copy, the app and the guide page change together.
# Run from the repo root: python3 _workspace/chapter-review/lessonbook/patch390.py
p = 'drills.src.html'
s = open(p, encoding='utf-8').read()
done = []
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    assert c == n, f"{what}: expected {n}, got {c}"
    s = s.replace(a, b); done.append(what)

# ── 1. the pen drawings: a turtle (swimming right, toward the high end), little waves, a cloud
i = s.index('// the bear (low end) and the bird (high end), small, in pen')
j = s.index('function fsBird(', i)
s = s[:i] + """// the turtle (low end, under the sea) and the bird (high end, up in the sky), small, in pen (Sohyun 2026-10-09)
function fsTurtle(x, y, k = 1) {
  const s = [], P = (a, b) => [x + a * k, y + b * k];
  const rot = (a, cx, cy) => { const r = a * Math.PI / 180, c = Math.cos(r), n = Math.sin(r); return [c, n, -n, c, x + cx * k, y + cy * k]; };
  s.push({ k: 'el', c: [0, 0], rx: 5.2 * k, ry: 2.4 * k, f: PEN_P, s: PEN_N, w: 1.6, m: rot(-28, -10, 7) });      // back flipper
  s.push({ k: 'el', c: [0, 0], rx: 6.2 * k, ry: 2.6 * k, f: PEN_P, s: PEN_N, w: 1.6, m: rot(30, 9, 7) });         // front flipper
  s.push({ k: 'pa', seg: [['M', P(-15, 3)], ['L', P(-20, 5)], ['L', P(-15, 6)], ['Z']], f: PEN_P, s: PEN_N, w: 1.4 });   // tail
  s.push({ k: 'el', c: P(19, -1), rx: 5.6 * k, ry: 4.4 * k, f: PEN_P, s: PEN_N, w: 1.8 });                       // head
  s.push({ k: 'el', c: P(20.6, -2.2), rx: 0.95 * k, ry: 0.95 * k, f: PEN_N });                                   // eye
  s.push({ k: 'pa', seg: [['M', P(-15, 4)], ['Q', P(-14, -11), P(0, -11)], ['Q', P(14, -11), P(15, 4)], ['Z']], f: PEN_P, s: PEN_N, w: 1.9 });   // shell
  s.push({ k: 'pa', seg: [['M', P(-4.5, -6)], ['L', P(4.5, -6)], ['L', P(6.5, -1)], ['L', P(4.5, 3.5)], ['L', P(-4.5, 3.5)], ['L', P(-6.5, -1)], ['Z']], f: 'none', s: PEN_N, w: 1.3 });
  [[-6.5, -1, -14.5, 1], [6.5, -1, 14.5, 1], [-4.5, -6, -7, -10], [4.5, -6, 7, -10]].forEach(([a, b, c2, d]) => s.push(penLine(P(a, b), P(c2, d), 1.2)));
  return s;
}
function fsWaves(x, y, w, k = 1, n = 3) {
  const seg = [['M', [x, y]]], step = w / n;
  for (let i = 0; i < n; i++) seg.push(['Q', [x + step * (i + 0.5), y - 4 * k], [x + step * (i + 1), y]]);
  return [{ k: 'pa', seg, f: 'none', s: PEN_N, w: 1.6 }];
}
function fsCloud(x, y, k = 1) {
  const P = (a, b) => [x + a * k, y + b * k];
  return [{ k: 'pa', seg: [['M', P(-13, 4)], ['Q', P(-16, -3), P(-8, -4)], ['Q', P(-6, -11), P(1, -9)], ['Q', P(8, -13), P(11, -5)], ['Q', P(17, -4), P(14, 4)], ['Z']], f: PEN_P, s: PEN_N, w: 1.6 }];
}
""" + s[j:]
done.append('fsTurtle, fsWaves, fsCloud (fsBear gone)')

# p2: the direction strip -- turtle under the sea at the low end, bird with a cloud at the high end
rep("""    s.push(...fsBear(22, 44, 0.9));
    s.push(...fsBird(320, 12, 0.95));
    s.push({ k: 'pa', seg: [['M', [60, 76]], ['L', [290, 76]]], f: 'none', s: PEN_C, w: 2, nw: true });
    s.push({ k: 'pa', seg: [['M', [284, 72]], ['L', [292, 76]], ['L', [284, 80]], ['Z']], f: PEN_C });
    s.push({ ...penText(62, 88, t('low voices', '낮은 소리'), { size: 9.5, weight: 900, fill: PEN_N }), halo: true });
    s.push({ ...penText(288, 88, t('high voices', '높은 소리'), { size: 9.5, weight: 900, fill: PEN_C, anchor: 'end' }), halo: true });""",
"""    s.push(...fsTurtle(23, 54, 0.82), ...fsWaves(6, 66, 36, 1, 3));
    s.push(...fsCloud(323, 15, 0.68), ...fsBird(322, 38, 0.85));
    s.push({ k: 'pa', seg: [['M', [60, 76]], ['L', [290, 76]]], f: 'none', s: PEN_C, w: 2, nw: true });
    s.push({ k: 'pa', seg: [['M', [284, 72]], ['L', [292, 76]], ['L', [284, 80]], ['Z']], f: PEN_C });
    s.push({ ...penText(62, 88, t('low: under the sea', '낮은 소리: 바다 아래'), { size: 9.5, weight: 900, fill: PEN_N }), halo: true });
    s.push({ ...penText(288, 88, t('high: up in the sky', '높은 소리: 하늘 위'), { size: 9.5, weight: 900, fill: PEN_C, anchor: 'end' }), halo: true });""",
    'p2 strip: turtle + sea, bird + sky')
rep("""label={t('The street runs from the bear\\'s low end to the bird\\'s high end', '거리는 곰의 낮은 쪽 끝에서 새의 높은 쪽 끝으로 이어져요')}""",
    """label={t('The street runs from the turtle under the sea at the low end to the bird in the sky at the high end', '거리는 바다 아래 거북이가 사는 낮은 쪽 끝에서 하늘 위 새가 나는 높은 쪽 끝으로 이어져요')}""",
    'p2 strip label')
# p5: middle C is the ground
rep("""    s.push({ ...penText(mcX + W / 2, Y + H + 27, t('middle C', '가운데 도'), { size: 10, weight: 900, fill: PEN_C, anchor: 'middle' }), halo: true });
    s.push({ ...penText(mcX - 10, Y + H + 12, t('← low voices', '← 낮은 목소리'), { size: 8.5, weight: 800, fill: PEN_N, anchor: 'end' }), halo: true });
    s.push({ ...penText(mcX + W + 10, Y + H + 12, t('high voices →', '높은 목소리 →'), { size: 8.5, weight: 800, fill: PEN_N, anchor: 'start' }), halo: true });
    s.push(...penPlace(fsBear(0, 0, 1), 0.72, [0, 0], [10, 38]));
    s.push(...penPlace(fsBird(0, 0, 1), 0.9, [0, 0], [548, 26]));""",
"""    s.push({ ...penText(mcX + W / 2, Y + H + 27, t('middle C: the ground', '가운데 도: 땅'), { size: 10, weight: 900, fill: PEN_C, anchor: 'middle' }), halo: true });
    s.push({ ...penText(mcX - 10, Y + H + 12, t('← down under the sea', '← 바다 아래로'), { size: 8.5, weight: 800, fill: PEN_N, anchor: 'end' }), halo: true });
    s.push({ ...penText(mcX + W + 10, Y + H + 12, t('up into the sky →', '하늘 위로 →'), { size: 8.5, weight: 800, fill: PEN_N, anchor: 'start' }), halo: true });
    s.push(...penPlace([...fsTurtle(0, 0, 1), ...fsWaves(-22, 12, 44, 1, 3)], 0.6, [0, 0], [11, 40]));
    s.push(...penPlace([...fsCloud(-24, 14, 0.8), ...fsBird(4, 0, 1)], 0.82, [0, 0], [548, 26]));""",
    'p5: middle C is the ground')
rep("""label={t('All 88 keys: 7 small and 7 big houses, the kennel, and middle C where the low and high voices meet', '88개 건반 전체: 작은 집 7채와 큰 집 7채, 개집, 그리고 낮은 목소리와 높은 목소리가 만나는 가운데 도')}""",
    """label={t('All 88 keys: 7 small and 7 big houses, the kennel, and middle C, the ground between the sea and the sky', '88개 건반 전체: 작은 집 7채와 큰 집 7채, 개집, 그리고 바다와 하늘 사이의 땅인 가운데 도')}""",
    'p5 picture label')

# ── 2. the words on the pages
rep("""그리고 거리는 <b>왼쪽(낮은 소리)에서 오른쪽(높은 소리)</b>으로 올라가요.</> : <>The black keys are the <b>roofs</b> of the houses. <b>Two black keys</b> = the small house's roof; <b>three</b> = the big house's. Small, big, small, big... the same two houses repeat all the way up the piano. And the street climbs from <b>left (low sounds) to right (high sounds)</b>.</>}</LbSay>""",
    """그리고 거리는 <b>왼쪽(낮은 소리, 바다 아래 거북이)</b>에서 <b>오른쪽(높은 소리, 하늘 위 새)</b>으로 올라가요.</> : <>The black keys are the <b>roofs</b> of the houses. <b>Two black keys</b> = the small house's roof; <b>three</b> = the big house's. Small, big, small, big... the same two houses repeat all the way up the piano. And the street climbs from <b>left (low sounds, the turtle under the sea)</b> to <b>right (high sounds, the bird in the sky)</b>.</>}</LbSay>""",
    'p2 text')
rep("""        <>눈을 감아요. 누가 높거나 낮은 소리를 하나 치면, 그 소리가 사는 쪽을 가리켜요.</>,""",
    """        <>눈을 감아요. 누가 높거나 낮은 소리를 하나 치면, 거북이 쪽인지 새 쪽인지 가리켜요.</>,""", 'p2 step 3 KO')
rep("""        <>Close your eyes. Someone plays one high or one low sound -- point to the end of the street where it lives.</>,""",
    """        <>Close your eyes. Someone plays one high or one low sound -- point to the turtle's end or the bird's end.</>,""", 'p2 step 3 EN')
rep("""{t('The bear (low end) and the bird (high end) carry the direction; loud/soft stays out of this chapter (her call).', '곰(낮은 쪽)과 새(높은 쪽)가 방향을 맡아요; 크고 작게는 이 챕터에서 뺐어요(소현님 결정).')}""",
    """{t('The turtle (low end, under the sea) and the bird (high end, up in the sky) carry the direction; loud and soft stay out of this chapter.', '거북이(낮은 쪽, 바다 아래)와 새(높은 쪽, 하늘 위)가 방향을 맡아요; 크고 작게는 이 챕터에서 다루지 않아요.')}""",
    'p2 teacher note')
rep("""<b>4번째 작은 집</b>까지 세면 그 왼쪽 문이 <b>가운데 도(middle C)</b>: 왼쪽은 낮은 목소리 나라, 오른쪽은 높은 목소리 나라, 가운데 도는 <b>둘이 만나는 문</b>이에요.</> : <>A real piano has <b>88 keys</b> -- yet still only 7 small houses and 7 big ones. Count to the <b>4th small house</b>: its left door is <b>middle C</b>. To its left live the low voices, to its right the high voices -- middle C is <b>the door where they meet</b>.</>}</LbSay>""",
    """<b>4번째 작은 집</b>까지 세면 그 왼쪽 문이 <b>가운데 도(middle C)</b>예요. 가운데 도는 <b>땅</b>이에요: 오른쪽으로 가면 <b>하늘 위로</b> 점점 높이, 왼쪽으로 가면 <b>바다 아래로</b> 점점 깊이 내려가요.</> : <>A real piano has <b>88 keys</b> -- yet still only 7 small houses and 7 big ones. Count to the <b>4th small house</b>: its left door is <b>middle C</b>. Middle C is <b>the ground</b>: go right and you climb <b>up into the sky</b>, higher and higher; go left and you dive <b>down under the sea</b>, lower and lower.</>}</LbSay>""",
    'p5 text')
rep("""        <><b>가운데 도</b>를 치고, 한 집 아래의 C(더 낮은 목소리)와 한 집 위의 C(더 높은 목소리)도 쳐 봐요.</>,""",
    """        <><b>가운데 도</b>를 치고, 한 집 아래의 C(바다 속으로)와 한 집 위의 C(하늘로)도 쳐 봐요.</>,""", 'p5 step 3 KO')
rep("""        <>Play <b>middle C</b>; then the C one house lower (a lower voice) and one house higher (a higher one).</>,""",
    """        <>Play <b>middle C</b>; then the C one house lower (down into the sea) and one house higher (up into the sky).</>,""", 'p5 step 3 EN')
rep("""<LbRemember>{t('Middle C: just left of the 4th small house -- where low and high meet.', '가운데 도: 4번째 작은 집 바로 왼쪽 -- 낮음과 높음이 만나는 곳.')}</LbRemember>""",
    """<LbRemember>{t('Middle C is the ground: up into the sky, down under the sea.', '가운데 도는 땅: 위로 가면 하늘, 아래로 가면 바다.')}</LbRemember>""", 'p5 remember')
rep("""{t('No staff yet: the Queen of G and the King of F wait for the Reading chapter -- here we only plant "the low and high voices meet at middle C".', '오선보는 아직이에요: 솔의 여왕과 파의 왕은 악보 읽기 챕터에서 등장해요 -- 여기서는 "낮은 목소리와 높은 목소리가 가운데 도에서 만난다"만 심어 둬요.')}""",
    """{t('No staff yet: the Queen of G and the King of F wait for the Reading chapter -- here we only plant "middle C is the ground: up into the sky, down under the sea".', '오선보는 아직이에요: 솔의 여왕과 파의 왕은 악보 읽기 챕터에서 등장해요 -- 여기서는 "가운데 도는 땅: 위로 가면 하늘, 아래로 가면 바다"만 심어 둬요.')}""",
    'p1 teacher note')

# ── 3. the paper turtle (Workbook icons, KeyScene) replaces the paper bear
i = s.index('// A bear (low sounds) and a bird (high sounds) -- <g> pieces to drop on any keyboard picture.')
j = s.index('function BirdG(', i)
s = s[:i] + """// A turtle (low sounds, under the sea) and a bird (high sounds, up in the sky) -- <g> pieces to drop on any keyboard picture.
function TurtleG({ x = 0, y = 0, s = 1 }) {
  return <g transform={`translate(${x} ${y}) scale(${s})`}>
    <ellipse cx="-10" cy="7" rx="5.2" ry="2.4" transform="rotate(-28 -10 7)" fill="#fff" {...ART_SW} strokeWidth="1.4"/>
    <ellipse cx="9" cy="7" rx="6.2" ry="2.6" transform="rotate(30 9 7)" fill="#fff" {...ART_SW} strokeWidth="1.4"/>
    <path d="M-15 3 L-20 5 L-15 6 Z" fill="#fff" {...ART_SW} strokeWidth="1.3"/>
    <ellipse cx="19" cy="-1" rx="5.6" ry="4.4" fill="#fff" {...ART_SW}/><circle cx="20.6" cy="-2.2" r="1" fill={BK.ink}/>
    <path d="M-15 4 Q-14 -11 0 -11 Q14 -11 15 4 Z" {...ART_SWF}/>
    <path d="M-4.5 -6 L4.5 -6 L6.5 -1 L4.5 3.5 L-4.5 3.5 L-6.5 -1 Z M-6.5 -1 L-14.5 1 M6.5 -1 L14.5 1 M-4.5 -6 L-7 -10 M4.5 -6 L7 -10" fill="none" {...ART_SW} strokeWidth="1.2"/>
    <path d="M-22 14 q 5.5 -4 11 0 q 5.5 -4 11 0 q 5.5 -4 11 0 q 5.5 -4 11 0" fill="none" {...ART_SW} strokeWidth="1.3"/>
  </g>;
}
""" + s[j:]
done.append('TurtleG (BearG gone)')
rep("""function KeyScene({ start = 'C', whites = 14, w = 40, h = 110, houses = true, doors = false, families = false, kennel = false, bear = false, bird = false,""",
    """function KeyScene({ start = 'C', whites = 14, w = 40, h = 110, houses = true, doors = false, families = false, kennel = false, turtle = false, bird = false,""",
    'KeyScene turtle prop')
rep("""  const padL = bear ? 40 + 24 * Math.max(1, Math.min(1.7, w / 34)) : 0,""", """  const padL = turtle ? 46 + 24 * Math.max(1, Math.min(1.7, w / 34)) : 0,""", 'KeyScene padL')
rep("""  const W = padL + whites * w + 4 + padR, H = top + h + (bear ? 4 : 4);""", """  const W = padL + whites * w + 4 + padR, H = top + h + 4;""", 'KeyScene H')
rep("""      {bear && <BearG x={padL - 30 * sc} y={top + h - 30 * sc} s={sc}/>}""", """      {turtle && <TurtleG x={padL - 32 * sc} y={top + h - 26 * sc} s={sc}/>}""", 'KeyScene draws the turtle')
rep("""// black key (a 1-group) gets a dog kennel. bear / bird: at the low end / the high end.""", """// black key (a 1-group) gets a dog kennel. turtle / bird: at the low end (under the sea) / the high end (in the sky).""", 'KeyScene comment')
rep("""const bearIcon = (s = 30) => <svg width={s} height={s} viewBox="-20 -24 40 52" style={{display:'block'}}><BearG s={0.9}/></svg>;""",
    """const turtleIcon = (s = 30) => <svg width={s} height={s} viewBox="-24 -16 50 34" style={{display:'block'}}><TurtleG s={0.9}/></svg>;""", 'turtleIcon')
rep("""// Sound-picture icons for the bear-or-bird puzzle""", """// Sound-picture icons for the turtle-or-bird puzzle""", 'icon comment')

# ── 4. the Workbook
rep("""    <Part kind="play" title="Bear or bird?" how="Low sounds live at the bear's end, high sounds at the bird's end. Draw a line from each sound to the bear or the bird, then make each sound on the piano!">""",
    """    <Part kind="play" title="Turtle or bird?" how="Low sounds swim with the turtle under the sea; high sounds fly with the bird up in the sky. Draw a line from each sound to the turtle or the bird, then make each sound on the piano!">""",
    'workbook p2 play')
rep("""{bearIcon(66)}low</div>""", """{turtleIcon(66)}low</div>""", 'workbook p2 turtle icon')
rep("""        <div style={{margin:'0 0 2px'}}>Bottom half -- the low keys, the bear's end</div><KeyScene start="A" whites={26} w={24} h={72} houses={false} bear/>
        <div style={{margin:'6px 0 2px'}}>Top half -- the high keys, the bird's end (carry on counting here)</div>""",
    """        <div style={{margin:'0 0 2px'}}>Bottom half -- the low keys, the turtle's end under the sea</div><KeyScene start="A" whites={26} w={24} h={72} houses={false} turtle/>
        <div style={{margin:'6px 0 2px'}}>Top half -- the high keys, the bird's end up in the sky (carry on counting here)</div>""",
    'workbook p5 halves')
rep("""    <Part kind="play" title="Low Land and High Land" how="Middle C is the door between them. Draw who lives in Low Land (left of the door) and who lives in High Land (right of it). Then play their voices!">""",
    """    <Part kind="play" title="Under the sea, up in the sky" how="Middle C is the ground. Draw what swims under the sea (to the left of middle C) and what flies up in the sky (to the right of it). Then play their sounds!">""",
    'workbook p5 play')
rep("""        {box('Low Land')}""", """        {box('Under the sea (low)')}""", 'workbook p5 sea box')
rep("""        {box('High Land')}""", """        {box('Up in the sky (high)')}""", 'workbook p5 sky box')
rep("""<circle cx="21" cy="24" r="2" fill={BK.coral}/></svg>middle C</div>""", """<circle cx="21" cy="24" r="2" fill={BK.coral}/></svg>middle C: the ground</div>""", 'workbook p5 ground label')

# ── 5. the Teacher copy
rep("""{tcAns('PLAY', ['bear (low): elephant, thunder, drum', 'bird (high): mouse, bell, whistle'])}""",
    """{tcAns('PLAY', ['turtle (low): elephant, thunder, drum', 'bird (high): mouse, bell, whistle'])}""", 'teacher p2 answers')
rep("""no staff yet (the Queen of G and the King of F wait for the Reading chapter -- here only "the low and high voices meet at middle C").""",
    """no staff yet (the Queen of G and the King of F wait for the Reading chapter -- here only "middle C is the ground: up into the sky, down under the sea").""", 'teacher intro')
rep("""      say="“Count the small houses to 4. Middle C is the door just to its left.”"/>""",
    """      say="“Count the small houses to 4. Middle C is the door just to its left -- the ground. Up is the sky, down is the sea.”"/>""", 'teacher p5 say')

# ── 6. the app's Whole piano tool
rep("""t('Middle C is the C nearest the middle of the piano. Count the small houses from the left: middle C is the white key just left of the 4th one.', '가운데 도는 피아노 한가운데에 가장 가까운 C예요. 왼쪽부터 작은 집을 세어 봐요: 네 번째 작은 집 바로 왼쪽 흰건반이 가운데 도예요.')""",
    """t('Middle C is the C nearest the middle of the piano. Count the small houses from the left: middle C is the white key just left of the 4th one. It is the ground: to the right the notes climb into the sky, to the left they dive under the sea.', '가운데 도는 피아노 한가운데에 가장 가까운 C예요. 왼쪽부터 작은 집을 세어 봐요: 네 번째 작은 집 바로 왼쪽 흰건반이 가운데 도예요. 가운데 도는 땅이에요: 오른쪽으로 가면 하늘 위로, 왼쪽으로 가면 바다 아래로 가요.')""",
    'WholePiano middle C note')

rep('{bearIcon(22)}', '{turtleIcon(22)}', 'HighCell icon')
assert 'fsBear' not in s and 'BearG' not in s and 'bearIcon' not in s, 'a bear is left'
open(p, 'w', encoding='utf-8').write(s)
print('\n'.join('ok: ' + d for d in done))
print('PATCH 390 DONE')
