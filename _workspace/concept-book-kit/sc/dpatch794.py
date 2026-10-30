#!/usr/bin/env python3
"""Build DQ (dashboard): DRILLS_HOUSE regenerated from the drills build with the fourth Grade 8 room (66 rooms: Knowing Your Pieces,
Grade 8 and Diplomas). Usage: python3 dpatch794.py td786.html td794.html house794.json"""
import sys, json, re
src, dst, house = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
H = json.load(open(house, encoding='utf-8'))
floors = [{ 'name': f['name'], 'extra': 1 if f['extra'] else 0, 'rooms': [[r[0], r[1], r[2], r[3], r[4]] for r in f['rooms']] } for f in H['floors']]
data = json.dumps({ 'floors': floors, 'cps': H['cps'] }, ensure_ascii=False, separators=(',', ':'))
n = len(re.findall(r'^const DRILLS_HOUSE = .*$', s, flags=re.M)); assert n == 1, n
s = re.sub(r'^const DRILLS_HOUSE = .*$', lambda m: 'const DRILLS_HOUSE = ' + data + ';', s, flags=re.M)
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s), 'rooms', sum(len(f['rooms']) for f in floors))
