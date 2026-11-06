#!/usr/bin/env python3
# Phase 406: her five fixes on the applied chapter 4 (Sohyun 2026-10-09 23:16)
#   1. the Queen's earrings redrawn as little drop earrings (stem + pearl at the jaw), both sides
#   2. the paper check-up moves from the Lesson Book's last page into the Workbook (its own page 7)
#   3. line notes show the line through the hole on paper (PaperStaff) and on screen (StaffView)
#   4. Workbook p3 fills its page: 8 "your turn" cells, so "Which is higher?" stops ballooning
#   5. the clef signs are introduced BIG and on their own first -- the Queen's and King's faces leave the staff drawings
#   python3 patch406.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# 1. drop earrings: a short stem from the jaw, the pearl hanging below it
rep("""  s.push({ k: 'el', c: P(-5.9, 2.9), rx: 0.95 * k, ry: 1.2 * k, f: PEN_P, s: PEN_N, w: 0.7 }, { k: 'el', c: P(5.9, 2.9), rx: 0.95 * k, ry: 1.2 * k, f: PEN_P, s: PEN_N, w: 0.7 });   // pearl earrings, at the jaw""",
    """  [-1, 1].forEach(sx => s.push(penLine(P(5.7 * sx, 2.1), P(6.2 * sx, 3.3), 1), { k: 'el', c: P(6.35 * sx, 4.3), rx: 1.05 * k, ry: 1.25 * k, f: PEN_P, s: PEN_N, w: 0.8 }));   // drop earrings: a stem from the jaw, the pearl below""", 'earrings')

# 5a. the clef introduced on its own, big: the sign with its coral line, and its owner beside it -- not inside the staff
rep("""  // p4: the Queen's five -- C D E F G, from Clara up to the Queen's G; the curl wraps the second line""",
    """  // the clef on its own first (Phase 406): the sign big, its line in coral, its owner beside it -- out of the staff
  const clefIntro = (clef) => {
    const line = clef === 'treble' ? 32 : 24, L = clef === 'treble' ? 'G' : 'F';
    return <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:30,width:'100%'}}>
      <div style={{width:175,flex:'0 0 auto'}}>
        <SfStaff clef={clef} width={130} pad={[16, 16]} label={clef === 'treble' ? t('The treble clef, big: its curl wraps the G line, in coral', '높은음자리표를 크게: 소용돌이가 산호색 G 줄을 감싸요') : t('The bass clef, big: its two dots guard the F line, in coral', '낮은음자리표를 크게: 두 점이 산호색 F 줄을 지켜요')}
          extra={(yOf, layer, txt) => layer === 'under'
            ? <line x1="4" x2="126" y1={yOf(line)} y2={yOf(line)} stroke={BK.coral} strokeOpacity="0.55" strokeWidth="3.4"/>
            : <text x="114" y={yOf(line) + 4.5} fontSize="14" fontWeight="900" fill={BK.coral} textAnchor="middle" style={txt}>{L}</text>}/>
      </div>
      <PenArt shapes={clef === 'treble' ? sfQueen(26, 28, 1.2) : sfKing(26, 28, 1.2)} vb={[0, 0, 52, 58]} style={{width:82,flex:'0 0 auto'}} label={clef === 'treble' ? t('the Queen', '여왕') : t('the King', '왕')}/>
    </div>;
  };
  const pic2 = (intro, main, h) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap:12,width:'100%',maxWidth:640,margin:'0 auto'}}>{intro}<div style={{width:'100%',maxWidth:600,margin:'0 auto'}}>{main}</div></div></LbPic>;
  // p4: the Queen's five -- C D E F G, from Clara up to the Queen's G; the curl wraps the second line""", 'clef intro')
# 5b. the faces leave the staff drawings
rep("    icons={[SF_ICON(queen, 268, 10, 0.9), SF_ICON(clara, 28, 92, 0.72)]}", "    icons={[SF_ICON(clara, 28, 92, 0.72)]}", 'p4 icons')
rep("    icons={[SF_ICON(king, 51, 166, 0.9), SF_ICON(clara, 304, 94, 0.62)]}", "    icons={[SF_ICON(clara, 304, 94, 0.62)]}", 'p5 icons')
rep("    icons={[SF_ICON(clara, 60, 96, 0.55), SF_ICON(clara, 60, 140, 0.55), SF_ICON(queen, 300, 50, 0.85), SF_ICON(king, 300, 140, 0.85)]}", "    icons={[SF_ICON(clara, 60, 96, 0.55), SF_ICON(clara, 60, 140, 0.55)]}", 'p6 icons')
# smaller top pads now that the faces are gone, and the pages use the intro + staff stack
rep("""  const p4 = <SfStaff clef="treble" width={340} pad={[50, 40]}""", """  const p4 = <SfStaff clef="treble" width={340} pad={[26, 40]}""", 'p4 pad')
rep("""  const p5 = <SfStaff clef="bass" width={340} pad={[56, 50]}""", """  const p5 = <SfStaff clef="bass" width={340} pad={[30, 46]}""", 'p5 pad')
rep("      {pic(p4, 210, 680)}", "      {pic2(clefIntro('treble'), p4, 290)}", 'p4 pic')
rep("      {pic(p5, 220, 680)}", "      {pic2(clefIntro('bass'), p5, 290)}", 'p5 pic')

# 2. the paper check-up belongs in the Workbook
rep("""      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_sf_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>
      <LbOnly print><SfPaperCheck/></LbOnly>""",
    """      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} live={<FiveChecks376 storeKey="pb_five_sf_v1" rows={checksRows.map(([a, vb, txt]) => [{ shapes: chkArts[a], vb }, txt])}/>}/>""", 'paper check out of the book')
rep("""title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('At the piano: show each one, then tick how it is going -- not yet, nearly, or got it! On paper: do the check-up below.', '피아노 앞에서: 하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요! 종이에서: 아래 점검을 풀어요.')}</LbSay>
      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>}""",
    """title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, then tick how it is going -- not yet, nearly, or got it! The check-up on paper is in the Workbook.', '피아노 앞에서 하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요! 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>}""", 'check say')
rep("""  return <>{frames ? lbFramed('staff', pages, startNo) : pages}</>;
}

// ─── the Teacher copy (Phase 405): answers, what to watch for, what to say -- her own lines ───""",
    """  // 7. the check-up on paper (Phase 406, Sohyun: it belongs in the Workbook, not the Lesson Book)
  P(<>
    <WbTop step={6}/>
    <SfPaperCheck/>
  </>);
  return <>{frames ? lbFramed('staff', pages, startNo) : pages}</>;
}

// ─── the Teacher copy (Phase 405): answers, what to watch for, what to say -- her own lines ───""", 'wb check page')
rep("""    <TcBlock page={7} title="Check-up (in the Lesson Book)\"""", """    <TcBlock page={7} title="Check-up\"""", 'tc title')

# 3. line notes show their line through the hole -- on paper and on screen
rep("""            {n.filled ? <ellipse cx={x} cy={y} rx="6.6" ry="4.7" transform={`rotate(-20 ${x} ${y})`} fill={c}/>
              : <g><ellipse cx={x} cy={y} rx="7" ry="4.9" fill={c}/><ellipse cx={x} cy={y} rx="3.3" ry="2.6" transform={`rotate(-38 ${x} ${y})`} fill="#fff"/></g>}""",
    """            {n.filled ? <ellipse cx={x} cy={y} rx="6.6" ry="4.7" transform={`rotate(-20 ${x} ${y})`} fill={c}/>
              : <g><ellipse cx={x} cy={y} rx="7" ry="4.9" fill={c}/><ellipse cx={x} cy={y} rx="3.3" ry="2.6" transform={`rotate(-38 ${x} ${y})`} fill="#fff"/>{(n.d - CLEFS[st].low) % 2 === 0 && <line x1={x - 3.6} x2={x + 3.6} y1={y} y2={y} stroke={ink} strokeOpacity="0.7" strokeWidth="1.05"/>}</g>}""", 'paper line through hole')
rep("""            <ellipse cx={x} cy={y} rx="7" ry="5" transform={`rotate(-20 ${x} ${y})`} fill={n.color || ink} data-d={n.d}/>""",
    """            <ellipse cx={x} cy={y} rx="7.2" ry="5.1" fill={n.color || ink} data-d={n.d}/>
            <ellipse cx={x} cy={y} rx="3.3" ry="2.6" transform={`rotate(-38 ${x} ${y})`} fill={ink === '#faf6ec' ? '#26296b' : '#fff'}/>
            {(n.d - CLEFS[st].low) % 2 === 0 && <line x1={x - 3.6} x2={x + 3.6} y1={y} y2={y} stroke={ink} strokeOpacity="0.75" strokeWidth="1.1"/>}""", 'screen line through hole')

# 4. Workbook p3 fills its page: 8 cells on your turn
rep("const s2 = withSeed(k('s2'), () => ({ tog: Array.from({ length: 4 }, () => mkSS(30, 38)), home: Array.from({ length: 4 }, () => mkSS(30, 38)), hi: Array.from({ length: 4 }, () => mkSS(30, 38)) }));",
    "const s2 = withSeed(k('s2'), () => ({ tog: Array.from({ length: 4 }, () => mkSS(30, 38)), home: Array.from({ length: 8 }, () => mkSS(30, 38)), hi: Array.from({ length: 4 }, () => mkSS(30, 38)) }));", 'wb s2 8 cells')


# 4b. the "Which is higher?" box hugs its four cells instead of filling the page
rep("""    <Part kind="play" style={{justifyContent:'center'}} title="Which is higher?" how="Circle the higher note in each pair -- then play both, low one first, and check with your ears.">""",
    """    <Part kind="play" grow={false} title="Which is higher?" how="Circle the higher note in each pair -- then play both, low one first, and check with your ears.">""", 'higher grow')

open(src, 'w', encoding='utf-8').write(s); print('patch406 ok')
