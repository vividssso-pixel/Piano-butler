# Kept for a later book: Songs 13-15 with the whole tune in the right hand and chords in the left (27 Nov, not used in Music Box 1).

# ---- 27 Nov 11:50, her '13-15 반주 넣어줘': Songs 13 to 15 get a left-hand accompaniment. The whole tune moves into the right hand
# (an octave up where it used to dip below middle C; Amazing Grace moves to G, where it needs no black key), and the left hand plays chords.
def _acc(n, rows, **kw):
    d = json.load(open(f'mb{n}.json')); g = d['gig']
    g['song_grid'] = [[dict({'r': r, 'w': w, 'f': f}, **({'lp': l} if (' ' in l) else {'l': l})) for r, l, f, w in ln] for ln in rows]
    for k, v in kw.items(): g[k] = v
    json.dump(d, open(f'mb{n}.json', 'w'), ensure_ascii=False)
CH = 'C: C and G (5, 1). G: D and G (4, 1). F: C and F (5, 2).'
_acc(13, [[('r r G.G', '', '- - 1.1', '- - Hap.py'), ("A G C'", 'C+G', '2 1 4', 'birth- day to'), ('B - G.G', 'D+G', '3 - 1.1', 'you, - Hap.py'), ("A G D'", 'D+G', '2 1 5', 'birth- day to'), ("C' - G.G", 'C+G', '4 - 1.1', 'you, - Hap.py')],
          [("G' E' C'", 'C+G', '5 3 1', 'birth- day dear'), ("B A F'.F'", 'C+F', '2 1 4.4', '(name), - Hap.py'), ("E' C' D'", 'C+G', '3 1 2', 'birth- day to'), ("C' - -", 'C+G', '1 - -', 'you! - -')]],
     today='Block chord', lkb=['c', 5, '5 4 . 2 1'], rkb=['g', 8, '1 2 3 4 5 x x x'], tool_cap=CH,
     job='The song for every birthday, in three: ONE two three. Now the left hand plays chords under the whole tune.',
     r_cap='Thumb on G. A small arrow ↑ marks the higher C, D, E, F and G. The numbers show where the hand moves.',
     song_how='New: a song in three. It starts on beat 3 with two quick notes. Hold each chord for the whole bar.')
_acc(14, [[("C' C' D' E'", 'C+G', '1 1 2 3', 'Yan- kee Doo- dle'), ("C' E' D' G", 'C+G', '1 3 2 1', 'went to town a-'), ("C' C' D' E'", 'C+G', '1 1 2 3', 'rid- ing on a'), ("C' - B -", 'D+G', '1 - 2 -', 'po- - ny, -')],
          [("C' C' D' E'", 'C+G', '1 1 2 3', 'stuck a fea- ther'), ("F' E' D' C'", 'C+F', '4 3 2 1', 'in his cap and'), ('B G A B', 'D+G', '3 1 2 3', 'called it ma- ca-'), ("C' - C' -", 'C+G', '4 - 4 -', 'ro- - ni. -')],
          [('A -.B A G', 'C+F', '2 -.3 2 1', 'Yan- -.kee Doo- dle'), ("A B C' A", 'C+F', '2 3 4 2', 'keep it up, -'), ('G -.A G F', 'C+G', '3 -.4 3 2', 'Yan- -.kee Doo- dle'), ('E - G -', 'C+G', '1 - 3 -', 'dan- - dy, -')],
          [('A -.B A G', 'C+F', '2 -.3 2 1', 'mind -.the mu- sic'), ("A B C' A", 'C+F', '2 3 4 2', 'and the step and'), ("G C' B D'", 'D+G', '1 4 3 5', 'with the girls be'), ("C' - C' -", 'C+G', '4 - 4 -', 'han- - dy. -')]],
     today='Block chord', lkb=['c', 5, '5 4 . 2 1'], rkb=['e', 9, 'x x 1 2 3 4 5 x x'], tool_cap=CH,
     r_cap='Thumb on G, or on the high C (C↑): the numbers show each move.',
     song_how='Keep marching: 1 2 3 4. Lines 3 and 4 are the chorus.')
AG = lambda r, l, f, w='- - -': (r, l, f, w)
_acc(15, [[AG('r r D', '', '- - 1', '- - A-'), AG('G - B.G', 'G', '1 - 3.1', 'ma- - zing.-'), AG('B - A', 'G', '3 - 2', 'grace, - how'), AG('G - E', 'C', '4 - 2', 'sweet - the'), AG('D - D', 'G', '1 - 1', 'sound, - that')],
          [AG('G - B.G', 'G', '1 - 3.1', 'saved - a.-'), AG('B - A.B', 'G', '3 - 2.3', 'wretch - like.-'), AG("D' - -", 'D', '5 - -', 'me! - -'), AG("- - B.D'", 'D', '- - 3.5', '- - I.-')],
          [AG("D' - B.G", 'G', '5 - 3.1', 'once - was.-'), AG('B - A', 'G', '3 - 2', 'lost, - but'), AG('G - E', 'C', '4 - 2', 'now - am'), AG('D - D', 'G', '1 - 1', 'found, - was')],
          [AG('G - B.G', 'G', '1 - 3.1', 'blind, - but.-'), AG('B - A', 'D', '3 - 2', 'now - I'), AG('G - -', 'G', '1 - -', 'see. - -')]],
     today='Roots', lkb=['g', 5, '5 . . 2 1', None, 120], rkb=['d', 8, '1 2 . 4 5 x . x'],
     job='A slow song in three, two hundred years old. Let every long note ring.',
     tool_cap='Home is G now: G with 5, C with 2, D with the thumb.',
     r_cap='Low place: thumb on D. High place: thumb on G. D↑ is the D above.',
     song_how='Slow, in three. The song starts on beat 3. A line holds the note; it can carry on into the next bar.')
