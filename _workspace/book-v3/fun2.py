# Rhythm games, batch 2
import random
exec(open('/tmp/claude-0/pk/fun.py').read())
R = random.Random(11)
pages = []
def add(title, how, inner, kind='FREE PRINTABLE'):
    pages.append(fpage(kind, title, how, inner, len(pages) + 5))
CUT = '<span class="cut">✂ cut along the lines</span>'

# 5 Memory cards
pairs = [(['sb'], 'semibreve<br><b>4</b>'), (['m'], 'minim<br><b>2</b>'), (['c'], 'crotchet<br><b>1</b>'), (['q', 'q'], 'two quavers<br><b>1</b>'), (['dm'], 'dotted minim<br><b>3</b>'), (['rc'], 'crotchet rest<br><b>1</b>'), (['rm'], 'minim rest<br><b>2</b>'), (['dc', 'q'], 'dotted crotchet + quaver<br><b>2</b>')]
mc = [f'<div class="mem">{pat(p, 42)}</div>' for p, _ in pairs] + [f'<div class="mem tx">{t}</div>' for _, t in pairs]
R.shuffle(mc)
add('Rhythm memory', 'For two to four players. Cut out the 16 cards and lay them face down. Turn over two: a rhythm and its name and beats make a pair. Clap the rhythm to keep the pair. Most pairs wins.',
    f'<h3>Cards {CUT}</h3><div class="memg">{"".join(mc)}</div><p class="sm">Harder: play without the names, matching rhythms that last the same number of beats.</p>')

# 6 Dominoes: chain where each tile's rhythm lasts as many beats as the next tile's number
chain = [(4, ['m', 'm']), (4, ['dm', 'c']), (4, ['sb']), (4, ['c', 'c', 'm']), (4, ['m', 'c', 'c']), (4, ['c', 'rc', 'm'])]
nums = [1, 2, 3, 4, 2, 3, 1, 4, 3, 2, 4, 1, 3, 4, 2]
pats = {1: [['c'], ['q', 'q'], ['rc']], 2: [['m'], ['c', 'c'], ['dc', 'q']], 3: [['dm'], ['m', 'c'], ['c', 'c', 'c']], 4: [['sb'], ['m', 'm'], ['dm', 'c']]}
tiles = []
for i, n in enumerate(nums):
    nxt = nums[(i + 1) % len(nums)]
    tiles.append(f'<div class="dom"><span class="dn">{n}</span><span class="dv"></span><span class="dp">{pat(R.choice(pats[nxt]), 34)}</span></div>')
add('Rhythm dominoes', 'Cut out the dominoes. Join them in a ring: a rhythm must touch a number that matches how many beats it lasts. Clap each rhythm as you place it.',
    f'<h3>Dominoes {CUT}</h3><div class="domg">{"".join(tiles)}</div><p class="sm">Two players: share out the dominoes and take turns to add one to either end. If you cannot go, clap the last rhythm and pass.</p>')

# 7 Word search
WORDS = ['MINIM', 'CROTCHET', 'QUAVER', 'SEMIBREVE', 'REST', 'TIE', 'DOT', 'BAR', 'BEAT', 'PULSE', 'TEMPO', 'TRIPLET']
S = 13
grid = [[''] * S for _ in range(S)]
dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]
for w in sorted(WORDS, key=len, reverse=True):
    for _ in range(500):
        dr, dc = R.choice(dirs); r = R.randrange(S); c = R.randrange(S)
        cells = [(r + dr * k, c + dc * k) for k in range(len(w))]
        if all(0 <= a < S and 0 <= b < S and grid[a][b] in ('', w[k]) for k, (a, b) in enumerate(cells)):
            for k, (a, b) in enumerate(cells): grid[a][b] = w[k]
            break
    else: raise SystemExit('no place ' + w)
for r in range(S):
    for c in range(S):
        if not grid[r][c]: grid[r][c] = R.choice('ABCDEFGHILMNOPRSTUVY')
ws = ''.join(f'<div class="wsc">{grid[r][c]}</div>' for r in range(S) for c in range(S))
clues = [(['m'], 'MINIM'), (['c'], 'CROTCHET'), (['q'], 'QUAVER'), (['sb'], 'SEMIBREVE'), (['rc'], 'REST')]
cl = ''.join(f'<div class="wcl">{pat(p, 30)}<span class="al"></span></div>' for p, _ in clues)
add('Rhythm word search', 'Twelve rhythm words are hidden across, down and diagonally. First name the five pictures, then find all twelve words.',
    f'<div class="wsg">{ws}</div><div class="two" style="grid-template-columns:1.2fr 1fr"><div><h3>Name them</h3><div class="wcg">{cl}</div></div><div><h3>Also find</h3><p class="wl">TIE · DOT · BAR · BEAT · PULSE · TEMPO · TRIPLET</p></div></div>')

# 8 Rhythm sudoku (4x4)
SYM = [['c', 'c'], ['m'], ['q', 'q', 'c'], ['c', 'rc']]
base = [[0, 1, 2, 3], [2, 3, 0, 1], [1, 0, 3, 2], [3, 2, 1, 0]]
givens = {(0, 0), (1, 1), (2, 0), (2, 2), (2, 3), (3, 0), (3, 2), (3, 3)}
def sud(sol, giv):
    out = ''
    for r in range(4):
        for c in range(4):
            cls = 'sdc' + (' br' if c == 1 else '') + (' bb' if r == 1 else '')
            out += f'<div class="{cls}">{pat(SYM[sol[r][c]], 26) if (r, c) in giv else ""}</div>'
    return f'<div class="sud">{out}</div>'
base2 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 1, 2, 3], [2, 3, 0, 1]]
giv2 = {(0, 0), (0, 1), (2, 1), (2, 2), (3, 1), (3, 3)}
base3 = [[3, 2, 1, 0], [1, 0, 3, 2], [2, 3, 0, 1], [0, 1, 2, 3]]
giv3 = {(0, 2), (1, 1), (1, 3), (2, 0), (2, 1)}
legend = '<div class="leg">' + ''.join(f'<span>{pat(s, 30)}</span>' for s in SYM) + '</div>'
add('Rhythm sudoku', 'Each row, each column and each 2 × 2 box must hold all four rhythms once. Draw the missing ones, then clap each row: it makes two bars of 4/4.',
    legend + f'<div class="sud2"><div><div class="cl3">Puzzle 1 ★</div>{sud(base, givens)}</div><div><div class="cl3">Puzzle 2 ★★</div>{sud(base2, giv2)}</div></div><div class="sud3"><div class="cl3">Puzzle 3 ★★★ (only five clues)</div>{sud(base3, giv3)}</div>')

# 9 Crotchet path maze
M = 7
path = [(0, 0)]
r = c = 0
while (r, c) != (M - 1, M - 1):
    opts_ = [(r + 1, c), (r, c + 1)] if R.random() < .8 else [(r, c + 1), (r + 1, c)]
    for nr, nc in opts_:
        if nr < M and nc < M: r, c = nr, nc; path.append((r, c)); break
ps = set(path)
mz = ''
for a in range(M):
    for b in range(M):
        k = R.choice(['c', 'rc']) if (a, b) in ps else R.choice(['m', 'q', 'sb', 'dm', 'sq', 'dc'])
        cls = 'mzc' + (' st' if (a, b) == (0, 0) else '') + (' en' if (a, b) == (M - 1, M - 1) else '')
        mz += f'<div class="{cls}">{g(k, 40)}</div>'
add('One-beat path', 'Get from START to FINISH stepping only on squares worth exactly one beat (a crotchet or a crotchet rest). Move up, down, left or right, never diagonally. Then clap your path as one long rhythm.',
    f'<div class="maze2">{mz}</div><div class="mzl"><span>START: top left</span><span>FINISH: bottom right</span></div>')

# 10 Dice composer
COLS = ['Bar 1', 'Bar 2', 'Bar 3', 'Bar 4']
BARS = [[['c', 'c', 'c', 'c'], ['m', 'c', 'c'], ['c', 'c', 'm'], ['q', 'q', 'c', 'c', 'c'], ['c', 'rc', 'c', 'c'], ['m', 'm']],
        [['c', 'q', 'q', 'm'], ['m', 'm'], ['c', 'c', 'c', 'rc'], ['dm', 'c'], ['q', 'q', 'q', 'q', 'm'], ['c', 'm', 'c']],
        [['c', 'c', 'c', 'c'], ['q', 'q', 'c', 'q', 'q', 'c'], ['m', 'c', 'rc'], ['c', 'c', 'm'], ['dc', 'q', 'm'], ['rc', 'c', 'c', 'c']],
        [['sb'], ['m', 'm'], ['dm', 'rc'], ['m', 'rm'], ['sb'], ['c', 'c', 'm']]]
rows = ''.join(f'<tr><td class="die"><span class="dface">{i + 1}</span></td>' + ''.join(f'<td>{pat(BARS[b][i], 26)}</td>' for b in range(4)) + '</tr>' for i in range(6))
add('The dice composer', 'Two hundred years ago, composers sold dice games for writing music by chance. Roll a die four times: the first roll chooses bar 1, the second bar 2, and so on. Copy your bars below, clap them, then play them on one key, or on a five-finger scale.',
    f'<table class="ht dice"><thead><tr><th></th>' + ''.join(f'<th>{c}</th>' for c in COLS) + f'</tr></thead><tbody>{rows}</tbody></table><h3>My piece</h3>' + staff('4/4', 4) + '<div class="tickrow"><span>Clapped it · Played it · Played it to someone</span>' + ticks(3) + '</div><p class="sm">There are 6 × 6 × 6 × 6 = 1,296 possible pieces.</p>')

# 11 Rhythm menu
MENU = [('Tea', ['c'], 'tea'), ('Juice', ['c'], 'juice'), ('Coffee', ['q', 'q'], 'cof-fee'), ('Cocoa', ['q', 'q'], 'co-coa'), ('Lemonade', ['q', 'q', 'c'], 'lem-on-ade'), ('Pancakes', ['q', 'q', 'c'], 'pan-cakes'), ('Ice cream', ['c', 'c'], 'ice cream'), ('Watermelon', ['sq', 'sq', 'sq', 'sq'], 'wa-ter-mel-on'), ('Pie', ['m'], 'pie… (long)')]
menu = ''.join(f'<div class="mi"><b>{n}</b><span class="dots2"></span>{pat(p, 26)}<i>{s}</i></div>' for n, p, s in MENU)
add('The rhythm café', 'Every dish on the menu has a rhythm: say it and clap it. Then order a meal that fills exactly one bar of 4/4 (4 beats). Write your order and its rhythm, and clap it to the waiter.',
    f'<div class="menu"><div class="mh">Café Rubato · Menu</div>{menu}</div><h3>My orders</h3>' + ''.join(f'<div class="ord"><span class="wn">{i}</span><span class="al"></span><span class="al"></span></div>' for i in range(1, 4)) + '<p class="sm">Make your own menu: your favourite foods, or your family’s names.</p>')

# 12 Escape room
LOCKS = [('Lock 1', 'How many beats in this bar?', pat(['m', 'c', 'c'], 30)), ('Lock 2', 'How many rests?', pat(['c', 'rc', 'c', 'rc', 'rc', 'c'], 28)), ('Lock 3', 'Beats in a dotted minim?', pat(['dm'], 34)), ('Lock 4', 'How many quavers make a semibreve?', pat(['sb'], 34))]
lk = ''.join(f'<div class="lock"><div class="lh">{n}</div><div class="lp">{p}</div><p>{q}</p><span class="ab big2"></span></div>' for n, q, p in LOCKS)
add('Rhythm escape room', 'You are locked in the practice room. Each lock gives one digit. Solve all four and write the code on the door to escape.',
    f'<div class="locks">{lk}</div><div class="door"><b>The door</b><div class="code">' + '<span class="ab big2"></span>' * 4 + '</div></div><p class="sm">Answer, upside down: <span class="ud">4 3 3 8</span></p>')

# 13 Tic-tac-toe
TTT = [['c', 'c', 'm'], ['q', 'q', 'c', 'm'], ['m', 'm'], ['c', 'rc', 'c', 'c'], ['sb'], ['dm', 'c'], ['c', 'q', 'q', 'm'], ['m', 'c', 'c'], ['rc', 'c', 'c', 'c']]
tt = ''.join(f'<div class="tt3">{pat(p, 30)}</div>' for p in TTT)
add('Rhythm noughts and crosses', 'Two players. To claim a square, clap its rhythm correctly while counting aloud; your partner judges. Claimed: draw your O or X. Three in a row wins.',
    '<div class="two" style="grid-template-columns:1fr 1fr;gap:26px 30px">' + ''.join(f'<div><div class="cl3">{lab}</div><div class="tttg">{"".join(f"<div class=tt3>{pat(p, 28)}</div>" for p in order)}</div></div>' for lab, order in (('Game 1: clap', TTT), ('Game 2: clap', TTT[::-1]), ('Game 3: play on one key', TTT[3:] + TTT[:3]), ('Game 4: play it, eyes closed', TTT[6:] + TTT[:6]))) + '</div>')

css += f'''
.memg{{display:grid;grid-template-columns:repeat(4,1fr);border-top:1.5px dashed #9a9cc4;border-left:1.5px dashed #9a9cc4}} .mem{{height:180px;display:flex;flex-direction:column;gap:6px;align-items:center;justify-content:center;border-right:1.5px dashed #9a9cc4;border-bottom:1.5px dashed #9a9cc4;background:#fff;text-align:center;font-size:15px}} .mem.tx b{{font-size:26px;color:{C}}}
.domg{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}} .dom{{display:flex;align-items:center;height:118px;border:2px solid {N};border-radius:10px;background:#fff}} .dn{{flex:1;text-align:center;font:700 34px 'PF',Georgia,serif;color:{C}}} .dv{{width:2px;align-self:stretch;background:{N}}} .dp{{flex:1.6;display:flex;justify-content:center}}
.wsg{{display:grid;grid-template-columns:repeat(13,1fr);border:1.5px solid {N}}} .wsc{{aspect-ratio:1.25;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:19px;border:.4px solid #e2ddd0;background:#fff}}
.wcl{{display:flex;align-items:center;gap:10px;padding:5px 0}} .wcl .al{{flex:1;height:26px}} .wl{{font-weight:700;letter-spacing:.06em;line-height:1.8}}
.leg{{display:flex;gap:30px;justify-content:center;margin:6px 0 14px}} .leg span{{border:1.5px solid {N};padding:8px 14px;background:#fff}}
.sud2{{display:grid;grid-template-columns:1fr 1fr;gap:30px}} .sud3{{width:50%;margin:16px auto 0}} .sud3 .sdc{{height:72px}} .sud2 .sdc{{height:72px}} .sud{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border:3px solid {N}}} .sdc{{height:150px;min-width:0;display:flex;align-items:center;justify-content:center;border:1px solid #9a9cc4;background:#fff}} .sdc.br{{border-right:3px solid {N}}} .sdc.bb{{border-bottom:3px solid {N}}}
.maze2{{display:grid;grid-template-columns:repeat(7,1fr);border:2px solid {N};max-width:678px;margin:0 auto}} .mzc{{aspect-ratio:1;display:flex;align-items:center;justify-content:center;border:1px solid #c9cbe0;background:#fff}} .mzc.st{{background:#e3f1ea}} .mzc.en{{background:#fdf0ec}}
.mzl{{display:flex;justify-content:space-between;max-width:678px;margin:6px auto 0;font-weight:700;font-size:13px;color:{MUTE}}}
.dice td{{text-align:center;padding:8px 4px}} .die{{width:56px}} .dface{{display:inline-flex;width:34px;height:34px;border:2px solid {N};border-radius:7px;align-items:center;justify-content:center;font-weight:700;font-size:17px}} .dice td{{padding:12px 4px}} .dice th{{text-align:center}}
.menu{{border:1.5px solid {N};outline:.6px solid {N};outline-offset:-6px;padding:20px 30px;background:#fff}} .mh{{font-family:'PF',Georgia,serif;font-size:24px;text-align:center;margin-bottom:10px}} .mi{{display:flex;align-items:center;gap:10px;padding:6px 0;font-size:16px}} .dots2{{flex:1;border-bottom:1.5px dotted #b9bbd3;transform:translateY(-4px)}} .mi i{{width:120px;font-size:13px;color:{MUTE}}}
.ord{{display:grid;grid-template-columns:24px 1fr 1fr;gap:16px;align-items:end;padding:4px 0}} .ord .al{{height:30px}}
.locks{{display:grid;grid-template-columns:1fr 1fr;gap:14px}} .lock{{border:2px solid {N};border-radius:12px;padding:14px;background:#fff;text-align:center}} .lh{{font-weight:700;color:{C};letter-spacing:.12em;text-transform:uppercase;font-size:12px}} .lp{{margin:10px 0;display:flex;justify-content:center}} .ab.big2{{width:54px;height:54px}}
.door{{margin:18px auto 0;width:340px;border:3px solid {N};border-radius:12px 12px 0 0;padding:18px;text-align:center;background:#fff}} .code{{display:flex;justify-content:center;gap:10px;margin-top:10px}}
.tttg{{display:grid;grid-template-columns:repeat(3,1fr);border:2px solid {N}}} .tt3{{height:100px;display:flex;align-items:center;justify-content:center;border:1.5px solid {N};background:#fff}}
'''
open('/mnt/user-data/outputs/house-rooms/rhythm-games2.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{"".join(pages)}</body></html>')
print('ok', len(pages))
