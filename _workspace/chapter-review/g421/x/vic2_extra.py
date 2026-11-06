#!/usr/bin/env python3
# SAMPLE ONLY, round 2 (Sohyun 2026-10-10 08:58: ' 빅토리안스타일 빌딩들을 좋아하거든, 웨인스코팅 이런거 들어간 스타일 ...
# 너무 아이들 스럽지 않게 어른들한테도 들어오고 싶은 느낌 ... 체스 생각하면 좋을 듯').
# Applied AFTER vic_sample.py. Each page is a wall of a Victorian music room:
#   cornice   the running head sits on a moulding: a thick line, a thin line and a row of dentils
#   pictures  hang in moulded frames with square corner blocks (like Victorian door casings)
#   wainscot  'At the piano' and the PLAY box are raised panels; REMEMBER is the chair rail
#   floor     a two-row chequered floor at the foot of every page, the page number on a small plaque
#   chess     section letters on chess squares, the opener's first letter set in a dark square, a chequered
#             diamond for the ornament; the labels become plaques. Green is a deeper bottle green.
#   python3 vic2_extra.py <src already patched by vic_sample.py>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

rep("green: '#2e8a6e', greenSoft: '#e4f2ec',", "green: '#2b6e56', greenSoft: '#e2efe9', band: '#efe6d2', ink2: 'rgba(38,41,107,0.55)',", 'green')
for name in ['VicRule', 'VicHead', 'VicFrame', 'LbPic', 'LbPiano', 'LbRemember', 'BkTag']:
    rep('function %s(' % name, 'function %sV1(' % name, name)
rep("""        <span style={{fontSize:10,fontWeight:900,color:'#fff',background:BK.ink,clipPath:'polygon(6px 0, calc(100% - 6px) 0, 100% 50%, calc(100% - 6px) 100%, 6px 100%, 0 50%)',padding:'2px 11px',letterSpacing:'0.08em'}}>p. {page}</span>""",
    """        <span style={{fontSize:10,fontWeight:900,color:'#fff',background:BK.ink,boxShadow:'inset 0 0 0 2px ' + BK.ink + ', inset 0 0 0 2.7px rgba(255,255,255,0.7)',padding:'3px 8px',letterSpacing:'0.08em'}}>p. {page}</span>""", 'tc badge')
# section letters on chess squares: A dark, B light, C dark ...
rep("""const bkSec = (letter, title) => <div style={{display:'flex',alignItems:'baseline',gap:8,margin:'9px 0 4px'}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:17,fontWeight:800,color:BK.ink,lineHeight:1}}>{letter}</span>""",
    """const bkSec = (letter, title) => <div style={{display:'flex',alignItems:'center',gap:9,margin:'7px 0 3px'}}><span style={{flex:'0 0 18px',height:18,display:'flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:12.5,fontWeight:800,lineHeight:1,...((letter.charCodeAt(0) % 2) ? {background:BK.ink,color:'#fff'} : {background:'#fff',color:BK.ink,boxShadow:'inset 0 0 0 1.2px ' + BK.ink})}}>{letter}</span>""", 'bkSec')
# the opener's first letter in a dark square
rep("""  .lb-opener .bk-body > p.lb-say:first-of-type::first-letter { float: left; font-family: 'Playfair Display', Georgia, serif; font-weight: 900; font-size: 3.15em; line-height: 0.82; padding: 5px 8px 0 0; color: #e4572e; }""",
    """  .lb-opener .bk-body > p.lb-say:first-of-type::first-letter { float: left; font-family: 'Playfair Display', Georgia, serif; font-weight: 900; font-size: 2.6em; line-height: 1; padding: 6px 11px 4px; margin: 5px 12px 0 0; color: #fff; background: #26296b; border: 4px double rgba(255,255,255,0.85); }""", 'drop cap')
rep("""  .bk-page { padding-bottom: 11.5mm !important; }""", """  .bk-page { padding-bottom: 11.5mm !important; }""", 'pad')

add = r'''
// ─── SAMPLE round 2: the music room (wainscoting, a chequered floor, chess) ──────────
// a chequered diamond: four small squares turned 45 degrees, two dark and two light
function VicChequer({ s = 12 }) {
  return <svg width={s} height={s} viewBox="0 0 10 10" style={{display:'block',flex:'0 0 auto'}} aria-hidden="true"><g transform="rotate(45 5 5)" stroke={BK.ink} strokeWidth="0.55">
    <rect x="1.8" y="1.8" width="3.2" height="3.2" fill={BK.ink}/><rect x="5" y="1.8" width="3.2" height="3.2" fill="#fff"/><rect x="1.8" y="5" width="3.2" height="3.2" fill="#fff"/><rect x="5" y="5" width="3.2" height="3.2" fill={BK.ink}/></g></svg>;
}
function VicRule({ w = 70, c = BK.ink, style }) {
  return <div aria-hidden="true" style={{display:'flex',alignItems:'center',justifyContent:'center',gap:7,...style}}>
    <span style={{width:w,borderTop:'0.9px solid ' + c}}/><VicChequer/><span style={{width:w,borderTop:'0.9px solid ' + c}}/>
  </div>;
}
// the cornice: spaced capitals, then a thick line, a thin line and a row of dentils
const VIC_DENTILS = "url(\"data:image/svg+xml," + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="7" height="4"><rect x="0" y="0" width="3.6" height="4" fill="#26296b"/></svg>') + "\")";
function VicHead({ left, right, mb = 12 }) {
  return <div className="lb-head" style={{marginBottom:mb}}>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',fontSize:8.6,color:BK.muted,fontWeight:700,paddingBottom:5,...VIC_CAPS}}>
      <span><b style={{color:BK.ink,fontWeight:800}}>Piano Butler</b> · {left}</span><span>{right}</span>
    </div>
    <div style={{borderTop:'2.2px solid ' + BK.ink}}/>
    <div style={{borderTop:'0.7px solid ' + BK.ink,marginTop:1.6}}/>
    <div style={{height:4,marginTop:1.6,backgroundImage:VIC_DENTILS,backgroundRepeat:'repeat-x',opacity:0.85}}/>
  </div>;
}
// the floor: two rows of chequered tiles across the foot of the page, the page number on a plaque
const VIC_FLOOR = "url(\"data:image/svg+xml," + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><rect width="8" height="8" fill="#26296b"/><rect x="8" y="8" width="8" height="8" fill="#26296b"/></svg>') + "\")";
function VicFrame({ no }) {
  return <>
    <div aria-hidden="true" style={{position:'absolute',left:'15mm',right:'15mm',bottom:'4.6mm',height:'4.2mm',borderTop:'0.8px solid ' + BK.ink,borderBottom:'0.8px solid ' + BK.ink,backgroundImage:VIC_FLOOR,backgroundSize:'2.1mm 2.1mm',backgroundPosition:'center 0',opacity:0.9,pointerEvents:'none'}}/>
    {no != null && <div className="lb-no" style={{position:'absolute',left:0,right:0,bottom:'calc(6.7mm - 11px)',display:'flex',justifyContent:'center',pointerEvents:'none'}}>
      <span style={{background:'#fff',minWidth:30,textAlign:'center',padding:'0 6px',boxShadow:'0 0 0 1px ' + BK.ink + ', 0 0 0 3px #fff, 0 0 0 3.7px ' + BK.ink,fontFamily:LB_SERIF,fontWeight:800,fontSize:13.5,lineHeight:'22px',color:BK.ink,fontVariantNumeric:'lining-nums'}}>{no}</span>
    </div>}
  </>;
}
// a corner block of a door casing: a square with a small ring inside
const vicBlock = (pos, key) => <span key={key} aria-hidden="true" style={{position:'absolute',width:13,height:13,background:BK.band,boxShadow:'inset 0 0 0 0.8px ' + BK.ink2,...pos,display:'flex',alignItems:'center',justifyContent:'center'}}><span style={{width:5,height:5,borderRadius:3,border:'0.8px solid ' + BK.ink2}}/></span>;
const vicBlocks = () => [vicBlock({left:0,top:0}, 'a'), vicBlock({right:0,top:0}, 'b'), vicBlock({left:0,bottom:0}, 'c'), vicBlock({right:0,bottom:0}, 'd')];
// a picture in a moulded frame: an outer line, a moulding band, an inner line; corner blocks
function LbPic({ children, h, gap = 18, pad = '14px 16px' }) {
  const pp = String(pad).split(' ').map(parseFloat), p = pp.length === 1 ? pp[0] + 'px ' + (pp[0] + 4) + 'px' : pp.map((v, i) => (i % 2 ? v + 4 : v) + 'px').join(' ');
  return <div className="lb-pic" style={{position:'relative',background:BK.soft,border:'0.8px solid ' + BK.ink2,boxShadow:'inset 0 0 0 6px ' + BK.band + ', inset 0 0 0 6.8px ' + BK.ink2,padding:p,display:'flex',alignItems:'center',justifyContent:'center',gap,minHeight:lbScreen() ? 0 : h,flex:'1 1 auto',flexWrap:'wrap'}}>{children}{vicBlocks()}</div>;
}
// the chair rail: thick and thin above, thin and thick below
function LbRemember({ children }) {
  return (
    <div style={{borderTop:'2.4px solid ' + BK.ink,borderBottom:'2.4px solid ' + BK.ink,padding:'1.3px 0'}}>
      <div style={{display:'flex',alignItems:'center',gap:12,borderTop:'0.7px solid ' + BK.ink,borderBottom:'0.7px solid ' + BK.ink,padding:'3px 2px'}}>
        <PbArt name="rabbit-head" h={40}/>
        <span style={{fontSize:9.5,fontWeight:800,color:BK.coral,...VIC_CAPS}}>{t('Remember', '기억해요')}</span>
        <span style={{fontSize:16.5,fontWeight:800,color:BK.ink}}>{children}</span>
      </div>
    </div>
  );
}
// a raised panel of the wainscot: outer line, a bevel band, inner line, a white field
const VIC_PANEL = { position:'relative', border:'0.8px solid ' + 'rgba(38,41,107,0.55)', boxShadow:'inset 0 0 0 5px #f4eedf, inset 0 0 0 5.7px rgba(38,41,107,0.45)', background:'#fff' };
function LbPiano({ steps, title, icon }) {
  return (
    <div className="lb-piano" style={{...VIC_PANEL,padding:'11px 16px 12px'}}>
      <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:7}}>{icon || <LbKeysIcon/>}<span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:21,fontWeight:700,color:BK.ink}}>{title || t('At the piano', '피아노 앞에서')}</span></div>
      <div style={{display:'flex',flexDirection:'column',gap:7}}>
        {steps.map((s, i) => (
          <div key={i} style={{display:'flex',alignItems:'flex-start',gap:10,fontSize:15,lineHeight:1.45,color:BK.ink}}>
            <span style={{flex:'0 0 23px',height:23,...(i % 2 ? {background:'#fff',color:BK.ink,boxShadow:'inset 0 0 0 1.2px ' + BK.ink} : {background:BK.ink,color:'#fff'}),fontFamily:LB_SERIF,fontWeight:800,fontSize:13.5,fontVariantNumeric:'lining-nums',display:'flex',alignItems:'center',justifyContent:'center'}}>{i + 1}</span>
            <span style={{flex:1,paddingTop:1}}>{s}</span>
            <LbTick label={t('Done', '했어요') + ' ' + (i + 1)}/>
          </div>
        ))}
      </div>
    </div>
  );
}
// the workbook's three parts as small plaques with a fine inner line
function BkTag({ kind }) {
  const g = BK_TAG[kind], play = kind === 'play';
  const fill = play ? '#fff' : g.bg, ink = play ? BK.coral : '#fff';
  return <span style={{flex:'0 0 auto',display:'inline-block',background:fill,color:play ? '#c0431f' : g.fg,boxShadow:'inset 0 0 0 2px ' + fill + ', inset 0 0 0 2.8px ' + (play ? BK.coral : 'rgba(255,255,255,0.75)') + (play ? ', 0 0 0 0.8px ' + BK.coral : ''),padding:'3px 10px 2px',fontSize:9.5,fontWeight:900,letterSpacing:'0.16em',lineHeight:1.3}}>{play && <BkStar size={10} fill={BK.coral}/>} {g.label}</span>;
}
'''
rep("// ─── SAMPLE: Victorian, minimal ─", add + "// ─── SAMPLE: Victorian, minimal ─", 'add')
# the PLAY box: a raised panel too
rep("""? <div style={{border:'3px double ' + BK.hair,borderRadius:3,padding:'9px 14px 10px',margin:'10px 0 0',""",
    """? <div style={{...VIC_PANEL,padding:'10px 16px 10px',margin:'10px 0 0',""", 'play panel')
# the openers' ornament: hairline -- chequered diamond -- hairline
import re
m = re.search(r"\n  \.lb-opener \[data-ch\]::after \{[^\n]*\n", s)
if not m: raise SystemExit('opener ornament')
svg = '<svg xmlns=\\"http://www.w3.org/2000/svg\\" viewBox=\\"0 0 190 16\\"><g stroke=\\"#26296b\\" stroke-width=\\"0.9\\"><line x1=\\"0\\" y1=\\"8\\" x2=\\"84\\" y2=\\"8\\"/><line x1=\\"106\\" y1=\\"8\\" x2=\\"190\\" y2=\\"8\\"/></g><g transform=\\"rotate(45 95 8)\\" stroke=\\"#26296b\\" stroke-width=\\"0.8\\"><rect x=\\"90\\" y=\\"3\\" width=\\"5\\" height=\\"5\\" fill=\\"#26296b\\"/><rect x=\\"95\\" y=\\"3\\" width=\\"5\\" height=\\"5\\" fill=\\"#fff\\"/><rect x=\\"90\\" y=\\"8\\" width=\\"5\\" height=\\"5\\" fill=\\"#fff\\"/><rect x=\\"95\\" y=\\"8\\" width=\\"5\\" height=\\"5\\" fill=\\"#26296b\\"/></g></svg>'
s = s[:m.start()] + "\n  .lb-opener [data-ch]::after { content: ''; display: block; height: 16px; margin: 8px auto 0; width: 190px; background: url(\"data:image/svg+xml,${encodeURIComponent('" + svg + "')}\") center / contain no-repeat; }\n" + s[m.end():]

rep("<div style={{fontFamily:LB_SERIF,fontSize:36,fontWeight:900,color:BK.ink,lineHeight:1.05,margin:'4px 0 7px'}}>{title}</div>", "<div style={{fontFamily:LB_SERIF,fontSize:36,fontWeight:900,color:BK.ink,lineHeight:1.05,margin:'3px 0 4px'}}>{title}</div>", 'title margin')
open(src, 'w', encoding='utf-8').write(s); print('vic2 ok')
