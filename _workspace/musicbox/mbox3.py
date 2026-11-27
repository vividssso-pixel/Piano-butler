# Music Box 3: the notes are real notes now. Every melody is converted by conv.py straight from an open score.
import json, copy, re, sys
sys.path.insert(0, '.')
import conv; Fr = conv.Fr
base = json.load(open('mb19.json'))
LET = 'CDEFGAB'; NAT = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
def triad(name):   # 'Em' -> [(letter, accidental, pitch class)] root, third, fifth
    m = re.match(r'^([A-G])([#b]?)(m?)', name); i = LET.index(m[1]); r = (NAT[m[1]] + {'#': 1, 'b': -1, '': 0}[m[2]]) % 12; out = []
    for st, semi in ((0, 0), (2, 3 if m[3] else 4), (4, 7)):
        L = LET[(i + st) % 7]; pc = (r + semi) % 12; a = (pc - NAT[L] + 6) % 12 - 6
        out.append((L, {0: '', 1: '#', -1: 'b'}[a], pc))
    return out
def voice(name, prev):   # three keys close together around the C below middle C, moving as little as possible
    t = triad(name); best = None
    for inv in range(3):
        order = t[inv:] + t[:inv]
        for lo in range(40, 60):   # one fixed shape for each chord, so C is always C E G: all three keys between the B flat below the C under middle C and the B flat above it
            if lo % 12 != order[0][2]: continue
            ms = [lo]
            for L, a, pc in order[1:]: ms.append(ms[-1] + (pc - ms[-1]) % 12)
            cost = sum(max(0, 46 - x) + max(0, x - 58) for x in ms) * 100 + abs(ms[0] - 48)
            if best is None or cost < best[0]: best = (cost, ms, order)
    _, ms, order = best
    def tk(L, a, m): o = (m - {'#': 1, 'b': -1, '': 0}[a]) // 12 - 1; return L + a + ("'" * (o - 3) if o > 3 else ',' * (3 - o))
    return [tk(L, a, m) for (L, a, pc), m in zip(order, ms)], ms
def build(title, to, semis, meter, box, rng, pattern, chords=None, per=4):
    bars, m, k = conv.load(title, to, semis); full = meter * box; out = []; i = 0
    while i < len(bars):   # two part-bars either side of a repeat sign make one bar
        b = bars[i]
        if 0 < i < len(bars) - 1 and b['len'] < full and bars[i + 1]['len'] == full - b['len']:
            n = bars[i + 1]; b = {'ev': b['ev'] + [(o + b['len'], p, d, t) for o, p, d, t in n['ev']], 'ch': b['ch'] + [(o + b['len'], c) for o, c in n['ch']], 'len': full}; i += 1
        out.append(b); i += 1
    bars = out[rng[0]:rng[1]]; res = []; cur = None; prev = None
    for bi, b in enumerate(bars):
        d = {'w': ''}; n = int(b['len'] / box)
        if b['len'] < full and bi == 0:
            b = dict(b, ev=[(o + full - b['len'], p, dd, t) for o, p, dd, t in b['ev']]); d['pick'] = n
        elif b['len'] < full: d['head'] = n
        d['r'] = conv.tok(b, meter, box)
        if d.get('pick'): d['r'] = ' '.join(['r'] * (meter - n) + d['r'].split()[meter - n:])
        ch = dict((int(o / box), c) for o, c in b['ch']) if chords is None else dict(chords[bi]) if bi < len(chords) and chords[bi] else {}
        if not d.get('pick'):
            names = ['-'] * meter; lp = ['-'] * meter; half = meter // 2; pat = 'half' if pattern in ('split', 'lowtop') and half in ch and ch[half] != ch.get(0, cur) else pattern   # two chords in the bar: a whole chord for each
            for x in range(meter):
                new = x in ch and ch[x] != cur
                if x in ch: cur = ch[x]
                if cur is None: continue
                if new: names[x] = cur
                if pattern == 'none': continue
                strike = {'block': new or x == 0, 'two': x in (0, half), 'split': x in (0, half), 'half': x in (0, half), 'lowtop': x in (0, half)}[pat]
                if d.get('head'): strike = x == 0
                if strike:
                    v, prev = voice(cur, prev)
                    lp[x] = v[0] if pat in ('split', 'lowtop') and x == 0 and not d.get('head') else '+'.join(v[1:]) if pat in ('split', 'lowtop') and not d.get('head') else '+'.join(v)
            d['ch'] = ' '.join(names)
            if pattern != 'none': d['lp'] = ' '.join(lp)
        res.append(d)
    lines = []; i = 0
    while i < len(res):
        n = per + (1 if i == 0 and res[0].get('pick') else 0); ln = res[i:i + n]; i += n
        if i < len(res) and res[i].get('head') and i == len(res) - 1: ln.append(res[i]); i += 1
        lines.append(ln)
    used = []
    for b in res:
        for c in b.get('ch', '').split():
            if c != '-' and c not in used: used.append(c)
    return lines, used
def table(used):
    return '<table class="ftb"><tr><th>Chord</th><th>Keys, bottom to top</th><th>Kind</th></tr>'.replace('<th>Kind</th>', '<th></th>') + ''.join(f'<tr><td class="n" style="width:60px">{re.sub("([A-G])b", chr(92) + "1♭", c).replace("#", "♯")}</td><td>{" ".join(re.sub("[',]", "", x).replace("#", "♯").replace("b", "♭") for x in voice(c, None)[0])}</td><td>{"minor" if c.endswith("m") else ""}</td></tr>' for c in used) + '</table>'
MENU = '<ol class="stp"><li><b>Whole chord</b>, held for the bar (Music Box 2, Song 1).</li><li><b>Bottom key, then the top two</b> (Song 4 of this book, or the waltz).</li><li><b>The fan</b>: one key at a time, bottom, middle, top (Music Box 2, Song 7).</li><li><b>Two keys rocking</b>: bottom and top (Music Box 2, Song 12).</li><li><b>Just the bottom key</b>, like a bass player.</li></ol>'
TICKS = ['Left hand alone', 'Right hand alone', 'Hands together', 'Three times through']; LT = ['Tune alone', 'Chords alone, named out loud', 'Together, my first way', 'Together, a second way']
S = []
def song(title, show, stage, args, job, how, ready, ways, unit='q', src='', composer='', note='', split=4, extra='table', ticks=None, beam=None, key=0):
    lines, used = build(*args)
    S.append(dict(title=show, stage=stage, beats=args[3], lines=lines, used=used, job=job, how=how, ready=ready, ways=ways, unit=unit, src=src, composer=composer, note=note, split=split, extra=extra, ticks=ticks or TICKS, beam=beam, key=key))
song("She'll be Coming Round the Mountain", "She’ll Be Coming Round the Mountain", 'plain', ("She'll be Coming Round the Mountain", 'C', None, 4, 1, (0, 17), 'block'),
 'Welcome to Music Box 3. From this page on, <b>no letters in the notes</b>. You read them the way every pianist does: by where they sit on the five lines. The left hand stays in letters for a little longer.',
 'Find your first note, then read by <b>shape</b>: next line or space up is the next key up; a jump on the page is a jump on the keys. Two landmarks: the curl of the clef wraps round the <b>G</b> line, and the middle line is <b>B</b>. A curved line joining two notes of the same height is a <b>tie</b>: play once and hold for both.',
 'you can start from any bar, not just the beginning.', ['Left hand: bottom key on beat 1, the top two keys on beat 3.', 'Play the tune eight keys lower. It sits near middle C and is easier to sing.'],
 src='Nottingham Music Database, moved from D to C', composer='Traditional, United States')
song('Grand Old Duke of York', 'The Grand Old Duke of York', 'plain', ('Grand Old Duke of York', 'C', None, 4, 1, (0, 9), 'two'),
 'A marching tune, so the left hand marches: <b>a chord on beat 1 and again on beat 3</b>. The right hand has quick pairs and dotted notes with no letters to lean on.',
 'Clap the rhythm of line 1 before you play it. A dot makes a note longer, and the short note after it comes late. Play the whole tune twice.',
 'the left hand keeps marching on 1 and 3 even when the right hand has a dotted note.', ['Left hand on every beat: four chords in a bar, like boots.', 'First time loud, second time soft: the army marches away.'],
 src='Nottingham Music Database, first part, moved from D to C', composer='Traditional, England')
BB = [None, {0: 'G'}, {0: 'G', 2: 'D'}, {0: 'G', 2: 'D'}, {0: 'G'}, {0: 'G'}, {0: 'C', 2: 'G'}, {0: 'D'}, {0: 'G', 2: 'D'}, {0: 'G', 2: 'D'}]
song('Blue Bells of Scotland', 'The Blue Bells of Scotland', 'plain', ('Blue Bells of Scotland', None, None, 4, 1, (0, 9), 'split', BB),
 'Home is G, so a <b>♯ sits at the start of every line</b>, on the F line: every F is F♯, the black key. The left hand splits each chord: <b>bottom key first, then the top two together</b>. Where a bar holds two chords, play each one whole.',
 'The tune starts high and falls. Before you play, trace line 1 with a finger and say <i>down, down, down, up</i>. Play lines 1 and 2, then line 1 again to finish.',
 'you play every F♯ without a sign in front of it to remind you.', ['Left hand: the fan, one key on each beat.', 'Play the tune alone, very smoothly, as if it were sung.'],
 src='Nottingham Music Database; the chords are this book’s own', composer='Traditional, Scotland', key=1, note='After line 2, go back to bar 1 and play line 1 once more to finish.')
song("It's a Long Way to Tipperary", 'It’s a Long Way to Tipperary', 'grand', ("It's a Long Way to Tipperary", 'C', None, 4, 1, (0, 33), 'block'),
 'The left hand gets <b>its own five lines</b>. The sign at the front is the bass clef, the King: its two dots sit either side of the <b>F</b> line. The chords you know are written there as three notes stacked up.',
 'You already know these chords by feel; now match each shape to its picture. Three notes stacked evenly, all on lines or all in spaces, are a chord in its plain shape, like C. A wider gap in the stack means the chord is turned round, the way you have always played F (C F A) and G (B D G). The coral name still tells you which chord it is.',
 'you can cover the coral names with a strip of paper and still play the left hand.', ['Left hand: play each chord twice in the bar, on beats 1 and 3.', 'Sing it. This song was made for marching and singing.'],
 src='Nottingham Music Database (chorus), moved from D to C', composer='Jack Judge and Harry Williams, 1912', split=3)
song('W3KOOA', 'We Three Kings', 'grand', ('W3KOOA', None, None, 6, Fr(1, 2), (0, 16), 'half', None, 3),   # 27 Nov: three bars a line, so a chord with a sharp has room in its box
 'A minor home, <b>E minor</b>, for the verse; then the chorus steps out into the bright G major. The left hand plays <b>two chords in a bar</b>, each lasting three quick counts.',
 'Six quick counts in a bar, felt as two swings: <b>1</b> 2 3 <b>4</b> 5 6. The left-hand chords land on 1 and on 4. Lines 1 and 2 are the verse; lines 3 and 4 are the chorus.',
 'you can feel the moment the music turns from dark to bright at line 3.', ['Left hand: bottom key on count 1, the top two on count 4.', 'Verse very quietly, chorus full and warm.'],
 unit='e', src='Nottingham Music Database', composer='John Henry Hopkins, 1857', split=3, key=1)
song("John Brown's Body", 'John Brown’s Body', 'grand', ("John Brown's Body", 'C', None, 6, Fr(1, 2), (0, 17), 'lowtop', None, 3),
 'The split chord, now written as notes: <b>one low note on the first swing, two notes together on the second</b>. Reading the left hand means reading two different shapes in every bar.',
 'This is the tune of <i>Glory, glory, hallelujah</i>. Line 1 is the verse rhythm, long-short, long-short. In the last two lines the notes get long: keep counting six.',
 'the low note and the two-note answer swing evenly, like a walking pace.', ['Left hand: whole chords on counts 1 and 4, as in We Three Kings.', 'Play the last two lines twice as loud as the first two.'],
 unit='e', src='Nottingham Music Database, moved from D to C', composer='Traditional, United States, 1850s', split=3)
song('Scotland the Brave', 'Scotland the Brave', 'lead', ('Scotland the Brave', 'F', -2, 4, 1, (0, 33), 'none'),
 '<b>No left hand at all</b>: only the tune and the names of the chords. This is a <b>lead sheet</b>, the way most songs are written down. The left hand is yours to invent.',
 'Each coral name lasts until the next one. Find its three keys in the table; choose how to play them from the menu. Home is F: the ♭ at the start of every line means every B is B♭.',
 'you have played it two different ways and know which you prefer.', ['A bagpipe has a drone: hold F and C in the left hand through a whole line.', 'Change the way at line 5, where the tune climbs.'],
 src='Nottingham Music Database, moved from G to F', composer='Traditional, Scotland', extra='menu', ticks=LT, key=-1)
song('Blaydon Races', 'Blaydon Races', 'lead', ('Blaydon Races', 'C', None, 6, Fr(1, 2), (0, 33), 'none'),
 'A second lead sheet, this time in swinging six. <b>Tune and chord names only.</b> The verse fills the first page, the chorus the second.',
 'In six, a chord pattern has two swings to fill. Try: bottom key on count 1, top two on count 4. In the chorus the chords change twice in a bar; a whole chord on each swing is enough.',
 'someone could sing along while you play, without you stopping.', ['Verse with just the bottom key of each chord; chorus with whole chords.', 'Sing the tune and play only the left hand.'],
 unit='e', src='Nottingham Music Database, moved from D to C', composer='George Ridley, 1862', extra='menu', ticks=LT)
# Twinkle, Yours: the tune as in Music Box 1 and 2, as a lead sheet
def TB(r, ch): return {'r': r, 'w': '', 'ch': ch}
A = [TB("C C G G", 'C - - -'), TB('A A G -', 'F - C -'), TB('F F E E', 'F - C -'), TB('D D C -', 'G - C -')]; M = [TB('G G F F', 'C - F -'), TB('E E D -', 'C - G -')]
S.append(dict(title='Twinkle, Yours', stage='lead', beats=4, lines=[A, M + copy.deepcopy(M), copy.deepcopy(A)], used=['C', 'F', 'G'],
 job='Music Box 1 gave you Twinkle with one key. Music Box 2 gave you whole chords and minor colours. Here it is one last time, <b>with nothing but the tune and the chord names</b>. Everything else is up to you.',
 how='Play it five times, each time with a different left hand from the menu. Then swap some chords for their minor cousins, as in Music Box 2: Am for C, Dm for F, Em for G. Keep what you like. That is arranging.',
 ready='you can take a tune you know, find its chords, and choose a left hand for it. After that, you do not need this book.', ways=['Write your favourite version down: chord names over the tune, and the name of the way.', 'Do the same with Song 1 of Music Box 1.'],
 unit='q', src='Traditional tune, as in Music Box 1 and 2', composer='Traditional, France, 1700s', note='', split=4, extra='menu', ticks=['Five different left hands', 'With minor colours', 'My own version', 'For someone'], beam=None))
P0 = 3
for i, s in enumerate(S, 1):
    d = copy.deepcopy(base); g = d['gig']; last = i == len(S)
    d.update(id=f'md{i}', title=s['title'], lesson=i, beats=s['beats'], book="THE PIANO BUTLER'S MUSIC BOX 3", label='End of Music Box 3' if last else f'Song {i}')
    d['composer'] = {'name': s['composer'], 'years': '', 'stamp': ''}
    for k in ('shapes', 'ways', 'ways2', 'lkb_from', 'counts'): g.pop(k, None)
    ex = ['The chords in this song', table(s['used'])] if s['extra'] == 'table' else ['Your left hand: the chords, and five ways to play them', '<div style="display:grid;grid-template-columns:1fr 1.25fr;gap:26px;align-items:start"><div>' + table(s['used']) + '</div><div>' + MENU + '</div></div>']
    st = ['Play the tune alone until you can hum it.', 'Find each chord in the table. Play them as <b>whole chords</b>, one for each name, saying the names out loud.', 'Tune and whole chords together, slowly.', 'Choose a way from the menu and play the song through.', 'Choose a second way. Which one fits this song?'] if s['stage'] == 'lead' else ['<b>Clap the rhythm</b> of line 1 while you count out loud.', 'Name the first note of each line. Read the rest by shape.', '<b>Left hand alone</b>, saying the chord names.', '<b>Right hand alone</b>. Pencil in a finger number wherever your hand has to move.', '<b>Hands together</b>, one line at a time, so slowly that you never have to stop.']
    g.update(mb2=s['stage'], unit=s['unit'], job=s['job'], song_how=s['how'], ready=s['ready'], song_grid=s['lines'], ways_txt=s['ways'], ticks=s['ticks'], steps=st, simple=1, grid=1, nokb=1, split=s['split'], extra=ex, src=s['src'], song_note=s['note'])
    if s['beam']: g['beam'] = s['beam']
    g['key'] = s.get('key', 0)
    if last: g['ready_label'] = 'You have finished the Music Box when'
    d['page0'] = P0; P0 += 1 + -(-len(s['lines']) // s['split'])
    json.dump(d, open(f'md{i}.json', 'w'), ensure_ascii=False)
json.dump([[s['title'], s['composer'], s['src']] for s in S], open('md-sources.json', 'w'), ensure_ascii=False, indent=1)
print(len(S), 'songs', [len(s['lines']) for s in S])
