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
HTOC = [(t, PM.PAGE[k]) for t, k in (('Chords and triads', 'H1'), ('Four kinds of triad', 'H2'), ('Chords in a key', 'H3'), ('Inversions', 'H4'), ('Seventh chords', 'H5'), ('Colour chords', 'H6'), ('The tower: 9, 11, 13', 'H7'), ('Slash chords', 'H8'), ('Chords from outside the key', 'H9'), ('Cadences', 'H10'), ('Chords under a melody', 'H11'), ('Progressions everywhere', 'H12'), ('Tips: when a chord sounds wrong', 'HT'))]
hflow = ''.join(f'<div class="fl"><b>{a}</b><span>{b}</span></div>' + ('<span class="fa">›</span>' if i < 4 else '') for i, (a, b) in enumerate([('Triads', 'the house'), ('Sevenths', 'one more floor'), ('The tower', '9, 11, 13'), ('Slash chords', 'a new bass'), ('Progressions', 'chords that travel')]))
HOPEN = f"""<section class="pg part2"><div class="pframe"><div class="pk">Part IV · Which notes sound together</div><div class="pt">Harmony</div><div class="pdv"></div>
<p class="pl">A melody is the singer; harmony is the band behind it: the chords underneath. Start with the triad, a house of three notes, then build it higher floor by floor, and finish with the chords that close a phrase and carry a song.</p>
<div class="flow">{hflow}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{p}</span></div>' for x, p in HTOC)}</div></div></section>"""

BIGSNOW = ('<svg viewBox="0 0 260 300" style="width:100%;max-width:330px;height:auto;display:block;margin:0 auto">'
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

# ---------- comic panels and snowmen (from the Secret Files mock-up, her 5 Nov A) ----------
N, R = '#26296b', '#e4572e'
def skb(n=8, W=30, H=100, marks='', hops=(), dots=(), ghost=(), fingers=None, labels=True):
    o = f'<svg viewBox="-4 -34 {n * W + 8} {H + 52}" style="width:100%;height:auto;display:block">'
    for i in range(n): o += f'<rect x="{i * W}" y="0" width="{W}" height="{H}" fill="#fff" stroke="{N}" stroke-width="1.6"/>'
    for i in range(n - 1):
        if 'CDEFGAB'[i % 7] in 'CDFGA': o += f'<rect x="{(i + 1) * W - W * 0.3}" y="0" width="{W * 0.6}" height="{H * 0.58}" rx="2" fill="{N}"/>'
    if labels:
        for i in range(n): o += f'<text x="{i * W + W / 2}" y="{H - 8}" text-anchor="middle" font-family="AH" font-size="11" font-weight="700" fill="{N}">{"CDEFGAB"[i % 7]}</text>'
    for i in ghost: o += f'<rect x="{i * W + 3}" y="{H * 0.62}" width="{W - 6}" height="{H * 0.22}" rx="4" fill="#eef0f8"/><text x="{i * W + W / 2}" y="{H * 0.78}" text-anchor="middle" font-family="CV" font-size="16" fill="#8d8fb3">skip</text>'
    for i in dots: o += f'<circle cx="{i * W + W / 2}" cy="{H * 0.72}" r="10" fill="{R}"/>'
    for a, b in hops:
        x1, x2 = a * W + W / 2, b * W + W / 2
        o += f'<path d="M{x1},-6 Q{(x1 + x2) / 2},-30 {x2},-6" fill="none" stroke="{R}" stroke-width="2.6" stroke-dasharray="5 4"/><path d="M{x2 - 8},-14 L{x2},-5 L{x2 + 3},-16" fill="none" stroke="{R}" stroke-width="2.6"/>'
    if fingers:
        for i, f in fingers: o += f'<circle cx="{i * W + W / 2}" cy="-16" r="11" fill="#fff" stroke="{R}" stroke-width="2.2"/><text x="{i * W + W / 2}" y="-11" text-anchor="middle" font-family="AH" font-size="13" font-weight="700" fill="{R}">{f}</text>'
    return o + marks + '</svg>'
def snowman(balls, letters=('C', 'E', 'G'), face=None, w=90, hat=True, red0=True, tags=True):
    ys, rs = [150, 98, 58], [34, 26, 20]
    o = f'<svg viewBox="0 0 {150 if tags else 120} 196" style="width:{w}px;height:auto;display:block;margin:0 auto">'
    for i in range(balls):
        o += f'<circle cx="60" cy="{ys[i] + 10}" r="{rs[i]}" fill="{"#fde6dd" if i == 0 else "#fff"}" stroke="{R if i == 0 else N}" stroke-width="2.6"/>'
        if tags: o += f'<text x="{60 + rs[i] + 8}" y="{ys[i] + 18}" font-family="PF" font-size="{24 - i * 2}" font-weight="700" fill="{R if i == 0 and red0 else N}">{letters[i]}</text>'
    top = ys[balls - 1] + 10; rt = rs[balls - 1]
    if hat: o += f'<path d="M{60 - rt * 0.8},{top - rt + 2} L{60 + rt * 0.8},{top - rt + 2} L{60 + rt * 0.6},{top - rt - 20} L{60 - rt * 0.6},{top - rt - 20} Z" fill="{N}"/><line x1="{60 - rt * 1.1}" x2="{60 + rt * 1.1}" y1="{top - rt + 2}" y2="{top - rt + 2}" stroke="{N}" stroke-width="4" stroke-linecap="round"/>' if balls == 3 else ''
    if face or balls < 3:
        f = face or 'happy'
        o += f'<circle cx="{60 - rt * 0.35}" cy="{top - rt * 0.25}" r="2.2" fill="{N}"/><circle cx="{60 + rt * 0.35}" cy="{top - rt * 0.25}" r="2.2" fill="{N}"/>'
        m = {'happy': f'M{60 - rt * 0.45},{top + rt * 0.25} Q60,{top + rt * 0.6} {60 + rt * 0.45},{top + rt * 0.25}', 'sad': f'M{60 - rt * 0.45},{top + rt * 0.5} Q60,{top + rt * 0.15} {60 + rt * 0.45},{top + rt * 0.5}', 'worried': f'M{60 - rt * 0.45},{top + rt * 0.4} Q{60 - rt * 0.2},{top + rt * 0.2} 60,{top + rt * 0.4} Q{60 + rt * 0.2},{top + rt * 0.6} {60 + rt * 0.45},{top + rt * 0.4}'}[f]
        o += f'<path d="{m}" fill="none" stroke="{N}" stroke-width="2.2" stroke-linecap="round"/>'
    return o + '</svg>'
def spanel(n, pic, cap): return f'<div class="pn"><span class="pnum">{n}</span>{pic}<p>{cap}</p></div>'

def guestman(letters, redi=(), w=70, tag=''):
    ys, rs = [150, 98, 58], [34, 26, 20]
    o = f'<svg viewBox="0 0 160 250" style="width:{w}px;height:auto;display:block;margin:0 auto">'
    for i in range(3):
        red = i in redi
        o += f'<circle cx="60" cy="{ys[i] + 10}" r="{rs[i]}" fill="{"#fde6dd" if red else "#fff"}" stroke="{R if red else N}" stroke-width="{3 if red else 2.4}"/>'
        o += f'<text x="{60 + rs[i] + 6}" y="{ys[i] + 20}" font-family="PF" font-size="{34 - i * 3}" font-weight="700" fill="{R if red else N}">{letters[i]}</text>'
    o += f'<path d="M48,49 L72,49 L69,27 L51,27 Z" fill="{N}"/><line x1="40" x2="80" y1="49" y2="49" stroke="{N}" stroke-width="4" stroke-linecap="round"/>'
    if tag:   # her 5 Nov: the chord name sits in its own label, clear of the snowman, so it reads as a name
        tw = 22 + 15 * len(tag.replace('♭', 'b').replace('♯', '#'))
        o += f'<rect x="{60 - tw / 2}" y="214" width="{tw}" height="32" rx="16" fill="{N}"/><text x="60" y="237" text-anchor="middle" font-family="AH" font-size="22" font-weight="700" fill="#fff">{tag}</text>'
    return o + '</svg>'

H1 = hpage(f"""{head('Part IV · Harmony · 1', 'Chords and triads', 'Press two or more notes at once and you have a <b>chord</b>. The favourite of all is the <b>triad</b>: three notes stacked like a snowman.')}
{two(BIGSNOW, '<div class="big3"><div><span>1</span><p>Pick a note: the <b class="co">root</b>, the big ball at the bottom. It holds the chord up and gives it its name.</p></div><div><span>2</span><p>Skip one letter, take the next: <b>E</b>, the <b>3rd</b>.</p></div><div><span>3</span><p>Skip again: <b>G</b>, the <b>5th</b>. C E G is the triad of C.</p></div></div>' + kbx('C', 8, W_, 100, label=True, shade={1: '#eef0f8', 3: '#eef0f8'}, marks=[dot(0, '1'), dot(2, '3'), dot(4, '5')], scale=1.0) + '<p class="sm" style="text-align:center;margin:4px 0 0">On the keys: play one, skip one (shaded), play one, skip one, play one.</p>', '1.1fr 1fr')}
{two(px('h_build', 104, 'The snowman on the staff: three lines in a row (or three spaces).'), '<p>On the staff, each ball sits on the <b>next line up</b> (or the next space up): the root, a <b>3rd</b> above it, a <b>5th</b> above the root.</p><p class="sm">First met: Level ½ (the tonic triad of C, G and F major).</p>', '1fr 1.15fr')}
{inaction('Build a triad on G', kbx('C', 10, W_, 92, label=True, shade={5: '#eef0f8', 7: '#eef0f8'}, marks=[dot(4, '1', y=67), dot(6, '3', y=67), dot(8, '5', y=67)], scale=1.0), ['<b>Start on G:</b> the root.', '<b>Skip A, play B:</b> the 3rd.', '<b>Skip C, play D:</b> the 5th.'], 'G B D: the triad of <b>G</b>. Same shape as C E G, just moved up.')}
<!--SPLIT-->
{two(h3('All lines or all spaces') + '<p>A stacked triad sits on <b>three lines in a row</b> or in <b>three spaces in a row</b>, in a neat stack. If one note breaks the pattern, it is not a triad.</p>', px('h_ls', 64, 'Lines, spaces, lines, spaces: every one a triad.'), '1fr 1.15fr')}
{two(h3('Solid and broken') + '<p>Played together, a chord is <b>solid</b> (or blocked). Played one note at a time, it is <b>broken</b>. Spread up and down the keyboard, a broken chord becomes an <b>arpeggio</b>. Left-hand accompaniments, the arpeggios in technical work and the chord names over a song are all triads.</p><p class="sm">First met: Level 0; arpeggios from Level 1.</p>', px('h_sb', 66, 'The same three notes, solid then broken.'), '1fr 1.15fr')}
{inaction('Is it a triad?', px('h_is', 58), ['<b>Chord 1:</b> D F A, all in spaces, each a 3rd apart: <b>a triad</b>.', '<b>Chord 2:</b> D E A: D to E is a 2nd. <b>Not a triad.</b>', '<b>Chord 3:</b> D G C, stacked in 4ths. <b>Not a triad.</b>'], 'Only chord 1 is a triad. Check that each note is a <b>3rd</b> above the one below.')}
{youknow('The Blue Danube (Johann Strauss II), here in C', YKDAN, 'The most famous waltz tune simply climbs the <b class="co">C triad</b>: <b>C, C E G, G</b>. Root, 3rd, 5th, then it holds the top: that is why it sounds so open.', 'Play C E G one at a time, then hum the waltz over it.')}
{thinkt('Solid: three friends shout “Hello!” together. Broken: each says it in turn.')}
{watch(['Stacking 2nds or 4ths: a triad skips exactly one letter each time.', 'Naming a chord from its top note: the root names it (at the bottom when the notes are stacked in 3rds).'])}
{game('Build one yourself', '<div class="pns">' + spanel('G', skb(n=10, dots=(4, 6, 8), hops=((4, 6), (6, 8)), ghost=(5, 7)) + snowman(3, ('G', 'B', 'D'), w=78), 'Start on G: <b>G B D</b>.') + spanel('F', skb(n=10, dots=(3, 5, 7), hops=((3, 5), (5, 7)), ghost=(4, 6)) + snowman(3, ('F', 'A', 'C'), w=78), 'Start on F: <b>F A C</b>.') + spanel('?', skb(n=10) + snowman(3, ('?', '?', '?'), w=78, red0=False), 'Your turn: start on <b>A</b>. Which three keys?') + '</div>', 'Build the snowman on A: play one, skip one, play one, skip one, play one.', 'A C E, the A minor chord.')}
{try10(skb(n=8, W=34, fingers=((0, 1), (2, 3), (4, 5)), dots=(0, 2, 4)), 'Thumb on C. Fingers <b class="co">1, 3, 5</b> down together.', 'That is the C chord. Slide your hand to any white key and do it again: the snowman shape always works.')}
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
{px('h3_cmaj', 80, 'The seven chords of C major. Only white keys, so the kinds come out as on p. {{H2+1}}.')}
{tbl(['Numeral', 'Name', 'Kind', 'Keys between', 'In C', 'In G'], [[a, b, c, {'major': '3 + 2', 'minor': '2 + 3', 'diminished': '2 + 2'}[c], d, e] for a, b, c, d, e in DEG], ['13%', '21%', '18%', '18%', '15%', '15%'])}
<p class="sm">The same in every major key: I, IV and V are major; ii, iii and vi are minor; vii° is diminished. First met: I, IV and V at Levels 1–2; the other chords from about Level 4.</p>
{two(h3('The three primary chords') + '<p><b class="co">I, IV and V</b> are the strongest chords of a key. Between them they hold <b>every note of the scale</b>: C E G, F A C, G B D. That is why so many tunes need only these three.</p>', thinkt('I is home. IV is a visit next door. V is the walk back, already looking at the front door: it wants to go home to I. Play C, F, G, C and hear it.'), '1.2fr 1fr')}
{inaction('Find I, IV and V in G major', px('h3_g', 74), ['<b>Count up the scale:</b> G A B C D. The 1st note is G, the 4th C, the 5th D.', '<b>Build a triad on each</b>, using the key signature: the F is F♯.', '<b>Check with the keys between:</b> all three are 3 + 2, major.'], 'In G major: <b>I = G</b>, <b>IV = C</b>, <b>V = D</b> (D F♯ A).')}
<!--SPLIT-->
{two(h3('In a minor key') + '<p>In A minor the three main chords are <b>i</b> (A minor), <b>iv</b> (D minor) and <b>V</b>: E G♯ B, made major by the <b class="co">raised 7th</b>, G♯, which pulls up to the home note A. Check: E G♯ B is 3 + 2, major.</p>', px('h3_min', 88, 'A minor: i, iv and V. The G♯ makes V major.'), '1fr 1.1fr')}
{h3('Which chord holds the note?')}
{tbl(['Note in C', 'C', 'D', 'E', 'F', 'G', 'A', 'B'], [['<b>Chord</b>', 'I or IV', 'V', 'I', 'IV', 'I or V', 'IV', 'V']], ['16%'] + ['12%'] * 7)}
<p class="sm">The same idea works in every key: find which of I, IV and V holds the note.</p>
{youknow('The twelve-bar blues', BLUES, 'Almost every blues, and a lot of rock ’n’ roll, is just <b class="co">I, IV and V</b> in twelve bars. Learn this chart and you can play along with hundreds of songs.', 'Play the chart in C with your left hand, one chord per bar, four beats each.')}
{watch(['Writing every numeral big: ii, iii and vi are minor, so they are written small.', 'Forgetting the raised 7th in a minor key: V in A minor is E G♯ B, not E G B.', 'Forgetting the raised 7th in a minor key: in A minor, V is E major, with G♯.'])}
{foot('Four kinds of triad p. {{H2}} · Major scales p. {{S3}} · Cadences p. {{H10}}', 'Workbook Harmony 3 · Online: Library › Chords')}""", 68)
css += """
.snowc{margin:0;font-size:15px;line-height:1.5}
.home7{display:grid;grid-template-columns:repeat(7,1fr);gap:2px} .hl{font-family:CV;font-size:19px;color:#6d6f9c;text-align:center;margin:-2px 0 6px} .g3{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;border-top:1.5px dashed #e4572e;padding-top:8px} .g3>div{display:flex;flex-direction:column;align-items:center;text-align:center} .g3 span{font-size:15px;line-height:1.3} .twr{display:flex;gap:10px;align-items:baseline;margin:6px 0 2px} .twr b{font-size:16px} .twr span{font-family:CV;font-size:19px;color:#6d6f9c} .twarrow{display:grid;grid-template-columns:repeat(7,1fr);text-align:center;font-family:CV;font-size:20px;color:#e4572e;height:22px;line-height:22px} .gkb{border:2px solid #26296b;border-radius:10px;padding:8px 10px 6px;display:flex;flex-direction:column;align-items:center;gap:2px;height:100%} .gkb b{font-size:17px;color:#e4572e} .gkb span{font-size:14px;color:#26296b;margin-bottom:4px}
.inv3{display:flex;align-items:center;justify-content:center;gap:6px;margin:4px 0 6px} .ic{display:flex;flex-direction:column;align-items:center;gap:2px;text-align:center;border:2px solid #e3e1ee;border-radius:10px;padding:8px 12px} .ic>b{font-size:15px} .nt{display:flex;gap:14px;align-items:baseline;font-size:22px;font-weight:700} .pop{color:#26296b} .cls{color:#e4572e} .bs{font-size:13.5px;color:#6d6f9c}
.rn{font-family:PF,serif;font-weight:700;display:inline-flex;align-items:center;gap:1px} .fg{display:inline-flex;flex-direction:column;font-family:AH,Arial;font-size:.58em;line-height:1;margin-left:1px} .fg i{font-style:normal} .invt td{vertical-align:middle;font-size:17px}
.hold3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px} .hold7{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin:8px 0 2px;text-align:center} .hold7>div{display:flex;flex-direction:column;align-items:center;gap:3px;border:1.5px solid #e3e1ee;border-radius:8px;padding:6px 2px} .hold7 b{font-family:PF;font-size:24px;color:#26296b} .hold7 span{color:#fff;font-weight:800;font-size:13px;border-radius:10px;padding:1px 8px}
.mel{font-family:PF;font-size:22px;font-weight:700;color:#26296b;text-align:center;margin:2px 0;letter-spacing:.06em}
.tip{border-left:3px solid #e4572e;background:#fdf6f2;padding:10px 16px 12px;margin:12px 0} .tip .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .tip .tt{display:block;font-size:16px;margin:2px 0 6px} .tip table{background:transparent;table-layout:fixed;width:100%} .tip td,.tip th{vertical-align:top;white-space:normal!important}
.fixes{display:grid;grid-template-columns:1fr 1fr;gap:8px 14px;margin:6px 0 10px} .fixes>div{position:relative;padding:10px 12px 10px 44px;border:1px solid #e2ddd0;display:flex;flex-direction:column;gap:2px;font-size:13.5px;line-height:1.45} .fixes b{font-size:14.5px} .fixes .rn{position:absolute;left:12px;top:12px;width:22px;height:22px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;font-size:12.5px;display:flex;align-items:center;justify-content:center}
.fnkey{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center;justify-content:center;font-size:15px;margin:2px 0 8px} .fnkey .cb{padding:2px 10px;min-width:0} .nocapsh th{text-transform:none!important;letter-spacing:0!important;font-size:13px!important;color:#26296b!important}
.tripc{display:grid;grid-template-columns:150px 1fr;gap:10px;align-items:center;border-top:1px solid #e3e1ee;padding:7px 0} .tt2 b{display:block;font-size:16px} .tt2 span{font-size:13.5px;color:#6d6f9c;line-height:1.3;display:block}
.trip{display:flex;flex-wrap:wrap;align-items:center;gap:4px} .ta{color:#e4572e;font-weight:800} .cb{display:inline-flex;flex-direction:column;align-items:center;border-radius:8px;padding:4px 8px;min-width:40px;color:#fff;line-height:1.1} .cb b{font-family:PF;font-size:20px} .cb small{font-size:12px;font-weight:700;opacity:.9}
.cb.home{background:#e4572e} .cb.home2{background:#f2a48c} .cb.away{background:#26296b} .cb.pull{background:#3f8f6b}
.kbt{font-size:16px;font-weight:700;margin:0 0 2px;text-align:center} .gp3{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:4px 0} .gp3 .pair{gap:4px}
.pc4{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:6px 0 10px} .pc{border:2px solid #26296b;border-radius:10px;padding:8px 6px 10px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:2px} .pmark{font-family:PF;font-weight:800;font-size:46px;line-height:1;color:#e4572e;height:48px} .pmark.pw{font-size:28px;line-height:48px} .pc b{font-size:16px} .pc i{font-style:normal;font-size:14px;color:#6d6f9c} .pair{display:flex;align-items:center;justify-content:center;gap:2px} .pf{font-family:CV;font-size:20px;color:#e4572e;line-height:1.1}
.twmin .fav{background:#fff7f3;border:2px dashed #e4572e;border-radius:8px} .big3.h3x{flex-direction:row;gap:16px;margin:10px 0 4px} .big3.h3x>div{flex:1}
.pns{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:10px 0 4px} .pn{position:relative;border:2px solid #26296b;border-radius:10px;padding:16px 10px 10px;background:#fff;display:flex;flex-direction:column;gap:6px} .pn p{margin:0;font-size:15px;line-height:1.4;text-align:center} .pnum{position:absolute;left:-10px;top:-12px;width:28px;height:28px;border-radius:50%;background:#e4572e;color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:15px}
.blues{display:grid;grid-template-columns:repeat(4,1fr);gap:5px;width:100%;max-width:330px;margin:0 auto} .blues span{border:1.5px solid #26296b;border-radius:4px;padding:4px 0 5px;text-align:center;font-weight:700;font-size:15px;line-height:1.1;background:#fff} .blues i{display:block;font-style:normal;font-size:10.5px;color:#6d6f9c;letter-spacing:.06em} .blues .b4{background:#fdeee8} .blues .b5{background:#e4572e;color:#fff;border-color:#e4572e} .blues .b5 i{color:#ffe1d6}
"""

# ---------- Harmony 4 · Inversions ----------
def pxr(k, ids, h, cap=''):   # a staff picture with chosen notes in red, and a caption
    f = ykfig(k, ids, h)
    return f.replace('</div></figure>', '</div>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>')
INV = [['root position', 'the root (C)', 'C', 'I', '5/3', 'Level ½'], ['1st inversion', 'the 3rd (E)', 'C/E', 'Ib', '6/3 (6)', 'Level 3'], ['2nd inversion', 'the 5th (G)', 'C/G', 'Ic', '6/4', 'Level 5']]
ROLL = f'<svg viewBox="0 0 70 60" style="width:56px;height:auto"><path d="M8,44 C14,6 52,4 60,30" fill="none" stroke="{R}" stroke-width="3.5"/><path d="M51,25 L61,32 L64,20" fill="none" stroke="{R}" stroke-width="3.5" stroke-linejoin="round"/><text x="35" y="59" text-anchor="middle" font-family="CV" font-size="20" fill="{R}">roll</text></svg>'
def figs(rn, top='', bot=''):   # a Roman numeral with stacked figures, as written in harmony class: I⁶₄
    if not top: return f'<span class="rn">{rn}</span>'
    return f'<span class="rn">{rn}<span class="fg"><i>{top}</i><i>{bot}</i></span></span>'
INVH = ('<div class="inv3">' + ''.join(f'<div class="ic"><b>{t}</b>{guestman(l, r, 112)}<div class="nt"><span class="pop">{sym}</span><span class="cls">{cl}</span></div><span class="bs">bass: {bs}</span></div>' + (ROLL if i < 2 else '')
         for i, (t, l, r, sym, cl, bs) in enumerate([('root position', ('C', 'E', 'G'), (0,), 'C', figs('I'), 'C, the root'), ('1st inversion', ('E', 'G', 'C'), (2,), 'C/E', figs('I', '6'), 'E, the 3rd'), ('2nd inversion', ('G', 'C', 'E'), (1,), 'C/G', figs('I', '6', '4'), 'G, the 5th')])) + '</div>')
H4 = hpage(f"""{head('Part IV · Harmony · 4', 'Inversions', 'Same three notes, a different one at the bottom. The chord keeps its name; only the bass changes. The red ball is the root, C: watch it travel.')}
{INVH}
<div class="big3 h3x"><div><span>1</span><p>Start with the snowman <b>C E G</b>: root at the bottom.</p></div><div><span>2</span><p>Roll the bottom ball to the top: <b>E G C</b>. That is the 1st inversion.</p></div><div><span>3</span><p>Roll again: <b>G C E</b>, the 2nd inversion. Still <b>C major</b>.</p></div></div>
{h3('Two ways to write it')}
{tbl(['', 'Root position', '1st inversion', '2nd inversion'], [['<b>Chord symbol</b> <span class="lvl2">pop, jazz</span>', 'C', 'C/E', 'C/G'], ['<b>Harmony class</b> <span class="lvl2">numerals</span>', figs('I'), figs('I', '6'), figs('I', '6', '4')], ['<b>Also written</b>', 'Ia, 5/3', 'Ib, 6/3', 'Ic, 6/4'], ['<b>First met</b>', 'Level ½', 'Level 3', 'Level 5']], ['31%', '23%', '23%', '23%'], 'invt')}
<p class="sm">The little numbers count up from the bass. E G C: C is a <b>6th</b> above E, so I⁶. G C E: E is a 6th and C a <b>4th</b> above G, so I⁶₄. A slash chord just names the bass: C/E (more on p. {{{{H8}}}}).</p>
{pxr('h4_inv', ('n2', 'n7', 'n9'), 90, 'The same three chords on the staff; the red note is the root, C. To find the root, restack the notes every other letter (like C E G): then the bottom ball is the root.')}
<!--SPLIT-->
{h3('Why inversions?')}
<p>They let your hand <b>move as little as possible</b>: keep any note two chords share, and move the others to the nearest note of the next chord. Left-hand accompaniments and hymn parts are written this way.</p>
{inaction('Play I, IV, V, I smoothly', px('h4_smooth', 86), ['<b>I:</b> C E G. <b>IV:</b> keep C, move E up to F and G up to A: C F A.', '<b>V:</b> no shared note. C steps down to B, F down to D, A down to G: B D G.', '<b>I again:</b> B up to C, D up to E, G stays: C E G.'], 'IV is F/C and V is G/B: <b>inversions</b> keep the hand in one place.')}
{youknow('Pachelbel’s Canon, the bass (here in C)', ykfig('yk_canon', ('n2', 'n4', 'n6'), 84), 'The famous bass walks <b>straight down the scale</b>: C B A G F E. It can, because some chords are <b class="co">inversions</b>: G/B, Em/G and C/E put a different note in the bass.', 'Play the bass slowly and hum the famous violin tune over it.')}
{h3('Chords of C, every position')}
{tbl(['Chord', 'Root position', '1st inversion', '2nd inversion'], [['<b>I</b> (C)', 'C E G', 'E G C', 'G C E'], ['<b>IV</b> (F)', 'F A C', 'A C F', 'C F A'], ['<b>V</b> (G)', 'G B D', 'B D G', 'D G B'], ['<b>vi</b> (Am)', 'A C E', 'C E A', 'E A C']], ['16%', '28%', '28%', '28%'])}
{thinkt('The same three friends in a photo, swapping places: still the same group (the same chord), but whoever stands at the front (the bass) changes the picture.')}
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
{inaction('Which seventh is it? G B D F', px('h7_mys', 76), ['<b>Count the keys between:</b> G to B is 3, B to D is 2, D to F is 2.', '<b>3 + 2 + 2</b> is the bluesy one.', '<b>The root is G:</b> G7.'], 'G B D F is <b>G7</b>, the chord that pulls hardest back to C.')}
{h3('Spot the difference')}
{pxr('h7_diff', ('n8', 'n12'), 80, 'One note decides: B makes Cmaj7, B♭ makes C7. Everything below stays the same.')}
{youknow('The blues, with sevenths', BLUES.replace('>C<', '>C7<').replace('>F<', '>F7<').replace('>G<', '>G7<'), 'Swap the triads for <b class="co">7th chords</b> and the twelve-bar chart (p. {{H3+1}}) turns into the real blues: the 7th is the blue note.', 'Play the chart with plain C, F and G first (p. {{H3+1}}), then add the red 7ths: B♭, E♭ and F.')}
{two(pxr('h7_pull', ('n3', 'n5', 'n7', 'n8'), 76), '<p><b>Why G7 pulls home:</b> its B wants to rise to <b class="co">C</b> and its F wants to fall to <b class="co">E</b>. Two small steps, and you are home in C.</p>', '1.2fr 1fr')}
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
    KW, KH, y = 40, 112, 90
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

{h3('Sus wants to come home')}
{pxr('h6_shimmer', ('n6', 'n12'), 76, 'The red note leans, then slides back to E: F steps down, D steps up. Play it slowly: C, Csus4, C, Csus2, C. Guitarists love this shimmer.')}
{h3('On any root, the counts stay the same')}
{tbl(['Colour', 'Keys between', 'On C', 'On G', 'On F', 'On D'], ANY, ['13%', '17%', '17.5%', '17.5%', '17.5%', '17.5%'])}""", 76)
H6B = hpage(f"""<div class="kick">Part IV · Harmony · 6 · continued</div>
{inaction('Which colour is it? G C D', pxr('h6_mys', (), 100), ['<b>Count the keys between:</b> G to C is 4, C to D is 1.', '<b>4 + 1</b> is the sus4 card: no B (no 3rd), and C has taken its place.', '<b>The root is G:</b> Gsus4.'], 'G C D is <b>Gsus4</b>. Let the C fall to <b class="co">B</b> and you have G major.')}
<p class="sm"><b>sus</b>: the 3rd held up or down · <b>5</b>: no 3rd at all · <b>6</b> and <b>add9</b>: one note added on top. Csus means Csus4.</p>
{h3('Spot the difference')}
{pxr('h6_diff', ('n3', 'n8'), 82, 'The same red D, two jobs. Csus2 throws the E out; Cadd9 keeps the E and puts the D on top.')}
{two(pxr('h6_power', (), 82), '<p><b>The power chord:</b> just the root and the 5th, played low in the left hand. With no 3rd it is neither happy nor sad, only <b class="co">strong</b>: the sound of rock guitar. Play C5, F5, G5, C5 and drum the rhythm.</p>', '1.1fr 1fr')}
{two(pxr('h6_twins', ('n1', 'n6'), 78), '<p><b>C6 or Am7?</b> The same four notes, C E G A. The red bottom note decides: C at the bottom is <b>C6</b>; A at the bottom is <b>Am7</b>. More on the bass note in Slash chords, p. {{H8}}.</p>', '1fr 1.1fr')}
{thinkt('Dressing the snowman: a scarf (the 6th) or a hat (the 9th) and it is still the same snowman. Sus moves its middle ball; a power chord takes the middle ball away.')}
{watch(['Writing C2: some books mean Csus2, others Cadd9. Check whether the E is there.', 'Calling Cadd9 a ninth chord: C9 also has the 7th (B♭). Add9 is just the triad plus the 9th (D on C), nothing else (The tower, p. {{H7}}).'])}
{foot('Four kinds of triad p. {{H2}} · Seventh chords p. {{H5}}', 'Workbook Harmony 6 · Online: Library › Chords')}""", 77)

# ---------- Harmony 7 · The tower: 9, 11, 13 (picture-first, her 5 Nov: 'triad on the scale's land, sevenths a floor up, and beyond?') ----------
def tower(w=150, h=31):
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
{pxr('h8_tall', ('n5', 'n10', 'n15', 'n20', 'n25'), 90, 'The red note is the top floor that gives each chord its name. C11 and C13 leave some notes out: see p. {{H7+1}}.')}
{tbl(['Chord', 'Built as', 'Notes', 'Sounds', 'Heard in'], TALL, ['14%', '24%', '24%', '14%', '24%'])}""", 78)
H7B = hpage(f"""<div class="kick">Part IV · Harmony · 7 · continued</div>
{h3('Too many notes? Leave some out')}
{two(pxr('h8_hand', ('n11',), 140, 'All seven notes sound muddy. Two hands play C13 with four: C in the left hand, B♭ E A in the right.'), '<p>Ten fingers, seven floors: you choose. <b>Keep</b> the 3rd and the 7th (they say what kind of chord it is) and the red top note (its colour). <b>Leave out</b> the 5th first. The right hand can drop the root too, when the left hand or a bass player plays it.</p><p class="sm">With a major 3rd, the 11th (F) rubs against E. So C13 leaves out the F. C11 does the opposite: it keeps the F and leaves out the E.</p>', '1fr 1fr')}
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
{pxr('h9_pedal', ('n4', 'n8', 'n12', 'n16'), 100, 'The bass holds C while the chords change above it: C, F/C, G/C, C. The chords pull away from the C, then come home. (It is called a pedal after the organ’s foot pedals, which hold long low notes.)')}
{h3('Job 4: a bass from outside the chord')}
{two(pxr('h9_out', ('n4', 'n8'), 140), '<p><b>F/G</b>: F A C over a G. G is not in the F chord, so it floats, open and unfinished, ready to land on C. Pop and gospel players love it.</p><p><b>D/C</b>: D F♯ A over a C. The C is not in the D chord, so it rubs, then usually steps down to B (D/C to G/B).</p>', '1fr 1.1fr')}
{inaction('Name it: G B D over a low B', pxr('h9_mys', ('n4',), 120), ['<b>The right hand:</b> G B D, the G chord.', '<b>The lowest note:</b> B, in the left hand.', '<b>Chord, slash, bass:</b> G/B. B is in the G chord: an inversion.'], 'It is <b>G/B</b>, “G over B”: G major, 1st inversion.')}
{thinkt('A house and the ground it stands on: the slash says what to build (the chord) and where to build it (the bass). Same house, new ground, new view.')}
{watch(['Writing it back to front: the chord comes first, the bass second. E/C would be an E chord over C.', 'Letting the right hand dip below the bass: the letter after the slash must be the lowest note you play.', 'Forgetting the chord itself: in C/E the right hand still plays the whole C chord, C E G, not just C.'])}
{foot('Inversions p. {{H4}} · Colour chords p. {{H6}}', 'Workbook Harmony 8 · Online: Library › Chords')}""", 81)

# ---------- Harmony 9 · Chords from outside the key (direction A: secret, picture first, game, Try it) ----------
HOME = ''.join(f'<div>{guestman((a, b_, c), (), 78, nm)}</div>' for a, b_, c, nm in [('C', 'E', 'G', 'C'), ('D', 'F', 'A', 'Dm'), ('E', 'G', 'B', 'Em'), ('F', 'A', 'C', 'F'), ('G', 'B', 'D', 'G'), ('A', 'C', 'E', 'Am'), ('B', 'D', 'F', 'B°')])

def gkb(moves, W=40, H=128):   # moves: (from semitone, to semitone, guest name, target name); semitones from C
    wpos = [0, 2, 4, 5, 7, 9, 11, 12]; n = 8
    def x(st): return wpos.index(st) * W + W / 2 if st in wpos else (wpos.index(st - 1) + 1) * W
    def isb(st): return st not in wpos
    o = f'<svg viewBox="-4 -40 {n * W + 8} {H + 46}" style="width:100%;height:auto;display:block">'
    for i in range(n): o += f'<rect x="{i * W}" y="0" width="{W}" height="{H}" fill="#fff" stroke="{N}" stroke-width="1.6"/>'
    for i in range(n - 1):
        if 'CDEFGAB'[i % 7] in 'CDFGA':
            o += f'<rect x="{(i + 1) * W - W * 0.3}" y="0" width="{W * 0.6}" height="{H * 0.58}" rx="2" fill="{N}"/>'
    for a, b, g, t in moves:
        xa, xb = x(a), x(b); ya = H * 0.4 if isb(a) else H * 0.78; yb = H * 0.4 if isb(b) else H * 0.78; up = xb > xa
        o += f'<path d="M{xa},-4 Q{(xa + xb) / 2},-38 {xb},-4" fill="none" stroke="{R}" stroke-width="3"/><path d="M{xb + (-9 if up else 9)},-13 L{xb},-3 L{xb + (-1 if up else 1)},-17" fill="none" stroke="{R}" stroke-width="3"/>'
        o += f'<circle cx="{xa}" cy="{ya}" r="13" fill="{R}" stroke="#fff" stroke-width="2"/><text x="{xa}" y="{ya + 4.5}" text-anchor="middle" font-family="AH" font-size="12" font-weight="800" fill="#fff">{g}</text>'
        o += f'<circle cx="{xb}" cy="{yb}" r="13" fill="#fff" stroke="{R}" stroke-width="2.6"/><text x="{xb}" y="{yb + 4.5}" text-anchor="middle" font-family="AH" font-size="13" font-weight="800" fill="{R}">{t}</text>'
    return o + '</svg>'
def arrow_svg(): return f'<svg viewBox="0 0 40 30" style="width:28px;height:auto"><path d="M4,15 L32,15 M24,7 L33,15 L24,23" fill="none" stroke="{R}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def gpair(a, ra, z, rz, na, nz, w=70): return f'<div class="pair">{guestman(a, ra, w, na)}{arrow_svg()}{guestman(z, rz, w, nz)}</div>'
MAJ = [('C', 'E', 'G', 'I', 'C'), ('D', 'F', 'A', 'ii', 'Dm'), ('E', 'G', 'B', 'iii', 'Em'), ('F', 'A', 'C', 'IV', 'F'), ('G', 'B', 'D', 'V', 'G'), ('A', 'C', 'E', 'vi', 'Am'), ('B', 'D', 'F', 'vii°', 'B°')]
MIN = [('C', 'E♭', 'G', (1,), 'Cm'), ('D', 'F', 'A♭', (2,), 'D°'), ('E♭', 'G', 'B♭', (0, 2), 'E♭'), ('F', 'A♭', 'C', (1,), 'Fm'), ('G', 'B♭', 'D', (1,), 'Gm'), ('A♭', 'C', 'E♭', (0, 2), 'A♭'), ('B♭', 'D', 'F', (0,), 'B♭')]
FAV = {3, 5, 6}   # the three favourites to borrow: Fm, A♭, B♭
TWINS = ('<div class="twins"><div class="twr"><b>C major</b><span>at home</span></div><div class="home7">' + ''.join(f'<div>{guestman((a, b_, c), (), 74, nm)}</div>' for a, b_, c, _, nm in MAJ) + '</div>'
         + '<div class="twarrow">' + ''.join(f'<span>{"↑ borrow" if i in FAV else ""}</span>' for i in range(7)) + '</div>'
         + '<div class="home7 twmin">' + ''.join(f'<div class="{"fav" if i in FAV else ""}">{guestman((a, b_, c), r, 74, nm)}</div>' for i, (a, b_, c, r, nm) in enumerate(MIN)) + '</div><div class="twr"><b>C minor</b><span>the twin: same home note, darker clothes</span></div></div>')

GTAB = [['<b>sharp guest</b>', 'D F♯ A', 'F♯ up to G', 'G', 'V of V'], ['<b>sharp guest</b>', 'A C♯ E', 'C♯ up to D', 'Dm', 'V of ii'], ['<b>sharp guest</b>', 'E G♯ B', 'G♯ up to A', 'Am', 'V of vi'],
        ['<b>flat guest</b>', 'F A♭ C', 'A♭ down to G', 'C', 'borrowed iv'], ['<b>flat guest</b>', 'A♭ C E♭', 'A♭ down to G', 'G or B♭', 'borrowed ♭VI'], ['<b>flat guest</b>', 'B♭ D F', 'B♭ on to C', 'C', 'borrowed ♭VII']]
PAIRS = [('A C♯ E', 'D F A', 'Dm', 'C♯ up to D'), ('D F♯ A', 'G B D', 'G', 'F♯ up to G'), ('E G♯ B', 'A C E', 'Am', 'G♯ up to A'), ('F A♭ C', 'C E G', 'C', 'A♭ down to G'), ('A♭ C E♭', 'G B D', 'G', 'A♭ down to G, E♭ down to D')]
PAIRTAB = [[f'<b>{a}</b>', f'<b class="co">{m}</b>', f'{b} ({c})'] for a, b, c, m in PAIRS]
H9 = hpage(f"""{head('Part IV · Harmony · 9', 'Chords from outside the key', 'C major lives on the white keys. A black key in a chord is a <b>guest</b>. Guests never stay: each one moves <b>one key</b>, and shows you where the music goes next.')}
{two('<div class="kbt">Sharp guests <b class="co">push up</b></div>' + gkb(((1, 2, 'C♯', 'D'), (6, 7, 'F♯', 'G'), (8, 9, 'G♯', 'A'))), '<div class="kbt">Flat guests <b class="co">sigh down</b></div>' + gkb(((8, 7, 'A♭', 'G'), (3, 2, 'E♭', 'D'))))}
<div class="big3 h3x"><div><span>1</span><p>Find the <b class="co">black key</b> in the chord: that is the guest.</p></div><div><span>2</span><p>A <b>sharp</b>? Go <b>up</b> one key. A <b>flat</b>? Go <b>down</b> one key.</p></div><div><span>3</span><p>You have found a note of the <b>next chord</b>. Play it and hear it land.</p></div></div>
{h3('Sharp guests: up one key names the next chord')}
<div class="gp3">{gpair(('A', 'C♯', 'E'), (1,), ('D', 'F', 'A'), (0,), 'A', 'Dm')}{gpair(('D', 'F♯', 'A'), (1,), ('G', 'B', 'D'), (0,), 'D', 'G')}{gpair(('E', 'G♯', 'B'), (1,), ('A', 'C', 'E'), (0,), 'E', 'Am')}</div>
<p class="sm" style="text-align:center">C♯ goes up to <b>D</b>, so the next chord is D minor. F♯ goes up to <b>G</b>: G. G♯ goes up to <b>A</b>: A minor.</p>
{two(pxr('h10_vv', ('n5',), 90), '<p>Try it in a song: C, D, G, C. The <b class="co">F♯</b> pushes up into G, then G leads home to C.</p>', '1.1fr 1fr')}
{h3('Flat guests: borrowed from the twin, they sigh down')}
{two(pxr('h10_iv', ('n9',), 90), '<p>C major and C minor are <b>twins</b>: the same home note, C, in different clothes. A flat guest is one piece of the twin’s outfit. In C, F, Fm, C the <b class="co">A♭</b> sighs down to G.</p>', '1.1fr 1fr')}
{TWINS}
<!--SPLIT-->
{h3('Their names, for later')}
{tbl(['Guest', 'Notes', 'Moves', 'Next chord', 'Its name'], GTAB, ['18%', '18%', '22%', '18%', '24%'])}
<p class="sm">B♭ is the one flat guest that walks <b>up</b> instead, on to C: the rock and film ending B♭ → C. The bigger guests (the Neapolitan, Level 7) follow the same idea.</p>
{two(pxr('h10_aug', ('n1', 'n3'), 90), '<p><b>An advanced guest (Extra):</b> the augmented 6th has two guests at once. The flat <b class="co">A♭</b> falls and the sharp <b class="co">F♯</b> rises, and both land on G. The rule still works.</p>', '1fr 1.2fr')}
{inaction('Find the guest: A C♯ E in C major', pxr('h10_mys', ('n2',), 90), ['<b>The black key:</b> C♯. That is the guest.', '<b>It is a sharp,</b> so it goes up one key: to D.', '<b>D names the next chord:</b> D minor (D F A).'], 'A C♯ E leads to <b>D minor</b>. Play them one after the other and hear C♯ slide into D.')}
{game('Where does the guest go?', '<div class="gm4" style="grid-template-columns:repeat(3,1fr)">' + ''.join(f'<div>{guestman(t, (), 92, n)}<b>{q}</b></div>' for t, n, q in ((('E', 'G♯', 'B'), 'E', '1'), (('D', 'F♯', 'A'), 'D', '2'), (('F', 'A♭', 'C'), 'Fm', '3'))) + '</div>', 'In C major: find each guest, follow it one key, and write the chord that comes next.', '1 G♯ up to A: A minor · 2 F♯ up to G: G · 3 A♭ down to G: C.')}
{try10(pxr('h10_iv', ('n9',), 64), 'Play C, F, Fm, C slowly.', 'Hear the A♭ sigh down to G? Now play C, D, G, C: the F♯ pushes up instead. One sighs, one pushes.')}
{thinkt('A surprise guest at dinner: one new face changes the whole conversation, and then everyone goes home.')}
{watch(['Following a sharp downwards: sharps push <b>up</b>, flats sigh <b>down</b>.', 'Learning the names first: play it, hear where the guest goes, then name it.', 'Mixing up the relatives: C minor is C major’s twin (same home note). A minor is its neighbour (same key signature). We borrow from the twin.'])}
{foot('Chords in a key p. {{H3}} · Slash chords p. {{H8}} · Cadences p. {{H10}}', 'Workbook Harmony 9 · Online: Library › Chromatic chords')}""", 82)

# ---------- Harmony 10 · Cadences (direction A: punctuation cards, game, Try it) ----------
def arrow_svg(): return f'<svg viewBox="0 0 40 30" style="width:28px;height:auto"><path d="M4,15 L32,15 M24,7 L33,15 L24,23" fill="none" stroke="{R}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CADS = [('.', 'Perfect', 'V → I', (('G', 'B', 'D'), 'V'), (('C', 'E', 'G'), 'I'), 'Home. The end.'),
        ('Amen', 'Plagal', 'IV → I', (('F', 'A', 'C'), 'IV'), (('C', 'E', 'G'), 'I'), 'A soft, gentle end.'),
        (',', 'Imperfect', '… → V', (('C', 'E', 'G'), 'I'), (('G', 'B', 'D'), 'V'), 'To be continued…'),
        ('?!', 'Interrupted', 'V → vi', (('G', 'B', 'D'), 'V'), (('A', 'C', 'E'), 'vi'), 'Surprise! Not home.')]
PCARDS = '<div class="pc4">' + ''.join(f'<div class="pc"><span class="pmark{" pw" if len(m) > 2 else ""}">{m}</span><b>{n}</b><i>{c}</i><div class="pair">{guestman(a[0], (), 56, a[1])}{arrow_svg()}{guestman(z[0], (0, 1, 2), 56, z[1])}</div><span class="pf">{f}</span></div>' for m, n, c, a, z, f in CADS) + '</div>'
H10 = hpage(f"""{head('Part IV · Harmony · 10', 'Cadences', 'A phrase is a musical sentence, and it needs punctuation. The last two chords of a phrase are its <b>cadence</b>. They tell you: finished, taking a breath, or surprise!')}
{PCARDS}
<div class="big3 h3x"><div><span>1</span><p>Find the end of a phrase: often a long note, or a breath.</p></div><div><span>2</span><p>Name its <b>last two chords</b> with numerals: V I, IV I, anything then V, or V vi.</p></div><div><span>3</span><p>Match the punctuation: full stop ( <b class="co">.</b> ), Amen, comma ( <b class="co">,</b> ) or <b class="co">?!</b></p></div></div>
{h3('The four cadences in C')}
{pxr('h11_cad', ('n4', 'n5', 'n6', 'n10', 'n11', 'n12', 'n16', 'n17', 'n18', 'n22', 'n23', 'n24'), 104, 'Perfect, plagal, imperfect, interrupted. The red chord is where each one lands.')}
{tbl(['Cadence', 'Chords', 'Feels like', 'Also called'], [['<b>Perfect</b>', 'V → I', 'a full stop: finished', 'authentic, full close'], ['<b>Plagal</b>', 'IV → I', 'the “A-men” sung at the end of a song in church', 'Amen cadence'], ['<b>Imperfect</b>', 'any → V', 'a comma: waiting', 'half close, half cadence'], ['<b>Interrupted</b>', 'V → vi', 'a surprise: not home yet', 'deceptive']], ['20%', '18%', '36%', '26%'])}
<!--SPLIT-->
{two(pxr('h11_v7', ('n1', 'n3'), 110), '<p><b>Make the full stop stronger:</b> add the 7th to V. In G7 the <b class="co">F</b> falls to E and the <b class="co">B</b> rises to C: two small steps home (Seventh chords, p. {{H5}}).</p>', '1fr 1.2fr')}
{inaction('How does this phrase end? C Am F G', pxr('h11_mys', ('n10', 'n11', 'n12'), 80), ['<b>The last two chords:</b> F, then G.', '<b>As numerals:</b> IV, then V.', '<b>It lands on V:</b> the comma.'], 'An <b>imperfect cadence</b>: the music takes a breath, and the next phrase answers it.')}
{game('Punctuate the phrases', '<div class="gm4" style="grid-template-columns:repeat(2,1fr);row-gap:6px">' + ''.join(f'<div style="flex-direction:row;justify-content:center;gap:10px"><b style="font-size:20px">{n}</b><div class="pair">{guestman(a, (), 56, x)}{arrow_svg()}{guestman(z, (), 56, y)}</div><span class="wl" style="width:70px"></span></div>' for n, a, x, z, y in (('1', ('F', 'A', 'C'), 'F', ('C', 'E', 'G'), 'C'), ('2', ('G', 'B', 'D'), 'G', ('A', 'C', 'E'), 'Am'), ('3', ('C', 'E', 'G'), 'C', ('G', 'B', 'D'), 'G'), ('4', ('G', 'B', 'D'), 'G', ('C', 'E', 'G'), 'C'))) + '</div>', 'Each pair ends a phrase in C major. Turn the letters into numerals first (C is I, F is IV, G is V, Am is vi), then write full stop, comma, Amen or ?! beside each.', '1 Amen (plagal), 2 ?! (interrupted), 3 comma (imperfect), 4 full stop (perfect).')}
{try10(pxr('h11_v7', ('n3',), 56), 'Play G7, then C. The end!', 'Now play G7, then A minor: “huh?!” That is the interrupted cadence. Then play F, then C, and sing “A-men”.')}
{thinkt('Punctuation in a sentence: a full stop ends it, a comma makes you wait, and a surprise makes you gasp. Music ends its phrases the same way.')}
{watch(['Calling every ending on I (C) perfect: a perfect cadence comes <b>from V</b>. F to C is plagal.', 'Mixing up imperfect and perfect: imperfect <b>ends on</b> V; perfect <b>starts on</b> V and lands on I.'])}
{foot('Chords in a key p. {{H3}} · Seventh chords p. {{H5}} · Chords under a melody p. {{H11}}', 'Workbook Harmony 10 · Online: Library › Cadences')}""", 87)

# ---------- Harmony 11 · Chords under a melody ----------
HOLD = [('C', ('I', 'IV')), ('D', ('V',)), ('E', ('I',)), ('F', ('IV',)), ('G', ('I', 'V')), ('A', ('IV',)), ('B', ('V',))]
HCOL = {'I': '#e4572e', 'IV': '#26296b', 'V': '#3f8f6b'}
HOLDMAP = ('<div class="hold3">' + ''.join(f'<div>{guestman(l, (), 96, t).replace("fill=\"#26296b\"/><text x=\"60\" y=\"237\"", f"fill=\"{HCOL[t]}\"/><text x=\"60\" y=\"237\"")}</div>' for l, t in ((('C', 'E', 'G'), 'I'), (('F', 'A', 'C'), 'IV'), (('G', 'B', 'D'), 'V'))) + '</div>'
           + '<div class="hold7">' + ''.join(f'<div><b>{n}</b>' + ''.join(f'<span style="background:{HCOL[c]}">{c}</span>' for c in cs) + '</div>' for n, cs in HOLD) + '</div>')
H11 = hpage(f"""{head('Part IV · Harmony · 11', 'Chords under a melody', 'The melody is the singer; the chords are the band. To choose a chord for each bar, look at the melody’s main notes and pick the snowman holding them.')}
{h3('Which snowman holds the note?')}
{HOLDMAP}
<p class="sm" style="text-align:center">Every note of C major lives in I, IV or V. C and G live in two: let your ear choose.</p>
<div class="big3 h3x"><div><span>1</span><p>Look at the <b>main notes</b> of the bar: the long ones, and the ones on beats 1 and 3.</p></div><div><span>2</span><p>Find the snowman that holds them: <b>I, IV or V</b>.</p></div><div><span>3</span><p>Play that chord in the left hand while the right hand plays the tune.</p></div></div>
{h3('Twinkle, Twinkle, with its chords')}
{px('h12_twk', 96, 'C C G G sit in I (C); A A in IV (F), then G in I; F F in IV, E E in I; D D in V (G), and the last C in I. The chord changes halfway through bars 2, 3 and 4.')}
{h3('Three ways to play the chord in the left hand')}
{px('h12_lh', 92, 'Block: all three at once. Broken: one at a time, up and down. Alberti: low, high, middle, high, named after Domenico Alberti, who loved it.')}
<!--SPLIT-->
{youknow('Mozart, Sonata in C, K. 545: the left hand', ykfig('h12_545', (), 78), 'The opening left hand is an <b class="co">Alberti bass</b>: C G E G is just the C chord, broken into low, high, middle, high; D G F G is G7 (G B D F, without the B). Mozart wrote it an octave higher, starting on middle C.', 'Play this left hand alone, then add the famous tune: C, E G, B, C D C.')}
{inaction('Choose the chord: E D C D | E E E', '<p class="mel"><b class="co">E</b> D <b class="co">C</b> D | <b class="co">E</b> E <b class="co">E</b></p><p class="sm" style="text-align:center;margin:0">red = beats 1 and 3</p>', ['<b>Bar 1:</b> the main notes are E and C (beats 1 and 3).', '<b>E and C</b> both live in I.', '<b>Bar 2:</b> E E E lives in I too.'], 'Both bars take <b>I</b> (C). That is the start of Mary Had a Little Lamb.')}
{game('Pick the snowman', '<div class="gm4" style="grid-template-columns:repeat(3,1fr)">' + ''.join(f'<div><p class="mel">{m}</p><b>{n}</b></div>' for n, m in (('1', 'F A F A'), ('2', 'D B G B'), ('3', 'G E C E'))) + '</div>', 'Each bar is in C major. Which snowman holds its notes: I, IV or V?', '1 IV (F A C) · 2 V (G B D) · 3 I (C E G).')}
{try10(px('h12_alb', 86), 'Left hand: C G E G, over and over.', 'That is the Alberti bass on the C chord. Keep it going while you hum Twinkle, then try it on F (F C A C) and G (G D B D).')}
{thinkt('Like picking a coat for the weather: when the tune changes, change the chord.')}
{watch(['Choosing a chord for a passing note: use the main notes (strong beats, long notes).', 'Playing the left hand louder than the tune: the melody is the star, the chords are the stage.'])}
{foot('Chords in a key p. {{H3}} · Cadences p. {{H10}}', 'Workbook Harmony 11 · Online: Library › Chords')}""", 89)

# ---------- Harmony 12 · Progressions everywhere + Harmony tips ----------
FN = {'I': 'home', 'vi': 'home2', 'iii': 'home2', 'IV': 'away', 'ii': 'away', 'V': 'pull', 'V7': 'pull'}
INC = {'I': 'C', 'ii': 'Dm', 'iii': 'Em', 'IV': 'F', 'V': 'G', 'V7': 'G7', 'vi': 'Am'}
def trip(nums, key=INC): return '<div class="trip">' + '<span class="ta">→</span>'.join(f'<span class="cb {FN[n]}"><b>{n}</b><small>{key[n]}</small></span>' for n in nums) + '</div>'
TRIPS = [('The pop four', ['I', 'V', 'vi', 'IV'], 'countless pop songs and ballads'), ('The fifties', ['I', 'vi', 'IV', 'V'], 'old rock ’n’ roll and doo-wop'), ('The jazz three-step', ['ii', 'V', 'I'], 'jazz standards (as ii7, V7, Imaj7)'), ('The canon', ['I', 'V', 'vi', 'iii', 'IV', 'I', 'IV', 'V'], 'Pachelbel’s Canon and its many children')]
H12 = hpage(f"""{head('Part IV · Harmony · 12', 'Progressions everywhere', 'A <b>progression</b> is a trip from chord to chord. A handful of trips turn up in song after song. Learn them by their numbers and you can play them in any key.')}
<div class="fnkey"><span class="cb home"><b>I</b></span> home <span class="cb home2"><b>vi iii</b></span> home’s cousins <span class="cb away"><b>IV ii</b></span> away <span class="cb pull"><b>V</b></span> the pull back home</div>
{''.join(f'<div class="tripc"><div class="tt2"><b>{t}</b><span>{w}</span></div>{trip(n)}</div>' for t, n, w in TRIPS)}
<div class="big3 h3x"><div><span>1</span><p>Learn the trip by <b>numbers</b>: I V vi IV.</p></div><div><span>2</span><p>Pick a key and turn the numbers into chords: in C, <b>C G Am F</b>.</p></div><div><span>3</span><p>Play it round and round. Change key: the numbers stay the same.</p></div></div>
<!--SPLIT-->
{h3('Same trip, any key')}
{tbl(['The pop four', 'I', 'V', 'vi', 'IV'], [['<b>in C</b>', 'C', 'G', 'Am', 'F'], ['<b>in G</b>', 'G', 'D', 'Em', 'C'], ['<b>in F</b>', 'F', 'C', 'Dm', 'B♭'], ['<b>in D</b>', 'D', 'A', 'Bm', 'G']], ['28%', '18%', '18%', '18%', '18%'], 'nocapsh')}
{youknow('Pachelbel’s Canon: the trip under the tune', ykfig('yk_canon', ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8'), 80), 'The famous bass walks down, and above it the chords take the <b class="co">canon trip</b>: C G Am Em F C F G. Countless songs borrow it.', 'Play the bass slowly with your left hand and the chords in your right.')}
{inaction('Play the pop four in G major', trip(['I', 'V', 'vi', 'IV'], {'I': 'G', 'V': 'D', 'vi': 'Em', 'IV': 'C'}), ['<b>I</b> is the key note: G.', '<b>V</b> is the 5th note of the G scale: D. <b>vi</b> is the 6th: E, minor, so Em.', '<b>IV</b> is the 4th note: C.'], 'G, D, Em, C: <b>the pop four in G</b>. Same trip, new key.')}
{game('Name the trip', '<div class="gm4" style="grid-template-columns:1fr">' + ''.join(f'<div style="flex-direction:row;justify-content:center;gap:14px"><b>{n}</b><p class="mel" style="margin:0">{c}</p></div>' for n, c in (('1', 'C · Am · F · G'), ('2', 'Dm · G · C'), ('3', 'C · G · Am · F'))) + '</div>', 'All in C major. Turn each into numbers, then name the trip: the pop four, the fifties or the jazz three-step.', '1 the fifties (I vi IV V) · 2 the jazz three-step (ii V I) · 3 the pop four (I V vi IV).')}
{try10(trip(['I', 'V', 'vi', 'IV']), 'Play C, G, Am, F, four beats each.', 'Go round four times without stopping, left hand plays the chord’s name note (C for C, A for Am), right hand the whole snowman. Hum any tune you like over it.')}
{thinkt('A walk round the block: leave home, wander, feel the pull, and turn the corner back home.')}
{watch(['Learning songs one by one: learn the trip by numbers, then change key.', 'Mixing up the pop four and the fifties: same four chords, different order. Listen to which chord comes second.'])}
{foot('Chords in a key p. {{H3}} · Cadences p. {{H10}} · Chords under a melody p. {{H11}}', 'Workbook Harmony 12 · Online: Library › Chords')}""", 91)
HT = hpage(f"""{head('Part IV · Harmony · Tips', 'When a chord sounds wrong', 'A chord that sounds wrong usually has one small slip. Name the slip, fix that one note, and the chord comes right.')}
{inaction('Fix a sour chord', '<div class="pair" style="justify-content:center">' + guestman(('C', 'E♭', 'G'), (1,), 82, 'C?') + arrow_svg() + guestman(('C', 'E', 'G'), (1,), 82, 'C') + '</div>', ['<b>It sounds dark</b>, but the music wants a bright C chord.', '<b>Count the keys between:</b> 2, then 3. That is minor.', '<b>Move one note:</b> E♭ up to E makes 3 + 2. Bright again.'], 'One note was off: <b>fix the middle of the snowman</b>.')}
<div class="tip"><div class="bh">Tip</div><b class="tt">What you notice, what to check</b>
{tbl(['What you notice', 'Check', 'Turn to'], [['A chord sounds sour', '<b class="co">the kind</b>: keys between, 3 + 2 or 2 + 3', 'p. {{H2}}'], ['Your hand jumps all over', '<b class="co">an inversion</b>: keep the shared note still', 'p. {{H4}}'], ['A big chord sounds muddy', '<b class="co">leave notes out</b>: drop the 5th first', 'p. {{H7}}'], ['A sharp or flat surprises you', '<b class="co">a guest</b>: sharps go up, flats go down', 'p. {{H9}}'], ['The end does not feel finished', '<b class="co">the cadence</b>: end with V → I', 'p. {{H10}}'], ['The left hand fights the tune', '<b class="co">the main notes</b>: pick the snowman holding them', 'p. {{H11}}']], ['36%', '50%', '14%'])}
</div>
{h3('Four ways to learn chords fast')}
<div class="fixes">{''.join(f'<div><span class="rn" style="font-family:AH">{i + 1}</span><b>{a}</b><span>{b_}</span></div>' for i, (a, b_) in enumerate([('Build, then play', 'Say the snowman (C E G) before your fingers go down.'), ('Hands alone first', 'Left hand chords alone, then the tune alone, then together.'), ('One trip a week', 'Learn one progression, then play it in three keys.'), ('Listen for the kind', 'Play major and minor side by side: bright, then dark.')]))}</div>
{thinkt('Like a mechanic: one odd sound points to one part. Fix that part and the engine runs smoothly.')}""", 93)

css += """
.big3{display:flex;flex-direction:column;gap:12px;font-size:16px;line-height:1.4} .big3 div{display:flex;gap:10px;align-items:flex-start} .big3 p{margin:0} .big3 span{flex:none;width:26px;height:26px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:14px}
.k7{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:6px 0 4px} .kc{border:1.5px solid #e3e1ee;border-radius:8px;padding:8px 8px 10px;display:flex;flex-direction:column;align-items:center;gap:4px;text-align:center}
.ks{font-family:PF,serif;font-size:26px;color:#26296b;line-height:1} .kn{font-size:12.5px;font-weight:700;color:#26296b} .km{font-size:17px;font-weight:700;color:#e4572e} .kw{font-size:11.5px;color:#6d6f9c;line-height:1.3}
"""

_secs = [assemble(k, pg) for k, pg in (('H1', H1), ('H2', H2), ('H3', H3), ('H4', H4), ('H5', (H5A, H5B)), ('H6', (H6A, H6B)), ('H7', (H7A, H7B)), ('H8', (H8A, H8B)), ('H9', H9), ('H10', H10), ('H11', H11), ('H12', H12))]
_secs.append(_re.sub(r'<div class="foot"><span>\d+</span></div>', f'<div class="foot"><span>{PM.PAGE["HT"]}</span></div>', HT))
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}</style></head><body>{HOPEN}{"".join(_secs)}{_flowjs}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-harmony.html', 'w').write(html)
print('ok')
