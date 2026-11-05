# The Piano Butler Workbook, Harmony: two pages per chapter (Learn, Use), matching Handbook Part III
exec(open('/tmp/claude-0/pk/wbpitch.py').read())   # helpers, css, SIZEJS, firstdone (rewrites the Pitch workbook, harmless)
def hpage2(inner, n, hb):
    return f'''<section class="pg"{' data-end="1"' if not hb else ''}><div class="top"><span>THE PIANO BUTLER WORKBOOK</span><span>{'HARMONY · HANDBOOK P. ' + str(hb) if hb else 'HARMONY'}</span></div><div class="rule"></div><div class="body">{inner}</div>
<div class="sign"><span style="flex:0 0 240px">Date <i></i></span></div><div class="foot"><span>{n}</span></div></section>'''
def th(kind, topic, title, rule, inner, n, hb):
    return hpage2(f'<div class="kick">Harmony · {topic} · {kind}</div><h1>{title}</h1><p class="rem2"><span>Remember</span>{rule}</p>{inner}', n, hb)
def DONE(k, lab=''):   # a worked first answer drawn on the staff, in red
    f = wpx(k, 84, 26).replace('class="chord">', 'class="chord" style="fill:#e4572e;color:#e4572e">')
    return f'<div class="fc">{f}<div class="add">{lab}</div></div>'
KW = 30
def kdot(i, t, y=62): return f'<circle cx="{i * KW + KW / 2}" cy="{y}" r="9" fill="#e4572e"/><text x="{i * KW + KW / 2}" y="{y + 4}" text-anchor="middle" font-family="AH,Arial" font-size="10" font-weight="700" fill="#fff">{t}</text>'

# ---------- 1 Chords and triads (Handbook pp. 64–65) ----------
HA1 = th('Learn', 'Chords and triads', 'Chords and triads', 'A triad is three notes stacked in 3rds: root, 3rd, 5th. Play one, skip one.', f'''
{ex(1, 'Build it', 1, 'Write the 3rd and the 5th above each root: play one, skip one. The first row is done.', tbl(['Root', '3rd', '5th', 'Root', '3rd', '5th'], [['<b>C</b>', '<b class="done2">E</b>', '<b class="done2">G</b>', '<b>G</b>', BOX, BOX], ['<b>D</b>', BOX, BOX, '<b>A</b>', BOX, BOX], ['<b>F</b>', BOX, BOX, '<b>B</b>', BOX, BOX]], ['14%', '18%', '18%', '14%', '18%', '18%'], 'bld'))}
{ex(2, 'On the keyboard', 1, 'Mark the root, 3rd and 5th of the F triad with 1, 3 and 5. The C triad is done.', '<div class="two" style="grid-template-columns:1fr 1fr">' + kbd('C', 8, KW, 78, label=True, shade={1: '#eef0f8', 3: '#eef0f8'}, marks=[kdot(0, '1', 52), kdot(2, '3', 52), kdot(4, '5', 52)]) + kbd('C', 8, KW, 78, label=True) + '</div><div class="anrow"><span><b>C triad</b> C E G</span><span><b>F triad</b>' + BOX + BOX + BOX + '</span></div>')}
{ex(3, 'Name the triad', 1, 'Write the root of each triad: the bottom note names it.', grid([pc('hn%d' % i, BOX, 58) for i in range(6)], 3))}
{ex(4, 'Play it', 1, 'Play C, F and G triads, solid then broken, each hand alone. Tick a circle each clean day.', '<div class="ts6">' + ''.join(f'<div><b>{s}</b>{ticks(4)}</div>' for s in ('C triad', 'F triad', 'G triad')) + '</div>')}''', 1, 64)
HB1 = th('Use', 'Chords and triads', 'Chords and triads', 'A stacked triad sits on three lines in a row or in three spaces in a row.', f'''
{ex(1, 'Lines or spaces?', 1, 'Circle lines or spaces for each triad.', grid([pc('hl%d' % i, circ('lines', 'spaces'), 58) for i in range(3)], 3))}
{ex(2, 'Is it a triad?', 2, 'Circle ✓ if the chord is stacked in 3rds, ✗ if it is not.', grid([pc('hi%d' % i, circ('✓', '✗'), 58) for i in range(4)], 4))}
{ex(3, 'Draw it', 2, 'Draw the 3rd and the 5th above each root, as semibreves stacked on top of it. The first is done.', grid([DONE('updone_c')] + [pc('uph%d' % i, '', 58) for i in range(1, 6)], 3))}
{ex(4, 'Solid or broken?', 1, 'Circle solid or broken.', grid([pc('hs%d' % i, circ('solid', 'broken'), 58) for i in range(4)], 4))}''', 2, 65)

# ---------- 2 Four kinds of triad (Handbook pp. 66–67) ----------
HA2 = th('Learn', 'Four kinds of triad', 'Four kinds of triad', 'Count the keys in between, black and white: major 3 + 2, minor 2 + 3, diminished 2 + 2, augmented 3 + 3.', f'''
{ex(1, 'Count the keys between', 1, 'Count the keys you skip, black and white: root to 3rd, then 3rd to 5th. Then write the kind. The first row is done.', tbl(['Triad', 'Root to 3rd', '3rd to 5th', 'Kind'], [['<b>C E G</b>', '<b class="done2">3</b>', '<b class="done2">2</b>', '<b class="done2">major</b>']] + [[f'<b>{t}</b>', BOX, BOX, LINE] for t in ('A C E', 'G B D', 'E G B', 'B D F')], ['25%', '22%', '22%', '31%'], 'bld'))}
{ex(2, 'Which kind?', 2, 'Write major, minor, dim or aug under each triad.', grid([pc('wk%d' % i, BOX, 58) for i in range(6)], 3))}
{ex(3, 'Major to minor', 1, 'Lower the 3rd by a semitone to make each major triad minor. The first is done.', tbl(['Major', 'Minor'], [['<b>C E G</b>', '<b class="done2">C E♭ G</b>']] + [[f'<b>{t}</b>', LINE] for t in ('F A C', 'G B D', 'D F♯ A')], ['40%', '60%'], 'bld'))}''', 3, 66)
HB2 = th('Use', 'Four kinds of triad', 'Four kinds of triad', 'Keys in between: major 3 + 2, minor 2 + 3.', f'''
{ex(1, 'Draw major and minor', 2, 'Draw a triad above each root: major on the top row, minor on the bottom row. Watch for sharps and flats. The first is done.', grid([DONE('updone_d', 'major')] + [pc('uph%d' % i, l, 58) for i, l in ((4, 'major'), (5, 'major'), (0, 'minor'), (2, 'minor'), (1, 'minor'))], 3))}
{ex(2, 'Bright or dark?', 1, 'Play each triad and circle what you hear.', ''.join(f'<div class="row"><b>{t}</b><span class="tf">bright &nbsp;·&nbsp; dark</span></div>' for t in ('C E G', 'A C E', 'G B D', 'D F A')))}
{ex(3, 'Sort the white keys', 2, 'Write the kind of each white-key triad. The first is done.', tbl(['Triad on', 'C', 'D', 'E', 'F', 'G', 'A', 'B'], [['<b>Kind</b>', '<b class="done2">major</b>'] + [LINE] * 6], ['16%'] + ['12%'] * 7, 'bld'))}
{ex(4, 'Play the four kinds', 1, 'Play C major, C minor, C diminished and C augmented, each hand alone. Tick a circle each day.', '<div class="ts6" style="grid-template-columns:1fr 1fr">' + ''.join(f'<div><b>{t}</b>{ticks(4)}</div>' for t in ('C major', 'C minor', 'C diminished', 'C augmented')) + '</div>')}''', 4, 67)

# ---------- 3 Chords in a key (Handbook pp. 68–69) ----------
NUMS = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']
HA3 = th('Learn', 'Chords in a key', 'Chords in a key', 'I on the 1st note, IV on the 4th, V on the 5th. Capitals major, small minor, ° diminished.', f"""
{ex(1, 'Number the chords', 1, 'Write the numeral for each triad of C major.', tbl(['Triad', 'C E G', 'D F A', 'E G B', 'F A C', 'G B D', 'A C E', 'B D F'], [['<b>Numeral</b>', '<b class="done2">I</b>'] + [LINE] * 6], ['16%'] + ['12%'] * 7, 'bld'))}
{ex(2, 'Find I, IV and V', 2, 'Write the letter names of chords I, IV and V in each key (F major has B♭). The first row is done.', tbl(['Key', 'I', 'IV', 'V'], [['<b>C major</b>', '<b class="done2">C</b>', '<b class="done2">F</b>', '<b class="done2">G</b>']] + [[f'<b>{k}</b>', BOX, BOX, BOX] for k in ('G major', 'F major', 'D major')], ['31%', '23%', '23%', '23%'], 'bld'))}
{ex(3, 'Spell them', 2, 'Write the three notes of I, IV and V in G major (one sharp: F♯). The first is done.', tbl(['Chord', 'Notes'], [['<b>I (G)</b>', '<b class="done2">G B D</b>'], ['<b>IV (C)</b>', LINE], ['<b>V (D)</b>', LINE]], ['30%', '70%'], 'bld'))}
{ex(4, 'Numerals on the staff', 2, 'These are chords of C major. Write the numeral under each.', grid([pc(k, BOX, 50) for k in ('hn1', 'hn2', 'hn3', 'hn4')], 4, 'tight'))}
{ex(5, 'Home, visit, walk back', 1, 'Play I, IV, V, I in C, then in G, left hand. Tick a circle each smooth day.', '<div class="ts6" style="grid-template-columns:1fr 1fr">' + ''.join(f'<div><b>{t}</b>{ticks(4)}</div>' for t in ('C: C F G C', 'G: G C D G')) + '</div>')}""", 5, 68)
HB3 = th('Use', 'Chords in a key', 'Chords in a key', 'I holds C E G, IV holds F A C, V holds G B D: every note of C major is in one of them.', f"""
{ex(1, 'Which chord holds it?', 1, 'Write I, IV or V for each note of C major. C and G fit two chords: write both.', '<div class="anrow">' + ''.join(f'<span><b>{n}</b>{BOX}</span>' for n in ('C', 'D', 'E', 'F', 'G', 'A', 'B')) + '</div>')}
{ex(2, 'Chords for Twinkle', 2, 'Write I, IV or V at the start of each bar, and again halfway through bars 2, 3 and 4.', wpx('w_twk', 70) + '<div class="anrow">' + ''.join(f'<span><b>{l}</b>{BOX}</span>' for l in ('bar 1', 'bar 2', '½', 'bar 3', '½', 'bar 4', '½')) + '</div>')}
{ex(3, 'The twelve-bar blues', 2, 'The same chart in G major: write the letter of each chord (I = G).', '<div class="bl12">' + ''.join(f'<span><i>{n}</i>{BOX}</span>' for n in ['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'IV', 'I', 'V']) + '</div>')}
{ex(4, 'Chords in A minor', 2, 'Write the notes of i, iv and V in A minor. Remember the raised 7th, G♯, in V.', tbl(['Chord', 'Notes'], [['<b>i (A minor)</b>', LINE], ['<b>iv (D minor)</b>', LINE], ['<b>V (E major)</b>', LINE]], ['34%', '66%'], 'bld'))}
{ex(5, 'Play the blues', 2, 'Play the twelve bars in C and in G with your left hand, four steady beats on each chord. Tick a circle each time you reach the end without stopping.', ticks(5))}""", 6, 69)

# ---------- 4 Inversions (Handbook pp. 70–71) ----------
def pos3(t): return f'<div class="row"><b>{t}</b><span class="tf">root &nbsp;·&nbsp; 1st &nbsp;·&nbsp; 2nd</span></div>'
HA4 = th('Learn', 'Inversions', 'Inversions', 'Root at the bottom: root position. 3rd at the bottom: 1st inversion. 5th at the bottom: 2nd inversion.', f"""
{ex(1, 'Which position?', 1, 'Circle the position of each C, F or G major chord (read from the bottom note up).', ''.join(pos3(t) for t in ('C E G', 'E G C', 'G C E', 'A C F', 'C F A', 'B D G')))}
{ex(2, 'Find the root', 2, 'Restack each chord in 3rds and write its root.', grid([pc('wi%d' % i, BOX, 58) for i in range(6)], 3))}
{ex(3, 'Write the inversions', 2, 'Write each chord in its 1st and 2nd inversion. The first row is done.', tbl(['Chord', 'Root position', '1st inversion', '2nd inversion'], [['<b>C</b>', 'C E G', '<b class="done2">E G C</b>', '<b class="done2">G C E</b>'], ['<b>F</b>', 'F A C', LINE, LINE], ['<b>G</b>', 'G B D', LINE, LINE], ['<b>Am</b>', 'A C E', LINE, LINE]], ['16%', '28%', '28%', '28%'], 'bld'))}""", 7, 70)
HB4 = th('Use', 'Inversions', 'Inversions', 'Keep any shared note; move the others to the nearest note of the next chord.', f"""
{ex(1, 'Draw the 2nd inversion', 2, 'Next to each chord, draw its 2nd inversion: lift the two bottom notes to the top. Example: C E G becomes G C E.', grid([pc('upi%d' % i, '', 58) for i in range(3)], 3))}
{ex(2, 'Slash chords', 2, 'Write the notes from the bottom up. The first is done.', tbl(['Symbol', 'Notes, bottom up'], [['<b>C/E</b>', '<b class="done2">E G C</b>'], ['<b>G/B</b>', LINE], ['<b>F/A</b>', LINE], ['<b>Am/C</b>', LINE]], ['30%', '70%'], 'bld'))}
{ex(3, 'The common note', 2, 'Write the note (or notes) the two chords share. The first is done.', tbl(['Chords', 'Shared', 'Chords', 'Shared'], [['<b>C and F</b>', '<b class="done2">C</b>', '<b>Am and F</b>', LINE], ['<b>C and G</b>', LINE, '<b>Em and C</b>', LINE]], ['25%', '25%', '25%', '25%'], 'bld'))}
{ex(4, 'Name it', 2, 'Write the chord symbol with its bass note, like C/E.', grid([pc(k, BOX, 50) for k in ('wi0', 'wi3', 'wi4', 'wi2')], 4, 'tight'))}
{ex(5, 'Play it smoothly', 1, 'Play C E G, C F A, B D G, C E G, left hand; then in G: G B D, G C E, F♯ A D, G B D.', '<div class="ts6" style="grid-template-columns:1fr 1fr">' + ''.join(f'<div><b>{t}</b>{ticks(4)}</div>' for t in ('in C', 'in G')) + '</div>')}""", 8, 71)
hans = [('p. 1', 'Build it: C E G · D F A · F A C · G B D · A C E · B D F. Keyboard: F A C. Name the triad: C, F, G, D, A, E.'),
        ('p. 2', 'Lines or spaces: lines, spaces, lines. Is it a triad: ✓, ✗, ✓, ✗. Draw it: C E G, F A C, G B D, D F A, A C E, E G B. Solid or broken: solid, broken, solid, broken.'),
        ('p. 3', 'Keys between: C E G 3 + 2 major · A C E 2 + 3 minor · G B D 3 + 2 major · E G B 2 + 3 minor · B D F 2 + 2 diminished. Which kind: minor, major, dim, aug, minor, major. Major to minor: C E♭ G · F A♭ C · G B♭ D · D F A.'),
        ('p. 4', 'Draw: major D F♯ A, A C♯ E, E G♯ B; minor C E♭ G, G B♭ D, F A♭ C. Bright or dark: bright, dark, bright, dark. White keys: C major, D minor, E minor, F major, G major, A minor, B diminished.'),
        ('p. 5', 'Numerals: I, ii, iii, IV, V, vi, vii°. I IV V: G C D · F B♭ C · D G A. In G: G B D · C E G · D F♯ A. On the staff: IV, V, ii, vi.'),
        ('p. 6', 'Which chord: C I or IV · D V · E I · F IV · G I or V · A IV · B V. Twinkle: I · IV I · IV I · V I. Blues in G: G G G G · C C G G · D C G D. A minor: A C E · D F A · E G♯ B.'),
        ('p. 7', 'Position: root, 1st, 2nd, 1st, 2nd, 1st. Roots: C, F, G, F, G, C. Inversions: F: A C F, C F A · G: B D G, D G B · Am: C E A, E A C.'),
        ('p. 8', 'Draw: G C E, C F A, D G B. Name it: C/E, F/C, G/D, G/B. Slash chords: B D G · A C F · C E A. Common notes: C and G: G · Am and F: A, C · Em and C: E, G.')]
HAN = hpage2(f'''<div class="kick">Harmony · Answers</div><h1>Answers</h1>
{tbl(['Page', 'Answers'], [[p, a] for p, a in hans], ['12%', '88%'], 'ansT')}
<p class="sm">“Play it” has no single answer to copy: check it at the piano with your teacher, or with the online lessons.</p>''', 9, None)
css += '''
.tight .fc .px{padding-top:0;padding-bottom:0} .bl12{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 14px;max-width:520px;margin:6px auto} .bl12 span{display:flex;align-items:center;justify-content:center;gap:8px;border:1px solid #e2ddd0;padding:6px} .bl12 i{font-style:normal;font-weight:700;color:#6d6f9c;min-width:22px} .bld td,.bld th{text-align:center} .bld td{padding-top:3px;padding-bottom:3px} .bld td b{font-size:16px} .bld .ab{margin:0 auto}
'''
HFIRST = {'Name it': [('fill', 'C/E')], 'Which position?': [('ring', 'root')], 'Find the root': [('fill', 'C')], 'Which chord holds it?': [('fill', 'I, IV')], 'Numerals on the staff': [('fill', 'IV')], 'Chords in A minor': [('fill', 'A C E')], 'Chords for Twinkle': [('fill', 'I')], 'The twelve-bar blues': [('fill', 'G')], 'Which kind?': [('fill', 'minor')], 'Bright or dark?': [('ring', 'bright')], 'Name the triad': [('fill', 'C')], 'Lines or spaces?': [('ring', 'lines')], 'Is it a triad?': [('ring', '✓')], 'Solid or broken?': [('ring', 'solid')]}
open('/mnt/user-data/outputs/house-rooms/workbook-harmony.html', 'w').write(firstdone.apply(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{HA1}{HB1}{HA2}{HB2}{HA3}{HB3}{HA4}{HB4}{HAN}{SIZEJS}</body></html>', HFIRST).replace('</style></head>', firstdone.CSS + '</style></head>', 1))
print('ok')
