# Phase 394 (Sohyun 2026-10-09): (1) the Lesson Book's first page and the Workbook's first page said the same thing --
# now they are ONE page (the chapter opener: words, picture, the steps to tick with their pages, what you can do by
# the end, the drill's code), and the last pages likewise (My five checks at the piano + the check-up on paper, one
# page). In a side-by-side print the opener is page 1 (the old cover's place), then each lesson page faces its
# workbook page, and the check-up page closes the chapter; a Workbook printed alone carries the same two pages.
# (2) Every page puts the lesson's words straight under the big title, before the picture. (3) "Turtle or bird?"
# uses sounds a child can make and hear, not sizes: a chick / a cow, a lion / a mouse, a whistle / a ship's horn.
# Run from the repo root: python3 _workspace/chapter-review/lessonbook/patch394.py
import re
p = 'drills.src.html'
s = open(p, encoding='utf-8').read()
done = []
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    assert c == n, f"{what}: expected {n}, got {c}"
    s = s.replace(a, b); done.append(what)
def cut(a, b, what):   # remove from marker a (inclusive) to marker b (exclusive)
    global s
    i = s.index(a); j = s.index(b, i)
    s = s[:i] + s[j:]; done.append(what)

# ── (2) words first ──
rep("""// One fixed A4 page of the Lesson Book.
function LbPage(""", """// Sohyun 2026-10-09 (Phase 394): the lesson's words come first, right under the big title -- a picture (or its live
// tool) that is followed by its words changes places with them, on paper and on screen.
const lbIsPic = (c) => !!c && (c.type === LbLive || c.type === LbPic || (c.type === LbOnly && c.props && c.props.children && c.props.children.type === LbPic));
function lbWordsFirst(children) {
  const a = React.Children.toArray(children);
  for (let i = 0; i < a.length - 1; i++) if (lbIsPic(a[i]) && a[i + 1].type === LbSay) { const x = a[i]; a[i] = a[i + 1]; a[i + 1] = x; i++; }
  return a;
}
// One fixed A4 page of the Lesson Book.
function LbPage(""", 'lbWordsFirst')
rep("""flexDirection:'column',gap:16}}><BkChapterCtx.Provider value={chId}>{children}</BkChapterCtx.Provider></div>""", """flexDirection:'column',gap:16}}><BkChapterCtx.Provider value={chId}>{lbWordsFirst(children)}</BkChapterCtx.Provider></div>""", 'LbPage words first')
rep("""        <div className="lb-screen" data-lb-screen={page.props.no} style={{display:'flex',flexDirection:'column',gap:14,margin:'4px 0 6px'}}>
          {children}""", """        <div className="lb-screen" data-lb-screen={page.props.no} style={{display:'flex',flexDirection:'column',gap:14,margin:'4px 0 6px'}}>
          {lbWordsFirst(children)}""", 'screen words first')
rep("""{opener.props.children}</div>""", """{lbWordsFirst(opener.props.children)}</div>""", 'app heads words first', 2)

# ── (1) the opener is the map too: steps with tick boxes, and the drill ──
rep("""function LbFig({ art, h, cap }) {""", """// Phase 394: the chapter opener is also the Workbook's map -- the drill's code and its levels
function LbDrillStrip({ id }) {
  const levels = bkLevels(id);
  return (
    <div data-lb-drill style={{display:'flex',gap:14,alignItems:'center',border:'1.5px solid ' + BK.line,borderRadius:12,padding:'8px 12px',background:BK.soft}}>
      <div style={{flex:'0 0 auto',padding:4,border:'1.5px solid ' + BK.line,borderRadius:8,background:'#fff',lineHeight:0}}><QR url={bkLink('drill=' + id + '&tab=drill&level=1&lock=1')} size={72}/></div>
      <div style={{flex:1,minWidth:0}}>
        <div style={{fontSize:10,fontWeight:900,letterSpacing:'0.1em',color:BK.coral}}>ONLINE</div>
        <div style={{fontSize:13,color:BK.ink,margin:'1px 0 5px'}}><b>The lesson and the drill.</b> Scan, pick a level, aim for 9 out of 10.</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(' + Math.max(1, Math.min(3, levels.length)) + ', 1fr)',gap:'3px 14px'}}>{levels.map(l => <div key={l.n} style={{display:'flex',alignItems:'center',gap:6,fontSize:11.5,color:BK.ink}}><span style={{flex:'0 0 auto',width:17,height:17,borderRadius:9,background:BK.ink,color:'#fff',fontSize:9.5,fontWeight:900,display:'inline-flex',alignItems:'center',justifyContent:'center'}}>{l.n}</span><span style={{flex:1}}>{l.label}</span><span style={{color:BK.muted,whiteSpace:'nowrap'}}>__/10</span></div>)}</div>
      </div>
    </div>
  );
}
// Phase 394: the check-up page's paper part
function LbPaperHead() {
  return <div style={{display:'flex',alignItems:'baseline',justifyContent:'space-between',gap:10,borderTop:'1.6px solid ' + BK.ink,paddingTop:6,flexWrap:'wrap'}}>
    <span style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,color:BK.ink}}>On paper</span>
    <span style={{fontSize:12,color:BK.muted}}>Name <span style={{display:'inline-block',width:120,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span>  Date <span style={{display:'inline-block',width:60,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span>  · no help, no piano · about 10 minutes</span>
  </div>;
}
function LbFig({ art, h, cap }) {""", 'LbDrillStrip + LbPaperHead')
rep(""".map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span>{n}</span><b>{p}</b></div>)""",
    """.map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><b>{'page ' + p}</b></div>)""", 'opener steps with ticks (ch2)')
rep(""".map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span>{n}</span><span style={{color:BK.muted,fontWeight:700}}>page {p}</span></div>)""",
    """.map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid #ece6d8'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkTick(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>page {p}</span></div>)""", 'opener steps with ticks (ch1)')
rep("""      <LbOnly print><div style={{fontSize:13,color:BK.muted}}>Goes with: the Workbook page beside each lesson page, and the online lesson.</div></LbOnly>""",
    """      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>""", 'opener drill strip', 2)
# chapter 2's opener carries the cover scene (the rabbit between the houses, the sea and the sky)
a = s.index("      <LbPic h={225}><div style={{width:'100%'}}><PenArt shapes={art1} vb={[0, 14, 340, 128]}")
b = s.index("</LbPic>", a) + len("</LbPic>")
s = s[:a] + "      <LbPic h={210}><FsCoverScene/></LbPic>" + s[b:]; done.append('ch2 opener picture = cover scene')
rep("""      <LbPic h={300}><LbFig art="puppet" h={350} cap={t('Sit tall, like a puppet on a string', '줄에 매달린 인형처럼 곧게 앉아요')}/></LbPic>""",
    """      <LbPic h={230}><LbFig art="puppet" h={290} cap={t('Sit tall, like a puppet on a string', '줄에 매달린 인형처럼 곧게 앉아요')}/></LbPic>""", 'ch1 opener picture size')

# ── (1) the last page: My five checks + the check-up on paper ──
# chapter 2
rep("""    <LbPage key="7" no={7} chId={ch} kicker={t('Step 5', '5단계')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Chapter 1\\'s five checks still come first, every time at the piano. These five are this chapter\\'s own""",
    """    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Chapter 1\\'s five checks still come first, every time at the piano. These five are this chapter\\'s own""", 'ch2 checks kicker')
rep("""      <LbSay>{t('Show, don\\'t tell! Give yourself a star for each check in each lesson.', '말로 말고, 직접 보여 줘요! 레슨마다 확인 하나에 별 하나씩 칠해요.')}</LbSay>
      <LbLive still={<div style={{display:'flex',flexDirection:'column',gap:9,flex:'1 1 auto'}}>
        <div style={{display:'grid',gridTemplateColumns:'110px 1fr repeat(6, 34px)',gap:8,alignItems:'end',fontSize:11,fontWeight:800,color:BK.muted,textAlign:'center'}}><span/><span style={{textAlign:'right',paddingRight:6}}>{t('Lesson', '레슨')}</span>{[1, 2, 3, 4, 5, 6].map(n => <span key={n}>{n}</span>)}</div>
        {checksRows.map(([a, vb, txt], i) => (
          <div key={i} style={{display:'grid',gridTemplateColumns:'110px 1fr repeat(6, 34px)',gap:8,alignItems:'center',border:'1px solid #ece6d8',borderRadius:12,padding:'6px 8px',flex:'1 1 auto'}}>
            <div style={{display:'flex',justifyContent:'center'}}><PenArt shapes={chkArts[a]} vb={vb} style={{width:92}}/></div>
            <div style={{fontSize:15,fontWeight:800,color:BK.ink}}>{txt}</div>
            {[1, 2, 3, 4, 5, 6].map(n => <span key={n} style={{width:30,height:30,border:'1.5px solid ' + BK.line,borderRadius:8,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center'}}><BkStarG size={14} fill="#ece6d8"/></span>)}
          </div>))}
      </div>} live={<FiveChecks376 storeKey="pb_five_fs_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
      <LbRemember>{t('Pattern first, names second -- the keyboard is a map you can read.', '패턴 먼저, 이름은 그다음 -- 건반은 읽을 수 있는 지도예요.')}</LbRemember>""",
    """      <LbSay>{t('At the piano: show each one and give yourself a star. On paper: do the check-up below. All done? Colour in the badge!', '피아노 앞에서: 하나씩 보여 주고 별을 칠해요. 종이에서: 아래 점검을 풀어요. 다 끝나면? 배지를 색칠해요!')}</LbSay>
      <LbLive still={<div style={{display:'flex',flexDirection:'column',gap:5}}>
        <div style={{display:'grid',gridTemplateColumns:'96px 1fr repeat(6, 28px)',gap:7,alignItems:'end',fontSize:10.5,fontWeight:800,color:BK.muted,textAlign:'center'}}><span style={{textAlign:'left',whiteSpace:'nowrap',fontFamily:LB_SERIF,fontSize:18,color:BK.ink}}>{t('At the piano', '피아노 앞에서')}</span><span style={{textAlign:'right',paddingRight:6}}>{t('Lesson', '레슨')}</span>{[1, 2, 3, 4, 5, 6].map(n => <span key={n}>{n}</span>)}</div>
        {checksRows.map(([a, vb, txt], i) => (
          <div key={i} style={{display:'grid',gridTemplateColumns:'96px 1fr repeat(6, 28px)',gap:7,alignItems:'center',border:'1px solid #ece6d8',borderRadius:10,padding:'3px 8px'}}>
            <div style={{display:'flex',justifyContent:'center'}}><PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/></div>
            <div style={{fontSize:14,fontWeight:800,color:BK.ink}}>{txt}</div>
            {[1, 2, 3, 4, 5, 6].map(n => <span key={n} style={{width:25,height:25,border:'1.5px solid ' + BK.line,borderRadius:7,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center'}}><BkStarG size={12} fill="#ece6d8"/></span>)}
          </div>))}
      </div>} live={<FiveChecks376 storeKey="pb_five_fs_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
      <LbOnly print><FsPaperCheck/></LbOnly>""", 'ch2 checks + paper')
# chapter 1
rep("""    <LbPage key="7" no={7} chId={ch} kicker={t('Step 5', '5단계')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('At the start of each lesson, the student says the five checks out loud while doing them; you only correct. When all five are easy, do the Chapter check-up in the Workbook.'""",
    """    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('At the start of each lesson, the student says the five checks out loud while doing them; you only correct. When all five are easy, do the paper part on the same page.'""", 'ch1 checks kicker')
rep("""      <LbSay>{t('Before you play, every time. Give yourself a star for each check in each lesson.', '칠 때마다, 치기 전에 먼저. 레슨마다 확인 하나에 별 하나씩 칠해요.')}</LbSay>""",
    """      <LbSay>{t('At the piano: before you play, every time -- give yourself a star for each check in each lesson. On paper: do the check-up below.', '피아노 앞에서: 칠 때마다, 치기 전에 먼저 -- 레슨마다 확인 하나에 별 하나씩. 종이에서: 아래 점검을 풀어요.')}</LbSay>""", 'ch1 checks words')
rep("""      <div style={{display:'flex',flexDirection:'column',gap:9,flex:'1 1 auto'}}>
        <div style={{display:'grid',gridTemplateColumns:scr ? '64px 1fr repeat(6, 26px)' : '150px 1fr repeat(6, 34px)',gap:scr ? 4 : 8,alignItems:'end',fontSize:11,fontWeight:800,color:BK.muted,textAlign:'center'}}><span/>""",
    """      <div style={{display:'flex',flexDirection:'column',gap:5}}>
        <div style={{display:'grid',gridTemplateColumns:scr ? '64px 1fr repeat(6, 26px)' : '96px 1fr repeat(6, 28px)',gap:scr ? 4 : 7,alignItems:'end',fontSize:10.5,fontWeight:800,color:BK.muted,textAlign:'center'}}><span style={{textAlign:'left',whiteSpace:'nowrap',fontFamily:LB_SERIF,fontSize:18,color:BK.ink}}>{t('At the piano', '피아노 앞에서')}</span>""", 'ch1 checks head')
rep("""          <div key={i} style={{display:'grid',gridTemplateColumns:scr ? '64px 1fr repeat(6, 26px)' : '150px 1fr repeat(6, 34px)',gap:scr ? 4 : 8,alignItems:'center',border:'1px solid #ece6d8',borderRadius:12,padding:scr ? '4px 6px' : '4px 8px',flex:'1 1 auto'}""",
    """          <div key={i} style={{display:'grid',gridTemplateColumns:scr ? '64px 1fr repeat(6, 26px)' : '96px 1fr repeat(6, 28px)',gap:scr ? 4 : 7,alignItems:'center',border:'1px solid #ece6d8',borderRadius:10,padding:scr ? '4px 6px' : '2px 8px'}""", 'ch1 checks rows')
rep("""<PbArt name={a} h={scr ? (a === 'chk-hand' ? 40 : 52) : a === 'chk-hand' ? 86 : 108}/></div>
            <div style={{fontSize:scr ? 13 : 15.5,fontWeight:800,color:BK.ink}}>{txt}</div>
            {[1, 2, 3, 4, 5, 6].map(n => <span key={n} style={{width:scr ? 24 : 30,height:scr ? 24 : 30,""",
    """<PbArt name={a} h={scr ? (a === 'chk-hand' ? 40 : 52) : a === 'chk-hand' ? 40 : 52}/></div>
            <div style={{fontSize:scr ? 13 : 14,fontWeight:800,color:BK.ink}}>{txt}</div>
            {[1, 2, 3, 4, 5, 6].map(n => <span key={n} style={{width:scr ? 24 : 25,height:scr ? 24 : 25,""", 'ch1 checks sizes')
rep("""      <LbRemember>{t('Check your posture before every practice.', '연습할 때마다 먼저 자세를 확인해요.')}</LbRemember>
    </LbPage>,
  ];
}
function PostureLessonBook()""", """      <LbOnly print><PhPaperCheck/></LbOnly>
    </LbPage>,
  ];
}
function PostureLessonBook()""", 'ch1 paper part')

# the two paper parts (the old Workbook check-ups, one page with the checks)
rep("""function FirstStepsTeacher() {""", """// Phase 394: chapter 2's check-up on paper, in the order of the five checks (houses, 3 and 4, names, middle C, Hot Cross Buns)
function FsPaperCheck() {
  const W = useMemo(() => fsWorkbook(), [LANG]);
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column'}}>
    <LbPaperHead/>
    {bkSec('A', 'Write S under each small house and B under each big house.')}
    <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 10px'}}><PaperKeys start="C" whites={14} w={30} h={56} boxes={[1, 4, 8, 11]}/></div>
    {bkSec('B', 'Whose house is the dotted white key? Write S (small) or B (big).')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.wh.map((w, i) => <BkCell key={i} n={5 + i}><div style={{display:'flex',alignItems:'center',gap:8,padding:'11px 4px 3px'}}><div style={{flex:1}}><PaperKeys start="C" whites={7} w={16} h={40} roofs dots={[w]}/></div>{bkBox(28, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Name the dotted key. Write its letter.')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.ln.map((w, i) => <BkCell key={i} n={9 + i}><div style={{display:'flex',alignItems:'center',gap:8,padding:'11px 4px 3px'}}><div style={{flex:1}}><PaperKeys start="C" whites={10} w={12} h={38} dots={[w]}/></div>{bkBox(28, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Middle C: count the small houses from the bottom.')}
    <div style={{display:'flex',gap:22,alignItems:'center',fontSize:13,color:BK.ink,padding:'2px 4px'}}><span><b style={{color:BK.coral}}>13</b> Middle C is the left door of small house number {bkBox(32, 24)}</span><span><b style={{color:BK.coral}}>14</b> A piano has {bkBox(44, 24)} keys.</span></div>
    {bkSec('E', 'Hot Cross Buns: which finger plays the dotted key?')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.sg.map((f, i) => <BkCell key={i} n={15 + i}><div style={{display:'flex',alignItems:'center',gap:8,padding:'11px 4px 3px'}}><div style={{flex:1}}><PaperKeys start="C" whites={7} w={20} h={40} blackDots={[f]}/></div>{bkBox(28, 24)}</div></BkCell>)}</BkGrid>
  </div>;
}
function FirstStepsTeacher() {""", 'FsPaperCheck')
rep("""function PostureTeacher() {""", """// Phase 394: chapter 1's check-up on paper, under the five checks
function PhPaperCheck() {
  const W = useMemo(() => phWorkbook(), [LANG]);
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column'}}>
    <LbPaperHead/>
    {bkSec('A', 'A good set-up? Circle the tick or the cross.')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.st.map(([id, , ok], i) => <PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={50}/>)}</BkGrid>
    {bkSec('B', 'A good hand shape? Circle the tick or the cross.')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.hs.map(([id, , ok], i) => <PhPic key={id} art={'q-hand-' + id} ok={ok} n={i + 5} h={40}/>)}</BkGrid>
    {bkSec('C', 'Left or right hand? Write L or R.  D  Which finger is coloured?')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.fn.map((f, i) => <BkCell key={i} n={(9 + i) + ' · ' + (13 + i)}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,padding:'11px 4px 3px'}}>
      <PbArt name={'q-fingers-' + W.chk.lr[i] + '-plain'} lit={f} h={54}/>
      <div style={{display:'grid',gap:5,fontSize:10,fontWeight:900,color:BK.coral}}><span>C {bkBox(28, 22)}</span><span>D {bkBox(28, 22)}</span></div>
    </div></BkCell>)}</BkGrid>
    {bkSec('E', 'Finger walks: write the missing number.')}
    <BkGrid cols={4} gap="5px 10px">{PH_FILL_CHK.map((seq, i) => <BkCell key={i} n={17 + i}><div style={{display:'flex',justifyContent:'center',padding:'12px 2px 2px'}}><PhCircles seq={seq} size={21}/></div></BkCell>)}</BkGrid>
  </div>;
}
function PostureTeacher() {""", 'PhPaperCheck')

# ── the Workbooks: the step pages only; printed alone, they carry the shared opener and check-up pages ──
rep("""const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook };""",
    """const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook };
// Phase 394: chapters whose first and last pages are shared by both books
const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages };
function lbFramed(id, pages, startNo) {
  const lb = LB_PAGE_FNS[id](false);
  return [React.cloneElement(lb[0], { key: 'frame-open', no: startNo }), ...pages, React.cloneElement(lb[lb.length - 1], { key: 'frame-check', no: startNo + 1 + pages.length })];
}""", 'LB_PAGE_FNS')
for fn, cid, steps_anchor in [('FirstStepsWorkbook', 'first-steps', '  // 2 (faces "Small house, big house")'), ('PostureWorkbook', 'posture-hands', '  // 2 (faces "Sit at the piano")')]:
    rep("function %s({ startNo = 1 }) {" % fn, "function %s({ startNo = 1, frames = true }) {" % fn, fn + ' frames')
    rep("""  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + pages.length} chId="%s">{content}</WbPage>);""" % cid,
        """  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="%s">{content}</WbPage>);""" % cid, fn + ' numbering')
    a = s.index("function %s(" % fn)
    i = s.index("  // 1 (faces the Lesson Book opener): the map", a); j = s.index(steps_anchor, a)
    s = s[:i] + "  // (the map is the Lesson Book's opener now -- one page for both books, Phase 394)\n\n" + s[j:]; done.append(fn + ' map out')
    i = s.index('  // 7 (faces "My five checks"): the chapter check-up', a); j = s.index("  return <>{pages}</>;", i)
    s = s[:i] + "  // (the check-up is on the Lesson Book's last page now, under My five checks -- Phase 394)\n  return <>{frames ? lbFramed('%s', pages, startNo) : pages}</>;" % cid + s[j + len("  return <>{pages}</>;"):]
    done.append(fn + ' check-up out')
rep("""function SpreadBook({ id }) {
  const lesson = LESSON_BOOKS[id](), work = WORKBOOKS[id]({ startNo: 1 });
  const lp = React.Children.toArray(lesson.props.children), wp = React.Children.toArray(work.props.children);
  const blank = (k) => <section key={'blank' + k} className="bk-page" data-spread-blank/>;""",
    """function SpreadBook({ id }) {
  const framed = !!LB_PAGE_FNS[id];
  const lesson = LESSON_BOOKS[id](), work = WORKBOOKS[id]({ startNo: 1, frames: false });
  const lp = React.Children.toArray(lesson.props.children), wp = React.Children.toArray(work.props.children);
  const blank = (k) => <section key={'blank' + k} className="bk-page" data-spread-blank/>;
  if (framed) {   // Phase 394: the opener is page 1 (a right-hand page), each lesson page faces its workbook page, the check-up closes
    const out = [lp[0]];
    for (let k = 1; k < lp.length - 1; k++) out.push(lp[k], wp[k - 1] || blank('w' + k));
    out.push(lp[lp.length - 1]);
    return <>{out}</>;
  }""", 'SpreadBook framed')

# the Teacher copies: page 7 is the check-up under the five checks
rep("""    <TcBlock page={7} title="Check-up" goBack={fsConcepts()} answers={<>{tcAns('A', ['S B S B'])}{tcAns('B', W.chk.hl.map(hi))}{tcAns('C', W.chk.wh.map(w => fsHouse(w) + ' (' + fsLetter(w) + ')'))}{tcAns('D', W.chk.ln.map(fsLetter))}{tcAns('E', W.chk.sg.map(f => String(finger[f])))}{tcAns('F', W.chk.lg.map(first => first ? 'top' : 'bottom'))}""",
    """    <TcBlock page={7} title="My five checks · the check-up on paper" answers={<>{tcAns('A', ['S B S B'])}{tcAns('B', W.chk.wh.map(w => fsHouse(w) + ' (' + fsLetter(w) + ')'))}{tcAns('C', W.chk.ln.map(fsLetter))}{tcAns('D', ['4 (the 4th small house)', '88'])}{tcAns('E', W.chk.sg.map(f => String(finger[f])))}""", 'tc ch2 p7 answers')
rep("""This chapter's five checks are shown on the keyboard (find the houses, say 3 and 4, name any white key, find middle C, Hot Cross Buns legato); you only correct. Score each concept on its own (4 marks each, pass 3+).</div></>}/>""",
    """This chapter's five checks are shown on the keyboard (find the houses, say 3 and 4, name any white key, find middle C, Hot Cross Buns legato); you only correct. The paper part follows the same order: score each part on its own (A, B, C, E: 4 marks, pass 3+; D: 2 marks). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5 · E p.6.</div></>}/>""", 'tc ch2 p7 scoring')
rep("""    <TcBlock page={7} title="Check-up" goBack={phConcepts()} answers={<>{tcAns('A', W.chk.st.map(([, , ok]) => yn(ok)))}{tcAns('B', W.chk.ar.map(([, ok]) => ok ? 'yes' : 'no'))}{tcAns('C', W.chk.hs.map(([, , ok]) => yn(ok)))}{tcAns('D', W.chk.lr)}{tcAns('E', W.chk.fn)}{tcAns('F', PH_FILL_CHK.map(fill))}""",
    """    <TcBlock page={7} title="My five checks · the check-up on paper" answers={<>{tcAns('A', W.chk.st.map(([, , ok]) => yn(ok)))}{tcAns('B', W.chk.hs.map(([, , ok]) => yn(ok)))}{tcAns('C', W.chk.lr)}{tcAns('D', W.chk.fn)}{tcAns('E', PH_FILL_CHK.map(fill))}""", 'tc ch1 p7 answers')
rep("""At the start of each lesson the student says the five checks out loud while doing them; you only correct. Score each concept on its own (4 marks each, pass 3+). Then check the posture at the piano, not just on paper.</div></>}/>""",
    """At the start of each lesson the student says the five checks out loud while doing them; you only correct. Score each paper part on its own (4 marks each, pass 3+). Not passed? Go back to that step's page: A p.2 · B p.4 · C and D p.5 · E p.6. Then check the posture at the piano, not just on paper.</div></>}/>""", 'tc ch1 p7 scoring')

# ── (3) Turtle or bird: sounds you can make, not sizes ──
rep("""    drum: <g><ellipse cx="30" cy="22" rx="18" ry="7" fill="#fff" {...ART_SW}/>""",
    """    lion: <g><path d={Array.from({ length: 28 }, (_, i) => { const a = i * Math.PI / 14 - Math.PI / 2, r = i % 2 ? 18 : 24; return (i ? 'L' : 'M') + (32 + r * Math.cos(a)).toFixed(1) + ' ' + (30 + r * Math.sin(a)).toFixed(1); }).join(' ') + ' Z'} {...ART_SW} fill="#fbe9e2"/><circle cx="22" cy="19" r="4" {...ART_SW} fill="#fff"/><circle cx="42" cy="19" r="4" {...ART_SW} fill="#fff"/><circle cx="32" cy="31" r="13.5" {...ART_SW} fill="#fff"/><circle cx="27" cy="28" r="1.5" fill={BK.ink}/><circle cx="37" cy="28" r="1.5" fill={BK.ink}/><path d="M29.5 32.5 L34.5 32.5 L32 35.5 Z" fill={BK.ink}/><ellipse cx="32" cy="39.5" rx="4.2" ry="3.4" fill={BK.ink}/></g>,
    cow: <g><ellipse cx="15" cy="21" rx="6.5" ry="3.2" transform="rotate(-18 15 21)" {...ART_SW} fill="#fff"/><ellipse cx="49" cy="21" rx="6.5" ry="3.2" transform="rotate(18 49 21)" {...ART_SW} fill="#fff"/><path d="M25 13 q-2 -7 -8 -8 M39 13 q2 -7 8 -8" {...ART_SW}/><ellipse cx="32" cy="27" rx="13" ry="15" {...ART_SW} fill="#fff"/><path d="M27 16 q5 -4 9 0 q-1 5 -5 5 q-4 -1 -4 -5 Z" fill={BK.ink}/><circle cx="27" cy="26" r="1.5" fill={BK.ink}/><circle cx="37" cy="26" r="1.5" fill={BK.ink}/><ellipse cx="32" cy="39" rx="10" ry="6.5" {...ART_SW} fill="#fbe3da"/><circle cx="28.5" cy="39" r="1.3" fill={BK.ink}/><circle cx="35.5" cy="39" r="1.3" fill={BK.ink}/></g>,
    chick: <g><ellipse cx="29" cy="37" rx="15" ry="13" {...ART_SW} fill="#fff"/><circle cx="39" cy="21" r="9" {...ART_SW} fill="#fff"/><path d="M47 19 L53 22 L47 25 Z" fill={BK.coral}/><circle cx="41" cy="19.5" r="1.5" fill={BK.ink}/><path d="M37 12.5 q0 -4 4 -4.5" {...ART_SW}/><path d="M20 35 q6 7 12 0" {...ART_SW}/><path d="M25 49.5 L23 55 M25 49.5 L27 55 M33 49.5 L31 55 M33 49.5 L35 55" stroke={BK.coral} strokeWidth="1.6" strokeLinecap="round"/></g>,
    ship: <g><path d="M4 49 q6 -4 12 0 t12 0 t12 0 t12 0 t12 0" {...ART_SW}/><path d="M9 36 L55 36 L49 46 L15 46 Z" {...ART_SW} fill="#fff"/><rect x="17" y="26" width="22" height="10" {...ART_SW} fill="#fff"/><circle cx="23" cy="31" r="1.6" fill={BK.ink}/><circle cx="29" cy="31" r="1.6" fill={BK.ink}/><circle cx="35" cy="31" r="1.6" fill={BK.ink}/><rect x="42" y="17" width="7" height="19" {...ART_SW} fill="#fff"/><rect x="42" y="21" width="7" height="3.5" fill={BK.coral}/><path d="M47 12 q4 -5 9 -2 q3 -5 7 -1" {...ART_SW}/></g>,
    drum: <g><ellipse cx="30" cy="22" rx="18" ry="7" fill="#fff" {...ART_SW}/>""", 'new sound icons')
a = s.index("""    <Part kind="play" title="Turtle or bird?" how=""")
b = s.index("    </Part>", a) + len("    </Part>")
s = s[:a] + """    <Part kind="play" title="Turtle or bird?" how="Make each sound with your voice first. In each pair, one is lower and one is higher: draw a line from the lower one to the turtle and from the higher one to the bird -- then find both sounds on the piano!">
      <div style={{display:'grid',gridTemplateColumns:'86px 1fr 86px',gap:10,alignItems:'center',flex:1}}>
        <div style={{display:'grid',justifyItems:'center',gap:2,fontSize:12,fontWeight:800,color:BK.ink}}>{turtleIcon(66)}low</div>
        <div style={{display:'grid',gap:8}}>{[[['chick', 'a chick', 'cheep cheep!'], ['cow', 'a cow', 'moooo']], [['lion', 'a lion', 'ROAR'], ['mouse', 'a mouse', 'squeak!']], [['whistle', 'a whistle', 'tweeeet!'], ['ship', 'a ship\\u2019s horn', 'booooo']]].map((pair, r) => (
          <div key={r} data-pair={r + 1} style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:14,background:BK.soft,borderRadius:10,padding:'4px 8px'}}>{pair.map(([k, lab, snd]) => <div key={k} style={{background:'#fff',border:'1px solid #ece6d8',borderRadius:8,display:'grid',gridTemplateColumns:'54px 1fr',alignItems:'center',gap:8,padding:'4px 10px',height:70}}><SoundIcon kind={k} size={52}/><div style={{lineHeight:1.25}}><div style={{fontSize:12,color:BK.ink,fontWeight:700}}>{lab}</div><div style={{fontSize:14,color:BK.coral,fontWeight:900,fontStyle:'italic'}}>{snd}</div></div></div>)}</div>))}</div>
        <div style={{display:'grid',justifyItems:'center',gap:2,fontSize:12,fontWeight:800,color:BK.coral}}>{birdIcon(66)}high</div>
      </div>
      <div style={{textAlign:'center',fontSize:12.5,color:BK.ink,marginTop:6}}>Listen to your own voice: a deep <b>moooo</b> sits <b>low</b> · a squeaky <b style={{color:BK.coral}}>cheep</b> sits <b style={{color:BK.coral}}>high</b></div>
    </Part>""" + s[b:]
done.append('turtle or bird: voices')
rep("{tcAns('PLAY', ['turtle (lower): the elephant, the big drum, the big bell', 'bird (higher): the mouse, the little drum, the little bell'])}",
    "{tcAns('PLAY', ['turtle (lower): the cow, the lion, the ship\\u2019s horn', 'bird (higher): the chick, the mouse, the whistle'])}", 'tc turtle or bird')

open(p, 'w', encoding='utf-8').write(s)
print('\n'.join('ok: ' + d for d in done))
print('PATCH 394 DONE')
