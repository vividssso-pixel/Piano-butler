#!/usr/bin/env python3
# Phase 458: CLAUDE.md: the log row; Book rules 7, 8 and 11.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:60]))
    s = s.replace(a, b)
rep("7. **Balance and reading, checked before she sees anything.**", "7. **Balance and reading, checked before she sees anything.** Every explanation short and plain, nothing extra (her 2026-10-13 20:45 '다 심플하게 설명해줘 군더더기 없이').")
rep("8. **Words and cast.**", "8. **Words and cast.** A second name is given as 'its other name is ...', never whose books use it (her 2026-10-13 20:45 'american 북은 이렇게 부른다는 내용은 빼고 다른 이름으로는 이렇게 부른다'): 'Its other name is a quarter note.'")
rep("Next: Level 1's note-values (draft v1, Phase 457, waiting for her answers to G1-G3 and B1-B13);", "Next: Level 1's note-values (draft v2, Phase 458, waiting for her answers to B4-B13 and G1-G3);")
ROW = """| 458 | 2026-10-13 | **Chapter 5 draft v2; 'its other name'; short and plain.** Her 20:45 on the chapter 5 draft: 'bird turtle 빼고 walk, running 으로 충분' (B2 yes, B3 no); 'american 북은 이렇게 부른다는 내용은 빼고 다른 이름으로는 이렇게 부른다' (B1, and everywhere: Book rule 8); '다 심플하게 설명해줘 군더더기 없이' (Book rule 7); and the minim rest and semibreve rest must say which line. Draft v2 (nvbook458.jsx in _workspace/chapter-review/g458/x; drills.src.html unchanged for chapter 5): walk under each crotchet and run-ning under each quaver pair; every page's words and tasks cut short ('A crotchet has a filled head and a stem. It lasts one beat. Walk: one step on each beat. Its other name is a quarter note.'); page 6 draws the five lines numbered from the bottom, the minim rest on the middle line (3) and the semibreve rest hanging from line 4, each line coral. Claude outputs/Chapter-05-Notes-Rests-draft-v2.pdf (8 pages: what changed, B4-B13 and G1-G3 still open, the pages). Chapter 11 (patch458.py): 'Its other name is a semitone / a tone', no Australian, British or American books, in the Lesson Book (pages 2 and 3, en and ko), the two old tone tool tips, the Teacher copy and the guide page (tones-and-semitones.html, --final). Checks: lbcheck note-values and tones 0/0 en and ko, tn444test, every picture inside its frame. |
"""
m = re.search(r'^\| 457 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 457')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 458, rules 7, 8, 11')
