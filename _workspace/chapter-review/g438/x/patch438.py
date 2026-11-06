#!/usr/bin/env python3
# Phase 438 (Sohyun 2026-10-12 13:17 '프레임에 안넣는건?', 14:45 '유리돔 빼고 쓰자. 대신 조명들 다 빼주고, 클릭될 때 클라라
# 안보여도 되고 대신에 유리돔을 보여주게 ... 유리돔 옆으로 좀 더 넓게'): the rooms' pictures hang without a frame, all in
# the same ink; your room shows its picture under a wide glass dome instead of Clara; no lamps anywhere in the house.
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit('count %d != %d for: %s' % (c, n, a[:100]))
    s = s.replace(a, b)
i = s.index("function thPic(cx, top, ic, faded) {"); j = s.index("\n}\n", i) + 3
s = s[:i] + """function thPic(cx, top, ic, faded) {   // the chapter's picture on the wall, no frame (Phase 438); faded: the guides' rooms without a page
  const k = 0.8, iw = 48 * k;
  return '<g transform="translate(' + pFix(cx - iw / 2) + ' ' + pFix(top + 2) + ') scale(' + k + ')" fill="none" stroke="' + ST.N + '" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" opacity="' + (faded ? 0.5 : 1) + '">' + ic + '</g>';
}
// your room: its picture under a wide glass dome on a little round table (her 14:45: the dome instead of Clara, wider)
function thDome(cx, top, ic) {
  const T = top + 33, fl = top + 46, R = 28, k = 0.66, iw = 48 * k;
  return stR(cx - R - 3, T - 3, 2 * R + 6, 3, 0.9)
    + stR(cx - 18, T, 36, 2.2, 0.8) + stR(cx - 1.3, T + 2.2, 2.6, fl - T - 6, 0.7)
    + stP(stD('M', cx - 10, fl, 'Q', cx - 3, fl - 2, cx, fl - 4.5, 'Q', cx + 3, fl - 2, cx + 10, fl), 0.8, 'none')
    + '<path d="' + stD('M', cx - R, T - 3, 'L', cx - R, top + 10, 'A', R, 16, 0, 0, 1, cx + R, top + 10, 'L', cx + R, T - 3) + '" fill="#fff" stroke-width="1.1"/>'
    + '<path d="' + stD('M', cx + R - 9, top - 1, 'A', 18, 13, 0, 0, 1, cx + R - 4, top + 9) + '" fill="none" stroke-width="0.6" opacity="0.5"/>'
    + stC(cx, top - 7.6, 1.7, 0, ST.C)
    + '<g transform="translate(' + pFix(cx - iw / 2) + ' ' + pFix(top + 7.2) + ') scale(' + k + ')" fill="none" stroke="' + ST.N + '" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">' + ic + '</g>';
}
""" + s[j:]
rep("""  if (ic) s += thPic(x + w / 2, Math.max(sy + lay.ml * 14 + 14, cy - 40), ic, st === 'new' && !on);   // one height on the floor
  if (on) out.fig = (view.pawn || stPawn)(x + w - 20, y + h - fh - 0.5, 0.4);""",
"""  const picTop = Math.max(sy + lay.ml * 14 + 14, cy - 40);   // one height on the floor
  if (ic && !on) s += thPic(x + w / 2, picTop, ic, dimNew && st === 'new');
  if (on) out.fig = stG(ic ? thDome(x + w / 2, picTop, ic) : '');   // your room: the dome, not Clara""")
rep("""    const [lp, lg] = thLamp(fs.lamp, X1 - 24, yy); body += lp; glow += lg;\n""", "")
rep("""  [camX - 6, camX + camH * 0.8 + 6].forEach(sx => { const [lp, lg] = thLamp('sconce', sx - 2, gy + 26); body += lp; glow += lg; });\n""", "")
rep("""  [dx - 58, dx + 58].forEach(lx => { body += stLantern(lx, gb + 12, 0.62); glow += stGlow(lx, gb + 12, 0.62); });\n""", "")
rep("""// Every floor has its own interior -- its wallpaper, its floor and the lamp on its stair -- like the rooms of a doll's
// house. A room is a chapter button; a finished room's number is green; yours has a coral frame and Clara in it.""",
"""// Every floor has its own interior -- its wallpaper and its floor -- like the rooms of a doll's house; no lamps (Phase 438).
// A room is a chapter button with its picture on the wall, no frame; a finished room's number is green; yours has a coral
// frame and its picture under a glass dome (Phase 438: the dome instead of Clara).""")
# a floor's names may go down to 12.5 to stay on one line before any of them wraps (걸음·건너뛰기 on a wide screen)
rep("  const Z = [16.5, 15, 13.5], one = (txt, w, z) => rdWidth(txt, 700, z, TH_SERIF) <= w - 33;", "  const Z = [16.5, 15, 13.5, 12.5], one = (txt, w, z) => rdWidth(txt, 700, z, TH_SERIF) <= w - 33;")
open(out, 'w', encoding='utf-8').write(s); print('438 ok')
