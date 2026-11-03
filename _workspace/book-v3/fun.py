# Fun formats for the activity bank and free printables: colour-by-beats picture, secret code, bingo, board game
import json, random
exec(open('/tmp/claude-0/pk/wbtime2.py').read())
random.seed(7)
def g(k, h=26):
    return gin('r', k[1:], h) if k.startswith('r') else gin('n', k, h)
def pat(keys, h=26): return '<span class="pat">' + ''.join(g(k, h) for k in keys) + '</span>'
def fpage(kind, title, how, inner, n, foot=True):
    ff = f'<div class="ffoot"><span>{bow}</span><span>More at <b>thepianobutler.com</b></span><span>Free to print and share for teaching. © Piano Butler</span></div>' if foot else ''
    return f'''<section class="pg"><div class="top"><span>PIANO BUTLER · {kind}</span><span>RHYTHM GAMES</span></div><div class="rule"></div>
<div class="body"><div class="kick">Rhythm game</div><h1>{title}</h1><p class="lead">{how}</p>{inner}</div>{ff}<div class="foot"><span>{n}</span></div></section>'''
bow = f'<svg viewBox="0 0 40 24" style="width:30px;height:18px"><path d="M2 3 L18 12 L2 21 Z" fill="none" stroke="{N}" stroke-width="2" stroke-linejoin="round"/><path d="M38 3 L22 12 L38 21 Z" fill="none" stroke="{N}" stroke-width="2" stroke-linejoin="round"/><circle cx="20" cy="12" r="2.6" fill="{C}"/></svg>'

# 1. Colour by beats: the hidden picture is the Piano Butler bow tie
MASK = ['................',
        '.##..........##.',
        '.####......####.',
        '.######..######.',
        '.######OO######.',
        '.######OO######.',
        '.######..######.',
        '.####......####.',
        '.##..........##.',
        '................']
cells = ''
for row in MASK:
    for ch in row:
        k = {'#': random.choice(['c', 'rc']), 'O': random.choice(['m', 'rm']), '.': random.choice(['q', 'sq', 'rq'])}[ch]
        cells += f'<div class="mc">{g(k, 24)}</div>'
key = '<div class="key">' + ''.join(f'<div><span class="sw" style="background:{c}"></span>{t}</div>' for c, t in ((N, '1 beat: navy'), (C, '2 beats: coral'), ('#fff', 'less than 1 beat: leave white'))) + '</div>'
P1 = fpage('FREE PRINTABLE', 'Colour by beats', 'Every square holds a note or a rest. Colour it by how many beats it lasts (crotchet = 1 beat). Something will appear.',
           key + f'<div class="mosaic">{cells}</div><h3>Then</h3><p>Clap the top row from left to right, counting aloud: every note and rest in its place. Then the bottom row, backwards.</p><p class="sm">Answer, upside down: <span class="ud">the Piano Butler’s bow tie</span></p>', 1)

# 2. Secret code: each one-bar rhythm stands for a letter
CODE = {'P': ['m', 'm'], 'I': ['c', 'c', 'c', 'c'], 'A': ['sb'], 'N': ['c', 'c', 'm'], 'O': ['m', 'c', 'c'], 'T': ['c', 'm', 'c'], 'E': ['c', 'rc', 'c', 'c'], 'S': ['rm', 'm'], 'L': ['c', 'c', 'c', 'rc'], 'Y': ['dm', 'c']}
keyrows = ''.join(f'<div class="ck"><b>{L}</b>{pat(v, 30)}</div>' for L, v in CODE.items())
msg = 'PIANO'
msgcells = ''.join(f'<div class="mcell">{pat(CODE[L], 32)}<span class="al"></span></div>' for L in msg)
msg2 = 'PLAY'
msgcells2 = ''.join(f'<div class="mcell">{pat(CODE[L], 32)}<span class="al"></span></div>' for L in msg2)
P2 = fpage('FREE PRINTABLE', 'The secret code', 'Each bar of 4/4 stands for a letter. Clap each bar of the message, find it in the code book, and write its letter underneath.',
           f'<h3>Code book</h3><div class="codebook">{keyrows}</div><h3>Message 1</h3><div class="msg">{msgcells}</div><h3>Message 2</h3><div class="msg">{msgcells2}</div>'
           f'<h3>Your turn</h3><p>Write your own name in rhythm code, then give it to a friend to decode.</p><div class="msg">' + '<div class="mcell"><span class="blank"></span><span class="al"></span></div>' * 5 + '</div>'
           '<p class="sm">Answers, upside down: <span class="ud">PIANO · PLAY</span></p>', 2)

# 3. Rhythm bingo
POOL = [['c', 'c'], ['m'], ['q', 'q', 'c'], ['c', 'rc'], ['rc', 'c'], ['q', 'q', 'q', 'q'], ['c', 'q', 'q'], ['dc', 'q'], ['rc', 'q', 'q'], ['q', 'q', 'rc'], ['m'], ['c', 'c']]
uniq = []
for p in POOL:
    if p not in uniq: uniq.append(p)
def card(seed):
    r = random.Random(seed); cs = r.sample(uniq, 9)
    return '<div class="bingo">' + ''.join(f'<div class="bc">{pat(c, 30) if i != 4 else "<b class=free>FREE</b>"}</div>' for i, c in enumerate(cs)) + '</div>'
calls = ''.join(f'<div class="call">{pat(c, 24)}</div>' for c in uniq)
P3 = fpage('FREE PRINTABLE', 'Rhythm bingo', 'For two to twenty players. The caller cuts out the call cards and claps one at a time (each lasts two beats). Players mark the matching square. Three in a row wins: clap your line back to prove it.',
           f'<div class="cards2">' + ''.join(f'<div><div class="cl3">Player card {L}</div>{card(i)}</div>' for i, L in enumerate('ABCD')) + '</div>'
           f'<h3>Caller’s cards <span class="cut">✂ cut along the lines</span></h3><div class="calls">{calls}</div>', 3)

# 4. Board game: race to the double bar
SQ = [['c', 'c', 'c', 'c'], ['m', 'm'], 'REST', ['c', 'c', 'm'], ['q', 'q', 'c', 'm'], ['sb'], 'FERM', ['c', 'rc', 'c', 'c'], ['dm', 'c'], ['q', 'q', 'q', 'q', 'm'], 'BACK', ['c', 'm', 'c'],
      ['dc', 'q', 'm'], ['rc', 'c', 'c', 'c'], 'FERM', ['q', 'q', 'c', 'q', 'q', 'c'], ['m', 'c', 'c'], 'REST', ['c', 'q', 'q', 'm'], ['dc', 'q', 'c', 'c'], 'BACK', ['q', 'q', 'q', 'q', 'q', 'q', 'c'], ['m.', 'c'] if False else ['dm', 'c'], 'END']
SPEC = {'REST': ('Rest', 'miss a turn'), 'FERM': ('Pause', 'roll again'), 'BACK': ('Repeat', 'back 3'), 'END': ('Final bar', 'you win')}
order = []
for r in range(4):
    row = list(range(r * 6, r * 6 + 6))
    order += row if r % 2 == 0 else row[::-1]
grid = [''] * 24
for pos, i in enumerate(order):
    s = SQ[i]
    if isinstance(s, str):
        t, sub = SPEC[s]; inner = f'<b class="sp">{t}</b><span class="sps">{sub}</span>'
    else: inner = pat(s, 30 if len(s) <= 4 else 24)
    grid[pos] = f'<div class="bsq{" spc" if isinstance(s, str) else ""}"><span class="bn">{i + 1}</span>{inner}</div>'
P4 = fpage('FREE PRINTABLE', 'Race to the double bar', 'Two to four players, one die, a counter each. Roll and move. Clap the rhythm on your square while counting aloud: if another player agrees it was right, stay; if not, go back to where you were. First to the final bar wins.',
           f'<div class="board">{"".join(grid)}</div><div class="rules"><div><b>Start</b> on square 1.</div><div><b>Harder:</b> play the rhythm on the piano instead of clapping, at ♩ = 80.</div><div><b>Team game:</b> one claps, the other counts aloud.</div></div>', 4)

css += f'''
.ffoot{{position:absolute;left:58px;right:58px;bottom:56px;display:flex;align-items:center;gap:12px;border-top:1.5px solid {N};padding-top:9px;font-size:12px;color:#3d4080}} .ffoot span:last-child{{margin-left:auto;color:{MUTE};font-size:10.5px}}
.pat{{display:inline-flex;align-items:flex-end;gap:2px}} .ud{{display:inline-block;transform:rotate(180deg)}}
.key{{display:flex;gap:22px;margin:4px 0 10px;font-size:14px;font-weight:700}} .key div{{display:flex;align-items:center;gap:8px}} .sw{{width:22px;height:22px;border:1.5px solid {N};display:inline-block}}
.mosaic{{display:grid;grid-template-columns:repeat(16,1fr);border:1.5px solid {N}}} .mc{{aspect-ratio:1;border:.6px solid #c9cbe0;display:flex;align-items:center;justify-content:center;background:#fff}}
.codebook{{display:grid;grid-template-columns:1fr 1fr;gap:6px 26px}} .ck{{display:flex;align-items:center;gap:14px;border-bottom:.6px solid #e2ddd0;padding:4px 0}} .ck b{{width:24px;font-size:18px;color:{C}}}
.msg{{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}} .mcell{{border:1px solid #e2ddd0;background:#fff;padding:10px 6px 8px;display:flex;flex-direction:column;align-items:center;gap:10px}} .mcell .al{{width:70%;height:22px}} .blank{{height:30px}}
.cards2{{display:grid;grid-template-columns:1fr 1fr;gap:20px}} .cl3{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTE};margin-bottom:4px}}
.bingo{{display:grid;grid-template-columns:repeat(3,1fr);border:2px solid {N}}} .bc{{height:78px;border:1px solid {N};display:flex;align-items:center;justify-content:center;background:#fff}} .free{{color:{C};letter-spacing:.14em}}
.cut{{font-size:12px;color:{MUTE};font-weight:400;margin-left:10px}} .calls{{display:grid;grid-template-columns:repeat(5,1fr);border-top:1.5px dashed #9a9cc4;border-left:1.5px dashed #9a9cc4}} .call{{height:62px;display:flex;align-items:center;justify-content:center;border-right:1.5px dashed #9a9cc4;border-bottom:1.5px dashed #9a9cc4;background:#fff}}
.board{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:6px}} .bsq{{position:relative;min-width:0;height:150px;overflow:hidden;border:1.6px solid {N};background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:14px 4px 4px}} .bsq.spc{{background:#fdf0ec;border-color:{C}}}
.bn{{position:absolute;left:5px;top:3px;font-size:11px;font-weight:700;color:{MUTE}}} .sp{{font-size:15px;color:{C}}} .sps{{font-size:11.5px;color:{MUTE}}}
.rules{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:12px;font-size:13.5px;line-height:1.45}}
'''
open('/mnt/user-data/outputs/house-rooms/rhythm-games.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{P1}{P2}{P3}{P4}</body></html>')
print('ok')
