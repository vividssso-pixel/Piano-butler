# The Piano Butler Handbook, Part II: Time, v2 (legible type, engraved notation, no pills)
import json, base64, re
V = json.load(open('/tmp/claude-0/vrv/out.json'))
HLT = {'ia_waltz': ['n1', 'n4', 'n7'], 'ia_dot': ['n1', 'n2', 'n3'], 'ia_anac': ['n1', 'n5'], 'ia_sync': ['n2'], 'ia_68': ['n1', 'n4', 'n7', 'n8'], 'ia_rest': ['n3', 'n5']}   # the notes that matter, coral
for _k, _ids in HLT.items():
    for _n in _ids:
        for _c in ('note', 'rest'): V[_k] = V[_k].replace(f'<g id="{_n}" class="{_c}">', f'<g id="{_n}" class="{_c}" fill="#e4572e" color="#e4572e" stroke="#e4572e">')
def inact(title, fig, steps, result): return '<div class="inact2"><div class="bh">Example</div><b class="it">' + title + '</b><div class="ia2">' + fig + '<ol>' + ''.join(f'<li><span class="in">{i + 1}</span><span>{t}</span></li>' for i, t in enumerate(steps)) + '</ol></div><div class="ires">' + result + '</div></div>'
def youknow(title, fig, line, tryit='', wide=False):   # her 4 Nov: one tune everyone knows, on the staff, the point in red: the 'aha' (replaces In real music); wide: the music takes the full width
    return '<div class="yk"><div class="bh">You know this</div><b class="it">' + title + '</b><div class="ykg"' + (' style="grid-template-columns:1fr"' if wide else '') + '>' + fig + '<p>' + line + '</p></div>' + (f'<p class="tryit"><b>Try it.</b> {tryit}</p>' if tryit else '') + '</div>'
def realm(title, items, tryit=''):   # 'In real music': where the idea lives across all music, not only exams
    return '<div class="realm"><div class="bh">In real music</div><b class="it">' + title + '</b><div class="rmg">' + ''.join(f'<div><i>{g}</i><span>{t}</span></div>' for g, t in items) + '</div>' + (f'<p class="tryit"><b>Try it.</b> {tryit}</p>' if tryit else '') + '</div>'
def listen(items):
    return '<div class="lis"><p class="lish">Listen for it</p><div class="lisg">' + ''.join('<div><b>'+a+'</b><span>'+b+'</span><i>'+c+'</i></div>' for a,b,c in items) + '</div></div>'
import math as _pm
def _slices(n):   # slice angles, ordered left to right like counting (her 4 Nov)
    sl = [(-_pm.pi / 2 + 2 * _pm.pi * i / n, -_pm.pi / 2 + 2 * _pm.pi * (i + 1) / n) for i in range(n)]
    return sorted(sl, key=lambda a: (round(_pm.cos((a[0] + a[1]) / 2), 3), round(_pm.sin((a[0] + a[1]) / 2), 3)))
def pizza(n, fill=0, R=15, apart=0, rest=False):   # one beat as a pizza cut into n slices, the first `fill` red; apart > 0 pulls the slices apart (single notes; a beamed group stays joined)
    cx = cy = R + 2 + apart; W_ = 2 * R + 4 + 2 * apart; o = f'<svg viewBox="0 0 {W_} {W_}" style="width:{W_}px;height:{W_}px;display:block"><defs><pattern id="hz" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="5" height="5" fill="#fff"/><line x1="0" y1="0" x2="0" y2="5" stroke="{N}" stroke-width="1.4"/></pattern></defs>'; FC = 'url(#hz)' if rest else C
    if n == 1: return o + f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{FC if fill else "#fff"}" fill-opacity="{1 if rest else 0.85}" stroke="{N}" stroke-width="1.6"/></svg>'
    for i, (a0, a1) in enumerate(_slices(n)):
        am = (a0 + a1) / 2; dx, dy = apart * _pm.cos(am), apart * _pm.sin(am)
        o += f'<g transform="translate({dx:.1f},{dy:.1f})"><path d="M{cx},{cy} L{cx + R * _pm.cos(a0):.1f},{cy + R * _pm.sin(a0):.1f} A{R},{R} 0 0 1 {cx + R * _pm.cos(a1):.1f},{cy + R * _pm.sin(a1):.1f} Z" fill="{FC if i < fill else "#fff"}" fill-opacity="{1 if rest else 0.85}" stroke="{N}" stroke-width="1.4"/></g>'
    return o + '</svg>'
def pzc(cut, k, col, R=15, cols=None):   # one pizza cut in `cut`; the first k slices (left to right) in `col`, or each slice its own colour from `cols`
    cx = cy = R + 2; o = f'<svg viewBox="0 0 {2 * R + 4} {2 * R + 4}" style="width:{2 * R + 4}px;height:{2 * R + 4}px;display:block">'
    cols = cols or [col] * k
    if cut == 1: return o + f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{cols[0] if cols else "#fff"}" stroke="{N}" stroke-width="1.6"/></svg>'
    for i, (a0, a1) in enumerate(_slices(cut)):
        o += f'<path d="M{cx},{cy} L{cx + R * _pm.cos(a0):.1f},{cy + R * _pm.sin(a0):.1f} A{R},{R} 0 0 1 {cx + R * _pm.cos(a1):.1f},{cy + R * _pm.sin(a1):.1f} Z" fill="{cols[i] if i < len(cols) else "#fff"}" stroke="{N}" stroke-width="1.4"/>'
    return o + '</svg>'
def pizzas(cut, full, part=0, rest=False): return '<span class="pzs">' + ''.join(pizza(cut, cut if i < full else (part if i == full else 0), 13, 2.5 if cut > 1 else 0, rest) for i in range(4)) + '</span>'
def carriage(seats, x0, label=''):   # one bar as a train carriage: seats = [(kind, n)] with kind 'n' (a passenger) or 'r' (a reserved, empty seat); each seat is one beat
    W = 56; n_all = sum(t[1] for t in seats); w = n_all * W + 16
    o = f'<rect x="{x0}" y="18" width="{w}" height="62" rx="10" fill="#fff" stroke="{N}" stroke-width="2"/>'
    o += f'<circle cx="{x0 + 22}" cy="88" r="7" fill="{N}"/><circle cx="{x0 + w - 22}" cy="88" r="7" fill="{N}"/>'
    x = x0 + 8
    for kind, n, k in seats:
        fill = '#f2b9a5' if kind == 'n' else 'url(#hz2)'
        o += f'<rect x="{x + 3}" y="30" width="{n * W - 6}" height="40" rx="6" fill="{fill}" stroke="{N}" stroke-width="1.4"/>'
        g = (NT if kind == 'n' else RS)[k]
        o += f'<text x="{x + 18}" y="{60 if kind == "n" else 57}" font-family="NM" font-size="{26 if kind == "n" else 24}" fill="{N}" style="paint-order:stroke" stroke="#fff" stroke-width="{0 if kind == "n" else 5}">{g}</text>'
        for j in range(1, n): o += f'<line x1="{x + j * W}" x2="{x + j * W}" y1="34" y2="66" stroke="{N}" stroke-width="1" stroke-dasharray="3 3" opacity=".45"/>'
        x += n * W
    o += ''.join(f'<text x="{x0 + 8 + j * W + W / 2}" y="12" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="{C}">{j + 1}</text>' for j in range(n_all))
    return o, w
def train(bars, ts='3/4'):
    o = '<defs><pattern id="hz2" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#fff"/><line x1="0" y1="0" x2="0" y2="6" stroke="#26296b" stroke-width="1.4"/></pattern></defs>'
    top, bot = ts.split('/')   # the engine carries the time signature
    o += f'<path d="M4,80 L4,30 Q4,18 16,18 L60,18 Q72,18 72,30 L72,80 Z" fill="{N}"/><text x="38" y="47" text-anchor="middle" font-family="PF,serif" font-size="27" font-weight="700" fill="#fff">{top}</text><text x="38" y="73" text-anchor="middle" font-family="PF,serif" font-size="27" font-weight="700" fill="#fff">{bot}</text><circle cx="20" cy="88" r="7" fill="{N}"/><circle cx="56" cy="88" r="7" fill="{N}"/><line x1="72" x2="86" y1="60" y2="60" stroke="{N}" stroke-width="3"/>'
    x = 86
    for i, b in enumerate(bars):
        c, w = carriage(b, x); o += c; x += w
        if i < len(bars) - 1: o += f'<line x1="{x}" x2="{x + 14}" y1="60" y2="60" stroke="{N}" stroke-width="3"/>'; x += 14
    return f'<svg viewBox="0 0 {x + 4} 100" style="width:100%;max-width:{(x + 4)}px;height:auto;display:block;margin:0 auto">{o}</svg>'
def drill(t): return '<p class="drill"><span>Two-minute drill</span><em>' + t + '</em></p>'
def thinkt(t): return '<p class="think"><span>Think of it</span>' + t + '</p>'
DK, N, C, CR, G, MUTE = '#1c1e4f', '#26296b', '#e4572e', '#fffdf7', '#2e8a6e', '#6d6f9c'
FD = '/tmp/claude-0/vrv/node_modules/@fontsource/'
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
FF = (f"@font-face{{font-family:'AH';font-weight:400;src:url(data:font/woff2;base64,{b64(FD + 'atkinson-hyperlegible/files/atkinson-hyperlegible-latin-400-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'AH';font-weight:700;src:url(data:font/woff2;base64,{b64(FD + 'atkinson-hyperlegible/files/atkinson-hyperlegible-latin-700-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'NM';src:url(data:font/woff2;base64,{b64(FD + 'noto-music/files/noto-music-music-400-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'PF';font-weight:700;src:url(data:font/woff2;base64,{b64('/tmp/claude-0/fnt/package/files/playfair-display-latin-700-normal.woff2')}) format('woff2')}}")

for _k in ('wbr34', 'wbr24'):
    if _k in V: V[_k] = V[_k].replace('class="mRest">', 'class="mRest" fill="#e4572e" color="#e4572e">')
PP = json.load(open('/tmp/claude-0/vrv/pout.json'))
def pvx(k, h=80, cap=''):   # a pitched snippet on a real staff
    svg = PP[k].replace('<svg ', '<svg style="max-height:%dpx" ' % h, 1)
    return '<figure class="vx"><div class="vs">' + svg + '</div>' + ('<figcaption>' + cap + '</figcaption>' if cap else '') + '</figure>'
ODE = '<figure class="vx"><div class="vs">' + PP['ode'].replace('<g id="n5" class="note">', '<g id="n5" class="note" style="fill:#e4572e;color:#e4572e">', 1).replace('<g id="n6" class="note">', '<g id="n6" class="note" style="fill:#e4572e;color:#e4572e">', 1).replace('<svg ', '<svg style="max-height:96px" ', 1) + '</div></figure>'   # her 4 Nov: meet the dotted crotchet in a tune everyone knows
def ykfig(k, red=(), h=72):   # a known tune on the staff, the notes that make the point in red
    s = PP[k].replace('<svg ', '<svg style="max-height:%dpx" ' % h, 1)
    for n in red:
        for c in ('note', 'rest'): s = s.replace(f'<g id="{n}" class="{c}">', f'<g id="{n}" class="{c}" style="fill:#e4572e;color:#e4572e">', 1)
    return '<figure class="vx"><div class="vs">' + s + '</div></figure>'
def vx(k, h=84, cap=''):
    return f'<figure class="vx"><div class="vs">{V[k].replace("<svg ", f"<svg style=\"max-height:{h}px\" ", 1)}</div>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>'
INK = json.load(open('/tmp/claude-0/pk/gm-ink.json'))
def gsym(ch, h=34, pad=4):
    L, R_, A, D, _ = INK['s:' + ch]; W = L + R_ + 2 * pad; H = A + D + 2 * pad
    return f'<svg viewBox="0 0 {W:.0f} {H:.0f}" style="height:{h}px;width:{h * W / H:.0f}px;display:block;margin:0 auto"><text x="{pad + L:.1f}" y="{pad + A:.1f}" font-family="NM" font-size="100" fill="{N}">{ch}</text></svg>'
def gin(kind, k, h=24): return gcell(kind, k, h).replace('display:block;margin:0 auto', 'display:inline-block;vertical-align:-6px;margin:0 2px')
def gcell(kind, k, h=42, W=100, H=140):
    ch = (NT if kind == 'n' else RS)[k]; L, R_, A, D, _ = INK[kind + ':' + k]
    x0 = W / 2 - (R_ - L) / 2; y0 = H / 2 - (D - A) / 2
    return f'<svg viewBox="0 0 {W} {H}" style="height:{h}px;width:{h * W / H:.0f}px;display:block;margin:0 auto;overflow:visible"><text x="{x0:.1f}" y="{y0:.1f}" font-family="NM" font-size="100" fill="{N}">{ch}</text></svg>'
def bars(kind, h=34):
    sw = {'bar': [(0, 3)], 'dbl': [(0, 3), (9, 3)], 'fin': [(0, 3), (9, 9)], 'rep': [(0, 9), (14, 3)], 'rep2': [(0, 3), (6, 9)]}
    def one(k, dx=0, dots=None):
        out = ''.join(f'<rect x="{dx + x}" y="0" width="{w}" height="60" fill="{N}"/>' for x, w in sw[k])
        if dots: out += ''.join(f'<circle cx="{dx + dots}" cy="{cy}" r="3.4" fill="{N}"/>' for cy in (22, 38))
        return out
    if kind == 'repeat': inner, W = one('rep', 0, 25) + one('rep2', 84, -12), 99   # start repeat |:  and end repeat :|, a clear gap between them (her 4 Nov: the end repeat needs its dots)
    else: inner, W = one({'bar': 'bar', 'dbl': 'dbl', 'fin': 'fin'}[kind]), 20
    return f'<svg viewBox="-2 -2 {W + 4} 64" style="height:{h}px;width:auto;display:block">{inner}</svg>'
def gl(ch, size=34): return f'<span class="gl2" style="font-size:{size}px">{ch}</span>'
NT = {'breve': '𝅜', 'dsb': '𝅝𝅭', 'sb': '𝅝', 'dm': '𝅗𝅥𝅭', 'm': '𝅗𝅥', 'dc': '𝅘𝅥𝅭', 'c': '𝅘𝅥', 'dq': '𝅘𝅥𝅮𝅭', 'q': '𝅘𝅥𝅮', 'sq': '𝅘𝅥𝅯', 'dsq': '𝅘𝅥𝅰', 'hdsq': '𝅘𝅥𝅱'}
RS = {'breve': '𝄺', 'dsb': '𝄻𝅭', 'sb': '𝄻', 'dm': '𝄼𝅭', 'm': '𝄼', 'dc': '𝄽𝅭', 'c': '𝄽', 'dq': '𝄾𝅭', 'q': '𝄾', 'sq': '𝄿', 'dsq': '𝅀', 'hdsq': '𝅁'}
import re as _ro
_VOID = {'br', 'img', 'hr', 'col', 'input', 'meta', 'link', 'wbr'}
_TAIL = {'inact': 1, 'inact2': 1, 'yk': 2, 'realm': 2, 'think': 3, 'watch': 4, 'links': 9}
def _nodes(t):   # top-level nodes of an HTML fragment (comments kept as their own nodes)
    out, depth, start, pos = [], 0, None, 0
    for m in _ro.finditer(r'<!--.*?-->|<(/?)([a-zA-Z][\w:-]*)((?:[^>"\']|"[^"]*"|\'[^\']*\')*?)(/?)>', t, _ro.S):
        if m.group(0).startswith('<!--'):
            if depth == 0: out.append(('gap', t[pos:m.start()])); out.append(('com', m.group(0))); pos = m.end()
            continue
        close, tag = m.group(1), m.group(2).lower(); selfc = bool(m.group(4)) or tag in _VOID
        if depth == 0 and not close:
            out.append(('gap', t[pos:m.start()])); start = m.start()
            if selfc: out.append(('el', t[start:m.end()])); pos = m.end(); continue
        if close: depth -= 1
        elif not selfc: depth += 1
        if depth == 0 and close: out.append(('el', t[start:m.end()])); pos = m.end()
    out.append(('gap', t[pos:]))
    return out
def _cat(el):
    m = _ro.match(r'<(\w+)[^>]*?class="([^"]*)"', el)
    return _TAIL.get(m.group(2).split()[0], 0) if m else 0
def order_blocks(inner):   # her 5 Nov: on every topic the boxes come in one order: the content, then In action (together), You know this, Think of it, Watch out
    ns = _nodes(inner)
    if ''.join(x for _, x in ns) != inner: return inner
    els, split_at = [], None
    for k, x in ns:
        if k == 'el': els.append(x)
        elif k == 'com' and 'SPLIT' in x: split_at = len(els)
        elif k == 'com': els.append(x)
    cats = [None] * len(els)
    for i in range(len(els) - 1, -1, -1):
        c = _cat(els[i]) if not els[i].startswith('<!--') else 0
        if _ro.match(r'<h[234][\s>]', els[i]): c = cats[i + 1] if i + 1 < len(els) else 0
        cats[i] = c
    if not any(c in (1, 2, 3, 4) for c in cats): return inner
    order = sorted(range(len(els)), key=lambda i: (cats[i], i))
    body = [_ro.sub(r'^<(\w+)', lambda m: f'<{m.group(1)} data-cat="{cats[i]}"', els[i], count=1) if cats[i] else els[i] for i in order]
    ex = [k for k, x in enumerate(body) if cats[order[k]] == 1 and '<div class="bh">Example</div>' in x]
    if len(ex) > 1:   # her 5 Nov: 'Example 1', 'Example 2' when a topic has two
        for n, k in enumerate(ex): body[k] = body[k].replace('<div class="bh">Example</div>', f'<div class="bh">Example {n + 1}</div>', 1)
    if split_at is not None: body.insert(split_at, '<!--SPLIT-->')
    return '\n'.join(body)
def page(inner, n, right='PART II · TIME'):
    inner = order_blocks(inner)
    return f'''<section class="pg"><div class="top"><span>THE PIANO BUTLER HANDBOOK</span><span>{right}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'''
def head(k, t, lead): return f'<div class="kick">{k}</div><h1>{t}</h1><p class="lead">{lead}</p>'
def h3(t): return f'<h3>{t}</h3>'
def tbl(head, rows, widths=None, cls=''):
    cg = ''.join(f'<col style="width:{w}">' for w in widths) if widths else ''
    return f'<table class="ht {cls}"><colgroup>{cg}</colgroup><thead><tr>{"".join(f"<th>{h}</th>" for h in head)}</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table>'
def lv(x): return x if x else '<span class="ex">Extra</span>'
def ts(a, b, h=29):
    w = 26 if max(len(str(a)), len(str(b))) == 1 else 40
    return f'<svg class="tsv" viewBox="0 0 {w} 44" style="height:{h}px;width:{h * w / 44:.0f}px;display:inline-block;vertical-align:middle"><text x="{w / 2}" y="20" text-anchor="middle" font-family="PF" font-weight="700" font-size="24" fill="{N}">{a}</text><text x="{w / 2}" y="41" text-anchor="middle" font-family="PF" font-weight="700" font-size="24" fill="{N}">{b}</text></svg>'
def box(t, body): return f'<div class="box"><div class="bh">{t}</div>{body}</div>'
def watch(items): return '<div class="watch"><div class="bh">Watch out</div>' + ''.join(f'<div class="wr"><span class="x">✗</span><span>{t}</span></div>' for t in items) + '</div>'
def remember(items): return '<div class="remem"><span class="rl">Remember?</span>' + ''.join(f'<span class="ri">{t} <i>p. {p}</i></span>' for t, p in items) + '</div>'
def foot(see, practise):
    nb = lambda t: t.replace('p. ', 'p.\u00a0').replace('› ', '›\u00a0')   # a page number or a menu step never splits across lines
    return f'<div class="links"><div><span class="lab">See also</span>{nb(see)}</div><div><span class="lab">Practise it</span>{nb(practise)}</div></div>'
def two(a, b, r='1fr 1fr'): return f'<div class="two" style="grid-template-columns:{r}"><div>{a}</div><div>{b}</div></div>'

flow = ''.join(f'<div class="fl"><b>{a}</b><span>{b}</span></div>' + ('<span class="fa">›</span>' if i < 4 else '') for i, (a, b) in enumerate([('Pulse and bar', 'the steady beat, in groups of 2, 3 or 4'), ('Note values', 'how long each sound and silence lasts'), ('Longer notes', 'dots and ties'), ('Time signature', 'how many beats, and which note is one beat'), ('Rhythm', 'long and short, on and off the beat')]))
OPEN = f'''<section class="pg part2"><div class="pframe"><div class="pk">Part II · When, and for how long</div><div class="pt">Time</div><div class="pdv"></div>
<p class="pl">Music never stands still. Underneath runs a steady <b>pulse</b>, packed into <b>bars</b>, and every note and rest gets its fair share. We start with the big beat and zoom in to a single note.</p>
<div class="flow">{flow}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{p - 2}</span></div>' for x, p in (('Pulse, tempo and the bar', 36), ('Notes and rests', 38), ('How long is a note?', 40), ('Time signatures', 42), ('Compound and irregular time', 44), ('Rhythm: groups and upbeats', 46), ('Rhythm: off the beat', 48), ('Tips: when the rhythm slips', 50)))}</div></div></section>'''

P36 = page(f'''{head('Part II · Time · 1', 'Pulse, tempo and the bar', 'Put your hand on your heart: that steady beat is a <b>pulse</b>, and almost every piece has one. Its speed is the <b>tempo</b>. Beats travel in groups called <b>bars</b>, and beat 1 is the strongest.')}
{two(h3('Tempo') + f'<p>Tempo is measured in beats per minute. A <b>metronome mark</b> at the top of the music shows it: <span class="mm">{gin("n", "c")} = 60</span> means 60 crotchet beats a minute, one beat a second. <span class="mm">{gin("n", "c")} = 120</span> is twice as fast. Tempo words such as <i>Andante</i> and <i>Allegro</i> come with Expression, later in the book.</p>',
     h3('Strong and weak beats') + tbl(['Beats', 'Pattern', 'Feels like'], [['2', '<b>Strong</b> weak', 'a march'], ['3', '<b>Strong</b> weak weak', 'a waltz'], ['4', '<b>Strong</b> weak <b>medium</b> weak', 'most songs']], ['16%', '50%', '34%']))}
{h3('Bars and bar lines')}
{tbl(['Sign', 'Name', 'Meaning'], [[bars('bar'), 'bar line', 'divides the music into bars'], [bars('dbl'), 'double bar line', 'marks the end of a section, or a change of key, time signature or tempo'], [bars('fin'), 'final bar line', 'marks the end of the piece'], [bars('repeat'), 'repeat signs', 'play the passage between them again; if there is no start sign, go back to the beginning']], ['18%', '24%', '58%'])}
<!--SPLIT-->
{h3('The beat in tunes you know')}
{tbl(['Tune', 'Beats in a bar', 'Pattern'], [['Twinkle, Twinkle, Little Star', '4', '<b>Strong</b> weak <b>medium</b> weak'], ['Happy Birthday', '3', '<b>Strong</b> weak weak'], ['The Blue Danube (a waltz)', '3', '<b>Strong</b> weak weak'], ['Radetzky March', '2', '<b>Strong</b> weak']], ['46%', '20%', '34%'])}
{h3('Counting')}
{vx('t34', 84, 'Three bars of 3/4. Every beat is counted, even inside a long note: the red number is where you play, the grey numbers are the beats you hold.')}
<p>Count aloud at one speed, a little louder on beat 1. With a metronome, start slower than you think and speed up only when the passage is steady.</p>
{inact('Is this a march or a waltz?', vx('ia_waltz', 70), ['<b>Tap a steady beat</b> as you clap or listen.', '<b>Find the strong one:</b> the red beats feel heavier.', '<b>Count the gap</b> between strong beats: 1 2 3, 1 2 3.'], 'Groups of three: a <b>waltz</b>, in 3/4. Groups of two would be a march.')}
{youknow('Radetzky March (Johann Strauss I)', ykfig('yk_clap', ('n1','n2','n3','n4','n5','n6'), 66), 'At the New Year concert the audience claps along on <b class="co">every beat</b>. That steady clap is the pulse; the orchestra’s tune moves freely over it.', 'Put on any march and clap only the beat, not the tune.')}
{inact('Feel the beat before you play', '<div><p class="mmk"><span class="mm">' + gin("n", "c") + ' = 96</span></p>' + vx('t34', 72) + '</div>', ['<b>Read the mark:</b> <span class="mm">' + gin("n", "c") + ' = 96</span>, 96 crotchet beats a minute.', '<b>Listen first:</b> set the metronome and let one full bar go by, counting “1 2 3” in your head.', '<b>Step in</b> on the next beat 1, the way you step onto a moving escalator.'], 'The first note lands <b>on the beat</b>, not a guess.')}
{thinkt('The beat is the stage and the notes are the actors: the stage is there before anyone walks on. So step in the way you step onto an escalator or take a plate off a sushi train: watch it move for a bar, then join in.')}
{watch(['Speeding up in the easy bars and slowing down in the hard ones: the pulse stays the same all the way through.', 'Counting only the notes you play: the beat goes on through long notes and rests.'])}
{foot('Time signatures p. 39 · Tempo words: Expression (later)', 'Workbook Level 0 · Pulse · Online: Metronome')}''', 36)

rows = [('breve', 'breve', 'double whole note', '8', 'Level 4'), ('dsb', 'dotted semibreve', 'dotted whole note', '6', ''), ('sb', 'semibreve', 'whole note', '4', 'Level 0'), ('dm', 'dotted minim', 'dotted half note', '3', 'Level 0'), ('m', 'minim', 'half note', '2', 'Level 0'), ('dc', 'dotted crotchet', 'dotted quarter note', '1½', 'Level ½'),
        ('c', 'crotchet', 'quarter note', '1', 'Level 0'), ('dq', 'dotted quaver', 'dotted eighth note', '¾', 'Level 3'), ('q', 'quaver', 'eighth note', '½', 'Level 0'), ('sq', 'semiquaver', 'sixteenth note', '¼', 'Level 2'), ('dsq', 'demisemiquaver', '32nd note', '⅛', ''), ('hdsq', 'hemidemisemiquaver', '64th note', '¹⁄₁₆', '')]
NTAB = '<table class="ht nt"><colgroup><col style="width:9%"><col style="width:9%"><col style="width:28%"><col style="width:26%"><col style="width:10%"><col style="width:18%"></colgroup><thead><tr><th>Note</th><th>Rest</th><th>Name</th><th>Also called</th><th>Beats*</th><th>First met</th></tr></thead><tbody>' + ''.join(
    f'<tr><td class="g">{gcell("n", k)}</td><td class="g">{gcell("r", k)}</td><td><b>{n}</b></td><td class="mu">{us}</td><td><b>{b}</b></td><td>{lv(l)}</td></tr>' for k, n, us, b, l in rows) + '</tbody></table>'
PZBOX = '<div class="pzbox"><b class="it">Why whole, half and quarter?</b><p class="sm" style="margin:2px 0 6px">Think of each beat as a pizza. A bar of 4/4 is four pizzas. The note that fills the whole bar is the <b>whole note</b>; the others are a half, a quarter, an eighth and a sixteenth of it. Two quavers beamed together fill one pizza. A rest is the same share left empty: shaded with lines.</p> ' + ''.join(f'<div class="pzrow{" pzrr" if rs else ""}"><span class="pzn">{gin(g, k)} {nm}</span>{pizzas(cut, full, part, rs)}<span>{oc}</span><span class="pzb">{bt}</span></div>' for k, nm, cut, full, part, oc, bt, rs, g in (('sb', 'semibreve', 1, 4, 0, 'whole note', '4 pizzas · 4 beats', False, 'n'), ('sb', 'semibreve rest', 1, 4, 0, 'silence', '4 empty pizzas · 4 beats', True, 'r'), ('m', 'minim', 1, 2, 0, 'half note', '2 pizzas · 2 beats', False, 'n'), ('m', 'minim rest', 1, 2, 0, 'silence', '2 empty pizzas · 2 beats', True, 'r'), ('c', 'crotchet', 1, 1, 0, 'quarter note', '1 pizza · 1 beat', False, 'n'), ('c', 'crotchet rest', 1, 1, 0, 'silence', '1 empty pizza · 1 beat', True, 'r'), ('q', 'quaver', 2, 0, 1, 'eighth note', 'half a pizza · ½ beat', False, 'n'), ('q', 'quaver rest', 2, 0, 1, 'silence', 'half an empty pizza · ½ beat', True, 'r'), ('sq', 'semiquaver', 4, 0, 1, 'sixteenth note', 'a quarter of a pizza · ¼ beat', False, 'n'), ('sq', 'semiquaver rest', 4, 0, 1, 'silence', 'a quarter of an empty pizza · ¼ beat', True, 'r'))) + '</div>'
P37 = page(f'''{head('Part II · Time · 2', 'Notes and rests', 'You can see how long a note lasts from its shape: each plain note is <b>half</b> the one above it. And every note has a twin <b>rest</b>, a silence you count just as carefully.')}
{NTAB}
<div class="fn">* With the crotchet as one beat, as in 2/4, 3/4 and 4/4. <span class="ex">Extra</span>: beyond Level 8.</div>
<!--SPLIT-->
{PZBOX}
{two(h3('Head, stem, flag') + '<p>The <b>head</b> sits on a line or in a space. A <b>stem</b> goes up on the right of the head or down on the left. <b>Flags</b> on the stem halve the value each time; groups of quavers are joined by <b>beams</b> instead of flags.</p>',
     h3('Which rest is which?') + '<figure class="vx"><svg viewBox="0 0 300 90" style="width:100%;height:auto;display:block"><line x1="10" x2="290" y1="20" y2="20" stroke="#26296b" stroke-width="1.2"/><line x1="10" x2="290" y1="32" y2="32" stroke="#26296b" stroke-width="1.2"/><line x1="10" x2="290" y1="44" y2="44" stroke="#26296b" stroke-width="1.2"/><line x1="10" x2="290" y1="56" y2="56" stroke="#26296b" stroke-width="1.2"/><line x1="10" x2="290" y1="68" y2="68" stroke="#26296b" stroke-width="1.2"/><line x1="150" x2="150" y1="20" y2="68" stroke="#26296b" stroke-width="1.2"/><rect x="62" y="32" width="26" height="7" fill="#26296b"/><rect x="202" y="37" width="26" height="7" fill="#26296b"/> <text x="75" y="86" text-anchor="middle" font-family="AH" font-size="12" font-weight="700" fill="#e4572e">semibreve rest</text><text x="215" y="86" text-anchor="middle" font-family="AH" font-size="12" font-weight="700" fill="#e4572e">minim rest</text></svg></figure>' + '<p class="sm">The semibreve rest <b>hangs</b> below the fourth line; the minim rest <b>sits</b> on the middle line.</p>', '1fr 1fr')}
{inact('How long is each sound, and each silence?', vx('ia_rest', 62), ['<b>Name each shape:</b> minim, crotchet, crotchet rest.', '<b>Count its beats:</b> 2, 1 and 1.', '<b>Count the rests too:</b> the red rests last as long as their notes.'], 'Every bar adds up to <b>4 beats</b>, silences included.')}
{box('The semibreve rest’s special power', '<p>Most rests last a fixed number of beats. The <b>semibreve rest</b> can also mean <b>a whole bar of silence</b> in any time signature: 4 beats in 4/4, but 3 in 3/4 and 2 in 2/4. It is then centred in the bar. No other rest can do this.</p><p class="sm" style="margin:4px 0 0">One more rule: keep the middle of a 4/4 bar visible. Silence on beats 2–3 is two crotchet rests, never one minim rest.</p>' + two(vx('wbr34', 50), vx('wbr24', 50)))}
{foot('Pulse and the bar p. 36 · How long is a note? p. 38', 'Workbook Level 0 · Note values · Online: Library › Notes and rests')}''', 37).replace('<svg viewBox="0 0 300 90"', '<svg viewBox="0 0 300 90" class="rst"', 1)

def _tri(i, n, g):   # cell i of n: tint by which half of the bar, divider weight by how big a split it marks
    f = i / n; bg = '#f6f4f8' if n == 1 else '#fdeee8' if f < 0.5 else '#eef0f8'
    bl = 'none' if i == 0 else ('2px solid #26296b' if f == 0.5 else '1.4px solid #9a9cc4' if (f * 4) % 1 == 0 else '1px dashed #c9cbe0' if (f * 8) % 1 == 0 else '1px dotted #d9d4c6')
    return f'<div class="tri" style="background:{bg};border-left:{bl}">{g}</div>'
tree = ''.join(f'<div class="trw"><span class="trl">{lab}</span><div class="trc">' + ''.join(_tri(i, n, gcell("n", k, 36)) for i in range(n)) + '</div></div>' + f'<div class="trw trr2"><span class="trl">{rl}</span><div class="trc">' + ''.join(_tri(i, n, gcell("r", k, 30)) for i in range(n)) + '</div></div>' for lab, rl, k, n in (('1 semibreve', 'its rest', 'sb', 1), ('2 minims', 'their rests', 'm', 2), ('4 crotchets', 'their rests', 'c', 4), ('8 quavers', 'their rests', 'q', 8), ('16 semiquavers', 'their rests', 'sq', 16)))
DD = '<svg viewBox="0 0 14 10" style="width:11px;height:8px;margin-left:-11px;vertical-align:-1px;position:relative"><circle cx="3" cy="7" r="2" fill="#26296b"/><circle cx="10" cy="7" r="2" fill="#26296b"/></svg>'
DOTBOX = '<div class="pzbox"><b class="it">The dot, in pizzas</b><p class="sm" style="margin:2px 0 6px">The dot is a helper that adds <b>half of whatever its note is worth</b>. Dark slices: the note. Lighter: what the dot adds. Lightest: a second dot, half of the first dot.</p>' + ''.join(f'<div class="pzrow pzd"><span class="pzn">{gin("n", "m") + DD if nm.startswith("double") else gin("n", k)} {nm}</span><span class="pzs">{"".join((("<b class=pzp>+</b>" if j and col != pz[j - 1][2] else "") + (pzc(c, f, col) if not isinstance(col, list) else pzc(c, 0, None, cols=col))) for j, (c, f, col) in enumerate(pz))}</span><span class="pzsum">{sm}</span></div>' for k, nm, pz, sm in (
    ('dm', 'dotted minim', [(1, 1, '#e98a6c'), (1, 1, '#e98a6c'), (1, 1, '#f6c9b8')], '2 + <b>1</b> (half of 2) = <b>3 beats</b>'),
    ('dc', 'dotted crotchet', [(1, 1, '#e98a6c'), (2, 1, '#f6c9b8')], '1 + <b>½</b> (half of 1) = <b>1½ beats</b>'),
    ('dq', 'dotted quaver', [(2, 1, '#e98a6c'), (4, 1, '#f6c9b8')], '½ + <b>¼</b> (half of ½) = <b>¾ beat</b>'),
    ('dm', 'double-dotted minim', [(1, 1, '#e98a6c'), (1, 1, '#e98a6c'), (1, 1, '#f6c9b8'), (2, 1, '#fbe6dd')], '2 + <b>1</b> + <b>½</b> = <b>3½ beats</b>'))) + '</div>'
P38 = page(f'''{head('Part II · Time · 3', 'How long is a note?', 'Need a note longer than its shape allows? Two signs stretch it: the <b>dot</b>, which adds half, and the <b>tie</b>, which glues two notes into one sound.')}
{two(h3('The dot') + '<p>A dot adds <b>half the note’s value</b>: a dotted minim lasts 2 + 1 = 3 beats; a dotted crotchet 1 + ½ = 1½. A <b>double dot</b> adds half, then a quarter: a double-dotted minim lasts 2 + 1 + ½ = 3½.</p>' + vx('dot', 78),
     h3('The tie') + '<p>A curve joining two notes <b>of the same pitch</b> makes one longer sound: play the first, hold through the second. Ties can cross a bar line, where a dot cannot.</p>' + vx('tie', 78))}
{DOTBOX}
<!--SPLIT-->
{h3('Tie or slur?')}
{two(pvx('tieA', 78, '<b>Tie</b>: the same pitch. Play once and hold: G for 4 beats, then E for 4.'), pvx('slurA', 78, '<b>Slur</b>: different pitches. Play every note, smoothly joined (legato).'))}
{inact('Dot or tie: which is longer?', vx('ia_dot', 60), ['<b>The dotted minim:</b> 2 + half of 2 = 3 beats.', '<b>The tied notes:</b> a minim tied to a crotchet, 2 + 1 = 3 beats.', '<b>Play both:</b> one sound, held for three beats.'], 'They are <b>the same length</b>. A tie can also cross a bar line, which a dot cannot.')}
{inact('Count through a tie across the bar line', vx('hem', 60), ['<b>Bar 1:</b> minim on 1–2, crotchet on 3.', '<b>The tie</b> joins beat 3 to beat 1 of the next bar: one sound.', '<b>Keep counting:</b> 3, 1 held, then 2–3 on the minim.'], 'A tie can cross the bar line: <b>play once, count on</b>.')}
{inact('A dotted crotchet you already know: Ode to Joy', ODE, ['<b>Bars 3–4 of Beethoven’s Ode to Joy.</b> Sing it: “C C D E, E — D D”.', '<b>The red E is a dotted crotchet:</b> 1 + ½ = 1½ beats, held through “1 & 2”.', '<b>The quaver D</b> falls on the “&” of beat 2; the last D takes beats 3 and 4.'], 'Long–short, then long: the dot is why the tune <b>leans</b> before it lands.')}
{inact('Which is longer: a dotted minim or a minim tied to a quaver?', '<div style="display:flex;gap:18px;align-items:center;justify-content:center">' + ''.join(pzc(*p) for p in ((1, 1, '#e98a6c'), (1, 1, '#e98a6c'), (1, 1, '#f6c9b8'))) + '<span style="font-weight:700">vs</span>' + ''.join(pzc(*p) for p in ((1, 1, '#e98a6c'), (1, 1, '#e98a6c'), (2, 1, '#e98a6c'))) + '</div>', ['<b>Dotted minim:</b> 2 + 1 = 3 pizzas.', '<b>Minim tied to a quaver:</b> 2 + ½ = 2½ pizzas.', '<b>Compare:</b> 3 is half a beat more than 2½.'], 'The <b>dotted minim</b> is longer, by half a beat.')}
{inact('Tie or slur? Read the curves', pvx('tsmix', 80), ['<b>The first curve</b> joins two Gs: the same pitch, so a <b>tie</b>.', '<b>Play G once</b> and hold it for both minims: 4 beats.', '<b>The second curve</b> covers C B A G: different pitches, so a <b>slur</b>: play each, smoothly joined.'], 'Same pitch: <b>tie</b> (one sound). Different pitches: <b>slur</b> (legato).')}
{thinkt('A tie couples two carriages: the passenger stays seated across the join, even over a bar line. A dot cannot cross the bar line.')}
{foot('Time signatures p. 39 · Rhythm p. 41', 'Workbook Level 0 · Note values · Online: Library › Notes and rests')}''', 38)

bottom = [['2', gcell('n', 'm', 34), 'minim', 'Level 3'], ['4', gcell('n', 'c', 34), 'crotchet', 'Level 0'], ['8', gcell('n', 'q', 34), 'quaver', 'Level 1'], ['16', gcell('n', 'sq', 34), 'semiquaver', lv('')]]
simple = [[ts(2, 4), '2 crotchets', 'Level 0'], [ts(3, 4), '3 crotchets', 'Level 0'], [f'<span class="tsrow">{ts(4, 4)}{gsym("𝄴", 26)}</span>', '4 crotchets (the C sign: common time)', 'Level 0'], [f'<span class="tsrow">{ts(2, 2)}{gsym("𝄵", 30)}</span>', '2 minims (the cut C: cut common time)', 'Level 3'], [ts(3, 2), '3 minims', 'Level 3'], [ts(4, 2), '4 minims', lv('')], [ts(3, 8), '3 quavers', 'Level 3']]
TRAIN = '<div class="pzbox"><b class="it">Think of a train</b><p class="sm" style="margin:2px 0 6px">In 3/4 every carriage (bar) has exactly <b>3 seats</b>; each seat is one crotchet beat. Notes book seats: a minim takes 2, a crotchet 1. A rest books a seat and leaves it <b>empty</b> (shaded). Every seat in every carriage must be booked.</p>' + train([[('n', 2, 'm'), ('n', 1, 'c')], [('n', 1, 'c'), ('r', 1, 'c'), ('n', 1, 'c')], [('n', 3, 'dm')]], '3/4') + '<p class="sm" style="margin:6px 0 0;text-align:center">minim + crotchet · crotchet, crotchet rest, crotchet · dotted minim: 3 seats each</p></div>'
P39 = page(f'''{head('Part II · Time · 4', 'Time signatures', 'Two numbers, like a train ticket: the <b>top number</b> says how many seats (counts) each bar has; the <b>bottom number</b> says which note fills one seat.')}
{h3('The bottom number') + tbl(['Bottom', 'Note', 'One count is a', 'First met'], bottom, ['18%', '16%', '36%', '30%'])}
{TRAIN}
<!--SPLIT-->
{h3('Simple time: each beat divides in two')}
{tbl(['Time signature', 'Each bar holds', 'First met'], simple, ['26%', '50%', '24%'])}
{h3('Changing time signature')}
<p>A new time signature can appear in the middle of a piece, right after a bar line; it holds until the next one. A time signature is written only once, not on every line.</p>
{watch(['Reading 6/8 as six beats: at most speeds it moves in two.', 'Mixing up 3/4 and 6/8: both hold six quavers, grouped differently (p. 40).'])}
{inact('Read a time signature', vx('ia_ts', 74), ['<b>Top number 3:</b> three counts in each bar.', '<b>Bottom number 4:</b> a crotchet is one count.', '<b>Check a bar:</b> two quavers + crotchet + crotchet = 3.'], '3/4: <b>three crotchet beats</b> in every bar.')}
{youknow('Minuet in G (from the Notebook for Anna Magdalena Bach)', ykfig('yk_min3', ('n1','n6'), 70), 'Every bar holds <b class="co">three crotchet beats</b>: 1 2 3, 1 2 3, the step of the dance. That is 3/4.', 'Count 1 2 3 aloud while someone plays it.')}
{inact('Which time signature fits?', vx('ia_which', 74), ['<b>Find the strong beats</b> by clapping, accenting the first note of each bar.', '<b>Count each bar:</b> two crotchets, or one minim: 2 beats.', '<b>Each beat is a crotchet.</b>'], 'It is in <b>2/4</b>: two crotchet beats a bar.')}
{foot('Pulse and the bar p. 36 · Compound time p. 40', 'Workbook Level 0 · Time signatures · Online: Library › Time signatures')}''', 39)

compound = [[ts(6, 8), '2 dotted crotchets', 'Level 1'], [ts(9, 8), '3 dotted crotchets', 'Level 3'], [ts(12, 8), '4 dotted crotchets', 'Level 3'], [ts(6, 4), '2 dotted minims', 'Level 4']]
irreg = [[ts(5, 4), '5 crotchets: 3 + 2 or 2 + 3', 'Level 5'], [ts(7, 4), '7 crotchets: 4 + 3 or 3 + 4', lv('')], [ts(5, 8), '5 quavers: 3 + 2 or 2 + 3', lv('')], [ts(7, 8), '7 quavers: 2 + 2 + 3 or 3 + 2 + 2', lv('')]]
P40 = page(f'''{head('Part II · Time · 5', 'Compound and irregular time', 'Compound time skips: each dotted beat splits into <b>three</b>. Irregular time keeps you guessing, with <b>five or seven</b> counts in uneven groups. (9/4, 12/4 and /16 signatures are rare.)')}
{h3('3/4 or 6/8?')}
{two(vx('t34q', 56, '3/4: six quavers in three twos'), vx('t68q', 56, '6/8: six quavers in two threes'))}
{box('Simple or compound?', '<p>In <b>simple time</b> each beat divides into <b>two</b>. In <b>compound time</b> each beat is a dotted note and divides into <b>three</b>.</p><p><b>Quick test:</b> a top number of 6, 9 or 12 means compound. Divide it by 3 to find the beats: 6/8 has 2, 9/8 has 3, 12/8 has 4.</p>')}
{h3('Compound time')}
{tbl(['Time signature', 'Each bar holds', 'First met'], compound, ['26%', '50%', '24%'])}
{h3('Counting 6/8')}
{vx('t68', 58, 'Slowly, count all six quavers. At speed, feel two beats, on 1 and 4: “1 & a, 2 & a”.')}
{thinkt('Like a skipping rope: two big swings, each with three little steps inside.')}
<!--SPLIT-->
{h3('Irregular time')}
{tbl(['Time signature', 'Each bar holds', 'First met'], irreg, ['26%', '50%', '24%'])}
{two(box('Uneven groups in 4/4', '<p>Many dances keep 4/4 but group the eight quavers 3 + 3 + 2: “1 2 3, 1 2 3, 1 2”.</p>'), vx('t332', 54), '1fr 1fr')}
{inact('Count 6/8 in two', vx('ia_68', 74), ['<b>Slowly, count all six:</b> 1 2 3 4 5 6.', '<b>Lean on 1 and 4</b>, the red notes.', '<b>Faster, count only those:</b> two beats, each a dotted crotchet.'], '6/8 has <b>two beats</b> in a bar, each split into three.')}
{youknow('Row, Row, Row Your Boat', ykfig('yk_row', ('n1','n2'), 70), 'Two big beats in every bar, each a <b class="co">dotted crotchet</b>: “Row, row”. Inside each beat, “gent-ly” splits it into three. That is 6/8.', 'Sway twice per bar while you sing it.')}
{inact('Hear 3 + 3 + 2 inside 4/4', vx('t332', 74), ['<b>Count eight quavers</b> in a bar of 4/4.', '<b>Group them</b> 3 + 3 + 2, accenting 1, 4 and 7.', '<b>Keep the beat</b> in your foot: it stays in four.'], 'The bar is still <b>4/4</b>; only the accents are uneven.')}
{foot('Time signatures p. 39 · Rhythm: groups and upbeats p. 41', 'Workbook Levels 1–4 · Compound time · Online: Rhythm clock')}''', 40)

P41 = page(f'''{head('Part II · Time · 6', 'Rhythm: groups and upbeats', 'Say your own name: long and short sounds, that’s <b>rhythm</b>. The pulse marches steadily on; the rhythm dances around it. How the notes are grouped on the page shows where the beats fall.')}
{h3('Grouping with beams')}
<p>Beams join the notes of <b>one beat</b>, so the beats stay visible. In 4/4 a beam may cover beats 1–2 or 3–4, but never cross the middle of the bar (except in a deliberate grouping such as 3 + 3 + 2). In compound time, quavers are beamed in threes.</p>
{two(vx('beamgood', 78, '✓ The middle of the bar can be seen.'), vx('beambad', 78, '✗ A beam across beats 2–3 hides it.'))}
{h3('The upbeat (anacrusis)')}
{two('<p>A piece can begin <b>before</b> the first full bar, with one or more notes called an upbeat or anacrusis. The last bar is then short by the same amount, so the two together make one full bar. Count the missing beats in silence before you start.</p>', vx('anac', 78, 'Count “1 2” silently, then play on 3.'))}
{inact('Balance the upbeat', vx('ia_anac', 74), ['<b>The upbeat:</b> one beat (count 3) before the first full bar.', '<b>The last bar:</b> only two beats.', '<b>Add them:</b> 1 + 2 = 3, one whole bar of 3/4.'], 'The upbeat and the last bar <b>make one full bar</b> together.')}
{thinkt('An upbeat is the breath before you speak: “and-ONE”. You lift on the upbeat so the strong beat can land.')}
<!--SPLIT-->
{h3('Triplets and duplets')}
{two(vx('trip', 80, 'Triplet: three exactly equal notes in the time of two. First met: Level 2.'), vx('dup', 80, 'Duplet: two notes in the time of three, in compound time. First met: Level 2.'))}
<div class="pzg">{''.join(f'<div>{pizza(n, n, 18)}{vx(k, 54)}<span>{t}</span></div>' for n, k, t in ((2, 'pz_q', '<b>Two quavers</b>: one beat cut in 2'), (3, 'pz_t', 'A <b class="co">triplet</b>: one beat cut in 3'), (4, 'pz_s', '<b>Four semiquavers</b>: one beat cut in 4')))}</div>
{h3('Counting smaller values')}
{vx('small', 100, 'Crotchet, two quavers, four semiquavers and a triplet (“1 & a”): one beat each.')}

{youknow('Happy Birthday', ykfig('yk_bday', ('n1','n2'), 70), '“Hap-py” comes <b class="co">before</b> the first strong beat: an upbeat. The strong beat lands on “birth”.', 'Sing it and clap only on “birth”, “day” and “you”: you feel where bar 1 starts.')}
{inact('Fit a triplet into a bar', vx('ia_trip2', 72), ['<b>Count the bar:</b> four crotchet beats, “1 2 3 4”.', '<b>Find the 3:</b> on beat 2, three quavers share one beat.', '<b>Say it:</b> “1, 2 & a, 3, 4”, keeping beats 3 and 4 steady.'], 'The triplet squeezes three notes into <b>beat 2</b>; the beat itself never moves.')}
{foot('Notes and rests p. 37 · Rhythm: off the beat p. 42', 'Workbook Levels ½–4 · Rhythm · Online: Rhythm clock')}''', 41)

terms = [['syncopation', 'the stress falls off the beat, often on a note held across it', 'Level 4'], ['hemiola', 'two bars of three felt as three bars of two', 'Level 4'], ['swing', 'pairs of quavers played long–short, like the first and last notes of a triplet', 'Level ½'], ['polyrhythm', 'two rhythms at once, such as three notes in one hand against two in the other', 'Level 7'], ['rubato', 'time stretched and given back, for expression; the pulse returns', lv('')]]
P42 = page(f'''{head('Part II · Time · 7', 'Rhythm: off the beat', 'Now the fun part: rhythm that teases the beat. It only works if the beat underneath stays rock-steady.')}
{two(h3('Syncopation') + vx('sync', 70, 'The crotchet starts on “&” and is held through beat 2.') + '<p class="sm">Level 4. Feel beat 2 even though nothing is played on it.</p>',
     h3('Hemiola') + vx('hemi', 70, 'Two bars of 3/4 felt as three minims.') + '<p class="sm">Level 4. Common at cadences in Baroque dances.</p>')}
<!--SPLIT-->
{h3('Swing <span class="lvl2">Level ½</span>')}
<p>Common from the first pieces: jazz, blues and many easy modern pieces are marked <i>swing</i>. Pairs of quavers are written evenly but played <b>long–short</b>, like the first and last notes of a triplet.</p>
{two(vx('swingw', 66, 'Written'), vx('swingp', 66, 'Played'))}
{two(h3('Polyrhythm <span class="lvl2">Level 7</span>') + vx('poly', 80, 'Three against two: a crotchet triplet above, two crotchets below, starting together.'),
     h3('Rubato <span class="lvl2">Extra</span>') + '<p>Time is stretched and then given back, for expression: the music leans into a phrase and catches up after it. The pulse always returns. Marked <i>rubato</i>, or simply part of the style in much Romantic music.</p>')}
{watch(['Rushing the short notes after a long one: keep counting inside the long note.', 'Playing a triplet unevenly: three equal notes, not two quick and one long.', 'Letting syncopation drag the pulse: tap the beat with your foot.'])}
{inact('Count a syncopation', vx('ia_sync', 74), ['<b>Tap the beats:</b> 1, 2.', '<b>Find the red crotchet:</b> it starts on the “&”, between the beats.', '<b>Hold it through beat 2</b>, then play bar 2 on the beats.'], 'The accent falls <b>off the beat</b>: that is syncopation.')}
{youknow('The Entertainer (Scott Joplin)', ykfig('yk_ent', ('n4','n6'), 70), 'The high <b class="co">C</b> keeps landing just after the beat, not on it: syncopation, the bounce of ragtime.', 'Tap the beat with your foot and hum the tune: hear the C slip between the taps.')}
{inact('Swing this bar', '<div><p class="mmk">Swing</p>' + vx('ia_swing', 72) + '</div>', ['<b>Find the quaver pairs:</b> beats 2 and 3.', '<b>Play each pair long–short:</b> “doo-ba, doo-ba”.', '<b>Leave the crotchets alone:</b> beats 1 and 4 stay as written.'], 'Only the <b>pairs</b> swing; the beat underneath stays even.')}
{inact('Count a hemiola', vx('hem', 74), ['<b>Two bars of 3/4:</b> six crotchet beats.', '<b>Regroup them</b> in twos: 1 2 | 3 4 | 5 6.', '<b>Feel three big beats</b> across the two bars.'], 'Two bars of three become <b>three bars of two</b> for a moment: a hemiola.')}
{thinkt('Syncopation is a skip in your walk: a step that lands between the beats. Swing is walking with a spring in your step, long-short, long-short. Rubato is borrowing time like pocket money: whatever you spend, you pay back.')}
{foot('Rhythm: groups and upbeats p. 41 · Words for how to play: Expression (later)', 'Workbook Levels ½–4 · Rhythm · Online: Rhythm clock')}''', 42)

css = f'''
@page {{ size: A4; margin: 0 }} *{{box-sizing:border-box}} body{{margin:0;background:#e9e4d8;font-family:'AH',Arial,sans-serif;color:{N}}}
.pg{{width:794px;height:1123px;background:#fff;margin:0 auto 24px;position:relative;overflow:hidden;padding:42px 58px 0;page-break-after:always}}
.top{{display:flex;justify-content:space-between;font-size:9.5px;font-weight:700;letter-spacing:.16em;color:#8a8cb0}} .rule{{height:5px;border-top:1.5px solid {N};border-bottom:.6px solid {N};margin:7px 0 18px}}
.foot{{position:absolute;left:0;right:0;bottom:30px;text-align:center}} .foot span{{display:inline-block;color:{N};font:700 13px 'AH',Arial;letter-spacing:.08em}}
.kick{{font-size:11.5px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{C}}} h1{{font-family:'PF',Georgia,serif;font-size:35px;line-height:1.1;margin:3px 0 8px;font-weight:700}}
.lead{{font-size:16.5px;line-height:1.5;margin:0 0 10px}} p{{font-size:15px;line-height:1.5;margin:4px 0 8px}} p.sm{{font-size:13.5px;color:{MUTE};margin:2px 0 4px}}
h3{{font-size:17px;font-weight:700;margin:12px 0 6px;padding-top:7px;border-top:1.5px solid {N}}}
.two{{display:grid;gap:22px;align-items:start}} .two h3:first-child{{margin-top:6px}}
.ht{{width:100%;border-collapse:collapse;table-layout:fixed;font-size:14.5px}} .ht th{{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#8a8cb0;text-align:left;padding:4px 8px;border-bottom:1.5px solid {N}}}
.ht td{{border-bottom:.6px solid #e2ddd0;padding:3px 8px;vertical-align:middle;line-height:1.35}} .nt td{{padding:3px 8px;vertical-align:middle}} .nt td.g{{text-align:center}} .mu{{color:{MUTE};font-size:13.5px}}
.ex{{color:#9a9cc4;font-style:italic}} .tsrow{{display:inline-flex;align-items:center;gap:10px}} .tsrow svg{{margin:0 !important}} .lvl2{{font-size:12px;font-weight:700;color:{MUTE};margin-left:8px;letter-spacing:.04em}} .fn{{font-size:12.5px;color:{MUTE};margin-top:6px}}
.gl2{{font-family:'NM';line-height:1;color:{N};display:inline-block;vertical-align:middle}} .mm{{white-space:nowrap;font-weight:700}}
.ts{{display:inline-flex;flex-direction:column;align-items:center;line-height:.8;font-family:'PF',Georgia,serif;font-size:17px;vertical-align:middle;margin-right:6px}}
.box{{border-left:3px solid {C};padding:6px 0 4px 14px;margin:10px 0}} .bh{{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin-bottom:2px}}
.rst{{max-height:78px}} .remem{{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 16px;border-top:1px dashed #c9cbe0;border-bottom:1px dashed #c9cbe0;padding:5px 2px;margin:5px 0 4px;font-size:13px;color:#3d4080}} .remem .rl{{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}} .remem .ri i{{font-style:normal;color:{MUTE};font-size:12px}} .lis{{margin:10px 0;border:1.5px solid #e3e1ee;border-radius:8px;padding:9px 12px}} .lish{{margin:0 0 6px;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}} .lisg{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}} .lisg div{{font-size:12.5px;line-height:1.4}} .lisg b{{display:block;color:#26296b}} .lisg span{{display:block;color:#6d6f9c;font-size:11.5px}} .lisg i{{display:block;font-style:normal;margin-top:3px}} .mmk{{margin:0 0 2px;font-weight:700;font-size:14px;color:#26296b}} .pzbox{{border:1.5px solid #e3e1ee;border-radius:8px;padding:8px 14px;margin:6px 0}} .pzrow{{display:grid;grid-template-columns:1.2fr 1.4fr 1fr 1.6fr;align-items:center;gap:10px;font-size:13.5px;padding:0;border-bottom:.6px solid #eeece4}} .pzn{{display:flex;align-items:center;gap:6px;font-weight:700}} .pzs{{display:flex;gap:6px}} .pzb{{color:#6d6f9c}} .pzg{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:8px 0 6px;border:1.5px solid #e3e1ee;border-radius:8px;padding:10px}} .pzg>div{{display:flex;flex-direction:column;align-items:center;gap:2px;font-size:13px;text-align:center}} .pzg .vx{{border:0;margin:0;padding:0}} .pzd{{grid-template-columns:1.5fr 1.6fr 1.7fr}} .pzd .pzn{{white-space:nowrap}} .pzsum{{font-size:13.5px}} .pzrr{{border-bottom:1.2px solid #d9d4c6}} .pzrr .pzn{{font-weight:400;color:#4a4d86}} .pzp{{font-size:18px;color:#26296b;margin:0 2px}} .pzs{{align-items:center}} .pzline{{display:flex;align-items:center;gap:8px;font-size:13.5px;margin:8px 0 4px;flex-wrap:wrap}} .pzline span{{margin-right:12px}} .co{{color:{C}}} .drill{{display:flex;gap:10px;align-items:baseline;font-size:13.5px;margin:8px 0;padding:8px 10px;background:#fdf6f2;color:#3d4080}} .drill em{{font-style:normal}} .drill span{{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}} .yk{{border-top:3px solid {N};background:#f6f6fb;padding:8px 12px 10px;margin:10px 0}} .yk .bh{{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{N}}} .yk .it{{font-size:15px;display:block;margin:1px 0 4px}} .ykg{{display:grid;grid-template-columns:1.25fr 1fr;gap:14px;align-items:center}} .ykg .vx{{border:0;background:none;margin:0;padding:0}} .ykg p{{margin:0;font-size:14px;line-height:1.5}} .realm{{border-top:3px solid {N};background:#f6f6fb;padding:8px 12px 10px;margin:10px 0}} .realm .bh{{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{N}}} .realm .it{{font-size:15px;display:block;margin:1px 0 6px}} .rmg{{display:grid;grid-template-columns:1fr 1fr;gap:6px 18px}} .rmg>div{{display:flex;flex-direction:column;font-size:13px;line-height:1.4;border-left:2px solid {C};padding-left:8px}} .rmg i{{font-style:normal;font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:{MUTE}}} .tryit{{font-size:13.5px;margin:8px 0 0}} .inact2{{border:1.5px solid {C};border-radius:4px;padding:8px 12px 10px;margin:10px 0;background:#fff}} .inact2 .bh{{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}} .inact2 .it{{font-size:15px;display:block;margin:1px 0 4px}} .ia2{{display:grid;grid-template-columns:1fr 1.1fr;gap:14px;align-items:center}} .ia2 .vx{{border:0;margin:0;padding:2px 0}} .ia2 ol{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:5px;font-size:13px;line-height:1.4}} .ia2 li{{display:flex;gap:8px}} .in{{flex:none;width:20px;height:20px;border-radius:50%;background:{C};color:#fff;font-weight:700;font-size:11.5px;display:flex;align-items:center;justify-content:center}} .ires{{margin-top:6px;padding-top:6px;border-top:1px solid #f0d8cf;font-size:14px}} .think{{display:flex;gap:10px;align-items:baseline;font-size:13.5px;margin:6px 0;color:#3d4080}} .think span{{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{G}}} .watch{{border-top:1px solid #c9cbe0;border-bottom:1px solid #c9cbe0;padding:6px 2px;margin:10px 0}} .wr{{display:flex;gap:10px;font-size:14.5px;line-height:1.45;padding:2px 0}} .x{{color:{C};font-weight:700}}
.links{{position:absolute;left:58px;right:58px;bottom:62px;display:grid;grid-template-columns:1fr 1fr;gap:22px;font-size:12.5px;line-height:1.45;color:#3d4080;border-top:1px solid #e2ddd0;padding-top:8px}} .lab{{display:block;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}}
.vx{{margin:6px 0;border:1px solid #e2ddd0;background:#fff;padding:8px 12px 6px}} .vs{{display:flex;justify-content:center}} .vs svg{{width:100%;height:auto;color:{N};fill:{N}}}
.vx text{{font-family:'AH',Arial !important;font-weight:700}} figcaption{{font-size:13px;color:{MUTE};margin-top:4px;line-height:1.4}}
.tree{{border:1px solid #e2ddd0;background:#fff;padding:8px 14px}} .trw{{display:flex;align-items:stretch;gap:12px;border-bottom:.6px solid #eee8da;padding:0}} .trw .trl{{align-self:center}} .trc{{display:flex;flex:1}} .trc .tri{{display:flex;align-items:center;justify-content:center;padding:3px 0}} .trw:last-child{{border:0}} .trl{{flex:none;width:130px;font-size:14px;font-weight:700}} .trr2{{border-bottom:1.2px solid #d9d4c6;padding-top:0}} .trr2 .trl{{font-weight:400;color:#6d6f9c;font-size:12.5px}} .trc{{flex:1;display:flex}} .tri{{flex:1;text-align:center;border-left:1px dashed #e2ddd0}} .tri:first-child{{border-left:0}}
.part2{{background:{DK};padding:34px}} .pframe{{position:absolute;inset:34px;border:1.5px solid rgba(255,253,247,.7);outline:.6px solid rgba(255,253,247,.45);outline-offset:-8px;color:{CR};padding:120px 64px 40px}}
.pk{{font-size:12px;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:#f4a9bb}} .pt{{font-family:'PF',Georgia,serif;font-size:80px;line-height:1;margin-top:10px}} .pdv{{width:90px;height:5px;border-top:1px solid {CR};border-bottom:1px solid {CR};margin:24px 0;opacity:.7}}
.pl{{font-size:17px;line-height:1.65;max-width:580px;opacity:.95}} .flow{{display:flex;align-items:stretch;gap:4px;margin:34px 0 30px}} .fl{{flex:1;border:1px solid rgba(255,253,247,.45);padding:10px 8px;text-align:center}} .fln{{display:block;font-weight:700;color:#f4a9bb}} .fl b{{display:block;font-size:15px;margin:2px 0}} .fl span:last-child{{display:block;font-size:11.5px;opacity:.8;line-height:1.35}} .fa{{align-self:center;color:#f4a9bb;font-size:18px}}
.pin{{position:absolute;right:64px;bottom:60px;width:380px}} .pih{{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;opacity:.75;margin-bottom:4px}} .tr{{display:flex;align-items:baseline;gap:6px;font-size:15px;padding:3px 0}} .dots{{flex:1;border-bottom:1px dotted rgba(255,253,247,.45);transform:translateY(-4px)}}
'''
html = ''   # (generators read the css above up to this line)
import re as _re
TBASE = 34   # Part II starts here (her 5 Nov, four parts: Pitch 22-32, Time opener 33)
_secs, _map, _n = [], {}, TBASE
for _old, _pg in zip(range(36, 43), (P36, P37, P38, P39, P40, P41, P42)):
    _map[_old] = _n
    if '<!--SPLIT-->' in _pg:
        _a, _b = _pg.split('<!--SPLIT-->', 1)
        _kick = _re.search(r'<div class="kick">(.*?)</div>', _a).group(1)
        _head_end = _a.index('<div class="body">') + len('<div class="body">')
        _foot = _pg[_pg.rindex('<div class="foot">'):]
        _secs.append((_a + '</div>' + _foot).replace('<section class="pg"', f'<section class="pg" data-flow="A{_old}"', 1))
        _secs.append((_a[:_head_end] + f'<div class="kick fk2">{_kick} · continued</div>' + _b).replace('<section class="pg"', f'<section class="pg" data-flow="B{_old}"', 1))
        _n += 2
    else:
        _secs.append(_pg); _n += 1
_secs = [_re.sub(r'<div class="foot"><span>\d+</span></div>', f'<div class="foot"><span>{TBASE + i}</span></div>', x) for i, x in enumerate(_secs)]
_body = ''.join(_secs)
_body = _re.sub(r'(p\.[ \u00a0]|page )(3[6-9]|4[0-2])\b', lambda m: m.group(1) + str(_map[int(m.group(2))]), _body)
# ---------- Part II ends with its own tips page (her 4 Nov: each part ends with its tips) ----------
css += """
.tip{border-left:3px solid #e4572e;background:#fdf6f2;padding:10px 16px 12px;margin:12px 0} .tip .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .tip .tt{display:block;font-size:16px;margin:2px 0 6px} .tip table{background:transparent} .tip td,.tip th{vertical-align:top}
.fixes{display:grid;grid-template-columns:1fr 1fr;gap:8px 14px;margin:6px 0 10px} .fixes>div{position:relative;padding:10px 12px 10px 44px;border:1px solid #e2ddd0;display:flex;flex-direction:column;gap:2px;font-size:13.5px;line-height:1.45} .fixes b{font-size:14.5px} .fixes .rn{position:absolute;left:12px;top:12px;width:22px;height:22px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;font-size:12.5px;display:flex;align-items:center;justify-content:center}
"""
TT = page(f"""{head('Part II · Time · Tips', 'When the rhythm slips', 'A rhythm that slips is nearly always a beat that was not counted. Find which beat, count it out loud, and the rest of the bar usually falls into place.')}
<div class="tip"><div class="bh">Tip</div><b class="tt">What you notice, what to check</b>
{tbl(['What you notice', 'Check', 'Turn to'], [['It speeds up or slows down', '<b class="co">the pulse</b>: count one bar aloud before you start', 'p. 34'], ['A rest gets skipped', '<b class="co">the rest</b>: it is counted just like a note', 'p. 36'], ['Long notes come out short', '<b class="co">the hold</b>: count every beat of a minim, dot or tie', 'p. 38'], ['The bar feels too long or too short', '<b class="co">the time signature</b>: how many counts, which note is one', 'p. 40'], ['6/8 sounds like 3/4', '<b class="co">the dotted beat</b>: two beats, each split in three', 'p. 42'], ['You lose your place in fast notes', '<b class="co">the beams</b>: each group is one beat', 'p. 44'], ['An off-beat note lands on the beat', '<b class="co">the “&”</b>: keep the beat in your foot and count it', 'p. 46']], ['38%', '50%', '12%'])}
</div>
{inact('Count the long notes', train([[('n', 2, 'm'), ('n', 1, 'c')], [('n', 3, 'dm')]], '3/4'), ['<b>Say 1 2 3</b> once through before you play, to feel the beat.', '<b>The minim books seats 1 and 2:</b> keep saying “2” while it sounds.', '<b>The dotted minim books all three:</b> let go on the next “1”, not before.'], 'Long notes are where counting slips: <b>say every seat</b> they book.')}
{h3('Four ways to steady a rhythm')}
<div class="fixes">{''.join(f'<div><span class="rn">{i + 1}</span><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate([('Count out loud', 'Say the counts while you play, not in your head: a slip you can hear is a slip you can fix.'), ('Tap, then play', 'Tap the rhythm on the lid and say the counts; play only when the tapping is steady.'), ('Walk the beat', 'Step the pulse while you clap the rhythm, so the beat lives in your feet.'), ('Split the beat', 'For dots and quavers, count “1 & 2 &”: the extra “&” shows exactly where each note goes.')]))}</div>
{thinkt('Like a dance partner: the beat leads and the rhythm follows. Lose the beat and every step after it goes wrong.')}""", 48)

_body += TT
TIME_MAP = _map
FLOWJS = '''<script>
// Each topic fills its first page, then flows on to its second: blocks move between the two until the first is as full as it can be.
(async function () { try { await document.fonts.ready; } catch (e) {}
  document.querySelectorAll('section[data-flow^="A"]').forEach(A => {
    const B = document.querySelector('section[data-flow="B' + A.dataset.flow.slice(1) + '"]'); if (!B) return;
    const ab = A.querySelector('.body'), bb = B.querySelector('.body'), kick = bb.querySelector('.fk2');
    const limit = () => A.querySelector('.foot').getBoundingClientRect().top - 24;
    const bottom = () => { let m = 0; [...ab.children].forEach(c => { const r = c.getBoundingClientRect(); if (r.height) m = Math.max(m, r.bottom); }); return m; };
    while (bottom() > limit() && ab.children.length > 3) bb.insertBefore(ab.lastElementChild, kick.nextSibling);
    let failCat = null; for (const nx of [...bb.children]) { if (failCat !== null && +(nx.dataset.cat || 0) !== failCat) break; if (nx === kick || nx.classList.contains('links') || nx.parentNode !== bb) continue; const grp = [nx]; if (/^H[234]$/.test(nx.tagName) && nx.nextElementSibling && !nx.nextElementSibling.classList.contains('links')) grp.push(nx.nextElementSibling); const ref = grp[grp.length - 1].nextSibling; grp.forEach(e => ab.appendChild(e)); if (bottom() > limit()) { grp.forEach(e => bb.insertBefore(e, ref)); if (grp.length > 1) break; failCat = +(grp[0].dataset.cat || 0); } }   // her 5 Nov: a block may only jump ahead of one of its own kind (content, In action, You know this, Think of it, Watch out keep their order)   // nothing jumps ahead of a heading that stays behind   // fill the first page: try each block in turn (a small one may fit where a big one did not); a heading only moves together with the block under it
    while (ab.lastElementChild && /^H[234]$/.test(ab.lastElementChild.tagName)) bb.insertBefore(ab.lastElementChild, kick.nextSibling);   // a heading never sits alone at the foot of a page: it goes over with its text
  });
  document.body.dataset.flowed = '1';
})();
</script>'''
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{OPEN}{_body}{FLOWJS}</body></html>'

open('/mnt/user-data/outputs/house-rooms/handbook-time2.html', 'w').write(html)
print('ok')
