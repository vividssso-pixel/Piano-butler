# Her 14 Nov ("바로 유료 판매"): the Workbook as one book for sale. Runs last in the build, on the generated HTML.
# (1) one page sequence through the whole Workbook (it restarted at 1 in every section), with every "page N", answer-key
#     "p. N" and the Handbook's "Workbook pp." references following it; (2) the fixes from the whole-book proofread of
#     14 Nov (two independent readers) that are text, labels, running heads or box sizes.
import re, sys, json
H = '/mnt/user-data/outputs/house-rooms/'
FRONT = 4   # Workbook front matter: cover, title and copyright, how to use with the Handbook, contents (wbfront.py)
ORDER = ['workbook-before', 'workbook-pitch', 'workbook-time2', 'workbook-expression', 'workbook-scales', 'workbook-harmony', 'workbook-shape', 'workbook-play']   # Going further waits for a later edition (her 14 Nov, A)
def secs(h): return re.findall(r'<section\b[^>]*>.*?</section>', h, re.S)
def offsets():
    off, n = {}, FRONT
    for f in ORDER:
        off[f] = n; n += len(secs(open(H + f + '.html').read()))
    return off, n
OFF, TOTAL = offsets()
json.dump({'front': FRONT, 'off': OFF, 'total': TOTAL}, open(H + 'workbook-pages.json', 'w'))

def text_sub(h, pat, fn):   # only between tags, never inside attributes or SVG
    return re.sub(r'>([^<>]*)<', lambda m: '>' + re.sub(pat, fn, m.group(1)) + '<', h)

FIX = {   # file: [(old, new)], each must match at least once
 'workbook-pitch': [('<h1>Semitones and tones</h1>', '<h1>Counting intervals</h1>')],
 'workbook-time2': [('<h1>Pulse and the bar</h1>', '<h1>Pulse, tempo and the bar</h1>'),
                    ('<h1>Groups and upbeats</h1>', '<h1>Rhythm: groups and upbeats</h1>'),
                    ('<h1>Off the beat</h1>', '<h1>Rhythm: off the beat</h1>'),
                    ('Swing written at the top', 'the word “Swing” written at the top')],
 'workbook-expression': [('a second letter means very', 'a doubled letter (pp, ff) means very'), ('An ornament starts on the beat.', 'A trill, mordent or turn starts on the beat.')],
 'workbook-scales': [],
 'workbook-harmony': [('<th>Borrowed iv</th>', '<th>Borrowed <span style="text-transform:none">iv</span></th>'),
                      ('Find the sharp, go up one key, and write the next chord (the note you reach names it).', 'Find the sharp (or sharps), go up one key, and write the chord of C major on the note you reach (D → Dm).'),
                      ('D♯, E, Em.', 'D♯, E, Em (F♯ → G).'),
                      ('If the notes disagree, pick the cake that holds most of them.', 'If the notes disagree, pick the cake that holds the notes on beats 1 and 3.'),
                      ('one mark for each answer.', 'one mark for each answer (one per triad in exercise 1).'),
                      ('<h1>Guest chords</h1>', '<h1>Chords from outside the key</h1>'), ('<td>guest chords</td>', '<td>chords from outside the key</td>'),
                      ('One more floor', 'One more layer'), ('Add the top floor', 'Add the top layer'), ('Count the floors', 'Count the layers')],
 'workbook-shape': [('<b>Block or broken?</b>', '<b>Block and Alberti</b>'), ('is one more sharp than', 'has one more sharp than'), ('bar 3 contrast (new notes)', 'bar 3 contrast (new shape and rhythm)')],
 'workbook-play': [('Going up the right hand, the thumb passes under; coming down, finger 3 crosses over.', 'Right hand: going up, the thumb passes under; coming down, finger 3 crosses over.'),
                   ('♩ = 72', '<span style="white-space:nowrap;font-family:\'NM\',\'AH\',sans-serif">♩&#8239;=&#8239;72</span>')],
}
WIDE = {   # exercise title: box width (px), for answers longer than one letter
 'workbook-harmony': {'Which chord holds it?': 64, 'Which cake holds it?': 64, 'Numerals first': 110, 'Write the symbol': 84, 'Over a C pedal': 84, 'Left hand, right hand': 84, 'Home, away or pull?': 84, 'Walk the bass down': 84},
}

def fix_file(f):
    p = H + f + '.html'; h = open(p).read(); off = OFF[f]
    for a, b in FIX.get(f, []):
        if a not in h: print('MISS', f, a[:50]); continue
        h = h.replace(a, b)
    for title, w in WIDE.get(f, {}).items():
        i = h.find(f'<b>{title}</b>')
        if i < 0: print('MISS box', f, title); continue
        j = h.find('<div class="ex2">', i); j = len(h) if j < 0 else j
        h = h[:i] + re.sub(r'<span class="ab( hasdone)?"', lambda m: f'<span style="width:{w}px" class="ab{m.group(1) or ""}"', h[i:j]) + h[j:]
    # running heads: a Use page names the next Handbook page of its chapter, not the Learn page's own
    out, prev = [], None
    for s in re.split(r'(?=<section\b)', h):
        m = re.search(r'(HANDBOOK P\.(?:\s|&nbsp;| | )?)(\d+)', s)
        kind = re.search(r'<div class="kick">[^<]*· (Learn|Use)</div>', s)
        if m and kind:
            if kind.group(1) == 'Use' and prev and int(m.group(2)) == prev: s = s[:m.start(2)] + str(prev + 1) + s[m.end(2):]
            prev = int(m.group(2)) if kind.group(1) == 'Learn' else None
        out.append(s)
    h = ''.join(out)
    def _long(m):   # longer chapter names stay on one line: a smaller title and a narrower chapter picture beside it
        t = m.group(0)
        return re.sub(r'<h1>([^<]{23,})</h1>', lambda n: f'<h1 style="font-size:30px">{n.group(1)}</h1>', t).replace('max-width:46%', 'max-width:32%') if re.search(r'<h1>[^<]{23,}</h1>', t) else t
    h = re.sub(r'<div class="wbhd">.*?</div><img[^>]*>|<h1>[^<]{23,}</h1>', _long, h, flags=re.S)
    # one page sequence
    h = re.sub(r'(<div class="foot"><span>)(\d+)(</span>)', lambda m: m.group(1) + str(int(m.group(2)) + off) + m.group(3), h)
    h = re.sub(r'<table class="ht ansT.*?</table>', lambda t: re.sub(r'<td>p\.[\s\u00a0\u2009\u202f]?(\d+)</td>', lambda m: f'<td>p. {int(m.group(1)) + off}</td>', t.group(0)), h, flags=re.S)   # answer keys only (progress tables name Handbook pages)
    h = text_sub(h, r'\b(pages?) (\d+)(?:(–)(\d+))?\b', lambda m: f'{m.group(1)} {int(m.group(2)) + off}' + (f'–{int(m.group(4)) + off}' if m.group(4) else ''))
    if f == 'workbook-pitch':   # the Before you play answers (they were printed on its own page)
        row = f'<tr><td>p. {OFF["workbook-before"] + 1}</td><td>Before you play: 1 thumb 1, index 2, middle 3, ring 4, little 5 · 2 B · 3 too low, right, too high · 4 T, F, F, T.</td></tr>'
        h = h.replace('<tbody><tr><td>p. ', '<tbody>' + row + '<tr><td>p. ', 1)
    if f == 'workbook-scales':   # one page per chapter, named as the Handbook names them
        names = ['Major scales', 'Minor scales', 'Keys and key signatures', 'Finding the key', 'The circle of fifths']
        k = [0]
        def lab(m):
            if k[0] >= len(names): return m.group(0)
            n = names[k[0]]; k[0] += 1
            return f'<div class="kick">Scales and keys · {n}</div>' + m.group(2) + f'<h1>{n}</h1>'
        h = re.sub(r'<div class="kick">Scales and keys · [^<]*· (Learn|Use)</div>(.*?)<h1>[^<]*</h1>', lab, h, flags=re.S)
    if f == 'workbook-harmony':   # Chords (Handbook Part V) and Harmony in music (Part VI) share this section
        h = re.sub(r'<div class="kick">Harmony · ', '<div class="kick">Chords and harmony · ', h)
        h = re.sub(r'(<span>)HARMONY( · HANDBOOK|</span>)', r'\1CHORDS AND HARMONY\2', h)
        for title, row, opt in (('Pick the chord in G', 'G B D B', 'I'), ('Name the trip', 'G D Em C', 'pop four')):   # the worked first row (the instruction already said so, so firstdone skipped it)
            i = h.find(f'<b>{title}</b>')
            if i >= 0: h = h[:i] + h[i:].replace(f'<b>{row}</b><span class="tf">{opt} ', f'<b>{row}</b><span class="tf"><b class="done2 ringd">{opt}</b> ', 1)
    open(p, 'w').write(h)

for f in ORDER: fix_file(f)

# the Handbook: "Practise it" boxes name the Workbook's own page numbers; the front matter describes the Workbook truly
F = {'P': 'workbook-pitch', 'T': 'workbook-time2', 'E': 'workbook-expression', 'S': 'workbook-scales', 'H': 'workbook-harmony', 'M': 'workbook-harmony', 'F': 'workbook-shape', 'L': 'workbook-play'}
def absolute(m):
    a, b = int(m.group(2)), int(m.group(4)) if m.group(4) else None
    return m.group(1) + str(a + OFF[CUR[0]]) + ('–' + str(b + OFF[CUR[0]]) if b else '')
import pagemap as PM
CH = {}
for pre, _, n in PM.PARTS:
    for i in range(1, n + 1):
        a, k = PM.pages_of(f'{pre}{i}')
        for pg in range(a, a + k): CH[pg] = pre
CUR = [None]; nref = 0
for f in ('handbook-pitch', 'handbook-time2', 'handbook-expression', 'handbook-scales', 'handbook-harmony', 'handbook-harmony2', 'handbook-shape', 'handbook-play'):
    s = open(H + f + '.html').read(); out = []
    for sec in re.split(r'(?=<section )', s):
        m = re.search(r'<div class="foot"><span>(\d+)</span>', sec) or re.search(r'class="foot[^"]*"[^>]*>\s*<span>(\d+)</span>', sec)
        pre = CH.get(int(m.group(1))) if m else None
        if pre in F:
            CUR[0] = F[pre]; new = re.sub(r'(Workbook pp?\.(?: | ))(\d+)(–(\d+))?', absolute, sec); nref += new != sec; sec = new
        out.append(sec)
    open(H + f + '.html', 'w').write(''.join(out))
for f2, fn in (('handbook-before', lambda t: re.sub(r'Workbook pp\.(\u00a0| )1–2', lambda m: f'Workbook pp.{m.group(1)}{OFF["workbook-before"] + 1}–{OFF["workbook-before"] + 2}', t)),
                ('handbook-further', lambda t: re.sub(r'Workbook pp?\.(\u00a0| )[0-9–]+ · ', '', t))):   # Going further is not in this Workbook edition
    t = open(H + f2 + '.html').read(); open(H + f2 + '.html', 'w').write(fn(t))
p = H + 'handbook-front.html'; s = open(p).read()
s = s.replace('Draft edition, November 2026', 'First edition, 2026').replace('<p>ISBN: to come</p>', '').replace(' Teachers may copy single Workbook pages for their own students.', '')   # her 15 Nov: copyright wording kept general
s = s.replace('two pages to write in for every chapter: Learn, then Use', 'pages to write in for every chapter: Learn, then Use (one page for each Scales and keys chapter)')
open(p, 'w').write(s)
print('wbfix', OFF, TOTAL, 'handbook pages with workbook refs', nref)
