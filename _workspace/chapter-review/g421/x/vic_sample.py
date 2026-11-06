#!/usr/bin/env python3
# SAMPLE ONLY (not for the site): the books in a Victorian, minimal look (Sohyun 2026-10-10 08:15:
# '전체 빅토리안 스타일로 가는것도 샘플 만들어서 보여줘 ... 체크하는 곳에는 초록색 ... 미니멀함을 유지하되 ... 모던함 가져가면서').
#   python3 vic_sample.py <drills.src.html>
# What changes (shared parts only, so every chapter follows):
#   paper     a hairline frame with cut-in corners; the page number sits on the frame's bottom line
#   type      running heads in spaced small capitals over a thick-and-thin rule; titles centred with a small
#             diamond ornament under them; subheads in Playfair italic; numerals in Playfair italic
#   colour    navy = the ink; coral = the point (look here: the example, the key word, YOUR TURN);
#             green = the check (tick boxes, Got it!, Checked, the Teacher copy's answers)
#   shapes    picture boxes and frames with square corners and a fine inner line; workbook tags as labels
#             with pointed ends; the PLAY box and the REMEMBER band in double rules
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# fonts: Playfair italic and the lighter weights
rep("family=Playfair+Display:wght@800;900", "family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,600;1,700;1,800", 'font link')

# palette: green joins navy and coral
rep("const BK = { ink: '#26296b', coral: '#e4572e', muted: '#6d6f9c', line: '#d9d3c4', soft: '#faf6ec',",
    "const BK = { ink: '#26296b', coral: '#e4572e', muted: '#6d6f9c', line: '#d9d3c4', soft: '#faf6ec', green: '#2e8a6e', greenSoft: '#e4f2ec', hair: 'rgba(38,41,107,0.28)',", 'BK')

# rename the parts this sample redraws (the new ones are added below)
for name in ['LbPage', 'LbPic', 'LbRemember', 'LbPiano', 'LbTick', 'LbStageIcon', 'LbStageRows', 'BkTag', 'Faces', 'WbPage', 'BkCell', 'ExCell', 'WbTop', 'TcBlock']:
    rep('function %s(' % name, 'function %sNow(' % name, name)

# Part: the PLAY box in a double rule, square corners
rep("""? <div style={{border:'1.6px dashed ' + BK.coral,borderRadius:12,padding:'9px 14px 10px',margin:'10px 0 0',""",
    """? <div style={{border:'3px double ' + BK.hair,borderRadius:3,padding:'9px 14px 10px',margin:'10px 0 0',""", 'play box')
rep("""      <BkTag kind={kind}/>
      <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:18.5,fontWeight:800,color:BK.ink,lineHeight:1.15}}>{title}</span>""",
    """      <BkTag kind={kind}/>
      <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:19,fontWeight:800,color:BK.ink,lineHeight:1.15}}>{title}</span>""", 'part title')

# small tick boxes = green; section letters and item numbers = navy italic numerals
rep("""const bkTick = (s = 18) => <span style={{display:'inline-block',width:s,height:s,border:'1.5px solid ' + BK.ink,borderRadius:4,""",
    """const bkTick = (s = 18) => <span style={{display:'inline-block',width:s,height:s,border:'1.5px solid ' + BK.green,borderRadius:2,""", 'bkTick')
rep("""const bkSec = (letter, title) => <div style={{display:'flex',alignItems:'baseline',gap:8,margin:'9px 0 4px'}}><span style={{fontSize:13,fontWeight:900,color:BK.coral}}>{letter}</span>""",
    """const bkSec = (letter, title) => <div style={{display:'flex',alignItems:'baseline',gap:8,margin:'9px 0 4px'}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:17,fontWeight:800,color:BK.ink,lineHeight:1}}>{letter}</span>""", 'bkSec')
rep("""<span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',fontSize:11,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{it.ex ? 'e.g.' : it.n}</span>""",
    """<span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',fontFamily:LB_SERIF,fontStyle:'italic',fontSize:13,fontWeight:700,fontVariantNumeric:'lining-nums',color:it.ex ? BK.coral : BK.ink,whiteSpace:'nowrap'}}>{it.ex ? 'e.g.' : it.n}</span>""", 'SfRow numbers')
# the Teacher copy's answers: green, like a tick
rep("""<span style={{color:BK.muted}}>{i + 1}.</span> <b>{a}</b></span>""",
    """<span style={{color:BK.muted}}>{i + 1}.</span> <b style={{color:BK.green}}>{a}</b></span>""", 'tcAns')
# the app's five checks: a chosen stage is green
rep("""style={{height:34,border:'1.5px solid ' + (on ? BK.coral : BK.line),borderRadius:17,background:on ? '#fdeee8' : '#fff',display:'flex',alignItems:'center',gap:4,padding:'0 9px',fontSize:11.5,fontWeight:800,color:on ? BK.coral : BK.muted,cursor:'pointer'}}>""",
    """style={{height:34,border:'1.5px solid ' + (on ? BK.green : BK.line),borderRadius:17,background:on ? BK.greenSoft : '#fff',display:'flex',alignItems:'center',gap:4,padding:'0 9px',fontSize:11.5,fontWeight:800,color:on ? BK.green : BK.muted,cursor:'pointer'}}>""", 'five checks app')

# square corners on the boxes to write in, the QR box; the paper part's head without its own rule (the running head has it)
rep("""border:'1.5px solid ' + (it.ex ? BK.coral : BK.ink),borderRadius:7,""", """border:'1.5px solid ' + (it.ex ? BK.coral : BK.ink),borderRadius:3,""", 'SfRow box')
rep("""const bkBox = (w = 44, h = 26) => <span style={{display:'inline-block',width:w,height:h,border:'1.5px solid ' + BK.line,borderRadius:6,""", """const bkBox = (w = 44, h = 26) => <span style={{display:'inline-block',width:w,height:h,border:'1.5px solid ' + BK.line,borderRadius:3,""", 'bkBox')
rep("""width:w,height:h,border:'1.5px solid ' + BK.coral,borderRadius:6,background:'#fff',color:BK.coral""", """width:w,height:h,border:'1.5px solid ' + BK.coral,borderRadius:3,background:'#fff',color:BK.coral""", 'bkHand')
rep("""<div style={{padding:4,border:'1.5px solid ' + BK.line,borderRadius:8,background:'#fff',lineHeight:0}}><QR url={bkLink('drill=' + id""", """<div style={{padding:4,border:'0.8px solid ' + BK.hair,borderRadius:2,background:'#fff',lineHeight:0}}><QR url={bkLink('drill=' + id""", 'QR strip')
rep("""return <div style={{display:'flex',alignItems:'baseline',justifyContent:'space-between',gap:10,borderTop:'1.6px solid ' + BK.ink,paddingTop:6,flexWrap:'wrap'}}>
    <span style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,color:BK.ink}}>On paper</span>""", """return <div style={{display:'flex',alignItems:'baseline',justifyContent:'space-between',gap:10,paddingTop:2,flexWrap:'wrap'}}>
    <span style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:800,color:BK.ink}}>On paper</span>""", 'paper head')

add = r'''
// ─── SAMPLE: Victorian, minimal ─────────────────────────────────────────────────
const VIC_CAPS = { textTransform: 'uppercase', letterSpacing: '0.17em' };
function VicDiamond({ s = 7, c = BK.ink, open }) {
  return <svg width={s} height={s} viewBox="0 0 10 10" style={{display:'block',flex:'0 0 auto'}} aria-hidden="true"><path d="M5 0.8 L9.2 5 L5 9.2 L0.8 5 Z" fill={open ? '#fff' : c} stroke={c} strokeWidth="1.1"/></svg>;
}
// hairline -- small diamond, big diamond, small diamond -- hairline
function VicRule({ w = 64, c = BK.ink, style }) {
  return <div aria-hidden="true" style={{display:'flex',alignItems:'center',justifyContent:'center',gap:5,...style}}>
    <span style={{width:w,borderTop:'0.9px solid ' + c}}/><VicDiamond s={5} c={c} open/><VicDiamond s={8} c={c}/><VicDiamond s={5} c={c} open/><span style={{width:w,borderTop:'0.9px solid ' + c}}/>
  </div>;
}
function VicKicker({ children, c = BK.coral, size = 11 }) {
  return <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:10,fontSize:size,fontWeight:800,color:c,...VIC_CAPS}}>
    <span style={{width:22,borderTop:'1px solid ' + c}}/>{children}<span style={{width:22,borderTop:'1px solid ' + c}}/>
  </div>;
}
// the running head: spaced capitals over a thick-and-thin rule
function VicHead({ left, right, mb = 12 }) {
  return <div className="lb-head" style={{marginBottom:mb}}>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',fontSize:8.6,color:BK.muted,fontWeight:700,paddingBottom:5,...VIC_CAPS}}>
      <span><b style={{color:BK.ink,fontWeight:800}}>Piano Butler</b> · {left}</span><span>{right}</span>
    </div>
    <div style={{borderTop:'1.5px solid ' + BK.ink}}/><div style={{borderTop:'0.6px solid ' + BK.ink,marginTop:2}}/>
  </div>;
}
// the page's frame: a hairline with cut-in corners, 6.5 mm in from the edge; the page number sits on its bottom line
function VicFrame({ no }) {
  const m = 6.5, r = 3.2, W = 210, H = 297, L = m, T = m, R = W - m, B = H - m;
  const d = `M${L + r} ${T} H${R - r} A${r} ${r} 0 0 0 ${R} ${T + r} V${B - r} A${r} ${r} 0 0 0 ${R - r} ${B} H${L + r} A${r} ${r} 0 0 0 ${L} ${B - r} V${T + r} A${r} ${r} 0 0 0 ${L + r} ${T} Z`;
  const i = 1.1, ri = r + i, Li = L + i, Ti = T + i, Ri = R - i, Bi = B - i;
  const di = `M${Li + ri - i} ${Ti} H${Ri - ri + i} A${ri} ${ri} 0 0 0 ${Ri} ${Ti + ri - i} V${Bi - ri + i} A${ri} ${ri} 0 0 0 ${Ri - ri + i} ${Bi} H${Li + ri - i} A${ri} ${ri} 0 0 0 ${Li} ${Bi - ri + i} V${Ti + ri - i} A${ri} ${ri} 0 0 0 ${Li + ri - i} ${Ti} Z`;
  return <>
    <svg className="vic-frame" viewBox={`0 0 ${W} ${H}`} style={{position:'absolute',left:0,top:0,width:'100%',height:'100%',pointerEvents:'none'}} aria-hidden="true">
      <path d={d} fill="none" stroke={BK.ink} strokeWidth="0.32"/>
      <path d={di} fill="none" stroke={BK.ink} strokeOpacity="0.45" strokeWidth="0.14"/>
    </svg>
    {no != null && <div className="lb-no" style={{position:'absolute',left:0,right:0,bottom:'calc(' + m + 'mm - 9px)',display:'flex',justifyContent:'center',pointerEvents:'none'}}>
      <span style={{background:'#fff',padding:'0 9px',fontFamily:LB_SERIF,fontStyle:'italic',fontWeight:700,fontSize:14.5,lineHeight:'18px',color:BK.ink,fontVariantNumeric:'lining-nums'}}>{no}</span>
    </div>}
  </>;
}
function LbPage({ no, chId, kicker, title, teacher, qr, book, children }) {
  return (
    <section className={'bk-page lb-page' + (title ? '' : ' lb-opener')} data-lb-page={no} style={{position:'relative'}}>
      <VicFrame no={no}/>
      <VicHead left={book || 'Lesson Book'} right={'Chapter ' + bkChapterNo(chId) + ' · ' + bkChapterName(chId)} mb={14}/>
      {title && <div style={{margin:'0 0 10px',textAlign:'center'}}>
        {kicker && <VicKicker>{kicker}</VicKicker>}
        <div style={{fontFamily:LB_SERIF,fontSize:36,fontWeight:900,color:BK.ink,lineHeight:1.05,margin:'4px 0 7px'}}>{title}</div>
        <VicRule/>
      </div>}
      <div className="bk-body" style={{flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column',gap:16}}><BkChapterCtx.Provider value={chId}>{lbWordsFirst(children)}</BkChapterCtx.Provider></div>
    </section>
  );
}
function WbPage({ no, chId, children, bare, teacher }) {
  return (
    <section className="bk-page" style={{position:'relative'}}>
      {!bare && <VicFrame no={no}/>}
      {!bare && <VicHead left={teacher ? <b style={{color:BK.coral}}>Teacher copy</b> : t('Workbook', '워크북')} right={chId === 'front' ? t('Start here', '여기서 시작') : t('Chapter ', '') + bkChapterNo(chId) + t('', '장') + ' · ' + bkChapterName(chId)} mb={9}/>}
      <div style={{flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column'}} className="bk-body"><BkChapterCtx.Provider value={chId}>{children}</BkChapterCtx.Provider></div>
    </section>
  );
}
// the picture box: square corners, a fine line inside the edge
function LbPic({ children, h, gap = 18, pad = '14px 16px' }) {
  return <div className="lb-pic" style={{background:BK.soft,borderRadius:2,border:'0.8px solid ' + BK.hair,boxShadow:'inset 0 0 0 4px ' + BK.soft + ', inset 0 0 0 4.7px ' + BK.hair,padding:pad,display:'flex',alignItems:'center',justifyContent:'center',gap,minHeight:lbScreen() ? 0 : h,flex:'1 1 auto',flexWrap:'wrap'}}>{children}</div>;
}
function LbRemember({ children }) {
  return (
    <div style={{display:'flex',alignItems:'center',gap:12,borderTop:'3px double ' + BK.ink,borderBottom:'3px double ' + BK.ink,padding:'4px 2px'}}>
      <PbArt name="rabbit-head" h={40}/>
      <span style={{fontSize:9.5,fontWeight:800,color:BK.coral,...VIC_CAPS}}>{t('Remember', '기억해요')}</span>
      <span style={{fontSize:16.5,fontWeight:800,color:BK.ink}}>{children}</span>
    </div>
  );
}
function LbTick({ label }) {
  const [on, setOn] = useState(false);
  if (!lbScreen()) return <span style={{flex:'0 0 auto',width:18,height:18,border:'1.6px solid ' + BK.green,borderRadius:2,marginTop:3}}/>;
  return <button onClick={() => setOn(v => !v)} aria-pressed={on} aria-label={label} style={{flex:'0 0 auto',width:24,height:24,border:'1.8px solid ' + BK.green,borderRadius:3,marginTop:0,background:on ? BK.green : '#fff',color:'#fff',fontWeight:900,fontSize:14,lineHeight:1,padding:0,cursor:'pointer'}}>{on ? '✓' : ''}</button>;
}
function LbPiano({ steps, title, icon }) {
  return (
    <div className="lb-piano" style={{border:'0.8px solid ' + BK.hair,boxShadow:'inset 0 0 0 3px #fff, inset 0 0 0 3.7px ' + BK.hair,borderRadius:2,padding:'10px 14px 12px',background:'#fff'}}>
      <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:7}}>{icon || <LbKeysIcon/>}<span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:21,fontWeight:700,color:BK.ink}}>{title || t('At the piano', '피아노 앞에서')}</span></div>
      <div style={{display:'flex',flexDirection:'column',gap:7}}>
        {steps.map((s, i) => (
          <div key={i} style={{display:'flex',alignItems:'flex-start',gap:10,fontSize:15,lineHeight:1.45,color:BK.ink}}>
            <span style={{flex:'0 0 24px',height:24,borderRadius:12,border:'1.3px solid ' + BK.ink,color:BK.ink,fontFamily:LB_SERIF,fontWeight:800,fontSize:14,fontVariantNumeric:'lining-nums',display:'flex',alignItems:'center',justifyContent:'center'}}>{i + 1}</span>
            <span style={{flex:1,paddingTop:1}}>{s}</span>
            <LbTick label={t('Done', '했어요') + ' ' + (i + 1)}/>
          </div>
        ))}
      </div>
    </div>
  );
}
function LbStageIcon({ i, on }) {
  const c = on ? BK.green : i === 2 ? BK.green : '#c9c3b2';
  if (i === 2) { const pts = Array.from({ length: 10 }, (_, k) => { const r = k % 2 ? 2.9 : 6.8, an = Math.PI / 5 * k - Math.PI / 2; return (8 + r * Math.cos(an)).toFixed(2) + ',' + (8.4 + r * Math.sin(an)).toFixed(2); }).join(' ');
    return <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><polygon points={pts} fill={on ? BK.green : 'none'} stroke={c} strokeWidth="1.6" strokeLinejoin="round"/></svg>; }
  return <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke={c} strokeWidth="1.8"/>{i === 1 && <path d="M8 2 A6 6 0 0 1 8 14 Z" fill={on ? BK.green : '#ddd7c6'}/>}</svg>;
}
// the printed five checks, as a ledger: a double rule above and below, a hairline between
function LbStageRows({ rows, big }) {
  const S = lbStages(), cols = big ? '140px 1fr repeat(3, 70px)' : '96px 1fr repeat(3, 62px)';
  return <div style={{display:'flex',flexDirection:'column',gap:big ? 6 : 4,flex:big ? '1 0 auto' : undefined}}>
    <div style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'end',fontSize:9.5,fontWeight:800,color:BK.muted,textAlign:'center',...VIC_CAPS,letterSpacing:'0.12em'}}>
      <span style={{gridColumn:'1 / 3',textAlign:'left',fontFamily:LB_SERIF,fontStyle:'italic',fontSize:19,fontWeight:700,color:BK.ink,whiteSpace:'nowrap',textTransform:'none',letterSpacing:0}}>{t('At the piano', '피아노 앞에서')}</span>
      {S.map((l, i) => <span key={i} style={i === 2 ? {color:BK.green} : null}>{l}</span>)}
    </div>
    <div style={{display:'flex',flexDirection:'column',flex:big ? '1 0 auto' : undefined,borderTop:'3px double ' + BK.ink,borderBottom:'3px double ' + BK.ink}}>
      {rows.map(([pic, txt], i) => <div key={i} style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'center',borderTop:i ? '0.8px solid ' + BK.hair : 'none',padding:big ? '9px 10px' : '3px 8px',flex:big ? '1 0 auto' : undefined}}>
        <div style={{display:'flex',justifyContent:'center',zoom:big ? 1.5 : undefined}}>{pic}</div>
        <div style={{fontSize:big ? 18 : 14,fontWeight:800,color:BK.ink,lineHeight:1.35}}>{txt}</div>
        {[0, 1, 2].map(k => <span key={k} style={{width:big ? 38 : 30,height:big ? 38 : 30,border:'1.5px solid ' + (k === 2 ? BK.green : BK.line),borderRadius:19,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center',zoom:big ? 1.2 : undefined}}><LbStageIcon i={k}/></span>)}
      </div>)}
    </div>
    <div style={{fontSize:13,color:BK.muted}}>{t('Colour a circle each time it gets better: not yet, then nearly, then got it!', '좋아질 때마다 동그라미를 하나씩 칠해요: 아직, 거의, 그리고 됐어요!')}</div>
  </div>;
}
// the workbook's three parts as labels with pointed ends
function BkTag({ kind }) {
  const g = BK_TAG[kind], play = kind === 'play';
  return <span style={{flex:'0 0 auto',display:'inline-block',background:play ? '#fbe3da' : g.bg,color:play ? '#c0431f' : g.fg,clipPath:'polygon(7px 0, calc(100% - 7px) 0, 100% 50%, calc(100% - 7px) 100%, 7px 100%, 0 50%)',padding:'3px 14px 2px',fontSize:9.5,fontWeight:900,letterSpacing:'0.16em',lineHeight:1.35}}>{play && <BkStar size={10} fill={BK.coral}/>} {g.label}</span>;
}
function Faces() {
  const face = (mouth, key) => (
    <svg key={key} width="30" height="30" viewBox="0 0 30 30"><circle cx="15" cy="15" r="13" fill="#fff" stroke={BK.ink} strokeWidth="1.3"/><circle cx="10.5" cy="12" r="1.6" fill={BK.ink}/><circle cx="19.5" cy="12" r="1.6" fill={BK.ink}/><path d={mouth} fill="none" stroke={BK.ink} strokeWidth="1.5" strokeLinecap="round"/></svg>
  );
  return (
    <div style={{display:'flex',alignItems:'center',justifyContent:'flex-end',gap:10,marginTop:8,fontSize:12,color:BK.muted}}>
      <span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:14,color:BK.ink}}>How did it feel? Circle one.</span>
      {face('M9 18 Q15 24 21 18', 'a')}{face('M10 19.5 L20 19.5', 'b')}{face('M9 21.5 Q15 16 21 21.5', 'c')}
      <span style={{marginLeft:14,color:BK.green,fontWeight:800,fontSize:9.5,...VIC_CAPS}}>Checked</span><span style={{width:24,height:24,border:'1.6px solid ' + BK.green,borderRadius:2}}/>
    </div>
  );
}
function BkCell({ n, children }) {
  return (
    <div style={{border:'0.8px solid ' + BK.hair,borderRadius:2,padding:'4px 6px 6px',position:'relative'}}>
      <span style={{position:'absolute',top:2,left:6,fontFamily:LB_SERIF,fontStyle:'italic',fontSize:13,fontWeight:700,fontVariantNumeric:'lining-nums',color:BK.ink}}>{n}</span>
      {children}
    </div>
  );
}
function ExCell({ n, ex, children }) {
  return (
    <div style={{border:ex ? '1.4px solid ' + BK.coral : '0.8px solid ' + BK.hair,background:ex ? '#fff8f5' : '#fff',borderRadius:2,padding:'4px 6px 6px',position:'relative'}}>
      <span style={{position:'absolute',top:ex ? 3 : 2,left:6,fontFamily:ex ? undefined : LB_SERIF,fontStyle:ex ? undefined : 'italic',fontSize:ex ? 9.5 : 13,fontWeight:ex ? 900 : 700,fontVariantNumeric:'lining-nums',color:ex ? BK.coral : BK.ink,letterSpacing:ex ? '0.12em' : 0}}>{ex ? 'EXAMPLE' : n}</span>
      {children}
    </div>
  );
}
function WbTop({ step }) {
  const chId = React.useContext(BkChapterCtx);
  return (
    <div className="wb-top" style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,margin:'0 0 2px'}}>
      <b style={{color:BK.coral,fontSize:10.5,fontWeight:800,...VIC_CAPS}}>{bkStepLabel(step)}</b>
      <span style={{display:'inline-flex',alignItems:'center',gap:6,fontSize:10.5,color:BK.muted}}>online<QR url={bkStepLink(chId, step)} size={34}/></span>
    </div>
  );
}
function TcBlock({ page, title, answers, watch, say, goBack }) {
  return (
    <div style={{border:'0.8px solid ' + BK.hair,boxShadow:'inset 0 0 0 3px #fff, inset 0 0 0 3.7px ' + BK.hair,borderRadius:2,padding:'10px 14px',marginBottom:12,breakInside:'avoid'}}>
      <div style={{display:'flex',alignItems:'baseline',gap:10,marginBottom:6}}>
        <span style={{fontSize:10,fontWeight:900,color:'#fff',background:BK.ink,clipPath:'polygon(6px 0, calc(100% - 6px) 0, 100% 50%, calc(100% - 6px) 100%, 6px 100%, 0 50%)',padding:'2px 11px',letterSpacing:'0.08em'}}>p. {page}</span>
        <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:17,fontWeight:800,color:BK.ink}}>{title}</span>
      </div>
      {answers}
      {goBack && <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,marginTop:6}}><b style={{color:BK.coral}}>If a concept is not passed, go back to:</b> {goBack.filter(c => c.chk !== false).map((c, i) => <span key={c.id}>{i > 0 && ' · '}<b>{'ABCDEFG'[i]}</b> {bkStepLabel(c.step)}, workbook page {c.page}</span>)}</div>}
      {(watch || say) && <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,marginTop:6}}>
        {watch && <div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>Watch for</b><br/>{watch}</div>}
        {say && <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,background:BK.soft,borderRadius:2,padding:'6px 9px'}}><b>If stuck, try saying</b><br/>{say}</div>}
      </div>}
    </div>
  );
}
// the chapter openers (every chapter): kicker and title centred, an ornament under the title, a drop capital,
// the contents with dotted leaders
const VIC_CSS = `
  .bk-page { padding-bottom: 11.5mm !important; }
  .lb-opener [data-ch] { text-align: center; }
  .lb-opener [data-ch] > div:first-child { font-size: 11.5px !important; font-weight: 800 !important; letter-spacing: 0.24em !important; }
  .lb-opener [data-ch] > div:first-child::before, .lb-opener [data-ch] > div:first-child::after { content: ''; display: inline-block; width: 26px; border-top: 1px solid currentColor; vertical-align: middle; margin: 0 12px 3px; }
  .lb-opener [data-ch] > div:nth-child(2) { margin-top: 6px !important; }
  .lb-opener [data-ch]::after { content: ''; display: block; height: 10px; margin: 9px auto 0; width: 190px; background: url("data:image/svg+xml,${encodeURIComponent('<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 190 10\"><g stroke=\"#26296b\" stroke-width=\"0.9\"><line x1=\"0\" y1=\"5\" x2=\"72\" y2=\"5\"/><line x1=\"118\" y1=\"5\" x2=\"190\" y2=\"5\"/></g><path d=\"M80 2.4 L82.6 5 L80 7.6 L77.4 5 Z\" fill=\"#fff\" stroke=\"#26296b\" stroke-width=\"0.9\"/><path d=\"M95 0.8 L99.2 5 L95 9.2 L90.8 5 Z\" fill=\"#26296b\"/><path d=\"M110 2.4 L112.6 5 L110 7.6 L107.4 5 Z\" fill=\"#fff\" stroke=\"#26296b\" stroke-width=\"0.9\"/></svg>')}") center / contain no-repeat; }
  .lb-opener .bk-body > p.lb-say:first-of-type::first-letter { float: left; font-family: 'Playfair Display', Georgia, serif; font-weight: 900; font-size: 3.15em; line-height: 0.82; padding: 5px 8px 0 0; color: #e4572e; }
  .lb-opener .bk-body div[style*="grid-template-columns"] > div > div:first-child { font-style: italic; font-weight: 700 !important; }
  .lb-opener .bk-body div[style*="grid-template-columns"] > div > div[style*="justify-content: space-between"] { border-bottom: none !important; gap: 8px; }
  .lb-opener .bk-body div[style*="grid-template-columns"] > div > div[style*="justify-content: space-between"] > span:first-child { flex: 0 1 auto; }
  .lb-opener .bk-body div[style*="grid-template-columns"] > div > div[style*="justify-content: space-between"]::after { content: ''; order: 1; flex: 1 1 auto; border-bottom: 1.4px dotted rgba(38,41,107,0.45); margin: 0 2px 4px; align-self: flex-end; }
  .lb-opener .bk-body div[style*="grid-template-columns"] > div > div[style*="justify-content: space-between"] > span:last-child { order: 2; font-family: 'Playfair Display', Georgia, serif; font-style: italic; font-weight: 700 !important; color: #26296b !important; font-variant-numeric: lining-nums; font-size: 15px; }
  .lb-opener .bk-body div[style*="grid-template-columns"] > div > div[style*="border-bottom"] { border-bottom-color: rgba(38,41,107,0.14) !important; }
`;
'''
rep("const LESSON_BOOKS = {", add + "const LESSON_BOOKS = {", 'add')
rep("const LB_CSS = PB_KID_CSS + `", "const LB_CSS = PB_KID_CSS + VIC_CSS + `", 'css')
open(src, 'w', encoding='utf-8').write(s); print('vic sample ok')
