import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a,s.count(a)); s=s.replace(a,b)
rep("  const [maxN, setMaxN] = useState(1);\n  const timers = useRef([]);\n  const tiny = useCbNarrow(380);",
    "  const [maxN, setMaxN] = useState(1);\n  const [view, setView] = useState('all');   // Phase 507: the order screen shows all seven first, then one by one\n  const timers = useRef([]);\n  const tiny = useCbNarrow(380);")
rep("  if (phase === 'order') return (<>\n    <KfChain hi={[0]}/>",
    """  if (phase === 'order' && view === 'all') return (<>
    <KfChain hi={[0]}/>
    <div style={titleStyle}>{sharp ? t('The order of sharps', '샤프의 순서') : t('The order of flats', '플랫의 순서')}</div>
    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'0 0 10px'}}>{sharp ? t('Seven sharps, always in this order.', '샤프는 일곱 개, 언제나 이 순서로 붙어요.') : t('Seven flats, the same order backwards.', '플랫도 일곱 개, 같은 순서를 거꾸로 붙어요.')}</div>
    <div style={{maxWidth:330,margin:'0 auto'}}><KSStaff count={7} type={type} width={260} numbers/></div>
    {wordsRow}
    {!sharp && <div style={{textAlign:'center',fontSize:12,color:'#5a5d8f',marginTop:-1}}>{t('the same sentence backwards', '같은 문장을 거꾸로')}</div>}
    <KfNext go={() => { clear(); setN(7); setLit(7); setView('one'); }} label={t('One by one →', '하나씩 →')} back={backFn}/>
  </>);
  if (phase === 'order') return (<>
    <KfChain hi={[0]}/>""")
rep("<KfNext go={mode === 'order' ? go : startFind} label={goLabel} back={backFn}/>\n  </>);\n  const prim",
    "<KfNext go={mode === 'order' ? go : startFind} label={goLabel} back={() => { clear(); setView('all'); }}/>\n  </>);\n  const prim")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
