#!/usr/bin/env python3
# draft build only: chapter 8's Lesson Book v1 (tsbook461.jsx) -> ?book=lesson&ch=time-signatures (drills.src.html itself unchanged)
import sys
src, jsx, out = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read(); add = open(jsx, encoding='utf-8').read()
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook, 'ledger-lines': LedgerLessonBook, tones: TonesLessonBook, pulse: PulseLessonBook, 'note-values': NotesRestsLessonBook };"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS')
s = s.replace(a, add + "\n" + a.replace("'note-values': NotesRestsLessonBook };", "'note-values': NotesRestsLessonBook, 'time-signatures': TimeSignaturesLessonBook };"))
open(out, 'w', encoding='utf-8').write(s); print('ts461 draft applied')
