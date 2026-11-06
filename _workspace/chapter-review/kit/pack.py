# Chapter 1 review pack: front pages (cover, what I found, the online drill) as HTML for Chromium to print
import html, os
NM = os.path.abspath('../tools/node_modules/@fontsource')
FONTS = ''.join(f"@font-face{{font-family:'Inter';font-weight:{w};src:url(file://{NM}/inter/files/inter-latin-{w}-normal.woff2) format('woff2');}}" for w in (400, 600, 700, 800)) + \
        ''.join(f"@font-face{{font-family:'Playfair Display';font-weight:{w};src:url(file://{NM}/playfair-display/files/playfair-display-latin-{w}-normal.woff2) format('woff2');}}" for w in (800, 900))
CSS = FONTS + """
@page { size:A4; margin:0; }
* { box-sizing:border-box; }
body { margin:0; font-family:Inter,'Noto Sans CJK KR',sans-serif; color:#26296b; font-size:11.5pt; line-height:1.45; }
.pg { width:210mm; height:297mm; padding:13mm 15mm 17mm; page-break-after:always; position:relative; overflow:hidden; }
.pg:last-child { page-break-after:auto; }
h1, h2 { font-family:'Playfair Display',Georgia,serif; margin:0; line-height:1.1; }
h1 { font-size:30pt; font-weight:900; }
h2 { font-size:17pt; font-weight:900; margin:0 0 2mm; }
.k { color:#e4572e; font-weight:800; font-size:10pt; margin-bottom:2mm; }
.sub { color:#4a4d86; margin:2mm 0 0; }
.box { border:1.2px solid #26296b; border-radius:3mm; padding:3.5mm 5mm; margin-top:4mm; }
.toc { width:100%; border-collapse:collapse; margin-top:2mm; font-size:11pt; }
.toc td { padding:1.4mm 0; border-bottom:0.6px solid #d9d4c4; }
.toc td.n { text-align:right; color:#6d6f9c; white-space:nowrap; }
.how li { margin:1mm 0; }
.q { margin-top:4mm; }
.q b { display:block; }
.lines { height:15mm; background:repeating-linear-gradient(#fff 0 6.6mm, #b9b6d8 6.6mm 6.9mm); margin-top:1mm; }
.lines.s { height:8.5mm; }
.item { display:grid; grid-template-columns:9mm 1fr 30mm; gap:2mm; padding:2.2mm 0; border-bottom:0.6px solid #d9d4c4; font-size:10.3pt; break-inside:avoid; }
.item .id { font-weight:800; color:#e4572e; }
.item .t b { color:#26296b; }
.item .t { color:#3c3f78; }
.item .fx { color:#26296b; font-weight:600; margin-top:0.8mm; }
.tick { font-size:9.5pt; color:#26296b; white-space:nowrap; }
.tick span { display:inline-block; width:3.6mm; height:3.6mm; border:1.2px solid #26296b; border-radius:0.8mm; vertical-align:-0.6mm; margin-right:1mm; }
.yel { background:#fff1a8; }
.item.yel { padding-left:1.5mm; padding-right:1.5mm; }
.ans { height:8mm; border-bottom:0.8px solid #b9b6d8; }
.grid3 { display:grid; grid-template-columns:repeat(3,1fr); gap:4mm; margin-top:3mm; align-items:start; }
.grid3 img { width:100%; border:0.6px solid #d9d4c4; border-radius:2mm; }
.cap { font-size:9.5pt; font-weight:700; margin-top:1mm; }
.why { font-size:9.6pt; color:#3c3f78; columns:2; column-gap:7mm; margin-top:3mm; }
.why p { margin:0 0 1.6mm; break-inside:avoid; }
.why b { color:#26296b; }
.foot { position:absolute; bottom:8mm; left:15mm; right:15mm; font-size:8.5pt; color:#6d6f9c; display:flex; justify-content:space-between; }
"""

def page(inner, foot):
    return f'<section class="pg">{inner}<div class="foot"><span>Piano Butler · Chapter 1 review · Posture &amp; Hand Shape</span><span>{foot}</span></div></section>'

def doc(pages):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'

def cover(toc):
    rows = ''.join(f'<tr><td>{html.escape(a)}</td><td class="n">{b}</td></tr>' for a, b in toc)
    inner = f'''
<div class="k">Chapter review 1 of 25</div>
<h1>Posture &amp; Hand Shape</h1>
<p class="sub">Everything in chapter 1, in one pack: the app lesson (as the Lesson Book), the Workbook, the Teacher copy, the online drill, and a first draft of the new public page for Google. Prepared 8 October 2026.</p>
<div class="box"><h2>What's inside</h2><table class="toc">{rows}</table></div>
<div class="box how"><h2>How to check</h2>
<ol style="margin:0;padding-left:5mm">
<li>Read pages 2 and 3 first: what I already found. Tick <b>Fix</b> or <b>Leave it</b>, and answer the yellow questions.</li>
<li>Go through the rest with a red pen. Mark anything wrong, unclear, or not how you teach it.</li>
<li>Send photos of the marked pages, or just tell me in the chat. Either is fine.</li>
</ol></div>
<div class="box"><h2>Three questions for the public page</h2>
<p class="sub" style="margin:0 0 1mm">Your answers become your own words on the page. Two or three sentences each is plenty.</p>
<div class="q"><b>1. What do students get wrong most in this chapter?</b><div class="lines"></div></div>
<div class="q"><b>2. What do you say or do that works? A phrase, a trick, a game.</b><div class="lines"></div></div>
<div class="q"><b>3. What must not be missing?</b><div class="lines s"></div></div>
</div>'''
    return page(inner, 'page 1')

FIX = [
    ('A1', '<b>Online drill, level 3 "Which finger?"</b> Every finger has its number drawn on it, so the answer is showing (see page 4 of this pack). The "Show me finger 3!" game in lesson step 6 has the same problem.', 'Hide the numbers while a question is asked; show them after the answer.'),
    ('A2', '<b>Workbook page 2, the map.</b> Step 7 says "in the app only", but Workbook page 6 is the posture checklist for step 7. Step 5 (Meet your fingers) is listed as "Left hand, right hand".', 'Step 5: Meet your fingers, page 4. Step 7: Posture check, page 6.'),
    ('A3', '<b>Lesson Book page 2.</b> The stool picture prints in the "too low" position with a red cross, under "move the stool until every check is green". On paper nobody can move it.', 'Print the good set-up, every check green.'),
    ('A4', '<b>Lesson Book page 3.</b> It says "six short exercises", but only one (Arm glide) is printed.', 'List all six, one line each (as on the website draft).'),
    ('A5', '<b>Stool or chair?</b> The Lesson Book and app say "stool"; the REMEMBER lines (Lesson Book pages 2 and 8) and Workbook pages 2, 3, 6 and 7 say "chair".', 'Use "stool" everywhere.'),
    ('A6', '<b>Finger 4 is explained two ways.</b> Lesson Book page 6: "tendons tie finger 4 to both 3 and 5". Page 7: "fingers 3 and 4 share a tendon".', 'One sentence in both places: "Finger 4 is tied to its neighbours by small bands between the tendons, so it is hard to lift on its own."'),
    ('A7', '<b>"Nail joint" or "tip joint"?</b> The drill and the hand-shape tool say "nail joint caving in"; the checklist says "tip joint firm".', 'Use "tip joint" everywhere.'),
    ('A8', '<b>Knuckle bridge.</b> The exercise says "press one key slowly and hold for 3", but the fix for collapsed knuckles says "tap each finger".', 'Match the exercise: press and hold.'),
    ('A9', '<b>Teacher copy page 2.</b> Check-up answers are numbered A1-4, B1-4..., but the Workbook check-up numbers them 1 to 20.', 'Use the Workbook numbers.'),
    ('A10', '<b>The "Wrist too high" drawing</b> (app, step 4) cuts off the word "wrist" at the top.', 'Make the picture a little taller.'),
    ('A11', '<b>Korean words (한국어 mode).</b> knuckle: 너클 / 마디 / 손가락 마디. forearm: 팔뚝 / 아래팔. tip joint: 손톱 마디 / 손끝 관절.', 'One word each: 마디, 아래팔, 손끝 관절.'),
]
ASK = [
    ('B1', '<b>"3 &amp; 2 - the strongest and most agile"</b> (Lesson Book page 6). The thumb is usually called the strongest finger; 2 and 3 are the most independent. Change to "2 &amp; 3 - the most independent and agile"?'),
    ('B2', '<b>Leaning forward.</b> The checklist says "back tall, leaning slightly forward" is right, but the Teacher copy page 1 lists "leaning forward" as a fault (sitting too far). How far forward is right for you?'),
    ('B3', '<b>Elbows or forearm?</b> Workbook pages 3 and 6 tick "elbows level with the keys"; everywhere else says "forearm level with the keys". The same thing for you, or should the elbow be a little above the keys?'),
    ('B4', '<b>Wrist height.</b> "A little above the keys, level with the forearm, nearly as high as the knuckles." Is that how you teach it?'),
    ('B5', '<b>Finger nicknames:</b> Captain Thumb, Pointer, Tall Middle, Shy Ring, Baby Pinky. Keep them, or the names you use?'),
    ('B6', '<b>Workbook page 6, Spot the difference.</b> Can a child see all 5 mistakes? Flat fingers are very small in the picture.'),
    ('B7', '<b>Lesson step 3, Feel the arm weight</b> (gravity, the chain from shoulder to fingertip). Right for the very first chapter, or too much?'),
    ('B8', '<b>Your name on the public page.</b> May it say "Written by Sohyun, a piano teacher in Sydney"? Another name, or no name?'),
]

def found():
    a = ''.join(f'<div class="item"><div class="id">{i}</div><div><div class="t">{t}</div><div class="fx">Fix: {fx}</div></div><div class="tick"><span></span>Fix<br><span></span>Leave it</div></div>' for i, t, fx in FIX)
    b = ''.join(f'<div class="item yel"><div class="id">{i}</div><div><div class="t">{t}</div><div class="ans"></div></div><div></div></div>' for i, t in ASK)
    p1 = page(f'<h2>A. Mistakes I found</h2><p class="sub" style="margin:0 0 2mm">I will fix these once you tick Fix. Leave it means keep it as it is.</p>{a}', 'page 2')
    p2 = page(f'<h2>B. Please decide</h2><p class="sub" style="margin:0 0 2mm">Teaching questions only you can answer. A word or two on the line is enough.</p>{b}', 'page 3')
    return [p1, p2]

SIT = [('Just right', 'Forearm level with the keys, elbows just in front of the body. That is the set-up.'),
       ('Stool too low', 'The forearm slopes up to the keys and the shoulders hunch. Raise the stool.'),
       ('Stool too high', 'The forearm slopes down onto the keys. Lower the stool until the forearm is level.'),
       ('Too close', 'The elbows are tucked behind the body and the arms are cramped. Slide the stool back a little.'),
       ('Too far', 'The arms reach out ahead of the body. Slide the stool closer.')]
HAND = [('The good shape', 'Knuckles make a bridge, the wrist is level with the forearm, and the finger plays on its tip.'),
        ('Flat fingers', 'The finger lies flat. Hold a small ball, then keep that round shape on the keys.'),
        ('Knuckles collapsed', 'The knuckles are lower than the wrist. Rebuild the bridge: tap each finger while the knuckles stay up.'),
        ('Nail joint caving in', 'The last joint bends backwards. Play slowly on the tip and keep it firm like a little pillar.'),
        ('Wrist dropped', 'The wrist sinks below the keys. Float it up, level with the forearm, like a balloon.'),
        ('Wrist too high', 'The wrist is hunched up. Let it sink until elbow, wrist and knuckle make a straight line.')]

def drill():
    why = ''.join(f'<p><b>Level 1 · {html.escape(a)}.</b> {html.escape(b)}</p>' for a, b in SIT) + ''.join(f'<p><b>Level 2 · {html.escape(a)}.</b> {html.escape(b)}</p>' for a, b in HAND)
    inner = f'''<h2>The online drill</h2>
<p class="sub" style="margin:0">Three levels, 10 questions each. After each answer the child sees one line of explanation. Every explanation is below.</p>
<div class="grid3">
<div><img src="dq1.png"><div class="cap">Level 1 · Is the stool set up right?</div></div>
<div><img src="dq2.png"><div class="cap">Level 2 · Spot the hand-shape fault</div></div>
<div><img src="dq3.png"><div class="cap" style="color:#e4572e">Level 3 · Which finger? The numbers give the answer away (A1)</div></div>
</div>
<div class="why">{why}<p><b>Level 3.</b> A left or right hand with one finger lit; the child taps 1 to 5.</p></div>'''
    return page(inner, 'page 4')

if __name__ == '__main__':
    import json, sys
    toc = json.load(open('toc.json')) if os.path.exists('toc.json') else []
    open('front.html', 'w').write(doc([cover(toc)] + found() + [drill()]))
    print('front.html written')
