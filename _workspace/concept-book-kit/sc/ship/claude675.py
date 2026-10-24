import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 650 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 651 | 2026-10-24 | **Three kinds of minor: Your turn in ten minor keys (her question 11:34, 'why only D?').** Built on row 650. The lesson's whole picture and one-by-one steps stay on D minor (one flat, so the one or two changed notes are easy to compare). Your turn now has key buttons above the form buttons: C, C♯, D, E, F, F♯, G, A, B♭, B minor (from C up; D first). The keyboard, the note names, the staff with that key's own key signature (the relative major's) and every line follow the key: notes the key signature changes in green, the raised 6th and 7th as coral accidentals beside the notes, with ♮ where the key signature has a flat (e.g. F harmonic minor's E♮, D melodic minor's B♮). Checked by playing every key in every form up and down, English and Korean. **Left out for now: G♯ minor and D♯ minor**, whose raised 7th is a double sharp (F𝄪, C𝄪) that the staff cannot draw yet; say if you want them (a double-sharp sign on the staff). Files: drills.html, drills.src.html, _workspace/concept-book-kit/sc/patch675.py. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
