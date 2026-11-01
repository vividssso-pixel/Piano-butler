p='drills.src.html'; s=open(p).read()
if 'm15' in s: print('already'); raise SystemExit
a="function SoundSettings() {"
s=s.replace(a,"function SoundSettings({ menu }) {   // m15: menu = inside the teacher's ⚙ menu, always open, no Done",1)
a2="  if (!open) return ("
assert s.count(a2)==1
s=s.replace(a2,"""  if (menu) return (
    <div data-testid="menu-sound" style={{display:'flex',flexDirection:'column',gap:6,fontSize:12.5,fontWeight:800,color:'#4a4d86'}}>
      <div style={{display:'flex',flexWrap:'wrap',gap:5}}>{chip(p.piano, t('Piano', '피아노'), () => set({ piano: true }))}{chip(!p.piano, t('Simple', '심플'), () => set({ piano: false }))}</div>
      <div style={{display:'flex',flexWrap:'wrap',gap:5,alignItems:'center'}}><span>{t('Count', '카운트')}</span>{chip(p.count === 'click', t('Click', '클릭'), () => set({ count: 'click' }))}{chip(p.count === 'voice', t('Voice 1 2 3 4', '음성 1 2 3 4'), () => set({ count: 'voice' }))}</div>
      <div style={{display:'flex',flexWrap:'wrap',gap:5}}>{p.count === 'click' ? [['wood', t('Woodblock', '우드블록')], ['tick', t('Tick', '틱')], ['beep', t('Beep', '삐')]].map(([k, l]) => <React.Fragment key={k}>{chip((p.click || 'wood') === k, l, () => set({ click: k }))}</React.Fragment>)
        : [['heart', t('Female (US)', '여성 (US)')], ['emma', t('Female (UK)', '여성 (UK)')], ['michael', t('Male', '남성')], ['myvoice', t('My voice', '내 목소리')]].map(([k, l]) => <React.Fragment key={k}>{chip((p.voice || 'heart') === k, l, () => set({ voice: k }))}</React.Fragment>)}</div>
      {p.count === 'voice' && p.voice === 'myvoice' && <MyVoiceRecorder/>}
    </div>
  );
"""+a2,1)
# global line: hide for teacher (it lives in the menu)
old="""          </div>
        )}
        <SoundSettings/>
"""
assert s.count(old)==1
s=s.replace(old,"""          </div>
        )}
        {!(T && !st.lock) && <SoundSettings/>}
""")
# menu: add a Sound block after Note names
old2="""{solfaEn ? 'Do Re Mi: on' : 'Do Re Mi: off'}</button></div>}
              </div>}"""
assert s.count(old2)==1
s=s.replace(old2,"""{solfaEn ? 'Do Re Mi: on' : 'Do Re Mi: off'}</button></div>}
                <div><div style={{fontSize:11,fontWeight:900,color:'var(--muted)',letterSpacing:'0.06em',textTransform:'uppercase',marginBottom:5}}>{t('Sound', '소리')}</div><SoundSettings menu/></div>
              </div>}""")
s=s.replace("boxShadow:'0 8px 24px rgba(38,41,107,0.14)',minWidth:200,display:'flex',flexDirection:'column',gap:10}}>","boxShadow:'0 8px 24px rgba(38,41,107,0.14)',minWidth:200,width:'min(300px, calc(100vw - 32px))',display:'flex',flexDirection:'column',gap:10}}>",1)
open(p,'w').write(s); print('ok')
