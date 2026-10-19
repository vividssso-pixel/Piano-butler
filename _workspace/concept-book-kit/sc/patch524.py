import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# KfNav: optional range
rep("function KfNav({ i, setI, children }) {\n  const m = KEY_SIGS.length, step = (d) => setI((i + d + m) % m);",
"function KfNav({ i, setI, children, lo = 0, hi = KEY_SIGS.length - 1 }) {   // Phase 524: lo/hi keep the arrows inside one group\n  const m = hi - lo + 1, step = (d) => setI(lo + ((i - lo + d) % m + m) % m);")
# KfMinor: group buttons
rep("  const pickKey = (x) => { clearTimeout(timer.current); setI(x); setStage(0); setFound(false); setBad(null); };\n  const tapTry",
"""  const pickKey = (x) => { clearTimeout(timer.current); setI(x); setStage(0); setFound(false); setBad(null); };
  const enterTry = (type) => { stopWalk(); setPh('try'); pickKey(type === 'sharp' ? 1 : 8); };   // Phase 524: try sharps or flats straight away
  const grp = ks.type === 'flat' ? 'flat' : 'sharp';
  const grpBtn = (type, label) => <button className="ghost-btn" aria-pressed={grp === type} style={{...KF_BTN,minWidth:110,...(grp === type ? {background:'#26296b',color:'#fffefa',borderColor:'#26296b'} : {})}} onClick={() => enterTry(type)}>{label}</button>;
  const tapTry""")
rep("{tryMode ? <KfNav i={i} setI={pickKey}>{staff}</KfNav> : staff}",
"""{tryMode && <div style={{display:'flex',gap:8,justifyContent:'center',margin:'0 0 6px'}}>{grpBtn('sharp', t('♯ Sharp keys', '♯ 샵 조'))}{grpBtn('flat', t('♭ Flat keys', '♭ 플랫 조'))}</div>}
    {tryMode ? <KfNav i={i} setI={pickKey} lo={grp === 'flat' ? 8 : 1} hi={grp === 'flat' ? 14 : 7}>{staff}</KfNav> : staff}""")
# learn screens: direct try row
rep("      {tryMode && found && go &&",
"""      {!tryMode && <div style={{flexBasis:'100%',display:'flex',gap:8,justifyContent:'center',alignItems:'center',flexWrap:'wrap'}}>
        <span style={{fontSize:13,fontWeight:800,color:'#6b6f9a'}}>{t('Try it:', '바로 해보기:')}</span>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:100}} onClick={() => enterTry('sharp')}>{t('♯ Sharps', '♯ 샵')}</button>
        <button className="ghost-btn" style={{...KF_BTN,minWidth:100}} onClick={() => enterTry('flat')}>{t('♭ Flats', '♭ 플랫')}</button>
      </div>}
      {tryMode && found && go &&""")
rep("() => { stopWalk(); setPh('try'); setStage(0); setFound(false); setBad(null); }}>{r === 0","() => enterTry('sharp')}>{r === 0")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
