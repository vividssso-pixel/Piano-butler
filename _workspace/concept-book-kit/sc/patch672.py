import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build K (her calls 2026-10-24, on t669): Scales and Key signatures keep their lessons and order; they take on the Lesson Book's
# look only: keyboards in the book's picture frame, the butler's Remember line under each lesson (the major scale's says
# T T S T T T S, like its keys). A Home lesson's tag says LESSON (레슨); a tool inside a lesson carries no second tag.
# (Build J, patch670, which put book pages into Scales and Key signatures, is withdrawn: she asked for the design, not the structure.)
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + "\n".join(open(SC + f, encoding='utf-8').read() for f in ['iv.jsx', 'ch.jsx', 'pg.jsx', 'rq.jsx', 'rq2.jsx', 'rq3.jsx', 'tq.jsx', 'lbh.jsx']) + s[j:]   # lbh.jsx last: it wraps lessons registered above

# the book's picture frame (lbh.jsx frames the pictures of the Scales and Key signature lessons; two in a row share one frame)
rep("""    .try-box { position: relative; }""", """    .try-box { position: relative; }
    .lbh-fig { background: #fff; border: 0.8px solid rgba(38,41,107,0.55); padding: 12px 10px 8px; margin: 4px 0 8px; }
    .lbh-fig + .lbh-fig { border-top: 0; margin-top: -8px; padding-top: 4px; }""")
# the tag: LESSON on a Home lesson, none on a tool inside it
rep("""    .try-box::before { content: 'TRY IT'; position: absolute; top: -8px; right: 10px; background: var(--coral); color: #fff; font-size: 9px; font-weight: 800; letter-spacing: 0.1em; padding: 2px 8px; border-radius: 8px; }""",
    """    .try-box::before { content: 'TRY IT'; position: absolute; top: -8px; right: 10px; background: var(--coral); color: #fff; font-size: 9px; font-weight: 800; letter-spacing: 0.1em; padding: 2px 8px; border-radius: 8px; }
    [data-home-lesson] .try-box::before { display: none; }
    [data-home-lesson] > .try-box::before { display: block; content: 'LESSON'; }
    html[lang=ko] [data-home-lesson] > .try-box::before { content: '레슨'; letter-spacing: 0.04em; }""")
rep("""      <div className="card">
        <div style={{fontSize:12,fontWeight:800,color:(TOOL_CATS.find(c => c.id === toolMeta(t.id).cat) || {}).color || 'var(--muted)',textTransform:'uppercase',letterSpacing:'0.06em',marginBottom:12}}>{t.kicker""",
    """      <div className="card" data-home-lesson={t.ch === 'concept' ? '1' : undefined}>
        <div style={{fontSize:12,fontWeight:800,color:(TOOL_CATS.find(c => c.id === toolMeta(t.id).cat) || {}).color || 'var(--muted)',textTransform:'uppercase',letterSpacing:'0.06em',marginBottom:12}}>{t.kicker""")
# Korean: 샵 ends in a consonant (샵은, 샵을, 샵으로, 샵이, 샵과, 샵이에요)
for a, b in [('샵는', '샵은'), ('샵를', '샵을'), ('샵로', '샵으로'), ('샵가', '샵이'), ('샵와', '샵과'), ('샵예요', '샵이에요')]:
    s = s.replace(a, b)
open(dst, 'w', encoding='utf-8').write(s); print('ok')
