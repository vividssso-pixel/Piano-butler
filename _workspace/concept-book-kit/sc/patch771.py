#!/usr/bin/env python3
"""Build CV (on t770 -> t771).
1. Floors named by grade only (Sohyun 2026-10-29 14:24: "Floor 1 ..." looks more complicated; keep the grade).
2. Clara only in the key-names chapter (her 14:22): everywhere else middle C, counted with C as 1
   (the Queen's G is the fifth note up from middle C, the King's F the fifth note down, treble C the eighth).
   Clara's ladder -> middle C's short line (Beginner) / its ledger line (Prelim, the Home).
   The pink pawn leaves the staff pictures; one middle C key icon marks middle C instead.
3. 'Beat your time' on screen: a tap stopwatch that keeps the best time on the device.
4. A wide drawing no longer sits in a tall empty frame: the frame hugs it and the page spreads the rest.
"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def nb(x):
    for _ in range(3): x = re.sub(r'(?<![A-Za-z0-9])([A-G0-9]) (?=[A-G0-9](?![A-Za-z0-9]))', '\\1\u00a0', x)
    return x
def R(old, new, n=1):
    global s
    if s.count(old) == 0 and s.count(nb(old)) > 0: old, new = nb(old), nb(new)
    c = s.count(old)
    assert c == n, (c, n, old[:120])
    s = s.replace(old, new)

# ───────────────────────── 1. floors by grade ─────────────────────────
R("""const floorName = (k, caps) => { if (PATH_STAGES[k].attic) return caps ? 'ATTIC' : t('The attic', '다락방'); if (PATH_STAGES[k].stories) return caps ? 'STORIES OF MUSIC' : t('Stories of music', '음악 이야기'); const s = PATH_STAGES[k], nm = caps ? s.en[0].toUpperCase() : t(s.en[0], s.ko[0]); return LANG === 'ko' && !caps ? (k + 1) + '층 · ' + nm : (caps ? 'FLOOR ' : 'Floor ') + (k + 1) + ' · ' + nm; };   // Build P""",
  """const floorName = (k, caps) => { if (PATH_STAGES[k].attic) return caps ? 'ATTIC' : t('The attic', '다락방'); if (PATH_STAGES[k].stories) return caps ? 'STORIES OF MUSIC' : t('Stories of music', '음악 이야기'); const s = PATH_STAGES[k]; return caps ? s.en[0].toUpperCase() : t(s.en[0], s.ko[0]); };   // Build P; Build CV (her 2026-10-29): the grade only, no floor number""")
R("""t('That was the last room on floor ' + (k + 1) + '. Next: ' + floorName(nk) + '.', (k + 1) + '층의 마지막 방이에요. 다음: ' + floorName(nk) + '.')""",
  """t('That was the last room in ' + floorName(k) + '. Next: ' + floorName(nk) + '.', floorName(k) + '의 마지막 방이에요. 다음: ' + floorName(nk) + '.')""")
R("""t('Floor ' + (k + 1) + ' of ' + houseFloorsN() + ': ' + s.en[0], houseFloorsN() + '층 중 ' + (k + 1) + '층: ' + s.ko[0])""",
  """t(s.en[0], s.ko[0])""")
R("""Start on floor 1, Beginner, and go up floor by floor.""", """Start on Beginner and go up floor by floor.""")
R("""1층 Beginner에서 시작해 한 층씩 올라가요.""", """Beginner에서 시작해 한 층씩 올라가요.""")
R("""New to the piano? Start on floor 1, Beginner.""", """New to the piano? Start on Beginner.""", 2)
R("""처음이라면 1층 Beginner부터""", """처음이라면 Beginner부터""", 2)
R("""st.s ? (o.print || LANG !== 'ko' ? 'FLOOR ' : '') + (k + 1) + (o.print || LANG !== 'ko' ? '' : '층') + ' · ' + st.s.en[0].toUpperCase() : 'LEVEL ' + (k + 1)""",
  """st.s ? st.s.en[0].toUpperCase() : 'LEVEL ' + (k + 1)""")

# ───────────────────────── 2. middle C, not Clara ─────────────────────────
# one middle C key: B C D, C in coral, the black key between C and D (and A sharp at the left edge)
R("""function sfClara(cx, cy, k = 1) { return vicPiece(VIC_PAWN, cx, cy, k); }""",
  """function sfClara(cx, cy, k = 1) { return vicPiece(VIC_PAWN, cx, cy, k); }
// Build CV (her 2026-10-29: Clara only while learning the key names): middle C is marked by its key -- B C D, C in coral
const MIDC_KEY_SVG = '<g stroke="#26296b" stroke-width="1.6" stroke-linejoin="round"><rect x="4" y="6" width="12" height="34" fill="#fff"/><rect x="16" y="6" width="12" height="34" fill="#e4572e"/><rect x="28" y="6" width="12" height="34" fill="#fff"/></g><rect x="24.6" y="6" width="6.8" height="20" fill="#26296b"/><rect x="0.6" y="6" width="6.8" height="20" fill="#26296b"/><text x="22" y="36.5" font-size="10" font-weight="900" fill="#fff" text-anchor="middle" font-family="Inter,system-ui,sans-serif">C</text>';
function sfMidKey(cx, cy, k = 1) { return [{ k: 'raw', svg: '<g transform="translate(' + pFix(cx - 22 * k) + ' ' + pFix(cy - 23 * k) + ') scale(' + k + ')">' + MIDC_KEY_SVG + '</g>' }]; }""")

# shared: landmarks, the fold tool, the staff level, the Toolbox
R(r"""t('Clara\'s middle C, on her own little ladder between the two staves: the middle of the piano.', '클라라의 가운데 도, 두 오선 사이 자기만의 작은 사다리 발판 위: 피아노의 한가운데.')""",
  r"""t('Middle C, on its own short line between the two staves: the middle of the piano.', '가운데 도, 두 오선 사이 자기만의 짧은 줄 위: 피아노의 한가운데.')""")
R("""one octave above Clara.', '높은음자리표 오선의 3번 칸, 클라라보다 한 옥타브 위.')""", """one octave above middle C.', '높은음자리표 오선의 3번 칸, 가운데 도보다 한 옥타브 위.')""")
R("""one octave below Clara.', '낮은음자리표 오선의 2번 칸, 클라라보다 한 옥타브 아래.')""", """one octave below middle C.', '낮은음자리표 오선의 2번 칸, 가운데 도보다 한 옥타브 아래.')""")
R(r"""t('Fold the staff at Clara\'s ladder', '클라라의 발판에서 오선 접기')""", r"""t('Fold the staff at middle C', '가운데 도에서 오선 접기')""")
R(r"""fold along Clara\'s ladder, and open it.', '데칼코마니처럼, 이번엔 발판 둘 바깥의 높은 도와 낮은 도까지: 높은음자리표 쪽에 물감을 묻히고, 클라라의 발판을 따라 접었다가 펼쳐요.')""",
  r"""fold along middle C, and open it.', '데칼코마니처럼, 이번엔 발판 둘 바깥의 높은 도와 낮은 도까지: 높은음자리표 쪽에 물감을 묻히고, 가운데 도를 따라 접었다가 펼쳐요.')""")
R("""'Around Clara: both staves': '클라라 둘레: 두 오선',""", """'Around middle C: both staves': '가운데 도 둘레: 두 오선',""")
R("""label: 'Around Clara: both staves',""", """label: 'Around middle C: both staves',""")
R(r"""title: 'Fold at Clara\'s ladder', blurb:""", r"""title: 'Fold at middle C', blurb:""")
R("""'fold': ['클라라의 발판에서 접기',""", """'fold': ['가운데 도에서 접기',""")
R("""low middle high turtle bird clara same""", """low middle high turtle bird middle c same""")

# ears: turtle, middle C or bird (middle C is the ground from Chapter 2)
R("""const lsClara = (w = 30) => <PenArt shapes={sfClara(26, 31, 1.2)} vb={[0, 0, 52, 58]} style={{width:w}}/>;""",
  """const lsMidC = (w = 30) => <svg width={w} height={w} viewBox="0 0 44 44" style={{display:'block'}} dangerouslySetInnerHTML={{__html: MIDC_KEY_SVG}}/>;   // Build CV: the middle is middle C's key, not Clara""")
R("""lsClara(24)""", """lsMidC(24)""", 2)
R("""lsClara((big ? 58 : 44) * k)""", """lsMidC((big ? 48 : 38) * k)""")
R("""'In the middle, near Clara (middle C).', q.answer === 'low' ? '낮은 음: 거북이와 함께 아래.' : q.answer === 'high' ? '높은 음: 새와 함께 위.' : '가운데, 클라라(가운데 도) 근처.')""",
  """'In the middle, near middle C.', q.answer === 'low' ? '낮은 음: 거북이와 함께 아래.' : q.answer === 'high' ? '높은 음: 새와 함께 위.' : '가운데, 가운데 도 근처.')""")
R("""['In the middle, near Clara (middle C).', '가운데, 클라라(가운데 도) 근처.']""", """['In the middle, near middle C.', '가운데, 가운데 도 근처.']""")
R("""t('Turtle, Clara or bird?', '거북이, 클라라, 새?')""", """t('Turtle, middle C or bird?', '거북이, 가운데 도, 새?')""", 2)
R("""'Turtle, Clara or bird?', '거북이, 클라라, 새?'""", """'Turtle, middle C or bird?', '거북이, 가운데 도, 새?'""")
R("""the middle, around middle C (Clara); high""", """the middle, around middle C; high""")
R("""stand tall like Clara, flap like the bird""", """stand tall on the ground, flap like the bird""")
R("""가운데는 가운데 도(클라라) 근처""", """가운데는 가운데 도 근처""")
R("""클라라처럼 똑바로 서기""", """땅 위에 똑바로 서기""")
R("""<b>가운데</b> 음은 클라라(가운데 도)와,""", """<b>가운데</b> 음은 땅 위 가운데 도에,""")
R("""<b>in the middle</b> with Clara (middle C), or""", """<b>in the middle</b> on the ground, around middle C, or""")
R("""가운데면 클라라처럼 똑바로 서고""", """가운데면 땅 위에 똑바로 서고""")
R("""Middle: stand tall like Clara.""", """Middle: stand tall on the ground.""")
R("""t('Low, middle, high: turtle, Clara, bird.', '낮은, 가운데, 높은: 거북이, 클라라, 새.')""", """t('Low, middle, high: turtle, middle C, bird.', '낮은, 가운데, 높은: 거북이, 가운데 도, 새.')""")
R("""<TcBlock page={2} title="Turtle, Clara or bird?\"""", """<TcBlock page={2} title="Turtle, middle C or bird?\"""")
R("""say="“Low, middle, high: turtle, Clara, bird.”"/>""", """say="“Low, middle, high: turtle, middle C, bird.”"/>""")

# hand positions
R("""t('Both thumbs on middle C (Clara).', '두 엄지 모두 가운데 도(클라라)에.')""", """t('Both thumbs on middle C.', '두 엄지 모두 가운데 도에.')""")
R("""<b>가운데 도(클라라)</b>에 함께""", """<b>가운데 도</b>에 함께""")
R("""<b>middle C (Clara)</b>. The rig""", """<b>middle C</b>. The rig""")

# note names: Clara stays here; the teacher note says where she stops
R("""Clara belongs to the royal family: the Queen and the King arrive with the staff.'""",
  """Clara is only the key-name helper: from the staff on, she is simply middle C.'""")
R("""클라라는 왕실 가족이에요: 여왕과 왕은 오선보와 함께 등장해요.')""", """클라라는 건반 이름을 익힐 때만 써요: 오선보부터는 그냥 가운데 도예요.')""")

# the staff chapter
R("""const queen = sfQueen(22, 24, 1), king = sfKing(22, 24, 1), clara = sfClara(22, 24, 1);""",
  """const queen = sfQueen(22, 24, 1), king = sfKing(22, 24, 1), midKey = sfMidKey(22, 23, 1);""", 3)
R("""s1.push(...sfKing(24, 22, 1), ...sfClara(mcx, 23, 0.95), ...sfQueen(352, 22, 1));""", """s1.push(...sfKing(24, 22, 1), ...sfQueen(352, 22, 1));""")
R("""t('Clara · middle C', '클라라 · 가운데 도')""", """t('middle C', '가운데 도')""")
R("""and Clara, a pink pawn with a tiara, in the middle, on middle C', '피아노: 낮은 쪽 끝에 남색 체스 킹(왕), 높은 쪽 끝에 산호색색 체스 퀸(여왕), 그리고 한가운데, 가운데 도 위에 티아라를 쓴 분홍 폰 클라라')""",
  """and middle C marked in the middle', '피아노: 낮은 쪽 끝에 남색 체스 킹(왕), 높은 쪽 끝에 산호색 체스 퀸(여왕), 그리고 한가운데에 표시한 가운데 도')""")
R("""    icons={[SF_ICON(clara, 28, 92, 0.72)]}\n""", "")
R("""    icons={[SF_ICON(clara, 304, 94, 0.62)]}\n""", "")
R("""[xs5[0], 'C', t('Clara', '클라라'), true]""", """[xs5[0], 'C', t('middle C', '가운데 도'), true]""")
R("""[xs5[4], 'C', t('Clara', '클라라'), true]""", """[xs5[4], 'C', t('middle C', '가운데 도'), true]""")
R("""label={t('The grand staff with one Clara between the two staves; visiting the Queen, her middle C is written on its ladder just under the treble staff; visiting the King, just over the bass staff. Dotted paths join Clara to both notes: the same key', '큰보표, 두 오선 사이에 클라라 한 명; 여왕네 갈 때는 가운데 도를 높은음자리표 오선 바로 아래 사다리 발판에, 왕네 갈 때는 낮은음자리표 오선 바로 위에 써요. 점선이 클라라와 두 음표를 이어요: 같은 건반')}""",
  """label={t('The grand staff with middle C\\'s one key between the two staves; visiting the Queen, middle C is written on its short line just under the treble staff; visiting the King, just over the bass staff. Dotted paths join the key to both notes: the same key', '큰보표, 두 오선 사이에 가운데 도 건반 하나; 여왕네 갈 때는 가운데 도를 높은음자리표 오선 바로 아래 짧은 줄에, 왕네 갈 때는 낮은음자리표 오선 바로 위에 써요. 점선이 건반과 두 음표를 이어요: 같은 건반')}""")
R("""icons={[SF_ICON(clara, 172, 116, 0.62)]}""", """icons={[SF_ICON(midKey, 172, 112, 0.64)]}""")
R("""clara: [...sfClara(24, 22, 0.8), { ...penText(62, 30,""", """clara: [...sfMidKey(24, 20, 0.82), { ...penText(62, 30,""")
R("""t('Meet the royal family of the keys. The King sings low, the Queen sings high. Clara lives between them, on middle C. Now we read their notes on paper.', '건반의 왕실 가족을 만나요. 왕은 낮은 목소리, 여왕은 높은 목소리로 노래해요. 클라라는 그 사이 가운데 도에 살아요. 이제 이들의 음을 종이에서 읽어요.')""",
  """t('Meet the royal family of the keys. The King sings low, the Queen sings high. Between them is middle C. Now we read their notes on paper.', '건반의 왕실 가족을 만나요. 왕은 낮은 목소리, 여왕은 높은 목소리로 노래해요. 그 사이에 가운데 도가 있어요. 이제 이들의 음을 종이에서 읽어요.')""")
R("""t('Clara can be written in two places on paper. How many keys is that on the piano?', '클라라는 종이에서 두 자리에 쓸 수 있어요. 피아노에서는 건반 몇 개일까요?')""",
  """t('Middle C can be written in two places on paper. How many keys is that on the piano?', '가운데 도는 종이에서 두 자리에 쓸 수 있어요. 피아노에서는 건반 몇 개일까요?')""")
R("""t('Middle C: Clara', '가운데 도: 클라라')""", """t('Middle C on both staves', '두 오선의 가운데 도')""", 2)
R("""클라라(가운데 도)에서 여왕의 G까지 <b>다섯 음</b>: C D E F G. C는 클라라의 작은 사다리 발판, D는""", """가운데 도에서 여왕의 G까지 <b>다섯 음</b>: C D E F G. C는 자기만의 짧은 줄, D는""")
R("""Clara (middle C) to the Queen's G is <b>five notes</b>: C D E F G. C on Clara's little ladder, D under""", """Middle C to the Queen's G is <b>five notes</b>: C D E F G. C on its own short line, D under""")
R(r"""t('The curl wraps round G: the Queen\'s line. Clara to the Queen: C D E F G.', '소용돌이는 G를 감싸요: 여왕의 줄. 클라라에서 여왕까지: C D E F G.')""",
  r"""t('The curl wraps round G: the Queen\'s line. Middle C to the Queen: C D E F G.', '소용돌이는 G를 감싸요: 여왕의 줄. 가운데 도에서 여왕까지: C D E F G.')""")
R("""왕의 F에서 클라라까지도 <b>다섯 음</b>: F G A B C. F는 왕의 줄, G는 그 위 칸, A는 맨 윗줄, B는 그 위, C는 클라라의 작은 사다리 발판.""",
  """왕의 F에서 가운데 도까지도 <b>다섯 음</b>: F G A B C. F는 왕의 줄, G는 그 위 칸, A는 맨 윗줄, B는 그 위, C는 자기만의 짧은 줄.""")
R("""The King's F to Clara is <b>five notes</b> too: F G A B C. F on the King's line, G in the space above, A on the top line, B over it, C on Clara's little ladder.""",
  """The King's F to middle C is <b>five notes</b> too: F G A B C. F on the King's line, G in the space above, A on the top line, B over it, C on its own short line.""")
R(r"""t('The two dots guard F: the King\'s line. The King to Clara: F G A B C.', '두 점은 F를 지켜요: 왕의 줄. 왕에서 클라라까지: F G A B C.')""",
  r"""t('The two dots guard F: the King\'s line. The King to middle C: F G A B C.', '두 점은 F를 지켜요: 왕의 줄. 왕에서 가운데 도까지: F G A B C.')""")
R("""두 궁전 사이 <b>가운데 도</b>에 <b>클라라</b>가 살아요: 2챕터의 땅. 클라라는 <b>한 명</b>, <b>작은 사다리 발판</b>도 하나.""",
  """두 궁전 사이에 <b>가운데 도</b>가 있어요: 2챕터의 땅. 가운데 도는 <b>하나</b>, <b>자기만의 짧은 줄</b>도 하나.""")
R("""<b>Clara</b> lives between the palaces, on <b>middle C</b>: the ground from Chapter 2. <b>One Clara</b>, <b>one little ladder of her own</b>. <b>Visiting the Queen</b>, her note goes just under""",
  """Between the palaces is <b>middle C</b>: the ground from Chapter 2. <b>One middle C</b>, on <b>one short line of its own</b>. <b>Visiting the Queen</b>, it goes just under""")
R("""<><b>가운데 도</b>를 쳐요: 클라라의 자리, 두 손이 다 닿는 단 한 곳.</>""", """<><b>가운데 도</b>를 쳐요: 두 손이 다 닿는 단 한 곳.</>""")
R("""누가 클라라의 음을 위 오선 아래나 아래 오선 위에 써요.""", """누가 가운데 도를 위 오선 아래나 아래 오선 위에 써요.""")
R("""<>Play <b>middle C</b>: Clara's place, the one key both hands can reach.</>""", """<>Play <b>middle C</b>: the one key both hands can reach.</>""")
R("""Someone writes Clara's note under the top staff""", """Someone writes middle C under the top staff""")
R(r"""t('Someone writes Clara under the top staff or over the bottom one: play middle C with the right hand for the Queen\'s, the left for the King\'s.', '누가 클라라를 위 오선 아래나""",
  r"""t('Someone writes middle C under the top staff or over the bottom one: play it with the right hand for the Queen\'s, the left for the King\'s.', '누가 가운데 도를 위 오선 아래나""")
R("""t('Clara lives between the Queen and the King: the same key on either staff.', '클라라는 여왕과 왕 사이에 살아요: 어느 오선에 써도 같은 건반.')""",
  """t('Middle C lives between the Queen and the King: the same key on either staff.', '가운데 도는 여왕과 왕 사이에 살아요: 어느 오선에 써도 같은 건반.')""")
R("""<PenArt shapes={sfClara(26, 28, 1)} vb={[2, 2, 48, 52]}""", """<PenArt shapes={sfMidKey(26, 27, 1.05)} vb={[2, 2, 48, 52]}""")
R("""t('Clara: middle C on her little ladder, the same key from either palace.', '클라라: 작은 사다리 발판 위의 가운데 도, 어느 궁전에서 써도 같은 건반.')""",
  """t('Middle C on its short line: the same key from either palace.', '짧은 줄 위의 가운데 도: 어느 궁전에서 써도 같은 건반.')""")
R("""who === 'clara' ? sfClara(22, 24, 1)""", """who === 'clara' ? sfMidKey(22, 22, 0.9)""")
R("""<Part kind="home" title="Clara visits" how="Draw the note each time, on its little ladder when it is middle C.">""",
  """<Part kind="home" title="Around middle C" how="Draw the note each time, on its short line when it is middle C. Count middle C as 1.">""")
R("""visit('One step up from Clara: draw D',""", """visit('The 2nd note up from middle C: draw D',""")
R("""visit('One step down from Clara: draw B',""", """visit('The 2nd note down from middle C: draw B',""")
R("""visit('Two steps up from Clara: draw E',""", """visit('The 3rd note up from middle C: draw E',""")
R("""visit('Two steps down from Clara: draw A',""", """visit('The 3rd note down from middle C: draw A',""")
R("""<TcBlock page={6} title="Middle C: Clara" """, """<TcBlock page={6} title="Middle C on both staves" """)
R("""tcAns('CLARA VISITS', ['C on the ladder just under the treble staff', 'C on the ladder just over the bass staff',""",
  """tcAns('AROUND MIDDLE C', ['C on the short line just under the treble staff', 'C on the short line just over the bass staff',""")
R("""say="“One Clara, one key, written from the Queen's side or the King's side.”"/>""", """say="“One middle C, one key, written from the Queen's side or the King's side.”"/>""")

# the whole staff
R("""; Clara, a pink pawn, between them', '큰보표: 위 오선에는 높은음자리표, 옆에 여왕의 체스 말; 아래 오선에는 낮은음자리표, 옆에 왕의 체스 말; 그 사이에 분홍 폰 클라라')""",
  """; middle C\\'s key between them', '큰보표: 위 오선에는 높은음자리표, 옆에 여왕의 체스 말; 아래 오선에는 낮은음자리표, 옆에 왕의 체스 말; 그 사이에 가운데 도 건반')""")
R("""SF_ICON(clara, 308, 108, 0.82)""", """SF_ICON(midKey, 306, 106, 0.8)""")
R(r"""between the staves, at Clara\'s ladder: folded,""", r"""between the staves, at middle C: folded,""")
R("""'오선 사이, 클라라의 발판 자리에 접는 점선:""", """'오선 사이, 가운데 도 자리에 접는 점선:""")
R("""icons={[SF_ICON(clara, 352, 110, 0.7)]}""", """icons={[SF_ICON(midKey, 352, 108, 0.66)]}""")
R(r"""Clara\'s middle C, the Queen\'s G""", r"""middle C, the Queen\'s G""")
R("""넷째 줄의 왕의 F, 클라라의 가운데 도,""", """넷째 줄의 왕의 F, 가운데 도,""")
R("""you read the nine notes around Clara. Now""", """you read the nine notes around middle C. Now""")
R("""챕터에서 클라라 둘레의 아홉 음을 읽었어요.""", """챕터에서 가운데 도 둘레의 아홉 음을 읽었어요.""")
R(r"""t('Fold at Clara\'s ladder', '클라라의 발판에서 접기')""", r"""t('Fold at middle C', '가운데 도에서 접기')""", 2)
R("""큰보표를 <b>클라라의 발판</b>에서 접어요. 줄은 줄에, 칸은 칸에 겹쳐요. <b>여왕의 G</b>는 <b>왕의 F</b>에 닿아요(클라라에서 위로 다섯, 아래로 다섯). 위 오선 칸의 <b>C</b>는 아래 오선 칸의 <b>C</b>에, 클라라는 클라라에 닿아요. 그래서 <b>C가 세 개</b>: 위에 하나, 가운데 클라라, 아래에 하나.""",
  """큰보표를 <b>가운데 도</b>에서 접어요. 줄은 줄에, 칸은 칸에 겹쳐요. <b>여왕의 G</b>는 <b>왕의 F</b>에 닿아요(가운데 도를 1로 세면 위로 다섯 번째, 아래로 다섯 번째). 위 오선 칸의 <b>C</b>는 아래 오선 칸의 <b>C</b>에, 가운데 도는 가운데 도에 닿아요. 그래서 <b>C가 세 개</b>: 위에 하나, 가운데 도, 아래에 하나.""")
R("""Fold the grand staff at <b>Clara's ladder</b>. Lines land on lines, spaces on spaces. <b>The Queen's G</b> lands on <b>the King's F</b>, five up and five down from Clara.""",
  """Fold the grand staff at <b>middle C</b>. Lines land on lines, spaces on spaces. <b>The Queen's G</b> lands on <b>the King's F</b>: count middle C as 1, and they are the fifth note up and the fifth note down.""")
R("""Clara lands on Clara. That makes <b>three Cs</b>: one up, Clara in the middle, one down.""", """Middle C lands on middle C. That makes <b>three Cs</b>: one up, middle C, one down.""")
R("""t('Fold at Clara: G meets F, C meets C.', '클라라에서 접으면: G는 F와, C는 C와 만나요.')""", """t('Fold at middle C: G meets F, C meets C.', '가운데 도에서 접으면: G는 F와, C는 C와 만나요.')""")
R(r"""bkSec('D', 'Fold at Clara in your head:""", r"""bkSec('D', 'Fold at middle C in your head:""")
R("""Ledger lines beyond Clara's ladder come in the next chapter.""", """Ledger lines beyond middle C's short line come in the next chapter.""")
R("""<TcBlock page={5} title="Fold at Clara's ladder" """, """<TcBlock page={5} title="Fold at middle C" """)
R("""say="“Fold at Clara: G meets F, C meets C.”"/>""", """say="“Fold at middle C: G meets F, C meets C.”"/>""")

# ledger lines (Prelim): middle C's short line has a real name
R("""between the staves Clara stands by middle C, written on its short line under the treble staff and again over the bass staff;""",
  """between the staves middle C\\'s key, and middle C written on its short line under the treble staff and again over the bass staff;""")
R("""두 오선 사이에는 클라라가 높은음자리표 오선 아래와 낮은음자리표 오선 위, 두 번 쓴 가운데 도 옆에 서 있고,""",
  """두 오선 사이에는 가운데 도 건반과, 높은음자리표 오선 아래와 낮은음자리표 오선 위에 두 번 쓴 가운데 도가 있고,""")
R("""SF_ICON(clara, 124, 112, 0.8)""", """SF_ICON(midKey, 140, 108, 0.72)""")
R(r"""middle C below the staff on Clara\'s ladder, and A above the staff on a ladder of its own.""", r"""middle C below the staff, and A above the staff.""")
R("""오선 아래 클라라의 발판 위의 가운데 도, 오선 위 자기 발판 위의 A,""", """오선 아래의 가운데 도, 오선 위의 A,""")
R(""" icons={[SF_ICON(clara, 99, 116, 0.6)]}""", "")
R(r"""middle C on Clara\'s ladder under the treble staff and over the bass staff;""", r"""middle C on its ledger line under the treble staff and over the bass staff;""")
R("""낮은음자리표 오선 위 클라라 발판의 가운데 도;""", """낮은음자리표 오선 위 덧줄의 가운데 도;""")
R(r"""t('The grand staff folded at Clara\'s ladder:""", r"""t('The grand staff folded at middle C:""")
R("""'클라라의 발판에서 접은 큰보표:""", """'가운데 도에서 접은 큰보표:""")
R("""icons={[SF_ICON(clara, 344, 104, 0.7)]}""", """icons={[SF_ICON(midKey, 344, 102, 0.66)]}""")
R("""클라라의 짧은 발판에는 진짜 이름이 있어요:""", """가운데 도의 짧은 줄에는 진짜 이름이 있어요:""")
R("""<>Clara's little ladder has a real name:""", """<>Middle C's short line has a real name:""")
R(r"""t('Clara\'s ladder is a ledger line', '클라라의 발판은 덧줄')""", r"""t('Middle C\'s short line is a ledger line', '가운데 도의 짧은 줄은 덧줄')""", 2)
R("""클라라의 발판도 덧줄이에요.""", """가운데 도의 짧은 줄도 덧줄이에요.""")
R("""Clara's ladder is one. The pattern""", """Middle C's short line is one. The pattern""")
R("""<b>클라라의 발판에서 접으면</b>""", """<b>가운데 도에서 접으면</b>""")
R("""Fold at <b>Clara's ladder</b>, as in Chapter""", """Fold at <b>middle C</b>, as in Chapter""")
R("""const LL_C_WORD = { 14: 'Sea', 28: 'Clara\\'s', 42: 'Sky' };""", """const LL_C_WORD = { 14: 'Sea', 28: 'Middle', 42: 'Sky' };""")
R("""[28, sfClara(22, 24, 1)]""", """[28, sfMidKey(22, 22, 0.9)]""")
R("""<TcBlock page={2} title="Clara's ladder is a ledger line" """, """<TcBlock page={2} title="Middle C's short line is a ledger line" """)

# tones and semitones: the doors, not Clara
R("""s.push(K.youW(2), ...sfClara(K.wx(2), 140, 0.9));""", """s.push(K.youW(2));""")
R("""t('The keyboard street with Clara at her C:""", """t('The keyboard street, C marked:""")
R("""'클라라가 C에 서 있는 건반 거리:""", """'C를 표시한 건반 거리:""")
R("""큰 집 <b>뒷문(B)</b>으로 나가면 옆 작은 집의 <b>클라라(C)</b>예요.""", """큰 집 <b>뒷문(B)</b>으로 나가면 옆 작은 집의 <b>왼쪽 문(C)</b>이에요.""")
R("""you meet <b>Clara (C)</b> at the next small house.""", """you are at the next small house's <b>left door (C)</b>.""")
R("""클라라의 C에서는 <b>C 샵""", """C에서는 <b>C 샵""")
R("""강아지의 D에서는 <b>D 플랫""", """D에서는 <b>D 플랫""")
R("""From Clara's C, it is <b>C sharp""", """From C, it is <b>C sharp""")
R("""From the Dog's D, it is <b>D flat""", """From D, it is <b>D flat""")

# Staff maker goals
R("""['clara', 'Visit Clara (middle C)', '클라라(가운데 도) 만나기']""", """['clara', 'Visit middle C', '가운데 도 만나기']""")
R("""클라라의 작은 발판(덧줄)을 타고""", """작은 발판(덧줄)을 타고""")
R("""Climb Clara's little ladders (ledger lines) up and down.""", """Climb the little ladders (ledger lines) up and down.""")

# the Home: Keys and staff (count middle C as 1)
R("""t('C = middle C, Clara’s key, near the middle of the keyboard', 'C = 가운데 도, 클라라의 건반, 건반 한가운데 가까이')""", """t('C = middle C, near the middle of the keyboard', 'C = 가운데 도, 건반 한가운데 가까이')""")
R("""y: ['Yes: middle C, Clara’s key, in the middle of the keyboard.', '맞아요. 클라라의 건반, 건반 한가운데의 가운데 도예요.']""", """y: ['Yes: middle C, in the middle of the keyboard.', '맞아요. 건반 한가운데의 가운데 도예요.']""")
R("""middle C, in the middle of the keyboard. Clara lives here.', 'C 하나는 이름이 따로 있어요. 건반 한가운데의 가운데 도예요. 클라라가 여기 살아요.']""",
  """middle C, in the middle of the keyboard.', 'C 하나는 이름이 따로 있어요. 건반 한가운데의 가운데 도예요.']""")
R("""Piano music stacks them. Clara, middle C, sits between the two staves: the treble staff reads to the right of her, the bass staff to the left.', '피아노 악보는 둘을 겹쳐 써요. 클라라, 가운데 도는 두 오선 사이에 있어요.""",
  """Piano music stacks them. Middle C sits between the two staves: the treble staff reads to the right of it, the bass staff to the left.', '피아노 악보는 둘을 겹쳐 써요. 가운데 도는 두 오선 사이에 있어요.""")
R("""'Fold the two staves at Clara’s ladder, middle C, and the landmarks mirror each other:""", """'Fold the two staves at middle C, and the landmarks mirror each other:""")
R("""'두 오선을 클라라의 발판, 가운데 도에서 접으면""", """'두 오선을 가운데 도에서 접으면""")
R("""on a short line of its own: Clara’s ladder. It is the centre""", """on a short line of its own, a ledger line. It is the centre""")
R("""자기만의 짧은 줄, 클라라의 발판 위에 있고""", """자기만의 짧은 줄, 덧줄 위에 있고""")
R("""'Fold at Clara’s ladder. The Queen’s G, 4 steps above, lands on the King’s F, 4 steps below. On the keyboard they are 7 keys either side.', '클라라의 발판에서 접어요. 4걸음 위 여왕의 G가 4걸음 아래 왕의 F에 겹쳐요. 건반에서는 양쪽으로 7칸이에요.'""",
  """'Fold at middle C. Count middle C as 1: the Queen’s G, the fifth note up, lands on the King’s F, the fifth note down. On the keyboard, the fifth white key up and the fifth white key down.', '가운데 도에서 접어요. 가운데 도를 1로 세면, 위로 다섯 번째인 여왕의 G가 아래로 다섯 번째인 왕의 F에 겹쳐요. 건반에서도 위로 다섯 번째, 아래로 다섯 번째 흰건반이에요.'""")
R("""'Seven steps above and seven steps below are the two other landmarks: treble C and bass C, an octave either side of middle C.', '7걸음 위와 7걸음 아래가 나머지 기준 음이에요.""",
  """'The eighth note up and the eighth note down are the two other landmarks: treble C and bass C, an octave either side of middle C.', '위로 여덟 번째와 아래로 여덟 번째가 나머지 기준 음이에요.""")
R("""'A short line below the lowest line: Clara’s ladder.', '가장 아래 줄 밑의 짧은 줄, 클라라의 발판이에요.'""", """'A short line below the lowest line: a ledger line.', '가장 아래 줄 밑의 짧은 줄, 덧줄이에요.'""")
R("""'A short line above the top line: Clara’s ladder again, the same key.', '가장 위 줄 위의 짧은 줄, 역시 클라라의 발판이에요. 같은 건반이에요.'""", """'A short line above the top line: a ledger line again, the same key.', '가장 위 줄 위의 짧은 줄, 역시 덧줄이에요. 같은 건반이에요.'""")
R("""['Clara (middle C)', '클라라 (가운데 도)'], ['Clara (middle C)', '클라라 (가운데 도)']""", """['middle C', '가운데 도'], ['middle C', '가운데 도']""")
R("""'Folded at Clara’s ladder, a note on a line lands on…', '클라라의 발판에서 접으면, 줄 위의 음은 어디에 닿을까요?'""", """'Folded at middle C, a note on a line lands on…', '가운데 도에서 접으면, 줄 위의 음은 어디에 닿을까요?'""")
R("""'Fold the grand staff at Clara’s ladder. Where does '""", """'Fold the grand staff at middle C. Where does '""")
R("""'큰보표를 클라라의 발판에서 접어요. '""", """'큰보표를 가운데 도에서 접어요. '""")
R("""['Clara lands on Clara: middle C sits right on the fold.', '클라라는 클라라에 닿아요. 가운데 도는 접는 선 바로 위에 있어요.']""", """['Middle C lands on itself: it sits right on the fold.', '가운데 도는 자기 자신에 닿아요. 접는 선 바로 위에 있어요.']""")
R("""['Clara lands on Clara: middle C sits right on the fold, its own mirror.', '클라라는 클라라에 닿아요. 가운데 도는 접는 선 바로 위, 자기 자신이 거울이에요.']""", """['Middle C lands on itself: it sits right on the fold, its own mirror.', '가운데 도는 자기 자신에 닿아요. 접는 선 바로 위, 자기 자신이 거울이에요.']""")
R("""['Fold at Clara: G meets F, C meets C. '""", """['Fold at middle C: G meets F, C meets C. '""")
R("""'클라라에서 접으면 G는 F와, C는 C와 만나요. '""", """'가운데 도에서 접으면 G는 F와, C는 C와 만나요. '""")
R("""'Fold at Clara’s ladder', '클라라의 발판에서 접기'""", """'Fold at middle C', '가운데 도에서 접기'""")

# ───────────────────────── 3. 'Beat your time' on screen: a stopwatch ─────────────────────────
R("""function LbChallenge({ children, kind = 'row', n = 5 }) {
  const scr = lbScreen(); const [on, setOn] = useState(0);
  const slots = kind === 'time'
    ? [0, 1, 2].map""",
  """// Build CV: 'Beat your time' online -- tap to start, tap to stop; the best time stays on this device
const BEAT_KEY = 'pb_beat_v1';
function LbStopwatch({ id }) {
  const [t0, setT0] = useState(null), [now, setNow] = useState(0), [last, setLast] = useState(null);
  const [best, setBest] = useState(() => { try { const v = JSON.parse(localStorage.getItem(BEAT_KEY) || '{}')[id]; return typeof v === 'number' ? v : null; } catch (e) { return null; } });
  useEffect(() => { if (t0 == null) return; const iv = setInterval(() => setNow(Date.now()), 100); return () => clearInterval(iv); }, [t0]);
  const tap = () => {
    if (t0 == null) { setT0(Date.now()); setNow(Date.now()); return; }
    const s = Math.round((Date.now() - t0) / 100) / 10; setT0(null); setLast(s);
    if (s >= 0.5 && (best == null || s < best)) { setBest(s); try { const m = JSON.parse(localStorage.getItem(BEAT_KEY) || '{}'); m[id] = s; localStorage.setItem(BEAT_KEY, JSON.stringify(m)); } catch (e) {} }
  };
  const run = t0 != null, sec = run ? ((now - t0) / 1000).toFixed(1) : null, nb = last != null && best === last;
  return <span style={{display:'inline-flex',alignItems:'center',gap:8,flexWrap:'wrap',justifyContent:'flex-end'}}>
    <button className="chip" data-testid="lb-timer" aria-pressed={run} onClick={tap} style={{padding:'3px 11px',fontSize:13,fontWeight:800,fontVariantNumeric:'tabular-nums',minWidth:76,borderColor:run ? BK.coral : undefined,color:run ? BK.coral : undefined}}>
      {run ? '■ ' + sec + ' s' : last != null ? t('▶ Again', '▶ 다시') : t('▶ Start', '▶ 시작')}</button>
    {last != null && !run && <span data-testid="lb-timer-last" style={{fontSize:13,fontWeight:800,color:nb ? BK.green : BK.ink,fontVariantNumeric:'tabular-nums'}}>{last.toFixed(1) + ' s' + (nb ? t(' · best!', ' · 최고!') : '')}</span>}
    {best != null && !(last != null && nb && !run) && <span data-testid="lb-timer-best" style={{fontSize:12,color:BK.muted,fontVariantNumeric:'tabular-nums'}}>{t('best ', '최고 ') + best.toFixed(1) + ' s'}</span>}
  </span>;
}
function LbChallenge({ children, kind = 'row', n = 5, tid }) {   // tid: a time challenge's own id (the best time is kept under it, in either language)
  const scr = lbScreen(); const [on, setOn] = useState(0);
  const slots = kind === 'time' && scr ? <LbStopwatch id={tid || 'lb'}/>
    : kind === 'time'
    ? [0, 1, 2].map""")
R("""    <span style={{flex:'1 1 230px',fontSize:13.5,lineHeight:1.38,color:BK.ink,minWidth:0}}>{children}</span>
    <span style={{display:'inline-flex',gap:6,alignItems:'center',flex:'0 0 auto'}}>{slots}</span>""",
  """    <span style={{flex:'1 1 230px',fontSize:13.5,lineHeight:1.38,color:BK.ink,minWidth:0}}>{children}</span>
    <span style={{display:'inline-flex',gap:6,alignItems:'center',flex:'0 0 auto'}}>{slots}</span>""")

# ───────────────────────── 4. a wide drawing: the frame hugs it ─────────────────────────
R("""      kids.forEach(c => { if (!('mw0' in c.dataset)) { c.dataset.mw0 = c.style.maxWidth || ''; c.dataset.ml0 = c.style.marginLeft || ''; c.dataset.mr0 = c.style.marginRight || ''; } c.style.maxWidth = c.dataset.mw0; c.style.marginLeft = c.dataset.ml0; c.style.marginRight = c.dataset.mr0; c.style.zoom = ''; });
      const cs = getComputedStyle(el), inner = el.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);""",
  """      kids.forEach(c => { if (!('mw0' in c.dataset)) { c.dataset.mw0 = c.style.maxWidth || ''; c.dataset.ml0 = c.style.marginLeft || ''; c.dataset.mr0 = c.style.marginRight || ''; } c.style.maxWidth = c.dataset.mw0; c.style.marginLeft = c.dataset.ml0; c.style.marginRight = c.dataset.mr0; c.style.zoom = ''; });
      el.style.flexGrow = '1'; el.style.minHeight = h ? h + 'px' : ''; el.style.height = ''; el.style.marginTop = ''; el.style.marginBottom = ''; const body = el.parentElement;
      const cs = getComputedStyle(el), inner = el.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);""")
R("""      let m = measure(); if (!(inner > 20 && m.need > inner + 2)) return;""",
  """      let m = measure();
      // Build CV: a wide, short drawing would float in a tall empty frame -- the frame hugs it, and the page's spare
      // room goes above and below the frame (the blocks after it stay together and the page still ends level)
      if (inner > 20 && m.need > 30 && m.need < inner * 0.62 && body && body.classList.contains('bk-body')) {
        const padY = parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom), hh = Math.round(m.need + padY + Math.min(80, m.need * 0.22));
        el.style.flexGrow = '0'; el.style.minHeight = '0px'; el.style.height = hh + 'px'; el.style.marginTop = 'auto'; el.style.marginBottom = 'auto'; return; }
      if (!(inner > 20 && m.need > inner + 2)) return;""")

k = [0]
def _tid(m):
    k[0] += 1
    return '<LbChallenge kind="time" tid="beat' + str(k[0]) + '">'
s = re.sub(r'<LbChallenge kind="time">', _tid, s)
assert k[0] == 12, k[0]
open(dst, 'w', encoding='utf-8').write(s)
left = [m.start() for m in re.finditer(r'Clara|클라라', s)]
print('ok', len(s))
