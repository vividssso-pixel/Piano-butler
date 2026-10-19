import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("<KSStaff count={n} type={type} width={200} ring={one ? undefined : want} tallBox={sharp}","<KSStaff count={n} type={type} width={200} numbers upto={one ? undefined : want} ring={one ? undefined : want} tallBox={sharp}")
rep("<KSStaff count={lit} type={type} width={200} tallBox={sharp} onPick=","<KSStaff count={lit} type={type} width={200} numbers upto={(stage === 1 || done) && !auto ? want : undefined} tallBox={sharp} onPick=")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
