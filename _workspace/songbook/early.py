# Lessons 1 to 3 (her 4 Nov 10:54): before the staff and the chords, page 3 explains the very basics instead of four ways.
# Run inside lesson.py (exec), so page, part, mus, ticks, N, C and MUTE are its own.

def hands():   # both hands from above, palms down: the left hand's thumb on its right, the right hand's on its left
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
    return (f'<svg viewBox="0 0 360 208" style="width:100%;max-width:280px;display:block">'
            f'{hand(0, True)}{hand(196, False)}{lab(83, "LEFT HAND")}{lab(279, "RIGHT HAND")}</svg>')

def groups():   # two octaves from C: the black keys in twos (coral) and threes (navy), every C named
    w, H = 24, 96; W = 14 * w; out = ''
    for i in range(14): out += f'<rect x="{i * w}" y="0" width="{w}" height="{H}" rx="2" fill="#fff" stroke="{N}" stroke-width="1.2"/>'
    for i in (0, 1, 3, 4, 5, 7, 8, 10, 11, 12):
        two = (i % 7) in (0, 1)
        out += f'<rect x="{(i + 1) * w - 7}" y="0" width="14" height="{H * 0.6}" rx="2" fill="{C if two else N}"/>'
    for i in (0, 7): out += f'<text x="{i * w + w / 2}" y="{H - 8}" text-anchor="middle" font-family="AH" font-weight="700" font-size="12" fill="{N}">C</text>'
    return f'<svg viewBox="-1 -1 {W + 2} {H + 2}" style="width:100%;max-width:280px;display:block">{out}</svg>'

def basics_page():
    B = SONG['basics']
    return page(f'''{part(3, 'Hello, piano', 'Three things every pianist knows. Read them with your teacher, then try each one.')}
<div class="sp"></div><div class="bas"><div>{hands()}</div><div><h3>Your fingers have numbers</h3><p class="cap2">Thumbs are 1, little fingers are 5, in both hands. Wiggle each number your teacher calls.</p>{ticks(['Wiggled 1 to 5, each hand'])}</div></div>
<div class="sp"></div><div class="bas"><div>{groups()}</div><div><h3>Black keys come in twos and threes</h3><p class="cap2">Play every group of two black keys, low to high, then every group of three. C is the white key just left of each two.</p>{ticks(['Found the twos and threes', 'Found every C'])}</div></div>
<div class="sp"></div><div class="bas one"><h3>Sit like a pianist</h3><p class="cap2">Sit on the front half of the bench, feet flat. Elbows a little in front of you, level with the keys. Round hands, as if holding a small ball.</p></div>
<div class="sp"></div>{part(4, 'Play it', B['play'])}
{''.join(f'<div class="wtag">{lab}</div>{mus(k)}' for k, lab in B.get('lines', [['p1', 'Right hand'], ['p2', 'Left hand']]))}
<div class="chk end"><div class="ch">5 · Check</div><div class="cgrid">
<div>{ticks(['I can say and clap it', 'I can sing it with the words', 'I can name its notes'])}</div>
<div><div class="ck2">I can play it:</div><div class="ticks h">{''.join(f'<span class="tk"><span class="bx"></span>{c}</span>' for c in B.get('checks', ['Right hand', 'Left hand']))}</div>
<div class="tch"><span>Teacher</span><span class="tk"><span class="bx"></span>Pass</span><span class="tk"><span class="bx"></span>Not yet</span></div></div></div></div>''', 3)

EARLY_CSS = f'''.bas{{display:grid;grid-template-columns:280px minmax(0,1fr);gap:22px;align-items:center}} .bas.one{{display:block}}
.bas h3{{font-family:'PF',Georgia,serif;font-size:19px;margin:0 0 4px}} .bas svg{{max-height:140px;width:auto !important;max-width:100%}} .bas .ticks{{margin:6px 0 0}}
.wtag{{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin:6px 0 -6px}}'''
