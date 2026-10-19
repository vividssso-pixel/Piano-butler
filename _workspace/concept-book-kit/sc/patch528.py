import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("  miss:   { white: '#fff', black: '#26296b', stroke: '#e4572e', sw: 2.5, text: '#e4572e' },",
"  miss:   { white: '#fff', black: '#26296b', stroke: '#e4572e', sw: 2.5, text: '#e4572e' },\n  pass:   { white: '#fbe3da', black: '#f6cbbb', stroke: '#e9b9a6', sw: 1, text: '#26296b', blackText: '#26296b' },   // Phase 528: a key the move passes through, pale; only the arrival is strong")
rep("""fill="#fff" style={{pointerEvents:'none',animation:'fadeUp 0.3s both'}}>{names[k.i]}</text>""","""fill={m && m.blackText ? m.blackText : '#fff'} style={{pointerEvents:'none',animation:'fadeUp 0.3s both'}}>{names[k.i]}</text>""")
rep("""fontWeight="700" fill="#faf6ec" style={{pointerEvents:'none'}}>{prettyNote(n)}</text>""","""fontWeight="700" fill={m && m.blackText ? m.blackText : '#faf6ec'} style={{pointerEvents:'none'}}>{prettyNote(n)}</text>""")
rep("      marks[pM] = 'mate';\n      for (let q = 1; q <= sd; q++) { const kk = m12(pM - q); marks[kk] = q === sd ? 'pick' : 'mate'; names[kk] = String(q); }",
"      marks[pM] = 'pass';\n      for (let q = 1; q <= sd; q++) { const kk = m12(pM - q); marks[kk] = q === 3 ? 'pick' : 'pass'; names[kk] = String(q); }")
rep("    if (stage === 1 || found) marks[pM] = 'mate';\n    if (found) marks[pm] = 'pick';","    if (stage === 1 || found) marks[pM] = 'pass';\n    if (found) marks[pm] = 'pick';")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
