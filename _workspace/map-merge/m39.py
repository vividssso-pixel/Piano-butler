p='drills.src.html'; s=open(p).read()
if 'm39' in s: print('already'); raise SystemExit
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)
# 1. grids never push past the page (tones p5's fifth card)
rep("  return <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',1fr)',gap}}>{children}</div>;",
    "  return <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap}}>{children}</div>;   // m39: a cell may shrink, never spill off the page")
# 2. tones: arrows keep inside their card
rep("  const bw = w * 0.6, bh = h * 0.6, T = arrow ? 26 : 3, W = whites * w + 4;",
    "  const bw = w * 0.6, bh = h * 0.6, T = arrow ? 26 : 3, W = whites * w + 4, PADX = arrow ? 16 : 0;   // m39: room for an arrow that runs past the end keys")
rep("    <svg viewBox={`0 0 ${W} ${T + h + 4}`} style={{width:'100%',display:'block'}}>\n      {arrow && (() => {",
    "    <svg viewBox={`${-PADX} 0 ${W + 2 * PADX} ${T + h + 4}`} style={{width:'100%',display:'block'}}>\n      {arrow && (() => {")
# 3. tones p2: the starting key is red or pink
rep('how="Your key is in red. Mark the key a half step up,', 'how="Your key is coloured. Mark the key a half step up,')
# 4. tones p5: the example's signs clear the EXAMPLE label
rep("<ExCell key={i} n={i + 10} ex={i === 0}><div style={{padding:'16px 4px 8px',display:'grid',justifyItems:'center',gap:10}}>\n        <div style={{fontSize:30,",
    "<ExCell key={i} n={i + 10} ex={i === 0}><div style={{padding:'24px 4px 8px',display:'grid',justifyItems:'center',gap:10}}>\n        <div style={{fontSize:27,")
# 5. note values p5: the example circles its answer
rep("    {words && <div style={{display:'flex',justifyContent:'center'}}>{nvChoose(words, ex ? nvNameEn[k] : null)}</div>}",
    "    {words && <div style={{display:'flex',justifyContent:'center'}}>{nvChoose(words, ex ? (words.includes('walk') ? (k === 'q' ? 'walk' : 'run-ning') : nvNameEn[k]) : null)}</div>}")
# 6. hand positions check-up C: middle C marked
rep("<HpKeys pos={pos} hands={h} span={[17, 37]} fingers={false} letters={false} names={false} mc={false} pale={false} lit={lit} W={7} k={1}/>",
    "<HpKeys pos={pos} hands={h} span={[17, 37]} fingers={false} letters={false} names={false} mc={true} pale={false} lit={lit} W={7} k={1}/>")
# 7. a continuation page says so (staff p7)
rep("function WbTop({ step }) {", "function WbTop({ step, cont }) {   // m39: cont, the step goes on over the page")
rep("<b style={{color:BK.coral,fontSize:10.5,fontWeight:800,...VIC_CAPS}}>{bkStepLabel(step)}</b>",
    "<b style={{color:BK.coral,fontSize:10.5,fontWeight:800,...VIC_CAPS}}>{bkStepLabel(step)}{cont ? ' · continued' : ''}</b>")
a0 = s.index("function SfWorkbook"); i1 = s.index("<WbTop step={5}/>", a0); i2 = s.index("<WbTop step={5}/>", i1 + 5)
s = s[:i2] + "<WbTop step={5} cont/>" + s[i2 + len("<WbTop step={5}/>"):]
open(p,'w').write(s); print('ok')
