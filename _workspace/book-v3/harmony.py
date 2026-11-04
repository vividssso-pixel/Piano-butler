# The Piano Butler Handbook, Part III: Harmony (her 4 Nov: Harmony after Pitch and Time; the snowman for triads)
import re as _re
exec(open('/tmp/claude-0/pk/pitch.py').read())   # helpers, css, px / kbx / inaction / howto (rewrites the Pitch draft, harmless)
def hpage(inner, n): return page(inner, n, 'PART III · HARMONY')
W_ = 34   # white-key width in the keyboard pictures
def dot(i, t='', col='#e4572e', y=74): return f'<circle cx="{i * W_ + W_ / 2}" cy="{y}" r="11" fill="{col}"/>' + (f'<text x="{i * W_ + W_ / 2}" y="{y + 4}" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" fill="#fff">{t}</text>' if t else '')

YKDAN = '<figure class="vx"><div class="vs">' + P['yk_dan'].replace('<svg ', '<svg style="max-height:72px" ', 1) + '</div></figure>'   # (K. 545 and the Alberti bass wait for Harmony 6, in the bass clef: her 4 Nov)
for _n in ('n2', 'n3', 'n4'): YKDAN = YKDAN.replace(f'<g id="{_n}" class="note">', f'<g id="{_n}" class="note" style="fill:#e4572e;color:#e4572e">', 1)
# ---------- Part III opener ----------
HTOC = [('Chords and triads', 64), ('Four kinds of triad', 66), ('Chords in a key', 68), ('Inversions', 70), ('Cadences', 72), ('Chords under a melody', 74), ('The dominant 7th', 76), ('Tips: when a chord sounds wrong', 78)]
hflow = ''.join(f'<div class="fl"><b>{a}</b><span>{b}</span></div>' + ('<span class="fa">›</span>' if i < 4 else '') for i, (a, b) in enumerate([('Triads', 'three notes stacked in 3rds'), ('Kinds', 'major, minor, diminished, augmented'), ('Chords in a key', 'I, IV and V'), ('Inversions', 'the same chord, a new bass'), ('Cadences', 'the endings of phrases')]))
HOPEN = f"""<section class="pg part2"><div class="pframe"><div class="pk">Part III · Which notes sound together</div><div class="pt">Harmony</div><div class="pdv"></div>
<p class="pl">A melody moves one note at a time. Harmony is what sounds with it: the chords underneath. This part starts with the triad, three notes stacked in 3rds, and ends with the chords that close a phrase and pull a piece home.</p>
<div class="flow">{hflow}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{p}</span></div>' for x, p in HTOC)}</div></div></section>"""

# ---------- Harmony 1 · Chords and triads ----------
WHITE = [('C', 'E', 'G'), ('D', 'F', 'A'), ('E', 'G', 'B'), ('F', 'A', 'C'), ('G', 'B', 'D'), ('A', 'C', 'E'), ('B', 'D', 'F')]
SNOW = ('<svg viewBox="0 0 120 150" style="width:58px;height:auto;display:block;margin:0 auto">'
        '<circle cx="60" cy="118" r="28" fill="#fff" stroke="#26296b" stroke-width="2.5"/><circle cx="60" cy="70" r="21" fill="#fff" stroke="#26296b" stroke-width="2.5"/><circle cx="60" cy="33" r="15" fill="#fff" stroke="#26296b" stroke-width="2.5"/>'
        '<text x="60" y="123" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="#e4572e">C</text><text x="60" y="75" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="#26296b">E</text><text x="60" y="38" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="#26296b">G</text></svg>')
H1 = hpage(f"""{head('Part III · Harmony · 1', 'Chords and triads', 'A <b>chord</b> is two or more notes sounding together. The most common chord is the <b>triad</b>: three notes stacked in 3rds. The bottom note, the <b>root</b>, gives the chord its name.')}
{two(h3('Root, 3rd and 5th') + '<p>Start on any note: that is the <b>root</b>. Add the note a <b>3rd</b> above it, then the note a <b>5th</b> above the root. On the staff each note sits one line or one space above the last. C, E and G make the triad of C.</p><p class="sm">First met: Level ½ (the tonic triad of C, G and F major).</p>', px('h_build', 104, 'The root, then a 3rd above it, then a 5th above the root.'), '1.15fr 1fr')}
{h3('Play one, skip one')}
<div class="fk"><div class="fkf">{kbx('C', 8, W_, 100, label=True, shade={1: '#eef0f8', 3: '#eef0f8'}, marks=[dot(0, '1'), dot(2, '3'), dot(4, '5')], scale=1.0)}</div><div>On the white keys a triad is <b>play one, skip one, play one, skip one, play one</b>: C (skip D) E (skip F) G. The red keys are the root, the 3rd and the 5th; the skipped keys are shaded.</div></div>
{h3('The seven white-key triads')}
{tbl(['Triad on', 'Root', '3rd', '5th'], [[f'<b>{r}</b>', f'<b class="co">{r}</b>', t, f] for r, t, f in WHITE], ['31%', '23%', '23%', '23%'])}
{inaction('Build a triad on G', kbx('C', 10, W_, 92, label=True, shade={5: '#eef0f8', 7: '#eef0f8'}, marks=[dot(4, '1', y=62), dot(6, '3', y=62), dot(8, '5', y=62)], scale=1.0), ['<b>Start on G:</b> the root.', '<b>Skip A, play B:</b> the 3rd.', '<b>Skip C, play D:</b> the 5th.'], 'G B D: the triad of <b>G</b>. Same shape as C E G, just moved up.')}
{two(SNOW, thinkt('A snowman: three balls stacked, each one sitting just above the last with no gap and no overlap. The biggest ball at the bottom, the root, holds the whole thing up and gives it its name.'), '70px 1fr')}
<!--SPLIT-->
{two(h3('All lines or all spaces') + '<p>A stacked triad sits on <b>three lines in a row</b> or in <b>three spaces in a row</b>, like a snowman. If one note breaks the pattern, it is not a triad.</p>', px('h_ls', 80, 'Lines, spaces, lines, spaces: every one a triad.'), '1fr 1.15fr')}
{two(h3('Solid and broken') + '<p>Played together, a chord is <b>solid</b> (or blocked). Played one note at a time, it is <b>broken</b>. Spread up and down the keyboard, a broken chord becomes an <b>arpeggio</b>.</p><p class="sm">First met: Level 0; arpeggios from Level 1.</p>', px('h_sb', 80, 'The same three notes, solid then broken.'), '1fr 1.15fr')}
{inaction('Is it a triad?', px('h_is', 64), ['<b>Chord 1:</b> D F A, all in spaces, each a 3rd apart: <b>a triad</b>.', '<b>Chord 2:</b> D E A: D to E is a 2nd. <b>Not a triad.</b>', '<b>Chord 3:</b> D G C, stacked in 4ths. <b>Not a triad.</b>'], 'Only chord 1 is a triad. Check that each note is a <b>3rd</b> above the one below.')}
{youknow('The Blue Danube (Johann Strauss II), here in C', YKDAN, 'The most famous waltz tune simply climbs the <b class="co">C triad</b>: <b>C, C E G, G</b>. Root, 3rd, 5th, then it holds the top: that is why it sounds so open.', 'Play C E G one at a time, then hum the waltz over it.')}
{watch(['Stacking 2nds or 4ths: a triad skips exactly one letter each time.', 'Naming a chord from its top note: the root, at the bottom of the stack, names it.'])}
{foot('Counting intervals p. 32 · Major scales p. 36', 'Workbook Harmony 1 · Online: Library › Chords')}""", 64)


# ---------- Harmony 2 · Four kinds of triad ----------
def semi(i, t, y=30, col='#26296b'): return f'<text x="{i}" y="{y}" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" fill="{col}">{t}</text>'
KINDS = [['<b>major</b>', 'major (4)', 'minor (3)', 'C E G', 'C', 'Level ½'], ['<b>minor</b>', 'minor (3)', 'major (4)', 'C E♭ G', 'Cm', 'Level 2'], ['<b>diminished</b>', 'minor (3)', 'minor (3)', 'C E♭ G♭', 'C° or Cdim', 'Level 5'], ['<b>augmented</b>', 'major (4)', 'major (4)', 'C E G♯', 'C+ or Caug', 'Level 6']]
FLOORS = ('<svg viewBox="0 0 300 120" style="width:100%;max-width:190px;height:auto;display:block;margin:0 auto">'
          + ''.join(f'<rect x="{x}" y="{110 - a - b}" width="52" height="{b}" fill="#fff" stroke="#26296b" stroke-width="2"/><rect x="{x}" y="{110 - a}" width="52" height="{a}" fill="{c}" stroke="#26296b" stroke-width="2"/><text x="{x + 26}" y="{118 - a - b - 12}" text-anchor="middle" font-family="AH,Arial" font-size="10" font-weight="700" fill="#26296b">{n}</text>'
                    for x, a, b, c, n in ((6, 40, 30, 'rgba(228,87,46,.25)', 'major'), (80, 30, 40, 'rgba(228,87,46,.25)', 'minor'), (154, 30, 30, 'rgba(228,87,46,.25)', 'dim'), (228, 40, 40, 'rgba(228,87,46,.25)', 'aug')))
          + '</svg>')
YKMOON = ykfig('yk_moon', ('n1', 'n2', 'n3'), 68)
H2 = hpage(f"""{head('Part III · Harmony · 2', 'Four kinds of triad', 'Every triad is two 3rds stacked. A <b>major 3rd</b> is four semitones; a <b>minor 3rd</b> is three. Which 3rd sits at the bottom decides the kind of triad, and its sound.')}
{tbl(['Kind', 'Bottom 3rd', 'Top 3rd', 'On C', 'Chord name', 'First met'], KINDS, ['18%', '17%', '17%', '16%', '17%', '15%'])}
{px('h2_four', 96, 'The four kinds on C. Only the 3rd and the 5th move; the root stays.')}
{h3('Count the semitones')}
<div class="fk"><div class="fkf">{kbx('C', 8, W_, 100, label=True, shade={0: '#fde6dd', 2: '#fde6dd', 4: '#fde6dd'}, marks=[semi(W_ / 2, '0'), semi(W_, '1', 46, '#fff'), semi(W_ * 1.5, '2'), semi(W_ * 2, '3', 46, '#fff'), semi(W_ * 2.5, '4', 30, '#e4572e'), semi(W_ * 3.5, '5'), semi(W_ * 4, '6', 46, '#fff'), semi(W_ * 4.5, '7', 30, '#e4572e')], scale=1.0)}</div><div>From the root, count every key, black and white. C to E is <b class="co">4</b> semitones: a major 3rd, so C E G is <b>major</b>. E to G is 3 more; the root to the 5th is always <b class="co">7</b> in a major or minor triad.</div></div>
{inaction('Major or minor? D F A', kbx('C', 8, W_, 92, label=True, shade={1: '#fde6dd', 3: '#fde6dd', 5: '#fde6dd'}, marks=[dot(1, '1', y=62), dot(3, '3', y=62), dot(5, '5', y=62)], scale=1.0), ['<b>Root to 3rd:</b> D, D♯, E, F is <b>3</b> semitones: a minor 3rd.', '<b>3rd to 5th:</b> F, F♯, G, G♯, A is <b>4</b>: a major 3rd.', '<b>Minor below, major above:</b> a minor triad.'], 'D F A is <b>D minor</b> (Dm). Three of the white-key triads are minor: D, E and A.')}
{two(FLOORS, thinkt('Two floors of a building: a tall floor (a major 3rd, four steps) and a short one (a minor 3rd, three). Major: tall, then short. Minor: short, then tall. Diminished: two short. Augmented: two tall.'), '200px 1fr')}
<!--SPLIT-->
{h3('The seven white-key triads, sorted')}
{px('h2_white', 72, 'C, F and G are major; D, E and A are minor; B is diminished.')}
<p>On the white keys the pattern never changes: <b>three major</b> (C, F, G), <b>three minor</b> (D, E, A) and <b>one diminished</b> (B). There is no augmented triad on the white keys.</p>
{h3('How they sound')}
{tbl(['Kind', 'Sounds', 'Heard in'], [['major', 'bright, settled, open', 'most cheerful tunes, fanfares'], ['minor', 'darker, softer, sadder', 'lullabies, laments, film tension'], ['diminished', 'tense, unstable, wants to move', 'suspense, the chord before home'], ['augmented', 'floating, dreamy, unsettled', 'dream scenes, a passing colour']], ['22%', '38%', '40%'])}
{inaction('Change one note', px('h2_chg', 80), ['<b>Start with C major:</b> C E G.', '<b>Lower the 3rd</b> one semitone: E becomes E♭.', '<b>Keep the root and the 5th.</b>'], 'C E♭ G: <b>C minor</b>. One semitone turns major into minor.')}
{youknow('Beethoven, Moonlight Sonata (first movement)', YKMOON, 'The famous slow triplets are the notes of a <b class="co">C♯ minor triad</b>: C♯, E and G♯, rocking gently. Minor is why it sounds so quiet and sad.', 'Play C♯ E G♯ together, then C♯ F G♯ (major): hear the mood change.')}
{watch(['Counting letters instead of semitones: C–E and C–E♭ are both 3rds; only the semitones tell major from minor.', 'Forgetting that in diminished and augmented triads the 5th changes too.'])}
{foot('Chords and triads p. 64 · Major, minor and perfect p. 34', 'Workbook Harmony 2 · Online: Library › Chords')}""", 66)

_secs = []
for _old, _pg in ((64, H1), (66, H2)):
    _a, _b = _pg.split('<!--SPLIT-->', 1)
    _kick = _re.search(r'<div class="kick">(.*?)</div>', _a).group(1)
    _head_end = _a.index('<div class="body">') + len('<div class="body">')
    _foot = _pg[_pg.rindex('<div class="foot">'):]
    _secs.append((_a + '</div>' + _foot).replace('<section class="pg"', f'<section class="pg" data-flow="A{_old}"', 1))
    _secs.append((_a[:_head_end] + f'<div class="kick fk2">{_kick} · continued</div>' + _b).replace('<section class="pg"', f'<section class="pg" data-flow="B{_old}"', 1))
_secs = [_re.sub(r'<div class="foot"><span>\d+</span></div>', f'<div class="foot"><span>{64 + i}</span></div>', x) for i, x in enumerate(_secs)]
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{HOPEN}{"".join(_secs)}{_flowjs}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-harmony.html', 'w').write(html)
print('ok')
