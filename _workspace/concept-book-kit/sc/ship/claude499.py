import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 497 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 498 | 2026-10-19 | **Circle of fifths joins the Key finder; scale keyboard labels balanced (her 09:15).** The Key finder is now five steps: sharps, flats, major and minor, the circle of fifths (tap a key: its signature, its relative minor), before a piece. The concept book gains the matching page (ten pages, TOC and five checks updated). On the scale keyboards the note name and finger number now sit evenly in the key instead of the letter hugging the black keys. Source `patch498.py`. Checked by me with screenshots (screen at 390, print EN and KO, no overflow, no console errors); the circle is the existing FifthsRing. |")
lines.insert(idx[0] + 2, "| 499 | 2026-10-19 | **'Say the order' draws the zigzag (her 09:17).** As each sharp sounds, a numbered dot appears above its key and a line joins them, so the left-right-left pattern shows; B♯ is drawn on an extra C to the right of B and E♯ on F, labelled. Flats get the same dots (their path is less regular). `TapKeyboard` got opt-in `extraC`, `trail`, `trailLabels`; nothing else changes. Source `patch499.py`. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
