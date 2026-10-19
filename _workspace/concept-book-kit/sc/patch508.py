import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a,s.count(a)); s=s.replace(a,b)
rep("  const [view, setView] = useState('all');","  const [view, setView] = useState('all');   // 'all' -> 'one' (adds one at a time) -> 'tap' (she taps them in order)\n  const [got, setGot] = useState(0);\n  const [bad, setBad] = useState(null);")
# one-by-one starts empty
rep("go={() => { clear(); setN(7); setLit(7); setView('one'); }} label={t('One by one →', '하나씩 →')}",
    "go={() => { clear(); setN(0); setLit(0); setRan(false); setView('one'); }} label={t('One by one →', '하나씩 →')}")
rep("disabled={n <= 1} style={{...KF_BTN,minWidth:52,padding:0,fontSize:22,opacity:n <= 1 ? 0.35 : 1}} onClick={less}",
    "disabled={n <= 0} style={{...KF_BTN,minWidth:52,padding:0,fontSize:22,opacity:n <= 0 ? 0.35 : 1}} onClick={less}")
rep("const less = () => { clear(); if (n > 1) { setN(n - 1); setLit(n - 1); } };","const less = () => { clear(); if (n > 0) { setN(n - 1); setLit(n - 1); } };")
rep("for (let i = 0; i < n; i++) timers.current.push(setTimeout(() => { playKey(kidx(order[i]), 0.45); setLit(i + 1); }, 350 + i * 520)); };",
    "for (let i = 0; i < 7; i++) timers.current.push(setTimeout(() => { playKey(kidx(order[i]), 0.45); setLit(i + 1); setN(i + 1); }, 350 + i * 520)); };")
# one-by-one page: Next -> tap stage
rep("<KfNext go={mode === 'order' ? go : startFind} label={goLabel} back={() => { clear(); setView('all'); }}/>",
    "<KfNext go={() => { clear(); setGot(0); setBad(null); setLit(0); setN(7); setRan(false); setView('tap'); }} label={t('Your turn →', '내가 해보기 →')} back={() => { clear(); setLit(7); setN(7); setView('all'); }}/>")
# tap stage
rep("  if (phase === 'order') return (<>\n    <KfChain hi={[0]}/>",
"""  const nameWord = sharp ? t('sharp', '샤프') : t('flat', '플랫');
  const tapOrd = (i) => {
    if (got >= 7) return;
    if (i % 12 === pcOfName(order[got])) { clear(); setBad(null); playKey(kidx(order[got]), 0.45); setGot(got + 1); setLit(got + 1); }
    else { setBad(i); clear(); timers.current.push(setTimeout(() => setBad(null), 650)); }
  };
  if (phase === 'order' && view === 'tap') return (<>
    <KfChain hi={[0]}/>
    <div style={titleStyle}>{got >= 7 ? t('All seven!', '일곱 개 모두!') : t('Tap ' + nameWord + ' ' + (got + 1), nameWord + ' ' + (got + 1) + '번을 눌러요')}</div>
    {staff}
    <div style={{display:'flex',flexWrap:'wrap',gap:'0 6px',justifyContent:'center',fontSize:14,fontWeight:700,lineHeight:1.5,margin:'2px 0 6px',textWrap:'balance'}}>
      {words.map((w, i) => <span key={i} style={{opacity:i < got ? 0.45 : 1,color:i === got ? '#c8361b' : '#26296b',fontWeight:i === got ? 900 : 700}}>{w}</span>)}
    </div>
    <div style={{maxWidth:300,margin:'0 auto'}}><TapKeyboard octaves={1} marks={bad != null ? { ...marks, [bad]: 'miss' } : marks} labels="all" bigLabels extraC={sharp} trail={trail} trailLabels={trailLabels} onTap={tapOrd}/></div>
    <KfNext go={mode === 'order' ? go : startFind} label={goLabel} back={() => { clear(); setGot(0); setBad(null); setN(0); setLit(0); setView('one'); }}/>
  </>);
  if (phase === 'order') return (<>
    <KfChain hi={[0]}/>""")
a="""    <KfNext go={mode === 'order' ? go : startFind} label={goLabel} back={() => { clear(); setGot(0); setBad(null); setN(0); setLit(0); setView('one'); }}/>\n  </>);"""
rep(a, open('/dev/stdin').read() if False else """    {got >= 7 ? <KfNext go={mode === 'order' ? go : startFind} label={goLabel} back={() => { clear(); setGot(0); setBad(null); setN(0); setLit(0); setView('one'); }}/>
      : <div style={{textAlign:'center',marginTop:14}}><button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { clear(); setGot(0); setBad(null); setN(0); setLit(0); setView('one'); }}>{t('← Back', '← 이전')}</button></div>}
  </>);""")
rep('want = sharp ? n - 1 : n - 2, auto = want < 0;', "want = sharp ? n - 1 : n - 2, auto = phase !== 'order' && want < 0;")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
