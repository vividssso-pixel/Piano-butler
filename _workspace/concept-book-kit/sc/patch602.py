import sys
L=open(sys.argv[1],encoding='utf-8').read().split('\n')
for n in (55127,55377,55442,55464,55502):
    l=L[n-1]; assert l.count('{prettyNote(k)}</button>')==1,(n,l[:80]); L[n-1]=l.replace('{prettyNote(k)}</button>','{scKeyBtn(k)}</button>')
s='\n'.join(L)
a="\nfunction ScStaffBtn("
assert s.count(a)==1
s=s.replace(a,"""
// a black key's button shows both its names, like the keyboard: sharp above, flat below
const SC_SH = { Db: 'C♯', Eb: 'D♯', Gb: 'F♯', Ab: 'G♯', Bb: 'A♯' };
const scKeyBtn = (k) => SC_SH[k] ? <span style={{display:'inline-grid',lineHeight:1.05,fontSize:12,gap:1}}><span>{SC_SH[k]}</span><span>{prettyNote(k)}</span></span> : prettyNote(k);"""+a)
open(sys.argv[2],'w',encoding='utf-8').write(s)
