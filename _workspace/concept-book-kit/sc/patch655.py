import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
old = "  'p-scale': {\n    lessons: ['sc-shape'"
assert s.count(old) == 1
new = """  'p-intervals': {
    lessons: ['ivx-ladder', 'ivx-count', 'ivx-hand', 'ivx-big', 'ivx-mh', 'ivx-tonic', 'semitone-counter', 'interval-ear', 'invert-interval', 'tritone'], check: 'intervals', tools: [], more: ['step-skip', 'interval-ruler', 'letter-hop', 'scale-intervals'],
  },
""" + old
s = s.replace(old, new)
open(dst, 'w', encoding='utf-8').write(s); print('ok')
