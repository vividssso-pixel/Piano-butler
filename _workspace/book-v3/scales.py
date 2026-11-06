# Mock-up (her 5 Nov): 'One hand, five scales' as a Secret File, built to carry the teacher's intent: mission -> try -> question -> (turn the page) -> secret revealed
_src = open('/tmp/claude-0/pk/mock/secret.py').read()
exec(_src.split("P1 = spage(")[0])
exec(_src[_src.index('CSS = f"""'):_src.index('html = f')])
SEMI = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
def scalekb(tonic, W=27, H=74, nw=9):
    L = 'CDEFGAB'; s0 = L.index(tonic); keys = []   # chromatic run from the tonic: (kind, x)
    for i in range(nw):
        keys.append(('w', i * W + W / 2))
        if L[(s0 + i) % 7] in 'CDFGA' and i < nw - 1: keys.append(('b', (i + 1) * W))
    o = f'<svg viewBox="-4 -4 {nw * W + 8} {H + 8}" style="width:100%;height:auto;display:block">'
    for i in range(nw): o += f'<rect x="{i * W}" y="0" width="{W}" height="{H}" fill="#fff" stroke="{N}" stroke-width="1.4"/>'
    for i in range(nw - 1):
        if L[(s0 + i) % 7] in 'CDFGA': o += f'<rect x="{(i + 1) * W - W * 0.3}" y="0" width="{W * 0.6}" height="{H * 0.58}" rx="2" fill="{N}"/>'
    for i in range(nw): o += f'<text x="{i * W + W / 2}" y="{H - 6}" text-anchor="middle" font-family="AH" font-size="10" font-weight="700" fill="{N}">{L[(s0 + i) % 7]}</text>'
    for n, (st, f) in enumerate(zip([0, 2, 4, 5, 7, 9, 11, 12], [1, 2, 3, 1, 2, 3, 4, 5])):
        kind, x = keys[st]; y = H * 0.66 if kind == 'w' else H * 0.4; th = f == 1
        o += f'<circle cx="{x}" cy="{y}" r="10" fill="{R if kind == "b" else N}" stroke="{"#f6c2b0" if th else "#fff"}" stroke-width="{4 if th else 1.5}"/><text x="{x}" y="{y + 4.3}" text-anchor="middle" font-family="AH" font-size="12.5" font-weight="700" fill="#fff">{f}</text>'
    return o + '</svg>'
FIVE = [('C', 'no black keys'), ('G', '1 black key: F♯'), ('D', '2: F♯ C♯'), ('A', '3: F♯ C♯ G♯'), ('E', '4: F♯ C♯ G♯ D♯')]
def circle(done=(), half=()):
    ks = ['C', 'G', 'D', 'A', 'E', 'B', 'F♯', 'D♭', 'A♭', 'E♭', 'B♭', 'F']; import math
    o = '<svg viewBox="-130 -130 260 260" style="width:100%;max-width:250px;height:auto;display:block;margin:0 auto">'
    for i, k in enumerate(ks):
        a = math.radians(i * 30 - 90); x, y = 92 * math.cos(a), 92 * math.sin(a)
        on, hf = k in done, k in half
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="24" fill="{R if on else "#fff"}" stroke="{R if (on or hf) else "#c9c7dc"}" stroke-width="{2.5 if hf else 1.8}" {"stroke-dasharray=\"4 3\"" if hf else ""}/>'
        o += f'<text x="{x:.1f}" y="{y + 6:.1f}" text-anchor="middle" font-family="PF" font-size="18" font-weight="700" fill="{"#fff" if on else (R if hf else "#a9a7c4")}">{k}</text>'
    return o + '<text x="0" y="-4" text-anchor="middle" font-family="CV" font-size="24" fill="#26296b">nearly</text><text x="0" y="22" text-anchor="middle" font-family="CV" font-size="24" fill="#26296b">half!</text></svg>'
ROWS = ''.join(f'<div class="srow"><div class="slab"><b>{t} major</b><span>{d}</span></div>{scalekb(t)}</div>' for t, d in FIVE)
S1 = spage(f"""<div class="ftab">Secret No. 12 <span>· Scales</span></div><div class="stamp">TOP SECRET</div>
<h1 class="sh">One hand, five scales</h1>
<div class="mission"><span class="ml">Your mission</span><p>Learn <b>five</b> major scales with <b>one</b> set of finger numbers.</p><p class="why2"><b>Why this order?</b> C, G, D, A, E: each one adds just <b class="co">one more black key</b>, and your fingers never have to change.</p></div>
<div class="tryl">Try it: play all five, right hand, slowly <span class="hand2" style="font-size:20px">(red = black key · the number is the finger · ringed = thumb)</span></div>
<div class="srows">{ROWS}</div>
<div class="detective"><span class="ml">Detective question</span><p>Look at the finger numbers in all five scales. <b>What is the same every time?</b> And which notes does your thumb always land on?</p><div class="lines"><span class="al"></span><span class="al"></span></div><span class="hand" style="right:16px;bottom:-14px">don’t turn the page yet!</span></div>
<p class="teach"><b>For teachers and parents:</b> let them play all five before saying anything. The rule is on the next page: it sticks when they find it first.</p>""", 1, 'SCALES AND KEYS')
S2 = spage(f"""<div class="ftab">Secret No. 12 <span>· revealed</span></div><div class="stamp" style="transform:rotate(6deg)">REVEALED</div>
<h1 class="sh" style="font-size:36px">Same fingers, every time</h1>
<div class="secret" style="font-size:19px"><b>1 2 3 · 1 2 3 4 5</b>, in all five. The thumb tucks under after finger 3, every time.</div>
<h3 class="sh3">Why it works: the thumb only lands on white keys</h3>
<div class="two" style="grid-template-columns:1.2fr 1fr;align-items:center"><div>{scalekb('D', W=34, H=92)}</div><div><p class="big2">Your thumb plays notes <b class="co">1</b> and <b class="co">4</b> of the scale.</p><p>In C, G, D, A and E, notes 1 and 4 are always <b>white</b> keys: C–F, G–C, D–G, A–D, E–A. The black keys fall under fingers 2, 3 or 4, where the long fingers reach easily.</p></div></div>
<h3 class="sh3">Fill in your circle</h3>
<div class="two" style="grid-template-columns:1fr 1.15fr;align-items:center">{circle(done=('C', 'G', 'D', 'A', 'E'), half=('B',)).replace('max-width:250px','max-width:290px')}<div><p>Colour in the five keys you just learned. Look where they sit: one after another, round the circle. <b>Five scales, one hand shape, and nearly half the circle.</b></p><p><span class="hand2">B joins the club for the right hand too!</span></p><p class="sm">Left hand: 5 4 3 2 1 · 3 2 1, the same for all five as well.</p></div></div>
<div class="tease2"><span class="ml">Next secret</span><p>The empty side of the circle belongs to the <b>black-key family</b>. Secret No. 13: <b>thumbs only on white keys</b>, and three more scales fall into place.</p></div>
<div class="unlock"><span class="seal">12</span><div><b>Secret No. 12 unlocked.</b> In your Workbook: fill your own circle, one key at a time.</div></div>""", 2, 'SCALES AND KEYS')
CSS2 = f"""
.mission,.detective,.tease2{{position:relative;border:2px solid {N};border-radius:10px;padding:10px 14px;margin:10px 0;background:#f6f5fa}} .detective{{border-color:{R};background:#fff7f3}} .tease2{{background:#fff}}
.ml{{display:block;font-weight:800;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:{R};margin-bottom:2px}} .mission p,.detective p,.tease2 p{{margin:3px 0;font-size:16px;line-height:1.5}} .why2{{font-size:15px!important}}
.tryl{{font-weight:700;font-size:16px;margin:12px 0 2px}} .srows{{display:flex;flex-direction:column;gap:2px}} .srow{{display:grid;grid-template-columns:150px 1fr;gap:12px;align-items:end}} .srow svg{{max-height:92px}} .slab b{{display:block;font-size:17px}} .slab span{{font-size:13.5px;color:#6d6f9c}}
.lines .al{{display:block;height:24px;border-bottom:1.4px solid #c9c7dc}} .teach{{font-size:14px;color:#6d6f9c;border-top:1px dashed #c9c7dc;padding-top:6px;margin-top:10px}}
.big2{{font-size:18px;font-weight:700;margin:0 0 6px}}
"""
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{CSS}{CSS2}</style></head><body>{S1}{S2}</body></html>'
open('/mnt/user-data/outputs/house-rooms/mock-scales.html', 'w').write(html)
print('ok')
