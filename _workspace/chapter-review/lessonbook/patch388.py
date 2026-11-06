# Phase 388: chapter 2 Workbook + Teacher copy follow the Lesson Book page by page; "small house" everywhere.
# Run from the repo root: python3 _workspace/chapter-review/lessonbook/patch388.py
import os
p = 'drills.src.html'
s = open(p, encoding='utf-8').read()
here = os.path.dirname(os.path.abspath(__file__))
new = open(os.path.join(here, 'wb388.jsx'), encoding='utf-8').read()
def span(name):
    i = s.index('function ' + name + '(')
    j = s.index('\n}\n', i) + 3
    return i, j
# remove the four old definitions, then insert the new block where fsWorkbook was
i, j = span('fsWorkbook'); s = s[:i] + '/*FS388*/' + s[j:]
for name in ['fsConcepts', 'FirstStepsWorkbook', 'FirstStepsTeacher']:
    i, j = span(name); s = s[:i] + s[j:]
assert s.count('/*FS388*/') == 1
s = s.replace('/*FS388*/', new)
# A1: small house everywhere (labels, words, comments)
n = s.count('little house')
s = s.replace('little house', 'small house')
open(p, 'w', encoding='utf-8').write(s)
print('patch 388 ok; little->small:', n)
