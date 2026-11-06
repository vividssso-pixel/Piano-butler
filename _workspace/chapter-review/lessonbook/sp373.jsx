// ─── Phase 373: the Lesson Book and the Workbook side by side (?book=spread&ch=<chapter>) ───
// For a chapter that has its own Lesson Book pages: a cover, then each Lesson Book page followed by its Workbook page.
// Printed double-sided, the cover is page 1 (a right-hand page), so every lesson page lands on the left and its
// workbook page faces it on the right -- both carry the same page number.
function SpreadCover({ id }) {
  return (
    <section className="bk-page" data-spread-cover={id}>
      <div style={{flex:1,display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',gap:18,textAlign:'center'}}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>{'CHAPTER ' + bkChapterNo(id)}</div>
        <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:46,fontWeight:900,color:BK.ink,lineHeight:1.05}}>{bkChapterName(id)}</div>
        <div style={{fontSize:16,fontWeight:800,color:BK.muted}}>Lesson Book <span style={{color:BK.coral}}>+</span> Workbook</div>
        <PbArt name="rabbit" h={300}/>
        <div style={{maxWidth:420,fontSize:13,color:BK.ink,lineHeight:1.55,border:'1.5px dashed ' + BK.line,borderRadius:12,padding:'10px 16px'}}>
          <b>Print double-sided</b> (flip on the long edge). Each Lesson Book page is on the left and its Workbook page faces it on the right, with the same page number. Read the left page, then do the right one.
        </div>
      </div>
      <div style={{textAlign:'center',fontSize:10.5,color:BK.muted,fontWeight:700}}>Piano Butler</div>
    </section>
  );
}
function SpreadBook({ id }) {
  const lesson = LESSON_BOOKS[id](), work = WORKBOOKS[id]({ startNo: 1 });
  const lp = React.Children.toArray(lesson.props.children), wp = React.Children.toArray(work.props.children);
  const blank = (k) => <section key={'blank' + k} className="bk-page" data-spread-blank/>;
  const out = [<SpreadCover key="cover" id={id}/>];
  for (let k = 0; k < Math.max(lp.length, wp.length); k++) out.push(lp[k] || blank('l' + k), wp[k] || blank('w' + k));
  return <>{out}</>;
}
