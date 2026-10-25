import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 663 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 664 | 2026-10-26 | **Same-name twins show once (the decision board's build queue, item 3; the curriculum plan's decision 5, 'the duplicate pairs become one each').** Built on row 663. Three rooms listed a lesson twice under one name; the chapter's own step (the one its Lesson Book uses) stays, the older twin is hidden from the lists (hidden: true, out of CHAPTER_TOOL_ORDER) but still opens from an old link or a teacher's saved set: Loud & soft 'Tie or slur?' keeps sdy-tie (tie-slur hidden); Pitch 'Big is low, small is high' keeps spr-big (size-pitch hidden) and 'Who plays where?' keeps spr-range (range-chart hidden). The 'stuck on legato/staccato' helper and the skill 'Repeats, D.C. and ties' now point at sdy-tie. The plan's third pair (Metronome) no longer exists as a twin: the Toolbox's metronome and Tempo's lesson 'The metronome' do different jobs (a full practice tool and a lesson step). Files: drills.html, drills.src.html, _workspace/concept-book-kit/sc/patch688.py. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
