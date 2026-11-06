#!/usr/bin/env python3
# Phase 436b: balance on each floor -- one name size per floor, ticks on all done rooms of a floor or none, the pictures in a row at one height (her 2026-10-12 12:08)
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit('count %d != %d for: %s' % (c, n, a[:90]))
    s = s.replace(a, b)

rep("""function thRoom(view, state, id, x, y, w, h, fs, out, dimNew) {   // dimNew: the guides' front page greys the rooms without a page""",
"""// A floor's names in one size -- the largest at which every name fits on one line, keeping the done tick if it can --
// and how many lines the longest takes, so the pictures on a floor hang in one row (her 2026-10-12: balance).
function thNames(state, rooms) {
  const Z = [16.5, 15, 13.5], one = (txt, w, z) => rdWidth(txt, 700, z, TH_SERIF) <= w - 33;   // the square, a gap and a margin each side
  const rs = rooms.map(([id, w]) => { const st = state[id], nm = CH_SHORT[id] || [id, ''], bare = st === 'print' ? nm[0] : t(nm[0], nm[1] || nm[0]); return { id, w, bare, full: (st === 'done' ? '✓\\u00a0' : '') + bare }; });
  // with the ticks if every name still fits on one line; else without (the green squares say done) -- the same on the whole floor
  let key = 'full', z = Z.find(z => rs.every(r => one(r.full, r.w, z)));
  if (z == null) { key = 'bare'; z = Z.find(z => rs.every(r => one(r.bare, r.w, z))); }
  if (z == null) { key = 'full'; z = 13.5; }   // a name too long for one line at any size: two lines, ticks kept
  const lines = {}; let ml = 1;
  rs.forEach(r => { lines[r.id] = thWrap(r[key], r.w - 33, z, TH_SERIF).slice(0, 2); ml = Math.max(ml, lines[r.id].length); });
  return { z, lines, ml };
}
function thRoom(view, state, id, x, y, w, h, fs, out, dimNew, lay) {   // dimNew: the guides' front page greys the rooms without a page; lay: thNames""")

rep("""  const nm = CH_SHORT[id] || [id, ''], bare = st === 'print' ? nm[0] : t(nm[0], nm[1] || nm[0]), avail = w - sq - 12;
  const fits = (txt, z) => thWrap(txt, avail, z, TH_SERIF).length <= 1 && rdWidth(txt, 700, z, TH_SERIF) <= avail;
  let name = (done ? '✓\\u00a0' : '') + bare, nz = [16.5, 15, 13.5].find(z => fits(name, z));
  if (!nz && done) { name = bare; nz = [16.5, 15, 13.5].find(z => fits(name, z)); }   // the green square already says done
  if (!nz) nz = 13.5;
  const lines = thWrap(name, avail, nz, TH_SERIF).slice(0, 2), nfill""",
"""  const nm = CH_SHORT[id] || [id, ''], nz = lay.z, lines = lay.lines[id], nfill""")
rep("""  if (ic) s += thPic(x + w / 2, Math.max(sy + lines.length * 14 + 14, cy - 40), ic, st === 'new' && !on);""",
"""  if (ic) s += thPic(x + w / 2, Math.max(sy + lay.ml * 14 + 14, cy - 40), ic, st === 'new' && !on);   // one height on the floor""")

# the floor: lay out the names first; a floor with a two-line name is one line taller
rep("""    const st = view.stages[k], fs = TH_FLOOR[k], n = st.ids.length, c = cols(n), fh = LH + RH * Math.ceil(n / c), here = st.ids.includes(view.here);""",
"""    const st = view.stages[k], fs = TH_FLOOR[k], n = st.ids.length, c = cols(n), here = st.ids.includes(view.here);
    const rwOf = (j) => (X1 - RX0) / Math.min(c, n - Math.floor(j / c) * c), lay = thNames(state, st.ids.map((id, j) => [id, rwOf(j)]));
    const rh = RH + (lay.ml - 1) * 14, fh = LH + rh * Math.ceil(n / c);""")
rep("""      const r = Math.floor(j / c), cc = j - r * c, inrow = Math.min(c, n - r * c), rw = (X1 - RX0) / inrow;
      body += thRoom(view, state, id, RX0 + cc * rw, yy + LH + r * RH, rw, RH, fs, out, o.dimNew);""",
"""      const r = Math.floor(j / c), cc = j - r * c, rw = rwOf(j);
      body += thRoom(view, state, id, RX0 + cc * rw, yy + LH + r * rh, rw, rh, fs, out, o.dimNew, lay);""")
open(out, 'w', encoding='utf-8').write(s); print('436b ok')
