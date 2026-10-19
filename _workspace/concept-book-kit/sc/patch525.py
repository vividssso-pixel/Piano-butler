import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("}, 450 + (q - 1) * 600)));","}, 800 + (q - 1) * 1500)));")
rep("playKey(m12(pM - q), 0.4);","playKey(m12(pM - q), 0.9);")
rep("playKey(pcOfName(k.major), 0.5); }, 550);","playKey(pcOfName(k.major), 0.9); }, 1000);")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
