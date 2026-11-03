import sys, io, re
md, hist = sys.argv[1], sys.argv[2]   # CLAUDE.md, CLAUDE-history.md
s = io.open(md, encoding='utf-8').read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
H = "### Direction decided 2026-11-01 (Sohyun, in the dashboard window) -- read before any build\n"
R(H, H + "**Books first (her 4 Nov 01:00; read this before the 1 Nov lines below).** Her own books come first, made and refined now, so that she starts teaching from them next year at the latest ('책을 먼저 계속 만들어서 다듬어가는게 맞는것 같아 늦어도 내년에는 내 책으로 시작하고 싶어서'); the diploma-prep product waits. The set, level by level: a **song-led Lesson Book** (each lesson one public-domain song: listen and sing, say and clap its rhythm, read it, play it four ways from the melody alone to a moving bass, then a check; her model is a Korean method book that builds each lesson on one song with A-D arrangements, minus its cartoons, clutter and long explanations), a **Workbook** to match, the **Handbook** as the reference, a Teacher copy each; drills is the companion (sound and drills by QR). First book: **Level 0**, children starting from nothing. Windows (her 4 Nov call): the chat window makes the song Lesson Book; the books/dashboard window keeps the Handbook and the Workbooks (`_workspace/book-v3`); one look for the set (book10.py's type and colours, check.js: every sign inside its line, row or box). Plan: a sample lesson in November for her to judge, Level 0 (12-16 lessons) by December, a print trial with a few students in January. The Workbooks' fun pass in drills stops after Level 3 (EF to EJ).\n")
a = s.index("1. The Workbooks, fun first, floor by floor:"); b = s.index("small commits).", a) + len("small commits).")
s = s[:a] + "1. The song Lesson Book, Level 0 (her 4 Nov 01:00, 'books first'): a sample lesson for her to judge first, then the book. The Workbooks' fun pass in drills paused after Level 3 (EF to EJ; Levels 4 to 8 later, the same way)." + s[b:]
R("- Push: EJ (one commit), before she opens a cloud window.", "- Push: the commits after `fd6c885`, before she opens a cloud window.")
s = re.sub(r"\| \*\*Git\*\* \| Pushed up to `b5f427b`[^|]*\|", "| **Git** | Pushed up to `fd6c885` on 2026-11-04 (EJ and the books window's work); later commits wait for her push. |", s, count=1)
io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [l for l in h if re.match(r'^\| \d{3} \|', l)]
last = max(int(l.split('|')[1]) for l in rows); n = last + 1
idx = [i for i, l in enumerate(h) if l.startswith('| %d |' % last)]
assert len(idx) == 1
h[idx[0] + 1:idx[0] + 1] = ["| %d | 2026-11-04 | **Direction: her books first, song-led (chat window, her 4 Nov 00:56 and 01:00).** She showed a Korean method book (one song a lesson: listen and sing, rhythm said and clapped, solfege written, then the song played four ways, A melody alone to D broken chords, with a pass box) as one example of where the Lesson Book could go, and asked for my view. My view: take the song as the spine, the same song at four levels, sound before symbol, a practical goal (accompanying a song) and the check; leave the cartoons, clutter, printed-twice lines and long explanations; songs public domain only, arrangements our own; the rooms and the Handbook stay as the reference the song lessons point into. Her calls: books first, made and refined now so she teaches from them next year at the latest; the first book for children starting from nothing (Level 0); a song-led set (Lesson Book, Workbook, Handbook); the two windows stay split (this one the song Lesson Book, the books window the Handbook and Workbooks). Next: a sample lesson for her to judge. |" % n]
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h))
print('CLAUDE.md and CLAUDE-history.md updated (row %d)' % n)
