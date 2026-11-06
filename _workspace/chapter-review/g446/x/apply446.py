#!/usr/bin/env python3
# draft build only: chapter 3's Lesson Book v1 (pl446book.jsx) -> ?book=lesson&ch=pulse (drills.src.html itself unchanged)
import sys
src, jsx, out = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read(); add = open(jsx, encoding='utf-8').read()
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook, 'ledger-lines': LedgerLessonBook, tones: TonesLessonBook };"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS')
s = s.replace(a, add + "\n" + a.replace("tones: TonesLessonBook };", "tones: TonesLessonBook, pulse: PulseLessonBook };"))
a = "function LbTune({ name, how, seq, icon }) {"
if s.count(a) != 1: raise SystemExit('LbTune')
s = s.replace(a, "function LbTune({ name, how, seq, icon, coral }) {   // coral (Phase 446): finger numbers in coral circles, so they never read as the count")
a = ": <span key={i} style={{width:28,height:28,borderRadius:14,background:'#fff',border:'2px solid ' + BK.ink,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14.5,fontWeight:900,color:BK.ink}}>{x}</span>)}"
if s.count(a) != 1: raise SystemExit('LbTune circle')
s = s.replace(a, ": <span key={i} style={{width:28,height:28,borderRadius:14,background:coral ? BK.coral : '#fff',border:'2px solid ' + (coral ? BK.coral : BK.ink),display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14.5,fontWeight:900,color:coral ? '#fff' : BK.ink}}>{x}</span>)}")
open(out, 'w', encoding='utf-8').write(s); print('pl446 applied')
