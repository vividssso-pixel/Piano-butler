import sys
s=open(sys.argv[1],encoding='utf-8').read()
s2=None
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
DOWN = "t('Coming down: the same fingers, in reverse.', '내려올 때: 같은 손가락을 거꾸로.')"
# ---- ScWhite: the last "one" screen (the whole fingering) can be played up and down
rep("  const last = steps.length - 1, N5 = 5;\n", "  const last = steps.length - 1, N5 = 5;\n  const PL = useScPlay([view, i]);\n")
rep("""    const E = steps[i], P = scPaintKey('C', hand, E.n);
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t(E.text[0], E.text[1])}</div>
      <ScKeys nums ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce={nonce + ':' + i}/>
""", """    const E = steps[i], P = scPaintKey('C', hand, E.n);
    const FF = scFingers('C', hand, 1), Qd = P.K.concat(P.K.slice(0, 7).reverse()), Nd = FF.map(String).concat(FF.slice(0, 7).reverse().map(String)), QSd = Qd.slice(1).map((k, j) => Math.abs(k - Qd[j])), Ad = i === last && PL.an >= 0 ? scAnim(Qd, Nd, QSd, PL.an, 7) : null;
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{Ad && Ad.dn ? %s : t(E.text[0], E.text[1])}</div>
      {Ad && scDirTag(Ad.dn)}
      <ScKeys nums ks={P.K} marks={Ad ? Ad.marks : P.marks} names={Ad ? Ad.names : P.names} ncol={P.ncol} arcs={Ad ? Ad.arcs : []} nonce={nonce + ':' + i + (Ad ? 'a' + PL.an : '')}/>
      {i === last && scPlayBtn(PL, Qd)}
""" % DOWN)
# ---- ScBlackHand: every key screen is a whole scale
rep("  const reset = () => { setFound([]); setBad(null); setWhy(''); setNonce(n => n + 1); };\n", "  const reset = () => { setFound([]); setBad(null); setWhy(''); setNonce(n => n + 1); };\n  const PL = useScPlay([view, i]);\n")
rep("""    const E = STEPS[i], P = scPaintKey(E.key, hand);
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{t(E.text[0], E.text[1])}</div>
      <ScKeys nums ks={P.K} marks={P.marks} names={P.names} ncol={P.ncol} arcs={[]} nonce={nonce + ':' + i}/>
""", """    const E = STEPS[i], P = scPaintKey(E.key, hand);
    const FF = SCALES[E.key].octaves[1][hand], Qd = P.K.concat(P.K.slice(0, 7).reverse()), Nd = FF.map(String).concat(FF.slice(0, 7).reverse().map(String)), QSd = Qd.slice(1).map((k, j) => Math.abs(k - Qd[j])), Ad = PL.an >= 0 ? scAnim(Qd, Nd, QSd, PL.an, 7) : null;
    body = <>
      <div style={scS.title}>{title}</div>
      <div style={scS.line}>{Ad && Ad.dn ? %s : t(E.text[0], E.text[1])}</div>
      {Ad && scDirTag(Ad.dn)}
      <ScKeys nums ks={P.K} marks={Ad ? Ad.marks : P.marks} names={Ad ? Ad.names : P.names} ncol={P.ncol} arcs={Ad ? Ad.arcs : []} nonce={nonce + ':' + i + (Ad ? 'a' + PL.an : '')}/>
      {scPlayBtn(PL, Qd)}
""" % DOWN)
# the half-step question: two half steps (3-4 and 7-8) are on the keys, only one is offered; say "which of these"
s2 = s
a="prompt(t('Between which degrees is a half step?', '어느 두 번호 사이가 반 걸음일까요?'))"
assert s2.count(a)==1
s2=s2.replace(a,"prompt(t('Which of these pairs is a half step?', '다음 중 반 걸음인 곳은 어디일까요?'))")
open(sys.argv[2],'w',encoding='utf-8').write(s2)
