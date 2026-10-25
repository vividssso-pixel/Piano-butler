import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
HPW = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hpw.jsx'), encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
# Build Y (the decision board's build queue, item 2): chapter 5's Workbook (pages 2-8, facing its Lesson Book) and its
# teacher's copy. The code: hpw.jsx, after the chapter's own code.
rep("""function HandPositionsLessonBook() { return <>{hpLbPages(false)}</>; }""", """function HandPositionsLessonBook() { return <>{hpLbPages(false)}</>; }""" + HPW)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
