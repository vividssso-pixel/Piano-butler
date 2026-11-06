#!/usr/bin/env python3
# Phase 436c: a name may break after a middle dot (걸음·건너뛰기 on a phone); the hall's words centred in their half
import sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit('count %d != %d for: %s' % (c, n, a[:90]))
    s = s.replace(a, b)
rep("""function thWrap(text, maxW, size, font) { const out = []; let cur = ''; String(text).split(' ').forEach(w => { const nx = cur ? cur + ' ' + w : w; if (cur && rdWidth(nx, 700, size, font) > maxW) { out.push(cur); cur = w; } else cur = nx; }); if (cur) out.push(cur); return out; }""",
"""function thWrap(text, maxW, size, font) {   // breaks at a space, or just after a middle dot (걸음·|건너뛰기)
  const out = []; let cur = '';
  String(text).split(' ').forEach(w => w.replace(/·/g, '·\\u0001').split('\\u0001').filter(Boolean).forEach((p, j) => { const nx = cur ? cur + (j ? '' : ' ') + p : p; if (cur && rdWidth(nx, 700, size, font) > maxW) { out.push(cur); cur = p; } else cur = nx; }));
  if (cur) out.push(cur); return out;
}""")
rep("""  const tx = o.wide ? dx + 200 : X1 - 10, T_ = (en, ko) => o.print ? en : t(en, ko);""",
"""  const tx = o.wide ? 2 * dx - (camX + camH * 0.4) : (dx + 44 + X1) / 2, T_ = (en, ko) => o.print ? en : t(en, ko);   // the words centred: opposite the portrait (wide), between the door and the wall (phone)""")
rep("""  body += stT(tx, gy + 58, T_('Your butler', '버틀러가'), { size: 17, weight: 700, anchor: 'end', font: TH_SERIF, italic: ita }) + stT(tx, gy + 76, T_('welcomes you.', '맞아 줘요.'), { size: 17, weight: 700, anchor: 'end', font: TH_SERIF, italic: ita });""",
"""  body += stT(tx, gy + 58, T_('Your butler', '버틀러가'), { size: 17, weight: 700, anchor: 'middle', font: TH_SERIF, italic: ita }) + stT(tx, gy + 76, T_('welcomes you.', '맞아 줘요.'), { size: 17, weight: 700, anchor: 'middle', font: TH_SERIF, italic: ita });""")
open(out, 'w', encoding='utf-8').write(s); print('436c ok')
