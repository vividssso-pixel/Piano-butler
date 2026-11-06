#!/usr/bin/env python3
# Phase 425 on the site: the guide drawings re-exported from the new book (chess pieces, no beige, chapter 4's labels),
# the front page's street, the worksheets and printables cards recaptured, the front page's words for the street.
#   python3 site425.py <repo root> <this x dir>
import sys, os, shutil, subprocess, glob
root, x = sys.argv[1], sys.argv[2]
def cp(a, b): shutil.copyfile(os.path.join(x, a), os.path.join(root, b)); print('copy', b)
for ch in ['first-steps', 'note-names', 'staff', 'index']:
    for f in sorted(glob.glob(os.path.join(x, 'svg', ch, '*.svg'))):
        cp(os.path.join('svg', ch, os.path.basename(f)), os.path.join('tools/lessons/svg', ch, os.path.basename(f)))
for f in sorted(os.listdir(os.path.join(x, 'img/lessons'))): cp('img/lessons/' + f, 'lessons/img/' + f)
for f in sorted(os.listdir(os.path.join(x, 'img/printables'))): cp('img/printables/' + f, 'printables/img/' + f)
subprocess.run(['node', os.path.join(x, 'fixph425.js'), os.path.join(root, 'tools/lessons/svg/posture-hands'), os.path.join(x, 'src', 'art')], check=True)
p = os.path.join(root, 'tools/lessons/src/index.html'); s = open(p, encoding='utf-8').read()
for a, b in [
    ('"title": "Piano Lesson Guides for Young Beginners: the Piano Butler\'s House | Piano Butler"', '"title": "Piano Lesson Guides for Young Beginners: the Piano Butler\'s Street | Piano Butler"'),
    ('"h1": "The Piano Butler\'s house"', '"h1": "The Piano Butler\'s street"'),
    ('as the rooms of one house. Each open room has a free guide page', 'as the windows of one street. Each open window has a free guide page'),
    ('"updated": "2026-10-09"', '"updated": "2026-10-10"'),
    ('<div class="kicker">26 chapters &middot; one room each</div>', '<div class="kicker">26 chapters &middot; one window each</div>'),
    ('<h1>The Piano Butler&rsquo;s house</h1>', '<h1>The Piano Butler&rsquo;s street</h1>'),
    ('Every floor of the house is a stage and every room is a chapter, from the front door up to the attic.', 'Every building on the street is a stage and every window is a chapter, from the Lodge at the foot of the street to the Museum at the top.'),
    ('Updated 9 October 2026', 'Updated 10 October 2026'),
    ('Rooms in dark ink have a guide page. The grey rooms are still being written', 'Windows in dark ink have a guide page. The grey windows are still being written'),
    ('<h2>Open rooms</h2>', '<h2>Open windows</h2>'),
    ('in the same order as the house.', 'in the same order as the street.')]:
    if s.count(a) != 1: raise SystemExit('index.html: ' + a[:60] + ' found %d' % s.count(a))
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s); print('words', p)
p = os.path.join(root, 'tools/lessons/README.md'); s = open(p, encoding='utf-8').read()
a = s[s.index("## The front page: the Piano Butler's house"):s.index('The drawing\'s links stay out of the tab order')]
b = """## The front page: the Piano Butler's street (`lessons/index.html`)

`src/index.html` is the guide pages' front page: the street from the app (Phase 425; it was a house, Phases 377-424),
one window per chapter. Windows with a guide page are drawn in dark ink and link to it; the others are grey. When a
chapter's page goes final:
1. redraw the street with the app's own code, listing every published page:
   `BUILD=drills.tNNN.html OUT=<svg/index> node street425gen.js '{"posture-hands":"posture-and-hand-shape.html", ...}'`
   (kept in `_workspace/chapter-review/kit/`; it writes `svg/index/house-wide.svg` (three stretches of street, big
   screens) and `house-tall.svg` (one street, phones) -- the file names stay -- and `house-og.svg`, from which
   `node streetimg425.js house-og.svg lessons/img/house.jpg` remakes the sharing picture);
2. add the chapter's card to "Open windows" in `src/index.html`;
3. `python3 tools/lessons/build.py index --final`.
"""
s = s.replace(a, b); s = s.replace('open its room on the front page (below)', 'open its window on the front page (below)')
s = s.replace('the "Open rooms" list is\nthe way in', 'the "Open windows" list is\nthe way in')
open(p, 'w', encoding='utf-8').write(s); print('words', p)
