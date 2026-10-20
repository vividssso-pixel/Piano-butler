import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# shared toggle: keyboard first, the staff only when she asks for it
rep("\nconst SC_D0 =", """
function ScStaffBtn({ on, set }) {
  return <div style={{display:'flex',justifyContent:'center',margin:'6px 0 2px'}}><button className="ghost-btn" style={{...scS.back,minHeight:40,padding:'0 16px',fontSize:13}} aria-pressed={on} onClick={() => set(!on)}>{on ? t('Hide the staff', '오선 숨기기') : t('Write it on the staff', '오선에 써 보기')}</button></div>;
}
const SC_D0 =""")
# ---- ScMinor
a = s.index("function ScMinor() {"); b = s.index("// lesson 5: the natural.", a) if "// lesson 5: the natural." in s[a:] else None
# the ScMinor function ends at the next top-level "\\n}\\n" after 'return scBox(\\'minor3\\', body);'
e = s.index("return scBox('minor3', body);", a)
seg = s[a:e]
def r(x, y, n=1):
    global seg
    assert seg.count(x) == n, (x[:80], seg.count(x)); seg = seg.replace(x, y)
r("const [view, setView] = useState('all');", "const [view, setView] = useState('all'), [stf, setStf] = useState(false);")
r("  const TXT = {", """  const TXK = {
    natural: ['Natural minor: nothing is raised. T S T T S T T.', '자연 단음계: 올리는 음이 없어요. T S T T S T T.'],
    harmonic: ['Harmonic minor, the one you’ll play most: raise the 7th note a semitone, going up and coming down. C becomes C♯.', '화성 단음계, 가장 많이 치게 될 단음계: 7번째 음을 반음 올려요, 올라갈 때도 내려올 때도. C가 C♯이 돼요.'],
    melodic: ['Melodic minor: going up, raise the 6th and 7th (B♮ and C♯). Coming down, play the natural minor.', '가락 단음계: 올라갈 때는 6음과 7음(B♮과 C♯)을 올려요. 내려올 때는 자연 단음계를 쳐요.']
  };
  const TXT = {""")
i0 = seg.index("  } else if (view === 'one') {"); i1 = seg.index("  } else {\n    const M = mk(fm)", i0)
old = seg[i0:i1]
# keyboard-first version
new = old
new = new.replace("const f = SC_MF[i], M = mk(f), Dn = f === 'melodic' ? mk('natural') : M, Q = M.K.concat(Dn.K.slice(0, 7).reverse()), QS = Q.slice(1).map((k, j) => Math.abs(k - Q[j])), an = P.an;",
  "const f = SC_MF[i], M = mk(f), Dn = f === 'melodic' ? mk('natural') : M, Q = M.K.concat(Dn.K.slice(0, 7).reverse()), N2 = M.N.concat(Dn.N.slice(0, 7).reverse()), QS = Q.slice(1).map((k, j) => Math.abs(k - Q[j])), an = P.an, A = an >= 0 ? scAnim(Q, N2, QS, an, 7, M.marks) : null;")
assert new != old
new = new.replace("<div style={scS.line}>{t(TXT[f][0], TXT[f][1])}</div>\n      {scDirTag(false)}\n      {stf(upI, cUp, aUp, onlyUp, an >= 0 && an <= 7 ? an : null, 'u' + f + an)}\n      {scDirTag(true)}\n      {stf(dnI, cDn, aDn, onlyDn, an >= 7 ? an - 7 : null, 'd' + f + an)}\n",
  "<div style={scS.line}>{stf ? t(TXT[f][0], TXT[f][1]) : t(TXK[f][0], TXK[f][1])}</div>\n      {A && scDirTag(A.dn)}\n      <ScKeys ks={M.K} marks={A ? A.marks : M.marks} names={A ? A.names : M.names} arcs={A ? A.arcs : M.ST.map((_, j) => mvK(M.K, M.ST, j, false))} nonce={nonce + ':' + i + (A ? 'a' + P.an : '')}/>\n")
assert 'TXK[f]' in new
# staves after the pills, behind the toggle
pill = "      {an >= 0 ? <ScPillRow st={QS} upTo={an} cur={an - 1}/> : <ScPillRow st={M.ST} upTo={7}/>}\n"
assert new.count(pill) == 1
legend_start = new.index("      <div style={{display:'flex',justifyContent:'center'")
new = new[:legend_start] + pill + "      <ScStaffBtn on={stf} set={setStf}/>\n      {stf && <>\n        {scDirTag(false)}\n        {stf0(upI, cUp, aUp, onlyUp, an >= 0 && an <= 7 ? an : null, 'u' + f + an)}\n        {scDirTag(true)}\n        {stf0(dnI, cDn, aDn, onlyDn, an >= 7 ? an - 7 : null, 'd' + f + an)}\n" + new[legend_start:new.index(pill)] + "      </>}\n" + new[new.index(pill)+len(pill):]
new = new.replace("const stf = (items, coral, alt, only, ring, key)", "const stf0 = (items, coral, alt, only, ring, key)")
seg = seg[:i0] + new + seg[i1:]
s = s[:a] + seg + s[e:]
# ---- ScAll
a = s.index("function ScAll() {"); b = s.index("\nfunction ", a + 10)
seg = s[a:b]
x = "const [view, setView] = useState('all');"
assert seg.count(x) == 1; seg = seg.replace(x, "const [view, setView] = useState('all'), [stf, setStf] = useState(false);")
x = "      <ScStaffScale k={kk} ring={A ? (P.an <= 7 ? P.an : 14 - P.an) : null}/>\n"
assert seg.count(x) == 1; seg = seg.replace(x, "      <ScStaffBtn on={stf} set={setStf}/>\n      {stf && <ScStaffScale k={kk} ring={A ? (P.an <= 7 ? P.an : 14 - P.an) : null}/>}\n")
s = s[:a] + seg + s[b:]
# ---- ScSame
a = s.index("function ScSame() {"); b = s.index("function ScDeg()", a)
seg = s[a:b]
x = "const [view, setView] = useState('all');"
assert seg.count(x) == 1; seg = seg.replace(x, "const [view, setView] = useState('all'), [stf, setStf] = useState(false);")
x = "      {E.n === 8 && <ScStaffScale k={E.key}/>}\n"
assert seg.count(x) == 1; seg = seg.replace(x, "      {E.n === 8 && <ScStaffBtn on={stf} set={setStf}/>}\n      {E.n === 8 && stf && <ScStaffScale k={E.key}/>}\n")
s = s[:a] + seg + s[b:]
open(sys.argv[2],'w',encoding='utf-8').write(s)
