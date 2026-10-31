"""Build DX (her 11:31 'the piano's story should have things like the black-key jam, it all feels stiff'): a free-play toy in
four of The Piano's Story's steps, under each step's own pad ('Now play freely'): play the three keyboards yourself over a
bass that goes round (step 1), strum the strings with the lid open (3), a pedal playground (4), slide along all 88 keys
and count the Cs (5). Step 2 has the room's make-it toy, Make a surprise! (Build DW). Code in sc/sps9.code.js."""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
CODE = open(os.path.join(here, 'sps9.code.js'), encoding='utf-8').read()
R("""// ── the book on screen: the opener is the lesson's head, every other page a step ──
function SpsLearn({ onStart }) {""", CODE + """
// ── the book on screen: the opener is the lesson's head, every other page a step ──
function SpsLearn({ onStart }) {""")
R("""function Step({ n, total, title, color, open, done, onToggle, onDone, children, id, bookExtra, make }) {""",
  """function Step({ n, total, title, color, open, done, onToggle, onDone, children, id, bookExtra, make, play: Play }) {""")
R("""          <StepCtx.Provider value={color}>{children}{make && <StepMake ids={make}/>}</StepCtx.Provider>""",
  """          <StepCtx.Provider value={color}>{children}{Play && <div data-step-play style={{margin:'14px 0 6px',paddingTop:10,borderTop:'1.5px dashed rgba(38,41,107,0.28)',minWidth:0}}>
            <div style={{fontSize:11.5,fontWeight:900,color:'#e4572e',letterSpacing:'0.1em',textTransform:'uppercase',margin:'0 0 6px'}}>{t('Now play freely', '이제 마음대로 쳐 봐요')}</div><Play/></div>}{make && <StepMake ids={make}/>}</StepCtx.Provider>""")
R("""        make: (MAKE_AT[id] || {})[i],""", """        make: (MAKE_AT[id] || {})[i], play: (STEP_PLAY[id] || {})[i],""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok piano story plays', len(s))
