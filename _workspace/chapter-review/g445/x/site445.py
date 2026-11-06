#!/usr/bin/env python3
# Phase 445 on the site: chapter 11's guide page (lessons/tones-and-semitones.html: her G1 white half steps first, G2 the
# nearest neighbour, the hidden attic; no parents' tip, G3), its drawings and worksheet; room 11 lit on the guides' front
# page (house redrawn, sharing picture, an "Open rooms" card); the sitemap; the printables card; every guide's
# previous/next links in path order (1-26).   python3 site445.py <repo root> <this x dir>
import sys, os, shutil, glob
root, x = sys.argv[1], sys.argv[2]
def cp(a, b):
    d = os.path.join(root, b); os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copyfile(os.path.join(x, a), d); print('copy', b)
for f in sorted(glob.glob(os.path.join(x, 'svg', 'tones', '*.svg'))):
    cp(os.path.relpath(f, x), 'tools/lessons/svg/tones/' + os.path.basename(f))
cp('svg/index/house-wide.svg', 'tools/lessons/svg/index/house-wide.svg')
cp('svg/index/house-tall.svg', 'tools/lessons/svg/index/house-tall.svg')
cp('img/house.jpg', 'lessons/img/house.jpg')
cp('img/tones-worksheet.jpg', 'lessons/img/tones-worksheet.jpg')
cp('img/wb-tones.jpg', 'printables/img/wb-tones.jpg')
cp('src/tones.html', 'tools/lessons/src/tones.html')
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        if s.count(a) != 1: raise SystemExit(rel + ': ' + a[:70] + ' found %d' % s.count(a))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('words', rel)
edit('tools/lessons/src/index.html', [
    ("""and the nine notes round middle C. With a free worksheet.</p></a>\n""",
     """and the nine notes round middle C. With a free worksheet.</p></a>
    <a class="card room" href="tones-and-semitones.html"><span class="no">11</span><h3>Tones and semitones</h3><p>Half steps and whole steps, the white half steps E F and B C, one black key with two names, sharp up and flat down, and sharps and flats on the staff. With a free worksheet.</p></a>\n""")])
edit('sitemap.xml', [
    ("""    <loc>https://thepianobutler.com/lessons/index.html</loc>
    <lastmod>2026-10-11</lastmod>""", """    <loc>https://thepianobutler.com/lessons/index.html</loc>
    <lastmod>2026-10-12</lastmod>"""),
    ("""    <loc>https://thepianobutler.com/lessons/ledger-lines.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
""", """    <loc>https://thepianobutler.com/lessons/ledger-lines.html</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://thepianobutler.com/lessons/tones-and-semitones.html</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
""")])
old_blurb = 'A semitone is your very best friend -- the very next key. A tone is a friend of a friend: one key in between.'
new_blurb = 'A semitone is a half step: the very next key, black or white. A tone is a whole step: two half steps, one key in between.'
p = os.path.join(root, 'printables.html'); s = open(p, encoding='utf-8').read()
for a, b, n in [(old_blurb, new_blurb, 2),
    ('alt="Workbook page from the Tones &amp; Semitones chapter: Best friend or friend of a friend? · S or T on your own · The friendship race"', 'alt="Workbook page from the Tones &amp; Semitones chapter: H or W, from C to C · H or W, from A to A · Find every E F and B C"', 1),
    ('<p class="parts"><b>On this page:</b> Best friend or friend of a friend? · S or T on your own · The friendship race</p>', '<p class="parts"><b>On this page:</b> H or W, from C to C · H or W, from A to A · Find every E F and B C</p>', 1),
    ('<div class="topic">Chapter 7</div>\n            <h3>Tones &amp; Semitones</h3>', '<div class="topic">Chapter 11</div>\n            <h3>Tones &amp; Semitones</h3>', 1)]:
    if s.count(a) != n: raise SystemExit('printables.html: ' + a[:60] + ' found %d (want %d)' % (s.count(a), n))
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s); print('words printables.html')
# previous / next chapter in path order (Phase 436's numbers 1-26)
edit('tools/lessons/src/first-steps.html', [
    ('<div><span class="lab">Next chapter</span><a href="musical-alphabet.html">3 &middot; The Musical Alphabet</a></div>',
     '<div><span class="lab">Next chapter</span><a href="../drills.html?drill=pulse">3 &middot; Pulse &amp; Counting</a></div>')])
edit('tools/lessons/src/note-names.html', [
    ('<div><span class="lab">Previous chapter</span><a href="keyboard-patterns.html">2 &middot; Keyboard Patterns</a></div>',
     '<div><span class="lab">Previous chapter</span><a href="../drills.html?drill=pulse">3 &middot; Pulse &amp; Counting</a></div>'),
    ('<div><span class="lab">Next chapter</span><a href="reading-the-staff.html">4 &middot; Reading the Staff</a></div>',
     '<div><span class="lab">Next chapter</span><a href="../drills.html?drill=note-values">5 &middot; Notes &amp; Rests</a></div>')])
edit('tools/lessons/src/staff.html', [
    ('<div><span class="lab">Previous chapter</span><a href="musical-alphabet.html">3 &middot; The Musical Alphabet</a></div>',
     '<div><span class="lab">Previous chapter</span><a href="../drills.html?drill=note-values">5 &middot; Notes &amp; Rests</a></div>'),
    ('<div><span class="lab">Next chapter</span><a href="../drills.html?drill=whole-staff">5 &middot; The Whole Staff</a></div>',
     '<div><span class="lab">Next chapter</span><a href="../drills.html?drill=whole-staff">7 &middot; The Whole Staff</a></div>')])
edit('tools/lessons/src/ledger-lines.html', [
    ('<div><span class="lab">Previous chapter</span><a href="../drills.html?drill=whole-staff">5 &middot; The Whole Staff</a></div>',
     '<div><span class="lab">Previous chapter</span><a href="../drills.html?drill=rhythm">14 &middot; Rhythm Patterns</a></div>'),
    ('<div><span class="lab">Next chapter</span><a href="../drills.html?drill=tones">7 &middot; Tones &amp; Semitones</a></div>',
     '<div><span class="lab">Next chapter</span><a href="../drills.html?drill=scales">16 &middot; Scales</a></div>')])
