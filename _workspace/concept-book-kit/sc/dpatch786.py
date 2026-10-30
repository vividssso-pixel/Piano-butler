#!/usr/bin/env python3
"""Build DJ (dashboard): DRILLS_HOUSE regenerated from the drills build after the split (65 rooms: Scales, Grade 2 and 3;
Intervals, Grade 2; Chords and Cadences, Grade 3; Rhythm, Grade 2 and 3; Writing a Melody, a Melody for a Couplet, for a
Stanza), and the old room ids a student's checks may still carry (harmony-23, rhythm-23) shown as the Grade 3 rooms.
Usage: python3 dpatch786.py td771.html td786.html house785.json"""
import sys, json, re
src, dst, house = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
H = json.load(open(house, encoding='utf-8'))
floors = [{ 'name': f['name'], 'extra': 1 if f['extra'] else 0, 'rooms': [[r[0], r[1], r[2], r[3], r[4]] for r in f['rooms']] } for f in H['floors']]
data = json.dumps({ 'floors': floors, 'cps': H['cps'] }, ensure_ascii=False, separators=(',', ':'))
n = len(re.findall(r'^const DRILLS_HOUSE = .*$', s, flags=re.M)); assert n == 1, n
s = re.sub(r'^const DRILLS_HOUSE = .*$', lambda m: 'const DRILLS_HOUSE = ' + data + ';', s, flags=re.M)
old = 'const dhRoom = (id) => { for (const f of DRILLS_HOUSE.floors) { const r = f.rooms.find(x => x[0] === id); if (r) return r; } return null; };'
assert s.count(old) == 1
s = s.replace(old, """const DH_OLD = { 'harmony-23': 'harmony-3', 'rhythm-23': 'rhythm-3' };   // Build DJ: rooms split by grade; a check saved under the old id
const dhRoom = (id) => { id = DH_OLD[id] || id; for (const f of DRILLS_HOUSE.floors) { const r = f.rooms.find(x => x[0] === id); if (r) return r; } return null; };""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s), 'rooms', sum(len(f['rooms']) for f in floors))
