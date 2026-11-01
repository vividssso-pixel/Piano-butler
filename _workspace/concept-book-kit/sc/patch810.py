"""Build EH (her 1 Nov 19:44: 'make it the best you think and keep going: build Grade 1, I'll check'): the Grade 1
Workbooks, fun first. Only the parts better changed, each swapped for one that practises the same thing, none added:
the parts that needed someone else at home, the free ones, and the fifth 'write what it means' in a row. Accidentals and
Key Signatures stay as they are. Code in sc/wbf46.code.js."""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
def RB(start, new):   # from `start` to the end of its Part (the first '    </Part>' after it)
    global s
    assert s.count(start) == 1, start[:80]
    a = s.index(start); a = s.rindex('\n', 0, a) + 1; b = s.index('    </Part>\n', a) + len('    </Part>\n')
    s = s[:a] + new + s[b:]
CODE = open(os.path.join(here, 'wbf46.code.js'), encoding='utf-8').read()
R("""function FmxWorkbook({ startNo = 1 }) {""", CODE + """function FmxWorkbook({ startNo = 1 }) {""")

# --- Chapter 26, 6/8 Time
# page 2: the third row of the week needed someone clapping
R("""'Walk on 1 and 4 while someone claps every quaver'""", """'Walk on 1 and 4 while you clap every quaver'""")
# page 5: words in twos and threes (in place of a week of someone at home clapping)
RB("""<Part kind="home" title="Listen this week" how="Ask someone to clap six quavers""",
   """    <Part kind="home" title="Words in twos and threes" how="Say each word over and over, a quaver a syllable, the first syllable loud: AP-ple AP-ple AP-ple. Loud every second quaver is 3/4; every third, 6/8. Write each word in its bar, four in each.">
      <E8Words/>
    </Part>
""")
R("""{tcAns('PLAY', ['3/4: [1 2] [3 4] [5 6], beats start on 1, 3, 5', '6/8: [1 2 3] [4 5 6], beats start on 1 and 4'], 5)}</>}
      watch="Counting the quavers (six either way) instead of looking at how they are grouped.\"""",
  """{tcAns('YOUR TURN', ['3/4: ' + E8_WORDS[34].join(', ') + ' (apple done)', '6/8: ' + E8_WORDS[68].join(', ')], null)}{tcAns('PLAY', ['3/4: [1 2] [3 4] [5 6], beats start on 1, 3, 5', '6/8: [1 2 3] [4 5 6], beats start on 1 and 4'], 5)}</>}
      watch="Counting the quavers (six either way) instead of looking at how they are grouped. In the words: saying a word once, not over and over; the loud syllables show the grouping only when the word repeats.\"""")
# page 6: counts into notes (in place of "write your own")
RB("""<Part kind="play" title="Write your own" how="Two bars of 6/8""",
   """    <Part kind="play" title="Counts into notes" how="A circled count starts a note. Draw the notes in each box: all three circled, three quavers; the first only, a dotted crotchet; the first and third, a crotchet and a quaver. Clap it, counting.">
      <div style={{display:'grid',gap:16,padding:'8px 0'}}>{E8_CODE.map((row, i) => <E8Code key={row} row={row} n={3 + i}/>)}{ivxTicks(['clapped, counting', 'played on one note'])}</div>
    </Part>
""")
R("""{tcAns('PLAY', ['any two bars that fill 6/8: each box is three quavers long'])}</>}
      watch="Skipping the counting step and clapping by guess. Every new line in the same order: counts out loud, clap, then play.\"""",
  """{tcAns('PLAY', E8_CODE.map(row => { const G = e8cGroups(row).map(g => E8C_NAME[g.join()]); return G[0] + ', ' + G[1] + ' | ' + G[2] + ', ' + G[3]; }), 3)}</>}
      watch="Skipping the counting step and clapping by guess. Every new line in the same order: counts out loud, clap, then play. In Counts into notes: a crotchet for a single circle (nothing starts on the next two counts: a dotted crotchet).\"""")

# --- Chapter 25, Musical Terms
# page 2: PLAY's second half needed the teacher
R("""how="Play C D E F G at each speed. Your teacher plays a scale: say its word. Tick each one.\"""",
  """how="Set a metronome to each word’s number and play C D E F G at that speed. Tick each one.\"""")
# page 5: the term crossword (in place of the fifth "write what each word means" in five pages)
RB("""<Part kind="home" title="What it means" how="Write what each word means.">""",
   """    <Part kind="home" title="The term crossword" how="Each clue is what a word means. Write the word in the squares, one letter a square. The words are in the bank.">
      <BkCell n={5}><TmxXword/></BkCell>
    </Part>
""")
R("""{sskRowN(11, <div style={{display:'flex',flexDirection:'column',gap:12,width:'100%'}}>""", """{sskRowN(6, <div style={{display:'flex',flexDirection:'column',gap:12,width:'100%'}}>""")
R("""{skgTcAns('YOUR TURN', W.turn5.map(en), 5)}</>}
      watch="Mezzo staccato played as staccato: it is half way. Sostenuto here means each note held its full length (not the pedal).\"""",
  """{skgTcAns('YOUR TURN', [(() => { const nb = xwNums(TMX_XW); return TMX_XW.slice().sort((a, b) => nb[a[0]] - nb[b[0]]).map(([w, , , d]) => nb[w] + (d === 'A' ? ' across ' : ' down ') + w).join(', '); })()], 5)}</>}
      watch="Mezzo staccato played as staccato: it is half way. Sostenuto here means each note held its full length (not the pedal). In the crossword the meaning decides, not the length.\"""")
# page 6: build the term (in place of six meanings and "make your own")
RB("""<Part kind="home" title="Write the term; make one\"""",
   """    <Part kind="home" title="Build the term" how="Each meaning is a little word and a term. Build each one from the tiles: every tile is used once.">
      <TmxBuild/>
    </Part>
""")
R("""title="One piece, three ways" how="Play a piece you know sempre staccato, then più mosso, then with a poco rit. at the end. Then play your own term from 11. Tick each.\"""",
  """title="One piece, four ways" how="Play a piece you know sempre staccato, then più mosso, then meno mosso, then with a poco rit. at the end. Tick each.\"""")
R("""{sskRowN(12, <div style={{display:'grid',gridTemplateColumns:'30px 190px minmax(0,1fr)'""", """{sskRowN(11, <div style={{display:'grid',gridTemplateColumns:'30px 190px minmax(0,1fr)'""")
R("""['sempre staccato', 'più mosso', 'poco rit.', null]""", """['sempre staccato', 'più mosso', 'meno mosso', 'poco rit.']""")
R("""{skgTcAns('YOUR TURN', W.turn6.concat(['the student’s own']), 5)}""", """{skgTcAns('YOUR TURN', TMX_BUILD.map(x => tmxBuildOf(x).w), 5)}""")
R("""watch="più and meno swapped (più: more; meno: less). poco read as “slow”. senza rit. read as a rit.\"""",
  """watch="più and meno swapped (più: more; meno: less). poco read as “slow”. senza rit. read as a rit. A tile left over: one pair is wrong.\"""")

# --- Chapter 27, Intervals
# page 4: the interval word (the notes above spell a word)
RB("""<Part kind="home" title="Write the note above" how="Draw the note, a semibreve. Odd numbers""",
   """    <Part kind="home" title="The interval word" how="Draw the note above, a semibreve (odd numbers: line to line, or space to space; even: line to space, or space to line). Write its letter in its box: 5 to 8 spell a word.">
      <IvxWord/>
    </Part>
""")
R("""{skgTcAns('YOUR TURN', W.turn4.map(([d, , n]) => nmA(d, n)), 5)}</>}
      watch="The octave called a 7th or a 9th. A 6th written line to line (6 is even: line to space, or space to line).\"""",
  """{skgTcAns('YOUR TURN', IVX_WORD.map(([d, , n]) => nmA(d, n)), 5)}{skgTcAns('THE WORD', [ivxWordOf()], null)}</>}
      watch="The octave called a 7th or a 9th. A 6th written line to line (6 is even: line to space, or space to line). In the interval word, a letter that breaks the word: count that interval again, the lower note as 1.\"""")
# page 5: both ways (in place of "your teacher plays six intervals")
RB("""<Part kind="play" title="Listen and say" how="Your teacher plays six intervals.""",
   """    <Part kind="play" title="Both ways" how="Play 5 to 8 both ways: one note after the other (melodic), then together (harmonic), as you wrote them. Say each one’s number. Tick each.">
      {sskRowN(9, <IvxBothWays/>)}
    </Part>
""")
R("""</>}
      watch="A harmonic 2nd drawn with one note on top of the other (they sit side by side, touching).\"""",
  """{skgTcAns('PLAY', ['5 to 8 both ways: ' + W.turn5.map(([, p]) => num(p)).join(', ')], 9)}</>}
      watch="A harmonic 2nd drawn with one note on top of the other (they sit side by side, touching).\"""")

# --- Chapter 28, Chords, page 3: major, then minor (in place of "your teacher plays six triads"; PLAY is 11, not 9)
RB("""<Part kind="play" title="Listen and say" how="Your teacher plays six triads.""",
   """    <Part kind="play" title="Major, then minor" how="Play each triad from 5 to 10 as it was, major, then as you wrote it, minor: only the middle note moves. Tick each.">
      {sskRowN(11, <ChxMajMin/>)}
    </Part>
""")
R("""{skgTcAns('YOUR TURN', W.turn3.map(r => minorOf(r)), 5)}</>}""",
  """{skgTcAns('YOUR TURN', W.turn3.map(r => minorOf(r)), 5)}{skgTcAns('PLAY', [W.turn3.map(r => prettyNote(r)).join(', ') + ': major, then minor, the 3rd a half step down'], 11)}</>}""")

# --- Chapter 29, Musical Form, page 5: A again, written out (in place of "make up your own B")
RB("""<Part kind="play" title="Your own B\"""",
   """    <Part kind="play" title="A again, written out" how="With no D.C. al Fine, A has to be written again. Copy bars 1 to 4 into these bars: now the road plays A B A straight through. Play it both ways. Tick each.">
      {sskRowN(6, <div style={{display:'flex',flexDirection:'column',gap:4,width:'100%'}}><div style={{fontFamily:LB_SERIF,fontSize:17,fontWeight:900,color:BK.ink,textAlign:'center'}}>A <span style={{fontSize:13,fontFamily:'Inter, sans-serif',fontWeight:800,color:BK.muted}}>(bars 1 to 4)</span> · B <span style={{fontSize:13,fontFamily:'Inter, sans-serif',fontWeight:800,color:BK.muted}}>(bars 5 to 8)</span> · A <span style={{fontSize:13,fontFamily:'Inter, sans-serif',fontWeight:800,color:BK.muted}}>(copy it here)</span></div>{fmxEmptyBars(4, 'Four empty bars: bars 1 to 4, copied.', [40, 36])}{ivxTicks(['with D.C. al Fine', 'straight through'])}</div>)}
    </Part>
""")
R("""{skgTcAns('YOUR TURN', ['bars 1 2 3 4 5 6 7 8 1 2 3 4 (two boxes empty); A B A'], 5)}</>}""",
  """{skgTcAns('YOUR TURN', ['bars 1 2 3 4 5 6 7 8 1 2 3 4 (two boxes empty); A B A'], 5)}{skgTcAns('PLAY', ['bars 1 to 4 copied after bar 8: ' + FMX_PH.A.map(bar => bar.map(n => dName(n[2])).join(' ')).join(' | ')], 6)}</>}""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok EH', len(s))
