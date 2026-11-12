# The Piano Butler Handbook: Before you play (her 11 Nov: posture, hand shape and finger numbers come first; drawings now, photos later).
# Three pages, 18-20, just before the Part I opener (p. 21), so no other page number moves.
exec(open('/tmp/claude-0/pk/shape.py').read())   # helpers (rewrites the Shape and Play drafts, harmless)
def bpage(inner, n): return page(inner, n, 'BEFORE YOU PLAY')
import json as _js
APP = _js.load(open('/tmp/claude-0/pk/posture_svgs.json')); WF = _js.load(open('/tmp/claude-0/pk/warm_frames.json'))
def appsvg(svg, mw, uid):   # the app's own pen drawings (her 11 Nov: match the app's posture and hand-shape pictures)
    svg = svg.replace('width="100%" height="100%" ', '', 1).replace('<svg ', f'<svg style="width:100%;max-width:{mw}px;height:auto;display:block;margin:0 auto" ', 1)
    return _re.sub(r'(id="|url\(#|href="#)([a-z]+[a-z0-9]*)', lambda m: m.group(1) + m.group(2) + uid, svg)
def app(key, mw, uid): return appsvg(APP[key], mw, uid)
def warmpic(k, mw, uid, at=0.4): fr = WF[k]; return appsvg(fr[min(len(fr) - 1, int(len(fr) * at))][1], mw, uid)

SECRETS['B1'] = 'Sit tall, forearms level with the keys, a round hand on the fingertips: then let the arm’s weight do the work.'
NV, RD, SOFT, LINE = '#26296b', '#e4572e', '#5a5d8f', '#c9cbe0'
def mark(x, y, n): return f'<circle cx="{x}" cy="{y}" r="11" fill="{RD}"/><text x="{x}" y="{y + 4.5}" text-anchor="middle" font-family="AH,Arial" font-size="13" font-weight="700" fill="#fff">{n}</text>'
def lab(x, y, t, anchor='start', col=NV, fs=13.5, w=700): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="AH,Arial" font-size="{fs}" font-weight="{w}" fill="{col}">{t}</text>'
def sitter(ox=0, oy=0, sc=1.0, elbow=0, full=True):
    """side view: a pianist at the keys. elbow: 0 level, +1 elbow below the keys (stool too low), -1 elbow above them (stool too high)"""
    g = f'<g transform="translate({ox},{oy}) scale({sc})">'
    g += f'<rect x="300" y="118" width="150" height="16" rx="3" fill="{NV}"/><rect x="300" y="110" width="150" height="9" fill="#fff" stroke="{NV}" stroke-width="2"/>'   # keybed and keys
    g += f'<rect x="436" y="40" width="14" height="250" fill="{NV}"/>'                                                                                                  # piano front
    g += f'<rect x="96" y="208" width="120" height="12" rx="4" fill="{SOFT}"/><rect x="104" y="220" width="10" height="70" fill="{SOFT}"/><rect x="198" y="220" width="10" height="70" fill="{SOFT}"/>'   # stool
    g += f'<line x1="40" y1="290" x2="470" y2="290" stroke="{LINE}" stroke-width="2"/>'
    sh = (178, 82); hip = (166, 198); el = (212, 150 + 22 * elbow); wr = (300, 112)
    g += f'<circle cx="186" cy="52" r="20" fill="none" stroke="{NV}" stroke-width="4"/>'                                                     # head
    g += f'<path d="M{hip[0]},{hip[1]} L{sh[0]},{sh[1]}" stroke="{NV}" stroke-width="6" stroke-linecap="round"/>'                           # back
    g += f'<path d="M{sh[0]},{sh[1]} L{el[0]},{el[1]} L{wr[0]},{wr[1]}" fill="none" stroke="{NV}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'   # arm
    g += f'<path d="M{wr[0]},{wr[1]} q10,-8 22,-2" fill="none" stroke="{NV}" stroke-width="4" stroke-linecap="round"/>'                     # hand
    g += f'<path d="M{hip[0]},{hip[1]} L262,{hip[1]} L262,288 L286,288" fill="none" stroke="{NV}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'   # leg and foot
    return g + '</g>'
SIT = [('forearms level with the keys', 'wrist neither dropped nor lifted'), ('elbows a little in front of you', 'not pinned to your sides'),
       ('sit on the front half of the stool', 'opposite Middle C'), ('feet flat on the floor', 'the right foot near the pedal'), ('back tall, shoulders loose', 'lean a little towards the keys')]
def hero_sit():
    leg = '<div class="sitl">' + ''.join(f'<div><span class="rn">{i + 1}</span><b>{t}</b><span>{u}</span></div>' for i, (t, u) in enumerate(SIT)) + '</div>'
    return f'<div class="two" style="grid-template-columns:1.2fr 1fr;align-items:center"><div>{app("1:Just right", 380, "h")}</div><div>{leg}</div></div>'
def hand_side(kind='round', w=230, cap=True):
    """a hand from the side, on a key. kind: round, flat, dent (a collapsed knuckle)"""
    o = f'<svg viewBox="0 0 230 150" style="width:100%;max-width:{w}px;height:auto;display:block;margin:0 auto">'
    o += f'<rect x="10" y="118" width="210" height="14" fill="#fff" stroke="{NV}" stroke-width="2"/><rect x="10" y="132" width="210" height="8" fill="{NV}"/>'
    wrist = (24, 82)
    if kind == 'round': path = f'M{wrist[0]},{wrist[1]} Q78,58 120,56 Q160,58 176,82 Q186,104 184,117'
    elif kind == 'flat': path = f'M{wrist[0]},{wrist[1]} Q90,100 150,108 Q186,112 206,116'
    else: path = f'M{wrist[0]},{wrist[1]} Q70,66 116,68 Q140,90 160,82 Q178,92 182,117'
    o += f'<path d="{path}" fill="none" stroke="{RD if kind == "round" else NV}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    if kind == 'round':
        o += f'<path d="M24,96 Q70,88 110,92" fill="none" stroke="{NV}" stroke-width="4" stroke-linecap="round"/>' + f'<circle cx="184" cy="117" r="5" fill="{RD}"/>'
    return o + '</svg>'
def hand_top():
    o = '<svg viewBox="0 0 300 170" style="width:100%;max-width:280px;height:auto;display:block;margin:0 auto">'
    o += f'<path d="M40,150 Q30,96 70,70 Q150,30 230,70 Q270,96 260,150" fill="#fff7f3" stroke="{RD}" stroke-width="3" stroke-dasharray="7 5"/>'
    o += lab(150, 112, 'a soft ball', 'middle', RD, 15) + lab(150, 130, 'under your palm', 'middle', RD, 13, 400)
    for i, x in enumerate((48, 92, 150, 208, 252)):
        o += f'<circle cx="{x}" cy="{150 if i in (0, 4) else 156}" r="9" fill="{NV}"/>'
    return o + '</svg>'
WARM = [('ragdoll', 'Rag doll', 'Flop forward, arms hanging heavy. Shake them loose. Float the hands up onto the keys.'),
        ('wings', 'Elbow wings', 'Elbows free, not stuck to your body. Float them out like wings, then back.'),
        ('glide', 'Arm glide', 'Skate the whole arm along the keys. The round hand rides to the next group of keys.'),
        ('dive', 'Arm drop', 'Lift the whole arm and let it drop into a key on finger 3: firm tip, soft wrist, a round sound.'),
        ('bridge', 'Knuckle bridge', 'Your knuckles are a bridge a little car can drive over. Press one key slowly and hold for 3.'),
        ('balloon', 'Wrist balloon', 'As the key goes down, a balloon lifts the wrist back up to level. The fingertip stays on the key.')]
B1 = bpage(f'''{head('Before you play', 'Posture and hand shape', 'How you sit and how you hold your hands decide how easy everything else will be. Set them up before the first note, check them every time you sit down, and they soon look after themselves.')}
{hero(hero_sit(), 'Tall back, level arms, flat feet')}
{h3('A round hand')}
{two(app('2:The good shape', 300, 'g') + '<p class="sm" style="text-align:center">knuckles up like a bridge, the wrist level, the sound from the <b>fingertip</b></p>', hand_top() + '<p class="sm" style="text-align:center">the shape a hand makes resting on a ball</p>')}
{tbl(['Part of the hand', 'What it does'], [['<b>fingertips</b>', 'play the keys, just behind the nail (keep nails short)'], ['<b>knuckles</b>', 'stay up, like a bridge: they never sink in'], ['<b>thumb</b>', 'plays on the side of its tip, relaxed, not stretched out'], ['<b>wrist</b>', 'level with the hand, loose, never resting on the wood']], ['30%', '70%'])}
<!--SPLIT-->
{h3('Finger numbers')}
{two(hand_pic(), '<p>Every finger has a number, <b>the same in both hands</b>: the thumb is <b>1</b>, then 2, 3, 4, and the little finger is <b>5</b>. Music often prints these numbers above or below the notes.</p><p class="sm">More on choosing fingers: Fingering p. {{L1}}.</p>', '1.25fr 1fr')}
{inact('Which hand is round?', '<div class="gm4" style="grid-template-columns:repeat(3,1fr)">' + ''.join(f'<div>{app(k, 200, "e" + n)}<b>{n}</b></div>' for n, k in (('A', '2:flat fingers'), ('B', '2:knuckles collapsed'), ('C', '2:The good shape'))) + '</div>', ['<b>Look at the knuckles:</b> up, or sunk in?', '<b>Look at the tips:</b> does the finger stand on its tip?', '<b>Which hand</b> could play all day?'], '<b>C</b>: knuckles up, curved fingers, standing on the tips. A is flat; B’s knuckle has caved in.')}
{inact('Is the stool right?', '<div class="gm4" style="grid-template-columns:repeat(3,1fr)">' + ''.join(f'<div>{app(k, 230, "s" + n)}<b>{n}</b></div>' for n, k in (('A', '1:stool too low'), ('B', '1:Just right'), ('C', '1:stool too high'))) + '</div>', ['<b>Follow the forearm</b> from the elbow to the keys.', '<b>Uphill or downhill?</b> Then the stool is too low or too high.', '<b>Which one</b> is level?'], '<b>B</b>: the forearm is level. In A the stool is too low (raise it, or add a cushion); in C it is too high.')}
<!--SPLIT-->
{h3('Six warm-ups')}
<div class="wu6">{''.join(f'<div>{warmpic(k, 150, "w" + k)}<b>{i + 1} · {a}</b><span>{b}</span></div>' for i, (k, a, b) in enumerate(WARM))}</div>
{howto('The 30-second check, every time you sit down', ['<b>Stool:</b> forearms level with the keys, opposite Middle C.', '<b>Body:</b> front half of the stool, feet flat, back tall.', '<b>Shoulders:</b> lift them, then let them drop.', '<b>Hands:</b> a soft ball under each palm, knuckles up.', '<b>Breathe out</b>, then play.'])}
{try10(app('2:The good shape', 200, 't'), 'The ball test.', 'Hold a small ball or an orange, then put the hand on the keys without changing its shape. That is your playing hand.')}
{thinkt('A good posture is like a well-tuned bicycle: you stop noticing it, and every ride gets easier.')}
{watch(['Wrists that sink below the keys, or rest on the wood: keep them level and loose.', 'Shoulders creeping up to the ears: let them drop between pieces.', 'Flat fingers, or a knuckle that caves in: stand on the fingertips.', 'Sitting too close, elbows squashed against your body: move the stool back a little.'])}
{foot('Fingering p. {{L1}} · Practising well p. {{L2}}', 'Workbook pp. 1–2 · Online: Posture & Hand Shape')}''', 18)

# her 12 Nov (C): one page that shows how a chapter works, before the first chapter (p. 17; nothing after it moves)
_PATH = ['The secret', 'Picture', 'Learn it', 'Example', 'Try it, Game', 'Trap', 'See also']
_G = [secret_box('The whole chapter in one sentence. It sits at the top of every chapter, beside the opening words. Read it first, and again at the end.'),
      inact('A question worked through', '<span></span>', ['Read the question.', 'Follow the numbered steps.', 'Check the answer underneath.'], 'The answer, and why.'),
      youknow('A tune you already know', '', 'The new idea is marked in <b class="co">red</b>, so you can hear it in real music.', wide=True),
      game('A puzzle', '', 'Play it on your own or with a friend.', 'printed upside down, so you can check yourself'),
      try10('', 'Try it at the piano.', 'Ten seconds, one small thing to feel in your hands.'),
      thinkt('A picture to keep in your head, so the idea is easy to remember.'),
      watch(['The mistake most people make, and how to avoid it.']),
      extra('Beyond your level', '<p class="sm">Skip it for now if you like; it will still be here later.</p>')]
GUIDE = f"""<section class="pg" data-flow="AGD"><div class="top"><span>THE PIANO BUTLER HANDBOOK</span><span>BEFORE YOU PLAY</span></div><div class="rule"></div><div class="body">
<div class="kick">Before you play</div><h1>How to read this book</h1><p class="lead">Every chapter walks the same path: one big idea, a picture of it, then ways to see it, play it and check it. Each box has its own job, so once you know the boxes you can find your way around any page.</p>
<div class="gpath">{''.join(f'<div><span>{i + 1}</span>{t}</div>' for i, t in enumerate(_PATH))}</div>
<p class="sm" style="margin:-6px 0 10px">The picture and the main lesson come next; these are the boxes around them. Some pages also have <b>You know this</b>, <b>Think of it</b>, <b>Extra</b>, <b>How to</b>, <b>The rule</b> or a <b>Tip</b>.</p><div class="g2x">{''.join(f'<div>{x}</div>' for x in _G)}</div>
{foot('Other pages on the same idea, with their page numbers', 'Matching Workbook pages, and drills in the app')}
<p class="sm" style="margin-top:10px">Use the book in any order: start with the chapter your piece needs. Every chapter can also be heard in the app, in <b>Read &amp; listen</b>.</p>
</div><div class="foot"><span>17</span></div></section>"""
html = GUIDE + assemble('B1', B1)
open('/mnt/user-data/outputs/house-rooms/handbook-before.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{OPENCSS} .sitl{{display:flex;flex-direction:column;gap:9px;text-align:left}} .sitl>div{{display:grid;grid-template-columns:24px 1fr;column-gap:8px;font-size:14.5px;line-height:1.3}} .sitl .rn{{grid-row:span 2;width:22px;height:22px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;font-size:13px;display:flex;align-items:center;justify-content:center}} .sitl b{{color:#26296b}} .sitl span:not(.rn){{color:#5a5d8f;font-size:13.5px}} .wu6{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px 14px;margin:6px 0 10px}} .wu6>div{{display:flex;flex-direction:column;gap:3px;font-size:13.5px;line-height:1.35;color:#5a5d8f}} .wu6 b{{color:#26296b;font-size:14.5px}} .wu6 svg{{height:96px!important;width:auto!important;max-width:100%}} .gpath{{display:flex;flex-wrap:nowrap;justify-content:space-between;gap:4px;margin:10px 0 14px}} .gpath>div{{display:flex;align-items:center;gap:5px;font-size:12.5px;color:#26296b;background:#f3f2f8;border-radius:16px;padding:3px 9px 3px 4px}} .gpath span{{width:20px;height:20px;border-radius:50%;background:#26296b;color:#fff;font-size:11.5px;font-weight:700;display:flex;align-items:center;justify-content:center}} .g2x{{display:grid;grid-template-columns:1fr 1fr;gap:12px 14px;align-items:stretch}} .g2x>div{{display:flex}} .g2x>div>*{{margin:0!important;flex:1}} .g2x .t10{{grid-template-columns:1fr}}</style></head><body>{html}{FLOWJS}</body></html>')
print('ok before')
