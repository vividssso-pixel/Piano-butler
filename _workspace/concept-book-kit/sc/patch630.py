import sys, re
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
i = s.index("\nconst KS_ROWS = [")
j = s.index("\nKS_ROWS.forEach(")
new = open('/home/claude/pbtest/sc/ks3.jsx', encoding='utf-8').read()
s = s[:i] + new + s[j:]
# the sections' lessons on Home
def lessons(gid, ids):
    global s
    m = re.search(r"(\{ id: '" + gid + r"', en: '[^']*', ko: '[^']*', lessons: )\[[^\]]*\]", s)
    assert m, gid
    s = s[:m.start()] + m.group(1) + "[" + ", ".join("'" + x + "'" for x in ids) + "]" + s[m.end():]
lessons('p-keys', ['kp-groups', 'kp-repeat', 'kp-middle', 'kp-hear'])
lessons('p-names', ['nn-letters', 'nn-houses', 'nn-updown', 'nn-find'])
lessons('p-stf', ['sf-lines', 'sf-treble', 'sf-bass', 'sf-grand', 'sf-climb'])
lessons('p-lines', ['ws-treble', 'ws-bass', 'ws-landmarks', 'ws-count', 'ws-read'])
lessons('p-ledger', ['ll-above', 'll-below', 'll-middle', 'll-8va'])
lessons('p-range', ['sr-size', 'sr-range'])
open(bb, 'w', encoding='utf-8').write(s)
