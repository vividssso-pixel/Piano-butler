import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("second-to-last","second last",4)
# one-flat exception example in the flat rule
rep("  const EX = sharp ? [3, 5, 2] : [3, 5, 2];\n  const n = EX[e], k = KEY_BY_COUNT(type, n), marks = {};\n  const want = sharp ? n - 1 : n - 2;\n  const lastNm = (sharp ? SHARP_ORDER : FLAT_ORDER)[want];\n  marks[pcOfName(lastNm)] = r === 0 ? 'pick' : 'mate';\n  if (r === 1) marks[pcOfName(k.major)] = 'pick';",
"""  const EX = sharp ? [3, 5, 2] : [3, 5, 1];   // flats end with the exception: one flat is F
  const n = EX[e], k = KEY_BY_COUNT(type, n), marks = {};
  const one = !sharp && n === 1;
  const want = sharp ? n - 1 : n - 2;
  const lastNm = one ? 'F' : (sharp ? SHARP_ORDER : FLAT_ORDER)[want];
  if (one) marks[pcOfName('F')] = 'pick';
  else { marks[pcOfName(lastNm)] = r === 0 ? 'pick' : 'mate'; if (r === 1) marks[pcOfName(k.major)] = 'pick'; }""")
rep("  const say = r === 0\n    ? (sharp","  const say = one ? t('With one ♭ there is no second last. The key is just F.', '플랫이 하나면 뒤에서 두 번째가 없어요. 그냥 F예요.') : r === 0\n    ? (sharp")
rep("tonicPos = r === 1 ? (sharp ?","tonicPos = r === 1 && !one ? (sharp ?")
rep("ring={want} tallBox={sharp} tonicPos={tonicPos}","ring={one ? undefined : want} tallBox={sharp} tonicPos={tonicPos}")
rep("visibility:r === 1 ? 'visible' : 'hidden'}}>{n}","visibility:r === 1 || one ? 'visible' : 'hidden'}}>{n}")
rep("{!sharp && r === 0 ? t('One ♭ is the exception: it is F.', '플랫이 하나면 예외예요: F.') : ''}","")
rep("      {r === 1 ? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => setR(0)}>","      {one ? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => { setE(e - 1); setR(1); }}>{t('← Back', '← 이전')}</button>\n        : r === 1 ? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => setR(0)}>")
rep("onClick={r === 0 ? () => { setR(1); playKey(pcOfName(k.major), 0.5); } : more ? () => { setE(e + 1); setR(0); } : go}>{r === 0 ? t('Next →', '다음 →') :",
    "onClick={r === 0 && !one ? () => { setR(1); playKey(pcOfName(k.major), 0.5); } : more ? () => { setE(e + 1); setR(0); } : go}>{r === 0 && !one ? t('Next →', '다음 →') :")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
