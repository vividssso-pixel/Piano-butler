"""Build EI (her 1 Nov 21:44 'yes': the Grade 2 floor, the same way): the Grade 2 Workbooks, fun first. Only the parts better
changed, none added: Rhythm, Grade 2's two PLAYs (sums and questions) now play the thing with words; one log row that was
a free task; Melody's 'make your own'. Scales, Grade 2 and Intervals, Grade 2 stay as they are. Code in sc/wbf47.code.js."""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
def RAfter(anchor, old, new):   # the first `old` after `anchor`
    global s
    assert s.count(anchor) == 1, anchor[:80]
    a = s.index(anchor); b = s.index(old, a)
    s = s[:b] + new + s[b + len(old):]
CODE = open(os.path.join(here, 'wbf47.code.js'), encoding='utf-8').read()
R("""function FmxWorkbook({ startNo = 1 }) {""", CODE + """function FmxWorkbook({ startNo = 1 }) {""")

# --- Rhythm, Grade 2 (the Workbook's steps 1 and 3; Grade 3's steps are untouched)
RAfter("""function R2Workbook({ startNo = 1, g = 3 }) {""", """<Part kind="play" title={playT} how={playH}>{quiz(rows)}</Part>""",
       """<Part kind="play" title={playT} how={playH}>{Array.isArray(rows) ? quiz(rows) : rows}</Part>""")
R("""'Semiquaver sums', 'How many semiquavers?', [['in a crotchet', 3], ['in a quaver', 4], ['in a dotted quaver', 5]]""",
  """'One beat a word', 'One note a syllable: draw each beat’s notes in its box (four syllables in one beat: four semiquavers). Then say it, clap it and play it on one note.', <R2WordLines lines={R2W_SEMI} n0={3}/>""")
R("""'Three for two, two for three', 'Answer.', R2_PLAY3""",
  """'Three for two, two for three', 'One beat a word, one note a syllable. In 2/4, three in a crotchet beat make a triplet; in 6/8, two in a dotted crotchet beat make a duplet. Draw each beat’s notes, then say, clap and play.', <R2WordLines lines={R2W_TRIP} n0={3}/>""")
R("""'Make up a bar of 2/4 with one triplet in it'""", """'Switch every beat: three claps (1 + a), then two (1 +), with the metronome at 60'""")
R("""{tcAns('PLAY', ['4', '2', '3'], 3)}""", """{tcAns('PLAY', r2wAns(R2W_SEMI), 3)}""")
R("""{tcAns('PLAY', ['3', '2'], 3)}""", """{tcAns('PLAY', r2wAns(R2W_TRIP), 3)}""")
R('''watch="Semiquavers rushed into the next beat. Say 1 e + a steadily before clapping."''',
  '''watch="Semiquavers rushed into the next beat. Say 1 e + a steadily before clapping. In the words: wa-ter-mel-on is four even notes, not two quavers and two semiquavers."''')
R('''watch="Triplets that turn into a quaver and two semiquavers; duplets that slip back into three."''',
  '''watch="Triplets that turn into a quaver and two semiquavers; duplets that slip back into three. In the words: ap-ple in 6/8 is a duplet; two quavers would leave the beat a quaver short."''')

# --- Melody and Phrasing, page 6: the sequences the other way (in place of "make a motif of your own")
R("""Then make a motif of your own and play it in sequence. Tick each.""", """Then play each the other way: 5 a step lower each time, 6 a step higher. Tick each.""")
R("""ivxTicks(['sequence 5', 'sequence 6', 'my own'])""", """ivxTicks(['sequence 5', 'sequence 6', 'both the other way'])""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok EI', len(s))
