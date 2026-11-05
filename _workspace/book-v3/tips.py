# The Piano Butler Handbook · Putting it together: the closing pages, after the last part (her 4 Nov: no separate Tips book; each part ends with its own tips)
import sys
src10 = open('/tmp/claude-0/pk/book10.py').read()
exec(src10.split("flow = ''.join(")[0])
css = eval("f'''" + src10[src10.index("css = f'''") + 10:src10.index("'''\nhtml =")] + "'''")
FF0 = FF
def tpage(inner, n): return page(inner, n, 'PUTTING IT TOGETHER')
svg = open('/tmp/claude-0/pk/tips/six_num.svg').read().replace('<svg ', '<svg style="width:100%;max-height:230px" ', 1)
FIG = f'<figure class="vx px tq sixf"><div class="vs">{svg}</div></figure>'
READ = [('The finger number', '<b class="co">3</b>: the middle finger plays it. Fingering is planned, not guessed.', 'Playing and listening (later)'),
        ('The beat', 'Beat 1 of bar 2, and it is held for <b>two beats</b>.', 'Part II · Time · p. 48'),
        ('The note name', '<b class="co">E</b>: the white key just right of the two black keys.', 'Part I · Pitch · p. 22'),
        ('The chord', 'The <b>C</b> above the staff: this E belongs to the C major chord.', 'Part III · Harmony · p. 64'),
        ('The marks', '<b style="font-family:PF,serif;font-style:italic;font-size:17px">p</b> and the slur: play it softly and smoothly.', 'Expression (later)'),
        ('The phrase', 'The slur ends here, so the note lands gently, like the end of a sentence.', 'Shape and style (later)')]
T1 = tpage(f"""{head('Putting it together · 1', 'Everything one note tells you', 'Look at the red note. It carries six pieces of information at once, and each one can be read straight off the page. Read all six and the note is right; miss one and it is only nearly right.')}
{FIG}
<div class="six rd">{''.join(f'<div><span class="rn">{i + 1}</span><b>{a}</b><span>{b}</span><i>{c}</i></div>' for i, (a, b, c) in enumerate(READ))}</div>
<p class="think"><span>Think of it</span>A note is like a word said aloud: its spelling, its timing, its tone of voice and its place in the sentence all change what it means.</p>
<div class="scores"><div class="hh">The same six, in any music</div><div><b>A classical score</b>Most of it is written in: finger numbers, dynamics, slurs. Your job is to read every one.</div><div><b>A pop lead sheet</b>A melody and chord names only. You choose the fingers, the marks and the shape yourself.</div><div><b>A jazz chart</b>Chords and a style word such as Swing: the beat and the shape are yours to feel.</div></div>
<p class="sm">Try it on any piece: point to one note and find all six. Finger numbers count as much as the note name.</p>""", 70)
T2 = tpage(f"""{head('Putting it together · 2', 'When a passage won’t come right', 'Name the problem first, then fix that one thing. Most hard bars are hard for one reason, and the six things a note tells you point straight to it.')}
<div class="tip"><div class="bh">Tip</div><b class="tt">What you notice, what to check</b>
{tbl(['What you notice', 'Check', 'Turn to'], [['You stumble in the same place every time', '<b class="co">the finger number</b>', 'Playing and listening'], ['It rushes, drags or the counting slips', '<b class="co">the beat</b>', 'Part II · Time'], ['A note sounds wrong', '<b class="co">the note name</b>', 'Part I · Pitch'], ['A chord sounds odd or thin', '<b class="co">the chord</b>', 'Harmony'], ['It is correct but flat and dull', '<b class="co">the marks</b>', 'Expression'], ['It does not seem to go anywhere', '<b class="co">the phrase</b>', 'Shape and style']], ['46%', '27%', '27%'])}
</div>
{h3('Six ways to fix a hard bar')}
<div class="fixes">{''.join(f'<div><span class="rn">{i + 1}</span><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate([('Slow it right down', 'Slow enough to be right three times in a row, then a little faster.'), ('Hands separately', 'Each hand on its own until it is easy, then together, slowly.'), ('Start from the end', 'Play the last beat, then the last two, then three: you always finish on what you know best.'), ('Practise the join', 'The last note of one bar and the first of the next: most slips live there.'), ('Climb the metronome', 'Up four clicks each time it is clean; down eight if it falls apart.'), ('Put it back', 'Play two bars before and two after, so the fixed bar lives inside the music again.')]))}</div>
{h3('Before you play a new piece: a thirty-second look')}
<div class="scan">{''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [('Key signature', 'Which sharps or flats, all the way through?'), ('Time signature', 'How many beats in a bar, and which note is one beat?'), ('Tempo and mood', 'The words at the top: how fast, what character?'), ('Patterns', 'Bars that repeat or nearly repeat: learn them once.')])}</div>
<p class="think"><span>Think of it</span>Like a doctor: name the symptom first, then treat that one thing. Practising everything harder rarely fixes the one bar that is wrong.</p>""", 71)
css += '''
.rd>div{position:relative;padding-left:44px} .rd .rn,.fixes .rn{position:absolute;left:12px;top:12px;width:22px;height:22px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;font-size:12.5px;display:flex;align-items:center;justify-content:center} .rd b{font-family:'AH',Arial;font-size:15px;color:#26296b} .co{color:#e4572e}
.six{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin:8px 0 10px} .six>div{border:1.5px solid #26296b;border-radius:6px;padding:10px 12px;display:flex;flex-direction:column;gap:4px;font-size:14px;line-height:1.45} .six i{font-style:normal;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#6d6f9c;margin-top:auto;padding-top:4px;border-top:1px solid #e2ddd0}
.tq{border:0;padding:0;margin:6px 0} .sixf{border:0} .sixf .vs svg text{font-family:'AH',Arial} .px .vs svg{width:100%;height:auto}
.think{display:flex;gap:10px;align-items:baseline;font-size:14px;margin:8px 0;color:#3d4080} .think span{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#2e8a6e}
.tip{border-left:3px solid #e4572e;background:#fdf6f2;padding:10px 16px 12px;margin:12px 0} .tip .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .tip .tt{display:block;font-size:16px;margin:2px 0 6px} .tip td,.tip th{white-space:nowrap}
.fixes{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px 14px;margin:6px 0 10px} .fixes>div{position:relative;padding:10px 12px 10px 44px;border:1px solid #e2ddd0;display:flex;flex-direction:column;gap:2px;font-size:13.5px;line-height:1.45} .fixes b{font-size:14.5px}
.scan{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:8px;margin:6px 0 8px} .scan>div{border-top:3px solid #26296b;border:1px solid #e2ddd0;border-top:3px solid #26296b;padding:8px 10px;display:flex;flex-direction:column;gap:2px;font-size:13px;line-height:1.4}
.six.rd>div{padding-left:44px} .scores{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin:10px 0 4px;background:#f6f5fa;border-top:3px solid #26296b;padding:10px 14px} .scores .hh{grid-column:1/-1;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#26296b} .scores div{border-left:3px solid #e4572e;padding-left:10px;font-size:13px;line-height:1.45;display:flex;flex-direction:column;gap:2px} .scores div.hh{border:0;padding:0} .scores b{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#6d6f9c}
'''
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{T1}{T2}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-tips.html', 'w').write(html)
print('ok')
