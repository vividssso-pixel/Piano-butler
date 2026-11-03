import json
from mq import *
d = json.load(open('/mnt/user-data/uploads/Piano Butler/Claude outputs/pb-art.json'))
CAMEO = open('/mnt/user-data/uploads/Piano Butler/Claude outputs/cameo.txt').read().strip()
G = '#2e8a6e'

def art(k, h):
    return d[k].replace('<svg ', f'<svg style="display:block;margin:0 auto;height:{h}px;max-width:100%" preserveAspectRatio="xMidYMid meet" ', 1)

def seat(label=True, **kw):
    H = (110 + kw.pop('hdx', 0), 190 + kw.pop('hdy', 0)); body, p = side(H, **kw); g = 280
    kx, ky = p['T'][0], p['T'][1] + 1
    s = ground_line(20, 330, g) + stool(H[0] - 34, H[0] + 22, H[1] + 10, g) + piano_side(kx, ky, g)
    if label: s += keyline(26, kx - 18, ky + 1) + f'<text x="26" y="{ky - 5:.0f}" font-family="Inter,Arial" font-size="11" font-weight="700" fill="{C}">key level</text>'
    return s + body

def stand(**kw):
    H = (90, 150); body, p = side(H, th=90, sh=90, foot=0, far=True, **kw)
    return ground_line(20, 170, 245) + body

def fr(*a, **k):
    return front_upper(*a, **k)[0]

def strip(frames, vb, h=120, labels=None):
    out = ''
    for i, f_ in enumerate(frames):
        if i: out += '<span class="arr">›</span>'
        lab = f'<i>{labels[i]}</i>' if labels else ''
        out += f'<div class="fr"><svg viewBox="{vb}" style="height:{h}px">{f_}</svg>{lab}</div>'
    return f'<div class="strip">{out}</div>'

def note(t):
    return f'<div class="note"><img src="{CAMEO}" alt=""><div><span class="nl">The Butler’s note</span>{t}</div></div>'

def page(kind, inner, n):
    return f'''<section class="pg"><div class="top"><span>PIANO BUTLER · {kind}</span><span>CHAPTER 1 · POSTURE AND HAND SHAPE</span></div><div class="rule"></div>
<div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'''

def sq(i, on=False): return f'<span class="sq{" dk" if (i % 2 == 0) else ""}">{i}</span>'

steps = ['Sit at the piano', 'Let the arm carry the hand', 'A round hand', 'Finger numbers', 'Play: finger walks', 'My five checks']
cans = ['sit at the right height and distance', 'move my hand with the whole arm', 'make a round hand and play on the tips', 'say every finger number, on both hands']

P1 = page('LESSON BOOK', f'''
<div class="kick">Chapter 1</div><h1 class="big">Posture and hand shape</h1>
<p class="lead">First, learn to sit and hold your hands. Then every note is easier.</p>
<div class="frame"><svg viewBox="0 52 340 236" style="height:330px">{seat(torso=-80, wr=(48, 40))}</svg><div class="cap">Sit tall, like a puppet on a string.</div></div>
<div class="guess"><span class="gl">Guess first</span>Which finger is number 1? <span class="gans">Answer on page 5</span></div>
<div class="two">
 <div><div class="h3">In this chapter</div>{''.join(f'<div class="row">{sq(i + 1)}<span>{s}</span><span class="pgn">{i + 2}</span></div>' for i, s in enumerate(steps))}</div>
 <div><div class="h3">After this chapter, I can</div>{''.join(f'<div class="row"><span class="cb"></span><span>{c}</span></div>' for c in cans)}</div>
</div>
''', 1)

# step 2: six moves, as on line
rag = strip([stand(torso=-90, wr=(4, 82)), stand(torso=8, neck=70, wr=(6, 84)), stand(torso=-90, wr=(56, 40))], '10 40 180 212', 118, ['hang', 'shake', 'float up'])
wings = strip([keyboard_front(10, 190, 138) + fr(100, 20, L=(-36, 120), R=(36, 120)), keyboard_front(10, 190, 138) + fr(100, 20, L=(-58, 112), R=(58, 112), bendL=1, bendR=-1)], '0 0 200 175', 108, ['in', 'out like wings'])
glide = strip([keyboard_front(10, 190, 138) + fr(100, 20, L=(-50, 120), R=(x, 120), bendR=1) for x in (8, 40, 72)], '0 0 200 175', 108, ['here', 'ride', 'there'])
drop = strip([seat(label=False, torso=-80, wr=w) for w in ((44, -4), (47, 18), (48, 40))], '60 52 200 236', 108, ['lift', 'drop', 'land on 3'])
bridge = f'<div class="strip"><div class="fr">{art("bridge", 108)}<i>press, hold for 3</i></div></div>'
balloon = f'<div class="strip"><div class="fr">{art("q-hand-low", 100)}<i class="x">not this: wrist sinks</i></div><span class="arr">›</span><div class="fr">{art("hand-good", 100)}<i>a balloon lifts it</i></div></div>'
moves = [('Rag doll', 'Flop forward, arms hanging heavy. Shake them loose. Float the hands up onto the keys.', rag),
         ('Elbow wings', 'Elbows free, not stuck to your body. Float them out like wings, then back. Stop a fist from your body.', wings),
         ('Arm glide', 'Skate the whole arm along the keys. The round hand rides to the next group of keys. The fingers ride, they don’t walk.', glide),
         ('Arm drop', 'Lift the whole arm and let it drop into a key on finger 3: firm tip, soft wrist, a round sound.', drop),
         ('Knuckle bridge', 'Your knuckles are a bridge a little car can drive over. Press one key slowly and hold for 3: the bridge stays up.', bridge),
         ('Wrist balloon', 'The wrist never sinks: as the key goes down, a balloon lifts it back up to level. The fingertip stays on the key.', balloon)]
mv = ''.join(f'<div class="mv"><div class="mvh">{sq(i + 1)}<b>{t}</b></div>{s}<p>{x}</p></div>' for i, (t, x, s) in enumerate(moves))
P3 = page('LESSON BOOK', f'''
<div class="kick">Step 2 of 6</div><h1>Let the arm carry the hand</h1>
<p class="lead">The fingertips stay connected to the piano. The <b>whole arm</b> leads the hand and fingers from above. Six moves, <b>in this order</b>, big body parts to small. Each one sets up the next.</p>
<div class="grid">{mv}</div>
<div class="row5"><span class="gl">5 in a row</span>All six moves in order, without looking at the book. <span class="dots">○ ○ ○ ○ ○</span></div>
{note('The arm leads from above, elbows free. It stays free, even while a finger presses.')}
''', 3)

# workbook page 1: the example is a fault
cells = [('EXAMPLE', seat(torso=-80, wr=(52, 18), hdy=24, th=-12, sh=82), False, 'Stool too low: the hands reach up.'),
         ('2', seat(torso=-80, wr=(48, 40)), None, ''),
         ('3', seat(torso=-80, wr=(70, 28)), None, ''),
         ('4', seat(torso=-80, wr=(48, 56), hdy=-22, th=18, sh=100), None, ''),
         ('5', seat(torso=-80, wr=(30, 40)), None, ''),
         ('6', seat(torso=-102, wr=(56, 44)), None, '')]
qc = ''
for lab, sv, ok, why in cells:
    ex = lab == 'EXAMPLE'
    qc += f'''<div class="qc{' ex' if ex else ''}"><span class="qn">{lab}</span><svg viewBox="0 52 340 236" style="height:150px">{sv}</svg>
<div class="yn"><span>✓</span><span class="{'ring' if ex else ''}">✗</span></div>{f'<div class="why">{why}</div>' if why else ''}</div>'''
W1 = page('WORKBOOK', f'''
<div class="kick">Lesson step 1</div><h1>Is this a good set-up?</h1>
<p class="lead">Look at each picture, then try it at the piano. Circle the tick or the cross. Check the forearm (level with the keys), the elbows (just in front of you) and the feet (flat).</p>
<div class="qg">{qc}</div>
<div class="row5"><span class="gl">Your turn</span>Sit at your own piano. Which picture are you? Ask someone to look from the side.</div>
''', 1)

css = f'''
@page {{ size: A4; margin: 0 }} *{{box-sizing:border-box}} body{{margin:0;background:#e9e4d8;font-family:Inter,Arial,sans-serif;color:{N}}}
.pg{{width:794px;height:1123px;background:{CR};margin:0 auto 24px;position:relative;overflow:hidden;padding:40px 60px 0;page-break-after:always}}
.top{{display:flex;justify-content:space-between;font-size:9px;font-weight:800;letter-spacing:.14em;color:#8a8cb0}}
.rule{{height:5px;border-top:1.5px solid {N};border-bottom:.6px solid {N};margin:7px 0 22px}}
.foot{{position:absolute;left:0;right:0;bottom:24px;text-align:center}} .foot span{{display:inline-block;width:26px;height:26px;line-height:26px;background:{N};color:#fff;font:700 13px Georgia,serif}}
.kick{{font-size:11px;font-weight:900;letter-spacing:.18em;text-transform:uppercase;color:{C}}}
h1{{font-family:'Playfair Display',Georgia,serif;font-size:34px;line-height:1.1;margin:4px 0 8px}} h1.big{{font-size:46px}}
.lead{{font-size:15.5px;line-height:1.55;color:#3d4080;margin:0 0 16px}}
.frame{{border:1.5px solid {N};outline:.6px solid {N};outline-offset:-6px;padding:16px;text-align:center;margin-bottom:14px}} .frame svg{{display:block;margin:0 auto}}
.cap{{font-family:'Playfair Display',Georgia,serif;font-style:italic;font-size:15px;color:#5a5d92;margin-top:4px}}
.guess{{display:flex;align-items:center;gap:12px;border-top:.8px solid #c9cbe0;border-bottom:.8px solid #c9cbe0;padding:10px 2px;font-size:15px;margin-bottom:18px}}
.gl{{font-size:10px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:{C};flex:none}} .gans{{margin-left:auto;font-size:12px;color:#8a8cb0;border-bottom:1px solid #c9cbe0;padding:0 0 1px 40px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:34px}} .h3{{font-family:'Playfair Display',Georgia,serif;font-style:italic;font-weight:700;font-size:18px;margin-bottom:6px}}
.row{{display:flex;align-items:center;gap:10px;font-size:14.5px;padding:6px 0;border-bottom:.6px solid #e2ddd0}} .pgn{{margin-left:auto;color:#8a8cb0;font-size:12px}}
.sq{{flex:none;display:inline-block;width:22px;height:22px;line-height:20px;text-align:center;border:1.5px solid {N};font:700 12px Georgia,serif;background:#fff}} .sq.dk{{background:{N};color:#fff}}
.cb{{flex:none;width:15px;height:15px;border:1.5px solid {N}}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px 28px}} .mv{{border-top:1.5px solid {N};padding-top:8px}} .mvh{{display:flex;align-items:center;gap:8px}} .mvh b{{font-family:'Playfair Display',Georgia,serif;font-size:19px}}
.mv p{{font-size:13px;line-height:1.5;color:#3d4080;margin:4px 0 0}}
.strip{{display:flex;align-items:flex-end;justify-content:center;gap:2px;margin:6px 0 2px;min-height:128px}} .fr{{text-align:center;min-width:0}} .fr svg{{display:block;margin:0 auto;max-width:100%}} .fr i{{display:block;font-size:10.5px;font-style:normal;font-weight:700;color:#6d6f9c;margin-top:2px}} .fr i.x{{color:{C}}}
.arr{{color:{C};font-size:20px;font-weight:700;align-self:center;padding:0 2px}}
.row5{{display:flex;align-items:center;gap:12px;border-top:.8px solid #c9cbe0;border-bottom:.8px solid #c9cbe0;padding:10px 2px;font-size:14.5px;margin:18px 0 14px}} .dots{{margin-left:auto;letter-spacing:4px;color:#9a9cc4;font-size:18px}}
.note{{display:flex;align-items:center;gap:14px}} .note img{{width:58px;height:72px;object-fit:contain;flex:none}}
.note div{{font-family:'Playfair Display',Georgia,serif;font-style:italic;font-size:17px;line-height:1.45}} .nl{{display:block;font-family:Inter,Arial;font-style:normal;font-size:10px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:{C}}}
.qg{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}} .qc{{position:relative;border:1.2px solid #d9d4c6;background:#fff;padding:22px 6px 8px;text-align:center}} .qc.ex{{border:1.5px solid {C};background:#fdf0ec}}
.qn{{position:absolute;left:8px;top:6px;font-size:11px;font-weight:900;letter-spacing:.1em}} .qc.ex .qn{{color:{C}}} .qc svg{{display:block;margin:0 auto;max-width:100%}}
.yn{{display:flex;justify-content:center;gap:24px;margin-top:4px}} .yn span{{width:32px;height:32px;line-height:30px;border-radius:50%;font-size:18px;font-weight:900;color:#9a9cc4}} .yn .ring{{border:2px solid {C};color:{C}}}
.why{{font-size:11px;color:{C};font-weight:700;margin-top:4px}}
'''
fonts = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">'
open('/mnt/user-data/outputs/house-rooms/ch1-v2.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8">{fonts}<style>{css}</style></head><body>{P1}{P3}{W1}</body></html>')
print('ok')
