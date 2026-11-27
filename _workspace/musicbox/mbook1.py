# Music Box 1, re-paced (her 27 Nov 15:03: 'build it by your own decisions and show me'). A SECOND version beside the current
# book: ids me0..me20; nothing in mb*.json changes. Plan: Book 1 teaches Roots, then Block chord (two keys); the new pattern
# gets four songs; Unit 1 ends with the Canon; Happy Birthday is the last song; Zigzag and waltz songs wait for later books.
# Moved out: Goin' Home, This Old Man (Book 3, Zigzag), The Blue Danube (Book 2, Waltz style), Twinkle, Now.
# New, each from a source: Canon (Mutopia, Canon per 3 violini e basso: violin 1 bars 3-6 and the cello, D to C);
# Go Tell Aunt Rhody (folktunefinder 161865, Rousseau, Musica Viva transcription, F to C); Long, Long Ago (folktunefinder
# 172850 and the Traditional Tune Archive: the first strain, identical in both, moved to C). Chords of Rhody are this book's own.
# Run mball.sh first, then this, then build me0..me20 (run this twice: page numbers come from the last build).
import json, copy, os
from pypdf import PdfReader
import mbstory as ST
B = lambda r, l, f=None, lp=None: {k: v for k, v in dict(r=r, l=l, w='', f=f, lp=lp).items() if v is not None}
def new(base, title, composer, job, how, grid, today, fmap, lcap, rcap, rfing=None, rmap=None, rkb=None, beats=4):
    d = json.load(open(base)); g = d['gig']
    for k in ('ways', 'ways_job', 'ways_how', 'ways_title', 'ways2', 'lkb', 'rkb', 'ready', 'note'): g.pop(k, None)
    d.update(title=title, beats=beats); d['composer'] = {'name': composer, 'years': '', 'stamp': ''}
    g.update(job=job, song_how=how, song_grid=grid, today=today, fmap=fmap, tool_cap=lcap, r_cap=rcap, shapes=1, simple=1, grid=1)
    if rfing: g['rfing'] = rfing
    if rmap: g['rmap'] = rmap
    if rkb: g['rkb'] = rkb
    return d
old = lambda n: json.load(open(f'mb{n}.json'))
# ---- Canon: the unit-end piece. One root under every note.
cb = lambda r, f, lp: B(r, lp[0], f, lp)
canon = new('mb11.json', 'Canon', 'Johann Pachelbel, late 1600s',
    'Eight bass notes that go round and round: C G A E, F C F G. A whole famous piece is built on them, and every one is a root.',
    'One left-hand key under every right-hand note. Learn the eight bass letters by heart first. An arrow ↑ means the higher key of that name.',
    [[cb("E' D' C' B", '5 4 3 2', 'C G A E'), cb('A G A B', '2 1 2 3', 'F C F G')], [cb("C' B A G", '4 3 2 1', 'C G A E'), cb('F E F D', '3 2 3 1', 'F C F G')], [B('C - - -', 'C', '1', 'C - - -'), B('- - - -', '', None, '- - - -')]],
    'Roots', {'c': 5, 'e': 3, 'f': 2, 'g': 1, 'a': 1}, 'C with 5, E with 3, F with 2. The thumb plays G, and slides up one key for A.',
    'Start with finger 5 on the high E and walk down. The numbers show where the hand moves.', rkb=['d', 9, 'x x x x x x x x x', None, 250])
# ---- Go Tell Aunt Rhody: line 1, the middle, line 1 again. Two chords in some bars.
C2, G2, F2 = 'C+G', 'D+G', 'C+F'
one = lambda r, c, f=None: B(r, c, f, c + ' - - -'); two = lambda r, a, b, f=None: B(r, a, f, f'{a} - {b} -')
A_ = [one('E E.D C C', C2), two('D D E.D C', G2, C2), one('G G.F E E', C2), two('D.C D.E C -', G2, C2)]
rhody = new('mb11.json', 'Go Tell Aunt Rhody', 'Jean-Jacques Rousseau, 1752',
    'A tune from an opera by Rousseau that became a nursery song on both sides of the ocean. Two keys in every chord again.',
    'Some bars have two chords: change on beat 3. In line 2 the hand moves up one key, and finger 5 plays A.',
    [A_, [one('E E.F G G', C2, '2 2.3 4 4'), two('A A G.F E', F2, C2, '5 5 4.3 2'), one('E E.F G G', C2, '2 2.3 4 4'), two('A A G -', F2, C2, '5 5 4 -')], copy.deepcopy(A_)],
    'Block chord', {'c': 5, 'd': 4, 'f': 2, 'g': 1}, 'C chord: C and G (5, 1). G chord: D and G (4, 1). F chord: C and F (5, 2).',
    'Thumb on C for lines 1 and 3. For line 2 the thumb moves to D.', rfing={'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 5}, rmap={'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 5})
# ---- Long, Long Ago: the first strain, as in both sources.
L1 = [B('C C.D E E.F', C2, '1 1.2 3 1.2'), B('G A.G E -', C2, '3 4.3 1 -'), B('G F.E D -', G2, '5 4.3 2 -'), B('F E.D C -', G2, '4 3.2 1 -')]
L2 = [B('C C.D E E.F', C2, '1 1.2 3 1.2'), B('G A.G E -', C2, '3 4.3 1 -'), B('G F.E D E.D', G2, '5 4.3 2 3.2'), B('C - - -', C2, '1')]
longago = new('mb11.json', 'Long, Long Ago', 'Thomas Haynes Bayly, 1833',
    'A song about remembering, nearly two hundred years old. Play it gently, as if telling a story.',
    'Long, short-short: the first note of each bar lasts a whole box, then two quick ones share a box. On the second E the thumb takes over, so the hand can reach A.',
    [L1, L2], 'Block chord', {'c': 5, 'd': 4, 'g': 1}, 'C chord: C and G (5, 1). G chord: D and G (4, 1).',
    'Thumb on C. In bars 1 and 5 the thumb moves up to E, then the hand comes back.', rfing={'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 5}, rmap={'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 5})
# ---- Ode to Joy, again: Song 5 with two keys in every chord (a growing song).
ode = old(5); g = ode['gig']
for k in ('ways', 'ways_job', 'ways_how', 'ways_title'): g.pop(k, None)
for ln in g['song_grid']:
    for b in ln: b['l'] = {'C': C2, 'G': G2}[b['l']]
ode['title'] = 'Ode to Joy, Again'
g.update(job='You played this as Song 5, with one key a bar. Here it is with the left hand you have now. Same tune, bigger left hand.', today='Block chord',
         fmap={'c': 5, 'd': 4, 'g': 1}, tool_cap='C chord: C and G (5, 1). G chord: D and G (4, 1). In line 3 the thumb plays one tune note, G.',
         song_how='<b>Then</b> (Song 5): one key a bar. <b>Now</b>: two keys together, on beat 1, held to the end of the bar.')
ORDER = [old(1), old(2), old(3), old(4), old(5), old(6), old(7), old(8), old(9), old(10), old(12), canon, old(11), rhody, longago, ode, old(14), old(15), old(13)]
UNIT = {1: 'Unit 1 · Roots: one key for every chord', 12: 'The end of Unit 1 · one root under every note', 13: 'Unit 2 · Block chord: two keys together', 17: 'Unit 3 · The left hand joins the tune', 19: 'The last song'}
P = 1; n = len(ORDER)
for i, d in enumerate(ORDER, 1):
    d.update(id=f'me{i}', lesson=i, label='End of Music Box 1' if i == n else f'Song {i}', page0=P)
    json.dump(d, open(f'me{i}.json', 'w'), ensure_ascii=False)
    P += len(PdfReader(f'lesson-me{i}.pdf').pages) if os.path.exists(f'lesson-me{i}.pdf') else 1
rows = ''
for i, d in enumerate(ORDER, 1):
    if i in UNIT: rows += f'<tr class="u"><td colspan="3">{UNIT[i]}</td></tr>'
    rows += f'<tr><td class="n">{i}</td><td><b>{d["title"]}</b></td><td>{d["gig"].get("today") or ""}</td></tr>'
p1 = f'''<div class="kick">Start here</div><h1>Music Box 1</h1><p class="byl">Nineteen songs, from one key to two</p>
{ST.LT}<table class="ftb"><tr><th style="width:5%"></th><th style="width:60%">Song</th><th style="width:35%">Left-hand pattern</th></tr>{rows}</table>'''
ST.save('me1.json', 'me0', 'Music Box 1', 'Start here', [p1], 0)
blk = [i for i, d in enumerate(ORDER, 1) if d['gig'].get('today') == 'Block chord']
c1 = ST.card(1, ST.INTRO, [('Roots', 'C - - -', 'One key: the letter in the chord’s name. Hold it.', 'Songs 1 to 12 and 18'),
                           ('Block chord', 'C+G - - -', 'The keys of the chord together. In this book, two: bottom and top. Hold them.', f'Songs {blk[0]} to {blk[-1]}')])
ST.save('me1.json', f'me{n + 1}', 'Pattern card', 'End of Music Box 1', [c1], P)
print('book 1 re-paced:', n, 'songs; card on page', P + 1)
