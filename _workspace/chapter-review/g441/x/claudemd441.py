#!/usr/bin/env python3
# Phase 441: CLAUDE.md -- the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ROW = """| 441 | 2026-10-12 | **Tones & Semitones: a sharp or a flat is not always a black key.** Her 15:37 on the opener ('And the black keys get their names: sharps and flats'): '샵 플랫은 하얀건반도 있을 수 있는데 ... 학생들이 샵 플랫은 검은건반 이라는 인식 심어주기 위험한데'. The book now says what the signs do, not which keys they are: opener 'two signs move a note a half step: the sharp up, the flat down' (두 기호가 음을 반 걸음 옮겨요); page 5 drops 'Now the black keys get their names' and ends 'But a sharp or a flat is not always a black key: a half step up from E is the white key F, so E sharp is the same key as F'; REMEMBER '♯ up a half step, ♭ down a half step -- to the very next key, black or white'. The p5 widget (TnSharpFlat) now has two octaves and lands on white keys too: E♯ -> 'the white key F: the same key. A sharp is not always a black key.', C♭ -> B; only the keyboard's two ends fall off. Teacher copy: 'writing and drilling E♯ = F, B♯ = C, F♭ = E and C♭ = B' waits for the scales chapters (the book says it once); watch adds 'Thinking every sharp or flat is a black key (E♯ is the white key F)'. Drills, Workbook and staff items unchanged (they still use black keys only). Checks: tn441test 16/16 (new P1-P4 widget, B4 wording), lbcheck tones 0/0 (en, ko), wbcheck tones pass. |
"""
m = re.search(r'^\| 440 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 440')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 441')
