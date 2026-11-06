#!/usr/bin/env python3
# Phase 411: chapter 1's Workbook, bigger (Sohyun: "the same for chapters 1-3 -- 그렇게 해줘") and every task set,
# not free (her Phase-410 rule): bigger pictures to judge, bigger hands and circles; the free finger walk becomes
# "the secret walk" (words -> finger numbers); the check-up page fills its page.
#   python3 patch411.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# p2: the set-up pictures, bigger; the drawing is set: what to draw is listed (it already was) -- keep
rep("""      <BkGrid cols={4} gap="6px 10px">{[PH_SIT[0], PH_SIT[1], PH_SIT[4], PH_SIT[2]].map(([id, , ok], i) => <PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} ex={i === 0} h={84}/>)}</BkGrid>""",
    """      <BkGrid cols={4} gap="6px 10px">{[PH_SIT[0], PH_SIT[1], PH_SIT[4], PH_SIT[2]].map(([id, , ok], i) => <PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} ex={i === 0} h={104}/>)}</BkGrid>""", 'p2 pics')
rep("""    <Part kind="play" title="Draw yourself at the piano" how="Draw yourself sitting at the piano. Then colour a star for each thing you drew.">""",
    """    <Part kind="play" title="Draw yourself at the piano" how="Draw yourself sitting at the piano with all five: sitting tall, feet flat, leaning a little forward, elbows away from the body, round hands. Colour a star for each one you drew.">""", 'p2 draw how')
# p3: the warm-up pictures, bigger
rep("""        <div style={{height:92,display:'flex',alignItems:'center'}}><PbArt name={art} h={88} style={{maxWidth:'100%'}}/></div>""",
    """        <div style={{height:108,display:'flex',alignItems:'center'}}><PbArt name={art} h={104} style={{maxWidth:'100%'}}/></div>""", 'p3 pics')
# p4: the hand pictures, bigger
rep("""      <BkGrid cols={3} gap="6px 10px">{PH_HAND.map(([id, , ok], i) => <PhPic key={id} art={'q-hand-' + id} ok={ok} n={i + 1} ex={i === 0} h={66}/>)}</BkGrid>""",
    """      <BkGrid cols={3} gap="6px 10px">{PH_HAND.map(([id, , ok], i) => <PhPic key={id} art={'q-hand-' + id} ok={ok} n={i + 1} ex={i === 0} h={92}/>)}</BkGrid>""", 'p4 pics')
rep("""    <Part kind="play" title="Hold the bubble" how="Hold a small ball (or a mandarin) in a round hand. Draw your hand round it, then colour a star for each.">""",
    """    <Part kind="play" title="Hold the bubble" how="Hold a small ball (or a mandarin) in your right hand, fingers round it. Draw your hand round the ball with all four: knuckles up, round fingers, playing on the tips, the thumb on its side. Colour a star for each one you drew.">""", 'p4 draw how')
# p5: which finger -- three across, big hands
rep("""      <BkGrid cols={6} gap="6px 8px">{W.fingers.map(([h, f], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4,padding:'12px 2px 2px'}}>
        <PbArt name={'q-fingers-' + h} lit={f} h={74}/>{nvBox(i === 0, String(f), 34, 28)}""",
    """      <BkGrid cols={3} gap="8px 12px">{W.fingers.map(([h, f], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:14,padding:'12px 2px 4px'}}>
        <PbArt name={'q-fingers-' + h} lit={f} h={112}/>{nvBox(i === 0, String(f), 42, 36)}""", 'p5 fingers')
rep("""      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,flex:1,minHeight:500}}>{['Left hand', 'Right hand'].map(l =>""",
    """      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,flex:1,minHeight:380}}>{['Left hand', 'Right hand'].map(l =>""", 'p5 trace min')
# p6: bigger circles; the free walk becomes the secret walk (her rule: set, not free)
rep("""        <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:15,fontWeight:800,color:BK.ink}}>{name}</span><PhCircles seq={seq} ex={i === 0}/>""",
    """        <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:16,fontWeight:800,color:BK.ink}}>{name}</span><PhCircles seq={seq} ex={i === 0} size={34}/>""", 'p6 circles')
rep("""    <Part kind="play" title="Make your own finger walk" how="Write a finger number (1 to 5) in each circle. Leave a circle empty to hold the note. Play it to someone!">
      <div style={{display:'grid',gap:12,justifyItems:'center'}}>
        <div style={{display:'flex',alignItems:'center',gap:8}}>{[0, 1, 2, 3, 'bar', 4, 5, 6, 7].map((k, i) => k === 'bar' ? <span key={i} style={{width:1.8,height:40,background:BK.ink,opacity:0.5,margin:'0 4px'}}/> : <span key={i} style={{width:40,height:40,borderRadius:20,border:'2px solid ' + BK.ink,background:'#fff'}}/>)}</div>
        <div style={{fontSize:13,color:BK.ink}}>My tune is called <span style={{display:'inline-block',width:220,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span></div>
      </div>
    </Part>""",
    """    <Part kind="play" title="The secret walk" how="Read the clues and write the finger numbers in the circles -- then play the walk with your right hand.">
      <div style={{display:'grid',gap:14,justifyItems:'center'}}>
        <ol style={{margin:0,padding:'0 0 0 20px',fontSize:13.5,color:BK.ink,lineHeight:1.6,justifySelf:'stretch'}}>
          <li>Start on your <b>thumb</b>.</li>
          <li>Walk up <b>one finger at a time</b> to your <b>middle finger</b>.</li>
          <li><b>Jump</b> to your <b>little finger</b>.</li>
          <li>Walk back down, one finger at a time, all the way <b>home to your thumb</b>.</li>
        </ol>
        <div style={{display:'flex',alignItems:'center',gap:9}}>{[0, 1, 2, 3, 4, 5, 6, 7].map(i => <span key={i} style={{width:44,height:44,borderRadius:22,border:'2px solid ' + (i === 0 ? BK.coral : BK.ink),background:'#fff',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:20,fontWeight:900,color:BK.coral}}>{i === 0 ? '1' : ''}</span>)}</div>
        <div style={{fontSize:12,color:BK.muted}}>The first one is done: the thumb is 1.</div>
      </div>
    </Part>""", 'p6 secret walk')

# the check-up on paper: on its own Workbook page now -- everything bigger
rep("""    <BkGrid cols={4} gap="5px 10px">{W.chk.st.map(([id, , ok], i) => <PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={LANG === 'ko' ? 42 : 46}/>)}</BkGrid>""",
    """    <BkGrid cols={4} gap="6px 10px">{W.chk.st.map(([id, , ok], i) => <PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={88}/>)}</BkGrid>""", 'chk A')
rep("""    <BkGrid cols={4} gap="5px 10px">{W.chk.hs.map(([id, , ok], i) => <PhPic key={id} art={'q-hand-' + id} ok={ok} n={i + 5} h={40}/>)}</BkGrid>""",
    """    <BkGrid cols={4} gap="6px 10px">{W.chk.hs.map(([id, , ok], i) => <PhPic key={id} art={'q-hand-' + id} ok={ok} n={i + 5} h={62}/>)}</BkGrid>""", 'chk B')
rep("""    <BkGrid cols={4} gap="5px 10px">{W.chk.fn.map((f, i) => <BkCell key={i} n={(9 + i) + ' · ' + (13 + i)}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,padding:'11px 4px 3px'}}>
      <PbArt name={'q-fingers-' + W.chk.lr[i] + '-plain'} lit={f} h={54}/>
      <div style={{display:'grid',gap:5,fontSize:10,fontWeight:900,color:BK.coral}}><span>C {bkBox(28, 22)}</span><span>D {bkBox(28, 22)}</span></div>""",
    """    <BkGrid cols={4} gap="6px 10px">{W.chk.fn.map((f, i) => <BkCell key={i} n={(9 + i) + ' · ' + (13 + i)}><div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,padding:'13px 4px 4px'}}>
      <PbArt name={'q-fingers-' + W.chk.lr[i] + '-plain'} lit={f} h={86}/>
      <div style={{display:'grid',gap:8,fontSize:11,fontWeight:900,color:BK.coral}}><span>C {bkBox(32, 28)}</span><span>D {bkBox(32, 28)}</span></div>""", 'chk CD')
rep("""    <BkGrid cols={4} gap="5px 10px">{PH_FILL_CHK.map((seq, i) => <BkCell key={i} n={17 + i}><div style={{display:'flex',justifyContent:'center',padding:'12px 2px 2px'}}><PhCircles seq={seq} size={21}/></div></BkCell>)}</BkGrid>""",
    """    <BkGrid cols={2} gap="8px 12px">{PH_FILL_CHK.map((seq, i) => <BkCell key={i} n={17 + i}><div style={{display:'flex',justifyContent:'center',padding:'16px 2px 6px'}}><PhCircles seq={seq} size={34}/></div></BkCell>)}</BkGrid>""", 'chk E')
# the Teacher copy: the secret walk's answer
rep("""function PostureTeacher() {""", """const PH_SECRET_WALK = '1 2 3 5 4 3 2 1';   // Phase 411: thumb, up to the middle finger, jump to 5, back home
function PostureTeacher() {""", 'secret walk const')

rep("""<div style={{fontSize:12,color:BK.ink}}>Own tune: any numbers 1 to 5; check that it is played with a round hand and the empty circles are held.</div>""",
    """{tcAns('SECRET WALK', [PH_SECRET_WALK + ' -- then played with a round hand'])}""", 'tc secret walk')
rep('    <TcBlock page={7} title="My five checks · the check-up on paper"', '    <TcBlock page={7} title="The check-up on paper (the Workbook\'s last page)"', 'tc p7 title')
open(src, 'w', encoding='utf-8').write(s); print('patch411 ok')
