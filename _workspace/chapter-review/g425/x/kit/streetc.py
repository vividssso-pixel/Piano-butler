# Map sample B, round 2: the street drawn as classical Victorian architecture -- lines only, navy on white; the shapes
# carry the classicism: plinths, string courses, cornices with dentils, pilasters and columns with bases and capitals,
# pediments, arched windows with keystones and sills on brackets, balustrades with urns, quoins, a dome on a drum.
from common import *
import math
W = 360; BX0, BX1 = 28, 332; BW = BX1 - BX0; CX = W / 2
LW, MW, FW = 1.6, 0.9, 0.55     # line weights: outline, detail, fine

def L(x1, y1, x2, y2, w=MW): return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (x1, y1, x2, y2, NAVY, w)
def R(x, y, w, h, sw=MW, fill='#fff'): return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, w, h, fill, NAVY, sw)
def P(d, sw=MW, fill='#fff'): return '<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (d, fill, NAVY, sw)

def cornice(x0, x1, y, dent=True, proj=6):
    """a projecting cornice: a fascia, a dentil course, a crowning moulding (y = its top)"""
    s = [R(x0 - proj, y, x1 - x0 + 2 * proj, 4, MW), R(x0 - proj + 2, y + 4, x1 - x0 + 2 * proj - 4, 2.5, FW)]
    if dent: s.append(''.join('<rect x="%.1f" y="%.1f" width="2.6" height="3" fill="%s"/>' % (x, y + 7, NAVY) for x in [x0 - proj + 4 + k * 5.2 for k in range(int((x1 - x0 + 2 * proj - 8) / 5.2))]))
    s.append(L(x0 - proj + 3, y + 11, x1 + proj - 3, y + 11, FW))
    return ''.join(s), 12
def string_course(x0, x1, y): return R(x0 - 2, y, x1 - x0 + 4, 3, FW)
def plinth(x0, x1, y, h=10): return R(x0 - 3, y, x1 - x0 + 6, h, MW) + L(x0 - 3, y + 3, x1 + 3, y + 3, FW)
def quoins(x, y0, y1, left=True):
    s = []; y = y0; k = 0
    while y < y1 - 2:
        h = min(9, y1 - y); w = 12 if k % 2 == 0 else 8
        s.append(R(x if left else x - w, y, w, h, FW)); y += h; k += 1
    return ''.join(s)
def pilaster(x, y0, y1, w=8):
    return R(x - w / 2, y0 + 4, w, y1 - y0 - 8, FW) + R(x - w / 2 - 1.5, y0, w + 3, 4, FW) + R(x - w / 2 - 1.5, y1 - 4, w + 3, 4, FW)
def column(x, y0, y1, r=5, ionic=False):
    """a column: a base of two rings, a slightly tapering shaft with flutes, a capital"""
    s = [R(x - r - 2.5, y1 - 3, 2 * r + 5, 3, FW), R(x - r - 1.5, y1 - 5.5, 2 * r + 3, 2.5, FW)]
    top = y0 + (6 if ionic else 5)
    s.append(P('M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (x - r, y1 - 5.5, x - r * 0.84, top, x + r * 0.84, top, x + r, y1 - 5.5), MW))
    s.append(L(x - r * 0.35, top + 2, x - r * 0.4, y1 - 7, FW * 0.8) + L(x + r * 0.35, top + 2, x + r * 0.4, y1 - 7, FW * 0.8))
    if ionic:
        s.append(R(x - r - 3, y0, 2 * r + 6, 2.5, FW))
        s.append('<circle cx="%.1f" cy="%.1f" r="2" fill="#fff" stroke="%s" stroke-width="%s"/><circle cx="%.1f" cy="%.1f" r="2" fill="#fff" stroke="%s" stroke-width="%s"/>' % (x - r - 0.5, y0 + 4.2, NAVY, FW, x + r + 0.5, y0 + 4.2, NAVY, FW))
    else:
        s.append(R(x - r - 2, y0, 2 * r + 4, 2.5, FW) + R(x - r, y0 + 2.5, 2 * r, 2.5, FW))
    return ''.join(s)
def baluster(x, y, h):
    """a turned baluster: a cap, a narrow neck, a bulb low down, a foot"""
    return (R(x - 3, y, 6, 1.6, FW) + P('M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f L%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f Z' % (
        x - 1.1, y + 1.6, x - 1.1, y + h * 0.3, x - 3, y + h * 0.5, x - 3, y + h * 0.7, x - 3, y + h - 3, x - 1.4, y + h - 2.2, x - 1.4, y + h - 1.6,
        x + 1.4, y + h - 1.6, x + 1.4, y + h - 2.2, x + 3, y + h - 3, x + 3, y + h * 0.7, x + 3, y + h * 0.5, x + 1.1, y + h * 0.3, x + 1.1, y + 1.6), FW) + R(x - 3, y + h - 1.6, 6, 1.6, FW))
def balustrade(x0, x1, y, h=14, urns=True):
    s = [R(x0, y, x1 - x0, 2.5, MW), R(x0, y + h - 2.5, x1 - x0, 2.5, MW)]
    n = int((x1 - x0 - 16) / 10)
    for k in range(n): s.append(baluster(x0 + 11 + k * (x1 - x0 - 22) / max(1, n - 1), y + 2.5, h - 5))
    for x in (x0, x1):
        s.append(R(x - 4, y - 1, 8, h + 1, MW))
        if urns: s.append(urn(x, y - 1))
    return ''.join(s)
def urn(x, y):
    return P('M%.1f %.1f L%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f L%.1f %.1f Z' % (x - 3, y, x - 2, y - 2, x - 6, y - 4, x - 5, y - 10, x, y - 11, x + 5, y - 10, x + 6, y - 4, x + 2, y - 2, x + 3, y), FW) + '<circle cx="%.1f" cy="%.1f" r="1.4" fill="%s"/>' % (x, y - 12.5, NAVY)
def finial(x, y, h=10): return L(x, y, x, y - h, MW) + '<circle cx="%.1f" cy="%.1f" r="1.8" fill="%s"/>' % (x, y - h - 1.5, NAVY) + P('M%.1f %.1f l3 -4 l3 4 Z' % (x - 3, y - 3), FW, NAVY)
def pediment(x0, x1, y, h, oculus=True):
    s = [P('M%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (x0 - 6, y, (x0 + x1) / 2, y - h, x1 + 6, y), LW)]
    s.append(P('M%.1f %.1f L%.1f %.1f L%.1f %.1f' % (x0 + 4, y - 3, (x0 + x1) / 2, y - h + 5, x1 - 4, y - 3), FW, 'none'))
    if oculus: s.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="%s" stroke-width="%s"/><circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="%s"/>' % ((x0 + x1) / 2, y - h * 0.4, h * 0.22, NAVY, MW, (x0 + x1) / 2, y - h * 0.4, h * 0.22 - 2, NAVY, FW))
    s.append(urn(x0 - 4, y) + urn(x1 + 4, y) + finial((x0 + x1) / 2, y - h, 6))
    return ''.join(s)
def steps(cx, y, w, n=3):
    return ''.join(R(cx - w / 2 - k * 6, y + k * 4, w + k * 12, 4, MW) for k in range(n))
def cresting(x0, x1, y):
    return L(x0, y, x1, y, MW) + ''.join('<path d="M%.1f %.1f v-6 m-2.5 2.5 l2.5 -2.5 l2.5 2.5 M%.1f %.1f a2 2 0 1 1 0.01 0" fill="none" stroke="%s" stroke-width="%s"/>' % (x, y, x, y - 8.5, NAVY, FW) for x in [x0 + 4 + k * 8 for k in range(int((x1 - x0 - 6) / 8) + 1)])
def chimney(x, y, h=26):
    return R(x, y - h, 14, h, MW) + R(x - 2, y - h - 4, 18, 4, MW) + R(x + 2, y - h - 9, 4, 5, FW) + R(x + 8, y - h - 9, 4, 5, FW)
def deco_window(x, y, w, h, arch=True):
    """a window that is not a chapter: glazing bars"""
    s = [chapter_frame(x, y, w, h, arch)]
    s.append(L(x + w / 2, y + (w / 2 if arch else 0), x + w / 2, y + h, FW) + L(x, y + h * 0.58, x + w, y + h * 0.58, FW))
    return ''.join(s)
def chapter_frame(x, y, w, h, arch=True, stroke=NAVY, sw=LW):
    """an architrave: the opening, a band around it, a keystone on an arch; a sill on two brackets"""
    r = w / 2; o = 3.2
    if arch:
        inner = 'M%.1f %.1f L%.1f %.1f A%.1f %.1f 0 0 1 %.1f %.1f L%.1f %.1f Z' % (x, y + h, x, y + r, r, r, x + w, y + r, x + w, y + h)
        outer = 'M%.1f %.1f L%.1f %.1f A%.1f %.1f 0 0 1 %.1f %.1f L%.1f %.1f' % (x - o, y + h, x - o, y + r, r + o, r + o, x + w + o, y + r, x + w + o, y + h)
        key = P('M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (x + r - 3, y - o - 2.5, x + r + 3, y - o - 2.5, x + r + 2, y + 3, x + r - 2, y + 3), MW)
    else:
        inner = 'M%.1f %.1f H%.1f V%.1f H%.1f Z' % (x, y, x + w, y + h, x)
        outer = 'M%.1f %.1f V%.1f H%.1f V%.1f' % (x - o, y + h, y - o, x + w + o, y + h)
        key = R(x - o - 3, y - o - 4, w + 2 * o + 6, 3, MW)   # a little cornice over a square window
    s = [P(outer, FW, 'none'), '<path d="%s" fill="#fff" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (inner, stroke, sw), key]
    s.append(R(x - o - 3, y + h, w + 2 * o + 6, 3, MW))                                      # sill
    s.append(P('M%.1f %.1f l2 0 l0 3 l-1 1 Z M%.1f %.1f l-2 0 l0 3 l1 1 Z' % (x - o, y + h + 3, x + w + o, y + h + 3), FW, NAVY))   # brackets
    return ''.join(s)
def chapter_window(i, x, y, w, h, arch=True):
    st, on = STATE[i], i == HERE; s = []
    s.append(chapter_frame(x, y, w, h, arch, CORAL if on else NAVY, 2.4 if on else LW))
    s.append(icon(i, x + w / 2 - 15, y + h * (0.42 if arch else 0.3), 0.62, 1 if st != 'new' or on else 0.5))
    s.append(square(x + w / 2 - 8, y + h + 12, 16, NUM[i] + 1, str(NUM[i]), fill=GREEN if st == 'done' else None, size=10.5))
    lines = wrap(('✓ ' if st == 'done' else '') + name(i), max(8, int((w + 16) / 6)))
    for k, ln in enumerate(lines[:2]): s.append(T(x + w / 2, y + h + 41 + k * 12, ln, 10.5, 800 if on or st == 'done' else 600, CORAL if on else (NAVY if st == 'done' else NEW), 'middle'))
    if on: s.append(pawn(x + w - 6, y + h - 2, 0.36))
    return ''.join(s)
def windows_row(ids, y, h, x0=BX0, x1=BX1, arch=True, wmax=44):
    n = len(ids); gap = (x1 - x0) / n; w = min(gap - 20, wmax)
    return ''.join(chapter_window(i, x0 + k * gap + (gap - w) / 2, y, w, h, arch) for k, i in enumerate(ids)), [x0 + k * gap + gap / 2 for k in range(n)]
def plaque(cx, y, txt):
    w = len(txt) * 6.6 + 22
    return R(cx - w / 2, y, w, 18, MW) + R(cx - w / 2 + 2, y + 2, w - 4, 14, FW, 'none') + T(cx, y + 13, txt, 11.5, 700, NAVY, 'middle', serif=True, italic=True)
def frieze(cx, y, txt): return T(cx, y, txt.upper(), 8.5, 800, MUTED, 'middle', ls='0.22em')
WIN_TOP, WIN_H, LAB, PL = 36, 58, 60, 10   # a hall: the plaque, the chapter windows, their numbers and names, the plinth
def entablature(x0, x1, y, name=None, proj=6):
    """cornice (with dentils), frieze (the building's name in spaced capitals), architrave (two fine lines); y = top"""
    c, ch = cornice(x0, x1, y, True, proj); s = [c]; f = y + ch
    s.append(R(x0 - 1, f, x1 - x0 + 2, 14, MW))
    if name: s.append(T((x0 + x1) / 2, f + 10.2, name.upper(), 7.6, 800, NAVY, 'middle', ls='0.32em'))
    s.append(R(x0 + 1, f + 14, x1 - x0 - 2, 3, FW) + R(x0 + 3, f + 17, x1 - x0 - 6, 2.5, FW))
    return ''.join(s), ch + 19.5
def hall(st, n, body, x0=BX0, x1=BX1, arch=True, wmax=44, pad=16, quoin=False, pil=False, cols=None, glass=False):
    """the storey every building shares: the stage plaque, the chapter windows, their numbers and names, the plinth"""
    extra = 8 if cols else 0; bh = WIN_TOP + extra + WIN_H + LAB + PL; base = body + bh; s = [R(x0, body, x1 - x0, bh, LW)]
    wy = body + WIN_TOP + extra
    if glass:   # glazing above a low stone wall that carries the numbers and names
        sill = wy + WIN_H + 7.5
        s.append(''.join(L(x0 + k * (x1 - x0) / 12, body + 3, x0 + k * (x1 - x0) / 12, sill, FW) for k in range(1, 12)) + L(x0, body + 30, x1, body + 30, FW))
        s.append(R(x0 - 2, sill, x1 - x0 + 4, 3.5, MW))
    if quoin: s.append(quoins(x0, body, base - PL, True) + quoins(x1, body, base - PL, False))
    if pil:
        for x in (x0 + 9, x1 - 9): s.append(pilaster(x, body + 2, base - PL, 9))
    s.append(plaque(CX, body + 8, '%d · %s' % (n, st['en'])))
    if cols:   # a colonnade standing on a ledge at the sills, carrying a beam over the windows
        k_ = len(st['ids']); gap = (x1 - x0 - 2 * pad) / k_
        s.append(R(x0 + pad - 8, wy + WIN_H + 7.5, x1 - x0 - 2 * pad + 16, 3, MW))
        s.append(R(x0 + pad - 8, wy - (13 if arch else 14), x1 - x0 - 2 * pad + 16, 3, MW))
        for j in range(k_ + 1): s.append(column(x0 + pad + j * gap, wy - (10 if arch else 11), wy + WIN_H + 7.5, cols, ionic=not arch))
    w, _ = windows_row(st['ids'], wy, WIN_H, x0 + pad, x1 - pad, arch, wmax); s.append(w)
    s.append(plinth(x0, x1, base - PL, PL))
    return ''.join(s), base

# ── the seven buildings; each returns (svg, height) drawn from y0 downwards ──
def lodge(st, y0):
    """The Lodge: a gabled cottage -- carved bargeboards, a finial, the butler's portrait in a roundel, chimneys, quoins"""
    s = []; top = y0 + 14; eave = top + 72
    s.append(chimney(BX0 + 40, eave - 24) + chimney(BX1 - 54, eave - 24))
    s.append(P('M%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (BX0 - 10, eave, CX, top, BX1 + 10, eave), LW))
    for side in (-1, 1):
        for k in range(1, 14):
            t0, t1 = (k - 1) / 13, k / 13
            xa, ya = CX + side * t0 * (BW / 2 + 10), top + t0 * (eave - top); xb, yb = CX + side * t1 * (BW / 2 + 10), top + t1 * (eave - top)
            s.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" stroke="%s" stroke-width="%s"/>' % (xa, ya + 3, (xa + xb) / 2, (ya + yb) / 2 + 8, xb, yb + 3, NAVY, FW))
    s.append(finial(CX, top, 12))
    s.append('<circle cx="%.1f" cy="%.1f" r="20" fill="#fff" stroke="%s" stroke-width="%s"/><circle cx="%.1f" cy="%.1f" r="23" fill="none" stroke="%s" stroke-width="%s"/>' % (CX, top + 42, NAVY, LW, CX, top + 42, NAVY, FW) + cameo(CX - 13.5, top + 25, 34))
    s.append(R(BX0, eave, BW, 14, MW) + T(CX, eave + 10.2, 'THE LODGE', 7.6, 800, NAVY, 'middle', ls='0.32em') + R(BX0 + 2, eave + 14, BW - 4, 3, FW))
    h, base = hall(st, 1, eave + 17, quoin=True, pad=14); s.append(h)
    return ''.join(s), base - y0
def library(st, y0):
    """The Library: a balustrade with urns over a full entablature; pilasters at the corners"""
    s = []; bt = y0 + 22; s.append(balustrade(BX0 + 4, BX1 - 4, bt, 18))
    e, eh = entablature(BX0, BX1, bt + 18, 'Library'); s.append(e)
    h, base = hall(st, 2, bt + 18 + eh, pil=True, pad=20); s.append(h)
    return ''.join(s), base - y0
def clocktower(st, y0):
    """The Clock Tower: a tower -- a spire with a finial, an arcaded belfry, a pilastered clock stage -- over a quoined hall"""
    s = []; tw = 62; tx = CX - tw / 2; rt = y0 + 20
    s.append(P('M%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (tx - 6, rt + 36, CX, rt, tx + tw + 6, rt + 36), LW))
    s.append(''.join(L(CX, rt + 5, CX + d, rt + 36, FW) for d in (-22, -11, 11, 22)))
    s.append(finial(CX, rt, 14))
    bel = rt + 36; s.append(R(tx, bel, tw, 30, LW))
    for k in range(3):
        x = tx + 9 + k * 16.5; s.append(P('M%.1f %.1f L%.1f %.1f A6 6 0 0 1 %.1f %.1f L%.1f %.1f Z' % (x, bel + 26, x, bel + 13, x + 12, bel + 13, x + 12, bel + 26), MW))
    clk = bel + 30; c, ch = cornice(tx, tx + tw, clk, False, 4); s.append(c)
    cs = clk + ch; cy = cs + 30
    s.append(R(tx, cs, tw, 60, LW) + pilaster(tx + 5, cs, cs + 60, 6) + pilaster(tx + tw - 5, cs, cs + 60, 6))
    s.append('<circle cx="%.1f" cy="%.1f" r="21" fill="#fff" stroke="%s" stroke-width="%s"/><circle cx="%.1f" cy="%.1f" r="17" fill="none" stroke="%s" stroke-width="%s"/>' % (CX, cy, NAVY, LW, CX, cy, NAVY, FW))
    s.append(''.join(L(CX + 14 * math.cos(a), cy + 14 * math.sin(a), CX + 17 * math.cos(a), cy + 17 * math.sin(a), MW) for a in [k * math.pi / 6 for k in range(12)]))
    s.append(L(CX, cy, CX, cy - 12, 1.6) + L(CX, cy, CX + 8, cy + 4, 1.6))
    e, eh = entablature(BX0, BX1, cs + 60, 'The Clock Tower'); s.append(e)
    h, base = hall(st, 3, cs + 60 + eh, quoin=True); s.append(h)
    return ''.join(s), base - y0
def conservatory(st, y0):
    """The Conservatory: a palm house -- a glass roof with curved shoulders on iron ribs, a raised lantern with a finial"""
    s = []; top = y0 + 30
    def shoulder_roof(x0, x1, ridge, eave, r, ribs):
        out = [P('M%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f' % (x0, eave, x0, ridge, x0 + r, ridge, x1 - r, ridge, x1, ridge, x1, eave), LW)]
        out.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" stroke="%s" stroke-width="%s"/>' % (x0 + 5, eave, x0 + 5, ridge + 5, x0 + r, ridge + 5, x1 - r, ridge + 5, x1 - 5, ridge + 5, x1 - 5, eave, NAVY, FW))
        for j in range(1, ribs):
            x = x0 + j * (x1 - x0) / ribs; d = min(x - x0, x1 - x)
            if d >= r: y = ridge
            else:
                t = 1 - math.sqrt(1 - d / r) if d < r else 1   # invert x(t) = x0 + r*(1-(1-t)^2) on the quadratic shoulder
                y = (1 - t) ** 2 * eave + 2 * t * (1 - t) * ridge + t * t * ridge
            out.append(L(x, eave, x, y, FW))
        return ''.join(out)
    lt = top; s.append(finial(CX, lt, 10))
    s.append(shoulder_roof(CX - 46, CX + 46, lt, lt + 22, 16, 10))
    s.append(R(CX - 46, lt + 22, 92, 18, MW) + ''.join(L(CX - 46 + j * 92 / 10, lt + 22, CX - 46 + j * 92 / 10, lt + 40, FW) for j in range(1, 10)))
    s.append(R(CX - 50, lt + 40, 100, 3, MW))
    ridge = lt + 43; eave = ridge + 44
    s.append(shoulder_roof(BX0, BX1, ridge, eave, 50, 24))
    s.append(R(BX0 - 4, eave, BW + 8, 3.5, MW) + R(BX0, eave + 3.5, BW, 13, MW) + T(CX, eave + 13.2, 'CONSERVATORY', 7.6, 800, NAVY, 'middle', ls='0.32em'))
    h, base = hall(st, 4, eave + 16.5, glass=True, pad=58, wmax=50); s.append(h)
    return ''.join(s), base - y0
def academy(st, y0):
    """The Academy: a temple front -- a pediment, a full entablature, Ionic columns between the windows on a ledge, steps"""
    s = []; ped = y0 + 56; s.append(pediment(BX0 + 6, BX1 - 6, ped, 46))
    e, eh = entablature(BX0, BX1, ped, 'Academy', 4); s.append(e)
    h, base = hall(st, 5, ped + eh, arch=False, wmax=38, pad=12, cols=4.6); s.append(h)
    s.append(steps(CX, base, BW - 16, 2))
    return ''.join(s), base + 8 - y0
def theatre(st, y0):
    """The Theatre: a mansard roof with round dormers, an arched attic with a lyre, an arcade on columns"""
    s = []; top = y0 + 34; eave = top + 42
    s.append(P('M%.1f %.1f A30 26 0 0 1 %.1f %.1f Z' % (CX - 32, top + 2, CX + 32, top + 2), LW))
    s.append('<path d="M%.1f %.1f A25 21 0 0 1 %.1f %.1f" fill="none" stroke="%s" stroke-width="%s"/>' % (CX - 26, top + 2, CX + 26, top + 2, NAVY, FW))
    ly = top - 1   # the lyre: two horns, a crossbar, strings, a foot
    s.append('<path d="M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f" fill="none" stroke="%s" stroke-width="1.3" stroke-linecap="round"/>' % (CX - 4, ly - 2, CX - 13, ly - 6, CX - 11, ly - 16, CX - 6, ly - 19, CX + 4, ly - 2, CX + 13, ly - 6, CX + 11, ly - 16, CX + 6, ly - 19, NAVY))
    s.append(L(CX - 8.5, ly - 14, CX + 8.5, ly - 14, MW) + R(CX - 5, ly - 2.5, 10, 2.5, FW, NAVY) + ''.join(L(CX + d, ly - 14, CX + d, ly - 2.5, FW) for d in (-3, -1, 1, 3)))
    s.append(finial(CX, top - 24, 8))
    s.append(P('M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (BX0 - 2, eave, BX0 + 16, top + 2, BX1 - 16, top + 2, BX1 + 2, eave), LW))
    s.append(R(BX0 + 12, top - 1, BW - 24, 3, MW))
    for x in (BX0 + 58, BX1 - 58):
        s.append('<circle cx="%.1f" cy="%.1f" r="9" fill="#fff" stroke="%s" stroke-width="%s"/><circle cx="%.1f" cy="%.1f" r="6" fill="none" stroke="%s" stroke-width="%s"/>' % (x, top + 21, NAVY, MW, x, top + 21, NAVY, FW))
        s.append(L(x - 6, top + 21, x + 6, top + 21, FW) + L(x, top + 15, x, top + 27, FW) + R(x - 12, top + 31, 24, 3, FW))
    e, eh = entablature(BX0, BX1, eave, 'Theatre'); s.append(e)
    h, base = hall(st, 6, eave + eh, arch=True, wmax=38, pad=8, cols=3.4); s.append(h)
    return ''.join(s), base - y0
def museum(st, y0):
    """The Museum: a ribbed dome on an arcaded drum with a lantern, over a balustrade, an entablature and a quoined hall"""
    s = []; lt = y0 + 14
    s.append(finial(CX, lt + 4, 8) + R(CX - 7, lt + 4, 14, 14, MW) + P('M%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (CX - 9, lt + 5, CX, lt - 2, CX + 9, lt + 5), FW))
    dt = lt + 18; s.append(P('M%.1f %.1f A52 44 0 0 1 %.1f %.1f Z' % (CX - 52, dt + 44, CX + 52, dt + 44), LW))
    s.append(''.join('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" stroke="%s" stroke-width="%s"/>' % (CX + d, dt + 44, CX + d * 0.55, dt + 10, CX, dt + 1, NAVY, FW) for d in (-36, -18, 18, 36)))
    drum = dt + 44; s.append(R(CX - 60, drum, 120, 3, MW) + R(CX - 58, drum + 3, 116, 24, LW))
    for k in range(6):
        x = CX - 49 + k * 18; s.append(P('M%.1f %.1f L%.1f %.1f A4 4 0 0 1 %.1f %.1f L%.1f %.1f Z' % (x, drum + 23, x, drum + 10, x + 8, drum + 10, x + 8, drum + 23), FW))
    bt = drum + 27; s.append(balustrade(BX0 + 4, BX1 - 4, bt, 18))
    e, eh = entablature(BX0, BX1, bt + 18, 'Museum'); s.append(e)
    h, base = hall(st, 7, bt + 18 + eh, quoin=True); s.append(h)
    return ''.join(s), base - y0
BUILD = [lodge, library, clocktower, conservatory, academy, theatre, museum]
def lamppost(x, y):
    return (R(x - 4, y - 4, 8, 4, MW) + L(x, y - 4, x, y - 50, 1.8) + L(x - 2, y - 30, x + 2, y - 30, MW)
            + P('M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (x - 6, y - 52, x + 6, y - 52, x + 4, y - 64, x - 4, y - 64), MW) + '<path d="M%.1f %.1f q3 -5 0 -9 q-3 4 0 9 z" fill="%s"/>' % (x, y - 54, CORAL)
            + P('M%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (x - 6, y - 64, x, y - 70, x + 6, y - 64), MW, NAVY))
RANGES = {}
def street():
    parts, y = [], 18
    for k in reversed(range(7)):
        svg, h = BUILD[k](STAGES[k], y); parts.append(svg); RANGES[k] = (y - 14, y + h + 22); y += h
        parts.append(''.join('<rect x="%d" y="%.1f" width="7" height="7" fill="%s"/>' % (x, y + 4 + (j % 2) * 7, NAVY) for j, x in enumerate(range(4, W - 4, 7))))
        parts.append('<rect x="4" y="%.1f" width="%d" height="14" fill="none" stroke="%s" stroke-width="0.8"/>' % (y + 4, W - 8, NAVY))
        parts.append(lamppost(14 if k % 2 else W - 14, y + 4))
        y += 44
    parts.append(T(CX, y - 14, 'Start at the Lodge and walk up the street.', 11, 600, MUTED, 'middle'))
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">%s</svg>' % (W, y - 4, ''.join(parts))
if __name__ == '__main__':
    import sys as _s
    if len(_s.argv) > 1 and _s.argv[1] == 'progress':   # chapters 1-7 done, chapter 8 where you are
        for i in ORDER: STATE[i] = 'new'
        for i in ORDER[:7]: STATE[i] = 'done'
        globals()['HERE'] = ORDER[7]
    s = street(); open('streetc.svg', 'w').write(s)
    import json; json.dump(RANGES, open('streetc-ranges.json', 'w'))
    open('streetc.html', 'w').write('<html><head>%s</head><body style="margin:0;background:#fff"><div style="width:390px">%s</div></body></html>' % (FONTS, s.replace('<svg ', '<svg width="390" ')))
