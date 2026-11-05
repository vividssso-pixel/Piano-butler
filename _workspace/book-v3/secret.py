# Mock-up (her 5 Nov: 'explain so even very young children get it; spare no pictures; a book you want to keep reading, like a top-secret 족보')
exec(open('/tmp/claude-0/pk/harmony.py').read().split("\n_secs = [assemble")[0])
import base64
CAV = base64.b64encode(open('/tmp/e2e/node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2', 'rb').read()).decode()
N, R = '#26296b', '#e4572e'
def kb(n=8, W=30, H=100, marks='', hops=(), dots=(), ghost=(), fingers=None, labels=True):
    o = f'<svg viewBox="-4 -34 {n * W + 8} {H + 52}" style="width:100%;height:auto;display:block">'
    for i in range(n): o += f'<rect x="{i * W}" y="0" width="{W}" height="{H}" fill="#fff" stroke="{N}" stroke-width="1.6"/>'
    for i in range(n - 1):
        if 'CDEFGAB'[i % 7] in 'CDFGA': o += f'<rect x="{(i + 1) * W - W * 0.3}" y="0" width="{W * 0.6}" height="{H * 0.58}" rx="2" fill="{N}"/>'
    if labels:
        for i in range(n): o += f'<text x="{i * W + W / 2}" y="{H - 8}" text-anchor="middle" font-family="AH" font-size="11" font-weight="700" fill="{N}">{"CDEFGAB"[i % 7]}</text>'
    for i in ghost: o += f'<rect x="{i * W + 3}" y="{H * 0.62}" width="{W - 6}" height="{H * 0.22}" rx="4" fill="#eef0f8"/><text x="{i * W + W / 2}" y="{H * 0.78}" text-anchor="middle" font-family="CV" font-size="16" fill="#8d8fb3">skip</text>'
    for i in dots: o += f'<circle cx="{i * W + W / 2}" cy="{H * 0.72}" r="10" fill="{R}"/>'
    for a, b in hops:
        x1, x2 = a * W + W / 2, b * W + W / 2
        o += f'<path d="M{x1},-6 Q{(x1 + x2) / 2},-30 {x2},-6" fill="none" stroke="{R}" stroke-width="2.6" stroke-dasharray="5 4"/><path d="M{x2 - 8},-14 L{x2},-5 L{x2 + 3},-16" fill="none" stroke="{R}" stroke-width="2.6"/>'
    if fingers:
        for i, f in fingers: o += f'<circle cx="{i * W + W / 2}" cy="-16" r="11" fill="#fff" stroke="{R}" stroke-width="2.2"/><text x="{i * W + W / 2}" y="-11" text-anchor="middle" font-family="AH" font-size="13" font-weight="700" fill="{R}">{f}</text>'
    return o + marks + '</svg>'
def snow(balls, letters=('C', 'E', 'G'), face=None, w=90, hat=True, red0=True, tags=True):
    ys, rs = [150, 98, 58], [34, 26, 20]
    o = f'<svg viewBox="0 0 {150 if tags else 120} 196" style="width:{w}px;height:auto;display:block;margin:0 auto">'
    for i in range(balls):
        o += f'<circle cx="60" cy="{ys[i] + 10}" r="{rs[i]}" fill="{"#fde6dd" if i == 0 else "#fff"}" stroke="{R if i == 0 else N}" stroke-width="2.6"/>'
        if tags: o += f'<text x="{60 + rs[i] + 8}" y="{ys[i] + 18}" font-family="PF" font-size="{24 - i * 2}" font-weight="700" fill="{R if i == 0 and red0 else N}">{letters[i]}</text>'
    top = ys[balls - 1] + 10; rt = rs[balls - 1]
    if hat: o += f'<path d="M{60 - rt * 0.8},{top - rt + 2} L{60 + rt * 0.8},{top - rt + 2} L{60 + rt * 0.6},{top - rt - 20} L{60 - rt * 0.6},{top - rt - 20} Z" fill="{N}"/><line x1="{60 - rt * 1.1}" x2="{60 + rt * 1.1}" y1="{top - rt + 2}" y2="{top - rt + 2}" stroke="{N}" stroke-width="4" stroke-linecap="round"/>' if balls == 3 else ''
    if face or balls < 3:
        f = face or 'happy'
        o += f'<circle cx="{60 - rt * 0.35}" cy="{top - rt * 0.25}" r="2.2" fill="{N}"/><circle cx="{60 + rt * 0.35}" cy="{top - rt * 0.25}" r="2.2" fill="{N}"/>'
        m = {'happy': f'M{60 - rt * 0.45},{top + rt * 0.25} Q60,{top + rt * 0.6} {60 + rt * 0.45},{top + rt * 0.25}', 'sad': f'M{60 - rt * 0.45},{top + rt * 0.5} Q60,{top + rt * 0.15} {60 + rt * 0.45},{top + rt * 0.5}', 'worried': f'M{60 - rt * 0.45},{top + rt * 0.4} Q{60 - rt * 0.2},{top + rt * 0.2} 60,{top + rt * 0.4} Q{60 + rt * 0.2},{top + rt * 0.6} {60 + rt * 0.45},{top + rt * 0.4}'}[f]
        o += f'<path d="{m}" fill="none" stroke="{N}" stroke-width="2.2" stroke-linecap="round"/>'
    return o + '</svg>'
def panel(n, pic, cap): return f'<div class="pn"><span class="pnum">{n}</span>{pic}<p>{cap}</p></div>'
WHITE7 = [('C', 'E', 'G', 'happy'), ('D', 'F', 'A', 'sad'), ('E', 'G', 'B', 'sad'), ('F', 'A', 'C', 'happy'), ('G', 'B', 'D', 'happy'), ('A', 'C', 'E', 'sad'), ('B', 'D', 'F', 'worried')]
def spage(inner, n, part='HARMONY'): return f'<section class="pg sf"><div class="top"><span>THE BUTLER’S SECRET FILES</span><span>{part}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'
P1 = spage(f"""<div class="ftab">Secret No. 1 <span>· Harmony</span></div><div class="stamp">TOP SECRET</div>
<h1 class="sh">The snowman rule</h1>
<div class="secret"><b>The secret:</b> the most-used chord in the world is built like a snowman. <b>Play one, skip one, play one, skip one, play one.</b></div>
<div class="pns">{panel(1, kb(dots=(0,)) + snow(1, w=92), 'Pick any white key. That is the <b class="co">root</b>: the big ball at the bottom.')}{panel(2, kb(dots=(0, 2), hops=((0, 2),), ghost=(1,)) + snow(2, w=92), 'Skip one key. Play the next. Second ball!')}{panel(3, kb(dots=(0, 2, 4), hops=((0, 2), (2, 4)), ghost=(1, 3)) + snow(3, w=92), 'Skip, play again. Hat on: you built a <b>chord</b>!')}</div>
<div class="try"><div class="trl">Try it · 10 seconds</div><div class="trg">{kb(n=8, W=34, fingers=((0, 1), (2, 3), (4, 5)), dots=(0, 2, 4))}<div><p class="big">Thumb on C. Fingers <b class="co">1, 3, 5</b> down together.</p><p>That sound is <b>C E G</b>, the C chord. Now slide your hand to any other white key and do it again: it always works.</p></div></div><span class="hand" style="right:24px;bottom:6px">works on every key!</span></div>
<h3 class="sh3">Why “root”?</h3>
<div class="why">{snow(3, face='happy', w=74)}<p>A tree grows from its root, and a chord grows from its bottom note. The root also gives the chord its <b>name</b>: a snowman standing on C is the <b>C chord</b>. <span class="hand2">← the name lives at the bottom</span></p></div>""", 66)
P2 = spage(f"""<div class="ftab">Secret No. 1 <span>· continued</span></div>
<h3 class="sh3" style="margin-top:4px">Meet the seven snowmen of the white keys</h3>
<div class="sn7">{''.join(f'<div>{snow(3, (a, b, c), face=f, w=76)}<b>{a}</b><i>{ {"happy": "happy", "sad": "sad", "worried": "worried"}[f]}</i></div>' for a, b, c, f in WHITE7)}</div>
<p class="tease">Same shape, different faces. Why do some smile and some frown? <b>That is Secret No. 2.</b> <span class="hand2">(hint: count the keys between the balls)</span></p>
<div class="game"><div class="trl">Game · spot the snowmen</div>{px('h_is', 66)}<p>Which of the three is a real snowman? Each ball must sit one skip above the last.</p><div class="ans">Answer: only number 1 (D F A). Number 2 has two balls touching; number 3 skips too far.</div></div>
<h3 class="sh3">Build one yourself</h3><div class="pns">{panel('G', kb(dots=(4, 6, 8), hops=((4, 6), (6, 8)), ghost=(5, 7), n=10) + snow(3, ('G', 'B', 'D'), w=80), 'Start on G: <b>G B D</b>.')}{panel('F', kb(dots=(3, 5, 7), hops=((3, 5), (5, 7)), ghost=(4, 6), n=10) + snow(3, ('F', 'A', 'C'), w=80), 'Start on F: <b>F A C</b>.')}{panel('?', kb(n=10) + snow(3, ('?', '?', '?'), w=80, red0=False), 'Your turn: start on A. Which three keys?')}</div>
<div class="trap"><span class="tst">TRAP</span><p>Two balls touching (like D and E) is <b>not</b> a snowman: it falls over. Always skip one.</p></div>
<div class="unlock"><span class="seal">1</span><div><b>Secret No. 1 unlocked.</b> Tick it in your Secret List, then try a snowman on every white key.</div></div>""", 67)
CSS = f"""@font-face{{font-family:'CV';src:url(data:font/woff2;base64,{CAV}) format('woff2')}}
.sf .body{{position:relative}} .ftab{{display:inline-block;background:{N};color:#fff;font-weight:700;font-size:13px;letter-spacing:.14em;text-transform:uppercase;padding:5px 12px 4px;border-radius:4px 4px 0 0}} .ftab span{{opacity:.7}}
.stamp{{position:absolute;right:10px;top:-6px;transform:rotate(-8deg);border:3px solid {R};color:{R};font-weight:800;letter-spacing:.2em;font-size:15px;padding:4px 10px;border-radius:4px;opacity:.85}}
.sh{{font-size:44px;margin:6px 0 8px}} .secret{{border:2px dashed {R};background:#fff7f3;padding:10px 14px;font-size:17px;line-height:1.5;border-radius:6px}}
.pns{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:14px 0}} .pn{{position:relative;border:2px solid {N};border-radius:10px;padding:16px 10px 10px;background:#fff;display:flex;flex-direction:column;gap:6px;justify-content:space-between}} .pn p{{margin:0;font-size:15px;line-height:1.4;text-align:center}} .pnum{{position:absolute;left:-10px;top:-12px;width:28px;height:28px;border-radius:50%;background:{R};color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:15px}}
.try{{position:relative;border:2px solid {N};border-radius:10px;padding:10px 14px;margin:10px 0;background:#f6f5fa}} .trl{{white-space:nowrap;font-weight:800;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:{R};margin-bottom:4px}} .trg{{display:grid;grid-template-columns:1fr 1.2fr;gap:16px;align-items:center}} .try p{{margin:4px 0;font-size:15px}} .big{{font-size:18px!important;font-weight:700}}
.hand{{position:absolute;font-family:CV;font-size:24px;color:{R};transform:rotate(-4deg)}} .hand2{{font-family:CV;font-size:21px;color:{R};white-space:nowrap}}
.sh3{{font-size:19px;margin:12px 0 6px;border-top:1.5px solid {N};padding-top:7px}} .why{{display:grid;grid-template-columns:90px 1fr;gap:14px;align-items:center}} .why p{{font-size:16px;line-height:1.55;margin:0}}
.sn7{{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;text-align:center}} .sn7 b{{display:block;font-size:16px;color:{N}}} .sn7 i{{display:block;font-family:CV;font-size:20px;color:{R};font-style:normal}} .tease{{font-size:16px;margin:6px 0 4px}}
.game{{border:2px solid {R};border-radius:10px;padding:10px 14px;margin:12px 0;position:relative}} .game p{{margin:4px 0;font-size:15px}} .ans{{transform:rotate(180deg);font-size:13.5px;color:#6d6f9c;text-align:center;margin-top:6px}}
.trap{{display:flex;gap:12px;align-items:center;margin:10px 0}} .tst{{border:3px solid {R};color:{R};font-weight:800;letter-spacing:.18em;padding:3px 9px;transform:rotate(-6deg);border-radius:4px}} .trap p{{margin:0;font-size:16px}}
.unlock{{display:flex;gap:12px;align-items:center;border-top:1.5px dashed {N};padding-top:10px;margin-top:8px;font-size:15px}} .seal{{width:42px;height:42px;border-radius:50%;background:{R};color:#fff;font-family:PF;font-weight:800;font-size:22px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 4px #fde6dd}}
"""
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{CSS}</style></head><body>{P1}{P2}</body></html>'
open('/mnt/user-data/outputs/house-rooms/mock-secret.html', 'w').write(html)
print('ok')
