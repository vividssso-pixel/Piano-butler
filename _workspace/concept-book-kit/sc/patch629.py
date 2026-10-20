import sys
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
# Keys and staff is one concept again (her call 2026-10-21): the six chapters are sections inside it.
rep("c.id === 'p-staff' ? HOME_STAFF : [c]);", "[c]);")
rep("  const [moreOpen, setMoreOpen] = useState(false);\n  const step = (n, title",
    "  const [moreOpen, setMoreOpen] = useState(false);\n  const [openG, setOpenG] = useState('p-keys');\n  const step = (n, title")
old = "          {(live.lessons || []).map(id => { const tl = TOOLS.find(x => x.id === id); return tl ? step(++n, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' })) : null; })}\n"
assert s.count(old) == 1
new = old.replace("{(live.lessons || [])", "{(live.groups ? [] : (live.lessons || []))") + """          {live.groups && live.groups.map((g, gi) => { const on = openG === g.id; return (
            <div key={g.id} data-ks-group={g.id} style={{border:'1.5px solid var(--navy-line)',borderRadius:16,background:on ? '#fffefa' : 'transparent',padding:on ? '4px 12px 14px' : 0}}>
              <button aria-expanded={on} onClick={() => setOpenG(on ? null : g.id)} style={{display:'flex',alignItems:'center',gap:12,width:'100%',minHeight:64,padding:on ? '10px 0' : '10px 14px',background:'none',border:'none',cursor:'pointer',textAlign:'left'}}>
                <span style={{flex:'none',width:34,height:34,borderRadius:17,background:on ? '#e4572e' : 'var(--navy)',color:'#fffefa',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800,fontSize:16}}>{gi + 1}</span>
                <span style={{flex:1,minWidth:0,fontWeight:800,fontSize:18,color:'var(--navy)'}}>{LANG === 'ko' ? g.ko : g.en}</span>
                <span style={{fontSize:16,color:'var(--navy)'}}>{on ? '\\u25B4' : '\\u25BE'}</span>
              </button>
              {on && <div style={{display:'flex',flexDirection:'column',gap:10,marginTop:4}}>
                {g.lessons.map((id, i) => { const tl = TOOLS.find(x => x.id === id); return tl ? step(i + 1, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' })) : null; })}
                {g.check && <button onClick={() => go({ view: 'home', drill: g.check, tab: 'drill', level: 1, mode: 'lesson' })} style={{display:'block',width:'100%',minHeight:52,marginTop:4,borderRadius:26,border:'none',background:'var(--navy)',color:'#fffefa',fontWeight:800,fontSize:17,cursor:'pointer'}}>{t('Questions, level by level \\u2192', '\\ubb38\\uc81c\\ub97c \\ub2e8\\uacc4\\ubcc4\\ub85c \\u2192')}</button>}
              </div>}
            </div>
          ); })}
"""
rep(old, new)
# the data: six sections, in the order of the chapters
rep("\nconst HOME_LIVE = {", "\nconst HOME_LIVE = {")
i = s.index("  'p-clock': {\n    lessons: ['ac-half'")
add = """  'p-staff': { lessons: [], groups: [
    { id: 'p-keys', en: 'Keyboard patterns', ko: '건반 패턴', lessons: ['kp-groups', 'kp-hear', 'kp-houses', 'kp-white', 'kp-piano', 'kp-song'], check: 'first-steps' },
    { id: 'p-names', en: 'Note names', ko: '음 이름', lessons: ['nn-letters', 'nn-wheel', 'nn-updown', 'nn-find', 'nn-skip'], check: 'note-names' },
    { id: 'p-stf', en: 'The staff and clefs', ko: '오선과 음자리표', lessons: ['sf-lines', 'sf-climb', 'sf-treble', 'sf-bass', 'sf-clefs', 'sf-story'], check: 'staff' },
    { id: 'p-lines', en: 'Line and space names', ko: '줄과 칸의 이름', lessons: ['ws-clef', 'ws-treble', 'ws-bass', 'ws-landmarks', 'ws-hop', 'ws-fold', 'ws-write', 'ws-flash'], check: 'whole-staff' },
    { id: 'p-ledger', en: 'Ledger lines and 8va', ko: '덧줄과 8va', lessons: ['ll-rungs', 'll-up', 'll-down', 'll-twins', 'll-fold', 'll-cs', 'll-8va'], check: 'ledger-lines' },
    { id: 'p-range', en: 'Pitch and range', ko: '음높이와 음역', lessons: ['sr-zone', 'sr-big', 'sr-family', 'sr-ladder', 'sr-range'], check: 'pitch-range' },
  ] },
"""
s = s[:i] + add + s[i:]
# the six old per-concept entries are no longer separate concepts
import re
for cid in ['p-keys', 'p-names', 'p-stf', 'p-lines', 'p-ledger', 'p-range']:
    m = re.search(r"\n  '" + cid + r"': \{ lessons: \[[^\n]*\n", s)
    assert m, cid
    s = s[:m.start()] + "\n" + s[m.end():]
open(bb, 'w', encoding='utf-8').write(s)
