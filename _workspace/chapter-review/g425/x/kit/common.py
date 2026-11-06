import json, sys, html
sys.path.insert(0, '/home/claude/pbtest/cast')
from cast import piece
from butlers import cameo_svg
NAVY, CORAL, GREEN, MUTED, NEW, CLARA, CLARA_D = '#26296b', '#e4572e', '#2b6e56', '#6d6f9c', '#8a8cb0', '#f4a9bb', '#e07c96'
D = json.load(open('/home/claude/pbtest/cast/mapicons.json'))
STAGES = D['stages']; ICONS = D['icons']; SHORT = D['short']
ORDER = [i for s in STAGES for i in s['ids']]
NUM = {i: k + 1 for k, i in enumerate(ORDER)}
STATE = {i: 'new' for i in ORDER}; STATE['posture-hands'] = 'done'; HERE = 'first-steps'
def name(i): return SHORT.get(i, [i])[0]
def esc(s): return html.escape(s, quote=True)
def T(x, y, s, size=11, weight=600, fill=NAVY, anchor='start', serif=False, italic=False, ls=None, op=None):
    st = ("font-family:'Playfair Display',Georgia,serif;" if serif else 'font-family:Inter,sans-serif;') + ('font-style:italic;' if italic else '') + ('letter-spacing:%s;' % ls if ls else '') + ('font-variant-numeric:lining-nums;' if serif else '')
    return '<text x="%.1f" y="%.1f" font-size="%s" font-weight="%s" fill="%s" text-anchor="%s" style="%s"%s>%s</text>' % (x, y, size, weight, fill, anchor, st, (' opacity="%s"' % op) if op else '', esc(s))
def icon(i, x, y, k=0.7, op=1):
    ic = ICONS.get(i)
    return ('<g transform="translate(%.1f %.1f) scale(%s)" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity="%s">%s</g>' % (x, y, k, NAVY, op, ic)) if ic else ''
def square(x, y, s, k, txt=None, fill=None, size=None):
    dark = fill or (NAVY if k % 2 == 0 else '#ffffff')
    out = '<rect x="%.1f" y="%.1f" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="1.1"/>' % (x, y, s, s, dark, NAVY if not fill else fill)
    if txt is not None: out += T(x + s / 2, y + s * 0.72, txt, size or s * 0.62, 800, '#ffffff' if dark != '#ffffff' else NAVY, 'middle', serif=True)
    return out
def wrap(s, n):
    words, lines, cur = s.split(), [], ''
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= n: cur = (cur + ' ' + w).strip()
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines
def pawn(x, y, k): return '<g transform="translate(%.1f %.1f) scale(%s)">%s</g>' % (x, y, k, piece('pawn', 'flat', CLARA, CLARA, tiara=True, tiara_col=CLARA_D))
def king(x, y, k, tone=NAVY): return '<g transform="translate(%.1f %.1f) scale(%s)">%s</g>' % (x, y, k, piece('king', 'flat', tone, tone))
def queen(x, y, k): return '<g transform="translate(%.1f %.1f) scale(%s)">%s</g>' % (x, y, k, piece('queen', 'flat', CORAL, CORAL))
import urllib.parse
CAMEO_URI = 'data:image/svg+xml,' + urllib.parse.quote(cameo_svg('fox', pink=CORAL), safe='')
def cameo(x, y, h): return '<image href="%s" x="%.1f" y="%.1f" height="%s" width="%.1f"/>' % (CAMEO_URI, x, y, h, h * 184 / 232)
FONTS = '''<style>
@font-face { font-family: Inter; font-weight: 400; src: url(/home/claude/pbtest/kit/node_modules/@fontsource/inter/files/inter-latin-400-normal.woff2); }
@font-face { font-family: Inter; font-weight: 600; src: url(/home/claude/pbtest/kit/node_modules/@fontsource/inter/files/inter-latin-600-normal.woff2); }
@font-face { font-family: Inter; font-weight: 700; src: url(/home/claude/pbtest/kit/node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2); }
@font-face { font-family: Inter; font-weight: 800; src: url(/home/claude/pbtest/kit/node_modules/@fontsource/inter/files/inter-latin-800-normal.woff2); }
@font-face { font-family: 'Playfair Display'; font-weight: 700; src: url(/home/claude/pbtest/kit/node_modules/@fontsource/playfair-display/files/playfair-display-latin-700-normal.woff2); }
@font-face { font-family: 'Playfair Display'; font-weight: 800; src: url(/home/claude/pbtest/kit/node_modules/@fontsource/playfair-display/files/playfair-display-latin-800-normal.woff2); }
@font-face { font-family: 'Playfair Display'; font-weight: 700; font-style: italic; src: url(/home/claude/pbtest/kit/node_modules/@fontsource/playfair-display/files/playfair-display-latin-700-italic.woff2); }
@font-face { font-family: 'Playfair Display'; font-weight: 800; font-style: italic; src: url(/home/claude/pbtest/kit/node_modules/@fontsource/playfair-display/files/playfair-display-latin-800-italic.woff2); }
</style>'''
