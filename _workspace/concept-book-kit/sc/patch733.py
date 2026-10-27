# Build BN (2026-10-27): her 23:15: "it could be shorter still; and I can't tell what is inside a room: Beginner's names
# roughly say it, above that it is hard to guess". (1) The compact house a little shorter again: lower rooms (the
# picture smaller), slimmer floor plaques, a lower roof and turrets. (2) Tap a room: a card slides up with what is
# inside: its full name, its floor, and its steps by title (from the room's own Lesson Book), ticks on the steps done;
# 'Go in' (or the same room again) opens it. The rooms' names stay short; the card says the rest.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)

# (1) a shorter compact house
rep("  const { RH, LH, SLAB, GH } = TH, W = o.wide ? 720 : TH.W, X0 = TH.X0, X1 = W - TH.X0, RX0 = X0, out = { btns: [], fig: null };\n  const cmp = !o.wide && !o.print;   // Build BM: the compact house on phones and narrow screens",
    "  const cmp = !o.wide && !o.print;   // Build BM: the compact house on phones and narrow screens\n  const { RH, SLAB, GH } = TH, LH = cmp ? 22 : TH.LH, W = o.wide ? 720 : TH.W, X0 = TH.X0, X1 = W - TH.X0, RX0 = X0, out = { btns: [], fig: null };   // Build BN: a slimmer plaque")
rep("    body += stR(px, yy + 4, pw, 20, 0.9) + stR(px + 2, yy + 6, pw - 4, 16, 0.4, 'none')\n      + stT((X0 + X1) / 2, yy + 18.4, name,",
    "    body += stR(px, yy + (cmp ? 2 : 4), pw, cmp ? 18 : 20, 0.9) + stR(px + 2, yy + (cmp ? 4 : 6), pw - 4, cmp ? 14 : 16, 0.4, 'none')\n      + stT((X0 + X1) / 2, yy + (cmp ? 15.2 : 18.4), name,")
rep("    const rh = (cmp ? 52 + (fs.wp === 'drape' ? 7 : 0) : RH) + (lay.ml - 1) * 14,", "    const rh = (cmp ? 45 + (fs.wp === 'drape' ? 7 : 0) : RH) + (lay.ml - 1) * 14,")
rep("  const picTop = cmp ? sy + lay.ml * 14 + 7 : Math.max(sy + lay.ml * 14 + 14, cy - 40);", "  const picTop = cmp ? sy + lay.ml * 14 + 5 : Math.max(sy + lay.ml * 14 + 14, cy - 40);")
rep("s += thPic(x + w / 2, picTop, ic, dimNew && st === 'new', cmp ? 0.52 : 0.8);", "s += thPic(x + w / 2, picTop, ic, dimNew && st === 'new', cmp ? 0.44 : 0.8);")
rep("thDome(x + w / 2, picTop - (cmp ? 4 : 0), ic, cmp ? 0.6 : 1)", "thDome(x + w / 2, picTop - (cmp ? 4 : 0), ic, cmp ? 0.52 : 1)")
rep("const rb = top, rt = top - 66,", "const rb = top, rt = top - (cmp ? 54 : 66),")
rep("'L', tx + tw / 2, rt - 82, 'L', tx + tw + 3, rt - 33, 'Z')", "'L', tx + tw / 2, rt - (cmp ? 70 : 82), 'L', tx + tw + 3, rt - 33, 'Z')")
rep("stPiece(pc, tx + tw / 2, rt - 81, 0.3)", "stPiece(pc, tx + tw / 2, rt - (cmp ? 69 : 81), 0.3)")
rep("const y0 = rt - 112, H = pv", "const y0 = rt - (cmp ? 100 : 112), H = pv")

# (2) what is inside a room: a card from the room's own Lesson Book
PEEK = r'''
// Build BN: what is inside a room, from its own Lesson Book: the steps' titles (the opener and the check-up left out)
const _roomSteps = {};
function roomSteps(id) {
  const k = id + '|' + LANG; if (_roomSteps[k]) return _roomSteps[k];
  let out = [];
  try { const f = LB_PAGE_FNS[id]; if (f) out = f(true).slice(1).filter(pg => pg && pg.props && typeof pg.props.title === 'string' && /Step|단계/.test(String(pg.props.kicker || ''))).map(pg => pg.props.title); } catch (e) { out = []; }
  return (_roomSteps[k] = out);
}
function RoomPeek({ id, num, floor, onGo, onClose }) {
  const steps = roomSteps(id), d = loadDone()[id] || {}, st = chapterState(id).status, nDone = steps.filter((_, i) => d[i]).length;
  return ReactDOM.createPortal(<div data-testid="room-peek" style={{position:'fixed',left:0,right:0,bottom:0,zIndex:60,display:'flex',justifyContent:'center',padding:'0 10px calc(10px + env(safe-area-inset-bottom, 0px))',pointerEvents:'none'}}>
    <div role="dialog" aria-label={t('Inside room ' + num, num + '번 방 안')} style={{pointerEvents:'auto',width:'100%',maxWidth:440,background:'#fffefa',border:'1.5px solid rgba(38,41,107,0.28)',borderRadius:16,boxShadow:'0 -6px 26px rgba(38,41,107,0.2)',padding:'12px 14px',maxHeight:'58vh',overflowY:'auto',animation:'fadeUp 0.2s both'}}>
      <div style={{display:'flex',alignItems:'center',gap:10}}>
        <span style={{flex:'0 0 30px',height:30,display:'inline-flex',alignItems:'center',justifyContent:'center',background:st === 'done' ? '#2e8a6e' : BK.ink,color:'#fff',fontFamily:LB_SERIF,fontWeight:800,fontSize:15}}>{num}</span>
        <div style={{flex:1,minWidth:0}}>
          <div style={{fontFamily:LB_SERIF,fontSize:19,fontWeight:800,color:BK.ink,lineHeight:1.15,textWrap:'balance'}}>{bkChapterName(id)}</div>
          <div style={{fontSize:12,fontWeight:800,color:BK.muted,marginTop:2}}>{floor}{steps.length ? ' · ' + t(nDone + ' of ' + steps.length + ' steps done', steps.length + '단계 중 ' + nDone + '단계 완료') : ''}</div>
        </div>
        <button type="button" onClick={onClose} aria-label={t('Close', '닫기')} style={{flex:'0 0 auto',width:36,height:36,borderRadius:18,border:'1.5px solid rgba(38,41,107,0.25)',background:'#fff',color:BK.ink,fontSize:18,fontWeight:900,cursor:'pointer',lineHeight:1}}>×</button>
      </div>
      {steps.length > 0 && <><div style={{fontSize:11.5,fontWeight:900,color:BK.coral,letterSpacing:'0.1em',margin:'10px 0 4px'}}>{t('INSIDE', '방 안에는')}</div>
        <ol style={{margin:0,padding:0,listStyle:'none',display:'grid',gap:3}}>{steps.map((x, i) => <li key={i} style={{display:'flex',gap:8,alignItems:'baseline',fontSize:14.5,lineHeight:1.35,color:BK.ink}}>
          <span style={{flex:'0 0 18px',fontWeight:900,color:d[i] ? '#2e8a6e' : BK.coral,textAlign:'right'}}>{d[i] ? '✓' : i + 1}</span><span>{x}</span></li>)}</ol></>}
      <button type="button" className="primary-btn" data-testid="room-peek-go" style={{marginTop:12,width:'100%'}} onClick={onGo}>{t('Go in →', '들어가기 →')}</button>
    </div>
  </div>, document.body);   // a portal: the map's fade-in transform would otherwise hold the card inside the house
}
'''
rep("let houseCameIn = false;", PEEK + "let houseCameIn = false;")
rep("  const [opening, setOpening] = useState(false);\n  const [wide, setWide]",
    "  const [opening, setOpening] = useState(false), [peek, setPeek] = useState(null);   // Build BN: the room whose card is showing\n  const [wide, setWide]")
rep("    const c = e.target.closest && e.target.closest('[data-chapter]'); if (c) onOpen(c.getAttribute('data-chapter'));\n  };",
    "    const c = e.target.closest && e.target.closest('[data-chapter]'); if (!c) { if (!(e.target.closest && e.target.closest('[data-testid=\"room-peek\"]'))) setPeek(null); return; }\n"
    "    const cid = c.getAttribute('data-chapter'); if (peek === cid) { setPeek(null); onOpen(cid); } else { setPeek(cid); try { const b = c.getBoundingClientRect(); if (b.bottom > window.innerHeight * 0.42) window.scrollBy({ top: b.top - window.innerHeight * 0.18, behavior: 'smooth' }); } catch (er) {} }   // the first tap shows what is inside (the room kept above the card); the second goes in\n  };")
rep("    else if (g.getAttribute('data-chapter')) { e.preventDefault(); onOpen(g.getAttribute('data-chapter')); }",
    "    else if (g.getAttribute('data-chapter')) { e.preventDefault(); const cid = g.getAttribute('data-chapter'); if (peek === cid) { setPeek(null); onOpen(cid); } else setPeek(cid); }")
rep("                <div style={hint}>{t('Tap a room to go in', '방을 누르면 들어가요')}</div></>",
    "                <div style={hint}>{t('Tap a room to see what is inside', '방을 누르면 안에 무엇이 있는지 보여요')}</div>\n"
    "                {peek && (() => { const k = stages.findIndex(x => x.ids.includes(peek)); return <RoomPeek id={peek} num={nums[peek]} floor={k >= 0 ? floorName(k) : ''} onGo={() => { const c = peek; setPeek(null); onOpen(c); }} onClose={() => setPeek(null)}/>; })()}</>")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
