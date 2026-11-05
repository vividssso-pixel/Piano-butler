# Mock-up (her 5 Nov: 'show me a draft'): a picture-first spread for Seventh chords, before it goes into the book
exec(open('/tmp/claude-0/pk/harmony.py').read().split("\n_secs = []")[0])
N, R, PINK, SOFT = '#26296b', '#e4572e', '#fde6dd', '#f6f5fa'

def building(notes, labels, top_new=1, w=150, h=46):
    n = len(notes); H = n * h + 70
    o = f'<svg viewBox="0 0 {w + 150} {H}" style="width:100%;max-width:{w + 150}px;height:auto;display:block;margin:0 auto">'
    o += f'<path d="M6,{H - n * h - 30} L{w / 2 + 6},{H - n * h - 62} L{w + 6},{H - n * h - 30}" fill="none" stroke="{N}" stroke-width="2.5"/>'
    for i, (nt, lb) in enumerate(zip(notes, labels)):
        y = H - 30 - (i + 1) * h; new = i >= n - top_new
        o += f'<rect x="10" y="{y}" width="{w - 8}" height="{h - 4}" rx="4" fill="{"#fbd2c2" if new else PINK}" stroke="{R if new else N}" stroke-width="{2.5 if new else 2}"/>'
        o += f'<text x="30" y="{y + 22}" font-family="AH,Arial" font-size="19" font-weight="700" fill="{R if i == 0 or new else N}">{nt}</text><text x="62" y="{y + 21}" font-family="AH,Arial" font-size="13" fill="{N}">{lb}</text>'
    yb = H - 30 - (n - top_new) * h + 2
    o += f'<path d="M{w + 12},{H - 32} L{w + 20},{H - 32} L{w + 20},{yb} L{w + 12},{yb}" fill="none" stroke="{N}" stroke-width="2"/><text x="{w + 28}" y="{(H - 32 + yb) / 2 + 5}" font-family="AH,Arial" font-size="13" font-weight="700" fill="{N}">triad</text>'
    o += f'<path d="M{w + 12},{yb - 4} L{w + 20},{yb - 4} L{w + 20},{yb - h + 6} L{w + 12},{yb - h + 6}" fill="none" stroke="{R}" stroke-width="2"/><text x="{w + 28}" y="{yb - h / 2 + 3}" font-family="AH,Arial" font-size="13" font-weight="700" fill="{R}">+ one floor</text>'
    o += f'<line x1="0" x2="{w + 20}" y1="{H - 28}" y2="{H - 28}" stroke="{N}" stroke-width="3"/><text x="0" y="{H - 8}" font-family="AH,Arial" font-size="11" font-weight="700" letter-spacing="2" fill="#6d6f9c">THE SCALE</text>'
    return o + '</svg>'

def minikb(keys, nums, W=22, H=90):   # 8 white keys from C; keys = list of (pos, name) where pos counts semitones from C; nums = keys-between labels
    wpos = [0, 2, 4, 5, 7, 9, 11, 12, 14]
    o = f'<svg viewBox="-2 -16 {8 * W + 4} {H + 20}" style="width:100%;max-width:{8 * W + 4}px;height:auto;display:block;margin:0 auto">'
    for i in range(8): o += f'<rect x="{i * W}" y="0" width="{W}" height="{H}" fill="#fff" stroke="{N}" stroke-width="1.2"/>'
    for i in (0, 1, 3, 4, 5):
        o += f'<rect x="{(i + 1) * W - W * 0.3}" y="0" width="{W * 0.6}" height="{H * 0.6}" fill="{N}"/>'
    for p, nm in keys:
        if p in wpos: x, y = wpos.index(p) * W + W / 2, H - 13
        else: x, y = (wpos.index(p - 1) + 1) * W, H * 0.6 - 10
        o += f'<circle cx="{x}" cy="{y}" r="7.5" fill="{R}"/>'
    o += f'<text x="{4 * W}" y="-4" text-anchor="middle" font-family="AH,Arial" font-size="{max(13, W * 0.62):.0f}" font-weight="700" fill="{R}">{nums}</text>'
    return o + '</svg>'

KINDS7 = [('Cmaj7', 'C E G B', [(0, 'C'), (4, 'E'), (7, 'G'), (11, 'B')], '3 + 2 + 3', 'dreamy', 'film music, bossa nova'),
          ('C7', 'C E G B♭', [(0, 'C'), (4, 'E'), (7, 'G'), (10, 'B♭')], '3 + 2 + 2', 'bluesy', 'the blues; wants to move'),
          ('Cm7', 'C E♭ G B♭', [(0, 'C'), (3, 'E♭'), (7, 'G'), (10, 'B♭')], '2 + 3 + 2', 'mellow', 'soul, jazz ballads'),
          ('Cø7', 'C E♭ G♭ B♭', [(0, 'C'), (3, 'E♭'), (6, 'G♭'), (10, 'B♭')], '2 + 2 + 3', 'searching', 'ii in a minor key'),
          ('C°7', 'C E♭ G♭ B𝄫', [(0, 'C'), (3, 'E♭'), (6, 'G♭'), (9, 'B𝄫')], '2 + 2 + 2', 'spooky', 'the villain in old films')]
CARDS = '<div class="k7">' + ''.join(f'<div class="kc"><b class="ks">{s}</b>{minikb(k, f)}<span class="kn">{n}</span><span class="km">{m}</span><span class="kw">{w}</span></div>' for s, n, k, f, m, w in KINDS7) + '</div>'

P1 = hpage(f"""{head('Part III · Harmony · 5', 'Seventh chords', 'Add one more floor to a triad and the chord changes colour: dreamy, bluesy, spooky. Same rule as before: skip one note, stack the next. The new note is the <b class="co">7th</b>.')}
{two(building(['C', 'E', 'G', 'B'], ['root', '3rd', '5th', '7th']), '<div class="big3"><div><span>1</span><p>Build the triad: <b>C E G</b>.</p></div><div><span>2</span><p>Skip one, add the next: <b class="co">B</b>.</p></div><div><span>3</span><p>Count the keys between: <b>3 + 2 + 3</b>. That is <b>Cmaj7</b>.</p></div></div>' + minikb([(0, 'C'), (4, 'E'), (7, 'G'), (11, 'B')], '3 + 2 + 3', 34, 110), '1fr 1.1fr')}
{h3('Five flavours, all on C')}
{CARDS}
<p class="sm">Count the keys between, floor by floor. The last number is the new one: 3 gives a major 7th, 2 a minor 7th.</p>
{h3('A seventh on every floor of C major')}
{px('h7_key', 84, 'Only white keys. G7 is the one with the strongest pull home.')}""", 72)

P2 = hpage(f"""<div class="kick">Part III · Harmony · 5 · continued</div>
{inaction('Which seventh is it? G B D F', px('h7_mys', 84), ['<b>Count the keys between:</b> G to B is 3, B to D is 2, D to F is 2.', '<b>3 + 2 + 2</b> is the bluesy one.', '<b>The root is G:</b> G7.'], 'G B D F is <b>G7</b>, the chord that pulls hardest back to C.')}
{h3('Spot the difference')}
{pxr('h7_diff', ('n8', 'n12'), 96, 'One note decides: B makes Cmaj7, B♭ makes C7. Everything below stays the same.')}
{youknow('The blues, with sevenths', BLUES.replace('>C<', '>C7<').replace('>F<', '>F7<').replace('>G<', '>G7<'), 'Play the twelve-bar blues with <b class="co">7th chords</b> instead of triads and it suddenly sounds like the blues.', 'Add B♭ to C, E♭ to F and F to G, and play the chart again.')}
{thinkt('A triad is plain toast. The 7th is the topping: the same bread, but now it tastes of something.')}
{watch(['Writing C7 when you mean Cmaj7: “7” alone means the bluesy one, with B♭.', 'Stacking the 7th from the wrong note: count a 7th up from the root, not from the 5th.'])}
{foot('Four kinds of triad p. 66 · Chords in a key p. 68', 'Workbook Harmony 5 · Online: Library › Chords')}""", 73)

css += """
.big3{display:flex;flex-direction:column;gap:12px;font-size:16px;line-height:1.4} .big3 div{display:flex;gap:10px;align-items:flex-start} .big3 p{margin:0} .big3 span{flex:none;width:26px;height:26px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:14px}
.k7{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:6px 0 4px} .kc{border:1.5px solid #e3e1ee;border-radius:8px;padding:8px 8px 10px;display:flex;flex-direction:column;align-items:center;gap:4px;text-align:center}
.ks{font-family:PF,serif;font-size:26px;color:#26296b;line-height:1} .kn{font-size:12.5px;font-weight:700;color:#26296b} .km{font-size:17px;font-weight:700;color:#e4572e} .kw{font-size:11.5px;color:#6d6f9c;line-height:1.3}
"""
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{P1}{P2}</body></html>'
open('/mnt/user-data/outputs/house-rooms/mock-sevenths.html', 'w').write(html)
print('ok')
