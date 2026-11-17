# Her 17 Nov proofread: the Workbook's small staves (drawn for 26 px staff) grow to the Handbook rule of at least 34 px.
import re, sys
for f in sys.argv[1:]:
    h = open(f).read(); n = 0
    def g(m):
        global n; n += 1; return f'{m.group(1)}height:{round(float(m.group(2)) * 1.32)}px'
    h = re.sub(r'(data-spx="26" overflow="visible" style=")height:([0-9.]+)px', g, h)
    open(f, 'w').write(h.replace('data-spx="26"', 'data-spx="34"')); print(f, n)
# the six 3rds on one line: they keep their size (six in a row; larger would push the page over)
for f in sys.argv[1:]:
    if not f.endswith('pitch.html'): continue
    h = open(f).read(); i = h.index('Major or minor 3rd?'); j = h.index('</div></div></div>', h.index('grid-template-columns:repeat(6,1fr)', i))
    seg = re.sub(r'(data-spx="34" overflow="visible" style=")height:([0-9.]+)px', lambda m: f'{m.group(1)}height:{round(float(m.group(2)) / 1.32)}px', h[i:j])
    open(f, 'w').write(h[:i] + seg + h[j:]); print('3rds kept small')
