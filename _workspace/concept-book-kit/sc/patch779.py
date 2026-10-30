#!/usr/bin/env python3
"""Build DD (on t778 -> t779). Sohyun 2026-10-30 13:03: the Books get their own tab next to Chapters (teacher view),
instead of a section inside the Toolbox. Home · Chapters · Books · Toolbox · Practice. `?view=books` opens it; the old
`?view=toolbox&sec=books` still lands there. The Toolbox keeps its activities only.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# the tab
R("""(T ? [['home', t('Home', '홈')], ['path', t('Chapters', '챕터')], ['toolbox', t('Toolbox', '도구함')], ['practice', t('Practice', '연습')]]""",
  """(T ? [['home', t('Home', '홈')], ['path', t('Chapters', '챕터')], ...(booksUnlocked() ? [['books', t('Books', '책')]] : []), ['toolbox', t('Toolbox', '도구함')], ['practice', t('Practice', '연습')]]""")
# the route: read, write, and the page itself
R("""p.get('view') === 'toolbox' ? 'toolbox' : p.get('view') === 'students'""",
  """p.get('view') === 'books' || (p.get('view') === 'toolbox' && p.get('sec') === 'books') ? 'books' : p.get('view') === 'toolbox' ? 'toolbox' : p.get('view') === 'students'""")
R("""      else if (st.view === 'students') p.set('view', 'students');""",
  """      else if (st.view === 'students') p.set('view', 'students');
      else if (st.view === 'books' && !st.drill) p.set('view', 'books');   // Build DD""")
R("""          T && st.view === 'toolbox'
            ? <ToolboxTab""", """          T && st.view === 'books'
            ? <div className="fade-up"><PageIntro title={t('Books', '책')} text={t('The printed books (Lesson Book, Workbook, Teacher copy for every chapter), the checkpoints on paper and the paper cut-outs.', '인쇄용 책(챕터마다 레슨북, 워크북, 교사용), 종이 중간점검, 오려 쓰는 종이 교구.')}/><BooksShelf/></div>
          : T && st.view === 'toolbox'
            ? <ToolboxTab""")
R("""const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'toolbox' || (HM && st.view === 'home')) && !!st.drill;""",
  """const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'toolbox' || st.view === 'books' || (HM && st.view === 'home')) && !!st.drill;""")
R("""function jumpToChapter(id) { setFindOpen(false); update({ view: (T && (st.view === 'toolbox' || st.view === 'chapters')) ? st.view : 'path',""",
  """function jumpToChapter(id) { setFindOpen(false); update({ view: (T && (st.view === 'toolbox' || st.view === 'chapters' || st.view === 'books')) ? st.view : 'path',""")
# the Toolbox: activities only
R("""      <PageIntro title={t('Toolbox', '도구함')} text={sec === 'books' ? t('The printed books (Lesson Book, Workbook, Teacher copy for every chapter) and paper cut-outs.', '인쇄용 책(챕터마다 레슨북, 워크북, 교사용)과 오려 쓰는 종이 교구.') : t(""",
  """      <PageIntro title={t('Toolbox', '도구함')} text={t(""")
R("""      {booksOn && <div style={{display:'flex',gap:6,margin:'-6px 0 12px'}}>
        {[['tools', t('Activities', '활동')], ['books', t('Books', '책')]].map(([k, l]) => (
          <button key={k} className={'chip' + (sec === k ? ' active' : '')} style={{padding:'6px 16px',fontSize:14,fontWeight:800}} onClick={() => setSec(k)}>{l}</button>
        ))}
      </div>}
      {booksOn && sec === 'books' && <BooksShelf/>}
""", "")
R("""  const [booksOn] = useState(booksUnlocked);
  const [sec, setSec] = useState(() => { try { return booksUnlocked() && new URLSearchParams(window.location.search).get('sec') === 'books' ? 'books' : 'tools'; } catch (e) { return 'tools'; } });
""", """  const sec = 'tools';   // Build DD: the Books are their own tab now
""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
