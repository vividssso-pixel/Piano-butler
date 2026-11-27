# The story thread in the Music Box (her 27 Nov 14:40). Three touches, all marked DRAFT until she confirms the wording:
#   1. the first page of each book: one line and a torn piece of the letter (lower staff empty; NOT the letter's real notes)
#   2. the last page of each book: the pattern card, "Returned: Roots." and so on, as a revision table
#   3. chord words where a minor chord is met: ACE only where A-C-E lie in that order; BEG and FAD say "turn the letters round";
#      FACE and CAGE wait for the seventh-chord book
# Not used (her decision): a caption on Song 1, the "Not yet, Miss Clara" lines, the letter's score or words, any birthday link.
# The student is always "you". Run after mbox.py, mbox2.py, mbfront2.py, mbox3.py, mbfront3.py.
import json, copy, os
N = '#26296b'; HERE = os.path.dirname(os.path.abspath(__file__))
GC = json.load(open(os.path.join(HERE, 'gclef.json')))['d']; FC = json.load(open(os.path.join(HERE, 'fclef.json')))['d']
DRF = 'drf'   # a class: the word DRAFT is drawn before the text until she confirms it
def letter():   # a torn corner of a letter in notes: the upper staff has a few notes, the lower staff is empty
    W, H, S = 300, 150, 7; t1, t2, x0 = 30, 90, 30
    edge = [(292, 6), (286, 20), (291, 33), (281, 47), (287, 60), (276, 74), (282, 88), (270, 101), (276, 114), (264, 126), (268, 138),
            (252, 133), (238, 141), (222, 134), (206, 142), (188, 135), (170, 143), (152, 136), (134, 143), (114, 137), (96, 144), (78, 137), (58, 144), (40, 138), (22, 144), (6, 139)]
    paper = 'M6 6 L' + ' L'.join(f'{x} {y}' for x, y in edge) + ' Z'
    g = f'<defs><clipPath id="ltc"><path d="{paper}"/></clipPath></defs><path d="{paper}" fill="#fff" stroke="{N}" stroke-opacity=".55" stroke-width="1.2" stroke-linejoin="round"/><g clip-path="url(#ltc)">'
    for t in (t1, t2):
        for i in range(5): g += f'<line x1="{x0}" x2="{W}" y1="{t + i * S}" y2="{t + i * S}" stroke="{N}" stroke-width="1"/>'
        for x in (150, 236): g += f'<line x1="{x}" x2="{x}" y1="{t}" y2="{t + 4 * S}" stroke="{N}" stroke-width="1"/>'
    g += f'<line x1="{x0}" x2="{x0}" y1="{t1}" y2="{t2 + 4 * S}" stroke="{N}" stroke-width="1.6"/>'
    g += f'<path d="M{x0 - 5} {t1} C{x0 - 13} {t1 + 22} {x0 - 3} {t1 + 30} {x0 - 13} {(t1 + t2 + 4 * S) / 2} C{x0 - 3} {t2 - 2} {x0 - 13} {t2 + 6} {x0 - 5} {t2 + 4 * S}" fill="none" stroke="{N}" stroke-width="2.2" stroke-linecap="round"/>'
    g += f'<g transform="translate({x0 + 5} {t1 + 3 * S}) scale({S * 4 / 1000})"><path transform="scale(1,-1)" d="{GC}" fill="{N}"/></g>'
    g += f'<g transform="translate({x0 + 5} {t2 + S}) scale({S * 4 / 1000})"><path transform="scale(1,-1)" d="{FC}" fill="{N}"/></g>'
    for x, st in ((78, 2), (100, 3), (122, 4), (172, 3), (196, 2), (220, 1), (256, 2)):   # steps above the bottom line: any notes, not the letter's
        y = t1 + 4 * S - st * S / 2
        g += f'<ellipse cx="{x}" cy="{y}" rx="4.7" ry="3.4" transform="rotate(-20 {x} {y})" fill="{N}"/><line x1="{x + 4.2}" x2="{x + 4.2}" y1="{y - 1}" y2="{y - 23}" stroke="{N}" stroke-width="1.3"/>'
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="A torn piece of a letter written in notes. The lower staff is empty.">{g}</g></svg>'
LINE = 'The letter has two hands. The lower one is the King’s, of all things low. This book gives some of it back.'
LT = f'<div class="lt">{letter()}<p class="{DRF}">{LINE}</p></div>'
def box(pat):   # four beat boxes for the card: 'C+E+G - - -'
    return '<span class="pcb">' + ''.join('<span>' + ('<i></i>' if t == '-' else '<br>'.join(reversed(t.split('+')))) + '</span>' for t in pat.split()) + '</span>'
def card(n, intro, rows):
    tr = ''.join(f'<tr><td class="rt">Returned: <b>{name}</b>.</td><td>{box(pat)}</td><td>{what}<br><span class="wh">{where}</span></td><td><span class="bx"></span></td></tr>' for name, pat, what, where in rows)
    return f'''<div class="kick">End of Music Box {n}</div><h1>Pattern card</h1><p class="byl">The left-hand patterns of this book, on one page</p>
<div class="mb-intro"><p class="{DRF}" style="font-size:17px">{intro}</p></div><div class="sp"></div><table class="pct">{tr}</table>
<div class="sp"></div><p class="fp" style="font-size:14px">The boxes show each pattern on a C chord, four slow beats. A line means keep holding. Letters stacked in one box are played together.</p>'''
INTRO = 'Each pattern you learn gives back one piece of the letter’s lower hand. Play each one again, slowly, and tick it when it still feels easy.'
def save(base, id_, title, label, pages, page0):
    d = copy.deepcopy(json.load(open(base))); d.update(id=id_, title=title, lesson=0, label=label, page0=page0)
    for k in ('nokb', 'extra', 'split', 'steps', 'song_note', 'cword'): d['gig'].pop(k, None)
    d['gig']['front'] = pages; json.dump(d, open(id_ + '.json', 'w'), ensure_ascii=False)
# ---- Music Box 1: a first page (it had none), page numbers, the card
PAT1 = {}
S1 = [json.load(open(f'mb{i}.json')) for i in range(1, 20)]
from pypdf import PdfReader
P1 = 1   # pages before this song: the first page, then every song's own page count (some songs have a second page), read from the last build
for i, d in enumerate(S1, 1):
    d['page0'] = P1; json.dump(d, open(f'mb{i}.json', 'w'), ensure_ascii=False)
    P1 += len(PdfReader(f'lesson-mb{i}.pdf').pages) if os.path.exists(f'lesson-mb{i}.pdf') else 1
rows = ''.join(f'<tr><td class="n">{i if i < 19 else ""}</td><td><b>{d["title"]}</b></td><td>{d["gig"].get("today") or ""}</td></tr>' for i, d in enumerate(S1, 1))
p1 = f'''<div class="kick">Start here</div><h1>Music Box 1</h1><p class="byl">Eighteen songs and one old friend</p>
{LT}<table class="ftb"><tr><th style="width:5%"></th><th style="width:60%">Song</th><th style="width:35%">Left-hand pattern</th></tr>{rows}</table>'''
save('mb1.json', 'mb0', 'Music Box 1', 'Start here', [p1], 0)
c1 = card(1, INTRO, [('Roots', 'C - - -', 'One key: the letter in the chord’s name. Hold it.', 'Songs 1 to 10, 12 and 15'),
                     ('Block chord', 'C+G - - -', 'The keys of the chord together. In this book, two: bottom and top. Hold them.', 'Song 11'),
                     ('Zigzag', 'C G C G', 'Bottom and top of the chord, rocking. No middle key.', 'Songs 16 and 17')])
save('mb1.json', 'mb20', 'Pattern card', 'End of Music Box 1', [c1], P1)
# ---- Music Box 2: the line on its first page, three chord words, the card
d = json.load(open('mc0.json')); f = d['gig']['front']; a = '<div class="sp"></div><table class="ftb"><tr><th style="width:4%">'
assert f[0].count(a) == 1 and 'class="lt"' not in f[0]; f[0] = f[0].replace(a, '<div class="sp"></div>' + LT + a.replace('<div class="sp"></div>', ''), 1); d['page0'] = 0; json.dump(d, open('mc0.json', 'w'), ensure_ascii=False)
CW = {8: 'E minor is E, G and B. Turn the letters round and they spell <b>BEG</b>.',
      10: 'A, C, E, from the bottom up: the A minor chord spells <b>ACE</b>.',
      14: 'D minor is D, F and A. Turn the letters round and they spell <b>FAD</b>.'}
for k, t in CW.items():
    d = json.load(open(f'mc{k}.json')); d['gig']['cword'] = t; json.dump(d, open(f'mc{k}.json', 'w'), ensure_ascii=False)
last = json.load(open('mc14.json')); end2 = last['page0'] + 1 + -(-len(last['gig']['song_grid']) // last['gig'].get('split', 99))
c2 = card(2, INTRO, [('Roots', 'C - - -', 'One key: the letter in the chord’s name. Hold it.', 'Song 11, and the older way in Songs 1 to 4'),
                     ('Block chord', 'C+E+G - - -', 'All three keys of the chord together. Hold them.', 'Songs 1 to 4, 6 and 10'),
                     ('Waltz style', 'C E+G C E+G', 'Bottom key, then the top two together.', 'Song 5 and the last page'),
                     ('Broken chord', 'C E G E', 'One key at a time: bottom, middle, top.', 'Songs 7, 8 and 13'),
                     ('Zigzag', 'C G C G', 'Bottom and top of the chord, rocking. No middle key.', 'Song 12')])
save('mc1.json', 'mc15', 'Pattern card', 'End of Music Box 2', [c2], end2)
# ---- Music Box 3: the line on its first page, the card
d = json.load(open('md0.json')); f = d['gig']['front']; a = '<div class="sp"></div><table class="ftb"><tr><th style="width:4%">'
assert f[0].count(a) == 1 and 'class="lt"' not in f[0]; f[0] = f[0].replace(a, '<div class="sp"></div>' + LT + a.replace('<div class="sp"></div>', ''), 1); json.dump(d, open('md0.json', 'w'), ensure_ascii=False)
last = json.load(open('md9.json')); end3 = last['page0'] + 1 + -(-len(last['gig']['song_grid']) // last['gig'].get('split', 99))
c3 = card(3, INTRO, [('Roots', 'C - - -', 'One key: the letter in the chord’s name. Hold it.', 'On the menu, Songs 7 to 9'),
                     ('Block chord', 'C+E+G - - -', 'All three keys of the chord together. Hold them.', 'Songs 1, 2, 4 and 5'),
                     ('Waltz style', 'C E+G C E+G', 'Bottom key, then the top two together.', 'Songs 3 and 6'),
                     ('Broken chord', 'C E G E', 'One key at a time: bottom, middle, top.', 'On the menu, Songs 7 to 9'),
                     ('Zigzag', 'C G C G', 'Bottom and top of the chord, rocking. No middle key.', 'On the menu, Songs 7 to 9')])
save('md1.json', 'md10', 'Pattern card', 'End of Music Box 3', [c3], end3)
print('story ok: card pages', P1 + 1, end2 + 1, end3 + 1)
