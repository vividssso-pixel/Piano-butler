import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 566 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 567 | 2026-10-19 | **Accidentals drill rebuilt to match the ten lessons (agreed plan, 22:18).** The `clock` drill's chips are renumbered and renamed like the Home lessons: 1–2 Half or whole?, 1 Play a half step, 1 White neighbours, 2 Play a whole step, 3–5 Name the sign, 3–4 Find the key, 3–4 On the staff, 5 The natural, 6 Until the bar line, 6 Its own line or space, 6 Which sign?, 7 Read the bar, 8 Black key names, 8 Two names, 9 Double signs (new), 10 Coral note (key signature of one sharp or flat). More practice: Listen, Bass clef, Accidentals in a key. New question kind `dbl` (`genDblQuestion`, `DblQuestion`): a double-sharp or double-flat name in large type, tap its key; feedback sits under the question like the other levels ('Not quite: it was F𝄫 = E♭', the right key lit); answers from her `ALL_NAMES` table. Level numbers `n` are renumbered 21–39 (the drill is new, no saved progress to keep). Source `patch572.py`; every chip opened in English and Korean with no errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
