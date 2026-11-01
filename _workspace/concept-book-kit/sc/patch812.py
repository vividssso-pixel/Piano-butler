"""Build EJ (her 1 Nov 23:32 'keep going'): the Grade 3 Workbooks, fun first. Only the parts better changed, none added:
Rhythm, Grade 3's three PLAYs (questions, the same as its check-up) now play the thing with Grade 2's words. Writing a
Melody, Scales, Grade 3 and Chords and Cadences, Grade 3 stay as they are. Code in sc/wbf48.code.js."""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
CODE = open(os.path.join(here, 'wbf48.code.js'), encoding='utf-8').read()
R("""function FmxWorkbook({ startNo = 1 }) {""", CODE + """function FmxWorkbook({ startNo = 1 }) {""")

# --- Rhythm, Grade 3 (the shared R2Workbook's steps 2, 4 and 5; Grade 2's steps untouched)
R("""'Long and short', 'Answer.', [['the count of the semiquaver after a dotted quaver', 3], ['a dotted quaver and a semiquaver make how many beats?', 4]]""",
  """'Even, then dotted', 'Draw each word’s notes twice: even, then dotted (long, short: a dotted quaver and a semiquaver, counted 1 a). Say both, clap both, then play a scale each way.', <R3WordLines lines={R3W_DOT} n0={3}/>""")
R("""'Beats in a bar', 'How many beats in one bar?', [['3/2', 3], ['2/2', 4], ['cut common time', 5]]""",
  """'One beat a word, in minims', 'In 2/2 and 3/2 the beat is a minim: one beat a word, one note a syllable (pie, a minim). Draw each beat’s notes, then say, clap and play, counting in minims.', <R3WordLines lines={R3W_MIN} n0={3}/>""")
R("""'Simple or compound?', 'Write S or C.', [['3/8', 3], ['6/8', 4], ['9/8', 5], ['3/4', 6]]""",
  """'Simple or compound?', 'Say one bar in words, one word a beat: ap-ple for a beat that splits in two, pine-ap-ple for one that splits in three. Write the words, then S (simple) or C (compound).', <R3SayBars n0={3}/>""")
R("""{tcAns('PLAY', ['a', 'one beat'], 3)}""", """{tcAns('PLAY', r3Ans(R3W_DOT), 3)}""")
R("""{tcAns('PLAY', ['3', '2', '2'], 3)}""", """{tcAns('PLAY', r3Ans(R3W_MIN), 3)}""")
R("""{tcAns('PLAY', ['S', 'C', 'C', 'S'], 3)}""", """{tcAns('PLAY', R3_SC.map(ts => ts.join('/') + ': ' + r3ScWords(ts).join(' ') + ', ' + (r3Compound(ts) ? 'C' : 'S')), 3)}""")
R('''watch="Counting crotchets in 2/2. The click falls on every minim."''',
  '''watch="Counting crotchets in 2/2. The click falls on every minim. In the words, pie is a whole minim beat here."''')
R('''watch="9/8 counted as three bars of 3/8 with equal weight. Lean on 1, 4 and 7 (in 12/8 on 1, 4, 7 and 10)."''',
  '''watch="9/8 counted as three bars of 3/8 with equal weight. Lean on 1, 4 and 7 (in 12/8 on 1, 4, 7 and 10). In the words, 3/8 is ap-ple three times (a quaver beat), not one pine-ap-ple."''')

# The Teacher copy: the minim-beat block moves to the first page (Grade 3's first page had room; its second ran over with
# the longer answers). Grade 2 never shows it.
L = s.split('\n')
i5 = [i for i, l in enumerate(L) if l.startswith('    <TcBlock page={5} title="The minim beat"')]
assert len(i5) == 1 and L[i5[0] - 1] == '  P(<>' and L[i5[0] - 2] == '  </>);', L[i5[0] - 2:i5[0]]
blk = L.pop(i5[0]); L.insert(i5[0] - 2, blk); s = '\n'.join(L)

open(dst, 'w', encoding='utf-8').write(s)
print('ok EJ', len(s))
