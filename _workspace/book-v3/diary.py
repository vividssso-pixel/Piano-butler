# The Piano Butler Practice Diary (her 16 Nov: free download; a richer version can be sold later).
# Built in the Handbook's own look (front-matter styles): a week on every page, plus the pages teachers and parents ask for.
import re, json
F = open('/mnt/user-data/outputs/pilot/full/front.html').read()
head = F[:F.index('<section')]; S = re.findall(r'<section\b.*?</section>', F, re.S)
NM = json.load(open('/tmp/claude-0/pk/newmap.json'))
CSS = '''<style>
.dg{display:grid;grid-template-columns:1fr 1fr;gap:10px 22px}.dl{border-bottom:1px solid #c9cbe0;height:30px}.dlab{font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#8a8cb0;margin-top:10px}
.tbox{border:1.5px solid #d9dbea;border-radius:10px;padding:10px 12px;min-height:330px}.tbox b{display:block;color:#e4572e;font-size:12px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:6px}
.ht td.c{text-align:center}.mins td{height:26px}.wkh{display:flex;justify-content:space-between;align-items:baseline}.wkh .dt{font-size:13px;color:#6d6f9c}
.chk{columns:2;column-gap:24px;font-size:12px}.chk div{display:flex;gap:8px;align-items:center;padding:2px 0;border-bottom:1px dotted #e3e1ee;break-inside:avoid}.chk .p{margin-left:auto;color:#8a8cb0}.chk h4{margin:8px 0 2px;font-size:12px;color:#e4572e;letter-spacing:.08em;text-transform:uppercase;break-after:avoid}
</style>'''
pages = []
def page(body, num, right='PRACTICE DIARY', z=1.0):
    pages.append(f'<section class="pg"><div class="top"><span>THE PIANO BUTLER</span><span>{right}</span></div><div class="rule"></div><div class="body"><div style="zoom:{z}">{body}</div></div><div class="foot"><span>{num}</span></div></section>')
box = '<span class="fbox"></span>'
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
def grid(rows, mins=True):
    th = ''.join(f'<th>{d}</th>' for d in DAYS)
    # her 16 Nov: a pupil may have six pieces or more, so 'Piece' rows carry a line to write each piece's name
    cell = lambda r: '<td><span style="display:inline-block;width:92%;border-bottom:1px solid #c9cbe0;height:18px"></span></td>' if r == 'PIECE' else f'<td><b>{r}</b></td>'
    tr = ''.join((('<tr><td colspan="8" style="padding-top:8px"><b style="font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#e4572e">My pieces</b></td></tr>') if r == 'PIECES' else
                  f'<tr>{cell(r)}' + ''.join(f'<td class="c">{box}</td>' for _ in DAYS) + '</tr>') for r in rows)
    if mins: tr += '<tr class="mins"><td><b>Minutes</b></td>' + ''.join('<td></td>' for _ in DAYS) + '</tr>'
    return f'<table class="ht"><colgroup><col style="width:30%">' + '<col style="width:10%">' * 7 + f'</colgroup><thead><tr><th></th>{th}</tr></thead><tbody>{tr}</tbody></table>'
# cover: the Handbook cover with a new title and line
cover = S[0].replace('<div class="fct">Handbook</div>', '<div class="fct">Practice Diary</div>')
cover = re.sub(r'<p class="fcs">.*?</p>', '<p class="fcs">A week on every page: what to practise, what went well, and what your teacher says.</p>', cover, flags=re.S)
cover = re.sub(r'<div class="fcf">.*?</div>', '<div class="fcf">Free to print · thepianobutler.com</div>', cover, flags=re.S)
pages.append(cover)
n = 2
page('''<div class="kick">Before you start</div><h1>How to use this diary</h1><p class="lead">One page for each week. It takes a minute a day, and it turns practice into something you can see.</p>
<div class="fnum"><div><span>1</span><p><b>At the lesson,</b> fill in the top of the week: the date, the piece, one thing to fix, and what your teacher says.</p></div>
<div><span>2</span><p><b>Each day,</b> tick what you played and write the minutes. Short and often beats long and rare: ten minutes every day is better than an hour on Sunday.</p></div>
<div><span>3</span><p><b>Before the next lesson,</b> look back at the week. Bring the diary, so your teacher can see what went well.</p></div></div>
<h3>What the rows mean</h3><table class="ht"><colgroup><col style="width:34%"><col style="width:66%"></colgroup><tbody>
<tr><td><b>30-second check</b></td><td>Sit tall, a round hand, feet flat: before every practice.</td></tr><tr><td><b>Warm-ups</b></td><td>Five-finger patterns or a few slow scales.</td></tr>
<tr><td><b>This week’s chapter</b></td><td>The Handbook chapter you are learning: listen to it, write its Workbook page, play its drill.</td></tr>
<tr><td><b>Scales</b></td><td>The scales and arpeggios on your list.</td></tr><tr><td><b>My pieces</b></td><td>Write each piece on its own line (up to seven). The hardest bars first, slowly, then the whole piece once.</td></tr><tr><td><b>Something just for fun</b></td><td>A piece you already love, or one you make up.</td></tr></tbody></table>
<p class="sm" style="margin-top:14px">© 2026 Clara Sohyun Park. Free to print as many copies as you like for yourself, your family or your students. Please share the link, not the file.</p>''', n, z=1.36); n += 1
lines = lambda k: ''.join('<div class="dl"></div>' for _ in range(k))
page(f'''<div class="kick">This year</div><h1>About me</h1><div class="dg"><div><div class="dlab">My name</div>{lines(1)}</div><div><div class="dlab">My teacher</div>{lines(1)}</div>
<div><div class="dlab">Lesson day and time</div>{lines(1)}</div><div><div class="dlab">I started piano</div>{lines(1)}</div></div>
<div class="dlab" style="margin-top:22px">This year I want to…</div>{lines(4)}<div class="dlab" style="margin-top:18px">Pieces I would love to play one day</div>{lines(4)}
<div class="dlab" style="margin-top:18px">My practice time and place</div>{lines(2)}''', n, z=1.3); n += 1
page('<div class="kick">This year</div><h1>Goals for each term</h1><p class="lead">One or two goals a term: a piece, a scale, a chapter, a concert. Tick them when they are done.</p><div class="dg">'
     + ''.join(f'<div class="tbox"><b>Term {t}</b>{lines(4)}</div>' for t in range(1, 5)) + '</div>', n, z=1.12); n += 1
for part in (1, 2):
    tr = ''.join('<tr><td style="height:30px"></td><td></td><td></td><td></td><td></td></tr>' for _ in range(24))
    page(f'<div class="kick">This year</div><h1>My pieces{" · continued" if part == 2 else ""}</h1>' + (f'<p class="lead">Every piece you learn, with the dates. It is a good list to look back on.</p>' if part == 1 else '')
         + f'<table class="ht"><colgroup><col style="width:38%"><col style="width:22%"><col style="width:13%"><col style="width:13%"><col style="width:14%"></colgroup><thead><tr><th>Piece</th><th>Composer</th><th>Started</th><th>Learned</th><th>Played for someone</th></tr></thead><tbody>{tr}</tbody></table>', n); n += 1
SC = ['C major', 'G major', 'F major', 'D major', 'A minor', 'E minor', 'D minor', 'B♭ major', 'A major', 'E♭ major', 'B minor', 'G minor', 'E major', 'C minor', 'Contrary motion', 'Chromatic', 'Arpeggios', '']
tr = ''.join(f'<tr><td><b>{s}</b></td>' + ''.join(f'<td class="c">{box}</td>' for _ in range(4)) + '</tr>' for s in SC)
page('<div class="kick">This year</div><h1>Scales and technique</h1><p class="lead">Tick each step when it is steady three times in a row. Add your own on the empty line.</p>'
     f'<table class="ht"><colgroup><col style="width:36%"><col style="width:16%"><col style="width:16%"><col style="width:16%"><col style="width:16%"></colgroup><thead><tr><th>Scale</th><th>Hands separately</th><th>Hands together</th><th>From memory</th><th>At speed</th></tr></thead><tbody>{tr}</tbody></table>', n, z=1.28); n += 1
for w in range(1, 41):
    page(f'''<div class="wkh"><div class="kick">Week {w}</div><span class="dt">Lesson date ____________</span></div><h1 style="margin-top:2px">My practice week</h1>
{grid(['30-second check', 'Warm-ups', 'This week’s chapter', 'Scales', 'PIECES'] + ['PIECE'] * 7 + ['Something just for fun'])}
<h3>This week</h3><div class="fwk"><div><b>Chapter</b><span class="fl"></span></div><div><b>Piece to work on most</b><span class="fl"></span></div><div><b>One thing to fix</b><span class="fl"></span></div><div><b>What went well</b><span class="fl"></span></div>
<div><b>My teacher says</b><span class="fl"></span><span class="fl"></span></div><div><b>A question for next lesson</b><span class="fl"></span><span class="fl"></span></div><div><b>Total minutes this week</b><span class="fl"></span></div><div><b>Next week I will…</b><span class="fl"></span></div></div>''', n, z=1.12); n += 1
page(f'''<div class="kick">Getting ready</div><h1>A concert or an exam</h1><div class="dg"><div><div class="dlab">What and when</div>{lines(1)}</div><div><div class="dlab">Where</div>{lines(1)}</div></div>
<h3>Four weeks before</h3><p>Play everything through once a day without stopping. Mark the bars that slip and practise only those.</p>
<h3>One week before</h3><p>Play for someone every day: a parent, a friend, a toy. Practise walking in, sitting, breathing and bowing.</p>
<h3>On the day</h3><p>Warm hands, one slow scale, then leave the music alone. Breathe out, feel one bar of the beat in your head, and begin.</p>
<div class="dlab" style="margin-top:16px">My pieces, in order</div>{lines(4)}<div class="dlab" style="margin-top:14px">Afterwards: what went well, what I will try next time</div>{lines(4)}''', n, z=1.22); n += 1
# Handbook chapters, ticked when learned (the new chapter list, with Handbook pages)
PN = {'pitch': 'Pitch', 'time': 'Time', 'expression': 'Expression', 'scales': 'Scales and keys', 'chords': 'Chords', 'harmony': 'Harmony in music', 'shape': 'Shape and style', 'play': 'Playing and listening', 'further': 'Going further'}
items, chunks = '', []
for part, pp in NM.items():
    if part == 'scales': chunks.append(items); items = ''
    hs = [x for x in pp if x['h1'] and not re.match(r'^[A-Z]+0$', x['k'])]
    if part == 'time':
        items += f'<h4>{PN[part]}</h4>' + ''.join(f'<div>{box}<span>{x["h1"]}</span><span class="p">{x["pg"]}</span></div>' for x in hs if not x['k'].startswith('B'))
        items += '<h4>Bars and repeats</h4>' + ''.join(f'<div>{box}<span>{x["h1"]}</span><span class="p">{x["pg"]}</span></div>' for x in hs if x['k'].startswith('B'))
    else: items += f'<h4>{PN[part]}</h4>' + ''.join(f'<div>{box}<span>{x["h1"]}</span><span class="p">{x["pg"]}</span></div>' for x in hs)
chunks.append(items)
page(f'<div class="kick">The Handbook</div><h1>Chapters I know</h1><p class="lead">Tick a chapter when you can say its Remember box in your own words. The number is its Handbook page; every chapter is free to hear in Read &amp; listen.</p><div class="chk">{chunks[0]}</div>', n, z=1.2); n += 1
page(f'<div class="kick">The Handbook</div><h1>Chapters I know · continued</h1><div class="chk">{chunks[1]}</div>', n, z=1.2); n += 1
html = head.replace('</head>', CSS + '</head>') + '<body>' + ''.join(pages) + '</body></html>'
html = html.replace('THE PIANO BUTLER HANDBOOK', 'THE PIANO BUTLER')
open('/mnt/user-data/outputs/practice-diary.html', 'w').write(html); print('pages', len(pages))
