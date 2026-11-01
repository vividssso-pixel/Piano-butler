# Map merge M1 (2026-11-01, Sohyun's 'yes, go that way'): Home + Chapters become one Map tab with two views,
# House (the chapters' house) and Topics (the Home and its Reference). Visitors keep the House only for now.
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
# 1. the tabs
rep("[['home', t('Home', '홈')], ['path', t('Chapters', '챕터')], ", "[['map', t('Map', '지도')], ")
rep("[['today', t('Today', '오늘')], ['path', t('Learn', '배우기')], ", "[['today', t('Today', '오늘')], ['map', t('Map', '지도')], ")
rep(" : [['path', t('Learn', '배우기')], ", " : [['map', t('Map', '지도')], ")
rep("update({ view: v, tool: null, kit: null, from: null, ret: null, drill: (v === 'practice' || v === 'students') ? st.drill : null, ...(v === 'home' ? { ha: null, hc: null, hs: null } : {}) });",
    "update({ view: v === 'map' ? mapPick(HM) : v, tool: null, kit: null, from: null, ret: null, drill: (v === 'practice' || v === 'students') ? st.drill : null, ...(v === 'map' ? { ha: null, hc: null, hs: null } : {}) });")
rep("color:(st.view === v || (v === 'path' && st.view === 'chapters') || (T && v === 'home' && st.view === 'tools' && (st.ret === 'home' || st.ret === 'toolbox'))) ? 'var(--navy)' : 'var(--muted)'",
    "color:(st.view === v || (v === 'map' && (st.view === 'path' || st.view === 'chapters' || st.view === 'home' || (T && st.view === 'tools' && (st.ret === 'home' || st.ret === 'toolbox'))))) ? 'var(--navy)' : 'var(--muted)'")
# the underline follows the same rule
i = h.index("['map', t('Map', '지도')], ")
seg_s = h.index("borderBottom:'3p", i); seg_e = h.index("}}>{l}</button>", seg_s)
seg = h[seg_s:seg_e]
if "st.view === v" in seg and "v === 'map'" not in seg.split("color:")[0]:
    head, tail = seg.split("color:", 1)
    head2 = head.replace("st.view === v", "(st.view === v || (v === 'map' && (st.view === 'path' || st.view === 'chapters' || st.view === 'home' || (T && st.view === 'tools' && (st.ret === 'home' || st.ret === 'toolbox')))))", 1)
    h = h[:seg_s] + head2 + "color:" + tail + h[seg_e:]
# 2. the switch on top of both views (top level only)
rep("<>{!st.ha && !st.hc && !st.hs && todayBack}<ConceptHome st={st} update={update}/></>",
    "<>{!st.ha && !st.hc && !st.hs && todayBack}{!st.ha && !st.hc && !st.hs && <MapSwitch value=\"topics\" onPick={(x) => { mapSave(x); update({ view: x === 'house' ? 'path' : 'home', ha: null, hc: null, hs: null, drill: null }); }}/>}<ConceptHome st={st} update={update}/></>")
rep(": <>{todayBack}<MapHome onOpen=",
    ": <>{todayBack}{HM && <MapSwitch value=\"house\" onPick={(x) => { mapSave(x); update({ view: x === 'house' ? 'path' : 'home', ha: null, hc: null, hs: null, drill: null }); }}/>}<MapHome onOpen=")
rep("function App() {", r'''// ── Map merge M1: one Map tab, two views of the same rooms. House = the chapters' house; Topics = the Home with its Reference.
// The last view a teacher (or an adult with Topics switched on) chose is kept; visitors and children see the House.
const MAP_VIEW_KEY = 'pb_map_view_v1';
function mapSave(x) { try { localStorage.setItem(MAP_VIEW_KEY, x); } catch (e) {} }
function mapPick(canTopics) { if (!canTopics) return 'path'; let x = null; try { x = localStorage.getItem(MAP_VIEW_KEY); } catch (e) {} return x === 'house' ? 'path' : 'home'; }
function MapSwitch({ value, onPick }) {
  const opts = [['house', t('House', '집'), t('by floor', '층별')], ['topics', t('Topics', '주제'), t('by topic', '주제별')]];
  return <div role="tablist" aria-label={t('Two views of the map', '지도를 보는 두 가지 방법')} data-map-switch={value} style={{display:'flex',border:'1.5px solid var(--navy)',borderRadius:12,overflow:'hidden',margin:'0 0 14px'}}>
    {opts.map(([k, l, s]) => <button key={k} type="button" role="tab" aria-selected={value === k} data-map-view={k} onClick={() => value !== k && onPick(k)}
      style={{flex:1,minHeight:44,border:'none',cursor:value === k ? 'default' : 'pointer',font:'inherit',padding:'6px 8px',background:value === k ? 'var(--navy)' : '#fffefa',color:value === k ? '#fffefa' : 'var(--navy)'}}>
      <span style={{display:'block',fontSize:14.5,fontWeight:900}}>{l}</span><span style={{display:'block',fontSize:11.5,fontWeight:600,opacity:0.8}}>{s}</span></button>)}
  </div>;
}

function App() {''')
# 3. words: the Home is now Topics
for old, new in [
    ("onClick={() => go({ ha: null, hc: null, hs: null })}>← {t('Home', '홈')}</button>", "onClick={() => go({ ha: null, hc: null, hs: null })}>← {t('Topics', '주제')}</button>"),
    ("onClick={() => update({ view: 'home', kit: null, kn: '' })}>{t('← Home', '← 홈')}</button>", "onClick={() => update({ view: 'home', kit: null, kn: '' })}>{t('← Topics', '← 주제')}</button>"),
    ("{t('The Home: every topic →', '홈: 모든 주제 →')}", "{t('The Map by topic →', '주제별 지도 →')}"),
]:
    rep(old, new)
h = h.replace("t('Home', '홈')", "t('Topics', '주제')")   # every way back to the old Home now says Topics
open(p, 'w', encoding='utf-8').write(h); print('m1 ok')
