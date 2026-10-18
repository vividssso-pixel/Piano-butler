#!/usr/bin/env python3
# Phase 502 (her 2026-10-19 09:31): the sharps and flats steps open on the ORDER alone (all seven, 'Say the order' with the zigzag),
# and only then unfold one by one: 1 sharp, find the key, 'One more ♯', ... up to 7. No count question at the start.
import sys
s = open(sys.argv[1], encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, 'found %d (want %d): %s' % (s.count(a), n, a[:90])
    s = s.replace(a, b)

rep("  const [ran, setRan] = useState(false);   // Phase 497: the order has been said: its keys are lit\n",
    "  const [ran, setRan] = useState(false);   // Phase 497: the order has been said: its keys are lit\n  const [phase, setPhase] = useState('order');   // Phase 502: 'order' (learn the order), then 'find' (one more each time)\n  const [maxN, setMaxN] = useState(1);\n")
rep("  const say = () => { clear(); setLit(0); setRan(true);",
    "  const startFind = () => { clear(); setPhase('find'); setN(1); setLit(1); setFound(false); setWrong(null); setRan(false); };\n  const toOrder = () => { clear(); setPhase('order'); setN(7); setLit(7); setFound(false); setWrong(null); setRan(false); };\n  const more = () => { pickN(n + 1); setMaxN(m => Math.max(m, n + 1)); };\n  const say = () => { clear(); setLit(0); setRan(true);")
a = s.index("  return (<>\n    <KfChain hi={[0, 1]}/>")
b = s.index("function KfNav(")
NEW = r'''  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',minHeight:27,textWrap:'balance'};
  const wordsRow = <div style={{display:'flex',flexWrap:'wrap',gap:'0 6px',justifyContent:'center',fontSize:14,fontWeight:700,lineHeight:1.5,margin:'2px 0',textWrap:'balance'}}>
    {words.map((w, i) => <span key={i} style={{opacity:i < lit ? 1 : 0.22,color:i === lit - 1 ? '#c8361b' : '#26296b',fontWeight:i === lit - 1 ? 900 : 700,transition:'opacity 0.3s'}}>{w}</span>)}
  </div>;
  const staff = <div style={{maxWidth:260,margin:'0 auto'}}><KSStaff count={lit} type={type} width={200} numbers={ran} upto={ran && lit > 0 ? lit - 1 : undefined}/></div>;
  const board = <div style={{maxWidth:300,margin:'0 auto'}}><TapKeyboard octaves={1} marks={marks} labels="all" bigLabels extraC={sharp} trail={trail} trailLabels={trailLabels}/></div>;
  if (phase === 'order') return (<>
    <KfChain hi={[0]}/>
    <div style={titleStyle}>{sharp ? t('The order of sharps', '샤프의 순서') : t('The order of flats', '플랫의 순서')}</div>
    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'0 0 6px'}}>{sharp ? t('Sharps always come in this order.', '샤프는 언제나 이 순서로 붙어요.') : t('Flats come in the same order, backwards.', '플랫은 같은 순서를 거꾸로 붙어요.')}</div>
    {staff}
    {wordsRow}
    {!sharp && <div style={{textAlign:'center',fontSize:12,color:'#5a5d8f',marginTop:-1}}>{t('the same sentence backwards', '같은 문장을 거꾸로')}</div>}
    <div style={{textAlign:'center',margin:'4px 0 10px'}}><button className="ghost-btn" style={{...KF_BTN,minWidth:120}} onClick={say}>{t('▶ Say the order', '▶ 순서 듣기')}</button></div>
    {board}
    <KfNext go={startFind}/>
  </>);
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  return (<>
    <KfChain hi={[0, 1]}/>
    <div style={titleStyle}>
      {done ? <span style={{animation:'fadeUp 0.3s both',display:'inline-block'}}>{n}{sym} → <span style={{color:'#c0431f'}}>{majName(k)}</span></span> : t('What key has ' + n + sym + '?', (sharp ? '샤프 ' : '플랫 ') + n + '개는 무슨 조?')}
    </div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + (tiny ? 4 : 7) + ', minmax(0, 1fr))',gap:4,marginBottom:6}}>
      {[1, 2, 3, 4, 5, 6, 7].map(i => <button key={i} className={'chip' + (n === i ? ' active' : '')} aria-pressed={n === i} aria-disabled={i > maxN} style={{...KF_BTN,minWidth:44,padding:'0 2px',fontSize:14,opacity:i > maxN ? 0.3 : 1}} onClick={() => { if (i <= maxN) pickN(i); }}>{i}{sym}</button>)}
    </div>
    {staff}
    {wordsRow}
    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px'}}>{auto ? t('Only one: it is F.', '하나뿐이면 F예요.') : sharp ? t('Now tap the last ♯.', '이제 마지막 샤프를 눌러요.') : t('Now tap the second-to-last ♭.', '이제 뒤에서 두 번째 플랫을 눌러요.')}</div>
    {!auto && <div style={{display:'flex',gap:4,justifyContent:'center',marginBottom:8}}>
      {order.slice(0, n).map((nm, i) => <button key={nm} aria-label={prettyNote(nm)} className="chip" style={{...KF_BTN,flex:'1 1 0',minWidth:0,maxWidth:56,padding:'0 2px',fontSize:15,
        background:done && i === want ? '#26296b' : '#fff',color:done && i === want ? '#fffefa' : '#26296b',borderColor:wrong === i ? '#e4572e' : undefined,borderWidth:wrong === i ? 2.5 : undefined,opacity:done && i !== want ? 0.35 : 1}} onClick={() => tap(i)}>{prettyNote(nm)}</button>)}
    </div>}
    {board}
    <div style={{textAlign:'center',fontSize:13,fontWeight:700,color:'#5a5d8f',minHeight:20,marginTop:6}}>{done && !auto ? (sharp ? t('A half step up from the last ♯.', '마지막 샤프의 반음 위!') : t('That ♭ is the key.', '그 플랫이 바로 그 조!')) : ''}</div>
    <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
      <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={toOrder}>{t('← The order', '← 순서')}</button>
      {done && (n < 7 ? <button className="ghost-btn" style={prim} onClick={more}>{t('One more ' + sym + ' →', (sharp ? '샤프' : '플랫') + ' 하나 더 →')}</button> : <button className="ghost-btn" style={prim} onClick={go}>{t('Next →', '다음 →')}</button>)}
    </div>
  </>);
}
'''
s = s[:a] + NEW + s[b:]
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
