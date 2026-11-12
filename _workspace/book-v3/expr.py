# The Piano Butler Handbook, Part III: Expression (her 8 Nov: "put in everything, in order; tell me when the Handbook is done").
# Loud and soft, touch, speed words, pedals, ornaments, tips. Helpers come from the Time draft (book10.py).
import json as _ej, re as _er
exec(open('/tmp/claude-0/pk/book10.py').read())   # helpers, css, page(), assemble() (rewrites the Time draft, harmless)
from openart import opener_art as _oa
EV = json.load(open('/tmp/claude-0/pk/ex/eout.json'))
def epage(inner, n): return page(inner, n, 'PART III · EXPRESSION')
def ex(k, h=80, cap='', red=()):   # an expression snippet on a real staff; red: note ids to colour
    s = EV[k].replace('<svg ', f'<svg style="max-height:{h}px" ', 1)
    for n in red:
        for c in ('note', 'rest', 'chord'): s = s.replace(f'<g id="{n}" class="{c}">', f'<g id="{n}" class="{c}" style="fill:#e4572e;color:#e4572e">', 1)
    return '<figure class="vx"><div class="vs">' + s + '</div>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>'
N_, R_ = '#26296b', '#e4572e'
def dsym(t, fs=30, col=N_): return f'<span style="font-family:PF,serif;font-style:italic;font-weight:700;font-size:{fs}px;color:{col};letter-spacing:-.02em">{t}</span>'
SECRETS.update({'E1': 'Six steps, from a whisper to a shout: pp p mp mf f ff. <b>m</b> means half.',
                'E2': 'Curve: join. Dot: short. Line: hold. Arrow: strong.',
                'E3': 'The word at the top sets the speed; rit. brakes gently, a tempo drives off again.',
                'E4': 'Play first, then change the pedal: up and straight down again.',
                'E5': 'An ornament is a necklace on the note: it borrows the next-door notes, and the main note still lands on time.'})

# ---------- heroes ----------
def hero_ladder(w=560):
    L = [('pp', 'very soft'), ('p', 'soft'), ('mp', 'half soft'), ('mf', 'half loud'), ('f', 'loud'), ('ff', 'very loud')]
    IT = ['pianissimo', 'piano', 'mezzo-piano', 'mezzo-forte', 'forte', 'fortissimo']
    o = f'<svg viewBox="0 0 600 244" style="width:100%;max-width:{w}px;height:auto;display:block;margin:0 auto">'
    for i, (s, t) in enumerate(L):
        x = 20 + i * 96; h = 30 + i * 26; y = 150 - h; col = ['#fbe1d6', '#f7c6b2', '#f3a98d', '#ef8c69', '#ea6f46', '#e4572e'][i]
        o += f'<rect x="{x}" y="{y}" width="76" height="{h}" rx="6" fill="{col}"/>'
        o += f'<text x="{x + 38}" y="190" text-anchor="middle" font-family="PF,serif" font-style="italic" font-weight="700" font-size="34" fill="{N_}">{s}</text>'
        o += f'<text x="{x + 38}" y="214" text-anchor="middle" font-family="AH,Arial" font-size="14" fill="#5a5d8f">{t}</text><text x="{x + 38}" y="234" text-anchor="middle" font-family="AH,Arial" font-size="12.5" font-weight="700" font-style="italic" fill="{N_}">{IT[i]}</text>'
    return o + '</svg>'
def fig_dyncurves():   # loudness over time: crescendo, diminuendo, sforzando, forte-piano
    o = '<svg viewBox="0 0 600 152" style="width:100%;max-width:600px;height:auto;display:block;margin:6px auto">'
    G = [('cresc.', 'M10,90 L130,20'), ('dim.', 'M10,20 L130,90'), ('sfz', 'M10,80 L50,80 L56,16 L64,80 L130,80'), ('fp', 'M10,18 L40,18 L44,82 L130,82')]
    for i, (lab, d) in enumerate(G):
        x = i * 150
        o += f'<g transform="translate({x},0)"><rect x="4" y="8" width="132" height="92" rx="8" fill="#f7f7fc" stroke="#e2ddd0"/><path d="M10,100 L10,8" stroke="#c9cbe0"/><path d="{d} L130,96 L10,96 Z" fill="#fde3d8" stroke="none"/><path d="{d}" fill="none" stroke="#e4572e" stroke-width="3.2" stroke-linejoin="round"/>'
        o += f'<text x="70" y="122" text-anchor="middle" font-family="PF,serif" font-style="italic" font-weight="700" font-size="20" fill="#26296b">{lab}</text></g>'
    return o + '<text x="300" y="146" text-anchor="middle" font-family="AH,Arial" font-size="11.5" fill="#5a5d8f">height = loudness · left to right = time</text></svg>'
def fig_droplift():   # a two-note slur: drop into the first note, lift off the second (lighter, shorter)
    o = '<svg viewBox="0 0 520 150" style="width:100%;max-width:520px;height:auto;display:block;margin:6px auto">'
    for k, x0 in enumerate((40, 290)):
        o += f'<path d="M{x0 + 20},70 Q{x0 + 85},30 {x0 + 150},70" fill="none" stroke="#26296b" stroke-width="2.4"/>'
        o += f'<ellipse cx="{x0 + 20}" cy="84" rx="13" ry="10" fill="#26296b" transform="rotate(-20 {x0 + 20} 84)"/><ellipse cx="{x0 + 150}" cy="84" rx="13" ry="10" fill="#9a9cc4" transform="rotate(-20 {x0 + 150} 84)"/>'
        o += f'<path d="M{x0 + 20},6 L{x0 + 20},46" stroke="#e4572e" stroke-width="4" marker-end="url(#dl)"/><text x="{x0 + 34}" y="24" font-family="AH,Arial" font-size="16" font-weight="700" fill="#e4572e">drop</text>'
        o += f'<path d="M{x0 + 150},50 L{x0 + 150},10" stroke="#5b6fd6" stroke-width="4" marker-end="url(#dl2)"/><text x="{x0 + 164}" y="30" font-family="AH,Arial" font-size="16" font-weight="700" fill="#5b6fd6">lift</text>'
        o += f'<rect x="{x0 + 6}" y="112" width="110" height="14" rx="4" fill="#e4572e"/><rect x="{x0 + 136}" y="112" width="40" height="14" rx="4" fill="#f6c2ad"/>'
    o += '<text x="260" y="146" text-anchor="middle" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">first note full and weighted · second lighter and shorter</text>'
    return o + '<defs><marker id="dl" viewBox="0 0 8 8" refX="4" refY="4" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#e4572e"/></marker><marker id="dl2" viewBox="0 0 8 8" refX="4" refY="4" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#5b6fd6"/></marker></defs></svg>'
def fig_ritaccel():   # rit.: the beats spread out; accel.: they close up
    o = '<svg viewBox="0 0 680 96" style="width:100%;max-width:640px;height:auto;display:block;margin:4px auto">'
    rows = [('rit.', [0, 50, 102, 158, 220, 290, 370], '#e4572e'), ('accel.', [0, 80, 150, 210, 262, 306, 344], '#5b6fd6')]
    for r, (lab, xs, col) in enumerate(rows):
        y = 26 + r * 44
        o += f'<text x="90" y="{y + 6}" text-anchor="end" font-family="PF,serif" font-style="italic" font-weight="700" font-size="20" fill="{col}">{lab}</text><line x1="110" x2="500" y1="{y}" y2="{y}" stroke="#d9d4c6" stroke-width="1.5"/>'
        o += ''.join(f'<circle cx="{120 + x}" cy="{y}" r="7" fill="{col}"/>' for x in xs)
        o += f'<text x="510" y="{y + 5}" font-family="AH,Arial" font-size="13" fill="#5a5d8f">{"beats further apart" if r == 0 else "beats closer together"}</text>'
    return o + '</svg>'
def fig_dampers():   # inside the piano: pedal up, the dampers rest on the strings (silence); pedal down, they lift (ringing)
    o = '<svg viewBox="0 0 600 190" style="width:100%;max-width:600px;height:auto;display:block;margin:6px auto">'
    for k, (x0, lab, up) in enumerate(((20, 'pedal up: dampers on the strings', False), (320, 'pedal down: dampers lifted', True))):
        for i in range(5):
            y = 70 + i * 16
            o += f'<line x1="{x0}" x2="{x0 + 260}" y1="{y}" y2="{y}" stroke="#26296b" stroke-width="2"/>'
            dy = -26 if up else -8
            o += f'<rect x="{x0 + 150}" y="{y + dy}" width="40" height="9" rx="3" fill="{"#e4572e" if up else "#9a9cc4"}"/>'
            if up: o += f'<path d="M{x0 + 205},{y} q8,-6 16,0 t16,0 t16,0" fill="none" stroke="#e4572e" stroke-width="1.6"/>'
        o += f'<text x="{x0 + 130}" y="172" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="{"#e4572e" if up else "#26296b"}">{lab}</text>'
        o += f'<text x="{x0 + 130}" y="30" text-anchor="middle" font-family="AH,Arial" font-size="13" fill="#5a5d8f">{"the strings keep vibrating" if up else "the strings are stopped"}</text>'
    return o + '</svg>'
def kb_door(letters, main, above=None, below=None, q=False, w=420):   # white keys; the main note red, its next-door notes marked
    W = 60; H = 150; n = len(letters); o = f'<svg viewBox="0 0 {n * W + 20} {H + 40}" style="width:100%;max-width:{w}px;height:auto;display:block;margin:6px auto">'
    blk = {'C', 'D', 'F', 'G', 'A'}
    for i, L in enumerate(letters):
        fill = '#e4572e' if i == main else ('#fde3d8' if i in (above, below) else '#fff')
        o += f'<rect x="{10 + i * W}" y="10" width="{W}" height="{H}" fill="{fill}" stroke="#26296b" stroke-width="1.6"/><text x="{10 + i * W + W / 2}" y="{H - 2}" text-anchor="middle" font-family="AH,Arial" font-size="17" font-weight="700" fill="{"#fff" if i == main else "#26296b"}">{"?" if q and i in (above, below) else L}</text>'
    for i, L in enumerate(letters[:-1]):
        if L in blk: o += f'<rect x="{10 + (i + 1) * W - 17}" y="10" width="34" height="92" rx="3" fill="#26296b"/>'
    for i, t in ((above, 'above'), (below, 'below')):
        if i is not None: o += f'<text x="{10 + i * W + W / 2}" y="{H + 30}" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="#e4572e">{t}</text>'
    o += f'<text x="{10 + main * W + W / 2}" y="{H + 30}" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="#26296b">main</text>'
    return o + '</svg>'
def hero_touch():
    rows = [('Legato', 'slur: joined, no gap', [(0, 1), (1, 1), (2, 1), (3, 1)], 'slur'), ('Staccato', 'dots: short, detached', [(0, .38), (1, .38), (2, .38), (3, .38)], 'dot'),
            ('Tenuto', 'lines: full length, a slight lean', [(0, .92), (1, .92), (2, .92), (3, .92)], 'line'), ('Accent', 'arrows: a stronger start', [(0, .8), (1, .8), (2, .8), (3, .8)], 'acc')]
    o = '<svg viewBox="0 0 640 250" style="width:100%;max-width:600px;height:auto;display:block;margin:0 auto">'
    o += '<text x="250" y="16" font-family="AH,Arial" font-size="12.5" font-weight="700" fill="#5a5d8f">how long each of four notes sounds</text>'
    for r, (n, d, bars, mark) in enumerate(rows):
        y = 34 + r * 54
        o += f'<text x="0" y="{y + 18}" font-family="AH,Arial" font-size="16" font-weight="700" fill="{N_}">{n}</text><text x="0" y="{y + 36}" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">{d}</text>'
        for k, ln in bars:
            x = 250 + k * 96; hh = 26 if mark != 'acc' else 22
            if mark == 'acc':
                o += f'<path d="M{x},{y + 4} L{x + 14},{y + 4} L{x + ln * 92},{y + 16} L{x + ln * 92},{y + 26} L{x},{y + 26} Z" fill="{R_}"/>'
            else:
                o += f'<rect x="{x}" y="{y + 4}" width="{ln * 96 - (0 if mark == "slur" else 4):.0f}" height="{hh - 4}" rx="{3 if mark == "slur" else 4}" fill="{R_ if mark != "line" else "#f08b6b"}"/>'
        if mark == 'slur': o += f'<path d="M252,{y} Q442,{y - 22} 632,{y}" fill="none" stroke="{N_}" stroke-width="2"/>'
    return o + '</svg>'
def hero_dial():
    import math
    W = ['Largo', 'Adagio', 'Andante', 'Moderato', 'Allegro', 'Presto']
    o = '<svg viewBox="0 0 560 270" style="width:100%;max-width:520px;height:auto;display:block;margin:0 auto">'
    cx, cy, R = 280, 230, 190
    o += f'<path d="M{cx - R},{cy} A{R},{R} 0 0 1 {cx + R},{cy}" fill="none" stroke="#e3e1ee" stroke-width="30"/>'
    o += f'<path d="M{cx - R},{cy} A{R},{R} 0 0 1 {cx + R * math.cos(math.radians(180 - 72)):.1f},{cy - R * math.sin(math.radians(180 - 72)):.1f}" fill="none" stroke="#f6c2ad" stroke-width="30"/>'
    for i, w in enumerate(W):
        a = math.radians(180 - (i + .5) * 180 / len(W)); x = cx + (R + 34) * math.cos(a); y = cy - (R + 34) * math.sin(a)
        o += f'<text x="{x:.1f}" y="{y + 5:.1f}" text-anchor="middle" font-family="PF,serif" font-weight="700" font-size="17" fill="{R_ if w == "Andante" else N_}">{w}</text>'
        x1, y1 = cx + (R - 15) * math.cos(a), cy - (R - 15) * math.sin(a); x2, y2 = cx + (R + 15) * math.cos(a), cy - (R + 15) * math.sin(a)
        o += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#fff" stroke-width="3"/>'
    a = math.radians(180 - 2.5 * 180 / len(W))
    o += f'<line x1="{cx}" y1="{cy}" x2="{cx + (R - 30) * math.cos(a):.1f}" y2="{cy - (R - 30) * math.sin(a):.1f}" stroke="{R_}" stroke-width="6" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="13" fill="{N_}"/>'
    o += f'<text x="{cx - R}" y="{cy + 30}" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="#5a5d8f">slow</text><text x="{cx + R}" y="{cy + 30}" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="#5a5d8f">fast</text>'
    return o + '</svg>'
def pedals(q=False, w=520):
    P3 = [('soft pedal', 'una corda', 'softer, gentler'), ('middle pedal', 'sostenuto', 'holds only some notes'), ('sustain pedal', 'damper pedal', 'notes keep ringing')]
    o = f'<svg viewBox="0 0 520 220" style="width:100%;max-width:{w}px;height:auto;display:block;margin:0 auto">'
    o += '<rect x="20" y="20" width="480" height="26" rx="4" fill="#26296b"/><rect x="60" y="46" width="400" height="60" fill="#3a3d7e"/>'
    for i, (a, b, c) in enumerate(P3):
        x = 110 + i * 150; col = R_ if i == 2 else '#c9cbe0'
        o += f'<line x1="{x}" y1="106" x2="{x}" y2="120" stroke="#3a3d7e" stroke-width="6"/><path d="M{x - 26},{124} Q{x},{112} {x + 26},{124} L{x + 22},{142} Q{x},{136} {x - 22},{142} Z" fill="{col}" stroke="#26296b" stroke-width="2"/>'
        if q: o += f'<circle cx="{x}" cy="178" r="15" fill="#fff3ee" stroke="{R_}" stroke-width="2"/><text x="{x}" y="184" text-anchor="middle" font-family="AH,Arial" font-size="16" font-weight="700" fill="{R_}">?</text>'
        else: o += f'<text x="{x}" y="166" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="{R_ if i == 2 else N_}">{a}</text><text x="{x}" y="184" text-anchor="middle" font-family="AH,Arial" font-size="12.5" font-style="italic" fill="#5a5d8f">{b}</text><text x="{x}" y="202" text-anchor="middle" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">{c}</text>'
    return o + '</svg>'
def pedmarks():   # the two ways to write the sustain pedal
    o = '<svg viewBox="0 0 520 96" style="width:100%;max-width:480px;height:auto;display:block;margin:0 auto">'
    o += f'<text x="10" y="30" font-family="PF,serif" font-style="italic" font-weight="700" font-size="20" fill="{N_}">Ped.</text><path d="M62,24 H200" stroke="#9a9cc4" stroke-dasharray="5 4" stroke-width="1.5"/><text x="208" y="32" font-family="AH,Arial" font-size="24" font-weight="700" fill="{N_}">*</text>'
    o += f'<text x="10" y="58" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">down at Ped., up at the star</text>'
    o += f'<path d="M290,12 V34 H380 L392,18 L404,34 H490 V12" fill="none" stroke="{N_}" stroke-width="2.2"/>'
    o += f'<text x="290" y="58" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">a bracket: the notch is a quick change</text>'
    o += f'<text x="380" y="84" font-family="AH,Arial" font-size="12" font-weight="700" fill="{R_}">up and down again</text><line x1="392" y1="22" x2="392" y2="70" stroke="{R_}" stroke-width="1.2" stroke-dasharray="2 2"/>'
    return o + '</svg>'
def pedsign(kind):   # her 11 Nov: the pedal is written in several ways; each drawn small, the same width
    o = '<svg viewBox="0 0 220 40" style="width:100%;max-width:150px;height:auto;display:block">'
    P = lambda x, y: f'<text x="{x}" y="{y}" font-family="PF,serif" font-style="italic" font-weight="700" font-size="17" fill="{N_}">Ped.</text>'
    S = lambda x, y: f'<text x="{x}" y="{y}" font-family="AH,Arial" font-size="22" font-weight="700" fill="{N_}">*</text>'
    if kind == 'star': o += P(4, 28) + f'<path d="M50,22 H170" stroke="#9a9cc4" stroke-dasharray="5 4" stroke-width="1.5"/>' + S(178, 31)
    elif kind == 'each': o += P(4, 28) + S(64, 31) + P(80, 28) + S(140, 31) + P(156, 28)
    elif kind == 'bracket': o += f'<path d="M8,10 V30 H212 V10" fill="none" stroke="{N_}" stroke-width="2.2"/>'
    elif kind == 'notch': o += f'<path d="M8,10 V30 H66 L76,14 L86,30 H134 L144,14 L154,30 H212 V10" fill="none" stroke="{N_}" stroke-width="2.2"/>'
    elif kind == 'words': o += f'<text x="4" y="28" font-family="PF,serif" font-style="italic" font-weight="700" font-size="17" fill="{N_}">con Ped. · senza Ped.</text>'
    elif kind == 'simile': o += P(4, 28) + f'<text x="50" y="28" font-family="PF,serif" font-style="italic" font-weight="700" font-size="17" fill="{N_}">simile</text>'
    return o + '</svg>'
PEDWAYS = [('star', '<b>Ped.</b> … <b>*</b>', 'down at Ped., up at the star'), ('each', '<b>* Ped.</b> under each chord', 'every new Ped. is a change: up, and straight down'),
           ('bracket', 'a line with two hooks', 'down where it starts, up where it ends'), ('notch', 'a line with notches', 'each notch is a change: up and down again'),
           ('words', '<i>con Ped.</i> · <i>senza Ped.</i>', 'with the pedal (you choose the changes) · without the pedal'), ('simile', '<i>Ped. simile</i>', 'go on pedalling the same way')]
def pedtime(w=520):   # keys and pedal on one timeline: the pedal changes just after each new chord
    o = f'<svg viewBox="0 0 540 120" style="width:100%;max-width:{w}px;height:auto;display:block;margin:0 auto">'
    o += f'<text x="0" y="34" font-family="AH,Arial" font-size="13" font-weight="700" fill="{N_}">hands</text><text x="0" y="88" font-family="AH,Arial" font-size="13" font-weight="700" fill="{N_}">pedal</text>'
    for i, c in enumerate(['C E G', 'F A C', 'G B D', 'C E G']):
        x = 70 + i * 116
        o += f'<rect x="{x}" y="18" width="104" height="26" rx="5" fill="#f6c2ad"/><text x="{x + 52}" y="36" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="{N_}">{c}</text>'
    d = 'M70,96 V74'
    for i in range(1, 4): x = 70 + i * 116; d += f' H{x + 6} L{x + 14},96 L{x + 22},74'
    d += ' H534 V96'
    o += f'<path d="{d}" fill="none" stroke="{R_}" stroke-width="2.6"/>'
    for i in range(1, 4): x = 70 + i * 116; o += f'<line x1="{x}" y1="46" x2="{x}" y2="70" stroke="#9a9cc4" stroke-dasharray="2 2"/>'
    return o + '<text x="300" y="116" text-anchor="middle" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">each notch comes just <tspan font-weight="700">after</tspan> the new group of notes</text></svg>'
def arrow_pair(a, b, lab=''):
    return (f'<div style="display:grid;grid-template-columns:1fr 60px 1.4fr;align-items:center;gap:6px">{a}<div style="text-align:center;font-family:CV,cursive;font-size:20px;font-weight:700;color:{R_};line-height:1">→<br><span style="font-size:15px">{lab}</span></div>{b}</div>')
def qdot(n=1): return '<span style="display:inline-flex;gap:6px">' + ''.join(f'<span style="width:30px;height:30px;border-radius:50%;background:#fff3ee;border:2px solid {R_};color:{R_};font:700 16px AH,Arial;display:inline-flex;align-items:center;justify-content:center">?</span>' for _ in range(n)) + '</span>'

# ---------- 1 · Loud and soft ----------
DYN = [[dsym('pp'), '<b>pianissimo</b>', 'very soft'], [dsym('p'), '<b>piano</b>', 'soft'], [dsym('mp'), '<b>mezzo-piano</b>', 'half soft: a little louder than <i>p</i>'],
       [dsym('mf'), '<b>mezzo-forte</b>', 'half loud: a little softer than <i>f</i>'], [dsym('f'), '<b>forte</b>', 'loud'], [dsym('ff'), '<b>fortissimo</b>', 'very loud']]
CHG = [['<svg viewBox="0 0 90 30" style="width:80px"><path d="M4,15 L86,4 M4,15 L86,26" stroke="#26296b" stroke-width="2" fill="none"/></svg>', '<b>crescendo</b> (<i>cresc.</i>)', 'getting louder, little by little'],
       ['<svg viewBox="0 0 90 30" style="width:80px"><path d="M4,4 L86,15 L4,26" stroke="#26296b" stroke-width="2" fill="none"/></svg>', '<b>diminuendo</b> (<i>dim.</i>, <i>decresc.</i>)', 'getting softer, little by little'],
       [dsym('sfz', 24) + ' / ' + dsym('sf', 24), '<b>sforzando</b>', 'one note made suddenly strong'], [dsym('fp', 24), '<b>forte-piano</b>', 'loud, then soft at once'], ['<i>subito p</i>', '<b>subito</b>', '“suddenly”: <i>subito p</i>, suddenly soft']]
E1 = epage(f'''{head('Part III · Expression · 1', 'Loud and soft', 'A voice can whisper, chat or shout. Music does the same, and small Italian words tell you which: the <b>dynamics</b>. They sit under the notes, shortened to one or two letters.')}
{hero(hero_ladder(), 'Six steps from a whisper to a shout')}
<div class="xlate">{rule('A sign lasts until the next one: <i>p</i> stays soft until a new sign arrives.')}</div>
{inact('Which is louder: mp or mf?', qtagT('<div style="display:flex;gap:34px;align-items:baseline;justify-content:center">' + dsym('mp', 44) + dsym('mf', 44) + '</div>'), ['<b>m means half.</b> Half of what?', '<b>p is soft, f is loud.</b>', '<b>So which half</b> is louder?'], '<b>mf</b>, half loud, is louder than <b>mp</b>, half soft. Both sit in the middle of the ladder.')}
<div class="xlate">{h3('Growing and fading')}{ex('e_words', 100, 'In words: <i>cresc.</i> and dots, then <i>ff</i>. A hairpin that opens does the same; one that closes fades.')}</div>
<div class="xlate">{tbl(['Sign', 'Name', 'What you do'], CHG, ['22%', '34%', '44%'])}{fig_dyncurves()}</div>
{inact('One strong note, or loud then soft?', two(ex('e_sfz', 100, 'A'), ex('e_fp', 100, 'B')), ['<b>Find the sign</b> under each tune.', '<b>sfz</b>: one note made suddenly strong; the music goes on as before.', '<b>fp</b>: loud for an instant, then soft at once.'], 'A is <b>sfz</b>: one strong note, then back to the music around it. B is <b>fp</b>: strike loud, and the next moment soft.')}
{inact('What happens across the hairpins?', qtagT(ex('e_tw_hair', 120), 560), ['<b>Find the start:</b> which sign?', '<b>The first hairpin opens</b> to which sign?', '<b>The second hairpin closes.</b> What happens?'], 'Start <i>p</i>, grow through bar 1 into <i>f</i>, then <b>fade</b> through bar 2.')}
{inact('Where is the loudest note?', qtagT(ex('e_tw_q', 120), 660), ['<b>Start:</b> <i>mp</i>.', '<b>Follow the hairpin</b> to its sign.', '<b>Then the long hairpin closes</b> to which sign?'], 'The <b>first A in bar 2</b>, at <i>f</i>. From the next note the tune fades all the way to <i>p</i>.')}
<!--SPLIT-->
{try10('<div style="text-align:center">' + dsym('pp', 30) + ' <span style="font:700 22px CV;color:#e4572e">→</span> ' + dsym('ff', 30) + '</div>', 'One note, six ways.', 'Play Middle C <i>pp</i>, then <i>p</i>, <i>mp</i>, <i>mf</i>, <i>f</i>, <i>ff</i>: six different steps, using the weight of your arm. Then come back down.')}
{howto('Practise a crescendo', ['<b>Play five notes up</b>, C to G, all <i>p</i>.', '<b>Now grow</b> one step on each note: <i>p</i> to <i>f</i>.', '<b>Come back down</b> the same notes, fading to <i>p</i>, without slowing down.'])}
{youknow('Haydn’s “Surprise” Symphony', ex('y_surprise', 70, red=('n1',)), 'The tune tiptoes along softly, <i>p</i>, then comes again even softer. Just as everyone relaxes, the whole orchestra crashes in with one <b class="co">ff</b> chord: the surprise that gave the symphony its name.', 'Hum it very softly, then clap once, as loud as you can.')}
{thinkt('Dynamics are a volume knob with six clicks. Turn it with the weight of your arm, not by hitting harder.')}
{watch(['Playing everything <i>mf</i>: each sign is a different step.', 'Speeding up in a crescendo: louder is not faster.'])}
{foot('Touch p. {{E2}} · Pulse, tempo and the bar p. {{T1}}', 'Online: Library › Dynamics')}''', 72)

# ---------- 2 · Touch ----------
MARKS = [['<span style="font-size:26px;color:#26296b">⌒</span>', '<b>slur</b> (<i>legato</i>)', 'join the notes smoothly, no gap'], ['<span style="font-size:30px;color:#26296b;line-height:.5">•</span>', '<b>staccato</b>', 'short and detached: let go early'],
         ['<span style="font-size:22px;font-weight:700;color:#26296b">—</span>', '<b>tenuto</b>', 'hold the full length, leaning a little'], ['<span style="font-size:24px;font-weight:700;color:#26296b">&gt;</span>', '<b>accent</b>', 'a stronger start to the note'],
         ['<span style="font-size:18px;color:#26296b">▼</span>', '<b>staccatissimo</b>', 'very short ' + lv('')], ['<span style="font-size:22px;font-weight:700;color:#26296b">^</span>', '<b>marcato</b>', 'very strong, marked ' + lv('')]]
E2 = epage(f'''{head('Part III · Expression · 2', 'Touch: smooth, short, strong', 'The same four notes can sound smooth or bouncy, gentle or strong. Small marks above or below the notes tell your fingers how to touch the keys: this is <b>articulation</b>.')}
{hero(hero_touch(), 'Same notes, four touches')}
<div class="xlate">{ex('a_four', 90, 'The same four notes: slurred, staccato, tenuto, accented.')}{tbl(['Mark', 'Name', 'How to play'], MARKS, ['14%', '32%', '54%'])}</div>
{inact('Line, dot or arrow?', qtagT(ex('a_tenq', 110), 560), ['<b>The first two Cs have lines:</b> how long?', '<b>The Gs have dots.</b>', '<b>The E in bar 2</b> has an arrow.'], 'The first two Cs held their <b>full length</b>, the Gs short, the E strong, and the last C plain, held for its two beats.')}
<!--SPLIT-->
<div class="xlate">{h3('Slurs and phrases')}{two(ex('a_legato', 96, 'Slurred: join E D C, then a tiny lift.'), ex('a_stacc', 96, 'Staccato: every E and D let go early.'))}<p>A curve over <b>different</b> notes is a slur: join them, then lift at its end, like a breath. A long slur over a whole line of tune is a <b>phrase mark</b>: one musical sentence. (A curve joining the <b>same</b> note twice is a tie, p. {{{{T3}}}}.)</p>{youknow('Ode to Joy (Beethoven)', ex('a_ode', 84), 'Two long slurs: two musical sentences. Lift your hand <b class="co">only</b> at the end of each one, like a singer taking a breath.', 'Sing it and breathe only where the slurs end.')}</div>
{inact('Which notes are short?', qtagT(ex('a_mixq', 110), 560), ['<b>Bar 1:</b> what does the curve ask?', '<b>Bar 2:</b> find the dots.', '<b>The last G</b> has a different mark: which?'], 'Bar 1 is joined; the <b>two dotted Gs are short</b>; the third G is accented, stronger but full length.')}
<div class="xlate">{h3('Two-note slurs')}{two(ex('a_two', 96), '<p>A slur over just two notes is a little sigh: <b>drop</b> into the first note, then <b>lift</b> off the second, lighter and a little shorter. Drop, lift.</p>')}{fig_droplift()}</div>
<!--SPLIT-->
<div class="xlate">{h3('Mood words')}<p>Some words describe the mood, not the speed.</p>{tbl(['Word', 'Meaning', 'Word', 'Meaning'], [['<i>dolce</i>', 'sweetly', '<i>leggiero</i>', 'lightly'], ['<i>cantabile</i>', 'in a singing style', '<i>espressivo</i>', 'with feeling'], ['<i>legato</i>', 'smoothly', '<i>grazioso</i>', 'gracefully'], ['<i>maestoso</i>', 'majestically', '<i>con moto</i>', 'with movement']], ['20%', '30%', '20%', '30%'])}</div>
{howto('Practise touch', ['<b>Play one bar</b> of a piece three ways: all legato, all staccato, then as written.', '<b>Listen:</b> can someone else hear which way was which?'])}
{thinkt('Legato is walking: one foot leaves the ground as the other lands. Staccato is hopping on hot sand.')}
{watch(['Making staccato loud: short is not the same as strong.', 'Lifting in the middle of a slur: keep every note joined until the curve ends.'])}
{foot('Loud and soft p. {{E1}} · Tie or slur? p. {{T3+2}}', 'Online: Library › Articulation')}''', 75)

# ---------- 3 · Speed words ----------
TEMPI = [['<b>Largo</b>', 'very slow and broad', '40–60'], ['<b>Lento</b>', 'slow', '45–60'], ['<b>Adagio</b>', 'slow, at ease', '60–76'], ['<b>Andante</b>', 'at a walking pace', '76–108'], ['<b>Moderato</b>', 'at a moderate speed', '108–120'],
         ['<b>Allegretto</b>', 'fairly fast, a little slower than Allegro', '112–120'], ['<b>Allegro</b>', 'fast and lively', '120–156'], ['<b>Vivace</b>', 'lively and brisk', '156–176'], ['<b>Presto</b>', 'very fast', '168–200']]
CHANGE = [['<i>rit.</i> (ritardando), <i>rall.</i> (rallentando)', 'gradually slower'], ['<i>accel.</i> (accelerando)', 'gradually faster'], ['<i>a tempo</i>', 'back to the speed before'],
          ['<svg viewBox="0 0 40 26" style="width:32px"><path d="M4,22 A16,16 0 0 1 36,22" fill="none" stroke="#26296b" stroke-width="3"/><circle cx="20" cy="19" r="3" fill="#26296b"/></svg> fermata (pause)', 'hold longer than written, then go on'],
          ['<i>poco a poco</i>', 'little by little'], ['<i>molto</i> · <i>poco</i> · <i>più</i> · <i>meno</i>', 'very · a little · more · less (<i>più mosso</i>: faster; <i>meno mosso</i>: slower)'], ['<i>rubato</i>', 'time borrowed and paid back (p. {{T7+1}}) ' + lv('')]]
E3 = epage(f'''{head('Part III · Expression · 3', 'Speed words', 'How fast is the beat? A word at the top of the music tells you, usually in Italian, and often a number too. Other words inside the music ask you to slow down, speed up, or wait.')}
{hero(hero_dial(), 'Andante: the speed of walking')}
<div class="xlate">{tbl(['Word', 'Meaning', 'About (beats a minute)'], TEMPI, ['24%', '46%', '30%'], 'nt')}<p class="sm">The numbers are a rough guide: the music and the room decide the rest.</p></div>
<!--SPLIT-->
<div class="xlate">{h3('The metronome mark')}{two(ex('t_mark', 96), '<p><b>♩&nbsp;=&nbsp;76</b> means 76 crotchet beats in one minute. Set a metronome to 76: each click is one beat. The word tells you the character; the number pins down the speed.</p>')}</div>
{inact('How fast is ♩ = 60?', qtagT('<div style="font:700 40px PF,serif;color:#26296b;text-align:center">♩ = 60</div>'), ['<b>60 beats</b> in one minute.', '<b>How many seconds</b> are there in a minute?', '<b>So one beat</b> lasts how long?'], 'One beat every <b>second</b>: tick, tick, like a clock.')}
<div class="xlate">{h3('Changing speed')}{tbl(['Word or sign', 'What you do'], CHANGE, ['48%', '52%'])}{fig_ritaccel()}{two(ex('t_rit', 84, '<i>rit.</i>: slow down into the end, then wait on the fermata.'), ex('t_accel', 84, '<i>accel.</i>: speed up, little by little, to the end.'))}</div>
{inact('Where does it slow down, and where does it come back?', qtagT(ex('t_atempo', 110), 560), ['<b>Find rall.</b> Which notes does it slow?', '<b>Find a tempo.</b>', '<b>What speed</b> does a tempo mean?'], 'Bar 1 slows into the two Gs; at <b>a tempo</b> (bar 3) the first speed comes straight back.')}
{inact('How long do you hold the fermata?', qtagT(ex('t_ferm', 110, red=('n5',)), 560), ['<b>The minim</b> is worth how many beats?', '<b>The fermata</b> asks for more. How much?', '<b>Then what?</b>'], 'Longer than 2 beats: hold until it <b>feels finished</b>, often half as long again or more, then go on.')}
<!--SPLIT-->
{youknow('Twinkle, Twinkle, Little Star', ex('y_tw_rit', 66, red=('n7',)), 'Players often slow down into the last “are”: a <b class="co">rit.</b>, then a fermata on the final C. The ending feels like coming home.', 'Sing the last line twice: once in time, once with a rit.')}
{thinkt('A rit. is a car braking gently at the lights; a tempo is driving off again at the same speed as before.')}
{watch(['Taking Andante as slow: it is a walking pace.', 'Slowing down all at once at rit.: slow little by little.', 'Forgetting a tempo: after a rit., the first speed comes back exactly.'])}
{foot('Pulse, tempo and the bar p. {{T1}} · Rubato p. {{T7+2}}', 'Online: Metronome')}''', 78)

# ---------- 4 · The pedals ----------
OTHER = [['<b>left</b>', 'soft pedal: <i>una corda</i>, written <i>u.c.</i>', 'a softer, gentler sound; lift it at <i>t.c.</i> (<i>tre corde</i>)'], ['<b>middle</b>', '<i>sostenuto</i> ' + lv(''), 'holds only the notes already down (on many uprights: a practice mute)'], ['<b>right</b>', 'sustain (damper) pedal: <i>Ped.</i>', 'every note keeps ringing until you lift it']]
E4 = epage(f'''{head('Part III · Expression · 4', 'The pedals', 'Most pianos have three pedals. The right one, the <b>sustain pedal</b>, lifts every damper off the strings, so notes keep ringing after your fingers let go. The left one makes the sound softer.')}
{hero(pedals(), 'Right pedal: the notes keep ringing')}
<div class="xlate">{h3('What the sustain pedal does')}{fig_dampers()}<p class="sm">Each string has a felt damper resting on it. Let go of a key and its damper stops the string. The sustain pedal lifts every damper at once, so the strings ring on.</p></div>
<div class="xlate">{tbl(['Pedal', 'Name and sign', 'What it does'], OTHER, ['14%', '40%', '46%'])}</div>
{inact('Which pedal?', pedals(True, 340), ['<b>Ped.</b>: which foot pedal?', '<b>u.c.</b>: which one?', '<b>t.c.</b>: what do you do?'], 'Ped. is the <b>right</b> pedal; <i>u.c.</i> the <b>left</b> one; <i>t.c.</i> means let the left pedal up.')}
<div class="xlate">{h3('Writing the sustain pedal')}<p class="sm">Down at <b>Ped.</b>, up at the star, or a line with hooks; six ways are on p. {{{{E4+2}}}}.</p>{rule('Heel on the floor, press with the ball of your foot. <b>Play first, then pedal</b>: new notes, then up and straight down again.')}</div>
{inact('Where does the pedal go down, and where does it come up?', qtagT(ex('p_pedq', 110), 560), ['<b>Find Ped.</b> under the first C.', '<b>Find the next sign:</b> a star with Ped.', '<b>Find the last star.</b>'], 'Down on the first C, <b>changed</b> at the first F (up and down again), and up at the end: each bar rings as one sound.')}
<!--SPLIT-->
<div class="xlate">{h3('Changing the pedal')}{pedtime()}<p class="sm">A chord is three or more notes played together. Play each new chord first, then change the pedal straight away.</p></div>
<!--SPLIT-->
<div class="xlate">{h3('Six ways to write the pedal')}{tbl(['How it looks', 'Its name', 'What your foot does'], [[pedsign(k), n, d] for k, n, d in PEDWAYS], ['38%', '28%', '34%'], 'pedw')}</div>
<div class="xlate">{extra('Half pedal and the middle pedal', '<p><b>Half pedal:</b> lift the pedal only part of the way, to clear some of the sound but not all. <b>Sostenuto</b> (the middle pedal on grand pianos): press it while notes are held, and only those notes keep ringing.</p>')}</div>
{try10('<div style="font:italic 700 44px PF,serif;color:#26296b;text-align:center">Ped.</div>', 'Hear the ringing.', 'Play C, E and G together, press the right pedal and take your hands off: the chord keeps sounding. Lift the pedal: silence. That is the dampers coming back down.')}
{howto('Practise the pedal change', ['<b>Without playing</b>, say “play, up-down” and move your foot on “up-down”.', '<b>Play C-E-G, then F-A-C, then G-B-D</b>, slowly. Change just after each one.', '<b>Listen</b> for a clean change with no gap of silence.'])}
{thinkt('The sustain pedal holds a door open: every note that walks in stays until the door shuts.')}
{watch(['Lifting the pedal before the new notes: a gap of silence. Play first, then change.', 'Keeping the pedal down through a new chord: muddy.'])}
{foot('Touch p. {{E2}} · Chords p. {{H1}}', 'Online: Library › Pedal')}''', 81)

# ---------- 5 · Ornaments ----------
ORN = [[ex('o_trill_w', 62), '<b>trill</b>', 'the note and the one above, back and forth quickly'], [ex('o_mord_w', 62), '<b>upper mordent</b>', 'the note, the one above, the note: one quick flick'],
       [ex('o_lmord_w', 62), '<b>lower mordent</b>', 'the note, the one below, the note'], [ex('o_turn_w', 62), '<b>turn</b>', 'above, the note, below, the note'],
       [ex('o_acc_w', 62), '<b>acciaccatura</b>', 'a tiny note with a slash: crushed in, as fast as you can'], [ex('o_app_w', 62), '<b>appoggiatura</b>', 'a tiny note, no slash: leans, taking half the main note’s time']]
E5 = epage(f'''{head('Part III · Expression · 5', 'Ornaments', 'Ornaments are decorations: a small sign that stands for a quick burst of notes around the main note. They borrow the notes <b>next door</b>, one letter name up or down: on D, the note above is E and the note below is C.')}
{hero(arrow_pair(ex('o_trill_w', 96), ex('o_trill_p', 96), 'played'), 'A small sign, a burst of notes')}
<div class="xlate">{h3('Next-door notes')}{kb_door('BCDEF', 2, above=3, below=1, w=330)}<p class="sm">Plain letters on white keys: no sharps or flats unless the music adds one.</p></div>
<div class="xlate">{h3('Written and played')}{tbl(['', 'Written', '', 'Played'], [[n, ex(w, 80), '<span style="font:700 22px CV,cursive;color:#e4572e">→</span>', ex(pl, 80)] for n, w, pl in (('<b>trill</b><br><span class="mu">the note and the one above, back and forth</span>', 'o_trill_w', 'o_trill_p'), ('<b>upper mordent</b><br><span class="mu">note, above, note: one flick</span>', 'o_mord_w', 'o_mord_p'))], ['24%', '30%', '6%', '40%'])}</div>
<div class="xlate">{tbl(['', '', '', ''], [[n, ex(w, 80), '<span style="font:700 22px CV,cursive;color:#e4572e">→</span>', ex(pl, 80)] for n, w, pl in (('<b>lower mordent</b><br><span class="mu">note, below, note</span>', 'o_lmord_w', 'o_lmord_p'), ('<b>turn</b><br><span class="mu">above, note, below, note</span>', 'o_turn_w', 'o_turn_p'))], ['24%', '30%', '6%', '40%'])}</div>
{inact('A lower mordent on G', kb_door('EFGAB', 2, above=3, below=1, q=True, w=300), ['<b>The main note</b> is G.', '<b>A lower mordent</b> borrows the note next door: above or below?', '<b>Play it:</b> main, next door, main.'], 'The note below G is <b>F</b>: <b>G F G</b>, one quick flick, then on. (A trill on G would use A, the note above.)')}
{inact('How do you play this trill?', qtagT(ex('o_q', 110, red=('n5',)), 560), ['<b>Which note</b> has the tr?', '<b>Its next-door note above</b> is…?', '<b>Go back and forth</b> for how long?'], 'On the E: <b>E F E F…</b> quickly for its two beats, then the last E on time.')}
<div class="xlate">{extra('Where does a trill start?', '<p>In music from the 1700s (Bach, Handel), a trill usually starts on the note <b>above</b>: F E F E on an E. In later music it starts on the main note. Your teacher or the edition will tell you.</p>')}</div>
<!--SPLIT-->
<div class="xlate">{h3('Tiny notes before the main note')}<p>A tiny note just before the main note borrows a moment from it. <b>With a slash</b> it is an <b>acciaccatura</b>: crushed in, as fast as you can. <b>Without a slash</b> it is an <b>appoggiatura</b>: it leans, taking about half the main note’s time.</p>{inact('Crushed, or leaning?', qtagT(two(ex('o_acc_w', 50), ex('o_app_w', 50))), ['<b>Look for the slash</b> through the tiny note.', '<b>With a slash:</b> how fast?', '<b>Without:</b> how much time does it take?'], 'Slash (acciaccatura): <b>crushed in</b>, almost at once. No slash (appoggiatura): <b>D for a crotchet</b>, then C.')}</div>
{youknow('Minuet in G (Notebook for Anna Magdalena Bach)', ex('o_minuet', 76, red=('n1',)), 'Here the first D is decorated with a <b class="co">mordent</b>: D, E, D, one quick flick, then the music walks on in time. The flick borrows from the D; the beat does not move.', 'Play the first bar with the mordent, then without it: hear the sparkle it adds.')}
{thinkt('Ornaments are like accessories: a necklace or a hair clip makes you look lovely, but you get dressed first. Learn the plain notes in time, then add the ornament.')}
{howto('Practise an ornament', ['<b>Play the main notes</b> alone first, in time; then <b>add the ornament slowly</b>, as written-out notes.', '<b>Speed it up</b> bit by bit, keeping the main note on the beat.'])}
{watch(['Starting a trill, mordent or turn before the beat: it begins on the beat. (Only the crushed acciaccatura slips in just before.)'])}
{foot('The keyboard p. {{P1}} · Sharps, flats and naturals p. {{P6}}', 'Online: Library › Ornaments')}''', 84)

# ---------- Tips ----------
ET = epage(f'''{head('Part III · Expression · Tips', 'When your playing sounds flat', 'Every note can be right and the music still sound flat. The fix is almost always one sign you read but did not play. Find what you notice, then check that one thing.')}
{box('Tip', '<b class="it">What you notice, what to check</b>' + tbl(['What you notice', 'Check', 'Turn to'], [['Everything is the same loudness', '<b>the dynamics:</b> is every sign a different step?', 'p. {{E1}}'], ['The tune sounds choppy', '<b>the slurs:</b> join every note inside the curve', 'p. {{E2}}'], ['Short notes sound heavy', '<b>staccato</b> is short, not loud', 'p. {{E2}}'], ['The end feels rushed', '<b>rit. and fermata:</b> slow little by little, then wait', 'p. {{E3}}'], ['The sound is muddy', '<b>the pedal:</b> change on each new chord', 'p. {{E4}}'], ['The ornament trips the beat', '<b>the main note</b> lands on time; practise it slowly', 'p. {{E5}}']], ['38%', '48%', '14%']))}
{h3('Four ways to bring music to life')}
<div class="fixes">{''.join(f'<div><span class="rn">{i + 1}</span><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate([('Sing it first', 'Sing the phrase: your voice shapes it naturally. Then copy your voice on the keys.'), ('Exaggerate', 'Play the dynamics twice as big as you think. It always sounds smaller to the listener.'), ('Record yourself', 'Listen back with the music: did each sign really happen?'), ('Shape every phrase', 'Grow towards the most important note, then let the phrase fall away.')]))}</div>
{inact('Give this phrase a shape', qtagT(ex('e_tw_bare', 80, red=('n5',))), ['<b>Sing it:</b> where does it want to go?', '<b>Which note</b> feels like the top of the hill?', '<b>Where</b> would you start soft and end soft?'], 'Start soft, grow to the first A, then fade: <b>a phrase is a hill</b>, up and down.')}
{thinkt('Expression is the difference between reading a story aloud and telling it.')}''', PM.PAGE['ET'])

EOPEN = _oa('Part III · How it should sound', 'Expression', 'The notes say <b>what</b> to play; expression says <b>how</b>: loud or soft, smooth or short, faster or slower, ringing or dry. Everything in this part is in these three bars.', 'E', PM.PAGE)
_ebody = ''.join(assemble(f'E{_i + 1}', _pg) for _i, _pg in enumerate((E1, E2, E3, E4, E5))) + ET
ehtml = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{OPENCSS} .pedw td{{padding-top:3px!important;padding-bottom:3px!important;font-size:14px!important;line-height:1.3}}</style></head><body>{EOPEN}{_ebody}{FLOWJS}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-expression.html', 'w').write(ehtml)
print('ok expression')
