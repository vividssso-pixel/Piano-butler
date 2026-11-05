# A plain keyboard drawing for the workbooks: no metaphors, just keys, groups, dots and marks.
N, C, CR = '#26296b', '#e4572e', '#fffdf7'
WHITE = 'CDEFGAB'
HAS_BLACK = {'C': 1, 'D': 1, 'F': 1, 'G': 1, 'A': 1}   # a black key to the right of these

def keyboard(start='C', n=14, W=22, H=88, shade=None, dots=(), bdots=(), brackets=(), bracket_labels=True, marks=None, label=None, scale=1):
    """shade: {white index: colour}; dots: white indices with a coral dot; bdots: (white index) of black keys right of it with a dot;
    brackets: list of (first white index, last white index, text, done) drawn under the keys."""
    s0 = WHITE.index(start); BW, BH = W * 0.58, H * 0.6
    out = []
    for i in range(n):
        x = i * W; fill = (shade or {}).get(i, '#fff')
        out.append(f'<rect x="{x}" y="0" width="{W}" height="{H}" fill="{fill}" stroke="{N}" stroke-width="1.4"/>')
        if i in dots: out.append(f'<circle cx="{x + W / 2}" cy="{H - 14}" r="4.6" fill="{C}"/>')
        if label: out.append(f'<text x="{x + W / 2}" y="{H - 8}" text-anchor="middle" font-family="Inter,Arial" font-size="10.5" font-weight="700" fill="{N}">{WHITE[(s0 + i) % 7]}</text>')
    for i in range(n - 1):
        if WHITE[(s0 + i) % 7] in HAS_BLACK:
            x = (i + 1) * W - BW / 2
            out.append(f'<rect x="{x:.1f}" y="0" width="{BW:.1f}" height="{BH:.1f}" rx="1.5" fill="{N}"/>')
            if i in bdots: out.append(f'<circle cx="{x + BW / 2:.1f}" cy="{BH - 9:.1f}" r="4.2" fill="#fff"/>')
    out.append(f'<rect x="0" y="0" width="{n * W}" height="{H}" fill="none" stroke="{N}" stroke-width="2.2" rx="2"/>')
    by = H + 10
    for a, b, t, done in brackets:
        x1, x2 = a * W + 3, (b + 1) * W - 3; col = C if done else '#b9bbd3'; dash = '' if done else ' stroke-dasharray="3 3"'
        out.append(f'<path d="M{x1} {by} v6 H{x2} v-6" fill="none" stroke="{col}" stroke-width="1.8"{dash}/>')
        if t: out.append(f'<text x="{(x1 + x2) / 2}" y="{by + 20}" text-anchor="middle" font-family="Inter,Arial" font-size="11" font-weight="800" fill="{col}">{t}</text>')
    if marks: out += marks
    h = H + (34 if brackets else 4)
    return f'<svg viewBox="-2 -2 {n * W + 4} {h + 2}" style="display:block;margin:0 auto;max-width:100%;height:{h * scale:.0f}px">' + ''.join(out) + '</svg>'

def black_groups(start, n):
    """(first white index, last white index, size) of each complete black-key group, as brackets under its black keys."""
    s0 = WHITE.index(start); g = []; i = 0
    while i < n - 1:
        L = WHITE[(s0 + i) % 7]
        if L in ('C', 'F'):
            k = 2 if L == 'C' else 3
            if i + k < n: g.append((i, i + k, k))
            i += k + 1
        else: i += 1
    return g
