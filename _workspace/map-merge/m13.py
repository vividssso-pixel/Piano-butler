import re
p='drills.src.html'; s=open(p).read()
if 'function RefCadences' in s: print('already'); raise SystemExit
i=s.index('function RefChords({ part })')
a=s.index('    <div style={{height:8}}/>\n    <RefTable k="cadences"', i)
note_end_marker="'다른 이름: 정격종지 = authentic, 반종지 = half cadence, 거짓종지 = deceptive.')}</RefNote>}"
b=s.index(note_end_marker, a)+len(note_end_marker)
block=s[a:b]
s=s[:a]+s[b:]
block=block.replace('    <div style={{height:8}}/>\n','',1)
comp=("// 7b. cadences (m13: their own section; her 'why are chords and cadences stuck together? split them')\n"
      "function RefCadences() {\n  return <div>\n"+block+"\n  </div>;\n}\n")
j=s.index('// 8. signs:')
s=s[:j]+comp+s[j:]
old="refSec('chords', 'Chords and cadences', '화음과 종지'),"
assert s.count(old)==1
s=s.replace(old,"refSec('chords', 'Chords', '화음'), refSec('cadences', 'Cadences', '종지'),")
s=s.replace("chords: RefChords, signs:","chords: RefChords, cadences: RefCadences, signs:",1)
old="['chords:a'], ['chords:b']"
assert s.count(old)==1
s=s.replace(old,"['chords:a', 'cadences'], ['chords:b']")
open(p,'w').write(s); print('ok')
