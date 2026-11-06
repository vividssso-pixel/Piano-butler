#!/usr/bin/env python3
# Phase 415: the Lesson Book's last page ('My five checks') fills its page in every chapter -- the five rows grow
# to share the room left (her rule: fill the page, no empty bottoms); chapter 4's rows are the big ones too.
#   python3 patch415.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)
rep("""  return <div style={{display:'flex',flexDirection:'column',gap:5}}>
    <div style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'end',fontSize:11,fontWeight:800,color:BK.muted,textAlign:'center'}}>""",
    """  return <div style={{display:'flex',flexDirection:'column',gap:big ? 8 : 5,flex:big ? '1 0 auto' : undefined}}>
    <div style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'end',fontSize:11,fontWeight:800,color:BK.muted,textAlign:'center'}}>""", 'rows container grows')
rep("""    {rows.map(([pic, txt], i) => <div key={i} style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'center',border:'1px solid #ece6d8',borderRadius:10,padding:big ? '14px 10px' : '3px 8px'}}>
      <div style={{display:'flex',justifyContent:'center',zoom:big ? 1.5 : undefined}}>{pic}</div>
      <div style={{fontSize:big ? 17 : 14,fontWeight:800,color:BK.ink,lineHeight:1.35}}>{txt}</div>
      {[0, 1, 2].map(k => <span key={k} style={{width:30,height:30,border:'1.5px solid ' + BK.line,borderRadius:15,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center'}}><LbStageIcon i={k}/></span>)}""",
    """    {rows.map(([pic, txt], i) => <div key={i} style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'center',border:'1px solid #ece6d8',borderRadius:10,padding:big ? '9px 10px' : '3px 8px',flex:big ? '1 0 auto' : undefined}}>
      <div style={{display:'flex',justifyContent:'center',zoom:big ? 1.5 : undefined}}>{pic}</div>
      <div style={{fontSize:big ? 18 : 14,fontWeight:800,color:BK.ink,lineHeight:1.35}}>{txt}</div>
      {[0, 1, 2].map(k => <span key={k} style={{width:big ? 38 : 30,height:big ? 38 : 30,border:'1.5px solid ' + BK.line,borderRadius:19,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center',zoom:big ? 1.2 : undefined}}><LbStageIcon i={k}/></span>)}""", 'rows grow')
rep("""      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_sf_v1" rows={""",
    """      <LbLive still={<LbStageRows big rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_sf_v1" rows={""", 'ch4 rows big')
# The side-by-side print lost the check-up on paper (Phase 409 moved it into the Workbook, but the spread asked for the
# Workbook without its frame) and, in chapter 4, the puzzle page too. Now: the opener; each lesson page facing its
# Workbook page; any extra Workbook page (chapter 4's puzzle page) facing a blank; and the five checks facing the
# check-up on paper -- one check, two ways, side by side.
rep("""  if (framed) {   // Phase 394: the opener is page 1 (a right-hand page), each lesson page faces its workbook page, the check-up closes
    const out = [lp[0]];
    for (let k = 1; k < lp.length - 1; k++) out.push(lp[k], wp[k - 1] || blank('w' + k));
    out.push(lp[lp.length - 1]);
    return <>{out}</>;
  }""",
    """  if (framed) {   // Phase 394/415: the opener is page 1 (a right-hand page), each lesson page faces its workbook page, the checks face the paper check-up
    const wf = React.Children.toArray(WORKBOOKS[id]({ startNo: 1, frames: true }).props.children);
    const steps = lp.length - 2, paper = wf[wf.length - 1];
    const out = [lp[0]];
    for (let k = 1; k <= steps; k++) out.push(lp[k], wf[k - 1] || blank('w' + k));
    wf.slice(steps, -1).forEach((pg, j) => out.push(blank('x' + j), pg));
    out.push(lp[lp.length - 1], paper);
    return <>{out}</>;
  }""", 'spread keeps the paper check-up')

open(src, 'w', encoding='utf-8').write(s); print('patch415 ok')
