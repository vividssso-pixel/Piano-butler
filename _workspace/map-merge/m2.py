# Map merge M2 (2026-11-01, her '2로 하자'): Topics for everyone. No per-student setting any more: every student and
# every visitor has the Map's two views; children and visitors open on the House, teachers on Topics (until they choose).
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
rep("const HM = T || (showToday && !st.lock && planHome());", "const HM = T || !st.lock;   // Map merge M2: Topics for every student and visitor (single-tool links, lock=1, stay as they are)")
rep("{onHome && planHome() && <div style={sec}>", "{onHome && <div style={sec}>")
rep("function mapPick(canTopics) { if (!canTopics) return 'path'; let x = null; try { x = localStorage.getItem(MAP_VIEW_KEY); } catch (e) {} return x === 'house' ? 'path' : 'home'; }",
    "function mapPick(canTopics, teacher) { if (!canTopics) return 'path'; let x = null; try { x = localStorage.getItem(MAP_VIEW_KEY); } catch (e) {} return x === 'house' ? 'path' : x === 'topics' ? 'home' : (teacher ? 'home' : 'path'); }   // M2: children and visitors start on the House")
rep("view: v === 'map' ? mapPick(HM) : v,", "view: v === 'map' ? mapPick(HM, T) : v,")
open(p, 'w', encoding='utf-8').write(h); print('m2 ok')
