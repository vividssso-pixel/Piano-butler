import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("""    const arcs = [], names = {};
    [[1, 0], [1, 2], [3, 2], [3, 4], [6, 5], [6, 7], [8, 7], [8, 9], [10, 9], [10, 11]].forEach(([a, b]) => { arcs.push([a, b, false]); });
    [0, 2, 4, 5, 7, 9, 11].forEach(k => { names[k] = L(k) + '♮'; });""",
"""    const arcs = [[6, 5, true], [10, 11, true]], names = { 6: 'F♯', 5: 'F♮', 10: 'B♭', 11: 'B♮' };   // one sharp, one flat: both come back to the plain key""")
rep("<AcKeys marks={{}} arcs={arcs} names={names} nonce=\"all\" stagger topRoom={46}/>\n      <div style={lineStyle}>{t('Natural (♮)", "<AcKeys marks={{}} arcs={arcs} names={names} nonce=\"all\" stagger topRoom={46}/>\n      <div style={lineStyle}>{t('Natural (♮)")
rep("<AcKeys marks={marks} arcs={shown ? [[e.a, e.b, true]] : []} names={names} nonce={nonce}/>\n      <div style={lineStyle}>{shown ? t(enLine(e)", "<AcKeys marks={marks} arcs={shown ? [[e.a, e.b, true]] : []} names={names} nonce={nonce} stagger topRoom={46}/>\n      <div style={lineStyle}>{shown ? t(enLine(e)")
rep("<AcKeys marks={marks} arcs={done ? [[e.a, e.b, true]] : []} names={names} nonce={nonce} onTap={tap}/>", "<AcKeys marks={marks} arcs={done ? [[e.a, e.b, true]] : []} names={names} nonce={nonce} onTap={tap} stagger topRoom={46}/>")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
