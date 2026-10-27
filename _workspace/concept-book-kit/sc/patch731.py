# Build BL (2026-10-27): smaller rooms on screen (her 20:17, "rooms are getting long; shrink each room so it is
# easy to see"; asked which, her answer: the size of each room). A room's page held every step open at once (Melody
# 12,500 px on a phone). Now one step is open at a time: the first step not yet ticked; the others show as their
# title line only. Got it ✓ folds the step and opens the next; tapping a step's title or its pill in the map opens
# that one and folds the rest. Nothing is removed; the books are unchanged.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)

rep("  const [open, setOpen] = useState(() => { const d = loadDone()[id] || {}; const o = {}; steps.forEach((s, i) => { o[i] = !d[sk(i)]; }); return o; });\n"
    "  useEffect(() => { const d = loadDone()[id] || {}; setDone(d); const o = {}; steps.forEach((s, i) => { o[i] = !d[sk(i)]; }); setOpen(o); }, [id]);",
    "  // Build BL: one step open at a time: the first one not yet ticked\n"
    "  const firstOpen = (d) => { const i = steps.findIndex((s, j) => !d[sk(j)]); return i < 0 ? {} : { [i]: true }; };\n"
    "  const [open, setOpen] = useState(() => firstOpen(loadDone()[id] || {}));\n"
    "  useEffect(() => { const d = loadDone()[id] || {}; setDone(d); setOpen(firstOpen(d)); }, [id]);")
rep("    if (mine[k]) { setOpen(o => ({ ...o, [i]: false, [i + 1]: true })); setTimeout(",
    "    if (mine[k]) { setOpen(i + 1 < steps.length ? { [i + 1]: true } : {}); setTimeout(")
rep("  const jump = (i) => { setOpen(o => ({ ...o, [i]: true })); setTimeout(",
    "  const jump = (i) => { setOpen({ [i]: true }); setTimeout(")
rep("open: !!open[i], done: !!done[sk(i)], onToggle: () => setOpen(o => ({ ...o, [i]: !o[i] })), onDone: () => markDone(i),",
    "open: !!open[i], done: !!done[sk(i)], onToggle: () => setOpen(o => (o[i] ? {} : { [i]: true })), onDone: () => markDone(i),")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
