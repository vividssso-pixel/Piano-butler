#!/usr/bin/env python3
"""Build DO (on t789 -> t790; call 31, her 21:23, 21:25 and 21:41): the dictionary. Reads terms31.json (the term cards)
and bring31.json (each chapter's 'Bring with you' terms, baked from the Lesson Books' text by scan31.js) next to this script.
Usage: python3 patch790.py t789.src.html t790.src.html"""
import json, sys, os
src, dst = sys.argv[1], sys.argv[2]
D = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(D, 'terms31.json'), encoding='utf-8')); B = json.load(open(os.path.join(D, 'bring31.json'), encoding='utf-8'))
terms_js = ',\n'.join("  { id: %s, room: %s, en: %s, ko: %s, defEn: %s, defKo: %s }" % (json.dumps(t['id']), json.dumps(t['room']), json.dumps(t['en'], ensure_ascii=False), json.dumps(t['ko'], ensure_ascii=False), json.dumps(t['defEn'], ensure_ascii=False), json.dumps(t['defKo'], ensure_ascii=False)) for t in T)
bring_js = json.dumps(B, ensure_ascii=False)
code = open(os.path.join(D, 'terms31.code.js'), encoding='utf-8').read().replace('__TERMS__', terms_js).replace('__BRING__', bring_js)
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
R("""function LbPage({ no, chId, kicker, title, teacher, qr, book, head, children }) {""", code + """
function LbPage({ no, chId, kicker, title, teacher, qr, book, head, children }) {""")
R("""  return <p className="lb-say" style={{fontSize:Math.max(size + 1.5, 18),lineHeight:1.55,fontWeight:500,color:BK.ink,margin:'2px 0'}}>{children}</p>;""",
  """  return <p className="lb-say" style={{fontSize:Math.max(size + 1.5, 18),lineHeight:1.55,fontWeight:500,color:BK.ink,margin:'2px 0'}}><Gloss>{children}</Gloss></p>;   // Build DO: the earlier rooms' words are links on screen""")
R("""            <span style={{flex:1,paddingTop:1}}>{s}</span>
            <LbTick label={t('Done', '했어요') + ' ' + (i + 1)}/>""", """            <span style={{flex:1,paddingTop:1}}><Gloss>{s}</Gloss></span>
            <LbTick label={t('Done', '했어요') + ' ' + (i + 1)}/>""")
R("""        <span className="lb-rem-txt" style={{fontSize:16.5,fontWeight:800,color:BK.ink,minWidth:0}}>{children}</span>""",
  """        <span className="lb-rem-txt" style={{fontSize:16.5,fontWeight:800,color:BK.ink,minWidth:0}}><Gloss>{children}</Gloss></span>""")
R("""      <BkChapterCtx.Provider value={page.props.chId}>
        <div className="lb-screen" data-lb-screen={page.props.no} style={{display:'flex',flexDirection:'column',gap:14,margin:'4px 0 6px'}}>
          {lbWordsFirst(children)}""", """      <BkChapterCtx.Provider value={page.props.chId}>
        <div className="lb-screen" data-lb-screen={page.props.no} style={{display:'flex',flexDirection:'column',gap:14,margin:'4px 0 6px'}}>
          <GlossSeen.Provider value={new Set()}>{lbWordsFirst(children)}</GlossSeen.Provider>""")
R("""      {!noArt && <ChapterArt id={STAFF_ART[id] ? id : String(id).split('-')[0]}/>}
      {head}""", """      {!noArt && <ChapterArt id={STAFF_ART[id] ? id : String(id).split('-')[0]}/>}
      {head}
      {DICT_BRING[id] && <DictChips ch={id}/>}""")
R("""      <div className="bk-body" style={{flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column',gap:16}}><BkChapterCtx.Provider value={chId}>{lbWordsFirst(children)}</BkChapterCtx.Provider></div>""",
  """      <div className="bk-body" style={{flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column',gap:16}}><BkChapterCtx.Provider value={chId}>{lbWordsFirst(children)}{!title && DICT_BRING[chId] && <LbOnly print><div data-term-print={chId} style={{fontSize:11.5,color:BK.muted,fontWeight:700,marginTop:'auto'}}>{t('Bring with you: ', '가져올 것: ') + DICT_BRING[chId].filter(id => dictEarlier(id, chId)).map(id => dictName(DICT_BY_ID[id]) + ' (' + (LANG === 'ko' ? bkChapterNo(DICT_BY_ID[id].room) + '장' : 'ch. ' + bkChapterNo(DICT_BY_ID[id].room)) + ')').join(' · ')}</div></LbOnly>}</BkChapterCtx.Provider></div>""")
R("""  return (
    <div style={{minHeight:'100vh',background:'var(--bg)'}}>
      <div style={{background:'var(--bg)',padding:'14px 16px 30px',backgroundImage:""", """  const [term, setTerm] = useState(null);   // Build DO: the dictionary card
  const termCtx = useMemo(() => ({ open: (id) => setTerm(id), room: (id) => { setTerm(null); jumpToChapter(id); } }), [st.view]);
  return (
    <DictCtx.Provider value={termCtx}>
    <div style={{minHeight:'100vh',background:'var(--bg)'}}>
      {term && <DictCard id={term} onClose={() => setTerm(null)}/>}
      <div style={{background:'var(--bg)',padding:'14px 16px 30px',backgroundImage:""")
i = s.index("function App() {"); j = s.index("\n    </div>\n  );\n}\n", i)
s = s[:j] + "\n    </div>\n    </DictCtx.Provider>\n  );\n}\n" + s[j + len("\n    </div>\n  );\n}\n"):]
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
