#!/usr/bin/env python3
# Phase 409 (Sohyun 2026-10-09 23:56):
#   1. the Workbook's copy of the book's opener goes ('워크북 이 페이지는 필요없는거아냐?') -- every chapter
#   2. no content twice ('같은 내용 다 빼줘'): the opener's ONLINE box keeps only the QR code; the paper check-up
#      lives only in the Workbook (chapters 1-3 too) -- the book's last page keeps the at-the-piano checks
#   3. chapter 4's Workbook redrawn with BIG staves -- one long staff per exercise, boxes under the notes
#   python3 patch409.py <drills.src.html> <sf409.wb.jsx>
import sys, re
src, wbsrc = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read(); wb = open(wbsrc, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# 1+2a. lbFramed: no opener; the paper check-up becomes the Workbook's own last page (chapters 1-3)
rep("""function lbFramed(id, pages, startNo) {
  const lb = LB_PAGE_FNS[id](false);
  return [React.cloneElement(lb[0], { key: 'frame-open', no: startNo, book: 'Workbook' }), ...pages, React.cloneElement(lb[lb.length - 1], { key: 'frame-check', no: startNo + 1 + pages.length, book: 'Workbook' })];
}""", """// Phase 409: the Workbook no longer repeats the book's opener; its last page is the check-up on paper (the book's
// last page keeps only the at-the-piano checks). Chapter 4 builds its own check-up page.
const LB_PAPER_PAGES = { 'posture-hands': () => <PhPaperCheck/>, 'first-steps': () => <FsPaperCheck/>, 'note-names': () => <NnPaperCheck/> };
function lbFramed(id, pages, startNo) {
  const paper = LB_PAPER_PAGES[id];
  return paper ? [...pages, <WbPage key="wb-paper" no={startNo + 1 + pages.length} chId={id}>{paper()}</WbPage>] : pages;
}""", 'lbFramed')
for comp in ['PhPaperCheck', 'FsPaperCheck', 'NnPaperCheck']:
    rep("      <LbOnly print><%s/></LbOnly>\n" % comp, "", 'book paper ' + comp)
rep("On paper: do the check-up below.'", "The check-up on paper is in the Workbook.'", 'say en', n=3)
rep("종이에서: 아래 점검을 풀어요.'", "종이 점검은 워크북에 있어요.'", 'say ko', n=3)
rep("do the paper part on the same page.'", "do the paper check-up in the Workbook.'", 'teacher en')


# 2c. the book's last page without the paper part: the five checks print bigger to fill it (chapters 1-3)
rep("""function LbStageRows({ rows }) {
  const S = lbStages(), cols = '96px 1fr repeat(3, 62px)';""", """function LbStageRows({ rows, big }) {   // Phase 409: big = the check page's rows fill the page (no paper part below)
  const S = lbStages(), cols = big ? '140px 1fr repeat(3, 70px)' : '96px 1fr repeat(3, 62px)';""", 'stage rows big')
rep("""    {rows.map(([pic, txt], i) => <div key={i} style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'center',border:'1px solid #ece6d8',borderRadius:10,padding:'3px 8px'}}>
      <div style={{display:'flex',justifyContent:'center'}}>{pic}</div>
      <div style={{fontSize:14,fontWeight:800,color:BK.ink}}>{txt}</div>""", """    {rows.map(([pic, txt], i) => <div key={i} style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'center',border:'1px solid #ece6d8',borderRadius:10,padding:big ? '14px 10px' : '3px 8px'}}>
      <div style={{display:'flex',justifyContent:'center',zoom:big ? 1.5 : undefined}}>{pic}</div>
      <div style={{fontSize:big ? 17 : 14,fontWeight:800,color:BK.ink,lineHeight:1.35}}>{txt}</div>""", 'stage rows big body')


for key in ['pb_five_fs_v1', 'pb_five_nn_v1']:
    seg = '<LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="' + key + '"'
    rep(seg, seg.replace('<LbStageRows rows=', '<LbStageRows big rows='), 'big ' + key)
rep("<LbLive still={<LbStageRows rows={checks5.map(", "<LbLive still={<LbStageRows big rows={checks5.map(", 'big ph')

# 2b. the ONLINE box: the QR code only (the level list repeated the drill)
i = s.index("function LbDrillStrip({ id }) {"); j = s.index("// Phase 394: the check-up page's paper part", i)
s = s[:i] + """function LbDrillStrip({ id }) {   // Phase 409: only the code -- the levels live in the drill itself
  return (
    <div data-lb-drill style={{display:'flex',justifyContent:'flex-end',alignItems:'center',gap:8,marginTop:'auto'}}>
      <span style={{fontSize:10.5,color:BK.muted}}>{t('online', '온라인')}</span>
      <div style={{padding:4,border:'1.5px solid ' + BK.line,borderRadius:8,background:'#fff',lineHeight:0}}><QR url={bkLink('drill=' + id + '&tab=drill&level=1&lock=1')} size={64}/></div>
    </div>
  );
}
""" + s[j:]

# 3. chapter 4's Workbook, its check-up and the Teacher copy: replaced whole
i = s.index("// ─── the Workbook (Phase 405): one page facing each Lesson Book page, in the two inks ───")
j = s.index("const LESSON_BOOKS = {", i)
old = s[i:j]
assert 'function SfTeacher()' in old and 'function SfWorkbook(' in old
s = s[:i] + wb + "\n" + s[j:]
# the old SfPaperCheck (book-side, above) goes -- the new one lives with the Workbook
i = s.index("function SfPaperCheck() {\n  const C = useMemo(() => sfChkData(), [LANG]);\n  const cell =")
j = s.index("\n}\n", i) + 3
s = s[:i] + s[j:]

open(src, 'w', encoding='utf-8').write(s); print('patch409 ok')
