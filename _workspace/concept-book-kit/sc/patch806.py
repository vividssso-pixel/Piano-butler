"""Build ED (her 31 Oct 15:56: 'the reference pages of the theory book in my folder are so good: I want almost all of it in
the Reference; there is more after my screenshots'): the Reference takes in the whole of the book's reference section in the
house's own data and drawings (sc/ref42.code.js replaces sc/ref41.code.js): the staff and the clefs, the breve to the
hemidemisemiquaver, the time signatures it lists, every scale spelt out, every chord on any root, the signs, the words for how
to play, words about music, the periods and the instruments; thirteen A4 pages on paper."""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
OLD = open(os.path.join(here, 'ref41.code.js'), encoding='utf-8').read()
NEW = open(os.path.join(here, 'ref42.code.js'), encoding='utf-8').read()
R(OLD, NEW)
R("""  'reference': ['한눈에 보기', 'Beginner부터 Grade 8까지의 이론을 표 몇 장에. 줄마다 그걸 배우는 방으로 가는 문.'],""",
  """  'reference': ['한눈에 보기', 'Beginner부터 Grade 8까지의 이론과 기호, 용어, 시대, 악기를 표 몇 장에. 줄마다 그걸 배우는 방으로 가는 문.'],""")
R("""title: 'Reference', blurb: 'The whole of the theory on a few tables, Beginner to Grade 8; each row a door into its room.',""",
  """title: 'Reference', blurb: 'The whole of the theory, the signs, the words, the periods and the instruments on a few tables, Beginner to Grade 8; each row a door into its room.',""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok reference ED', len(s))
