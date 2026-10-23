import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build E (her order 2026-10-24: after the Pitch gaps, Rhythm). Rhythm groups 1 and 2 on the Home: the steady beat, how long notes last.
# The lesson files kq, iv, ch, pg are re-spliced as in 663; rq.jsx (the rhythm lessons) follows pg.jsx.
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + open(SC + 'iv.jsx', encoding='utf-8').read() + "\n" + open(SC + 'ch.jsx', encoding='utf-8').read() + "\n" + open(SC + 'pg.jsx', encoding='utf-8').read() + "\n" + open(SC + 'rq.jsx', encoding='utf-8').read() + s[j:]

# ── the Home: Beat and time becomes a live concept (two groups so far)
rep("  'p-modes': {\n", """  'r-beat': { lessons: [], groups: [
    { id: 'rb-pulse', en: 'The steady beat', ko: '꾸준한 박', lessons: ['rb-beat', 'rb-count', 'rb-silent', 'rb-words'], check: 'pulse' },
    { id: 'rb-values', en: 'How long notes last', ko: '음표와 쉼표의 길이', lessons: ['rn-q', 'rn-h', 'rn-long', 'rn-p', 'rn-rest'], check: 'note-values' },
  ] },
  'p-modes': {
""")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
