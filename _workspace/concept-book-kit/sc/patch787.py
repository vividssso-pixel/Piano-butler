#!/usr/bin/env python3
"""Build DL (on t786 -> t787; her 14:57 'a room of their own for the cut-out printables, apart from the Books, so they can be
shown later as free printables'). A Printables tab in the teacher view, next to Books (Home · Chapters · Books · Printables ·
Toolbox · Practice), at ?view=printables: one sheet, each cut-out set as a card with its name, its chapter and floor, what it
is for, its pages, and Print. The Books tab keeps the books and the checkpoints only; the opener's note says 'Printables'.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# the view
R("""p.get('view') === 'books' || (p.get('view') === 'toolbox' && p.get('sec') === 'books') ? 'books' :""",
  """p.get('view') === 'books' || (p.get('view') === 'toolbox' && p.get('sec') === 'books') ? 'books' : p.get('view') === 'printables' ? 'printables' :""")
R("""  const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'toolbox' || st.view === 'books' || (HM && st.view === 'home')) && !!st.drill;""",
  """  const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'toolbox' || st.view === 'books' || st.view === 'printables' || (HM && st.view === 'home')) && !!st.drill;""")
R("""      else if (st.view === 'books' && !st.drill) p.set('view', 'books');   // Build DD""",
  """      else if (st.view === 'books' && !st.drill) p.set('view', 'books');   // Build DD
      else if (st.view === 'printables' && !st.drill) p.set('view', 'printables');   // Build DL""")
R("""  function jumpToChapter(id) { setFindOpen(false); update({ view: (T && (st.view === 'toolbox' || st.view === 'chapters' || st.view === 'books')) ? st.view : 'path'""",
  """  function jumpToChapter(id) { setFindOpen(false); update({ view: (T && (st.view === 'toolbox' || st.view === 'chapters' || st.view === 'books' || st.view === 'printables')) ? st.view : 'path'""")
R("""...(booksUnlocked() ? [['books', t('Books', '책')]] : []), ['toolbox', t('Toolbox', '도구함')]""",
  """...(booksUnlocked() ? [['books', t('Books', '책')], ['printables', t('Printables', '교구')]] : []), ['toolbox', t('Toolbox', '도구함')]""")
R("""          T && st.view === 'books'
            ? <div className="fade-up"><PageIntro title={t('Books', '책')} text={t('The printed books (Lesson Book, Workbook, Teacher copy for every chapter), the checkpoints on paper and the paper cut-outs.', '인쇄용 책(챕터마다 레슨북, 워크북, 교사용), 종이 중간점검, 오려 쓰는 종이 교구.')}/>""",
  """          T && st.view === 'printables'
            ? <div className="fade-up"><PageIntro title={t('Printables', '교구')} text={t('Paper tools to print, cut out and play with at the lesson table. Each set is a few A4 pages with a Try this box.', '인쇄해서 오려 쓰는 종이 교구. 세트마다 A4 몇 장과 해 보기 상자가 있어요.')}/><PrintablesShelf onChapter={jumpToChapter}/></div>
          : T && st.view === 'books'
            ? <div className="fade-up"><PageIntro title={t('Books', '책')} text={t('The printed books (Lesson Book, Workbook, Teacher copy for every chapter) and the checkpoints on paper.', '인쇄용 책(챕터마다 레슨북, 워크북, 교사용)과 종이 중간점검.')}/>""")

# the Books shelf loses its cut-outs section
i = s.index("""      <div className="card" style={{marginBottom:10,padding:'8px 12px'}}>
        <div style={{fontSize:11.5,fontWeight:900,color:KIND.cutouts.col,letterSpacing:.4,marginBottom:2}}>{t('CUT-OUTS · PRINT, CUT AND PLAY'""")
j = s.index("""        <div style={{display:'flex',gap:6,flexWrap:'wrap',marginTop:6}}>{wholeBtn('cutouts', 'all', t('All Cut-outs', '교구 전체'))}</div>
      </div>
""", i)
s = s[:i] + s[j + len("""        <div style={{display:'flex',gap:6,flexWrap:'wrap',marginTop:6}}>{wholeBtn('cutouts', 'all', t('All Cut-outs', '교구 전체'))}</div>
      </div>
"""):]

# the shelf of printables, next to the Books shelf
R("""function BooksShelf() {""", """// Build DL: the Printables shelf (her 14:57). One sheet: a card per cut-out set, in the map's order. Minimal, navy and coral:
// the name, the chapter and its floor, one line on what it is for, the pages, and Print (the paper layout in a new tab).
function PrintablesShelf({ onChapter }) {
  const href = (id) => '?book=cutouts&ch=' + id + '&lang=en';
  const floorOf = (ch) => { const k = STAGES.findIndex(st => st.ids.includes(ch)); return k < 0 ? '' : floorName(k); };
  return (
    <div>
      <div className="card" style={{marginBottom:10,padding:'10px 12px',display:'flex',alignItems:'center',gap:10,flexWrap:'wrap'}}>
        <div style={{flex:'1 1 220px',fontSize:13,color:'var(--muted)',lineHeight:1.5}}>{t('Flashcards are two-sided: print the fronts page, then the backs page on the other side (flip on the long edge). Card or thick paper cuts best. The sets are in English.', '카드는 양면이에요: 앞면 쪽을 인쇄하고 뒷면 쪽을 그 뒤에(긴 쪽으로 뒤집어서). 두꺼운 종이가 잘 잘려요. 세트는 영어예요.')}</div>
        <a href={href('all')} target="_blank" rel="noopener" className="chip" style={{textDecoration:'none',fontWeight:800}}>{t('Print all sets', '전체 인쇄')}</a>
      </div>
      <div data-testid="printables-shelf" style={{display:'grid',gridTemplateColumns:'repeat(auto-fill, minmax(230px, 1fr))',gap:10}}>
        {CUTOUT_LIST.slice().sort((a, b) => (a.ch ? bkChapterNo(a.ch) : 999) - (b.ch ? bkChapterNo(b.ch) : 999)).map(c => (
          <div key={c.id} className="card" data-printable={c.id} style={{padding:'10px 12px',display:'flex',flexDirection:'column',gap:4}}>
            <div style={{display:'flex',alignItems:'center',gap:6}}><CutScissors size={14}/><span style={{fontSize:15,fontWeight:900,color:'var(--navy)',lineHeight:1.2}}>{c.name}</span></div>
            <div style={{fontSize:12,color:'var(--muted)',fontWeight:700}}>{c.ch ? <>{t('Chapter ', '') + bkChapterNo(c.ch) + (LANG === 'ko' ? '장' : '')} · {floorOf(c.ch)} · <button className="linkish" onClick={() => onChapter(c.ch)} style={{background:'none',border:'none',padding:0,font:'inherit',color:'var(--navy)',cursor:'pointer',textDecoration:'underline'}}>{bkChapterName(c.ch)}</button></> : t('Any chapter', '어느 챕터든')}</div>
            <div style={{fontSize:13,color:'var(--ink)',lineHeight:1.45}}>{c.blurb}</div>
            <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,marginTop:4}}>
              <span style={{fontSize:11.5,color:'var(--muted)'}}>{c.pages} {t(c.pages === 1 ? 'page' : 'pages', '쪽')}</span>
              <a href={href(c.id)} target="_blank" rel="noopener" style={{fontSize:12.5,fontWeight:800,color:'var(--navy)',border:'1.5px solid var(--navy)',borderRadius:8,padding:'4px 12px',textDecoration:'none',background:'#fff'}}>{t('Print', '인쇄')}</a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
function BooksShelf() {""")
R("""          <span style={{color:BK.muted,fontSize:11.5}}>Print them from Books, Cut-outs in the app.</span>""",
  """          <span style={{color:BK.muted,fontSize:11.5}}>Print them from Printables in the app.</span>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
