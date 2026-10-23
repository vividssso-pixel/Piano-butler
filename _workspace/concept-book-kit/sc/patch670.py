import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build J (her calls 2026-10-24): Scales and Key signatures in the Lesson Book's feel, the butler at the bottom; a Home lesson's
# tag says LESSON (레슨), and a tool inside a lesson carries no second tag.
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + "\n".join(open(SC + f, encoding='utf-8').read() for f in ['iv.jsx', 'ch.jsx', 'pg.jsx', 'rq.jsx', 'rq2.jsx', 'rq3.jsx', 'tq.jsx', 'lbh.jsx']) + s[j:]   # lbh.jsx last: it swaps the Scales and Key finder lessons' components, registered above

rep("""    lessons: ['kf-what', 'kf-sharps', 'kf-flats', 'kf-msharp', 'kf-mflat', 'kf-minor', 'kf-piece', 'kf-write', 'kf-trans'], check: 'key-signatures', tools: [], more: [],""",
    """    lessons: ['kf-what', 'kf-gf', 'kf-acc', 'kf-dbb', 'kf-sharps', 'kf-flats', 'kf-msharp', 'kf-mflat', 'kf-minor', 'kf-piece', 'kf-write', 'kf-trans'], check: 'key-signatures', tools: [], more: [],""")
rep("""    lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-both', 'sc-all', 'sc-chrom', 'sc-min', 'sc-penta'], check: 'scales', tools: ['scale-finder'], more: [],""",
    """    lessons: ['sc-shape', 'sc-wr', 'sc-wl', 'sc-deg', 'sc-same', 'sc-br', 'sc-bl', 'sc-both', 'sc-all', 'sc-chrom', 'sc-min', 'sc-penta'], check: 'scales', tools: ['scale-finder'], more: [],""")
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
