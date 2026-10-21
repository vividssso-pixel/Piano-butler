import sys, re
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
blk = open('/home/claude/pbtest/sc/ks4.jsx', encoding='utf-8').read()
# 1. the registry: p-keys and p-names become one section
i = s.index("  ['p-keys', [\n"); j = s.index("  ['p-stf', [\n")
s = s[:i] + "  KS_ROWS_KEYS,\n" + s[j:]
rep("\nconst KS_ROWS = [", blk + "\nconst KS_ROWS = [")
# 2. Home: one section with its two chapter drills
m = re.search(r"    \{ id: 'p-keys', en: 'Keyboard patterns', ko: '[^']*', lessons: \[[^\]]*\], check: 'first-steps' \},\n    \{ id: 'p-names'[^\n]*\n", s)
assert m
s = s[:m.start()] + "    { id: 'p-keys', en: 'Keyboard patterns and note names', ko: '건반 패턴과 음 이름', lessons: ['kp-groups', 'kp-hear', 'kp-small', 'kp-big', 'nn-find', 'kp-middle', 'kp-repeat'], checks: [['first-steps', 'Questions: keyboard patterns', '문제: 건반 패턴'], ['note-names', 'Questions: note names', '문제: 음 이름']] },\n" + s[m.end():]
# the kicker name
rep("{ id: 'p-keys', area: 'pitch', en: 'Keyboard patterns', ko: '건반 무늬' }", "{ id: 'p-keys', area: 'pitch', en: 'Keyboard patterns and note names', ko: '건반 패턴과 음 이름' }")
# 3. the section renders one button per chapter drill
k = s.index("{g.check && <button onClick={() => go({ view: 'home', drill: g.check,")
e = s.index("</button>}", k) + len("</button>}")
s = s[:k] + "{(g.checks || (g.check ? [[g.check, 'Questions, level by level', '\\u6587\\u984c']] : [])).map(([id, en, ko]) => <button key={id} onClick={() => go({ view: 'home', drill: id, tab: 'drill', level: 1, mode: 'lesson' })} style={{display:'block',width:'100%',minHeight:52,marginTop:4,borderRadius:26,border:'none',background:'var(--navy)',color:'#fffefa',fontWeight:800,fontSize:17,cursor:'pointer'}}>{LANG === 'ko' ? (ko === '\\u6587\\u984c' ? '문제를 단계별로' : ko) + ' \\u2192' : en + ' \\u2192'}</button>)}" + s[e:]
open(bb, 'w', encoding='utf-8').write(s)
