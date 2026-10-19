import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# find screen: same keyboard as the orders (extra C for sharps, extra B for flats); the key note lights where the order screen lights it
rep("marks[tonic] = 'pick'; }","marks[kidx(k.major)] = 'pick'; }")
rep("labels=\"all\" bigLabels extraC={sharp} onTap={done || auto ? undefined : (i) => hit(i, null)}","labels=\"all\" bigLabels extraC={sharp} extraB={!sharp} onTap={done || auto ? undefined : (i) => hit(i, null)}")
# rule screen
i=s.index("function KfRule("); j=s.index("function KfMajor(")
b=s[i:j]
assert b.count("<TapKeyboard octaves={1} marks={marks} labels=\"all\" bigLabels />")==1 or b.count("<TapKeyboard octaves={1} marks={marks} labels=\"all\" bigLabels/>")==1
b=b.replace("<TapKeyboard octaves={1} marks={marks} labels=\"all\" bigLabels />","<TapKeyboard octaves={1} marks={marks} labels=\"all\" bigLabels extraC={sharp} extraB={!sharp}/>").replace("<TapKeyboard octaves={1} marks={marks} labels=\"all\" bigLabels/>","<TapKeyboard octaves={1} marks={marks} labels=\"all\" bigLabels extraC={sharp} extraB={!sharp}/>")
b=b.replace("  const one = !sharp && n === 1;","  const one = !sharp && n === 1;\n  const kx = (nm) => (sharp && pcOfName(nm) === 0 ? 12 : !sharp && pcOfName(nm) === 11 ? -1 : pcOfName(nm));")
b=b.replace("marks[pcOfName(lastNm)] = r === 0 ? 'pick' : 'mate'; if (r === 1) marks[pcOfName(k.major)] = 'pick'; }","marks[kx(lastNm)] = r === 0 ? 'pick' : 'mate'; if (r === 1) marks[kx(k.major)] = 'pick'; }")
assert "kx(k.major)" in b and "extraB" in b
s=s[:i]+b+s[j:]
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
