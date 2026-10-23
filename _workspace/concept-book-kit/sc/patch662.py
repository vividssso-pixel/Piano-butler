import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build C (her calls 2026-10-24 00:17): Intervals lesson 5 on the major scale; Home group headers name their lesson range;
# Korean staff lines without the English mnemonics.

# ── re-splice the three lesson files (kq, iv, ch) at their markers
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + open(SC + 'iv.jsx', encoding='utf-8').read() + "\n" + open(SC + 'ch.jsx', encoding='utf-8').read() + s[j:]

# ── 1. Home groups: an outlined pill with the lesson range (1–3, 4–7, 8–10) instead of a second 1 2 3
rep("""                <span style={{flex:'none',width:34,height:34,borderRadius:17,background:on ? '#e4572e' : 'var(--navy)',color:'#fffefa',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800,fontSize:16}}>{gi + 1}</span>""",
    """                <span style={{flex:'none',minWidth:50,height:30,padding:'0 10px',boxSizing:'border-box',borderRadius:15,border:'1.5px solid ' + (on ? '#e4572e' : 'var(--navy)'),background:on ? '#e4572e' : 'transparent',color:on ? '#fffefa' : 'var(--navy)',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800,fontSize:14,fontVariantNumeric:'tabular-nums',whiteSpace:'nowrap'}}>{g.lessons.length > 1 ? (off + 1) + '\\u2013' + (off + g.lessons.length) : off + 1}</span>""")

open(dst, 'w', encoding='utf-8').write(s); print('ok')
