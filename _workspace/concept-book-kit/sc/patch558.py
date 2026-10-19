import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# her 15:49: in her turn she taps the white key, then taps the sharp key itself on the keyboard (no button)
rep("  const [from, setFrom] = useState(null), [to, setTo] = useState(null);\n  const timers = useRef([]);",
    "  const [from, setFrom] = useState(null), [to, setTo] = useState(null), [miss, setMiss] = useState(null);\n  const timers = useRef([]);")
rep("""    const go = () => { if (!ok(from)) return; clear(); setTo(target(from)); setNonce(n => n + 1); snd(from, 0.4); timers.current.push(setTimeout(() => snd(target(from), 0.6), 450)); };
    const line = from == null ? t('Tap a white key. Then press ' + D.word[0] + '.', '흰건반을 눌러요. 그다음 ' + D.word[1] + '을 눌러요.')
      : to != null ? t(en(from), ko(from))
      : !isW(from) ? t('Tap a white key.', '흰건반을 눌러요.')
      : !ok(from) ? t('Tap a white key in the middle.', '가운데 흰건반을 눌러요.')
      : t('Now press ' + D.word[0] + '.', '이제 ' + D.word[1] + '을 눌러요.');""",
"""    const tap = (k) => {
      clear(); snd(k, 0.5);
      if (from != null && to == null && ok(from) && k === target(from)) { setTo(k); setMiss(null); setNonce(n => n + 1); return; }   // the sharp key itself
      if (ok(k)) { setFrom(k); setTo(null); setMiss(null); setNonce(n => n + 1); return; }                                          // a new white key
      setMiss(from != null && to == null ? 'wrong' : 'white'); setNonce(n => n + 1);
    };
    const line = from == null ? (miss ? t('Tap a white key first.', '먼저 흰건반을 눌러요.') : t('Tap a white key.', '흰건반을 눌러요.'))
      : to != null ? t(en(from), ko(from))
      : miss === 'wrong' ? t('Not that one. Where is the ' + D.word[0] + ' of ' + L(from) + '?', '그 건반이 아니에요. ' + L(from) + ' ' + D.word[1] + '은 어디일까요?')
      : t('Now tap the ' + D.word[0] + ' of ' + L(from) + '.', '이제 ' + L(from) + ' ' + D.word[1] + ' 건반을 눌러요.');""")
rep("onTap={(k) => { clear(); setFrom(k); setTo(null); setNonce(n => n + 1); snd(k, 0.5); }}/>\n      <div style={lineStyle}>{line}</div>\n      {row(<button className=\"ghost-btn\" style={{...KF_BTN,minWidth:150,opacity:ok(from) && to == null ? 1 : 0.4}} disabled={!ok(from) || to != null} onClick={go}>{t(D.btn[0], D.btn[1])}</button>)}\n",
    "onTap={tap}/>\n      <div style={lineStyle}>{line}</div>\n")
rep("  useEffect(() => clear, []);\n  const snd = (k, d) => { if (k >= 0) playKey(k, d); };\n  const EX = D.order", "  useEffect(() => clear, []);\n  useEffect(() => { setMiss(null); }, [view]);\n  const snd = (k, d) => { if (k >= 0) playKey(k, d); };\n  const EX = D.order")
# one name for every copy-link button
rep("(LANG === 'ko' ? '학생 링크 복사' : 'Copy student link')", "(LANG === 'ko' ? '링크 복사' : 'Copy link')")
rep("t('Copy student link', '학생 링크 복사')", "t('Copy link', '링크 복사')")
rep("(LANG === 'ko' ? '학생 링크' : 'Student link')", "(LANG === 'ko' ? '링크 복사' : 'Copy link')")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
