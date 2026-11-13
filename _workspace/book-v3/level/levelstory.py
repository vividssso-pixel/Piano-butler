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
    return '<div style="display:flex;align-items:flex-end;justify-content:center;gap:22px">' + ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px"><span style="width:74px;height:{h}px;background:{C};opacity:{o};border-radius:6px 6px 0 0"></span><i style="font-family:\'Playfair Display\',serif;font-weight:900;font-size:44px;color:{N};line-height:1">{s}</i><span style="font-size:17px;color:{N}">{w}</span></div>' for s, w, h, o in items) + '</div>'

def story(name, i, title, k, n, pic, text, piano, rid=None, first=False):
    r = ROOMS[rid] if rid else None
    q = f'<a class="lvqr" href="{listen_url(r)}">{qr(listen_url(r))}<span>Scan to listen</span></a>' if first and r and r.get('ch') != 'EAR' else ''
    hd = f'<div class="lvhead"><div><div class="kick">{name} · Room {i} · {k} of {n}</div><h1>{title}</h1></div>{q}</div>' if first else f'<div class="kick fk2">{name} · Room {i} · {title} · {k} of {n}</div>'
    return f'{hd}<div class="stpic"><div class="stin">{pic}</div></div><div class="sttx">{text}</div><div class="stpn"><span>At the piano</span>{piano}</div>'
ROOMSTORY = {
 'hbr-B1': ('Sitting and hands', [
   (hb(18, 'hero'), '<p><b>Sit tall</b> on the front half of the stool, with both <b>feet flat</b> on the floor.</p><p>Your arms float out in front, <b>level with the keys</b>, like a table top.</p>', 'Sit down. Lift your shoulders up to your ears, then let them drop.'),
   (app('2:The good shape'), '<p>Hold a small ball in your hand. That <b>round shape</b> is your playing hand.</p><p>Your knuckles stand up like a <b>bridge</b>, and you play on your <b>fingertips</b>.</p>', 'Hold a ball or an orange. Put your hand on the keys without changing its shape.'),
   (row((app('2:flat fingers', 200), '✗ flat', True), (app('2:knuckles collapsed', 200), '✗ fallen in', True), (app('2:The good shape', 200), '✓ round', False), gap=14), '<p>A <b>flat</b> hand is lying down on the job. A bridge that has <b>fallen in</b> cannot carry anything.</p><p>The <b>round</b> hand can play all day.</p>', 'Make the flat hand, then the fallen bridge, then the round hand. Feel the difference.')]),
 'hbr-P1': ('The keyboard', [
   (kb(15, 600, 170), '<p>Look at the black keys. They come in <b>twos</b> and <b>threes</b>, again and again, all the way along.</p><p>Find the pattern once and you can never get lost.</p>', 'Touch every group of two black keys, from the bottom to the top. Then every group of three.'),
   (f'<svg viewBox="0 0 640 250" style="width:640px"><g transform="translate(20 60)">{kb(15, 600, 150)[kb(15, 600, 150).index(">") + 1:-6]}</g>{bear(70, 30, 1.7)}{bird(585, 30, 1.6)}<text x="70" y="246" text-anchor="middle" font-size="22" font-weight="700" fill="{N}" font-family="Atkinson Hyperlegible,sans-serif">low</text><text x="585" y="246" text-anchor="middle" font-size="22" font-weight="700" fill="{N}" font-family="Atkinson Hyperlegible,sans-serif">high</text></svg>', '<p><b>Left is low</b>, like a big grumpy bear. <b>Right is high</b>, like a little bird.</p><p>Go to the right and every key sounds a little higher.</p>', 'Play the lowest key you can reach, then the highest. Bear, then bird.'),
   (kb(7, 560, 190, labels=True, mark={0, 1, 2}), '<p>Every white key has a letter. Beside the <b>two</b> black keys live <b>C, D, E</b>. Beside the <b>three</b> live <b>F, G, A, B</b>.</p><p>After B comes C again: seven letters, round and round.</p>', 'Find a group of two black keys. Play the three white keys around it and say C, D, E.')]),
 'hbr-L1': ('Finger numbers', [
   (hb(163, 'hero'), '<p>Every finger has a <b>number</b>. The <b>thumb is 1</b>, then 2, 3, 4, and the little finger is <b>5</b>.</p><p>It is the same in both hands: thumbs are always 1.</p>', 'Hold up both hands. Wiggle finger 1, then 2, 3, 4, 5, saying the numbers.'),
   (keys5('1 2 3 4 5'.split()).replace('class="k5"', 'class="k5 k5big"'), '<p>Put your right thumb on C. Now each finger has its own key: <b>C D E F G</b> are fingers <b>1 2 3 4 5</b>.</p><p>One finger, one key. No finger has to jump.</p>', 'Thumb on C. Play C D E F G and back again, saying the finger numbers out loud.')]),
 'hbr-P2': ('The staff and the clefs', [
   (staff5([(150, 2, 'on a line'), (330, 3, 'in a space')]), '<p>Music is written on <b>five lines</b>, called the <b>staff</b>.</p><p>A note sits <b>on a line</b>, with the line through its middle, or <b>in a space</b> between two lines. Higher on the staff means higher on the piano.</p>', 'Count the lines from the bottom: 1, 2, 3, 4, 5. Then count the four spaces.'),
   (hb(27, 'hero'), '<p>A <b>clef</b> at the start says which notes the lines stand for.</p><p>The <b>treble clef</b> is the Queen of the high notes: her curl wraps round the line for <b>G</b>. The <b>bass clef</b> is the King of the low notes: his two dots hug the line for <b>F</b>.</p>', 'Right hand plays the Queen’s notes, high up. Left hand plays the King’s, down low. Play one of each.')]),
 'hbr-T1': ('The beat', [
   (beats([4, 4]), '<p>Music has a steady <b>beat</b>, like a heartbeat. It never speeds up and never stops.</p><p>We count the beats: 1, 2, 3, 4, and round again.</p>', 'Put a hand on your heart. Tap that steady beat on your knee and count 1 2 3 4.'),
   (beats([3, 3, 3], rest=4), '<p><b>Bar lines</b> put the beats into groups called <b>bars</b>. <b>Beat 1</b> of every bar is the strongest.</p><p>Sometimes a beat is <b>silent</b>. You still count it.</p>', 'Clap three in a bar: STRONG, weak, weak. Then leave out one clap, but keep counting.')]),
 'hbr-T2': ('Notes: crotchet and minim', [
   (row((big(CR), '1', False), (big(CR), '2', False), (big(CR), '3', False), (big(CR), '4', False)), '<p>This is a <b>crotchet</b>. It lasts <b>one beat</b>.</p><p>Four crotchets fill a bar of four: play, play, play, play.</p>', 'Play C four times, one for each beat, counting 1 2 3 4.'),
   (row((big(MI), '1 – 2', False), (big(MI), '3 – 4', False), gap=120), '<p>This is a <b>minim</b>. Its head is empty, and it lasts <b>two beats</b>.</p><p>Play on the first beat and <b>hold</b> through the second.</p>', 'Play C as a minim: press on 1, hold through 2. Then again on 3, holding through 4.'),
   (row((big(CR), 'play', False), (big(RC), 'shh', True), (big(CR), 'play', False), (big(RC), 'shh', True)), '<p>Silence has signs too, called <b>rests</b>. A <b>crotchet rest</b> is one beat of silence.</p><p>You count a rest just like a note. You just do not play.</p>', 'Play, shh, play, shh: C on beats 1 and 3, silence on 2 and 4. Keep counting.')]),
 'hbr-T2-s2': ('Notes: three beats and four', [
   (row((big(MI), '2 beats', False), (big('+', 70), '', False), (f'<span style="display:inline-block;width:26px;height:26px;border-radius:50%;background:{C};margin-bottom:26px"></span>', 'a dot', True), (big('=', 70), '', False), (big(DM), '3 beats', False), gap=26), '<p>A <b>dot</b> after a note makes it half as long again.</p><p>A minim is two beats. A <b>dotted minim</b> is two and one more: <b>three beats</b>.</p>', 'Play C and hold for 1 2 3. Sway on beat 1, like a waltz.'),
   (row((big(SB), '1 – 2 – 3 – 4', False)), '<p>This is a <b>semibreve</b>: an empty head and no stem. It lasts <b>four beats</b>, a whole bar of four.</p><p>Press once, and listen until the sound has had all four beats.</p>', 'Play C and hold for 1 2 3 4. Lift exactly when the next bar begins.'),
   (hb(53, 'hero'), '<p>Now you know the family. Each note is <b>half</b> of the one above it.</p><p>One semibreve is as long as two minims, or four crotchets.</p>', 'Left hand holds a semibreve on C while the right hand plays four crotchets on G.')]),
 'hbr-E1': ('Loud and soft', [
   (dyn([('p', 'soft', 70, .45), ('f', 'loud', 190, 1)]), '<p>Music can be <b>soft</b> or <b>loud</b>. The signs are Italian: <b><i>p</i></b> for <i>piano</i>, soft, and <b><i>f</i></b> for <i>forte</i>, loud.</p><p>To play louder, let more of your arm’s weight into the key. Do not hit it.</p>', 'Play C softly, like a secret. Then play it loudly, like calling across a field.'),
   (dyn([('pp', 'very soft', 40, .3), ('p', 'soft', 80, .45), ('f', 'loud', 160, .8), ('ff', 'very loud', 210, 1)]), '<p>Two letters mean <b>very</b>: <b><i>pp</i></b> is very soft, <b><i>ff</i></b> is very loud.</p><p>Soft does not mean slow, and loud does not mean fast. The beat stays the same.</p>', 'Play C four times: pp, p, f, ff. Four steps, the same speed.')]),
}
def build_story(floor_i, name, line):
    global RIGHT; RIGHT = name.upper()
    out = []; toc = []; n = 2
    for i, rid in enumerate(FLOORS[floor_i]['ids'], 1):
        r = ROOMS[rid]
        if r.get('ear'):
            toc.append((i, 'Ear training')); a, b_ = ear_spread(r, name, i, n); out += [section(a, n, 'L' + rid), section(b_, n + 1, 'P' + rid)]; n += 2; continue
        title, steps = ROOMSTORY[rid]; toc.append((i, title))
        for k, (pic, text, piano) in enumerate(steps, 1):
            out.append(section(story(name, i, title, k, len(steps), pic, text, piano, rid, k == 1), n, f'S{k}{rid}')); n += 1
        pr = practice(rid)[:3]
        out.append(section(f'<div class="kick">{name} · Room {i} · Practise</div><h1>Practise</h1>' + ''.join(pr), n, 'P' + rid)); n += 1
    cover = f'''<section class="pg part2"><div class="pframe"><div class="pk">The Piano Butler · Level book</div><div class="pt">{name}</div><div class="pdv"></div>
<p class="pl">{line}</p><div class="pin"><div class="pih">The rooms</div>{"".join(f'<div class="tr"><span>{i} · {t}</span><span class="dots"></span><span></span></div>' for i, t in toc)}</div></div></section>'''
    extra = EXTRA_CSS + """
.stpic{height:520px;margin:14px 0 24px;background:#faf8f3;border-radius:16px;display:flex;align-items:center;justify-content:center;overflow:hidden} .stpic>.stin{display:block;width:max-content;max-width:680px;flex:none;transform-origin:center center} .stpic .hero{margin:0!important;border:0!important;background:none!important;width:640px} .stpic .hcap{display:none}
.stpic svg{display:block;max-width:none}
.sttx{font-size:27px;line-height:1.45;color:#26296b} .sttx p{margin:0 0 16px;font-size:27px!important;line-height:1.45!important} .sttx b{color:#e4572e}
.stpn{margin-top:22px;border-top:2px solid #26296b;padding-top:14px;font-size:21px!important;line-height:1.45;color:#26296b} .stpn span{display:block;font-size:13px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e;margin-bottom:3px}
.k5big>div{width:86px!important;height:190px!important} .k5big b{font-size:40px!important} .k5big span{font-size:26px!important}
"""
    fit = """<script>(async()=>{try{await document.fonts.ready}catch(e){}
document.querySelectorAll('.stpic').forEach(b=>{const i=b.querySelector('.stin');if(!i)return;const W=b.clientWidth-48,H=b.clientHeight-40,w=i.offsetWidth,h=i.offsetHeight;if(!w||!h)return;const s=Math.min(W/w,H/h,2.4);i.style.transform='scale('+s.toFixed(3)+')';});
document.querySelectorAll('section.pg .body').forEach(b=>{const s=b.closest('section'),f=s.querySelector('.foot');if(!f)return;const lim=f.getBoundingClientRect().top-20,top=b.getBoundingClientRect().top;let m=0;[...b.children].forEach(c=>{const r=c.getBoundingClientRect();if(r.height)m=Math.max(m,r.bottom)});if(m>lim){b.style.zoom=Math.max(.6,(lim-top)/(m-top)).toFixed(3);}});
document.body.dataset.pruned='1';})();</script>"""
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body>{cover}{"".join(out)}{fit}</body></html>'
    fn = f'/mnt/user-data/outputs/house-rooms/levelbook-{name.lower()}.html'
    open(fn, 'w').write(html); return fn
if __name__ == '__main__':
    print(build_story(0, 'Beginner', 'Read it like a storybook: one step on each page, a big picture, a few words, and one thing to try at the piano. After each room, a page to practise.'))
