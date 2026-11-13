# The Level books, written new for each level (her 13 Nov: "단계마다 심플하게 큰 그림 위주로 ... 스토리북 보듯", "a로 가자").
# The Handbook stays the reference; a Level book is read like a storybook: one step a page, a big picture and two or three
# sentences, then one thing to do at the piano. Only what this level has met appears. The pictures are the Handbook's own
# (blocks.json), the app's pen drawings (posture_svgs.json) and a few simple drawings made here. After each room: one Practise page.
exec(open('/tmp/claude-0/lvl/levelbook.py').read().split("if __name__ == '__main__':")[0])
APP = json.load(open('/tmp/claude-0/pk/posture_svgs.json'))
_uid = [0]
def app(key, w=420):   # the app's pen drawing, ids made unique so several can share a page
    _uid[0] += 1; u = f'u{_uid[0]}'
    s = APP[key].replace('width="100%" height="100%" ', f'style="width:{w}px;height:auto;display:block" ', 1)
    return re.sub(r'(id="|url\(#|href="#)([a-z]+[a-z0-9]*)', lambda m: m.group(1) + m.group(2) + u, s)
def hb(page, key): return dict(keyed(page))[key]
N, C = '#26296b', '#e4572e'
def bear(x, y, s=1): return f'''<g transform="translate({x} {y}) scale({s})" fill="#fff" stroke="{N}" stroke-width="2" stroke-linejoin="round"><rect x="-13" y="8" width="6" height="9" rx="2.5"/><rect x="2" y="8" width="6" height="9" rx="2.5"/><ellipse cx="-3" cy="3" rx="15" ry="10" fill="{N}"/><circle cx="10.5" cy="-11" r="3"/><circle cx="20" cy="-11" r="3"/><circle cx="15" cy="-4" r="8"/><ellipse cx="18.8" cy="-1.4" rx="3.6" ry="2.6" stroke-width="1.4"/><circle cx="20.6" cy="-2.3" r="1.2" fill="{N}" stroke="none"/><circle cx="13.6" cy="-5.8" r="1.1" fill="{N}" stroke="none"/></g>'''
def bird(x, y, s=1): return f'''<g transform="translate({x} {y}) scale({s})" fill="#fff" stroke="{N}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"><path d="M-16 -2 L-24 -8 L-22 2 Z"/><ellipse cx="-4" cy="2" rx="13" ry="9"/><circle cx="9" cy="-6" r="6.5"/><path d="M15 -7 L22 -5 L15 -3 Z" fill="{C}" stroke="{C}"/><circle cx="10.5" cy="-7.5" r="1.1" fill="{N}" stroke="none"/><path d="M-10 1 q6 6 13 0" fill="none"/><path d="M-4 11 v6 M2 11 v6" fill="none"/></g>'''
def kb(n=15, w=560, h=150, labels=None, mark=None, start=0, shade=None):   # a plain keyboard: n white keys from C (start = index of the first key in C D E F G A B)
    kw = w / n; out = f'<svg viewBox="0 0 {w} {h + 34}" style="width:{w}px">'
    for i in range(n):
        L = 'CDEFGAB'[(i + start) % 7]; f = (shade or {}).get(i, '#fff')
        out += f'<rect x="{i * kw}" y="0" width="{kw}" height="{h}" fill="{f}" stroke="{N}" stroke-width="2"/>'
        if labels and (labels is True or i in labels): out += f'<text x="{i * kw + kw / 2}" y="{h - 12}" text-anchor="middle" font-size="{kw * .42:.0f}" font-weight="700" fill="{C if mark and i in mark else N}" font-family="Atkinson Hyperlegible,sans-serif">{L}</text>'
    for i in range(n - 1):
        if 'CDEFGAB'[(i + start) % 7] in 'CDFGA': out += f'<rect x="{(i + 1) * kw - kw * .3}" y="0" width="{kw * .6}" height="{h * .62}" fill="{N}"/>'
    return out + '</svg>'
def staff5(notes=(), w=520, clef=None, label=True):   # five lines; notes = [(x, step, text)] step 0 = bottom line
    t, g = 36, 22; y = lambda st: t + 4 * g - st * g / 2
    out = f'<svg viewBox="0 0 {w} {t + 4 * g + 70}" style="width:{w}px">' + ''.join(f'<line x1="10" x2="{w - 10}" y1="{t + i * g}" y2="{t + i * g}" stroke="{N}" stroke-width="2.2"/>' for i in range(5))
    if label: out += ''.join(f'<text x="{w - 4}" y="{y(2 * i) + 5}" font-size="14" fill="#6d6f9c" font-family="Atkinson Hyperlegible,sans-serif" text-anchor="end" dx="-2" dy="-8">line {i + 1}</text>' for i in range(5))
    for x, st, tx in notes:
        out += f'<ellipse cx="{x}" cy="{y(st)}" rx="14" ry="10.5" transform="rotate(-20 {x} {y(st)})" fill="{C}" stroke="{C}"/><text x="{x}" y="{t + 4 * g + 46}" text-anchor="middle" font-size="18" font-weight="700" fill="{N}" font-family="Atkinson Hyperlegible,sans-serif">{tx}</text>'
    return out + '</svg>'
def big(s, z=120): return f'<span style="font-family:NM;font-size:{z}px;line-height:1.15;color:{N}">{s}</span>'
def row(*xs, gap=46): return f'<div style="display:flex;align-items:flex-end;justify-content:center;gap:{gap}px">' + ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px">{a}<b style="font-size:20px;color:{C if red else N}">{b_}</b></div>' for a, b_, red in xs) + '</div>'
def beats(groups, rest=None):   # big beat dots in bars; rest = index of a silent beat
    out, k = '', 0
    for gi, g in enumerate(groups):
        for i in range(g):
            d = 44 if i == 0 else 30
            out += f'<span style="display:inline-flex;flex-direction:column;align-items:center;gap:8px;width:54px"><span style="width:{d}px;height:{d}px;border-radius:50%;{"border:3px dashed #9a9cc0;box-sizing:border-box" if k == rest else "background:" + (C if i == 0 else N)}"></span><b style="font-size:20px;color:{C if i == 0 else N}">{i + 1}</b></span>'; k += 1
        if gi < len(groups) - 1: out += f'<span style="width:4px;height:74px;background:{N};margin:0 10px;align-self:flex-start"></span>'
    return f'<div style="display:flex;align-items:flex-start;justify-content:center">{out}</div>'
def dyn(items):   # dynamics as growing bars
    return '<div style="display:flex;align-items:flex-end;justify-content:center;gap:22px">' + ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px"><span style="width:74px;height:{h}px;background:{C};opacity:{o};border-radius:6px 6px 0 0"></span><i style="font-family:\'Playfair Display\',serif;font-weight:900;font-size:44px;color:{N};line-height:1">{s}</i><span style="font-size:17px;color:{N};min-height:22px;line-height:22px">{w or "&nbsp;"}</span></div>' for s, w, h, o in items) + '</div>'

# her 13 Nov ("체스가 깔끔하다"): every page of a Level book sits in a double-rule frame on the books' chequered floor,
# with the page number on a plaque. The hidden .foot marks the bottom of the frame for the shrink-to-fit pass.
DENT = '<svg class="dent" viewBox="0 0 694 16" preserveAspectRatio="none"><rect x="0" y="0" width="694" height="1.6" fill="#26296b"/><rect x="0" y="14.4" width="694" height="1.6" fill="#26296b"/>' + ''.join(f'<rect x="{4 + k * 12.02:.2f}" y="5" width="6" height="6" fill="#26296b"/>' for k in range(58)) + '</svg>'   # drawn squares, not a CSS pattern: patterns came out pink in Preview
RABBIT = json.load(open('/tmp/claude-0/lvl/pb-art.json'))['rabbit-head'].replace('<svg ', '<svg style="display:block;height:62px" preserveAspectRatio="xMidYMid meet" ', 1)
def section(inner, n, flow):
    # her 14 Nov ("예전 레슨북 디자인 그대로", then the dentil line "이 라인이랑 섞어서 있었다"): the Lesson Book page of 2 Nov (book1.py): caps running head,
    # a band of small squares between two rules above and below, coral kicker, big Playfair title, the rabbit's bubble, "Try it at the piano", navy page square
    return f'<section class="pg cx" data-flow="{flow}"><div class="lbtop"><span>The Piano Butler · Level book</span><span>{RIGHT}</span></div>{DENT}<div class="fr"><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></div><div class="lbbot">{DENT}</div><div class="plq">{n}</div></section>'
def fivekeys():   # C to G with their black keys and the right-hand finger numbers
    k = kb(5, 520, 190, labels=True); body = k[k.index('>') + 1:-6]
    nums = ''.join(f'<text x="{i * 104 + 52}" y="46" text-anchor="middle" font-size="46" font-weight="700" fill="{C}" font-family="Atkinson Hyperlegible,sans-serif">{i + 1}</text>' for i in range(5))
    return f'<svg viewBox="0 0 520 290" style="width:520px">{nums}<g transform="translate(0 62)">{body}</g></svg>'
def family():   # semibreve, minims, crotchets: each row fills four beats
    rw = lambda lab, notes, z: f'<div style="display:grid;grid-template-columns:150px 1fr;align-items:end;border-bottom:1.5px solid #e3e1ee;padding:6px 0"><b style="font-size:19px;color:{N};padding-bottom:10px">{lab}</b><div style="display:flex;justify-content:space-around;align-items:flex-end;height:{z + 20}px">{notes}</div></div>'
    g = lambda ch, z: f'<span style="font-family:NM;font-size:{z}px;line-height:1.1;color:{N}">{ch}</span>'
    return f'<div style="width:600px">{rw("1 semibreve", g(SB, 96), 96)}{rw("2 minims", g(MI, 96) * 2, 96)}{rw("4 crotchets", g(CR, 96) * 4, 96)}</div>'
# her 13 Nov: practise pages written for the room (two exercises, only what the room has taught)
tick5 = '<div class="tk5">' + '<span></span>' * 5 + '</div>'
def kb14():   # two octaves C to B, for counting the groups
    return kb(14, 400, 96)
PRACT = {
 'hbr-B1': lambda: [ex(1, 'Flat, fallen in, or round?', 'Write the word under each hand. The first is done.', grid([(app('2:flat fingers', 105), DONE('flat')), (app('2:The good shape', 105), LINE), (app('2:knuckles collapsed', 105), LINE)], 3)), wb_pick(ROOMS['hbr-B1'], ['Too low, too high, or right?'])[0]],
 'hbr-P1': lambda: [ex(1, 'Twos and threes', 'Circle every group of two black keys. Draw a box round every group of three. How many of each?', kb14() + '<p style="margin-top:8px">groups of two ' + BOX + ' &nbsp; groups of three ' + BOX + '</p>'),
                    re.sub(r'<p class="how">.*?</p>', '<p class="how">Find the black-key group next to each number. Write the letter of the numbered key. The first is done.</p>', wb_pick(ROOMS['hbr-P1'], ['Name the keys'])[0], count=1, flags=re.S)],
 'hbr-L1': lambda: [wb_pick(ROOMS['hbr-B1'], ['Finger numbers'])[0], ex(2, 'Which finger?', 'Right hand, thumb on C. Write the finger that plays each note. The first is done.', tbl_l(['Note', 'E', 'G', 'D', 'F', 'C'], [['Finger', DONE('3'), BOX, BOX, BOX, BOX]]))],
 'hbr-T2': lambda: [ex(1, 'One beat or two?', 'Write 1 or 2 under each. The first is done.', grid([(G(MI), DONE('2')), (G(CR), BOX), (G(RC), BOX), (G(MI), BOX), (G(CR), BOX)], 5)), STEP['hbr-T2'][1]],
 'hbr-T2-s2': lambda: [ex(1, 'Name and beats', 'Fill in the table. The first row is done.', '<table class="lvt"><tr><th>Note</th><th>Name</th><th>Beats</th></tr>' + ''.join(f'<tr><td>{G(n)}</td><td>{a}</td><td>{b_}</td></tr>' for n, a, b_ in ((SB, DONE('semibreve'), DONE('4')), (MI, LINE, BOX), (CR, LINE, BOX), (DM, LINE, BOX))) + '</table>'),
                       ex(2, 'Three in a bar', 'Each bar has three beats. Count 1 2 3 and play each bar. Write how many notes it has. The first is done.', grid([(G(DM), DONE('1')), (G(MI + ' ' + CR), BOX), (G(CR + ' ' + CR + ' ' + CR), BOX)], 3), 2)],
 'hbr-E1': lambda: [ex(1, 'What does it mean?', 'Write soft, loud, quite soft or quite loud. The first is done.', tbl_l(['Sign', 'Means'], [['<i><b>p</b></i>', DONE('soft')], ['<i><b>f</b></i>', LINE], ['<i><b>mp</b></i>', LINE], ['<i><b>mf</b></i>', LINE]])),
                    ex(2, 'Play it', 'Play C four times: p, mp, mf, f. Four steps, the same speed. Tick a circle each day.', tick5)],
}
def practise_for(rid):
    xs = PRACT[rid]() if rid in PRACT else practice(rid)[:2]
    return [re.sub(r'<span class="en">\d+</span>', f'<span class="en">{i + 1}</span>', h, count=1) for i, h in enumerate(xs)]
EARCARDS = [('1', 'Low, middle or high?'), ('2', 'Same clapping, or different?'), ('3', 'Same tune, or different?'), ('4', 'Which way did it go?'), ('5', 'Find the note')]
EARHOME = {'Prelim': [('Clap the beat', 'A grown-up plays in two or in three, slow or quick. Clap the beat, and keep clapping when the music stops.'), ('Echo the rhythm', 'They clap a short pattern. Clap it back exactly.'), ('Sing the notes', 'They play five notes slowly, one at a time. Sing each one after it.'), ('Higher or lower?', 'They play two notes. Say whether the second is higher or lower. Tick a circle for each day you play these games.')]}
def ear_story(r, name, i, n):
    url = 'https://thepianobutler.com/drills.html?drill=' + r['id']
    pre = name == 'Beginner'; ec = EARCARDS if pre else [(str(k + 1), p_['en']) for k, p_ in enumerate(r['ear'])]
    cards = '<div style="display:grid;grid-template-columns:repeat(' + ('3' if len(ec) > 4 else '2') + ',200px);gap:16px;justify-content:center">' + ''.join(f'<div style="border:2px solid {N};border-radius:10px;padding:26px 10px;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center"><span style="width:58px;height:58px;border-radius:50%;background:{C};color:#fff;font-weight:700;font-size:30px;display:flex;align-items:center;justify-content:center">{a}</span><b style="font-size:22px;color:{N};line-height:1.25">{b_}</b></div>' for a, b_ in ec) + '</div>'
    hd = f'<div class="lvhead"><div><div class="cxk">Room {i} <i>◆</i> 1 of 1</div><h1>Ear training</h1></div><a class="lvqr" href="{url}">{qr(url)}<span>Scan to play</span></a></div>'
    left = f'{hd}<div class="stpic"><div class="stin">{cards}</div></div><div class="sttx"><p><b>Listen first, then play.</b> Good ears make good fingers.</p><p>' + ('Five listening games are waiting in the app. Scan the code and play one each day.' if pre else 'Four listening games belong to this level. Each one is in the app: scan the code and play one each day.') + '</p></div><div class="stpn"><span>At the piano</span>Before you play a note, sing it. Then play it and listen: were you right?</div>'
    home = EARHOME.get(name) or [('Floor, tummy or sky?', 'A grown-up plays one key: very low, in the middle, or very high. Eyes closed! Point to the floor, your tummy or the sky.'), ('Copy-cat clap', 'A grown-up claps a short pattern. Clap it back exactly. Then swap: you clap, they copy.')]
    right = f'<div class="cxk cxc">Room {i} <i>◆</i> Ear training <i>◆</i> Practise</div><div class="prbig">' + ''.join(ex(k + 1, a, b_, tick5, 1) for k, (a, b_) in enumerate(home)) + '</div>'
    return left, right
def story(name, i, title, k, n, pic, text, piano, rid=None, first=False):
    r = ROOMS[rid] if rid else None
    q = f'<a class="lvqr" href="{listen_url(r)}">{qr(listen_url(r))}<span>Scan to listen</span></a>' if first and r and r.get('ch') != 'EAR' else ''
    hd = (f'<div class="lvhead"><div><div class="cxk">Room {i} <i>◆</i> {k} of {n}</div><h1>{title}</h1></div>{q}</div>' if first
          else f'<div class="cxk cxc">Room {i} <i>◆</i> {title} <i>◆</i> {k} of {n}</div>')
    return f'{hd}<div class="stpic"><div class="stin">{pic}</div></div><div class="sttx">{text}</div><div class="stpn"><span>At the piano</span>{piano}</div>'
ROOMSTORY = {
 'hbr-B1': ('Sitting and hands', [
   (app('1:Just right', 460), '<p><b>Sit tall</b> on the front half of the stool, with both <b>feet flat</b> on the floor.</p><p>Your arms float out in front, <b>level with the keys</b>, like a table top.</p>', 'Sit down. Lift your shoulders up to your ears, then let them drop.'),
   (app('2:The good shape'), '<p>Hold a small ball in your hand. That <b>round shape</b> is your playing hand.</p><p>Your knuckles stand up like a <b>bridge</b>, and you play on your <b>fingertips</b>.</p>', 'Hold a ball or an orange. Put your hand on the keys without changing its shape.'),
   (row((app('2:flat fingers', 250), '✗ flat', True), (app('2:knuckles collapsed', 250), '✗ fallen in', True), (app('2:The good shape', 250), '✓ round', False), gap=10), '<p>A <b>flat</b> hand is fast asleep. A bridge that has <b>fallen in</b> cannot carry anything.</p><p>The <b>round</b> hand can play all day.</p>', 'Make the flat hand, then the fallen bridge, then the round hand. Feel the difference.')]),
 'hbr-P1': ('The keyboard', [
   (kb(15, 600, 170), '<p>Look at the black keys. They come in <b>twos</b> and <b>threes</b>, again and again, all the way along.</p><p>Find the pattern once and you can never get lost.</p>', 'Touch every group of two black keys, from the left end to the right end. Then every group of three.'),
   (f'<svg viewBox="0 0 640 250" style="width:640px"><g transform="translate(20 60)">{kb(15, 600, 150)[kb(15, 600, 150).index(">") + 1:-6]}</g>{bear(70, 30, 1.7)}{bird(585, 30, 1.6)}<text x="70" y="246" text-anchor="middle" font-size="22" font-weight="700" fill="{N}" font-family="Atkinson Hyperlegible,sans-serif">low</text><text x="585" y="246" text-anchor="middle" font-size="22" font-weight="700" fill="{N}" font-family="Atkinson Hyperlegible,sans-serif">high</text></svg>', '<p><b>Left is low</b>, like a big grumpy bear. <b>Right is high</b>, like a little bird.</p><p>Go to the right and every key sounds a little higher.</p>', 'Play the lowest key you can reach, then the highest. Bear, then bird.'),
   (kb(7, 560, 190, labels=True, mark={0, 1, 2}), '<p>Every white key has a letter. Beside the <b>two</b> black keys live <b>C, D, E</b>. Beside the <b>three</b> live <b>F, G, A, B</b>.</p><p>After B comes C again: seven letters, round and round.</p>', 'Find a group of two black keys. Play the three white keys around it and say C, D, E.')]),
 'hbr-L1': ('Finger numbers', [
   (hb(163, 'hero'), '<p>Every finger has a <b>number</b>. The <b>thumb is 1</b>, then 2, 3, 4, and the little finger is <b>5</b>.</p><p>It is the same in both hands: thumbs are always 1.</p>', 'Hold up both hands. Wiggle finger 1, then 2, 3, 4, 5, saying the numbers.'),
   (fivekeys(), '<p>Find any <b>C</b>: the white key just left of two black keys. Put your right thumb on it. Now <b>C D E F G</b> are fingers <b>1 2 3 4 5</b>.</p><p>In the left hand the little finger starts: C D E F G are <b>5 4 3 2 1</b>.</p>', 'Right thumb on C. Play C D E F G and back, saying the finger numbers. Then the left hand, starting with finger 5.')]),
 'hbr-P2': ('The staff and the clefs', [
   (staff5([(150, 2, 'on a line'), (330, 3, 'in a space')]), '<p>Music is written on <b>five lines</b>, called the <b>staff</b>.</p><p>A note can sit <b>on a line</b>. Or it can sit <b>in a space</b>. Higher up means higher on the piano.</p>', 'Count the lines from the bottom: 1, 2, 3, 4, 5. Then count the four spaces.'),
   (hb(27, 'hero'), '<p>A <b>clef</b> at the start says which notes the lines stand for.</p><p>The <b>treble clef</b> is the Queen of the high notes: her curl wraps round the line for <b>G</b>. The <b>bass clef</b> is the King of the low notes: his two dots hug the line for <b>F</b>.</p>', 'Play any high key with your right hand: the Queen’s side. Then any low key with your left: the King’s side.')]),
 'hbr-T1': ('The beat', [
   (beats([4, 4]), '<p>Music has a steady <b>beat</b>, like a heartbeat. It never speeds up and never stops.</p><p>We count the beats: 1, 2, 3, 4, and round again.</p>', 'Put a hand on your heart. Tap that steady beat on your knee and count 1 2 3 4.'),
   (beats([3, 3, 3], rest=4), '<p><b>Bar lines</b> put the beats into groups called <b>bars</b>. <b>Beat 1</b> of every bar is the strongest.</p><p>Sometimes a beat is <b>silent</b>. You still count it.</p>', 'Clap three in a bar: STRONG, weak, weak. Then leave out one clap, but keep counting.')]),
 'hbr-T2': ('Notes: crotchet and minim', [
   (row((big(CR), '1', False), (big(CR), '2', False), (big(CR), '3', False), (big(CR), '4', False)), '<p>This is a <b>crotchet</b>. It lasts <b>one beat</b>.</p><p>Four crotchets fill a bar of four: play, play, play, play.</p>', 'Play C four times, one for each beat, counting 1 2 3 4.'),
   (row((big(MI), '1 – 2', False), (big(MI), '3 – 4', False), gap=120), '<p>This is a <b>minim</b>. Its head is empty, and it lasts <b>two beats</b>.</p><p>Play on the first beat and <b>hold</b> through the second.</p>', 'Play C as a minim: press on 1, hold through 2. Then again on 3, holding through 4.'),
   (row((big(CR), 'play', False), (big(RC), 'shh', True), (big(CR), 'play', False), (big(RC), 'shh', True)), '<p>Silence has signs too, called <b>rests</b>. A <b>crotchet rest</b> is one beat of silence.</p><p>You count a rest just like a note. You just do not play.</p>', 'Play, shh, play, shh: C on beats 1 and 3, silence on 2 and 4. Keep counting.')]),
 'hbr-T2-s2': ('Notes: three beats and four', [
   (row((big(MI), '2 beats', False), (big('+', 70), '', False), (f'<span style="display:inline-block;width:26px;height:26px;border-radius:50%;background:{C};margin-bottom:26px"></span>', 'a dot', True), (big('=', 70), '', False), (big(DM), '3 beats', False), gap=26), '<p>A <b>dot</b> after a minim adds one more beat.</p><p>Two beats and one more: a <b>dotted minim</b> lasts <b>three beats</b>.</p>', 'Play C and hold for 1 2 3. Lean in on beat 1.'),
   (row((big(SB), '1 – 2 – 3 – 4', False)), '<p>This is a <b>semibreve</b>: an empty head and no stem. It lasts <b>four beats</b>, a whole bar of four.</p><p>Press once, and listen until the sound has had all four beats.</p>', 'Play C and hold for 1 2 3 4. Lift exactly when the next bar begins.'),
   (family(), '<p>Now you know the family. Each note is <b>half</b> of the one above it.</p><p>One semibreve is as long as two minims, or four crotchets.</p>', 'Play four crotchets on C. Then one semibreve, held for all four beats. The same length!')]),
 'hbr-E1': ('Loud and soft', [
   (dyn([('p', 'soft', 70, .45), ('f', 'loud', 190, 1)]), '<p>Music can be <b>soft</b> or <b>loud</b>. The signs are Italian: <b><i>p</i></b> for <i>piano</i>, soft, and <b><i>f</i></b> for <i>forte</i>, loud.</p><p>To play louder, let your arm feel heavy. Do not hit the key.</p>', 'Play C softly, like a secret. Then play it loudly, like calling across a field.'),
   (dyn([('p', 'soft', 60, .4), ('mp', 'quite soft', 105, .6), ('mf', 'quite loud', 150, .8), ('f', 'loud', 200, 1)]), '<p>In between come two more. The <b><i>m</i></b> is for <i>mezzo</i>, which means <b>half</b> or <b>medium</b>: <b><i>mp</i></b> is quite soft, <b><i>mf</i></b> is quite loud.</p><p>Soft does not mean slow, and loud does not mean fast. The beat stays the same.</p>', 'Play C four times: p, mp, mf, f. Four steps, the same speed.')]),
}

# ---------- the Prelim book (her 13 Nov: written new; examples in the exam keys C and G major, A and E minor) ----------
QV = '𝅘𝅥𝅮'; DC = '𝅘𝅥.'
F_ = 'font-family="Atkinson Hyperlegible,sans-serif"'
def st(notes, clef='t', w=560, names=True, led=True):   # a staff with a clef; notes = [(step, label)], step 0 = bottom line
    t, g = 46, 24; y = lambda k: t + 4 * g - k * g / 2; n = len(notes); x0 = 150; dx = (w - x0 - 50) / max(1, n - 1) if n > 1 else 0
    o = f'<svg viewBox="0 0 {w} {t + 4 * g + 96}" style="width:{w}px">' + ''.join(f'<line x1="10" x2="{w - 10}" y1="{t + i * g}" y2="{t + i * g}" stroke="{N}" stroke-width="2.2"/>' for i in range(5))
    o += f'<text x="20" y="{t + 4 * g - (g * .95 if clef == "t" else g * 1.05)}" font-family="NM" font-size="{g * 4.05 if clef == "t" else g * 3.9}" fill="{N}">{"𝄞" if clef == "t" else "𝄢"}</text>'
    for i, (k, lab) in enumerate(notes):
        x = x0 + i * dx if n > 1 else w / 2 + 40
        if led:
            for L in list(range(-2, k - 1, -2)) + list(range(10, k + 1, 2)): o += f'<line x1="{x - 24}" x2="{x + 24}" y1="{y(L)}" y2="{y(L)}" stroke="{N}" stroke-width="2.2"/>'
        o += f'<ellipse cx="{x}" cy="{y(k)}" rx="15" ry="11" transform="rotate(-20 {x} {y(k)})" fill="{C}"/>'
        if names and lab: o += f'<text x="{x}" y="{t + 4 * g + 84}" text-anchor="middle" font-size="26" font-weight="700" fill="{N}" {F_}>{lab}</text>'
    return o + '</svg>'
def grand():   # the two staves with Middle C on its own little line between them
    g = 22; w = 520; o = f'<svg viewBox="0 0 {w} 330" style="width:{w}px">'
    for top in (30, 200): o += ''.join(f'<line x1="10" x2="{w - 10}" y1="{top + i * g}" y2="{top + i * g}" stroke="{N}" stroke-width="2.2"/>' for i in range(5))
    o += f'<line x1="10" x2="10" y1="30" y2="{200 + 4 * g}" stroke="{N}" stroke-width="3"/><text x="22" y="{30 + 4 * g - g * .95}" font-family="NM" font-size="{g * 4.05}" fill="{N}">𝄞</text><text x="22" y="{200 + 4 * g - g * 1.05}" font-family="NM" font-size="{g * 3.9}" fill="{N}">𝄢</text>'
    o += f'<line x1="236" x2="292" y1="159" y2="159" stroke="{N}" stroke-width="2.4"/><ellipse cx="264" cy="159" rx="15" ry="11" transform="rotate(-20 264 159)" fill="{C}"/><text x="310" y="167" font-size="24" font-weight="700" fill="{C}" {F_}>Middle C</text>'
    o += f'<text x="{w - 14}" y="22" text-anchor="end" font-size="17" fill="#6d6f9c" {F_}>right hand</text><text x="{w - 14}" y="322" text-anchor="end" font-size="17" fill="#6d6f9c" {F_}>left hand</text>'
    return o + '</svg>'
def kbm(n, start, white=None, black=None, w=600, h=170, labels=False):   # a keyboard with marked keys: white {index: text}, black {index of the white key on its left: text}
    kw = w / n; k = kb(n, w, h, labels=labels, start=start); body = k[k.index('>') + 1:-6]; o = ''
    for i, tx in (white or {}).items(): o += f'<circle cx="{i * kw + kw / 2}" cy="{h - 34}" r="{kw * .3:.0f}" fill="{C}"/><text x="{i * kw + kw / 2}" y="{h - 34 + kw * .13:.0f}" text-anchor="middle" font-size="{kw * .36:.0f}" font-weight="700" fill="#fff" {F_}>{tx}</text>'
    for i, tx in (black or {}).items(): o += f'<circle cx="{(i + 1) * kw}" cy="{h * .62 - 30}" r="{kw * .24:.0f}" fill="{C}"/><text x="{(i + 1) * kw}" y="{h * .62 - 30 + kw * .1:.0f}" text-anchor="middle" font-size="{kw * .27:.0f}" font-weight="700" fill="#fff" {F_}>{tx}</text>'
    return f'<svg viewBox="0 0 {w} {h + 6}" style="width:{w}px">{body}{o}</svg>'
def cards(xs, cols=3, wd=190):
    return f'<div style="display:grid;grid-template-columns:repeat({cols},{wd}px);gap:16px;justify-content:center">' + ''.join(f'<div style="border:2px solid {N};border-radius:10px;padding:22px 10px;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center"><span style="min-width:58px;height:58px;padding:0 10px;border-radius:29px;background:{C};color:#fff;font-weight:700;font-size:28px;display:flex;align-items:center;justify-content:center;box-sizing:border-box">{a}</span><b style="font-size:21px;color:{N};line-height:1.25">{b_}</b></div>' for a, b_ in xs) + '</div>'
def ladder(xs, hot=None):
    return '<div style="display:flex;align-items:flex-end;justify-content:center;gap:16px">' + ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px"><span style="width:84px;height:{60 + 34 * i}px;background:{C};opacity:{.35 + .16 * i};border-radius:6px 6px 0 0"></span><b style="font-size:26px;color:{N}">{x}</b></div>' for i, x in enumerate(xs)) + '</div>'
def boxes(xs, red=()):   # bars as boxes: 'A', 'B :|' ...
    return '<div style="display:flex;justify-content:center;align-items:flex-end;padding-top:40px">' + ''.join(f'<div style="position:relative;min-width:104px;height:92px;border:3px solid {N};margin-left:-3px;display:flex;align-items:center;justify-content:center;font-family:\'Playfair Display\',PF,serif;font-weight:900;font-size:40px;color:{C if i in red else N};padding:0 14px;box-sizing:border-box">{x}</div>' for i, x in enumerate(xs)) + '</div>'
def tsig(a, b_): return f'<span style="display:inline-flex;flex-direction:column;align-items:center;font-family:\'Playfair Display\',PF,serif;font-weight:900;font-size:64px;line-height:.92;color:{N}"><span>{a}</span><span>{b_}</span></span>'
def tsrow(a, b_, n): return f'<div style="display:flex;align-items:center;gap:30px;margin:6px 0">{tsig(a, b_)}{beats([n])}</div>'
def tie():   # two notes of the same pitch joined by a curve
    return f'<svg viewBox="0 0 420 230" style="width:420px"><text x="70" y="150" font-family="NM" font-size="150" fill="{N}">{MI}</text><text x="250" y="150" font-family="NM" font-size="150" fill="{N}">{CR}</text><path d="M96 168 Q200 214 300 168" fill="none" stroke="{C}" stroke-width="6" stroke-linecap="round"/><text x="200" y="226" text-anchor="middle" font-size="24" font-weight="700" fill="{C}" {F_}>2 + 1 = 3 beats</text></svg>'
SQ = '𝅘𝅥𝅯'
def disc(part=1, z=40, div=1):   # her 14 Nov: one circle = one beat. part: the piece shown (1, .5, .25); div: dashed cuts in a whole circle (2 = two quavers joined, 4 = four semiquavers)
    import math
    cuts = ''.join(f'<line x1="20" y1="20" x2="{20 + 18 * math.sin(2 * math.pi * k / div):.1f}" y2="{20 - 18 * math.cos(2 * math.pi * k / div):.1f}" stroke="#fff" stroke-width="2.2" stroke-dasharray="3 2.5"/>' for k in range(div)) if div > 1 else ''
    if div == 2: cuts = '<line x1="20" y1="2" x2="20" y2="38" stroke="#fff" stroke-width="2.2" stroke-dasharray="3 2.5"/>'
    if part == 1: body = f'<circle cx="20" cy="20" r="18" fill="{C}"/>{cuts}'
    else:
        a = 2 * math.pi * part; x, y = 20 + 18 * math.sin(a), 20 - 18 * math.cos(a)
        body = f'<circle cx="20" cy="20" r="17.2" fill="none" stroke="#b9b8d0" stroke-width="1.5" stroke-dasharray="3 3"/><path d="M20 20 L20 2 A18 18 0 {1 if part > .5 else 0} 1 {x:.1f} {y:.1f} Z" fill="{C}"/>'
    return f'<svg viewBox="0 0 40 40" style="width:{z}px;height:{z}px">{body}</svg>'
def apple(part=1, z=40): return disc(part, z)
def apples(n, z=34, div=1):   # n beats as circles: 4, 3, 2, 1, 1.5, .5, .25
    full = int(n); rest = n - full
    return '<span style="display:inline-flex;gap:4px;align-items:center;justify-content:center">' + disc(1, z, div) * full + (disc(rest, z) if rest else '') + '</span>'
def bq(n=2, h=150, col=None, beams=1):   # n quavers joined by a beam (her 14 Nov: one has a tail, two or more are beamed); beams=2 for semiquavers
    col = col or N; sp = 70 if beams == 1 else 56; w = 60 + (n - 1) * sp
    heads = ''.join(f'<ellipse cx="{24 + i * sp}" cy="118" rx="19" ry="13.5" transform="rotate(-22 {24 + i * sp} 118)" fill="{col}"/><rect x="{39 + i * sp}" y="16" width="5" height="100" fill="{col}"/>' for i in range(n))
    bm = ''.join(f'<rect x="39" y="{12 + k * 20}" width="{(n - 1) * sp + 5}" height="12" fill="{col}"/>' for k in range(beams))
    return f'<svg viewBox="0 0 {w} 136" style="height:{h}px;width:{h * w / 136:.0f}px;vertical-align:bottom">{heads}{bm}</svg>'
def hairpin(open_right=True, w=300):
    a, b_ = (10, 290) if open_right else (290, 10)
    return f'<svg viewBox="0 0 300 90" style="width:{w}px"><path d="M{b_} 12 L{a} 45 L{b_} 78" fill="none" stroke="{C}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/></svg>'
def slur():   # her 14 Nov: the slur sits on the head side of the notes
    return f'<svg viewBox="0 0 520 250" style="width:520px">' + ''.join(f'<text x="{60 + i * 120}" y="{176 - i * 14}" font-family="NM" font-size="130" fill="{N}">{CR}</text>' for i in range(4)) + f'<path d="M70 208 Q270 262 448 164" fill="none" stroke="{C}" stroke-width="6" stroke-linecap="round"/></svg>'
RPT = '<span style="font-family:Atkinson Hyperlegible,sans-serif;font-size:34px">:</span>‖'
NTH = lambda k: f'<small style="position:absolute;top:-34px;left:-3px;right:8px;height:22px;border-top:3px solid {C};border-left:3px solid {C};padding:0 8px;font-size:19px;line-height:22px;text-align:left;font-family:Atkinson Hyperlegible,sans-serif">{k}.</small>'
def touch():   # legato, staccato, accent as sound bars: how long each of four notes sounds
    def r(lab, sub, bars): return f'<div style="display:flex;align-items:center;gap:26px;margin:14px 0"><div style="width:150px;text-align:right"><b style="font-size:26px;color:{N}">{lab}</b><br><span style="font-size:17px;color:#6d6f9c">{sub}</span></div><div style="display:flex;gap:0;align-items:flex-end;height:44px">{bars}</div></div>'
    cell = lambda inner: f'<span style="width:92px;height:44px;display:flex;align-items:flex-end">{inner}</span>'
    leg = ''.join(cell(f'<span style="width:92px;height:30px;background:{C};border-right:2px solid #fff;box-sizing:border-box"></span>') for _ in range(4))
    sta = ''.join(cell(f'<span style="width:30px;height:30px;background:{C};border-radius:4px"></span>') for _ in range(4))
    acc = ''.join(cell(f'<span style="width:0;height:0;border-left:80px solid {C};border-top:{44 if i == 0 else 22}px solid transparent;opacity:{1 if i == 0 else .55}"></span>') for i in range(4))
    return '<div>' + r('Legato', 'joined', leg) + r('Staccato', 'short', sta) + r('Accent', 'first note stronger', acc) + '</div>'
ROOMSTORY.update({
 'hbr-L2': ('Practising well', [
   (cards([('1', 'Slow'), ('2', 'Small'), ('3', 'Correct')]), '<p>Good practice is <b>slow</b>, <b>small</b> and <b>correct</b>.</p><p>Slow enough to get it right. A small piece at a time. And right from the very first try.</p>', 'Choose two bars of your piece. Play them at half speed, with no wrong notes.'),
   (ladder(['60', '66', '72', '80']), '<p>When it is right <b>three times</b> in a row, go <b>one step faster</b>.</p><p>If it falls apart, step back down. This is the metronome ladder.</p>', 'Set a metronome (a ticking beat-keeper; there is one in the app) to 60. Play your two bars three times. All right? Move up to 66.'),
   (boxes(['1', '2', '3', '4'], red={2}), '<p>Every piece has a <b>hardest bar</b>. Find it and practise it <b>first</b>, while your mind is fresh.</p><p>Then join it to the bar before and the bar after.</p>', 'Find the hardest bar in your piece. Play it slowly five times, then play it with its neighbours.')]),
 'hbr-P3': ('The staff and the keyboard', [
   (grand(), '<p>Piano music uses <b>two staves</b> joined together: the top one for the right hand, the bottom one for the left.</p><p>The curly sign at the top is the <b>treble clef</b>. The one below is the <b>bass clef</b>.</p><p><b>Middle C</b> sits between them, on a little line of its own.</p>', 'Find Middle C: the C nearest the middle of your piano. Play it with each thumb.'),
   (st([(-2, 'C'), (-1, 'D'), (0, 'E'), (1, 'F'), (2, 'G')]), '<p>From Middle C, each <b>step up</b> on the staff, line to space, space to line, is the <b>next white key</b> to the right.</p><p>Line, space, line, space, line: C, D, E, F, G.</p>', 'Right thumb on Middle C. Play C D E F G while you look at the five notes on the staff.')]),
 'hbr-P4': ('Reading the notes', [
   (st([(0, 'E'), (2, 'G'), (4, 'B'), (6, 'D'), (8, 'F')]), '<p>The five <b>lines</b> of the treble staff are <b>E G B D F</b>, from the bottom up.</p><p>A sentence helps: <b>E</b>very <b>G</b>ood <b>B</b>oy <b>D</b>eserves <b>F</b>un.</p>', 'Play E G B D F going up from the E above Middle C, saying the sentence.'),
   (st([(1, 'F'), (3, 'A'), (5, 'C'), (7, 'E')]), '<p>The four <b>spaces</b> of the treble staff spell a word: <b>F A C E</b>.</p><p>Lines and spaces take turns, so the notes go F, G, A, B, C, D, E.</p>', 'Play F A C E going up. Then play F G A and say which is a space and which is a line.'),
   (st([(0, 'G'), (2, 'B'), (4, 'D'), (6, 'F'), (8, 'A')], clef='b'), '<p>The bass staff is different. Its <b>lines</b> are <b>G B D F A</b>: <b>G</b>reat <b>B</b>ig <b>D</b>ragons <b>F</b>ly <b>A</b>way.</p><p>Its spaces are <b>A C E G</b>: <b>A</b>ll <b>C</b>ows <b>E</b>at <b>G</b>rass.</p>', 'With your left hand, play G B D F A going up from the second G below Middle C, saying the sentence.')]),
 'hbr-T3': ('How long is a note?', [
   (row((big(SB, 96), apples(4, 26), False), (big(DM, 96), apples(3, 26), False), (big(MI, 96), apples(2, 26), False), (big(CR, 96), apples(1, 26), False), gap=44), '<p>One circle is <b>one beat</b>. A <b>crotchet</b> is one circle. A <b>minim</b> is two, a <b>dotted minim</b> three and a <b>semibreve</b> four.</p><p>Now come the notes shorter than one beat: pieces of the circle.</p>', 'Play C as a semibreve, a dotted minim, a minim and a crotchet, counting the beats out loud: 1 2 3 4.'),
   (row((big(QV), apples(.5, 44), False), (bq(2, 150), apples(1, 44, div=2), True), (big('=', 70), '', False), (big(CR), apples(1, 44), False), gap=40), '<p>Cut the circle in half. A <b>quaver</b> is <b>half a beat</b>, and on its own it has a <b>tail</b>.</p><p>Put two halves together and you have one whole beat: two quavers joined by a <b>beam</b>. We count them <b>1 and</b>.</p>', 'Play C in crotchets, counting 1 2 3 4. Then in quavers, counting 1 and 2 and 3 and 4 and.'),
   (row((big(SQ), apples(.25, 44), False), (bq(4, 150, beams=2), apples(1, 44, div=4), True), (big('=', 70), '', False), (big(CR), apples(1, 44), False), gap=36), '<p>Cut each half again. A <b>semiquaver</b> is a <b>quarter of a beat</b>, and on its own it has <b>two tails</b>.</p><p>Put four quarters together and you have one whole beat: four semiquavers joined by <b>two beams</b>. Say <b>wa-ter-me-lon</b>.</p>', 'Clap four beats. Then tap four semiquavers on every beat, saying wa-ter-me-lon.'),
   (row((big(MI, 110), apples(2, 30), False), (big('+', 60), '', False), (big(CR, 110), apples(1, 30), False), (big('=', 60), '', False), (big(DM, 110), apples(3, 30), True), gap=26), '<p>A <b>dot after a note</b> makes it longer: it adds <b>half</b> of the note again.</p><p>A minim is 2 beats. Half of 2 is 1. So a dotted minim is 2 + 1 = <b>3 beats</b>.</p>', 'Play C as a minim, counting 1 2. Then as a dotted minim, counting 1 2 3.'),
   (row((big(DC), apples(1.5, 38), False), (big(QV), apples(.5, 38), True), gap=70), '<p>The same dot works on a crotchet: 1 + ½. A <b>dotted crotchet</b> is <b>one beat and a half</b>.</p><p>A quaver usually follows it to finish the second beat. Long, then short: <b>1 – 2 and</b>.</p>', 'Play C long, then D short, counting 1, 2 AND. The D comes on the “and”.'),
   (tie(), '<p>A <b>tie</b> is a curved line joining two notes of the <b>same</b> pitch. Play the first one and <b>hold</b> through the second.</p><p>A minim tied to a crotchet lasts three beats.</p>', 'Play C and hold it for 1 2 3. You have played two notes with one press.'),
   (row((big(RC), '1 beat', False), (big(RM), '2 beats', False), (big(RS), '4 beats', False), gap=80), '<p>A <b>rest</b> is a beat of <b>silence</b>. You count it just like a note, but you do not play.</p><p>The crotchet rest lasts 1 beat. The minim rest sits on a line for 2. The semibreve rest hangs under a line for 4.</p>', 'Play C, C, then lift your hand for one beat, then C: 1, 2, (rest), 4. Keep counting through the silence.')]),
 'hbr-T4': ('Time signatures', [
   (f'<div style="display:flex;align-items:center;gap:36px">{tsig(4, 4)}{beats([4])}</div>', '<p>The two numbers at the start are the <b>time signature</b>.</p><p>The <b>top number</b> says how many beats are in every bar. The bottom 4 says each beat is a crotchet.</p>', 'Clap four beats in a bar, the first one stronger: ONE two three four.'),
   (f'<div>{tsrow(2, 4, 2)}{tsrow(3, 4, 3)}{tsrow(4, 4, 4)}</div>', '<p><b>Two</b> in a bar marches: left, right. <b>Three</b> in a bar swings round, like a waltz. <b>Four</b> in a bar walks.</p><p>Beat 1 is always the strongest.</p>', 'Clap each one: ONE two · ONE two three · ONE two three four. Which does your piece use?'),
   (cards([('1', 'Andante<br><span style="font-weight:400;font-size:17px">at a walk</span>'), ('2', 'Moderato<br><span style="font-weight:400;font-size:17px">not slow, not fast</span>'), ('3', 'Allegro<br><span style="font-weight:400;font-size:17px">quick and lively</span>')]), '<p>A word above the first bar tells you <b>how fast</b> the beat goes. The words are Italian.</p><p><b>Andante</b> is a walking speed. <b>Moderato</b> is in the middle. <b>Allegro</b> is quick and lively.</p>', 'Clap four beats Andante, then Moderato, then Allegro. Find the speed word at the top of your piece.')]),
 'hbr-T8': ('Repeats', [
   (boxes(['A', 'B &nbsp;' + RPT], red={1}), '<p>Two dots beside a double bar line make a <b>repeat sign</b>. It means: <b>go back and play it again</b>.</p><p>So this music is played A B, then A B once more.</p>', 'Find a repeat sign in your book. Play up to it, then go back to the start and play it again.'),
   (boxes(['A', NTH(1) + 'B &nbsp;' + RPT, NTH(2) + 'C'], red={1, 2}), '<p>Sometimes the ending changes. The bar marked <b>1</b> is played the first time only.</p><p>The second time, <b>skip it</b> and jump to the bar marked <b>2</b>: A B, then A C.</p>', 'Say the order out loud for this picture: A, B, back, A, C. Then look for a first-time bar in your music.')]),
 'hbr-E2': ('Touch: smooth and short', [
   (touch(), '<p>The same notes can be played in different ways. <b>Legato</b> means smooth and joined. <b>Staccato</b>, a dot above or below the note head, means short. (A dot <i>after</i> a note makes it longer.)</p><p>An <b>accent</b> (&gt;) means that note is stronger.</p>', 'Play C D E F G smoothly, each finger passing the sound to the next. Then play it staccato, like hot keys.'),
   (slur(), '<p>A curved line over <b>different</b> notes is a <b>slur</b>. Play them smoothly, in one breath, and lift gently at the end.</p><p>A tie joins the same note; a slur joins different ones.</p>', 'Play C D E F as one slur: sink into the C, float off the F.')]),
 'hbr-S1': ('Major scales', [
   (kbm(8, 0, white={i: str(i + 1) for i in range(8)}), '<p>A <b>scale</b> is a ladder of eight notes. Play the white keys from C to the next C and you have <b>C major</b>.</p><p>Notes <b>3–4</b> and <b>7–8</b> are close together, with no black key between. Every other pair has a black key between.</p>', 'Play C major going up with one finger, saying the numbers 1 to 8. Listen for the two close steps. (Fingering comes in step 3.)'),
   (kbm(8, 4, white={0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 7: '8'}, black={6: '7'}), '<p>Start the same ladder on G and one note has to change: the 7th note becomes <b>F sharp</b>, so that 7–8 stay close. A <b>sharp</b> (♯) is the very next key to the right, here a black one.</p><p>That is <b>G major</b>: one sharp, F♯.</p>', 'Play G A B C D E, then the black key F♯, then G. Now try it with a white F: hear how it sounds wrong.'),
   (kbm(8, 0, white={i: '12312345'[i] for i in range(8)}), '<p>Eight notes, five fingers. Going up, the right hand plays <b>1 2 3</b>, then the <b>thumb tucks under</b> and plays <b>1 2 3 4 5</b>.</p><p>From one C to the next is one <b>octave</b>. Coming down, play 5 4 3 2 1, then finger 3 crosses over: 3 2 1.</p>', 'Right hand, C major, one octave up and down, slowly. Say the finger numbers. Your teacher will show you the left hand.'),
   (cards([('0', 'C major<br>A minor'), ('1 ♯', 'G major<br>E minor')], cols=2, wd=230), '<p>Music in G major would need a sharp on every F. So one sharp is printed once, right after the clef. That is the <b>key signature</b>.</p><p>No sharps: C major or A minor. One sharp: G major or E minor.</p>', 'Look at the start of your piece. How many sharps are after the clef? Say which two keys it could be.')]),
 'hbr-S2': ('Minor scales', [
   (kbm(8, 5, white={i: 'ABCDEFGA'[i] for i in range(8)}), '<p>Play the white keys from A to A and you have <b>A minor</b>. It uses the same notes as C major, but A is home, and it sounds darker.</p><p>This plain form is the <b>natural minor</b>.</p>', 'Play C major up and down, then A natural minor. Same white notes, a different mood.'),
   (kbm(8, 5, white={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 7: 'A'}, black={6: 'G♯'}), '<p>Raise the 7th note one key, G to <b>G sharp</b>, and the scale pulls strongly back home.</p><p>This is the <b>harmonic minor</b>: A B C D E F G♯ A.</p>', 'Play A harmonic minor slowly. Stop on G♯ and feel how much it wants to go up to A.'),
   (kbm(8, 2, white={0: 'E', 2: 'G', 3: 'A', 4: 'B', 5: 'C', 7: 'E'}, black={1: 'F♯', 6: 'D♯'}), '<p><b>E minor</b> uses the same notes as G major, so it keeps <b>F sharp</b>. E is home.</p><p>For the harmonic minor, raise its 7th note too: D becomes <b>D sharp</b>.</p>', 'Play E natural minor (with F♯), then E harmonic minor (F♯ and D♯).')]),
 'hbr-H1': ('Chords and triads', [
   (kbm(7, 0, white={0: 'C', 2: 'E', 4: 'G'}), '<p>A <b>chord</b> is three or more notes played together. The simplest chord is a <b>triad</b>: three notes.</p><p>To build one: <b>play one, skip one, play one, skip one, play one</b>. C, E, G.</p>', 'Right hand fingers 1, 3 and 5 on C, E and G. Play them one at a time, then all together.'),
   (f'<div>{kbm(7, 4, white={0: "G", 2: "B", 4: "D"}, w=520, h=120)}<div style="height:18px"></div>{kbm(7, 5, white={0: "A", 2: "C", 4: "E"}, w=520, h=120)}</div>', '<p>The same shape works on other white keys too. On G it gives <b>G B D</b>. On A it gives <b>A C E</b>.</p><p>The bottom note names the triad. C and G sound bright: <b>major</b>. A sounds darker: <b>minor</b>.</p>', 'Keep your hand in the triad shape and move it: C E G, then G B D, then A C E.')]),
})
PRACT.update({
 'hbr-L2': lambda: wb_pick(ROOMS['hbr-L2'], ['Good habit?', 'My fifteen minutes']),
 'hbr-P3': lambda: wb_pick(ROOMS['hbr-P3'], ['Which key?', 'Count from Middle C']),
 'hbr-P4': lambda: wb_pick(ROOMS['hbr-P4'], ['The letters on the staff', 'Treble clef notes']),
 'hbr-T3': lambda: [ex(1, 'How many beats?', 'Write the beats. A quaver is ½. The first is done.', grid([(G(CR), DONE('1')), (G(QV), BOX), (G(DC), BOX), (G(MI), BOX), (G(DM), BOX)], 5)),
                    ex(2, 'Add them up', 'Write the total number of beats. The first is done.', tbl_l(['Notes', 'Beats'], [[bq(2, 46), DONE('1')], [bq(4, 46, beams=2), BOX], [G(DC + ' ' + QV, 40), BOX], [G(MI, 40) + ' <span style="font-size:22px;color:#e4572e">‿</span> ' + G(CR, 40) + ' <span class="sm">(tied)</span>', BOX], [G(CR + ' ' + RC + ' ' + MI, 40), BOX]]), 2)],
 'hbr-T4': lambda: [ex(1, 'How many beats in a bar?', 'Write the top number that fits. The first is done.', tbl_l(['One bar', 'Beats'], [[G(CR + ' ' + CR + ' ' + CR, 40), DONE('3')], [G(MI + ' ' + MI, 40), BOX], [G(CR + ' ' + CR, 40), BOX], [G(DM, 40), BOX], [G(MI + ' ' + CR + ' ' + CR, 40), BOX]])),
                    ex(2, 'Two, three or four?', 'Clap each one with a strong beat 1. Write 2, 3 or 4.', tbl_l(['It feels like…', 'Beats in a bar'], [['LEFT right, LEFT right', BOX], ['ONE two three, ONE two three', BOX], ['ONE two three four', BOX]]), 2)],
 'hbr-T8': lambda: [ex(1, 'Write the order', 'Each letter is one bar. At a repeat sign, go back to the start once. Write the letters in the order you play them. The first is done.', tbl_l(['The music', 'You play'], [['A &nbsp; B &nbsp;' + RPT, DONE('A B A B')], ['A &nbsp;' + RPT + '&nbsp; B', LINE], ['A &nbsp; B &nbsp; C &nbsp;' + RPT, LINE], ['A &nbsp; B &nbsp;' + RPT + '&nbsp; C', LINE]]))] + [x.replace('|: ', '').replace(':|', RPT) for x in STEP['hbr-T8'][1:2]],
 'hbr-E2': lambda: wb_pick(ROOMS['hbr-E2'], ['Which notes are short?', 'Slur or tie?']),
 'hbr-S1': lambda: [ex(1, 'Write the scale', 'Write the eight notes going up. The first is done.', tbl_l(['Scale', 'Notes'], [['C major', DONE('C D E F G A B C')], ['G major', LINE]])),
                    ex(2, 'Where are the close steps?', 'In a major scale two pairs of notes are close together, with no key between. Write their numbers.', '<p style="font-size:15px">Notes ' + BOX + ' – ' + BOX + ' &nbsp; and &nbsp; notes ' + BOX + ' – ' + BOX + '</p>', 2)],
 'hbr-S2': lambda: [ex(1, 'Write the scale', 'Write the eight notes going up. The first is done.', tbl_l(['Scale', 'Notes'], [['A natural minor', DONE('A B C D E F G A')], ['A harmonic minor', LINE], ['E natural minor', LINE], ['E harmonic minor', LINE]])),
                    ex(2, 'Which note is raised?', 'In the harmonic minor the 7th note goes up one key. Write it. The first is done.', tbl_l(['Scale', 'The 7th note becomes'], [['A harmonic minor', DONE('G sharp')], ['E harmonic minor', LINE]]), 2) + ex(3, 'Same notes as…', 'Each minor scale shares its notes with a major scale. Write it.', tbl_l(['Minor', 'Major'], [['A minor', DONE('C major')], ['E minor', LINE]]), 1)],
 'hbr-H1': lambda: [ex(1, 'Build the triad', 'Play one, skip one, play one, skip one, play one. Write the three notes. The first is done.', tbl_l(['On', 'The triad'], [['C', DONE('C E G')], ['G', LINE], ['A', LINE], ['E', LINE]])),
                    ex(2, 'Major or minor?', 'Play each triad and listen: bright or dark? Circle one. The first is done.', tbl_l(['Triad', ''], [['C E G', '<span style="border:2px solid #e4572e;border-radius:12px;padding:0 6px;color:#e4572e">major</span> &nbsp;·&nbsp; minor'], ['A C E', 'major &nbsp;·&nbsp; minor'], ['G B D', 'major &nbsp;·&nbsp; minor'], ['E G B', 'major &nbsp;·&nbsp; minor']]), 2)],
})
ROOMSTORY['x-dyn'] = ('Loud and soft', [
   (dyn([('p', 'soft', 60, .4), ('mp', 'quite soft', 105, .6), ('mf', 'quite loud', 150, .8), ('f', 'loud', 200, 1)]), '<p>Four signs tell you how loud to play. <b><i>p</i></b> is <i>piano</i>, soft. <b><i>f</i></b> is <i>forte</i>, loud.</p><p><i>Mezzo</i> means medium: <b><i>mp</i></b>, mezzo piano, is quite soft and <b><i>mf</i></b>, mezzo forte, is quite loud.</p>', 'Play C four times: p, mp, mf, f. Four steps, the same speed.'),
   (dyn([('pp', 'very soft', 40, .3), ('p', '', 75, .45), ('mp', '', 110, .6), ('mf', '', 145, .75), ('f', '', 180, .9), ('ff', 'very loud', 215, 1)]), '<p>Two letters mean <b>very</b>: <b><i>pp</i></b> is very soft, <b><i>ff</i></b> is very loud.</p><p>That makes six steps, from a whisper to a shout.</p>', 'Play C six times, one step louder each time. Then come back down the steps.'),
   (f'<div style="display:flex;gap:70px;justify-content:center">' + ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{hairpin(o, 250)}<b style="font-size:24px;color:{N}">{w_}</b><span style="font-size:18px;color:#6d6f9c">{t_}</span></div>' for o, w_, t_ in ((True, 'crescendo', 'getting louder'), (False, 'diminuendo', 'getting softer'))) + '</div>', '<p>A sign that <b>opens</b> means get louder little by little: <b>crescendo</b>. A sign that <b>closes</b> means get softer: <b>diminuendo</b>.</p><p>The wide end is the loud end.</p>', 'Play C D E F G getting louder, then G F E D C getting softer.')])
PRACT['x-dyn'] = lambda: [ex(1, 'What does it mean?', 'Write the meaning. The first is done.', tbl_l(['Sign', 'Means'], [['<i><b>mp</b></i>', DONE('quite soft')], ['<i><b>mf</b></i>', LINE], ['<i><b>pp</b></i>', LINE], ['<i><b>ff</b></i>', LINE]])),
                          ex(2, 'Softest to loudest', 'Write the six signs in order, from the softest to the loudest. The first is done.', '<p style="font-size:17px"><i><b class="done2">pp</b></i> &nbsp; ' + (BOX + ' &nbsp; ') * 5 + '</p><p class="how" style="margin-top:10px">f &nbsp;·&nbsp; mp &nbsp;·&nbsp; ff &nbsp;·&nbsp; p &nbsp;·&nbsp; mf</p>', 2)]
ROOMS['x-dyn'] = dict(ROOMS['hbr-E1'], id='x-dyn')
def build_story(floor_i, name, line):
    global RIGHT; RIGHT = name.upper()
    out = []; toc = []; n = 2
    ids = [x for x in FLOORS[floor_i]['ids'] if not ROOMS[x].get('review')]   # her 14 Nov: no review room, the basics are taught in rooms of their own
    if name == 'Prelim': ids.insert(1, 'x-dyn')
    for i, rid in enumerate(ids, 1):
        r = ROOMS[rid]
        if r.get('ear'):
            toc.append((i, 'Ear training')); a, b_ = ear_story(r, name, i, n); out += [section(a, n, 'L' + rid), section(b_, n + 1, 'P' + rid)]; n += 2; continue
        if r.get('review'):
            toc.append((i, 'Review')); a, b_ = review_spread(r, name, i); out += [section('<div class="rvbig">' + a + '</div>', n, 'L' + rid), section('<div class="rvbig">' + b_ + '</div>', n + 1, 'P' + rid)]; n += 2; continue
        title, steps = ROOMSTORY[rid]; toc.append((i, title))
        for k, (pic, text, piano) in enumerate(steps, 1):
            out.append(section(story(name, i, title, k, len(steps), pic, text, piano, rid, k == 1), n, f'S{k}{rid}')); n += 1
        pr = practise_for(rid)   # her 13 Nov: big and simple, two exercises a page
        out.append(section(f'<div class="cxk cxc">Room {i} <i>◆</i> {title} <i>◆</i> Practise</div><div class="prbig">' + ''.join(pr) + '</div>', n, 'P' + rid)); n += 1
    if 0 and name in EXAM:   # her 14 Nov: comparable to the exam level, but nothing exam-only in the book
        earn = next((k for k, t_ in toc if t_ == 'Ear training'), '')
        a, b_ = exam_spread(name, toc, earn); out += [section('<div class="rvbig xl">' + a + '</div>', n, 'LX'), section('<div class="rvbig">' + b_ + '</div>', n + 1, 'PX')]; n += 2; toc.append(('', 'The exam corner'))
    cover = f'''<section class="pg part2"><div class="pframe"><div class="pk">The Piano Butler · Level book</div><div class="pt">{name}</div><div class="pdv"></div>
<p class="pl">{line}</p><div class="pin"><div class="pih">The rooms</div>{"".join(f'<div class="tr"><span>{str(i) + " · " if i else ""}{t}</span><span class="dots"></span><span></span></div>' for i, t in toc)}</div></div></section>'''
    extra = EXTRA_CSS + """
section.pg.cx{padding:40px 50px 36px} .prbig{zoom:1.38;margin-top:14px} .prbig figure.vx svg{max-height:120px!important} .rvbig{zoom:1.55} .rvbig.xl{zoom:1.42} .rvbig .tk5{margin-top:8px} .prbig .sent .ab{min-width:74px} .prbig .sent .ab.hasdone{padding:0 6px} .prbig .ex2{margin-bottom:18px}
.cx .lbtop{display:flex;justify-content:space-between;font-size:9.5px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#6d6f9c;padding-bottom:7px} .cx svg.dent{display:block;width:100%;height:16px}
.cx .fr{position:relative;height:938px;box-sizing:border-box;padding:18px 0 0} .cx .fr>.foot{position:absolute;left:0;right:0;bottom:2px;height:1px;visibility:hidden}
.cx .lbbot{position:absolute;left:50px;right:50px;bottom:44px} .cx .plq{position:absolute;bottom:37px;left:50%;transform:translateX(-50%);background:#26296b;color:#fff;min-width:30px;height:30px;line-height:30px;text-align:center;font-family:'Playfair Display',PF,serif;font-weight:700;font-size:14px;box-shadow:0 0 0 6px #fff}
.cx .kk{font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#e4572e;margin-bottom:2px} .cx h1.lbh{font-family:'Playfair Display',PF,serif;font-weight:700;font-size:42px;line-height:1.08;color:#26296b;margin:0 0 12px}
.cx .lvhead{display:flex;justify-content:space-between;align-items:flex-start;border:0;padding:0} .cx .kick{font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#e4572e}
.stpic{position:relative;height:400px;margin:0 0 16px;display:flex;align-items:center;justify-content:center;overflow:hidden} .stpic>.stin{display:block;width:max-content;max-width:680px;flex:none;transform-origin:center center} .stpic .hero{margin:0!important;border:0!important;background:none!important;width:640px} .stpic .hcap{display:none}
.stpic svg{display:block;max-width:none}
.bub{display:flex;gap:14px;align-items:center;margin:0 0 16px} .bub .bf{flex:none} .bub .bt{position:relative;flex:1;background:#fff;border:2px solid #26296b;border-radius:18px;padding:14px 20px;color:#26296b} .bub .bt p{margin:0;font-size:25px!important;line-height:1.4!important} .bub .bt b{color:#e4572e}
.bub .bt:before{content:'';position:absolute;left:-11px;top:50%;margin-top:-9px;border:9px solid transparent;border-right-color:#26296b;border-left:0}
.sttx{font-size:24px;line-height:1.45;color:#26296b} .sttx p{margin:0 0 12px;font-size:25px!important;line-height:1.42!important} .sttx b{color:#e4572e}
.try{margin-top:16px;background:#fff;border:2px solid #26296b;border-radius:16px;padding:12px 18px 14px;color:#26296b} .try .tt{font-family:'Playfair Display',PF,serif;font-size:21px;font-weight:700;margin-bottom:6px} .try .li{display:flex;gap:14px;align-items:center;font-size:20px;line-height:1.38}
.try .nb{flex:none;width:28px;height:28px;background:#26296b;color:#fff;text-align:center;line-height:28px;font-family:'Playfair Display',PF,serif;font-weight:700;font-size:15px} .try .tx{flex:1;font-size:21px!important;line-height:1.38!important} .try .nb{font-size:15px!important} .try .tt{font-size:22px!important} .try .ck{flex:none;width:24px;height:24px;border:2px solid #c9cbe0;border-radius:50%}
.k5big>div{width:86px!important;height:190px!important} .k5big b{font-size:40px!important} .k5big span{font-size:26px!important}
"""
    fit = """<script>(async()=>{try{await document.fonts.ready}catch(e){}
document.querySelectorAll('.stpic').forEach(b=>{const i=b.querySelector('.stin');if(!i)return;const W=b.clientWidth-40,H=b.clientHeight-24,w=i.offsetWidth,h=i.offsetHeight;if(!w||!h)return;const s=Math.min(W/w,H/h,2.4);i.style.transform='scale('+s.toFixed(3)+')';});
document.querySelectorAll('section.pg .body').forEach(b=>{const s=b.closest('section'),f=s.querySelector('.foot');if(!f)return;const lim=f.getBoundingClientRect().top-20,top=b.getBoundingClientRect().top;let m=0;[...b.children].forEach(c=>{const r=c.getBoundingClientRect();if(r.height)m=Math.max(m,r.bottom)});if(m>lim){b.style.zoom=Math.max(.6,(lim-top)/(m-top)).toFixed(3);}});
document.body.dataset.pruned='1';})();</script>"""
    for _a, _b in [(' Start from G.', ''), ('notes have dots.', 'notes have a staccato dot.'), ('faster to fix a slip', 'play faster after a slip'), ('walk in, bow, play, bow.', 'walk in, sit, breathe out, play.')]: out = [o.replace(_a, _b) for o in out]
    out = [o.replace('Try it · 10 seconds', 'Try it') if 'rvbig' in o else o for o in out]
    out = [o.replace('M1576,1057 C2341,396 5000,316 5564,787 C4981,376 2363,455 1576,1057', 'M1420,1560 C2500,1940 4600,1770 5420,1330 C4600,1700 2500,1870 1420,1560') for o in out]
    out = [re.sub(r'<div class="cxk cxc">Room (\d+) <i>◆</i> (.*?) <i>◆</i> (\d+ of \d+|Practise)</div>', lambda m: f'<div class="kk">Room {m.group(1)} · ' + ('Practise' if m.group(3) == 'Practise' else 'Step ' + m.group(3)) + f'</div><h1 class="lbh">{m.group(2)}</h1>', o) for o in out]
    out = [re.sub(r'<div class="cxk">Room (\d+) <i>◆</i> (\d+ of \d+)</div><h1>', lambda m: f'<div class="kk">Room {m.group(1)} · Step {m.group(2)}</div><h1 class="lbh">', o) for o in out]
    def _staffhead(o):   # her 14 Nov (picture of a five-line header): the room title sits on a staff across the top, the page number in coral at its right end
        t = re.search(r'<h1 class="lbh">(.*?)</h1>', o, flags=re.S); n_ = re.search(r'<div class="plq">(\d+)</div>', o)
        if not (t and n_): return o
        o = o.replace(t.group(0), '', 1).replace(n_.group(0), '', 1)
        return re.sub(r'<div class="lbtop">.*?</div>', f'<div class="sth"><span class="stt">{t.group(1)}</span><span class="stn">{n_.group(1)}</span></div>', o, count=1, flags=re.S)
    out = [re.sub(r'<div class="stpn"><span>At the piano</span>(.*?)</div>', lambda m: f'<div class="try"><div class="tt">Try it at the piano</div><div class="li"><span class="nb">1</span><span class="tx">{m.group(1)}</span><span class="ck"></span></div></div>', o, flags=re.S) for o in out]
    out = [re.sub(r'<div class="sttx">(<p>.*?</p>)', lambda m: f'<div class="bub"><div class="bf">{RABBIT}</div><div class="bt">{m.group(1)}</div></div><div class="sttx">', o, count=1, flags=re.S) for o in out]
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body>{cover}{"".join(out)}{fit}</body></html>'
    fn = f'/mnt/user-data/outputs/house-rooms/levelbook-{name.lower()}.html'
    open(fn, 'w').write(html); return fn
if __name__ == '__main__':
    print(build_story(0, 'Beginner', 'Read it like a storybook: one step on each page, a big picture, a few words, and one thing to try at the piano. After each room, a page to practise.'))
    print(build_story(1, 'Prelim', 'One step on each page: a big picture, a few words, and one thing to try at the piano. After each room, a page to practise. The last room trains your ears.'))
