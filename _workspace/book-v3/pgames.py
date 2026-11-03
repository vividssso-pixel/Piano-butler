# Pitch games: six new formats (not copies of the rhythm games)
import json
exec(open('/tmp/claude-0/pk/wbpitch.py').read())
WP.update(json.load(open('/tmp/claude-0/pk/wp/gout_c.json')))
bow = f'<svg viewBox="0 0 40 24" style="width:30px;height:18px"><path d="M2 3 L18 12 L2 21 Z" fill="none" stroke="{N_}" stroke-width="2" stroke-linejoin="round"/><path d="M38 3 L22 12 L38 21 Z" fill="none" stroke="{N_}" stroke-width="2" stroke-linejoin="round"/><circle cx="20" cy="12" r="2.6" fill="{C}"/></svg>'
def gpage(title, how, inner, n):
    return f'''<section class="pg"><div class="top"><span>PIANO BUTLER · FREE PRINTABLE</span><span>PITCH GAMES</span></div><div class="rule"></div>
<div class="body"><div class="kick">Pitch game</div><h1>{title}</h1><p class="lead">{how}</p>{inner}</div><div class="ffoot"><span>{bow}</span><span>More at <b>thepianobutler.com</b></span><span>Free for personal and classroom use. Share the link, not the file. © Piano Butler</span></div><div class="foot"><span>{n}</span></div></section>'''
def ud(t): return f'<p class="sm">Answers, upside down: <span class="ud">{t}</span></p>'

# 1. Note crossword: every clue is written in notes
G = ['CABBAGE', 'A.A...G', 'FADE..G', 'E.G....', '..EDGE.']
NUMS = {(0, 0): 1, (0, 2): 2, (0, 6): 3, (2, 0): 4, (4, 2): 5}
xw = ''.join((f'<div class="xc">' + (f'<span class="xn">{NUMS[(r, c)]}</span>' if (r, c) in NUMS else '') + '</div>') if ch != '.' else '<div class="xb"></div>' for r, row in enumerate(G) for c, ch in enumerate(row))
clue = lambda n, k: f'<div class="fc xcl"><span class="xq">{n}</span>{wpx(k, 74)}</div>'
P1 = gpage('Note crossword', 'Every clue is a word written in notes. Name the notes, then write the word in the grid, one letter per square. Watch the clef!',
           f'''<div class="xgrid">{xw}</div><div class="xwrap"><div><h3>Across</h3><div class="xcls">{clue("1", "x_CABBAGE")}{clue("4", "x_FADE")}{clue("5", "x_EDGE")}</div></div>
<div><h3>Down</h3><div class="xcls">{clue("1", "x_CAFE")}{clue("2", "x_BADGE")}{clue("3", "x_EGG")}</div></div></div>
<h3>Your turn</h3><p>Write a word of your own in notes for a friend to solve. Only the letters A to G can be used: try <b>BAGGAGE</b>, <b>DECADE</b> or <b>CABBAGE</b>.</p><div class="fc" style="height:96px">{wpx("blank_t", 70)}</div>
{ud("Across: CABBAGE, FADE, EDGE · Down: CAFE, BADGE, EGG")}''', 1)

# 2. Keyboard battleships
def bkb(title):
    W_, H_ = 24, 92
    marks = [f'<text x="{i * W_ + W_ / 2}" y="{H_ + 16}" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" fill="{C}">C{3 + i // 7}</text>' for i in (0, 7, 14)]
    return f'<div class="bsh"><div class="cl3">{title}</div>{kbd("C", 21, W_, H_, extra_h=22, marks=marks, scale=1.0)}</div>'
P2 = gpage('Keyboard battleships', 'For two players. Each player secretly hides a fleet on the top keyboard: one ship of 4 white keys, one of 3 and two of 2, each on keys side by side. Take turns calling a key by letter and octave (“D4!”). Hit or miss? Mark the bottom keyboard: X for a hit, O for a miss. Sink the whole fleet to win.',
           f'''<div class="bsg"><div><h3>Player 1</h3>{bkb("My fleet")}{bkb("Their fleet")}</div><div><h3>Player 2</h3>{bkb("My fleet")}{bkb("Their fleet")}</div></div>
<div class="rules"><div><b>Octave numbers:</b> C4 is middle C. Every key from one C up to the next B shares its number: C4 D4 E4 F4 G4 A4 B4.</div><div><b>Harder:</b> ships may sit on black keys too. Call them by either name, F♯3 or G♭3.</div><div><b>Hardest:</b> call by interval only. “A 5th above your last call.”</div></div>''', 2)

# 3. Scale trains
def train(engine, cars):
    out = []; x = 0
    out.append(f'<rect x="4" y="18" width="92" height="46" rx="6" fill="{N_}"/><rect x="60" y="4" width="26" height="22" fill="{N_}"/><text x="46" y="48" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="#fff">{engine}</text><circle cx="26" cy="70" r="7" fill="{N_}"/><circle cx="74" cy="70" r="7" fill="{N_}"/>')
    for i, L in enumerate(cars):
        x = 104 + i * 86
        out.append(f'<rect x="{x}" y="18" width="78" height="46" rx="4" fill="#fff" stroke="{N_}" stroke-width="2"/><text x="{x + 39}" y="50" text-anchor="middle" font-family="PF,serif" font-size="24" font-weight="700" fill="{N_}">{L}</text><circle cx="{x + 18}" cy="70" r="6" fill="none" stroke="{N_}" stroke-width="2"/><circle cx="{x + 60}" cy="70" r="6" fill="none" stroke="{N_}" stroke-width="2"/><rect x="{x - 4}" y="12" width="86" height="70" fill="none" stroke="#9a9cc4" stroke-width="1.2" stroke-dasharray="4 3"/>')
    return f'<figure class="vx trn"><svg viewBox="0 0 {104 + len(cars) * 86} 86" style="width:100%;height:auto;display:block">{"".join(out)}</svg></figure>'
P3 = gpage('Scale trains', 'Cut out the carriages along the dashed lines. Line them up behind the engine in scale order, starting on the key note. Then fix the train: write in every sharp or flat the scale needs.',
           f'''<h3>Train 1</h3>{train("G major", list("DGBEACF"))}<p class="add">Which carriage needs a sharp or flat? {BOX}</p>
<h3>Train 2</h3>{train("F major", list("CAEGBDF"))}<p class="add">Which carriage needs a sharp or flat? {BOX}</p>
<h3>Train 3</h3>{train("D major", list("ADFBGEC"))}<p class="add">Which carriages need a sharp or flat? {BOX} {BOX}</p>
<h3>Race</h3><p>Two players, two sets of the same train. First to line up the scale correctly and play it on the piano wins the round.</p>
{ud("G A B C D E F♯ · F G A B♭ C D E · D E F♯ G A B C♯")}''', 3)

# 4. Spot the difference
P4 = gpage('Spot the difference', 'The second tune was copied with five mistakes. Circle each one on the second staff, then write what changed. Play both tunes: can you hear every difference?',
           f'''<h3>The original</h3>{wpx("sd_a", 120)}<h3>The copy</h3>{wpx("sd_b", 120)}
{tbl(["", "Bar", "What changed"], [[str(i), BOX, LINE] for i in range(1, 6)], ["8%", "16%", "76%"])}
<h3>Your turn</h3><p>Copy a line from a piece you know, with three mistakes hidden in it, and swap with a friend.</p>
{ud("bar 1: A became B · bar 2: F became F♯ · bar 3: D became E · bar 3: F became A · bar 4: the last G became E")}''', 4)

# 5. Who am I? Key riddles
RID = ['I have one sharp, and I am major.', 'I have one flat. My key note is a semitone above E.', 'I have no sharps or flats, and I am minor.', 'I have two sharps. My relative minor is B minor.', 'I have two flats, and I am minor.', 'I have three sharps, and I am major.']
cards = ''.join(f'<div class="rid"><span class="rn">{i + 1}</span><p>{t}</p><div class="add">I am {LINE.replace("al", "al in")}</div></div>' for i, t in enumerate(RID))
kcards = ''.join(f'<div class="fc kc">{wpx(k, 70)}<span class="kl">{L}</span></div>' for L, k in zip('ABCDEF', ('ks2f', 'ks1s', 'ks3s', 'blank_t', 'ks2s', 'ks1f')))
P5 = gpage('Who am I?', 'Read each riddle and name the key. Then cut out the key signature cards and match each one to its riddle. Play the scale of every key you find.',
           f'<div class="rids">{cards}</div><h3>Key signature cards <span class="cut">✂ cut along the lines</span></h3><div class="kcs">{kcards}</div>'
           '<h3>Make one up</h3><p>Write a riddle of your own for a key and test it on a friend. Hint: give two clues, never the key note’s name.</p>'
           + ud('1 G major (B) · 2 F major (F) · 3 A minor (D) · 4 D major (E) · 5 G minor (A) · 6 A major (C)'), 5)

# 6. Frog hops: interval routes that spell words
ROUTES = [('D', ['down a 2nd', 'up a 6th', 'down a 2nd', 'down a 3rd']), ('C', ['down a 2nd', 'up a 4th', 'up a 4th', 'up a 4th']), ('G', ['down a 2nd', 'up a 3rd', 'up a 3rd', 'up a 3rd']), ('A', ['up a 2nd', 'down a 2nd', 'up a 4th', 'up a 4th', 'down a 3rd'])]
def route(i, start, hops):
    cells = f'<span class="hs"><b>start</b>{start}</span>' + ''.join(f'<span class="hp"><i>{h}</i>{BOX}</span>' for h in hops)
    return f'<div class="rt"><span class="rn">{i}</span><div class="hops">{cells}</div></div>'
frog = kbd('C', 14, 34, 100, label=True, scale=1.1)
P6 = gpage('Frog hops', 'The frog hops along the white keys. Start on the given key and follow each hop, counting letter names (both ends included). Write the key it lands on after every hop: the letters spell a word.',
           f'{frog}<div class="rts">' + ''.join(route(i + 1, s, h) for i, (s, h) in enumerate(ROUTES)) + '</div>'
           f'<div class="add">The words: 1 {BOX} 2 {BOX} 3 {BOX} 4 {BOX}</div><h3>Your turn</h3><p>Make a frog route that spells <b>BAG</b> or <b>EGG</b>. Give it to a friend, then play each route on the piano and sing the notes.</p>'
           + ud('CAGE · BEAD · FACE · BADGE'), 6)

css += f'''
.ffoot{{position:absolute;left:58px;right:58px;bottom:56px;display:flex;align-items:center;gap:12px;border-top:1.5px solid {N_};padding-top:9px;font-size:12px;color:#3d4080}} .ffoot span:last-child{{margin-left:auto;color:{MUTE};font-size:10.5px}}
.ud{{display:inline-block;transform:rotate(180deg)}} .cut{{font-size:12px;color:{MUTE};font-weight:400;margin-left:10px}} .cl3{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTE};margin:4px 0}}
.xwrap{{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:start}} .xgrid{{display:grid;grid-template-columns:repeat(7,44px);grid-auto-rows:44px;gap:2px;margin:12px auto 4px;width:max-content}} .xc{{position:relative;border:1.8px solid {N_};background:#fff}} .xb{{background:transparent}} .xn{{position:absolute;left:3px;top:1px;font-size:10px;font-weight:700;color:{C}}}
.xcls{{display:grid;grid-template-columns:1fr;gap:6px}} .xcl{{position:relative;padding:4px}} .xq{{position:absolute;left:6px;top:4px;font-weight:700;color:{C};font-size:14px}} .xcl .px{{border:0;padding:2px 2px 2px 26px}}
.bsg{{display:grid;grid-template-columns:1fr 1fr;gap:22px}} .bsh{{border:1px solid #e2ddd0;background:#fff;padding:6px 8px 4px;margin-bottom:8px}} .bsh .kbf{{border:0;padding:0;margin:0}}
.rules{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:12px;font-size:13.5px;line-height:1.45}}
.trn{{padding:6px 8px}} .rids{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}} .rid{{position:relative;border:1.5px solid {N_};background:#fff;padding:10px 12px 10px 38px;font-size:14.5px}} .rid p{{margin:0 0 8px}} .rid .add{{display:flex;align-items:flex-end;gap:6px;white-space:nowrap}} .rid .al.in{{flex:1;width:auto}} .rn{{position:absolute;left:10px;top:9px;font-family:PF;font-weight:700;font-size:20px;color:{C}}}
.kcs{{display:grid;grid-template-columns:repeat(3,1fr);border-top:1.5px dashed #9a9cc4;border-left:1.5px dashed #9a9cc4}} .kc{{position:relative;border:0;border-right:1.5px dashed #9a9cc4;border-bottom:1.5px dashed #9a9cc4;padding:16px 4px 4px}} .kc .px{{border:0}} .kl{{position:absolute;left:6px;top:3px;font-weight:700;color:{C}}}
.rts{{display:grid;gap:8px;margin:12px 0}} .rt{{position:relative;border:1px solid #e2ddd0;background:#fff;padding:8px 10px 8px 40px}} .rt .rn{{top:7px}} .hops{{display:flex;flex-wrap:wrap;gap:10px;align-items:flex-end}} .hs,.hp{{display:flex;flex-direction:column;align-items:center;gap:4px;font-size:13px}} .hs b{{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:{MUTE}}} .hs{{font-family:PF;font-size:24px;font-weight:700}} .hp i{{font-style:normal;color:{MUTE}}}
'''
open('/mnt/user-data/outputs/house-rooms/pitch-games.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{P1}{P2}{P3}{P4}{P5}{P6}</body></html>')
print('games ok')
