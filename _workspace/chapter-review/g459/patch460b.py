# Phase 460b: real names first. Titles, labels, buttons, checks and drills say treble clef / bass clef
# (높은음자리표 / 낮은음자리표); Queensland and Kingsland are said once, in the chapter 7 opener, as the story.
# Chapter 7 is renamed 'Line and Space Names' (줄과 칸 이름).
import re, sys
B = '/home/claude/pbtest/g460/out/'
s = open(B + 't460a.src.html').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:120])
    s = s.replace(old, new)

# ── the chapter name ──
rep("t('The Whole Staff', '오선 전체 읽기')", "t('Line and Space Names', '줄과 칸 이름')", 2)
rep("label: 'The Whole Staff'", "label: 'Line and Space Names'", 2)
rep("'whole-staff': '오선 전체 읽기'", "'whole-staff': '줄과 칸 이름'")
rep("'whole-staff': ['Whole staff', '오선 전체']", "'whole-staff': ['Line and space names', '줄과 칸 이름']")
rep("' · The Whole Staff, every line and space on both staves, and the rhymes that go with them.', bkChapterNo('whole-staff') + '챕터 · 오선 전체 읽기, 두 오선의 모든 줄과 칸, 그리고 외우는 문장들.'",
    "' · Line and Space Names: every line and space in the treble and bass clefs, and their sayings.', bkChapterNo('whole-staff') + '챕터 · 줄과 칸 이름: 높은음자리표와 낮은음자리표의 모든 줄과 칸, 그리고 외우는 문장들.'")

# ── chapter 7 book: the opener says the story once ──
rep("t('The staff is a map of two lands. The Queen\\'s Queensland is on top, the King\\'s Kingsland below. In Chapter ' + bkChapterNo('staff') + ' you read the nine notes around Clara. Now read every line and space.', '오선은 두 나라의 지도예요. 위는 여왕의 퀸즈랜드, 아래는 왕의 킹스랜드. ' + bkChapterNo('staff') + '챕터에서 클라라 둘레의 아홉 음을 읽었어요. 이제 모든 줄과 칸을 읽어요.')",
    "t('The top staff has the treble clef. It is the Queen\\'s land, Queensland. The bottom staff has the bass clef. It is the King\\'s land, Kingsland. In Chapter ' + bkChapterNo('staff') + ' you read the nine notes around Clara. Now read every line and space.', '위 오선에는 높은음자리표가 있어요. 여왕의 나라, 퀸즈랜드예요. 아래 오선에는 낮은음자리표가 있어요. 왕의 나라, 킹스랜드예요. ' + bkChapterNo('staff') + '챕터에서 클라라 둘레의 아홉 음을 읽었어요. 이제 모든 줄과 칸을 읽어요.')")
rep("[[t('Crown check first', '왕관 확인 먼저'), 2], [t('Queensland', '퀸즈랜드'), 3], [t('Kingsland', '킹스랜드'), 4]",
    "[[t('Clef check first', '음자리표 확인 먼저'), 2], [t('Treble clef', '높은음자리표'), 3], [t('Bass clef', '낮은음자리표'), 4]")
rep("t('check the crown before you read', '읽기 전에 왕관부터 확인할 수 있어요'), t('read every line and space in Queensland', '퀸즈랜드의 모든 줄과 칸을 읽을 수 있어요'), t('read every line and space in Kingsland', '킹스랜드의 모든 줄과 칸을 읽을 수 있어요')",
    "t('check the clef before you read', '읽기 전에 음자리표부터 확인할 수 있어요'), t('read every line and space in the treble clef', '높은음자리표의 모든 줄과 칸을 읽을 수 있어요'), t('read every line and space in the bass clef', '낮은음자리표의 모든 줄과 칸을 읽을 수 있어요')")
rep("title={t('Crown check first', '왕관 확인 먼저')}", "title={t('Clef check first', '음자리표 확인 먼저')}")
rep("<>두 나라는 줄과 칸은 같고 이름은 달라요. <b>2번 줄</b>은 퀸즈랜드에서 <b>G</b>, 킹스랜드에서 <b>B</b>. <b>1번 칸</b>은 <b>F</b>와 <b>A</b>. 그래서 <b>왕관</b>(음자리표)부터 봐요. 여왕의 소용돌이면 퀸즈랜드, 왕의 두 점이면 킹스랜드.</>",
    "<>두 오선은 줄과 칸은 같고 이름은 달라요. <b>2번 줄</b>은 높은음자리표에서 <b>G</b>, 낮은음자리표에서 <b>B</b>. <b>1번 칸</b>은 <b>F</b>와 <b>A</b>. 그래서 <b>음자리표</b>부터 봐요. 여왕의 소용돌이는 높은음자리표, 왕의 두 점은 낮은음자리표.</>")
rep("<>The two lands share lines and spaces, not names. <b>Line 2</b> is <b>G</b> in Queensland, <b>B</b> in Kingsland. <b>Space 1</b> is <b>F</b> and <b>A</b>. So check the <b>crown</b> (the clef) first. The Queen's curl means Queensland, the King's two dots Kingsland.</>",
    "<>The two staves share lines and spaces, not names. <b>Line 2</b> is <b>G</b> in the treble clef, <b>B</b> in the bass clef. <b>Space 1</b> is <b>F</b> and <b>A</b>. So check the <b>clef</b> first. The Queen's curl is the treble clef, the King's two dots the bass clef.</>")
rep("<><b>왕관 확인 놀이:</b> 선생님이 음표 카드를 보여 줘요. \"퀸즈랜드!\"나 \"킹스랜드!\"를 먼저 외치고, 이름을 말하고, 쳐요.</>",
    "<><b>음자리표 확인 놀이:</b> 선생님이 음표 카드를 보여 줘요. \"높은음자리표!\"나 \"낮은음자리표!\"를 먼저 외치고, 이름을 말하고, 쳐요.</>")
rep("<>같은 자리, 다른 이름: 2번 줄을 오른손으로 G, 왼손으로 B, 두 나라에서 한 번씩 쳐요.</>",
    "<>같은 자리, 다른 이름: 2번 줄을 오른손으로 G, 왼손으로 B, 두 오선에서 한 번씩 쳐요.</>")
rep("<><b>Crown check game:</b> your teacher shows a note card. Call out \"Queensland!\" or \"Kingsland!\" first, then name the note and play it.</>",
    "<><b>Clef check game:</b> your teacher shows a note card. Call out \"Treble!\" or \"Bass!\" first, then name the note and play it.</>")
rep("<>Same place, two names: play line 2 in both lands, G with the right hand, B with the left.</>",
    "<>Same place, two names: play line 2 in both clefs, G with the right hand, B with the left.</>")
rep("t('Crown check first: whose land is it?', '왕관 확인 먼저: 어느 나라예요?')", "t('Clef check first: treble or bass?', '음자리표 확인 먼저: 높은음자리표, 낮은음자리표?')")
rep("title={t('Queensland', '퀸즈랜드')}>", "title={t('Treble clef', '높은음자리표')}>")
rep("title={t('Kingsland', '킹스랜드')}>", "title={t('Bass clef', '낮은음자리표')}>")
rep("<>여왕의 다섯 <b>줄</b>은 아래에서부터 <b>E G B D F</b>", "<>높은음자리표의 다섯 <b>줄</b>은 아래에서부터 <b>E G B D F</b>")
rep("<>The Queen's five <b>lines</b>, from the bottom, are <b>E G B D F</b>: <b>{A('B1', 'Every Good Boy Deserves Fun')}</b>. Her four <b>spaces</b> are <b>F A C E</b>, her hidden <b>FACE</b>.",
    "<>The treble clef's five <b>lines</b>, from the bottom, are <b>E G B D F</b>: <b>{A('B1', 'Every Good Boy Deserves Fun')}</b>. Its four <b>spaces</b> are <b>F A C E</b>, the Queen's hidden <b>FACE</b>.")
rep("t('Queensland: Every Good Boy Deserves Fun on the lines, the Queen\\'s FACE in the spaces.', '퀸즈랜드: 줄에는 Every Good Boy Deserves Fun, 칸에는 여왕의 FACE.')",
    "t('Treble clef: Every Good Boy Deserves Fun on the lines, the Queen\\'s FACE in the spaces.', '높은음자리표: 줄에는 Every Good Boy Deserves Fun, 칸에는 여왕의 FACE.')")
rep("<>왕의 다섯 <b>줄</b>은 <b>G B D F A</b>. 용이 줄을 따라 날아가요: <b>Great Big Dragon Flies Away</b>. 네 <b>칸</b>은 <b>A C E G</b>. 소들이 칸에서 풀을 먹어요: <b>All Cows Eat Grass</b>. 문장은 저마다 자기 나라에서만 써요.</>",
    "<>낮은음자리표의 다섯 <b>줄</b>은 <b>G B D F A</b>. 왕의 용이 줄을 따라 날아가요: <b>Great Big Dragon Flies Away</b>. 네 <b>칸</b>은 <b>A C E G</b>. 왕의 소들이 칸에서 풀을 먹어요: <b>All Cows Eat Grass</b>. 문장은 저마다 자기 음자리표에서만 써요.</>")
rep("<>The King's five <b>lines</b> are <b>G B D F A</b>. His dragon flies along them: <b>Great Big Dragon Flies Away</b>. His four <b>spaces</b> are <b>A C E G</b>. His cows graze there: <b>All Cows Eat Grass</b>. Each saying works only in its own land.</>",
    "<>The bass clef's five <b>lines</b> are <b>G B D F A</b>. The King's dragon flies along them: <b>Great Big Dragon Flies Away</b>. Its four <b>spaces</b> are <b>A C E G</b>. The King's cows graze there: <b>All Cows Eat Grass</b>. Each saying works only in its own clef.</>")
rep("t('Kingsland: the King\\'s dragon flies on the lines, his cows eat grass in the spaces.', '킹스랜드: 왕의 용은 줄 위를 날고, 소들은 칸에서 풀을 먹어요.')",
    "t('Bass clef: the King\\'s dragon flies on the lines, his cows eat grass in the spaces.', '낮은음자리표: 왕의 용은 줄 위를 날고, 소들은 칸에서 풀을 먹어요.')")
rep("선생님이 음표 하나를 짚으면 왕관 확인 →", "선생님이 음표 하나를 짚으면 음자리표 확인 →")
rep("your teacher points to a note. Crown check →", "your teacher points to a note. Clef check →")
rep("t('Crown check first: I name the land before the note', '왕관 확인 먼저: 음 이름보다 나라를 먼저 말해요')",
    "t('Clef check first: I name the clef before the note', '음자리표 확인 먼저: 음 이름보다 음자리표를 먼저 말해요')")
rep("t('I can read every line and space in Queensland', '퀸즈랜드의 모든 줄과 칸을 읽을 수 있어요')", "t('I can read every line and space in the treble clef', '높은음자리표의 모든 줄과 칸을 읽을 수 있어요')")
rep("t('I can read every line and space in Kingsland', '킹스랜드의 모든 줄과 칸을 읽을 수 있어요')", "t('I can read every line and space in the bass clef', '낮은음자리표의 모든 줄과 칸을 읽을 수 있어요')")
# pictures: the watermark and the little heads say the real names
rep("landName(t('QUEENSLAND', '퀸즈랜드'), 34, 'treble', 160), landName(t('KINGSLAND', '킹스랜드'), 22, 'bass', 160)",
    "landName(t('TREBLE CLEF', '높은음자리표'), 34, 'treble', 160), landName(t('BASS CLEF', '낮은음자리표'), 22, 'bass', 160)")
rep("landName(t('QUEENSLAND', '퀸즈랜드'), 34, 'treble', 186), landName(t('KINGSLAND', '킹스랜드'), 22, 'bass', 186)",
    "landName(t('TREBLE CLEF', '높은음자리표'), 34, 'treble', 186), landName(t('BASS CLEF', '낮은음자리표'), 22, 'bass', 186)")
rep("t('The grand staff as a map of two lands: QUEENSLAND is the top staff, with the Queen\\'s chess piece beside it; KINGSLAND is the bottom staff, with the King\\'s chess piece beside it; Clara, a pink pawn, between them', '큰보표는 두 나라의 지도: 위 오선은 퀸즈랜드, 옆에 여왕의 체스 말; 아래 오선은 킹스랜드, 옆에 왕의 체스 말; 그 사이에 분홍 폰 클라라')",
    "t('The grand staff: the top staff has the treble clef, with the Queen\\'s chess piece beside it; the bottom staff has the bass clef, with the King\\'s chess piece beside it; Clara, a pink pawn, between them', '큰보표: 위 오선에는 높은음자리표, 옆에 여왕의 체스 말; 아래 오선에는 낮은음자리표, 옆에 왕의 체스 말; 그 사이에 분홍 폰 클라라')")
rep("t('In Queensland (treble clef) the note on line 2 is G', '퀸즈랜드(높은음자리표)에서 2번 줄 음표는 G') : t('In Kingsland (bass clef) the note on line 2 is B', '킹스랜드(낮은음자리표)에서 2번 줄 음표는 B')",
    "t('In the treble clef the note on line 2 is G', '높은음자리표에서 2번 줄 음표는 G') : t('In the bass clef the note on line 2 is B', '낮은음자리표에서 2번 줄 음표는 B')")

# ── chapter 7 app: the step 1 toy and the drill's first level ──
rep("t('Tap a line or a space: see its name in each land, and hear both.', '줄이나 칸을 눌러 봐요: 두 나라에서의 이름을 보고, 두 소리를 들어요.')",
    "t('Tap a line or a space: see its name in each clef, and hear both.', '줄이나 칸을 눌러 봐요: 두 음자리표에서의 이름을 보고, 두 소리를 들어요.')")
rep("t('WHOSE LAND?', '어느 나라?') : t('Crown check: whose land is this note in?', '왕관 확인: 이 음은 어느 나라에 있나요?')",
    "t('TREBLE OR BASS?', '높은음? 낮은음?') : t('Clef check: treble or bass?', '음자리표 확인: 높은음자리표, 낮은음자리표?')")
rep("t('The Queen\\'s curl: Queensland. This note is ', '여왕의 소용돌이: 퀸즈랜드. 이 음은 ') : t('The King\\'s two dots: Kingsland. This note is ', '왕의 두 점: 킹스랜드. 이 음은 ')",
    "t('The Queen\\'s curl: the treble clef. This note is ', '여왕의 소용돌이: 높은음자리표. 이 음은 ') : t('The King\\'s two dots: the bass clef. This note is ', '왕의 두 점: 낮은음자리표. 이 음은 ')")
rep("label: 'Crown check: whose land?'", "label: 'Clef check: treble or bass?'")
rep("'Crown check: whose land?': '왕관 확인: 어느 나라?', 'Queensland: every line and space': '퀸즈랜드: 모든 줄과 칸', 'Kingsland: every line and space': '킹스랜드: 모든 줄과 칸'",
    "'Clef check: treble or bass?': '음자리표 확인: 높은음자리표, 낮은음자리표?', 'Treble clef: every line and space': '높은음자리표: 모든 줄과 칸', 'Bass clef: every line and space': '낮은음자리표: 모든 줄과 칸'")
rep("label: 'Queensland: every line and space', ", "label: 'Treble clef: every line and space',")
rep("label: 'Kingsland: every line and space',  ", "label: 'Bass clef: every line and space',  ")
rep("t('𝄞 Queensland', '𝄞 퀸즈랜드') : t('𝄢 Kingsland', '𝄢 킹스랜드')", "t('𝄞 Treble clef', '𝄞 높은음자리표') : t('𝄢 Bass clef', '𝄢 낮은음자리표')")
rep("title: 'The sayings of the two lands', blurb: 'Queensland and Kingsland, line by line, tap by tap.'", "title: 'The sayings of the two clefs', blurb: 'Treble clef and bass clef, line by line, tap by tap.'")
rep("'rhymes': ['두 나라의 외우는 문장', '퀸즈랜드와 킹스랜드, 줄 하나씩, 눌러 가며.']", "'rhymes': ['두 음자리표의 외우는 문장', '높은음자리표와 낮은음자리표, 줄 하나씩, 눌러 가며.']")
rep("t('The Queen\\'s curl wraps round this line: line 2 of Queensland.', '여왕의 소용돌이가 감싸는 줄: 퀸즈랜드의 2번 줄.')", "t('The Queen\\'s curl wraps round this line: line 2 of the treble clef.', '여왕의 소용돌이가 감싸는 줄: 높은음자리표의 2번 줄.')")
rep("t('The King\\'s two dots guard this line: line 4 of Kingsland.', '왕의 두 점이 지키는 줄: 킹스랜드의 4번 줄.')", "t('The King\\'s two dots guard this line: line 4 of the bass clef.', '왕의 두 점이 지키는 줄: 낮은음자리표의 4번 줄.')")
rep("t('Space 3 of Queensland, one octave above Clara.', '퀸즈랜드의 3번 칸, 클라라보다 한 옥타브 위.')", "t('Space 3 of the treble clef, one octave above Clara.', '높은음자리표의 3번 칸, 클라라보다 한 옥타브 위.')")
rep("t('Space 2 of Kingsland, one octave below Clara.', '킹스랜드의 2번 칸, 클라라보다 한 옥타브 아래.')", "t('Space 2 of the bass clef, one octave below Clara.', '낮은음자리표의 2번 칸, 클라라보다 한 옥타브 아래.')")

# ── chapter 7 Workbook and Teacher copy ──
rep('title="Whose land?" how="Look at the crown at the start of each staff. Circle Q for Queensland or K for Kingsland."',
    'title="Treble or bass?" how="Look at the clef at the start of each staff. Circle treble or bass."')
rep("wsChoose(['Q', 'K'], i === 0 ? (cl === 'treble' ? 'Q' : 'K') : null)", "wsChoose(['treble', 'bass'], i === 0 ? (cl === 'treble' ? 'treble' : 'bass') : null)")
rep('title="Crown check, then name it" how="First circle the land: Q for Queensland, K for Kingsland. Then write the note\'s name."',
    'title="Clef check, then name it" how="First circle the clef: treble or bass. Then write the note\'s name."')
rep("wsChoose(['Q', 'K'])", "wsChoose(['treble', 'bass'])", 2)
rep('title="Which crown makes it true?"', 'title="Which clef makes it true?"')
rep('how="All nine of Queensland\'s lines and spaces, mixed up.', 'how="All nine lines and spaces of the treble clef, mixed up.')
rep('title="Name the Queensland notes" how="Crown check: the Queen\'s curl. Then write each letter."', 'title="Name the treble clef notes" how="Clef check: the Queen\'s curl. Then write each letter."')
rep('title="Write words in Queensland" how="Draw each note above its letter: on its line or in its space in the Queen\'s land.',
    'title="Write words in the treble clef" how="Draw each note above its letter: on its line or in its space.')
rep('how="All nine of Kingsland\'s lines and spaces, mixed up.', 'how="All nine lines and spaces of the bass clef, mixed up.')
rep('title="Name the Kingsland notes" how="Crown check: the King\'s two dots. Then write each letter."', 'title="Name the bass clef notes" how="Clef check: the King\'s two dots. Then write each letter."')
rep('how="1-4: draw each note\'s partner in Kingsland. 5-8: draw each partner in Queensland.', 'how="1-4: draw each note\'s partner in the bass clef. 5-8: draw each partner in the treble clef.')
rep("write the partner's letter in Kingsland.\">", "write the partner's letter in the bass clef.\">")
rep('how="Crown check, find the nearest landmark, then hop.', 'how="Clef check, find the nearest landmark, then hop.')
rep('how="Crown check, then write each note\'s letter. This word travels through both lands.', 'how="Clef check, then write each note\'s letter. This word travels through both clefs.')
rep("bkSec('A', 'Crown check: circle Q or K, then write the name.')", "bkSec('A', 'Clef check: circle treble or bass, then write the name.')")
rep("bkSec('B', 'Queensland: name the notes.')", "bkSec('B', 'Treble clef: name the notes.')")
rep("bkSec('C', 'Kingsland: name the notes.')", "bkSec('C', 'Bass clef: name the notes.')")
rep("write the letter of each note\\'s partner in Kingsland.')", "write the letter of each note\\'s partner in the bass clef.')")
rep("Crown check first, every time: the sayings belong to their land.", "Clef check first, every time: each saying belongs to its clef.")
rep('<TcBlock page={2} title="Crown check first"', '<TcBlock page={2} title="Clef check first"')
rep("const land = (cl) => cl === 'treble' ? 'Q' : 'K';", "const land = (cl) => cl === 'treble' ? 'treble' : 'bass';")
rep('watch="Naming before looking at the clef, the most common slip of all. And reading a Kingsland note with a Queensland saying (two letters too high)."',
    'watch="Naming before looking at the clef, the most common slip of all. And reading a bass clef note with a treble clef saying (two letters too high)."')
rep('say="“Crown check first: whose land is it?”"', 'say="“Clef check first: treble or bass?”"')
rep('<TcBlock page={3} title="Queensland"', '<TcBlock page={3} title="Treble clef"')
rep('<TcBlock page={4} title="Kingsland"', '<TcBlock page={4} title="Bass clef"')
rep('say="“Crown check, then the nearest friend.”"', 'say="“Clef check, then the nearest friend.”"')
rep("The crown check game and the landmark hop need only note cards.", "The clef check game and the landmark hop need only note cards.")
rep("const WS_LAND = { treble: 'Queensland', bass: 'Kingsland' };", "const WS_LAND = { treble: 'treble clef', bass: 'bass clef' };")
rep("answerLabel: (q) => q.kind === 'crown' ? (q.answer === 'treble' ? t('Queensland', '퀸즈랜드') : t('Kingsland', '킹스랜드'))",
    "answerLabel: (q) => q.kind === 'crown' ? (q.answer === 'treble' ? t('Treble clef', '높은음자리표') : t('Bass clef', '낮은음자리표'))")

open(B + 't460b0.src.html', 'w').write(s)
print('ok')
