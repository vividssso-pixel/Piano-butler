# Map merge M6 (2026-11-01, her 'the Home's categories: make them separate, not public, only for me; only the Reference shows').
# Topics = the Reference only, for everyone. The old Home's categories and their short lessons move to a teacher-only tab, Lessons.
import sys, re
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
ACT_MAP = "(v === 'map' && !st.lib && (st.view === 'path' || st.view === 'chapters' || st.view === 'home' || (T && st.view === 'tools' && st.ret === 'toolbox')))"
ACT_LIB = "(v === 'lib' && !!st.lib && (st.view === 'home' || (st.view === 'tools' && st.ret === 'home')))"
OLD_MAP = "(v === 'map' && (st.view === 'path' || st.view === 'chapters' || st.view === 'home' || (T && st.view === 'tools' && (st.ret === 'home' || st.ret === 'toolbox'))))"
rep("[['map', t('Map', '지도')], ...(booksUnlocked()", "[['map', t('Map', '지도')], ['lib', t('Lessons', '레슨')], ...(booksUnlocked()")
rep("update({ view: v === 'map' ? mapPick(HM, T) : v, tool: null, kit: null, from: null, ret: null, drill: (v === 'practice' || v === 'students') ? st.drill : null, ...(v === 'map' ? { ha: null, hc: null, hs: null } : {}) });",
    "update({ view: v === 'map' ? mapPick(HM, T) : v === 'lib' ? 'home' : v, lib: v === 'lib', tool: null, kit: null, from: null, ret: null, drill: (v === 'practice' || v === 'students') ? st.drill : null, ...(v === 'map' || v === 'lib' ? { ha: null, hc: null, hs: null } : {}) });")
rep("(st.view === v || " + OLD_MAP + ")", "((st.view === v && v !== 'lib') || " + ACT_MAP + " || " + ACT_LIB + ")", 2)
rep("(T && v === 'home' && st.view === 'tools' && st.ret === 'home')", "false")
# the Topics view: the Reference only; the categories only in Lessons (teacher)
rep("""          <>{!st.ha && !st.hc && !st.hs && todayBack}{!st.ha && !st.hc && !st.hs && <MapSwitch value="topics" onPick={(x) => { mapSave(x); update({ view: x === 'house' ? 'path' : 'home', ha: null, hc: null, hs: null, drill: null }); }}/>}{!st.ha && !st.hc && !st.hs && <ReferenceView pick onChapter={jumpToChapter}/>}<ConceptHome st={st} update={update}/></>""",
    """          (T && (st.lib || st.ha || st.hc || st.hs))
            ? <ConceptHome st={st} update={update}/>
            : <>{todayBack}<MapSwitch value="topics" onPick={(x) => { mapSave(x); update({ view: x === 'house' ? 'path' : 'home', lib: false, ha: null, hc: null, hs: null, drill: null }); }}/><ReferenceView pick onChapter={jumpToChapter}/></>""")
rep("{HM && <MapSwitch value=\"house\" onPick={(x) => { mapSave(x); update({ view: x === 'house' ? 'path' : 'home', ha: null, hc: null, hs: null, drill: null }); }}/>}",
    "{HM && <MapSwitch value=\"house\" onPick={(x) => { mapSave(x); update({ view: x === 'house' ? 'path' : 'home', lib: false, ha: null, hc: null, hs: null, drill: null }); }}/>}")
# every way back inside the categories now says Lessons (the switch keeps its own 'Topics')
h = re.sub(r"(?<!\['topics', )t\('Topics', '주제'\)", "t('Lessons', '레슨')", h)
if h.count("t('Topics', '주제')") != 1: raise SystemExit('switch label check')
open(p, 'w', encoding='utf-8').write(h); print('m6 ok')
