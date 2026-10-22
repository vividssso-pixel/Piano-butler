import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 632 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 633 | 2026-10-22 | **Home concepts now share one shape (her 14:45-14:50 question).** Every Home concept and every Keys and staff group shows lessons, then one navy 'Questions →' button directly under them (Scales, Key signatures and Sharps/flats had a bottom 'Start the drill' button; Keys and staff group 1 had two). The Keyboard patterns drill ('first-steps') now carries the note-name levels as levels 4-8 (the old 'note-names' drill stays for its Toolbox chapter), so group 1 has one button with 8 levels. Patch: sc/patch654.py applied on the t653 build. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
