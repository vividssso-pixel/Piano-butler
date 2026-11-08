# The Piano Butler Handbook, Part III: Expression (her 8 Nov: "put in everything, in order; tell me when the Handbook is done").
# Loud and soft, touch, speed words, pedals, ornaments, tips. Helpers come from the Time draft (book10.py).
import json as _ej, re as _er
exec(open('/tmp/claude-0/pk/book10.py').read())   # helpers, css, page(), assemble() (rewrites the Time draft, harmless)
from openart import opener_art as _oa
EV = json.load(open('/tmp/claude-0/pk/ex/eout.json'))
def epage(inner, n): return page(inner, n, 'PART III · EXPRESSION')
def ex(k, h=80, cap='', red=()):   # an expression snippet on a real staff; red: note ids to colour
    s = EV[k].replace('<svg ', f'<svg style="max-height:{h}px" ', 1)
    for n in red:
        for c in ('note', 'rest', 'chord'): s = s.replace(f'<g id="{n}" class="{c}">', f'<g id="{n}" class="{c}" style="fill:#e4572e;color:#e4572e">', 1)
    return '<figure class="vx"><div class="vs">' + s + '</div>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>'
N_, R_ = '#26296b', '#e4572e'
def dsym(t, fs=30, col=N_): return f'<span style="font-family:PF,serif;font-style:italic;font-weight:700;font-size:{fs}px;color:{col};letter-spacing:-.02em">{t}</span>'
SECRETS.update({'E1': 'Six steps, from a whisper to a shout: pp p mp mf f ff. <b>m</b> means half.',
                'E2': 'Curve: join. Dot: short. Line: hold. Arrow: strong.',
                'E3': 'The word at the top sets the speed; rit. brakes gently, a tempo drives off again.',
                'E4': 'Play first, then change the pedal: up and straight down again.',
                'E5': 'An ornament is a necklace on the note: it borrows the next-door notes, and the main note still lands on time.'})

# ---------- heroes ----------
def hero_ladder(w=560):
    L = [('pp', 'very soft'), ('p', 'soft'), ('mp', 'half soft'), ('mf', 'half loud'), ('f', 'loud'), ('ff', 'very loud')]
    o = f'<svg viewBox="0 0 600 230" style="width:100%;max-width:{w}px;height:auto;display:block;margin:0 auto">'
    for i, (s, t) in enumerate(L):
        x = 20 + i * 96; h = 30 + i * 26; y = 150 - h; col = R_ if i in (0, 5) else ('#f08b6b' if i in (1, 4) else '#f6c2ad')
        o += f'<rect x="{x}" y="{y}" width="76" height="{h}" rx="6" fill="{col}"/>'
        o += f'<text x="{x + 38}" y="190" text-anchor="middle" font-family="PF,serif" font-style="italic" font-weight="700" font-size="34" fill="{N_}">{s}</text>'
        o += f'<text x="{x + 38}" y="216" text-anchor="middle" font-family="AH,Arial" font-size="14" fill="#5a5d8f">{t}</text>'
    return o + '<path d="M30,22 L560,22" stroke="#26296b" stroke-width="1.5" stroke-dasharray="4 4"/><text x="30" y="14" font-family="AH,Arial" font-size="13" font-weight="700" fill="#26296b">whisper</text><text x="560" y="14" text-anchor="end" font-family="AH,Arial" font-size="13" font-weight="700" fill="#26296b">shout</text></svg>'
def hero_touch():
    rows = [('Legato', 'slur: joined, no gap', [(0, 1), (1, 1), (2, 1), (3, 1)], 'slur'), ('Staccato', 'dots: short, detached', [(0, .38), (1, .38), (2, .38), (3, .38)], 'dot'),
            ('Tenuto', 'lines: full length, a slight lean', [(0, .92), (1, .92), (2, .92), (3, .92)], 'line'), ('Accent', 'arrows: a stronger start', [(0, .8), (1, .8), (2, .8), (3, .8)], 'acc')]
    o = '<svg viewBox="0 0 640 250" style="width:100%;max-width:600px;height:auto;display:block;margin:0 auto">'
    o += '<text x="250" y="16" font-family="AH,Arial" font-size="12.5" font-weight="700" fill="#5a5d8f">how long each of four notes sounds</text>'
    for r, (n, d, bars, mark) in enumerate(rows):
        y = 34 + r * 54
        o += f'<text x="0" y="{y + 18}" font-family="AH,Arial" font-size="16" font-weight="700" fill="{N_}">{n}</text><text x="0" y="{y + 36}" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">{d}</text>'
        for k, ln in bars:
            x = 250 + k * 96; hh = 26 if mark != 'acc' else 22
            if mark == 'acc':
                o += f'<path d="M{x},{y + 4} L{x + 14},{y + 4} L{x + ln * 92},{y + 16} L{x + ln * 92},{y + 26} L{x},{y + 26} Z" fill="{R_}"/>'
            else:
                o += f'<rect x="{x}" y="{y + 4}" width="{ln * 96 - (0 if mark == "slur" else 4):.0f}" height="{hh - 4}" rx="{3 if mark == "slur" else 4}" fill="{R_ if mark != "line" else "#f08b6b"}"/>'
        if mark == 'slur': o += f'<path d="M252,{y} Q442,{y - 22} 632,{y}" fill="none" stroke="{N_}" stroke-width="2"/>'
    return o + '</svg>'
def hero_dial():
    import math
    W = ['Largo', 'Adagio', 'Andante', 'Moderato', 'Allegro', 'Presto']
    o = '<svg viewBox="0 0 560 270" style="width:100%;max-width:520px;height:auto;display:block;margin:0 auto">'
    cx, cy, R = 280, 230, 190
    o += f'<path d="M{cx - R},{cy} A{R},{R} 0 0 1 {cx + R},{cy}" fill="none" stroke="#e3e1ee" stroke-width="30"/>'
    o += f'<path d="M{cx - R},{cy} A{R},{R} 0 0 1 {cx + R * math.cos(math.radians(180 - 72)):.1f},{cy - R * math.sin(math.radians(180 - 72)):.1f}" fill="none" stroke="#f6c2ad" stroke-width="30"/>'
    for i, w in enumerate(W):
        a = math.radians(180 - (i + .5) * 180 / len(W)); x = cx + (R + 34) * math.cos(a); y = cy - (R + 34) * math.sin(a)
        o += f'<text x="{x:.1f}" y="{y + 5:.1f}" text-anchor="middle" font-family="PF,serif" font-weight="700" font-size="17" fill="{R_ if w == "Andante" else N_}">{w}</text>'
        x1, y1 = cx + (R - 15) * math.cos(a), cy - (R - 15) * math.sin(a); x2, y2 = cx + (R + 15) * math.cos(a), cy - (R + 15) * math.sin(a)
        o += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#fff" stroke-width="3"/>'
    a = math.radians(180 - 2.5 * 180 / len(W))
    o += f'<line x1="{cx}" y1="{cy}" x2="{cx + (R - 30) * math.cos(a):.1f}" y2="{cy - (R - 30) * math.sin(a):.1f}" stroke="{R_}" stroke-width="6" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="13" fill="{N_}"/>'
    o += f'<text x="{cx - R}" y="{cy + 30}" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="#5a5d8f">slow</text><text x="{cx + R}" y="{cy + 30}" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="#5a5d8f">fast</text>'
    return o + '</svg>'
def pedals(q=False, w=520):
    P3 = [('soft pedal', 'una corda', 'softer, gentler'), ('middle pedal', 'sostenuto', 'holds only some notes'), ('sustain pedal', 'damper pedal', 'notes keep ringing')]
    o = f'<svg viewBox="0 0 520 220" style="width:100%;max-width:{w}px;height:auto;display:block;margin:0 auto">'
    o += '<rect x="20" y="20" width="480" height="26" rx="4" fill="#26296b"/><rect x="60" y="46" width="400" height="60" fill="#3a3d7e"/>'
    for i, (a, b, c) in enumerate(P3):
        x = 110 + i * 150; col = R_ if i == 2 else '#c9cbe0'
        o += f'<line x1="{x}" y1="106" x2="{x}" y2="120" stroke="#3a3d7e" stroke-width="6"/><path d="M{x - 26},{124} Q{x},{112} {x + 26},{124} L{x + 22},{142} Q{x},{136} {x - 22},{142} Z" fill="{col}" stroke="#26296b" stroke-width="2"/>'
        if q: o += f'<circle cx="{x}" cy="178" r="15" fill="#fff3ee" stroke="{R_}" stroke-width="2"/><text x="{x}" y="184" text-anchor="middle" font-family="AH,Arial" font-size="16" font-weight="700" fill="{R_}">?</text>'
        else: o += f'<text x="{x}" y="166" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="{R_ if i == 2 else N_}">{a}</text><text x="{x}" y="184" text-anchor="middle" font-family="AH,Arial" font-size="12.5" font-style="italic" fill="#5a5d8f">{b}</text><text x="{x}" y="202" text-anchor="middle" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">{c}</text>'
    return o + '</svg>'
def pedmarks():   # the two ways to write the sustain pedal
    o = '<svg viewBox="0 0 520 96" style="width:100%;max-width:480px;height:auto;display:block;margin:0 auto">'
    o += f'<text x="10" y="30" font-family="PF,serif" font-style="italic" font-weight="700" font-size="20" fill="{N_}">Ped.</text><path d="M62,24 H200" stroke="#9a9cc4" stroke-dasharray="5 4" stroke-width="1.5"/><text x="208" y="32" font-family="AH,Arial" font-size="24" font-weight="700" fill="{N_}">*</text>'
    o += f'<text x="10" y="58" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">down at Ped., up at the star</text>'
    o += f'<path d="M290,12 V34 H380 L392,18 L404,34 H490 V12" fill="none" stroke="{N_}" stroke-width="2.2"/>'
    o += f'<text x="290" y="58" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">a bracket: the notch is a quick change</text>'
    o += f'<text x="380" y="84" font-family="AH,Arial" font-size="12" font-weight="700" fill="{R_}">up and down again</text><line x1="392" y1="22" x2="392" y2="70" stroke="{R_}" stroke-width="1.2" stroke-dasharray="2 2"/>'
    return o + '</svg>'
def pedtime(w=520):   # keys and pedal on one timeline: the pedal changes just after each new chord
    o = f'<svg viewBox="0 0 540 120" style="width:100%;max-width:{w}px;height:auto;display:block;margin:0 auto">'
    o += f'<text x="0" y="34" font-family="AH,Arial" font-size="13" font-weight="700" fill="{N_}">hands</text><text x="0" y="88" font-family="AH,Arial" font-size="13" font-weight="700" fill="{N_}">pedal</text>'
    for i, c in enumerate(['C E G', 'F A C', 'G B D', 'C E G']):
        x = 70 + i * 116
        o += f'<rect x="{x}" y="18" width="104" height="26" rx="5" fill="#f6c2ad"/><text x="{x + 52}" y="36" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="{N_}">{c}</text>'
    d = 'M70,96 V74'
    for i in range(1, 4): x = 70 + i * 116; d += f' H{x + 6} L{x + 14},96 L{x + 22},74'
    d += ' H534 V96'
    o += f'<path d="{d}" fill="none" stroke="{R_}" stroke-width="2.6"/>'
    for i in range(1, 4): x = 70 + i * 116; o += f'<line x1="{x}" y1="46" x2="{x}" y2="70" stroke="#9a9cc4" stroke-dasharray="2 2"/>'
    return o + '<text x="300" y="116" text-anchor="middle" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">each notch comes just <tspan font-weight="700">after</tspan> the new group of notes</text></svg>'
def arrow_pair(a, b, lab=''):
    return (f'<div style="display:grid;grid-template-columns:1fr 60px 1.4fr;align-items:center;gap:6px">{a}<div style="text-align:center;font-family:CV,cursive;font-size:20px;font-weight:700;color:{R_};line-height:1">→<br><span style="font-size:15px">{lab}</span></div>{b}</div>')
def qdot(n=1): return '<span style="display:inline-flex;gap:6px">' + ''.join(f'<span style="width:30px;height:30px;border-radius:50%;background:#fff3ee;border:2px solid {R_};color:{R_};font:700 16px AH,Arial;display:inline-flex;align-items:center;justify-content:center">?</span>' for _ in range(n)) + '</span>'

# ---------- 1 · Loud and soft ----------
DYN = [[dsym('pp'), '<b>pianissimo</b>', 'very soft'], [dsym('p'), '<b>piano</b>', 'soft'], [dsym('mp'), '<b>mezzo-piano</b>', 'half soft: a little louder than <i>p</i>'],
       [dsym('mf'), '<b>mezzo-forte</b>', 'half loud: a little softer than <i>f</i>'], [dsym('f'), '<b>forte</b>', 'loud'], [dsym('ff'), '<b>fortissimo</b>', 'very loud']]
CHG = [['<svg viewBox="0 0 90 30" style="width:80px"><path d="M4,15 L86,4 M4,15 L86,26" stroke="#26296b" stroke-width="2" fill="none"/></svg>', '<b>crescendo</b> (<i>cresc.</i>)', 'getting louder, little by little'],
       ['<svg viewBox="0 0 90 30" style="width:80px"><path d="M4,4 L86,15 L4,26" stroke="#26296b" stroke-width="2" fill="none"/></svg>', '<b>diminuendo</b> (<i>dim.</i>, <i>decresc.</i>)', 'getting softer, little by little'],
       [dsym('sfz', 24) + ' / ' + dsym('sf', 24), '<b>sforzando</b>', 'one note made suddenly strong'], [dsym('fp', 24), '<b>forte-piano</b>', 'loud, then soft at once'], ['<i>subito p</i>', '<b>subito</b>', '“suddenly”: <i>subito p</i>, suddenly soft']]
E1 = epage(f'''{head('Part III · Expression · 1', 'Loud and soft', 'A voice can whisper, chat or shout. Music does the same, and small Italian words tell you which: the <b>dynamics</b>. They sit under the notes, shortened to one or two letters.')}
{hero(hero_ladder(), 'Six steps from a whisper to a shout')}
{tbl(['Sign', 'Say it', 'How it sounds'], DYN, ['16%', '30%', '54%'], 'nt')}
{rule('<b>p</b> is soft, <b>f</b> is loud; <b>m</b> (mezzo) means half; a second letter means very. A sign lasts until the next one.')}
<!--SPLIT-->
{h3('Growing and fading')}
{two(ex('e_tw_hair', 86, 'A hairpin that opens grows louder; one that closes fades. From <i>p</i> to <i>f</i> and back.'), ex('e_words', 86, 'The same idea in words: <i>cresc.</i> and dashes, then <i>ff</i>.'))}
{tbl(['Sign', 'Name', 'What you do'], CHG, ['22%', '34%', '44%'])}
{inact('Which is louder: mp or mf?', qtagT('<div style="display:flex;gap:34px;align-items:baseline;justify-content:center">' + dsym('mp', 44) + dsym('mf', 44) + '</div>'), ['<b>m means half.</b> Half of what?', '<b>p is soft, f is loud.</b>', '<b>So which half</b> is louder?'], '<b>mf</b>, half loud, is louder than <b>mp</b>, half soft. Both sit in the middle of the ladder.')}
{inact('What happens across the hairpins?', qtagT(ex('e_tw_hair', 80)), ['<b>Find the start:</b> which sign?', '<b>The first hairpin opens</b> to which sign?', '<b>The second hairpin closes.</b> What happens?'], 'Start <i>p</i>, grow through bar 1 into <i>f</i>, then <b>fade</b> through bar 2.')}
{inact('Where is the loudest note?', qtagT(ex('e_tw_q', 80)), ['<b>Start:</b> <i>mp</i>.', '<b>Follow the hairpin</b> to its sign.', '<b>Then the long hairpin closes</b> to which sign?'], 'The <b>first A in bar 2</b>, at <i>f</i>. From the next note the tune fades all the way to <i>p</i>.')}
{youknow('Haydn’s “Surprise” Symphony', ex('y_surprise', 70, red=('n1',)), 'The tune tiptoes along softly, then comes again even softer, <i>pp</i>. Just as everyone relaxes, the whole orchestra crashes in with one <b class="co">ff</b> chord: the surprise that gave the symphony its name.', 'Hum it very softly, then clap once, as loud as you can.')}
{game('Soft to loud', qitems([dsym('mf', 24), dsym('pp', 24), dsym('f', 24), dsym('p', 24), dsym('ff', 24), dsym('mp', 24)], 6), 'Put the six signs in order from the softest to the loudest.', 'pp · p · mp · mf · f · ff.')}
{try10('<div style="text-align:center">' + dsym('pp', 30) + ' <span style="font:700 22px CV;color:#e4572e">→</span> ' + dsym('ff', 30) + '</div>', 'One note, six ways.', 'Play Middle C <i>pp</i>, then <i>p</i>, <i>mp</i>, <i>mf</i>, <i>f</i>, <i>ff</i>. Six different steps? Then come back down.')}
{thinkt('Dynamics are a volume knob with six clicks. Turn it with the weight of your arm, not by hitting harder.')}
{watch(['Playing everything <i>mf</i>: each sign is a different step.', 'Speeding up in a crescendo: louder is not faster.'])}
{howto('Practise a crescendo', ['<b>Play five notes up</b>, C to G, all <i>p</i>.', '<b>Now grow</b> one step on each note: <i>p</i> to <i>f</i>.', '<b>Come back down</b> the same notes, fading to <i>p</i>, without slowing down.'])}
{foot('Touch p. {{E2}} · Pulse and tempo p. {{T1}}', 'Online: Library › Dynamics')}''', 72)

# ---------- 2 · Touch ----------
MARKS = [['<span style="font-size:26px;color:#26296b">⌒</span>', '<b>slur</b> (<i>legato</i>)', 'join the notes smoothly, no gap'], ['<span style="font-size:30px;color:#26296b;line-height:.5">•</span>', '<b>staccato</b>', 'short and detached: let go early'],
         ['<span style="font-size:22px;font-weight:700;color:#26296b">—</span>', '<b>tenuto</b>', 'hold the full length, leaning a little'], ['<span style="font-size:24px;font-weight:700;color:#26296b">&gt;</span>', '<b>accent</b>', 'a stronger start to the note'],
         ['<span style="font-size:18px;color:#26296b">▼</span>', '<b>staccatissimo</b>', 'very short ' + lv('')], ['<span style="font-size:22px;font-weight:700;color:#26296b">^</span>', '<b>marcato</b>', 'very strong, marked ' + lv('')]]
E2 = epage(f'''{head('Part III · Expression · 2', 'Touch: smooth, short, strong', 'The same four notes can sound smooth or bouncy, gentle or strong. Small marks above or below the notes tell your fingers how to touch the keys: this is <b>articulation</b>.')}
{hero(hero_touch(), 'Same notes, four touches')}
{ex('a_four', 62, 'The same four notes: slurred, staccato, tenuto, accented.')}
{tbl(['Mark', 'Name', 'How to play'], MARKS, ['14%', '32%', '54%'])}
<!--SPLIT-->
{h3('Slurs and phrases')}
{two(ex('a_legato', 74, 'Slurred: join E D C, then a tiny lift.'), ex('a_stacc', 74, 'Staccato: every E and D let go early.'))}
<p>A curve over <b>different</b> notes is a slur: join them, then lift at its end, like a breath. A long slur over a whole line of tune is a <b>phrase mark</b>: one musical sentence. (A curve joining the <b>same</b> note twice is a tie, p. {{{{T3}}}}.)</p>
{h3('Two-note slurs')}
{two(ex('a_two', 70), '<p>A slur over just two notes is a little sigh: <b>drop</b> into the first note, then <b>lift</b> off the second, lighter and a little shorter. Drop, lift.</p>')}
{inact('Which notes are short?', qtagT(ex('a_mixq', 76)), ['<b>Bar 1:</b> what does the curve ask?', '<b>Bar 2:</b> find the dots.', '<b>The last G</b> has a different mark: which?'], 'Bar 1 is joined; the <b>two dotted Gs are short</b>; the third G is accented, stronger but full length.')}
{inact('How do you play the end of a slur?', qtagT(ex('a_legato', 74, red=('n3',))), ['<b>Join E D C</b> under the first curve.', '<b>At the end of the curve:</b> hold, or lift?', '<b>The next curve</b> starts on E again.'], 'Join the notes, then <b>lift after the C</b>: a small breath before the next E, like a singer.')}
{inact('Line, dot or arrow?', qtagT(ex('a_tenq', 76)), ['<b>The first two Cs have lines:</b> how long?', '<b>The Gs have dots.</b>', '<b>The E in bar 2</b> has an arrow.'], 'The first two Cs held their <b>full length</b>, the Gs short, the E strong, and the last C plain, held for its two beats.')}
{youknow('Ode to Joy (Beethoven)', ex('a_ode', 64), 'Two long slurs: two musical sentences. Lift your hand <b class="co">only</b> at the end of each one, like a singer taking a breath.', 'Sing it and breathe only where the slurs end.')}
{h3('Mood words')}
<p>Some words describe the mood, not the speed.</p>
{tbl(['Word', 'Meaning', 'Word', 'Meaning'], [['<i>dolce</i>', 'sweetly', '<i>leggiero</i>', 'lightly'], ['<i>cantabile</i>', 'in a singing style', '<i>espressivo</i>', 'with feeling'], ['<i>legato</i>', 'smoothly', '<i>grazioso</i>', 'gracefully'], ['<i>maestoso</i>', 'majestically', '<i>con moto</i>', 'with movement']], ['20%', '30%', '20%', '30%'])}
{game('Name the touch', qitems(['a dot', 'a line', '&gt;', 'a long curve'], 4), 'Name each mark and say how the note sounds.', '1 staccato, short · 2 tenuto, full and leaning · 3 accent, a strong start · 4 slur, joined (over different notes).')}
{try10(ex('a_stacc', 56), 'Hot Cross Buns, two ways.', 'Play E D C joined (fingers 3 2 1), then short and bouncy. Same notes, same fingers: two different tunes.')}
{thinkt('Legato is walking: one foot leaves the ground as the other lands. Staccato is hopping on hot sand.')}
{watch(['Making staccato loud: short is not the same as strong.', 'Lifting in the middle of a slur: keep every note joined until the curve ends.'])}
{howto('Practise touch', ['<b>Play one bar</b> of a piece three ways: all legato, all staccato, then as written.', '<b>Listen:</b> can someone else hear which way was which?'])}
{foot('Loud and soft p. {{E1}} · Tie or slur? p. {{T3+1}}', 'Online: Library › Articulation')}''', 75)

# ---------- 3 · Speed words ----------
TEMPI = [['<b>Largo</b>', 'very slow and broad', '40–60'], ['<b>Lento</b>', 'slow', '45–60'], ['<b>Adagio</b>', 'slow, at ease', '60–76'], ['<b>Andante</b>', 'at a walking pace', '76–108'], ['<b>Moderato</b>', 'at a moderate speed', '108–120'],
         ['<b>Allegretto</b>', 'fairly fast, a little slower than Allegro', '100–120'], ['<b>Allegro</b>', 'fast and lively', '120–156'], ['<b>Vivace</b>', 'lively and brisk', '152–168'], ['<b>Presto</b>', 'very fast', '168–200']]
CHANGE = [['<i>rit.</i> (ritardando), <i>rall.</i> (rallentando)', 'gradually slower'], ['<i>accel.</i> (accelerando)', 'gradually faster'], ['<i>a tempo</i>', 'back to the speed before'],
          ['<svg viewBox="0 0 40 26" style="width:32px"><path d="M4,22 A16,16 0 0 1 36,22" fill="none" stroke="#26296b" stroke-width="3"/><circle cx="20" cy="19" r="3" fill="#26296b"/></svg> fermata (pause)', 'hold longer than written, then go on'],
          ['<i>poco a poco</i>', 'little by little'], ['<i>molto</i> · <i>poco</i> · <i>più</i> · <i>meno</i>', 'very · a little · more · less (<i>più mosso</i>: faster; <i>meno mosso</i>: slower)'], ['<i>rubato</i>', 'time borrowed and paid back (p. {{T7+1}}) ' + lv('')]]
E3 = epage(f'''{head('Part III · Expression · 3', 'Speed words', 'How fast is the beat? A word at the top of the music tells you, usually in Italian, and often a number too. Other words inside the music ask you to slow down, speed up, or wait.')}
{hero(hero_dial(), 'Andante: the speed of walking')}
{tbl(['Word', 'Meaning', 'About (beats a minute)'], TEMPI, ['24%', '46%', '30%'], 'nt')}
<p class="sm">The numbers are a rough guide: the music and the room decide the rest.</p>
<!--SPLIT-->
{h3('The metronome mark')}
{two(ex('t_mark', 74), '<p><b>♩&nbsp;=&nbsp;76</b> means 76 crotchet beats in one minute. Set a metronome to 76: each click is one beat. The word tells you the character; the number pins down the speed.</p>')}
{h3('Changing speed')}
{tbl(['Word or sign', 'What you do'], CHANGE, ['48%', '52%'])}
{two(ex('t_rit', 70, '<i>rit.</i>: slow down into the end, then wait on the fermata.'), ex('t_accel', 70, '<i>accel.</i>: speed up, little by little, to the end.'))}
{inact('How fast is ♩ = 60?', qtagT('<div style="font:700 40px PF,serif;color:#26296b;text-align:center">♩ = 60</div>'), ['<b>60 beats</b> in one minute.', '<b>How many seconds</b> are there in a minute?', '<b>So one beat</b> lasts how long?'], 'One beat every <b>second</b>: tick, tick, like a clock.')}
{inact('Where does it slow down, and where does it come back?', qtagT(ex('t_atempo', 70)), ['<b>Find rall.</b> Which notes does it slow?', '<b>Find a tempo.</b>', '<b>What speed</b> does a tempo mean?'], 'Bar 1 slows into the two Gs; at <b>a tempo</b> (bar 3) the first speed comes straight back.')}
{inact('How long do you hold the fermata?', qtagT(ex('t_ferm', 70, red=('n5',))), ['<b>The minim</b> is worth how many beats?', '<b>The fermata</b> asks for more. How much?', '<b>Then what?</b>'], 'Longer than 2 beats: hold until it <b>feels finished</b>, often half as long again or more, then go on.')}
{youknow('Twinkle, Twinkle, Little Star', ex('y_tw_rit', 66, red=('n7',)), 'Players often slow down into the last “are”: a <b class="co">rit.</b>, then a fermata on the final C. The ending feels like coming home.', 'Sing the last line twice: once in time, once with a rit.')}
{game('Slow to fast', qitems(['Allegro', 'Largo', 'Andante', 'Presto'], 4), 'Put the four words in order from the slowest to the fastest.', 'Largo · Andante · Allegro · Presto.')}
{try10('<div style="font:700 26px PF,serif;color:#26296b;text-align:center">Andante</div>', 'Walk it.', 'Walk across the room at a calm pace, saying 1 2 3 4 with your steps: that is Andante. Now jog on the spot: Allegro.')}
{thinkt('A rit. is a car braking gently at the lights; a tempo is driving off again at the same speed as before.')}
{watch(['Taking Andante as slow: it is a walking pace.', 'Slowing down all at once at rit.: slow little by little.', 'Forgetting a tempo: after a rit., the first speed comes back exactly.'])}
{foot('Pulse and tempo p. {{T1}} · Rubato p. {{T7+1}}', 'Online: Metronome')}''', 78)

# ---------- 4 · The pedals ----------
OTHER = [['<b>left</b>', 'soft pedal: <i>una corda</i>, written <i>u.c.</i>', 'a softer, gentler sound; lift it at <i>t.c.</i> (<i>tre corde</i>)'], ['<b>middle</b>', '<i>sostenuto</i> ' + lv(''), 'holds only the notes already down (on many uprights: a practice mute)'], ['<b>right</b>', 'sustain (damper) pedal: <i>Ped.</i>', 'every note keeps ringing until you lift it']]
E4 = epage(f'''{head('Part III · Expression · 4', 'The pedals', 'Most pianos have three pedals. The right one, the <b>sustain pedal</b>, lifts every damper off the strings, so notes keep ringing after your fingers let go. The left one makes the sound softer.')}
{hero(pedals(), 'Right pedal: the notes keep ringing')}
{tbl(['Pedal', 'Name and sign', 'What it does'], OTHER, ['14%', '40%', '46%'])}
{h3('Writing the sustain pedal')}
{pedmarks()}
{rule('Heel on the floor, press with the ball of your foot. <b>Play first, then pedal</b>: new notes, then up and straight down again.')}
<!--SPLIT-->
{h3('Changing the pedal')}
{pedtime()}
{ex('p_ped', 70, 'A chord is three or more notes played together. The ✻Ped. sits under each new chord: play it first, then change straight away.')}
{inact('Where does the pedal go down, and where does it come up?', qtagT(ex('p_pedq', 72)), ['<b>Find Ped.</b> under the first C.', '<b>Find the next sign:</b> a star with Ped.', '<b>Find the last star.</b>'], 'Down on the first C, <b>changed</b> at the first F (up and down again), and up at the end: each bar rings as one sound.')}
{inact('Why change at every new chord?', qtagT(ex('p_ped', 66)), ['<b>Hold the pedal</b> from C-E-G into F-A-C. What do you hear?', '<b>Now change</b> just after the F.', '<b>Compare</b> the two.'], 'Without a change, the two groups <b>blur</b> into a muddle. Change on each new chord: clean, and still joined.')}
{inact('Which pedal?', pedals(True, 340), ['<b>Ped.</b>: which foot pedal?', '<b>u.c.</b>: which one?', '<b>t.c.</b>: what do you do?'], 'Ped. is the <b>right</b> pedal; <i>u.c.</i> the <b>left</b> one; <i>t.c.</i> means let the left pedal up.')}
{game('Up or down?', qitems(['Ped.', '*', 'u.c.', 't.c.'], 4), 'Which pedal, and up or down?', '1 right pedal down · 2 right pedal up · 3 left pedal down · 4 left pedal up.')}
{try10(ex('p_pedq', 64), 'Hear the ringing.', 'Play C, E and G together, press the right pedal and take your hands off: the chord keeps sounding. Lift the pedal: silence.')}
{thinkt('The sustain pedal holds a door open: every note that walks in stays in the room until you let the door shut.')}
{watch(['Lifting the pedal before the new notes: a gap of silence. Play first, then change.', 'Keeping the pedal down through a new chord: muddy.'])}
{howto('Practise the pedal change', ['<b>Without playing</b>, say “play, up-down” and move your foot on “up-down”.', '<b>Play C-E-G, then F-A-C, then G-B-D</b>, slowly. Change just after each one.', '<b>Listen</b> for a clean change with no gap of silence.'])}
{extra('Half pedal and the middle pedal', '<p><b>Half pedal:</b> lift the pedal only part of the way, to clear some of the sound but not all. <b>Sostenuto</b> (the middle pedal on grand pianos): press it while notes are held, and only those notes keep ringing.</p>')}
{foot('Touch p. {{E2}} · Chords p. {{H1}}', 'Online: Library › Pedal')}''', 81)

# ---------- 5 · Ornaments ----------
ORN = [[ex('o_trill_w', 62), '<b>trill</b>', 'the note and the one above, back and forth quickly'], [ex('o_mord_w', 62), '<b>upper mordent</b>', 'the note, the one above, the note: one quick flick'],
       [ex('o_lmord_w', 62), '<b>lower mordent</b>', 'the note, the one below, the note'], [ex('o_turn_w', 62), '<b>turn</b>', 'above, the note, below, the note'],
       [ex('o_acc_w', 62), '<b>acciaccatura</b>', 'a tiny note with a slash: crushed in, as fast as you can'], [ex('o_app_w', 62), '<b>appoggiatura</b>', 'a tiny note, no slash: leans, taking half the main note’s time']]
E5 = epage(f'''{head('Part III · Expression · 5', 'Ornaments', 'Ornaments are decorations: a small sign that stands for a quick burst of notes around the main note. They borrow the notes <b>next door</b>, one letter name up or down: on D, the note above is E and the note below is C.')}
{hero(arrow_pair(ex('o_trill_w', 84), ex('o_trill_p', 84), 'played'), 'A small sign, a burst of notes')}
{tbl(['Written', 'Name', 'How to play'], ORN, ['28%', '24%', '48%'])}
<!--SPLIT-->
{h3('Written and played')}
{tbl(['', 'Written', '', 'Played'], [[n, ex(w, 58), '<span style="font:700 22px CV,cursive;color:#e4572e">→</span>', ex(pl, 58)] for n, w, pl in (('<b>upper mordent</b>', 'o_mord_w', 'o_mord_p'), ('<b>lower mordent</b>', 'o_lmord_w', 'o_lmord_p'), ('<b>turn</b>', 'o_turn_w', 'o_turn_p'), ('<b>appoggiatura</b>', 'o_app_w', 'o_app_p'))], ['20%', '32%', '8%', '40%'])}
{inact('How do you play this trill?', qtagT(ex('o_q', 56, red=('n5',))), ['<b>Which note</b> has the tr?', '<b>Its next-door note above</b> is…?', '<b>Go back and forth</b> for how long?'], 'On the E: <b>E F E F…</b> quickly for its two beats, then the last E on time.')}
{inact('Crushed, or leaning?', qtagT(two(ex('o_acc_w', 50), ex('o_app_w', 50))), ['<b>Look for the slash</b> through the tiny note.', '<b>With a slash:</b> how fast?', '<b>Without:</b> how much time does it take?'], 'Slash (acciaccatura): <b>crushed in</b>, almost at once. No slash (appoggiatura): <b>D for a crotchet</b>, then C.')}
{inact('Which notes does the turn use?', qtagT(ex('o_turn_w', 54)), ['<b>The main note</b> is D.', '<b>Next door above</b>, and <b>next door below</b>?', '<b>Order:</b> above, main, below, main.'], '<b>E D C D</b>, then hold the D: four quick notes, ending on the main note.')}
{extra('Where does a trill start?', '<p>In music from the 1700s (Bach, Handel), a trill usually starts on the note <b>above</b>: F E F E on an E. In later music it starts on the main note. Your teacher or the edition will tell you.</p>')}
{game('Above or below?', qitems(['trill', 'upper mordent', 'lower mordent', 'turn'], 4), 'Which next-door note does each one use: above, below, or both?', '1 above · 2 above · 3 below · 4 both.')}
{try10(ex('o_trill_p', 56), 'A slow trill.', 'Play D and E with fingers 2 and 3, slowly, eight times. Then a little faster. A trill is just that, at speed, with the beat still steady.')}
{watch(['Adding a sharp or flat that is not there: use the plain next-door letter.', 'Starting the ornament late: it begins on the beat (a crushed note just before it).'])}
{howto('Practise an ornament', ['<b>Play the main notes</b> alone first, in time.', '<b>Add the ornament slowly</b>, as written-out notes.', '<b>Speed it up</b> bit by bit, keeping the main note on the beat.'])}
{foot('The keyboard p. {{P1}} · Sharps and flats p. {{P5}}', 'Online: Library › Ornaments')}''', 84)

# ---------- Tips ----------
ET = epage(f'''{head('Part III · Expression · Tips', 'When your playing sounds flat', 'Every note can be right and the music still sound flat. The fix is almost always one sign you read but did not play. Find what you notice, then check that one thing.')}
{box('Tip', '<b class="it">What you notice, what to check</b>' + tbl(['What you notice', 'Check', 'Turn to'], [['Everything is the same loudness', '<b>the dynamics:</b> is every sign a different step?', 'p. {{E1}}'], ['The tune sounds choppy', '<b>the slurs:</b> join every note inside the curve', 'p. {{E2}}'], ['Short notes sound heavy', '<b>staccato</b> is short, not loud', 'p. {{E2}}'], ['The end feels rushed', '<b>rit. and fermata:</b> slow little by little, then wait', 'p. {{E3}}'], ['The sound is muddy', '<b>the pedal:</b> change on each new chord', 'p. {{E4}}'], ['The ornament trips the beat', '<b>the main note</b> lands on time; practise it slowly', 'p. {{E5}}']], ['38%', '48%', '14%']))}
{h3('Four ways to bring music to life')}
<div class="fixes">{''.join(f'<div><span class="rn">{i + 1}</span><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate([('Sing it first', 'Sing the phrase: your voice shapes it naturally. Then copy your voice on the keys.'), ('Exaggerate', 'Play the dynamics twice as big as you think. It always sounds smaller to the listener.'), ('Record yourself', 'Listen back with the music: did each sign really happen?'), ('Shape every phrase', 'Grow towards the most important note, then let the phrase fall away.')]))}</div>
{inact('Give this phrase a shape', qtagT(ex('e_tw_bare', 80, red=('n5',))), ['<b>Sing it:</b> where does it want to go?', '<b>Which note</b> feels like the top of the hill?', '<b>Where</b> would you start soft and end soft?'], 'Start soft, grow to the first A, then fade: <b>a phrase is a hill</b>, up and down.')}
{thinkt('Expression is the difference between reading a story aloud and telling it.')}''', PM.PAGE['ET'])

EOPEN = _oa('Part III · How it should sound', 'Expression', 'The notes say <b>what</b> to play; expression says <b>how</b>: loud or soft, smooth or short, faster or slower, ringing or dry. Everything in this part is in these three bars.', 'E', PM.PAGE)
_ebody = ''.join(assemble(f'E{_i + 1}', _pg) for _i, _pg in enumerate((E1, E2, E3, E4, E5))) + ET
ehtml = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{OPENCSS}</style></head><body>{EOPEN}{_ebody}{FLOWJS}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-expression.html', 'w').write(ehtml)
print('ok expression')
