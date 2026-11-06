p='tsbook461.jsx'; s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:90]); s=s.replace(a,b)
rep("    else out.push(nvbNote(nx, G(32), k === 'hd' ? 'h' : k, { dot: k === 'hd', col: c }).svg);",
    "    else out.push(nvbNote(nx, G(32), k === 'hd' ? 'h' : k, { col: c }).svg + (k === 'hd' ? '<circle cx=\"' + pFix(nx + 14) + '\" cy=\"' + pFix(G(33)) + '\" r=\"2.6\" fill=\"' + c + '\"/>' : ''));")
rep("const x1 = noteX[a] + 2, x2 = noteX[b] - 2, y = G(32) + 9;", "const x1 = noteX[a] + 2, x2 = noteX[b] - 2, y = G(32) + 6.5;")
rep("' Q' + pFix((x1 + x2) / 2) + ' ' + pFix(y + 9) + ' '", "' Q' + pFix((x1 + x2) / 2) + ' ' + pFix(y + 11) + ' '")
rep("const yH = G(30) + (o.dyH || 30), yC = yH + 26;", "const yH = G(30) + (o.dyH || 30), yC = yH + (o.strong ? 31 : 26);")
rep("else if (k === 'wr') out.push('<rect x=\"' + pFix(x + n * D / 2 - 8) + '\"", "else if (k === 'wr') out.push('<rect x=\"' + pFix(x + 12 + (n - 1) * D / 2 - 8) + '\"")
rep("extra={tags(tag(62, (yOf) => yOf(40, 'treble') - 6, t('time signature', '박자표')), tag(208, (yOf) => yOf(40, 'treble') - 6, t('bar line', '세로줄')), tag(380, (yOf) => yOf(40, 'treble') - 6, t('the end', '끝')))}/>;",
    "extra={tags(tag(62, (yOf) => yOf(40, 'treble') - 6, t('time signature', '박자표')), tag(226, (yOf) => yOf(40, 'treble') - 6, t('bar line', '세로줄')), tag(400, (yOf) => yOf(40, 'treble') - 6, t('double bar line', '끝세로줄'), BK.coral, 'end'))}/>;")
rep("extra={tags(tag(70, (yOf) => yOf(40, 'treble') - 6, t('bar 1', '1마디')), tag(190, (yOf) => yOf(40, 'treble') - 6, t('bar 2', '2마디')), tag(306, (yOf) => yOf(40, 'treble') - 6, t('bar 3', '3마디')))}/>;",
    "extra={tags(tag(122, (yOf) => yOf(40, 'treble') - 6, t('bar 1', '1마디')), tag(236, (yOf) => yOf(40, 'treble') - 6, t('bar 2', '2마디')), tag(350, (yOf) => yOf(40, 'treble') - 6, t('bar 3', '3마디')))}/>;")
rep("""  const p3 = [2, 3, 4].map(n => <TsStaff key={n} width={330} items={[['ts', n], ...tsQ(n), ['||']]} o={{ D: 46, topCoral: true }} pad={[12, 62]}""",
    """  const p3 = [2, 3, 4, 'C'].map(n => n === 'C' ? <TsStaff key={n} width={330} items={[['C'], ...tsQ(4), ['||']]} o={{ D: 46 }} pad={[30, 62]}
    label={t('A bar of common time: the sign C instead of 4/4, four crotchets counted 1 2 3 4.', '보통박자 한 마디: 4/4 대신 C, 4분음표 넷을 1 2 3 4로 세요.')}
    extra={(yOf, txt) => <text x="150" y={yOf(40, 'treble') - 6} textAnchor="start" fontSize="11.5" fontWeight="900" fill={BK.coral} style={txt}>{t('C = 4/4, common time', 'C = 4/4, 보통박자')}</text>}/> : <TsStaff key={n} width={330} items={[['ts', n], ...tsQ(n), ['||']]} o={{ D: 46, topCoral: true }} pad={[12, 62]}""")
rep("      {stack(p3.map((s, i) => <div key={i}>{s}</div>), 300, 460)}", "      {stack(p3.map((s, i) => <div key={i}>{s}</div>), 390, 440)}")
rep("const p4 = [[3, t('strong, weak, weak', '강, 약, 약')], [4, t('strong, weak, a little strong, weak', '강, 약, 조금 강, 약')]].map(([n, w]) => <TsStaff key={n} width={420} items={[['ts', n], ...tsQ(n), ['|'], ...tsQ(n), ['||']]} o={{ D: 36, strong: true, mid: n === 4 }} pad={[30, 64]}",
    "const p4 = [[3, t('strong, weak, weak', '강, 약, 약')], [4, t('strong, weak, medium, weak', '강, 약, 중간, 약')]].map(([n, w]) => <TsStaff key={n} width={420} items={[['ts', n], ...tsQ(n), ['|'], ...tsQ(n), ['||']]} o={{ D: 36, strong: true, mid: n === 4 }} pad={[34, 68]}")
rep("    extra={tags(tag(60, (yOf) => yOf(40, 'treble') - 14, w, BK.coral, 'start'))}/>);", "    extra={tags(tag(60, (yOf) => yOf(40, 'treble') - 6, w, BK.coral, 'start'))}/>);")
rep("    extra={tags(tag(200, (yOf) => yOf(40, 'treble') - 6, t('the tie crosses the bar line', '붙임줄이 세로줄을 건너가요'), BK.coral))}/>;", "    extra={tags(tag(206, (yOf) => yOf(40, 'treble') - 6, t('the tie crosses the bar line', '붙임줄이 세로줄을 건너가요'), BK.coral))}/>;")
rep("<>A <b>bar line</b> cuts the music into <b>bars</b>. Each bar holds the same number of beats. A <b>double bar line</b> is the end. With two dots before it, it is a <b>repeat sign</b>: go back and play it again. A bar's other name is a measure.</>",
    "<>A <b>bar line</b> cuts the music into <b>bars</b>. Each bar holds the same number of beats. Its other name is a measure. A <b>double bar line</b> is the end. With two dots before it, it is a <b>repeat sign</b>: go back to the start and play it again.</>")
rep("<><b>세로줄</b>이 음악을 <b>마디</b>로 나눠요. 마디마다 같은 수의 박이 들어가요. <b>겹세로줄</b>은 끝이에요. 그 앞에 점이 두 개 있으면 <b>도돌이표</b>: 처음으로 돌아가서 한 번 더 쳐요.</>",
    "<><b>세로줄</b>이 음악을 <b>마디</b>로 나눠요. 마디마다 같은 수의 박이 들어가요. <b>끝세로줄</b>은 끝이에요. 그 앞에 점이 두 개 있으면 <b>도돌이표</b>예요. 처음으로 돌아가서 한 번 더 쳐요.</>")
rep("<>오른손 3번 손가락, 여왕의 G: 위의 세 마디를 쳐요, 마디마다 1 2 3으로 세면서.</>", "<>오른손 3번 손가락, 여왕의 G: 마디마다 1 2 3을 세면서 위의 세 마디를 쳐요.</>")
rep("<>도돌이표가 있는 두 마디: 끝까지 치고, 처음으로 돌아가 한 번 더. 모두 네 마디예요.</>", "<>오른손 3번 손가락, G: 도돌이표가 있는 두 마디를 1 2 3으로 세면서 쳐요. 처음으로 돌아가 한 번 더. 모두 네 마디예요.</>")
rep("<>The two bars with the repeat sign: play to the end, go back, play them again. Four bars in all.</>", "<>Right hand, finger 3 on G: play the two bars with the repeat sign, counting 1 2 3. Go back and play them again. Four bars in all.</>")
rep("<>마디의 <b>1박</b>은 <b>강한 박</b>이에요. 조금 더 세게: <b>1</b> 2 3. {A('B4', <>4/4에서는 3박도 조금 강해요.</>)}</>", "<>마디의 <b>1박</b>은 <b>강한 박</b>이에요. 조금 더 세게 쳐요: <b>1</b> 2 3. {A('B4', <>4/4에서는 3박이 중간 박이에요.</>)}</>")
rep("{A('B4', <>In 4/4, beat 3 is a little strong too.</>)}", "{A('B4', <>In 4/4, beat 3 is a medium beat.</>)}")
rep("<>{A('B5', <>1에서 발을 구르고, 나머지 박에서 손뼉: 2/4, 3/4, 4/4를 네 마디씩.</>)}</>", "<>{A('B5', <>1에서 무릎을 치고, 나머지 박에서 손뼉을 쳐요. 소리 내어 세요. 2/4, 3/4, 4/4를 네 마디씩.</>)}</>")
rep("<>{A('B5', <>Stamp on 1 and clap on the other beats: 2/4, 3/4 and 4/4, four bars each.</>)}</>", "<>{A('B5', <>Pat your knees on 1 and clap on the other beats. Count out loud. Four bars each of 2/4, 3/4 and 4/4.</>)}</>")
rep("오선에서 4분쉼표는 <b>가운데</b>에 서고, 2분쉼표는 <b>3번 줄 위에 앉고</b>, 온쉼표는 <b>4번 줄에 매달려요</b>. {A('B6', <>온쉼표는 한 마디 내내 쉬어요.</>)}",
    "4분쉼표는 오선 <b>가운데</b>에 서요. 2분쉼표는 <b>3번 줄 위에 앉아요</b>. 온쉼표는 <b>4번 줄에 매달려요</b>. {A('B6', <>4/4에서 온쉼표는 한 마디 내내 쉬어요.</>)}")
rep("On the staff, the crotchet rest stands in the <b>middle</b>, the minim rest <b>sits on line 3</b> and the semibreve rest <b>hangs from line 4</b>. {A('B6', <>A semibreve rest is a whole bar of silence.</>)}",
    "The crotchet rest stands in the <b>middle</b> of the staff. The minim rest <b>sits on line 3</b>. The semibreve rest <b>hangs from line 4</b>. {A('B6', <>In 4/4, a semibreve rest is a whole bar of silence.</>)}")
rep("<>3/4 세 마디: 소리 내어 세면서 쳐요. 8분음표 둘은 2 +.</>", "<>오른손 3번 손가락, G: 3/4 세 마디를 소리 내어 세면서 쳐요. 8분음표 둘은 2 +.</>")
rep("<>The three bars of 3/4: count out loud as you play. Two quavers are 2 +.</>", "<>Right hand, finger 3 on G: play the three bars of 3/4 and count out loud. Two quavers are 2 +.</>")
rep("<>이번엔 붙임줄 없이: 2마디 1박에서 G를 다시 쳐요. 두 소리를 비교해요.</>", "<>오른손 3번 손가락, G: 이번엔 붙임줄 없이 쳐요. 2마디 1박에서 G를 다시 쳐요. 두 소리를 비교해요.</>")
rep("<>Now without the tie: play G again on beat 1 of bar 2. Hear the difference.</>", "<>Right hand, finger 3 on G: play the two bars again without the tie. Play G again on beat 1 of bar 2. Hear the difference.</>")
rep("t('A tie: play once, hold for both.', '붙임줄: 한 번 치고, 둘 다 누르고 있어요.')", "t('A tie: play once, hold for both.', '붙임줄: 한 번 치고, 두 음표만큼 누르고 있어요.')")
rep("t('I can show the bar lines, the end and the repeat sign', '세로줄, 끝, 도돌이표를 짚을 수 있어요')", "t('I can show the bar lines, the double bar line and the repeat sign', '세로줄, 끝세로줄, 도돌이표를 짚을 수 있어요')")
rep("bars: [nvbNote(12, 30, 'q', { k: 0.6 }), penLine([28, 10], [28, 40], 1.4, PEN_N), nvbNote(44, 30, 'q', { k: 0.6 }), penLine([62, 10], [62, 40], 1.1, PEN_N), penLine([66, 10], [66, 40], 3, PEN_N), { ...penText(56, 22, ':', { size: 16, weight: 900, fill: PEN_N, anchor: 'middle' }) }],",
    "bars: [nvbNote(12, 30, 'q', { k: 0.6 }), penLine([28, 10], [28, 40], 1.4, PEN_N), nvbNote(44, 30, 'q', { k: 0.6 }), penLine([62, 10], [62, 40], 1.1, PEN_N), penLine([66, 10], [66, 40], 3, PEN_N), { k: 'raw', svg: '<circle cx=\"57\" cy=\"21\" r=\"1.6\" fill=\"' + PEN_N + '\"/><circle cx=\"57\" cy=\"29\" r=\"1.6\" fill=\"' + PEN_N + '\"/>' }],")
rep("{ ...penText(60, 32, '1 2 3', { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' }) }],", "...[1, 2, 3].map(n => ({ ...penText(38 + n * 12, 32, String(n), { size: 12, weight: 900, fill: PEN_N, anchor: 'middle' }) }))],")
rep("strong: [{ ...tnHeart(18, 22, 2.4, PEN_C), nw: true }, { ...tnHeart(46, 24, 1.5, PEN_C), nw: true }, { ...tnHeart(70, 24, 1.5, PEN_C), nw: true }],",
    "strong: [{ ...tnHeart(18, 22, 2.4, PEN_C), nw: true }, { ...tnHeart(46, 24, 1.5, PEN_C, true), nw: true }, { ...tnHeart(70, 24, 1.5, PEN_C, true), nw: true }],")
open(p,'w').write(s); print('ok')
