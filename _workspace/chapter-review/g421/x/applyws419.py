#!/usr/bin/env python3
# draft build only: chapter 5's Lesson Book v1 (ws419.jsx) -> ?book=lesson&ch=whole-staff
import sys
src, jsx = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read(); add = open(jsx, encoding='utf-8').read()
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook };"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS')
s = s.replace(a, add + "\n" + a.replace("staff: StaffLessonBook };", "staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook };"))
open(src, 'w', encoding='utf-8').write(s); print('ws419 applied')
