# The Piano Butler Handbook: front matter, pp. 1-16 (her 12 Nov, "B": finish the public-ready pieces before the pilot).
# Cover, title, copyright, contents, welcome, how the pieces fit, the levels, the cast, for parents, for teachers,
# where to start, a practice week, notes. Page 17 (How to read this book) follows; nothing after it moves.
exec(open('/tmp/claude-0/pk/shape.py').read())   # helpers (rewrites the Shape and Play drafts, harmless)
import json as _fj
ZOOM = {7: 1.4, 8: 1.3, 9: 1.22, 10: 1.25, 11: 1.32, 12: 1.2, 13: 1.1, 14: 1.3}   # front matter reads large: the pages are short on purpose
def fpage(inner, n, right='ABOUT THIS BOOK', end=False):   # end: a form or a bottom-set page, exempt from the fill rule
    if n in ZOOM: inner = f'<div style="zoom:{ZOOM[n]}">{inner}</div>'
    return f'<section class="pg"{' data-end="1"' if end else ''} data-flow="F{n:02d}"><div class="top"><span>THE PIANO BUTLER HANDBOOK</span><span>{right}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'
def blank(n): return f'<section class="pg fblank" data-flow="F{n:02d}"><div class="body"></div></section>'
def bow(s=90, col='#26296b', knot='#e4572e'):
    return (f'<svg viewBox="0 0 40 24" style="width:{s}px;height:{s * 0.6:.0f}px;display:block;margin:0 auto"><path d="M2 3 L18 12 L2 21 Z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linejoin="round"/>'
            f'<path d="M38 3 L22 12 L38 21 Z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linejoin="round"/><circle cx="20" cy="12" r="2.4" fill="{knot}"/></svg>')
_s = open('/mnt/user-data/outputs/books/read/index.html').read()
CHL, _ = _fj.JSONDecoder().raw_decode(_s[_s.index('const CH = ') + 11:])
_D = open('/tmp/claude-0/house/data.js').read().split('\n')
ROOMS = {r['id']: r for r in _fj.loads(_D[0][len('const HB_ROOMS = '):].rstrip(';'))}
FLOORS = _fj.loads(_D[1][len('const HB_FLOORS = '):].rstrip(';'))

# 1 cover · 2 inside cover · 3 title
COVER = f'''<section class="pg fcover" data-end="1" data-flow="F01"><div class="fcv">
<div class="fck">The Piano Butler</div>{bow(120, '#fff', '#e4572e')}<div class="fct">Handbook</div><div class="fcd"></div>
<p class="fcs">Everything behind the music you play: reading, rhythm, expression, scales, chords, harmony, shape and style, from your first lesson to Grade 8.</p>
<div class="fcf">With the Workbook, the app and Read &amp; listen</div></div><div class="body"></div><div class="foot" style="visibility:hidden"><span></span></div></section>'''
P2 = f'''<section class="pg" data-end="1" data-flow="F02"><div class="body fown"><div class="fownb"><p class="fownh">This book belongs to</p><span class="fl"></span><p class="fownh" style="margin-top:28px">My teacher</p><span class="fl"></span><p class="fownh" style="margin-top:28px">I started on</p><span class="fl" style="width:50%"></span></div></div><div class="foot" style="visibility:hidden"><span></span></div></section>'''
P3 = f'''<section class="pg" data-end="1" data-flow="F03"><div class="body ftitle">{bow(96)}<p class="ftk">The Piano Butler</p><h1 class="fth">Handbook</h1><div class="fcd" style="background:#e4572e"></div>
<p class="fts">Music theory for pianists,<br>from the first lesson to Grade 8</p><p class="fta">Sohyun Park</p><p class="ftp">thepianobutler.com</p></div><div class="foot" style="visibility:hidden"><span></span></div></section>'''
# 4 copyright
P4 = fpage(f'''<div class="fcopy">
<p><b>The Piano Butler Handbook</b><br>Draft edition, November 2026</p>
<p>Text, music examples and drawings © 2026 Sohyun Park. All rights reserved. No part of this book may be copied, stored or shared, in print or online, without written permission, except short quotations in a review. Teachers may copy single Workbook pages for their own students.</p>
<p>The music examples are drawn from works in the public domain (traditional tunes and composers who died more than 70 years ago), newly engraved for this book.</p>
<p>Piano Butler is independent. It is not affiliated with, or endorsed by, any examination board. Grade levels in this book are a guide to the order in which ideas are usually met.</p>
<p>The Read &amp; listen narration uses computer-generated voices.</p>
<p>ISBN: to come</p>
<p class="sm">Set in Atkinson Hyperlegible and Playfair Display. Music engraved with Verovio.</p></div>''', 4, end=True)

# 5-6 contents
def toc_rows(parts):
    out = ''
    for part in parts:
        rows = [c for c in CHL if c['part'] == part]
        out += f'<div class="ftp1">{part}</div>' + ''.join(f'<div class="tr ftr"><span>{c["t"]}</span><span class="dots"></span><span>{c["pages"][0]}</span></div>' for c in rows if c['k'][-1] not in 'O')
    return out
_parts = list(dict.fromkeys(c['part'] for c in CHL))
def head_c(t, lead=''): return f'<div class="kick">About this book</div><h1>{t}</h1>' + (f'<p class="lead">{lead}</p>' if lead else '')
P5 = fpage(head_c('Contents').replace('About this book', 'The Piano Butler Handbook') + '<div class="ftoc">' + toc_rows(_parts[:4]) + '</div>', 5)
P6 = fpage('<div class="kick fk2">Contents · continued</div><div class="ftoc">' + toc_rows(_parts[4:]) + '</div>', 6)

# 7 welcome
P7 = fpage(head_c('Welcome', 'This book explains the music you play: what the signs on the page mean, why a piece sounds the way it does, and how to play it well. It is the whole picture in one place, for you to dip into whenever a piece asks a question.') + f'''
{h3('Who it is for')}
<div class="fnum"><div><span>1</span><p><b>Students</b> from the first lesson to Grade 8, reading with a teacher or a parent, or on their own.</p></div><div><span>2</span><p><b>Adults</b> coming back to the piano, who want the reasons, not only the rules.</p></div><div><span>3</span><p><b>Teachers</b> who want one clear explanation of each idea, with exercises to match.</p></div></div>
{h3('Three promises')}
<div class="fprom"><div><b>A picture first.</b><span>Every idea starts with something you can see, then something you can play.</span></div><div><b>Said once, clearly.</b><span>Each idea has one home in this book. Other pages point to it instead of saying it again.</span></div><div><b>Always at the piano.</b><span>Every chapter ends at the keys: a ten-second Try it, a tune you know, a game.</span></div></div>
{thinkt('A good butler keeps the whole house in order, so that you can simply enjoy living in it. This book keeps the theory in order, so that you can simply enjoy playing.')}''', 7)

# 8 how the pieces fit
P8 = fpage(head_c('How the pieces fit', 'The Handbook is the centre. Everything else is cut from it, so an idea always looks and sounds the same wherever you meet it.') + '''
<div class="ffit"><div class="ffc"><b>The Handbook</b><span>the whole picture, by topic</span></div>
<div class="ffg"><div><b>The Workbook</b><span>two pages to write in for every chapter: Learn, then Use</span></div>
<div><b>Read &amp; listen</b><span>every chapter read aloud, the page moving with the voice; scan a code or open it in the app</span></div>
<div><b>The house</b><span>in the app: the chapters in the order you need them, a floor for each level, a room for each step, with drills</span></div>
<div><b>Level books</b><span>one floor of the house in print: one spread per room, then practise</span></div></div></div>
<h3>Which one when?</h3>''' + tbl(['When you want to…', 'Use'], [['understand an idea, or look it up', '<b>the Handbook</b>'], ['check you really know it', '<b>the Workbook</b>'], ['hear it explained, at home or on the bus', '<b>Read &amp; listen</b>'], ['know what to learn next', '<b>the house</b>, or your <b>Level book</b>'], ['practise it until it is easy', '<b>the drills</b> in the app']], ['58%', '42%']), 8)

# 9-10 the levels
def floor_block(f):
    rows = ''.join(f'<div class="flr"><span>{ROOMS[i]["en"] + (": " + ROOMS[i]["again"][0] if ROOMS[i].get("again") else "")}</span><i>{ROOMS[i]["pages"]}</i></div>' for i in f['ids'])
    return f'<div class="flv"><div class="flh"><b>{f["en"][0]}</b><span>{f["en"][1]}</span></div>{rows}</div>'
P9 = fpage(head_c('The levels', 'The house in the app puts the chapters in the order you need them, one floor for each level. Here are the floors, with the Handbook pages for each room. In the chapters, “First met: Level 0” means the Beginner floor, “Level ½” Prelim, and “Level 1” to “Level 8” Grades 1 to 8.') + '<div class="flvs">' + ''.join(floor_block(f) for f in FLOORS[:3]) + '</div>', 9)
P10 = fpage('<div class="kick fk2">The levels · continued</div><div class="flvs">' + ''.join(floor_block(f) for f in FLOORS[3:]) + '</div><p class="sm" style="margin-top:12px">A room marked with a second title, such as “a step further”, comes back to a chapter you have met before and goes one step deeper. The rest of the chapter can wait for its own level.</p>', 10)

# 11 the cast
CAST = [('The Butler', 'your guide', 'Explains every chapter, calmly, one step at a time. He is never in a hurry.'),
        ('Clara', 'the student', 'Asks the questions you might be thinking, and sometimes gets them wrong, so you do not have to.'),
        ('The Queen', 'the treble clef', 'Rules the high notes. Her curl wraps round line 2, the note G.'),
        ('The King', 'the bass clef', 'Rules the low notes. His two dots sit either side of line 4, the note F.'),
        ('The Doorkeeper', 'the key signature', 'Stands at the start of every line and reads out the sharps or flats for the whole piece.'),
        ('The Guest', 'an accidental', 'Arrives in one bar wearing a sharp or flat hat, and leaves at the bar line. A natural: the hat comes off.'),
        ('The Stationmaster', 'the time signature', 'Checks the ticket: how many beats in each carriage, and that every carriage is full.')]
P11 = fpage(head_c('Meet the cast', 'You will hear these voices in Read &amp; listen and meet them in the Think of it boxes. Each one stands for an idea, so the idea is easy to remember.') + '<div class="fcast">' + ''.join(f'<div><b>{a}</b><i>{b}</i><span>{c}</span></div>' for a, b, c in CAST) + '</div>', 11)

# 12 for parents
P12 = fpage(head_c('For parents', 'You do not need to read music to help. Ten minutes, twice a week, is enough.') + f'''
{h3('Each week')}
<div class="fnum"><div><span>1</span><p><b>Listen together.</b> Scan the code on this week’s page, or open Read &amp; listen in the app. Most rooms take three to five minutes.</p></div><div><span>2</span><p><b>One page to write.</b> The Workbook or Level book page for the same room. The first answer is always done, as an example.</p></div><div><span>3</span><p><b>Ask one question.</b> "What is the secret?" If your child can say the red box in their own words, the room is learned.</p></div></div>
{h3('Good to know')}
{tbl(['If…', 'Try this'], [['the page looks hard', 'Read only the secret and play the Try it. The rest can wait for the lesson.'], ['your child is tired', 'Listen only, no writing. Hearing it once already helps.'], ['you missed a week', 'Do nothing extra. The teacher will pick it up in the lesson.'], ['your child asks something you cannot answer', 'Write it down for the teacher. A good question is worth more than a right answer.']], ['36%', '64%'])}
{try10(bow(60), 'Ask: "Show me."', 'After any page, ask your child to show you the idea at the piano. Teaching it to you is the best practice there is.')}''', 12)

# 13 for teachers
P13 = fpage(head_c('For teachers', 'The book is built so that theory happens at home and the lesson stays at the piano. Set one room a week; check it in two minutes.') + f'''
{h3('In a 30-minute lesson')}
{tbl(['When', 'If the room was done at home', 'If it was not'], [['First 2–3 min', 'Check the page; ask for the secret in the student’s own words.', 'Read the secret and the Example together (3 min).'], ['Next 2 min', 'Find the idea in the piece being learned.', 'The same: always in the piece.'], ['The rest', 'Pieces and technique.', 'Pieces and technique.'], ['Last minute', 'Send the next room.', 'Send the same room again, with the next.']], ['18%', '41%', '41%'])}
{h3('Good habits')}
<div class="fprom"><div><b>Five minutes at most.</b><span>If theory was not done, it never takes more than five minutes of the lesson.</span></div><div><b>Always in the piece.</b><span>The idea is found in the music the student is playing, every week.</span></div><div><b>One room at a time.</b><span>The house orders the rooms; a Level book prints one floor.</span></div></div>
{h3('Reading the boxes in a lesson')}
{tbl(['Box', 'Use it for'], [['<b>The secret</b>', 'the two-minute check: can the student say it in their own words?'], ['<b>Example</b>', 'the three-minute catch-up when the room was not done'], ['<b>Try it</b>', 'a warm-up at the start of the lesson'], ['<b>Game</b>', 'a group lesson, or the last two minutes'], ['<b>Trap</b>', 'when the same mistake comes back in a piece']], ['26%', '74%'])}
<p class="sm" style="margin-top:10px">Not sure where a new student fits? Use the <b>Handbook check</b> in the app, a short quiz that names the first chapter to read, or <b>Where do I start?</b> on p. 14.</p>''', 13)

# 14 where do I start
P14 = fpage(head_c('Where do I start?', 'You do not have to start at page 1. Find your place, then read from there.') + f'''
{tbl(['If you are…', 'Start at'], [['brand new to the piano', f'<b>Before you play</b>, p. {PM.PAGE["B1"]}, then the Beginner floor'], ['reading simple pieces already', 'the <b>Handbook check</b> (free, in the app): it names your first chapter'], ['preparing for a grade', 'your floor in <b>The levels</b>, p. 9'], ['stuck on one thing in a piece', f'the <b>Glossary and index</b>, p. {PM.PAGE["X"] + 2}, or the Tips page at the end of each part'], ['coming back after years away', 'each Part’s <b>opening map</b>: read the secrets only, and stop where they stop making sense']], ['42%', '58%'])}
{h3('The part openers')}
<p>Each Part opens with a map: every chapter in one line, with its secret. Read a map in two minutes and you know what the Part holds.</p>
{h3('A good week')}
<div class="fnum"><div><span>1</span><p><b>One room.</b> Listen once, read the page, write the Workbook page.</p></div><div><span>2</span><p><b>Find it in your piece.</b> The idea is somewhere in the music you are playing.</p></div><div><span>3</span><p><b>Drill it for five minutes</b> in the app, on two or three days.</p></div></div>
{thinkt('A map does not walk for you, but it stops you walking in circles.')}''', 14)

# 15 my practice week
P15 = fpage(head_c('My practice week', 'Copy this page, or draw your own. Tick a box each day you practise.') + tbl(['', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], [[f'<b>{x}</b>'] + ['<span class="fbox"></span>'] * 7 for x in ('30-second check', 'Warm-ups', 'This week’s room', 'Scales', 'My piece', 'Something just for fun')], ['30%'] + ['10%'] * 7) + f'''
{h3('This week')}
<div class="fwk"><div><b>Room</b><span class="fl"></span></div><div><b>Piece</b><span class="fl"></span></div><div><b>One thing to fix</b><span class="fl"></span></div><div><b>My teacher says</b><span class="fl"></span><span class="fl"></span></div></div>''', 15, end=True)
# 16 notes
P16 = fpage(head_c('My questions', 'Write down anything you want to ask in your next lesson.') + '<div class="fnotes">' + '<span class="fl"></span>' * 18 + '</div>', 16, end=True)

css += """
.fcover{background:#26296b!important} .fcover .fcv{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 70px;color:#fff;border:3px double rgba(255,255,255,.55);margin:28px}
.fck{font-size:15px;letter-spacing:.32em;text-transform:uppercase;margin-bottom:26px;color:#fff} .fct{font-family:'Playfair Display',PF,serif;font-weight:900;font-size:78px;line-height:1;margin-top:22px;color:#fff}
.fcd{width:90px;height:3px;background:#e4572e;margin:22px auto} .fcs{font-size:17px;line-height:1.5;max-width:30em;color:#e8e7f3} .fcf{position:absolute;bottom:60px;left:0;right:0;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#c9c7e6}
.fown{display:flex;align-items:flex-end;justify-content:center} .fownb{width:70%;margin-bottom:120px} .fownh{font-family:'Playfair Display',PF,serif;font-size:22px;color:#26296b;margin:0 0 6px}
.fl{display:block;border-bottom:1.5px solid #c9c7dc;height:30px;width:100%}
.ftitle{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;height:100%} .ftk{font-size:14px;letter-spacing:.32em;text-transform:uppercase;color:#6d6f9c;margin:24px 0 0} .fth{font-size:68px!important;margin:6px 0 0!important}
.fts{font-size:18px;color:#26296b;line-height:1.5} .fta{font-size:16px;font-weight:700;color:#26296b;margin-top:70px} .ftp{font-size:13px;color:#6d6f9c;letter-spacing:.1em}
.fcopy{margin-top:auto;font-size:12.5px;line-height:1.55;color:#4a4d7f;display:flex;flex-direction:column;justify-content:flex-end;height:100%} .fcopy p{margin:0 0 10px}
.ftoc{columns:1} .ftp1{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e;margin:12px 0 3px} .ftr{font-size:13.5px;padding:1.5px 0}
.fprom{display:flex;flex-direction:column;gap:8px;margin:6px 0 12px} .fprom>div{display:grid;grid-template-columns:170px 1fr;gap:10px;font-size:14px;border-left:3px solid #e4572e;padding:4px 0 4px 12px} .fprom b{color:#26296b} .fprom span{color:#4a4d7f}
.ffit{display:flex;flex-direction:column;align-items:center;gap:12px;margin:12px 0 14px} .ffc{background:#26296b;color:#fff;border-radius:10px;padding:14px 30px;text-align:center} .ffc b{display:block;font-size:20px} .ffc span{font-size:12.5px;color:#d9d8ee}
.ffg{display:grid;grid-template-columns:1fr 1fr;gap:10px;width:100%} .ffg>div{border:1.5px solid #e3e1ee;border-radius:8px;padding:10px 12px;display:flex;flex-direction:column;gap:3px} .ffg b{color:#26296b;font-size:15px} .ffg span{font-size:13px;color:#4a4d7f;line-height:1.35}
.flvs{columns:2;column-gap:18px} .flv{break-inside:avoid;margin-bottom:12px} .flh{border-bottom:2px solid #26296b;padding-bottom:3px;margin-bottom:3px} .flh b{display:block;font-size:15px;color:#26296b} .flh span{font-size:11px;color:#6d6f9c;line-height:1.3;display:block}
.flr{display:flex;justify-content:space-between;gap:8px;font-size:12px;padding:1.5px 0;border-bottom:1px dotted #e3e1ee;color:#26296b} .flr i{font-style:normal;color:#6d6f9c;white-space:nowrap}
.fcast{display:grid;grid-template-columns:1fr 1fr;gap:10px} .fcast>div{border:1.5px solid #e3e1ee;border-radius:8px;padding:10px 12px;display:flex;flex-direction:column;gap:2px} .fcast b{font-size:16px;color:#26296b} .fcast i{font-style:normal;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#e4572e} .fcast span{font-size:13.5px;color:#4a4d7f;line-height:1.4}
.fnum{display:flex;flex-direction:column;gap:8px;margin:6px 0 12px} .fnum>div{display:grid;grid-template-columns:28px 1fr;gap:10px;align-items:start} .fnum>div>span{width:24px;height:24px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center} .fnum p{margin:0;font-size:14.5px;line-height:1.45} .fbox{display:inline-block;width:18px;height:18px;border:1.5px solid #c9c7dc;border-radius:4px}
.fwk{display:grid;grid-template-columns:1fr 1fr;gap:6px 20px} .fwk b{font-size:13px;color:#26296b} .fnotes{margin-top:10px}
"""
FRONT = COVER + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9 + P10 + P11 + P12 + P13 + P14 + P15 + P16
open('/mnt/user-data/outputs/house-rooms/handbook-front.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{OPENCSS}</style></head><body>{FRONT}{FLOWJS}</body></html>')
print('ok front')
