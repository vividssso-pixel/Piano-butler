#!/usr/bin/env python3
# Phase 433 in CLAUDE.md: Book rules 8 and 9 -- the butler is the rabbit; the Phase row.   python3 claudemd433.py <CLAUDE.md>
import sys
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('CLAUDE.md: %r found %d' % (a[:70], s.count(a)))
    s = s.replace(a, b)
rep("""   the butler is a FOX and appears only as his oval portrait with a coral bow tie (the REMEMBER band, the map's Lodge,
   the welcomes) -- never as a full figure in a picture ('그냥 초상화에만 넣자'); the rabbit is gone; frames and props are straight;""",
    """   the butler is the RABBIT (Phase 433, her 2026-10-12 08:34 '토끼로 바꿔줘 마스코트' -- after the fox of Phases 424-432 and
   four new concepts she turned down) and appears only as his oval portrait, centred in the oval, with a coral bow tie
   (the REMEMBER band, the map's hall, the welcomes) -- never as a full figure in a picture ('그냥 초상화에만 넣자'); frames and props are straight;""")
rep("""REMEMBER as the chair rail with the fox's
   portrait""", """REMEMBER as the chair rail with the butler's
   portrait""")
rep("""the hall at the foot (the fox's portrait, a pedimented front door)""", """the hall at the foot (the rabbit butler's portrait, a pedimented front door)""")
if '| 433 | 2026-10-12 |' in s: raise SystemExit('CLAUDE.md: row 433 already there')
row = """| 433 | 2026-10-12 | **The butler is the rabbit again.** Her 08:34 '아 그리고 토끼로 바꿔줘 마스코트' -- the decision she held over from 00:55 ('내일 결정하자'), after fox samples (front, profile, E3/F1), a dog, a penguin, bow-tie-only marks and four new concepts (engraved, bow-tie bunny, monocle gentleman, seal) that she turned down at 01:00 ('디자인 다 맘에 안드는데'). The rabbit she had before, centred in his oval (cast/fox429/rabbit430.py: translate(12.7 22) scale(0.9), the suit at x 97, the bow tie at 97,170): VIC_CAMEO now holds him, so the REMEMBER band of every book, the map's hall and the welcomes all show the rabbit; no 'fox' left in drills.src.html. Guides' front page: the house's hall (house-wide/-tall.svg, lessons/index.html rebuilt) and its sharing picture lessons/img/house.jpg. Book rules 8 and 9 say rabbit. Checks: ll431test 24/24, ws419 45/45, lbcheck chapters 1-6 0 overflow en/ko; the portrait looked at in the REMEMBER band and the hall. |
"""
i = s.index('| 432 | 2026-10-12 |'); j = s.index('\n', i) + 1
s = s[:j] + row + s[j:]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md ok')
