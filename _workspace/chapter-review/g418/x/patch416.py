#!/usr/bin/env python3
# Phase 416: chapter 1's Workbook against the house rules (her 00:39 note: 'always check balance, space, how it reads,
# not too much at once -- before you show me'): the secret walk's empty top gets a second set walk (left hand);
# the step-4 page ends with How did it feel? like every other page; the check-up page fills its page
# (the set-up and hand pictures two across, so they can be big).
#   python3 patch416.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# p6: two secret walks, right hand then left hand (set, solo) -- the whole Part is replaced, from its title to </Part>
i0 = s.index('    <Part kind="play" title="The secret walk" how=')
i1 = s.index('    </Part>\n', i0) + len('    </Part>\n')
if s.count('title="The secret walk"') != 1: raise SystemExit('secret walk part')
s = s[:i0] + """    <Part kind="play" title="The secret walks" how="Read the clues and write the finger numbers in the circles -- then play each walk with its hand. The first circle is done.">
      <div style={{display:'grid',gap:12}}>{PH_SECRET_CLUES.map(([hand, clues, first], k) => <div key={hand} style={{border:'1px solid #ece6d8',borderRadius:10,padding:'9px 14px 12px'}}>
        <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:16,fontWeight:800,color:BK.ink,marginBottom:2}}>{k + 1} · {hand}</div>
        <ol style={{margin:'0 0 10px',padding:'0 0 0 20px',fontSize:13.5,color:BK.ink,lineHeight:1.6}}>{clues.map((c, j) => <li key={j}>{c}</li>)}</ol>
        <div style={{display:'flex',justifyContent:'center',gap:9}}>{[0, 1, 2, 3, 4, 5, 6, 7].map(i => <span key={i} style={{width:44,height:44,borderRadius:22,border:'2px solid ' + (i === 0 ? BK.coral : BK.ink),background:'#fff',display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:20,fontWeight:900,color:BK.coral}}>{i === 0 ? first : ''}</span>)}</div>
      </div>)}</div>
    </Part>
""" + s[i1:]
rep("""const PH_SECRET_WALK = '1 2 3 5 4 3 2 1';   // Phase 411: thumb, up to the middle finger, jump to 5, back home""",
    """const PH_SECRET_WALK = '1 2 3 5 4 3 2 1';   // Phase 411: thumb, up to the middle finger, jump to 5, back home
const PH_SECRET_WALK_L = '5 4 3 1 2 3 4 5';  // Phase 416: the left hand -- little finger down to the middle, jump to the thumb, back up
const PH_SECRET_CLUES = [
  ['Right hand', [<>Start on your <b>thumb</b>.</>, <>Walk up <b>one finger at a time</b> to your <b>middle finger</b>.</>, <><b>Jump</b> to your <b>little finger</b>.</>, <>Walk back down, one finger at a time, all the way <b>home to your thumb</b>.</>], '1'],
  ['Left hand', [<>Start on your <b>little finger</b>.</>, <>Walk <b>one finger at a time</b> to your <b>middle finger</b>.</>, <><b>Jump</b> to your <b>thumb</b>.</>, <>Walk back, one finger at a time, all the way to your <b>little finger</b>.</>], '5'],
];""", 'secret walk L const')
rep("""{tcAns('SECRET WALK', [PH_SECRET_WALK + ' -- then played with a round hand'])}""",
    """{tcAns('SECRET WALKS', ['right hand: ' + PH_SECRET_WALK, 'left hand: ' + PH_SECRET_WALK_L, 'then each played with a round hand'])}""", 'tc secret walks')

# p5: the trace page ends like the others
rep("""      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,flex:1,minHeight:380}}>{['Left hand', 'Right hand'].map(l =>""",
    """      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,flex:1,minHeight:340}}>{['Left hand', 'Right hand'].map(l =>""", 'p5 trace min')
rep("""'A ring round each finger 4', 'Left and right the right way round'].map(x =>""", """'A ring round each finger 4', 'Left and right the right way round'].map(x =>""", 'p5 check row (anchor)')
i = s.index("'A ring round each finger 4', 'Left and right the right way round'].map(x =>")
j = s.index("    </Part>\n  </>);", i)
s = s[:j] + "    </Part>\n    <Faces/>\n  </>);" + s[j + len("    </Part>\n  </>);"):]

# the check-up page: pictures two across, big
rep("""    <BkGrid cols={4} gap="6px 10px">{W.chk.st.map(([id, , ok], i) => <PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={88}/>)}</BkGrid>""",
    """    <BkGrid cols={4} gap="6px 10px">{W.chk.st.map(([id, , ok], i) => <PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={100}/>)}</BkGrid>""", 'chk A bigger')
rep("""    <BkGrid cols={4} gap="6px 10px">{W.chk.hs.map(([id, , ok], i) => <PhPic key={id} art={'q-hand-' + id} ok={ok} n={i + 5} h={62}/>)}</BkGrid>""",
    """    <BkGrid cols={2} gap="6px 12px">{W.chk.hs.map(([id, , ok], i) => <PhPic key={id} art={'q-hand-' + id} ok={ok} n={i + 5} h={116}/>)}</BkGrid>""", 'chk B two across')
rep("""    <BkGrid cols={2} gap="8px 12px">{PH_FILL_CHK.map((seq, i) => <BkCell key={i} n={17 + i}><div style={{display:'flex',justifyContent:'center',padding:'16px 2px 6px'}}><PhCircles seq={seq} size={34}/></div></BkCell>)}</BkGrid>""",
    """    <BkGrid cols={2} gap="8px 12px">{PH_FILL_CHK.map((seq, i) => <BkCell key={i} n={17 + i}><div style={{display:'flex',justifyContent:'center',padding:'20px 2px 12px'}}><PhCircles seq={seq} size={44}/></div></BkCell>)}</BkGrid>""", 'chk E')
rep("""    {bkSec('C', 'Left or right hand? Write L or R.  D  Which finger is coloured?')}""",
    """    {bkSec('C · D', 'Left or right hand? Write L or R in box C. Which finger is coloured? Write its number in box D.')}""", 'chk CD heading')
rep("""      <PbArt name={'q-fingers-' + W.chk.lr[i] + '-plain'} lit={f} h={86}/>""", """      <PbArt name={'q-fingers-' + W.chk.lr[i] + '-plain'} lit={f} h={100}/>""", 'chk CD hands')

open(src, 'w', encoding='utf-8').write(s); print('patch416 ok')
