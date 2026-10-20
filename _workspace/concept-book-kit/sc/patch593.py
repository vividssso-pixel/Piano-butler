import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
HELP = r"""
// ─── Phase 586 (her ask, 2026-10-20 13:40): the lessons play the scale up and then down, one key at a time, animated, so up and down are seen. Colours clear when the way down starts, and a direction tag says which way.
function useScPlay(deps) {
  const [an, setAn] = useState(-1); const tm = useRef([]);
  const stop = () => { tm.current.forEach(clearTimeout); tm.current = []; setAn(-1); };
  useEffect(() => { stop(); }, deps);
  useEffect(() => () => { tm.current.forEach(clearTimeout); }, []);
  const play = (Q, ms = 480) => { stop(); setAn(0); playKey(Q[0], 0.4); Q.forEach((k, i) => { if (i) tm.current.push(setTimeout(() => { setAn(i); playKey(k, 0.4); }, i * ms)); }); tm.current.push(setTimeout(() => setAn(-1), Q.length * ms + 700)); };
  return { an, play, stop };
}
function scAnim(Q, N2, QS, an, split, tmark) {
  const ps = an > split ? split : 0, marks = {}, names = {}, arcs = [];
  for (let j = ps; j <= an; j++) { marks[Q[j]] = j === an ? 'pick' : (tmark && j <= split && tmark[Q[j]] === 'target') ? 'target' : 'pass'; names[Q[j]] = N2[j]; }
  for (let j = ps; j < an; j++) arcs.push([Q[j], Q[j + 1], j === an - 1, scColOf(QS[j])]);
  return { marks, names, arcs, dn: an > split };
}
const scPlayBtn = (P, Q) => <div style={{textAlign:'center',marginTop:10}}><button className="ghost-btn" style={{...KF_BTN,minWidth:200,borderColor:'#e4572e',color:'#c0431f'}} onClick={() => P.an >= 0 ? P.stop() : P.play(Q)}>{P.an >= 0 ? t('■ Stop', '■ 멈추기') : t('▶ Up and down', '▶ 올라갔다 내려오기')}</button></div>;
"""
rep("\nconst scDirTag =", HELP + "\nconst scDirTag =")
# ---- ScAll
rep("[tk, setTk] = useState('Eb'), [at, setAt] = useState(0), [bad, setBad] = useState(null);",
    "[tk, setTk] = useState('Eb'), [at, setAt] = useState(0), [bad, setBad] = useState(null);\n  const P = useScPlay([view, i, kk, tk]);")
rep("    K.forEach((k, j) => { marks[k] = j === 7 ? 'pick' : 'pass'; names[k] = N[j]; });\n    const pickK",
    "    K.forEach((k, j) => { marks[k] = j === 7 ? 'pick' : 'pass'; names[k] = N[j]; });\n    const Q = K.concat(K.slice(0, 7).reverse()), N2 = N.concat(N.slice(0, 7).reverse()), QS = Q.slice(1).map((k, j) => Math.abs(k - Q[j])), A = P.an >= 0 ? scAnim(Q, N2, QS, P.an, 7) : null;\n    const pickK")
rep("      <ScKeys ks={K} marks={marks} names={names} arcs={ST.map((_, j) => mv(K, j, false))} nonce={nonce + ':' + i + kk}/>\n      <ScPills/>",
    "      {A && scDirTag(A.dn)}\n      <ScKeys ks={K} marks={A ? A.marks : marks} names={A ? A.names : names} arcs={A ? A.arcs : ST.map((_, j) => mv(K, j, false))} nonce={nonce + ':' + i + kk + (A ? 'a' + P.an : '')}/>\n      {A ? <ScPillRow st={QS} upTo={P.an} cur={P.an - 1}/> : <ScPills/>}\n      {scPlayBtn(P, Q)}")
# ---- ScMinor
rep("[fm, setFm] = useState('harmonic'), [at, setAt] = useState(0), [bad, setBad] = useState(null);",
    "[fm, setFm] = useState('harmonic'), [at, setAt] = useState(0), [bad, setBad] = useState(null);\n  const P = useScPlay([view, i, fm]);")
rep("    const f = SC_MF[i], M = mk(f);\n",
    "    const f = SC_MF[i], M = mk(f), D = f === 'melodic' ? mk('natural') : M, Q = M.K.concat(D.K.slice(0, 7).reverse()), N2 = M.N.concat(D.N.slice(0, 7).reverse()), QS = Q.slice(1).map((k, j) => Math.abs(k - Q[j])), A = P.an >= 0 ? scAnim(Q, N2, QS, P.an, 7, M.marks) : null;\n")
rep("      <ScKeys ks={M.K} marks={M.marks} names={M.names} arcs={M.ST.map((_, j) => mvK(M.K, M.ST, j, false))} nonce={nonce + ':' + i}/>\n      <ScPillRow st={M.ST} upTo={7}/>",
    "      {A && scDirTag(A.dn)}\n      <ScKeys ks={M.K} marks={A ? A.marks : M.marks} names={A ? A.names : M.names} arcs={A ? A.arcs : M.ST.map((_, j) => mvK(M.K, M.ST, j, false))} nonce={nonce + ':' + i + (A ? 'a' + P.an : '')}/>\n      {A ? <ScPillRow st={QS} upTo={P.an} cur={P.an - 1}/> : <ScPillRow st={M.ST} upTo={7}/>}\n      {scPlayBtn(P, Q)}")
# ---- ScChrom
rep("  const handKo = (h) => h === 'RH' ? '오른손' : '왼손';\n", "  const handKo = (h) => h === 'RH' ? '오른손' : '왼손';\n  const P = useScPlay([view, i, hand]);\n")
rep("    const nums = E.mode === 'RH' || E.mode === 'LH';\n",
    "    const nums = E.mode === 'RH' || E.mode === 'LH';\n    const Q = K0.concat(K0.slice(0, 12).reverse()), N2 = Q.map((k, j) => j <= 12 ? CHROM_UP[k % 12] : CHROM_DOWN[k % 12]), QS = Q.slice(1).map(() => 1), A = !nums && P.an >= 0 ? scAnim(Q, N2, QS, P.an, 12) : null;\n")
rep("      <ScKeys ring={nums} ks={K0} marks={marks} names={names} arcs={arcs} nonce={nonce + ':' + i}/>\n",
    "      {A && scDirTag(A.dn)}\n      <ScKeys ring={nums} ks={K0} marks={A ? A.marks : marks} names={A ? A.names : names} arcs={A ? A.arcs : arcs} nonce={nonce + ':' + i + (A ? 'a' + P.an : '')}/>\n      {A && <ScPillRow st={QS} upTo={P.an} cur={P.an - 1}/>}\n      {!nums && scPlayBtn(P, Q)}\n")
# ---- ScSame (all view)
a = s.index("function ScSame() {"); b = s.index("function ScDeg()", a)
seg = s[a:b]
def r2(x, y):
    global seg
    assert seg.count(x) == 1, (x[:80], seg.count(x)); seg = seg.replace(x, y)
r2("[kk, setKk] = useState('G'), [at, setAt] = useState(0), [bad, setBad] = useState(null);", "[kk, setKk] = useState('G'), [at, setAt] = useState(0), [bad, setBad] = useState(null);\n  const P = useScPlay([view, i, kk]);")
r2("K.forEach((k, j) => { marks[k] = j === 6 ? 'pick' : 'pass'; names[k] = N[j]; });\n",
   "K.forEach((k, j) => { marks[k] = j === 6 ? 'pick' : 'pass'; names[k] = N[j]; });\n    const Q = K.concat(K.slice(0, 7).reverse()), N2 = N.concat(N.slice(0, 7).reverse()), QS = Q.slice(1).map((k, j) => Math.abs(k - Q[j])), A = P.an >= 0 ? scAnim(Q, N2, QS, P.an, 7) : null;\n")
r2("      <ScKeys ks={K} marks={marks} names={names} arcs={ST.map((_, j) => mv(K, j, false))} nonce=\"all\"/>\n      <ScPills/>",
   "      {A && scDirTag(A.dn)}\n      <ScKeys ks={K} marks={A ? A.marks : marks} names={A ? A.names : names} arcs={A ? A.arcs : ST.map((_, j) => mv(K, j, false))} nonce={'all' + (A ? 'a' + P.an : '')}/>\n      {A ? <ScPillRow st={QS} upTo={P.an} cur={P.an - 1}/> : <ScPills/>}\n      {scPlayBtn(P, Q)}")
s = s[:a] + seg + s[b:]
open(sys.argv[2],'w',encoding='utf-8').write(s)
