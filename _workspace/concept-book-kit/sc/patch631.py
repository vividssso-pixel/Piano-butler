import sys
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
rep("const [openG, setOpenG] = useState('p-keys');", "const [openG, setOpenG0] = useState(() => (window.__ksOpen === undefined ? 'p-keys' : window.__ksOpen));\n  const setOpenG = (v) => { window.__ksOpen = v; setOpenG0(v); };")
open(bb, 'w', encoding='utf-8').write(s)
