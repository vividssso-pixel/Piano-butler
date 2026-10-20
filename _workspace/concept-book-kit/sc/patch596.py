import sys
s=open(sys.argv[1],encoding='utf-8').read()
a="      <ScStaffScale k={kk} ring={A ? (P.an <= 7 ? P.an : 14 - P.an) : null}/>\n"
assert s.count(a)==1
b="      {scFingers(kk, 'RH', 1) && scFingers(kk, 'LH', 1) && <ScPair keyName={kk} n={1} cur={A ? (P.an <= 7 ? P.an : 14 - P.an) : undefined}/>}\n"+a
s=s.replace(a,b)
open(sys.argv[2],'w',encoding='utf-8').write(s)
