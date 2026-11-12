# Her 12 Nov ("1.2 오케이"): one set of level names everywhere, the house's: Beginner, Prelim, Grade 1-8.
# The generators still write "Level 0 / Level ½ / Level n"; this pass renames them in the built Handbook and Workbook pages.
# "Level book(s)" (the product) is left alone.
import re, glob
H = '/mnt/user-data/outputs/house-rooms/'
N = {'0': 'Beginner', '½': 'Prelim'}
def one(x): return N.get(x) or f'Grade {x}'
def lv(t):
    t = re.sub(r'Levels (0|½|\d)\s*[–-]\s*(½|\d)(?! book)', lambda m: (one(m.group(1)) + ' to ' + one(m.group(2))) if m.group(1) in N else f'Grades {m.group(1)}–{m.group(2)}', t)
    t = re.sub(r'Level (0|½|\d)(?![\d ]?book)', lambda m: one(m.group(1)), t)
    return t
def text_only(html):   # change text between tags, never attributes
    return re.sub(r'>([^<]+)<', lambda m: '>' + lv(m.group(1)) + '<', html)
n = 0
for f in glob.glob(H + 'handbook-*.html') + glob.glob(H + 'workbook-*.html'):
    s = open(f).read(); t = text_only(s)
    if t != s: open(f, 'w').write(t); n += 1
print('ok levelnames', n)
