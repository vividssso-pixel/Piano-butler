import sys
s=open(sys.argv[1],encoding='utf-8').read()
for a in ["  { n: 8, label: 'Extra: D and B♭ major', short: ['D and B♭ signs', 'D와 B♭의 조표'], extra: true, kind: 'acc2', time: 9 },\n",
          "  { n: 10, label: 'My keys: the scale notes', short: ['My keys', '나의 조'], extra: true, kind: 'mykeys', time: 10 },\n"]:
    assert s.count(a)==1, a[:40]; s=s.replace(a,'')
open(sys.argv[2],'w',encoding='utf-8').write(s)
