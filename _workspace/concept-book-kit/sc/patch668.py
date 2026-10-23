import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Her call 2026-10-24: tapping Rhythm opens its chapter straight away. An area with only one concept (Rhythm: Beat and
# time) skips its one-row list: the area opens the concept, and the concept's back button goes to the Home.
rep("const cat0 = homeCatById(st.hc), cat = cat0 && cat0.area !== 'beside' ? cat0 : undefined;",
    "const soloOf = (aid) => { const cs = aid ? homeCats(aid) : []; return cs.length === 1 && HOME_LIVE[cs[0].id] ? cs[0] : null; };\n"
    "  const cat0 = homeCatById(st.hc) || (st.ha && !st.hc ? soloOf(st.ha) : undefined), cat = cat0 && cat0.area !== 'beside' ? cat0 : undefined;")
rep("onClick={() => go({ hc: null, hs: null })}>← {area ? area.name : t('Home', '홈')}</button>",
    "onClick={() => go(area && !soloOf(area.id) ? { hc: null, hs: null } : { ha: null, hc: null, hs: null })}>← {area && !soloOf(area.id) ? area.name : t('Home', '홈')}</button>")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
