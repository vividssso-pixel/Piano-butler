import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
x = "stroke={clean ? '#d3cab4' : m ? m.stroke : (pixel ? '#26296b' : '#dbd2bd')} strokeWidth={clean ? 1 : m ?"
assert s.count(x) == 1
s = s.replace(x, "stroke={clean ? (m ? '#fff' : '#d3cab4') : m ? m.stroke : (pixel ? '#26296b' : '#dbd2bd')} strokeWidth={clean ? (m ? 2.5 : 1) : m ?")
open(b, 'w', encoding='utf-8').write(s); print('ok')
