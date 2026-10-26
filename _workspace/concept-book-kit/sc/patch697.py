import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AG (plan call 5, her 2026-10-26: "카테고리를 최대한 단순하게"): Touch and expression, Technique and Pieces open straight
# onto their rooms, the way Rhythm already does. One list of rooms per door, no topic level in between. Small rooms join their
# neighbour: the pedals and the ornaments go into Touch, 'More about tempo' into Tempo. Pitch keeps its seven topics (22 rooms
# would be too long for one list). Old links (concept=t-touch and so on) open the merged door with that room open.
rep("""// Build O (the curriculum plan, 2026-10-25): the floor of every Home lesson.""",
"""// Build AG (plan call 5, 2026-10-26: as few categories as possible): Touch and expression, Technique and Pieces are one list of
// rooms each, opened straight from the Home like Rhythm. Pitch keeps its seven topics. HOME_OLD sends old concept links to the
// merged door and opens that room.
const HOME_DOOR = [{ id: 'h-touch', area: 'touch' }, { id: 'h-tech', area: 'tech' }, { id: 'h-piece', area: 'piece' }]
  .map(d => ({ id: d.id, area: d.area, get name() { return TOOL_AREAS.find(a => a.id === d.area).name; } }));
const HOME_OLD = {};
(() => {
  const L = HOME_LIVE, g = (cid, gid) => L[cid].groups.find(x => x.id === gid);
  const art = g('t-touch', 't-art'), speed = g('t-tempo', 't-speed');
  L['h-touch'] = { lessons: [], groups: [g('t-touch', 't-dyn'),
    { ...art, lessons: art.lessons.concat(g('t-touch', 't-pedal').lessons, g('t-touch', 't-orn').lessons) },
    { ...speed, lessons: speed.lessons.concat(g('t-tempo', 't-feel').lessons) }, g('t-tempo', 't-terms')],
    tools: L['t-tempo'].tools, tryLine: L['t-tempo'].tryLine };
  L['h-tech'] = { lessons: [], groups: [
    { id: 'k-post', en: 'Posture and hands', ko: '자세와 손', lessons: L['k-posture'].lessons.slice(), check: L['k-posture'].check },
    { id: 'k-pos', en: 'Hand positions', ko: '손 자리', lessons: L['k-positions'].lessons.filter(id => !L['k-posture'].lessons.includes(id)), check: L['k-positions'].check },
  ].concat(L['k-play'].groups) };
  L['h-piece'] = { lessons: [], groups: [
    { id: 'c-read', en: 'Reading tunes', ko: '선율 읽기', lessons: L['c-reading'].lessons.slice(), check: L['c-reading'].check },
  ].concat(L['c-map'].groups) };
  Object.assign(HOME_OLD, { 't-touch': ['h-touch', 't-dyn'], 't-tempo': ['h-touch', 't-speed'], 'k-posture': ['h-tech', 'k-post'],
    'k-positions': ['h-tech', 'k-pos'], 'k-play': ['h-tech', 'kpl-scales'], 'c-reading': ['h-piece', 'c-read'], 'c-map': ['h-piece', 'c-signs'] });
  Object.keys(HOME_OLD).forEach(k => { delete L[k]; });
})();
// Build O (the curriculum plan, 2026-10-25): the floor of every Home lesson.""")
rep("""const homeCats = (areaId) => { const all =""", """const homeCats = (areaId) => { const dr = HOME_DOOR.find(d => d.area === areaId); if (dr) return [dr]; const all =""")
rep("""HOME_STAFF.find(c => c.id === id) || (id === 'aural' ? HOME_AURAL : undefined);""",
    """HOME_STAFF.find(c => c.id === id) || HOME_DOOR.find(c => c.id === id) || (id === 'aural' ? HOME_AURAL : undefined);""")
rep("""hc: homeCatById(p.get('concept')) ? p.get('concept') : null,""",
    """hc: HOME_OLD[p.get('concept')] ? (window.__ksOpen = HOME_OLD[p.get('concept')][1], HOME_OLD[p.get('concept')][0]) : homeCatById(p.get('concept')) ? p.get('concept') : null,""")
# a lesson opened from a door page that skips its topic level (Rhythm, and now the three merged doors) says where it goes back to
rep("""((homeCatById(st.hc) || {}).name || t('Home', '홈'))""",
    """((homeCatById(st.hc) || (st.ha && homeCats(st.ha).length === 1 ? homeCats(st.ha)[0] : null) || {}).name || t('Home', '홈'))""", 2)
# the try tool under a list of rooms (the metronome, the circle of fifths) is numbered after the last lesson, not '1'
rep("""{(() => { let n = 0; return <>""", """{(() => { let n = live.groups ? live.groups.reduce((a, x) => a + x.lessons.length, 0) : 0; return <>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
