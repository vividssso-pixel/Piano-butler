#!/usr/bin/env python3
# Phase 436 on the site: the guide pages count their chapters in the five levels (kickers, crumbs, the front page's
# room numbers and lead), the front page's house and its sharing picture redrawn (LEVEL plaques, everything centred).
#   python3 site436.py <repo root> <this x dir>
import sys, os, shutil
root, x = sys.argv[1], sys.argv[2]
def cp(a, b): shutil.copyfile(os.path.join(x, a), os.path.join(root, b)); print('copy', b)
def edit(path, pairs):
    p = os.path.join(root, path); s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if s.count(a) != 1: raise SystemExit('%s: %d x %s' % (path, s.count(a), a[:80]))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('edit', path)
cp('svg/index/house-wide.svg', 'tools/lessons/svg/index/house-wide.svg')
cp('svg/index/house-tall.svg', 'tools/lessons/svg/index/house-tall.svg')
cp('img/house.jpg', 'lessons/img/house.jpg')
S = 'tools/lessons/src/'
edit(S + 'posture-hands.html', [('Chapter 1 of 26 &middot; Getting started', 'Chapter 1 of 26 &middot; Level 1')])
edit(S + 'first-steps.html', [('Chapter 2 of 26 &middot; Getting started', 'Chapter 2 of 26 &middot; Level 1')])
edit(S + 'note-names.html', [('&rsaquo; Chapter 3</nav>', '&rsaquo; Chapter 4</nav>'), ('Chapter 3 of 26 &middot; Getting started', 'Chapter 4 of 26 &middot; Level 1')])
edit(S + 'staff.html', [('&rsaquo; Chapter 4</nav>', '&rsaquo; Chapter 6</nav>'), ('Chapter 4 of 26 &middot; Reading notes', 'Chapter 6 of 26 &middot; Level 1')])
edit(S + 'ledger-lines.html', [('&rsaquo; Chapter 6</nav>', '&rsaquo; Chapter 15</nav>'), ('Chapter 6 of 26 &middot; Reading notes', 'Chapter 15 of 26 &middot; Level 3')])
edit(S + 'index.html', [
  ('Every floor of the house is a stage and every room is a chapter: your butler meets you in the hall, and you go up, floor by floor.',
   'The house has five floors and a room for each chapter: your butler meets you in the hall, and you go up floor by floor -- on each floor, any room first.'),
  ('"updated": "2026-10-11"', '"updated": "2026-10-12"'), ('Updated 11 October 2026', 'Updated 12 October 2026'),
  ('href="musical-alphabet.html"><span class="no">3</span>', 'href="musical-alphabet.html"><span class="no">4</span>'),
  ('href="reading-the-staff.html"><span class="no">4</span>', 'href="reading-the-staff.html"><span class="no">6</span>'),
  ('href="ledger-lines.html"><span class="no">6</span>', 'href="ledger-lines.html"><span class="no">15</span>')])
edit('tools/lessons/README.md', [('one floor per stage and one room per chapter', 'one floor per level (five, Phase 436) and one room per chapter')])
