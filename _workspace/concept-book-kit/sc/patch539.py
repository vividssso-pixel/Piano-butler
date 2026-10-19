import sys,re
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# the extras that belong elsewhere leave this drill (the questions stay in the code for their own concepts)
for n in ("3, label: 'Name the coral note'","4, label: 'Key signature and accidental'","7, label: 'Listen: right or wrong?'","8, label: 'The bass staff'","10, label: 'My keys: name the key'"):
    a=s.index("  { n: "+n); b=s.index("\n",a)+1; s=s[:a]+s[b:]
# the bass staff joins the main levels: now and then the key signature is on the bass staff
rep("  const pool = kind === 'kn-majS' ?","  const clef = Math.random() < 0.35 ? 'bass' : 'treble';   // Phase 539: the bass staff is mixed in\n  const pool = kind === 'kn-majS' ?")
rep("return { kind, key: 'k' + k.major, k, answer: minName(k),","return { kind, clef, key: 'k' + k.major, k, answer: minName(k),")
rep("  return { kind, key: 'k' + k.major, k, answer: majName(k), choices: shuffle([majName(k), ...others(majName)]), uid };\n}","  return { kind, clef, key: 'k' + k.major, k, answer: majName(k), choices: shuffle([majName(k), ...others(majName)]), uid };\n}")
rep("{prompt(t('Which minor key has this key signature?', '이 조표는 어떤 단조일까요?'))}{paper(<KSStaff count={q.k.count} type={q.k.type} ink={ink} width={170}/>)}","{prompt(t('Which minor key has this key signature?', '이 조표는 어떤 단조일까요?'))}{paper(<KSStaff count={q.k.count} type={q.k.type} ink={ink} width={170} clef={q.clef}/>)}")
rep("{prompt(t('Which major key has this key signature?', '이 조표는 어떤 장조일까요?'))}{paper(<KSStaff count={q.k.count} type={q.k.type} ink={ink} width={170}/>)}</>;\n  }\n  return <div><BoardTrack","{prompt(t('Which major key has this key signature?', '이 조표는 어떤 장조일까요?'))}{paper(<KSStaff count={q.k.count} type={q.k.type} ink={ink} width={170} clef={q.clef}/>)}</>;\n  }\n  return <div><BoardTrack")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
