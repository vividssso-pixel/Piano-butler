import json, re, base64
R = json.load(open('/tmp/claude-0/pk/lib-notes-rows.json'))
DK, N, C, CR, G = '#1c1e4f', '#26296b', '#e4572e', '#fffdf7', '#2e8a6e'
src = open('/tmp/claude-0/pk/book2.py').read()
base = src[src.index("css = f'''") + 10:src.index("'''\nfonts")].replace('{{', '{').replace('}}', '}').replace('{N}', N).replace('{C}', C).replace('{CR}', CR)
def g(i, h=40): return R[i]['html'].replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block;margin:0 auto" ', 1)
def bowtie(col, knot, s=64):
    return (f'<svg viewBox="0 0 40 24" style="width:{s}px;height:{s * 0.6:.0f}px;display:block;margin:0 auto"><path d="M2 3 L18 12 L2 21 Z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linejoin="round"/>'
            f'<path d="M38 3 L22 12 L38 21 Z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linejoin="round"/><circle cx="20" cy="12" r="2.4" fill="{knot}"/></svg>')
def page(inner, n, right='CONTENTS'):
    return f'''<section class="pg"><div class="top"><span>PIANO BUTLER · HANDBOOK</span><span>{right}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'''

COVER = f'''<section class="pg cover"><div class="cframe"><div class="ctop">PIANO BUTLER</div>
<div class="cmid">{bowtie(CR, C, 96)}<div class="cpre">The Piano Butler</div><div class="cbook">Handbook</div><div class="clvl">A companion to every room of music</div><div class="cdiv"></div>
<div class="csub">Pitch, time, harmony, expression, form and history, from the whole picture to the smallest detail. For any piece, any method, from the first lesson to Level 8.</div></div>
<div class="cfoot">Prepared by the Piano Butler · thepianobutler.com</div></div></section>'''

PARTS = [('I', 'Pitch', 'Where notes sit: from the keyboard and the staff to scales and keys.', [('The keyboard', 8), ('The staff and the clefs', 10), ('Intervals', 14), ('Scales', 18), ('Keys and key signatures', 24), ('Related keys', 28), ('Modes', 30), ('Transposition', 32)]),
         ('II', 'Time', 'How music moves: the pulse, the bar, the length of every note.', [('Pulse and the bar', 36), ('Notes and rests', 38), ('Time signatures', 40), ('Rhythm', 44)]),
         ('III', 'Harmony', 'Notes sounding together, and how they lead somewhere.', [('Chords', 50), ('Cadences', 56), ('Non-chord notes', 60), ('Chromatic chords', 62)]),
         ('IV', 'Expression', 'The signs and words that tell you how to play.', [('Signs', 66), ('How to play: tempo, dynamics, touch', 70), ('Ornaments', 76)]),
         ('V', 'Shape and style', 'How pieces are built, and the music of each age.', [('Melody', 80), ('Texture', 82), ('Form', 84), ('Kinds of pieces', 88), ('Periods', 92), ('Composers', 96)]),
         ('VI', 'Playing and listening', 'The body at the piano, and the ear.', [('Technique', 102), ('Aural', 108), ('Instruments', 112)])]
toc = ''.join(f'''<div class="part"><div class="ph"><span class="pn">Part {r}</span><b>{t}</b></div><p class="pd">{dsc}</p>
{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span class="pg2">{p}</span></div>' for x, p in items)}</div>''' for r, t, dsc, items in PARTS)
CONTENTS = page(f'''<div class="kick">Contents</div><h1 class="big">A map of music</h1>
<p class="lead">Six parts, from the largest idea to the smallest detail. Read a part from the start for the whole picture, or go straight to the table you need.</p>
<div class="toc">{toc}</div>
<div class="tr end"><span><b>Glossary</b> · every music word, A to Z</span><span class="dots"></span><span class="pg2">116</span></div>
<div class="tr end"><span><b>Index</b></span><span class="dots"></span><span class="pg2">124</span></div>''', 3)

steps = [('Pulse', 'the steady beat underneath'), ('Bar', 'beats grouped: 2, 3 or 4'), ('Time signature', 'how many beats, and which note is one beat'), ('Note values', 'how long each note lasts'), ('Rhythm', 'the pattern of long and short')]
flow = ''.join(f'<div class="fl"><span class="fn">{i + 1}</span><b>{a}</b><i>{b}</i></div>' + ('<span class="fa">›</span>' if i < 4 else '') for i, (a, b) in enumerate(steps))
PART2 = f'''<section class="pg part2"><div class="pframe"><div class="pk">Part II</div><div class="pt">Time</div><div class="pdv"></div>
<p class="pl">Music moves through time. Underneath it runs a steady <b>pulse</b>; the pulse is grouped into <b>bars</b>; and every note and rest takes up a measured share of it. This part goes from that big picture down to the length of a single note.</p>
<div class="flow">{flow}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span class="pg2">{p}</span></div>' for x, p in PARTS[1][3])}</div></div></section>'''

names = [('breve', '8', 'Level 4'), ('dotted semibreve', '6', ''), ('semibreve', '4', 'Level 0'), ('dotted minim', '3', 'Level 0'), ('minim', '2', 'Level 0'), ('dotted crotchet', '1½', 'Level ½'), ('crotchet', '1', 'Level 0'), ('dotted quaver', '¾', 'Level 3'), ('quaver', '½', 'Level 0'), ('semiquaver', '¼', 'Level 2'), ('demisemiquaver', '⅛', ''), ('hemidemisemiquaver', '1/16', '')]
rows = ''.join(f'<tr><td>{g(2 * i)}</td><td>{g(2 * i + 1)}</td><td class="nmc">{n}</td><td class="bt">{b}</td><td class="lv">{l or "<i>beyond Level 8</i>"}</td></tr>' for i, (n, b, l) in enumerate(names))
NOTES = page(f'''<div class="kick">Part II · Time</div><h1>Notes and rests</h1>
<p class="lead">A note’s shape shows how long it lasts. Each plain note lasts <b>half as long</b> as the one above it; a <b>dot</b> adds half the note’s value again. Every note has a rest of the same length: a silence, counted just as carefully.</p>
<table class="nt"><thead><tr><th>Note</th><th>Rest</th><th>Name</th><th>Beats*</th><th>First met</th></tr></thead><tbody>{rows}</tbody></table>
<div class="fn2">* With the crotchet as one beat, as in 2/4, 3/4 and 4/4.</div>
<div class="two" style="margin-top:14px"><div><div class="h3">Groups of other sizes</div>
<div class="tup"><div>{g(24, 46)}</div><span><b>Triplet</b>: three notes in the time of two. <i>Level 2</i></span></div>
<div class="tup"><div>{g(25, 46)}</div><span><b>Duplet</b>: two notes in the time of three. <i>Level 3</i></span></div></div>
<div><div class="h3">See also</div><div class="tr"><span>Time signatures</span><span class="dots"></span><span class="pg2">40</span></div><div class="tr"><span>Rhythm</span><span class="dots"></span><span class="pg2">44</span></div>
<div class="h3" style="margin-top:12px">Practise it</div><div class="tr"><span>Workbook Level 0 · Note values</span></div><div class="tr"><span>Online · Library › Notes and rests</span></div></div></div>''', 38, 'PART II · TIME')

css = base + f'''
.cover{{background:{DK};padding:34px}} .cframe{{position:absolute;inset:34px;border:1.5px solid rgba(255,253,247,.7);outline:.6px solid rgba(255,253,247,.45);outline-offset:-8px;color:{CR};display:flex;flex-direction:column;align-items:center;padding:56px 64px 40px}}
.ctop{{font-size:12px;font-weight:800;letter-spacing:.42em;opacity:.85}} .cmid{{margin-top:auto;margin-bottom:auto;text-align:center}}
.cpre{{font-family:'Playfair Display',Georgia,serif;font-style:italic;font-size:24px;margin-top:26px;opacity:.9}} .cbook{{font-family:'Playfair Display',Georgia,serif;font-size:84px;font-weight:700;margin-top:4px;line-height:1}} .clvl{{font-family:'Playfair Display',Georgia,serif;font-style:italic;font-size:21px;color:#f4a9bb;margin-top:16px}}
.cdiv{{width:120px;height:5px;border-top:1px solid {CR};border-bottom:1px solid {CR};margin:28px auto;opacity:.7}} .csub{{font-size:14px;line-height:1.65;max-width:430px;margin:0 auto;opacity:.86}}
.cfoot{{font-size:10.5px;letter-spacing:.12em;opacity:.6;text-transform:uppercase}}
.toc{{columns:2;column-gap:34px}} .part{{break-inside:avoid;margin-bottom:14px}} .ph{{display:flex;align-items:baseline;gap:10px;border-top:1.5px solid {N};padding-top:6px}} .pn{{font-size:10px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:{C}}} .ph b{{font-family:'Playfair Display',Georgia,serif;font-size:19px}}
.pd{{font-size:12px;font-style:italic;color:#6d6f9c;margin:2px 0 4px;line-height:1.4}}
.tr{{display:flex;align-items:baseline;gap:6px;font-size:13px;padding:2.5px 0}} .dots{{flex:1;border-bottom:1px dotted #b9bbd3;transform:translateY(-3px)}} .pg2{{font-variant-numeric:tabular-nums;color:#3d4080;font-size:12.5px}} .tr.end{{border-top:.6px solid #e2ddd0;padding-top:6px;margin-top:2px;font-size:13.5px}}
.part2{{background:{DK};padding:34px}} .pframe{{position:absolute;inset:34px;border:1.5px solid rgba(255,253,247,.7);outline:.6px solid rgba(255,253,247,.45);outline-offset:-8px;color:{CR};padding:120px 64px 40px}}
.pk{{font-size:12px;font-weight:900;letter-spacing:.3em;text-transform:uppercase;color:#f4a9bb}} .pt{{font-family:'Playfair Display',Georgia,serif;font-size:76px;line-height:1;margin-top:10px}} .pdv{{width:90px;height:5px;border-top:1px solid {CR};border-bottom:1px solid {CR};margin:24px 0;opacity:.7}}
.pl{{font-size:16px;line-height:1.7;max-width:560px;opacity:.92}}
.flow{{display:flex;align-items:stretch;gap:4px;margin:34px 0 30px}} .fl{{flex:1;border:1px solid rgba(255,253,247,.45);padding:10px 8px;text-align:center}} .fn{{display:block;font:700 14px Georgia,serif;color:#f4a9bb}} .fl b{{display:block;font-family:'Playfair Display',Georgia,serif;font-size:15px;margin:2px 0}} .fl i{{display:block;font-size:10.5px;font-style:normal;opacity:.75;line-height:1.35}} .fa{{align-self:center;color:#f4a9bb;font-size:18px}}
.pin{{max-width:360px}} .pih{{font-size:10px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;opacity:.7;margin-bottom:4px}} .pin .tr{{font-size:14px}} .pin .dots{{border-color:rgba(255,253,247,.4)}} .pin .pg2{{color:{CR}}}
.nt{{width:100%;border-collapse:collapse;margin-top:4px}} .nt th{{font-size:9.5px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:#8a8cb0;text-align:left;padding:4px 6px;border-bottom:1.5px solid {N}}}
.nt td{{border-bottom:.6px solid #e2ddd0;padding:3px 6px;vertical-align:middle}} .nt td:nth-child(1),.nt td:nth-child(2){{width:46px}} .nmc{{font-size:14px;font-weight:600}} .bt{{font-weight:800;font-size:14px;width:70px}} .lv{{font-size:11.5px;color:#6d6f9c;width:110px}} .lv i{{font-style:italic;color:#9a9cc4}}
.fn2{{font-size:11px;color:#8a8cb0;margin-top:4px}} .tup{{display:flex;align-items:center;gap:12px;font-size:13px;padding:4px 0;border-bottom:.6px solid #e2ddd0}} .tup>div{{flex:none;width:70px}} .tup i{{color:#6d6f9c}}
'''
FF = ''.join("@font-face{font-family:'Playfair Display';font-weight:700;font-style:%s;src:url(data:font/woff2;base64,%s) format('woff2')}" % (st, base64.b64encode(open('/tmp/claude-0/fnt/package/files/playfair-display-latin-700-%s.woff2' % st, 'rb').read()).decode()) for st in ('normal', 'italic'))
open('/mnt/user-data/outputs/house-rooms/handbook.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>{css}</style></head><body>{COVER}{CONTENTS}{PART2}{NOTES}</body></html>')
print('ok')
