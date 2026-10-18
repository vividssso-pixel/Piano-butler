import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 494 |')]
assert len(idx) == 1, 'row494'
row = ("| 495 | 2026-10-19 | **Concept book 'Scales and keys' rebuilt to follow the finder steps (her 06:20 'yes').** The printed book (`?book=concept&ch=p-scales`) is now nine pages: an opener, one page per step of the Key finder (sharps, flats, major and minor, before a piece) and of the Scale finder (white keys, black keys, all twelve), then five checks; each step page is one picture and one line, with the same words as the tool. On screen the book is the step screens themselves: Home's Learn and the Toolbox concept-book card open the Key finder, Try opens the Scale finder; the hidden `cb-p-scales` id still resolves (to the Key finder) so old links and QR codes work. The old nine pages stay in the file as `cbScalesPagesOld`, unused. Source `patch495.py`. "
"Full rule-15 review by one fresh reviewer (theory EN and KO, layout of all nine pages, links, leftovers): no wrong music facts; fixed the finger-group colour legend shown on the D♭ page where it does not fit, the Print link that always asked for English, and two Korean/English wordings. "
"**Open for her:** whether to delete the old hidden pages for good; the 'Reading a piece' map stays parked. |")
lines.insert(idx[0] + 1, row)
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('ok')
