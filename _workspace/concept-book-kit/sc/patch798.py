"""Build DV (mock-up), her 11:17 'the doll's house in colour, the butler where I am', then 11:34 'no colour is better; or
change only the brick border so each floor shows as its own section': the corner stones (quoins) drawn floor by floor,
three ways to choose from behind a URL setting, remembered on this device (?house=off forgets it):
  ?house=alt   the stones navy on every other floor, white on the rest
  ?house=tint  the stones in a pastel per floor (the floor's wallpaper), nothing else coloured
  ?house=here  white stones, your floor's in coral
and the rabbit butler's oval portrait on the wall of the room you are in (every look). Without the setting the house is as
before, apart from the portrait."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

R("""const TH_FLOOR = [""", """// Build DV: the corner stones floor by floor (mock-up). read once at load, before the app tidies the address bar
const TH_Q = (() => { try { const m = location.search.match(/[?&]house=(alt|tint|here|off)/); if (m) { if (m[1] === 'off') localStorage.removeItem('pb_house_q'); else localStorage.setItem('pb_house_q', m[1]); return m[1] === 'off' ? null : m[1]; } return localStorage.getItem('pb_house_q'); } catch (e) { return null; } })();
const TH_Q_TINT = { panel: '#f6c4cf', sprig: '#bfe3d2', scale: '#b9d4ec', trellis: '#d3c3ea', damask: '#f3dc9a', drape: '#e7a3b2', regency: '#f6c4cf' };
const TH_FLOOR = [""")
R("""function stQuoins(x, y0, y1, left) {   // the stepped corner stones, long and short in turn
  let s = '', y = y0, k = 0;
  while (y < y1 - 2) { const h = Math.min(9, y1 - y), w = k % 2 === 0 ? 12 : 8; s += stR(left ? x : x - w, y, w, h, ST.FW); y += h; k++; }""",
  """function stQuoins(x, y0, y1, left, fill) {   // the stepped corner stones, long and short in turn (Build DV: a floor's own fill)
  let s = '', y = y0, k = 0;
  while (y < y1 - 2) { const h = Math.min(9, y1 - y), w = k % 2 === 0 ? 12 : 8; s += stR(left ? x : x - w, y, w, h, ST.FW, fill); y += h; k++; }""")
# remember each floor's span, its wallpaper and whether you are on it
R("""  let garretBot = 0;
  for (let k = view.stages.length - 1; k >= 0; k--) {   // the floors, the top stage first""", """  let garretBot = 0; const spans = [];
  for (let k = view.stages.length - 1; k >= 0; k--) {   // the floors, the top stage first""")
R("""    y = yy + fh;
  }
  // the ground floor: the hall""", """    if (!gi) spans.push({ y0: y, y1: yy + fh, wp: fs.wp, here, k });
    y = yy + fh;
  }
  // the ground floor: the hall""")
R("""  body += stQuoins(X0, qTop, gb, false) + stQuoins(X1, qTop, gb, true) + stL(X0, qTop, X0, gb, 2.2) + stL(X1, qTop, X1, gb, 2.2);""",
  """  const qm = o.print ? null : TH_Q;
  if (!qm) body += stQuoins(X0, qTop, gb, false) + stQuoins(X1, qTop, gb, true);
  else { const segs = spans.filter(sp => sp.y1 > qTop).map(sp => ({ ...sp, y0: Math.max(sp.y0, qTop) })).concat([{ y0: hallTop, y1: gb, wp: 'panel', here: false, k: -1, hall: true }]);
    segs.forEach((sp, i) => { const f = qm === 'alt' ? (i % 2 === 0 ? ST.N : '#fff') : qm === 'tint' ? (sp.hall ? '#fff' : TH_Q_TINT[sp.wp] || '#fff') : (sp.here ? ST.C : '#fff');
      body += stQuoins(X0, sp.y0, sp.y1, false, f) + stQuoins(X1, sp.y0, sp.y1, true, f); }); }
  body += stL(X0, qTop, X0, gb, 2.2) + stL(X1, qTop, X1, gb, 2.2);""")
# the butler's portrait on the wall of the room you are in
R("""  s += '<rect x="' + pFix(x + 1) + '" y="' + pFix(y + h - fh) + '" width="' + pFix(w - 2) + '" height="' + fh + '" fill="url(#thfl-' + fs.fl + ')" stroke="none" opacity="0.32"/>' + stL(x + 1, y + h - fh, x + w - 1, y + h - fh, 0.5);""",
  """  s += '<rect x="' + pFix(x + 1) + '" y="' + pFix(y + h - fh) + '" width="' + pFix(w - 2) + '" height="' + fh + '" fill="url(#thfl-' + fs.fl + ')" stroke="none" opacity="0.32"/>' + stL(x + 1, y + h - fh, x + w - 1, y + h - fh, 0.5);
  if (on) { const ch = cmp ? 22 : 34, cw2 = ch * 0.8, ccx = x + w - cw2 / 2 - (cmp ? 5 : 9), ccy = cy - ch / 2 - (cmp ? 3 : 6);   // Build DV: the butler's portrait on your room's wall
    s += '<ellipse cx="' + pFix(ccx) + '" cy="' + pFix(ccy) + '" rx="' + pFix(cw2 / 2 + 1.6) + '" ry="' + pFix(ch / 2 + 1.6) + '" fill="#fff" stroke="' + ST.N + '" stroke-width="1.2"/>'
      + '<image href="' + VIC_CAMEO + '" x="' + pFix(ccx - cw2 / 2) + '" y="' + pFix(ccy - ch / 2) + '" width="' + pFix(cw2) + '" height="' + pFix(ch) + '" preserveAspectRatio="xMidYMid meet"/>'
      + stL(ccx, ccy - ch / 2 - 1.6, ccx, ccy - ch / 2 - (cmp ? 5 : 8), 0.8) + stC(ccx, ccy - ch / 2 - (cmp ? 5.5 : 8.5), cmp ? 1 : 1.4, 0, ST.N); }""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok house quoins', len(s))
