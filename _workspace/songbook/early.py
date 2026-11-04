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
    fing = fing or {'as': '2', 'cs': '3', 'ds': '4'}
    whites = 'fgabcde'; w, H = 46, 150; W = len(whites) * w; out = ''
    for i, l in enumerate(whites):
        out += f'<rect x="{i * w}" y="0" width="{w}" height="{H}" rx="3" fill="#fff" stroke="{N}" stroke-width="1.5"/>'
        out += f'<text x="{i * w + w / 2}" y="{H - 12}" text-anchor="middle" font-family="AH" font-weight="700" font-size="16" fill="{MUTE}">{l.upper()}</text>'
    for i, name in [(0, 'fs'), (1, 'gs'), (2, 'as'), (4, 'cs'), (5, 'ds')]:
        x = (i + 1) * w - 14; lit = name in fing
        out += f'<rect x="{x}" y="0" width="28" height="{H * 0.6}" rx="2" fill="{C if lit else N}"/>'
        if lit: out += f'<circle cx="{x + 14}" cy="{H * 0.6 - 18}" r="12" fill="#fff"/><text x="{x + 14}" y="{H * 0.6 - 13}" text-anchor="middle" font-family="AH" font-weight="700" font-size="15" fill="{C}">{fing[name]}</text>'
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
    return p1 + p2

def play_page():   # an early lesson's page 3: the song on the keys, step by step
    B = SONG['basics']
    return page(f'''{part(3, 'Play it', B['play'])}
<div class="sp"></div><div class="bas"><div>{blackkb(260) if B.get('blackpic') else kb(width=300, fmap=SONG.get('fmap')) if B.get('kb') else keys(1, True, True, 200)}</div><div><p class="cap2">{B.get('keys_note', '')}</p></div></div>
{''.join((f'<div class="sp"></div><div class="wtag">{lab}</div>' if lab else '') + mus(k) for k, lab in B.get('lines', []))}
<div class="sp"></div>
<div class="chk end"><div class="ch">4 · Check</div><div class="cgrid">
<div>{ticks(B.get('can', ['I can say and clap it', 'I can sing it with the words', 'I can sing the letter names']))}</div>
<div><div class="ck2">I can play it:</div><div class="ticks h">{''.join(f'<span class="tk"><span class="bx"></span>{c}</span>' for c in B.get('checks', ['Right hand', 'Left hand']))}</div>
<div class="tch"><span>Teacher</span><span class="tk"><span class="bx"></span>Pass</span><span class="tk"><span class="bx"></span>Not yet</span></div></div></div></div>''', 3)

basics_page = play_page

EARLY_CSS = f'''.bas{{display:grid;grid-template-columns:auto minmax(0,1fr);gap:22px;align-items:center}} .bas.one{{display:block}}
.bas h3{{font-family:'PF',Georgia,serif;font-size:19px;margin:0 0 4px}} .bas .ticks{{margin:6px 0 0}}
.wtag{{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin:6px 0 -6px}}
.act{{font-size:16px;line-height:1.5;color:{N};margin:2px 0}} .act b{{font-weight:700}}
.trace{{display:flex;justify-content:center}} .tbox{{width:100%;height:330px;border:2px dashed {C};border-radius:14px;display:flex;align-items:flex-end;justify-content:center;padding:12px}} .tbox span{{font-size:13px;color:{MUTE};font-weight:700}}
.sit .ticks{{gap:10px}}'''
