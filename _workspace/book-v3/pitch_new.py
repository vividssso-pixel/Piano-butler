# Part I Pitch, chapters 1-7, rewritten 7 Nov (her: "make every question and example a path to the aha";
# keyboard notes by landmark name, never octave numbers). exec'd from pitch.py; uses its helpers.
# One counting rule for the whole part: COUNT THE NOTES (start at 1, both ends) for letter distance and interval numbers;
# COUNT THE HOPS (each move to the very next key is 1, drawn as an arc) for semitones.
import re as _re
for _d in (P, PP):
    for _k in _d: _d[_k] = _d[_k].replace('>middle C<', '>Middle C<').replace('>treble G<', '>treble G<')
LMK = {'C2': 'Low C', 'C3': 'Bass C', 'C4': 'Middle C', 'C5': 'Treble C', 'C6': 'High C'}
NAV, RED, PINK, BLUE = '#26296b', '#e4572e', '#fde6dd', '#eef0f8'
_WH = 'CDEFGAB'

def _bpos(i, W): return (i + 1) * W          # centre of the black key just right of white key i
def _wpos(i, W): return (i + 0.5) * W
def qkb(start, n, W=34, H=110, tags=None, q=(), qb=(), dots=(), bdots=(), nums=(), arcs=(), shade=None, label=True, scale=1.0, tagcol=None):
    """A keyboard that asks: '?' on the key to find (q white indices, qb black keys right of white i), red dots, numbered
    circles on keys (nums: ('w'|'b', i, text, red)), hop arcs above the keys (arcs: (x0, x1) in key units: white i = i + .5,
    black right of i = i + 1), landmark name tags under the keys (tags: {white index: name})."""
    BH = H * 0.6; m = []
    for i in dots: m.append(f'<circle cx="{_wpos(i, W)}" cy="{H - 30}" r="{min(10, W * .3):.1f}" fill="{RED}"/>')
    for i in bdots: m.append(f'<circle cx="{_bpos(i, W)}" cy="{BH - 14}" r="{min(9, W * .26):.1f}" fill="{RED}"/>')
    def bubble(x, y, t, red, r=None):
        r = r or min(12, W * .36)
        return (f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="{RED if red else "#fff"}" stroke="{RED if red else NAV}" stroke-width="2"/>'
                f'<text x="{x}" y="{y + r * .42:.1f}" text-anchor="middle" font-family="AH,Arial" font-size="{r * 1.15:.1f}" font-weight="700" fill="{"#fff" if red else NAV}">{t}</text>')
    for i in q: m.append(f'<rect x="{i * W + 2}" y="{H - 20}" width="{W - 4}" height="17" fill="{(shade or {}).get(i, "#fff")}"/>' + bubble(_wpos(i, W), H - 32, '?', True))
    for i in qb: m.append(bubble(_bpos(i, W), BH - 16, '?', True))
    for kind, i, t, red in nums: m.append(bubble(_wpos(i, W) if kind == 'w' else _bpos(i, W), (H - 32) if kind == 'w' else (BH - 16), t, red, min(10, W * .3)))
    top = 0
    for k, (a, b) in enumerate(arcs):   # one hop each: a small hump above the keys
        x0, x1 = a * W, b * W; h = 16; top = 24
        m.append(f'<path d="M{x0 + 3:.1f},-3 Q{(x0 + x1) / 2:.1f},{-3 - 2 * h} {x1 - 3:.1f},-3" fill="none" stroke="{RED}" stroke-width="2.4" stroke-linecap="round"/>'
                 f'<text x="{(x0 + x1) / 2:.1f}" y="{-6 - h:.1f}" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" fill="{RED}">{k + 1}</text>')
    bot = 0
    if tags:
        bot = 26
        for i, t in tags.items():
            x = _wpos(i, W); col = (tagcol or {}).get(i, RED)
            m.append(f'<path d="M{x},{H + 3} v7" stroke="{col}" stroke-width="2"/><text x="{x}" y="{H + 23}" text-anchor="middle" font-family="AH,Arial" font-size="12.5" font-weight="700" fill="{col}">{t}</text>')
    s = keyboard(start, n, W, H, shade=shade, marks=m, label=label, scale=1)
    vb = _re.search(r'viewBox="(-?[\d.]+) (-?[\d.]+) ([\d.]+) ([\d.]+)" style="([^"]*)height:(\d+)px', s)
    w0, h0 = float(vb.group(3)), float(vb.group(4)); pad = 60 if tags else 4   # tags may run past the ends
    nh = h0 + top + bot
    s = s.replace(vb.group(0), f'viewBox="{float(vb.group(1)) - pad / 2} {-2 - top} {w0 + pad} {nh}" style="{vb.group(5)}height:{nh * scale:.0f}px')
    return s

def ask(html, ids=(), hide=False):   # her 7 Nov: the Example asks, the result line answers: '?' under the target notes, other labels kept (or all hidden)
    def one(m):
        nid = m.group(1); head = m.group(0)[:m.start(2) - m.start(0)]; tail = m.group(0)[m.end(2) - m.start(0):]
        if nid in ids: return head.replace('<tspan font-size', '<tspan fill="#e4572e" font-size') + '?' + tail
        return head + ('' if hide else m.group(2)) + tail
    return _re.sub(r'<g id="([^"]+)" class="note"(?:(?!<g id="[^"]+" class="note").)*?<tspan font-size="\d+px">([^<]*)</tspan>', one, html, flags=_re.S)

def clef_hero():   # her 7 Nov: a magnifying glass on each clef; the line it names in red
    base = P['hero_clef']
    for d in ('M0 1080 L3078 1080', 'M0 2520 L3078 2520'):
        base = base.replace(f'd="{d}"', f'd="{d}" style="stroke:{RED};stroke-width:30"')
    def lens(x0, y0, w, h, txt, sub):
        inner = _re.search(r'<svg class="definition-scale"[^>]*>', base).group(0)
        z = base.replace(inner, f'<svg class="definition-scale" color="black" x="8" y="8" width="104" height="104" viewBox="{x0} {y0} {w} {h}" preserveAspectRatio="xMidYMid meet">', 1)
        z = _re.sub(r'^<svg viewBox="[^"]*"', '<svg viewBox="0 0 150 150"', z, count=1)
        cid = f'lens{y0}'
        z = z.replace('<desc>', f'<defs><clipPath id="{cid}"><circle cx="60" cy="60" r="52"/></clipPath></defs><circle cx="60" cy="60" r="52" fill="#fff"/><g clip-path="url(#{cid})"><desc>', 1)
        z = z[:z.rindex('</svg>')] + f'</g><circle cx="60" cy="60" r="52" fill="none" stroke="{NAV}" stroke-width="6"/><path d="M98,98 L140,140" stroke="{NAV}" stroke-width="12" stroke-linecap="round"/></svg>'
        z = z.replace('<svg viewBox="0 0 150 150"', '<svg viewBox="0 0 150 150" style="width:196px;height:196px;flex:none"', 1)
        return f'<div style="display:flex;align-items:center;gap:12px">{z}<div style="text-align:left;white-space:nowrap"><div style="font-family:AH,Arial;font-weight:700;font-size:16px;color:{NAV}">{txt}</div><div style="font-size:14px;color:{RED};font-weight:700">{sub}</div></div></div>'
    main = base.replace('<svg ', '<svg style="height:250px;width:auto;max-width:100%" ', 1).replace('font-family="Times,serif"', 'font-family="AH,Arial" font-weight="700"')
    for n in ('n2', 'n5'): main = main.replace(f'<g id="{n}" class="note">', f'<g id="{n}" class="note" style="fill:{RED};color:{RED}">', 1)
    return f'<div style="display:flex;justify-content:center;align-items:center;gap:22px"><div>{main}</div><div style="display:flex;flex-direction:column;gap:6px">{lens(560, 380, 1500, 1500, "Treble clef = G clef", "curls round line 2: G")}{lens(600, 2200, 1250, 1250, "Bass clef = F clef", "its dots hug line 4: F")}</div></div>'
def kq(*a, **k): return '<figure class="vx kbf">' + qkb(*a, **k) + '</figure>'
def hops(start_i, black_first, n):
    """arcs for n hops up from white key start_i: walk white/black keys in order (black only where one exists)."""
    seq = []; i = start_i
    pos = _wpos(i, 1)
    keys = []
    for j in range(start_i, start_i + 12):
        keys.append(j + 0.5)
        if _WH[j % 7] in 'CDFGA': keys.append(j + 1)
    return [(keys[k], keys[k + 1]) for k in range(n)]
def xlate(t, body): return f'<div class="xlate xbox"><div class="xbh">Extra · going further</div><b class="it">{t}</b>{body}</div>'
def staff_kb(svg, red=(), gap=260):   # her 8 Nov: a keyboard drawn under the staff, each white key under its own note, so the page shows which key each note means
    vb = _re.search(r'<svg viewBox="0 0 ([\d.]+) ([\d.]+)"', svg); W, H = float(vb.group(1)), float(vb.group(2))
    ivb = _re.search(r'<svg class="definition-scale" color="black" viewBox="0 0 ([\d.]+) ([\d.]+)">', svg); IW, IH = float(ivb.group(1)), float(ivb.group(2)); k = IW / W
    notes = sorted((float(x) + 146, nid) for nid, x in _re.findall(r'<g id="(n\d+)" class="note">.*?<use xlink:href="#[^"]*" x="([\d.]+)"', svg, flags=_re.S))
    xs = [x for x, _ in notes]; d = (xs[-1] - xs[0]) / (len(xs) - 1); top = IH + gap; kh = d * 3.2
    letters = 'GABCDEF'; out = []
    for i, (x, nid) in enumerate(notes):
        fill = '#fbd0c2' if nid in red else '#fff'
        out.append(f'<rect x="{x - d / 2:.0f}" y="{top:.0f}" width="{d:.0f}" height="{kh:.0f}" fill="{fill}" stroke="#26296b" stroke-width="22"/>')
        if nid in red: out.append(f'<circle cx="{x:.0f}" cy="{top + kh - d * .55:.0f}" r="{d * .2:.0f}" fill="#e4572e"/>')
    for i, (x, nid) in enumerate(notes[:-1]):
        if letters[i % 7] in 'CDFGA': out.append(f'<rect x="{x + d / 2 - d * .29:.0f}" y="{top:.0f}" width="{d * .58:.0f}" height="{kh * .6:.0f}" fill="#26296b"/>')
    nH = H + (gap + kh + 60) / k
    svg = svg.replace(vb.group(0), f'<svg viewBox="0 0 {W} {nH:.2f}"', 1).replace(ivb.group(0), f'<svg class="definition-scale" color="black" viewBox="0 0 {IW} {nH * k:.1f}">', 1)
    i = svg.rindex('</svg>'); i = svg.rindex('</svg>', 0, i)
    return svg[:i] + '<g class="kbunder">' + ''.join(out) + '</g>' + svg[i:]
def pxc(k, ids, h):   # a staff picture with the landmark notes (and their letters) in red, the other letters navy
    s = (staff_kb(P[k], ids) if k == 'gs_climb' else P[k]).replace('<svg ', '<svg style="max-height:%dpx;width:auto;max-width:100%%" ' % h, 1)
    for n in ids: s = s.replace(f'<g id="{n}" class="note">', f'<g id="{n}" class="note" style="fill:#e4572e;color:#e4572e">', 1)
    return '<div class="vs">' + s.replace('font-family="Times,serif"', 'font-family="AH,Arial" font-weight="700"') + '</div>'
def kfig(start, n, blk, wht, W=36, H=104):   # her 8 Nov: a small keyboard beside each sign Example, the keys named on them
    BH = H * 0.6; m = []
    for i, (t, red) in blk.items():
        x = (i + 1) * W
        for j, l in enumerate(t.split('/')): m.append(f'<text x="{x}" y="{BH * 0.34 + j * 14:.1f}" text-anchor="middle" font-family="AH,Arial" font-size="11.5" font-weight="700" fill="{RED if red else "#fff"}">{l}</text>')
        if red: m.append(f'<circle cx="{x}" cy="{BH - 11:.1f}" r="6.5" fill="{RED}"/>')
    for i, (t, red) in wht.items():
        x = (i + .5) * W; m.append(f'<circle cx="{x}" cy="{H - 30}" r="7.5" fill="{RED if red else NAV}"/>')
        if t: m.append(f'<text x="{x}" y="{H - 44}" text-anchor="middle" font-family="AH,Arial" font-size="11.5" font-weight="700" fill="{RED}">{t}</text>')
    s = keyboard(start, n, W, H, label=True, marks=m).replace('fill="#26296b"/>', 'fill="#26296b"/>', 1)
    return '<figure class="vx kbf" style="flex:0 0 auto;margin:0">' + s + '</figure>'
def side(a, b): return f'<div style="display:flex;align-items:center;justify-content:center;gap:22px">{a}{b}</div>'
def rule(t): return f'<div class="secret1" style="margin:8px 0"><span class="sl">The rule</span><span>{t}</span></div>'
def cards(items, cols=3):
    return f'<div class="pcards" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(f'<div><div class="pcf">{f}</div><b>{t}</b><span>{d}</span></div>' for f, t, d in items) + '</div>'
css += """
.pcards{display:grid;gap:12px;margin:8px 0 10px} .pcards>div{border:1.5px solid #e3e1ee;border-radius:9px;padding:9px 10px 10px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:3px}
.pcards .pcf{width:100%} .pcards .pcf svg{max-width:100%;height:auto} .pcards b{font-size:14.5px;color:#26296b} .pcards span{font-size:12.5px;line-height:1.35;color:#4a4d86}
"""

# ---------- 1 The keyboard ----------
g15 = black_groups('C', 15)
def hero_apart():   # her 7 Nov: pull the two groups apart, so the first key (start) and last key (end) of each are plain to see
    W, H = 66, 214
    def grp(start, n, title, col, shade):
        g = qkb(start, n, W, H, shade={i: shade for i in range(n)} | {0: '#fbd0c2'}, dots=(0,), tags={0: 'start', n - 1: 'end'}, tagcol={0: RED, n - 1: NAV})
        return f'<div style="text-align:center"><div style="font-family:AH,Arial;font-weight:700;font-size:16px;color:{col};margin-bottom:6px">{title}</div>{g}</div>'
    arrow = '<svg viewBox="0 0 60 40" style="width:54px"><path d="M6,20 H54 M14,12 L6,20 L14,28 M46,12 L54,20 L46,28" fill="none" stroke="#c9c7da" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return f'<div style="display:flex;justify-content:center;gap:18px;align-items:flex-start">{grp("C", 3, "2 black keys: C D E", RED, "#fdeee8")}<div style="align-self:center;text-align:center;margin-top:-20px">{arrow}<div style="font-family:CV,cursive;font-size:15px;color:#6d6f9c;line-height:1.1">on the piano<br>E and F touch</div></div>{grp("F", 4, "3 black keys: F G A B", NAV, BLUE)}</div>'
P22 = ppage(f"""{head('Part I · Pitch · 1', 'The keyboard', 'Left is <b>low</b>, right is <b>high</b>. The black keys come in groups of <b>two</b> and <b>three</b>. Each group has a first white key, just to its left: <b>C</b> for the two, <b>F</b> for the three. Find the group, find its first key, then walk on.')}
{hero(hero_apart(), 'Pulled apart: each family has a first key (start) and a last key (end)')}
{inaction('Higher or lower?', kq('C', 15, 44, 132, label=False, dots=(4, 9), tags={4: 'first', 9: 'second'}, tagcol={4: NAV, 9: NAV}), ['<b>Find the two red keys.</b>', '<b>Which one is further right?</b>', '<b>Right means higher:</b> play both and listen.'], 'The second note is <b>higher</b>: it is to the right. Left is always lower, right always higher.')}
<div class="xlate">{rule('<b>Find the group, then its first key.</b> Looking for D or E? Find two black keys and start on C. Looking for G, A or B? Find three black keys and start on F. You never have to count from far away.')}
{hero(qkb('C', 21, 30, 128, label=False, shade={i: ('#fbd0c2' if i % 7 == 0 else ('#dfe3f5' if i % 7 == 3 else '#fff')) for i in range(21)}, tags={0: 'C', 3: 'F', 7: 'C', 10: 'F', 14: 'C', 17: 'F'}, tagcol={3: NAV, 10: NAV, 17: NAV}), 'The pattern repeats all the way along: every two starts on C, every three on F')}</div>
<!--SPLIT-->
<div class="xlate"><div class="keep">{h3('Seven letters, round and round')}<p>The white keys use only seven letters: <b>A B C D E F G</b>. There is no H. After G the next key is <b>A</b> again, and the seven letters go round and round, like the days of the week, all the way up the keyboard. <b>C D E</b> always sit round the two black keys, <b>F G A B</b> round the three. <b>E–F</b> and <b>B–C</b> have no black key between.</p>
{hero(qkb('A', 15, 42, 128, label=True, shade={i: ('#fdeee8' if 'CDEFGAB'[(5 + i) % 7] in 'CDE' else BLUE) for i in range(15)}, tags={7: 'A again', 14: 'A again'}), 'A B C D E F G, A B C D E F G, A …: after G, back to A')}</div></div>
<div class="xlate">{hero('<div style="display:flex;justify-content:center;gap:46px">' + ''.join(f'<div style="text-align:center">{qkb(st, 4, 50, 160, label=True, shade={1: "#fbd0c2", 2: "#fbd0c2"})}<div style="font-family:AH,Arial;font-weight:700;font-size:15px;color:#e4572e;margin-top:4px">{k}–{n}: no black key between</div></div>' for st, k, n in (('D', 'E', 'F'), ('A', 'B', 'C'))) + '</div>', 'The only two pairs of white keys that touch: E–F and B–C')}</div>
<div class="xlate"><div class="keep">{h3('Going down: say it backwards')}<p>Walking <b>left</b>, down the keyboard, the letters run <b>backwards</b>: G F E D C B A, then G again. Practise saying them backwards until it is as quick as forwards: reading music that goes down depends on it.</p>
<div style="text-align:center;font:700 24px AH,Arial;color:#e4572e;letter-spacing:.12em;margin:4px 0 -4px">← walk left: A G F E D C B A</div>{kq('A', 8, 50, 130, label=True, nums=tuple(('w', 7 - k, str(k + 1), True) for k in range(8)), shade={i: '#fdeee8' for i in range(8)})}</div></div>
{inaction('Walk down from E', kq('A', 8, 46, 124, label=False, tags={4: 'E'}, q=(3, 2, 1, 0), shade={4: '#fbd0c2'}), ['<b>Start on E</b>, between the two black keys.', '<b>Step left</b> one white key at a time: name each one.', '<b>Fill the gaps</b> out loud too: G _ E _ C.'], 'E <b>D C B A</b>: backwards. And G <b>F</b> E <b>D</b> C.')}
<div class="xlate">{two(h3('Where the keyboard starts') + '<p>The very first key, bottom left, is an <b>A</b>. Look at the black keys there: only <b>one</b>, on its own. It is a group of three that has been cut off: only its end is left. The end of F G A B is <b>A B</b>, so the piano starts on A. After A and B comes the first full group of two, and its first key is <b>Lowest C</b>.</p>' + qkb('A', 3, 52, 130, label=True, shade={0: '#e9e9f5', 1: '#e9e9f5', 2: '#fbd0c2'}, tags={0: 'first key', 2: 'Lowest C'}, tagcol={0: NAV}),
     h3('Where it ends') + '<p>The very last key, top right, has <b>no black key</b> after it. Look left: the last group is <b>three</b> black keys, F G A B. After B comes C, the first key of a new group of two that was never built. So the last key is a <b>C</b>: <b>Highest C</b>.</p>' + qkb('F', 5, 46, 130, label=True, shade={i: '#e9e9f5' for i in range(4)} | {4: '#fbd0c2'}, tags={1: 'last three', 4: 'Highest C'}, tagcol={1: NAV}))}</div>
<!--SPLIT-->
<div class="xlate"><div class="keep">{h3('The eight Cs have names')}<p>Count the Cs from the bottom and there are eight. The C nearest the middle is <b>Middle C</b>. Either side are <b>Bass C</b> and <b>Treble C</b>; further out, <b>Low C</b> and <b>High C</b>. At the ends: <b>Lowest C</b> at the bottom; at the top, <b>Very High C</b>, then <b>Highest C</b>, the very last key. (No Very Low C: the piano starts on A.) From one C to the next is an <b>octave</b>: C D E F G A B C, eight notes, both Cs counted.</p><p class=\"sm\">Theory books and apps number them from the bottom instead: C1 is Lowest C, C4 Middle C, C8 Highest C.</p>
{hero(qkb('A', 52, 13, 128, label=False, dots=(2, 9, 16, 23, 30, 37, 44, 51), tags={2: 'Lowest C', 9: 'Low C', 16: 'Bass C', 23: 'Middle C', 30: 'Treble C', 37: 'High C', 44: 'Very High C', 51: 'Highest C'}, tagcol={23: RED, 2: NAV, 9: NAV, 16: NAV, 30: NAV, 37: NAV, 44: NAV, 51: NAV}), 'All 88 keys, eight Cs: the five in the middle, Low C to High C, are the ones you will use most')}</div></div>
{inaction('Find Bass C and Treble C', kq('C', 15, 48, 176, label=False, tags={7: 'Middle C'}, q=(0, 14), shade={7: '#fbd0c2'}), ['<b>Start on Middle C.</b>', '<b>Walk left</b> to the next pair of black keys. The C just left of it is one <b>?</b>.', '<b>Walk right</b> the same way, to the next pair: the other <b>?</b>.'], 'Left <b>?</b>: <b>Bass C</b>. Right <b>?</b>: <b>Treble C</b>. Each is one octave, eight notes, from Middle C.')}
<!--SPLIT-->
{inaction('Find three keys: B, E and G', kq('C', 15, 46, 150, label=False, nums=(('w', 6, '1', True), ('w', 9, '2', True), ('w', 11, '3', True)), dots=(3, 7), tags={3: 'F', 7: 'C'}, tagcol={3: NAV, 7: NAV}), ['<b>Which family?</b> C D E sit round the <b>two</b> black keys; F G A B round the <b>three</b>.', '<b>Find its first key:</b> C or F (the red dots).', '<b>Walk on</b> to each numbered key and name it.'], '1 is <b>B</b>, the last of F G A B · 2 is <b>E</b>, the last of C D E · 3 is <b>G</b>, one key after F. Find the group, find its first key, walk on: no counting from far away.')}
<!--SPLIT-->
{youknow('Hot Cross Buns, on three black keys', kq('E', 5, 66, 176, label=False, nums=(('b', 1, 2, True), ('b', 2, 3, True), ('b', 3, 4, True))), 'Right hand, fingers <b>2 3 4</b> on the three black keys (thumb is 1, little finger 5). Play from the top: <b class="co">4 3 2</b>, 4 3 2, then quickly, twice as fast, <b class="co">2 2 2 2, 3 3 3 3</b>, and 4 3 2 to finish. A whole tune, and not one white key.', 'Find another group of three, higher up, and play it again there.')}
{thinkt('The black keys are bumps you can feel in the dark. Close your eyes and slide your hand along: two bumps, and the key to their left is C; three bumps, and the key to their left is F.')}
{watch(['Counting every key from C: find the nearest group and start from its C or F.', 'Mixing up the families: C is left of the <b>two</b> black keys, F left of the <b>three</b>.'])}
{foot('The staff and the clefs p. {{P2}} · The staff and the keyboard p. {{P3}}', 'Workbook Pitch 1 · Online: Keyboard Patterns · The Musical Alphabet')}""", 22)

# ---------- 2 The staff and the clefs ----------
_T2 = {}; exec(open('/tmp/claude-0/pk/t2figs.py').read(), _T2); fig_staffnum = _T2['fig_staffnum']; fig_cde = _T2['fig_cde']; fig_linespace, fig_stepskip, fig_mnemonic = _T2['fig_linespace'], _T2['fig_stepskip'], _T2['fig_mnemonic']; fig_firstledger, fig_8va = _T2['fig_firstledger'], _T2['fig_8va']; fig_white = _T2['fig_white']; fig_readdown = _T2['fig_readdown']
P23 = ppage(f"""{head('Part I · Pitch · 2', 'The staff and the clefs', 'Music is written on a <b>staff</b>: five lines and four spaces, counted from the <b>bottom</b>. Higher on the staff means higher on the keyboard. The <b>clef</b> at the start is the key to the code: it names one line, and every other note follows from it.')}
{hero(clef_hero(), 'The treble clef is the <b>G clef</b>: it curls round G · the bass clef is the <b>F clef</b>: its dots hug F')}
<div class="xlate">{h3('Five lines, four spaces')}{fig_staffnum()}<p class="sm">Always count from the <b>bottom</b>: line 1 is the lowest line, space 1 the lowest space.</p></div>
<div class="xlate">{h3('The grand staff')}{'<p>Two staves joined by a brace: the <b>treble</b> staff on top, usually for the right hand, and the <b>bass</b> staff below, usually for the left. <b>Middle C</b> sits between them on its own short line, in either staff.</p>'}{px('gs_c', 164, 'Middle C in the treble staff (left) and in the bass staff (right): the same key.')}</div>
<!--SPLIT-->
{inaction('Which staff is this key written on?', kq('C', 15, 36, 104, tags={7: 'Middle C'}, q=(3,), shade={i: (BLUE if i < 7 else '#fdeee8') for i in range(15)}), ['<b>Find Middle C.</b>', '<b>Is the ? to its left or right?</b> Left is lower: the blue half.', '<b>Low keys go on the bass staff</b>, high keys on the treble staff.'], 'The <b>?</b> is below Middle C, so it is written on the <b>bass staff</b>, usually for the left hand.')}
{youknow('Twinkle, Twinkle, Little Star', ykfig('yk_twk', ('n3','n4','n7'), 84), 'The treble clef curls round <b class="co">line 2: G</b>, the very note Twinkle leaps up to. Read the round head, not the stem: the stem never changes the note.', 'Point to the G line, then play C C G G A A G.')}
{thinkt('A clef is a pair of glasses: the same lines, read through a different pair.')}
{watch(['Reading bass-clef notes as if they were treble: check the clef on every line.'])}
{foot('The staff and the keyboard p. {{P3}} · Reading the notes p. {{P4}}', 'Workbook Pitch 2 · Online: The Staff &amp; the Two Clefs')}""", 23)

# ---------- 3 The staff and the keyboard (her 8 Nov: before reading, so 2-3-4 never repeat) ----------
P24 = ppage(f"""{head('Part I · Pitch · 3', 'The staff and the keyboard', 'Each line and each space of the grand staff is one white key. Climb the staff and you climb the keyboard: here are two octaves, from Bass C to Treble C, with Middle C in red where the two staves meet.')}
<figure class="vx px mapf"><div class="vs">{P['map'].replace('<svg ', '<svg style="max-height:560px" ', 1)}</div></figure>
<p>Between the two staves there is only one key: <b>Middle C</b>, written twice, below the treble staff or above the bass staff. No other key is missed out.</p>
<p>One step on the staff, line to space or space to line, is the very next <b>white</b> key (the black keys come in chapter 6, p.&nbsp;{{{{P6}}}}). Up the staff is to the <b>right</b> on the keyboard; down the staff is to the <b>left</b>. A note on a line and the note in the space just above it are next-door white keys, so no key is ever missed out.</p>
{inaction('From the page to the key', px('lm_b', 124), ['<b>Name the note:</b> line 4 of the bass staff, between the clef’s dots, is F.', '<b>On the piano,</b> find the three black keys just below Middle C.', '<b>F is the first key</b> of that family: play it with the left hand.'], 'The bass-clef F is the <b>F just below Middle C</b>: left of the three black keys under it.')}
{inaction('Mirror notes either side of Middle C', ask(px('landmarks', 300).replace('class="vx px"', 'class="vx px big"', 1), ('n3', 'n4')), ['<b>Treble G:</b> the three black keys just above Middle C; G is the second key, after F.', '<b>Bass F:</b> the three black keys just below Middle C; F is the first key.', '<b>Now count each from Middle C:</b> C D E F G up, C B A G F down. Which number?'], 'Both are <b>note 5</b>: mirror images. Fold the grand staff at Middle C and treble G lands exactly on bass F; the staves meet line for line.')}
{youknow('Frère Jacques, in both hands', ykfig('yk_frere', ('n5','n6','n7','n8'), 150), 'The left hand plays the <b class="co">same letters</b>, C D E C, one octave lower, written in the bass clef.', 'Play it right hand, then left hand, then both together.')}
<!--SPLIT-->
{inaction('From the key to the page', '<div style="display:flex;gap:24px;align-items:center;justify-content:center">' + kq('C', 8, 44, 128, label=False, tags={0: 'Middle C'}, q=(2,), shade={0: '#fbd0c2'}) + '<div style="flex:1;max-width:400px">' + fig_cde() + '</div></div>', ['<b>Find the ? key:</b> count up from Middle C, C 1, D 2 …', '<b>Do the same on the staff:</b> Middle C on its ledger line, D in the space under the staff …', '<b>Where do you land?</b>'], 'The <b>?</b> is <b>E</b>, note 3, and it sits on the <b>bottom line</b> of the treble staff.')}
{watch(['Skipping a key: every line and every space is used, one white key each.', 'Counting from 0: the note you start on is note 1.'])}
{thinkt('The staff is a ladder laid beside the keyboard: each rung, a line or a space, is the next white key.')}
{try10(kbx('C', 8, 34, 104, label=True, shade={0: PINK, 7: PINK}, scale=1.0), 'Play Middle C, then walk up.', 'Say each white key as you play it, C D E F G A B C, and picture each one climbing the staff: line, space, line, space.')}
{foot('The staff and the clefs p. {{P2}} · Reading the notes p. {{P4}}', 'Workbook Pitch 3 · Online: The Staff &amp; the Two Clefs · Line and Space Names')}""", 24)

# ---------- 4 Reading the notes ----------
P25 = ppage(f"""{head('Part I · Pitch · 4', 'Reading the notes', 'Every line and space has one letter. You do not have to learn them all at once: start from a note you always know, then <b>step</b> or <b>skip</b> to the one you want.')}
{hero(pxc('gs_climb', ('n15', 'n28', 'n32'), 330), 'Middle C in the middle; treble G and bass F, the clef notes, either side. Every line and space is the next letter, with its own key underneath (the keyboard starts on G, so its first black keys belong to a group of three).')}
<div class="xlate">{rule('<b>Step</b>: to the very next line or space (one letter on). <b>Skip</b>: line to the next line, or space to the next space (two letters on).')}{fig_stepskip()}</div>
<div class="xlate">{xlate('Read the shape, not just the notes', '<p>Good readers see the jumps before the letters. Notes that touch, line then space, are a <b>step</b>: the next letter. Notes with one line between them, line to line or space to space, are a <b>skip</b>: one letter missed out. Name the first note, then let the shape name the rest: up a step, up a skip, down a step.</p>')}</div>
<!--SPLIT-->
<div class="xlate">{h3('Line note or space note?')}{fig_linespace()}<p class="sm">Count both from the bottom: line 1 is the bottom line, space 1 the bottom space.</p></div>
<div class="xlate">{h3('Words to remember the lines and spaces')}{fig_mnemonic()}</div>
<!--SPLIT-->
{inaction('Read a line note with its sentence', '<div style="display:flex;justify-content:center;gap:24px;align-items:center"><div style="flex:1;min-width:0">' + ask(px('ia_read', 150), (), True) + '</div><div style="flex:1;min-width:0">' + ask(ykfig('ex_bf', ('n3',), 150), ('n3',)) + '</div></div>', ['<b>Treble lines:</b> <i>Every Good Boy Deserves Fun</i>. The red note on line 4 is the fourth word.', '<b>Bass lines:</b> <i>Great Big Dragons Fly Away</i>. The red note on line 3 is the third word.', '<b>Check each</b> from its clef note: treble G, bass F.'], 'Treble line 4: <b>D</b> (Deserves). Bass line 3: <b>D</b> (Dragons). Same letter, different keys: the clef decides.')}
{inaction('One line, two notes', '<div style="display:flex;justify-content:center;gap:24px"><div style="flex:1;min-width:0">' + ask(ykfig('tr_lines', ('n1',), 150), ('n1',), True) + '</div><div style="flex:1;min-width:0">' + ask(ykfig('bs_lines', ('n1',), 150), ('n1',), True) + '</div></div>', ['<b>Look at the red notes:</b> both sit on the bottom line.', '<b>Now look at the clefs:</b> treble on the left, bass on the right.', '<b>Use each clef’s sentence:</b> the first word of the treble lines, <i>Every…</i>; the first word of the bass lines, <i>Great…</i>.'], 'Treble bottom line: <b>E</b> (<i>Every</i>). Bass bottom line: <b>G</b> (<i>Great</i>). Same line, different note: always read the <b>clef</b> first.')}
{inaction('Read it downwards', fig_readdown(), ['<b>Start on G</b>, the clef note: line 2.', '<b>Each step down</b> is the letter before: say the alphabet backwards.', '<b>Skips down</b> go back two letters. Start on F, the top line.'], 'Steps: G <b>F E D C</b>, down to Middle C. Skips: F <b>D B G E</b>, the lines backwards.')}
<!--SPLIT-->
{inaction('Find Treble C and Bass C', '<div style="display:flex;justify-content:center;gap:24px;align-items:center"><div style="flex:1;min-width:0">' + ask(ykfig('tr_spaces', ('n3',), 150), ('n3',), True) + '</div><div style="flex:1;min-width:0">' + ask(ykfig('bs_spaces', ('n2',), 150), ('n2',), True) + '</div></div>', ['<b>Treble spaces</b> spell <i>FACE</i>: space 3 is the third letter.', '<b>Bass spaces:</b> <i>All Cows Eat Grass</i>: space 2 is the second word.', '<b>Play both:</b> one octave either side of Middle C.'], 'Treble space 3: <b>C</b>, Treble C. Bass space 2: <b>C</b>, Bass C. Mirror images, an octave above and below Middle C.')}
{youknow('Mary Had a Little Lamb', ykfig('yk_mary', ('n1','n2','n3'), 120), 'E D C: <b class="co">line, space, Middle C’s own little line</b>, one step down each time. Read the shape and the tune walks down with it.', 'Read the notes aloud before you play them.')}
{thinkt('The clef notes are lamp posts on a dark road: walk from the nearest one and you are never lost.')}
{watch(['Naming bass notes with treble names: in the bass, the bottom line is G, not E.', 'Mixing up step and skip: a step changes line to space; a skip stays on lines (or on spaces).', 'Mistaking a space note for a line note: a line runs through a line note; a space note sits between two lines.', 'Counting lines from the top: line 1 is always the bottom line.'])}
{foot('The staff and the keyboard p. {{P3}} · Ledger lines p. {{P5}}', 'Workbook Pitch 4 · Online: Line and Space Names · Steps &amp; Skips')}""", 25)

# ---------- 5 Ledger lines (her 8 Nov: its own chapter, after reading) ----------
P25b = ppage(f"""{head('Part I · Pitch · 5', 'Ledger lines', 'Some notes are too high or too low for the staff. They sit on short extra lines called <b>ledger lines</b>, spaced exactly like the staff lines. Read them the way you read the staff: step out from the nearest staff line, line, space, line.')}
{hero(side(px('gs_c2', 230), kfig('A', 5, {}, {2: ('', True)}, W=54, H=180)), 'Middle C sits on a ledger line of its own: below the treble staff, or above the bass staff. One key, two ways to write it.')}
<div class="xlate">{h3('Below and above the staff')}{px('ledger', 170, 'Treble: C, B, A below; A, B, C above.')}<p ><b>Count ledger lines from the staff outwards:</b> the first ledger line is the one nearest the staff. Step out line, space, line, and never skip one.</p></div><div class="xlate">{px('ledger_b', 170, 'Bass: E, D, C below; C, D, E above.')}</div>
<!--SPLIT-->
{inaction('Read a high note on ledger lines', ask(ykfig('ex_hi', ('n5',), 150), ('n5',)), ['<b>The top line</b> of the treble staff is F.', '<b>Step up</b> one note at a time: G sits on top of the staff, A on the first ledger line.', '<b>Keep stepping</b> to the red note: B above it, then the second ledger line.'], 'Two ledger lines above the treble staff: <b>High C</b>, two octaves above Middle C.')}
{inaction('Read a low note on ledger lines', ask(ykfig('ex_lo', ('n5',), 150), ('n5',)), ['<b>The bottom line</b> of the bass staff is G.', '<b>Step down</b> one note at a time: F in the space below, E on the first ledger line.', '<b>Keep stepping</b> to the red note: D below it, then the second ledger line.'], 'Two ledger lines below the bass staff: <b>Low C</b>, two octaves below Middle C. Its mirror is High C, two ledger lines above the treble.')}
<!--SPLIT-->
<div class="xlate">{h3('The four first ledger lines')}{fig_firstledger()}<p class="sm">Only Middle C belongs to both staves.</p></div>
{xlate('Too many ledger lines? 8va', '<p>Very high notes need lots of ledger lines, and lots of ledger lines are hard to read. So a high passage is often written lower, with <b>8va</b> and a dotted line above it: play those notes <b>one octave higher</b> (eight notes up, from a C to the next C, p. {{P1+1}}) until the dotted line stops. <b>8vb</b> under the notes means an octave lower. (On its own, 8ve is just short for octave.)</p>' + fig_8va())}
{thinkt('Ledger lines are the staff’s ladder carried on past its ends: the same rungs, just shorter. Climb them one rung at a time, from the staff outwards, and you can read any note however high or low.')}
{watch(['Reading ledger lines from the wrong end: step out from the staff.', 'Counting from the outside in: the first ledger line is the one nearest the staff.'])}
{foot('Reading the notes p. {{P4}} · Sharps, flats and naturals p. {{P6}}', 'Workbook Pitch 5 · Online: Ledger Lines')}""", 26)

# ---------- 6 Sharps, flats and naturals ----------
acc = [[gsym('♯', 28), 'sharp', 'one key to the right (a semitone higher)', 'Level 0'], [gsym('♭', 28), 'flat', 'one key to the left (a semitone lower)', 'Level 0'], [gsym('♮', 28), 'natural', 'cancels a sharp or flat: back to the white key', 'Level ½']]
P26 = ppage(f"""{head('Part I · Pitch · 6', 'Sharps, flats and naturals', 'A sign in front of a note moves it to the very next key. <b>Sharp</b>: one key to the <b>right</b>, a <b>semitone</b> higher. <b>Flat</b>: one key to the <b>left</b>, a semitone lower. Usually that next key is black, which is how the black keys get their names. These signs are called <b>accidentals</b>.')}
{hero(keyboard('C', 5, 86, 278, label=True, shade={1: BLUE}, marks=[f'<circle cx="{1.5 * 86}" cy="202" r="13" fill="#fff" stroke="{NAV}" stroke-width="2.4"/>', f'<circle cx="{2 * 86}" cy="97" r="13" fill="{RED}"/>', f'<circle cx="{1 * 86}" cy="97" r="13" fill="{RED}"/>', f'<text x="{2 * 86}" y="54" text-anchor="middle" font-family="AH,Arial" font-size="17" font-weight="700" fill="#fff">D♯</text>', f'<text x="{1 * 86}" y="54" text-anchor="middle" font-family="AH,Arial" font-size="17" font-weight="700" fill="#fff">D♭</text>', f'<path d="M{1.5 * 64 + 8},132 Q{1.75 * 86},100 {2 * 64 - 4},90" fill="none" stroke="{RED}" stroke-width="3.5" stroke-linecap="round" marker-end="url(#ah)"/>', f'<path d="M{1.5 * 64 - 8},132 Q{1.25 * 86},100 {1 * 64 + 4},90" fill="none" stroke="{RED}" stroke-width="3.5" stroke-linecap="round" marker-end="url(#ah)"/>', f'<defs><marker id="ah" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker></defs>'], scale=1.0), '♯ one key right · ♭ one key left')}
{tbl(['Sign', 'Name', 'What it does', 'First met'], acc, ['12%', '20%', '50%', '18%'])}
<!--SPLIT-->
{inaction('Find F♯ and B♭', kq('C', 8, 64, 176, label=False, qb=(3, 5), dots=(3, 6), tags={3: 'F', 6: 'B'}, tagcol={3: NAV, 6: NAV}), ['<b>Find F and B</b> (the red dots): F just left of the three black keys, B just right of them.', '<b>Sharp means right:</b> F♯ is the very next key to the right of F.', '<b>Flat means left:</b> B♭ is the very next key to the left of B. Black or white?'], 'The left <b>?</b> is <b>F♯</b>, the first black key of the three; the right <b>?</b> is <b>B♭</b>, the highest one, on the right.')}
<div class="xlate"><p class="sm">A <b>semitone</b> is the smallest step on the piano: from one key to the very next, black or white (American books call it a <i>half step</i>). More on p. {{{{P7}}}}. With no black key between (E–F, B–C), the next key is white: E♯ = F and B♯ = C; F♭ = E and C♭ = B. And every black key has two names: C♯ = D♭.</p>{fig_white()}</div>
<!--SPLIT-->
<div class="xlate">{rule('<b>A sign belongs to one line or space.</b> It changes only that line or space, in that octave, and only until the bar line. The same letter in another octave, and every other note, stays as it is.')}<p class="sm">A <b>bar</b> is the space between two <b>bar lines</b> (p. {{{{T1}}}}). A <b>key signature</b> at the start of every line is different: it lasts the whole piece (p. {{{{S3}}}}). And a natural cancels a sharp just as it cancels a flat.</p></div>
{inaction('How long does the sharp last?', side(ask(px('acc_bar', 84), ('n2', 'n4', 'n5')), kfig('D', 5, {2: ('F♯', True)}, {2: ('', False)})), ['<b>The first note</b> has a sharp: F♯.', '<b>Later in the same bar</b> there is no sign. Is it still sharp?', '<b>After the bar line</b>: is it still sharp?'], 'Still <b>F♯</b> until the bar line; after it, plain <b>F</b> again. A sign lasts <b>to the end of its bar</b>.')}
{inaction('A natural cancels the flat', side(ask(px('acc_nat', 88), ('n4',)), kfig('G', 4, {1: ('B♭', True)}, {2: ('B♮', True)})), ['<b>B</b>: the white key.', '<b>B♭</b>: one key left, and it stays flat for the rest of the bar.', '<b>The last note</b> has a natural sign: what does it do?'], 'The natural <b>cancels</b> the flat: back to the white key B, until the bar line.')}
{inaction('One key, two names', side(ask(px('enh', 84), ('n6',)), kfig('C', 7, {0: ('C♯/D♭', False), 3: ('F♯/G♭', True)}, {3: ('E♯', True)})), ['<b>The first bar:</b> F♯, then G♭. Find both on the keyboard.', '<b>Are they different keys?</b>', '<b>The last bar:</b> E♯. Which key is one right of E?'], 'F♯ and G♭ are the <b>same black key</b>; E♯ is the white key <b>F</b>, so the <b>?</b> is plain F, the same key as E♯. Same sound, different names: <b>enharmonic</b>. The same trick with no black key between: <b>B♯</b> is the white key C, <b>F♭</b> is the white key E.')}
{youknow('Für Elise (Beethoven)', ykfig('yk_elise', ('n2','n4'), 112), 'E, <b class="co">D♯</b>, E, <b class="co">D♯</b>: the next key down and back. The bar line wipes the sharp out, so it is written again; later the D needs a <b>natural</b>, or it would still be D♯.', 'Play E and D♯ back and forth: the black key just left of E.')}
{thinkt('A sharp or flat is a sticky note on one line of the staff: it stays stuck until the bar line, then it falls off.')}
{watch(['Carrying a sharp or flat past the bar line: after it, the note is plain again.'])}
{foot('Keys and key signatures p. {{S3}}', 'Workbook Pitch 6 · Online: Accidentals · Tones &amp; Semitones')}""", 26)

# ---------- 6 Counting intervals ----------
def hopkb(start, n_white, W, H, a, nh, label=True, ends=True, scale=1.0, cap=None):
    """count the hops: from white key a, nh hops up (every key, black and white), arcs numbered 1..nh, both end keys red."""
    seq = []
    for j in range(a, a + 14):
        seq.append(('w', j))
        if _WH[(_WH.index(start) + j) % 7] in 'CDFGA': seq.append(('b', j))
    t, j = seq[nh]; shade = {a: '#f6c2b0'}
    for tt, jj in seq[1:nh]:
        if tt == 'w': shade[jj] = '#fdf1ec'
    if t == 'w': shade[j] = '#f6c2b0'
    nums = [(tt, jj, k + 1, False) for k, (tt, jj) in enumerate(seq[1:nh])]   # her 7 Nov: number the keys IN BETWEEN (her snowman count)
    tg = {a: 'start'}; tc = {a: NAV}
    s = qkb(start, n_white, W, H, nums=nums, shade=shade, label=label, scale=scale, tags=tg, tagcol=tc)
    if t == 'b':   # the black end key in red
        BW, BH = W * 0.58, H * 0.6; x = (j + 1) * W - BW / 2
        s = s.replace('</svg>', f'<rect x="{x:.1f}" y="0" width="{BW:.1f}" height="{BH:.1f}" rx="1.5" fill="{RED}"/></svg>')
    return s
P27 = ppage(f"""{head('Part I · Pitch · 7', 'Counting intervals', 'The smallest step on the piano is a <b>semitone</b>: from one key to the very next. Two semitones make a <b>tone</b>. Bigger distances are <b>intervals</b>: to give one a number, <b>count the notes</b>, both ends included.')}
{hero('<div style="display:flex;gap:18px;align-items:center"><div style="flex:1.3;min-width:0">' + px('tones', 170) + '</div><div style="flex:1;min-width:0">' + qkb('C', 8, 46, 150, label=True, shade={2: '#fbd0c2', 3: '#fbd0c2', 6: '#fbd0c2', 7: '#fbd0c2', 0: BLUE, 1: BLUE}) + '</div></div>', 'E–F and B–C: next door, a semitone. C–D and F–G: a black key between, a tone.')}
{rule('<b>Semitone:</b> the very next key, with nothing between: white to white (E–F, B–C), white to black, or black to white. <b>Tone:</b> exactly one key between.')}
{inaction('Tone or semitone?', kq('C', 8, 56, 150, dots=(2, 3)), ['<b>Look between the red keys:</b> is there a black key?', '<b>No black key</b> means they are next-door keys.', '<b>Now try C and D</b>: is there a black key between?'], 'E–F is a <b>semitone</b> (next door). C–D has C♯ between: a <b>tone</b>.')}
<div class="xlate">{h3('Intervals: count the notes')}<figure class="vx" style="border:0;background:none">{hero_third()}<figcaption>C to E: count the notes, 1 2 3: a 3rd</figcaption></figure>
{rule('<b>Count the letters</b> for the number: start at 1 on the first note and count white keys, or lines and spaces, never the black keys. C to E is C D E: 3 notes, a <b>3rd</b>. Sharps and flats never change the number.')}</div>
<div class="xlate">{h3('Interval numbers from C')}
{px('intv', 120)}{kq('C', 8, 50, 96, label=True, nums=tuple(('w', i, str(i + 1), i in (0, 2, 4, 7)) for i in range(8)))}</div>
<!--SPLIT-->
{inaction('How far apart are these notes?', px('ia_iv', 120), ['<b>Call the first note 1:</b> here F is 1.', '<b>Count every letter</b> up to the second note.', '<b>Going down works the same:</b> start at 1 on the top note and count down.'], 'F G A is 3 notes: a <b>3rd</b>. C B A G is 4 notes: a <b>4th</b>.')}
{inaction('Name an interval on the keyboard', kq('C', 8, 50, 120, dots=(2, 7)), ['<b>Find both red keys:</b> E, and the C above it.', '<b>Count the notes</b> from E: E is 1 …', '<b>Stop on the C.</b> What number is it?'], 'E F G A B C is 6 notes: a <b>6th</b>.')}
<!--SPLIT-->
{inaction('Melodic or harmonic?', px('mel_harm', 88), ['<b>The first bar:</b> C, then E, one after the other.', '<b>The second bar:</b> C and E at the same time.', '<b>Count the notes</b> in each.'], 'Both are a <b>3rd</b>: <b>melodic</b> when played one after the other, <b>harmonic</b> when played together.')}
{try10(kbx('C', 8, 30, 88, label=True, shade={0: PINK, 4: PINK}, scale=1.0), 'Thumb on C, finger 5 on G.', 'Your hand is a ruler: thumb to little finger on white keys is a 5th. Play it, then thumb to finger 3: a 3rd.')}
{watch(['Counting only the gaps: C to E is 3 notes, not 2 gaps. And a sharp or flat never changes the number: C to G♯ is still a 5th.'])}
{foot('Major, minor and perfect p. {{P8}} · Major scales p. {{S1}}', 'Workbook Pitch 7 · Online: Intervals · Tones &amp; Semitones')}""", 27)

# ---------- 7 Major, minor and perfect ----------
iv = [['3rd', '2 (minor)', '3 (major)'], ['4th', '', '4 (perfect)'], ['5th', '', '6 (perfect)'], ['6th', '7 (minor)', '8 (major)'], ['octave', '', '11 (perfect)']]
P28 = ppage(f"""{head('Part I · Pitch · 8', 'Major, minor and perfect', 'C to E and C to E♭ are both 3rds: three notes each. But they sound different, bright and dark. To tell them apart, <b>count the keys in between</b>, black and white: the keys you do not play.')}
{hero(two(hopkb('C', 7, 70, 190, 0, 4) + '<p class="sm">C to <b class="co">E</b>: 3 keys between. A <b>major</b> 3rd: bright.</p>', hopkb('C', 7, 70, 190, 0, 3) + '<p class="sm">C to <b class="co">E♭</b>: 2 keys between, one fewer. A <b>minor</b> 3rd: dark.</p>'), 'One key fewer between: a major 3rd becomes minor')}
{rule('<b>Count the notes</b> for the number (a 3rd). <b>Count the keys in between</b> for the size (major or minor): black and white, not the two you play.')}
<p class="sm">Why count the keys in between? Because the size is what you hear: one key more or less turns bright into dark, or makes a 5th sound hollow and strange.</p>
{two(tbl(['Number', 'Keys between: minor', 'Major or perfect'], iv, ['30%', '35%', '35%']), '<p><b>3rds and 6ths</b> come in two sizes: <b>major</b> and <b>minor</b>.</p><p><b>4ths, 5ths and octaves</b> have one main size, called <b>perfect</b>. They are never major or minor.</p>', '1.15fr 1fr')}
<div class="xlate">{h3('A perfect 4th')}{hopkb('C', 7, 46, 118, 0, 5)}<p class="sm">C to <b class="co">F</b>: four notes, a 4th, with <b>4 keys between</b>: a <b>perfect 4th</b>.</p></div>
{inaction('Major or minor 3rd? A up to C', hopkb('C', 8, 44, 128, 5, 3), ['<b>Count the notes:</b> A B C, three letters, so it is a 3rd.', '<b>Count the keys in between:</b> they are numbered.', '<b>A major 3rd has 3 between.</b> How many here?'], 'A to C has <b>2 keys between</b> (B♭ and B): one fewer than major, a <b>minor 3rd</b>. Dark, like C to E♭.')}
<!--SPLIT-->
{inaction('Name F up to A', hopkb('C', 8, 44, 128, 3, 4), ['<b>Count the notes:</b> F G A is 3, so it is a 3rd.', '<b>Count the keys in between:</b> they are numbered.', '<b>3 between, or 2?</b>'], 'F to A has 3 keys between: a <b>major 3rd</b>, the same size as C to E.')}
{youknow('Beethoven, Symphony No. 5', ykfig('yk_b5', ('n2','n3','n4','n5'), 128), 'Da-da-da-DUM: G down to <b class="co">E♭</b> is three notes, a 3rd, with 3 keys between (F♯, F, E): a <b>major 3rd</b>. Counting down works the same way.', 'Count the keys between G and E♭ on the keyboard.')}
<!--SPLIT-->
{inaction('Name D up to A', hopkb('C', 8, 52, 150, 1, 7), ['<b>The number:</b> D E F G A, five notes, a 5th.', '<b>The size:</b> count the keys in between: the numbered keys.', '<b>A 5th with 6 between</b> is its main size. What is that called?'], 'D up to A is a <b>perfect 5th</b>: 6 keys between.')}
{watch(['Counting white keys only: count every key between, black and white.', 'Calling a 4th or 5th “major”: they are perfect.', 'C–D♯ is a 2nd, C–E♭ a 3rd: the same keys, but the letters decide the number.'])}
{thinkt('A major and a minor 3rd are a smile and a frown: the same face, one small change at the corners.')}
{foot('Counting intervals p. {{P7}} · Chords and triads p. {{H1}}', 'Workbook Pitch 8 · Online: Intervals (Major or minor 3rd)')}""", 28)
