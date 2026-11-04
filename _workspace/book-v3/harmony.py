# The Piano Butler Handbook, Part III: Harmony (her 4 Nov: Harmony after Pitch and Time; the snowman for triads)
import re as _re
exec(open('/tmp/claude-0/pk/pitch.py').read())   # helpers, css, px / kbx / inaction / howto (rewrites the Pitch draft, harmless)
def hpage(inner, n): return page(inner, n, 'PART III · HARMONY')
W_ = 34   # white-key width in the keyboard pictures
def dot(i, t='', col='#e4572e', y=74): return f'<circle cx="{i * W_ + W_ / 2}" cy="{y}" r="11" fill="{col}"/>' + (f'<text x="{i * W_ + W_ / 2}" y="{y + 4}" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" fill="#fff">{t}</text>' if t else '')

YK545 = '<figure class="vx"><div class="vs">' + ''.join([P['yk_545'].replace('<svg ', '<svg style="max-height:68px" ', 1)]) + '</div></figure>'
for _n in ('n1', 'n2', 'n3', 'n4'): YK545 = YK545.replace(f'<g id="{_n}" class="note">', f'<g id="{_n}" class="note" style="fill:#e4572e;color:#e4572e">', 1)
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
{youknow('Mozart, Sonata in C, K. 545: the left hand', YK545, 'The famous rippling left hand is just the <b class="co">C triad</b>, broken: <b>C G E G</b>, over and over. Root, 5th, 3rd, 5th: one chord, one note at a time.', 'Play C G E G evenly with your left hand, then C E G together.')}
{watch(['Stacking 2nds or 4ths: a triad skips exactly one letter each time.', 'Naming a chord from its top note: the root, at the bottom of the stack, names it.'])}
{foot('Counting intervals p. 32 · Major scales p. 36', 'Workbook Harmony 1 · Online: Library › Chords')}""", 64)

_secs = []
for _old, _pg in ((64, H1),):
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
