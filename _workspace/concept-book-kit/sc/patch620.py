import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
rep("const [an, setAn] = useState(-1), tmR = useRef([]);\n  const stopA = () => { tmR.current.forEach(clearTimeout); tmR.current = []; setAn(-1); };",
    "const [an, setAn] = useState(-1), [wt, setWt] = useState(false), tmR = useRef([]);\n  const stopA = () => { tmR.current.forEach(clearTimeout); tmR.current = []; setAn(-1); setWt(false); };")
old = s[s.index("  const playA = () => {"):s.index("  const thumbNow = ")]
new = """  // plays on until the next thumb, then waits for the button, so there is time to take it in
  const runFrom = (i0) => {
    tmR.current.forEach(clearTimeout); tmR.current = []; setWt(false); let at = 0;
    for (let i = i0; i < seq.length; i++) {
      const sq = seq[i];
      tmR.current.push(setTimeout(() => { setAn(i); playKey(sq.k, 0.5); if (thumbs(i)) setWt(true); }, at));
      if (thumbs(i)) return;
      at += 520;
    }
    tmR.current.push(setTimeout(() => setAn(-1), at + 300));
  };
  const playA = () => { if (an >= 0) { stopA(); return; } runFrom(0); };
"""
s = s.replace(old, new)
rep("<div data-sfd-thumb style={{ minHeight: 24, textAlign: 'center', fontWeight: 900, fontSize: 14, color: '#c0431f', marginTop: 6 }}>{thumbMsg}</div>",
    "<div data-sfd-thumb style={{ minHeight: 24, textAlign: 'center', fontWeight: 900, fontSize: 14, color: '#c0431f', marginTop: 6 }}>{thumbMsg}</div>\n            {wt && <div style={{ textAlign: 'center', marginTop: 4 }}><button className=\"ghost-btn\" style={scS.prim} data-sfd-next onClick={() => runFrom(an + 1)}>{t('Next →', '다음 →')}</button></div>}")
rep("t('▶ Up and down: stops at each thumb', '▶ 올라갔다 내려오기: 엄지에서 멈춰요')", "t('▶ Up and down: you press Next at each thumb', '▶ 올라갔다 내려오기: 엄지마다 \\'다음\\'을 눌러요')")
open(b, 'w', encoding='utf-8').write(s)
