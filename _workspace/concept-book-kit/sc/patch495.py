#!/usr/bin/env python3
# Phase 495: the concept book 'Scales and keys' follows the Key finder and Scale finder steps.
# One page per step, one picture, one line. On screen the book IS the step screens (Learn opens the Key finder);
# the printed book carries the same pages. The old pages stay in the file as cbScalesPagesOld (hidden, not deleted).
#   python3 patch495.py in.src.html out.src.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:110]))
    s = s.replace(a, b)

rep("function cbScalesPages(scr = false) {", "function cbScalesPagesOld(scr = false) {   // Phase 495: the old nine pages, kept but no longer used")

NEW = r"""
// ── Phase 495: the new book: one page per step of the Key finder (4) and the Scale finder (3) ──
function CbFindPic({ type, n }) {
  const sharp = type === 'sharp', sym = sharp ? '♯' : '♭', order = sharp ? SHARP_ORDER : FLAT_ORDER, words = KF_WORDS[type];
  const k = KEY_BY_COUNT(type, n), want = sharp ? n - 1 : n - 2, marks = {};
  if (sharp) marks[pcOfName(order[want])] = 'mate';
  marks[pcOfName(k.major)] = 'pick';
  return <div role="img" aria-label={t(n + sym + ' is ' + prettyNote(k.major) + ' major. The sharps or flats in order, then the key.', n + sym + '은 ' + prettyNote(k.major) + '장조.')} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:16,width:'100%',maxWidth:540}}>
    <div aria-hidden="true" style={{width:'100%',maxWidth:440}}><KSStaff count={n} type={type} width={420}/></div>
    <div aria-hidden="true" style={{display:'flex',flexWrap:'wrap',gap:'0 8px',justifyContent:'center',fontSize:20,fontWeight:700,lineHeight:1.5}}>
      {words.map((w, i) => <span key={i} style={{opacity:i < n ? 1 : 0.22,color:i === n - 1 ? '#c8361b' : '#26296b',fontWeight:i === n - 1 ? 900 : 700}}>{w}</span>)}
    </div>
    {!sharp && <div aria-hidden="true" style={{fontSize:13,color:'#5a5d8f',marginTop:-8}}>{t('the same sentence backwards', '같은 문장을 거꾸로')}</div>}
    <div aria-hidden="true" style={{display:'flex',gap:6,justifyContent:'center'}}>
      {order.slice(0, n).map((nm, i) => <span key={nm} style={{minWidth:56,textAlign:'center',padding:'9px 8px',borderRadius:14,border:'1.5px solid #26296b',fontWeight:900,fontSize:22,background:i === want ? '#26296b' : '#fff',color:i === want ? '#fffefa' : '#26296b',opacity:i === want ? 1 : 0.45}}>{prettyNote(nm)}</span>)}
    </div>
    <div aria-hidden="true" style={{width:'100%',maxWidth:480}}><TapKeyboard octaves={1} marks={marks} labels="all" bigLabels/></div>
    <div aria-hidden="true" style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:32,fontWeight:900,color:'#26296b'}}>{n}{sym} → <span style={{color:'#c0431f'}}>{majName(k)}</span></div>
  </div>;
}
function CbMinorPic() {
  const ks = KEY_SIGS.find(q => q.major === 'A') || KEY_SIGS[0], marks = {};
  marks[pcOfName(ks.minor)] = 'mate'; marks[pcOfName(ks.major)] = 'pick';
  const card = (txt, strong) => <div style={{flex:'1 1 0',textAlign:'center',padding:'10px 6px',borderRadius:12,fontWeight:900,fontSize:26,background:strong ? '#e4572e' : '#fbe3da',color:strong ? '#fff' : '#26296b',border:'1.5px solid ' + (strong ? '#c0431f' : '#e9b9a6')}}>{txt}</div>;
  return <div role="img" aria-label={t(prettyNote(ks.major) + ' major and ' + prettyNote(ks.minor) + ' minor share one key signature. From the major, count 3 half steps down.', prettyNote(ks.major) + '장조와 ' + prettyNote(ks.minor) + '단조는 조표가 같아요. 장조에서 반음 3칸 아래.')} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:18,width:'100%',maxWidth:540}}>
    <div aria-hidden="true" style={{width:'100%',maxWidth:380}}><KSStaff count={ks.count} type={ks.type} width={360}/></div>
    <div aria-hidden="true" style={{display:'flex',gap:10,width:'100%',maxWidth:460}}>{card(cbNoteElName(ks.major, t(' major', '장조')), true)}{card(cbNoteElName(ks.minor, t(' minor', '단조')), false)}</div>
    <div aria-hidden="true" style={{width:'100%',maxWidth:480}}><TapKeyboard octaves={1} marks={marks} labels="all" bigLabels/></div>
  </div>;
}
function CbChainBig({ at }) {
  const items = [t('Read it', '읽기'), t('Name the key', '조 찾기'), t('Play its scale', '스케일 치기')];
  return <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,width:'100%'}}>
    {items.map((l, i) => <React.Fragment key={i}>{i > 0 && <span style={{color:'#a3a5c2',fontWeight:800,fontSize:18}}>→</span>}<span style={{flex:'1 1 0',minWidth:0,textAlign:'center',padding:'12px 6px',borderRadius:22,fontSize:19,fontWeight:800,background:at === i ? '#e4572e' : '#efe8d6',color:at === i ? '#fff' : '#26296b'}}>{l}</span></React.Fragment>)}
  </div>;
}
function CbPiecePic() {
  const ks = KEY_SIGS.find(q => q.major === 'D') || KEY_SIGS[0];
  return <div role="img" aria-label={t('Before a piece: read the key signature, name the key, play its scale once. Example: two sharps, D major.', '곡을 치기 전에: 조표를 읽고, 조를 찾고, 스케일을 한 번 쳐요. 예: 샤프 둘, D장조.')} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:26,width:'100%',maxWidth:560}}>
    <div aria-hidden="true" style={{width:'100%'}}><CbChainBig at={2}/></div>
    <div aria-hidden="true" style={{width:'100%',maxWidth:400}}><KSStaff count={ks.count} type={ks.type} width={380}/></div>
    <div aria-hidden="true" style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:36,fontWeight:900,color:'#26296b'}}>{majName(ks)} · {minName(ks)}</div>
  </div>;
}
function CbScalePic({ k, label }) {
  const info = scaleData(k, 'major') || SCALES.C, e = info.octaves[1];
  const sp = spellFor(k, 'major'), nmz = sp.concat([sp[0]]);
  return <div role="img" aria-label={label} style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:560}}>
    <div aria-hidden="true"><div style={{fontSize:12,fontWeight:900,color:'#5a5d8f',letterSpacing:'0.05em',marginBottom:2}}>{t('RIGHT', '오른손')}</div><ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.RH} hand="RH" names={nmz}/></div>
    <div aria-hidden="true"><div style={{fontSize:12,fontWeight:900,color:'#5a5d8f',letterSpacing:'0.05em',marginBottom:2}}>{t('LEFT', '왼손')}</div><ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.LH} hand="LH" names={nmz}/></div>
    <div aria-hidden="true" style={{display:'flex',gap:16,justifyContent:'center',fontSize:14,fontWeight:800,color:'#26296b'}}>
      <span style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:16,height:16,borderRadius:4,background:SEGMENT_COLORS.three.fill,border:'1.5px solid ' + SEGMENT_COLORS.three.stroke}}/>1-2-3</span>
      <span style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:16,height:16,borderRadius:4,background:SEGMENT_COLORS.four.fill,border:'1.5px solid ' + SEGMENT_COLORS.four.stroke}}/>1-2-3-4</span>
    </div>
  </div>;
}
function CbTwelvePic() {
  return <div role="img" aria-label={t('The twelve major keys, each a half step above the one before: C, D flat, D, E flat, E, F, F sharp, G, A flat, A, B flat, B.', '열두 장조, 한 칸마다 반음씩 위로: C, D♭, D, E♭, E, F, F♯, G, A♭, A, B♭, B.')} style={{display:'flex',alignItems:'center',justifyContent:'center',gap:22,flexWrap:'wrap',width:'100%'}}>
    <div aria-hidden="true" style={{width:'100%',maxWidth:300}}><KeyRing sel="C" o={{ shape: true, nums: false }}/></div>
    <div aria-hidden="true" style={{display:'grid',gridTemplateColumns:'repeat(4, 66px)',gap:10}}>
      {SF12.map((x, i) => <span key={x} style={{textAlign:'center',padding:'11px 0',borderRadius:14,border:'1.5px solid #26296b',fontWeight:900,fontSize:22,background:i === 0 ? '#26296b' : '#fff',color:i === 0 ? '#fffefa' : '#26296b'}}>{prettyNote(x)}</span>)}
    </div>
  </div>;
}
function cbScalesPages(scr = false) {
  const ch = 'scales', cid = 'p-scales', X = X5, head = cbRight(cid), book = cbBookName();
  const P = (no, kicker, title, pic, line, rem) => <LbPage key={no} no={no} chId={ch} head={head} book={book} kicker={kicker} title={title}>
    <LbPic h={470}>{pic}</LbPic>
    <LbSay size={19}>{line}</LbSay>
    {rem ? <LbRemember>{rem}</LbRemember> : null}
  </LbPage>;
  const kk = (n) => t('Find the key · step ' + n + ' of 4', '조 찾기 · 4단계 중 ' + n + '단계');
  const sk = (n) => t('Play the scales · step ' + n + ' of 3', '스케일 치기 · 3단계 중 ' + n + '단계');
  const steps = [
    [t('Sharps', '샤프'), 2], [t('Flats', '플랫'), 3], [t('Major and minor', '장조와 단조'), 4], [t('Before a piece', '곡 치기 전에'), 5],
    [t('White keys', '흰건반'), 6], [t('Black keys', '검은건반'), 7], [t('All twelve', '열두 조'), 8],
  ];
  const checksRows = [
    ['sig', t('I can say the order of sharps and of flats', '샤프의 순서와 플랫의 순서를 말할 수 있어요')],
    ['any', t('I can name the major key from its key signature', '조표를 보고 장조 이름을 말할 수 있어요')],
    ['minor', t('I can find the relative minor, 3 half steps down', '장조에서 반음 3칸 아래로 나란한조를 찾을 수 있어요')],
    ['steps', t('I can play a white-key major scale with fingering: right hand, left hand, both', '흰건반 장음계를 손가락 번호대로 오른손, 왼손, 양손으로 칠 수 있어요')],
    ['circle', t('I can play the major scale from all twelve keys, going up by half steps', '반음씩 올라가며 열두 조의 장음계를 칠 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? cbNbKo(x) : cbNbEn(x)]);
  const ic = {
    steps: [{ k: 'raw', svg: [0, 1, 2, 3].map(i => { const x = 6 + i * 21, c = i === 2 ? PEN_C : PEN_N; return '<path d="M' + x + ' 18 L' + x + ' 24 L' + (x + 17) + ' 24 L' + (x + 17) + ' 18" fill="none" stroke="' + c + '" stroke-width="' + (i === 2 ? 2.8 : 2) + '" stroke-linejoin="round"/>'; }).join('') }],
    any: [{ k: 'raw', svg: '<text x="46" y="28" text-anchor="middle" font-family="Inter, sans-serif" font-size="17" font-weight="900" fill="' + PEN_N + '">3♯ → A</text>' }],
    sig: [{ k: 'raw', svg: '<text x="46" y="30" text-anchor="middle" font-family="' + MUSIC_FONT.replace(/"/g, "'") + '" font-size="26" fill="' + PEN_C + '">♯♯♯</text>' }],
    circle: [{ k: 'raw', svg: '<circle cx="46" cy="20" r="15" fill="none" stroke="' + PEN_N + '" stroke-width="1.6" stroke-dasharray="3 3"/>' + Array.from({ length: 12 }, (_, i) => { const a = (-90 + i * 30) * Math.PI / 180; return '<circle cx="' + (46 + 15 * Math.cos(a)).toFixed(1) + '" cy="' + (20 + 15 * Math.sin(a)).toFixed(1) + '" r="' + (i === 0 ? 4.2 : 2.6) + '" fill="' + (i === 0 ? PEN_C : PEN_N) + '"/>'; }).join('') }],
    minor: [{ k: 'raw', svg: '<text x="46" y="28" text-anchor="middle" font-family="Inter, sans-serif" font-size="17" font-weight="900" fill="' + PEN_N + '">C → Am</text>' }],
  };
  return [
    <LbPage key="1" no={1} chId={ch} head={head} book={book}>
      <div data-ch={cid}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>{(TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + cbBookName()).toUpperCase()}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Scales and keys', '스케일과 조')}</div>
      </div>
      <LbSay size={19}>{t('Find the key from its signature. Then play its scale.', '조표로 조를 찾아요. 그다음 그 조의 스케일을 쳐요.')}</LbSay>
      <LbPic h={120}><CbChainBig at={-1}/></LbPic>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:20}}>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this book', '이 책에서는')}</div>
          {steps.map(([n, p], i) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'3px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{i < 4 ? t('Key: ', '조: ') : t('Scale: ', '스케일: ')}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
          <div className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'3px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{t('My five checks', '나의 다섯 가지 확인')}</span><span style={{color:BK.muted,fontWeight:800}}>9</span></div>
        </div>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 책을 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'3px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{cbSx(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <div style={{display:'flex',justifyContent:'flex-end',alignItems:'center',gap:8,marginTop:'auto'}}>
        <span style={{fontSize:10.5,color:BK.muted}}>{t('the steps on screen', '화면으로 보기')}</span>
        <div style={{padding:4,border:'0.8px solid ' + BK.hair,borderRadius:2,background:'#fff',lineHeight:0}}><QR url={bkLink('tool=key-finder')} size={64}/></div>
      </div>
    </LbPage>,
    P(2, kk(1), t('What key has 3♯?', '샤프 3개는 무슨 조?'), <CbFindPic type="sharp" n={3}/>,
      X('Say the sharps in order. The last ♯ is the key’s 7th note: go a half step up.', '샤프를 순서대로 말해요. 마지막 샤프의 반음 위가 그 조의 으뜸음이에요.'),
      X('Sharps F C G D A E B. The key is a half step above the last ♯.', '샤프 F C G D A E B. 마지막 샤프의 반음 위가 장조.')),
    P(3, kk(2), t('What key has 3♭?', '플랫 3개는 무슨 조?'), <CbFindPic type="flat" n={3}/>,
      X('Say the flats in order. The key is the second-to-last ♭. One flat is F.', '플랫을 순서대로 말해요. 뒤에서 두 번째 플랫이 그 조예요. 플랫이 하나면 F.'),
      X('Flats B E A D G C F. The key is the second-to-last ♭.', '플랫 B E A D G C F. 뒤에서 두 번째 플랫이 장조.')),
    P(4, kk(3), t('Is it major or minor?', '장조일까, 단조일까?'), <CbMinorPic/>,
      X('The same signature has both. From the major, count 3 half steps down.', '조표는 같아요. 장조에서 반음 3칸 아래로 내려가면 단조.'),
      X('Minor: 3 half steps below the major.', '단조는 장조에서 반음 3칸 아래.')),
    P(5, kk(4), t('Before you play the piece', '곡을 치기 전에'), <CbPiecePic/>,
      X('Read the signature, name the key, then play its scale once.', '조표를 읽고, 조를 찾고, 그 스케일을 한 번 쳐요.')),
    P(6, sk(1), t('How do you play C major?', 'C장조는 어떻게 쳐요?'), <CbScalePic k="C" label={t('C major on the keys, with finger numbers: right hand, then left hand.', 'C장조 건반과 손가락 번호: 오른손, 그다음 왼손.')}/>,
      X('White keys first: right hand, then left hand, then both.', '흰건반부터: 오른손, 왼손, 그다음 양손.'),
      X('Finger groups: 1-2-3 and 1-2-3-4.', '손가락 묶음: 1-2-3, 1-2-3-4.')),
    P(7, sk(2), t('How do you play D♭ major?', 'D♭장조는 어떻게 쳐요?'), <CbScalePic k="Db" label={t('D flat major on the keys, with finger numbers: right hand, then left hand.', 'D♭장조 건반과 손가락 번호: 오른손, 그다음 왼손.')}/>,
      X('Now start on a black key: right hand, then left hand, then both.', '이번에는 검은건반에서 시작해요: 오른손, 왼손, 그다음 양손.')),
    P(8, sk(3), t('Twelve keys, a half step apart', '열두 조, 반음씩 올라가요'), <CbTwelvePic/>,
      X('Go up by a half step each time: right hand, then left hand, then both.', '반음씩 올라가요: 오른손, 왼손, 그다음 양손.')),
    <LbPage key="9" no={9} chId={ch} head={head} book={book} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, in the keys of your step.', '내가 있는 단계의 조로, 하나씩 피아노 앞에서 보여 줘요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, cbSx(x)])}/>} live={<FiveChecks376 storeKey="pb_five_cb_scales_v2" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, cbSx(x)])}/>}/>
    </LbPage>,
  ];
}
"""
rep("function CbScalesBook() { return <>{cbScalesPages(false)}</>; }", NEW + "function CbScalesBook() { return <>{cbScalesPages(false)}</>; }")

# screen: the book is the Key finder's steps
a = s.index("// on screen: the opener as the head, then one step a page")
b = s.index("TOOLS.push({ id: 'cb-p-scales'")
b2 = s.index("\n", b)
s = s[:a] + "// on screen (Phase 495): the book is the step screens themselves; this hidden entry keeps old links and QR codes working\n" + \
 "TOOLS.push({ id: 'cb-p-scales', ch: 'concept', title: 'Concept book: Scales and keys', blurb: 'Four steps to find the key, three to play the scales.', hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + cbBookName(); }, C: () => <KeyFinder/> });" + s[b2:]
rep("TOOL_KO['cb-p-scales'] = ['개념책: 스케일과 조', '규칙 하나, 모든 조를 한눈에, 그리고 단계별 연습.'];", "TOOL_KO['cb-p-scales'] = ['개념책: 스케일과 조', '조 찾기 네 단계, 스케일 치기 세 단계.'];")
rep("const CB_TOOL = { 'p-scales': 'cb-p-scales' };", "const CB_TOOL = { 'p-scales': 'key-finder' };")
rep("{t('The rule, every key at once, then the steps to practise it.', '규칙 하나, 모든 조를 한눈에, 그리고 단계별 연습.')}</div></div>", "{t('Find the key in four steps, play the scales in three.', '조 찾기 네 단계, 스케일 치기 세 단계.')}</div></div>")
# Home
rep("    learn: 'cb-p-scales', check: 'scales', tools: ['scale-finder', 'key-finder'],", "    learn: 'key-finder', check: 'scales', tools: ['scale-finder'],")
rep("    learnLine: ['One page: the rule, and all 12 keys at once', '한 장: 규칙, 그리고 12개 조를 한꺼번에'],\n    tryLine: ['Two tools: Scale finder, Key finder', '도구 둘: 스케일 찾기, 조 찾기'],",
    "    learnLine: ['Four steps: find the key from its signature', '네 단계: 조표로 조 찾기'],\n    tryLine: ['Three steps: white keys, black keys, all twelve', '세 단계: 흰건반, 검은건반, 열두 조'],")

# review fixes
rep("X('Say the sharps in order. The last ♯ is the key’s 7th note: go a half step up.', '샤프를 순서대로 말해요. 마지막 샤프의 반음 위가 그 조의 으뜸음이에요.')", "X('Say the sharps in order. The key is a half step above the last ♯.', '샤프를 순서대로 말해요. 마지막 샤프의 반음 위가 그 조예요.')")
rep("X('Say the flats in order. The key is the second-to-last ♭. One flat is F.', '플랫을 순서대로 말해요. 뒤에서 두 번째 플랫이 그 조예요. 플랫이 하나면 F.')", "X('Say the flats in order. The key is the second-to-last ♭. One flat is F.', '플랫을 말해요. 뒤에서 두 번째 플랫이 그 조예요. 하나면 F.')")
rep("function CbScalePic({ k, label }) {", "function CbScalePic({ k, label, legend = true }) {")
rep("    <div aria-hidden=\"true\" style={{display:'flex',gap:16,justifyContent:'center',fontSize:14,fontWeight:800,color:'#26296b'}}>\n      <span style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:16,height:16,borderRadius:4,background:SEGMENT_COLORS.three", "    {legend && <div aria-hidden=\"true\" style={{display:'flex',gap:16,justifyContent:'center',fontSize:14,fontWeight:800,color:'#26296b'}}>\n      <span style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:16,height:16,borderRadius:4,background:SEGMENT_COLORS.three")
rep("1-2-3-4</span>\n    </div>\n  </div>;\n}\nfunction CbTwelvePic", "1-2-3-4</span>\n    </div>}\n  </div>;\n}\nfunction CbTwelvePic")
rep("<CbScalePic k=\"Db\" label", "<CbScalePic k=\"Db\" legend={false} label")
rep("const href = '?book=concept&ch=' + cid + '&lang=en';", "const href = '?book=concept&ch=' + cid + '&lang=' + LANG;")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
