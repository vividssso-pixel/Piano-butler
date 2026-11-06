#!/usr/bin/env python3
# Phase 436a: the townhouse -- every boxed label centred (Sohyun 2026-10-12 12:08); the floor plaque says only the floor
# ("LEVEL 2" / "2층", her 11:43 and 12:08); a finished floor's plaque turns green (the plaque's chess square is gone).
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit('count %d != %d for: %s' % (c, n, a[:90]))
    s = s.replace(a, b)

# 1. the room: the number's square and the name centred over the picture; a second line centred under it
rep("""  // number on a chess square (green when done), the name, the picture
  const sq = 17, sx = x + 6, sy = y + (fs.wp === 'drape' ? 13 : 6);
  s += stSquare(sx, sy, sq, num, done ? ST.G : null, 11);
  const nm = CH_SHORT[id] || [id, ''], bare = st === 'print' ? nm[0] : t(nm[0], nm[1] || nm[0]), avail = w - sq - 12;""",
"""  // the number on a chess square (green when done) and the name, centred over the picture (her 2026-10-12: every box centred)
  const sq = 17, sy = y + (fs.wp === 'drape' ? 13 : 6), cx = x + w / 2;
  const nm = CH_SHORT[id] || [id, ''], bare = st === 'print' ? nm[0] : t(nm[0], nm[1] || nm[0]), avail = w - sq - 12;""")
rep("""  const lines = thWrap(name, avail, nz, TH_SERIF).slice(0, 2);
  lines.forEach((ln, k) => { s += stT(sx + sq + 5, sy + 13 + k * 14, ln, { size: nz, weight: 700, font: TH_SERIF, fill: on ? ST.C : dimNew && st === 'new' ? ST.NEW : ST.N }); });""",
"""  const lines = thWrap(name, avail, nz, TH_SERIF).slice(0, 2), nfill = on ? ST.C : dimNew && st === 'new' ? ST.NEW : ST.N;
  const sx = cx - (sq + 5 + rdWidth(lines[0], 700, nz, TH_SERIF)) / 2;   // the square and the first line together, centred
  s += stSquare(sx, sy, sq, num, done ? ST.G : null, 11) + stT(sx + sq + 5, sy + 13, lines[0], { size: nz, weight: 700, font: TH_SERIF, fill: nfill });
  if (lines[1]) s += stT(cx, sy + 27, lines[1], { size: nz, weight: 700, font: TH_SERIF, fill: nfill, anchor: 'middle' });""")

# 2. the floor's plaque: "LEVEL 2" / "2층", centred on the floor; green once every room on it is done
rep("""    // the floor's plaque: its number on a chess square and its name, in a moulded frame
    const name = (o.print ? st.s.en[0] : t(st.s.en[0], st.s.ko[0])).toUpperCase(), mw = rdWidth(name, 700, 11.5, TH_CAPS), pw = (thFontsIn() ? mw : Math.max(mw, name.length * 9.4)) + name.length * 1.04 + 36;   // Cinzel's capitals are wide: trust a measure only once the letters are in
    body += stR(RX0 + 6, yy + 4, pw, 20, 0.9) + stR(RX0 + 8, yy + 6, pw - 4, 16, 0.4, 'none') + stSquare(RX0 + 11, yy + 7.5, 13, k + 1, st.st.every(v => v === 'done') ? ST.G : null, 9)
      + stT(RX0 + 30, yy + 18.4, name, { size: 11.5, weight: 700, font: TH_CAPS, ls: '0.09em', fill: here ? ST.C : ST.N });""",
"""    // the floor's plaque, centred in a moulded frame: just the floor -- "LEVEL 2", "2층" (her 2026-10-12: no floor names);
    // coral on your floor, green once every room on it is done
    const name = o.print || LANG !== 'ko' ? 'LEVEL ' + (k + 1) : (k + 1) + '층', mw = rdWidth(name, 700, 11.5, TH_CAPS), pw = (thFontsIn() ? mw : Math.max(mw, name.length * 9.4)) + name.length * 1.04 + 30, px = (X0 + X1) / 2 - pw / 2;   // Cinzel's capitals are wide: trust a measure only once the letters are in
    body += stR(px, yy + 4, pw, 20, 0.9) + stR(px + 2, yy + 6, pw - 4, 16, 0.4, 'none')
      + stT((X0 + X1) / 2, yy + 18.4, name, { size: 11.5, weight: 700, font: TH_CAPS, ls: '0.09em', fill: here ? ST.C : st.st.every(v => v === 'done') ? ST.G : ST.N, anchor: 'middle' });""")

# 3. as many floors as there are stages
rep("for (let k = 6; k >= 0; k--) {   // the floors, the top stage first", "for (let k = view.stages.length - 1; k >= 0; k--) {   // the floors, the top stage first")
open(out, 'w', encoding='utf-8').write(s); print('436a ok')
