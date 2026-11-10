# Refresh the Music Box on 'The books' page without rebuilding the other books (her 11 Nov 00:15: keep going).
# Uses the same cover_mb/panel/layout code as books-split.py. Usage: python3 mbindex.py <books-split.py> <index.html> <shelf.json> <out index.html>
import html, json, re, sys
s, t, MB = open(sys.argv[1]).read(), open(sys.argv[2]).read(), json.load(open(sys.argv[3]))
def grab(a, b): i = s.index(a); return s[i:s.index(b, i)]
g = {'html': html, 'cards': {'mb': {'Songs': [tuple(c) for c in MB['cards']]}}}
exec("E = lambda x: html.escape(x, quote=True)\n" + grab("def card(c):", "BOOKS = [") + grab("def cover_mb(b):", "def cover(b):") + grab("def panel(b):", "def layout(") + grab("def layout(", "_K = lambda b"), g)
b = tuple(MB['book']); L = g['layout']({'mb': [g['cover_mb'](b)]}, {'mb': [g['panel'](b)]}, {'mb': len(MB['cards'])})
top = re.search(r'<button type="button" class="book top" data-series="mb".*?</button>', L, re.S).group(0)
sec = re.search(r'<section class="series" id="s-mb" hidden>.*</section>', L, re.S).group(0)
t = re.sub(r'<button type="button" class="book top" data-series="mb".*?</button>', lambda m: top, t, count=1, flags=re.S)
i = t.index('<section class="series" id="s-mb" hidden>'); j = t.index('</section></section>', i) + len('</section></section>')
t = t[:i] + sec + t[j:]
open(sys.argv[4], 'w').write(t); print('music box:', len(MB['cards']), 'songs')
