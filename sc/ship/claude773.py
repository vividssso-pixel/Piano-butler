import sys, io
md, hist = sys.argv[1], sys.argv[2]   # CLAUDE.md, CLAUDE-history.md
s = io.open(md, encoding='utf-8').read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
R("| **Git** | Pushed up to CU (`b71506b`) on 2026-10-29. CV (`0766ad5`), the CLAUDE.md tidy (`ee9c28e`) and CW committed, waiting for her push. |",
  "| **Git** | Pushed up to CW (`93fc0e3`) on 2026-10-29. CX committed, waiting for her push. |")
R("1. The Beginner floor's two checkpoints on paper (bespoke paper items in the books' style, with a teacher-copy key).\n2. The Prelim floor's Lesson Books, fun first, once the trial has started.",
  "1. The Prelim floor's Lesson Books, fun first, once the trial has started.")
a = s.index("| **drills.html** (the Piano Butler drills, unlisted) |"); b = s.index(" |\n", a)
s = s[:b] + " The Beginner floor's two checkpoints are also on paper, with a teacher key: `?book=check&floor=0a|0b` and `?book=checkkey&floor=0a|0b`, on the Books shelf after chapters 7 and 13 (CX)." + s[b:]
io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(h) if l.startswith('| 742 |')]
assert len(idx) == 1 and not any(l.startswith('| 743 |') for l in h)
h[idx[0] + 1:idx[0] + 1] = ["| 743 | 2026-10-29 | **The Beginner floor's checkpoints on paper (Build CX; the board's next step after CV and CW).** `?book=check&floor=0a|0b`: Beginner checkpoint 1 (chapters 1 to 7, four pages) and 2 (chapters 8 to 13, three pages): two parts of each room's check-up on paper (the Workbook's last page), each room under its chapter number and name, the parts keeping their letters and item numbers; title page 'Show what you remember!', name and date; the last page lists the rooms to visit again (the teacher ticks) and a CHECKPOINT DONE! stamp. Ear Prep has no Workbook, so two listening parts the teacher plays (turtle, middle C or bird; same or different). `?book=checkkey&floor=…`: one page, each room's answers taken from its own Teacher copy (TcBlock in key mode, through CkpKeyCtx and a portal, filtered by the parts' letters), and 'Any wrong: visit again. A -> step 1 (Lesson Book page 2)'. Fresh items: the route is read first (const CKP at the top of the app); withSeed salts every seed with the checkpoint, and the fixed check-up data of the parts used gets new items on that route only (PH_FILL_CHK, fsWorkbook wh, NN_CHK_WORDS, sfChkData tr/ba, wsChkData q/k, PL_CHK, HP_WB.chk, NV_CHK, SDY_CHK, SSK_CHK, TS_CHK, TN_CHK). bkSec and tcAns carry data-sec; WbPage takes head and left. The Books shelf shows each checkpoint after the last room it checks. Parts per room: posture A E, keyboard patterns C D, pulse B D, note names A E, hand positions A C, ear prep A B, note values A C, dynamics A D, staff C D, steps and skips B C, line and space names B C, time signatures A B, tones A D. Tests: ckp773.js (pages, overflow, two parts a room, the key's answers), shelf773.js, and the usual sweeps and regression. |"]
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h))
print('CLAUDE.md and CLAUDE-history.md updated (row 743)')
