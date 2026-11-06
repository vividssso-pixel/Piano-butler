// ─── Phase 424: the Victorian music room (Sohyun 2026-10-10: wainscoting, chess, minimal) ───────────────────────
// Each printed page is one wall of a Victorian music room: the running head sits on a cornice (a thick line, a thin
// line, dentils); pictures hang in white frames with cut-in corners; 'At the piano' and PLAY are raised panels; REMEMBER
// is the chair rail with the fox butler's portrait; a chequered floor runs along the foot with the page number on a
// plaque. Colours: navy (the ink), coral (the point: look here), green (the check); pink only for Clara; no beige.
// The royal family are chess pieces; numbers and section letters sit on dark and light squares.
const VIC_CAPS = { textTransform: 'uppercase', letterSpacing: '0.17em' };
const VIC_PANEL = { position: 'relative', border: '0.8px solid rgba(38,41,107,0.55)', boxShadow: 'inset 0 0 0 5px #fff, inset 0 0 0 5.7px rgba(38,41,107,0.45)', background: '#fff' };
const VIC_DENTILS = "url(\"data:image/svg+xml," + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="7" height="4"><rect x="0" y="0" width="3.6" height="4" fill="#26296b"/></svg>') + "\")";
const VIC_FLOOR = "url(\"data:image/svg+xml," + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><rect width="8" height="8" fill="#26296b"/><rect x="8" y="8" width="8" height="8" fill="#26296b"/></svg>') + "\")";
// a dark or a light chess square holding a number or a letter
const vicSquare = (k, size = 23) => (k % 2 ? { background: '#fff', color: BK.ink, boxShadow: 'inset 0 0 0 1.2px ' + BK.ink } : { background: BK.ink, color: '#fff' });
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
function VicKicker({ children, c = BK.coral, size = 11 }) {
  return <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:10,fontSize:size,fontWeight:800,color:c,...VIC_CAPS}}>
    <span style={{width:22,borderTop:'1px solid ' + c}}/>{children}<span style={{width:22,borderTop:'1px solid ' + c}}/>
  </div>;
}
// the cornice: spaced capitals, then a thick line, a thin line and a row of dentils
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
// the floor: two rows of chequered tiles at the foot of the page, the page number on a plaque
function VicFloor({ no }) {
  return <>
    <div aria-hidden="true" style={{position:'absolute',left:'15mm',right:'15mm',bottom:'4.6mm',height:'4.2mm',borderTop:'0.8px solid ' + BK.ink,borderBottom:'0.8px solid ' + BK.ink,backgroundImage:VIC_FLOOR,backgroundSize:'2.1mm 2.1mm',backgroundPosition:'center 0',opacity:0.9,pointerEvents:'none'}}/>
    {no != null && <div className="lb-no" style={{position:'absolute',left:0,right:0,bottom:'calc(6.7mm - 10px)',display:'flex',justifyContent:'center',pointerEvents:'none'}}>
      <span style={{background:'#fff',minWidth:28,textAlign:'center',padding:'0 6px',boxShadow:'0 0 0 1px ' + BK.ink + ', 0 0 0 2.6px #fff, 0 0 0 3.2px ' + BK.ink,fontFamily:LB_SERIF,fontWeight:800,fontSize:13,lineHeight:'20px',color:BK.ink,fontVariantNumeric:'lining-nums'}}>{no}</span>
    </div>}
  </>;
}
// the royal family as chess pieces: each stands in the box the crown (and before it the face) used, foot 7.4 K below
// the centre, 19.5 K tall -- so every drawing that places a royal keeps its layout
const vicPiece = (svg, cx, cy, k) => { const K = k * 2.1, sc = 19.5 * K / 97; return [{ k: 'raw', svg: '<g transform="translate(' + pFix(cx) + ' ' + pFix(cy + 7.4 * K) + ') scale(' + sc.toFixed(4) + ')">' + svg + '</g>' }]; };
function sfKing(cx, cy, k = 1) { return vicPiece(VIC_KING, cx, cy, k); }     // the King's piece (navy)
function sfQueen(cx, cy, k = 1) { return vicPiece(VIC_QUEEN, cx, cy, k); }   // the Queen's piece (coral)
function sfClara(cx, cy, k = 1) { return vicPiece(VIC_PAWN, cx, cy, k); }    // Princess Clara: a pink pawn with a tiara
// a hairline frame with cut-in corners and a finer line inside it, drawn inside a box (it measures the box)
function VicCutFrame({ inset = 9, r = 11, gap = 3 }) {
  const ref = React.useRef(null); const [sz, setSz] = useState(null);
  React.useLayoutEffect(() => { const el = ref.current; if (!el) return; const m = () => { const b = el.getBoundingClientRect(); setSz([b.width, b.height]); }; m(); let ro = null; try { ro = new ResizeObserver(m); ro.observe(el); } catch (e) {} return () => { if (ro) ro.disconnect(); }; }, []);
  const d = (w, h, i, rr) => { const L = i, T = i, R = w - i, B = h - i; return `M${L + rr} ${T} H${R - rr} A${rr} ${rr} 0 0 0 ${R} ${T + rr} V${B - rr} A${rr} ${rr} 0 0 0 ${R - rr} ${B} H${L + rr} A${rr} ${rr} 0 0 0 ${L} ${B - rr} V${T + rr} A${rr} ${rr} 0 0 0 ${L + rr} ${T} Z`; };
  return <svg ref={ref} aria-hidden="true" style={{position:'absolute',left:0,top:0,width:'100%',height:'100%',pointerEvents:'none',overflow:'visible'}}>
    {sz && sz[0] > 40 && sz[1] > 40 && <><path d={d(sz[0], sz[1], inset, r)} fill="none" stroke={BK.ink} strokeWidth="1.1"/><path d={d(sz[0], sz[1], inset + gap, r + gap)} fill="none" stroke={BK.ink} strokeOpacity="0.45" strokeWidth="0.6"/></>}
  </svg>;
}
function LbPage({ no, chId, kicker, title, teacher, qr, book, children }) {
  return (
    <section className={'bk-page lb-page' + (title ? '' : ' lb-opener')} data-lb-page={no} style={{position:'relative'}}>
      <VicFloor no={no}/>
      <VicHead left={book || 'Lesson Book'} right={'Chapter ' + bkChapterNo(chId) + ' · ' + bkChapterName(chId)} mb={14}/>
      {title && <div style={{margin:'0 0 10px',textAlign:'center'}}>
        {kicker && <VicKicker>{kicker}</VicKicker>}
        <div style={{fontFamily:LB_SERIF,fontSize:36,fontWeight:900,color:BK.ink,lineHeight:1.05,margin:'3px 0 4px'}}>{title}</div>
        <VicRule/>
      </div>}
      <div className="bk-body" style={{flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column',gap:16}}><BkChapterCtx.Provider value={chId}>{lbWordsFirst(children)}</BkChapterCtx.Provider></div>
      {/* Sohyun 2026-10-09: teacher content prints in the Teacher copy, not in the Lesson Book;
          on screen it still shows in the teacher view (LbScreenPage). */}
    </section>
  );
}
// One fixed A4 page. Head: book + chapter on the cornice; foot: the floor and the page number.
function WbPage({ no, chId, children, bare, teacher }) {
  return (
    <section className="bk-page" style={{position:'relative'}}>
      {!bare && <VicFloor no={no}/>}
      {!bare && <VicHead left={teacher ? <b style={{color:BK.coral}}>Teacher copy</b> : t('Workbook', '워크북')} right={chId === 'front' ? t('Start here', '여기서 시작') : t('Chapter ', '') + bkChapterNo(chId) + t('', '장') + ' · ' + bkChapterName(chId)} mb={9}/>}
      <div style={{flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column'}} className="bk-body"><BkChapterCtx.Provider value={chId}>{children}</BkChapterCtx.Provider></div>
    </section>
  );
}
// the picture box takes whatever height the page has left, so every page ends level (it shrinks back to h when printed
// inside page margins); white, with the cut-in-corner frame inside
function LbPic({ children, h, gap = 18, pad = '14px 16px' }) {
  const pp = String(pad).split(' ').map(parseFloat), p = pp.length === 1 ? (pp[0] + 4) + 'px ' + (pp[0] + 8) + 'px' : pp.map((v, i) => (i % 2 ? v + 8 : v + 4) + 'px').join(' ');
  return <div className="lb-pic" style={{position:'relative',background:'#fff',border:'0.8px solid ' + BK.ink2,padding:p,display:'flex',alignItems:'center',justifyContent:'center',gap,minHeight:lbScreen() ? 0 : h,flex:'1 1 auto',flexWrap:'wrap'}}>{children}<VicCutFrame/></div>;
}
// the chair rail: thick and thin above, thin and thick below, the butler's portrait at its start
function LbRemember({ children }) {
  return (
    <div className="lb-remember" style={{borderTop:'2.4px solid ' + BK.ink,borderBottom:'2.4px solid ' + BK.ink,padding:'1.3px 0'}}>
      <div style={{display:'flex',alignItems:'center',gap:12,borderTop:'0.7px solid ' + BK.ink,borderBottom:'0.7px solid ' + BK.ink,padding:'3px 2px'}}>
        <img src={VIC_CAMEO} alt="" style={{height:42,width:'auto',flex:'0 0 auto'}}/>
        <span style={{fontSize:9.5,fontWeight:800,color:BK.coral,...VIC_CAPS}}>{t('Remember', '기억해요')}</span>
        <span style={{fontSize:16.5,fontWeight:800,color:BK.ink}}>{children}</span>
      </div>
    </div>
  );
}
// an "At the piano" tick box (green: a check): printed, an empty box; on screen, a box the student can tick
function LbTick({ label }) {
  const [on, setOn] = useState(false);
  if (!lbScreen()) return <span style={{flex:'0 0 auto',width:18,height:18,border:'1.6px solid ' + BK.green,borderRadius:2,marginTop:3}}/>;
  return <button onClick={() => setOn(v => !v)} aria-pressed={on} aria-label={label} style={{flex:'0 0 auto',width:24,height:24,border:'1.8px solid ' + BK.green,borderRadius:3,marginTop:0,background:on ? BK.green : '#fff',color:'#fff',fontWeight:900,fontSize:14,lineHeight:1,padding:0,cursor:'pointer'}}>{on ? '✓' : ''}</button>;
}
// 'At the piano': a raised panel of the wainscot; the steps numbered on dark and light squares
function LbPiano({ steps, title, icon }) {
  return (
    <div className="lb-piano" style={{...VIC_PANEL,padding:'11px 16px 12px'}}>
      <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:7}}>{icon || <LbKeysIcon/>}<span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:21,fontWeight:700,color:BK.ink}}>{title || t('At the piano', '피아노 앞에서')}</span></div>
      <div style={{display:'flex',flexDirection:'column',gap:7}}>
        {steps.map((s, i) => (
          <div key={i} style={{display:'flex',alignItems:'flex-start',gap:10,fontSize:15,lineHeight:1.45,color:BK.ink}}>
            <span style={{flex:'0 0 23px',height:23,...vicSquare(i),fontFamily:LB_SERIF,fontWeight:800,fontSize:13.5,fontVariantNumeric:'lining-nums',display:'flex',alignItems:'center',justifyContent:'center'}}>{i + 1}</span>
            <span style={{flex:1,paddingTop:1}}>{s}</span>
            <LbTick label={t('Done', '했어요') + ' ' + (i + 1)}/>
          </div>
        ))}
      </div>
    </div>
  );
}
function LbStageIcon({ i, on }) {
  const c = on || i === 2 ? BK.green : '#c9c3b2';
  if (i === 2) { const pts = Array.from({ length: 10 }, (_, k) => { const r = k % 2 ? 2.9 : 6.8, an = Math.PI / 5 * k - Math.PI / 2; return (8 + r * Math.cos(an)).toFixed(2) + ',' + (8.4 + r * Math.sin(an)).toFixed(2); }).join(' ');
    return <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><polygon points={pts} fill={on ? BK.green : 'none'} stroke={c} strokeWidth="1.6" strokeLinejoin="round"/></svg>; }
  return <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke={c} strokeWidth="1.8"/>{i === 1 && <path d="M8 2 A6 6 0 0 1 8 14 Z" fill={on ? BK.green : '#ddd7c6'}/>}</svg>;
}
// the printed five checks, as a ledger: a double rule above and below, a hairline between; 'Got it!' is green
function LbStageRows({ rows, big }) {   // Phase 409: big = the check page's rows fill the page (no paper part below)
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
// the Workbook's three parts as small plaques with a fine inner line
function BkTag({ kind }) {
  const g = BK_TAG[kind], play = kind === 'play';
  const fill = play ? '#fff' : g.bg;
  return <span style={{flex:'0 0 auto',display:'inline-block',background:fill,color:play ? '#c0431f' : g.fg,boxShadow:'inset 0 0 0 2px ' + fill + ', inset 0 0 0 2.8px ' + (play ? BK.coral : 'rgba(255,255,255,0.75)') + (play ? ', 0 0 0 0.8px ' + BK.coral : ''),padding:'3px 10px 2px',fontSize:9.5,fontWeight:900,letterSpacing:'0.16em',lineHeight:1.3}}>{play && <BkStar size={10} fill={BK.coral}/>} {g.label}</span>;
}
// Three faces to circle: how did this page feel? 'Checked' is green
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
    <div style={{...VIC_PANEL,boxShadow:'inset 0 0 0 3px #fff, inset 0 0 0 3.7px ' + BK.hair,border:'0.8px solid ' + BK.hair,padding:'10px 14px',marginBottom:12,breakInside:'avoid'}}>
      <div style={{display:'flex',alignItems:'baseline',gap:10,marginBottom:6}}>
        <span style={{fontSize:10,fontWeight:900,color:'#fff',background:BK.ink,boxShadow:'inset 0 0 0 2px ' + BK.ink + ', inset 0 0 0 2.7px rgba(255,255,255,0.7)',padding:'3px 8px',letterSpacing:'0.08em'}}>p. {page}</span>
        <span style={{fontFamily:LB_SERIF,fontSize:17,fontWeight:800,color:BK.ink}}>{title}</span>
      </div>
      {answers}
      {goBack && <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,marginTop:6}}><b style={{color:BK.coral}}>If a concept is not passed, go back to:</b> {goBack.filter(c => c.chk !== false).map((c, i) => <span key={c.id}>{i > 0 && ' · '}<b>{'ABCDEFG'[i]}</b> {bkStepLabel(c.step)}, workbook page {c.page}</span>)}</div>}
      {(watch || say) && <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,marginTop:6}}>
        {watch && <div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}><b style={{color:BK.coral}}>Watch for</b><br/>{watch}</div>}
        {say && <div style={{fontSize:12,color:BK.ink,lineHeight:1.5,border:'0.8px solid ' + BK.hair,padding:'6px 9px'}}><b>If stuck, try saying</b><br/>{say}</div>}
      </div>}
    </div>
  );
}
// the chapter openers (every chapter): kicker and title centred over the chequered diamond, the first letter set in
// a dark square, the contents with dotted leaders; a little more room at the foot for the floor
const VIC_OPENER_ORN = encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 190 16"><g stroke="#26296b" stroke-width="0.9"><line x1="0" y1="8" x2="84" y2="8"/><line x1="106" y1="8" x2="190" y2="8"/></g><g transform="rotate(45 95 8)" stroke="#26296b" stroke-width="0.8"><rect x="90" y="3" width="5" height="5" fill="#26296b"/><rect x="95" y="3" width="5" height="5" fill="#fff"/><rect x="90" y="8" width="5" height="5" fill="#fff"/><rect x="95" y="8" width="5" height="5" fill="#26296b"/></g></svg>');
const VIC_CSS = `
  .bk-page { padding-bottom: 11.5mm !important; }
  .lb-opener [data-ch] { text-align: center; }
  .lb-opener [data-ch] > div:first-child { font-size: 11.5px !important; font-weight: 800 !important; letter-spacing: 0.24em !important; }
  .lb-opener [data-ch] > div:first-child::before, .lb-opener [data-ch] > div:first-child::after { content: ''; display: inline-block; width: 26px; border-top: 1px solid currentColor; vertical-align: middle; margin: 0 12px 3px; }
  .lb-opener [data-ch] > div:nth-child(2) { margin-top: 6px !important; }
  .lb-opener [data-ch]::after { content: ''; display: block; height: 16px; margin: 8px auto 0; width: 190px; background: url("data:image/svg+xml,${VIC_OPENER_ORN}") center / contain no-repeat; }
  .lb-opener .bk-body > p.lb-say:first-of-type::first-letter { float: left; font-family: 'Playfair Display', Georgia, serif; font-weight: 900; font-size: 2.6em; line-height: 1; padding: 6px 11px 4px; margin: 5px 12px 0 0; color: #fff; background: #26296b; border: 4px double rgba(255,255,255,0.85); }
  .lb-toc .lb-toc-h { font-style: italic; font-weight: 700 !important; }
  .lb-toc .lb-toc-row { border-bottom: none !important; gap: 8px; }
  .lb-toc .lb-toc-row > span:first-child { flex: 0 1 auto; }
  .lb-toc .lb-toc-row::after { content: ''; order: 1; flex: 1 1 auto; border-bottom: 1.4px dotted rgba(38,41,107,0.45); margin: 0 2px 4px; align-self: flex-end; }
  .lb-toc .lb-toc-row > span:last-child { order: 2; font-family: 'Playfair Display', Georgia, serif; font-style: italic; font-weight: 700 !important; color: #26296b !important; font-variant-numeric: lining-nums; font-size: 15px; }
  .lb-toc div[style*="border-bottom"] { border-bottom-color: rgba(38,41,107,0.14) !important; }
`;
