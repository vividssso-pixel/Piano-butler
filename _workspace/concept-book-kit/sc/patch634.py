import sys, re
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
i = s.index("// ─── Keys and staff, built again from the start in the Scales style")
j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open('/home/claude/pbtest/sc/kq.jsx', encoding='utf-8').read() + s[j:]
m = re.search(r"(\{ id: 'p-keys', en: '[^']*', ko: '[^']*', lessons: )\[[^\]]*\]", s)
assert m
s = s[:m.start()] + m.group(1) + "['kq-black', 'kq-houses', 'kq-names']" + s[m.end():]
for gid, ls in [('p-stf', "['kq-lines', 'kq-climb', 'kq-clefs']"), ('p-lines', "['kq-letters', 'kq-landmarks', 'kq-read']"), ('p-ledger', "['kq-ledger', 'kq-middlec', 'kq-8va']"), ('p-range', "['kq-octave', 'kq-size', 'kq-range']")]:
    m2 = re.search(r"(\{ id: '" + gid + r"', en: '[^']*', ko: '[^']*', lessons: )\[[^\]]*\]", s)
    assert m2, gid
    s = s[:m2.start()] + m2.group(1) + ls + s[m2.end():]
s = s.replace("en: 'Line and space names', ko: '줄과 칸의 이름'", "en: 'Notes on the staff', ko: '오선 위의 음 이름'")
# ScKeys: 'plain' keeps the letters above the keys but leaves out the black-key names and the letters on the white keys (the first lessons)
x = "function ScKeys({ marks, onTap, arcs, nonce, names, ks, ncol, nums, ring, mw, oct, clean, inKey }) {"
assert s.count(x) == 1
s = s.replace(x, "function ScKeys({ marks, onTap, arcs, nonce, names, ks, ncol, nums, ring, mw, oct, clean, inKey, plain }) {")
y = "labels={arcs.length ? 'white' : 'all'}"
assert s.count(y) == 1
s = s.replace(y, "labels={plain ? null : arcs.length ? 'white' : 'all'}")
open(bb, 'w', encoding='utf-8').write(s)
