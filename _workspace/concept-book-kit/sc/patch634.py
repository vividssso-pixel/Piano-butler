import sys, re
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
i = s.index("// ─── Keys and staff, built again from the start in the Scales style")
j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open('/home/claude/pbtest/sc/kq.jsx', encoding='utf-8').read() + s[j:]
m = re.search(r"(\{ id: 'p-keys', en: '[^']*', ko: '[^']*', lessons: )\[[^\]]*\]", s)
assert m
s = s[:m.start()] + m.group(1) + "['kq-black', 'kq-houses', 'kq-names']" + s[m.end():]
open(bb, 'w', encoding='utf-8').write(s)
