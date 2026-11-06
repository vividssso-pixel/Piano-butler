#!/usr/bin/env python3
# Phase 428 on the site: chapter 6's guide page (lessons/ledger-lines.html, from src/ledger-lines.html and the Lesson
# Book's own drawings), its room lit on the guides' front page (house redrawn, sharing picture, an "Open rooms" card),
# the sitemap, and the printables card (the same sample page as the guide).   python3 site428.py <repo root> <this x dir>
import sys, os, shutil, glob
root, x = sys.argv[1], sys.argv[2]
def cp(a, b):
    d = os.path.join(root, b); os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copyfile(os.path.join(x, a), d); print('copy', b)
for f in sorted(glob.glob(os.path.join(x, 'svg', 'ledger-lines', '*.svg'))):
    cp(os.path.relpath(f, x), 'tools/lessons/svg/ledger-lines/' + os.path.basename(f))
cp('svg/index/house-wide.svg', 'tools/lessons/svg/index/house-wide.svg')
cp('svg/index/house-tall.svg', 'tools/lessons/svg/index/house-tall.svg')
cp('img/house.jpg', 'lessons/img/house.jpg')
cp('img/ledger-lines-worksheet.jpg', 'lessons/img/ledger-lines-worksheet.jpg')
cp('img/wb-ledger-lines.jpg', 'printables/img/wb-ledger-lines.jpg')
cp('src/ledger-lines.html', 'tools/lessons/src/ledger-lines.html')
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if s.count(a) != 1: raise SystemExit(rel + ': ' + a[:70] + ' found %d' % s.count(a))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('words', rel)
edit('tools/lessons/src/index.html', [
    ('"updated": "2026-10-10"', '"updated": "2026-10-11"'),
    ('Updated 10 October 2026', 'Updated 11 October 2026'),
    ("""and the nine notes round middle C. With a free worksheet.</p></a>\n""",
     """and the nine notes round middle C. With a free worksheet.</p></a>
    <a class="card room" href="ledger-lines.html"><span class="no">6</span><h3>Ledger lines</h3><p>What a ledger line is and how to draw one, up into the sky over the treble staff and down into the sea under the bass staff, the notes between the staves, and five Cs to read from. With a free worksheet.</p></a>\n""")])
edit('sitemap.xml', [
    ("""    <loc>https://thepianobutler.com/lessons/index.html</loc>
    <lastmod>2026-10-09</lastmod>""", """    <loc>https://thepianobutler.com/lessons/index.html</loc>
    <lastmod>2026-10-11</lastmod>"""),
    ("""    <loc>https://thepianobutler.com/lessons/reading-the-staff.html</loc>
    <lastmod>2026-10-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
""", """    <loc>https://thepianobutler.com/lessons/reading-the-staff.html</loc>
    <lastmod>2026-10-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://thepianobutler.com/lessons/ledger-lines.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
""")])
old_blurb = 'The staff is a ladder. Ledger lines are extra rungs clipped on above and below -- so you can keep climbing: line, space, line, space.'
new_blurb = 'Ledger lines are the rungs of a ladder that lets notes climb out of the staff: up into the sky over the treble staff, down into the sea under the bass staff.'
p = os.path.join(root, 'printables.html'); s = open(p, encoding='utf-8').read()
for a, b, n in [
    ('drills.html?book=work&ch=ledger-lines&lang=en&pages=3', 'drills.html?book=work&ch=ledger-lines&lang=en&pages=1', 3),
    (old_blurb, new_blurb, 2),
    ('alt="Workbook page from the Ledger Lines chapter: Name the notes · Name them on your own · Rocket launch"', 'alt="Workbook page from the Ledger Lines chapter: Neat or not? · Draw the rungs · How many rungs?"', 1),
    ('<p class="parts"><b>On this page:</b> Name the notes · Name them on your own · Rocket launch</p>', '<p class="parts"><b>On this page:</b> Neat or not? · Draw the rungs · How many rungs?</p>', 1)]:
    if s.count(a) != n: raise SystemExit('printables.html: ' + a[:60] + ' found %d (want %d)' % (s.count(a), n))
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s); print('words printables.html')
