#!/usr/bin/env python3
# Phase 426 on the site: the lesson guides' front page shows the townhouse (it showed the street, Phase 425), its
# sharing picture too; the guide pages load the house's classical letters (Cinzel, Cormorant Garamond) and Playfair's
# italic; the wide house is held to a readable width.   python3 site426.py <repo root> <this x dir>
import sys, os, shutil
root, x = sys.argv[1], sys.argv[2]
def cp(a, b): shutil.copyfile(os.path.join(x, a), os.path.join(root, b)); print('copy', b)
cp('svg/index/house-wide.svg', 'tools/lessons/svg/index/house-wide.svg')
cp('svg/index/house-tall.svg', 'tools/lessons/svg/index/house-tall.svg')
cp('img/house.jpg', 'lessons/img/house.jpg')
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if s.count(a) != 1: raise SystemExit(rel + ': ' + a[:70] + ' found %d' % s.count(a))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('words', rel)
edit('tools/lessons/src/index.html', [
    ('"title": "Piano Lesson Guides for Young Beginners: the Piano Butler\'s Street | Piano Butler"', '"title": "Piano Lesson Guides for Young Beginners: the Piano Butler\'s House | Piano Butler"'),
    ('"h1": "The Piano Butler\'s street"', '"h1": "The Piano Butler\'s house"'),
    ('as the windows of one street. Each open window has a free guide page', 'as the rooms of one house. Each open room has a free guide page'),
    ('<div class="kicker">26 chapters &middot; one window each</div>', '<div class="kicker">26 chapters &middot; one room each</div>'),
    ('<h1>The Piano Butler&rsquo;s street</h1>', '<h1>The Piano Butler&rsquo;s house</h1>'),
    ('Every building on the street is a stage and every window is a chapter, from the Lodge at the foot of the street to the Museum at the top.',
     'Every floor of the house is a stage and every room is a chapter: your butler meets you in the hall, and you go up, floor by floor.'),
    ('Windows in dark ink have a guide page. The grey windows are still being written', 'Rooms in dark ink have a guide page. The grey rooms are still being written'),
    ('<h2>Open windows</h2>', '<h2>Open rooms</h2>'),
    ('in the same order as the street.', 'in the same order as the house.')])
edit('tools/lessons/build.py', [
    ('family=Playfair+Display:wght@700;800;900&display=swap', 'family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700;1,800&family=Cinzel:wght@700&family=Cormorant+Garamond:ital,wght@0,700;1,700&display=swap'),
    ('.house-wide {{ display:none; }}', '.house-wide {{ display:none; max-width:680px; margin-left:auto; margin-right:auto; }}')])
p = os.path.join(root, 'tools/lessons/README.md'); s = open(p, encoding='utf-8').read()
a = s[s.index("## The front page: the Piano Butler's street"):s.index('The drawing\'s links stay out of the tab order')]
b = """## The front page: the Piano Butler's house (`lessons/index.html`)

`src/index.html` is the guide pages' front page: the townhouse from the app (Phase 426; before it a street, Phase 425,
and a first house, Phases 377-424), one floor per stage and one room per chapter. Rooms with a guide page are drawn
in dark ink and link to it; the others are grey. When a chapter's page goes final:
1. redraw the house with the app's own code, listing every published page:
   `BUILD=drills.tNNN.html OUT=<svg/index> node house428gen.js '{"posture-hands":"posture-and-hand-shape.html", ...}'`
   (kept in `_workspace/chapter-review/kit/`; it writes `svg/index/house-wide.svg` (the wide house, every floor's rooms
   in one row, big screens) and `house-tall.svg` (phones) and `house-og.svg`, from which
   `node houseimg428.js house-og.svg lessons/img/house.jpg` remakes the sharing picture);
2. add the chapter's card to "Open rooms" in `src/index.html`;
3. `python3 tools/lessons/build.py index --final`.
"""
s = s.replace(a, b)
for a2, b2 in [('open its window on the front page (below)', 'open its room on the front page (below)'), ('the "Open windows" list is\nthe way in', 'the "Open rooms" list is\nthe way in')]:
    if s.count(a2) != 1: raise SystemExit('README: ' + a2 + ' found %d' % s.count(a2))
    s = s.replace(a2, b2)
open(p, 'w', encoding='utf-8').write(s); print('words', p)
