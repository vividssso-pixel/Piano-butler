p='drills.src.html'; s=open(p).read()
if 'm17' in s: print('already'); raise SystemExit
# 1. favourites + per-book tools in RefShelf
s=s.replace("function RefShelf({ onChapter, onHouse }) {","const SHELF_TOOLS = { time: [['metronome', 'Metronome', '메트로놈']], scales: [['scale-finder', 'Scale finder', '스케일 찾기']] };   // m17\nconst SHELF_FAVS = [['scale-finder', 'Scale finder', '스케일 찾기'], ['metronome', 'Metronome', '메트로놈']];   // m17: for now (her 'like a favourites list, for now')\nfunction RefShelf({ onChapter, onHouse, onTool }) {",1)
favrow='''    {onTool && <div data-ref-favs style={{display:'flex',alignItems:'center',gap:6,flexWrap:'wrap',margin:'10px 0 0'}}><span style={{fontSize:10.5,fontWeight:900,letterSpacing:'0.1em',textTransform:'uppercase',color:'#4a4d86'}}>★ {t('Favourites', '즐겨찾기')}</span>
      {SHELF_FAVS.map(([id, en, ko2]) => <button key={id} type="button" className="chip" data-ref-fav={id} onClick={() => onTool(id)} style={{padding:'4px 12px',fontSize:13,fontWeight:800}}>{t(en, ko2)}</button>)}</div>}
    {REF_SHELVES.map('''
s=s.replace("    {REF_SHELVES.map(",favrow,1)
s=s.replace("      <RefHead id={s.id}/><B/>\n    </section>}","      <RefHead id={s.id}/>\n      {onTool && SHELF_TOOLS[s.id] && <div style={{display:'flex',gap:6,flexWrap:'wrap',margin:'0 0 10px'}}>{SHELF_TOOLS[s.id].map(([id, en, ko2]) => <button key={id} type=\"button\" className=\"ghost-btn\" data-ref-tool={id} onClick={() => onTool(id)} style={{padding:'6px 14px',fontSize:13.5}}>{t(en, ko2)} ›</button>)}</div>}\n      <B/>\n    </section>}",1)
old="<RefShelf onChapter={jumpToChapter} onHouse="
assert s.count(old)==1
s=s.replace(old,"<RefShelf onChapter={jumpToChapter} onTool={(id) => { update({ view: 'tools', tool: id, ret: 'toolbox', lib: false }); try { window.scrollTo(0, 0); } catch (e) {} }} onHouse=")
old="st.ret === 'home' ? homeBack : toolBackCh ?"
assert s.count(old)==1
s=s.replace(old,"st.ret === 'home' ? homeBack : (st.ret === 'toolbox' && T) ? t('← Library', '← 서재') : toolBackCh ?")
# 2. the House intro, short (A/B)
old2="text={t('The Piano Butler’s house: ' + houseFloors() + ', a room for each chapter. Your butler meets you in the hall. Open the door and go up, floor by floor; on each floor, any room first. New to the piano? Start on Beginner. Already playing? Go straight to any room, or carry on with the button.', '피아노 버틀러의 집: ' + houseFloors(true) + ', 챕터마다 방 하나. 버틀러가 현관에서 맞아 줘요. 문을 열고 한 층씩 올라가요. 같은 층에서는 어느 방부터 해도 돼요. 처음이라면 Beginner부터, 이미 배우고 있다면 어느 방으로든 바로 가거나 버튼을 눌러 이어서 해요.')}"
assert s.count(old2)==1, 'intro'
s=s.replace(old2,"text={<>{t((['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve'][houseFloorsN()] || houseFloorsN()) + ' floors of music. ', houseFloorsN() + '층의 음악. ')}<b style={{color:'var(--navy)'}}>{t('Open any door', '아무 문이나 열고')}</b>{t(' and climb.', ' 올라가요.')}</>}   /* m17: her 'too long, nobody reads it' */")
# MapHead: no big button when nothing is started
old3="      {next\n        ? <button className=\"primary-btn\" data-testid=\"map-continue\""
assert s.count(old3)==1, 'head'
s=s.replace(old3,"      {next && focus.kind === 'start'\n        ? <div data-testid=\"map-door-hint\" style={{fontSize:13.5,color:'#4a4d86',margin:'2px 0 0'}}>{t('The front door is just below: tap it to go in.', '현관문은 바로 아래에 있어요. 눌러서 들어가요.')}</div>\n        : next\n        ? <button className=\"primary-btn\" data-testid=\"map-continue\"",1)
open(p,'w').write(s); print('ok')
