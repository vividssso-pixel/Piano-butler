#!/usr/bin/env python3
# Phases 442-443 on the site: the rabbit back in the chapter 1 and 2 guide heroes; the phones' house with each floor's
# rooms counted from the bottom left; 'Clara', not 'Princess Clara', on the guide pages and printables.
#   python3 site443.py <repo root> <this x dir>
import sys, os, shutil
root, x = sys.argv[1], sys.argv[2]
def cp(a, b): shutil.copyfile(os.path.join(x, a), os.path.join(root, b)); print('copy', b)
cp('svg/posture-hands/hero.svg', 'tools/lessons/svg/posture-hands/hero.svg')
cp('svg/first-steps/hero.svg', 'tools/lessons/svg/first-steps/hero.svg')
cp('svg/index/house-tall.svg', 'tools/lessons/svg/index/house-tall.svg')
cp('svg/index/house-wide.svg', 'tools/lessons/svg/index/house-wide.svg')
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b, n in pairs:
        if s.count(a) != n: raise SystemExit(rel + ': ' + a[:70] + ' found %d (want %d)' % (s.count(a), n))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('words', rel)
edit('tools/lessons/src/note-names.html', [
    ('In the small house lives Princess Clara, at the left door (C),', 'In the small house lives Clara, a little princess, at the left door (C),', 1),
    ('Princess Clara', 'Clara', 2)])
edit('tools/lessons/src/staff.html', [('Princess Clara', 'Clara', 3)])
edit('tools/lessons/src/ledger-lines.html', [('Princess Clara', 'Clara', 1)])
edit('printables.html', [('Princess Clara', 'Clara', 2)])
