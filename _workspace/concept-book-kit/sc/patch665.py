import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build F: Rhythm groups 3 and 4 on the Home: bars and time signatures, rhythm patterns (rq2.jsx, after rq.jsx).
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + open(SC + 'iv.jsx', encoding='utf-8').read() + "\n" + open(SC + 'ch.jsx', encoding='utf-8').read() + "\n" + open(SC + 'pg.jsx', encoding='utf-8').read() + "\n" + open(SC + 'rq.jsx', encoding='utf-8').read() + "\n" + open(SC + 'rq2.jsx', encoding='utf-8').read() + s[j:]
rep("""    { id: 'rb-values', en: 'How long notes last', ko: '음표와 쉼표의 길이', lessons: ['rn-q', 'rn-h', 'rn-long', 'rn-p', 'rn-rest'], check: 'note-values' },
""", """    { id: 'rb-values', en: 'How long notes last', ko: '음표와 쉼표의 길이', lessons: ['rn-q', 'rn-h', 'rn-long', 'rn-p', 'rn-rest'], check: 'note-values' },
    { id: 'rb-bars', en: 'Bars and time signatures', ko: '마디와 박자표', lessons: ['rt-bars', 'rt-ts', 'rt-strong', 'rt-fill', 'rt-tie'], check: 'time-signatures' },
    { id: 'rb-patterns', en: 'Rhythm patterns', ko: '리듬 패턴', lessons: ['rp-beams', 'rp-alone', 'rp-dot', 'rp-up', 'rp-read'], check: 'rhythm' },
""")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
