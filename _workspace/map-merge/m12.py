# The header, tidied (her 'sort out these tabs', 1 Nov): teacher view = one row, [Dashboard] [Student view] [⚙],
# language and Do Re Mi inside the ⚙ menu; "Teacher view" moves under the title as a small label. Students and
# visitors keep the single language chip.
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
rep("""              {st.lock ? (st.view === 'kit' ? (st.kn || t('Your tools', '내 도구')) : st.tool ? (TOOLS.find(tl => tl.id === st.tool) || {}).title : active.label) : t('Practice Drills', '연습 드릴')}
            </h1>
          </div>""", """              {st.lock ? (st.view === 'kit' ? (st.kn || t('Your tools', '내 도구')) : st.tool ? (TOOLS.find(tl => tl.id === st.tool) || {}).title : active.label) : t('Practice Drills', '연습 드릴')}
            </h1>
            {T && <div data-testid="teacher-label" style={{fontSize:11,fontWeight:900,color:'#e4572e',letterSpacing:'0.06em',textTransform:'uppercase',marginTop:2}}>{t('Teacher view', '교사 화면')}</div>}
          </div>""")
rep("""            <button className="chip" style={{padding:'3px 9px',fontSize:12}} onClick={toggleLang} title={t('한국어로 보기', 'View in English')}>{lang === 'ko' ? 'EN' : '한국어'}</button>
            {T && lang !== 'ko' && <button className={'chip' + (solfaEn ? ' active' : '')} style={{padding:'3px 9px',fontSize:12}} onClick={toggleSolfa} title="Show fixed-do syllables (C = Do) beside the letter names">Do Re Mi</button>}
            {T && <div style={{textAlign:'right'}}>
              <div style={{fontSize:11,fontWeight:900,color:'#e4572e',letterSpacing:'0.06em'}}>{t('TEACHER VIEW', '교사 화면')}</div>
              <button className="chip" style={{padding:'3px 10px',fontSize:12,marginTop:3}} onClick={() => setPreview(true)}>{t('Student view', '학생 화면')}</button>{' '}
              <a className="chip" data-testid="to-dashboard" href="teacher-dashboard.html" style={{padding:'3px 10px',fontSize:12,marginTop:3,textDecoration:'none',display:'inline-block'}}>{t('Dashboard', '대시보드')}</a>
            </div>}""", """            {!T && <button className="chip" style={{padding:'3px 9px',fontSize:12}} onClick={toggleLang} title={t('한국어로 보기', 'View in English')}>{lang === 'ko' ? 'EN' : '한국어'}</button>}
            {T && <div style={{display:'flex',gap:6,alignItems:'center',position:'relative'}} data-testid="teacher-head">
              <a className="chip" data-testid="to-dashboard" href="teacher-dashboard.html" style={{padding:'5px 12px',fontSize:13,fontWeight:800,textDecoration:'none',display:'inline-block'}}>{t('Dashboard', '대시보드')}</a>
              <button className="chip" style={{padding:'5px 12px',fontSize:13,fontWeight:800}} onClick={() => setPreview(true)}>{t('Student view', '학생 화면')}</button>
              <button className="chip" data-testid="head-settings" aria-expanded={headMenu} aria-label={t('Settings', '설정')} onClick={() => setHeadMenu(x => !x)} style={{padding:'5px 10px',fontSize:14,fontWeight:800,minWidth:34}}>⚙</button>
              {headMenu && <div role="menu" data-testid="head-menu" style={{position:'absolute',right:0,top:'calc(100% + 6px)',zIndex:60,background:'#fffefa',border:'1.5px solid var(--navy-line)',borderRadius:12,padding:'10px 12px',boxShadow:'0 8px 24px rgba(38,41,107,0.14)',minWidth:200,display:'flex',flexDirection:'column',gap:10}}>
                <div><div style={{fontSize:11,fontWeight:900,color:'var(--muted)',letterSpacing:'0.06em',textTransform:'uppercase',marginBottom:5}}>{t('Language', '언어')}</div>
                  <div style={{display:'flex',gap:5}}>{[['en', 'English'], ['ko', '한국어']].map(([k, l]) => <button key={k} className={'chip' + (lang === k ? ' active' : '')} onClick={() => { if (lang !== k) toggleLang(); }} style={{padding:'4px 12px',fontSize:13,fontWeight:800}}>{l}</button>)}</div></div>
                {lang !== 'ko' && <div><div style={{fontSize:11,fontWeight:900,color:'var(--muted)',letterSpacing:'0.06em',textTransform:'uppercase',marginBottom:5}}>{t('Note names', '음 이름')}</div>
                  <button className={'chip' + (solfaEn ? ' active' : '')} onClick={toggleSolfa} title="Show fixed-do syllables (C = Do) beside the letter names" style={{padding:'4px 12px',fontSize:13,fontWeight:800}}>{solfaEn ? 'Do Re Mi: on' : 'Do Re Mi: off'}</button></div>}
              </div>}
            </div>}""")
rep("  const [findOpen, setFindOpen] = useState(false);", "  const [findOpen, setFindOpen] = useState(false);\n  const [headMenu, setHeadMenu] = useState(false);   // m12: the teacher's ⚙ menu")
open(p, 'w', encoding='utf-8').write(h); print('m12 ok')
