"""Build EG (her 1 Nov 10:39 'show me the plan' and 14:37 'yes' to the plan and to one page first): the Prelim Workbooks,
fun first. Only the parts better changed, each swapped for a game that practises the same thing, none added.
Code in sc/wbf45.code.js."""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
CODE = open(os.path.join(here, 'wbf45.code.js'), encoding='utf-8').read()
R("""function LedgerWorkbook({ startNo = 1 }) {""", CODE + """function LedgerWorkbook({ startNo = 1 }) {""")

# --- Chapter 17, Ledger Lines, page 2: the ladder race (in place of counting the same ladders again)
R("""    <Part kind="play" title="How many ladders?" how="The ladders are missing. Count the dotted lines out to each note: how many does it need? 0, 1, 2 or 3.">
      {(() => { const xs = sfXs(W.count.length, 440, true); return <SfRow clef="treble" width={440} notes={W.count.map((d, i) => ({ d, x: xs[i], rungs: [] }))} guides={[3, 2]}
        items={W.count.map((d, i) => ({ x: xs[i], n: 14 + i, ex: i === 0, ans: String(llRungCount('treble', d)) }))}/>; })()}
    </Part>""",
  """    <Part kind="play" title="The ladder race" how="Write each note's ladders. Then from the star, move that many squares each time: land exactly on the flag!">
      <LlRace/>
    </Part>""")
R("""{tcAns('PLAY', W.count.map(d => String(llRungCount('treble', d))), 14)}</>}
      watch="Ladders drawn as one long line, a gap between the staff and the note, a lid on a note in a space (one line too many on top), ladders further apart than the staff lines. The notes just outside the staff (G over the treble staff, F under the bass staff) need no ladder.\"""",
  """{tcAns('PLAY', LL_RACE.map(([cl, d]) => dName(d) + ' ' + llRungCount(cl, d)))}{tcAns('THE RACE', ['squares ' + llRacePath().map(i => i + 1).join(', ') + ', then the flag (14)'], null)}</>}
      watch="Ladders drawn as one long line, a gap between the staff and the note, a lid on a note in a space (one line too many on top), ladders further apart than the staff lines. The notes just outside the staff (G over the treble staff, F under the bass staff) need no ladder. In the ladder race one wrong count takes the counter off the path, and from every square off it the counts run past the flag: if it does not land on the flag, look for the note counted wrong.\"""")

# --- Chapter 19, Playing Scales, page 3: the four-bar scale (in place of the sums)
R("""    <Part kind="play" title="Beat puzzle" how="One note a beat, up and back, and the last note held for two beats. Count it out.">
      <div style={{display:'grid',gap:12,padding:'10px 4px',fontSize:13.5,fontWeight:800,color:BK.ink}}>
        <span style={{display:'flex',alignItems:'center',gap:10}}>{nvNum(5)} How many beats is one C major scale, up and back? {bkBox(48, 32)}</span>
        <span style={{display:'flex',alignItems:'center',gap:10}}>{nvNum(6)} And G major? {bkBox(48, 32)}</span>
        <span style={{display:'flex',alignItems:'center',gap:10}}>{nvNum(7)} At metronome 76, is one scale more or less than 15 seconds? {bkBox(64, 32)}</span>
      </div>
    </Part>""",
  """    <Part kind="play" title="The four-bar scale" how="One note a beat, up and back, the last note held for two beats. Write each scale's letters, one in a box: the held note takes two. Four bars exactly! Then play it.">
      <SpFourBarPlay/>
    </Part>""")
R("""{tcAns('PLAY', ['16 beats (15 notes, the last held for two)', '16', 'less (16 beats at 76 is about 13 seconds)'], 5)}</>}
      watch="The hands running ahead after a turn; the last note cut short. Start at 60; move to 76 only when the turns are even.\"""",
  """{tcAns('PLAY', ['C', 'G'].map(k => [0, 1, 2, 3].map(b => spFourBar(k).slice(4 * b, 4 * b + 4).join(' ')).join(' | ')), 5)}</>}
      watch="The hands running ahead after a turn; the last note cut short. Start at 60; move to 76 only when the turns are even. In the four-bar scale, a row a box short or a box over has a note missing or written twice: most often the top note twice.\"""")

# --- Chapter 20, Minor Scales, page 3: same keys, a new home (in place of matching the same four pairs again)
R("""    <Part kind="play" title="Key signature twins" how="Draw a line from each major key to the minor key that shares its key signature.">
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'14px 120px',justifyContent:'center',padding:'14px 40px',fontFamily:LB_SERIF,fontSize:20,fontWeight:800,color:BK.ink}}>
        {[['C major', 'D minor'], ['G major', 'A minor'], ['F major', 'G minor'], ['B♭ major', 'E minor']].map(([a, b]) => <React.Fragment key={a}><span style={{display:'flex',alignItems:'center',justifyContent:'flex-end',gap:10}}>{a}<span style={{width:9,height:9,borderRadius:5,background:BK.ink}}/></span><span style={{display:'flex',alignItems:'center',gap:10}}><span style={{width:9,height:9,borderRadius:5,background:BK.ink}}/>{b}</span></React.Fragment>)}
      </div>
    </Part>""",
  """    <Part kind="play" title="Same keys, a new home" how="Twins share a key signature, so they share their keys. Play up and down from the navy star: the major. Then from the red star, on the same keys: its minor twin (the natural minor). Tick each.">
      <MsTwinsPlay/>
    </Part>""")
R("""{tcAns('PLAY', ['C–A, G–E, F–D, B♭–G'])}</>}
      watch="Counting up instead of down (C up three half steps is E♭), or naming the minor on the same note (C major, C minor): that key has a different key signature. A key signature alone does not say major or minor: the piece's first and last notes do.\"""",
  """{tcAns('PLAY', MS_TWINS.map(([M, m]) => SP_SC[M].en + ' and ' + SP_SC[m].en.replace('natural ', '') + ': ' + (SP_SC[M].nm.filter(x => x.length > 1).join(', ') || 'the white keys')), null)}</>}
      watch="Counting up instead of down (C up three half steps is E♭), or naming the minor on the same note (C major, C minor): that key has a different key signature. A key signature alone does not say major or minor: the piece's first and last notes do. In Same keys, a new home: playing the minor with the major's pattern from its note (C♯ in A, G♯ in E): stay on the lit keys. This is the natural minor; the raised 7th is the next page.\"""")

# --- Chapter 20, Minor Scales, page 5: the step trail (in place of writing the code "from memory" under the answer)
R("""    <Part kind="play" title="The secret code" how="Every harmonic minor has the same code of seven steps. Write it from memory, then check it against the boxes above.">
      <div style={{display:'flex',gap:8,justifyContent:'center',padding:'12px 0'}}>{Array.from({ length: 7 }, (_, j) => <span key={j} style={{width:46,height:46,border:'2px solid ' + BK.coral,borderRadius:8}}/>)}</div>
    </Part>""",
  """    <Part kind="play" title="The step trail" how="From the star, go up: T is 2 half steps, S is 1, T½ is 3. Write each step's number on the key it lands on. Step 7 lands on the flag! Then name the scale.">
      <MsTrail/>
    </Part>""")
R("""{tcAns('PLAY', ['T S T T S T½ S'])}</>}
      watch="Calling the tone and a half a tone, because the two letters are next to each other (F to G♯). Count the half steps, not the letters.\"""",
  """{tcAns('PLAY', [SP_SC[MS_TRAIL.nm].nm.slice(1).concat([SP_SC[MS_TRAIL.nm].nm[0]]).map((x, i) => (i + 1) + ' ' + x).join(', ') + ': 7 on the flag', MS_TRAIL.m + ' harmonic minor'], null)}</>}
      watch="Calling the tone and a half a tone, because the two letters are next to each other (F to G♯). Count the half steps, not the letters. In the step trail, the T½ counted as three white keys: count every key, black ones too.\"""")

# --- Chapter 20, Minor Scales, page 6: the same tune, darker (in place of a week of someone playing scales to the child)
R("""    <Part kind="home" title="Listen this week" how="Ask someone to play you a scale, up and down. Is it major or harmonic minor? Tick a box when you get it right.">
      <PhLog rows={['C major, then A harmonic minor', 'G major, then E harmonic minor', 'F major, then D harmonic minor', 'Mixed: someone picks, you say']} label={300}/>
    </Part>""",
  """    <Part kind="home" title="The same tune, darker" how="Each tune in major, with its steps. Write the same steps in its minor twin. Play both: the same tune, darker.">
      <MsTunes/>
    </Part>""")
R("""{nvNum(5 + i)}<span style={{letterSpacing:'0.12em'}}>""", """{nvNum(9 + i)}<span style={{letterSpacing:'0.12em'}}>""")
R("""{tcAns('PLAY', ['major', 'harmonic minor'], 5)}</>}
      watch="By ear: playing the scale fast. Play it at a walking pace, up and down; the darker third comes at once, the wide step near the top.\"""",
  """{tcAns('YOUR TURN', MS_TUNES.map(([si, M, m]) => msTuneLetters(m, MT_SONGS[si][2]).join(' ')), 5)}{tcAns('PLAY', ['major', 'harmonic minor'], 9)}</>}
      watch="By ear: playing the scale fast. Play it at a walking pace, up and down; the darker third comes at once, the wide step near the top. In the same tune, darker: counting the steps from the major's first note again; in the minor, its own first note is 1 (A in A minor). The tunes use no 7th, so they sound the same in the natural and the harmonic minor.\"""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok EG', len(s))
