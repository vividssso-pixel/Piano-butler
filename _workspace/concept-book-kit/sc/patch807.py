"""Build EE (the rest of call 39, her 02:09; her 20:30 'it has to make sense: only the ones better changed'): the staff under
the 7th-chord keyboards of Arpeggios and Progressions, Grades 6 to 8 (the dominant 7th and the diminished 7th of a key, the
dominant 7th in its four positions): the notes in 3rds on the treble staff, spelt as the chips above spell them; in the
'of a key' pads each note joins the staff as it is found (the chips keep the names hidden till then), in the four positions
the position's five notes with its first in coral. Code in sc/run43.code.js."""
import sys, os
src, dst = sys.argv[1], sys.argv[2]
here = os.path.dirname(os.path.abspath(__file__))
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
CODE = open(os.path.join(here, 'run43.code.js'), encoding='utf-8').read()
R("""// Build DQ (her 01:48): note by note, do the hands go together?""", CODE + """// Build DQ (her 01:48): note by note, do the hands go together?""")
# the dominant 7th and the diminished 7th of a key: its four notes, the one to find next in coral
R("""onTap={tap} up={done && F && F.R ? Object.fromEntries(N.map((x, j) => [x, F.R[j]])) : {}} label={t('Build the chord', '화음 쌓기')}/>""",
  """onTap={tap} up={done && F && F.R ? Object.fromEntries(N.map((x, j) => [x, F.R[j]])) : {}} label={t('Build the chord', '화음 쌓기')}/>
      {lbScreen() && got > 0 && <SpRunStaff label={(kind === 'dom' ? t('The dominant 7th of ', '딸림7화음: ') : t('The diminished 7th of ', '감7화음: ')) + KN} rows={[{ hand: 'R', keys: N.slice(0, got), names: nm.slice(0, got) }]}/>}""")
# the dominant 7th from every note: the position on the staff, its first note in coral
R("""onTap={tap} label={t('Find the first note', '첫 음 찾기')}/>""",
  """onTap={tap} label={t('Find the first note', '첫 음 찾기')}/>
      {lbScreen() && <SpRunStaff label={t(D7_POS[inv][0], D7_POS[inv][1])} rows={[{ hand: 'R', keys: [0, 1, 2, 3, 4].map(j => N[(inv + j) % 4] + 12 * Math.floor((inv + j) / 4)), names: [0, 1, 2, 3, 4].map(j => nm[(inv + j) % 4]), hl: [0] }]}/>}""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok EE', len(s))
