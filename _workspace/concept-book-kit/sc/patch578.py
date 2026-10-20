import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("const scHat = (n) => n + '̂';", "const scHat = (n) => String(n);   // her 'no hat over the numbers' (2026-10-20)")
open(sys.argv[2],'w',encoding='utf-8').write(s)
