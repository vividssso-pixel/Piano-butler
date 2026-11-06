#!/usr/bin/env python3
# Phase 437: chapter 7 (Tones & Semitones) -- the Lesson Book (final), on screen, the drill, the Workbook, the Teacher copy.
#   python3 apply437.py <src> <book.jsx> <app.jsx> <out>
import sys
src, book, app, out = sys.argv[1:5]
s = open(src, encoding='utf-8').read()
add = open(book, encoding='utf-8').read() + '\n' + open(app, encoding='utf-8').read()
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook, 'ledger-lines': LedgerLessonBook };"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS')
s = s.replace(a, add + "\n" + a.replace("'ledger-lines': LedgerLessonBook };", "'ledger-lines': LedgerLessonBook, tones: TonesLessonBook };"))
open(out, 'w', encoding='utf-8').write(s); print('437 applied')
