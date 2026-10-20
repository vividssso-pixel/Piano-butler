import sys,re
s=open(sys.argv[1],encoding='utf-8').read()
def fn(name, nxt):
    global s
    a = s.index("function %s(" % name); b = s.index(nxt, a + 10)
    seg = s[a:b]
    def r(x, y, n=1):
        nonlocal seg
        assert seg.count(x) == n, (name, x[:70], seg.count(x)); seg = seg.replace(x, y)
    r("const [view, setView] = useState('all')", "const [go, setGo] = useState(false);\n  const [view, setView] = useState('all')")
    r("useEffect(() => clear, []);", "useEffect(() => clear, []);\n  useEffect(() => { if (at < 7 && go) setGo(false); }, [at, go]);")
    r("const ps = at >= 7 ? 7 : 0;", "const pat = at === 7 && !go, ps = at >= 7 && !pat ? 7 : 0;")
    r("j === at && !done ? 'pick'", "j === at && !done && !pat ? 'pick'")
    r("const line = done ? ", "const line = pat ? t('That is the way up: look at the pattern. Then we come back down.', '올라가는 길이에요. 패턴을 보세요. 그다음 내려와요.') : done ? ")
    r("const tap = (k) => { if (done) return;", "const tap = (k) => { if (done || pat) return;")
    r("{!done && scDirTag(at >= 7)}", "{!done && scDirTag(at >= 7 && !pat)}")
    if name != 'ScMinor': r("const dn = at >= 7, word", "const dn = at >= 7 && !pat, word")
    else: r("const dn = at >= 7, cnt", "const dn = at >= 7 && go, cnt")
    st = 'prim' if name == 'ScSame' else 'scS.prim'
    r("{done && <button className=\"ghost-btn\" style={%s}" % st, "{pat && <button className=\"ghost-btn\" style={%s} onClick={() => { setGo(true); setNonce(n => n + 1); }}>{t('Come down →', '내려가기 →')}</button>}\n        {done && <button className=\"ghost-btn\" style={%s}" % (st, st))
    s = s[:a] + seg + s[b:]
fn('ScSame', 'function ScDeg(')
fn('ScAll', '\nfunction ')
fn('ScMinor', '// ─── Phase 585')
open(sys.argv[2],'w',encoding='utf-8').write(s)
