import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
# Build Z (the decision board's build queue, item 3; the curriculum plan's decision 5, 'the duplicate pairs become one each'):
# three rooms listed the same lesson twice under one name. Each now shows once: the chapter's own step (the one its Lesson
# Book uses) stays; the older twin is hidden from the lists but still opens from an old link or a teacher's saved set.
rep("""  { id: 'size-pitch', ch: 'pitch-range', title""", """  { id: 'size-pitch', ch: 'pitch-range', hidden: true, title""")   # twin of spr-big
rep("""  { id: 'range-chart', ch: 'pitch-range', title""", """  { id: 'range-chart', ch: 'pitch-range', hidden: true, title""")   # twin of spr-range
rep("""  { id: 'tie-slur', ch: 'dynamics', title""", """  { id: 'tie-slur', ch: 'dynamics', hidden: true, title""")   # twin of sdy-tie
rep("""  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-range', 'size-pitch', 'string-lab', 'range-chart', 'hz-explorer', 'octave-ladder'],""",
    """  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-range', 'string-lab', 'hz-explorer', 'octave-ladder'],   // Build Z: size-pitch, range-chart were twins""")
rep("""  'dynamics': ['sdy-pf', 'sdy-ladder', 'sdy-hair', 'sdy-touch', 'sdy-tie', 'dyn-order', 'hairpin', 'touch-ear', 'touch-lengths', 'tie-slur', 'pedal'],""",
    """  'dynamics': ['sdy-pf', 'sdy-ladder', 'sdy-hair', 'sdy-touch', 'sdy-tie', 'dyn-order', 'hairpin', 'touch-ear', 'touch-lengths', 'pedal'],   // Build Z: tie-slur was sdy-tie's twin""")
rep("""  ['can’t tell legato from staccato', ['touch-lengths', 'touch-ear', 'tie-slur']],""", """  ['can’t tell legato from staccato', ['touch-lengths', 'touch-ear', 'sdy-tie']],""")
rep("""  ['r8', 'read', 'Repeats, D.C. and ties', ['road-map', 'sdy-tie', 'tie-slur']],""", """  ['r8', 'read', 'Repeats, D.C. and ties', ['road-map', 'sdy-tie']],""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
