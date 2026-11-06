#!/usr/bin/env python3
# Phase 407: her three notes on the v2 print (Sohyun 2026-10-09 23:34)
#   1. page 5's labels were clipped (the top pad shrank too far in Phase 406) -- restored; and the clef intro now
#      reads as an equation: treble clef = the Queen, bass clef = the King ('높은음자리표=여왕얼굴')
#   2. page 6: ONE Princess Clara between the staves -- visiting the Queen her C is written just under the treble
#      staff, visiting the King just over the bass staff ('사람을 하나로 하고...')
#   3. the Workbook's framed opener/check pages printed a 'Lesson Book' header ('이건 중간에 왜 또 나와?') --
#      LbPage takes a book name, lbFramed passes 'Workbook'
#   python3 patch407.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# 1a. page 5's top pad back up -- the letter row above the staff was clipped
rep("""  const p5 = <SfStaff clef="bass" width={340} pad={[30, 46]}""", """  const p5 = <SfStaff clef="bass" width={340} pad={[48, 46]}""", 'p5 pad')
# 1b. the clef intro as an equation: the sign = its owner
rep("""      <PenArt shapes={clef === 'treble' ? sfQueen(26, 28, 1.2) : sfKing(26, 28, 1.2)} vb={[0, 0, 52, 58]} style={{width:82,flex:'0 0 auto'}} label={clef === 'treble' ? t('the Queen', '여왕') : t('the King', '왕')}/>""",
    """      <div style={{fontSize:34,fontWeight:900,color:BK.ink,flex:'0 0 auto',lineHeight:1}} aria-hidden="true">=</div>
      <PenArt shapes={clef === 'treble' ? sfQueen(26, 28, 1.2) : sfKing(26, 28, 1.2)} vb={[0, 0, 52, 58]} style={{width:82,flex:'0 0 auto'}} label={clef === 'treble' ? t('the Queen', '여왕') : t('the King', '왕')}/>""", 'clef equation')
rep("""    return <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:30,width:'100%'}}>""",
    """    return <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:22,width:'100%'}}>""", 'intro gap')

# 2. page 6: one Clara, two visits
old6 = s[s.index("  const p6 = <SfStaff clef=\"grand\" width={340} pad={[26, 30]}"):]
old6 = old6[:old6.index("</g>}/>;") + len("</g>}/>;")]
rep(old6, """  const p6 = <SfStaff clef="grand" width={340} pad={[26, 30]} label={t('The grand staff with one Princess Clara between the two staves; visiting the Queen, her middle C is written on its ladder rung just under the treble staff; visiting the King, just over the bass staff -- dotted paths join Clara to both notes: the same key', '큰보표, 두 오선 사이에 클라라 공주 한 명; 여왕네 갈 때는 가운데 도를 높은음자리표 오선 바로 아래 사다리 발판에, 왕네 갈 때는 낮은음자리표 오선 바로 위에 써요 -- 점선이 공주와 두 음표를 이어요: 같은 건반')}
    notes={[{ d: 28, x: 104, staff: 'treble', color: PEN_C }, { d: 28, x: 266, staff: 'bass', color: PEN_C }]}
    icons={[SF_ICON(clara, 172, 116, 0.62)]}
    extra={(yOf, layer, txt) => layer === 'over' && <g style={txt}>
      <path d={`M168 134 Q136 128 112 ${yOf(28, 'treble') + 9}`} fill="none" stroke={BK.coral} strokeWidth="1.4" strokeDasharray="4 3.5"/>
      <path d={`M204 134 Q236 140 258 ${yOf(28, 'bass') - 9}`} fill="none" stroke={BK.coral} strokeWidth="1.4" strokeDasharray="4 3.5"/>
      <text x="104" y={yOf(28, 'treble') - 12} fontSize="9" fontWeight="900" fill={BK.ink} textAnchor="middle">{t('visiting the Queen', '여왕네 갈 때')}</text>
      <text x="104" y={yOf(28, 'treble') + 20} fontSize="8" fontWeight="800" fill={BK.muted} textAnchor="middle">{t('just under her staff', '여왕의 오선 바로 아래')}</text>
      <text x="266" y={yOf(28, 'bass') - 16} fontSize="8" fontWeight="800" fill={BK.muted} textAnchor="middle">{t('just over his staff', '왕의 오선 바로 위')}</text>
      <text x="266" y={yOf(28, 'bass') + 21} fontSize="9" fontWeight="900" fill={BK.ink} textAnchor="middle">{t('visiting the King', '왕네 갈 때')}</text>
      <text x="186" y="160" fontSize="9.5" fontWeight="900" fill={BK.coral} textAnchor="middle">{t('the same key!', '같은 건반!')}</text>
    </g>}/>;""", 'p6 one clara')
rep("""공주의 음은 자기만의 <b>작은 사다리 발판</b>에 써요: 여왕의 오선에 붙을 땐 <b>바로 아래</b>, 왕의 오선에 붙을 땐 <b>바로 위</b>. 종이에서는 두 자리처럼 보여도 피아노에서는 <b>한 건반</b> -- 그래서 클라라가 양쪽에 서 있어요.""",
    """공주는 <b>한 명</b>이고, 음도 자기만의 <b>작은 사다리 발판</b> 하나뿐이에요. <b>여왕네 갈 때</b>는 여왕의 오선 바로 아래에 쓰고, <b>왕네 갈 때</b>는 왕의 오선 바로 위에 써요. 종이에서는 두 자리처럼 보여도 피아노에서는 <b>같은 건반</b>이에요.""", 'p6 ko say')
rep("""Her note is written on <b>a little ladder rung of its own</b>: <b>just under</b> the Queen's staff when it belongs up there, <b>just over</b> the King's when it belongs down. Two places on paper, <b>one key</b> on the piano -- that is why Clara stands by both.""",
    """There is <b>one Clara</b>, and she has <b>one little ladder rung of her own</b>. <b>Visiting the Queen</b>, her note is written just under the Queen's staff; <b>visiting the King</b>, just over his. Two places on paper -- <b>the same key</b> on the piano.""", 'p6 en say')

# 3. the Workbook's framed pages say Workbook in the header
rep("""function LbPage({ no, chId, kicker, title, teacher, qr, children }) {""",
    """function LbPage({ no, chId, kicker, title, teacher, qr, book, children }) {""", 'lbpage prop')
rep("""        <span><b style={{color:BK.ink}}>Piano Butler</b> · Lesson Book</span>""",
    """        <span><b style={{color:BK.ink}}>Piano Butler</b> · {book || 'Lesson Book'}</span>""", 'lbpage header')
rep("""  return [React.cloneElement(lb[0], { key: 'frame-open', no: startNo }), ...pages, React.cloneElement(lb[lb.length - 1], { key: 'frame-check', no: startNo + 1 + pages.length })];""",
    """  return [React.cloneElement(lb[0], { key: 'frame-open', no: startNo, book: 'Workbook' }), ...pages, React.cloneElement(lb[lb.length - 1], { key: 'frame-check', no: startNo + 1 + pages.length, book: 'Workbook' })];""", 'framed book name')

open(src, 'w', encoding='utf-8').write(s); print('patch407 ok')
