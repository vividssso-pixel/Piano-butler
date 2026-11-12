# The Level books (her 12 Nov: "레벨북 따로", Level 0 first): the house in print. For one floor, every room in house order:
# the Handbook blocks its clips point at (re-laid, not cropped), then a short practice sheet. Nothing is written twice:
# blocks come from the built Handbook and Workbook (extract.js -> blocks.json), the order from the house data and the audio cues.
import json, re, sys
B = json.load(open('/tmp/claude-0/lvl/blocks.json'))
D = open('/tmp/claude-0/house/data.js').read().split('\n')
ROOMS = {r['id']: r for r in json.loads(D[0][len('const HB_ROOMS = '):].rstrip(';'))}
FLOORS = json.loads(D[1][len('const HB_FLOORS = '):].rstrip(';'))
_s = open('/mnt/user-data/outputs/books/read/index.html').read()
CH, _ = json.JSONDecoder().raw_decode(_s[_s.index('const CH = ') + 11:]); CH = {c['k']: c for c in CH}
FLOWJS = (lambda t: t[t.index('<script>'):t.index('</script>', t.index('Each topic fills')) + 9])(open('/mnt/user-data/outputs/house-rooms/handbook-time2.html').read())
import re as _r2
def _nofont(c): return _r2.sub(r'@font-face\{[^}]*\}', '', c)
CSS = B['css']['handbook-time2'] + '\n' + '\n'.join(_nofont(B['css'][f]) for f in ('workbook-time2', 'workbook-before', 'workbook-pitch', 'workbook-play', 'workbook-expression', 'handbook-before', 'handbook-pitch', 'handbook-expression', 'handbook-play'))   # the Handbook's own rules last

def keyed(page):   # number repeated keys on a page the way Read & listen does (xlate, xlate2 ...)
    seen, out = {}, []
    for b in B['hb'].get(str(page), []):
        seen[b['key']] = seen.get(b['key'], 0) + 1
        out.append((b['key'] + (str(seen[b['key']]) if seen[b['key']] > 1 else ''), b['html']))
    return out
def wb_ex(prefix, hbpage, titles):   # Workbook exercises by title, from the Learn/Use page of that Handbook page
    out = []
    for k, v in B['wb'].items():
        if not k.startswith(prefix + '|') or not re.search(r'P\.\W*' + str(hbpage) + r'\|', k): continue
        for b in v:
            if b['key'].startswith('ex') and b['title'].strip() in titles: out.append((titles.index(b['title'].strip()), b['html']))
    return [h for _, h in sorted(out)]
ROWBAND = {'semibreve': (0, 68), 'minims': (68, 130), 'crotchets': (130, 192), 'quavers': (192, 256)}
def rows_only(html, rows):   # the note table, only the rows met so far, stacked without gaps
    i, j = html.index('<svg'), html.index('</svg>') + 6; svg = html[i:j]
    body = svg[svg.index('>') + 1:-6]
    els = re.findall(r'<text[^>]*>.*?</text>', body, flags=re.S)
    keep = [r for r in ROWBAND if r in rows]; out = ''; dy = 0
    for r in ROWBAND:
        a, b_ = ROWBAND[r]
        if r not in keep: continue
        sel = [e for e in els if e.startswith('<text') and a <= float(re.search(r' y="([\d.]+)"', e).group(1)) < b_]
        if r == keep[0] and any('its rest' in e for e in els): sel += [e for e in els if 'its rest' in e and e not in sel]
        shift = a - dy; out += f'<g transform="translate(0,{-shift})">' + ''.join(sel) + '</g>'; dy += b_ - a
    new = f'<svg viewBox="0 0 640 {dy + 6}" style="width:100%;max-width:640px">{out}</svg>'
    h = html[:i] + new + html[j:]
    return h if 'semibreve' in rows else re.sub(r'<p class="hcap">.*?</p>', '', h)
SKIP = ('kick', 'links')
def room_blocks(r):
    c = CH[r['ch']]; clips = [c['clips'][n - 1] for n in r['clips']] if r.get('clips') else c['clips']
    order = []
    for k in clips:
        for l in k['l']:
            cu = l.get('cue') or {}
            if cu.get('p') and cu.get('r') and (cu['p'], cu['r']) not in order: order.append((cu['p'], cu['r']))
    out = []
    for p, key in order:
        if key in SKIP or key.startswith('h:'): continue
        h = dict(keyed(p)).get(key)
        if not h: continue
        if r.get('rows') and 'semibreve' not in r['rows'] and key in ('lead', 'secret'): continue   # 'each note is half the one above' waits for the semibreve room
        if key == 'hero' and r.get('rows') and p == 53: h = rows_only(h, r['rows'].split(','))
        out.append((key, h))
    return out
def learn_blocks(r):   # her 12 Nov ("단순하게"): one idea per room: its secret, its picture, one example, one Try it
    bl = room_blocks(r); pick = []
    for want in ('secret', 'hero', 'ex', 'try10'):
        h = next((h for k, h in bl if (k.startswith('ex') and k[2:].isdigit() if want == 'ex' else k == want)), None)
        if h and h not in pick: pick.append(h)
    return pick

# ---- practice sheets: Workbook exercises for whole chapters and slices, new sheets for the one-note steps ----
G = lambda s, z=34: f'<span style="font-family:NM;font-size:{z}px;line-height:1;color:#26296b">{s}</span>'
CR, MI, DM, SB, RC, RM, RS = '𝅘𝅥', '𝅗𝅥', '𝅗𝅥.', '𝅝', '𝄽', '𝄼', '𝄻'
BOX, LINE = '<span class="ab"></span>', '<span class="al"></span>'
DONE = lambda x: f'<b class="done2">{x}</b>'
def ex(n, title, how, body, stars=1): return f'<div class="ex2"><div class="eh"><span class="en">{n}</span><b>{title}</b><span class="el">{"★" * stars}<span class="so">{"★" * (3 - stars)}</span></span></div><p class="how">{how}</p>{body}</div>'
def grid(cells, cols): return f'<div class="lvg" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(f'<div>{a}<span>{b}</span></div>' for a, b in cells) + '</div>'
STEP = {
 'hbr-T2': [ex(1, 'How many beats?', 'Write the number of beats under each one. The first is done.', grid([(G(CR), DONE('1')), (G(RC), BOX), (G(CR), BOX), (G(RC), BOX)], 4)),
            ex(2, 'Play and count', 'Say the counts out loud and play: a crotchet is play, a rest is shh. Write 1 2 3 4 under the bar.', grid([(G(CR), DONE('1')), (G(CR), BOX), (G(RC), BOX), (G(CR), BOX)], 4), 2),
            ex(3, 'Draw it', 'Draw four crotchets, then two crotchet rests (a little lightning bolt).', '<div class="lvdraw"></div>', 2)],
 'hbr-T2-s2': [ex(1, 'One beat or two?', 'Write 1 or 2 under each. The first is done.', grid([(G(MI), DONE('2')), (G(CR), BOX), (G(RM), BOX), (G(RC), BOX), (G(MI), BOX)], 5)),
               ex(2, 'Fill the bar', 'Four beats in each bar. Write the missing note: crotchet or minim. The first is done.', '<table class="lvt"><tr><td>' + G(CR) + ' ' + G(CR) + ' + ?</td><td>' + DONE('minim') + '</td></tr><tr><td>' + G(MI) + ' + ? + ' + G(CR) + '</td><td>' + LINE + '</td></tr><tr><td>' + G(MI) + ' + ?</td><td>' + LINE + '</td></tr></table>', 2),
               ex(3, 'The hat', 'Draw a minim rest: a block sitting on the middle line, like a hat. Then draw two minims.', '<div class="lvdraw"></div>', 2)],
 'hbr-T2-s3': [ex(1, 'How many beats?', 'Write the number of beats. The first is done.', grid([(G(DM), DONE('3')), (G(MI), BOX), (G(CR), BOX), (G(DM), BOX)], 4)),
               ex(2, 'Waltz time', 'Each bar has three beats. Count 1 2 3 and play. Which note fills the whole bar?', grid([(G(DM), LINE), (G(MI) + ' ' + G(CR), LINE), (G(CR) + ' ' + G(CR) + ' ' + G(CR), LINE)], 3), 2),
               ex(3, 'Add the dot', 'Make each minim last three beats: draw the dot after it.', grid([(G(MI), ''), (G(MI), ''), (G(MI), '')], 3), 2)],
 'hbr-T2-s4': [ex(1, 'Name, beats and rest', 'Fill in the table. The first row is done.', '<table class="lvt"><tr><th>Note</th><th>Name</th><th>Beats</th><th>Its rest</th></tr>' + ''.join(f'<tr><td>{G(n)}</td><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for n, a, b, c in ((SB, DONE('semibreve'), DONE('4'), G(RS, 28)), (MI, LINE, BOX, BOX), (CR, LINE, BOX, BOX), (DM, LINE, BOX, '—'))) + '</table>'),
               ex(2, 'Coat or hat?', 'The semibreve rest hangs like a coat; the minim rest sits like a hat. Write coat or hat.', grid([(G(RS), DONE('coat')), (G(RM), LINE), (G(RS), LINE), (G(RM), LINE)], 4)),
               ex(3, 'Four beats', 'Each bar must add up to four beats. Write the missing note.', '<table class="lvt"><tr><td>' + G(MI) + ' + ' + G(CR) + ' + ?</td><td>' + DONE('crotchet') + '</td></tr><tr><td>' + G(DM) + ' + ?</td><td>' + LINE + '</td></tr><tr><td>? (one note)</td><td>' + LINE + '</td></tr></table>', 2)],
}
WB = {   # room -> (workbook, handbook page of the Learn/Use page, exercise titles)
 'hbr-B1': [('workbook-before', 18, ['Finger numbers', 'Which hand is round?', 'Too low, too high, or right?', 'The 30-second check'])],
 'hbr-P1': [('workbook-pitch', 22, ['Twos and threes', 'Name the keys', 'Round and round'])],
 'hbr-L1': [('workbook-play', 163, ['Five-finger position', 'C major, right hand', 'Play it'])],
 'hbr-P2': [('workbook-pitch', 27, ['The clefs', 'Line or space?', 'Treble or bass?']), ('workbook-pitch', 28, ['Which staff?', 'The grand staff'])],
 'hbr-T1': [('workbook-time2', 50, ['Count it', 'Add the bar lines', 'Clap and count'])],
 'hbr-E1': [('workbook-expression', 76, ['Say it', 'Play it'])],
}
def practice(rid):
    if rid in STEP: xs = STEP[rid]
    else: xs = [h for f, p, t in WB.get(rid, []) for h in wb_ex(f, p, t)]
    return [re.sub(r'<span class="en">\d+</span>', f'<span class="en">{i + 1}</span>', h, count=1) for i, h in enumerate(xs)]

def section(inner, n, flow): return f'<section class="pg" data-flow="{flow}"><div class="top"><span>THE PIANO BUTLER · LEVEL BOOK</span><span>{RIGHT}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'
def chain(key, head, blocks, n0, cont='continued', pages=4):
    first = section(head + ''.join(blocks), n0, 'A' + key)
    rest = ''.join(section(f'<div class="kick fk2">{cont}</div>', n0 + i, 'BCDE'[i - 1] + key) for i in range(1, pages))
    return first + rest
def build(floor_i, name, line):
    global RIGHT; RIGHT = name.upper()
    ids = FLOORS[floor_i]['ids']; out = []; toc = []; n = 2
    for i, rid in enumerate(ids, 1):
        r = ROOMS[rid]; title = r['en'] if not r.get('again') else r['en'] + ': ' + r['again'][0]
        toc.append((i, title))
        head = f'<div class="kick">{name} · Room {i}</div><h1>{title}</h1><p class="lead lvl">Handbook pp. {r["pages"]} · listen in the app: Room {i}</p>'
        pr = practice(rid)[:3]   # one spread per room: Learn on the left, three exercises on the right
        out.append(section(head + ''.join(learn_blocks(r)), n, 'L' + rid)); n += 1
        out.append(section(f'<div class="kick">{name} · Room {i} · Practise</div><h1>Practise</h1>' + ''.join(pr), n, 'P' + rid)); n += 1
    cover = f'''<section class="pg part2"><div class="pframe"><div class="pk">The Piano Butler · Level book</div><div class="pt">{name}</div><div class="pdv"></div>
<p class="pl">{line}</p><div class="pin"><div class="pih">The rooms</div>{"".join(f'<div class="tr"><span>{i} · {t}</span><span class="dots"></span><span></span></div>' for i, t in toc)}</div></div></section>'''
    extra = """.lvl{font-size:13px!important;color:#6d6f9c} .lvg{display:grid;gap:10px;margin:8px 0} .lvg>div{display:flex;flex-direction:column;align-items:center;gap:6px;border:1.5px solid #e3e1ee;border-radius:8px;padding:10px 4px}
.lvt{width:100%;border-collapse:collapse;margin:8px 0;font-size:15px} .lvt td,.lvt th{border-bottom:1px solid #e3e1ee;padding:8px 6px;text-align:left} .lvt th{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#6d6f9c}
.lvdraw{height:120px;margin:8px 0;background:repeating-linear-gradient(#fff 0 18px,#26296b 18px 19px,#fff 19px 24px);background-size:100% 24px;border-radius:4px;opacity:.55}
section.pg.lvempty{display:none} h3.lvpr{margin-top:18px;padding-top:10px;border-top:2px solid #26296b;font-size:20px}"""
    prune = """<script>(async()=>{try{await document.fonts.ready}catch(e){}
document.querySelectorAll('section.pg .body').forEach(b=>{const s=b.closest('section'),f=s.querySelector('.foot');if(!f)return;const lim=f.getBoundingClientRect().top-20,top=b.getBoundingClientRect().top;let m=0;[...b.children].forEach(c=>{const r=c.getBoundingClientRect();if(r.height)m=Math.max(m,r.bottom)});if(m>lim){b.style.zoom=Math.max(.6,(lim-top)/(m-top)).toFixed(3);}});
document.body.dataset.pruned='1';})();</script>"""
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body>{cover}{"".join(out)}{prune}</body></html>'
    fn = f'/mnt/user-data/outputs/house-rooms/levelbook-{name.lower().replace(" ", "").replace("½", "half")}.html'
    open(fn, 'w').write(html); return fn
if __name__ == '__main__':
    print(build(0, 'Level 0', 'Ten rooms: sitting and hands, the keyboard, fingering, the staff, the beat, notes and rests one at a time, loud and soft. Read each room, listen to it in the app, then practise.'))
