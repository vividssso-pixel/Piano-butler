# The Piano Butler Workbook, Time: practice pages that follow Handbook Part II
import json
exec(open('/tmp/claude-0/pk/book10.py').read().split("flow = ''.join(")[0])   # helpers, fonts, glyphs (V = handbook snippets)
src10 = open('/tmp/claude-0/pk/book10.py').read()
css = src10[src10.index("css = f'''") + 10:src10.index("'''\nhtml =")]
css = eval("f'''" + css + "'''")
W = json.load(open('/tmp/claude-0/vrv/wout.json'))
def wx(k, h=80, cap=''):
    svg = W[k].replace('<svg ', '<svg style="max-height:%dpx" ' % h, 1)
    return '<figure class="vx"><div class="vs">' + svg + '</div>' + ('<figcaption>' + cap + '</figcaption>' if cap else '') + '</figure>'
def wpage(inner, n, hb):
    return f'''<section class="pg"><div class="top"><span>THE PIANO BUTLER WORKBOOK</span><span>TIME · HANDBOOK P. {hb}</span></div><div class="rule"></div><div class="body">{inner}</div>
<div class="sign"><span>Date <i></i></span><span>Practised <i class="s"></i> times</span><span>Checked <i></i></span></div><div class="foot"><span>{n}</span></div></section>'''
def ex(n, title, level, how, body):
    return f'<div class="ex2"><div class="eh"><span class="en">{n}</span><b>{title}</b><span class="el">{level}</span></div><p class="how">{how}</p>{body}</div>'
def ticks(n=5): return '<span class="tk">' + '<i></i>' * n + '</span>'
BOX = '<span class="ab"></span>'
LINE = '<span class="al"></span>'

def beats_row(lbl, n, bars=2):
    cells = ''.join('<span class="bar">' + ''.join('<i></i>' for _ in range(n)) + '</span>' for _ in range(bars))
    return f'<div class="br"><b>{lbl}</b>{cells}</div>'
P1 = wpage(f'''<div class="kick">Workbook · Time · 1</div><h1>Pulse and the bar</h1>
{ex(1, 'Count it', 'Level 0', 'Write a count in every box: the beat you play, then the beats you hold. The first bar is done.', wx('wc34', 86))}
{ex(2, 'Strong beats', 'Level 0', 'Each dot is one beat. Circle the strong beat in every bar. In 4/4, also underline the medium beat.', beats_row('2/4', 2) + beats_row('3/4', 3) + beats_row('4/4', 4))}
{ex(3, 'Name the signs', 'Level 0', 'Write the name of each sign and what it tells you.', tbl(['Sign', 'Name', 'It tells you'], [[bars('bar'), LINE, LINE], [bars('dbl'), LINE, LINE], [bars('fin'), LINE, LINE], [bars('repeat'), LINE, LINE]], ['18%', '32%', '50%']))}
{ex(4, 'Clap and count', 'Level 0', 'Set a metronome to ♩ = 60. Clap on the notes, open your hands on the rests, and count aloud. Tick a circle each time it is steady.', wx('wr1', 70) + ticks())}''', 1, 36)

items = [('sb', 'semibreve', '4'), ('c', '', ''), ('m', '', ''), ('q', '', ''), ('dm', '', ''), ('sq', '', '')]
rows = [[gcell('n', k, 40), f'<b>{n}</b>' if n else LINE, f'<b>{b}</b>' if b else BOX, gcell('r', k, 40) if n else BOX] for k, n, b in items]
P2 = wpage(f'''<div class="kick">Workbook · Time · 2</div><h1>Notes and rests</h1>
{ex(1, 'Name, beats and rest', 'Levels 0–2', 'For each note, write its name and how many beats it lasts (crotchet = 1 beat), then draw the rest of the same length. The first row is done.', '<table class="ht nt"><colgroup><col style="width:14%"><col style="width:40%"><col style="width:18%"><col style="width:28%"></colgroup><thead><tr><th>Note</th><th>Name</th><th>Beats</th><th>Rest</th></tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td class="g">{c}</td>' if i in (0, 3) else f'<td>{c}</td>' for i, c in enumerate(r)) + '</tr>' for r in rows) + '</tbody></table>')}
{ex(2, 'Rests on the staff', 'Level 0', 'Draw a semibreve rest in the first bar (it hangs below the fourth line) and a minim rest in the second (it sits on the middle line).', '<figure class="vx"><svg viewBox="0 0 600 80" style="width:100%;height:auto;display:block">' + ''.join(f'<line x1="10" x2="590" y1="{14 + i * 12}" y2="{14 + i * 12}" stroke="#26296b" stroke-width="1.3"/>' for i in range(5)) + '<line x1="300" x2="300" y1="14" y2="62" stroke="#26296b" stroke-width="1.3"/><line x1="586" x2="586" y1="14" y2="62" stroke="#26296b" stroke-width="1.3"/><line x1="592" x2="592" y1="14" y2="62" stroke="#26296b" stroke-width="4"/></svg></figure>')}
{ex(3, 'The other name', 'Level 0', 'Many books call the notes by other names. Write the other name for each one. The first is done.', tbl(['Name', 'Also called'], [['semibreve', '<b class="done2">whole note</b>'], ['minim', LINE], ['crotchet', LINE], ['quaver', LINE], ['semiquaver', LINE]], ['40%', '60%']))}''', 2, 37)

sums = [(['m', 'c'], '3'), (['c', 'q'], ''), (['dm', 'c'], ''), (['sb', 'm'], ''), (['dc', 'q'], ''), (['q', 'q', 'q', 'q'], '')]
srows = ''.join('<div class="sum">' + ' <span class="pl">+</span> '.join(gin('n', k, 34) for k in ks) + f' <span class="pl">=</span> ' + (f'<b class="done">{a}</b>' if a else BOX) + ' <span class="mu2">beats</span></div>' for ks, a in sums)
fills = ''.join(f'<div class="fc">{wx(k, 70)}<div class="add">add one note {BOX}</div></div>' for k in ('wf1', 'wf2', 'wf3', 'wf4', 'wf5', 'wf6'))
P3 = wpage(f'''<div class="kick">Workbook · Time · 3</div><h1>How long is a note?</h1>
{ex(1, 'Note sums', 'Levels 0–½', 'Add up the beats (crotchet = 1 beat). The first one is done.', f'<div class="sums">{srows}</div>')}
{ex(2, 'Complete the bar', 'Levels 0–1', 'Each bar is one note short. Write the one note that completes it.', f'<div class="fills">{fills}</div>')}
{ex(3, 'Dots and ties: count it', 'Level ½', 'Write a count in every box.', wx('wc44', 84))}
{ex(4, 'Clap and count', 'Level ½', 'Clap the dotted rhythms, counting the “&” inside each dotted crotchet. Tick a circle each time it is steady.', wx('wl2', 70) + ticks())}''', 3, 38)

tsx = ''.join(f'<div class="fc">{wx(k, 66)}<div class="add">time signature {BOX}</div></div>' for k in ('wt1', 'wt2', 'wt3', 'wt4', 'wt5', 'wt6'))
sc = [ts(3, 4), ts(6, 8), ts(2, 2), ts(9, 8), ts(4, 4), ts(12, 8), ts(3, 8), ts(6, 4)]
scrows = ''.join(f'<div class="scc">{x}<span class="sel">simple · compound</span><span class="add">beats {BOX}</span></div>' for x in sc)
P4 = wpage(f'''<div class="kick">Workbook · Time · 4</div><h1>Time signatures</h1>
{ex(1, 'Which time signature?', 'Levels 0–3', 'Each line is one full bar. Write a time signature that fits (top number over bottom number).', f'<div class="fills">{tsx}</div>')}
{ex(2, 'Simple or compound?', 'Levels 0–4', 'Circle simple or compound, then write how many beats are in each bar.', f'<div class="scg">{scrows}</div>')}
{ex(3, 'Add the bar lines', 'Levels 0–1', 'Draw a bar line after every full bar, and a final bar line at the end.', wx('wb1', 54) + wx('wb2', 54) + wx('wb3', 54))}''', 4, 39)

grp = ''.join(f'<div class="fc">{wx(k, 66)}<div class="add">✓ &nbsp; ✗</div></div>' for k in ('wg1', 'wg2', 'wg3', 'wg4'))
lines = ''.join(f'<div class="cl2"><div class="clh"><span class="lv3">{lv_}</span>{ticks()}</div>{wx(k, 70)}</div>' for k, lv_ in (('wl3', 'Level 2 · triplets and semiquavers'), ('wl4', 'Level 4 · syncopation')))
P5 = wpage(f'''<div class="kick">Workbook · Time · 5</div><h1>Rhythm</h1>
{ex(1, 'Good grouping?', 'Level 4', 'Beams should show the beats. Circle ✓ if the grouping is right, ✗ if it hides a beat.', f'<div class="fills g2">{grp}</div>')}
{ex(2, 'Count it', 'Levels 2–4', 'Write a count in every box: a triplet, then a syncopation.', '<div class="two" style="grid-template-columns:1fr 1fr">' + wx('wtr', 80) + wx('wsy', 80) + '</div>')}
{ex(3, 'Clap and count', 'Levels 2–4', 'Clap each line while counting aloud, with a metronome. Tick a circle each day it is steady.', lines)}''', 5, 41)

css += f'''
.ex2{{border-top:1.5px solid {N};padding-top:8px;margin-top:12px}} .eh{{display:flex;align-items:baseline;gap:10px}} .en{{font-weight:700;font-size:17px;color:{C}}} .eh b{{font-size:17px}} .el{{margin-left:auto;font-size:12.5px;color:{MUTE};font-weight:700}}
.how{{font-size:14.5px;margin:3px 0 8px}} .ab{{display:inline-block;width:46px;height:30px;border:1.5px solid {N};background:#fff;vertical-align:middle}} .al{{display:block;border-bottom:1.2px solid #b9bbd3;height:24px}}
.br{{display:flex;align-items:center;gap:16px;padding:6px 0;border-bottom:.6px solid #e2ddd0}} .br b{{width:48px;font-size:15px}} .bar{{display:flex;gap:18px;padding:0 18px;border-right:2px solid {N}}} .bar i{{width:16px;height:16px;border-radius:50%;background:{N};display:inline-block}}
.tk{{display:flex;gap:10px;margin-top:6px}} .tk i{{width:24px;height:24px;border:1.6px solid #c9cbe0;border-radius:50%;display:inline-block}}
.sums{{display:grid;grid-template-columns:1fr 1fr;gap:6px 30px}} .sum{{display:flex;align-items:center;gap:6px;font-size:16px;padding:4px 0;border-bottom:.6px solid #e2ddd0}} .pl{{font-weight:700;font-size:18px;margin:0 4px}} .done2{{color:{C}}} .done{{color:{C};font-size:18px;width:46px;text-align:center}} .mu2{{color:{MUTE};font-size:13px}}
.fills{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}} .fills.g2{{grid-template-columns:1fr 1fr}} .fc .vx{{margin:0;height:84px;display:flex;align-items:center}} .fc .vx .vs{{width:100%}} .add{{display:flex;align-items:center;justify-content:flex-end;gap:8px;font-size:13px;color:{MUTE};margin-top:4px}}
.scg{{display:grid;grid-template-columns:1fr 1fr;gap:4px 30px}} .scc{{display:flex;align-items:center;gap:14px;border-bottom:.6px solid #e2ddd0;padding:4px 0;font-size:14px}} .sel{{flex:1;color:{MUTE}}} .scc .add{{margin:0}}
.cl2{{margin-top:6px}} .clh{{display:flex;align-items:center;justify-content:space-between}} .clh .tk{{margin:0}} .cl2 .vx{{margin:4px 0}} .lv3{{font-size:12.5px;font-weight:700;color:{MUTE}}}
.sign{{position:absolute;left:58px;right:58px;bottom:58px;display:flex;gap:24px;border-top:.8px solid #c9cbe0;padding-top:8px;font-size:12px;color:{MUTE}}} .sign span{{display:flex;align-items:flex-end;gap:6px;flex:1}} .sign i{{flex:1;border-bottom:1px solid #b9bbd3;height:14px}} .sign i.s{{flex:none;width:34px}}
'''
open('/mnt/user-data/outputs/house-rooms/workbook-time.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{P1}{P2}{P3}{P4}{P5}</body></html>')
print('ok')
