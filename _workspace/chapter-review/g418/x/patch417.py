#!/usr/bin/env python3
# Phase 417: a fresh-eyes review of every Workbook page of chapters 1-4 against the house rules (one reviewer that had
# not seen the work), and its findings fixed before Sohyun sees them:
#   solo (no one needed on paper), set (no choosing), nothing twice (no re-teaching), big enough to write in,
#   and four real mistakes: chapter 2's 'just left of the 4th small house' (that is B -- middle C is its LEFT DOOR),
#   chapter 3's duplicate number 4, chapter 4's check-up item 7 (line 1 to line 3 is neither a step nor a skip),
#   and chapter 4's F road that only touched at the corners and did not start at the King.
#   python3 patch417.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# ── shared: answer boxes UNDER a paper keyboard, centred under given keys (i may be fractional: between keys) ──
rep("""// A row of letter boxes; given[i] = letter printed, ex[i] = worked answer in coral, else empty.""",
    """// Phase 417: answer boxes under a paper keyboard (big enough to write in), centred under key i (i can be x.5)
function KeyBoxRow({ whites, w, idx, nos, bw = 42, bh = 38 }) {
  const W = whites * w + 4;
  return <div style={{position:'relative',height:bh + 16,marginTop:4}}>{idx.map(i => <span key={i} style={{position:'absolute',left:((i + 0.5) * w + 2) / W * 100 + '%',transform:'translateX(-50%)',top:0,display:'flex',flexDirection:'column',alignItems:'center'}}>
    <span style={{width:bw,height:bh,border:'1.5px solid ' + BK.ink,borderRadius:7,background:'#fff'}}/>
    {nos && nos[i] != null && <span style={{fontSize:10.5,fontWeight:900,color:BK.coral,marginTop:2}}>{nos[i]}</span>}</span>)}</div>;
}
// A row of letter boxes; given[i] = letter printed, ex[i] = worked answer in coral, else empty.""", 'KeyBoxRow')

# ══ Chapter 1 ══
# p2: the answers are not all crosses (the good set-up sits third), the example is a fault
for a in ["[PH_SIT[0], PH_SIT[1], PH_SIT[4], PH_SIT[2]].map(([id, , ok], i) => <PhPic", "tcAns('TRY IT', [PH_SIT[0], PH_SIT[1], PH_SIT[4], PH_SIT[2]]"]:
    rep(a, a.replace('[PH_SIT[0], PH_SIT[1], PH_SIT[4], PH_SIT[2]]', '[PH_SIT[1], PH_SIT[4], PH_SIT[0], PH_SIT[2]]'), 'ch1 p2 order')
rep("""how="Before you practise, set up and tick each one. Ask someone at home to check, or use a mirror.\"""",
    """how="Before you practise, set up and tick each one. Check yourself in a mirror.\"""", 'ch1 p2 solo')
# p3: the week's log does not print the order the TRY IT asks for
rep("""    <Part kind="home" title="My warm-ups this week" how="Do the six in order before you practise. Tick a box for each one you did.">
      <PhLog rows={PH_WARMUPS.map(([, n], i) => (i + 1) + '  ' + n)} days={7} label={150}/>""",
    """    <Part kind="home" title="My warm-ups this week" how="Before you practise, do all six in the order you found above. Tick each one you did.">
      <PhLog rows={PH_WARMUPS.map(([, n]) => n).sort()} days={7} label={150}/>""", 'ch1 p3 log')
# p4: no listener needed; draw with one hand, hold the ball in the other
rep("""how="Circle the tick for the good hand shape and the cross for a fault. Then say what is wrong.\"""",
    """how="Circle the tick for the good hand shape and the cross for a fault.\"""", 'ch1 p4 solo')
rep("""how="Hold a small ball (or a mandarin) in your right hand, fingers round it.""", """how="Hold a small ball (or a mandarin) in the hand you don't draw with, fingers round it.""", 'ch1 p4 ball hand')
# p5: the finger quiz in one row, so the hand-tracing boxes are big enough for a child's hand
rep("""      <BkGrid cols={3} gap="8px 12px">{W.fingers.map(([h, f], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:14,padding:'12px 2px 4px'}}>
        <PbArt name={'q-fingers-' + h} lit={f} h={112}/>{nvBox(i === 0, String(f), 42, 36)}""",
    """      <BkGrid cols={6} gap="6px 8px">{W.fingers.map(([h, f], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6,padding:'14px 2px 6px'}}>
        <PbArt name={'q-fingers-' + h} lit={f} h={78}/>{nvBox(i === 0, String(f), 40, 34)}""", 'ch1 p5 quiz one row')
rep("""      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,flex:1,minHeight:340}}>{['Left hand', 'Right hand'].map(l =>""",
    """      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,flex:1,minHeight:470}}>{['Left hand', 'Right hand'].map(l =>""", 'ch1 p5 trace taller')
# check-up E: '2 3 2 _' had two right answers -- now a plain walk up
rep("""const PH_FILL_CHK = [['1', '2', '3', '?4', '5'], ['5', '4', '?3', '2', '1'], ['2', '3', '2', '?3'], ['1', '?2', '3', '2', '1']];""",
    """const PH_FILL_CHK = [['1', '2', '3', '?4', '5'], ['5', '4', '?3', '2', '1'], ['2', '3', '4', '?5'], ['1', '?2', '3', '2', '1']];   // Phase 417: no item with two right answers""", 'ch1 chk E')

# ══ Chapter 2 ══
# p2: no lines across the cards -- circle the lower, star the higher
rep("""<Part kind="play" title="Turtle or bird?" how="Make each sound with your voice first. In each pair, one is lower and one is higher: draw a line from the lower one to the turtle and from the higher one to the bird -- then find both sounds on the piano!">""",
    """<Part kind="play" title="Turtle or bird?" how="Make each sound with your voice first. In each pair, circle the lower one (the turtle's) and draw a star by the higher one (the bird's) -- then find both sounds on the piano!">""", 'ch2 p2 play')
# p3: draw the faces; big house outlines to draw in (no colouring of tiny roofs)
rep("""how="Draw one smiley face for each white key: 3 faces in the small house, 4 faces in the big house. Then colour the small house's roof coral and the big house's roof navy.\"""",
    """how="Draw one smiley face for each white key: 3 faces in the small house, 4 faces in the big house.\"""", 'ch2 p3 play')
rep("""<svg viewBox="0 0 120 30" style={{width:n === 2 ? 70 : 96}}>""", """<svg viewBox="0 0 120 30" style={{width:n === 2 ? 120 : 164}}>""", 'ch2 p3 roofs bigger')
rep("""{tcAns('PLAY', ['3 faces in the small house, 4 in the big house -- one per white key', 'small roof coral, big roof navy'])}""",
    """{tcAns('PLAY', ['3 faces in the small house, 4 in the big house -- one per white key'])}""", 'ch2 tc p3')
# p4: the count is theirs to write; circle the lighthouse key (too narrow to draw on); middle C = the LEFT DOOR
rep("""<span>Small houses: {bkHand('7', 36, 28)}</span>""", """<span style={{display:'inline-flex',alignItems:'center',gap:8}}>Small houses: {bkBox(44, 36)}</span>""", 'ch2 p4 count')
rep("""        <div>2 · Draw a little lighthouse on the lonely black key at the very bottom, by the sea.</div>
        <div>3 · Draw a star on <b>middle C</b> -- the white key just left of the 4th small house.</div>""",
    """        <div>2 · Circle the lonely black key at the very bottom, by the sea -- that is the lighthouse.</div>
        <div>3 · Draw a star on <b>middle C</b> -- the left door of the 4th small house.</div>""", 'ch2 p4 tasks')
rep("""'the lighthouse on the 2nd key from the bottom (A♯0/B♭0)'""", """'the lighthouse circled: the 2nd key from the bottom (A♯0/B♭0)'""", 'ch2 tc lighthouse')
rep("""say="“Count the small houses to 4. Middle C is the door just to its left -- the ground. Up is the sky, down is the sea.”\"""",
    """say="“Count the small houses to 4. Middle C is its left door -- the ground. Up is the sky, down is the sea.”\"""", 'ch2 tc say')
rep("""t('I can find middle C (just left of the 4th small house)', '가운데 도를 찾을 수 있어요 (4번째 작은 집 바로 왼쪽)')""",
    """t('I can find middle C (the left door of the 4th small house)', '가운데 도를 찾을 수 있어요 (4번째 작은 집의 왼쪽 문)')""", 'ch2 five checks row')
# p5: the legato pictures become a question (no re-teaching): which one is legato?
rep("""<Part kind="play" title="The relay baton: legato" how="Hold the key until the next one plays -- the moment it sounds, let the old one go. Trace the dotted path from pot to pot in one smooth line -- don't lift your pencil, no gaps: that's legato!">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16,marginBottom:4}}>
        <div style={{border:'1px solid #ece6d8',background:BK.soft,borderRadius:8,padding:'4px 10px'}}><Footsteps smooth/><div style={{fontSize:11.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>Legato: one foot is always on the ground.</div></div>
        <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'4px 10px'}}><Footsteps smooth={false}/><div style={{fontSize:11.5,fontWeight:800,color:BK.muted,textAlign:'center'}}>Not legato: a gap between every step.</div></div>
      </div>""",
    """<Part kind="play" title="The relay baton: legato" how="Which walk is legato, A or B? Circle it. Then trace the dotted path from pot to pot in one smooth line -- don't lift your pencil.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:16,marginBottom:4}}>
        {[['A', false], ['B', true]].map(([l, sm]) => <div key={l} style={{border:'1px solid #ece6d8',borderRadius:8,padding:'4px 10px',position:'relative'}}><span style={{position:'absolute',left:10,top:6,width:26,height:26,borderRadius:13,border:'1.5px solid ' + BK.ink,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14,fontWeight:900,color:BK.ink}}>{l}</span><Footsteps smooth={sm}/></div>)}
      </div>""", 'ch2 p5 legato question')
rep("""<div style={{fontSize:12,color:BK.ink}}>PLAY: one unbroken line through all six pots. Then play the roof walk legato.</div>""",
    """<div style={{fontSize:12,color:BK.ink}}>PLAY: B is legato (one foot always on the ground); one unbroken line through all six pots. Then play the roof walk legato.</div>""", 'ch2 tc p5')
# check-up A: numbered boxes under the keyboard, one under the middle of each house
rep("""<div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'4px 10px'}}><PaperKeys start="C" whites={14} w={42} h={80} boxes={[1, 4, 8, 11]}/></div>""",
    """<div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'4px 10px'}}><PaperKeys start="C" whites={14} w={42} h={64}/><KeyBoxRow whites={14} w={42} idx={[1, 4.5, 8, 11.5]} nos={{ 1: 1, 4.5: 2, 8: 3, 11.5: 4 }}/></div>""", 'ch2 chk A boxes')

rep("""<PaperKeys start="C" whites={10} w={30} h={52} dots={pp}/>""", """<PaperKeys start="C" whites={10} w={30} h={46} dots={pp}/>""", 'ch2 chk B room')
rep("""<PaperKeys start="C" whites={7} w={30} h={54} roofs dots={[w]}/></div>{bkBox(36, 30)}""", """<PaperKeys start="C" whites={7} w={30} h={48} roofs dots={[w]}/></div>{bkBox(36, 30)}""", 'ch2 chk C room')
rep("""<PaperKeys start="C" whites={7} w={30} h={54} blackDots={[f]}/>""", """<PaperKeys start="C" whites={7} w={30} h={48} blackDots={[f]}/>""", 'ch2 chk E room')

# ══ Chapter 3 ══
# p2: the dotted keys, one keyboard to a line, with real answer boxes under the keys; the others give back the room
rep("""      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12}}>{W.s1.kb.map((kb, i) => <KeysCell key={i} n={i === 0 ? '1-4' : '5-8'}><PaperKeys start={kb.start} whites={10} w={30} h={132} dots={kb.dots} boxes={kb.dots} boxNos={Object.fromEntries([...kb.dots].sort((a, b) => a - b).map((d, j) => [d, 4 * i + j + 1]))}/></KeysCell>)}</div>""",
    """      <div style={{display:'grid',gap:10}}>{W.s1.kb.map((kb, i) => <KeysCell key={i} n={i === 0 ? '1-4' : '5-8'} pad="12px 10px 2px"><PaperKeys start={kb.start} whites={10} w={30} h={40} dots={kb.dots}/><KeyBoxRow whites={10} w={30} bh={34} idx={kb.dots} nos={Object.fromEntries([...kb.dots].sort((a, b) => a - b).map((d, j) => [d, 4 * i + j + 1]))}/></KeysCell>)}</div>""", 'ch3 p2 dotted keys')
rep("""<KeysCell ex><PaperKeys start="E" whites={15} w={40} h={150} boxes={cf}""", """<KeysCell ex><PaperKeys start="E" whites={15} w={40} h={96} boxes={cf}""", 'ch3 p2 C and F')
rep("""<KeyScene start="C" whites={14} w={40} h={200} houses={false} lost={['D', 'G', 'B', 'C', 'A']}/>""", """<KeyScene start="C" whites={14} w={40} h={96} houses={false} lost={['D', 'G', 'B', 'C', 'A']}/>""", 'ch3 p2 lost letters')
# p4: 'in my head' -- each day's starting letter is printed (set, not chosen)
rep("""      <div style={{marginTop:10,fontSize:13,color:BK.ink}}><b>In my head, no piano:</b> say the letters backwards, from a different letter each day. Tick a day:</div>
      <div style={{display:'flex',justifyContent:'space-between',marginTop:6,padding:'0 4px'}}>{BK_DAYS.map(d => <span key={d} style={{display:'inline-flex',alignItems:'center',gap:5,fontSize:11.5,color:BK.muted,fontWeight:700}}>{d}<span style={{width:22,height:22,border:'1.5px solid ' + BK.line,borderRadius:5}}/></span>)}</div>""",
    """      <div style={{marginTop:10,fontSize:13,color:BK.ink}}><b>In my head, no piano:</b> say the letters backwards, all seven, starting from the day's letter. Tick the day:</div>
      <div style={{display:'flex',justifyContent:'space-between',marginTop:6,padding:'0 4px'}}>{BK_DAYS.map((d, j) => <span key={d} style={{display:'inline-flex',alignItems:'center',gap:5,fontSize:11.5,color:BK.muted,fontWeight:700}}>{d} <b style={{fontSize:14,color:BK.coral}}>{NN_HEAD_DAYS[j]}</b><span style={{width:22,height:22,border:'1.5px solid ' + BK.line,borderRadius:5}}/></span>)}</div>""", 'ch3 p4 days')
rep("""// Phase 413: the word search's bonus is set, not free -- two riddles in music letters""",
    """// Phase 417: 'in my head' starts from a set letter each day (Mon..Sun)
const NN_HEAD_DAYS = ['G', 'C', 'E', 'A', 'D', 'B', 'F'];
// Phase 413: the word search's bonus is set, not free -- two riddles in music letters""", 'head days const')
# p5: numbers run on (1-4, 5-7, 8-13) and the how-line says it in order
rep("""    <Part kind="home" title="Name it at a glance" how="First the last three: a dot on their keys. Then write the letter of each dotted key below -- don't count from C, think who lives there.">
      <BkGrid cols={4} gap="8px 10px">{W.gl.home.map((L, i) => <ResCell key={L} L={L} n={i + 4}/>)}</BkGrid>
      <div style={{marginTop:8}}><KeysCell n="7-12">""",
    """    <Part kind="home" title="Name it at a glance" how="5-7: put a dot on the key where each one lives. 8-13: write the letter of each dotted key -- don't count from C, think who lives there.">
      <BkGrid cols={4} gap="8px 10px">{W.gl.home.map((L, i) => <ResCell key={L} L={L} n={i + 5}/>)}</BkGrid>
      <div style={{marginTop:8}}><KeysCell n="8-13">""", 'ch3 p5 numbers')
rep("""dots={W.gl.kb} boxes={W.gl.kb} boxNos={Object.fromEntries([...W.gl.kb].sort((a, b) => a - b).map((d, j) => [d, j + 7]))}/>""",
    """dots={W.gl.kb} boxes={W.gl.kb} boxNos={Object.fromEntries([...W.gl.kb].sort((a, b) => a - b).map((d, j) => [d, j + 8]))}/>""", 'ch3 p5 box numbers')
# p6: the star from C (the book shows it from A -- so the page does not hand over the answer)
rep("""<Part kind="play" title="Draw the letter star" how="Start on A. Skip a letter each time (A, C, E...) and join them with a ruler as you go. Keep going until you are back on A -- what shape did you make?">""",
    """<Part kind="play" title="Draw the letter star" how="Start on C. Skip a letter each time (C, E, G...) and join them with a ruler as you go. Keep going until you are back on C -- what shape did you make?">""", 'ch3 p6 how')
rep("""        <LetterRing size={310} star start="A"/>""", """        <LetterRing size={310} star start="C"/>""", 'ch3 p6 ring')
rep("""{['A', '', '', '', '', '', '', 'A'].map((l, i) =>""", """{['C', '', '', '', '', '', '', 'C'].map((l, i) =>""", 'ch3 p6 boxes')
rep("""{tcAns('PLAY', ['A C E G B D F A -- a 7-point star'])}""", """{tcAns('PLAY', ['C E G B D F A C -- a 7-point star'])}""", 'ch3 tc star')
rep("""<Part kind="home" title="Your turn" how="Rows 1-2 skip up. Rows 3-4 skip down (C, A, F...).">""", """<Part kind="home" title="Skip on your own" how="Rows 1-2 skip up. Rows 3-4 skip down (C, A, F...).">""", 'ch3 p6 title')
# check-up A: start on F, so the first black keys are a whole big house (a cut group of two looked like a small house)
rep("""<PaperKeys start="G" whites={10} w={30} h={150} dots={W.chk.nm} boxes={W.chk.nm} boxNos={Object.fromEntries([...W.chk.nm].sort((a, b) => a - b).map((d, j) => [d, j + 1]))}/>""",
    """<PaperKeys start="F" whites={11} w={30} h={150} dots={W.chk.nm.map(i => i + 1)} boxes={W.chk.nm.map(i => i + 1)} boxNos={Object.fromEntries([...W.chk.nm].sort((a, b) => a - b).map((d, j) => [d + 1, j + 1]))}/>""", 'ch3 chk A from F')

# ══ Chapter 4 ══
# p2: a real title; the number is part of the answer (set, not 'if you can')
rep("""<Part kind="home" title="Your turn" how="L or S -- and add the number if you can: L3 is line 3, S2 is space 2.">""",
    """<Part kind="home" title="Line or space? On your own" how="Write L or S and its number: L3 is line 3, S2 is space 2. Count from the bottom.">""", 'ch4 p2 title')
# p3: circle the words (no writing 'skip down' in a small box); the four kinds all appear; the higher note is not always first
rep("""    return <SfRow width={width} notes={list.flatMap((it, i) => [{ d: it.a, x: cs[i] - 16 }, { d: it.b, x: cs[i] + 16 }])}
      items={list.map((it, i) => ({ x: cs[i], n: (opts.from || 1) + i, ex: opts.ex && i === 0, ans: sfSSName(it), w: 88, box: opts.box }))}/>; };""",
    """    return <SfRow width={width} notes={list.flatMap((it, i) => [{ d: it.a, x: cs[i] - 16 }, { d: it.b, x: cs[i] + 16 }])}
      items={list.map((it, i) => ({ x: cs[i], n: (opts.from || 1) + i, ex: opts.ex && i === 0, ans: sfSSName(it), w: 88, box: opts.box, choose: opts.box !== false }))}/>; };""", 'ch4 pairs choose')
rep("""    {items.some(it => it.box !== false) && <div style={{position:'relative',height:boxH + 4,marginTop:3}}>{items.map((it, i) => it.box !== false && (it.label != null""",
    """    {items.some(it => it.box !== false) && <div style={{position:'relative',height:items.some(it => it.choose) ? 50 : boxH + 4,marginTop:3}}>{items.map((it, i) => it.box !== false && (it.choose
      ? <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:0,display:'grid',gap:3,justifyItems:'center'}}>{[['step', 'skip'], ['up', 'down']].map((pair, r) => <span key={r} style={{display:'flex',gap:6}}>{pair.map(wd => { const on = it.ex && it.ans.split(' ')[r] === wd; return <span key={wd} style={{fontSize:12.5,fontWeight:800,color:on ? BK.coral : BK.ink,border:'1.5px solid ' + (on ? BK.coral : 'transparent'),borderRadius:12,padding:'0 7px',lineHeight:'19px'}}>{wd}</span>; })}</span>)}</span>
      : it.label != null""", 'SfRow choose')
rep("""<Part kind="together" title="Step or skip? Up or down?" how="From the first note to the second. Write it, like “step up” or “skip down”.">""",
    """<Part kind="together" title="Step or skip? Up or down?" how="From the first note to the second: circle step or skip, and up or down.">""", 'ch4 p3 how')
rep("""    <Part kind="home" title="Your turn">
      {pairs(W.s2.home, 400, { from: 4 })}""", """    <Part kind="home" title="Step or skip? On your own">
      {pairs(W.s2.home, 400, { from: 4 })}""", 'ch4 p3 title')
rep("""  const s3 = withSeed(k('s3'), () => ({ home: run(6, 28, 32) }));""",
    """  // Phase 417: the four kinds of move all appear in 'on your own'; the higher note is first in two pairs, second in two
  const kindPair = (gap) => { for (;;) { const a = rnd(30, 38), b = a + gap; if (b >= 30 && b <= 38) return { a, b }; } };
  Object.assign(s2, withSeed(k('s2b'), () => ({ home: shuffle([1, 2, -1, -2]).map(kindPair), hi: shuffle([1, 2, -1, -2]).map(g => kindPair(g)) })));
  // the Queen's five / the King's five: every note once, then one more (no note three times)
  const five = (lo) => { const a = shuffle([lo, lo + 1, lo + 2, lo + 3, lo + 4]); let x; do { x = rnd(lo, lo + 4); } while (x === a[4]); return [...a, x].map(d => ({ d })); };
  const s3 = withSeed(k('s3b'), () => ({ home: five(28) }));""", 'ch4 s2 s3 data')
rep("""    return { home: run(6, 24, 28), grid, path };""", """    return { home: five(24), grid, path };""", 'ch4 s4 home five')
# p5: the F road is one side-by-side path from the King (left of its first stone) to the castle (right of its last)
rep("""    let r = rnd(0, 3); const path = [[r, 0]];
    for (let c = 1; c < 5; c++) { r = Math.max(0, Math.min(3, r + rnd(-1, 1))); path.push([r, c]); }""",
    """    let r = rnd(0, 3); const path = [[r, 0]];
    for (let c = 1; c < 5; c++) { const nr = Math.max(0, Math.min(3, r + rnd(-1, 1))); if (nr !== r) path.push([nr, c - 1]); r = nr; path.push([r, c]); }""", 'ch4 maze road')
rep("""    <Part kind="play" title="Help the King get home" how="Colour every F. The F stones touching each other make the road from the King to his castle.">
      <div style={{display:'flex',alignItems:'center',gap:8}}>
        <PenArt shapes={sfKing(22, 26, 1)} vb={[4, 0, 36, 48]} style={{width:44,flex:'0 0 auto'}} label="the King"/>
        <div style={{flex:1}}><BkGrid cols={5} gap="6px 6px">{W.s4.grid.flatMap((row, r) => row.map((d, c) => <div key={r + '-' + c} style={{border:'1.2px solid #e2dccb',borderRadius:9,padding:'3px 5px'}}><PaperStaff clef="bass" notes={[{ d }]} width={84} minSpan={[29, 17]}/></div>))}</BkGrid></div>
        <svg viewBox="0 0 36 48" style={{width:44,flex:'0 0 auto'}} aria-label="his castle"><path d="M6 44 V20 H10 V15 H14 V20 H16 V15 H20 V20 H22 V15 H26 V20 H30 V44 Z" fill={BK.soft} stroke={BK.ink} strokeWidth="1.8" strokeLinejoin="round"/><path d="M15 44 V32 Q18 28 21 32 V44" fill={BK.coral} stroke={BK.ink} strokeWidth="1.4"/></svg>
      </div>""",
    """    <Part kind="play" title="Help the King get home" how="Colour every F stone. They join side by side -- up, down or across, never corner to corner -- into one road from the King to his castle.">
      <div style={{display:'grid',gridTemplateColumns:'48px repeat(5, 1fr) 48px',gap:'6px 6px',alignItems:'center'}}>
        {W.s4.grid.flatMap((row, r) => [
          <div key={'k' + r} style={{display:'flex',justifyContent:'center'}}>{r === W.s4.path[0][0] && <PenArt shapes={sfKing(22, 26, 1)} vb={[4, 0, 36, 48]} style={{width:44}} label="the King"/>}</div>,
          ...row.map((d, c) => <div key={r + '-' + c} style={{border:'1.2px solid #e2dccb',borderRadius:9,padding:'3px 5px'}}><PaperStaff clef="bass" notes={[{ d }]} width={84} minSpan={[29, 17]}/></div>),
          <div key={'c' + r} style={{display:'flex',justifyContent:'center'}}>{r === W.s4.path[W.s4.path.length - 1][0] && <svg viewBox="0 0 36 48" style={{width:44}} aria-label="his castle"><path d="M6 44 V20 H10 V15 H14 V20 H16 V15 H20 V20 H22 V15 H26 V20 H30 V44 Z" fill={BK.soft} stroke={BK.ink} strokeWidth="1.8" strokeLinejoin="round"/><path d="M15 44 V32 Q18 28 21 32 V44" fill={BK.coral} stroke={BK.ink} strokeWidth="1.4"/></svg>}</div>])}
      </div>""", 'ch4 maze grid')
# check-up B: circle the words; item 7 is a real skip (E to G), not line 1 to line 3
rep("""    ss: [[31, 32], [34, 32], [30, 34], [37, 36]].map(([a, b]) => ({ a, b })),""", """    ss: [[31, 32], [34, 32], [30, 32], [37, 36]].map(([a, b]) => ({ a, b })),   // Phase 417: item 7 E-G (was E-B, a 5th)""", 'ch4 chk item 7')
rep("""{bkSec('B', 'Step or skip? Up or down? Write it.')}""", """{bkSec('B', 'Step or skip? Up or down? Circle the words.')}""", 'ch4 chk B words')
rep("""items={pcs.map((x, i) => ({ x, n: i + 5, w: 88 }))}/>""", """items={pcs.map((x, i) => ({ x, n: i + 5, w: 88, choose: true }))}/>""", 'ch4 chk B choose')

open(src, 'w', encoding='utf-8').write(s); print('patch417 ok')
