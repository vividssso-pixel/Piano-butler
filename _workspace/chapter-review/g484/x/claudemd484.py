#!/usr/bin/env python3
# Phase 484: CLAUDE.md: rule 16 (the foundation: five areas, concept first), rule 11 (more scales waits), the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def one(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('not found once: ' + a[:60])
    s = s.replace(a, b)
one("page 6 pop (verse, chorus, bridge; C G Am F). Next more scales.",
    "page 6 pop (verse, chorus, bridge; C G Am F). More scales waits: the foundation (rule 16) folds it into Scales and keys.")
RULE = """16. **The foundation: five areas, concept first** (her 2026-10-17 21:09 '스케일 하나 둘 설명하는게 아니라 개념알려주고 쫙
   다 적용시킬 수 있게 ... 나는 좀 거꾸로 하고싶어서'; 21:13 '이게 pitch 영역이면 그것만, 리듬 영역이면 그것만, 터치
   아티큘레이션, 테크닉에 스케일 코드 이런식으로'; 21:20 '시험지도는 당장 만들 필요는 없고 바탕 정리를 해놓는게 우선';
   21:32 '그렇게 하자. 이렇게 가는게 맞아 내 레슨 성격에 더 맞아'). Everything sits in five areas, each holding only its own
   kind of thing, 13 concepts in all: Pitch (keys and staff; semitones and accidentals; intervals; scales and keys;
   chords), Rhythm (beat and time), Touch and expression (touch; tempo and character), Technique (posture and hands; positions
   and finger numbers; playing scales and chords), Pieces (reading tunes; melody and form). The stories of music (the piano,
   composers, styles) and the practice helpers sit beside the five, not in them. Each concept is taught whole, once: one
   rule and the whole of it at once (all twelve major scales from one pattern, not C, then G, then F), then practised
   in steps (First, Then, Further, Later) that differ by student. Scales and chords are explained in Pitch and played in
   Technique. The Toolbox is the backbone: since Phase 484 `TOOL_AREAS`, `TOOL_CATS` (the 15 groups) and `TOOL_CONCEPT`
   put every tool under one concept, and tools that do the same job stay side by side until she chooses which to keep.
   A Lesson Book becomes a short concept book (the rule, the whole map, how to use the tools, a check); the Workbook and
   the drill follow the practice steps. Exams (AMEB first, then ABRSM) are laid over the foundation later, as routes
   through it; nothing is built for an exam yet. The plan and the inventory of every lesson step, Workbook page, drill
   level and tool under its concept: https://claude.ai/artifact/V29Y63iAxpApaCz9tx9s14. Order: the Toolbox grouped
   (Phase 484), then Scales and keys rebuilt as the model concept book, then the other concepts one by one, then the
   exams. The house of five levels (rule 10) and the 27 chapters stay as they are for now.
"""
one("\n\n## Verified Piece Counts (2026 Syllabus)", "\n" + RULE + "\n## Verified Piece Counts (2026 Syllabus)")
ROW = open(sys.argv[2], encoding='utf-8').read()
m = re.search(r'^\| 483 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 483')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: rule 16, rule 11, log row 484')
