import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:80])
    s = s.replace(old, new)
# the Chords lessons (sc/ch.jsx), after the Intervals ones
i = s.index("\nconst scDirTag = ")
s = s[:i] + "\n" + open('/home/claude/pbtest/sc/ch.jsx', encoding='utf-8').read() + s[i:]
# Home: Chords in three groups, each with its Questions button at its own level of the chords drill
rep("  'p-intervals': { lessons: [], groups: [\n", """  'p-chords': { lessons: [], groups: [
    { id: 'ch-build', en: 'Building a triad', ko: '3화음 쌓기', lessons: ['ch-stack', 'ch-staff', 'ch-hands'], check: 'chords', level: 1 },
    { id: 'ch-majmin', en: 'Major and minor', ko: '장3화음과 단3화음', lessons: ['ch-mm', 'ch-ear'], check: 'chords', level: 3 },
    { id: 'ch-key', en: 'Chords in a key', ko: '조 안의 화음', lessons: ['ch-tonic', 'ch-145', 'ch-inv'], check: 'chords', level: 7 },
  ] },
  'p-intervals': { lessons: [], groups: [
""")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
