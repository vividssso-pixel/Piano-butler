import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
rep("bigLabels = false, extraC = false, trail = null, trailLabels = null }) {","bigLabels = false, extraC = false, extraB = false, trail = null, trailLabels = null }) {   // Phase 512: extraB = one more B at the left end (C♭ sits there)")
rep("  let w = 0;\n  for (let i = 0; i < octaves * 12; i++) {\n    const info = PC_INFO[i % 12];\n    if (info.white) { whites.push({ i, x: w * whiteW, info }); w++; }\n    else blacks.push({ i, x: w * whiteW - blackW / 2, info });\n  }\n  if (extraC) { whites.push({ i: octaves * 12, x: w * whiteW, info: PC_INFO[0] }); w++; }\n  const width = w * whiteW;",
    "  let w = 0;\n  const off = extraB ? whiteW : 0;\n  if (extraB) whites.push({ i: -1, x: 0, info: PC_INFO[11] });\n  for (let i = 0; i < octaves * 12; i++) {\n    const info = PC_INFO[i % 12];\n    if (info.white) { whites.push({ i, x: off + w * whiteW, info }); w++; }\n    else blacks.push({ i, x: off + w * whiteW - blackW / 2, info });\n  }\n  if (extraC) { whites.push({ i: octaves * 12, x: off + w * whiteW, info: PC_INFO[0] }); w++; }\n  const width = w * whiteW + off;")
rep("const kidx = (nm) => (sharp && pcOfName(nm) === 0 ? 12 : pcOfName(nm));   // B♯ is the C above B",
    "const kidx = (nm) => (sharp && pcOfName(nm) === 0 ? 12 : !sharp && pcOfName(nm) === 11 ? -1 : pcOfName(nm));   // B♯ is the C above B; C♭ is the B below C (Phase 512)")
rep("order.slice(0, lit).forEach(nm => { if (sharp && (nm[0] === 'E' || nm[0] === 'B')) o[kidx(nm)] = prettyNote(nm); }); return o; })() : null;",
    "order.slice(0, lit).forEach(nm => { if (sharp ? (nm[0] === 'E' || nm[0] === 'B') : (nm[0] === 'C' || nm[0] === 'F')) o[kidx(nm)] = prettyNote(nm); }); return o; })() : null;")
rep("labels=\"all\" bigLabels extraC={sharp}","labels=\"all\" bigLabels extraC={sharp} extraB={!sharp}",2)
rep("if (i % 12 === pcOfName(order[got]))","if (((i % 12) + 12) % 12 === pcOfName(order[got]))")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
