# Build BM (2026-10-27): a shorter house (her 22:21: "the house is too long too; how can I see it without much
# scrolling?"). On a phone it was 2,370 px (19 rows of rooms). Now: up to four rooms a row (13 rooms as 4 3 3 3,
# seven as 4 3, eight as 4 4, four in one row), and each room lower: the name, the picture smaller, the chair rail
# and the floor; the empty wainscot panels go. Your room's dome is scaled to fit. The wide house and the printed
# colouring page keep their layout.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)

rep("function thPic(cx, top, ic, faded) {   // the chapter's picture on the wall, no frame (Phase 438); faded: the guides' rooms without a page\n  const k = 0.8, iw = 48 * k;",
    "function thPic(cx, top, ic, faded, k = 0.8) {   // the chapter's picture on the wall, no frame (Phase 438); faded: the guides' rooms without a page; k: Build BM, smaller in the compact house\n  const iw = 48 * k;")
rep("function thDome(cx, top, ic) {\n  const T = top + 33,",
    "function thDome(cx, top, ic, sc = 1) {   // sc: Build BM, the dome scaled to a compact room\n  if (sc !== 1) return '<g transform=\"translate(' + pFix(cx) + ' ' + pFix(top) + ') scale(' + sc + ') translate(' + pFix(-cx) + ' ' + pFix(-top) + ')\">' + thDome(cx, top, ic) + '</g>';\n  const T = top + 33,")
# a compact room (phone and narrow screens): the chair rail near the floor, no panels, the picture under the name
rep("function thRoom(view, state, id, x, y, w, h, fs, out, dimNew, lay) {   // dimNew: the guides' front page greys the rooms without a page; lay: thNames\n  const st = state[id], on = id === view.here, done = st === 'done', num = view.nums[id], cy = y + h - 22;",
    "function thRoom(view, state, id, x, y, w, h, fs, out, dimNew, lay, cmp) {   // dimNew: the guides' front page greys the rooms without a page; lay: thNames; cmp: Build BM, a compact room\n  const st = state[id], on = id === view.here, done = st === 'done', num = view.nums[id], cy = y + h - (cmp ? 10 : 22);")
rep("  const fh = 6, np = w > 120 ? 3 : 2, pw = (w - 6 - np * 6) / np;\n  for (let k = 0; k < np; k++) s +=",
    "  const fh = 6, np = cmp ? 0 : w > 120 ? 3 : 2, pw = (w - 6 - np * 6) / Math.max(1, np);\n  for (let k = 0; k < np; k++) s +=")
rep("  const picTop = Math.max(sy + lay.ml * 14 + 14, cy - 40);",
    "  const picTop = cmp ? sy + lay.ml * 14 + 7 : Math.max(sy + lay.ml * 14 + 14, cy - 40);")
rep("  if (ic && !on) s += thPic(x + w / 2, picTop, ic, dimNew && st === 'new');\n  if (on) out.fig = stG(ic ? thDome(x + w / 2, picTop, ic) : '');",
    "  if (ic && !on) s += thPic(x + w / 2, picTop, ic, dimNew && st === 'new', cmp ? 0.52 : 0.8);\n  if (on) out.fig = stG(ic ? thDome(x + w / 2, picTop - (cmp ? 4 : 0), ic, cmp ? 0.6 : 1) : '');")
# the floors: rows of up to four, balanced, the fuller rows at the bottom
rep("  const cols = (n) => o.wide ? (n <= 6 ? n : Math.ceil(n / 2)) : n <= 3 ? n : n === 4 ? 2 : 3;   // Build Q: twelve rooms, two rows of six",
    "  const cmp = !o.wide && !o.print;   // Build BM: the compact house on phones and narrow screens\n"
    "  const rowsOf = (n) => { const m = o.wide ? 6 : cmp ? 4 : 3, nr = Math.ceil(n / m), b = Math.floor(n / nr), ex = n % nr; return Array.from({ length: nr }, (_, r) => b + (r < ex ? 1 : 0)); };   // the bottom row first\n"
    "  const cols = (n) => o.wide ? (n <= 6 ? n : Math.ceil(n / 2)) : n <= 3 ? n : n === 4 ? 2 : 3;   // Build Q: twelve rooms, two rows of six")
rep("    const rwOf = (j) => (L1 - L0) / Math.min(c, n - Math.floor(j / c) * c), lay = thNames(state, st.ids.map((id, j) => [id, rwOf(j)]));\n    const rh = RH + (lay.ml - 1) * 14, fh = LH + rh * Math.ceil(n / c);",
    "    const RS = cmp ? rowsOf(n) : null, at = (j) => { if (!RS) { const r = Math.floor(j / c); return [r, j - r * c, Math.min(c, n - r * c)]; } let r = 0, a = j; while (a >= RS[r]) { a -= RS[r]; r++; } return [r, a, RS[r]]; };\n"
    "    const rwOf = (j) => (L1 - L0) / at(j)[2], lay = thNames(state, st.ids.map((id, j) => [id, rwOf(j)]));\n"
    "    const rh = (cmp ? 52 + (fs.wp === 'drape' ? 7 : 0) : RH) + (lay.ml - 1) * 14, fh = LH + rh * (RS ? RS.length : Math.ceil(n / c));")
rep("    const nr = Math.ceil(n / c);   // Phase 442: the first rooms on the lowest row, counted from the bottom left -- you climb the house\n    st.ids.forEach((id, j) => {\n      const r = Math.floor(j / c), cc = j - r * c, rw = rwOf(j);\n      body += thRoom(view, state, id, L0 + cc * rw, yy + LH + (nr - 1 - r) * rh, rw, rh, fs, out, o.dimNew, lay);",
    "    const nr = RS ? RS.length : Math.ceil(n / c);   // Phase 442: the first rooms on the lowest row, counted from the bottom left -- you climb the house\n    st.ids.forEach((id, j) => {\n      const [r, cc] = at(j), rw = rwOf(j);\n      body += thRoom(view, state, id, L0 + cc * rw, yy + LH + (nr - 1 - r) * rh, rw, rh, fs, out, o.dimNew, lay, cmp);")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
