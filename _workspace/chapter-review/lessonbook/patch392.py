# Phase 392 (Sohyun 2026-10-09, on the chapter 2 side-by-side print): (1) the spread cover gets a keyboard-pattern
# scene around the rabbit; (2) Lesson Book p2: the words sit under their own picture (houses, then the sea-to-sky
# street, drawn wider with a boat, the turtle under the waves, clouds and the bird); (3) the books never assume who is
# teaching (a teacher, a parent, or nobody): TOGETHER / AT HOME become TRY IT / YOUR TURN, "your teacher" leaves the
# student pages of every Workbook; (4) Workbook p2 "Turtle or bird?" asks about PAIRS (which one is lower?), so every
# answer is certain. Names (her B1): chapter 2 = "Keyboard Patterns / 건반 패턴", chapter 3 = "The Musical Alphabet /
# 음악 알파벳". Run from the repo root: python3 _workspace/chapter-review/lessonbook/patch392.py
import re
p = 'drills.src.html'
s = open(p, encoding='utf-8').read()
done = []
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    assert c == n, f"{what}: expected {n}, got {c}"
    s = s.replace(a, b); done.append(what)

# ── names ──
rep("id: 'first-steps', label: 'Keyboard Patterns & Note Names',", "id: 'first-steps', label: 'Keyboard Patterns',", 'ch2 drill + map labels', 2)
rep("'first-steps': '건반 패턴과 음이름', 'note-names': '음이름',", "'first-steps': '건반 패턴', 'note-names': '음악 알파벳',", 'Korean names')
rep("{t('Keyboard Patterns & Note Names', '건반 패턴과 음이름')}</div>", "{t('Keyboard Patterns', '건반 패턴')}</div>", 'ch2 book title')
rep("<Lesson id=\"first-steps\" title={t('Keyboard Patterns & Note Names', '건반 패턴과 음이름')}", "<Lesson id=\"first-steps\" title={t('Keyboard Patterns', '건반 패턴')}", 'ch2 app title')
rep("// ─── Chapter 2: Keyboard Patterns & Note Names (Phase 387 -- applied) ───", "// ─── Chapter 2: Keyboard Patterns (Phase 387 -- applied; renamed from \"Keyboard Patterns & Note Names\" in Phase 392) ───", 'ch2 comment')
rep("  // Phase 388: the chapter 2 Workbook follows the Lesson Book page by page (Keyboard Patterns & Note Names)", "  // Phase 388: the chapter 2 Workbook follows the Lesson Book page by page (Keyboard Patterns)", 'ch2 wb comment')
rep("{ id: 'note-names', label: 'Note Names', concept: NOTE_NAMES_DRILL, track: 'pitch' },", "{ id: 'note-names', label: 'The Musical Alphabet', concept: NOTE_NAMES_DRILL, track: 'pitch' },", 'ch3 map label')
rep("  id: 'note-names',\n  label: 'Note Names',", "  id: 'note-names',\n  label: 'The Musical Alphabet',", 'ch3 drill label')
rep("<Lesson id=\"note-names\" title={t('Finding notes on the keyboard', '건반에서 음이름 찾기')}", "<Lesson id=\"note-names\" title={t('The Musical Alphabet', '음악 알파벳')}", 'ch3 app title')
rep("'note-names': ['Note names', '음 이름'],", "'note-names': ['Alphabet', '알파벳'],", 'ch3 room')
rep("  'note-names': 'note name letter alphabet keyboard',", "  'note-names': 'note name names letter alphabet musical alphabet forwards backwards step skip octave keyboard',", 'ch3 keywords')

# ── (1) the spread cover: a scene for chapter 2 ──
rep("""function SpreadCover({ id }) {""", """// Phase 392 (Sohyun 2026-10-09): a chapter's cover can carry its own scene around the rabbit butler.
// Chapter 2: the rabbit stands on the ground between the small house (C D E) and the big house (F G A B);
// the sea and the turtle lie at the low end on the left, the clouds and the bird at the high end on the right.
function fsCoverShapes() {
  const s = [], G = 262, W = 46, H = 134, Y = G - H;
  const house = (x, letters, tint) => {
    const n = letters.length, BW = W * 0.62, BH = H * 0.58;
    const out = [{ k: 'rc', x, y: Y, w: n * W, h: H, rx: 2, f: PEN_P, s: PEN_N, sw: 2.8, nw: true }];
    for (let i = 0; i < n; i++) out.push({ k: 'rc', x: x + i * W + 1.2, y: Y + 2.2, w: W - 2.4, h: H - 4.4, rx: 1.5, f: tint, nw: true });
    for (let i = 1; i < n; i++) out.push({ ...penLine([x + i * W, Y], [x + i * W, Y + H], 1.4), nw: true });
    for (let i = 0; i < n - 1; i++) out.push({ k: 'rc', x: x + (i + 1) * W - BW / 2, y: Y, w: BW, h: BH, rx: 1, f: PEN_N, solid: true, nw: true });
    letters.forEach((l, i) => out.push({ ...penText(x + (i + 0.5) * W, Y + H - 12, l, { size: 22, weight: 900, fill: i === 0 ? PEN_C : PEN_N, anchor: 'middle' }) }));
    out.push(...fsRoof({ kind: n === 3 ? 'small' : 'big', x1: x + W - BW / 2 - W * 0.14, x2: x + (n - 1) * W + BW / 2 + W * 0.14 }, Y - 1, n === 3 ? 26 : 33, { w: 3 }));
    return out;
  };
  // the sea at the low end: waves, a turtle swimming under them
  s.push(...fsWaves(0, G + 2, 118, 1.6, 4));
  s.push(...fsWaves(8, G + 24, 100, 1.2, 3).map(e => ({ ...e, s: '#9a9cc4' })));
  s.push(...fsTurtle(54, G + 54, 1.6));
  s.push({ k: 'el', c: [100, G + 40], rx: 2.6, ry: 2.6, f: 'none', s: PEN_N, w: 1.4 }, { k: 'el', c: [106, G + 30], rx: 1.9, ry: 1.9, f: 'none', s: PEN_N, w: 1.3 });
  // the ground, the two houses
  s.push(penLine([114, G], [672, G], 2, '#bdb7a6'));
  s.push(...house(124, ['C', 'D', 'E'], '#fbe9e2'));
  s.push(...house(452, ['F', 'G', 'A', 'B'], '#e9eaf4'));
  // the sky at the high end: clouds and the bird
  s.push(...fsCloud(580, 44, 2), ...fsCloud(654, 66, 1.3), ...fsBird(614, 92, 1.8));
  return s;
}
function FsCoverScene() {
  const shapes = useMemo(() => {
    const RH = 240, RW = RH * 160 / 210;    // the rabbit butler (his baked drawing), standing on the ground at x = 357
    const r = PB_ART.rabbit || '', inner = r.slice(r.indexOf('>') + 1, r.lastIndexOf('</svg>'));   // a group, not a nested svg (page css sizes every svg)
    const rabbit = '<g transform="translate(' + (357 - RW / 2).toFixed(1) + ' ' + (264 - RH) + ') scale(' + (RH / 210).toFixed(4) + ')">' + inner + '</g>';
    return [...fsCoverShapes(), { k: 'raw', svg: rabbit }];
  }, []);
  return <div style={{width:680,maxWidth:'100%'}}><PenArt shapes={shapes} vb={[0, 20, 680, 324]} label="The rabbit butler stands on the ground between a small house of keys, C D E, and a big house, F G A B; the sea and a turtle at the low end, clouds and a bird at the high end"/></div>;
}
const SPREAD_SCENES = { 'first-steps': () => <FsCoverScene/> };
function SpreadCover({ id }) {""", 'cover scene')
rep("""        <PbArt name="rabbit" h={300}/>
        <div style={{maxWidth:420,fontSize:13,color:BK.ink,lineHeight:1.55,border:'1.5px dashed ' + BK.line,borderRadius:12,padding:'10px 16px'}}>""",
    """        {SPREAD_SCENES[id] ? SPREAD_SCENES[id]() : <PbArt name="rabbit" h={300}/>}
        <div style={{maxWidth:420,fontSize:13,color:BK.ink,lineHeight:1.55,border:'1.5px dashed ' + BK.line,borderRadius:12,padding:'10px 16px'}}>""", 'cover uses the scene')

# ── (2) Lesson Book p2: two pictures, each with its own words ──
a = s.index("  const art2b = (() => {")
b = s.index("  // p3: each house carries its white keys")
s = s[:a] + """  // p2b (Phase 392): the street from the low end (a boat on the waves, the turtle under the sea) to the high end
  // (clouds, the bird up in the sky), drawn wider so the two ends tell the story
  const art2b = (() => {
    const s = [];
    const K = fsKeysShapes(74, 34, 21, 9.4, 42);
    s.push(...K.shapes);
    // the sea: waves, a little sailing boat on top, the turtle underneath
    s.push(...fsWaves(0, 52, 66, 1.1, 4));
    s.push(...fsWaves(6, 66, 54, 0.8, 3).map(e => ({ ...e, s: '#9a9cc4' })));
    s.push({ k: 'pa', seg: [['M', [19, 47]], ['L', [49, 47]], ['L', [44, 54]], ['L', [24, 54]], ['Z']], f: PEN_P, s: PEN_N, w: 1.6 });
    s.push(penLine([34, 47], [34, 20], 1.5));
    s.push({ k: 'pa', seg: [['M', [36, 23]], ['L', [36, 44]], ['L', [50, 44]], ['Z']], f: PEN_P, s: PEN_N, w: 1.4 });
    s.push({ k: 'pa', seg: [['M', [33, 20]], ['L', [41, 22.5]], ['L', [33, 25.5]], ['Z']], f: PEN_C });
    s.push(...fsTurtle(30, 84, 0.72));
    s.push({ k: 'el', c: [50, 75], rx: 1.7, ry: 1.7, f: 'none', s: PEN_N, w: 1.1 }, { k: 'el', c: [54, 69], rx: 1.2, ry: 1.2, f: 'none', s: PEN_N, w: 1 });
    // the sky: two clouds and the bird
    s.push(...fsCloud(300, 16, 0.78), ...fsCloud(328, 34, 0.55), ...fsBird(306, 54, 0.95));
    // the direction
    s.push({ k: 'pa', seg: [['M', [78, 90]], ['L', [262, 90]]], f: 'none', s: PEN_C, w: 2, nw: true });
    s.push({ k: 'pa', seg: [['M', [262, 86]], ['L', [270, 90]], ['L', [262, 94]], ['Z']], f: PEN_C });
    s.push({ ...penText(4, 106, t('low: under the sea', '낮은 소리: 바다 아래'), { size: 9.5, weight: 900, fill: PEN_N }), halo: true });
    s.push({ ...penText(336, 106, t('high: up in the sky', '높은 소리: 하늘 위'), { size: 9.5, weight: 900, fill: PEN_C, anchor: 'end' }), halo: true });
    return s;
  })();
""" + s[b:]
done.append('p2 street scene')
a = s.index("    // 2. small house, big house (+ the low -> high direction)")
b = s.index("      <LbPiano steps={LANG === 'ko' ? [\n        <>피아노 가운데쯤에서 <b>작은 집</b>")
old = s[a:b]
head = old[:old.index("      <LbLive still=")]
s = s[:a] + head + """      <LbLive still={<LbPic h={190}><div style={{width:'100%',maxWidth:420,margin:'0 auto'}}><PenArt shapes={art2} vb={[0, 0, 300, 162]} label={t('One octave: a small house over the two black keys, a big house with a chimney over the three', '한 옥타브: 검은건반 두 개 위에 작은 집, 세 개 위에 굴뚝 달린 큰 집')}/></div></LbPic>} live={<KeyHouses modes={['houses']}/>}/>
      <LbSay>{LANG === 'ko' ? <>검은건반은 집의 <b>지붕</b>이에요. <b>검은건반 2개</b> = 작은 집의 지붕, <b>3개</b> = 큰 집의 지붕. 작은 집, 큰 집, 작은 집, 큰 집... 피아노 끝까지 같은 두 집이 반복돼요.</> : <>The black keys are the <b>roofs</b> of the houses. <b>Two black keys</b> = the small house's roof; <b>three</b> = the big house's. Small, big, small, big... the same two houses repeat all the way up the piano.</>}</LbSay>
      <LbLive still={<LbPic h={150} pad="10px 12px"><div style={{width:'100%'}}><PenArt shapes={art2b} vb={[0, 4, 340, 108]} label={t('The street of keys runs from the low end, where a boat sails on the waves and the turtle swims under the sea, to the high end, where the bird flies among the clouds', '건반 거리는 배가 떠 있고 거북이가 바다 아래 헤엄치는 낮은 쪽 끝에서, 새가 구름 사이를 나는 높은 쪽 끝으로 이어져요')}/></div></LbPic>} live={<HighLowGame pitchOnly/>}/>
      <LbSay>{LANG === 'ko' ? <>거리는 <b>왼쪽</b>에서 <b>오른쪽</b>으로 올라가요: 낮은 소리는 왼쪽 끝, <b>바다 아래 거북이</b>와 함께 살고, 높은 소리는 오른쪽 끝, <b>하늘 위 새</b>와 함께 살아요.</> : <>And the street climbs from <b>left</b> to <b>right</b>: the low sounds live at the left end with <b>the turtle under the sea</b>, the high sounds at the right end with <b>the bird up in the sky</b>.</>}</LbSay>
""" + s[b:]
done.append('p2 words under their pictures')

# ── (3) the books never assume who is teaching ──
rep("""const BK_TAG = {
  together: { label: 'TOGETHER', sub: 'in your lesson', bg: BK.ink, fg: '#fff' },
  home: { label: 'AT HOME', sub: 'on your own', bg: BK.coral, fg: '#fff' },""",
    """// Phase 392 (Sohyun 2026-10-09): a page may be done with a teacher, with a parent, or alone -- so the parts say what
// to do, not where or with whom: TOGETHER -> TRY IT (the first item is the worked example), AT HOME -> YOUR TURN.
const BK_TAG = {
  together: { label: 'TRY IT', sub: 'the first one is an example', bg: BK.ink, fg: '#fff' },
  home: { label: 'YOUR TURN', sub: 'the same, on your own', bg: BK.coral, fg: '#fff' },""", 'part tags')
rep("    ['LESSON BOOK', 'Read one step with your teacher.'],\n    ['WORKBOOK', 'Do that step’s page: TOGETHER, AT HOME, PLAY.'],",
    "    ['LESSON BOOK', 'Read one step.'],\n    ['WORKBOOK', 'Do that step’s page.'],", 'route cards')
rep("checkPage ? 'Page ' + checkPage + ', in the lesson, when every step is done.' : 'The last page, in the lesson, when every step is done.'",
    "checkPage ? 'Page ' + checkPage + ', when every step is done.' : 'The last page, when every step is done.'", 'route check-up')
rep("Real-piano missions for this chapter. Tick one box each time you do it with your teacher or at home.", "Real-piano missions for this chapter. Tick one box each time you do it.", 'map missions note')
rep("""      <span style={{marginLeft:14}}>Teacher</span><span style={{width:22,height:22,border:'1.5px solid ' + BK.line,borderRadius:5}}/>""",
    """      <span style={{marginLeft:14}}>Checked</span><span style={{width:22,height:22,border:'1.5px solid ' + BK.line,borderRadius:5}}/>""", 'page foot box')
rep("Your teacher writes the page. You tick it when it is done. Your teacher checks it next lesson -- and you get a sticker!", "Write the page and the date. Tick it when it is done -- and when it has been checked, add a sticker!", 'homework log')
rep("""          <span>Parent <span style={{display:'inline-block',width:140,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></span>
          <span>Teacher <span style={{display:'inline-block',width:140,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></span>""",
    """          <span>Checked by <span style={{display:'inline-block',width:180,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></span>""", 'practice log signature')
rep("""<div style={{fontSize:13,fontWeight:900,color:BK.ink}}>Teacher's note</div>""", """<div style={{fontSize:13,fontWeight:900,color:BK.ink}}>Notes</div>""", 'check-up note box')
rep("In the lesson -- no help, no piano -- about 10 minutes", "No help, no piano -- about 10 minutes", 'check-up line', 2)
rep("the <b style={{color:BK.ink}}>Lesson Book</b> (what your teacher explains)", "the <b style={{color:BK.ink}}>Lesson Book</b> (the idea, explained)", 'front: lesson book')
rep("    {tagRow('together', 'In your lesson.', 'The first few, with your teacher. The first one is always an example, already done for you.')}\n    {tagRow('home', 'On your own.', 'The same thing at home -- about 10 minutes. Your teacher writes at the top when it is due.')}",
    "    {tagRow('together', 'Try it.', 'The first few. The first one is always an example, already done for you.')}\n    {tagRow('home', 'Your turn.', 'The same thing on your own -- about 10 minutes. Write at the top when it is due.')}", 'front: tag rows')
rep("Your teacher writes the drill level and your best score there.", "Write the drill level and your best score there.", 'front: strip')
rep("Do the Chapter check-up{checkPage ? ' on page ' + checkPage : ''} in your lesson, then colour in the badge.", "Do the Chapter check-up{checkPage ? ' on page ' + checkPage : ''}, then colour in the badge.", 'map: check-up callout')
rep("<span><b>Finished a chapter?</b> Do its check-up in your lesson, colour in the badge", "<span><b>Finished a chapter?</b> Do its check-up, colour in the badge", 'front: finished')
# Teacher copies: the same names for the parts
n1 = s.count("tcAns('TOGETHER'"); s = s.replace("tcAns('TOGETHER'", "tcAns('TRY IT'"); done.append('tc TRY IT x%d' % n1)
n2 = len(re.findall(r"tcAns\('AT HOME", s)); s = re.sub(r"tcAns\('AT HOME", "tcAns('YOUR TURN", s); done.append('tc YOUR TURN x%d' % n2)
rep(">AT HOME</div>", ">YOUR TURN</div>", 'tc time-sig label')
rep(">AT HOME (beams)</div>", ">YOUR TURN (beams)</div>", 'tc beams label')
rep(">TOGETHER + AT HOME</div>", ">TRY IT + YOUR TURN</div>", 'tc combined label')
rep("Do TOGETHER in the lesson, set AT HOME and PLAY as homework.", "TRY IT comes first (its first item is the worked example), then YOUR TURN and PLAY.", 'tc intro nn')
rep("Set one page per lesson step: do TOGETHER in the lesson, set AT HOME and PLAY as homework, and write Set / Due on the strip.",
    "Set one page per lesson step: TRY IT first (its first item is the worked example), then YOUR TURN and PLAY; write Set / Due on the strip.", 'tc intro generic')
# the student pages: "your teacher" -> someone / a grown-up
for a_, b_ in [
    ("Ask your teacher to photocopy this page first. ", "Photocopy this page first. "),
    ("how=\"Your teacher shows you 10 cards.", "how=\"Someone shows you 10 cards."),
    ("<b style={{color:BK.coral}}>Teacher: photocopy this page before cutting</b>", "<b style={{color:BK.coral}}>Grown-ups: photocopy this page before cutting</b>"),
    ("try to catch your teacher out!", "try to catch someone out!"),
    ("how=\"Your teacher calls a letter:", "how=\"Someone calls a letter:"),
    ("Play it to your teacher next lesson!", "Play it to someone!"),
    ("<span>I played it to my teacher</span>", "<span>I played it to someone</span>"),
    (">My teacher's stars</span>", ">My stars</span>"),
    ("make up a riddle of your own and try it on your teacher!", "make up a riddle of your own and try it on someone!"),
    ("give it a title, and play it to your teacher!", "give it a title, and play it to someone!"),
    ("then clap each card with your teacher.", "then clap each card."),
    ("Look at each picture with your teacher, then try it at the piano.", "Look at each picture, then try it at the piano."),
    ("Then tell your teacher what is wrong.", "Then say what is wrong."),
    ("Leave a circle empty to hold the note. Play it to your teacher!", "Leave a circle empty to hold the note. Play it to someone!"),
    ("how=\"Your teacher claps a 4-beat rhythm. Clap it back, then write it in the box together.", "how=\"Someone claps a 4-beat rhythm. Clap it back, then write it in the box."),
    ("text={<>Teacher claps -- ", "text={<>Someone claps -- "),
    ("Give your tune a name and play it to your teacher!", "Give your tune a name and play it to someone!"),
    ("look through your pieces and your teacher's books.", "look through your pieces and your music books."),
    ("<b>Teacher:</b> photocopy this page before cutting", "<b>Grown-ups:</b> photocopy this page before cutting"),
    ("how=\"Make up 3 silly instructions for your teacher using little words -- “molto presto e staccato”! Write them, then your teacher has to play a scale exactly that way.",
     "how=\"Make up 3 silly instructions using little words -- “molto presto e staccato”! Write them, then someone has to play a scale (or clap, or walk!) exactly that way."),
    ("No phone? Your teacher plays a 3-note tune -- you echo it.", "No phone? Someone plays a 3-note tune -- you echo it."),
    ("Your teacher keeps a click going -- or scan the code", "Someone keeps a click going -- or scan the code"),
    ("No phone? Your teacher plays two phrases and you call it.", "No phone? Someone plays two phrases and you call it."),
    ("A friend (or your teacher) checks the key below.", "A friend checks the key below."),
    ("how=\"Say the letters round the wheel with your teacher, then fill the gaps.", "how=\"Say the letters round the wheel out loud, then fill the gaps."),
    ("how=\"Say each row out loud with your teacher first, then fill the gaps.", "how=\"Say each row out loud first, then fill the gaps."),
]:
    c_ = s.count(a_); assert c_ >= 1, a_; s = s.replace(a_, b_); done.append('student text x%d: %s' % (c_, a_[:34]))
s = s.replace("<div style={{fontSize:12,color:BK.ink}}>AT HOME: ", "<div style={{fontSize:12,color:BK.ink}}>YOUR TURN: "); done.append('tc inline YOUR TURN')
rep('how="Be a piano detective at home. Count carefully -- then compare with a friend’s piano or your teacher’s.">', 'how="Be a piano detective. Count carefully -- then compare with another piano you know.">', 'piano detective')
# the chapter 1 Lesson Book's mirror game
rep("""          <>선생님이 "오른손 3번!" 하고 부르면 그 손가락을 꼼지락거려요. 열 번 해 봐요.</>,
          <>바꿔요: 내가 손가락을 부르고, 선생님이 꼼지락거려요.</>,""",
    """          <>누가 "오른손 3번!" 하고 부르면 그 손가락을 꼼지락거려요. 열 번 해 봐요.</>,
          <>바꿔요: 내가 손가락을 부르고, 상대가 꼼지락거려요.</>,""", 'ch1 mirror ko')
rep("""          <>Your teacher calls "Right hand, 3!" and you wiggle it. Try ten calls.</>,
          <>Swap: you call the finger, and your teacher wiggles it.</>,""",
    """          <>Someone calls "Right hand, 3!" and you wiggle it. Try ten calls.</>,
          <>Swap: you call the finger, and they wiggle it.</>,""", 'ch1 mirror en')

# ── (4) Workbook p2 "Turtle or bird?": pairs, so every answer is certain ──
a = s.index("""    <Part kind="play" title="Turtle or bird?" how=""")
b = s.index("    <Faces/>", a)
s = s[:a] + """    <Part kind="play" title="Turtle or bird?" how="In each pair, one sound is lower and one is higher. Draw a line from the lower one to the turtle and from the higher one to the bird -- then make both sounds on the piano!">
      <div style={{display:'grid',gridTemplateColumns:'86px 1fr 86px',gap:10,alignItems:'center',flex:1}}>
        <div style={{display:'grid',justifyItems:'center',gap:2,fontSize:12,fontWeight:800,color:BK.ink}}>{turtleIcon(66)}low</div>
        <div style={{display:'grid',gap:8}}>{[[['mouse', 'a mouse', 46], ['elephant', 'an elephant', 82]], [['drum', 'a big drum', 78], ['drum', 'a little drum', 42]], [['bell', 'a little bell', 40], ['bell', 'a big bell', 76]]].map((pair, r) => (
          <div key={r} data-pair={r + 1} style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:14,background:BK.soft,borderRadius:10,padding:'4px 8px'}}>{pair.map(([k, lab, sz]) => <div key={lab} style={{background:'#fff',border:'1px solid #ece6d8',borderRadius:8,display:'grid',justifyItems:'center',alignContent:'end',padding:'0 4px 3px',fontSize:11.5,color:BK.ink,height:80}}><SoundIcon kind={k} size={sz}/>{lab}</div>)}</div>))}</div>
        <div style={{display:'grid',justifyItems:'center',gap:2,fontSize:12,fontWeight:800,color:BK.coral}}>{birdIcon(66)}high</div>
      </div>
      <div style={{textAlign:'center',fontSize:12.5,color:BK.ink,marginTop:6}}>Big and heavy sounds <b>low</b> · small and light sounds <b style={{color:BK.coral}}>high</b></div>
    </Part>
""" + s[b:]
done.append('turtle or bird: pairs')
rep("{tcAns('PLAY', ['turtle (low): elephant, thunder, drum', 'bird (high): mouse, bell, whistle'])}",
    "{tcAns('PLAY', ['turtle (lower): the elephant, the big drum, the big bell', 'bird (higher): the mouse, the little drum, the little bell'])}", 'tc turtle or bird')

open(p, 'w', encoding='utf-8').write(s)
print('\n'.join('ok: ' + d for d in done))
print('PATCH 392 DONE')
