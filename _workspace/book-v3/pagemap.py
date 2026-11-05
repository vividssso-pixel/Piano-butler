# One page map for the whole Handbook (her 5 Nov: topics may take 2 or 3 pages, so page numbers are computed, never typed).
# Write a reference as {{H3}} (first page of Harmony 3) or {{H3+1}} (its second page); page() fills in the number.
import re
PARTS = [('P', 'Pitch', 5), ('T', 'Time', 7), ('S', 'Scales and keys', 7), ('H', 'Harmony', 9)]
PLANNED = {'H': 12}   # chapters planned but not built yet: their numbers follow on, for forward references
TIPS = {'P': True, 'T': True, 'S': True, 'H': False}
COUNT = {'T2': 3, 'H1': 3, 'H9': 3}          # pages per topic; 2 unless set here
START = 21          # the Pitch opener
def build(count=None, legacy=False):
    c = {} if legacy else dict(COUNT, **(count or {})); page, n = {}, START
    for p, _, k in PARTS:
        page[p + 'O'] = n; n += 1
        for i in range(1, k + 1):
            page[f'{p}{i}'] = n; n += c.get(f'{p}{i}', 2)
        m = n
        for i in range(k + 1, PLANNED.get(p, k) + 1): page[f'{p}{i}'] = m; m += 2
        if TIPS[p]: page[p + 'T'] = n; n += 1
    page['X'] = n; page['_END'] = n + 2
    return page
PAGE = build()
def pages_of(key): return PAGE[key], (COUNT.get(key, 2) if key[1:].isdigit() else 1)
def resolve(t):
    return re.sub(r'\{\{([A-Z]{1,2}\d{0,2}|X)(?:\+(\d))?\}\}', lambda m: str(PAGE[m.group(1)] + int(m.group(2) or 0)), t)
# the numbering used before 5 Nov (every topic 2 pages): legacy page -> live page, for the workbooks' old references
_L = build(legacy=True)
def legacy(n):
    best = None
    for k, v in _L.items():
        if k.startswith('_') or (k[0] == 'H' and k[1:].isdigit() and int(k[1:]) > 7): continue
        span = 2 if k[1:].isdigit() else (2 if k == 'X' else 1)
        if v <= n < v + span: best = (k, n - v)
    return PAGE[best[0]] + best[1] if best else n
