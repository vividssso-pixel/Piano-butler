#!/usr/bin/env python3
# draft build only: chapter 6's Lesson Book v1 (ll427.jsx) -> ?book=lesson&ch=ledger-lines
import sys
src, jsx = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read(); add = open(jsx, encoding='utf-8').read()
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook };"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS')
s = s.replace(a, add + "\n" + a.replace("'whole-staff': WholeStaffLessonBook };", "'whole-staff': WholeStaffLessonBook, 'ledger-lines': LedgerLessonBook };"))
open(src, 'w', encoding='utf-8').write(s); print('ll427 applied')
