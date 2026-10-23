import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build I (her call 2026-10-24): Rhythm and Posture on the Home follow the Lesson Book page by page (lbh.jsx takes the book's
# pages apart: title, words, picture, Remember, At the piano, Not like this); the fold at Clara's ladder joins Notes on the staff.
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + "\n".join(open(SC + f, encoding='utf-8').read() for f in ['iv.jsx', 'ch.jsx', 'pg.jsx', 'rq.jsx', 'rq2.jsx', 'rq3.jsx', 'tq.jsx', 'lbh.jsx']) + s[j:]

rep("""    { id: 'p-lines', en: 'Notes on the staff', ko: '오선 위의 음 이름', lessons: ['kq-letters', 'kq-landmarks', 'kq-read', 'kq-write'], check: 'whole-staff' },""",
    """    { id: 'p-lines', en: 'Notes on the staff', ko: '오선 위의 음 이름', lessons: ['kq-letters', 'kq-fold', 'kq-landmarks', 'kq-read', 'kq-write'], check: 'whole-staff' },""")
rep("""  'k-posture': { lessons: ['kp-sit', 'kp-arm', 'kp-hand', 'kp-check'], check: 'posture-hands' },""",
    """  'k-posture': { lessons: ['kp-sit', 'kp-arm', 'kp-hand', 'kp-fingers', 'kp-walks', 'kp-check'], check: 'posture-hands' },""")
rep("""    { id: 'rb-pulse', en: 'The steady beat', ko: '꾸준한 박', lessons: ['rb-beat', 'rb-count', 'rb-silent', 'rb-words'], check: 'pulse' },""",
    """    { id: 'rb-pulse', en: 'The steady beat', ko: '꾸준한 박', lessons: ['rb-beat', 'rb-count', 'rb-silent', 'rb-words', 'rb-finger'], check: 'pulse' },""")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
