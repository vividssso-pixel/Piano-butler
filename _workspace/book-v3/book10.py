# The Piano Butler Handbook, Part II: Time, v2 (legible type, engraved notation, no pills)
import json, base64, re
V = json.load(open('/tmp/claude-0/vrv/out.json'))
DK, N, C, CR, G, MUTE = '#1c1e4f', '#26296b', '#e4572e', '#fffdf7', '#2e8a6e', '#6d6f9c'
FD = '/tmp/claude-0/vrv/node_modules/@fontsource/'
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
FF = (f"@font-face{{font-family:'AH';font-weight:400;src:url(data:font/woff2;base64,{b64(FD + 'atkinson-hyperlegible/files/atkinson-hyperlegible-latin-400-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'AH';font-weight:700;src:url(data:font/woff2;base64,{b64(FD + 'atkinson-hyperlegible/files/atkinson-hyperlegible-latin-700-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'NM';src:url(data:font/woff2;base64,{b64(FD + 'noto-music/files/noto-music-music-400-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'PF';font-weight:700;src:url(data:font/woff2;base64,{b64('/tmp/claude-0/fnt/package/files/playfair-display-latin-700-normal.woff2')}) format('woff2')}}")

def vx(k, h=84, cap=''):
    return f'<figure class="vx"><div class="vs">{V[k].replace("<svg ", f"<svg style=\"max-height:{h}px\" ", 1)}</div>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>'
INK = json.load(open('/tmp/claude-0/pk/gm-ink.json'))
def gin(kind, k, h=24): return gcell(kind, k, h).replace('display:block;margin:0 auto', 'display:inline-block;vertical-align:-6px;margin:0 2px')
def gcell(kind, k, h=42, W=100, H=140):
    ch = (NT if kind == 'n' else RS)[k]; L, R_, A, D, _ = INK[kind + ':' + k]
    x0 = W / 2 - (R_ - L) / 2; y0 = H / 2 - (D - A) / 2
    return f'<svg viewBox="0 0 {W} {H}" style="height:{h}px;width:{h * W / H:.0f}px;display:block;margin:0 auto;overflow:visible"><text x="{x0:.1f}" y="{y0:.1f}" font-family="NM" font-size="100" fill="{N}">{ch}</text></svg>'
def bars(kind, h=34):
    sw = {'bar': [(0, 3)], 'dbl': [(0, 3), (9, 3)], 'fin': [(0, 3), (9, 9)], 'rep': [(0, 9), (14, 3)], 'rep2': [(0, 3), (6, 9)]}
    def one(k, dx=0, dots=None):
        out = ''.join(f'<rect x="{dx + x}" y="0" width="{w}" height="60" fill="{N}"/>' for x, w in sw[k])
        if dots: out += ''.join(f'<circle cx="{dx + dots}" cy="{cy}" r="3.4" fill="{N}"/>' for cy in (22, 38))
        return out
    if kind == 'repeat': inner, W = one('rep', 0, 25) + one('rep2', 46, -0.5 + 40), 64
    else: inner, W = one({'bar': 'bar', 'dbl': 'dbl', 'fin': 'fin'}[kind]), 20
    return f'<svg viewBox="-2 -2 {W + 4} 64" style="height:{h}px;width:auto;display:block">{inner}</svg>'
def gl(ch, size=34): return f'<span class="gl2" style="font-size:{size}px">{ch}</span>'
NT = {'breve': '𝅜', 'dsb': '𝅝𝅭', 'sb': '𝅝', 'dm': '𝅗𝅥𝅭', 'm': '𝅗𝅥', 'dc': '𝅘𝅥𝅭', 'c': '𝅘𝅥', 'dq': '𝅘𝅥𝅮𝅭', 'q': '𝅘𝅥𝅮', 'sq': '𝅘𝅥𝅯', 'dsq': '𝅘𝅥𝅰', 'hdsq': '𝅘𝅥𝅱'}
RS = {'breve': '𝄺', 'dsb': '𝄻𝅭', 'sb': '𝄻', 'dm': '𝄼𝅭', 'm': '𝄼', 'dc': '𝄽𝅭', 'c': '𝄽', 'dq': '𝄾𝅭', 'q': '𝄾', 'sq': '𝄿', 'dsq': '𝅀', 'hdsq': '𝅁'}
def page(inner, n, right='PART II · TIME'):
    return f'''<section class="pg"><div class="top"><span>THE PIANO BUTLER HANDBOOK</span><span>{right}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'''
def head(k, t, lead): return f'<div class="kick">{k}</div><h1>{t}</h1><p class="lead">{lead}</p>'
def h3(t): return f'<h3>{t}</h3>'
def tbl(head, rows, widths=None, cls=''):
    cg = ''.join(f'<col style="width:{w}">' for w in widths) if widths else ''
    return f'<table class="ht {cls}"><colgroup>{cg}</colgroup><thead><tr>{"".join(f"<th>{h}</th>" for h in head)}</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table>'
def lv(x): return x if x else '<span class="ex">Extra</span>'
def ts(a, b): return f'<span class="ts"><b>{a}</b><b>{b}</b></span>'
def box(t, body): return f'<div class="box"><div class="bh">{t}</div>{body}</div>'
def watch(items): return '<div class="watch"><div class="bh">Watch out</div>' + ''.join(f'<div class="wr"><span class="x">✗</span><span>{t}</span></div>' for t in items) + '</div>'
def foot(see, practise): return f'<div class="links"><div><span class="lab">See also</span>{see}</div><div><span class="lab">Practise it</span>{practise}</div></div>'
def two(a, b, r='1fr 1fr'): return f'<div class="two" style="grid-template-columns:{r}"><div>{a}</div><div>{b}</div></div>'

flow = ''.join(f'<div class="fl"><span class="fln">{i + 1}</span><b>{a}</b><span>{b}</span></div>' + ('<span class="fa">›</span>' if i < 4 else '') for i, (a, b) in enumerate([('Pulse', 'the steady beat underneath'), ('Bar', 'beats in groups of 2, 3 or 4'), ('Time signature', 'how many beats, and which note is one beat'), ('Note values', 'how long each sound lasts'), ('Rhythm', 'the pattern of long and short')]))
OPEN = f'''<section class="pg part2"><div class="pframe"><div class="pk">Part II</div><div class="pt">Time</div><div class="pdv"></div>
<p class="pl">Music moves through time. Underneath it runs a steady <b>pulse</b>; the pulse is grouped into <b>bars</b>; and every note and rest takes a measured share of it. This part goes from that big picture down to the length of a single note.</p>
<div class="flow">{flow}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{p}</span></div>' for x, p in (('Pulse, tempo and the bar', 36), ('Notes and rests', 37), ('How long is a note?', 38), ('Time signatures', 39), ('Compound and irregular time', 40), ('Rhythm: groups and upbeats', 41), ('Rhythm: off the beat', 42)))}</div></div></section>'''

P36 = page(f'''{head('Part II · Time · 1', 'Pulse, tempo and the bar', 'Under almost every piece runs a <b>pulse</b>: a steady beat, like a heartbeat or a clock. Its speed is the <b>tempo</b>. Beats are grouped into <b>bars</b>, and the first beat of every bar is the strongest.')}
{two(h3('Tempo') + f'<p>Tempo is measured in beats per minute. A <b>metronome mark</b> at the top of the music shows it: <span class="mm">{gin("n", "c")} = 60</span> means 60 crotchet beats a minute, one beat a second. <span class="mm">{gin("n", "c")} = 120</span> is twice as fast. Tempo words such as <i>Andante</i> and <i>Allegro</i> are on page 70.</p>',
     h3('Strong and weak beats') + tbl(['Beats', 'Pattern', 'Feels like'], [['2', '<b>Strong</b> weak', 'a march'], ['3', '<b>Strong</b> weak weak', 'a waltz'], ['4', '<b>Strong</b> weak <b>medium</b> weak', 'most songs']], ['16%', '50%', '34%']))}
{h3('Bars and bar lines')}
{tbl(['Sign', 'Name', 'Meaning'], [[bars('bar'), 'bar line', 'marks the end of a bar'], [bars('dbl'), 'double bar line', 'marks the end of a section'], [bars('fin'), 'final bar line', 'marks the end of the piece'], [bars('repeat'), 'repeat signs', 'play the music between them twice; with only the end sign, go back to the start']], ['18%', '24%', '58%'])}
{h3('Counting')}
{vx('t34', 92, 'Three bars of 3/4. The counting never changes, whatever the notes do: a long note still has every one of its beats counted.')}
<p>Count aloud at one speed, a little louder on beat 1. With a metronome, start slower than you think and speed up only when the passage is steady.</p>
{watch(['Speeding up in the easy bars and slowing down in the hard ones: choose a tempo you can keep in the hardest bar.', 'Counting the notes instead of the beats.'])}
{foot('Time signatures p. 39 · Tempo words p. 70', 'Workbook Level 0 · Pulse · Online: Metronome')}''', 36)

rows = [('breve', 'breve', 'double whole note', '8', 'Level 4'), ('dsb', 'dotted semibreve', 'dotted whole note', '6', ''), ('sb', 'semibreve', 'whole note', '4', 'Level 0'), ('dm', 'dotted minim', 'dotted half note', '3', 'Level 0'), ('m', 'minim', 'half note', '2', 'Level 0'), ('dc', 'dotted crotchet', 'dotted quarter note', '1½', 'Level ½'),
        ('c', 'crotchet', 'quarter note', '1', 'Level 0'), ('dq', 'dotted quaver', 'dotted eighth note', '¾', 'Level 3'), ('q', 'quaver', 'eighth note', '½', 'Level 0'), ('sq', 'semiquaver', 'sixteenth note', '¼', 'Level 2'), ('dsq', 'demisemiquaver', '32nd note', '⅛', ''), ('hdsq', 'hemidemisemiquaver', '64th note', '1/16', '')]
NTAB = '<table class="ht nt"><colgroup><col style="width:9%"><col style="width:9%"><col style="width:28%"><col style="width:26%"><col style="width:10%"><col style="width:18%"></colgroup><thead><tr><th>Note</th><th>Rest</th><th>Name</th><th>In the USA</th><th>Beats*</th><th>First met</th></tr></thead><tbody>' + ''.join(
    f'<tr><td class="g">{gcell("n", k)}</td><td class="g">{gcell("r", k)}</td><td><b>{n}</b></td><td class="mu">{us}</td><td><b>{b}</b></td><td>{lv(l)}</td></tr>' for k, n, us, b, l in rows) + '</tbody></table>'
P37 = page(f'''{head('Part II · Time · 2', 'Notes and rests', 'A note’s shape shows how long it lasts: each plain note lasts <b>half as long</b> as the one above it. Every note has a <b>rest</b> of the same length, a silence counted just as carefully as a sound.')}
{NTAB}
<div class="fn">* With the crotchet as one beat, as in 2/4, 3/4 and 4/4. <span class="ex">Extra</span>: beyond Level 8.</div>
{two(h3('Parts of a note') + '<p>The <b>head</b> sits on a line or in a space. A <b>stem</b> goes up on the right of the head or down on the left. <b>Flags</b> on the stem halve the value each time; groups of quavers are joined by <b>beams</b> instead of flags.</p>',
     h3('Which rest is which?') + '<figure class="vx"><svg viewBox="0 0 300 90" style="width:100%;height:auto;display:block"><line x1="10" x2="290" y1="20" y2="20" stroke="#26296b" stroke-width="1.2"/><line x1="10" x2="290" y1="32" y2="32" stroke="#26296b" stroke-width="1.2"/><line x1="10" x2="290" y1="44" y2="44" stroke="#26296b" stroke-width="1.2"/><line x1="10" x2="290" y1="56" y2="56" stroke="#26296b" stroke-width="1.2"/><line x1="10" x2="290" y1="68" y2="68" stroke="#26296b" stroke-width="1.2"/><line x1="150" x2="150" y1="20" y2="68" stroke="#26296b" stroke-width="1.2"/><rect x="62" y="32" width="26" height="7" fill="#26296b"/><rect x="202" y="37" width="26" height="7" fill="#26296b"/> <text x="75" y="86" text-anchor="middle" font-family="AH" font-size="12" font-weight="700" fill="#e4572e">semibreve rest</text><text x="215" y="86" text-anchor="middle" font-family="AH" font-size="12" font-weight="700" fill="#e4572e">minim rest</text></svg></figure>' + '<p class="sm">The semibreve rest <b>hangs</b> below the fourth line; the minim rest <b>sits</b> on the middle line.</p>', '1fr 1fr')}''', 37)

tree = ''.join(f'<div class="trw"><span class="trl">{lab}</span><div class="trc">' + ''.join(f'<div class="tri">{gcell("n", k, 36)}</div>' for _ in range(n)) + '</div></div>' for lab, k, n in (('1 semibreve', 'sb', 1), ('2 minims', 'm', 2), ('4 crotchets', 'c', 4), ('8 quavers', 'q', 8), ('16 semiquavers', 'sq', 16)))
P38 = page(f'''{head('Part II · Time · 2', 'How long is a note?', 'Each row lasts exactly as long as the row above it: the same stretch of time, cut in half again and again.')}
<div class="tree">{tree}</div>
{two(h3('The dot') + '<p>A dot adds <b>half the note’s value</b>: a dotted minim lasts 2 + 1 = 3 beats; a dotted crotchet 1 + ½ = 1½. A <b>double dot</b> adds half, then a quarter: a double-dotted minim lasts 2 + 1 + ½ = 3½.</p>' + vx('dot', 78),
     h3('The tie') + '<p>A curve joining two notes <b>of the same pitch</b> makes one longer sound: play the first, hold through the second. Ties can cross a bar line, where a dot cannot.</p>' + vx('tie', 78))}
{box('Tie or slur?', '<p>The same curve over notes of <b>different</b> pitches is a <b>slur</b>: play them smoothly joined (legato). Same pitch: a tie. Different pitches: a slur.</p>')}
{h3('Rests in a bar')}
{two(vx('restgood', 70, '✓ A whole silent bar takes a semibreve rest, in any time signature. The silence on beats 3–4 is one minim rest.'), vx('restbad', 70, '✗ In 4/4, a minim rest on beats 2–3 hides the middle of the bar: write two crotchet rests.'))}
{foot('Time signatures p. 39 · Rhythm p. 41', 'Workbook Level 0 · Note values · Online: Library › Notes and rests')}''', 38)

bottom = [['2', gcell('n', 'm', 34), 'minim', 'Level 3'], ['4', gcell('n', 'c', 34), 'crotchet', 'Level 0'], ['8', gcell('n', 'q', 34), 'quaver', 'Level 1'], ['16', gcell('n', 'sq', 34), 'semiquaver', lv('')]]
simple = [[ts(2, 4), '2 crotchets', 'Level 0'], [ts(3, 4), '3 crotchets', 'Level 0'], [ts(4, 4) + ' ' + gl('𝄴', 30), '4 crotchets (the C sign: common time)', 'Level 0'], [ts(2, 2) + ' ' + gl('𝄵', 30), '2 minims (the cut C: cut common time)', 'Level 3'], [ts(3, 2), '3 minims', 'Level 3'], [ts(4, 2), '4 minims', lv('')], [ts(3, 8), '3 quavers', 'Level 3']]
P39 = page(f'''{head('Part II · Time · 3', 'Time signatures', 'Two numbers at the start of the music. The <b>top number</b> says how many counts are in each bar; the <b>bottom number</b> says which note gets one count.')}
{two(h3('The bottom number') + tbl(['Bottom', 'Note', 'One count is a', 'First met'], bottom, ['18%', '16%', '36%', '30%']),
     box('Simple or compound?', '<p>In <b>simple time</b> each beat divides into <b>two</b>. In <b>compound time</b> each beat is a dotted note and divides into <b>three</b>.</p><p><b>Quick test:</b> a top number of 6, 9 or 12 means compound. Divide it by 3 to find the beats: 6/8 has 2, 9/8 has 3, 12/8 has 4.</p>'))}
{h3('Simple time: each beat divides in two')}
{tbl(['Time signature', 'Each bar holds', 'First met'], simple, ['26%', '50%', '24%'])}
{h3('Changing time signature')}
<p>A new time signature can appear in the middle of a piece, right after a bar line; it holds until the next one. A time signature is written only once, not on every line.</p>
{watch(['Reading 6/8 as six beats: at most speeds it moves in two.', 'Mixing up 3/4 and 6/8: both hold six quavers, grouped differently (page 40).'])}
{foot('Pulse and the bar p. 36 · Compound time p. 40', 'Workbook Level 0 · Time signatures · Online: Library › Time signatures')}''', 39)

compound = [[ts(6, 8), '2 dotted crotchets', 'Level 1'], [ts(9, 8), '3 dotted crotchets', 'Level 3'], [ts(12, 8), '4 dotted crotchets', 'Level 3'], [ts(6, 4), '2 dotted minims', 'Level 4']]
irreg = [[ts(5, 4), '5 crotchets: 3 + 2 or 2 + 3', 'Level 0'], [ts(7, 4), '7 crotchets: 4 + 3 or 3 + 4', lv('')], [ts(5, 8), '5 quavers: 3 + 2 or 2 + 3', lv('')], [ts(7, 8), '7 quavers: 2 + 2 + 3 or 3 + 2 + 2', lv('')]]
P40 = page(f'''{head('Part II · Time · 3', 'Compound and irregular time', 'Compound time has dotted beats that divide into three; irregular time has five or seven counts, grouped unevenly. (9/4, 12/4 and the /16 signatures exist but are rare.)')}
{h3('Compound time')}
{tbl(['Time signature', 'Each bar holds', 'First met'], compound, ['26%', '50%', '24%'])}
{h3('Counting 6/8')}
{vx('t68', 66, 'Slowly, count all six quavers. At speed, feel two beats, on 1 and 4: “1 & a, 2 & a”.')}
{h3('3/4 or 6/8?')}
{two(vx('t34q', 66, '3/4: six quavers in three twos'), vx('t68q', 66, '6/8: six quavers in two threes'))}
{h3('Irregular time')}
{tbl(['Time signature', 'Each bar holds', 'First met'], irreg, ['26%', '50%', '24%'])}
{two(box('Uneven groups in 4/4', '<p>Many dances keep 4/4 but group the eight quavers 3 + 3 + 2: “1 2 3, 1 2 3, 1 2”.</p>'), vx('t332', 64), '1fr 1fr')}''', 40)

P41 = page(f'''{head('Part II · Time · 4', 'Rhythm: groups and upbeats', 'Rhythm is the pattern of long and short sounds over the pulse. The pulse stays steady; the rhythm moves around it. The way notes are grouped on the page shows where the beats are.')}
{h3('Grouping with beams')}
<p>Beams join the notes of <b>one beat</b>, so the beats stay visible. In 4/4 a beam may cover beats 1–2 or 3–4, but never cross the middle of the bar. In compound time, quavers are beamed in threes.</p>
{two(vx('beamgood', 78, '✓ The middle of the bar can be seen.'), vx('beambad', 78, '✗ A beam across beats 2–3 hides it.'))}
{h3('The upbeat (anacrusis)')}
{two('<p>A piece can begin <b>before</b> the first full bar, with one or more notes called an upbeat or anacrusis. The last bar is then short by the same amount, so the two together make one full bar. Count the missing beats in silence before you start.</p>', vx('anac', 78, 'Count “1 2” silently, then play on 3.'))}
{h3('Triplets and duplets')}
{two(vx('trip', 80, 'Triplet: three notes in the time of two.') + '<p class="sm">Level 2. Three exactly equal notes.</p>', vx('dup', 80, 'Duplet: two notes in the time of three, in compound time.') + '<p class="sm">Level 2.</p>')}
{h3('Counting smaller values')}
{vx('small', 100, 'Crotchet, two quavers, four semiquavers and a triplet (“1 & a”): one beat each.')}''', 41)

terms = [['syncopation', 'the stress falls off the beat, often on a note held across it', 'Level 4'], ['hemiola', 'two bars of three felt as three bars of two', 'Level 4'], ['swing', 'pairs of quavers played long–short, like the first and last notes of a triplet', lv('')], ['polyrhythm', 'two rhythms at once, such as three notes in one hand against two in the other', 'Level 7'], ['rubato', 'time stretched and given back, for expression; the pulse returns', lv('')]]
P42 = page(f'''{head('Part II · Time · 4', 'Rhythm: off the beat', 'Once the pulse is secure, rhythm can pull against it. These effects only work if the beat underneath stays steady.')}
{two(h3('Syncopation') + vx('sync', 70, 'The crotchet starts on “&” and is held through beat 2.') + '<p class="sm">Level 4. Feel beat 2 even though nothing is played on it.</p>',
     h3('Hemiola') + vx('hemi', 70, 'Two bars of 3/4 become three minims.') + '<p class="sm">Level 4. Common at cadences in Baroque dances.</p>')}
{h3('Swing')}
{two(vx('swingw', 70, 'Written'), vx('swingp', 70, 'Played'))}
{h3('More terms')}
{tbl(['Term', 'What it means', 'First met'], terms, ['20%', '60%', '20%'])}
{watch(['Rushing the short notes after a long one: keep counting inside the long note.', 'Playing a triplet unevenly: three equal notes, not two quick and one long.', 'Letting syncopation drag the pulse: tap the beat with your foot.'])}
{foot('Notes and rests p. 37 · Words for how to play p. 70', 'Workbook Levels 2–4 · Rhythm · Online: Rhythm clock')}''', 42)

css = f'''
@page {{ size: A4; margin: 0 }} *{{box-sizing:border-box}} body{{margin:0;background:#e9e4d8;font-family:'AH',Arial,sans-serif;color:{N}}}
.pg{{width:794px;height:1123px;background:{CR};margin:0 auto 24px;position:relative;overflow:hidden;padding:42px 58px 0;page-break-after:always}}
.top{{display:flex;justify-content:space-between;font-size:9.5px;font-weight:700;letter-spacing:.16em;color:#8a8cb0}} .rule{{height:5px;border-top:1.5px solid {N};border-bottom:.6px solid {N};margin:7px 0 18px}}
.foot{{position:absolute;left:0;right:0;bottom:30px;text-align:center}} .foot span{{display:inline-block;width:26px;height:26px;line-height:26px;background:{N};color:#fff;font:700 13px 'AH',Arial}}
.kick{{font-size:11.5px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{C}}} h1{{font-family:'PF',Georgia,serif;font-size:35px;line-height:1.1;margin:3px 0 8px;font-weight:700}}
.lead{{font-size:16.5px;line-height:1.5;margin:0 0 10px}} p{{font-size:15px;line-height:1.5;margin:4px 0 8px}} p.sm{{font-size:13.5px;color:{MUTE};margin:2px 0 4px}}
h3{{font-size:17px;font-weight:700;margin:14px 0 6px;padding-top:8px;border-top:1.5px solid {N}}}
.two{{display:grid;gap:22px;align-items:start}} .two h3:first-child{{margin-top:6px}}
.ht{{width:100%;border-collapse:collapse;table-layout:fixed;font-size:14.5px}} .ht th{{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#8a8cb0;text-align:left;padding:4px 8px;border-bottom:1.5px solid {N}}}
.ht td{{border-bottom:.6px solid #e2ddd0;padding:3px 8px;vertical-align:middle;line-height:1.35}} .nt td{{padding:3px 8px;vertical-align:middle}} .nt td.g{{text-align:center}} .mu{{color:{MUTE};font-size:13.5px}}
.ex{{color:#9a9cc4;font-style:italic}} .fn{{font-size:12.5px;color:{MUTE};margin-top:6px}}
.gl2{{font-family:'NM';line-height:1;color:{N};display:inline-block;vertical-align:middle}} .mm{{white-space:nowrap;font-weight:700}}
.ts{{display:inline-flex;flex-direction:column;align-items:center;line-height:.8;font-family:'PF',Georgia,serif;font-size:17px;vertical-align:middle;margin-right:6px}}
.box{{border-left:3px solid {C};padding:6px 0 4px 14px;margin:10px 0}} .bh{{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin-bottom:2px}}
.watch{{border-top:1px solid #c9cbe0;border-bottom:1px solid #c9cbe0;padding:8px 2px;margin:12px 0}} .wr{{display:flex;gap:10px;font-size:14.5px;line-height:1.45;padding:2px 0}} .x{{color:{C};font-weight:700}}
.links{{display:grid;grid-template-columns:1fr 1fr;gap:22px;font-size:13.5px;margin-top:10px;color:#3d4080}} .lab{{display:block;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}}
.vx{{margin:6px 0;border:1px solid #e2ddd0;background:#fff;padding:8px 12px 6px}} .vs{{display:flex;justify-content:center}} .vs svg{{width:100%;height:auto;color:{N};fill:{N}}}
.vx text{{font-family:'AH',Arial !important;fill:{C} !important;font-weight:700}} figcaption{{font-size:13px;color:{MUTE};margin-top:4px;line-height:1.4}}
.tree{{border:1px solid #e2ddd0;background:#fff;padding:8px 14px}} .trw{{display:flex;align-items:center;gap:12px;border-bottom:.6px solid #eee8da;padding:3px 0}} .trw:last-child{{border:0}} .trl{{flex:none;width:130px;font-size:14px;font-weight:700}} .trc{{flex:1;display:flex}} .tri{{flex:1;text-align:center;border-left:1px dashed #e2ddd0}} .tri:first-child{{border-left:0}}
.part2{{background:{DK};padding:34px}} .pframe{{position:absolute;inset:34px;border:1.5px solid rgba(255,253,247,.7);outline:.6px solid rgba(255,253,247,.45);outline-offset:-8px;color:{CR};padding:120px 64px 40px}}
.pk{{font-size:12px;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:#f4a9bb}} .pt{{font-family:'PF',Georgia,serif;font-size:80px;line-height:1;margin-top:10px}} .pdv{{width:90px;height:5px;border-top:1px solid {CR};border-bottom:1px solid {CR};margin:24px 0;opacity:.7}}
.pl{{font-size:17px;line-height:1.65;max-width:580px;opacity:.95}} .flow{{display:flex;align-items:stretch;gap:4px;margin:34px 0 30px}} .fl{{flex:1;border:1px solid rgba(255,253,247,.45);padding:10px 8px;text-align:center}} .fln{{display:block;font-weight:700;color:#f4a9bb}} .fl b{{display:block;font-size:15px;margin:2px 0}} .fl span:last-child{{display:block;font-size:11.5px;opacity:.8;line-height:1.35}} .fa{{align-self:center;color:#f4a9bb;font-size:18px}}
.pin{{max-width:380px}} .pih{{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;opacity:.75;margin-bottom:4px}} .tr{{display:flex;align-items:baseline;gap:6px;font-size:15px;padding:3px 0}} .dots{{flex:1;border-bottom:1px dotted rgba(255,253,247,.45);transform:translateY(-4px)}}
'''
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{OPEN}{P36}{P37}{P38}{P39}{P40}{P41}{P42}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-time2.html', 'w').write(html)
print('ok')
