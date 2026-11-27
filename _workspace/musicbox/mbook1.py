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
# ---- Happy Birthday twice (her 27 Nov 17:34 and 18:22): it closes Unit 1 with Roots, and closes the book with Block chord.
# The whole tune is in the right hand (thumb on G, up to the higher G), the rows kept in mbox-rh-only-13-15.py. Same tune, bigger left hand.
HB = [[('r r G.G', '', '- - 1.1', '- - Hap.py'), ("A G C'", 'C', '2 1 4', 'birth- day to'), ('B - G.G', 'G', '3 - 1.1', 'you, - Hap.py'), ("A G D'", 'G', '2 1 5', 'birth- day to'), ("C' - G.G", 'C', '4 - 1.1', 'you, - Hap.py')],
      [("G' E' C'", 'C', '5 3 1', 'birth- day dear'), ("B A F'.F'", 'F', '2 1 4.4', '(name), - Hap.py'), ("E' C' D'", 'C', '3 1 2', 'birth- day to'), ("C' - -", 'C', '1 - -', 'you! - -')]]
def hbsong(block):
    d = old(13); g = d['gig']
    for k in ('ways', 'ways_job', 'ways_how', 'ways_title', 'note'): g.pop(k, None)
    two = {'C': 'C+G', 'G': 'D+G', 'F': 'C+F'}
    g['song_grid'] = [[{'r': r, 'l': (two.get(l, l) if block else l), 'f': f, 'w': w} for r, l, f, w in ln] for ln in HB]
    g.update(rmap={'g': 1, 'a': 2, 'b': 3, 'c': 4, 'd': 5}, rfing={'G': 1, 'A': 2, 'B': 3, 'C': 4, 'D': 5}, rkb=['g', 8, '1 2 3 4 5 x x x'],
             r_cap='Thumb on G. A small arrow ↑ marks the higher C, D, E, F and G. The numbers show where the hand moves.')
    if block:
        d['title'] = 'Happy Birthday, Again'
        g.update(today='Block chord', fmap={'c': 5, 'd': 4, 'f': 2, 'g': 1}, lkb=['c', 5, '5 4 . 2 1'], tool_cap='C chord: C and G (5, 1). G chord: D and G (4, 1). F chord: C and F (5, 2).',
                 job='You played this at the end of Unit 1 with one key a bar. Now the same tune with the left hand you have now. Play it at the next birthday.',
                 song_how='<b>Then</b>: one key a bar. <b>Now</b>: two keys together on beat 1, held for the whole bar. It starts on beat 3 with two quick notes.')
    else:
        g.update(today='Roots', fmap={'c': 5, 'f': 2, 'g': 1}, lkb=['c', 5, '5 . . 2 1'], tool_cap='C with 5, F with 2, G with 1. One key on beat 1, held for the whole bar.',
                 job='The song for every birthday, in three: ONE two three. The right hand plays the whole tune; the left hand plays one root a bar.',
                 song_how='New: a song in three. It starts on beat 3 with two quick notes. Hold each left-hand key for the whole bar.')
    return d
# ---- Two more Block chord songs (27 Nov 21:41): the same tunes as Music Box 2 Songs 1 and 2, already checked there
# (Essen, Alle meine Entchen; Nottingham Music Database, Oh Susanna). Here in letters, with the two-key left hand.
TWO = {'C': 'C+G', 'G': 'D+G', 'F': 'C+F'}
def from2(n, fing):
    rows = []
    for ln in json.load(open(f'mc{n}.json'))['gig']['song_grid']:
        row = []
        for b in ln:
            ch = (b.get('ch') or '').split()
            if not ch: row.append(B(b['r'], '', b.get('f'))); continue
            if len(ch) == 1: row.append(B(b['r'], TWO[ch[0]], b.get('f') or fing(b['r']), TWO[ch[0]] + ' - - -'))
            else: row.append(B(b['r'], TWO[ch[0]], b.get('f') or fing(b['r']), ' '.join(TWO.get(x, x) for x in ch)))
        rows.append(row)
    return rows
RF = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 5}
ducks = new('mb11.json', 'All My Little Ducklings', 'German folk song',
    'Little ducks swimming on the lake, heads in the water, tails up high. A short song to start Unit 2: two keys in the left hand, held for the whole bar.',
    'The left hand changes only on beat 1. Press both keys together and hold them for the whole bar.',
    from2(1, None), 'Block chord', {'c': 5, 'd': 4, 'f': 2, 'g': 1}, 'C chord: C and G (5, 1). G chord: D and G (4, 1). F chord: C and F (5, 2).',
    'Thumb on middle C. A is one key past your little finger: reach for it, then come back.', rfing=RF, rmap={'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 5})
susanna = new('mb11.json', 'Oh! Susanna', 'Stephen Foster, 1848',
    'A song from 1848 about a long journey with a banjo on your knee. It starts before bar 1, with two quick notes on beat 4.',
    'Count 1 2 3 out loud, then play C D on <i>four-and</i>. In two bars the chord changes on beat 3.',
    from2(2, None), 'Block chord', {'c': 5, 'd': 4, 'f': 2, 'g': 1}, 'C chord: C and G (5, 1). G chord: D and G (4, 1). F chord: C and F (5, 2).',
    'Thumb on middle C. Reach finger 5 to A, as in All My Little Ducklings.', rfing=RF, rmap={'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 5})
ORDER = [old(1), old(2), old(3), old(4), old(5), old(6), old(7), old(8), old(9), old(10), old(12), canon, hbsong(False), ducks, old(11), rhody, susanna, longago, ode, old(14), old(15), hbsong(True)]
UNIT = {1: 'Unit 1 · Roots: one key for every chord', 13: 'The end of Unit 1', 14: 'Unit 2 · Block chord: two keys together', 20: 'Unit 3 · The left hand joins the tune', 22: 'The last song: the same tune, a bigger left hand'}
P = 1; n = len(ORDER)
for i, d in enumerate(ORDER, 1):
    d.update(id=f'me{i}', lesson=i, label='End of Music Box 1' if i == n else f'Song {i}', page0=P)
    json.dump(d, open(f'me{i}.json', 'w'), ensure_ascii=False)
    P += len(PdfReader(f'lesson-me{i}.pdf').pages) if os.path.exists(f'lesson-me{i}.pdf') else 1
rows = ''
for i, d in enumerate(ORDER, 1):
    if i in UNIT: rows += f'<tr class="u"><td colspan="3">{UNIT[i]}</td></tr>'
    rows += f'<tr><td class="n">{i}</td><td><b>{d["title"]}</b></td><td>{d["gig"].get("today") or ""}</td></tr>'
p1 = f'''<div class="kick">Start here</div><h1>Music Box 1</h1><p class="byl">Twenty-two songs, from one key to two</p>
{ST.LT}<table class="ftb sm"><tr><th style="width:5%"></th><th style="width:60%">Song</th><th style="width:35%">Left-hand pattern</th></tr>{rows}</table>'''
ST.save('me1.json', 'me0', 'Music Box 1', 'Start here', [p1], 0)
def said(ns):   # [1,2,3,5,6] -> 'Songs 1 to 3, 5 and 6'
    runs = []
    for n in ns:
        if runs and n == runs[-1][1] + 1: runs[-1][1] = n
        else: runs.append([n, n])
    t = [f'{a}' if a == b else f'{a} and {b}' if b == a + 1 else f'{a} to {b}' for a, b in runs]
    return 'Songs ' + (', '.join(t[:-1]) + ' and ' + t[-1] if len(t) > 1 else t[0])
blk = [i for i, d in enumerate(ORDER, 1) if d['gig'].get('today') == 'Block chord']
c1 = ST.card(1, ST.INTRO, [('Roots', 'C - - -', 'One key: the letter in the chord’s name. Hold it.', said([i for i, d in enumerate(ORDER, 1) if d['gig'].get('today') == 'Roots'])),
                           ('Block chord', 'C+G - - -', 'The keys of the chord together. In this book, two: bottom and top. Hold them.', said(blk))])
ST.save('me1.json', f'me{n + 1}', 'Pattern card', 'End of Music Box 1', [c1], P)
print('book 1 re-paced:', n, 'songs; card on page', P + 1)
