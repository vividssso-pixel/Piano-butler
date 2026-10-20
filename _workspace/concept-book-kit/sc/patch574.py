import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("""  { n: 26, label: 'Find the key', short: ['Find the key', '건반 찾기'], num: '3–4', kind: 'key', time: 9, noPrint: true },
  { n: 27, label: 'Sharps and flats on the staff', short: ['On the staff', '오선 위 음'], num: '3–4', kind: 'staff', time: 10, noPrint: true },
""","""  { n: 26, label: 'Find the key', short: ['Find the key', '건반 찾기'], num: '3–4', kind: 'key', mix: true, time: 10, noPrint: true },
""")
rep("lv.kind === 'find' && lv.mix ? genTnQuestion({ ...lv, size: pick([1, 2]) }, prev) :",
    "lv.kind === 'find' && lv.mix ? genTnQuestion({ ...lv, size: pick([1, 2]) }, prev) : lv.kind === 'key' && lv.mix && Math.random() < 0.5 ? genTnQuestion({ kind: 'staff' }, prev) :")
open(sys.argv[2],'w',encoding='utf-8').write(s)
