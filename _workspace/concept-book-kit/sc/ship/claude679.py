import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 654 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 655 | 2026-10-25 | **Beginner is one floor (her 15:02, 'before Prelim, one floor is better, right?').** Built on row 654. The two Beginner storeys join into one floor of twelve rooms in the same order (rooms 1-6, the first-tutor stage, then 7-12, the bridge to Prelim); the house has four floors: 'FLOOR 1 · BEGINNER', 'FLOOR 2 · PRELIM – GRADE 1', 'FLOOR 3 · PRELIM – GRADE 1', 'FLOOR 4 · GRADES 2–3'. Rooms and chapter numbers unchanged; the phone house shows the floor as four rows of three. A floor of more than six rooms takes two rows of six on big screens and on the Workbook's house page; the books' small house gives it two rows, the floor's name on the first. Every 'five floors' counts the floors now (houseFloors: 'four floors' / '네 층'). **Told her:** with twelve rooms, the floor checkpoint stays one 30-question mock test, and a young beginner's milestones are the room checks; the house's 'any room first' still holds, the room numbers giving the suggested order. Files: drills.html, drills.src.html, _workspace/concept-book-kit/sc/patch679.py. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
