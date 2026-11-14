# Her 14 Nov ("바로 유료 판매"): the Workbook's own front matter (it had none): cover, title, copyright, how to use it
# with the Handbook, contents. Built from the Handbook's front-matter pages so the two books look like a set.
# Runs after wbfix.py, which writes the page sequence to workbook-pages.json.
import re, json
H = '/mnt/user-data/outputs/house-rooms/'
J = json.load(open(H + 'workbook-pages.json')); OFF = J['off']
src = open(H + 'handbook-front.html').read()
head = src[:src.index('<section')]
S = re.findall(r'<section\b[^>]*>.*?</section>', src, re.S)
cover, owner, title, copy = S[0], S[1], S[2], S[3]
cover = cover.replace('<div class="fct">Handbook</div>', '<div class="fct">Workbook</div>')
cover = re.sub(r'<p class="fcs">.*?</p>', '<p class="fcs">Pages to write in for every chapter of the Handbook: learn it, use it, check it. With answers.</p>', cover, flags=re.S)
cover = re.sub(r'<div class="fcf">.*?</div>', '<div class="fcf">With the Handbook, the app and Read &amp; listen</div>', cover, flags=re.S)
title = title.replace('<h1 class="fth">Handbook</h1>', '<h1 class="fth">Workbook</h1>').replace('Music theory for pianists,<br>from the first lesson to Grade 8', 'Written practice for the Handbook,<br>from the first lesson to Grade 8')
COPY = '''<div class="fcopy">
<p><b>The Piano Butler Workbook</b><br>First edition, 2026</p>
<p>Text, music examples and drawings © 2026 Sohyun Park. All rights reserved. No part of this book may be copied, stored or shared, in print or online, without written permission, except short quotations in a review.</p>
<p>Teachers may copy single Workbook pages for their own students.</p>
<p>The music examples are drawn from works in the public domain (traditional tunes and composers who died more than 70 years ago), newly engraved for this book.</p>
<p>Piano Butler is independent. It is not affiliated with, or endorsed by, any examination board. Grade levels are a guide to the order in which ideas are usually met.</p>
<p class="sm">Set in Atkinson Hyperlegible and Playfair Display. Music engraved with Verovio.</p></div>'''
copy = re.sub(r'<div class="fcopy">.*?</div></div>', COPY + '</div>', copy, flags=re.S).replace('THE PIANO BUTLER HANDBOOK', 'THE PIANO BUTLER WORKBOOK').replace('<div class="foot"><span>4</span></div>', '<div class="foot"><span>3</span></div>')
NAMES = [('workbook-before', 'Before you play', 'Sitting, hand shape, finger numbers'), ('workbook-pitch', 'Pitch', 'Handbook Part I'), ('workbook-time2', 'Time', 'Handbook Part II'),
         ('workbook-expression', 'Expression', 'Handbook Part III'), ('workbook-scales', 'Scales and keys', 'Handbook Part IV'), ('workbook-harmony', 'Chords and harmony', 'Handbook Parts V and VI'),
         ('workbook-shape', 'Shape and style', 'Handbook Part VII'), ('workbook-play', 'Playing and listening', 'Handbook Part VIII')]
rows = ''.join(f'<tr><td><b>{n}</b></td><td>{d}</td><td style="text-align:right">{OFF[f] + 1}</td></tr>' for f, n, d in NAMES)
use = f'''<section class="pg" data-end="1"><div class="top"><span>THE PIANO BUTLER WORKBOOK</span><span>HOW TO USE THIS BOOK</span></div><div class="rule"></div><div class="body"><div class="fcopy" style="font-size:15px;line-height:1.5">
<h2 style="font-family:'PF',Georgia,serif;font-size:30px;margin:0 0 10px;color:#26296b">How to use this book</h2>
<p><b>Read first, then write.</b> Every chapter of the Handbook has its pages here. The running head at the top of each page names the Handbook page it goes with.</p>
<p><b>Learn, then Use.</b> The Learn page checks the idea; the Use page puts it to work, with something to play. Scales and keys has one page for each chapter.</p>
<p><b>The first one is done.</b> The first answer of most exercises is filled in red, so you can see what to do.</p>
<p><b>Stars</b> show how hard an exercise is: ★ to ★★★.</p>
<p><b>Remember the story?</b> A question about the chapter’s story, from the Handbook or Read &amp; listen. The answer is in the Answers.</p>
<p><b>Review, My progress and Answers</b> close every part (Before you play is marked with the Pitch answers). Do the Review without help, then mark it with the Answers.</p>
<h2 style="font-family:'PF',Georgia,serif;font-size:24px;margin:22px 0 8px;color:#26296b">Contents</h2>
<table class="ht" style="width:100%"><tbody>{rows}</tbody></table></div></div><div class="foot"><span>4</span></div></section>'''
h = head + cover + title.replace('<div class="foot" style="visibility:hidden"><span></span></div>', '<div class="foot" style="visibility:hidden"><span></span></div>') + copy + use + '</body></html>'
open(H + 'workbook-front.html', 'w').write(h)
print('wbfront', len(re.findall(r'<section', h)), 'pages')
