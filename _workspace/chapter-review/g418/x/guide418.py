#!/usr/bin/env python3
# Phases 411-417 on the site: the four guide pages' sample worksheets are recaptured (the Workbooks were redrawn big),
# chapter 2's middle-C line says 'the left door of the 4th small house', the worksheet texts follow the set tasks,
# and printables.html's chapter 1-3 cards finally match the Workbook pages they link to (they still showed the
# pre-review pages and the old chapter names) -- each card now shows the same sample page as its guide page.
#   python3 guide418.py <repo root> <img dir>
import sys, os, shutil
root, imgs = sys.argv[1], sys.argv[2]
def edit(rel, pairs):
    p = os.path.join(root, rel); s = open(p, encoding='utf-8').read()
    for a, b, n in pairs:
        c = s.count(a)
        if c != n: raise SystemExit('%s: %r expected %d, got %d' % (rel, a[:80], n, c))
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s); print('ok', rel)

edit('tools/lessons/src/first-steps.html', [
    ('<li>I can find middle C, just left of the 4th small house</li>', '<li>I can find middle C, the left door of the 4th small house</li>', 1),
    ('alt="Worksheet page: colour the white keys under each roof, write S or B for whose house a dotted key belongs to, then draw a family of 3 and a family of 4."',
     'alt="Worksheet page: colour the white keys under each roof, write S or B for whose house a dotted key belongs to, then draw one smiley face for each white key of a small house and a big house."', 1),
    ('<p>Colour the 3 white keys under every small roof and the 4 under every big roof, decide whose house six dotted keys belong to, then draw the two families. One A4 page.</p>',
     '<p>Colour the 3 white keys under every small roof and the 4 under every big roof, decide whose house six dotted keys belong to, then draw one smiley face for each white key: 3 in the small house, 4 in the big one. One A4 page.</p>', 1)])
edit('tools/lessons/src/staff.html', [
    ('alt="Worksheet page: write L or S under line and space notes on two big staves, then draw skewers and sandwiches on two plates."',
     'alt="Worksheet page: write L or S and the line or space number under notes on two big staves, then draw skewers and sandwiches on two plates."', 1),
    ('<p>Skewer or sandwich: write L or S for ten notes on two big staves, then cook -- skewers on lines 1, 3 and 5, sandwiches in spaces 1, 2 and 4. One A4 page.</p>',
     '<p>Skewer or sandwich: write L or S for ten notes on two big staves (the last six with their number too: L3, S2), then cook -- skewers on lines 1, 3 and 5, sandwiches in spaces 1, 2 and 4. One A4 page.</p>', 1)])
edit('tools/lessons/src/note-names.html', [
    ('then draw Princess Clara, her Dog, Grandma and her Apple garden on their keys. One A4 page.</p>',
     'then draw all seven -- Princess Clara, her Dog, the Exit, the Front door, Grandma, her Apple garden and the Back door -- on their keys. One A4 page.</p>', 1)])

# printables.html: chapter 1-3 cards = the guide pages' sample pages, with today's names and parts
P = 'printables.html'
edit(P, [
    # chapter 1: Workbook page 2 (pages=1)
    ('href="drills.html?book=work&ch=posture-hands&lang=en&pages=2"', 'href="drills.html?book=work&ch=posture-hands&lang=en&pages=1"', 2),
    ('alt="Workbook page from the Posture &amp; Hand Shape chapter: Is this good sitting? · Sitting and arms · Draw yourself at the piano"',
     'alt="Workbook page from the Posture &amp; Hand Shape chapter: Is this a good set-up? · Set up at home · Draw yourself at the piano"', 1),
    ('<p class="parts"><b>On this page:</b> Is this good sitting? · Sitting and arms · Draw yourself at the piano</p>',
     '<p class="parts"><b>On this page:</b> Is this a good set-up? · Set up at home · Draw yourself at the piano</p>', 1),
    # chapter 2: Keyboard Patterns, Workbook page 3 (pages=2, unchanged)
    ('aria-label="Open the Black Keys &amp; Your First Song sample page to print"', 'aria-label="Open the Keyboard Patterns sample page to print"', 1),
    ('alt="Workbook page from the Black Keys &amp; Your First Song chapter: Which is higher? · Star the higher one · Sound pictures"',
     'alt="Workbook page from the Keyboard Patterns chapter: Who lives under each roof? · Whose house? · Who lives here?"', 1),
    ('<h3>Black Keys &amp; Your First Song</h3>', '<h3>Keyboard Patterns</h3>', 1),
    ('<p>The black keys are a map of the piano -- and your very first song lives on them. You&#x27;ll also learn to play smoothly: legato.</p>',
     '<p>The black keys make small houses and big houses -- a map of the whole piano. Find every house, high and low, and middle C, the ground between the sea and the sky.</p>', 1),
    ('<p class="parts"><b>On this page:</b> Which is higher? · Star the higher one · Sound pictures</p>',
     '<p class="parts"><b>On this page:</b> Who lives under each roof? · Whose house? · Who lives here?</p>', 1),
    # chapter 3: The Musical Alphabet, Workbook page 5 (pages=4)
    ('href="drills.html?book=work&ch=note-names&lang=en&pages=2"', 'href="drills.html?book=work&ch=note-names&lang=en&pages=4"', 2),
    ('aria-label="Open the Note Names sample page to print"', 'aria-label="Open the Musical Alphabet sample page to print"', 1),
    ('alt="Workbook page from the Note Names chapter: Find every C and F · Name the dotted keys · Lost letters"',
     'alt="Workbook page from the Musical Alphabet chapter: Who lives where? · Name it at a glance · Draw who lives here"', 1),
    ('<h3>Note Names</h3>', '<h3>The Musical Alphabet</h3>', 1),
    ('<p>The black keys are your map: groups of 2 and 3 show you where every white key is.</p>',
     '<p>Seven letters, A to G, live on the white keys -- and Princess Clara, her Dog and Grandma tell you who lives where.</p>', 1),
    ('<p class="parts"><b>On this page:</b> Find every C and F · Name the dotted keys · Lost letters</p>',
     '<p class="parts"><b>On this page:</b> Who lives where? · Name it at a glance · Draw who lives here</p>', 1),
    # chapter 4: the second part has a real title now
    ('Reading the Staff chapter: Line or space? · Your turn · Skewer plate, sandwich plate"', 'Reading the Staff chapter: Line or space? · Line or space? On your own · Skewer plate, sandwich plate"', 1),
    ('<p class="parts"><b>On this page:</b> Line or space? · Your turn · Skewer plate, sandwich plate</p>',
     '<p class="parts"><b>On this page:</b> Line or space? · Line or space? On your own · Skewer plate, sandwich plate</p>', 1),
])
# the 'jump' links near the top of printables.html point at the same sample pages
edit(P, [('book=work&ch=posture-hands&lang=en&pages=2', 'book=work&ch=posture-hands&lang=en&pages=1', 1),
         ('book=work&ch=note-names&lang=en&pages=2', 'book=work&ch=note-names&lang=en&pages=4', 1)])

# images
for f in ['posture-hands-worksheet.jpg', 'first-steps-worksheet.jpg', 'note-names-worksheet.jpg', 'reading-the-staff-worksheet.jpg']:
    shutil.copyfile(os.path.join(imgs, f), os.path.join(root, 'lessons/img', f)); print('img lessons/img/' + f)
for f in ['wb-posture-hands.jpg', 'wb-first-steps.jpg', 'wb-note-names.jpg', 'wb-staff.jpg']:
    shutil.copyfile(os.path.join(imgs, f), os.path.join(root, 'printables/img', f)); print('img printables/img/' + f)
