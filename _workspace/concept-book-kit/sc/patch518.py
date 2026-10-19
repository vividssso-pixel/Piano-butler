import sys
s=open(sys.argv[1],encoding='utf-8').read()
a="aria-pressed={n === i} aria-disabled={i > maxN} style={{...KF_BTN,minWidth:44,padding:'0 2px',fontSize:14,opacity:i > maxN ? 0.3 : 1}} onClick={() => { if (i <= maxN) pickN(i); }}>"
b="aria-pressed={n === i} style={{...KF_BTN,minWidth:44,padding:'0 2px',fontSize:14}} onClick={() => pickN(i)}>"
assert s.count(a)==1
open(sys.argv[2],'w',encoding='utf-8').write(s.replace(a,b));print('ok')
