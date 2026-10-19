import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("}, 800 + (q - 1) * 1500)));","}, 600 + (q - 1) * 1000)));")
rep("playKey(pcOfName(k.major), 0.9); }, 1000);","playKey(pcOfName(k.major), 0.9); }, 700);")
rep("    {tryMode ? <KfNav i={i} setI={pickKey} lo={grp === 'flat' ? 8 : 1} hi={grp === 'flat' ? 14 : 7}>{staff}</KfNav> : staff}",
"""    {staff}
    {tryMode && (() => { const lo = grp === 'flat' ? 8 : 1, hi = grp === 'flat' ? 14 : 7, sg = grp === 'flat' ? '♭' : '♯';
      const pm1 = (txt, d, lab) => <button className="ghost-btn" aria-label={lab} disabled={i + d < lo || i + d > hi} style={{...KF_BTN,minWidth:84,fontSize:22,opacity:(i + d < lo || i + d > hi) ? 0.35 : 1}} onClick={() => pickKey(i + d)}>{txt}</button>;
      return <div style={{display:'flex',gap:12,justifyContent:'center',alignItems:'center',margin:'4px 0 0'}}>
        {pm1('−', -1, t('One less ' + sg, sg + ' 하나 빼기'))}
        <span style={{fontSize:18,fontWeight:900,color:'#26296b',minWidth:34,textAlign:'center'}}>{ks.count}{sg}</span>
        {pm1('+', 1, t('One more ' + sg, sg + ' 하나 더하기'))}
      </div>; })()}""")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
