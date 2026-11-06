import sys
p = sys.argv[1] + '/tools/lessons/src/first-steps.html'; s = open(p, encoding='utf-8').read()
a = 'At the very bottom lives one lonely black key with no house at all.'
assert s.count(a) == 1; s = s.replace(a, 'At the very bottom stands one lonely black key with no house at all: the lighthouse, by the sea.')
open(p, 'w', encoding='utf-8').write(s); print('guide400 ok')
