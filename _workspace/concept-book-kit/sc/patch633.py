import sys, re
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
# 1. out with the first-pass and the fitted-in blocks, in with the new Keys and staff
i = s.index("// ─── Keys and staff on Home (her call 2026-10-21: \"1, 2, 3, in order\")")
j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open('/home/claude/pbtest/sc/kq.jsx', encoding='utf-8').read() + s[j:]
# 2. the strong blue key (the big house), same family as the strong coral one
rep("  pick:   { white: '#e4572e', black: '#e4572e', stroke: '#c0431f', sw: 1.5, text: '#fff' },", "  pick:   { white: '#e4572e', black: '#e4572e', stroke: '#c0431f', sw: 1.5, text: '#fff' },\n  pickB:  { white: '#3b4fa8', black: '#3b4fa8', stroke: '#26296b', sw: 1.5, text: '#fff' },")
# 3. Home: the lessons of the five sections
def lessons(gid, ids):
    global s
    m = re.search(r"(\{ id: '" + gid + r"', en: '[^']*', ko: '[^']*', lessons: )\[[^\]]*\]", s)
    assert m, gid
    s = s[:m.start()] + m.group(1) + "[" + ", ".join("'" + x + "'" for x in ids) + "]" + s[m.end():]
lessons('p-keys', ['kq-groups', 'kq-hear', 'kq-small', 'kq-big', 'kq-find', 'kq-middle', 'kq-repeat'])
lessons('p-stf', ['kq-lines', 'kq-treble', 'kq-bass', 'kq-grand', 'kq-climb'])
lessons('p-lines', ['kq-ntreble', 'kq-nbass', 'kq-landmarks', 'kq-count', 'kq-read'])
lessons('p-ledger', ['kq-above', 'kq-below', 'kq-middlec', 'kq-8va'])
lessons('p-range', ['kq-size', 'kq-range'])
open(bb, 'w', encoding='utf-8').write(s)
