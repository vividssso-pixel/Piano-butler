# The Piano Butler Handbook, Part III: Harmony (her 4 Nov: Harmony after Pitch and Time; the snowman for triads)
import re as _re
exec(open('/tmp/claude-0/pk/pitch.py').read())   # helpers, css, px / kbx / inaction / howto (rewrites the Pitch draft, harmless)
def hpage(inner, n): return page(inner, n, 'PART IV · HARMONY')
W_ = 34   # white-key width in the keyboard pictures
def dot(i, t='', col='#e4572e', y=73):   # her 5 Nov: key markers are outlined (white inside), so they never look like the filled step badges, and sit clear of the black keys
    if not t: return f'<circle cx="{i * W_ + W_ / 2}" cy="{y}" r="8" fill="{col}"/>'
    return f'<circle cx="{i * W_ + W_ / 2}" cy="{y}" r="8.5" fill="#fff" stroke="{col}" stroke-width="2"/><text x="{i * W_ + W_ / 2}" y="{y + 3.8}" text-anchor="middle" font-family="AH,Arial" font-size="10.5" font-weight="700" fill="{col}">{t}</text>'

YKDAN = '<figure class="vx"><div class="vs">' + P['yk_dan'].replace('<svg ', '<svg style="max-height:72px" ', 1) + '</div></figure>'   # (K. 545 and the Alberti bass wait for Harmony 6, in the bass clef: her 4 Nov)
for _n in ('n1', 'n2', 'n3', 'n4', 'n5'): YKDAN = YKDAN.replace(f'<g id="{_n}" class="note">', f'<g id="{_n}" class="note" style="fill:#e4572e;color:#e4572e">', 1)
# ---------- Part III opener ----------
HTOC = [(t, PM.PAGE[k]) for t, k in (('Chords and triads', 'H1'), ('Four kinds of triad', 'H2'), ('Chords in a key', 'H3'), ('Inversions', 'H4'), ('Seventh chords', 'H5'), ('Colour chords', 'H6'), ('The tower: 9, 11, 13', 'H7'), ('Slash chords', 'H8'), ('Chords from outside the key', 'H9'), ('Cadences', 'H10'), ('Chords under a melody', 'H11'), ('Progressions everywhere', 'H12'))] + [('Tips', PM.PAGE['H12'] + 2)]
hflow = ''.join(f'<div class="fl"><b>{a}</b><span>{b}</span></div>' + ('<span class="fa">›</span>' if i < 4 else '') for i, (a, b) in enumerate([('Triads', 'the house'), ('Sevenths', 'one more floor'), ('The tower', '9, 11, 13'), ('Slash chords', 'a new bass'), ('Progressions', 'chords that travel')]))
HOPEN = f"""<section class="pg part2"><div class="pframe"><div class="pk">Part IV · Which notes sound together</div><div class="pt">Harmony</div><div class="pdv"></div>
<p class="pl">A melody is the singer; harmony is the band behind it: the chords underneath. Start with the triad, a house of three notes, then build it higher floor by floor, and finish with the chords that close a phrase and carry a song.</p>
<div class="flow">{hflow}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{p}</span></div>' for x, p in HTOC)}</div></div></section>"""

BIGSNOW = ('<svg viewBox="0 0 260 300" style="width:100%;max-width:250px;height:auto;display:block;margin:0 auto">'
    '<circle cx="100" cy="232" r="56" fill="#fde6dd" stroke="#e4572e" stroke-width="3"/><circle cx="100" cy="134" r="42" fill="#fff" stroke="#26296b" stroke-width="3"/><circle cx="100" cy="60" r="31" fill="#fff" stroke="#26296b" stroke-width="3"/>'
    '<path d="M76,32 L124,32 L118,4 L82,4 Z" fill="#26296b"/><line x1="66" x2="134" y1="32" y2="32" stroke="#26296b" stroke-width="5" stroke-linecap="round"/>'
    '<text x="100" y="244" text-anchor="middle" font-family="PF,serif" font-size="36" font-weight="700" fill="#e4572e">C</text><text x="100" y="146" text-anchor="middle" font-family="PF,serif" font-size="32" font-weight="700" fill="#26296b">E</text><text x="100" y="70" text-anchor="middle" font-family="PF,serif" font-size="28" font-weight="700" fill="#26296b">G</text>'
    '<text x="170" y="238" font-family="AH,Arial" font-size="17" font-weight="700" fill="#e4572e">root</text><text x="156" y="140" font-family="AH,Arial" font-size="17" font-weight="700" fill="#26296b">3rd</text><text x="145" y="66" font-family="AH,Arial" font-size="17" font-weight="700" fill="#26296b">5th</text>'
    '<text x="196" y="186" font-family="AH,Arial" font-size="13" fill="#8d8fb3">skip D</text><text x="178" y="100" font-family="AH,Arial" font-size="13" fill="#8d8fb3">skip F</text></svg>')
# ---------- Harmony 1 · Chords and triads ----------
WHITE = [('C', 'E', 'G'), ('D', 'F', 'A'), ('E', 'G', 'B'), ('F', 'A', 'C'), ('G', 'B', 'D'), ('A', 'C', 'E'), ('B', 'D', 'F')]
SNOW = ('<svg viewBox="0 0 120 150" style="width:58px;height:auto;display:block;margin:0 auto">'
        '<circle cx="60" cy="118" r="28" fill="#fff" stroke="#26296b" stroke-width="2.5"/><circle cx="60" cy="70" r="21" fill="#fff" stroke="#26296b" stroke-width="2.5"/><circle cx="60" cy="33" r="15" fill="#fff" stroke="#26296b" stroke-width="2.5"/>'
        '<text x="60" y="123" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="#e4572e">C</text><text x="60" y="75" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="#26296b">E</text><text x="60" y="38" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="#26296b">G</text></svg>')
H1 = hpage(f"""{head('Part IV · Harmony · 1', 'Chords and triads', 'Press two or more notes at once and you have a <b>chord</b>. The favourite of all is the <b>triad</b>: three notes stacked like a snowman.')}
{two(BIGSNOW, '<div class="big3"><div><span>1</span><p>Pick a note: the <b class="co">root</b>, the big ball at the bottom. It holds the chord up and gives it its name.</p></div><div><span>2</span><p>Skip one letter, take the next: <b>E</b>, the <b>3rd</b>.</p></div><div><span>3</span><p>Skip again: <b>G</b>, the <b>5th</b>. C E G is the triad of C.</p></div></div>' + kbx('C', 8, W_, 100, label=True, shade={1: '#eef0f8', 3: '#eef0f8'}, marks=[dot(0, '1'), dot(2, '3'), dot(4, '5')], scale=1.0) + '<p class="sm" style="text-align:center;margin:4px 0 0">On the keys: play one, skip one (shaded), play one, skip one, play one.</p>', '0.9fr 1.1fr')}
{two(px('h_build', 104, 'The snowman on the staff: three lines in a row (or three spaces).'), '<p>On the staff, each ball sits on the <b>next line up</b> (or the next space up): the root, a <b>3rd</b> above it, a <b>5th</b> above the root.</p><p class="sm">First met: Level ½ (the tonic triad of C, G and F major).</p>', '1fr 1.15fr')}
{inaction('Build a triad on G', kbx('C', 10, W_, 92, label=True, shade={5: '#eef0f8', 7: '#eef0f8'}, marks=[dot(4, '1', y=67), dot(6, '3', y=67), dot(8, '5', y=67)], scale=1.0), ['<b>Start on G:</b> the root.', '<b>Skip A, play B:</b> the 3rd.', '<b>Skip C, play D:</b> the 5th.'], 'G B D: the triad of <b>G</b>. Same shape as C E G, just moved up.')}
<!--SPLIT-->
{two(h3('All lines or all spaces') + '<p>A stacked triad sits on <b>three lines in a row</b> or in <b>three spaces in a row</b>, in a neat stack. If one note breaks the pattern, it is not a triad.</p>', px('h_ls', 64, 'Lines, spaces, lines, spaces: every one a triad.'), '1fr 1.15fr')}
{two(h3('Solid and broken') + '<p>Played together, a chord is <b>solid</b> (or blocked). Played one note at a time, it is <b>broken</b>. Spread up and down the keyboard, a broken chord becomes an <b>arpeggio</b>. Left-hand accompaniments, the arpeggios in technical work and the chord names over a song are all triads.</p><p class="sm">First met: Level 0; arpeggios from Level 1.</p>', px('h_sb', 66, 'The same three notes, solid then broken.'), '1fr 1.15fr')}
{inaction('Is it a triad?', px('h_is', 58), ['<b>Chord 1:</b> D F A, all in spaces, each a 3rd apart: <b>a triad</b>.', '<b>Chord 2:</b> D E A: D to E is a 2nd. <b>Not a triad.</b>', '<b>Chord 3:</b> D G C, stacked in 4ths. <b>Not a triad.</b>'], 'Only chord 1 is a triad. Check that each note is a <b>3rd</b> above the one below.')}
{youknow('The Blue Danube (Johann Strauss II), here in C', YKDAN, 'The most famous waltz tune simply climbs the <b class="co">C triad</b>: <b>C, C E G, G</b>. Root, 3rd, 5th, then it holds the top: that is why it sounds so open.', 'Play C E G one at a time, then hum the waltz over it.')}
{thinkt('Solid: three friends shout “Hello!” together. Broken: each says it in turn.')}
{watch(['Stacking 2nds or 4ths: a triad skips exactly one letter each time.', 'Naming a chord from its top note: the root names it (at the bottom when the notes are stacked in 3rds).'])}
{foot('Counting intervals p. {{S1}} · Major scales p. {{S3}}', 'Workbook Harmony 1 · Online: Library › Chords')}""", 64)


# ---------- Harmony 2 · Four kinds of triad ----------
def semi(i, t, y=30, col='#26296b'): return f'<text x="{i}" y="{y}" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" fill="{col}">{t}</text>'
KINDS = [['<b>major</b>', '<b class="co">3 + 2</b>', 'C E G', 'C', 'Level ½'], ['<b>minor</b>', '<b class="co">2 + 3</b>', 'C E♭ G', 'Cm', 'Level 2'], ['<b>diminished</b>', '<b class="co">2 + 2</b>', 'C E♭ G♭', 'C° or Cdim', 'Level 5'], ['<b>augmented</b>', '<b class="co">3 + 3</b>', 'C E G♯', 'C+ or Caug', 'Level 6']]   # her 5 Nov: count the keys in between (3 + 2 = major)
FLOORS = ('<svg viewBox="0 0 300 120" style="width:100%;max-width:150px;height:auto;display:block;margin:0 auto">'
          + ''.join(f'<rect x="{x}" y="{110 - a - b}" width="52" height="{b}" fill="#fff" stroke="#26296b" stroke-width="2"/><rect x="{x}" y="{110 - a}" width="52" height="{a}" fill="{c}" stroke="#26296b" stroke-width="2"/><text x="{x + 26}" y="{110 - a - b - 6}" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="#26296b">{n}</text>'
                    for x, a, b, c, n in ((6, 40, 30, 'rgba(228,87,46,.25)', 'major'), (80, 30, 40, 'rgba(228,87,46,.25)', 'minor'), (154, 30, 30, 'rgba(228,87,46,.25)', 'dim'), (228, 40, 40, 'rgba(228,87,46,.25)', 'aug')))
          + '</svg>')
YKMOON = ykfig('yk_moon', ('n1', 'n2', 'n3'), 84)
H2 = hpage(f"""{head('Part IV · Harmony · 2', 'Four kinds of triad', 'Every triad is two 3rds stacked. To tell the kinds apart, count the keys <b>in between</b>, black and white, that you do not play: root to 3rd, then 3rd to 5th. Those two numbers name the kind, and its sound.')}
{tbl(['Kind', 'Keys between', 'On C', 'Chord name', 'First met'], KINDS, ['20%', '22%', '20%', '20%', '18%'])}
<p class="sm">Chord names: a letter alone means major (C); m means minor (Cm). You see them above the melody in songbooks and lead sheets: C | Am | F | G. In interval names, 3 keys between is a major 3rd and 2 is a minor 3rd (p. {{S2}}).</p>
{px('h2_four', 96, 'The four kinds on C. Only the 3rd and the 5th move; the root stays.')}
{h3('Count the keys in between')}
<div class="fk"><div class="fkf">{kbx('C', 8, W_, 100, label=True, shade={1: '#eef0f8', 3: '#eef0f8'}, marks=[dot(0, '1'), semi(W_, '1', 46, '#fff'), semi(W_ * 1.5, '2'), semi(W_ * 2, '3', 46, '#fff'), dot(2, '3'), semi(W_ * 3.5, '1'), semi(W_ * 4, '2', 46, '#fff'), dot(4, '5')], scale=1.0)}</div><div>Play C and E and count the keys you skip, black and white: C♯, D, D♯ is <b class="co">3</b>. Then E to G: F, F♯ is <b class="co">2</b>. <b>3 + 2 is major.</b> Any root works the same way: from D, skip 3 to F♯, then 2 to A: D F♯ A, D major.</div></div>
{inaction('Major or minor? D F A', kbx('C', 8, W_, 92, label=True, shade={1: '#fde6dd', 3: '#fde6dd', 5: '#fde6dd'}, marks=[dot(1, '1', y=67), dot(3, '3', y=67), dot(5, '5', y=67)], scale=1.0), ['<b>Root to 3rd:</b> D to F skips D♯ and E: <b>2</b>.', '<b>3rd to 5th:</b> F to A skips F♯, G and G♯: <b>3</b>.', '<b>2 + 3</b> is minor.'], 'D F A is <b>D minor</b> (Dm). Three of the white-key triads are minor: D, E and A.')}
{thinkt('Two floors of a building: a tall floor (3 keys between) and a short one (2). Major: tall, then short, 3 + 2. Minor: short, then tall, 2 + 3. Diminished: two short, 2 + 2. Augmented: two tall, 3 + 3.')}
<!--SPLIT-->
{h3('The seven white-key triads, sorted')}
{px('h2_white', 60, 'Always the same on the white keys: <b>three major</b> (C, F, G), <b>three minor</b> (D, E, A), <b>one diminished</b> (B), no augmented. In any major key, chords I, IV and V are the major ones (p. {{H3}}).')}
{h3('How they sound')}
{tbl(['Kind', 'Sounds', 'Heard in'], [['major', 'bright, settled, open', 'most cheerful tunes, fanfares'], ['minor', 'darker, softer, sadder', 'lullabies, laments, film tension'], ['diminished', 'tense, unstable, wants to move', 'suspense, the chord before home'], ['augmented', 'floating, dreamy, unsettled', 'dream scenes, a passing colour']], ['22%', '38%', '40%'])}
{youknow('Beethoven, Moonlight Sonata (first movement)', YKMOON, 'The famous slow triplets are the notes of a <b class="co">C♯ minor triad</b>: C♯, E and G♯, rocking gently. Minor is why it sounds so dark and sad.', '', True)}
{watch(['Counting the keys you play: count only the keys in between, black and white.', 'Forgetting that in diminished and augmented triads the 5th changes too.', 'Spelling with the wrong letter: a triad skips one letter, so C minor is C E♭ G, never C D♯ G.'])}
{foot('Chords and triads p. {{H1}} · Major, minor and perfect p. {{S2}}', 'Workbook Harmony 2 · Online: Library › Chords')}""", 66)

# ---------- Harmony 3 · Chords in a key ----------
DEG = [['<b>I</b>', 'tonic', 'major', 'C', 'G'], ['ii', 'supertonic', 'minor', 'Dm', 'Am'], ['iii', 'mediant', 'minor', 'Em', 'Bm'], ['<b>IV</b>', 'subdominant', 'major', 'F', 'C'], ['<b>V</b>', 'dominant', 'major', 'G', 'D'], ['vi', 'submediant', 'minor', 'Am', 'Em'], ['vii°', 'leading note', 'diminished', 'B°', 'F♯°']]
BLUES = '<div class="blues">' + ''.join(f'<span class="{"b1" if c == "C" else "b4" if c == "F" else "b5"}"><i>{n}</i>{c}</span>' for n, c in zip(['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'IV', 'I', 'V'], ['C', 'C', 'C', 'C', 'F', 'F', 'C', 'C', 'G', 'F', 'C', 'G'])) + '</div>'
H3 = hpage(f"""{head('Part IV · Harmony · 3', 'Chords in a key', 'Build a triad on every note of a scale and you have the chords of that key. <b>Roman numerals</b> name each one by its place in the scale: I on the 1st note, IV on the 4th, V on the 5th. Capitals are major, small numerals are minor, and small with ° is diminished.')}
{px('h3_cmaj', 92, 'The seven chords of C major. Only white keys, so the kinds come out as on p. {{H2+1}}.')}
{tbl(['Numeral', 'Name', 'Kind', 'Keys between', 'In C', 'In G'], [[a, b, c, {'major': '3 + 2', 'minor': '2 + 3', 'diminished': '2 + 2'}[c], d, e] for a, b, c, d, e in DEG], ['13%', '21%', '18%', '18%', '15%', '15%'])}
<p class="sm">The same in every major key: I, IV and V are major; ii, iii and vi are minor; vii° is diminished. First met: I, IV and V at Levels 1–2; the other chords from about Level 4.</p>
{two(h3('The three primary chords') + '<p><b class="co">I, IV and V</b> are the strongest chords of a key. Between them they hold <b>every note of the scale</b>: C E G, F A C, G B D. That is why so many tunes need only these three.</p>', thinkt('I is home. IV is a visit next door. V is the walk back, already looking at the front door: it wants to go home to I. Play C, F, G, C and hear it.'), '1.2fr 1fr')}
{inaction('Find I, IV and V in G major', px('h3_g', 84), ['<b>Count up the scale:</b> G A B C D. The 1st note is G, the 4th C, the 5th D.', '<b>Build a triad on each</b>, using the key signature: the F is F♯.', '<b>Check with the keys between:</b> all three are 3 + 2, major.'], 'In G major: <b>I = G</b>, <b>IV = C</b>, <b>V = D</b> (D F♯ A).')}
<!--SPLIT-->
{two(h3('In a minor key') + '<p>In A minor the three main chords are <b>i</b> (A minor), <b>iv</b> (D minor) and <b>V</b>: E G♯ B, made major by the <b class="co">raised 7th</b>, G♯, which pulls up to the home note A. Check: E G♯ B is 3 + 2, major.</p>', px('h3_min', 88, 'A minor: i, iv and V. The G♯ makes V major.'), '1fr 1.1fr')}
{h3('Which chord holds the note?')}
{tbl(['Note in C', 'C', 'D', 'E', 'F', 'G', 'A', 'B'], [['<b>Chord</b>', 'I or IV', 'V', 'I', 'IV', 'I or V', 'IV', 'V']], ['16%'] + ['12%'] * 7)}
<p class="sm">The same idea works in every key: find which of I, IV and V holds the note.</p>
{inaction('Choose a chord for each bar: Twinkle', px('h3_twk', 80), ['<b>Look at the notes</b> in each bar (or half bar).', '<b>Find I, IV or V</b> that holds them, from the table above.', '<b>End V then I</b> (a perfect cadence, p. {{H5}}): the tune comes home.'], 'Twinkle needs only <b>I, IV and V</b>: C, F and G.')}
{youknow('The twelve-bar blues', BLUES, 'Almost every blues, and a lot of rock ’n’ roll, is just <b class="co">I, IV and V</b> in twelve bars. Learn this chart and you can play along with hundreds of songs.', 'Play the chart in C with your left hand, one chord per bar, four beats each.')}
{watch(['Writing every numeral big: ii, iii and vi are minor, so they are written small.', 'Forgetting the raised 7th in a minor key: V in A minor is E G♯ B, not E G B.'])}
{foot('Four kinds of triad p. {{H2}} · Major scales p. {{S3}} · Cadences p. {{H10}}', 'Workbook Harmony 3 · Online: Library › Chords')}""", 68)
css += """
.snowc{margin:0;font-size:15px;line-height:1.5}
.blues{display:grid;grid-template-columns:repeat(4,1fr);gap:5px;width:100%;max-width:330px;margin:0 auto} .blues span{border:1.5px solid #26296b;border-radius:4px;padding:4px 0 5px;text-align:center;font-weight:700;font-size:15px;line-height:1.1;background:#fff} .blues i{display:block;font-style:normal;font-size:10.5px;color:#6d6f9c;letter-spacing:.06em} .blues .b4{background:#fdeee8} .blues .b5{background:#e4572e;color:#fff;border-color:#e4572e} .blues .b5 i{color:#ffe1d6}
"""

# ---------- Harmony 4 · Inversions ----------
def pxr(k, ids, h, cap=''):   # a staff picture with chosen notes in red, and a caption
    f = ykfig(k, ids, h)
    return f.replace('</div></figure>', '</div>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>')
INV = [['root position', 'the root (C)', 'C', 'I', '5/3', 'Level ½'], ['1st inversion', 'the 3rd (E)', 'C/E', 'Ib', '6/3 (6)', 'Level 3'], ['2nd inversion', 'the 5th (G)', 'C/G', 'Ic', '6/4', 'Level 5']]
H4 = hpage(f"""{head('Part IV · Harmony · 4', 'Inversions', 'Shuffle a chord’s three notes and it is still the same chord. Root at the bottom: <b>root position</b>. Lift the root to the top and a new note takes the bottom: an <b>inversion</b>. Same name, new bass note.')}
{pxr('h4_inv', ('n2', 'n7', 'n9'), 100, 'The red note is the root, C. Watch it climb: at the bottom, then on top, then in the middle. The chord is always C major.')}
{tbl(['Position', 'Bass note', 'Chord symbol', 'Numeral', 'Figures', 'First met'], INV, ['21%', '18%', '17%', '13%', '15%', '16%'])}
<p class="sm">Only the lowest note decides: E C G, or E G C E, is still a 1st inversion. Chord symbols write the bass after a slash: C/E is a C chord with E in the bass (more uses in Slash chords, p. {{H8}}). Figures count the intervals above the bass, by letters: in E G C, G is a 3rd and C a 6th above E, so 6/3.</p>
{h3('Roll the bottom note to the top')}
<div class="fk"><div class="fkf">{kbx('C', 10, W_, 100, label=True, shade={0: '#eef0f8'}, marks=[f'<circle cx="{W_ / 2}" cy="74" r="11" fill="none" stroke="#e4572e" stroke-width="2" stroke-dasharray="3 2"/>', f'<path d="M{W_ / 2},60 C{W_ * 2},2 {W_ * 6},2 {W_ * 7.4},58" fill="none" stroke="#e4572e" stroke-width="2.5"/><path d="M{W_ * 7.4 - 7},52 L{W_ * 7.4 + 1},61 L{W_ * 7.4 + 4},50" fill="none" stroke="#e4572e" stroke-width="2.5"/>', dot(2, 'E', col='#26296b'), dot(4, 'G', col='#26296b'), dot(7, 'C')], scale=1.0)}</div><div>Play C E G, then lift the <b class="co">root C</b> and put it on top (the red arrow): <b>E G C</b>. The E is now the bass: the 1st inversion. Do it again (G C E) for the 2nd inversion. In an inversion the stack has a <b>gap of a 4th</b> (G up to C): the note above the gap is the root.</div></div>
{inaction('Name this chord: E G C', pxr('h4_name', ('n2', 'n5'), 84), ['<b>Restack it in 3rds</b>, like the snowman: C E G.', '<b>The bottom of the stack is the root:</b> C, so it is C major.', '<b>Which note is in the bass?</b> E, the 3rd: 1st inversion.'], 'E G C is <b>C major, 1st inversion</b>: C/E.')}
{thinkt('The same three friends in a photo, swapping places: still the same group (the same chord), but whoever stands at the front (the bass) changes the picture.')}
<!--SPLIT-->
{h3('Why inversions?')}
<p>They let your hand <b>move as little as possible</b>: keep any note two chords share, and move the others to the nearest note of the next chord. Left-hand accompaniments and hymn parts are written this way.</p>
{inaction('Play I, IV, V, I smoothly', px('h4_smooth', 96), ['<b>I:</b> C E G. <b>IV:</b> keep C, move E up to F and G up to A: C F A.', '<b>V:</b> no shared note, so each moves to the nearest: C to B, F to D, A to G: B D G.', '<b>I again:</b> back to C E G. Each finger moved one or two keys.'], 'IV is F/C and V is G/B: <b>inversions</b> keep the hand in one place.')}
{youknow('Pachelbel’s Canon, the bass (here in C)', ykfig('yk_canon', ('n2', 'n4', 'n6'), 84), 'The famous bass walks <b>straight down the scale</b>: C B A G F E. It can, because some chords are <b class="co">inversions</b>: G/B, Em/G and C/E put a different note in the bass.', 'Play the bass slowly and hum the famous violin tune over it.')}
{h3('Chords of C, every position')}
{tbl(['Chord', 'Root position', '1st inversion', '2nd inversion'], [['<b>I</b> (C)', 'C E G', 'E G C', 'G C E'], ['<b>IV</b> (F)', 'F A C', 'A C F', 'C F A'], ['<b>V</b> (G)', 'G B D', 'B D G', 'D G B'], ['<b>vi</b> (Am)', 'A C E', 'C E A', 'E A C']], ['16%', '28%', '28%', '28%'])}
{watch(['Naming a chord from its bass note: in an inversion the bass is not the root. Restack it in 3rds first.', 'Thinking an inversion is a new chord: E G C is still C major.'])}
{foot('Chords and triads p. {{H1}} · Chords in a key p. {{H3}} · Cadences p. {{H10}}', 'Workbook Harmony 4 · Online: Library › Chords')}""", 70)

# ---------- Harmony 5 · Seventh chords (picture-first, her 5 Nov) ----------
N, R, PINK, SOFT = '#26296b', '#e4572e', '#fde6dd', '#f6f5fa'

def building(notes, labels, top_new=1, w=150, h=46):
    n = len(notes); H = n * h + 70
    o = f'<svg viewBox="0 0 {w + 150} {H}" style="width:100%;max-width:{w + 150}px;height:auto;display:block;margin:0 auto">'
    o += f'<path d="M6,{H - n * h - 30} L{w / 2 + 6},{H - n * h - 62} L{w + 6},{H - n * h - 30}" fill="none" stroke="{N}" stroke-width="2.5"/>'
    for i, (nt, lb) in enumerate(zip(notes, labels)):
        y = H - 30 - (i + 1) * h; new = i >= n - top_new
        o += f'<rect x="10" y="{y}" width="{w - 8}" height="{h - 4}" rx="4" fill="{"#fbd2c2" if new else PINK}" stroke="{R if new else N}" stroke-width="{2.5 if new else 2}"/>'
        o += f'<text x="30" y="{y + 22}" font-family="AH,Arial" font-size="19" font-weight="700" fill="{R if i == 0 or new else N}">{nt}</text><text x="62" y="{y + 21}" font-family="AH,Arial" font-size="13" fill="{N}">{lb}</text>'
    yb = H - 30 - (n - top_new) * h + 2
    o += f'<path d="M{w + 12},{H - 32} L{w + 20},{H - 32} L{w + 20},{yb} L{w + 12},{yb}" fill="none" stroke="{N}" stroke-width="2"/><text x="{w + 28}" y="{(H - 32 + yb) / 2 + 5}" font-family="AH,Arial" font-size="13" font-weight="700" fill="{N}">triad</text>'
    o += f'<path d="M{w + 12},{yb - 4} L{w + 20},{yb - 4} L{w + 20},{yb - h + 6} L{w + 12},{yb - h + 6}" fill="none" stroke="{R}" stroke-width="2"/><text x="{w + 28}" y="{yb - h / 2 + 3}" font-family="AH,Arial" font-size="13" font-weight="700" fill="{R}">+ one floor</text>'
    o += f'<line x1="0" x2="{w + 20}" y1="{H - 28}" y2="{H - 28}" stroke="{N}" stroke-width="3"/>'
    return o + '</svg>'

def minikb(keys, nums, W=22, H=90):   # 8 white keys from C; keys = list of (pos, name) where pos counts semitones from C; nums = keys-between labels
    wpos = [0, 2, 4, 5, 7, 9, 11, 12, 14]
    fs = max(13, W * 0.62)   # the count above the keys; the viewBox grows with it so it is never cut off
    o = f'<svg viewBox="-2 {-(fs + 8):.0f} {8 * W + 4} {H + fs + 12:.0f}" style="width:100%;max-width:{8 * W + 4}px;height:auto;display:block;margin:0 auto">'
    for i in range(8): o += f'<rect x="{i * W}" y="0" width="{W}" height="{H}" fill="#fff" stroke="{N}" stroke-width="1.2"/>'
    for i in (0, 1, 3, 4, 5):
        o += f'<rect x="{(i + 1) * W - W * 0.3}" y="0" width="{W * 0.6}" height="{H * 0.6}" fill="{N}"/>'
    for j, (p, nm) in enumerate(keys):
        if p in wpos: x, y = wpos.index(p) * W + W / 2, H - 13
        else: x, y = (wpos.index(p - 1) + 1) * W, H * 0.6 - 10
        o += f'<circle cx="{x}" cy="{y}" r="7.5" fill="{R if j == len(keys) - 1 else N}" stroke="#fff" stroke-width="1.5"/>'   # the 7th red, the triad navy
    o += f'<text x="{4 * W}" y="-4" text-anchor="middle" font-family="AH,Arial" font-size="{max(13, W * 0.62):.0f}" font-weight="700" fill="{R}">{nums}</text>'
    return o + '</svg>'

KINDS7 = [('Cmaj7', 'C E G B', [(0, 'C'), (4, 'E'), (7, 'G'), (11, 'B')], '3 + 2 + 3', 'dreamy', 'bossa nova, film'),
          ('C7', 'C E G B♭', [(0, 'C'), (4, 'E'), (7, 'G'), (10, 'B♭')], '3 + 2 + 2', 'bluesy', 'the blues'),
          ('Cm7', 'C E♭ G B♭', [(0, 'C'), (3, 'E♭'), (7, 'G'), (10, 'B♭')], '2 + 3 + 2', 'mellow', 'soul, jazz ballads'),
          ('Cø7', 'C E♭ G♭ B♭', [(0, 'C'), (3, 'E♭'), (6, 'G♭'), (10, 'B♭')], '2 + 2 + 3', 'searching', 'Bø7 is ii in A minor'),
          ('C°7', 'C E♭ G♭ B𝄫 (= A)', [(0, 'C'), (3, 'E♭'), (6, 'G♭'), (9, 'B𝄫')], '2 + 2 + 2', 'spooky', 'old film villains')]
CARDS = '<div class="k7">' + ''.join(f'<div class="kc"><b class="ks">{s}</b>{minikb(k, f)}<span class="kn">{n}</span><span class="km">{m}</span><span class="kw">{w}</span></div>' for s, n, k, f, m, w in KINDS7) + '</div>'

H5A = hpage(f"""{head('Part IV · Harmony · 5', 'Seventh chords', 'Add one more floor to a triad and the chord changes colour: dreamy, bluesy, spooky. Same rule as before: skip one note, stack the next. The new note is the <b class="co">7th</b>.')}
{two(building(['C', 'E', 'G', 'B'], ['root', '3rd', '5th', '7th']), '<div class="big3"><div><span>1</span><p>Build the triad: <b>C E G</b>.</p></div><div><span>2</span><p>Skip one, add the next: <b class="co">B</b>.</p></div><div><span>3</span><p>Count the keys between: <b>3 + 2 + 3</b>. That is <b>Cmaj7</b>.</p></div></div>' + minikb([(0, 'C'), (4, 'E'), (7, 'G'), (11, 'B')], '3 + 2 + 3', 34, 110), '1fr 1.1fr')}
{h3('Five flavours, all on C')}
{CARDS}
<p class="sm">How the names work: major triad + major 7th = <b>maj7</b> · major triad + minor 7th = <b>7</b> · minor triad + minor 7th = <b>m7</b> · diminished triad + minor 7th = <b>ø7</b> · diminished triad + diminished 7th = <b>°7</b>. Also written: CM7 or CΔ = Cmaj7, C–7 = Cm7, Cm7♭5 = Cø7, Cdim7 = C°7.</p>
{h3('A seventh on every floor of C major')}
{px('h7_key', 84, 'Only white keys. G7 is the one with the strongest pull home.')}""", 72)

H5B = hpage(f"""<div class="kick">Part IV · Harmony · 5 · continued</div>
{inaction('Which seventh is it? G B D F', px('h7_mys', 84), ['<b>Count the keys between:</b> G to B is 3, B to D is 2, D to F is 2.', '<b>3 + 2 + 2</b> is the bluesy one.', '<b>The root is G:</b> G7.'], 'G B D F is <b>G7</b>, the chord that pulls hardest back to C.')}
{h3('Spot the difference')}
{pxr('h7_diff', ('n8', 'n12'), 96, 'One note decides: B makes Cmaj7, B♭ makes C7. Everything below stays the same.')}
{youknow('The blues, with sevenths', BLUES.replace('>C<', '>C7<').replace('>F<', '>F7<').replace('>G<', '>G7<'), 'Swap the triads for <b class="co">7th chords</b> and the twelve-bar chart (p. {{H3+1}}) turns into the real blues: the 7th is the blue note.', 'Play the chart with plain C, F and G first (p. {{H3+1}}), then add the red 7ths: B♭, E♭ and F.')}
{two(pxr('h7_pull', ('n3', 'n5', 'n7', 'n8'), 86), '<p><b>Why G7 pulls home:</b> its B wants to rise to <b class="co">C</b> and its F wants to fall to <b class="co">E</b>. Two small steps, and you are home in C.</p>', '1.2fr 1fr')}
{thinkt('A triad is plain toast. The 7th is the topping: the same bread, but now it tastes of something.')}
{watch(['Writing C7 when you mean Cmaj7: “7” alone means the bluesy one, with B♭.', 'Stacking the 7th from the wrong note: count a 7th up from the root, not from the 5th.'])}
{foot('Four kinds of triad p. {{H2}} · Chords in a key p. {{H3}}', 'Workbook Harmony 5 · Online: Library › Chords')}""", 73)

# ---------- Harmony 6 · Colour chords (picture-first, her 5 Nov: most chord types, fun, visual) ----------
def minikb2(keys, red=(), ghost=(), nums='', W=20, H=78, nw=9):   # nw white keys from C; keys: semitone positions; red: the changed notes; ghost: where a note used to be (dashed)
    wpos = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17]
    o = f'<svg viewBox="-2 -22 {nw * W + 4} {H + 26}" style="width:100%;max-width:{nw * W + 4}px;height:auto;display:block;margin:0 auto">'
    for i in range(nw): o += f'<rect x="{i * W}" y="0" width="{W}" height="{H}" fill="#fff" stroke="{N}" stroke-width="1.2"/>'
    for i in range(nw - 1):
        if i % 7 in (0, 1, 3, 4, 5): o += f'<rect x="{(i + 1) * W - W * 0.3}" y="0" width="{W * 0.6}" height="{H * 0.6}" fill="{N}"/>'
    def xy(p): return (wpos.index(p) * W + W / 2, H - 13) if p in wpos else ((wpos.index(p - 1) + 1) * W, H * 0.6 - 10)
    for p in ghost:
        x, y = xy(p); o += f'<circle cx="{x}" cy="{y}" r="7.5" fill="none" stroke="{N}" stroke-width="1.8" stroke-dasharray="2.5 2"/>'
    for p in keys:
        x, y = xy(p); o += f'<circle cx="{x}" cy="{y}" r="7" fill="{R if p in red else N}" stroke="#fff" stroke-width="1.5"/>'
    o += f'<text x="{nw * W / 2}" y="-3" text-anchor="middle" font-family="AH,Arial" font-size="19" font-weight="700" fill="{R}">{nums}</text>'
    return o + '</svg>'
COL = [('Csus2', 'C D G', [0, 2, 7], [2], [4], '1 + 4', 'open', 'the 3rd steps down'),
       ('Csus4', 'C F G', [0, 5, 7], [5], [4], '4 + 1', 'floating', 'the 3rd steps up'),
       ('C5', 'C G', [0, 7], [], [4], '6', 'strong', 'no 3rd at all'),
       ('C6', 'C E G A', [0, 4, 7, 9], [9], [], '3 + 2 + 1', 'warm', 'add the 6th'),
       ('Cadd9', 'C E G D', [0, 4, 7, 14], [14], [], '3 + 2 + 6', 'sparkly', 'add the 9th on top')]
CCARDS = '<div class="k7">' + ''.join(f'<div class="kc"><b class="ks">{s}</b>{minikb2(k, r, g, f)}<span class="kn">{n}</span><span class="km">{m}</span><span class="kw">{w}</span></div>' for s, n, k, r, g, f, m, w in COL) + '</div>'
def _hero6():   # her 5 Nov: big, clear keys; markers outlined and clear of the black keys; the hop drawn as a red arc
    KW, KH, y = 40, 124, 100
    cx = lambda i: i * KW + KW / 2
    def mk(i, t, col, dash=False):
        st = ' stroke-dasharray="4 3"' if dash else ''
        return f'<circle cx="{cx(i)}" cy="{y}" r="11" fill="#fff" stroke="{col}" stroke-width="2.2"{st}/><text x="{cx(i)}" y="{y + 4.6}" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="{col}">{t}</text>'
    def arc(a, b):
        x1, x2 = cx(a) + (8 if b > a else -8), cx(b) + (-9 if b > a else 9); d = 1 if b > a else -1
        return (f'<path d="M{x1},{y - 9} Q{(x1 + x2) / 2},{y - 36} {x2},{y - 11}" fill="none" stroke="{R}" stroke-width="2.4"/>'
                f'<path d="M{x2 - d * 8},{y - 15} L{x2},{y - 11} L{x2 - d * 1},{y - 20}" fill="none" stroke="{R}" stroke-width="2.4" stroke-linejoin="round"/>')
    return kbx('C', 7, KW, KH, shade={1: '#fde6dd', 3: '#fde6dd'}, marks=[mk(0, 'C', N), mk(2, 'E', N, True), mk(4, 'G', N), mk(1, 'D', R), mk(3, 'F', R), arc(2, 1), arc(2, 3),
        f'<text x="{cx(1)}" y="{KH - 4}" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="{R}">sus2</text><text x="{cx(3)}" y="{KH - 4}" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="{R}">sus4</text>'], scale=1.0)
HERO6 = _hero6()
ANY = [['<b>sus2</b>', '1 + 4', 'C D G', 'G A D', 'F G C', 'D E A'], ['<b>sus4</b>', '4 + 1', 'C F G', 'G C D', 'F B♭ C', 'D G A'], ['<b>5</b>', '6', 'C G', 'G D', 'F C', 'D A'],
       ['<b>6</b>', '3 + 2 + 1', 'C E G <b class="co">A</b>', 'G B D <b class="co">E</b>', 'F A C <b class="co">D</b>', 'D F♯ A <b class="co">B</b>'], ['<b>add9</b>', '3 + 2 + 6', 'C E G <b class="co">D</b>', 'G B D <b class="co">A</b>', 'F A C <b class="co">G</b>', 'D F♯ A <b class="co">E</b>']]
H6A = hpage(f"""{head('Part IV · Harmony · 6', 'Colour chords', 'The 3rd is the chord’s mood: major or minor, happy or sad. Slide it aside, take it away, or add one note, and a plain chord takes on a new colour. Five colours, all from C&nbsp;E&nbsp;G.')}
{two(HERO6, '<div class="big3"><div><span>1</span><p>Start from <b>C E G</b>. The <b>E</b> (the 3rd) makes it major.</p></div><div><span>2</span><p>Slide the E up to the next letter, <b class="co">F</b>: <b>Csus4</b>.</p></div><div><span>3</span><p>Or down to the letter below, <b class="co">D</b>: <b>Csus2</b>. With no 3rd, the chord is neither major nor minor: it <b>hangs in the air</b>.</p></div></div>', '1.15fr 1fr')}
{h3('Five colours, all on C')}
{CCARDS}
<p class="sm"><b>sus</b> = suspended: the 3rd is held up or down · <b>5</b> = root and 5th only · <b>6</b> = add the 6th (on C: A) · <b>add9</b> = add the 9th, the 2nd an octave up (on C: D). Csus means Csus4. Red dot: the new note; dashed ring: where the 3rd was.</p>
{h3('Sus wants to come home')}
{pxr('h6_shimmer', ('n6', 'n12'), 86, 'The red note leans, then slides back to E: F steps down, D steps up. Play it slowly: C, Csus4, C, Csus2, C. Guitarists love this shimmer.')}
{h3('On any root, the counts stay the same')}
{tbl(['Colour', 'Keys between', 'On C', 'On G', 'On F', 'On D'], ANY, ['13%', '17%', '17.5%', '17.5%', '17.5%', '17.5%'])}""", 76)
H6B = hpage(f"""<div class="kick">Part IV · Harmony · 6 · continued</div>
{inaction('Which colour is it? G C D', pxr('h6_mys', (), 100), ['<b>Count the keys between:</b> G to C is 4, C to D is 1.', '<b>4 + 1</b> is the sus4 card: no B (no 3rd), and C has taken its place.', '<b>The root is G:</b> Gsus4.'], 'G C D is <b>Gsus4</b>. Let the C fall to <b class="co">B</b> and you have G major.')}
{h3('Spot the difference')}
{pxr('h6_diff', ('n3', 'n8'), 96, 'The same red D, two jobs. Csus2 throws the E out; Cadd9 keeps the E and puts the D on top.')}
{two(pxr('h6_power', (), 96), '<p><b>The power chord:</b> just the root and the 5th, played low in the left hand. With no 3rd it is neither happy nor sad, only <b class="co">strong</b>: the sound of rock guitar. Play C5, F5, G5, C5 and drum the rhythm.</p>', '1.1fr 1fr')}
{two(pxr('h6_twins', ('n1', 'n6'), 100), '<p><b>C6 or Am7?</b> The same four notes, C E G A. The red bottom note decides: C at the bottom is <b>C6</b>; A at the bottom is <b>Am7</b>. More on the bass note in Slash chords, p. {{H8}}.</p>', '1fr 1.1fr')}
{thinkt('Dressing the snowman: a scarf (the 6th) or a hat (the 9th) and it is still the same snowman. Sus moves its middle ball; a power chord takes the middle ball away.')}
{watch(['Writing C2: some books mean Csus2, others Cadd9. Check whether the E is there.', 'Calling Cadd9 a ninth chord: C9 also has the 7th (B♭). Add9 is just the triad plus the 9th (D on C), nothing else (The tower, p. {{H7}}).'])}
{foot('Four kinds of triad p. {{H2}} · Seventh chords p. {{H5}}', 'Workbook Harmony 6 · Online: Library › Chords')}""", 77)

# ---------- Harmony 7 · The tower: 9, 11, 13 (picture-first, her 5 Nov: 'triad on the scale's land, sevenths a floor up, and beyond?') ----------
def tower(w=150, h=34):
    fl = [('C', 'root', 0), ('E', '3rd', 0), ('G', '5th', 0), ('B♭', '7th', 1), ('D', '9th', 2), ('F', '11th', 2), ('A', '13th', 2)]
    n = len(fl); H = n * h + 60
    o = f'<svg viewBox="0 0 {w + 170} {H}" style="width:100%;max-width:{w + 170}px;height:auto;display:block;margin:0 auto">'
    o += f'<path d="M6,{H - n * h - 30} L{w / 2 + 6},{H - n * h - 54} L{w + 6},{H - n * h - 30}" fill="none" stroke="{N}" stroke-width="2.5"/>'
    for i, (nt, lb, k) in enumerate(fl):
        y = H - 30 - (i + 1) * h
        fill, st = (PINK, N) if k == 0 else (('#f1effa', N) if k == 1 else ('#fbd2c2', R))
        o += f'<rect x="10" y="{y}" width="{w - 8}" height="{h - 4}" rx="4" fill="{fill}" stroke="{st}" stroke-width="{2.4 if k == 2 else 2}"/>'
        o += f'<text x="28" y="{y + 20}" font-family="AH,Arial" font-size="17" font-weight="700" fill="{R if k == 2 else N}">{nt}</text><text x="66" y="{y + 19}" font-family="AH,Arial" font-size="13" fill="{N}">{lb}</text>'
    def br(a, b, t, col):
        y1, y2 = H - 30 - a * h - 3, H - 30 - (b + 1) * h + 1
        return f'<path d="M{w + 12},{y1} L{w + 20},{y1} L{w + 20},{y2} L{w + 12},{y2}" fill="none" stroke="{col}" stroke-width="2"/><text x="{w + 28}" y="{(y1 + y2) / 2 + 5}" font-family="AH,Arial" font-size="13" font-weight="700" fill="{col}">{t}</text>'
    o += br(0, 2, 'triad', N) + br(3, 3, '+ 7th', N) + br(4, 6, 'top floors', R)
    o += f'<line x1="0" x2="{w + 20}" y1="{H - 28}" y2="{H - 28}" stroke="{N}" stroke-width="3"/>'
    return o + '</svg>'
def strip():   # two octaves of letters; every other one is a floor of the tower
    L = 'CDEFGABCDEFGA'; W = 34; o = f'<svg viewBox="-2 -4 {len(L) * W + 4} 74" style="width:100%;max-width:{len(L) * W + 4}px;height:auto;display:block;margin:0 auto">'
    for i, c in enumerate(L):
        on = i % 2 == 0; tall = i >= 8
        o += f'<rect x="{i * W + 2}" y="18" width="{W - 4}" height="28" rx="4" fill="{("#fbd2c2" if tall else PINK) if on else "#fff"}" stroke="{(R if tall else N) if on else "#c9c7dc"}" stroke-width="{2 if on else 1.2}"/>'
        o += f'<text x="{i * W + W / 2}" y="37" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="{(R if tall else N) if on else "#a9a7c4"}">{c}</text>'
        if on: o += f'<text x="{i * W + W / 2}" y="64" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="{R if tall else N}">{i + 1}</text>'
        if on and i + 2 < len(L): o += f'<path d="M{i * W + W / 2 + 6},16 Q{i * W + W},2 {i * W + 1.5 * W + W / 2 - 6},16" fill="none" stroke="#b9bbd3" stroke-width="1.5"/>'
    return o + '</svg>'
TALL = [['<b>C9</b>', 'C7 + 9th', 'C E G B♭ <b class="co">D</b>', 'soulful', 'funk, soul'], ['<b>Cmaj9</b>', 'Cmaj7 + 9th', 'C E G B <b class="co">D</b>', 'dreamy', 'film, ballads'],
        ['<b>Cm9</b>', 'Cm7 + 9th', 'C E♭ G B♭ <b class="co">D</b>', 'smooth', 'neo-soul, R&amp;B'], ['<b>C11</b>', 'C9 + 11th, no 3rd', 'C G B♭ D <b class="co">F</b>', 'airy', 'gospel, pop'],
        ['<b>C13</b>', 'C7 + 13th', 'C E B♭ (D) <b class="co">A</b>', 'rich', 'jazz, blues endings']]
H7A = hpage(f"""{head('Part IV · Harmony · 7', 'The tower: 9, 11, 13', 'Why stop at the 7th? Keep stacking 3rds and the building grows three more floors: the 9th, the 11th and the 13th. At the top you have used <b>all seven letters, A to G</b>.')}
{two(tower(), '<div class="big3"><div><span>1</span><p>Build the seventh chord: <b>C E G B♭</b> (C7).</p></div><div><span>2</span><p>Keep skipping one letter: <b class="co">D</b>, <b class="co">F</b>, <b class="co">A</b>. Those floors are the <b>9th, 11th and 13th</b>.</p></div><div><span>3</span><p>Take 7 away to find the letter: 9 → 2nd (D), 11 → 4th (F), 13 → 6th (A). Same letters, an octave up.</p></div></div>', '1.05fr 1fr')}
{h3('Skip a letter, all the way up')}
<figure class="vx px">{strip()}<figcaption>Start on C and take every other letter: C E G B D F A (letters only: in C7 the B is B♭). After the 13th comes C again: the tower is full.</figcaption></figure>
{h3('Five tall chords on C')}
{pxr('h8_tall', ('n5', 'n10', 'n15', 'n20', 'n25'), 100, 'The red note is the top floor that gives each chord its name. C11 and C13 leave some notes out: see p. {{H7+1}}.')}
{tbl(['Chord', 'Built as', 'Notes', 'Sounds', 'Heard in'], TALL, ['14%', '24%', '24%', '14%', '24%'])}""", 78)
H7B = hpage(f"""<div class="kick">Part IV · Harmony · 7 · continued</div>
{h3('Too many notes? Leave some out')}
{two(pxr('h8_hand', ('n11',), 150, 'All seven notes sound muddy. Two hands play C13 with four: C in the left hand, B♭ E A in the right.'), '<p>Ten fingers, seven floors: you choose. <b>Keep</b> the 3rd and the 7th (they say what kind of chord it is) and the red top note (its colour). <b>Leave out</b> the 5th first. The right hand can drop the root too, when the left hand or a bass player plays it.</p><p class="sm">With a major 3rd, the 11th (F) rubs against E. So C13 leaves out the F. C11 does the opposite: it keeps the F and leaves out the E.</p>', '1fr 1fr')}
{h3('6 or 13? add9 or 9?')}
{tbl(['Same top note', 'Without the 7th', 'With the 7th (B♭)'], [['A on C', '<b>C6</b>: C E G A', '<b>C13</b>: C E B♭ A'], ['D on C', '<b>Cadd9</b>: C E G D', '<b>C9</b>: C E G B♭ D']], ['24%', '38%', '38%'])}
<p class="sm">Look for the 7th. No 7th: a colour chord (p. {{H6}}). A 7th: a tower chord.</p>
{inaction('Name this tall chord: G B D F A', pxr('h8_mys', ('n5',), 110), ['<b>Find the root:</b> each note skips one letter, so the bottom note, G, is the root.', '<b>The first four floors</b>, G B D F, count 3 + 2 + 2: G7.', '<b>One more floor:</b> A is the 2nd above G, an octave up: the 9th.'], 'G B D F A is <b>G9</b>: G7 with the 9th on top.')}
{thinkt('A tower block has a lift: you don’t stop at every floor. Get out at the 3rd, the 7th and the top floor with the view.')}
{watch(['Hunting far up for the 9th: it is just the 2nd, an octave higher (D on C).', 'Calling C13 a C6: the 13th chord has the 7th (B♭) as well.', 'Playing F and E together in C13 or C11: they clash. C13 drops the F; C11 drops the E.'])}
{foot('Seventh chords p. {{H5}} · Colour chords p. {{H6}}', 'Workbook Harmony 7 · Online: Library › Chords')}""", 79)

# ---------- Harmony 8 · Slash chords (her 5 Nov: cover all the uses) ----------
SLASHSVG = ('<svg viewBox="0 0 320 220" style="width:100%;max-width:290px;height:auto;display:block;margin:0 auto">'
    '<text x="92" y="92" text-anchor="middle" font-family="PF,serif" font-size="92" font-weight="700" fill="#26296b">C</text>'
    '<line x1="150" y1="20" x2="104" y2="200" stroke="#26296b" stroke-width="6" stroke-linecap="round"/>'
    '<text x="170" y="196" text-anchor="middle" font-family="PF,serif" font-size="92" font-weight="700" fill="#e4572e">E</text>'
    '<text x="8" y="120" font-family="AH,Arial" font-size="15" font-weight="700" fill="#26296b">the chord</text><text x="8" y="140" font-family="AH,Arial" font-size="14" fill="#26296b">right hand</text>'
    '<text x="222" y="150" font-family="AH,Arial" font-size="15" font-weight="700" fill="#e4572e">the bass</text><text x="222" y="170" font-family="AH,Arial" font-size="14" fill="#e4572e">left hand,</text><text x="222" y="188" font-family="AH,Arial" font-size="14" fill="#e4572e">lowest note</text></svg>')
JOBS = [['<b>Inversion</b>', 'C/E · C/G', 'a note of the chord', 'smoother changes (p. {{H4}})'], ['<b>Walk-down</b>', 'C · G/B · Am', 'one step down each time', 'a bass line that walks down'],
        ['<b>Pedal</b>', 'F/C · G/C', 'the same note, held', 'chords move over a floor'], ['<b>Colour</b>', 'F/G · D/C', 'not in the chord', 'open, modern: pop, gospel']]
H8A = hpage(f"""{head('Part IV · Harmony · 8', 'Slash chords', 'C/E means one chord with a chosen bass note: play a C chord, with E as the lowest note. It is not a fraction, and not two chords.')}
{two(SLASHSVG, '<div class="big3"><div><span>1</span><p>Before the slash: the <b>chord</b>. C means C E G, in the right hand.</p></div><div><span>2</span><p>After the slash: the <b class="co">bass</b>. E goes in the left hand, below everything.</p></div><div><span>3</span><p>Play them together: <b>C/E</b>, “C over E”.</p></div></div>' + pxr('h9_hero', ('n4',), 120), '1fr 1.1fr')}
{h3('Four jobs for a slash chord')}
{tbl(['Job', 'Example', 'The bass note is', 'What you hear'], JOBS, ['20%', '22%', '28%', '30%'])}
{h3('Job 2: a bass that walks down')}
{pxr('h9_walk', ('n4', 'n8', 'n12', 'n16', 'n20'), 160, 'The red bass walks straight down, C B A G F, while the right hand moves a step at most. G/B and C/G make the steps possible.')}""", 80)
H8B = hpage(f"""<div class="kick">Part IV · Harmony · 8 · continued</div>
{h3('Job 3: a pedal, one bass under everything')}
{pxr('h9_pedal', ('n4', 'n8', 'n12', 'n16'), 110, 'The bass holds C while the chords change above it: C, F/C, G/C, C. The chords pull away from the C, then come home. (It is called a pedal after the organ’s foot pedals, which hold long low notes.)')}
{h3('Job 4: a bass from outside the chord')}
{two(pxr('h9_out', ('n4', 'n8'), 140), '<p><b>F/G</b>: F A C over a G. G is not in the F chord, so it floats, open and unfinished, ready to land on C. Pop and gospel players love it.</p><p><b>D/C</b>: D F♯ A over a C. The C is not in the D chord, so it rubs, then usually steps down to B (D/C to G/B).</p>', '1fr 1.1fr')}
{inaction('Name it: G B D over a low B', pxr('h9_mys', ('n4',), 120), ['<b>The right hand:</b> G B D, the G chord.', '<b>The lowest note:</b> B, in the left hand.', '<b>Chord, slash, bass:</b> G/B. B is in the G chord: an inversion.'], 'It is <b>G/B</b>, “G over B”: G major, 1st inversion.')}
{thinkt('A house and the ground it stands on: the slash says what to build (the chord) and where to build it (the bass). Same house, new ground, new view.')}
{watch(['Writing it back to front: the chord comes first, the bass second. E/C would be an E chord over C.', 'Letting the right hand dip below the bass: the letter after the slash must be the lowest note you play.', 'Forgetting the chord itself: in C/E the right hand still plays the whole C chord, C E G, not just C.'])}
{foot('Inversions p. {{H4}} · Colour chords p. {{H6}}', 'Workbook Harmony 8 · Online: Library › Chords')}""", 81)

css += """
.big3{display:flex;flex-direction:column;gap:12px;font-size:16px;line-height:1.4} .big3 div{display:flex;gap:10px;align-items:flex-start} .big3 p{margin:0} .big3 span{flex:none;width:26px;height:26px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:14px}
.k7{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:6px 0 4px} .kc{border:1.5px solid #e3e1ee;border-radius:8px;padding:8px 8px 10px;display:flex;flex-direction:column;align-items:center;gap:4px;text-align:center}
.ks{font-family:PF,serif;font-size:26px;color:#26296b;line-height:1} .kn{font-size:12.5px;font-weight:700;color:#26296b} .km{font-size:17px;font-weight:700;color:#e4572e} .kw{font-size:11.5px;color:#6d6f9c;line-height:1.3}
"""

_secs = [assemble(k, pg) for k, pg in (('H1', H1), ('H2', H2), ('H3', H3), ('H4', H4), ('H5', (H5A, H5B)), ('H6', (H6A, H6B)), ('H7', (H7A, H7B)), ('H8', (H8A, H8B)))]
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}</style></head><body>{HOPEN}{"".join(_secs)}{_flowjs}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-harmony.html', 'w').write(html)
print('ok')
