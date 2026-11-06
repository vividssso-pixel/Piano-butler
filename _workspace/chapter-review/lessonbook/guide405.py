#!/usr/bin/env python3
# Phase 405: the chapter 4 guide page goes up -- room 4 opens on the house page, chapter 3 links forward,
# and the sitemap learns the new page.
#   python3 guide405.py <repo root>
import sys, os
root = sys.argv[1]
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b, n in pairs:
        c = s.count(a)
        if c != n: raise SystemExit('%s: %r expected %d, got %d' % (rel, a[:60], n, c))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('ok', rel)

edit('tools/lessons/src/note-names.html', [(
    '<div><span class="lab">Next chapter</span><a href="../drills.html?drill=staff">4 &middot; Reading the Staff</a></div>',
    '<div><span class="lab">Next chapter</span><a href="reading-the-staff.html">4 &middot; Reading the Staff</a></div>', 1)])
edit('tools/lessons/src/index.html', [(
    '    <a class="card room" href="musical-alphabet.html"><span class="no">3</span><h3>The musical alphabet</h3><p>The seven letters A to G on the white keys, forwards and backwards, every key named at a glance, skipping a letter, and words spelled on the keys. With a free worksheet.</p></a>\n',
    '    <a class="card room" href="musical-alphabet.html"><span class="no">3</span><h3>The musical alphabet</h3><p>The seven letters A to G on the white keys, forwards and backwards, every key named at a glance, skipping a letter, and words spelled on the keys. With a free worksheet.</p></a>\n'
    '    <a class="card room" href="reading-the-staff.html"><span class="no">4</span><h3>Reading the staff</h3><p>Lines and spaces, steps and skips, the Queen&rsquo;s treble clef and the King&rsquo;s bass clef, and the nine notes round middle C. With a free worksheet.</p></a>\n', 1)])
edit('sitemap.xml', [(
    '''    <loc>https://thepianobutler.com/lessons/musical-alphabet.html</loc>
    <lastmod>2026-10-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>''',
    '''    <loc>https://thepianobutler.com/lessons/musical-alphabet.html</loc>
    <lastmod>2026-10-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://thepianobutler.com/lessons/reading-the-staff.html</loc>
    <lastmod>2026-10-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>''', 1)])
print('guide405 ok')
