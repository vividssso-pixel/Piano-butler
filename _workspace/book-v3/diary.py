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
cover = re.sub(r'<p class="fcs">.*?</p>', '<p class="fcs">Lessons and practice, a week on every page: what your teacher set, what you practised, and how it went.</p>', cover, flags=re.S)
cover = re.sub(r'<div class="fcf">.*?</div>', '<div class="fcf">Free to print · thepianobutler.com</div>', cover, flags=re.S)
pages.append(cover)
n = 2
page('''<div class="kick">Before you start</div><h1>How to use this diary</h1><p class="lead">One page for each week: your lesson and your practice on the same page, so you (and your teacher, if you have one) can see at a glance how the week went.</p>
<div class="fnum"><div><span>1</span><p><b>At the start of the week,</b> you or your teacher fill in the week’s list: each piece, scale or task on its own line, with what to do and a goal (for example “bars 8–16, left hand alone, slowly”).</p></div>
<div><span>2</span><p><b>Each day,</b> tick every line you practised and write your minutes. Short and often beats long and rare: ten minutes every day is better than an hour on Sunday.</p></div>
<div><span>3</span><p><b>Before the next lesson,</b> write what went well and one question. Bring the diary to your lesson, or use it to plan your next week.</p></div></div>
<h3>What goes on the list</h3><table class="ht"><colgroup><col style="width:30%"><col style="width:70%"></colgroup><tbody>
<tr><td><b>Technique</b></td><td>Scales, arpeggios, exercises: which ones, how fast.</td></tr>
<tr><td><b>Pieces</b></td><td>One line each: which bars, and what to listen for.</td></tr>
<tr><td><b>Theory</b></td><td>This week’s topic: read it, write it, then play it.</td></tr>
<tr><td><b>Aural and sight-reading</b></td><td>A few minutes: sing it back, clap it back, read something new.</td></tr></tbody></table>
<p class="sm" style="margin-top:14px">© 2026 Clara Sohyun Park. Free to print as many copies as you like for yourself, your family or your students. Please share the link, not the file.</p>''', n, z=1.3); n += 1
lines = lambda k: ''.join('<div class="dl"></div>' for _ in range(k))
page(f'''<div class="kick">This year</div><h1>About me</h1><div class="dg"><div><div class="dlab">My name</div>{lines(1)}</div><div><div class="dlab">My teacher</div>{lines(1)}</div>
<div><div class="dlab">Lesson day and time</div>{lines(1)}</div><div><div class="dlab">I started piano</div>{lines(1)}</div></div>
<div class="dlab" style="margin-top:22px">This year I want to…</div>{lines(4)}<div class="dlab" style="margin-top:18px">Pieces I would love to play one day</div>{lines(4)}
<div class="dlab" style="margin-top:18px">My practice time and place</div>{lines(2)}''', n, z=1.3); n += 1
page('<div class="kick">This year</div><h1>Goals for each term</h1><p class="lead">One or two goals a term: a piece, a scale, a theory topic, a concert. Tick them when they are done.</p><div class="dg">'
     + ''.join(f'<div class="tbox"><b>Term {t}</b>{lines(4)}</div>' for t in range(1, 5)) + '</div>', n, z=1.12); n += 1
for part in (1, 2):
    tr = ''.join('<tr><td style="height:30px"></td><td></td><td></td><td></td><td></td></tr>' for _ in range(24))
    page(f'<div class="kick">This year</div><h1>My pieces{" · continued" if part == 2 else ""}</h1>' + (f'<p class="lead">Every piece you learn, with the dates. It is a good list to look back on.</p>' if part == 1 else '')
         + f'<table class="ht"><colgroup><col style="width:38%"><col style="width:22%"><col style="width:13%"><col style="width:13%"><col style="width:14%"></colgroup><thead><tr><th>Piece</th><th>Composer</th><th>Started</th><th>Learned</th><th>Played for someone</th></tr></thead><tbody>{tr}</tbody></table>', n); n += 1
# her 16 Nov ("마이너는?"): majors and minors apart, in circle-of-fifths order; each minor names its form (natural, harmonic, melodic)
MAJ = ['C major', 'G major', 'D major', 'A major', 'E major', 'B major', 'F major', 'B♭ major', 'E♭ major', 'A♭ major', '']
MIN = ['A minor', 'E minor', 'B minor', 'F♯ minor', 'D minor', 'G minor', 'C minor', 'F minor', '']
OTH = ['Contrary motion', 'Chromatic', 'Arpeggios', '']
def srow(name, minor=False):
    lab = f'<b>{name}</b>' + (' <span style="font-size:11px;color:#6d6f9c;letter-spacing:.04em;margin-left:6px">natural · harmonic · melodic</span>' if minor and name else '')
    return f'<tr><td>{lab}</td>' + ''.join(f'<td class="c">{box}</td>' for _ in range(3)) + '<td style="vertical-align:bottom"><span style="font-size:15px;color:#6d6f9c">♩ =</span><span style="display:inline-block;width:58%;border-bottom:1px solid #c9cbe0;height:16px;margin-left:4px"></span></td></tr>'
def shead(t): return f'<tr><td colspan="5" style="padding-top:9px"><b style="font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#e4572e">{t}</b></td></tr>'
tr = shead('Major scales') + ''.join(srow(x) for x in MAJ) + shead('Minor scales · circle the form') + ''.join(srow(x, True) for x in MIN) + shead('Technique') + ''.join(srow(x) for x in OTH)
page('<div class="kick">This year</div><h1>Scales and technique</h1><p class="lead">Tick each step when it is steady three times in a row, and write the speed you reach. For a minor scale, circle the form you are learning. Add your own on the empty lines.</p>'
     f'<table class="ht tight"><colgroup><col style="width:44%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:14%"></colgroup><thead><tr><th>Scale</th><th style="text-align:center">Hands separately</th><th style="text-align:center">Hands together</th><th style="text-align:center">From memory</th><th style="text-align:center">Speed</th></tr></thead><tbody>{tr}</tbody></table>', n, z=0.96); n += 1
def keyboard(octaves=2, start=48):
    W, H, BH, BW = 26, 96, 60, 16; n = 7 * octaves + 1; g = ''
    names = 'CDEFGAB'
    for i in range(n): g += f'<rect x="{i * W}" y="0" width="{W}" height="{H}" fill="#fff" stroke="#26296b" stroke-width="1.2"/>'
    for i in range(n - 1):
        if names[i % 7] in 'CDFGA': g += f'<rect x="{i * W + W - BW / 2}" y="0" width="{BW}" height="{BH}" rx="2" fill="#26296b"/>'
    g += f'<text x="{7 * W * (octaves // 2) + W / 2}" y="{H - 8}" text-anchor="middle" font-size="9" font-weight="700" fill="#e4572e" font-family="Atkinson Hyperlegible,sans-serif">C</text>'
    return f'<svg viewBox="-2 -2 {n * W + 4} {H + 4}" style="width:86%;height:auto;display:block;margin:0 auto">{g}</svg>'
def weeklist(n_rows):
    th = ''.join(f'<th style="text-align:center;padding-left:0;padding-right:0">{d[0]}</th>' for d in DAYS)
    ln = '<span style="display:block;height:30px"></span>'
    tr = ''.join(f'<tr><td style="border-right:1px solid #e2ddd0">{ln}</td><td style="border-right:1px solid #e2ddd0">{ln}</td>' + ''.join(f'<td class="c">{box}</td>' for _ in DAYS) + '</tr>' for _ in range(n_rows))
    tr += '<tr class="mins"><td colspan="2"><b>Minutes each day</b></td>' + ''.join('<td></td>' for _ in DAYS) + '</tr>'
    return ('<table class="ht"><colgroup><col style="width:22%"><col style="width:36%">' + '<col style="width:6%">' * 7 + '</colgroup>'
            f'<thead><tr><th>Piece or task</th><th>What to do · goal</th>{th}</tr></thead><tbody>{tr}</tbody></table>')
for w in range(1, 41):
    page(f'''<div class="wkh"><div class="kick">Week {w}</div><span class="dt">Date ____________ · Next lesson ____________</span></div><h1 style="margin-top:2px">This week</h1>
<div class="dlab" style="margin-top:4px">Set at the lesson, or by you · ticked every day</div>
{weeklist(10)}
<div class="fwk" style="margin-top:12px"><div><b>Notes</b><span class="fl"></span><span class="fl"></span><span class="fl"></span></div><div><b>What went well</b><span class="fl"></span><span class="fl"></span><span class="fl"></span></div>
<div><b>Total minutes</b><span class="fl"></span></div><div><b>A question for next time</b><span class="fl"></span></div></div>
<div class="dlab" style="margin-top:12px">Mark notes, fingering or a chord</div>{keyboard()}''', n, z=1.1); n += 1
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
        items += f'<h4>{PN[part]}</h4>' + ''.join(f'<div>{box}<span>{x["h1"]}</span></div>' for x in hs if not x['k'].startswith('B'))
        items += '<h4>Bars and repeats</h4>' + ''.join(f'<div>{box}<span>{x["h1"]}</span></div>' for x in hs if x['k'].startswith('B'))
    else: items += f'<h4>{PN[part]}</h4>' + ''.join(f'<div>{box}<span>{x["h1"]}</span></div>' for x in hs)
chunks.append(items)
page(f'<div class="kick">This year</div><h1>Music theory I know</h1><p class="lead">Tick a topic when you can explain it in your own words and find it in a piece. Every topic is explained free, read aloud, at thepianobutler.com.</p><div class="chk">{chunks[0]}</div>', n, z=1.2); n += 1
page(f'<div class="kick">This year</div><h1>Music theory I know · continued</h1><div class="chk">{chunks[1]}</div>', n, z=1.2); n += 1
html = head.replace('</head>', CSS + '</head>') + '<body>' + ''.join(pages) + '</body></html>'
html = html.replace('THE PIANO BUTLER HANDBOOK', 'THE PIANO BUTLER')
open('/mnt/user-data/outputs/practice-diary.html', 'w').write(html); print('pages', len(pages))
