import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:80])
    s = s.replace(old, new)
# kqKb passes hop arrows (arcs) to the keyboard (also in sc/kq.jsx)
rep("ncol={f.ncol || {}} arcs={[]} nonce={0} onTap={onTap}", "ncol={f.ncol || {}} arcs={f.arcs || []} nonce={f.nonce || 0} onTap={onTap}")
# the Intervals lessons (sc/iv.jsx), after the Keys and staff registry
i = s.index("\nconst scDirTag = ")
s = s[:i] + "\n" + open('/home/claude/pbtest/sc/iv.jsx', encoding='utf-8').read() + s[i:]
# Home: Intervals in four groups, each with its Questions button at its own level of the intervals drill
i = s.index("  'p-intervals': {\n    lessons: ['ivx-ladder'")
j = s.index("  },\n", i) + len("  },\n")
s = s[:i] + """  'p-intervals': { lessons: [], groups: [
    { id: 'iv-num', en: 'The number', ko: '음정의 숫자', lessons: ['iv-count', 'iv-staff'], check: 'intervals', level: 1 },
    { id: 'iv-qual', en: 'Major, minor and perfect', ko: '장음정, 단음정, 완전음정', lessons: ['iv-half', 'iv-tonic', 'iv-minor'], check: 'intervals', level: 3 },
    { id: 'iv-hear', en: 'Hearing intervals', ko: '음정 듣기', lessons: ['iv-mh', 'iv-ear'], check: 'intervals', level: 7 },
    { id: 'iv-turn', en: 'Upside down, and the tritone', ko: '음정 뒤집기와 트라이톤', lessons: ['iv-invert', 'iv-tritone'], check: 'intervals', level: 8 },
  ] },
""" + s[j:]
rep("go({ view: 'home', drill: g.check, tab: 'drill', level: 1, mode: 'lesson' })", "go({ view: 'home', drill: g.check, tab: 'drill', level: g.level || 1, mode: 'lesson' })")
# a concept's first group opens when the open group belongs to another concept
rep("{live.groups && live.groups.map((g, gi) => { const on = openG === g.id;", "{live.groups && live.groups.map((g, gi) => { const on = (live.groups.some(x => x.id === openG) ? openG : openG === null ? null : live.groups[0].id) === g.id;")
# lesson titles: lining figures (Playfair's old-style 3, 5, 6 dropped below the line in "3도는 6도로", "5도권")
rep("  title: {textAlign:'center',fontFamily:\"'Playfair Display', Georgia, serif\",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'},\n  line: {textAlign:'center',fontSize:15",
    "  title: {textAlign:'center',fontFamily:\"'Playfair Display', Georgia, serif\",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance',fontVariantNumeric:'lining-nums'},\n  line: {textAlign:'center',fontSize:15")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
