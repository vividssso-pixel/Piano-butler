import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 579 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 580 | 2026-10-20 | **Warm, always-guiding feedback (her call, 13:00).** Every wrong-answer line in the Accidentals and Scales lessons that began \"Not that key.\" / \"Not that one.\" / \"Not quite.\" / \"Not a thumb key.\" now begins \"Almost!\" and keeps its pointer to the right answer (Korean: \"거의 다 왔어요!\"); the \"standard or different?\" right answer says \"Yes, well done!\" (\"잘했어요!\"). No other behaviour changed. Wording is for adults and children alike; Korean unverified. Built as `t588`. Checked: the hands-together round still completes in English and Korean. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
