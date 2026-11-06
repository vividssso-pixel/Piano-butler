#!/usr/bin/env python3
# Phase 450 DRAFT (her 2026-10-12 19:17, on the tipped-boat thumb picture): the thumb's in-and-out check and each finger
# playing while the others keep the balance -- two moving cards under the thumb picture in the app's step 3 (the book's
# page 4), and the same two things as lines on the page.
#   python3 patch450.py <src> <dst> <thumb450.jsx>
import sys
src, dst, jsx = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
code = open(jsx, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
rep("const WARM_UPS = [", code + "const WARM_UPS = [")
rep("""        <RoundHand376/>
        <LbPic h={120}><LbFig art="hand-thumb" h={118} cap={t('The thumb bends in and plays on the side of its tip, like a tipped boat', '엄지는 안으로 꺾여 손끝 옆면으로 쳐요. 옆으로 누운 배처럼')}/></LbPic>""",
"""        <RoundHand376/>
        <LbPic h={120}><LbFig art="hand-thumb" h={118} cap={t('The thumb bends in and plays on the side of its tip, like a tipped boat', '엄지는 안으로 꺾여 손끝 옆면으로 쳐요. 옆으로 누운 배처럼')}/></LbPic>
        <ThumbMoves450/>""")
rep("""Say: "Hold a little bubble in your hand. Don\\'t pop it!"', '손끝 관절을, 특히 5번 손가락을 봐 주세요: 지금은 학생이 알아차리도록만 도와요. 이렇게 말해 주세요: "손 안에 작은 비눗방울을 쥐고 있어. 터뜨리지 마!"')}</>}>""",
"""Say: "Hold a little bubble in your hand. Don\\'t pop it!" Thumb in and out: a thumb that cannot slide in and out means a tight hand. Shake it loose and try again.', '손끝 관절을, 특히 5번 손가락을 봐 주세요: 지금은 학생이 알아차리도록만 도와요. 이렇게 말해 주세요: "손 안에 작은 비눗방울을 쥐고 있어. 터뜨리지 마!" 엄지 인앤아웃: 엄지가 들어갔다 나왔다 하지 못하면 손에 힘이 들어간 거예요. 손을 털고 다시 해 봐요.')}</>}>""")
rep("""        <>손가락마다 건반 하나씩, 손끝으로 쳐요. 마디는 위로 그대로.</>,
        <>손끝을 건반에 대고: 롤러 위에 있는 것처럼 손목을 위아래로, 그다음 좌우로 흔들어요. 마디와 손끝을 살펴보고, 무너지지 않게 해 봐요.</>,""",
"""        <>손가락마다 건반 하나씩, 손끝으로 쳐요. 마디는 위로 그대로, 나머지 손가락은 자기 건반 위에서 균형을 잡아요.</>,
        <>손끝을 건반에 대고: 롤러 위에 있는 것처럼 손목을 위아래로, 그다음 좌우로 흔들어요. 마디와 손끝을 살펴보고, 무너지지 않게 해 봐요.</>,
        <><b>엄지 인앤아웃:</b> 엄지를 2, 3, 4번 손가락 아래로 쏙 넣었다가 다시 빼요. 손은 둥글게, 가만히.</>,""")
rep("""        <>Play one key with each finger, on the tip. The knuckles stay up.</>,
        <>Fingertip on a key: sway the wrist up and down, then side to side, as if on a roller. Notice the knuckles and the tip, and try not to let them cave in.</>,""",
"""        <>Play one key with each finger, on the tip. The knuckles stay up, and the other fingers rest on their keys to keep the balance.</>,
        <>Fingertip on a key: sway the wrist up and down, then side to side, as if on a roller. Notice the knuckles and the tip, and try not to let them cave in.</>,
        <><b>Thumb in and out:</b> slide the thumb in under fingers 2, 3 and 4, then back out. The hand stays round and still.</>,""")
# the book's thumb picture now shows where the thumb goes in, too (her 21:17 '응'); LbFig can take a drawing of its own
rep("""function LbFig({ art, h, cap }) {
  return <div style={lbScreen() ? {display:'flex',flexDirection:'column',alignItems:'center',gap:5,maxWidth:'100%',minWidth:0} : {display:'grid',justifyItems:'center',gap:5,width:'min-content'}}><PbArt name={art} h={h}/>""",
"""function LbFig({ art, h, cap, pic }) {
  return <div style={lbScreen() ? {display:'flex',flexDirection:'column',alignItems:'center',gap:5,maxWidth:'100%',minWidth:0} : {display:'grid',justifyItems:'center',gap:5,width:'min-content'}}>{pic || <PbArt name={art} h={h}/>}""")
rep("""        <LbFig art="hand-thumb" h={128} cap={t('The thumb bends in and plays on the side of its tip, like a tipped boat', '엄지는 안으로 꺾여 손끝 옆면으로 쳐요. 옆으로 누운 배처럼')}/>
      </LbPic>} live={<>""",
"""        <LbFig pic={<PenArt shapes={thumbBook450()} vb={[0, 0, 204, 152]} style={{height:150,width:202}}/>} cap={t('The thumb plays on the side of its tip, like a tipped boat, and slides in and out', '엄지는 옆으로 누운 배처럼 손끝 옆면으로 치고, 안으로 들어갔다 나와요')}/>
      </LbPic>} live={<>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
