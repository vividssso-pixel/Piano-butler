import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
def rep_all(old, new, atleast=1):
    global s
    c = s.count(old); assert c >= atleast, (c, old[:90]); s = s.replace(old, new); return c

# Build CB (her 09:38): (1) the aural rooms are called Ear Training (청음), not Hear and Sing; (2) the rooms whose thing to make
# came before the mk- toys show it on the room's MAKE YOUR OWN card too: Patterns (Black-key jam), Rhythm (Make a rhythm card),
# Key signatures (Transpose a tune, with its 'my tune'), Form (Build your own form), Melody (Draw a tune). Time signatures'
# 'Build a bar' is already a step of that room, so it stays a step.

# ── 1. Ear Training ──
rep_all('Hear and Sing, Grade ', 'Ear Training, Grade ', 10)
rep_all('Hear and sing, Grade ', 'Ear training, Grade ', 5)
rep_all('Hear and Sing Further', 'Ear Training, Grades 2–3', 4)
rep_all('Hear and sing further', 'Ear training, Grades 2–3', 2)
rep("""'listen-23': ['Hear & sing', '듣고 부르기']""", """'listen-23': ['Aural 2–3', '청음 2–3']""")
for g in '45678':
    rep("""'listen-%s': ['Hear & sing %s', '듣기 %s']""" % (g, g, g), """'listen-%s': ['Aural %s', '청음 %s']""" % (g, g, g))
rep_all('듣고 부르기, Grade ', '청음, Grade ', 15)
rep_all('더 듣고 부르기', '청음, Grade 2–3', 4)
for k in ['listen-23', 'listen-4', 'listen-5', 'listen-6', 'listen-7', 'listen-8']:
    rep("""'%s': 'aural ear """ % k, """'%s': 'ear training aural ear """ % k)

# ── 2. the older things to make on the room's card ──
rep("""function LessonMake({ id }) {   // Build CA: the room's own thing to make, at the end of the room
  const toys = TOOLS.filter(tl => tl.ch === id && /^mk-/.test(tl.id) && !tl.hidden);""",
"""const MAKE_EXTRA = { 'first-steps': ['black-key-jam'], rhythm: ['make-card'], 'key-signatures': ['transpose'], form: ['form-builder'], melody: ['draw-tune'] };   // Build CB: made before the mk- toys
function LessonMake({ id }) {   // Build CA: the room's own thing to make, at the end of the room
  const toys = TOOLS.filter(tl => tl.ch === id && /^mk-/.test(tl.id) && !tl.hidden).concat((MAKE_EXTRA[id] || []).map(x => TOOLS.find(tl => tl.id === x)).filter(Boolean));""")
rep("""!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|chx|tmx|fmx|mlx|cpx|csx|sac|ts|nv|mk)-/.test(x) && !own.includes(x))""",
    """!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|chx|tmx|fmx|mlx|cpx|csx|sac|ts|nv|mk)-/.test(x) && !own.includes(x) && !(MAKE_EXTRA[id] || []).includes(x))""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
