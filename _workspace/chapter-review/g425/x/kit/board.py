# Map sample C: the board -- Clara's journey. Seven ranks, one for each stage; a chapter on each square of the path,
# Clara the pawn on the square you are on, the Queen waiting at the far end (a pawn that crosses the board becomes a queen).
from common import *
W = 360; N = 5; SQ = 58; BX = (W - N * SQ) / 2
def board():
    s = []; ranks = list(enumerate(STAGES)); y = 120; centres = []
    rows = []
    for k, st in ranks: rows.append((k, st))
    # draw from the top rank (stage 7) down to the bottom (stage 1)
    H_LAB = 22
    total = len(rows) * (SQ + H_LAB)
    top = y
    for rr, (k, st) in enumerate(reversed(rows)):
        ry = top + rr * (SQ + H_LAB)
        s.append(T(BX + 2, ry + 15, '%d · %s' % (k + 1, st['en']), 12, 700, NAVY, serif=True, italic=True))
        ids = st['ids']; n = len(ids)
        left_to_right = (k % 2 == 0)
        for c in range(N):
            x = BX + c * SQ; yy = ry + H_LAB; dark = (c + k) % 2 == 0
            slot = c if left_to_right else N - 1 - c
            i = ids[slot] if slot < n else None
            s.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" fill="%s"/>' % (x, yy, SQ, SQ, NAVY if dark else '#fff'))
            if i:
                on, stt = i == HERE, STATE[i]; fg = '#fff' if dark else NAVY
                if on: s.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" fill="none" stroke="%s" stroke-width="3"/>' % (x + 1.5, yy + 1.5, SQ - 3, SQ - 3, CORAL))
                s.append(T(x + 6, yy + 16, str(NUM[i]), 14, 800, CORAL if on else fg, serif=True))
                for li, ln in enumerate(wrap(name(i), 9)[:2]): s.append(T(x + 6, yy + 33 + li * 11, ln, 9, 700 if on else 600, CORAL if on else fg, op=None if (stt != 'new' or on) else 0.75))
                if stt == 'done': s.append('<circle cx="%.1f" cy="%.1f" r="7" fill="%s"/><path d="M%.1f %.1f l2.6 2.6 l5 -5.4" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>' % (x + SQ - 10, yy + 10, GREEN, x + SQ - 14, yy + 10))
                centres.append((NUM[i], x + SQ / 2, yy + SQ / 2, on))
    # the frame of the board
    bh = len(rows) * (SQ + H_LAB)
    s.insert(0, '<rect x="%.1f" y="%.1f" width="%d" height="%d" fill="#fff" stroke="%s" stroke-width="1.8"/><rect x="%.1f" y="%.1f" width="%d" height="%d" fill="none" stroke="%s" stroke-width="0.6"/>' % (BX - 8, top - 8, N * SQ + 16, bh + 12, NAVY, BX - 4, top - 4, N * SQ + 8, bh + 4, NAVY))
    # the path in order (dotted coral), then the pieces
    centres.sort()
    for num, cx, cy, on in centres:
        if on: s.append(pawn(cx + 19, cy + 27, 0.4))
    # the goal: the Queen at the top, beside the King
    s.append(queen(W / 2 + 22, top - 18, 0.62) + king(W / 2 - 22, top - 18, 0.62))
    s.append(T(W / 2, top - 92, 'Clara’s journey', 18, 800, NAVY, 'middle', serif=True, italic=True))
    s.append(T(W / 2, top - 76, 'A pawn that crosses the board becomes a queen.', 10.5, 600, MUTED, 'middle'))
    s.append(cameo(BX - 4, top + bh + 18, 64) + T(BX + 58, top + bh + 46, 'Your butler welcomes you.', 12.5, 700, NAVY, serif=True, italic=True) + T(BX + 58, top + bh + 62, 'One square a chapter, from the bottom up.', 10.5, 600, MUTED))
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">%s</svg>' % (W, top + bh + 92, ''.join(s))
if __name__ == '__main__':
    s = board(); open('board.svg', 'w').write(s)
    open('board.html', 'w').write('<html><head>%s</head><body style="margin:0;background:#fff"><div style="width:390px">%s</div></body></html>' % (FONTS, s.replace('<svg ', '<svg width="390" ')))
