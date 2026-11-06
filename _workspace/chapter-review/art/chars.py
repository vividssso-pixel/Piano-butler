# Three character options for Piano Butler (two colours: navy + coral on paper), each in the same three scenes,
# plus the new hand drawings. Writes one SVG per drawing into svg/ and a preview page.
import os, math
N, C, P, F = '#26296b', '#e4572e', '#fffdf7', '#f6f0e1'
SW = 3.2
os.makedirs('svg', exist_ok=True)

def L(a, b, w=SW, c=N):
    return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
def PL(pts, w=SW, c=N, fill='none'):
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    return f'<polyline points="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w*2}" height="{h*2}">{body}</svg>'

# ---- heads / bodies per character -------------------------------------------------------------
def head(style, c, face=1, tilt=0):
    """c = head centre; face = +1 looks right, -1 left, 0 front"""
    x, y = c
    if style == 'A':   # round-head stick kid with a hair tuft
        s = f'<circle cx="{x}" cy="{y}" r="12.5" fill="{P}" stroke="{N}" stroke-width="{SW}"/>'
        s += f'<path d="M{x-4},{y-12} q4,-7 9,-3" fill="none" stroke="{N}" stroke-width="2.6" stroke-linecap="round"/>'
        if face == 0:
            s += f'<circle cx="{x-4.5}" cy="{y-1}" r="1.9" fill="{N}"/><circle cx="{x+4.5}" cy="{y-1}" r="1.9" fill="{N}"/>'
            s += f'<path d="M{x-4},{y+4} q4,4 8,0" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round"/>'
        else:
            s += f'<circle cx="{x+5*face}" cy="{y-2}" r="1.9" fill="{N}"/>'
            s += f'<path d="M{x+2*face},{y+5} q{3*face},2.5 {7*face},-1" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round"/>'
        return s
    if style == 'B':   # note-head kid: the head is a filled note head, the stem + a coral quaver flag is the ponytail
        ang = -20 * (face if face else 1)
        s = f'<ellipse cx="{x}" cy="{y}" rx="13.5" ry="10" transform="rotate({ang} {x} {y})" fill="{N}"/>'
        sx = x + (10 if face >= 0 else -10)
        s += L((sx, y - 4), (sx, y - 36), 2.8)
        s += f'<path d="M{sx},{y-36} q{9 if face >= 0 else -9},6 {11 if face >= 0 else -11},18 q-1,-7 {-8 if face >= 0 else 8},-10" fill="{C}" stroke="{C}" stroke-width="1.5" stroke-linejoin="round"/>'
        if face == 0:
            s += f'<circle cx="{x-4.5}" cy="{y-1}" r="2" fill="{P}"/><circle cx="{x+4.5}" cy="{y-1}" r="2" fill="{P}"/>'
        else:
            s += f'<circle cx="{x+5*face}" cy="{y-2}" r="2.1" fill="{P}"/>'
        return s
    return ''

def butler_body(top, bottom, face=1):
    """Little butler: one rounded body from top to bottom (cream), a small face, a coral bow tie"""
    (x1, y1), (x2, y2) = top, bottom
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    h = math.hypot(x2 - x1, y2 - y1); ang = math.degrees(math.atan2(y2 - y1, x2 - x1)) - 90
    s = f'<g transform="rotate({ang:.1f} {cx:.1f} {cy:.1f})">'
    s += f'<rect x="{cx-17}" y="{cy-h/2-6}" width="34" height="{h+12}" rx="17" fill="{F}" stroke="{N}" stroke-width="{SW}"/>'
    ey = cy - h / 2 + 8
    if face == 0:
        s += f'<circle cx="{cx-5}" cy="{ey}" r="2" fill="{N}"/><circle cx="{cx+5}" cy="{ey}" r="2" fill="{N}"/><path d="M{cx-4},{ey+5} q4,4 8,0" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round"/>'
    else:
        s += f'<circle cx="{cx+7*face}" cy="{ey}" r="2" fill="{N}"/><path d="M{cx+4*face},{ey+6} q{3*face},2.5 {7*face},-1" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round"/>'
    by = ey + 15
    s += f'<path d="M{cx-9},{by-5} L{cx},{by} L{cx-9},{by+5} Z M{cx+9},{by-5} L{cx},{by} L{cx+9},{by+5} Z" fill="{C}" stroke="{C}" stroke-width="1.4" stroke-linejoin="round"/><circle cx="{cx}" cy="{by}" r="2.4" fill="{C}"/>'
    return s + '</g>'

def figure(style, j, face=1):
    """j: dict of joints: neck, hip, head, shoulder, arms [[sh, el, wr, tip]...], legs [[hip, knee, ankle, toe]...]"""
    s = ''
    for leg in j['legs']:
        s += PL(leg)
    if style == 'C':
        for arm in j['arms']: s += PL(arm)
        s += butler_body(j['head'], j['hip'], face)
        return s
    s += L(j['neck'], j['hip'])
    for arm in j['arms']:
        s += PL(arm)
        tip = arm[-1]; s += f'<circle cx="{tip[0]}" cy="{tip[1]}" r="3.4" fill="{N}"/>'
    s += head(style, j['head'], face)
    return s

# ---- props --------------------------------------------------------------------------------------
def floor(w, y=162): return L((6, y), (w - 6, y), 2.2, '#c9c2ae')
def piano(x=150, y=58, w=56, floor_y=162, key_y=98):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{floor_y-y}" rx="3" fill="{F}" stroke="{N}" stroke-width="{SW}"/>'
    s += f'<rect x="{x-26}" y="{key_y}" width="{30}" height="9" rx="2" fill="{P}" stroke="{N}" stroke-width="2.4"/>'
    for i in range(1, 4): s += L((x - 26 + i * 7.5, key_y), (x - 26 + i * 7.5, key_y + 9), 1.4)
    return s
def stool(x1=46, x2=100, y=114, floor_y=162):
    return f'<rect x="{x1}" y="{y}" width="{x2-x1}" height="8" rx="3" fill="{F}" stroke="{N}" stroke-width="{SW}"/>' + L((x1 + 7, y + 8), (x1 + 7, floor_y)) + L((x2 - 7, y + 8), (x2 - 7, floor_y))

# ---- scenes -------------------------------------------------------------------------------------
def scene_sit(style):
    W, H = 220, 172
    j = {'hip': (76, 110), 'neck': (80, 64), 'head': (84, 47),
         'arms': [[(80, 70), (96, 92), (124, 92), (131, 99)]],
         'legs': [[(76, 110), (108, 112), (108, 158), (118, 158)]]}
    if style == 'C': j['head'] = (82, 46)
    body = floor(W) + stool() + piano() + figure(style, j, 1)
    body += f'<text x="8" y="91" font-size="8.5" font-weight="800" fill="{C}" font-family="Inter,sans-serif">key level</text>' + f'<line x1="8" y1="96" x2="124" y2="96" stroke="{C}" stroke-width="1.3" stroke-dasharray="4 4" opacity="0.8"/>'
    return svg(W, H, body)

def scene_balloon(style):
    W, H = 220, 172
    keys = f'<rect x="112" y="104" width="76" height="10" rx="2" fill="{P}" stroke="{N}" stroke-width="2.4"/>' + ''.join(L((112 + i * 9.5, 104), (112 + i * 9.5, 114), 1.3) for i in range(1, 8))
    j = {'hip': (80, 116), 'neck': (80, 72), 'head': (82, 55),
         'arms': [[(82, 78), (104, 96), (126, 86), (136, 103)], [(78, 78), (70, 100), (70, 120)]],
         'legs': [[(80, 116), (72, 138), (68, 160), (60, 160)], [(80, 116), (88, 138), (92, 160), (100, 160)]]}
    if style == 'C': j['head'] = (80, 50)
    balloon = f'<path d="M126,86 C132,62 150,52 152,38" fill="none" stroke="{N}" stroke-width="1.6"/>'
    balloon += f'<ellipse cx="154" cy="24" rx="13" ry="16" fill="{C}"/><path d="M151,40 l3,-4 l3,4 z" fill="{C}"/><ellipse cx="149" cy="18" rx="3" ry="5" fill="#fff" opacity="0.45"/>'
    body = floor(W) + keys + balloon + figure(style, j, 1)
    return svg(W, H, body)

def scene_dive(style):
    W, H = 220, 172
    board = f'<rect x="6" y="70" width="62" height="7" rx="2" fill="{F}" stroke="{N}" stroke-width="{SW}"/>' + L((18, 77), (18, 162)) + floor(W)
    wave = 'M90,142 q10,-7 20,0 t20,0 t20,0 t20,0 t20,0 t20,0'
    water = f'<path d="{wave} L210,162 L90,162 Z" fill="{F}"/>' + f'<path d="{wave}" fill="none" stroke="{N}" stroke-width="2.6" stroke-linecap="round"/>'
    arc = f'<path d="M66,62 Q96,30 132,74" fill="none" stroke="{N}" stroke-width="1.6" stroke-dasharray="3 5" opacity="0.6"/>'
    splash = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C}"/>' for x, y, r in [(150, 128, 3.2), (160, 120, 2.6), (140, 121, 2.4), (168, 130, 2), (132, 131, 2)])
    d = (0.62, 0.78); hip = (98, 64)
    at = lambda base, k, off=(0, 0): (base[0] + k * d[0] + off[0], base[1] + k * d[1] + off[1])
    neck = at(hip, 30); hd = at(neck, 15)
    if style == 'C': hd = at(neck, 12)
    j = {'hip': hip, 'neck': neck, 'head': hd,
         'arms': [[neck, at(neck, 20, (5, -3)), at(neck, 38, (5, -3)), at(neck, 44, (4, -2))], [neck, at(neck, 20, (-4, 3)), at(neck, 38, (-4, 3)), at(neck, 44, (-3, 3))]],
         'legs': [[hip, at(hip, -22, (-3, 3)), at(hip, -42, (-3, 3)), at(hip, -46, (-8, 2))], [hip, at(hip, -22, (4, -3)), at(hip, -42, (4, -3)), at(hip, -46, (-1, -6))]]}
    body = board + arc + water + splash + figure(style, j, 1)
    return svg(W, H, body)

def scene_stand(style):
    W, H = 120, 172
    j = {'hip': (60, 112), 'neck': (60, 68), 'head': (60, 51),
         'arms': [[(62, 74), (74, 92), (86, 80)], [(58, 74), (48, 94), (46, 114)]],
         'legs': [[(60, 112), (54, 136), (52, 160), (44, 160)], [(60, 112), (66, 136), (68, 160), (76, 160)]]}
    if style == 'C': j['head'] = (60, 46)
    return svg(W, H, floor(W) + figure(style, j, 0))

for st in 'ABC':
    for name, fn in [('stand', scene_stand), ('sit', scene_sit), ('balloon', scene_balloon), ('dive', scene_dive)]:
        open(f'svg/{st}-{name}.svg', 'w').write(fn(st))

# ---- the new hands (navy line, paper fill, coral only where it matters) --------------------------
def hand_side():
    W, H = 240, 140
    keys = f'<rect x="10" y="112" width="220" height="16" rx="3" fill="{P}" stroke="{N}" stroke-width="2.6"/>' + ''.join(L((10 + i * 22, 112), (10 + i * 22, 128), 1.4) for i in range(1, 10))
    ball = f'<circle cx="138" cy="84" r="20" fill="{C}"/><path d="M126,68 q8,16 0,32 M150,68 q-8,16 0,32" fill="none" stroke="#fff" stroke-width="2"/>'
    hand = (f'<path d="M8,56 L92,52 Q112,50 130,40 Q150,30 166,46 Q178,60 176,108 Q176,114 170,113 Q166,112 164,104 Q160,74 146,66 Q128,62 112,72 L92,76 L8,78 Z" '
            f'fill="{P}" stroke="{N}" stroke-width="{SW}" stroke-linejoin="round"/>')
    tip = f'<circle cx="171" cy="111" r="4.5" fill="{C}"/>'
    lab = (f'<path d="M140,22 L142,34" stroke="{C}" stroke-width="1.6"/><text x="104" y="18" font-size="10.5" font-weight="800" fill="{C}" font-family="Inter,sans-serif">knuckles: a bridge</text>'
           f'<text x="186" y="100" font-size="10.5" font-weight="800" fill="{C}" font-family="Inter,sans-serif">tip</text>'
           f'<text x="20" y="70" font-size="10" font-weight="700" fill="{N}" font-family="Inter,sans-serif">wrist level</text>')
    return svg(W, H, keys + ball + hand + tip + lab)

def hand_top(side):
    W, H = 150, 170
    R = side == 'R'
    xs = [44, 66, 88, 110] if R else [106, 84, 62, 40]   # fingers 2..5
    tops = [34, 24, 32, 48]
    s = ''
    palm_x = 30 if R else 24
    s += f'<rect x="{palm_x}" y="88" width="96" height="62" rx="24" fill="{P}" stroke="{N}" stroke-width="{SW}"/>'
    for i, (x, t) in enumerate(zip(xs, tops)):
        s += f'<rect x="{x-9}" y="{t}" width="18" height="{100-t}" rx="9" fill="{P}" stroke="{N}" stroke-width="{SW}"/>'
        s += f'<text x="{x}" y="{t+17}" text-anchor="middle" font-size="13" font-weight="900" fill="{C}" font-family="Inter,sans-serif">{i+2}</text>'
    tx = 34 if R else 116
    ang = -38 if R else 38
    s += f'<g transform="rotate({ang} {tx} 118)"><rect x="{tx-10}" y="72" width="20" height="52" rx="10" fill="{P}" stroke="{N}" stroke-width="{SW}"/></g>'
    # cover the joins so the palm reads as one shape
    s += f'<rect x="{palm_x+3}" y="92" width="90" height="20" fill="{P}"/>'
    a = math.radians(ang); nx, ny = tx + 34 * math.sin(a), 118 - 34 * math.cos(a)
    s += f'<text x="{nx:.1f}" y="{ny+5:.1f}" text-anchor="middle" font-size="13" font-weight="900" fill="{C}" font-family="Inter,sans-serif">1</text>'
    s += f'<text x="{palm_x+48}" y="134" text-anchor="middle" font-size="13" font-weight="800" fill="{N}" font-family="Inter,sans-serif">{"Right" if R else "Left"}</text>'
    return svg(W, H, s)

open('svg/hand-side.svg', 'w').write(hand_side())
open('svg/hand-L.svg', 'w').write(hand_top('L'))
open('svg/hand-R.svg', 'w').write(hand_top('R'))

# preview
rows = ''
for st, nm in [('A', 'A · Stick kid'), ('B', 'B · Note-head kid'), ('C', 'C · Little butler')]:
    rows += f'<h2>{nm}</h2><div class="row">' + ''.join(f'<div class="cell">{open(f"svg/{st}-{n}.svg").read()}<p>{n}</p></div>' for n in ['stand', 'sit', 'balloon', 'dive']) + '</div>'
rows += '<h2>New hands</h2><div class="row">' + ''.join(f'<div class="cell">{open(f"svg/{n}.svg").read()}</div>' for n in ['hand-side', 'hand-L', 'hand-R']) + '</div>'
open('preview.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;background:#fff;color:{N};margin:20px}} .row{{display:flex;gap:14px;align-items:flex-end;flex-wrap:wrap}} .cell{{background:{F};border-radius:12px;padding:8px}} .cell svg{{width:auto;height:200px;display:block}} p{{margin:4px 0 0;font-size:12px}}</style></head><body>{rows}</body></html>')
print('ok')
