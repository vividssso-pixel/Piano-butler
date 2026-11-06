# The Scale & Chord Book (her 5–6 Nov): fingering for every key, told as Secret Files in her own teaching order:
# C G D A E on one set of fingers → the circle nearly half full → the black-key family (thumbs on white keys) → majors complete → minors as changes to the parallel major.
# Every secret: Your mission (with why this order) → Try it → Detective question → turn the page → Secret revealed → fill your circle → Next secret → unlock stamp; a line for teachers and parents.
_src = open('/tmp/claude-0/pk/mock/secret.py').read()
exec(_src.split("P1 = spage(")[0])
exec(_src[_src.index('CSS = f"""'):_src.index('html = f')])
import math as _m
SEMI = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
MAJ = [0, 2, 4, 5, 7, 9, 11, 12]
def scalekb(tonic, fingers, W=27, H=74, nw=9, steps=MAJ, names=None):   # a one-octave scale on the keys: fingers on the keys (black keys red), thumbs ringed
    L = 'CDEFGAB'; s0 = L.index(tonic[0]); keys = []   # chromatic run from the tonic's white key
    for i in range(nw):
        keys.append(('w', i * W + W / 2))
        if L[(s0 + i) % 7] in 'CDFGA' and i < nw - 1: keys.append(('b', (i + 1) * W))
    o = f'<svg viewBox="-4 -4 {nw * W + 8} {H + 8}" style="width:100%;height:auto;display:block">'
    for i in range(nw): o += f'<rect x="{i * W}" y="0" width="{W}" height="{H}" fill="#fff" stroke="{N}" stroke-width="1.4"/>'
    for i in range(nw - 1):
        if L[(s0 + i) % 7] in 'CDFGA': o += f'<rect x="{(i + 1) * W - W * 0.3}" y="0" width="{W * 0.6}" height="{H * 0.58}" rx="2" fill="{N}"/>'
    for i in range(nw): o += f'<text x="{i * W + W / 2}" y="{H - 6}" text-anchor="middle" font-family="AH" font-size="10" font-weight="700" fill="{N}">{L[(s0 + i) % 7]}</text>'
    for st, f in zip(steps, fingers):
        kind, x = keys[st]; y = H * 0.66 if kind == 'w' else H * 0.4; th = f == 1
        o += f'<circle cx="{x}" cy="{y}" r="10" fill="{R if kind == "b" else N}" stroke="{"#f6c2b0" if th else "#fff"}" stroke-width="{4 if th else 1.5}"/><text x="{x}" y="{y + 4.3}" text-anchor="middle" font-family="AH" font-size="12.5" font-weight="700" fill="#fff">{f}</text>'
    return o + '</svg>'
# her 6 Nov, her own order: the seven white-key majors in keyboard order, C D E F G A B, right hand first, then the left hand;
# then the black-key keys by group (two black keys, then three); the circle (right adds ♯, left adds ♭; every white-key major but F is a sharp key);
# F and B learned apart for their fingering; then all twelve up by semitones, hands together; then the minors, from Cm, in the same order.
RH = [1, 2, 3, 1, 2, 3, 4, 5]; LH = [5, 4, 3, 2, 1, 3, 2, 1]
RHF = [1, 2, 3, 4, 1, 2, 3, 4]; LHB = [4, 3, 2, 1, 4, 3, 2, 1]
SEVEN = [('C', 'no black keys'), ('D', '2 black keys: F♯ C♯'), ('E', '4: F♯ C♯ G♯ D♯'), ('F', '1: B♭'), ('G', '1: F♯'), ('A', '3: F♯ C♯ G♯'), ('B', '5: F♯ C♯ D♯ G♯ A♯')]
def rows(hand): return ''.join(f'<div class="srow"><div class="slab"><b>{t} major</b><span>{d}</span></div>{scalekb(t, (RHF if t == "F" else RH) if hand == "R" else (LHB if t == "B" else LH))}</div>' for t, d in SEVEN)
def circle(done=(), half=(), note=('', '')):
    ks = ['C', 'G', 'D', 'A', 'E', 'B', 'F♯', 'D♭', 'A♭', 'E♭', 'B♭', 'F']
    o = '<svg viewBox="-130 -130 260 260" style="width:100%;max-width:250px;height:auto;display:block;margin:0 auto">'
    for i, k in enumerate(ks):
        a = _m.radians(i * 30 - 90); x, y = 92 * _m.cos(a), 92 * _m.sin(a)
        on, hf = k in done, k in half
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="24" fill="{R if on else "#fff"}" stroke="{R if (on or hf) else "#c9c7dc"}" stroke-width="{2.5 if hf else 1.8}" {"stroke-dasharray=\"4 3\"" if hf else ""}/>'
        o += f'<text x="{x:.1f}" y="{y + 6:.1f}" text-anchor="middle" font-family="PF" font-size="18" font-weight="700" fill="{"#fff" if on else (R if hf else "#a9a7c4")}">{k}</text>'
    return o + f'<text x="0" y="-4" text-anchor="middle" font-family="CV" font-size="24" fill="#26296b">{note[0]}</text><text x="0" y="22" text-anchor="middle" font-family="CV" font-size="24" fill="#26296b">{note[1]}</text></svg>'

def mission(what, why): return f'<div class="mission"><span class="ml">Your mission</span><p>{what}</p><p class="why2"><b>Why this order?</b> {why}</p></div>'
def detective(q, lines=2): return f'<div class="detective"><span class="ml">Detective question</span><p>{q}</p><div class="lines">{"<span class=\"al\"></span>" * lines}</div><span class="hand2 dont">don’t turn the page yet!</span></div>'
def teach(t): return f'<p class="teach"><b>For teachers and parents:</b> {t}</p>'
def tease(n, t): return f'<div class="tease2"><span class="ml">Next secret</span><p>{t}</p></div>'
def unlock(n, t): return f'<div class="unlock"><span class="seal">{n}</span><div><b>Secret No. {n} unlocked.</b> {t}</div></div>'
def tab(n, sub): return f'<div class="ftab">Secret No. {n} <span>· {sub}</span></div>'
STAMP = '<div class="stamp">TOP SECRET</div>'; REV = '<div class="stamp" style="transform:rotate(6deg)">REVEALED</div>'
PART = 'SCALES AND CHORDS'

def ticks7(hand): return f'<h3 class="sh3">Your seven, {hand}</h3><div class="t7">' + ''.join(f'<div><b>{k}</b><span>{"<i></i>" * 3}</span>{"<em>" + ("1 2 3 4 · 1 2 3 4" if k == "F" and hand == "right hand" else "4 3 2 1 · 4 3 2 1") + "</em>" if (k == "F" and hand == "right hand") or (k == "B" and hand == "left hand") else ""}</div>' for k in 'CDEFGAB') + '</div><p class="sm2" style="text-align:center">One circle each time a scale is clean: slow, even, and without stopping.</p>'
# ---------- Secret 1 · seven scales, right hand ----------
S1 = spage(f"""{tab(1, 'Scales')}{STAMP}
<h1 class="sh">Seven white keys, seven scales</h1>
{mission('Play a major scale from <b>every white key</b>, C D E F G A B, with the <b>right hand</b>.', 'Along the keyboard, one key at a time: you always know which scale comes next. Every major scale has the same steps, so only the <b class="co">black keys</b> change.')}
<div class="tryl">Try it: play all seven, right hand, slowly <span class="hand2" style="font-size:20px">(red = black key · the number is the finger · ringed = thumb)</span></div>
<div class="srows">{rows('R')}</div>
{detective('Six of the seven scales use <b>the same finger numbers</b>. Which one is different? And in that one, where would the thumb have landed?')}
{teach('let them play all seven before saying anything. The odd one out is on the next page: it sticks when they find it first.')}""", 1, PART)
S2 = spage(f"""{tab(1, 'revealed')}{REV}
<h1 class="sh" style="font-size:36px">Same fingers, except F</h1>
<div class="secret" style="font-size:19px"><b>1 2 3 · 1 2 3 4 5</b> for C, D, E, G, A and B. The thumb tucks under after finger 3.<br><b class="co">F major</b> is the one that changes: <b>1 2 3 4 · 1 2 3 4</b>.</div>
<h3 class="sh3">Why: the thumb stays on white keys</h3>
<div class="two" style="grid-template-columns:1.2fr 1fr;align-items:center"><div>{scalekb('F', RHF, W=34, H=92)}</div><div><p class="big2">In F major the 4th note is <b class="co">B♭</b>, a black key.</p><p>With the usual fingers the thumb would land on it. So finger 4 plays B♭, and the thumb tucks under one note later, onto C. The thumb always looks for a white key.</p></div></div>
<div class="two" style="grid-template-columns:1.2fr 1fr;align-items:center;margin-top:8px"><div>{scalekb('D', RH, W=34, H=92)}</div><div><p class="big2">Everywhere else the thumb plays notes <b class="co">1</b> and <b class="co">4</b>.</p><p>In D major that is D and G: both white. The black keys fall under fingers 2, 3 or 4, where the long fingers reach easily.</p></div></div>
{ticks7('right hand')}
{tease(2, 'Now the <b>left hand</b>. Same seven scales, and its own odd one out: Secret No. 2.')}
{unlock(1, 'In your Workbook: tick each scale when it is clean at a slow, even speed.')}""", 2, PART)

# ---------- Secret 2 · seven scales, left hand ----------
S3 = spage(f"""{tab(2, 'Scales')}{STAMP}
<h1 class="sh">The left hand’s turn</h1>
{mission('Play the same <b>seven</b> scales with the <b>left hand</b>.', 'The right hand already knows these keys, so the left hand only has to learn its fingers. And most of them are the right hand <b class="co">in a mirror</b>.')}
<div class="tryl">Try it: play all seven, left hand, slowly <span class="hand2" style="font-size:20px">(start on finger 5, the little finger, and climb)</span></div>
<div class="srows">{rows('L')}</div>
{detective('Read the left hand’s numbers <b>backwards</b>, from the top note down. What do you notice? Which scale is the odd one out this time, and is it the same one as for the right hand?')}
{teach('ask them to say the right-hand numbers while looking at the left-hand picture. The mirror is easier to hear than to see.')}""", 3, PART)
S4 = spage(f"""{tab(2, 'revealed')}{REV}
<h1 class="sh" style="font-size:36px">A mirror, except B</h1>
<div class="secret" style="font-size:19px">Left hand: <b>5 4 3 2 1 · 3 2 1</b> for C, D, E, F, G and A. From the top it reads 1 2 3 · 1 2 3 4 5: the right hand in a mirror.<br><b class="co">B major</b> is the one that changes: <b>4 3 2 1 · 4 3 2 1</b>.</div>
<h3 class="sh3">Why: the thumb stays on white keys, again</h3>
<div class="two" style="grid-template-columns:1.2fr 1fr;align-items:center"><div>{scalekb('B', LHB, W=34, H=92)}</div><div><p class="big2">In B major the 5th note is <b class="co">F♯</b>, a black key.</p><p>The usual left hand puts the thumb there. So the left hand starts on finger 4, and its thumbs land on <b>E</b> and <b>B</b>: white keys.</p></div></div>
<div class="pair2"><div><b>Right hand</b><span>F is different</span></div><div><b>Left hand</b><span>B is different</span></div></div>
<h3 class="sh3">Hands together</h3>
<div class="two" style="grid-template-columns:1fr 1fr;align-items:start"><div><p><b>Thumbs do not land together.</b> Going up, the right thumb tucks under after note 3; the left thumb plays note 5 and finger 3 crosses over it. That is why hands together feels wobbly at first.</p></div><div><p><b>Practise the join alone:</b> notes 3 4 5 of the scale, both hands, five times. Then the whole scale.</p></div></div>
{ticks7('left hand')}
{tease(3, 'Next, the <b>circle</b>: why some scales get sharps and some get flats, and why every white-key scale except F is a sharp key.')}
{unlock(2, 'Hands separately first, then the join, then together.')}""", 4, PART)


# ---------- Secret 3 · the circle: right adds a sharp, left adds a flat ----------
CK = ['C', 'G', 'D', 'A', 'E', 'B', 'F♯', 'D♭', 'A♭', 'E♭', 'B♭', 'F']
def circle2(fill=None, labels=None, arrows=False, big=False, center=('', '')):   # fill: key -> 'sharp' | 'flat' | 'home' | None
    fill = fill or {}; labels = labels or {}; R0 = 96
    o = f'<svg viewBox="-168 -172 336 332" style="width:100%;max-width:{310 if big else 250}px;height:auto;display:block;margin:0 auto">'
    if arrows:
        for sgn, col, t in ((1, R, '♯'), (-1, N, '♭')):
            a0, a1 = _m.radians(-90 + sgn * 8), _m.radians(-90 + sgn * 70); r = 138
            o += f'<path d="M{r * _m.cos(a0):.1f},{r * _m.sin(a0):.1f} A{r},{r} 0 0 {1 if sgn > 0 else 0} {r * _m.cos(a1):.1f},{r * _m.sin(a1):.1f}" fill="none" stroke="{col}" stroke-width="4" stroke-linecap="round"/>'
            hx, hy = r * _m.cos(a1), r * _m.sin(a1); ang = _m.degrees(a1) + (90 if sgn > 0 else -90)
            o += f'<path d="M-8,-7 L6,0 L-8,7 Z" fill="{col}" transform="translate({hx:.1f} {hy:.1f}) rotate({ang:.1f})"/>'
            tx, ty = 147 * _m.cos(_m.radians(-90 + sgn * 40)), 147 * _m.sin(_m.radians(-90 + sgn * 40))
            o += f'<text x="{tx:.1f}" y="{ty + 6:.1f}" text-anchor="middle" font-family="AH" font-size="17" font-weight="800" fill="{col}">+{t}</text>'
    for i, k in enumerate(CK):
        a = _m.radians(i * 30 - 90); x, y = R0 * _m.cos(a), R0 * _m.sin(a); f = fill.get(k)
        bg = {'sharp': R, 'flat': N, 'home': '#fff'}.get(f, '#fff'); st = {'sharp': R, 'flat': N, 'home': N}.get(f, '#c9c7dc'); tc = '#fff' if f in ('sharp', 'flat') else (N if f == 'home' else '#a9a7c4')
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="22" fill="{bg}" stroke="{st}" stroke-width="2"/><text x="{x:.1f}" y="{y + 6:.1f}" text-anchor="middle" font-family="PF" font-size="{17 if len(k) < 2 else 15}" font-weight="700" fill="{tc}">{k}</text>'
        if k in labels:
            lx, ly = (R0 - 42) * _m.cos(a), (R0 - 42) * _m.sin(a)
            o += f'<text x="{lx:.1f}" y="{ly + 5:.1f}" text-anchor="middle" font-family="AH" font-size="13" font-weight="800" fill="{R if "♯" in labels[k] else N}">{labels[k]}</text>'
    o += f'<text x="0" y="-2" text-anchor="middle" font-family="CV" font-size="22" fill="{N}">{center[0]}</text><text x="0" y="22" text-anchor="middle" font-family="CV" font-size="22" fill="{N}">{center[1]}</text>'
    return o + '</svg>'
SEV = [('C', 'none'), ('D', 'F♯ C♯'), ('E', 'F♯ C♯ G♯ D♯'), ('F', 'B♭'), ('G', 'F♯'), ('A', 'F♯ C♯ G♯'), ('B', 'F♯ C♯ G♯ D♯ A♯')]
sevtab = '<table class="sev"><tr><th>Scale</th><th>Its black keys</th><th>How many?</th></tr>' + ''.join(f'<tr><td><b>{k} major</b></td><td>{b}</td><td><span class="bx"></span></td></tr>' for k, b in SEV) + '</table>'
S5 = spage(f"""{tab(3, 'Scales')}{STAMP}
<h1 class="sh">Where do your seven live?</h1>
{mission('Find your seven white-key scales on the <b>circle of fifths</b>, and see why some get sharps and one gets a flat.', 'You already play all seven. Now the circle tells you <b class="co">before you play</b> how many black keys a scale will need, for every key on the piano.')}
<div class="two" style="grid-template-columns:1fr 1.05fr;align-items:center;gap:18px"><div>{sevtab}<p class="sm2">Count the black keys you played in Secrets 1 and 2 and write the number.</p></div><div>{circle2(fill={'C': 'home'}, center=('C at the', 'top'))}</div></div>
<div class="tryl">Try it: on the circle, colour every scale with <b class="co">sharps</b> red and every scale with <b>flats</b> blue. <span class="hand2" style="font-size:20px">(or turn the Scale finder in the app)</span></div>
{detective('Which side of the circle are the red ones on? Read them clockwise from C: does the number of sharps go up one at a time? And which white-key scale is all alone on the other side?')}
{teach('let them colour first, with the app’s Scale finder open if you have it: right is ♯, left is ♭. Say nothing about F until they spot it.')}""", 5, PART)
S6 = spage(f"""{tab(3, 'revealed')}{REV}
<h1 class="sh" style="font-size:36px">Right for sharps, left for flats</h1>
<div class="secret" style="font-size:19px">Clockwise from C, each step adds <b class="co">one sharp</b>: G 1, D 2, A 3, E 4, B 5. One step anticlockwise adds <b>one flat</b>: F. So every white-key major is a sharp key <b class="co">except F</b>.</div>
<div class="two" style="grid-template-columns:1.05fr 1fr;align-items:center;gap:18px"><div>{circle2(fill={'C': 'home', 'G': 'sharp', 'D': 'sharp', 'A': 'sharp', 'E': 'sharp', 'B': 'sharp', 'F': 'flat'}, labels={'G': '1♯', 'D': '2♯', 'A': '3♯', 'E': '4♯', 'B': '5♯', 'F': '1♭'}, arrows=True, big=True)}</div>
<div><h3 class="sh3" style="margin-top:0">The new sharp is always note 7</h3><table class="sev"><tr><th>Key</th><th>Sharps</th><th>The new one</th></tr>{''.join(f'<tr><td><b>{k}</b></td><td>{s_}</td><td><b class="co">{n}</b> = note 7 of {k}</td></tr>' for k, s_, n in (('G', 'F♯', 'F♯'), ('D', 'F♯ C♯', 'C♯'), ('A', 'F♯ C♯ G♯', 'G♯'), ('E', 'F♯ C♯ G♯ D♯', 'D♯'), ('B', 'F♯ C♯ G♯ D♯ A♯', 'A♯')))}</table><p class="sm2">Each step keeps the old sharps and adds one more: the note just below the new key note.</p></div></div>
<h3 class="sh3">F, the odd one out, twice over</h3>
<div class="pair2"><div><b>On the circle</b><span>the only flat white key</span></div><div><b>Under the right hand</b><span>1 2 3 4 · 1 2 3 4</span></div></div>
<p class="sm2" style="text-align:center">The same B♭ that makes F the flat key also moves the right-hand thumb (Secret No. 1).</p>
{tease(4, 'The rest of the left side of the circle is the <b>black-key family</b>. Next we play them in keyboard order: the keys of the <b>two black keys</b> first, then the <b>three</b>.')}
{unlock(3, 'In your Workbook: colour your own circle, and write the number of sharps or flats in each key.')}""", 6, PART)

CSS2 = f"""
.mission,.detective,.tease2{{position:relative;border:2px solid {N};border-radius:10px;padding:10px 14px;margin:10px 0;background:#f6f5fa}} .detective{{border-color:{R};background:#fff7f3}} .tease2{{background:#fff}}
.ml{{display:block;font-weight:800;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:{R};margin-bottom:2px}} .mission p,.detective p,.tease2 p{{margin:3px 0;font-size:16px;line-height:1.5}} .why2{{font-size:15px!important}}
.tryl{{font-weight:700;font-size:16px;margin:12px 0 2px}} .srows{{display:flex;flex-direction:column;gap:2px}} .srow{{display:grid;grid-template-columns:150px 1fr;gap:12px;align-items:end}} .srow svg{{max-height:92px}} .slab b{{display:block;font-size:16px}} .slab span{{font-size:13px;color:#6d6f9c}} .srows .srow svg{{max-height:66px}} .srows{{gap:0}} .t7{{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin:6px 0}} .t7>div{{border:1.5px solid {N};border-radius:10px;padding:6px 2px 8px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:4px}} .t7 b{{font-family:PF,serif;font-size:24px}} .t7 span{{display:flex;gap:3px}} .t7 i{{display:inline-block;width:14px;height:14px;border-radius:50%;border:1.5px solid #b9bad6}} .t7 em{{font-style:normal;font-size:10px;font-weight:700;color:{R};line-height:1.2}}
.sev{{width:100%;border-collapse:collapse;font-size:14.5px}} .sev th{{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#6d6f9c;text-align:left;border-bottom:1.5px solid {N};padding:4px 6px}} .sev td{{border-bottom:1px solid #e3e1ee;padding:6px}} .sev .bx{{display:inline-block;width:34px;height:24px;border:1.5px solid {N};border-radius:4px}}
.pair2{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0}} .pair2>div{{border:2px solid {R};border-radius:10px;padding:8px 12px;text-align:center}} .pair2 b{{display:block;font-size:16px}} .pair2 span{{font-family:CV,cursive;font-size:22px;font-weight:700;color:{R}}}
.lines .al{{display:block;height:24px;border-bottom:1.4px solid #c9c7dc}} .teach{{font-size:14px;color:#6d6f9c;border-top:1px dashed #c9c7dc;padding-top:6px;margin-top:10px}}
.big2{{font-size:18px;font-weight:700;margin:0 0 6px}} .sm2{{font-size:13.5px;color:#6d6f9c;margin:4px 0 0}} .dont{{position:absolute;right:14px;bottom:-14px;font-size:22px;color:{R};transform:rotate(-3deg)}}
"""
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{CSS}{CSS2}</style></head><body>{S1}{S2}{S3}{S4}{S5}{S6}</body></html>'
open('/mnt/user-data/outputs/house-rooms/scalebook.html', 'w').write(html)
print('ok')
