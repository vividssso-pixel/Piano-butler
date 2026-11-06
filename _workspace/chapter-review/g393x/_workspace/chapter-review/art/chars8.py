# Phase 369: chapter 1 in pen and ink, with the storybook cast (Sohyun 2026-10-08: "pen-drawn, vintage";
# "rabbit piano butler like Alice, plus a sister and a brother"; "joints easier to see in the posture pictures").
#
# 1. Compose the drawings in the flat ink style (chars5 / chars6 helpers): the sister and the brother take turns
#    page by page, the rabbit butler works the puppet strings on the opener and calls the mirror game, and every
#    posture picture gets white joint dots (the joint the picture is about in coral).
# 2. Turn each one into pen and ink, baked into the geometry (no SVG filters, so the PDF stays vector and small):
#    big solid navy shapes become hatching with an outline, thick navy limbs become an outline with hatching inside,
#    and every long outline is resampled and nudged by a smooth noise field so it wobbles like a dip pen.
#    Small things (eyes, shoes, hair, heads) move rigidly with the field so they stay crisp and line up.
# 3. Write a3/art369.jsx: PB_ART + PbArt. Every child is drawn twice (girl and boy, one hidden), so ?kid=girl or
#    ?kid=boy prints every picture with one child, by CSS (PB_KID_CSS).
import re, math, json, os
import numpy as np
from svgpathtools import parse_path
import chars5, chars6
from chars5 import floor, piano, stool, keyrow, place, keylevel, handbase, J_SIT, add, J_STAND, J_WAVE, J_HOP
from chars6 import ell, dot, path, bowtie, glove, tailcoat, legs, metronome, limb
from chars import N, C, P, L, svg
import kids
from kids import KID

SERIF = "Georgia, 'Times New Roman', serif"
# Phase 393 (Sohyun 2026-10-09): only the characters look hand-drawn -- props (floor, stool, chair, metronome, rod and
# strings, balloon, boards, marks, tune icons) are drawn straight: the bake passes data-rigid elements through as they are.
def RG(svgtxt): return re.sub(r'<(line|rect|path|polyline|polygon|ellipse|circle)(?![^>]*data-rigid)', r'<\1 data-rigid="1"', svgtxt)
_floor, _stool, _keylevel, _metronome = floor, stool, keylevel, metronome
def floor(*a, **k): return RG(_floor(*a, **k))
def stool(*a, **k): return RG(_stool(*a, **k))
def keylevel(*a, **k): return RG(_keylevel(*a, **k))
def metronome(*a, **k): return RG(_metronome(*a, **k))
HAIR = set(kids.HAIR)
def inner(svgtxt): return re.sub(r'^<svg[^>]*>|</svg>$', '', svgtxt.strip())
def mplace(inner_, k, src, dst):   # place, mirrored left-right
    return f'<g transform="translate({dst[0] + src[0]*k:.2f} {dst[1] - src[1]*k:.2f}) scale({-k} {k})">{inner_}</g>'

# ---- the rabbit butler, with arms that can do things ------------------------------------------------------
RCX = 80
def rabbit(arm_l=None, arm_r=None, metro=True, d=7):
    """arm_l / arm_r: joint chains (shoulder, elbow, paw) in the rabbit's own frame; None = the standing pose"""
    cx = RCX; s = legs(feet=(11, 4.5))
    al = arm_l or [(cx - 17, 98), (cx - 27, 122), (cx - 22, 140)]
    ar = arm_r or [(cx + 17, 98), (cx + 28, 118), (cx + 16, 128)]
    lt = limb(al, 7, N) + glove(*add(al[-1], (0, 0)))
    rt = limb(ar, 7, N) + glove(*ar[-1])
    raised_l = al[-1][1] < 98
    if not raised_l: s += lt
    s += tailcoat()
    s += ell(70, 30 + d, 6.5, 22, P, 2.4, -8) + ell(91, 27 + d, 6.5, 23, P, 2.4, 10) + L((70.5, 18 + d), (69.5, 42 + d), 1.4) + L((90, 14 + d), (92, 38 + d), 1.4)
    s += ell(cx, 68 + d, 16, 18) + dot(73, 66 + d) + dot(87, 66 + d) + path(f'M{cx-2.6},{73+d} L{cx+2.6},{73+d} L{cx},{76+d} Z', fill=N, sw=1)
    s += ''.join(L((cx + sx * 5, 76 + d + dy), (cx + sx * 15, 74 + d + dy * 2), 1) for sx in (-1, 1) for dy in (0, 2.5))
    s += path(f'M{cx-10},92 L{cx},100 L{cx+10},92', fill='none', sw=2)
    s += bowtie(cx, 96)
    if raised_l: s += lt
    s += rt
    if metro and not arm_r: s += metronome(98, 122)
    return s
RABBIT_FOOT = (RCX, 202)

def rabbit_head():
    cx = 30; s = ''
    s += ell(22, 20, 5.2, 17, P, 2.2, -8) + ell(38, 18, 5.2, 18, P, 2.2, 10)
    s += ell(cx, 46, 14, 15) + dot(24, 44, 2) + dot(36, 44, 2) + path(f'M{cx-2.2},50 L{cx+2.2},50 L{cx},52.6 Z', fill=N, sw=1)
    s += ''.join(L((cx + sx * 4, 53 + dy), (cx + sx * 13, 51 + dy * 2), 0.9) for sx in (-1, 1) for dy in (0, 2.4))
    s += path(f'M{cx-8},62 L{cx},68 L{cx+8},62', fill='none', sw=1.8) + bowtie(cx, 64, 0.8)
    return svg(60, 74, s)

# ---- joints -----------------------------------------------------------------------------------------------
def joints(j, coral=(), skip=()):
    pts = {'shoulder': j['arms'][0][0], 'elbow': j['arms'][0][1], 'wrist': j['arms'][0][2], 'hip': j['legs'][0][0], 'knee': j['legs'][0][1], 'ankle': j['legs'][0][2]}
    s = ''
    for k, p in pts.items():
        if k in skip: continue
        s += f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="3.2" fill="{C if k in coral else P}" stroke="{N}" stroke-width="1.3"/>'
    return s
def label(x, y, t, anchor='start', size=8.5, col=C):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="800" fill="{col}" font-family="Inter,sans-serif">{t}</text>'

ART = {}
def put(name, w, h, body): ART[name] = svg(w, h, body)

# ---- 1. opener: the rabbit holds the girl up tall, like a puppet on a string -----------------------------
def opener():
    W, H, YF, DX = 270, 214, 204, 58
    scene = f'<g transform="translate({DX} {YF - 162})">{stool()}{piano()}{KID(J_SIT, 1, "girl")}</g>'
    head = (84 + DX, 53 + YF - 162)
    k = 0.86; rx = 56
    paw_local = (RCX + 30, 58)
    arm = [(RCX + 17, 98), (RCX + 31, 80), paw_local]
    rab = place(rabbit(arm_r=arm, metro=False), k, RABBIT_FOOT, (rx, YF))
    paw = (rx + (paw_local[0] - RABBIT_FOOT[0]) * k, YF - (RABBIT_FOOT[1] - paw_local[1]) * k)
    bar_y = head[1] - 46
    tip = (head[0], bar_y - 9)
    s = RG(L((6, YF), (W - 6, YF), 1.6, '#bdb7a6')) + rab + scene
    s += RG(f'<path d="M{paw[0]:.1f},{paw[1]+2:.1f} Q{(paw[0]+tip[0])/2:.1f},{tip[1]-14:.1f} {tip[0]:.1f},{tip[1]:.1f}" fill="none" stroke="{N}" stroke-width="2.6" stroke-linecap="round"/>')
    s += glove(paw[0], paw[1], 4.4)
    s += RG(L((tip[0], tip[1]), (tip[0], bar_y), 1.2))
    s += RG(f'<rect x="{head[0]-20}" y="{bar_y}" width="40" height="5" rx="2" fill="{N}"/><rect x="{head[0]-2.5}" y="{bar_y-6}" width="5" height="18" rx="2" fill="{N}"/>')
    s += RG(f'<line x1="{head[0]}" y1="{bar_y+12}" x2="{head[0]}" y2="{head[1]-10}" stroke="{C}" stroke-width="1.8" stroke-dasharray="3 3.5"/>')
    return svg(W, H, s)
ART['puppet'] = opener()

# ---- 2. sitting: the boy, joints marked; the three faults -------------------------------------------------
put('sit', 220, 172, floor(220) + keylevel() + stool() + piano() + KID(J_SIT, 1, 'boy') + joints(J_SIT, coral=('elbow', 'wrist'))
    + label(105, 72, 'elbow') + RG(f'<path d="M104,70 L99.5,86.5" stroke="{C}" stroke-width="1.2" stroke-linecap="round"/>')
    + label(130, 80, 'wrist') + RG(f'<path d="M129,78 L123,88" stroke="{C}" stroke-width="1.2" stroke-linecap="round"/>'))

J_SOFA = {'hip': (66, 108), 'neck': (50, 70), 'head': (45, 56),
          'arms': [[(53, 73), (84, 90), (118, 95), (125, 99)], [(49, 74), (80, 92), (114, 97)]],
          'legs': [[(68, 108), (100, 106), (104, 154)], [(64, 109), (95, 109), (97, 154)]]}
J_CLOSE = {'hip': (104, 110), 'neck': (106, 68), 'head': (108, 54),
           'arms': [[(108, 72), (99, 95), (121, 95), (127, 99)], [(104, 72), (96, 96), (117, 96)]],
           'legs': [[(106, 110), (128, 112), (126, 155)], [(102, 111), (124, 113), (121, 155)]]}
J_SWING = {'hip': (76, 96), 'neck': (80, 56), 'head': (83, 42),
           'arms': [[(82, 60), (96, 78), (121, 94), (127, 99)], [(78, 61), (92, 80), (117, 96)]],
           'legs': [[(78, 96), (104, 98), (100, 128)], [(73, 97), (97, 100), (92, 126)]]}
chair = (f'<path d="M30,64 L38,114" stroke="{N}" stroke-width="5" stroke-linecap="round"/><rect x="34" y="110" width="58" height="9" rx="3" fill="{P}" stroke="{N}" stroke-width="2.4"/>'
         + L((40, 119), (40, 162), 2.4) + L((86, 119), (86, 162), 2.4))
put('not-sofa', 220, 172, floor(220) + RG(chair) + piano() + KID(J_SOFA, 1, 'girl') + joints(J_SOFA, coral=('shoulder', 'hip')))
put('not-close', 220, 172, floor(220) + stool(78, 130) + piano() + KID(J_CLOSE, 1, 'boy') + joints(J_CLOSE, coral=('elbow',))
    + RG(f'<path d="M92,100 q-6,-4 -4,-10 M90,104 q-9,-3 -9,-12" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>'))
put('not-swing', 220, 172, floor(220) + stool(46, 100, 100) + piano() + KID(J_SWING, 1, 'girl') + joints(J_SWING, coral=('ankle',))
    + RG(f'<path d="M86,136 q8,6 18,0 M84,142 q10,7 22,0" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>'))

# ---- 3. the six warm-ups: the children take turns (hand pictures are shared with chars5) ------------------
for name in ['hand-L', 'hand-R']:
    ART[name] = chars5.ART[name]
# the thumb, seen from the front of the keyboard: it bends in and plays on the side of its tip (Sohyun 2026-10-08)
def thumb_front():
    s = ''
    for k in (0, 1, 3, 4, 5, 6):   # black keys behind
        s += RG(f'<rect data-solid="1" x="{6 + 24*(k+1) - 7}" y="88" width="14" height="16" rx="1.5" fill="{N}"/>')
    s += RG(f'<rect x="6" y="104" width="192" height="30" fill="{P}" stroke="{N}" stroke-width="2"/>' + ''.join(L((6 + 24*k, 104), (6 + 24*k, 134), 1.3) for k in range(1, 8)))
    s += f'<path d="M72,4 L136,4 L136,34 L72,34 Z" fill="{N}" stroke="{N}" stroke-width="2"/>'                      # sleeve, going away
    for cx in (66, 90, 114, 138):                                                                                  # fingers 2-5 on their keys
        s += limb([(cx, 52), (cx + 1.5, 78), (cx, 101)], 13, P, N, 1.8)
    s += limb([(64, 62), (32, 82), (42, 101)], 15, P, N, 1.9)                                                    # the thumb: out, then the tip bends in
    s += f'<rect x="54" y="26" width="98" height="40" rx="17" fill="{P}" stroke="{N}" stroke-width="2.2"/>'          # back of the hand
    s += ''.join(f'<path d="M{cx-6},{62} q6,5 12,0" fill="none" stroke="{N}" stroke-width="1.2"/>' for cx in (66, 90, 114, 138))
    s += f'<g transform="rotate(30 36 92)"><ellipse cx="34.5" cy="93" rx="3.4" ry="6.4" fill="{P}" stroke="{N}" stroke-width="1.3"/></g>'   # the nail, on its side
    s += f'<circle cx="40.5" cy="103.5" r="3.6" fill="{C}"/>'
    s += RG(f'<path d="M16,76 Q12,98 31,106" fill="none" stroke="{C}" stroke-width="2" stroke-linecap="round"/><path d="M26,101 L31,106 L24,108" fill="none" stroke="{C}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    s += RG(f'<g transform="translate(170 14) rotate(-24)"><path d="M-12,0 L12,0 L8,6 L-8,6 Z" fill="{P}" stroke="{N}" stroke-width="1.6"/><path d="M-1,-1 L-1,-14 L8,-2 Z" fill="{C}"/></g>')  # the tipped boat
    s += f'<text x="44" y="146" text-anchor="middle" font-size="9" font-weight="800" fill="{C}" font-family="Inter,sans-serif">the side of the tip</text>'
    return svg(204, 150, s)
ART['hand-thumb'] = thumb_front()
# the hand from the side, jointed, at the app's angles (handside.py)
from handside import hand_side
ART['hand-good'] = hand_side('good', ball=True)
ART['hand-flat'] = hand_side('flat', labels=False)
ART['hand-cave'] = hand_side('nail', labels=False)
ART['hand-high'] = hand_side('high', labels=False)
ART['bridge'] = hand_side('good', labels=False, faults=False, car=True)
ART['chk-hand'] = hand_side('good', labels=False, faults=False, ball=True, vb=(118, 72, 130, 80))
put('ragdoll', 150, 172, floor(150) + KID({'hip': (70, 104), 'neck': (90, 72), 'head': (100, 63),
    'arms': [[(89, 75), (90, 97), (89, 117), (89, 123)], [(85, 77), (84, 99), (83, 119)]],
    'legs': [[(72, 104), (73, 131), (74, 157)], [(68, 104), (66, 131), (64, 157)]]}, 1, 'girl')
    + RG(f'<path d="M80,128 l-4,4 l4,4 l-4,4 M98,128 l4,4 l-4,4 l4,4" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'))
put('glide', 220, 160, RG(L((6, 152), (214, 152), 1.6, '#bdb7a6')) + keyrow(112, 80, 10)
    + RG(''.join(L((x, y), (x + 18, y), 1.8, N) for x, y in [(8, 60), (14, 72), (8, 84)]))
    + KID({'hip': (64, 100), 'neck': (74, 60), 'head': (79, 46),
           'arms': [[(76, 64), (98, 74), (120, 75), (127, 79)], [(72, 64), (56, 78), (44, 90)]],
           'legs': [[(66, 100), (82, 120), (84, 140)], [(62, 100), (48, 119), (34, 133)]]}, 1, 'boy')
    + RG(f'<rect x="76" y="138" width="17" height="6" rx="3" fill="{N}"/><circle cx="79" cy="147" r="3" fill="{C}"/><circle cx="90" cy="147" r="3" fill="{C}"/>')
    + RG(f'<g transform="rotate(-22 34 133)"><rect x="26" y="131" width="17" height="6" rx="3" fill="{N}"/><circle cx="29" cy="140" r="3" fill="{C}"/><circle cx="40" cy="140" r="3" fill="{C}"/></g>'))
put('wings', 150, 172, floor(150) + KID({'hip': (75, 106), 'neck': (75, 64), 'head': (75, 49),
    'arms': [[(84, 67), (104, 76), (92, 90), (87, 92)], [(66, 67), (46, 76), (58, 90), (63, 92)]],
    'legs': [[(79, 106), (80, 132), (81, 157)], [(71, 106), (70, 132), (69, 157)]]}, 0, 'girl')
    + RG(f'<path d="M108,66 q5,4 4,12 M112,62 q8,6 6,18 M42,66 q-5,4 -4,12 M38,62 q-8,6 -6,18" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>')
    + RG(f'<path d="M112,24 q6,-6 12,0 q6,-6 12,0" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round"/>'))
put('balloon', 220, 172, floor(220) + keyrow(112, 104, 8)
    + RG(f'<path d="M124,80 C130,58 148,50 151,40" fill="none" stroke="{N}" stroke-width="1.6"/><ellipse cx="153" cy="25" rx="13" ry="16" fill="{C}"/><path d="M150,41 l3,-4 l3,4 z" fill="{C}"/><ellipse cx="148" cy="19" rx="3" ry="5" fill="#fff" opacity="0.45"/>')
    + KID({'hip': (80, 106), 'neck': (80, 64), 'head': (82, 50),
           'arms': [[(82, 67), (103, 86), (124, 80), (130, 102)], [(78, 68), (74, 88), (75, 106)]],
           'legs': [[(82, 106), (85, 132), (87, 157)], [(78, 106), (74, 132), (71, 157)]]}, 1, 'boy'))
dv = (0.62, 0.78); pp = (-dv[1], dv[0]); hip = (96, 60); nk = add(hip, dv, 36); hd = add(nk, dv, 13)
put('dive', 220, 172, RG(f'<rect x="6" y="70" width="62" height="7" rx="2" fill="{P}" stroke="{N}" stroke-width="2.6"/>' + L((18, 77), (18, 162), 2.6)) + floor(220)
    + RG(f'<path d="M64,60 Q92,24 124,64" fill="none" stroke="{N}" stroke-width="1.4" stroke-dasharray="3 5" opacity="0.6"/>')
    + RG(f'<path d="M90,142 q10,-7 20,0 t20,0 t20,0 t20,0 t20,0 t20,0" fill="none" stroke="{N}" stroke-width="2.4" stroke-linecap="round"/>')
    + RG(''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C}"/>' for x, y, r in [(156, 130, 3.2), (166, 122, 2.6), (146, 123, 2.4), (174, 132, 2), (138, 133, 2)]))
    + KID({'hip': hip, 'neck': nk, 'head': hd,
           'arms': [[add(nk, pp, 3), add(add(nk, dv, 20), pp, 5), add(add(nk, dv, 38), pp, 4), add(add(nk, dv, 44), pp, 4)],
                    [add(nk, pp, -3), add(add(nk, dv, 20), pp, -2), add(add(nk, dv, 38), pp, -1), add(add(nk, dv, 44), pp, -1)]],
           'legs': [[add(hip, pp, 3), add(add(hip, dv, -24), pp, 4), add(add(hip, dv, -46), pp, 4)], [add(hip, pp, -3), add(add(hip, dv, -24), pp, -3), add(add(hip, dv, -46), pp, -6)]]}, 1, 'girl'))

# ---- 5. the mirror game: the rabbit calls, the boy wiggles ------------------------------------------------
def mirror():
    W, H, YF = 240, 172, 160
    bro = KID({'hip': (70, 106), 'neck': (70, 66), 'head': (72, 52),
               'arms': [[(72, 69), (88, 72), (98, 56)], [(68, 70), (66, 90), (67, 106)]],
               'legs': [[(72, 106), (74, 132), (75, 157)], [(68, 106), (66, 132), (64, 157)]]}, 1, 'boy')
    k = 0.76
    arm = [(RCX - 17, 98), (RCX - 32, 82), (RCX - 36, 60)]
    rab = place(rabbit(arm_l=arm), k, RABBIT_FOOT, (184, YF))
    s = floor(W, YF + 2) + bro + rab
    s += RG(f'<path d="M100,46 q4,-6 2,-12 M106,50 q8,-8 4,-18" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>')
    s += label(120, 112, '"Right hand, 3!"', 'middle', 9.5)
    s += RG(f'<path d="M140,58 l-8,-3 M140,64 l-9,1 M141,70 l-7,4" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>')
    return svg(W, H, s)
ART['mirror'] = mirror()

# ---- 6. tune icons ----------------------------------------------------------------------------------------
def mini(j, face=1, k=0.42, at=(0, 0), src=(64, 157), who='girl'): return place(KID(j, face, who), k, src, at)
stairs = RG(''.join(f'<path d="M{8+i*10},{88-i*10} L{18+i*10},{88-i*10} L{18+i*10},{78-i*10}" fill="none" stroke="{N}" stroke-width="2.2" stroke-linejoin="round"/>' for i in range(4)))
put('tune-stairs', 120, 96, RG(L((4, 90), (116, 90), 1.4, '#bdb7a6')) + stairs
    + RG(f'<path d="M48,48 L56,48 C70,48 76,86 104,88" fill="none" stroke="{C}" stroke-width="3" stroke-linecap="round"/>') + mini(J_WAVE, 1, 0.3, (52, 48), who='girl'))
put('tune-hop', 120, 96, RG(L((4, 90), (116, 90), 1.4, '#bdb7a6')) + RG(f'<path d="M16,88 Q30,52 46,88 M48,88 Q62,52 78,88" fill="none" stroke="{C}" stroke-width="2" stroke-dasharray="3 3"/>')
    + mini(J_HOP, 1, 0.38, (92, 72), (64, 146), who='boy'))
put('tune-neighbours', 120, 96, RG(L((4, 90), (116, 90), 1.4, '#bdb7a6')) + mini(J_WAVE, 1, 0.38, (38, 90), who='girl')
    + mplace(KID(J_WAVE, 1, 'boy'), 0.38, (64, 157), (84, 90))
    + RG(f'<path d="M54,44 q7,-6 14,0" fill="none" stroke="{C}" stroke-width="2" stroke-linecap="round"/>'))

# small hills for the 3-note and 4-note tunes: up n steps and back down, a child on top
def hill(n, who):
    w = 10; x0 = (120 - (2 * n * w + w)) / 2; y0 = 88
    pts = [(x0, y0)]
    for i in range(n): pts += [(x0 + i * w, y0 - (i + 1) * 10), (x0 + (i + 1) * w, y0 - (i + 1) * 10)]
    top = y0 - n * 10; pts += [(x0 + (n + 1) * w, top)]
    for i in range(n): pts += [(x0 + (n + 1 + i) * w, top + (i + 1) * 10), (x0 + (n + 2 + i) * w, top + (i + 1) * 10)]
    d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    cx = x0 + (n + 0.5) * w
    return (RG(L((4, 90), (116, 90), 1.4, '#bdb7a6')) + RG(f'<path d="{d}" fill="none" stroke="{N}" stroke-width="2.2" stroke-linejoin="round"/>')
            + mini(J_WAVE, 1, 0.3, (cx, top), who=who))
put('tune-hill3', 120, 96, hill(3, 'girl'))
put('tune-hill4', 120, 96, hill(4, 'boy'))

# ---- 7. the five checks: the boy (page 1 opens with the girl, page 7 closes with the boy), joints marked, the joint each check is about in coral -----------------
def check(mark, coral=()):
    scene = f"{floor(220)}{stool()}{piano()}{KID(J_SIT, 1, 'boy')}{joints(J_SIT, coral=coral)}{RG(mark)}"
    return svg(150, 120, place(scene, 0.66, (126, 108), (75, 72)))
ART['chk-front'] = check(f'<rect x="62" y="113" width="38" height="5" rx="2" fill="{C}"/>', ('hip',))
ART['chk-feet'] = check(f'<line x1="94" y1="161" x2="124" y2="161" stroke="{C}" stroke-width="4" stroke-linecap="round"/><path d="M68,46 Q84,36 100,44 M95,39 L100,44 L93,47" fill="none" stroke="{C}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>', ('ankle',))
ART['chk-tall'] = check(f'<line x1="84" y1="42" x2="84" y2="4" stroke="{C}" stroke-width="2.4" stroke-dasharray="3 4"/>', ('shoulder', 'hip'))
ART['chk-forearm'] = check(f'<line x1="90" y1="88" x2="136" y2="88" stroke="{C}" stroke-width="2.4" stroke-dasharray="4 4"/>', ('elbow', 'wrist'))
# ---- the chapter 1 drill (the app's quiz), drawn with the same cast: no hints, every joint white -----------
J_LOW = {'hip': (76, 124), 'neck': (80, 82), 'head': (83, 67),
         'arms': [[(82, 85), (95, 107), (119, 100), (126, 98)], [(78, 86), (90, 108), (114, 101)]],
         'legs': [[(78, 124), (106, 117), (108, 155)], [(73, 125), (99, 119), (100, 155)]]}
J_FAR = {'hip': (60, 110), 'neck': (72, 70), 'head': (77, 56),
         'arms': [[(74, 73), (99, 86), (121, 94), (128, 98)], [(70, 74), (95, 88), (116, 96)]],
         'legs': [[(62, 110), (92, 111), (96, 155)], [(57, 111), (85, 113), (88, 155)]]}
def quiz_sit(stool_svg, j, who):
    return svg(220, 172, floor(220) + keylevel() + stool_svg + piano() + KID(j, 1, who) + joints(j))
ART['q-sit-good'] = quiz_sit(stool(), J_SIT, 'girl')
ART['q-sit-low'] = quiz_sit(stool(46, 100, 128), J_LOW, 'boy')
ART['q-sit-high'] = quiz_sit(stool(46, 100, 100), J_SWING, 'girl')
ART['q-sit-close'] = quiz_sit(stool(78, 130), J_CLOSE, 'boy')
ART['q-sit-far'] = quiz_sit(stool(30, 84), J_FAR, 'girl')
for pose in ('good', 'flat', 'bridge', 'nail', 'low', 'high'):
    ART['q-hand-' + pose] = hand_side(pose, labels=False, faults=False)
def fingers(sd, label=True):
    """a hand from above with no numbers; each finger carries data-f so PbArt(lit=n) can light one up"""
    R = sd == 'R'
    xs = [44, 66, 88, 110] if R else [106, 84, 62, 40]; tops = [34, 24, 32, 48]
    px0 = 30 if R else 24
    s = f'<rect x="{px0}" y="88" width="96" height="62" rx="24" fill="{P}" stroke="{N}" stroke-width="2.6"/>'
    for i, (x, t) in enumerate(zip(xs, tops)):
        s += f'<rect data-f="{i+2}" x="{x-9}" y="{t}" width="18" height="{100-t}" rx="9" fill="{P}" stroke="{N}" stroke-width="2.6"/>'
    tx = 34 if R else 116; ang = -38 if R else 38
    s += f'<g transform="rotate({ang} {tx} 118)"><rect data-f="1" x="{tx-10}" y="72" width="20" height="52" rx="10" fill="{P}" stroke="{N}" stroke-width="2.6"/></g>'
    s += f'<rect x="{px0+3}" y="92" width="90" height="20" fill="{P}"/>'
    s += f'<rect x="{px0+10}" y="142" width="76" height="30" rx="6" fill="{N}"/>'
    if label: s += f'<text x="{px0+48}" y="128" text-anchor="middle" font-size="12.5" font-weight="800" fill="{N}" font-family="Inter,sans-serif">{"Right" if R else "Left"}</text>'
    return svg(150, 176, s)
ART['q-fingers-L'] = fingers('L'); ART['q-fingers-R'] = fingers('R')
ART['q-fingers-L-plain'] = fingers('L', False); ART['q-fingers-R-plain'] = fingers('R', False)   # left or right? (check-up)
# ---- page 6: each hand from above with its fingertips on five white keys (left hand on the left, right on the right)
def keys_hand(sd):
    R = sd == 'R'
    x0, kw = 8, 22
    s = ''.join(f'<rect data-rigid="1" x="{x0 + k*kw}" y="10" width="{kw}" height="94" fill="{P}" stroke="{N}" stroke-width="1.8"/>' for k in range(7))
    for k in (0, 1, 3, 4, 5):
        s += f'<rect data-solid="1" data-rigid="1" x="{x0 + (k+1)*kw - 6.5}" y="10" width="13" height="56" rx="1.5" fill="{N}"/>'
    cxs = [x0 + k * kw + 11 for k in range(5)]
    nums = [1, 2, 3, 4, 5] if R else [5, 4, 3, 2, 1]
    tipy = {2: 80, 3: 75, 4: 80, 5: 88}
    palm = (30, 116) if R else (10, 96)
    # the thumb first, so the palm covers its base and it emerges from under the hand's edge
    # at a natural angle, like the Gray's-anatomy view (Sohyun 2026-10-09)
    tcx = cxs[0] if R else cxs[4]
    tbase = (palm[0] + 11, 148) if R else (palm[1] - 11, 148)
    tmid = (tcx + 5, 121) if R else (tcx - 5, 121)
    s += limb([tbase, tmid, (tcx, 100)], 13, P, N, 1.8)
    s += f'<rect x="{palm[0]}" y="112" width="{palm[1]-palm[0]}" height="62" rx="22" fill="{P}" stroke="{N}" stroke-width="2.4"/>'
    labels = ''
    for cx, n in zip(cxs, nums):
        if n == 1:
            ty = 100
        else:
            s += limb([(cx, 128), (cx, tipy[n])], 14, P, N, 1.8); ty = tipy[n]
        col = C if n == 1 else P; tc = '#fff' if n == 1 else N
        s += f'<circle cx="{cx}" cy="{ty + 7.5}" r="6.6" fill="{col}" stroke="{N}" stroke-width="1.2"/>'
        labels += f'<text x="{cx}" y="{ty + 11.2}" text-anchor="middle" font-size="9.5" font-weight="900" fill="{tc}" font-family="Inter,sans-serif">{n}</text>'
    s += f'<rect x="{palm[0]+3}" y="115" width="{palm[1]-palm[0]-6}" height="16" fill="{P}"/>'
    s += f'<rect x="{palm[0]+10}" y="166" width="{palm[1]-palm[0]-20}" height="24" rx="5" fill="{N}"/>'
    labels += f'<text x="{(palm[0]+palm[1])/2}" y="152" text-anchor="middle" font-size="11.5" font-weight="800" fill="{N}" font-family="Inter,sans-serif">{"Right hand" if R else "Left hand"}</text>'
    return svg(170, 192, s + labels)
ART['keys-hand-L'] = keys_hand('L'); ART['keys-hand-R'] = keys_hand('R')

ART['rabbit-head'] = rabbit_head()
ART['rabbit'] = svg(160, 210, rabbit())

# =========================================================================================================
# pen and ink, baked
# =========================================================================================================
HATCH_SP, HATCH_W = 3.2, 1.15
def to_pen(svgtxt):
    """flat ink -> pen and ink markers: big navy fills -> url(#HATCH), thick navy limbs -> outline + hatched core"""
    def limbfix(mm):
        el = mm.group(0); w = float(mm.group(1))
        if w < 6: return el
        a = el.replace(f'stroke-width="{mm.group(1)}"', f'stroke-width="{w + 0.4:.1f}"')
        b = el.replace(f'stroke="{N}"', 'stroke="url(#HATCH)"').replace(f'stroke-width="{mm.group(1)}"', f'stroke-width="{max(2.0, w - 3.4):.1f}"')
        return a + b
    svgtxt = re.sub(r'<polyline[^>]*stroke="#26296b" stroke-width="([\d.]+)"[^>]*/>', limbfix, svgtxt)
    def shapefix(mm):
        el = mm.group(0)
        if 'data-solid' in el: return el
        d = re.search(r' d="([^"]+)"', el)
        if d:
            if d.group(1) in HAIR: return el
            nums = [float(x) for x in re.findall(r'-?\d+\.?\d*', d.group(1))]
            xs, ys = nums[0::2], nums[1::2]
            if not xs or (max(xs) - min(xs)) * (max(ys) - min(ys)) < 260: return el
        else:
            w = re.search(r' width="([\d.]+)"', el); h = re.search(r' height="([\d.]+)"', el)
            if not (w and h) or float(w.group(1)) * float(h.group(1)) < 400: return el
        return el.replace(f'fill="{N}"', 'fill="url(#HATCH)"', 1)
    svgtxt = re.sub(r'<(?:path|rect)[^>]*fill="#26296b"[^>]*/>', shapefix, svgtxt)
    return svgtxt

# a smooth 2-D noise field: a few random plane waves, two octaves, like feTurbulence at baseFrequency ~0.035
def make_field(seed=7, sigma=0.55):
    rng = np.random.default_rng(seed)
    comps = []
    for _ in range(2):
        c = []
        for fmin, fmax, amp, n in [(0.016, 0.04, 1.0, 5), (0.05, 0.085, 0.45, 4)]:
            for _ in range(n):
                f = rng.uniform(fmin, fmax); th = rng.uniform(0, 2 * math.pi)
                c.append((2 * math.pi * f * math.cos(th), 2 * math.pi * f * math.sin(th), rng.uniform(0, 2 * math.pi), amp))
        norm = math.sqrt(sum(a * a / 2 for *_, a in c))
        comps.append([(kx, ky, ph, a * sigma / norm) for kx, ky, ph, a in c])
    def field(x, y):
        return tuple(sum(a * math.sin(kx * x + ky * y + ph) for kx, ky, ph, a in cc) for cc in comps)
    return field

def tf_parse(s):
    M = np.eye(3)
    for name, args in re.findall(r'(\w+)\(([^)]*)\)', s or ''):
        a = [float(x) for x in re.split(r'[\s,]+', args.strip()) if x]
        if name == 'translate': T = np.array([[1, 0, a[0]], [0, 1, a[1] if len(a) > 1 else 0], [0, 0, 1]])
        elif name == 'scale': sx = a[0]; sy = a[1] if len(a) > 1 else sx; T = np.diag([sx, sy, 1.0])
        elif name == 'rotate':
            t = math.radians(a[0]); c, si = math.cos(t), math.sin(t)
            R = np.array([[c, -si, 0], [si, c, 0], [0, 0, 1]])
            if len(a) == 3:
                T = np.array([[1, 0, a[1]], [0, 1, a[2]], [0, 0, 1]]) @ R @ np.array([[1, 0, -a[1]], [0, 1, -a[2]], [0, 0, 1]])
            else: T = R
        else: continue
        M = M @ T
    return M

ATTR = re.compile(r'([\w:-]+)="([^"]*)"')
GEOM = {'x', 'y', 'width', 'height', 'rx', 'ry', 'cx', 'cy', 'r', 'x1', 'y1', 'x2', 'y2', 'points', 'd'}
def geom_d(tag, a):
    f = lambda k, dflt=0.0: float(a.get(k, dflt))
    if tag == 'line': return f"M{f('x1')},{f('y1')} L{f('x2')},{f('y2')}", False
    if tag in ('polyline', 'polygon'):
        p = [float(v) for v in re.split(r'[\s,]+', a['points'].strip())]
        return 'M' + ' L'.join(f'{p[i]},{p[i+1]}' for i in range(0, len(p), 2)) + (' Z' if tag == 'polygon' else ''), tag == 'polygon'
    if tag == 'rect':
        x, y, w, h = f('x'), f('y'), f('width'), f('height'); rx = min(f('rx', a.get('ry', 0)), w / 2, h / 2); ry = min(f('ry', rx), h / 2)
        if rx <= 0: return f'M{x},{y} H{x+w} V{y+h} H{x} Z', True
        return (f'M{x+rx},{y} H{x+w-rx} A{rx},{ry} 0 0 1 {x+w},{y+ry} V{y+h-ry} A{rx},{ry} 0 0 1 {x+w-rx},{y+h} '
                f'H{x+rx} A{rx},{ry} 0 0 1 {x},{y+h-ry} V{y+ry} A{rx},{ry} 0 0 1 {x+rx},{y} Z'), True
    if tag in ('circle', 'ellipse'):
        cx, cy = f('cx'), f('cy'); rx = f('r') if tag == 'circle' else f('rx'); ry = f('r') if tag == 'circle' else f('ry')
        return f'M{cx-rx},{cy} A{rx},{ry} 0 1 0 {cx+rx},{cy} A{rx},{ry} 0 1 0 {cx-rx},{cy} Z', True
    return a['d'], 'z' in a['d'].lower()

def num(v):
    s = f'{v:.1f}'
    return '0' if s in ('-0.0', '0.0') else (s[:-2] if s.endswith('.0') else s)

def bake(svgtxt, uid, field, step=4.6, small=17):
    m = re.match(r'(<svg[^>]*>)(.*)</svg>\s*$', svgtxt, re.S)
    head, body = m.group(1), m.group(2)
    parts = re.split(r'(<text.*?</text>)', body, flags=re.S)
    out = []; stack = [np.eye(3)]; scales = set()
    def hatch_id(Mtot):
        s = math.sqrt(abs(np.linalg.det(Mtot[:2, :2])))
        key = int(round(s * 20)); scales.add(key)
        return f'url(#h{uid}{key})'
    for part in parts:
        if part.startswith('<text'): out.append(part); continue
        for tok in re.findall(r'<[^>]+>', part):
            mm = re.match(r'<(/?)(\w+)(.*?)(/?)>$', tok, re.S)
            close, tag, rest, selfc = mm.groups()
            if tag == 'g':
                if close: stack.pop(); out.append(tok); continue
                a = dict(ATTR.findall(rest)); stack.append(stack[-1] @ tf_parse(a.get('transform')))
                out.append(tok); continue
            if tag not in ('line', 'polyline', 'polygon', 'rect', 'circle', 'ellipse', 'path'):
                out.append(tok); continue
            a = dict(ATTR.findall(rest))
            Mel = stack[-1] @ tf_parse(a.get('transform'))
            if 'data-rigid' in a:   # keyboards: drawn straight, exactly as given (Sohyun 2026-10-09)
                out.append(tok.replace('data-rigid="1" ', '').replace('url(#HATCH)', hatch_id(Mel))); continue
            for k in ('fill', 'stroke'):
                if a.get(k) == 'url(#HATCH)': a[k] = hatch_id(Mel)
            d, closed = geom_d(tag, a)
            pth = parse_path(d)
            # global size
            samp = [pth.point(t) for t in np.linspace(0, 1, 9)] if pth.length() > 0 else [pth.start]
            g = [Mel @ np.array([z.real, z.imag, 1]) for z in samp]
            gx = [p[0] for p in g]; gy = [p[1] for p in g]
            keep = {k: v for k, v in a.items() if k not in GEOM}
            if tag in ('line', 'polyline') and 'fill' not in keep: keep['fill'] = 'none'
            attrs = ''.join(f' {k}="{v}"' for k, v in keep.items())
            if max(max(gx) - min(gx), max(gy) - min(gy)) < small or (tag == 'path' and a.get('d') in HAIR):
                # rigid: shift by the field at its centre, expressed in the parent frame
                cxg, cyg = (max(gx) + min(gx)) / 2, (max(gy) + min(gy)) / 2
                dg = np.array(field(cxg, cyg))
                dl = np.linalg.solve(stack[-1][:2, :2], dg)
                orig = tok.replace('url(#HATCH)', hatch_id(Mel)) if 'url(#HATCH)' in tok else tok
                out.append(f'<g transform="translate({num(dl[0])} {num(dl[1])})">{orig}</g>')
                continue
            inv = np.linalg.inv(Mel[:2, :2])
            sc = math.sqrt(abs(np.linalg.det(Mel[:2, :2]))) or 1
            dd = []
            for sub in pth.continuous_subpaths():
                pts = []
                for seg in sub:
                    n = max(1, int(math.ceil(seg.length() * sc / step)))
                    ts = np.linspace(0, 1, n + 1)
                    for i, t in enumerate(ts):
                        if pts and i == 0: continue
                        z = seg.point(t); pts.append((z.real, z.imag))
                isc = sub.isclosed()
                if isc and len(pts) > 2: pts = pts[:-1]
                q = []
                for x, y in pts:
                    gp = Mel @ np.array([x, y, 1]); dv = inv @ np.array(field(gp[0], gp[1]))
                    q.append((x + dv[0], y + dv[1]))
                r = [(round(x * 10), round(y * 10)) for x, y in q]
                rel = ''.join(pair((r[i][0] - r[i-1][0]) / 10, (r[i][1] - r[i-1][1]) / 10) for i in range(1, len(r)))
                dd.append('M' + num(q[0][0]) + ' ' + num(q[0][1]) + 'l' + rel.lstrip(' ') + ('z' if isc else ''))
            out.append(f'<path d="{"".join(dd)}"{attrs}/>')
    defs = '<defs>' + ''.join(
        f'<pattern id="h{uid}{k}" width="{num2(HATCH_SP*20/k)}" height="{num2(HATCH_SP*20/k)}" patternUnits="userSpaceOnUse" patternTransform="rotate(40)">'
        f'<rect width="{num2(HATCH_SP*20/k)}" height="{num2(HATCH_SP*20/k)}" fill="{P}"/><line x1="0" y1="0" x2="0" y2="{num2(HATCH_SP*20/k)}" stroke="{N}" stroke-width="{num2(HATCH_W*20/k)}"/></pattern>'
        for k in sorted(scales)) + '</defs>'
    return head + (defs if scales else '') + ''.join(out) + '</svg>'
def cnum(v):
    t = num(v)
    return t.replace('0.', '.', 1) if t.startswith('0.') else (t.replace('-0.', '-.', 1) if t.startswith('-0.') else t)
def pair(dx, dy):
    a, b = cnum(dx), cnum(dy)
    out = ('' if a.startswith('-') else ' ') + a
    out += ('' if b.startswith('-') or (b.startswith('.') and '.' in a) else ' ') + b
    return out
def num2(v): return f'{v:.2f}'.rstrip('0').rstrip('.')

field = make_field()
PEN = {}
for i, (k, v) in enumerate(ART.items()):
    PEN[k] = bake(to_pen(v), 'p' + re.sub(r'[^a-z0-9]', '', k)[:10], field)

if __name__ == '__main__':
    os.makedirs('svg', exist_ok=True)
    for k, v in PEN.items(): open(f'svg/pen8-{k}.svg', 'w').write(v)
    cells = ''.join(f'<div class="cell">{v}<p>{k} · {len(v)//1024} KB</p></div>' for k, v in PEN.items())
    open('preview8.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;margin:14px;background:#fff}} .row{{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}} .cell{{border:1px solid #eee6d6;border-radius:10px;padding:6px;background:#fffdf7}} .cell svg{{width:auto;height:200px;display:block}} p{{margin:2px 0 0;font-size:11px}}</style></head><body><div class="row">{cells}</div></body></html>')
    js = {k: re.sub(r' width="\d+" height="\d+">', '>', v, count=1).replace('<svg xmlns="http://www.w3.org/2000/svg" ', '<svg ') for k, v in PEN.items()}
    open('../a3/art369.jsx', 'w').write(
        '// Phase 369: chapter 1 drawings in pen and ink, with the storybook cast (the rabbit butler, a sister and a brother).\n'
        '// Generated from chars/chars8.py -- edit the generator, not this file. ?kid=girl or ?kid=boy prints every picture with one sibling.\n'
        'const PB_ART = ' + json.dumps(js, ensure_ascii=False, indent=0) + ';\n'
        "const PB_KID = (() => { try { const k = new URLSearchParams(location.search).get('kid'); return k === 'girl' || k === 'boy' ? k : ''; } catch (e) { return ''; } })();\n"
        "const PB_KID_CSS = ` .pbk-girl [data-who=girl], .pbk-boy [data-who=boy] { display: inline !important; } .pbk-girl [data-who=boy], .pbk-boy [data-who=girl] { display: none !important; }`;\n"
        'function PbArt({ name, h = 120, style, lit }) {\n'
        '  let s = PB_ART[name]; if (!s) return null;\n'
        '  if (lit) s = s.replace(new RegExp(\'(data-f="\' + lit + \'"[^>]*?)fill="#fffdf7"\'), \'$1fill="#e4572e"\');\n'
        '  const m = /viewBox="[\\d.-]+ [\\d.-]+ ([\\d.]+) ([\\d.]+)"/.exec(s); const w = m ? h * (+m[1]) / (+m[2]) : h;\n'
        "  return <span className={'pb-art' + (PB_KID ? ' pbk-' + PB_KID : '')} data-art={name} style={{display:'inline-block',lineHeight:0,width:w,height:h,flex:'0 0 auto',...style}} dangerouslySetInnerHTML={{__html: s.replace('<svg ', '<svg width=\"100%\" height=\"100%\" ')}}/>;\n"
        '}\n')
    print(len(PEN), 'drawings;', sum(len(v) for v in js.values()) // 1024, 'KB')
