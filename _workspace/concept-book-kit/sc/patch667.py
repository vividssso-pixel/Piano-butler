import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build H: Technique on the Home. Posture and hands (sit, the arm, a round hand, the five checks), Finger numbers and
# positions (finger numbers, C and G positions, five-finger positions in every key), and Playing scales and chords,
# which links to the scale-fingering lessons where they stay (Pitch > Scales) and to 'Chords with your hands'.
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + "\n".join(open(SC + f, encoding='utf-8').read() for f in ['iv.jsx', 'ch.jsx', 'pg.jsx', 'rq.jsx', 'rq2.jsx', 'rq3.jsx', 'tq.jsx']) + s[j:]

# a concept's own Questions button can start at a level (Positions: 'Which finger?', level 3 of Posture & Hand Shape)
rep("{live.check && <button data-questions={live.check} onClick={() => go({ view: 'home', drill: live.check, tab: 'drill', level: 1, mode: 'lesson' })}",
    "{live.check && <button data-questions={live.check} onClick={() => go({ view: 'home', drill: live.check, tab: 'drill', level: live.level || 1, mode: 'lesson' })}")
rep("""  'r-beat': { lessons: [], groups: [""", """  'k-posture': { lessons: ['kp-sit', 'kp-arm', 'kp-hand', 'kp-check'], check: 'posture-hands' },
  'k-positions': { lessons: ['kp-fingers', 'kp-cpos', 'kp-gpos', 'kp-five'], check: 'posture-hands', level: 3 },
  'k-play': { lessons: ['sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-both', 'ch-hands'] },
  'r-beat': { lessons: [], groups: [""")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
