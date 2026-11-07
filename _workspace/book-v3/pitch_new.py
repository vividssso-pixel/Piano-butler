# Part I Pitch, chapters 1-7, rewritten 7 Nov (her: "make every question and example a path to the aha";
# keyboard notes by landmark name, never octave numbers). exec'd from pitch.py; uses its helpers.
# One counting rule for the whole part: COUNT THE NOTES (start at 1, both ends) for letter distance and interval numbers;
# COUNT THE HOPS (each move to the very next key is 1, drawn as an arc) for semitones.
import re as _re
for _d in (P, PP):
    for _k in _d: _d[_k] = _d[_k].replace('>middle C<', '>Middle C<').replace('>treble G<', '>treble G<')
LMK = {'C2': 'Low C', 'C3': 'Bass C', 'C4': 'Middle C', 'C5': 'Treble C', 'C6': 'High C'}
NAV, RED, PINK, BLUE = '#26296b', '#e4572e', '#fde6dd', '#eef0f8'
_WH = 'CDEFGAB'

def _bpos(i, W): return (i + 1) * W          # centre of the black key just right of white key i
def _wpos(i, W): return (i + 0.5) * W
def qkb(start, n, W=34, H=110, tags=None, q=(), qb=(), dots=(), bdots=(), nums=(), arcs=(), shade=None, label=True, scale=1.0, tagcol=None):
    """A keyboard that asks: '?' on the key to find (q white indices, qb black keys right of white i), red dots, numbered
    circles on keys (nums: ('w'|'b', i, text, red)), hop arcs above the keys (arcs: (x0, x1) in key units: white i = i + .5,
    black right of i = i + 1), landmark name tags under the keys (tags: {white index: name})."""
    BH = H * 0.6; m = []
    for i in dots: m.append(f'<circle cx="{_wpos(i, W)}" cy="{H - 30}" r="{min(10, W * .3):.1f}" fill="{RED}"/>')
    for i in bdots: m.append(f'<circle cx="{_bpos(i, W)}" cy="{BH - 14}" r="{min(9, W * .26):.1f}" fill="{RED}"/>')
    def bubble(x, y, t, red, r=None):
        r = r or min(12, W * .36)
        return (f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="{RED if red else "#fff"}" stroke="{RED if red else NAV}" stroke-width="2"/>'
                f'<text x="{x}" y="{y + r * .42:.1f}" text-anchor="middle" font-family="AH,Arial" font-size="{r * 1.15:.1f}" font-weight="700" fill="{"#fff" if red else NAV}">{t}</text>')
    for i in q: m.append(f'<rect x="{i * W + 2}" y="{H - 20}" width="{W - 4}" height="17" fill="{(shade or {}).get(i, "#fff")}"/>' + bubble(_wpos(i, W), H - 32, '?', True))
    for i in qb: m.append(bubble(_bpos(i, W), BH - 16, '?', True))
    for kind, i, t, red in nums: m.append(bubble(_wpos(i, W) if kind == 'w' else _bpos(i, W), (H - 32) if kind == 'w' else (BH - 16), t, red, min(10, W * .3)))
    top = 0
    for k, (a, b) in enumerate(arcs):   # one hop each: a small hump above the keys
        x0, x1 = a * W, b * W; h = 16; top = 24
        m.append(f'<path d="M{x0 + 3:.1f},-3 Q{(x0 + x1) / 2:.1f},{-3 - 2 * h} {x1 - 3:.1f},-3" fill="none" stroke="{RED}" stroke-width="2.4" stroke-linecap="round"/>'
                 f'<text x="{(x0 + x1) / 2:.1f}" y="{-6 - h:.1f}" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" fill="{RED}">{k + 1}</text>')
    bot = 0
    if tags:
        bot = 26
        for i, t in tags.items():
            x = _wpos(i, W); col = (tagcol or {}).get(i, RED)
            m.append(f'<path d="M{x},{H + 3} v7" stroke="{col}" stroke-width="2"/><text x="{x}" y="{H + 23}" text-anchor="middle" font-family="AH,Arial" font-size="12.5" font-weight="700" fill="{col}">{t}</text>')
    s = keyboard(start, n, W, H, shade=shade, marks=m, label=label, scale=1)
    vb = _re.search(r'viewBox="(-?[\d.]+) (-?[\d.]+) ([\d.]+) ([\d.]+)" style="([^"]*)height:(\d+)px', s)
    w0, h0 = float(vb.group(3)), float(vb.group(4)); pad = 60 if tags else 4   # tags may run past the ends
    nh = h0 + top + bot
    s = s.replace(vb.group(0), f'viewBox="{float(vb.group(1)) - pad / 2} {-2 - top} {w0 + pad} {nh}" style="{vb.group(5)}height:{nh * scale:.0f}px')
    return s

def ask(html, ids=(), hide=False):   # her 7 Nov: the Example asks, the result line answers: '?' under the target notes, other labels kept (or all hidden)
    def one(m):
        nid = m.group(1); head = m.group(0)[:m.start(2) - m.start(0)]; tail = m.group(0)[m.end(2) - m.start(0):]
        if nid in ids: return head.replace('<tspan font-size', '<tspan fill="#e4572e" font-size') + '?' + tail
        return head + ('' if hide else m.group(2)) + tail
    return _re.sub(r'<g id="([^"]+)" class="note"(?:(?!<g id="[^"]+" class="note").)*?<tspan font-size="\d+px">([^<]*)</tspan>', one, html, flags=_re.S)
def kq(*a, **k): return '<figure class="vx kbf">' + qkb(*a, **k) + '</figure>'
def hops(start_i, black_first, n):
    """arcs for n hops up from white key start_i: walk white/black keys in order (black only where one exists)."""
    seq = []; i = start_i
    pos = _wpos(i, 1)
    keys = []
    for j in range(start_i, start_i + 12):
        keys.append(j + 0.5)
        if _WH[j % 7] in 'CDFGA': keys.append(j + 1)
    return [(keys[k], keys[k + 1]) for k in range(n)]
def rule(t): return f'<div class="secret1" style="margin:8px 0"><span class="sl">The rule</span><span>{t}</span></div>'
def cards(items, cols=3):
    return f'<div class="pcards" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(f'<div><div class="pcf">{f}</div><b>{t}</b><span>{d}</span></div>' for f, t, d in items) + '</div>'
css += """
.pcards{display:grid;gap:12px;margin:8px 0 10px} .pcards>div{border:1.5px solid #e3e1ee;border-radius:9px;padding:9px 10px 10px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:3px}
.pcards .pcf{width:100%} .pcards .pcf svg{max-width:100%;height:auto} .pcards b{font-size:14.5px;color:#26296b} .pcards span{font-size:12.5px;line-height:1.35;color:#4a4d86}
"""

# ---------- 1 The keyboard ----------
g15 = black_groups('C', 15)
def hero_families():   # her 7 Nov: C and F are the two axes; every white key belongs to the two-group (C D E) or the three-group (F G A B)
    W, H = 72, 210
    marks = [f'<circle cx="{i * W + W / 2}" cy="{H - 52}" r="15" fill="{RED}"/>' for i in (0, 3)]
    marks += [f'<text x="{W * 1.5}" y="-14" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="{RED}">the two</text>', f'<text x="{W * 5}" y="-14" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="{NAV}">the three</text>']
    s = keyboard('C', 7, W, H, label=True, shade={0: '#fbd0c2', 1: '#fdeee8', 2: '#fdeee8', 3: '#cfd4ee', 4: BLUE, 5: BLUE, 6: BLUE}, marks=marks,
                 brackets=[(0, 2, 'C starts the two: C D E', True), (3, 6, 'F starts the three: F G A B', False)], scale=1.0)
    return s.replace('viewBox="-2 -2 ', 'viewBox="-2 -34 ', 1).replace(f'height:{H + 34:.0f}px', f'height:{H + 66:.0f}px', 1).replace(f'{7 * W + 4} {H + 36}', f'{7 * W + 4} {H + 68}', 1)
P22 = ppage(f"""{head('Part I · Pitch · 1', 'The keyboard', 'Left is <b>low</b>, right is <b>high</b>. The black keys come in groups of <b>two</b> and <b>three</b>. Each group has a first white key, just to its left: <b>C</b> for the two, <b>F</b> for the three. Find the group, find its first key, then walk on.')}
{hero(hero_families(), 'Two black keys: C D E · three black keys: F G A B')}
{rule('<b>Find the group, then its first key.</b> Looking for D or E? Find two black keys and start on C. Looking for G, A or B? Find three black keys and start on F. You never have to count from far away.')}
{two(h3('Seven letters, two families') + '<p>The white keys use seven letters, <b>A B C D E F G</b>, then start again, like the days of the week. They live in two families: <b>C D E</b> round the two black keys, <b>F G A B</b> round the three.</p>',
     h3('The five Cs have names') + '<p>The C nearest the middle is <b>Middle C</b>. The Cs either side are <b>Bass C</b> and <b>Treble C</b>; further out, <b>Low C</b> and <b>High C</b>. From one C to the next is an <b>octave</b>: C D E F G A B C, eight notes, both Cs included.</p>')}
{hero(qkb('C', 29, 21, 92, label=False, dots=(0, 7, 14, 21, 28), tags={0: 'Low C', 7: 'Bass C', 14: 'Middle C', 21: 'Treble C', 28: 'High C'}, tagcol={14: RED, 0: NAV, 7: NAV, 21: NAV, 28: NAV}))}
<!--SPLIT-->
{inaction('Find G', kq('C', 15, 32, 78, q=(11,), dots=(10,)), ['<b>Which family?</b> G is in F G A B: look for <b>three</b> black keys.', '<b>Find its first key:</b> F, just left of the three (the red dot).', '<b>Walk on one key.</b> That is the <b>?</b>.'], 'The <b>?</b> is <b>G</b>: the key after F. No need to start from C and count five.')}
{inaction('Find E', kq('C', 15, 32, 78, q=(9,), dots=(7,)), ['<b>Which family?</b> E is in C D E: look for <b>two</b> black keys.', '<b>Find its first key:</b> C, just left of the two (the red dot).', '<b>Walk on:</b> C, D … the third key is the <b>?</b>.'], 'The <b>?</b> is <b>E</b>: the last of the C D E family, just right of the two black keys.')}
{inaction('Find B', kq('C', 15, 32, 78, q=(6,), dots=(3,)), ['<b>Which family?</b> B is in F G A B: three black keys.', '<b>Start on F</b> (the red dot).', '<b>Walk on:</b> F, G, A … the last key of the family is the <b>?</b>.'], 'The <b>?</b> is <b>B</b>: the last of F G A B, just right of the three black keys.')}
{inaction('Find the A below Middle C', kq('C', 15, 30, 56, tags={7: 'Middle C'}, q=(5,), shade={7: '#fbd0c2'}), ['<b>Which family?</b> A is in F G A B.', '<b>From Middle C, look left</b> for the nearest three black keys, and start on their F.', '<b>Walk on:</b> F, G … the third key is the <b>?</b>.'], 'The <b>?</b> is <b>A</b>: F, G, A. Find the family first, and every key is at most three steps away.')}
{game('Name the key', '<div class="gm4" style="grid-template-columns:repeat(3,1fr)">' + ''.join(f'<div>{kbx("C", 8, 22, 64, label=False, marks=[f"<circle cx=\"{x}\" cy=\"{y}\" r=\"7\" fill=\"#e4572e\"/>"], scale=1.0)}<b>{n}</b></div>' for n, x, y in (('1', 22 * 1.5, 50), ('2', 22 * 5.5, 50), ('3', 22 * 3.5, 50))) + '</div>', 'Find the group, then its first key, then walk on. Name each red key.', '1 D (C, then D) · 2 A (F, G, A) · 3 F (the first of the three).')}
{game('Which family?', qitems(['D', 'A', 'F', 'E', 'B', 'G'], 6), 'Does each white key live with the <b>two</b> black keys (start on C) or the <b>three</b> (start on F)?', '1 two · 2 three · 3 three (the first) · 4 two (the last) · 5 three (the last) · 6 three.')}
<!--SPLIT-->
{inaction('Find Bass C and Treble C', kq('C', 15, 32, 94, tags={7: 'Middle C'}, q=(0, 14), shade={7: '#fbd0c2'}), ['<b>Start on Middle C.</b>', '<b>Walk left</b> to the next pair of black keys. The C just left of it is one <b>?</b>.', '<b>Walk right</b> the same way, to the next pair: the other <b>?</b>.'], 'Left <b>?</b>: <b>Bass C</b>. Right <b>?</b>: <b>Treble C</b>. Each is one octave, eight notes, from Middle C.')}
{youknow('Hot Cross Buns, on three black keys', kq('E', 5, 52, 130, label=False, nums=(('b', 1, 1, True), ('b', 2, 2, True), ('b', 3, 3, True))), 'Play the group of three black keys from the top: <b class="co">3 2 1</b>, 3 2 1, then 1 1 1 1, 2 2 2 2, 3 2 1. You just played a whole tune without one white key.', 'Find another group of three, higher up, and play it again there.')}
{inaction('Higher or lower?', kq('C', 15, 30, 84, dots=(4, 9), tags={4: 'first', 9: 'second'}, tagcol={4: NAV, 9: NAV}), ['<b>Find the two red keys.</b>', '<b>Which one is further right?</b>', '<b>Right means higher:</b> play both and listen.'], 'The second note is <b>higher</b>: it is to the right. Left is always lower, right always higher.')}
{watch(['Counting every key from C: find the nearest group and start from its C or F.', 'Mixing up the families: C is left of the <b>two</b> black keys, F left of the <b>three</b>.'])}
{thinkt('The black keys are bumps you can feel in the dark. Close your eyes and slide your hand along: two bumps, and the key to their left is C; three bumps, and the key to their left is F.')}
{try10(qkb('C', 8, 24, 70, dots=(0, 3), scale=1.0), 'Play every C, then every F.', 'Bottom to top, saying the names: Low C, Bass C, Middle C, Treble C, High C. Then every F: left of the three.')}
{foot('The staff and the clefs p. {{P2}} · The staff and the keyboard p. {{P4}}', 'Workbook Pitch 1 · Online: Library › Keyboard')}""", 22)

# ---------- 2 The staff and the clefs ----------
P23 = ppage(f"""{head('Part I · Pitch · 2', 'The staff and the clefs', 'Music is written on a <b>staff</b>: five lines and four spaces, counted from the <b>bottom</b>. Higher on the staff means higher on the keyboard. The <b>clef</b> at the start is the key to the code: it names one line, and every other note follows from it.')}
{hero(pxh('hero_clef', ('n2', 'n5'), 200), 'The treble clef curls round G · the bass clef’s dots hug F')}
{two(h3('The grand staff') + '<p>Piano music uses two staves joined by a brace: the <b>treble</b> staff on top, usually for the right hand, and the <b>bass</b> staff below, usually for the left. <b>Middle C</b> sits between them on a short line of its own, and can be written in either staff.</p>', px('gs_c', 104, 'Middle C in the treble staff (left) and in the bass staff (right): the same key.'), '1fr 1fr')}
{h3('Ledger lines: the staff carried on')}
{two(px('ledger', 84, 'Treble: A, B, C below; A, B, C above.'), px('ledger_b', 84, 'Bass: E, D, C below; C, D, E above.'))}
<p>Notes too high or too low for the staff sit on short extra lines called <b>ledger lines</b>, spaced exactly like the staff lines. Read them by stepping on from the nearest staff line: line, space, line, space.</p>
<!--SPLIT-->
{inaction('One line, two notes', '<div style="display:flex;justify-content:center;gap:40px">' + ask(ykfig('tr_lines', ('n1',), 96), ('n1',), True) + ask(ykfig('bs_lines', ('n1',), 96), ('n1',), True) + '</div>', ['<b>Look at the red notes:</b> both sit on the bottom line.', '<b>Now look at the clefs:</b> treble on the left, bass on the right.', '<b>Read each from its clef note:</b> treble G is line 2, so step down (F in the space) to line 1; bass F is line 4, so step down line by line.'], 'Treble bottom line: <b>E</b>. Bass bottom line: <b>G</b>. Same line, different note: always read the <b>clef</b> first.')}
{inaction('Which staff is this key written on?', kq('C', 15, 32, 98, tags={7: 'Middle C'}, q=(3,), shade={i: (BLUE if i < 7 else '#fdeee8') for i in range(15)}), ['<b>Find Middle C.</b>', '<b>Is the ? to its left or right?</b> Left is lower: the blue half.', '<b>Low keys go on the bass staff</b>, high keys on the treble staff.'], 'The <b>?</b> is below Middle C, so it is written on the <b>bass staff</b>, usually for the left hand.')}
{youknow('Twinkle, Twinkle, Little Star', ykfig('yk_twk', ('n3','n4','n7'), 74), 'The treble clef curls round <b class="co">line 2: G</b>, the very note Twinkle leaps up to. Middle C hangs on its own ledger line below.', 'Point to the G line, then play C C G G A A G.')}
{watch(['Reading bass-clef notes as if they were treble: check the clef on every line.', 'Reading ledger lines from the wrong end: start at the staff and step outwards.'])}
<!--SPLIT-->
{inaction('Read a high note on ledger lines', ask(ykfig('ex_hi', ('n5',), 100), ('n5',)), ['<b>The top line</b> of the treble staff is F.', '<b>Step up</b> one note at a time: G sits on top of the staff, A on the first ledger line.', '<b>Keep stepping</b> to the red note: B above it, then the second ledger line.'], 'Two ledger lines above the treble staff: <b>High C</b>, two octaves above Middle C.')}
<div class="two" style="grid-template-columns:1.2fr 1fr"><div>{h3('8va: play it an octave higher')}<p>Lots of ledger lines are hard to read. So a very high passage is written on the staff with <b>8va</b> and a dotted line above it: play those notes <b>one octave higher</b>, eight notes up, until the dotted line stops. <b>8vb</b> under the staff means an octave lower.</p></div><div>{thinkt('A clef is a pair of glasses: the same five lines read as different notes, depending on which pair you put on.')}</div></div>
{game('Treble or bass?', qitems(['the E above Middle C', 'the lowest key on the piano', 'Middle C', 'High C'], 4), 'Which staff would each note be written on?', '1 treble · 2 bass, with ledger lines · 3 either: it sits between the two · 4 treble, two ledger lines up.')}
{try10(px('gs_c', 100), 'Point, then play.', 'Point to the line the treble clef curls round and play that G. Point to the line between the bass clef’s dots and play that F. Middle C sits between them.')}
{foot('Reading the notes p. {{P3}} · The staff and the keyboard p. {{P4}}', 'Workbook Pitch 2 · Online: Library › Staff and clefs')}""", 23)

# ---------- 3 Reading the notes ----------
P24 = ppage(f"""{head('Part I · Pitch · 3', 'Reading the notes', 'Every line and space has one letter. You do not have to learn them all at once: start from a note you always know, then <b>step</b> or <b>skip</b> to the one you want.')}
{hero(pxh('hero_lm', ('n3', 'n6', 'n9'), 214), 'Three notes you always know: bass F, Middle C, treble G')}
{rule('<b>Step</b>: to the very next line or space (one letter on). <b>Skip</b>: line to the next line, or space to the next space (two letters on).')}
{two(px('tr_lines', 92, 'Treble lines, E G B D F: <i>Every Good Boy Deserves Fun</i>'), px('tr_spaces', 92, 'Treble spaces, F A C E: they spell <i>FACE</i>'))}
{two(px('bs_lines', 92, 'Bass lines, G B D F A: <i>Great Big Dragons Fly Away</i>'), px('bs_spaces', 92, 'Bass spaces, A C E G: <i>All Cows Eat Grass</i>'))}
<!--SPLIT-->
{inaction('Read a note you are not sure of', ask(px('ia_read', 84), (), True), ['<b>The clef:</b> treble, so the clef note is G, on line 2.', '<b>From G, skip up</b> line to line: one letter jumped each time.', '<b>Count the skips</b> up to the other red note, on line 4: G, then B, then …'], 'The red note is <b>D</b>: G, B, D, two skips up from the clef’s G.')}
{inaction('Read a bass note from the clef', ask(ykfig('ex_bf', ('n3',), 88), ('n3',)), ['<b>The bass clef’s dots</b> sit either side of line 4: that line is F.', '<b>Step down</b> to the space below.', '<b>One more step down</b> to the red note on line 3.'], 'F, E, <b>D</b>: bass line 3 is D, two steps down from the clef’s F.')}
{youknow('Mary Had a Little Lamb', ykfig('yk_mary', ('n1','n2','n3'), 96), 'E D C: <b class="co">line, space, ledger line</b>, one step down each time. Read the shape and the tune walks down with it.', 'Read the notes aloud before you play them.')}
<!--SPLIT-->
{inaction('Find Treble C on the staff', ask(ykfig('tr_spaces', ('n3',), 88), ('n3',), True), ['<b>These notes sit in the spaces.</b> The bottom space is F.', '<b>Step up through the spaces:</b> F, A … they spell a word.', '<b>The red note is space 3.</b> Which letter is it?'], 'F A <b>C</b> E: space 3 is <b>C</b>, Treble C, the same C you found on the keyboard, one octave above Middle C.')}
{inaction('Find Bass C on the staff', ask(ykfig('bs_spaces', ('n2',), 88), ('n2',), True), ['<b>These notes sit in the bass spaces.</b> The bottom space is A: <i>All</i>.', '<b>Say the next word:</b> <i>All Cows</i> …', '<b>The red note is space 2.</b> Which letter?'], 'A <b>C</b> E G: space 2 of the bass staff is <b>C</b>, Bass C, one octave below Middle C.')}
{watch(['Naming bass notes with treble names: in the bass, the bottom line is G, not E.', 'Mixing up step and skip: a step changes line to space; a skip stays on lines (or on spaces).'])}
{thinkt('The clef notes are lamp posts on a dark road: walk from the nearest one and you are never lost.')}
{game('Name it from the clef note', qitems(['treble line 3', 'treble space 1', 'bass line 3', 'bass space 3'], 4), 'Start from the clef note (treble G on line 2, bass F on line 4), then step or skip.', '1 B (skip up from G) · 2 F (step down from G) · 3 D (two steps down from F) · 4 E (step down from F).')}
{try10(px('tr_lines', 64), 'Say the treble lines up and down.', '“E G B D F”, then “F D B G E”, out loud, as fast as you can without a slip. Then the spaces: “F A C E”.')}
{foot('The staff and the clefs p. {{P2}} · The staff and the keyboard p. {{P4}}', 'Workbook Pitch 2 · Online: Library › Staff and clefs')}""", 24)

# ---------- 4 The staff and the keyboard ----------
P25 = ppage(f"""{head('Part I · Pitch · 4', 'The staff and the keyboard', 'Each line and each space of the grand staff is one white key. Climb the staff and you climb the keyboard: here are two octaves, from Bass C to Treble C, with Middle C in red where the two staves meet.')}
<figure class="vx px mapf"><div class="vs">{P['map'].replace('<svg ', '<svg style="max-height:620px" ', 1)}</div></figure>
<p>Middle C can be written in either staff: on a ledger line below the treble staff, or above the bass staff. Same key; the hand that plays it chooses.</p>
{rule('One step on the staff (line to space, or space to line) is the very next <b>white</b> key. The black keys sit in between; how they are written is the next chapter (p.&nbsp;{{P5}}).')}
<!--SPLIT-->
{inaction('From the page to the key', px('lm_b', 84), ['<b>Name the note:</b> line 4 of the bass staff, between the clef’s dots, is F.', '<b>On the piano,</b> find the three black keys just below Middle C.', '<b>F is the first key</b> of that family: play it with the left hand.'], 'The bass-clef F is the <b>F just below Middle C</b>: left of the three black keys under it.')}
{inaction('Mirror notes either side of Middle C', '<div style="width:70%;margin:0 auto">' + ask(px('landmarks', 220), ('n3', 'n4')) + '</div>', ['<b>Treble G:</b> the three black keys just above Middle C; G is the second key, after F.', '<b>Bass F:</b> the three black keys just below Middle C; F is the first key.', '<b>Now count each from Middle C:</b> C D E F G up, C B A G F down. Which number?'], 'Both are <b>note 5</b>: treble G and bass F are mirror images, the same distance either side of Middle C.')}
{youknow('Frère Jacques, in both hands', ykfig('yk_frere', ('n5','n6','n7','n8'), 150), 'The left hand plays the <b class="co">same letters</b>, C D E C, one octave lower, written in the bass clef.', 'Play it right hand, then left hand, then both together.')}
<!--SPLIT-->
{inaction('From the key to the page', kq('C', 8, 40, 100, tags={0: 'Middle C'}, q=(2,), shade={0: '#fbd0c2'}), ['<b>Find the ? key:</b> count up from Middle C, C 1, D 2 …', '<b>Do the same on the staff:</b> Middle C on its ledger line, D in the space under the staff …', '<b>Where do you land?</b>'], 'The <b>?</b> is <b>E</b>, note 3, and it sits on the <b>bottom line</b> of the treble staff.')}
{watch(['Skipping a key: every line and every space is used, one white key each.', 'Counting from 0: the note you start on is note 1.'])}
{thinkt('The staff is a ladder laid beside the keyboard: each rung, a line or a space, is the next white key.')}
{game('Count the notes', qitems(['Middle C up to A', 'Middle C down to E', 'G up to the next G'], 3), 'Count the notes, both ends included. The staff climbs the same way: one line or space per note.', '1 six (C D E F G A) · 2 six (C B A G F E) · 3 eight: an octave.')}
{try10(kbx('C', 8, 24, 70, label=True, shade={0: PINK, 7: PINK}, scale=1.0), 'Play Middle C, then walk up.', 'Say each white key as you play it, C D E F G A B C, and picture each one climbing the staff: line, space, line, space.')}
{foot('The keyboard p. {{P1}} · Reading the notes p. {{P3}}', 'Workbook Pitch 1–2 · Online: Library › Staff and clefs')}""", 25)

# ---------- 5 Sharps, flats and naturals ----------
acc = [[gsym('♯', 28), 'sharp', 'one key to the right (a semitone higher)', 'Level 0'], [gsym('♭', 28), 'flat', 'one key to the left (a semitone lower)', 'Level 0'], [gsym('♮', 28), 'natural', 'cancels a sharp or flat: back to the white key', 'Level ½']]
P26 = ppage(f"""{head('Part I · Pitch · 5', 'Sharps, flats and naturals', 'A sign in front of a note moves it to the very next key. <b>Sharp</b>: one key to the <b>right</b>. <b>Flat</b>: one key to the <b>left</b>. Usually that next key is black, which is how the black keys get their names.')}
{hero(keyboard('C', 5, 64, 190, label=True, shade={1: BLUE}, marks=[f'<circle cx="{1.5 * 64}" cy="150" r="13" fill="#fff" stroke="{NAV}" stroke-width="2.4"/>', f'<circle cx="{2 * 64}" cy="72" r="13" fill="{RED}"/>', f'<circle cx="{1 * 64}" cy="72" r="13" fill="{RED}"/>', f'<text x="{2 * 64}" y="40" text-anchor="middle" font-family="AH,Arial" font-size="17" font-weight="700" fill="#fff">D♯</text>', f'<text x="{1 * 64}" y="40" text-anchor="middle" font-family="AH,Arial" font-size="17" font-weight="700" fill="#fff">D♭</text>', f'<path d="M{1.5 * 64 + 8},132 Q{1.75 * 64},100 {2 * 64 - 4},90" fill="none" stroke="{RED}" stroke-width="3.5" stroke-linecap="round" marker-end="url(#ah)"/>', f'<path d="M{1.5 * 64 - 8},132 Q{1.25 * 64},100 {1 * 64 + 4},90" fill="none" stroke="{RED}" stroke-width="3.5" stroke-linecap="round" marker-end="url(#ah)"/>', f'<defs><marker id="ah" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker></defs>'], scale=1.0), '♯ one key right · ♭ one key left')}
{tbl(['Sign', 'Name', 'What it does', 'First met'], acc, ['12%', '20%', '50%', '18%'])}
<!--SPLIT-->
{inaction('Find F♯', kq('C', 8, 40, 96, qb=(3,), dots=(3,)), ['<b>Find F</b> (the red dot): just left of the three black keys.', '<b>Sharp means right:</b> move to the very next key.', '<b>Is it black or white?</b> Put your finger on it.'], 'The <b>?</b> is <b>F♯</b>: the first black key of the group of three.')}
{inaction('Find B♭', kq('C', 8, 40, 96, qb=(5,), dots=(6,)), ['<b>Find B</b> (the red dot): just right of the three black keys.', '<b>Flat means left:</b> move to the very next key.', '<b>Which black key is it?</b>'], 'The <b>?</b> is <b>B♭</b>: the top black key of the group of three.')}
{inaction('How long does the sharp last?', ask(px('acc_bar', 84), ('n2', 'n4', 'n5')), ['<b>The first note</b> has a sharp: F♯.', '<b>Later in the same bar</b> there is no sign. Is it still sharp?', '<b>After the bar line</b>: is it still sharp?'], 'Still <b>F♯</b> until the bar line; after it, plain <b>F</b> again. A sign lasts <b>to the end of its bar</b>.')}
<!--SPLIT-->
{inaction('A natural cancels the flat', ask(px('acc_nat', 88), ('n4',)), ['<b>B</b>: the white key.', '<b>B♭</b>: one key left, and it stays flat for the rest of the bar.', '<b>The last note</b> has a natural sign: what does it do?'], 'The natural <b>cancels</b> the flat: back to the white key B, until the bar line.')}
{inaction('One key, two names', ask(px('enh', 84), ('n6',)), ['<b>The first bar:</b> F♯, then G♭. Find both on the keyboard.', '<b>Are they different keys?</b>', '<b>The last bar:</b> E♯. Which key is one right of E?'], 'F♯ and G♭ are the <b>same black key</b>; E♯ is the white key <b>F</b>. Same sound, different names: <b>enharmonic</b>.')}
{youknow('Für Elise (Beethoven)', ykfig('yk_elise', ('n2','n4'), 72), 'E, <b class="co">D♯</b>, E, <b class="co">D♯</b>: the very next key down and back. The sharp is written again in the new bar, because the bar line wiped it out.', 'Play E and D♯ back and forth: the black key just left of E.')}
{watch(['Carrying a sharp or flat past the bar line: after it, the note is plain again.'])}
{thinkt('A sharp or flat is a sticky note on one line of the staff: it stays stuck until the bar line, then it falls off.')}
{game('Which key is it?', qitems(['C♯', 'E♭', 'B♯', 'F♭'], 4), 'Sharp: one key to the right. Flat: one key to the left. Which key do you press?', '1 the black key right of C · 2 the black key left of E · 3 the white key C · 4 the white key E.')}
{foot('Keys and key signatures p. {{S3}}', 'Workbook Pitch 3 · Online: Library › Signs')}""", 26)

# ---------- 6 Counting intervals ----------
def hopkb(start, n_white, W, H, a, nh, label=True, ends=True, scale=1.0, cap=None):
    """count the hops: from white key a, nh hops up (every key, black and white), arcs numbered 1..nh, both end keys red."""
    seq = []
    for j in range(a, a + 14):
        seq.append(('w', j))
        if _WH[(_WH.index(start) + j) % 7] in 'CDFGA': seq.append(('b', j))
    t, j = seq[nh]; shade = {a: '#f6c2b0'}
    for tt, jj in seq[1:nh]:
        if tt == 'w': shade[jj] = '#fdf1ec'
    if t == 'w': shade[j] = '#f6c2b0'
    nums = [(tt, jj, k + 1, k + 1 == nh) for k, (tt, jj) in enumerate(seq[1:nh + 1])]
    s = qkb(start, n_white, W, H, nums=nums, shade=shade, label=label, scale=scale, tags={a: 'start'}, tagcol={a: NAV})
    if t == 'b':   # the black end key in red
        BW, BH = W * 0.58, H * 0.6; x = (j + 1) * W - BW / 2
        s = s.replace('<circle', f'<rect x="{x:.1f}" y="0" width="{BW:.1f}" height="{BH:.1f}" rx="1.5" fill="#f3a48c"/><circle', 1)
    return s
P27 = ppage(f"""{head('Part I · Pitch · 6', 'Counting intervals', 'How far apart are two notes? That distance is an <b>interval</b>. To give it a number, <b>count the notes</b>: the first note is 1, and you count every letter up to the second, both ends included.')}
{hero(hero_third(), 'C to E: count the notes, 1 2 3: a 3rd')}
{rule('<b>Count the notes</b> for the number: start at 1 on the first note. C to E is C D E: 3 notes, a <b>3rd</b>. Sharps and flats never change the number.')}
{h3('Interval numbers from C')}
{px('intv', 92)}
{inaction('How far apart are these notes?', px('ia_iv', 92), ['<b>Call the first note 1:</b> here F is 1.', '<b>Count every letter</b> up to the second note.', '<b>Going down works the same:</b> start at 1 on the top note and count down.'], 'F G A is 3 notes: a <b>3rd</b>. C B A G is 4 notes: a <b>4th</b>.')}
<!--SPLIT-->
{h3('The smallest steps: semitones and tones')}
{two(px('tones', 84, 'E–F and B–C: no black key between, a semitone. C–D and F–G: a black key between, a tone.'), '<p>From any key to the <b>very next key</b>, black or white, is a <b>semitone</b>: the smallest step on the piano. Two semitones make a <b>tone</b>. On the white keys most steps are tones, but <b>E–F</b> and <b>B–C</b> have no black key between them: they are semitones.</p>', '1fr 1fr')}
{inaction('Tone or semitone?', kq('C', 8, 40, 104, dots=(2, 3)), ['<b>Look between the red keys:</b> is there a black key?', '<b>No black key</b> means they are next-door keys.', '<b>Now try C and D</b>: is there a black key between?'], 'E–F is a <b>semitone</b> (next door). C–D has C♯ between: a <b>tone</b>.')}
{youknow('Twinkle, Twinkle, Little Star', ykfig('yk_twk5', ('n1','n3'), 74), 'The leap from the first “twinkle” to the second is C up to G: C D E F G, <b class="co">five notes, a 5th</b>.', 'Sing the first two notes of any song, then count the notes between them.')}
{watch(['Counting only the gaps, not the notes: C to E is 3 notes, not 2 gaps.', 'Letting a sharp or flat change the number: C to G♯ is still a 5th.'])}
<!--SPLIT-->
{inaction('Name an interval on the keyboard', kq('C', 8, 40, 104, dots=(2, 7)), ['<b>Find both red keys:</b> E, and the C above it.', '<b>Count the notes</b> from E: E is 1 …', '<b>Stop on the C.</b> What number is it?'], 'E F G A B C is 6 notes: a <b>6th</b>.')}
{inaction('Melodic or harmonic?', px('mel_harm', 88), ['<b>The first bar:</b> C, then E, one after the other.', '<b>The second bar:</b> C and E at the same time.', '<b>Count the notes</b> in each.'], 'Both are a <b>3rd</b>: <b>melodic</b> when played one after the other, <b>harmonic</b> when played together.')}
{thinkt('Monday to Wednesday is three days, not two: you count the day you start on. Intervals count the same way.')}
{game('Count the notes', qitems(['C up to G', 'D up to F', 'E up to the next E', 'G up to A'], 4), 'Count every note, both ends included. What is each interval called?', '1 a 5th (C D E F G) · 2 a 3rd · 3 an octave (8) · 4 a 2nd.')}
{try10(kbx('C', 8, 24, 70, label=True, shade={0: PINK, 4: PINK}, scale=1.0), 'Thumb on C, finger 5 on G.', 'Your hand is a ruler: thumb to little finger on white keys is a 5th. Play it, then thumb to finger 3: a 3rd.')}
{foot('Major, minor and perfect p. {{P7}} · Major scales p. {{S1}}', 'Workbook Pitch 4 · Online: Library › Intervals')}""", 27)

# ---------- 7 Major, minor and perfect ----------
iv = [['3rd', '3 (minor)', '4 (major)'], ['4th', '', '5 (perfect)'], ['5th', '', '7 (perfect)'], ['6th', '8 (minor)', '9 (major)'], ['octave', '', '12 (perfect)']]
P28 = ppage(f"""{head('Part I · Pitch · 7', 'Major, minor and perfect', 'C to E and C to E♭ are both 3rds: three notes each. But they sound different, bright and dark. To tell them apart, <b>count the hops</b>: every move to the very next key, black or white, is one hop.')}
{hero(two(hopkb('C', 7, 40, 128, 0, 4) + '<p class="sm">C to <b class="co">E</b>: 4 hops. A <b>major</b> 3rd: bright.</p>', hopkb('C', 7, 40, 128, 0, 3) + '<p class="sm">C to <b class="co">E♭</b>: 3 hops, one fewer. A <b>minor</b> 3rd: dark.</p>'), 'One hop less: a major 3rd becomes minor')}
{rule('<b>Count the notes</b> for the number (a 3rd). <b>Count the hops</b> for the size (major or minor). Do not count the key you start on: the first move is hop 1.')}
{two(tbl(['Number', 'Smaller', 'Main size'], iv, ['30%', '35%', '35%']), '<p><b>3rds and 6ths</b> come in two sizes: <b>major</b>, and <b>minor</b>, one hop smaller.</p><p><b>4ths, 5ths and octaves</b> have one main size, called <b>perfect</b>. They are never major or minor.</p>', '1.15fr 1fr')}
<!--SPLIT-->
{inaction('Major or minor 3rd?', kq('C', 8, 40, 110, dots=(0,), bdots=(1,)), ['<b>Count the notes:</b> C D E, three letters, so it is a 3rd.', '<b>Count the hops</b> from C to the red black key, E♭: C♯ 1, D 2 …', '<b>Major has 4 hops.</b> How many here?'], 'C to E♭ is <b>3 hops</b>: a <b>minor 3rd</b>.')}
{inaction('Name F up to A', hopkb('C', 8, 40, 128, 3, 4), ['<b>Count the notes:</b> F G A is 3, so it is a 3rd.', '<b>Count the hops:</b> every key you land on, black and white, is numbered.', '<b>4 hops or 3?</b>'], 'F to A is 4 hops: a <b>major 3rd</b>, the same size as C to E.')}
{youknow('Beethoven, Symphony No. 5', ykfig('yk_b5', ('n2','n3','n4','n5'), 112), 'Da-da-da-DUM: G down to <b class="co">E♭</b> is three notes, a 3rd, and 4 hops (F♯, F, E, E♭): a <b>major 3rd</b>.', 'Count the hops from G down to E♭ on the keyboard.')}
<!--SPLIT-->
{inaction('Name D up to A', hopkb('C', 8, 40, 128, 1, 7), ['<b>The number:</b> D E F G A, five notes, a 5th.', '<b>The size:</b> count the hops: the numbered keys.', '<b>A 5th of 7 hops</b> is its main size. What is that called?'], 'D up to A is a <b>perfect 5th</b>: 7 hops.')}
{inaction('Name E up to C', hopkb('C', 8, 36, 124, 2, 8), ['<b>The number:</b> E F G A B C, six notes, a 6th.', '<b>The size:</b> count the hops.', '<b>A major 6th</b> has 9 hops. Is this one more or one fewer?'], 'E up to C is 8 hops, one fewer than major: a <b>minor 6th</b>.')}
{watch(['Counting white keys only: count every hop, black and white.', 'Counting the start key as hop 1: the first move is hop 1.', 'Calling a 4th or 5th “major”: they are perfect.'])}
{thinkt('A major and a minor 3rd are a smile and a frown: the same face, one small change at the corners.')}
{game('Perfect, major or minor?', qitems(['C–G', 'D–F', 'C–E', 'E–A'], 4), 'Count the notes for the number, then the hops for the size.', '1 perfect 5th (7 hops) · 2 minor 3rd (3) · 3 major 3rd (4) · 4 perfect 4th (5).')}
{try10(kbx('C', 8, 24, 70, label=True, shade={0: PINK, 2: PINK}, scale=1.0), 'Play C–E, then C–E♭.', 'Bright, then dark. One hop makes the difference: the major 3rd has four, the minor 3rd three.')}
{foot('Counting intervals p. {{P6}} · Chords and triads p. {{H1}}', 'Workbook Pitch 4 · Online: Library › Intervals')}""", 28)
