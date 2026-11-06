# Round 6: "pen and ink". The same cast and the house, redrawn so the lines wobble like a dip pen,
# solid navy becomes hatching (vintage engraving look, and much less ink), small things stay solid
# (hair, shoes, eyes), coral stays for the thing being learnt. Labels stay crisp (outside the wobble).
import re, math, random, html
from chars import N, C, P

def defs(uid, seed=3, wob=2.2, freq=0.035):
    return (f'<defs>'
            f'<filter id="pen{uid}" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="2" seed="{seed}" result="n"/>'
            f'<feDisplacementMap in="SourceGraphic" in2="n" scale="{wob}" xChannelSelector="R" yChannelSelector="G"/></filter>'
            f'<pattern id="h{uid}" width="3.2" height="3.2" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="3.2" height="3.2" fill="{P}"/><line x1="0" y1="0" x2="0" y2="3.2" stroke="{N}" stroke-width="1.15"/></pattern>'
            f'<pattern id="x{uid}" width="3" height="3" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="3" height="3" fill="{P}"/><line x1="0" y1="0" x2="0" y2="3" stroke="{N}" stroke-width="1.1"/><line x1="0" y1="0" x2="3" y2="0" stroke="{N}" stroke-width="0.9"/></pattern>'
            f'<pattern id="l{uid}" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><line x1="0" y1="0" x2="0" y2="5" stroke="{N}" stroke-width="0.8"/></pattern>'
            f'</defs>')

def pen(svgtxt, uid, wob=2.0):
    """turn an ink drawing into pen and ink: solid navy shapes -> hatched with an outline; thick navy limbs -> outlined + hatched"""
    m = re.match(r'(<svg[^>]*>)(.*)</svg>\s*$', svgtxt, re.S)
    head, body = m.group(1), m.group(2)
    texts = ''.join(re.findall(r'<text.*?</text>', body, re.S))
    body = re.sub(r'<text.*?</text>', '', body, flags=re.S)
    def limbfix(mm):
        el = mm.group(0); w = float(mm.group(1))
        if w < 6: return el
        inner = max(2.0, w - 3.2)
        a = el.replace(f'stroke-width="{mm.group(1)}"', f'stroke-width="{w + 0.4:.1f}"')
        b = el.replace(f'stroke="{N}"', f'stroke="url(#h{uid})"').replace(f'stroke-width="{mm.group(1)}"', f'stroke-width="{inner:.1f}"')
        return a + b
    body = re.sub(r'<polyline[^>]*stroke="#26296b" stroke-width="([\d.]+)"[^>]*/>', limbfix, body)
    # big solid shapes (jumpers, coats, penguin body) -> hatch with outline; leave small dots/ellipses solid
    def shapefix(mm):
        el = mm.group(0)
        d = re.search(r' d="([^"]+)"', el)
        if not d: return el
        nums = [float(x) for x in re.findall(r'-?\d+\.?\d*', d.group(1))]
        xs, ys = nums[0::2], nums[1::2]
        if not xs or (max(xs) - min(xs)) * (max(ys) - min(ys)) < 260: return el
        return el.replace(f'fill="{N}"', f'fill="url(#h{uid})"', 1)
    body = re.sub(r'<path[^>]*fill="#26296b"[^>]*/>', shapefix, body)
    return head + defs(uid) + f'<g filter="url(#pen{uid})">{body}</g>' + texts + '</svg>'

src = {k: open(f'svg/{k}.svg').read() for k in ['k-girl-joints', 'k-boy', 'k-girl', 'b-rabbit', 'b-penguin', 'e-balloon', 'e-dive', 'e-glide', 'e-hand-good', 'e-mirror', 'e-not-sofa']}
OUT = {}
for i, (k, v) in enumerate(src.items()):
    OUT['pen-' + k] = pen(v, f'p{i}')

# ---- the house, drawn in pen ------------------------------------------------------------------------
hs = open('../charcanvas/project/House.dc.html').read()
rooms = re.findall(r'>(\d+)</span><span style="font-size: 12px; font-weight: 700; line-height: 1.2">(.*?)</span></div>\s*(?:<div[^>]*>\s*)?(<svg width="58" height="40".*?</svg>)', hs, re.S)
R = {int(n): (html.unescape(name), icon) for n, name, icon in rooms}
FLOORS = [(7, 'Know the music', [22, 23, 24, 25]), (6, 'Making music', [17, 18, 19, 20, 21]), (5, 'Theory', [13, 14, 15, 16]),
          (4, 'Reading tunes', [11, 12]), (3, 'Rhythm', [7, 8, 9, 10]), (2, 'Reading notes', [4, 5, 6]), (1, 'Getting started', [1, 2, 3])]
SERIF = "Georgia, 'Times New Roman', serif"
def icon_inner(svg):
    return re.sub(r'^<svg[^>]*>|</svg>$', '', svg.strip())

def house(uid='hh'):
    X0, W, ST, FH, TOP = 150, 900, 140, 112, 160
    art, txt = '', ''
    # roof with hatched tiles, a plaque, a chimney with a curl of smoke
    art += f'<rect x="{X0+700}" y="40" width="30" height="62" fill="url(#x{uid})" stroke="{N}" stroke-width="2.4"/>'
    art += f'<path d="M{X0+716},36 c-10,-10 8,-14 0,-24 c-8,-10 10,-12 4,-22" fill="none" stroke="{N}" stroke-width="1.6"/>'
    art += f'<polygon points="{X0},{TOP} {X0+70},{TOP-90} {X0+830},{TOP-90} {X0+900},{TOP}" fill="url(#h{uid})" stroke="{N}" stroke-width="3" stroke-linejoin="round"/>'
    art += f'<rect x="{X0+320}" y="{TOP-78}" width="260" height="64" rx="10" fill="{P}" stroke="{N}" stroke-width="2.4"/>'
    art += f'<path d="M{X0+430},{TOP-70} L{X0+447},{TOP-62} L{X0+430},{TOP-54} Z M{X0+470},{TOP-70} L{X0+453},{TOP-62} L{X0+470},{TOP-54} Z" fill="none" stroke="{N}" stroke-width="2.2" stroke-linejoin="round"/><circle cx="{X0+450}" cy="{TOP-62}" r="3.4" fill="{C}"/>'
    txt += f'<text x="{X0+450}" y="{TOP-26}" text-anchor="middle" font-family="{SERIF}" font-size="26" font-weight="700" font-style="italic" fill="{N}">Piano Butler</text>'
    for wx in (210, 690):
        art += f'<circle cx="{X0+wx}" cy="{TOP-42}" r="17" fill="{P}" stroke="{N}" stroke-width="2.4"/><path d="M{X0+wx-17},{TOP-42} H{X0+wx+17} M{X0+wx},{TOP-59} V{TOP-25}" stroke="{N}" stroke-width="1.5"/>'
    y = TOP
    for fi, (no, name, chs) in enumerate(FLOORS):
        right = (no % 2 == 1)
        # floor box and slab
        art += f'<rect x="{X0}" y="{y}" width="{W}" height="{FH}" fill="{P}" stroke="{N}" stroke-width="3"/>'
        art += f'<rect x="{X0}" y="{y+FH-7}" width="{W}" height="7" fill="url(#x{uid})" stroke="{N}" stroke-width="1.6"/>'
        art += f'<line x1="{X0+ST}" y1="{y}" x2="{X0+ST}" y2="{y+FH-7}" stroke="{N}" stroke-width="2.2"/>'
        # stairs, with hatching under the flight
        steps = []
        for k in range(8):
            sx = 6 + k * 16; sy = FH - 9 - k * 11
            steps += [(sx, sy + 11 if k else FH - 7), (sx, sy)] if k == 0 else [(sx, sy + 11), (sx, sy)]
            steps.append((sx + 16, sy))
        pts = [(X0 + (x if right else ST - x), y + yy) for x, yy in steps]
        under = pts + [(pts[-1][0], y + FH - 7), (pts[0][0], y + FH - 7)]
        art += f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in under)}" fill="url(#l{uid})" stroke="none"/>'
        art += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{N}" stroke-width="2" stroke-linejoin="round"/>'
        hx1, hx2 = (X0 + 4, X0 + 132) if right else (X0 + ST - 4, X0 + ST - 132)
        art += f'<line x1="{hx1}" y1="{y+FH-30}" x2="{hx2}" y2="{y+2}" stroke="{N}" stroke-width="1.4"/>'
        lx, anchor = (X0 + 8, 'start') if right else (X0 + ST - 8, 'end')
        txt += f'<text x="{lx}" y="{y+17}" text-anchor="{anchor}" font-family="{SERIF}" font-size="12" font-weight="700" fill="{N}">{no} · {html.escape(name)}</text>'
        # rooms
        rw = (W - ST) / len(chs)
        for ri, ch in enumerate(chs):
            rx = X0 + ST + ri * rw
            if ri: art += f'<line x1="{rx:.1f}" y1="{y}" x2="{rx:.1f}" y2="{y+FH-7}" stroke="{N}" stroke-width="2.2"/>'
            if ch == 1: art += f'<rect x="{rx+1.5:.1f}" y="{y+1.5}" width="{rw-3:.1f}" height="{FH-10}" fill="#fde9e1"/>'
            # a little picture rail and a lamp on a cord, for dollhouse charm
            art += f'<line x1="{rx+rw/2:.1f}" y1="{y}" x2="{rx+rw/2:.1f}" y2="{y+10}" stroke="{N}" stroke-width="1"/><path d="M{rx+rw/2-6:.1f},{y+16} Q{rx+rw/2:.1f},{y+8} {rx+rw/2+6:.1f},{y+16} Z" fill="{N}"/>'
            name_, icon = R[ch]
            cc = C if ch == 1 else N
            art += f'<circle cx="{rx+16:.1f}" cy="{y+20}" r="10" fill="{P}" stroke="{cc}" stroke-width="2"/>'
            txt += f'<text x="{rx+16:.1f}" y="{y+24.5}" text-anchor="middle" font-family="{SERIF}" font-size="12" font-weight="700" fill="{cc}">{ch}</text>'
            words = name_.split(' ')
            lines, cur = [], ''
            for w in words:
                if len(cur + ' ' + w) > (13 if rw < 160 else 19) and cur: lines.append(cur); cur = w
                else: cur = (cur + ' ' + w).strip()
            lines.append(cur)
            for li, ln in enumerate(lines[:3]):
                txt += f'<text x="{rx+31:.1f}" y="{y+24 + li*14}" font-family="{SERIF}" font-size="12" font-style="italic" fill="{N}">{html.escape(ln)}</text>'
            art += f'<g transform="translate({rx+rw/2-29:.1f} {y+FH-52}) scale(1.2)" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{icon_inner(icon).replace(chr(10), "")}</g>'
            if ch == 1: txt += f'<text x="{rx+rw-8:.1f}" y="{y+FH-14}" text-anchor="end" font-family="{SERIF}" font-size="11" font-style="italic" font-weight="700" fill="{C}">you are here</text>'
        y += FH
    # ground with grass, the kids on the first flight, the butler by the door
    art += f'<path d="M20,{y+2} H{X0+W+30}" stroke="{N}" stroke-width="2"/>' + ''.join(f'<path d="M{gx},{y+2} l2,-6 M{gx+4},{y+2} l-1,-5" stroke="{N}" stroke-width="1"/>' for gx in range(26, X0 + W + 20, 23))
    return art, txt, y + 12

art, txt, H = house()
kid_b = re.sub(r'^<svg[^>]*>|</svg>$', '', open('svg/k-boy.svg').read().strip())
kid_g = re.sub(r'^<svg[^>]*>|</svg>$', '', open('svg/k-girl.svg').read().strip())
rab = re.sub(r'^<svg[^>]*>|</svg>$', '', open('svg/b-rabbit.svg').read().strip())
y1 = 160 + 6 * 112
extra = (f'<g transform="translate({150+8} {y1+18}) scale(0.44)">{kid_b}</g>'
         f'<g transform="translate({150+42} {y1-6}) scale(0.44)">{kid_g}</g>'
         f'<g transform="translate(4 {H-12-214*0.78}) scale(0.78)">{rab}</g>')
def fix_inner(s, uid):   # the same pen treatment for the cast placed inside the house drawing
    tmp = pen(f'<svg viewBox="0 0 10 10">{s}</svg>', uid)
    return re.sub(r'^<svg[^>]*>|</svg>$', '', tmp)
cast = fix_inner(extra, 'hc')
OUT['pen-house'] = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 {H}" width="1080" height="{H}">' + defs('hh', seed=5, wob=2.4)
                    + f'<g filter="url(#penhh)">{art}</g>' + cast + txt + '</svg>')

for k, v in OUT.items(): open(f'svg/{k}.svg', 'w').write(v)
cells = ''.join(f'<div class="cell">{v}<p>{k}</p></div>' for k, v in OUT.items() if k != 'pen-house')
open('preview7.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;margin:14px;background:#fff}} .row{{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}} .cell{{border:1px solid #eee6d6;border-radius:10px;padding:6px;background:#fffdf7}} .cell svg{{width:auto;height:220px;display:block}} p{{margin:2px 0 0;font-size:11px}}</style></head><body><div class="row">{cells}</div><div style="margin-top:12px;width:900px;background:#fffdf7">{OUT["pen-house"].replace(chr(39) + "1080" + chr(39), "1080")}</div></body></html>')
print('ok', len(OUT))
