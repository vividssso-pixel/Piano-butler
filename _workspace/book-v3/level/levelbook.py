# The Level books (her 12 Nov: "레벨북 따로", Level 0 first): the house in print. For one floor, every room in house order:
# the Handbook blocks its clips point at (re-laid, not cropped), then a short practice sheet. Nothing is written twice:
# blocks come from the built Handbook and Workbook (extract.js -> blocks.json), the order from the house data and the audio cues.
import json, re, sys, io, segno
SITE = 'https://thepianobutler.com/books/read/'
def listen_url(r):   # her 12 Nov: the room in Read & listen, only its clips and the note rows met so far (same link the app's room uses)
    q = 'ch=' + r['ch'] + ('&clips=' + ','.join(map(str, r['clips'])) if r.get('clips') else '') + ('&rows=' + r['rows'] if r.get('rows') else '')
    return SITE + '?' + q
def qr(url):
    b = io.BytesIO(); segno.make(url, error='m').save(b, kind='svg', scale=1, border=0, dark='#26296b', xmldecl=False, svgns=True)
    return b.getvalue().decode().replace('<svg ', '<svg class="qrs" ', 1)
B = json.load(open('/tmp/claude-0/lvl/blocks.json'))
D = open('/tmp/claude-0/house/data.js').read().split('\n')
ROOMS = {r['id']: r for r in json.loads(D[0][len('const HB_ROOMS = '):].rstrip(';'))}
FLOORS = json.loads(D[1][len('const HB_FLOORS = '):].rstrip(';'))
_s = open('/mnt/user-data/outputs/books/read/index.html').read()
CH, _ = json.JSONDecoder().raw_decode(_s[_s.index('const CH = ') + 11:]); CH = {c['k']: c for c in CH}
FLOWJS = (lambda t: t[t.index('<script>'):t.index('</script>', t.index('Each topic fills')) + 9])(open('/mnt/user-data/outputs/house-rooms/handbook-time2.html').read())
import re as _r2
def _nofont(c): return _r2.sub(r'@font-face\{[^}]*\}', '', c)
CSS = B['css']['handbook-time2'] + '\n' + '\n'.join(_nofont(B['css'][f]) for f in ('workbook-time2', 'workbook-before', 'workbook-pitch', 'workbook-play', 'workbook-expression', 'workbook-scales', 'workbook-harmony', 'handbook-before', 'handbook-pitch', 'handbook-expression', 'handbook-scales', 'handbook-harmony', 'handbook-play'))   # the Handbook's own rules last

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
    bl = room_blocks(r); o = LEARN.get(r['id'], {}); got = {}
    for want in ('secret', 'hero', 'ex', 'try10'):
        h = next((h for k, h in bl if (k.startswith('ex') and k[2:].isdigit() if want == 'ex' else k == want)), None)
        if h: got[want] = h
    if o.get('hero_p'):
        h = dict(keyed(o['hero_p'])).get('hero')
        if h: got['hero'] = rows_only(h, r['rows'].split(',')) if r.get('rows') else h
    if 'secret' in o: got['secret'] = secret_l(o['secret'])
    if 'ex' in o: got['ex'] = inact_l(*o['ex'])
    if 'try' in o: got['try10'] = try_l(*o['try'])
    for a, b_ in o.get('sub', []): got = {k: v.replace(a, b_) for k, v in got.items()}
    if got.get('ex'): got['ex'] = re.sub(r'(<div class="bh">Example) \d+', r'\1', got['ex'], count=1)
    pick = []
    for want in ('secret', 'hero', 'ex', 'try10'):
        if got.get(want) and got[want] not in pick: pick.append(got[want])
    return pick

# ---- practice sheets: Workbook exercises for whole chapters and slices, new sheets for the one-note steps ----
CR, MI, DM, SB, RC, RM, RS = '𝅘𝅥', '𝅗𝅥', '𝅗𝅥.', '𝅝', '𝄽', '𝄼', '𝄻'
BOX, LINE = '<span class="ab"></span>', '<span class="al"></span>'
G = lambda s, z=46: f'<span style="font-family:NM;font-size:{z}px;line-height:1;color:#26296b">{s}</span>'   # review 12 Nov: bigger notes and rests
def rst(kind, w=70):   # review 12 Nov: minim and semibreve rests drawn on a five-line staff, so hat and coat can be told apart
    y = {'m': 24, 's': 20}[kind]
    return f'<svg viewBox="0 0 {w} 60" style="width:{w}px;height:60px">' + ''.join(f'<line x1="2" x2="{w - 2}" y1="{10 + 10 * i}" y2="{10 + 10 * i}" stroke="#26296b" stroke-width="1.3"/>' for i in range(5)) + f'<rect x="{w / 2 - 9}" y="{y}" width="18" height="6.5" fill="#26296b"/></svg>'
RMS, RSS = rst('m'), rst('s')
def secret_l(t): return f'<div class="secret1"><span class="sl">The secret</span><span>{t}</span></div>'
def inact_l(title, fig, steps, result): return '<div class="inact2"><div class="bh">Example</div><b class="it">' + title + '</b><div class="ia2">' + fig + '<ol>' + ''.join(f'<li><span class="in">{i + 1}</span><span>{t}</span></li>' for i, t in enumerate(steps)) + '</ol></div><div class="ires">' + result + '</div></div>'
def try_l(fig, big, text): return f'<div class="try10"><div class="bh">Try it · 10 seconds</div><div class="t10">{fig}<div><p class="big">{big}</p><p>{text}</p></div></div></div>'
def dots(groups, mark1=True, w=None):   # beat dots in bars: beat 1 big and coral
    out = []
    for g in groups:
        out.append(''.join(f'<span class="bd{" b1" if (i == 0 and mark1) else ""}"></span>' for i in range(g)))
    return '<div class="bds">' + '<span class="bl"></span>'.join(out) + '</div>'
def keys5(nums):   # five white keys C-G with finger numbers
    return '<div class="k5">' + ''.join(f'<div><b>{n}</b><span>{l}</span></div>' for l, n in zip('CDEFG', nums)) + '</div>'
LEARN = {
 'hbr-P1': {'try': ('<div class="bds" style="font-size:30px">2 · 3</div>', 'Find every group of two.', 'Start at the bottom of the piano. Touch each group of two black keys with fingers 2 and 3, all the way to the top. Then do the same with the groups of three.')},
 'hbr-L1': {'ex': ('Which finger plays the E?', keys5('1 ? ? ? ?'.split()), ['<b>Right hand:</b> thumb on C.', '<b>One finger</b> for each key: C D E F G.', '<b>Count up</b> to E: 1, 2, 3.'], 'Finger <b>3</b>. In this position the fingers 1 2 3 4 5 play C D E F G.'),
            'try': (keys5('1 2 3 4 5'.split()), 'Five fingers, five keys.', 'Thumb on C. Play C D E F G and back, saying the finger numbers out loud.')},
 'hbr-P2': {'try': ('<div style="font-family:NM;font-size:54px;color:#26296b">𝄞 𝄢</div>', 'Draw the two clefs.', 'Trace a treble clef in the air, curling round line 2 (G). Then a bass clef, its dot starting on line 4 (F).')},
 'hbr-T1': {'secret': 'The beat is steady, like a heartbeat. Bar lines group the beats, and beat 1 of every bar is the strongest.',
            'sub': [('rest: still count', 'silent beat: still count'), ('nest still count', 'silent beat')],
            'ex': ('Feel the beat before you play', dots([3, 3]), ['<b>Set a metronome</b> to 96: 96 beats a minute.', '<b>Listen first:</b> let one bar go by, counting 1 2 3 in your head.', '<b>Step in</b> on the next beat 1, like stepping onto a moving escalator.'], 'The first note lands <b>on the beat</b>, not a guess.')},
 'hbr-T2': {'secret': 'A <b>crotchet</b> lasts one beat; a <b>minim</b> lasts two: play on one count and hold through the next. Each has a rest just as long: count it, but do not play.',
            'ex': ('How many beats in this bar?', G(MI + '  ' + CR + '  ' + RC, 50), ['<b>Minim:</b> 2 beats.', '<b>Crotchet:</b> 1. <b>Crotchet rest:</b> 1, silent.', '<b>Add them up.</b>'], '2 + 1 + 1 = <b>4 beats</b>: a full bar, with one beat of silence.'),
            'try': (G(CR + ' ' + MI, 54), 'Clap, then press and hold.', 'Clap four crotchets, counting 1 2 3 4. Then play C as a minim: press on 1, hold through 2. Do it twice to fill the bar.')},   # her 12 Nov: two lengths a room
 'hbr-T2-s2': {'secret': 'A dot adds half: a <b>dotted minim</b> lasts three beats. A <b>semibreve</b> lasts four, a whole bar of four; its rest hangs from the fourth line, like a coat.',
            'hero_p': 53,
            'ex': ('Which note fills the bar?', G(DM + '    ' + SB, 50), ['<b>A bar of three:</b> count 1 2 3.', '<b>A bar of four:</b> count 1 2 3 4.', '<b>Dotted minim</b> 2 + 1; <b>semibreve</b> 4.'], 'Three beats: the <b>dotted minim</b>. Four beats: the <b>semibreve</b>.'),
            'try': (G(DM + ' ' + SB, 54), 'Hold for three, then four.', 'Press C and hold for 1 2 3, swaying like a waltz. Then press again and hold for all four beats, listening to the very end.')},
 'hbr-T8': {'secret': 'Two dots facing back mean: go back and play it again. A first-time bar is played once; the second time through, you skip it and play the second-time bar.'},
 'hbr-E1': {'secret': 'Dynamics tell you how loud to play: <b><i>p</i></b> is soft, <b><i>f</i></b> is loud. The weight of your arm makes the change, not the speed.',
            'ex': ('Which is louder: mp or mf?', '<div style="font-family:serif;font-style:italic;font-weight:700;font-size:40px;color:#26296b">mp · mf</div>', ['<b>m</b> means <i>mezzo</i>: half.', '<b>p</b> soft, <b>f</b> loud.', '<b>Half loud</b> beats half soft.'], '<b><i>mf</i></b>, half loud, is louder than <i>mp</i>, half soft.')},
}
DONE = lambda x: f'<b class="done2">{x}</b>'
def tbl_l(head, rows): return '<table class="lvt"><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</table>'
def ex(n, title, how, body, stars=1): return f'<div class="ex2"><div class="eh"><span class="en">{n}</span><b>{title}</b><span class="el">{"★" * stars}<span class="so">{"★" * (3 - stars)}</span></span></div><p class="how">{how}</p>{body}</div>'
def grid(cells, cols): return f'<div class="lvg" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(f'<div>{a}<span>{b}</span></div>' for a, b in cells) + '</div>'
STEP = {
 'hbr-T1': [ex(1, 'How many beats in each bar?', 'Count the dots between the bar lines. The first is done.', '<table class="lvt">' + ''.join(f'<tr><td>{dots([n])}</td><td style="width:22%">{a}</td></tr>' for n, a in ((3, DONE('3')), (4, BOX), (2, BOX), (4, BOX))) + '</table>'),
            ex(2, 'Add the bar lines', 'Beat 1 is the big coral dot. Draw a bar line just before each one (the first is done).', dots([4, 4, 4]).replace('<span class="bl"></span>', '<span class="bl gh"></span>').replace('<span class="bl gh"></span>', '<span class="bl"></span>', 1), 2),
            ex(3, 'Clap and count', 'Set a metronome to 60. Clap on beat 1, tap your knees on 2, 3 and 4, and count aloud. Keep going for a whole minute. Tick a circle each day.', '<div class="tk5">' + '<span></span>' * 5 + '</div>', 2)],
 'hbr-L1': [None, ex(2, 'Which finger?', 'Right hand, thumb on C. Write the finger that plays each note. The first is done.', tbl_l(['Note', 'E', 'G', 'D', 'F', 'C'], [['Finger', DONE('3'), BOX, BOX, BOX, BOX]])), None],
 'hbr-E1': [None, None, ex(3, 'Which is louder?', 'Circle the louder sign in each pair. The first is done.', tbl_l(['Pair', 'Louder'], [['<i><b>p</b></i> · <i><b>f</b></i>', DONE('<i>f</i>')], ['<i><b>mp</b></i> · <i><b>mf</b></i>', LINE], ['<i><b>pp</b></i> · <i><b>p</b></i>', LINE], ['<i><b>f</b></i> · <i><b>ff</b></i>', LINE]]))],
 'hbr-T2': [ex(1, 'How many beats?', 'Write the number of beats under each one. The first is done.', grid([(G(CR), DONE('1')), (G(RC), BOX), (G(CR), BOX), (G(RC), BOX)], 4)),
            ex(2, 'Play and count', 'Say the counts out loud and play: a crotchet is play, a rest is shh. Write 1 2 3 4 under the bar.', grid([(G(CR), DONE('1')), (G(CR), BOX), (G(RC), BOX), (G(CR), BOX)], 4), 2),
            ex(3, 'Draw it', 'Draw four crotchets, then two crotchet rests (a little lightning bolt).', '<div class="lvdraw"></div>', 2)],
 'hbr-T2-s2': [ex(1, 'One beat or two?', 'Write 1 or 2 under each. The first is done.', grid([(G(MI), DONE('2')), (G(CR), BOX), (RMS, BOX), (G(RC), BOX), (G(MI), BOX)], 5)),
               ex(2, 'Fill the bar', 'Four beats in each bar. Write the missing note: crotchet or minim. The first is done.', '<table class="lvt"><tr><td>' + G(CR) + ' ' + G(CR) + ' + ?</td><td>' + DONE('minim') + '</td></tr><tr><td>' + G(MI) + ' + ? + ' + G(CR) + '</td><td>' + LINE + '</td></tr><tr><td>' + G(MI) + ' + ?</td><td>' + LINE + '</td></tr></table>', 2),
               ex(3, 'The hat', 'Draw a minim rest: a block sitting on the middle line, like a hat. Then draw two minims.', '<div class="lvdraw"></div>', 2)],
 'hbr-T2-s3': [ex(1, 'How many beats?', 'Write the number of beats. The first is done.', grid([(G(DM), DONE('3')), (G(MI), BOX), (G(CR), BOX), (G(DM), BOX)], 4)),
               ex(2, 'Waltz time', 'Each bar has three beats. Count 1 2 3 and play each bar. Write how many notes it has. The first is done.', grid([(G(DM), DONE('1')), (G(MI + ' ' + CR), BOX), (G(CR + ' ' + CR + ' ' + CR), BOX)], 3), 2),
               ex(3, 'Add the dot', 'Make each minim last three beats: draw the dot after it.', grid([(G(MI), ''), (G(MI), ''), (G(MI), '')], 3), 2)],
 'hbr-T2-s4': [ex(1, 'Name, beats and rest', 'Fill in the table. The first row is done.', '<table class="lvt"><tr><th>Note</th><th>Name</th><th>Beats</th><th>Its rest</th></tr>' + ''.join(f'<tr><td>{G(n)}</td><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for n, a, b, c in ((SB, DONE('semibreve'), DONE('4'), RSS), (MI, LINE, BOX, BOX), (CR, LINE, BOX, BOX), (DM, LINE, BOX, '—'))) + '</table>'),
               ex(2, 'Coat or hat?', 'The semibreve rest hangs like a coat; the minim rest sits like a hat. Write coat or hat.', grid([(RSS, DONE('coat')), (RMS, LINE), (RSS, LINE), (RMS, LINE)], 4)),
               ex(3, 'Four beats', 'Each bar must add up to four beats. Write the missing note.', '<table class="lvt"><tr><td>' + G(MI) + ' + ' + G(CR) + ' + ?</td><td>' + DONE('crotchet') + '</td></tr><tr><td>' + G(DM) + ' + ?</td><td>' + LINE + '</td></tr><tr><td>? (one note)</td><td>' + LINE + '</td></tr></table>', 2)],
}
_S = STEP   # her 12 Nov: the four note steps fold into two rooms
_S['hbr-T8'] = [ex(1, 'Write the order', 'Each letter is one bar. Write the letters in the order you play them. The first is done.', tbl_l(['The music', 'You play'], [['A &nbsp; B :|', DONE('A B A B')], ['|: A &nbsp; B :| &nbsp; C', LINE], ['A &nbsp; |: B &nbsp; C :|', LINE], ['|: A :| &nbsp; |: B :|', LINE]])),
                 ex(2, 'First and second time', 'The bar marked 1 is played the first time only; the second time you skip it and play the bar marked 2. Write the order. The first is done.', tbl_l(['The music', 'You play'], [['|: A &nbsp; [1. B :| &nbsp; [2. C', DONE('A B A C')], ['|: A &nbsp; B &nbsp; [1. C :| &nbsp; [2. D', LINE], ['|: A &nbsp; [1. B :| &nbsp; [2. C &nbsp; D', LINE]]), 2),
                 ex(3, 'True or false?', 'Circle T or F.', tbl_l(['', ''], [['With no start sign, a repeat goes back to the very beginning.', 'T &nbsp; F'], ['A repeat sign means: play the bars between the signs three times.', 'T &nbsp; F'], ['The second time through, you skip the first-time bar.', 'T &nbsp; F'], ['Two dots beside a double bar line make a repeat sign.', 'T &nbsp; F']]))]
STEP = {**{k: v for k, v in _S.items() if not k.startswith('hbr-T2')},
        'hbr-T2': [_S['hbr-T2-s2'][0], _S['hbr-T2-s2'][1], _S['hbr-T2'][1]],
        'hbr-T2-s2': [_S['hbr-T2-s4'][0], _S['hbr-T2-s3'][1], _S['hbr-T2-s4'][1]]}
WB = {   # room -> (workbook, handbook page of the Learn/Use page, exercise titles)
 'hbr-B1': [('workbook-before', 18, ['Finger numbers', 'Too low, too high, or right?', 'The 30-second check'])],   # review 12 Nov: 'Which hand is round?' is the Learn page's example
 'hbr-P1': [('workbook-pitch', 22, ['Twos and threes', 'Name the keys', 'Round and round'])],
 'hbr-L1': [('workbook-play', 163, ['Five-finger position', 'C major, right hand', 'Play it'])],
 'hbr-P2': [('workbook-pitch', 27, ['The clefs', 'Line or space?']), ('workbook-pitch', 28, ['The grand staff'])],   # review 12 Nov: 'Treble or bass?' names Cs never taught
 'hbr-T1': [('workbook-time2', 50, ['Count it', 'Add the bar lines', 'Clap and count'])],
 'hbr-E1': [('workbook-expression', 76, ['Say it', 'Play it'])],
}
WBFILE = {'B': 'workbook-before', 'P': 'workbook-pitch', 'T': 'workbook-time2', 'E': 'workbook-expression', 'S': 'workbook-scales', 'H': 'workbook-harmony', 'L': 'workbook-play'}
def wb_auto(r):   # the chapter's Workbook pages in order: every exercise of its Learn page, then its Use page
    f = WBFILE.get(r['ch'][0]); a, b_ = (int(x) for x in (r['pages'].split('–') + [r['pages']])[:2]); out = []
    for k in sorted(B['wb'], key=lambda k: int(k.rsplit('|', 1)[1])):
        m = re.search(r'P\.\W*(\d+)\|', k)
        if k.startswith(f + '|') and m and a <= int(m.group(1)) <= b_: out += [x['html'] for x in B['wb'][k] if x['key'].startswith('ex')]
    return out
# her 13 Nov: the Prelim book. The exercises of each room, chosen so that nothing asks for an idea of a later level
# (compound time, the melodic minor, D.C. and D.S. belong to higher floors). 'Title#2' = the second exercise of that name.
WBPICK = {'hbr-T3': ['Note sums', 'Clap and count', 'In your music'], 'hbr-T4': ['Add the bar lines', 'Book every seat'],
          'hbr-S2': ['Which notes move?', 'Build it'], 'hbr-S1': ['Fix the scale', 'The major pattern'], 'hbr-E2': ['Which notes are short?', 'Slur or tie?', 'Play it']}
def wb_pick(r, titles):
    f = WBFILE.get(r['ch'][0]); a, b_ = (int(x) for x in (r['pages'].split('–') + [r['pages']])[:2]); allx = []
    for k in sorted(B['wb'], key=lambda k: int(k.rsplit('|', 1)[1])):
        m = re.search(r'P\.\W*(\d+)\|', k)
        if k.startswith(f + '|') and m and a <= int(m.group(1)) <= b_: allx += [(x['title'].strip(), x['html']) for x in B['wb'][k] if x['key'].startswith('ex')]
    out = []
    for t in titles:
        nm, _, nth = t.partition('#'); hits = [h for tt, h in allx if tt == nm]
        if hits: out.append(hits[min(len(hits), int(nth or 1)) - 1])
    return out
def practice(rid):
    wb = [h for f, p, t in WB.get(rid, []) for h in wb_ex(f, p, t)] if rid in WB else wb_pick(ROOMS[rid], WBPICK[rid]) if rid in WBPICK else (wb_auto(ROOMS[rid]) if rid not in STEP else [])
    if rid in STEP: xs = [x if x is not None else (wb[i] if i < len(wb) else None) for i, x in enumerate(STEP[rid])]; xs = [x for x in xs if x]
    else: xs = wb
    return [re.sub(r'<span class="en">\d+</span>', f'<span class="en">{i + 1}</span>', h, count=1) for i, h in enumerate(xs)]

EAR_HOME = {   # away-from-the-screen games, with a grown-up or a teacher
 'Beginner': [('Floor, tummy or sky?', 'A grown-up plays one key: very low, in the middle, or very high. Eyes closed! Point to the floor, your tummy or the sky.'),
              ('Copy-cat clap', 'A grown-up claps four beats. Clap it back exactly. Then swap: you clap, they copy. Was it the same?'),
              ('Stairs up, stairs down', 'A grown-up plays three keys next to each other, going up or going down. Show the way with your hand, then sing it.')]}
def ear_spread(r, name, i, n):
    pre = name == 'Beginner'; url = 'https://thepianobutler.com/drills.html?drill=' + r['id']
    head = f'<div class="lvhead"><div><div class="kick">{name} · Room {i}</div><h1>Ear training</h1><p class="lead lvl">{"Listening games before the exams" if pre else "The listening tests of this level"}</p></div><a class="lvqr" href="{url}">{qr(url)}<span>Scan to play</span></a></div>'
    sec = secret_l('Listen first, then play. Good ears make good fingers.' if pre else 'Sing it out loud. If you can sing it, you can hear it; if you can hear it, you can play it.')
    rows = ''.join(f'<tr><td><b>{k + 1}</b></td><td><b>{p["en"]}</b></td><td>{p["exam"].replace("Before the exams: ", "").capitalize() if pre else p["exam"]}</td></tr>' for k, p in enumerate(r['ear']))
    tb = f'<table class="lvt lvear"><tr><th></th><th>{"Game" if pre else "Test"}</th><th>{"What you listen for" if pre else "In the exam"}</th></tr>{rows}</table>'
    tr = try_l(G('𝄞', 54), 'Sing before you play.', 'Before you play a note, sing it. Then play it and listen: were you right?')
    note = '' if pre else '<p class="sm" style="margin-top:8px">Based on the aural tests of the AMEB 2026 syllabus. Check the current syllabus with your teacher before an exam.</p>'
    home = EAR_HOME.get(name) or [(p['en'], 'Your teacher or a grown-up plays the part of the examiner. ' + p['exam']) for p in r['ear']]
    tick = '<div class="tk5">' + '<span></span>' * 5 + '</div>'
    pr = ''.join(ex(k + 1, a, b_, tick, 1) for k, (a, b_) in enumerate(home))
    return head + sec + tb + tr + note, f'<div class="kick">{name} · Room {i} · Practise</div><h1>Practise</h1><p class="lead lvl">Away from the screen, with a grown-up or your teacher. Tick a circle each time.</p>' + pr
def review_spread(r, name, i):
    url = 'https://thepianobutler.com/drills.html?drill=' + r['id']
    head = f'<div class="lvhead"><div><div class="kick">{name} · Room {i}</div><h1>Review: a step further</h1><p class="lead lvl">Short parts of chapters from the level before, one step further</p></div><a class="lvqr" href="{url}">{qr(url)}<span>Scan to open</span></a></div>'
    rows = ''.join(f'<tr><td><b>{k + 1}</b></td><td><b>{p["en"]}</b></td><td>{p["chen"]}</td><td>pp. {p["pages"]}</td></tr>' for k, p in enumerate(r['review']))
    tb = f'<table class="lvt lvear"><tr><th></th><th>The step further</th><th>Chapter</th><th>Handbook</th></tr>{rows}</table>'
    left = head + secret_l('Go back to go forward: each part adds one step to a room you have already finished.') + tb + try_l(G('𝄞', 54), 'One part a day.', 'Listen to the part in the app, then play its drill. Five minutes is enough.')
    tick = '<div class="tk5">' + '<span></span>' * 3 + '</div>'
    right = f'<div class="kick">{name} · Room {i} · Practise</div><h1>Practise</h1><p class="lead lvl">For each part: listen, play its drill, then tick. Three ticks and it is yours.</p>' + ''.join(ex(k + 1, p['en'], f'{p["chen"]}, Handbook pp. {p["pages"]}.', tick, 1) for k, p in enumerate(r['review']))
    return left, right
# her 13 Nov ("6. 응"): an exam corner in each Level book, from the first exam level up. Facts from the AMEB 2026 syllabus
# (data_technical_ameb.js, data_aural_ameb.js, Manual of Syllabuses: sight-reading applies to Grades 1-8; general knowledge
# asks about the notes, rests, signs, terms and key of the pieces played). Scales are listed in general terms only (her 13 Nov).
EXAM = {'Prelim': dict(near='Preliminary',
    tech=['Scales, hands separately, one octave: <b>C major</b> and <b>G major</b>; <b>A minor</b> and <b>E minor</b>, natural and harmonic.', 'Two short technical exercises, chosen with your teacher.'],
    know=['the names of the <b>notes</b> and <b>rests</b> in your pieces, and how long each lasts', 'every <b>sign</b> and <b>word</b> printed in your pieces: what it means', 'the <b>key</b> of each piece, and its <b>time signature</b>'],
    sight='There is no sight-reading test at this level. It starts at Grade 1.')}
def exam_spread(name, toc, earn):
    E = EXAM[name]
    head = f'<div class="kick">{name} · The exam corner</div><h1>If you take an exam</h1><p class="lead lvl">This level is about the standard of a {E["near"]} exam.</p>'
    box = lambda t, body: f'<div class="lvx"><b>{t}</b>{body}</div>'
    ul = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    left = head + secret_l('An exam asks: can you play your pieces and your scales, hear what is played, and say what is on your page?') \
        + box('Pieces', '<p>Chosen with your teacher. Everything in this book is there to help you read and shape them.</p>') + box('Technical work', ul(E['tech'])) \
        + box('Aural tests', f'<p>The listening tests are Room {earn} of this book: one game for each test.</p>') + box('General knowledge', '<p>The examiner points at your music and asks about:</p>' + ul(E['know'])) + box('Sight-reading', f'<p>{E["sight"]}</p>') \
        + '<p class="sm" style="margin-top:8px">Based on the AMEB 2026 syllabus. Syllabuses change: check the current one with your teacher before you enter.</p>'
    tick = '<span class="fbx"></span>'
    rows = ''.join(f'<tr><td>{tick}</td><td>{x}</td></tr>' for x in ['I can play each piece from start to finish without stopping.', 'I can say the key and the time signature of each piece.', 'I can name every sign and word on my pages.', 'I can play each scale slowly, evenly, with the right fingers.', 'I have played all the ear games in Room ' + str(earn) + ' this week.', 'I have played my pieces for someone at home.', 'I know how to walk in, sit, set the stool and breathe out before I play.'])
    right = f'<div class="kick">{name} · The exam corner</div><h1>Four weeks to go</h1><p class="lead lvl">Tick a box when it is true. Go through the list again each week.</p><table class="lvt lvck">{rows}</table>' + try_l(G('𝄞', 54), 'Play it for someone.', 'Each week, play one piece for a person at home, as if it were the exam: walk in, bow, play, bow.')
    return left, right
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
        if r.get('review'):
            a, b_ = review_spread(r, name, i); out += [section(a, n, 'L' + rid), section(b_, n + 1, 'P' + rid)]; n += 2; continue
        if r.get('ear'):   # her 12 Nov: the floor's Ear training room, matched to that level's aural tests
            a, b_ = ear_spread(r, name, i, n); out += [section(a, n, 'L' + rid), section(b_, n + 1, 'P' + rid)]; n += 2; continue
        head = f'<div class="lvhead"><div><div class="kick">{name} · Room {i}</div><h1>{title}</h1><p class="lead lvl">More in the Handbook, pp. {r["pages"]}</p></div><a class="lvqr" href="{listen_url(r)}">{qr(listen_url(r))}<span>Scan to listen</span></a></div>'
        pr = practice(rid)[:3]   # one spread per room: Learn on the left, three exercises on the right
        out.append(section(head + ''.join(learn_blocks(r)), n, 'L' + rid)); n += 1
        out.append(section(f'<div class="kick">{name} · Room {i} · Practise</div><h1>Practise</h1>' + ''.join(pr), n, 'P' + rid)); n += 1
    if name in EXAM:
        earn = next((k for k, t_ in toc if t_ == 'Ear training'), '')
        a, b_ = exam_spread(name, toc, earn); out += [section(a, n, 'LX'), section(b_, n + 1, 'PX')]; n += 2; toc.append(('', 'The exam corner'))
    cover = f'''<section class="pg part2"><div class="pframe"><div class="pk">The Piano Butler · Level book</div><div class="pt">{name}</div><div class="pdv"></div>
<p class="pl">{line}</p><div class="pin"><div class="pih">The rooms</div>{"".join(f'<div class="tr"><span>{str(i) + " · " if i else ""}{t}</span><span class="dots"></span><span></span></div>' for i, t in toc)}</div></div></section>'''
    extra = """.lvl{font-size:13px!important;color:#6d6f9c} .lvx{border-left:3px solid #e4572e;padding:3px 0 3px 12px;margin:9px 0;font-size:14px} .lvx>b{color:#26296b;font-size:15px} .lvx p{margin:2px 0} .lvx ul{margin:2px 0 0;padding-left:18px} .lvx li{margin:1px 0} .lvck td{font-size:15px;padding:9px 6px} .lvck td:first-child{width:30px} .fbx{display:inline-block;width:18px;height:18px;border:1.5px solid #c9c7dc;border-radius:4px} .lvear td{font-size:14px;vertical-align:top} .lvear td:first-child{color:#e4572e;width:22px} .lvear td:nth-child(2){width:34%} .lvg>div{white-space:nowrap} .bds{display:flex;align-items:center;gap:7px;flex-wrap:nowrap} .bd{width:16px;height:16px;border-radius:50%;background:#26296b} .bd.b1{width:24px;height:24px;background:#e4572e} .bds .bl{width:2.5px;height:34px;background:#26296b;margin:0 6px} .bds .bl.gh{background:none;border-left:1.5px dashed #c9c7dc;width:0} .k5{display:flex;gap:3px} .k5>div{width:34px;height:74px;border:1.5px solid #26296b;border-radius:0 0 5px 5px;display:flex;flex-direction:column;justify-content:space-between;align-items:center;padding:5px 0 4px;background:#fff} .k5 b{color:#e4572e;font-size:16px} .k5 span{font-size:12px;color:#6d6f9c} .tk5{display:flex;gap:10px;justify-content:flex-end} .tk5 span{width:26px;height:26px;border:1.5px solid #c9c7dc;border-radius:50%} .lvhead{display:flex;justify-content:space-between;align-items:flex-start;gap:14px} .lvqr{display:flex;flex-direction:column;align-items:center;gap:3px;text-decoration:none;flex:none} .lvqr .qrs{width:64px;height:64px} .lvqr span{font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#e4572e} .lvg{display:grid;gap:10px;margin:8px 0} .lvg>div{display:flex;flex-direction:column;align-items:center;gap:6px;border:1.5px solid #e3e1ee;border-radius:8px;padding:10px 4px}
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
    print(build(0, 'Beginner', 'Nine rooms: sitting and hands, the keyboard, fingering, the staff, the beat, notes and rests, loud and soft, and games for your ears. Read each room, listen to it in the app, then practise.'))
    print(build(1, 'Prelim', 'Twelve rooms: how to practise, reading the notes, how long a note lasts, time signatures, repeats, touch, major and minor scales, your first chords, ear training and a review. Then the exam corner.'))
