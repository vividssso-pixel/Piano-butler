import sys
p = sys.argv[1]
txt = open(p, encoding='utf-8').read()
lines = txt.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 593 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 594 | 2026-10-20 | **Coming down in the fingering lessons, a clearer half-step question, and a standing reminder.** Lessons 4–7 (white keys and black keys, each hand) now have the ▶ Up and down animation on their whole-scale screens: the keys light one at a time with the finger numbers, and coming down shows the same fingers in reverse with the direction tag and the line \"Coming down: the same fingers, in reverse.\" The drill \"Where is the half step?\" showed two half steps on the keys (3–4 and 7–8) but offered only one; its question now reads \"Which of these pairs is a half step?\". New section \"Reminder: rebuild the books on the new Scales concept\" added above the Book rules. Built by `patch603.py` (`t607`). Checked in English and Korean, no console errors. Local commit only, not pushed. |")
txt = '\n'.join(lines)
marker = "## Book rules -- Sohyun's decisions for the Lesson Book, Workbook and Teacher copy"
assert txt.count(marker) == 1
rem = """## Reminder: rebuild the books on the new Scales concept (Sohyun, 2026-10-20)

Sohyun's plan: first finish the Scales concept (`p-scale`, 11 lessons + drill) in drills.html and arrange it on Home one lesson at a time; **then rebuild the Lesson Book, Workbook, Teacher copy, chapters and Toolbox to match it.** Remind her of this when the Scales work is finished, and do not rebuild the books before she says the lessons are final.

What the books must follow (the rules the lessons now carry):
- The eleven lessons in order: 1 the shape (whole and half steps), 2 the same pattern from any note, 3 degrees, 4 white keys right hand, 5 white keys left hand, 6 black keys right hand, 7 black keys left hand, 8 both hands together (1, 2 and 4 octaves), 9 all twelve keys, 10 the chromatic scale (fingering), 11 three kinds of minor (D minor).
- One focus per screen; the whole picture first, then one at a time, then she does it herself. Keyboard first; the staff comes after, on request (a "Write it on the staff" button), never suddenly.
- Staff colours: notes that come from the key signature are green, accidentals (the raised 7th, the raised 6th and 7th of the melodic minor) are coral. Say plainly that accidentals are not part of the key signature, that the natural minor follows the key signature, and that the melodic minor coming down returns to it.
- Up and down: her turns go up and then down; show the way up as a pattern, then clear the colours and come down with a direction tag. Fingering coming down is the same fingers in reverse.
- Feedback: when wrong, say plainly it is wrong and always give a guide to the right answer (no "Almost!").
- Black-key buttons show both names (sharp above, flat below), like the keyboard.
- Palette: navy and coral on cream; green only for "from the key signature" and "correct".
- Still to do around it: curriculum artifact (still Phase 485), old half-step / whole-step lessons to be re-hung as recaps, old tools (ChromaticScale, MinorFormsCard and others) are deleted only after her decision.

"""
txt = txt.replace(marker, rem + marker)
open(p, 'w', encoding='utf-8').write(txt); print('ok')
