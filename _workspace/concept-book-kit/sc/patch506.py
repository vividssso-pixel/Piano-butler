import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a,s.count(a)); s=s.replace(a,b)
rep("setLit(n + 1); playKey(pcOfName(order[n]), 0.45); } };","setLit(n + 1); playKey(kidx(order[n]), 0.45); } };")
rep("timers.current.push(setTimeout(() => { playKey(pcOfName(order[i]), 0.45); setLit(i + 1); }","timers.current.push(setTimeout(() => { playKey(kidx(order[i]), 0.45); setLit(i + 1); }")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
