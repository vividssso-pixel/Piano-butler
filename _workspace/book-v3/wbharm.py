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
HA2 = th('Learn', 'Four kinds of triad', 'Four kinds of triad', 'Major 3rd = 4 semitones, minor 3rd = 3. Major: major below, minor above. Minor: the other way round.', f'''
{ex(1, 'Count the 3rds', 1, 'Count the semitones in each 3rd, then write the kind. The first row is done.', tbl(['Triad', 'Bottom 3rd', 'Top 3rd', 'Kind'], [['<b>C E G</b>', '<b class="done2">4</b>', '<b class="done2">3</b>', '<b class="done2">major</b>']] + [[f'<b>{t}</b>', BOX, BOX, LINE] for t in ('A C E', 'G B D', 'E G B', 'B D F')], ['25%', '22%', '22%', '31%'], 'bld'))}
{ex(2, 'Which kind?', 2, 'Write major, minor, dim or aug under each triad.', grid([pc('wk%d' % i, BOX, 58) for i in range(6)], 3))}
{ex(3, 'Major to minor', 1, 'Lower the 3rd by a semitone to make each major triad minor. The first is done.', tbl(['Major', 'Minor'], [['<b>C E G</b>', '<b class="done2">C E♭ G</b>']] + [[f'<b>{t}</b>', LINE] for t in ('F A C', 'G B D', 'D F♯ A')], ['40%', '60%'], 'bld'))}''', 3, 66)
HB2 = th('Use', 'Four kinds of triad', 'Four kinds of triad', 'A minor triad has the short 3rd at the bottom: 3 semitones, then 4. A major triad has the tall one: 4, then 3.', f'''
{ex(1, 'Draw major and minor', 2, 'Draw a triad above each root: major on the top row, minor on the bottom row. Watch for sharps and flats. The first is done.', grid([DONE('updone_d', 'major')] + [pc('uph%d' % i, l, 58) for i, l in ((4, 'major'), (5, 'major'), (0, 'minor'), (2, 'minor'), (1, 'minor'))], 3))}
{ex(2, 'Bright or dark?', 1, 'Play each triad and circle what you hear.', ''.join(f'<div class="row"><b>{t}</b><span class="tf">bright &nbsp;·&nbsp; dark</span></div>' for t in ('C E G', 'A C E', 'G B D', 'D F A')))}
{ex(3, 'Sort the white keys', 2, 'Write the kind of each white-key triad. The first is done.', tbl(['Triad on', 'C', 'D', 'E', 'F', 'G', 'A', 'B'], [['<b>Kind</b>', '<b class="done2">major</b>'] + [LINE] * 6], ['16%'] + ['12%'] * 7, 'bld'))}
{ex(4, 'Play the four kinds', 1, 'Play C major, C minor, C diminished and C augmented, each hand alone. Tick a circle each day.', '<div class="ts6" style="grid-template-columns:1fr 1fr">' + ''.join(f'<div><b>{t}</b>{ticks(4)}</div>' for t in ('C major', 'C minor', 'C diminished', 'C augmented')) + '</div>')}''', 4, 67)
hans = [('p. 1', 'Build it: C E G · D F A · F A C · G B D · A C E · B D F. Keyboard: F A C. Name the triad: C, F, G, D, A, E.'),
        ('p. 2', 'Lines or spaces: lines, spaces, lines. Is it a triad: ✓, ✗, ✓, ✗. Draw it: C E G, F A C, G B D, D F A, A C E, E G B. Solid or broken: solid, broken, solid, broken.'),
        ('p. 3', 'Count the 3rds: C E G 4, 3 major · A C E 3, 4 minor · G B D 4, 3 major · E G B 3, 4 minor · B D F 3, 3 diminished. Which kind: minor, major, dim, aug, minor, major. Major to minor: C E♭ G · F A♭ C · G B♭ D · D F A.'),
        ('p. 4', 'Draw: major D F♯ A, A C♯ E, E G♯ B; minor C E♭ G, G B♭ D, F A♭ C. Bright or dark: bright, dark, bright, dark. White keys: C major, D minor, E minor, F major, G major, A minor, B diminished.')]
HAN = hpage2(f'''<div class="kick">Harmony · Answers</div><h1>Answers</h1>
{tbl(['Page', 'Answers'], [[p, a] for p, a in hans], ['12%', '88%'], 'ansT')}
<p class="sm">“Play it” has no single answer to copy: check it at the piano with your teacher, or with the online lessons.</p>''', 5, None)
css += '''
.bld td{text-align:center} .bld td b{font-size:16px} .bld .ab{margin:0 auto}
'''
HFIRST = {'Which kind?': [('fill', 'minor')], 'Bright or dark?': [('ring', 'bright')], 'Name the triad': [('fill', 'C')], 'Lines or spaces?': [('ring', 'lines')], 'Is it a triad?': [('ring', '✓')], 'Solid or broken?': [('ring', 'solid')]}
open('/mnt/user-data/outputs/house-rooms/workbook-harmony.html', 'w').write(firstdone.apply(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{HA1}{HB1}{HA2}{HB2}{HAN}{SIZEJS}</body></html>', HFIRST).replace('</style></head>', firstdone.CSS + '</style></head>', 1))
print('ok')
