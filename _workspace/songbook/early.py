# The first lessons (her 4 Nov 10:54 and 12:02). Before any song, two "Getting ready" pages: the hands and their numbers,
# sitting at the piano, the black keys in twos and threes, high and low. Then each early lesson's page 3 is "Play it".
# Run inside lesson.py (exec), so page, part, mus, ticks, N, C and MUTE are its own.

def hands(maxw=300):   # both hands from above, palms down: the left hand's thumb on its right, the right hand's on its left
    def hand(x0, left):
        L = [(1, 40), (2, 64), (3, 72), (4, 66), (5, 50)]   # thumb to little finger: number and length
        out = f'<rect x="{x0 + 10}" y="98" width="146" height="78" rx="34" fill="#fbe3da" stroke="{N}" stroke-width="2"/>'
        for k, (f, ln) in enumerate(L):
            i = 4 - k if left else k                     # left hand: the thumb is the right-most finger
            cx = x0 + 23 + i * 30
            if f == 1: cx += 6 if left else -6
            top = 106 - ln + (30 if f == 1 else 0)
            out += f'<rect x="{cx - 12}" y="{top}" width="24" height="{ln + 22}" rx="12" fill="#fbe3da" stroke="{N}" stroke-width="2"/>'
            out += f'<circle cx="{cx}" cy="{top + 15}" r="11" fill="{C}"/><text x="{cx}" y="{top + 20}" text-anchor="middle" font-family="AH" font-weight="700" font-size="14" fill="#fff">{f}</text>'
        return out
    lab = lambda x, s: f'<text x="{x}" y="200" text-anchor="middle" font-family="AH" font-weight="700" font-size="12" letter-spacing="1.5" fill="{MUTE}">{s}</text>'
    return (f'<svg viewBox="0 0 360 208" style="width:100%;max-width:{maxw}px;display:block;margin:0 auto">'
            f'{hand(0, True)}{hand(196, False)}{lab(83, "LEFT HAND")}{lab(279, "RIGHT HAND")}</svg>')

def keys(octaves=2, colour=True, names=True, maxw=320):   # from C: the twos coral and the threes navy, or all plain to colour in
    w, H = 24, 96; n = 7 * octaves; W = n * w; out = ''
    for i in range(n): out += f'<rect x="{i * w}" y="0" width="{w}" height="{H}" rx="2" fill="#fff" stroke="{N}" stroke-width="1.2"/>'
    for i in [i for i in range(n - 1) if i % 7 in (0, 1, 3, 4, 5)]:
        fill = (C if i % 7 in (0, 1) else N) if colour else '#fff'
        out += f'<rect x="{(i + 1) * w - 7}" y="0" width="14" height="{H * 0.6}" rx="2" fill="{fill}" stroke="{N}" stroke-width="1.2"/>'
    if names:
        for i in range(0, n, 7): out += f'<text x="{i * w + w / 2}" y="{H - 8}" text-anchor="middle" font-family="AH" font-weight="700" font-size="12" fill="{N}">C</text>'
    return f'<svg viewBox="-1 -1 {W + 2} {H + 2}" style="width:100%;max-width:{maxw}px;display:block">{out}</svg>'

def blackkb(width=330, fing=None):   # F up to E: the three black keys side by side (A sharp, C sharp, D sharp) lit, with their fingers
    fing = fing or {k[:2]: str(v) for k, v in SONG.get('rh_finger', {}).items()} or {'as': '2', 'cs': '3', 'ds': '4'}
    hand = {k[:2]: v for k, v in SONG.get('hand', {}).items()}   # a song played with the hands mixed: L or R on each lit key
    whites = 'fgabcde'; w, H = 46, 150; W = len(whites) * w; out = ''
    for i, l in enumerate(whites):
        out += f'<rect x="{i * w}" y="0" width="{w}" height="{H}" rx="3" fill="#fff" stroke="{N}" stroke-width="1.5"/>'
        out += f'<text x="{i * w + w / 2}" y="{H - 12}" text-anchor="middle" font-family="AH" font-weight="700" font-size="16" fill="{MUTE}">{l.upper()}</text>'
    for i, name in [(0, 'fs'), (1, 'gs'), (2, 'as'), (4, 'cs'), (5, 'ds')]:
        x = (i + 1) * w - 14; lit = name in fing
        out += f'<rect x="{x}" y="0" width="28" height="{H * 0.6}" rx="2" fill="{C if lit else N}"/>'
        if lit: out += f'<circle cx="{x + 14}" cy="{H * 0.6 - 18}" r="12" fill="#fff"/><text x="{x + 14}" y="{H * 0.6 - 13}" text-anchor="middle" font-family="AH" font-weight="700" font-size="15" fill="{C}">{fing[name]}</text>'
        if lit and hand: out += f'<text x="{x + 14}" y="26" text-anchor="middle" font-family="AH" font-weight="700" font-size="15" fill="#fff">{hand.get(name, "R")}</text>'
    return f'<svg viewBox="-2 -2 {W + 4} {H + 4}" style="width:100%;max-width:{width}px;display:block;margin:0 auto">{out}</svg>'

def ready_pages():   # the two pages before Lesson 1
    p1 = page(f'''<div class="kick">Before the songs</div><h1>Getting ready</h1>
<p class="lead">Two pages to do before Lesson 1, at the piano and away from it: your hands, how to sit, and the keyboard’s own map.</p>
<div class="sp"></div>{part(1, 'Your fingers have numbers', 'Thumbs are 1 and little fingers are 5, in both hands. Pianists use the numbers to say which finger plays.')}
<div class="sp"></div>{hands(360)}
<div class="sp"></div><div class="act"><b>Number game.</b> Your teacher calls a number; wiggle that finger on both hands. Then thumbs tap together, then the 3s, then the 5s: your hands are mirrors.</div>
{ticks(['Wiggled 1 to 5, each hand', 'Tapped the mirror fingers together'], True)}
<div class="sp"></div><div class="trace"><div class="tbox"><span>Draw around your right hand here, then write 1 to 5 on the fingertips.</span></div></div>
<div class="sp"></div>''', 1)
    p2 = page(f'''{part(2, 'Sit like a pianist', 'Check each one at the start of every practice.')}
<div class="sit">{ticks(['On the front half of the bench', 'Feet flat on the floor (or on a box)', 'Elbows a little in front of you, level with the keys', 'Round hands, as if holding a small ball'])}</div>
<div class="sp"></div>{part(3, 'The keyboard’s map', 'The black keys come in twos and threes, all the way along. They are how you find every white key.')}
<div class="bas"><div>{keys()}</div><div><p class="cap2"><b>Twos and threes.</b> Play every group of two black keys from the bottom to the top, then every group of three.</p><p class="cap2"><b>Find C.</b> C is the white key just left of each two. Play every C.</p></div></div>
<div class="sp"></div><div class="act"><b>Low and high.</b> Left is low, right is high: the turtle walks down low, the bird flies up high. Play a turtle note, then a bird note.</div>
<div class="sp"></div><div class="act"><b>Colour the map.</b> Colour every two black keys one colour and every three another, then write C under every C.</div>
<div class="sp"></div>{keys(3, False, False, 660)}
<div class="sp"></div><div class="end">{ticks(['Played all the twos and threes', 'Found every C', 'Low and high', 'Coloured the map'], True)}</div>''', 2)
    def seq(groups, label):   # finger numbers in time: a circle a beat, a long one held for two, bars between groups
        cells = ''.join('<div class="sb">' + ''.join(f'<span class="fn{" h" if f.endswith("-") else ""}">{f.rstrip("-")}</span>' for f in g.split()) + '</div>' for g in groups)
        return f'<div class="sq"><span class="sql">{label}</span><div class="sqr">{cells}</div></div>'
    p3 = page(f'''{part(4, 'Warm up fingers 2, 3 and 4', 'Lesson 1 is played by the three middle fingers. Wake them up: first tapping on the closed lid, then on the keys. Right hand, then left hand: the numbers are the same in both.')}
<div class="sp"></div><div class="wsub">On the lid · tap and say the numbers</div>
{seq(['2 3 2 3', '2 3 2 3'], 'Two fingers')}
{seq(['2 3 4 3', '2 3 4 3'], 'Three fingers')}
{seq(['2 2 3 3', '4 4 3 3'], 'Twice each')}
<div class="sp"></div><div class="wsub">On the keys · C D E</div>
<div class="bas"><div>{kb(width=300, fmap={'c': 2, 'd': 3, 'e': 4})}</div><div><p class="cap2"><b>Right hand:</b> 2 on middle C, 3 on D, 4 on E. <b>Left hand:</b> an octave lower, 4 on C, 3 on D, 2 on E.</p></div></div>
{seq(['2 3 4-', '4 3 2-'], 'Up and down')}
{seq(['4 3 2-', '4 3 2-'], 'Down, down')}
<div class="sp"></div><div class="act"><b>Echo.</b> Your teacher plays three notes with fingers 2, 3 and 4; play them back. Then you play three and your teacher copies you.</div>
<div class="sp"></div><div class="end">{ticks(['Tapped 2 3 on the lid', 'Tapped 2 3 4 on the lid', 'Played 2 3 4 on the keys', 'Played the echo game'], True)}</div>''', 3)
    return p1 + p2 + p3

def play_page():   # an early lesson's page 3: the song on the keys, step by step
    B = SONG['basics']
    return page(f'''{part(3, 'Play it', B['play'])}
<div class="sp"></div><div class="bas"><div>{blackkb(260) if B.get('blackpic') else kb(width=300, fmap=SONG.get('fmap')) if B.get('kb') else keys(1, True, True, 200)}</div><div><p class="cap2">{B.get('keys_note', '')}</p></div></div>
{hand_panels(B.get('lines', []))}{('<div class="sp"></div>' + B['after']) if B.get('after') else ''}
<div class="sp"></div>
<div class="chk end"><div class="ch">4 · Check</div><div class="cgrid">
<div>{ticks(B.get('can', ['I can say and clap it', 'I can sing it with the words', 'I can sing the letter names']))}</div>
<div><div class="ck2">I can play it:</div><div class="ticks h">{''.join(f'<span class="tk"><span class="bx"></span>{c}</span>' for c in B.get('checks', ['Right hand', 'Left hand']))}</div>
<div class="tch"><span>Teacher</span><span class="tk"><span class="bx"></span>Pass</span><span class="tk"><span class="bx"></span>Not yet</span></div></div></div></div>''', 3)

def hand_panels(lines):   # her 4 Nov 12:34: the right hand and the left hand each in a panel of its own, so the two never blur
    groups = []
    for k, lab in lines:
        if lab or not groups: groups.append([lab, []])
        groups[-1][1].append(k)
    out = ''
    for lab, ks in groups:
        bits = [b.strip() for b in lab.split('·')]
        name = next((b for b in bits if 'hand' in b.lower()), lab); rest = ' · '.join(b for b in bits[1:] if b != name) if len(bits) > 1 else ''
        both = 'both' in name.lower(); left = not both and 'left' in name.lower()
        tag = '<span class="hb lb">L</span><span class="hb">R</span>' if both else f'<span class="hb">{"L" if left else "R"}</span>'
        out += (f'<div class="sp"></div><div class="hp{" lh" if left else ""}"><div class="hh">{tag}<span class="hn">{name}</span>'
                f'<span class="hf">{rest}</span></div>' + ''.join(mus(k) for k in ks) + '</div>')
    return out

basics_page = play_page

EARLY_CSS = f'''.bas{{display:grid;grid-template-columns:auto minmax(0,1fr);gap:22px;align-items:center}} .bas.one{{display:block}}
.bas h3{{font-family:'PF',Georgia,serif;font-size:19px;margin:0 0 4px}} .bas .ticks{{margin:6px 0 0}}
.wtag{{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin:6px 0 -6px}}
.act{{font-size:16px;line-height:1.5;color:{N};margin:2px 0}} .act b{{font-weight:700}}
.trace{{display:flex;justify-content:center}} .tbox{{width:100%;height:330px;border:2px dashed {C};border-radius:14px;display:flex;align-items:flex-end;justify-content:center;padding:12px}} .tbox span{{font-size:13px;color:{MUTE};font-weight:700}}
.sit .ticks{{gap:10px}}
.wsub{{font-size:11.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin:4px 0 2px}}
.sq{{display:grid;grid-template-columns:120px minmax(0,1fr);align-items:center;gap:12px;margin:6px 0}} .sql{{font-size:14px;font-weight:700}}
.sqr{{display:flex;border-left:2px solid {N}}} .sb{{flex:1;display:flex;justify-content:space-around;align-items:center;border-right:2px solid {N};padding:6px 6px}}
.fn{{width:34px;height:34px;border-radius:50%;background:{C};color:#fff;font-weight:700;font-size:17px;display:flex;align-items:center;justify-content:center}} .fn.h{{width:84px;border-radius:17px;background:#fff;color:{C};border:2.5px solid {C}}}
.hp{{border:1.5px solid {N};border-radius:12px;padding:10px 14px 8px;display:flex;flex-direction:column;gap:6px}} .hp.lh{{border-color:{C}}}
.hh{{display:flex;align-items:center;gap:10px}} .hb{{width:26px;height:26px;border-radius:50%;background:{N};color:#fff;font-weight:700;font-size:14px;display:flex;align-items:center;justify-content:center}}
.hp.lh .hb, .hb.lb{{background:{C}}} .hb.lb{{margin-right:-6px}} .hn{{font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{N}}} .hp.lh .hn{{color:{C}}} .hf{{font-size:13px;color:{MUTE};font-weight:700}}'''
