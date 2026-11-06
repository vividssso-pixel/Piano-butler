#!/usr/bin/env python3
# Phase 412: chapter 2's Workbook, bigger keyboards and set tasks (her Phase-410 rule); the check-up fills its page
#   python3 patch412.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# p3: whose house -- two across, bigger keyboards
rep("""      <BkGrid cols={3} gap="8px 12px">{W.s3.map((w, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',gap:10,padding:'14px 4px 4px'}}>
        <div style={{flex:1}}><PaperKeys start="C" whites={7} w={22} h={64} roofs dots={[w]}/></div>{nvBox(i === 0, fsHouse(w), 34, 28)}""",
    """      <BkGrid cols={2} gap="8px 14px">{W.s3.map((w, i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',gap:14,padding:'10px 8px 2px'}}>
        <div style={{flex:1}}><PaperKeys start="C" whites={7} w={34} h={64} roofs dots={[w]}/></div>{nvBox(i === 0, fsHouse(w), 42, 36)}""", 'p3 whose house')
rep("""      <KeysCell ex><PaperKeys start="C" whites={14} w={40} h={120} roofs fills={{ 0: '#fbe9e2', 1: '#fbe9e2', 2: '#fbe9e2' }}/></KeysCell>""",
    """      <KeysCell ex><PaperKeys start="C" whites={14} w={40} h={100} roofs fills={{ 0: '#fbe9e2', 1: '#fbe9e2', 2: '#fbe9e2' }}/></KeysCell>""", 'p3 try it')
rep("""      <div style={{display:'grid',gridTemplateColumns:'1fr 1.33fr',gap:14,flex:1,minHeight:150}}>""",
    """      <div style={{display:'grid',gridTemplateColumns:'1fr 1.33fr',gap:14,flex:1,minHeight:110}}>""", 'p3 play min')
# p3 play: set -- a smiley face on every white key
rep("""    <Part kind="play" title="Who lives here?" how="Draw a family of 3 under the small roof and a family of 4 under the big one -- one for each white key. Give them names!">""",
    """    <Part kind="play" title="Who lives here?" how="Draw one smiley face for each white key: 3 faces in the small house, 4 faces in the big house. Then colour the small house's roof coral and the big house's roof navy.">""", 'p3 play how')
rep("""        {[['Small house: 3 live here', 2], ['Big house: 4 live here', 3]].map(([l, n]) =>""",
    """        {[['Small house: 3 smiley faces', 2], ['Big house: 4 smiley faces', 3]].map(([l, n]) =>""", 'p3 play labels')
# p4 play: set -- what to draw under the sea and up in the sky
rep("""    <Part kind="play" title="Under the sea, up in the sky" how="Middle C is the ground. Draw what swims under the sea (to the left of middle C) and what flies up in the sky (to the right of it). Then play their sounds!">""",
    """    <Part kind="play" title="Under the sea, up in the sky" how="Middle C is the ground. Under the sea (left of middle C) draw a fish, a crab and the turtle. Up in the sky (right of middle C) draw a cloud, the sun and the bird. Then play a low note for each sea friend and a high note for each sky friend.">""", 'p4 play how')
rep("""        {box('Under the sea (low)')}""", """        {box('Under the sea (low): fish · crab · turtle')}""", 'p4 sea')
rep("""        {box('Up in the sky (high)')}""", """        {box('Up in the sky (high): cloud · sun · bird')}""", 'p4 sky')
# p5: the log's last row is set too
rep("""'Echo game with someone at home', 'My own black-key tune']} label={190}/>""",
    """'Left hand 2 3 4 on a big roof', 'Roof walk back down: 4 3 2']} label={190}/>""", 'p5 log')   # the echo game needs a partner: it stays in the lesson

# p2 play: the sound pairs bigger, to fill the page
rep("""<div style={{display:'grid',gap:8}}>{[[['chick', 'a chick', 'cheep cheep!']""", """<div style={{display:'grid',gap:10}}>{[[['chick', 'a chick', 'cheep cheep!']""", 'p2 pairs gap')
rep("""gridTemplateColumns:'54px 1fr',alignItems:'center',gap:8,padding:'4px 10px',height:70}}><SoundIcon kind={k} size={52}/><div style={{lineHeight:1.25}}><div style={{fontSize:12,color:BK.ink,fontWeight:700}}>{lab}</div><div style={{fontSize:14,color:BK.coral,fontWeight:900,fontStyle:'italic'}}>{snd}</div>""",
    """gridTemplateColumns:'62px 1fr',alignItems:'center',gap:8,padding:'4px 10px',height:88}}><SoundIcon kind={k} size={60}/><div style={{lineHeight:1.25}}><div style={{fontSize:13,color:BK.ink,fontWeight:700}}>{lab}</div><div style={{fontSize:16,color:BK.coral,fontWeight:900,fontStyle:'italic',whiteSpace:'nowrap'}}>{snd}</div>""", 'p2 pair cells')
rep("""{turtleIcon(66)}low</div>""", """{turtleIcon(80)}low</div>""", 'p2 turtle')
rep("""{birdIcon(66)}high</div>""", """{birdIcon(80)}high</div>""", 'p2 bird')
rep("""      <div style={{display:'grid',gridTemplateColumns:'86px 1fr 86px',gap:10,alignItems:'center',flex:1}}>""",
    """      <div style={{display:'grid',gridTemplateColumns:'96px 1fr 96px',gap:10,alignItems:'center',flex:1}}>""", 'p2 cols')
# p4: the 88 keys taller
rep("""<KeyScene start="A" whites={26} w={24} h={72} houses={false} turtle/>""", """<KeyScene start="A" whites={26} w={24} h={96} houses={false} turtle/>""", 'p4 low half')
rep("""<KeyScene start="F" whites={26} w={24} h={72} houses={false} bird/>""", """<KeyScene start="F" whites={26} w={24} h={96} houses={false} bird/>""", 'p4 high half')

# the check-up on paper: on its own page now -- bigger keyboards, two across
rep("""    <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'2px 10px'}}><PaperKeys start="C" whites={14} w={30} h={56} boxes={[1, 4, 8, 11]}/></div>""",
    """    <div style={{border:'1px solid #ece6d8',borderRadius:8,padding:'4px 10px'}}><PaperKeys start="C" whites={14} w={42} h={80} boxes={[1, 4, 8, 11]}/></div>""", 'chk A')
rep("""    <BkGrid cols={4} gap="5px 10px">{W.chk.hl.map((pp, i) => <BkCell key={i} n={5 + i}><div style={{padding:'11px 6px 4px'}}><PaperKeys start="C" whites={10} w={22} h={44} dots={pp}/></div></BkCell>)}</BkGrid>""",
    """    <BkGrid cols={2} gap="6px 12px">{W.chk.hl.map((pp, i) => <BkCell key={i} n={5 + i}><div style={{padding:'12px 6px 3px'}}><PaperKeys start="C" whites={10} w={30} h={52} dots={pp}/></div></BkCell>)}</BkGrid>""", 'chk B')
rep("""    <BkGrid cols={4} gap="5px 10px">{W.chk.wh.map((w, i) => <BkCell key={i} n={9 + i}><div style={{display:'flex',alignItems:'center',gap:8,padding:'11px 4px 3px'}}><div style={{flex:1}}><PaperKeys start="C" whites={7} w={16} h={40} roofs dots={[w]}/></div>{bkBox(28, 24)}</div></BkCell>)}</BkGrid>""",
    """    <BkGrid cols={2} gap="6px 12px">{W.chk.wh.map((w, i) => <BkCell key={i} n={9 + i}><div style={{display:'flex',alignItems:'center',gap:12,padding:'12px 8px 3px'}}><div style={{flex:1}}><PaperKeys start="C" whites={7} w={30} h={54} roofs dots={[w]}/></div>{bkBox(36, 30)}</div></BkCell>)}</BkGrid>""", 'chk C')
rep("""    <div style={{display:'flex',gap:22,alignItems:'center',fontSize:13,color:BK.ink,padding:'2px 4px'}}><span><b style={{color:BK.coral}}>13</b> Middle C is the left door of small house number {bkBox(32, 24)}</span><span><b style={{color:BK.coral}}>14</b> A piano has {bkBox(44, 24)} keys.</span></div>""",
    """    <div style={{display:'flex',gap:28,alignItems:'center',fontSize:14.5,color:BK.ink,padding:'4px 4px'}}><span style={{display:'inline-flex',alignItems:'center',gap:6}}><b style={{color:BK.coral}}>13</b> Middle C is the left door of small house number {bkBox(38, 30)}</span><span style={{display:'inline-flex',alignItems:'center',gap:6}}><b style={{color:BK.coral}}>14</b> A piano has {bkBox(52, 30)} keys.</span></div>""", 'chk D')
rep("""    <BkGrid cols={4} gap="5px 10px">{W.chk.sg.map((f, i) => <BkCell key={i} n={15 + i}><div style={{display:'flex',alignItems:'center',gap:8,padding:'11px 4px 3px'}}><div style={{flex:1}}><PaperKeys start="C" whites={7} w={20} h={40} blackDots={[f]}/></div>{bkBox(28, 24)}</div></BkCell>)}</BkGrid>""",
    """    <BkGrid cols={2} gap="6px 12px">{W.chk.sg.map((f, i) => <BkCell key={i} n={15 + i}><div style={{display:'flex',alignItems:'center',gap:12,padding:'12px 8px 3px'}}><div style={{flex:1}}><PaperKeys start="C" whites={7} w={30} h={54} blackDots={[f]}/></div>{bkBox(36, 30)}</div></BkCell>)}</BkGrid>""", 'chk E')

# the Teacher copy: the set play tasks have answers now
rep("""{tcAns('YOUR TURN', W.s3.map(w => fsHouse(w) + ' (' + fsLetter(w) + ')'))}</>}""",
    """{tcAns('YOUR TURN', W.s3.map(w => fsHouse(w) + ' (' + fsLetter(w) + ')'))}{tcAns('PLAY', ['3 faces in the small house, 4 in the big house -- one per white key', 'small roof coral, big roof navy'])}</>}""", 'tc p3 play')
rep("""'the star on the 24th white key from the left: middle C'])}</>}""",
    """'the star on the 24th white key from the left: middle C'])}{tcAns('PLAY', ['sea (left of middle C): fish, crab, turtle', 'sky (right of middle C): cloud, sun, bird', 'then a low note for each sea friend, a high note for each sky friend'])}</>}""", 'tc p4 play')
rep('    <TcBlock page={6} title="My five checks · the check-up on paper"', '    <TcBlock page={6} title="The check-up on paper (the Workbook\'s last page)"', 'tc p6 title')

open(src, 'w', encoding='utf-8').write(s); print('patch412 ok')
