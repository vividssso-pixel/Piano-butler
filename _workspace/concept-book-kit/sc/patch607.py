import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
DOWN = "t('Coming down: the same fingers, in reverse.', '내려올 때: 같은 손가락을 거꾸로.')"
# ===== ScWhite (lessons 4 and 5): once she has answered, the key can be played up and down with its fingers
rep("  const last = steps.length - 1, N5 = 5;\n  const PL = useScPlay([view, i]);\n", "  const last = steps.length - 1, N5 = 5;\n  const PL = useScPlay([view, i, at, given]);\n")
rep("    const done = at >= seq.length, ck = done ? 'C' : seq[at], isOdd = ck === odd, P = scPaintKey(ck, hand), N = scNames(ck);\n",
    "    const done = at >= seq.length, ck = done ? 'C' : seq[at], isOdd = ck === odd, P = scPaintKey(ck, hand), N = scNames(ck);\n    const FFt = scFingers(ck, hand, 1), Qt = P.K.concat(P.K.slice(0, 7).reverse()), Nt = FFt.map(String).concat(FFt.slice(0, 7).reverse().map(String)), QSt = Qt.slice(1).map((k, j) => Math.abs(k - Qt[j])), Ad = given != null && !done && PL.an >= 0 ? scAnim(Qt, Nt, QSt, PL.an, 7) : null;\n")
rep("      {!done && <ScKeys nums ks={P.K} marks={given != null ? P.marks : { [P.K[0]]: 'pick' }} names={given != null ? P.names : {}} ncol={P.ncol} arcs={[]} nonce={nonce + ck}/>}\n",
    "      {Ad && scDirTag(Ad.dn)}\n      {!done && <ScKeys nums ks={P.K} marks={Ad ? Ad.marks : given != null ? P.marks : { [P.K[0]]: 'pick' }} names={Ad ? Ad.names : given != null ? P.names : {}} ncol={P.ncol} arcs={Ad ? Ad.arcs : []} nonce={nonce + ck + (Ad ? 'a' + PL.an : '')}/>}\n      {!done && given != null && scPlayBtn(PL, Qt)}\n      {Ad && Ad.dn && <div style={{...scS.line,minHeight:0,fontSize:13}}>{%s}</div>}\n" % DOWN)
# ===== ScBlackHand (lessons 6 and 7): thumbs going up, then the way up stays as a pattern, then the thumbs again coming down
rep("  const [found, setFound] = useState([]), [bad, setBad] = useState(null), [why, setWhy] = useState('');\n  const timers", "  const [found, setFound] = useState([]), [bad, setBad] = useState(null), [why, setWhy] = useState(''), [ph, setPh] = useState(0);\n  const timers")
rep("  const reset = () => { setFound([]); setBad(null); setWhy(''); setNonce(n => n + 1); };\n  const PL = useScPlay([view, i]);\n", "  const reset = () => { setFound([]); setBad(null); setWhy(''); setPh(0); setNonce(n => n + 1); };\n  const PL = useScPlay([view, i, kk, ph]);\n")
rep("    const done = found.length >= thumbs.length, P = scPaintKey(kk, hand), marks = {}, names = {}, ncol = {};\n",
    "    const done = found.length >= thumbs.length, pat = done && ph === 0, fin = done && ph === 1, P = scPaintKey(kk, hand), marks = {}, names = {}, ncol = {};\n    const Qt = K.concat(K.slice(0, 7).reverse()), Nt = F.map(String).concat(F.slice(0, 7).reverse().map(String)), QSt = Qt.slice(1).map((k, j) => Math.abs(k - Qt[j])), Ad = fin && PL.an >= 0 ? scAnim(Qt, Nt, QSt, PL.an, 7) : null;\n")
rep("    const line = done ? t('Both thumbs found.", "    const line = pat ? t('Both thumbs found: that is the way up. Coming down, the thumbs are on the same keys.', '엄지 둘을 찾았어요. 올라가는 길이에요. 내려올 때도 엄지는 같은 건반에 가요.') : Ad && Ad.dn ? %s : done ? t('Both thumbs found." % DOWN)
rep("      : bad != null ? why : t(N[0] + ' major, ' + handWord + ': tap the keys where the thumb goes.", "      : bad != null ? why : ph === 1 ? t(N[0] + ' major, coming down, ' + handWord + ': tap the thumb keys again. (' + found.length + '/' + thumbs.length + ')', N[0] + ' 장음계 내려오기, ' + handKo + ': 엄지 건반을 한 번 더 눌러요. (' + found.length + '/' + thumbs.length + ')') : t(N[0] + ' major, ' + handWord + ': tap the keys where the thumb goes.")
rep("      <ScKeys nums ks={K} marks={marks} names={names} ncol={ncol} arcs={[]} nonce={nonce + kk + hand} onTap={tap}/>\n",
    "      {!fin && scDirTag(ph === 1)}{Ad && scDirTag(Ad.dn)}\n      <ScKeys nums ks={K} marks={Ad ? Ad.marks : marks} names={Ad ? Ad.names : names} ncol={ncol} arcs={Ad ? Ad.arcs : []} nonce={nonce + kk + hand + ph + (Ad ? 'a' + PL.an : '')} onTap={tap}/>\n      {fin && scPlayBtn(PL, Qt)}\n")
rep("        {done && <button className=\"ghost-btn\" style={scS.prim} onClick={() => reset()}>{t('Again', '다시 하기')}</button>}", "        {pat && <button className=\"ghost-btn\" style={scS.prim} onClick={() => { setPh(1); setFound([]); setBad(null); setWhy(''); setNonce(n => n + 1); }}>{t('Come down →', '내려가기 →')}</button>}\n        {fin && <button className=\"ghost-btn\" style={scS.prim} onClick={() => reset()}>{t('Again', '다시 하기')}</button>}")
open(sys.argv[2],'w',encoding='utf-8').write(s)
