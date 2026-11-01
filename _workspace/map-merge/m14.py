p='drills.src.html'; s=open(p).read()
if 'function RefShelf' in s: print('already'); raise SystemExit
comp=r'''// m14: the Library (her 1 Nov: 'books like this' -- the navy and ivory spines, gold bands, a wooden shelf; a book taken from the
// shelf opens below with its table). It replaces the Topics chips; the House is behind 'My house'.
const REF_SHELVES = [
  ['Reading music', '악보 읽기', [['staff', 'Staff and clefs', '오선과 음자리표'], ['notes', 'Notes and rests', '음표와 쉼표'], ['time', 'Time signatures', '박자표'], ['signs', 'Signs', '기호']]],
  ['Pitch and harmony', '음높이와 화성', [['keys', 'Keys', '조성'], ['scales', 'Scales', '음계'], ['intervals', 'Intervals', '음정'], ['chords', 'Chords', '화음'], ['cadences', 'Cadences', '종지']]],
  ['Words and history', '용어와 역사', [['play', 'How to play', '연주 용어'], ['terms', 'Music words', '음악 낱말'], ['periods', 'Periods', '시대'], ['instruments', 'Instruments', '악기']]],
];
const REF_SPINE_H = [150, 138, 160, 128, 144, 132, 156, 140, 150, 136, 148, 130, 142];
function RefSpine({ id, label, dark, h, on, onPick }) {
  const ko = LANG === 'ko', band = (top) => <i aria-hidden="true" style={{position:'absolute',left:0,right:0,[top ? 'top' : 'bottom']:12,height:5,borderTop:'1px solid ' + (dark ? '#c9a24f' : '#a8823f'),borderBottom:'1px solid ' + (dark ? '#c9a24f' : '#a8823f')}}/>;
  return <button type="button" data-ref-spine={id} aria-pressed={on} onClick={() => onPick(on ? null : id)} title={label}
    style={{flex:'none',position:'relative',width:'clamp(36px, 9vw, 58px)',height:h,border:'none',padding:0,cursor:'pointer',borderRadius:'4px 4px 1px 1px',
      background:dark ? 'linear-gradient(90deg,#1a1c55 0%,#2f3280 30%,#2a2d78 65%,#17194c 100%)' : 'linear-gradient(90deg,#e6dcc3 0%,#fbf6ea 30%,#f6efdd 65%,#ddd1b4 100%)',
      color:dark ? '#fff' : 'var(--navy)',boxShadow:on ? '0 8px 12px rgba(38,41,107,.28)' : '0 1px 0 rgba(0,0,0,.08)',transform:on ? 'translateY(-10px)' : 'none',transition:'transform .18s',display:'flex',alignItems:'center',justifyContent:'center'}}>
    {band(true)}{band(false)}
    <span style={{writingMode:'vertical-rl',textOrientation:ko ? 'upright' : 'mixed',transform:ko ? 'none' : 'rotate(180deg)',fontFamily:LB_SERIF,fontWeight:700,fontSize:ko ? 14 : 15,letterSpacing:ko ? '0.08em' : '0.03em',whiteSpace:'nowrap'}}>{label}</span>
  </button>;
}
function RefShelf({ onChapter, onHouse }) {
  const [sel, setSel] = useState(() => { let x = null; try { x = localStorage.getItem(REF_PICK_KEY + '_shelf'); } catch (e) {} return REF_SECS.some(s => s.id === x) ? x : null; });
  const panel = useRef(null), ko = LANG === 'ko';
  const pick = (id) => { setSel(id); try { localStorage.setItem(REF_PICK_KEY + '_shelf', id || ''); } catch (e) {} if (id) setTimeout(() => { const el = panel.current; if (el && el.scrollIntoView) el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 60); };
  const s = sel && REF_SECS.find(z => z.id === sel), B = s && REF_BODY[s.id];
  const L = (typeof tLessonGet === 'function' && tLessonGet()) || null;
  let k = 0;
  return <RefGo.Provider value={onChapter || null}><div data-ref-shelf data-ref-open={sel || ''} style={{marginBottom:26}}>
    <div style={{display:'flex',alignItems:'center',gap:12,margin:'0 0 6px'}}>
      <img src={VIC_CAMEO} alt="" style={{height:50,flex:'none'}}/>
      <div><div style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:16.5,color:'var(--navy)'}}>{t('“Which book shall I fetch?”', '“어떤 책을 꺼내 드릴까요?”')}</div>
        <div style={{fontSize:12.5,color:'#4a4d86',marginTop:2}}>{L && L.name ? L.name + ' · ' : ''}<button type="button" data-ref-house onClick={onHouse} style={{border:'none',background:'none',padding:0,font:'inherit',fontWeight:800,color:'var(--coral, #e4572e)',cursor:'pointer'}}>{t('My house ›', '나의 집 ›')}</button></div></div>
    </div>
    {REF_SHELVES.map(([en, kr, books]) => <div key={en} style={{marginTop:18}}>
      <div style={{fontSize:10.5,fontWeight:900,letterSpacing:'0.1em',textTransform:'uppercase',color:'#4a4d86',margin:'0 0 8px'}}>{t(en, kr)}</div>
      <div style={{display:'flex',alignItems:'flex-end',gap:5,padding:'0 4px',borderBottom:'5px solid #b59a68',boxShadow:'0 3px 0 rgba(38,41,107,.12)',minHeight:120}}>
        {books.map(([id, ben, bko], i) => { const label = t(ben, bko), h = Math.max(REF_SPINE_H[k++ % 13], label.length * (ko ? 15 : 8.2) + 64);
          return <RefSpine key={id} id={id} label={label} dark={i % 2 === 0} h={h} on={sel === id} onPick={pick}/>; })}
      </div></div>)}
    {s && <section ref={panel} data-ref-panel={s.id} style={{marginTop:22,background:'#fff',borderRadius:6,padding:'22px 16px 22px',position:'relative',boxShadow:'0 0 0 1.5px rgba(38,41,107,.14)',scrollMarginTop:12}}>
      <i aria-hidden="true" style={{position:'absolute',left:16,right:16,top:8,height:5,borderTop:'1px solid #c9a24f',borderBottom:'1px solid #c9a24f'}}/>
      <i aria-hidden="true" style={{position:'absolute',left:16,right:16,bottom:8,height:5,borderTop:'1px solid #c9a24f',borderBottom:'1px solid #c9a24f'}}/>
      <div style={{display:'flex',justifyContent:'flex-end'}}><button type="button" data-ref-close onClick={() => pick(null)} style={{border:'none',background:'none',font:'inherit',fontSize:13,fontWeight:800,color:'#4a4d86',cursor:'pointer',padding:'2px 0'}}>{t('Back on the shelf ✕', '책장에 꽂기 ✕')}</button></div>
      <RefHead id={s.id}/><B/>
    </section>}
  </div></RefGo.Provider>;
}
'''
anchor='function ReferenceView({ onChapter, pick }) {'
assert s.count(anchor)==1
s=s.replace(anchor, comp+anchor)
old="""<>{todayBack}<MapSwitch value="topics" onPick={(x) => { mapSave(x); update({ view: x === 'house' ? 'path' : 'home', lib: false, ha: null, hc: null, hs: null, drill: null }); }}/><ReferenceView pick onChapter={jumpToChapter}/></>"""
new="""<>{todayBack}<RefShelf onChapter={jumpToChapter} onHouse={() => { mapSave('house'); update({ view: 'path', lib: false, ha: null, hc: null, hs: null, drill: null }); try { window.scrollTo(0, 0); } catch (e) {} }}/></>"""
assert s.count(old)==1; s=s.replace(old,new)
old2="""{HM && <MapSwitch value="house" onPick={(x) => { mapSave(x); update({ view: x === 'house' ? 'path' : 'home', lib: false, ha: null, hc: null, hs: null, drill: null }); }}/>}"""
new2="""{HM && <div style={{display:'flex',justifyContent:'flex-end',margin:'0 0 8px'}}><button type="button" className="chip" data-map-library onClick={() => { mapSave('topics'); update({ view: 'home', lib: false, ha: null, hc: null, hs: null, drill: null }); try { window.scrollTo(0, 0); } catch (e) {} }} style={{padding:'4px 12px',fontSize:13,fontWeight:800}}>{t('The library ›', '서재 ›')}</button></div>}"""
assert s.count(old2)==1; s=s.replace(old2,new2)
old3="(T ? [['map', t('Map', '지도')],"
assert s.count(old3)==1; s=s.replace(old3,"(T ? [['map', t('Library', '서재')],")
open(p,'w').write(s); print('ok')
