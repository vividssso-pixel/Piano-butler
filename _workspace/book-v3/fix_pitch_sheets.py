# Her 16 Nov (free printables check): the pitch game sheets stand alone (no book page numbers), and the crossword clues
# share one staff size, so the long Across 1 (CABBAGE) is as easy to read as the others.
import re, sys
p = sys.argv[1]; h = open(p).read()
h = re.sub(r'<div class="foot"><span>\d+</span></div>', '', h)
secs = re.findall(r'<section class="pg">.*?</section>', h, re.S); s0 = secs[0]
a = s0.index('<div class="xwrap">'); part = s0[a:]
part2 = part.replace('style="width:100%;height:auto;max-height:74px"', 'style="height:46px;width:auto;max-width:100%"').replace('style="width:100%;height:auto;max-height:70px"', 'style="height:46px;width:auto;max-width:100%"', 0)
h = h.replace(s0, s0[:a] + part2)
open(p, 'w').write(h); print('page numbers left:', len(re.findall(r'class="foot"><span>\d', h)), '| clue staves resized:', part.count('max-height:74px'))
