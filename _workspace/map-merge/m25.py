p='drills.src.html'; s=open(p).read()
if 'm25' in s: print('already'); raise SystemExit
old="    const lang = tm.term === 'M.M.' ? 'en' : fr ? 'fr' : 'it';"
assert s.count(old)==1
s=s.replace(old,"    const lang = tm.lang || (tm.term === 'M.M.' ? 'en' : fr ? 'fr' : 'it');   // m25: a word may bring its own language")
old="    u.lang = lang === 'it' ? 'it-IT' : lang === 'fr' ? 'fr-FR' : 'en-AU'; u.rate = 0.8;"
assert s.count(old)==1
s=s.replace(old,"    u.lang = lang === 'it' ? 'it-IT' : lang === 'fr' ? 'fr-FR' : lang === 'de' ? 'de-DE' : 'en-AU'; u.rate = 0.8;")
old="""      <span style={{color:BK.muted}}> · </span><span>{w.mean}</span></div>
    <span style={{display:'flex',gap:4,alignItems:'center'}}>{w.tm && <RefHear k={'w' + w.term} on={() => playTerm(w.tm)}/>}<RefDoor room={w.room} g={w.g}/></span>"""
assert s.count(old)==1
s=s.replace(old,"""      {PRON[w.term] ? <span style={{color:BK.muted,fontSize:'0.82em',fontStyle:'italic'}}> [{PRON[w.term]}]</span> : null}<span style={{color:BK.muted}}> · </span><span>{w.mean}</span></div>
    <span style={{display:'flex',gap:4,alignItems:'center'}}><RefSay term={w.term} lang={w.lang}/>{w.tm && <RefHear k={'w' + w.term} on={() => playTerm(w.tm)}/>}<RefDoor room={w.room} g={w.g}/></span>""")
old="function RefWordRow({ w }) {"
s=s.replace(old,"""// m25 (her 'it would be nice to hear how the words are said'): 🗣 says the word in its language (the device's own voice)
function RefSay({ term, lang }) {
  if (React.useContext(RefPaper)) return null;
  let ok = false; try { ok = !!window.speechSynthesis; } catch (e) {}
  if (!ok || !term) return null;
  return <button type="button" className="chip" data-ref-say={term} aria-label={t('Say ', '발음 ') + term} title={t('How it is said', '발음 듣기')} onClick={() => speakTerm({ term, lang })}
    style={{minHeight:28,minWidth:30,padding:'2px 7px',fontSize:13,lineHeight:1}}>🗣</button>;
}
"""+old,1)
open(p,'w').write(s); print('ok')
