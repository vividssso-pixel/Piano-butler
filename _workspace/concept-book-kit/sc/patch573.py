import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# two chips instead of four for lessons 1-2: recognise (half/whole + white neighbours mixed), play (half and whole mixed)
rep("""  { n: 21, label: 'Half step or whole step?', short: ['Half or whole?', '반음? 온음?'], num: '1–2', kind: 'hw', time: 7, noPrint: true },
  { n: 22, label: 'Play a half step, up or down', short: ['Play a half step', '반음 치기'], num: '1', kind: 'find', size: 1, time: 9, noPrint: true },
  { n: 23, label: 'White neighbours: E F and B C', short: ['White neighbours', '흰건반 이웃'], num: '1', kind: 'wn', time: 7, noPrint: true },
  { n: 24, label: 'Play a whole step, up or down', short: ['Play a whole step', '온음 치기'], num: '2', kind: 'find', size: 2, time: 9, noPrint: true },
""","""  { n: 21, label: 'Half step or whole step?', short: ['Half or whole?', '반음? 온음?'], num: '1–2', kind: 'hw', mix: true, time: 8, noPrint: true },
  { n: 22, label: 'Play a half or whole step, up or down', short: ['Play the step', '반음·온음 치기'], num: '1–2', kind: 'find', mix: true, time: 9, noPrint: true },
""")
rep("'Double sharps and flats': '겹샵과 겹플랫' });","'Double sharps and flats': '겹샵과 겹플랫', 'Play a half or whole step, up or down': '반음·온음 치기, 위나 아래로' });")
rep("generate: (lv, prev) => lv.kind === 'dbl' ? genDblQuestion(prev) :",
    "generate: (lv, prev) => lv.kind === 'dbl' ? genDblQuestion(prev) : lv.kind === 'hw' && lv.mix && Math.random() < 0.4 ? genTnQuestion({ kind: 'wn' }, prev) : lv.kind === 'find' && lv.mix ? genTnQuestion({ ...lv, size: pick([1, 2]) }, prev) :")
open(sys.argv[2],'w',encoding='utf-8').write(s)
