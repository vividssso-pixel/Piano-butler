import json, re
d = json.load(open('/mnt/user-data/uploads/Piano Butler/Claude outputs/pb-art.json'))
CAMEO = open('/mnt/user-data/uploads/Piano Butler/Claude outputs/cameo.txt').read().strip()
N, C, G, CR = '#26296b', '#e4572e', '#2e8a6e', '#fffdf7'
# take the css of the v2 draft as the base
src = open('/tmp/claude-0/pk/book2.py').read()
base_css = src[src.index("css = f'''") + len("css = f'''"):src.index("'''\nfonts")]
base_css = base_css.replace('{{', '{').replace('}}', '}').replace('{N}', N).replace('{C}', C).replace('{CR}', CR)

def art(k, h=None, w=None):
    st = 'display:block;margin:0 auto;max-width:100%;' + (f'height:{h}px;' if h else '') + (f'width:{w}px;' if w else '')
    return d[k].replace('<svg ', f'<svg style="{st}" preserveAspectRatio="xMidYMid meet" ', 1)

def page(kind, inner, n, foot=''):
    return f'''<section class="pg"><div class="top"><span>PIANO BUTLER · {kind}</span><span>CHAPTER 1 · POSTURE AND HAND SHAPE</span></div><div class="rule"></div>
<div class="body">{inner}</div>{foot}<div class="foot"><span>{n}</span></div></section>'''
def sq(i): return f'<span class="sq{" dk" if i % 2 == 0 else ""}">{i}</span>'
def head(k, t, lead=''): return f'<div class="kick">{k}</div><h1>{t}</h1>' + (f'<p class="lead">{lead}</p>' if lead else '')
def note(t): return f'<div class="note"><img src="{CAMEO}" alt=""><div><span class="nl">The Butler’s note</span>{t}</div></div>'
def bar(lab, t, tail=''): return f'<div class="row5"><span class="gl">{lab}</span><span>{t}</span>{tail}</div>'
def frame(inner, cap=''): return f'<div class="frame">{inner}' + (f'<div class="cap">{cap}</div>' if cap else '') + '</div>'
def piano(items, title='At the piano'):
    return f'<div class="h3">{title}</div>' + ''.join(f'<div class="row">{sq(i + 1)}<span>{t}</span><span class="cb r"></span></div>' for i, t in enumerate(items))
def nots(items, h=92):
    return '<div class="h3 sm">Not like this</div><div class="nrow">' + ''.join(f'<div class="nc">{art(k, h)}<div class="nl2">✗ {l}</div></div>' for k, l in items) + '</div>'
DOTS = '<span class="dots">○ ○ ○ ○ ○</span>'

L = []
steps = [('Sit at the piano', 2), ('Let the arm carry the hand', 3), ('A round hand', 4), ('Finger numbers', 5), ('Play: finger walks', 6), ('My five checks', 7)]
cans = ['sit at the right height and distance', 'move your hand with the whole arm', 'make a round hand and play on the tips', 'say every finger number, on both hands']
L.append(page('LESSON BOOK', f'''
<div class="kick">Chapter 1</div><h1 class="big">Posture and hand shape</h1>
<p class="lead">First, learn to sit and hold your hands. Then every note is easier.</p>
{frame(art('puppet', 300), 'Sit tall, like a puppet on a string.')}
<div class="guess"><span class="gl">Guess first</span>Which finger is number 1? <span class="gans">answer on page 5</span></div>
<div class="two"><div><div class="h3">In this chapter</div>{''.join(f'<div class="row">{sq(i + 1)}<span>{s}</span><span class="pgn">{p}</span></div>' for i, (s, p) in enumerate(steps))}</div>
<div><div class="h3">After this chapter, I can</div>{''.join(f'<div class="row"><span class="cb"></span><span>{c}</span></div>' for c in cans)}</div></div>''', 1))

L.append(page('LESSON BOOK', f'''
{head('Step 1 of 6', 'Sit at the piano', 'Set two things: <b>how high</b> and <b>how far</b>. Forearm level with the keys, elbows just in front of you.')}
{frame(art('sit', 290))}
{piano(['Sit on the <b>front half</b> of the stool, feet flat on the floor, leaning a little toward the piano.', 'Raise or lower the stool until your <b>forearm is level</b> with the keys.', 'Slide in or out until your <b>elbows are just in front of you</b>, a fist from your sides.'])}
{nots([('not-sofa', 'Leaning back, like on a sofa'), ('not-close', 'So close the elbows squash in'), ('not-swing', 'Too high: feet swinging')])}
{bar('5 in a row', 'Ready in 5 seconds: front half of the stool, feet flat, sitting tall. Someone counts.', DOTS)}
{note('Front half of the stool, feet flat, sit tall, leaning a little forward.')}''', 2))

moves = [('ragdoll', 'Rag doll', 'Flop forward, arms hanging heavy. Shake them loose. Float the hands up onto the keys.'),
         ('wings', 'Elbow wings', 'Elbows free, not stuck to your body. Float them out like wings, then back. Stop a fist from your body.'),
         ('glide', 'Arm glide', 'Skate the whole arm along the keys. The round hand rides to the next group of keys. The fingers ride, they don’t walk.'),
         ('dive', 'Arm drop', 'Lift the whole arm and let it drop into a key on finger 3: firm tip, soft wrist, a round sound.'),
         ('bridge', 'Knuckle bridge', 'Your knuckles are a bridge a little car can drive over. Press one key slowly and hold for 3: the bridge stays up.'),
         ('balloon', 'Wrist balloon', 'The wrist never sinks: as the key goes down, a balloon lifts it back up to level. The fingertip stays on the key.')]
mv = ''.join(f'<div class="mv3"><div class="mvh">{sq(i + 1)}<b>{t}</b></div><div class="mvp">{art(k, 128)}</div><p>{x}</p></div>' for i, (k, t, x) in enumerate(moves))
L.append(page('LESSON BOOK', f'''
{head('Step 2 of 6', 'Let the arm carry the hand', 'The fingertips stay connected to the piano. The <b>whole arm</b> leads the hand and fingers from above. Six moves, <b>in this order</b>, big body parts to small. Each one sets up the next.')}
<div class="grid3">{mv}</div>
{bar('5 in a row', 'All six movements in order, without looking at the book.', DOTS)}
{note('The arm leads from above, elbows free. It stays free, even while a finger presses.')}''', 3))

L.append(page('LESSON BOOK', f'''
{head('Step 3 of 6', 'A round hand', 'Let your arms hang, then lift your hands as if holding a small ball. Keep that shape on the keys. <b>Knuckles up</b> like a bridge. Play on the <b>fingertips</b>. Keep the wrist free: with the tip on the key, the hand sways up and down and side to side, as if a roller sat under the forearm.')}
<div class="frame two-art"><div>{art('hand-good', 150)}<div class="cap">Round, like holding a ball</div></div><div>{art('hand-thumb', 150)}<div class="cap">The thumb plays on the side of its tip, like a tipped boat</div></div></div>
{piano(['Hands on your knees. Hold an imaginary ball.', 'Move the ball shape onto the keys without squashing it.', 'Play one key with each finger, on the tip. Knuckles stay up. The other fingers rest on their keys for balance.', 'Fingertip on a key: sway the wrist up and down, then side to side, as if on a roller.', 'Thumb in and out: slide the thumb in under fingers 2, 3 and 4, then back out. The hand stays round and still.'])}
{nots([('hand-flat', 'Flat fingers'), ('hand-cave', 'Tip joint caving in'), ('hand-high', 'Wrist stiff and high')], 70)}
{bar('5 in a row', 'One key with each finger, on the tip, knuckles up: not one knuckle caves in.', DOTS)}
{note('A free wrist, as if on a roller. Watch the knuckles and fingertips.')}''', 4))

L.append(page('LESSON BOOK', f'''
{head('Step 4 of 6', 'Finger numbers', 'Fingers are numbered <b>1 to 5, from the thumb</b>. Same on both hands: thumbs are 1, little fingers are 5. <span class="ans">(Page 1’s answer: the thumb.)</span>')}
<div class="frame two-art"><div>{art('hand-L', 230)}</div><div>{art('hand-R', 230)}</div></div>
<div class="names"><span><b>1</b> Captain Thumb</span><span><b>2</b> Pointer</span><span><b>3</b> Tall Middle</span><span><b>4</b> Shy Ring</span><span><b>5</b> Baby Pinky</span></div>
<div class="game"><div>{piano(['Hold both hands up. Wiggle each finger as you say its number.', 'Someone calls <b>“Right hand, 3!”</b> and you wiggle it. Try ten calls.', 'Swap: you call the finger, and they wiggle it.'], 'The mirror game')}</div><div class="gp">{art('mirror', 170)}</div></div>
{bar('Beat your time', 'Number race: someone calls “Left hand, 4!” and you wiggle it. How fast can you answer ten calls?', '<span class="times">___ s &nbsp; ___ s &nbsp; ___ s</span>')}
{note('Fingers are numbered 1 to 5 from the thumb, on both hands.')}''', 5))

def walk(k, name, sub, nums):
    cs = ''.join(f'<span class="c{" hold" if x == "_" else ""}">{"" if x == "_" else x}</span>' for x in nums)
    return f'<div class="walk"><div class="wp">{art(k, 70)}</div><div class="wt"><b>{name}</b><i>{sub}</i></div><div class="cs">{cs}</div></div>'
L.append(page('LESSON BOOK', f'''
{head('Step 5 of 6 · Play', 'Finger walks', 'Sit well, make a round hand, and play. Start small: one note, then two, three, four, five. Key to key, the hand draws <b>a little rainbow</b>. Relaxed, never squeezed: the whole hand helps. One circle is one steady beat.')}
<div class="frame two-art"><div>{art('keys-hand-L', 130)}</div><div>{art('keys-hand-R', 130)}</div></div>
{walk('tune-hop', 'Hop on 3', 'one note: an arm drop on every 3', ['3', '_', '3', '_', '3', '3', '3', '_'])}
{walk('tune-neighbours', 'Neighbours', 'two notes, next door, taking turns', ['2', '3', '2', '_', '3', '2', '3', '_'])}
{walk('tune-hill3', 'Up and back', 'three notes: up, then back down', ['1', '2', '3', '_', '3', '2', '1', '_'])}
{walk('tune-hill4', 'Little hill', 'four notes: up the hill and down', ['1', '2', '3', '4', '3', '2', '1', '_'])}
{walk('tune-stairs', 'Stairs and slide', 'all five: up the stairs, then down the slide', ['1', '2', '3', '4', '5', '5', '4', '3', '2', '1'])}
<div class="hint">An empty dashed circle: hold the note one more beat.</div>
{bar('5 in a row', '1 2 3 4 5 and back: a little rainbow over every key, shoulders soft.', DOTS)}
{note('A little rainbow from key to key. Relaxed: the whole hand helps.')}''', 6))

def chk(k, t): return f'<div class="chk"><div class="cp">{art(k, 74)}</div><div class="ct">{t}</div><div class="cc"><span></span><span></span><span class="st">★</span></div></div>'
L.append(page('LESSON BOOK', f'''
{head('Step 6 of 6 · Check-up', 'My five checks', 'Every time, before you play, tick each one: not yet, nearly, or got it! The check-up on paper is in the Workbook.')}
<div class="chkh"><span></span><span></span><span>not yet</span><span>nearly</span><span>got it!</span><span></span></div>
{chk('chk-front', 'Front half of the stool')}{chk('chk-feet', 'Feet flat, leaning a little toward the piano')}{chk('chk-tall', 'Sit tall, like a puppet on a string')}{chk('chk-forearm', 'Forearm level with the keys, elbows away from your body')}{chk('q-hand-good', 'Round hand, play on the tips')}
<div class="hint">Colour a circle each time it gets better: not yet, then nearly, then got it!</div>
{note('All five? Then this room is yours. On to the next one.')}''', 7))

# ---------- Workbook ----------
W = []
FEEL = '<div class="feel"><span>How did it feel? Circle one.</span><span class="fc">☺ &nbsp; ☹︎</span><span class="ckd">CHECKED <i></i></span></div>'
def qgrid(cells, h, cols=3):
    out = ''
    for i, (k, ex) in enumerate(cells):
        out += f'''<div class="qc{' ex' if ex else ''}"><span class="qn">{'EXAMPLE' if ex else i + 1}</span>{art(k, h)}<div class="yn"><span>✓</span><span class="{'ring' if ex else ''}">✗</span></div></div>'''
    return f'<div class="qg" style="grid-template-columns:repeat({cols},1fr)">{out}</div>'
def stars(items): return '<div class="stars">' + ''.join(f'<span>☆ {s}</span>' for s in items) + '</div>'

W.append(page('WORKBOOK', f'''
{head('Lesson step 1', 'Is this a good set-up?', 'Look at each picture, then try it at the piano. Circle the tick or the cross. The example is done.')}
{qgrid([('q-sit-low', True), ('q-sit-good', False), ('q-sit-high', False), ('q-sit-close', False), ('q-sit-far', False), ('not-sofa', False)], 112)}
<div class="h3" style="margin-top:14px">Draw yourself at the piano</div>
<p class="sub">Sitting tall, feet flat, leaning a little forward, elbows away from the body, round hands. Colour a star for each one you drew.</p>
<div class="drawbox"></div>{stars(['sitting tall', 'feet flat', 'leaning a little forward', 'elbows away from the body', 'round hands'])}''', 1, FEEL))

order = [('ragdoll', 'Rag doll', '1'), ('bridge', 'Knuckle bridge', ''), ('glide', 'Arm glide', ''), ('balloon', 'Wrist balloon', ''), ('wings', 'Elbow wings', ''), ('dive', 'Arm drop', '')]
oc = ''.join(f'<div class="oc{" ex" if n else ""}">{art(k, 96)}<div class="ol"><span>{t}</span><span class="ob">{n}</span></div></div>' for k, t, n in order)
yn = [('The arm leads from above.'), ('My elbows stay stuck to my body.'), ('Even while a finger presses a key, the whole arm stays free.'), ('After a key goes down, my wrist sinks below the keys.')]
W.append(page('WORKBOOK', f'''
{head('Lesson step 2', 'Put the warm-ups in order', 'Big parts of the body first, small parts last. Write 1 to 6 in the boxes. The first one is done.')}
<div class="og">{oc}</div>
<div class="h3" style="margin-top:16px">Yes or no?</div>
{''.join(f'<div class="row">{sq(i + 1)}<span>{t}</span><span class="yn2"><b>yes</b><b>no</b></span></div>' for i, t in enumerate(yn))}''', 2, FEEL))

W.append(page('WORKBOOK', f'''
{head('Lesson step 3', 'Spot the good hand', 'Circle the tick for a good hand shape and the cross for a fault. The example is done.')}
{qgrid([('q-hand-flat', True), ('q-hand-good', False), ('q-hand-nail', False), ('q-hand-bridge', False), ('q-hand-low', False), ('q-hand-high', False)], 80)}
<div class="h3" style="margin-top:14px">Hold the bubble</div>
<p class="sub">Hold a small ball (or a mandarin) in the hand you don’t draw with, fingers round it. Draw your hand round the ball: knuckles up, round fingers, playing on the tips, the thumb on its side.</p>
<div class="drawbox" style="height:300px"></div>{stars(['knuckles up', 'round fingers', 'playing on the tips', 'the thumb on its side'])}''', 3, FEEL))

W.append(page('WORKBOOK', f'''
{head('Lesson step 4', 'Number the fingers', 'Write the number on every finger. Thumbs are 1 on both hands!')}
<div class="frame two-art"><div>{art('q-fingers-L-plain', 220)}<div class="cap">Left</div></div><div>{art('q-fingers-R-plain', 220)}<div class="cap">Right</div></div></div>
<div class="h3" style="margin-top:12px">Trace your hands</div>
<p class="sub">Put each hand flat in its box and draw round it. Write the finger numbers on every finger, then draw a ring on each finger 4.</p>
<div class="two" style="gap:14px"><div class="drawbox" style="height:330px"></div><div class="drawbox" style="height:330px"></div></div>
<div class="checks"><span class="cb"></span>5 fingers on each hand <span class="cb"></span>Thumbs are 1 <span class="cb"></span>A ring on each finger 4 <span class="cb"></span>Left and right the right way round</div>''', 4, FEEL))

def miss(name, nums):
    cs = ''.join(f'<span class="c{" red" if x == "?" else ""}{" done" if x.startswith("!") else ""}">{x.strip("!?")}</span>' for x in nums)
    return f'<div class="walk"><div class="wt"><b>{name}</b></div><div class="cs">{cs}</div></div>'
def clue(t, lines, first):
    return f'<div class="clue"><b>{t}</b><ol>{"".join(f"<li>{x}</li>" for x in lines)}</ol><div class="cs">' + f'<span class="c done">{first}</span>' + '<span class="c"></span>' * 7 + '</div></div>'
W.append(page('WORKBOOK', f'''
{head('Lesson step 5', 'Fill in the missing numbers', 'Write the missing finger numbers in the red circles, then play the tune. The first one is done.')}
{miss('Up and back', ['1', '2', '!3', '3', '?', '1'])}{miss('Little hill', ['1', '2', '?', '4', '?', '2', '1'])}{miss('Stairs and slide', ['1', '2', '3', '?', '5', '5', '?', '3', '2', '1'])}
<div class="h3" style="margin-top:16px">The secret walks</div>
<p class="sub">Read the clues and write the finger numbers in the circles. Then play each walk with its hand. The first circle is done.</p>
<div class="two" style="gap:20px">{clue('1 · Right hand', ['Start on your thumb.', 'Walk up one finger at a time to your middle finger.', 'Jump to your little finger.', 'Walk back down, one finger at a time, all the way home to your thumb.'], '1')}
{clue('2 · Left hand', ['Start on your little finger.', 'Walk one finger at a time to your middle finger.', 'Jump to your thumb.', 'Walk back, one finger at a time, all the way to your little finger.'], '5')}</div>''', 5, FEEL))

W.append(page('WORKBOOK', f'''
<div class="kick">Check-up</div><h1>On paper</h1><div class="nameline">Name ____________ &nbsp; Date ________ &nbsp; · no help, no piano · about 10 minutes</div>
<div class="h3 sec">A &nbsp;A good set-up? Circle the tick or the cross.</div>
{qgrid([('q-sit-high', False), ('q-sit-good', False), ('q-sit-far', False), ('q-sit-close', False)], 92, 4)}
<div class="h3 sec">B &nbsp;A good hand shape? Circle the tick or the cross.</div>
{qgrid([('q-hand-bridge', False), ('q-hand-low', False), ('q-hand-good', False), ('q-hand-flat', False)], 58, 4)}
<div class="h3 sec">C &nbsp;Finger walks: write the missing number.</div>
{miss('', ['1', '2', '3', '?', '5'])}{miss('', ['5', '4', '?', '2', '1'])}{miss('', ['2', '3', '4', '?'])}{miss('', ['1', '?', '3', '2', '1'])}''', 6))

css = base_css + f'''
.h3.sm{{font-size:15px;margin:12px 0 4px}} .cb.r{{margin-left:auto;border-radius:50%}}
.nrow{{display:flex;gap:10px}} .nc{{flex:1;min-width:0;border:1px solid #e2ddd0;background:#fff;padding:6px 4px 6px}} .nl2{{text-align:center;color:{C};font-weight:700;font-size:11.5px;margin-top:2px}}
.row5 span:nth-child(2){{flex:1}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px 18px}} .mv3{{border-top:1.5px solid {N};padding-top:7px}} .mv3 p{{font-size:12.5px;line-height:1.45;color:#3d4080;margin:4px 0 0}} .mvp{{height:136px;display:flex;align-items:center}}
.two-art{{display:flex;justify-content:space-around;align-items:flex-end;gap:16px}} .two-art>div{{flex:1;min-width:0}}
.names{{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin:-2px 0 12px}} .names span{{border:1px solid {N};border-radius:16px;padding:3px 10px;font-size:13px;background:#fff}} .names b{{color:{C}}}
.game{{display:flex;gap:14px;align-items:center}} .game>div:first-child{{flex:1}} .gp{{flex:none;width:200px}}
.times{{margin-left:auto;color:#8a8cb0;font-size:13px;white-space:nowrap}} .ans{{color:#8a8cb0;font-size:13px}}
.walk{{display:flex;align-items:center;gap:12px;border-bottom:.6px solid #e2ddd0;padding:6px 0}} .wp{{flex:none;width:96px}} .wt{{flex:none;width:170px}} .wt b{{display:block;font-family:'Playfair Display',Georgia,serif;font-size:16px}} .wt i{{display:block;font-size:11.5px;color:#6d6f9c;font-style:normal}}
.cs{{display:flex;gap:5px;flex-wrap:wrap}} .cs .c{{width:28px;height:28px;border:2px solid {N};border-radius:50%;text-align:center;line-height:24px;font-weight:800;font-size:14px;background:#fff}} .cs .c.hold{{border-style:dashed;border-color:#9a9cc4}} .cs .c.red{{border-color:{C};background:#fdf0ec}} .cs .c.done{{color:{C}}}
.hint{{font-size:12.5px;color:#6d6f9c;margin:8px 0 0}}
.chkh{{display:grid;grid-template-columns:110px 1fr 44px 44px 44px 12px;gap:10px;font-size:10px;font-weight:900;letter-spacing:.12em;text-transform:uppercase;color:#8a8cb0;text-align:center}}
.chk{{display:grid;grid-template-columns:110px 1fr 174px;align-items:center;gap:10px;border-bottom:.6px solid #e2ddd0;padding:8px 0}} .ct{{font-size:15px;font-weight:600}} .cc{{display:flex;gap:10px}} .cc span{{width:44px;height:44px;border:1.8px solid #c9cbe0;border-radius:50%;display:flex;align-items:center;justify-content:center}} .cc .st{{color:{G};border-color:{G};font-size:20px}}
.feel{{position:absolute;left:60px;right:60px;bottom:62px;display:flex;align-items:center;gap:14px;border-top:.8px solid #c9cbe0;padding-top:8px;font-size:12px;color:#6d6f9c}} .fc{{font-size:18px}} .ckd{{margin-left:auto;font-size:10px;font-weight:900;letter-spacing:.14em;color:{G};display:flex;align-items:center;gap:6px}} .ckd i{{width:16px;height:16px;border:1.5px solid {G};display:inline-block}}
.sub{{font-size:13.5px;line-height:1.5;color:#3d4080;margin:0 0 8px}} .drawbox{{height:250px;border:1.5px solid {N};background:#fff}}
.stars{{display:flex;flex-wrap:wrap;gap:8px 14px;margin-top:8px;font-size:13px;color:#3d4080}}
.og{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}} .oc{{border:1.2px solid #d9d4c6;background:#fff;padding:8px}} .oc.ex{{border-color:{C};background:#fdf0ec}} .ol{{display:flex;align-items:center;justify-content:space-between;margin-top:6px;font-size:13.5px;font-weight:700}} .ob{{width:30px;height:30px;border:1.8px solid {N};text-align:center;line-height:27px;font:700 15px Georgia,serif;color:{C};background:#fff}}
.yn2{{margin-left:auto;display:flex;gap:8px}} .yn2 b{{border:1px solid #c9cbe0;border-radius:12px;padding:2px 10px;font-size:12px;color:#6d6f9c}}
.checks{{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:center;font-size:12.5px;margin-top:10px;color:#3d4080}}
.clue{{border-top:1.5px solid {N};padding-top:8px}} .clue b{{font-family:'Playfair Display',Georgia,serif;font-size:16px}} .clue ol{{font-size:13px;line-height:1.5;color:#3d4080;padding-left:18px;margin:6px 0 10px}}
.nameline{{font-size:12.5px;color:#6d6f9c;margin:-2px 0 6px}} .h3.sec{{font-size:15px;margin:14px 0 6px}}
'''
fonts = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">'
for nm, pages in (('lesson', L), ('work', W)):
    open(f'/mnt/user-data/outputs/house-rooms/ch1-v3-{nm}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8">{fonts}<style>{css}</style></head><body>{"".join(pages)}</body></html>')
print('ok', len(L), len(W))
