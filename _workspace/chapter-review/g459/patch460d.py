# Phase 460d: the fresh reviewer's points on 460a-c.
import re
B = '/home/claude/pbtest/g460/out/'
s = open(B + 't460b.src.html').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:120])
    s = s.replace(old, new)

# 1. the staff chapter's teacher sayings
rep('say="“Crown check first: whose palace is this? The curl holds', 'say="“Clef check first: treble or bass? The curl holds')
rep('say="“Crown check: this is the King\'s staff. His two dots guard F.', 'say="“Clef check: bass clef, the King\'s staff. His two dots guard F.')
rep('say="“Crown check, then count from the nearest friend:', 'say="“Clef check, then count from the nearest friend:')
# 2. the staff chapter's 'Next' line: one colon
rep("' · Line and Space Names: every line and space in the treble and bass clefs, and their sayings.', bkChapterNo('whole-staff') + '챕터 · 줄과 칸 이름: 높은음자리표와 낮은음자리표의 모든 줄과 칸, 그리고 외우는 문장들.'",
    "' · Line and Space Names. Every line and space on the treble and bass staves, and their sayings.', bkChapterNo('whole-staff') + '챕터 · 줄과 칸 이름. 높은음자리표 오선과 낮은음자리표 오선의 모든 줄과 칸, 그리고 외우는 문장들.'")
# 3. the fold: which Cs meet
rep("칸의 <b>C</b>는 <b>C</b>에, 클라라는 클라라에.", "위 오선 칸의 <b>C</b>는 아래 오선 칸의 <b>C</b>에, 클라라는 클라라에 닿아요.")
rep("Space <b>C</b> lands on space <b>C</b>, Clara on Clara.", "The <b>C</b> in the treble spaces lands on the <b>C</b> in the bass spaces. Clara lands on Clara.")
# 4. clef check page: space 1 in each clef
rep("<b>1번 칸</b>은 <b>F</b>와 <b>A</b>.", "<b>1번 칸</b>은 높은음자리표에서 <b>F</b>, 낮은음자리표에서 <b>A</b>.")
rep("<b>Space 1</b> is <b>F</b> and <b>A</b>.", "<b>Space 1</b> is <b>F</b> in the treble clef, <b>A</b> in the bass clef.")
# 5. no long dash
rep("{t('Make up your own', '나만의 가락')}</b> — {t(", "{t('Make up your own', '나만의 가락')}</b>: {t(")
# 6. a label that ran out of its box
rep("if (k === 1) return up ? (ko ? L + ' 맨 윗줄 바로 위 칸' : 'just over ' + L + '\\'s top line') : (ko ? L + ' 맨 아랫줄 바로 아래 칸' : 'just under ' + L + '\\'s bottom line');",
    "if (k === 1) return up ? (ko ? L + ' 맨 윗줄 바로 위 칸' : 'just over ' + L) : (ko ? L + ' 맨 아랫줄 바로 아래 칸' : 'just under ' + L);")
# 7. the chapter 7 opener: real names first, the story name as 'its other name'
rep("t('The top staff has the treble clef. It is the Queen\\'s land, Queensland. The bottom staff has the bass clef. It is the King\\'s land, Kingsland. In Chapter '",
    "t('The treble staff is on top. Its other name is Queensland, the Queen\\'s land. The bass staff is below. Its other name is Kingsland, the King\\'s land. In Chapter '")
rep("'위 오선에는 높은음자리표가 있어요. 여왕의 나라, 퀸즈랜드예요. 아래 오선에는 낮은음자리표가 있어요. 왕의 나라, 킹스랜드예요. '",
    "'높은음자리표 오선은 위에 있어요. 다른 이름은 여왕의 나라, 퀸즈랜드예요. 낮은음자리표 오선은 아래에 있어요. 다른 이름은 왕의 나라, 킹스랜드예요. '")
# 8-11. a place on the page is a staff
rep("this line: line 2 of the treble clef.', '여왕의 소용돌이가 감싸는 줄: 높은음자리표의 2번 줄.'", "this line: line 2 of the treble staff.', '여왕의 소용돌이가 감싸는 줄: 높은음자리표 오선의 2번 줄.'")
rep("this line: line 4 of the bass clef.', '왕의 두 점이 지키는 줄: 낮은음자리표의 4번 줄.'", "this line: line 4 of the bass staff.', '왕의 두 점이 지키는 줄: 낮은음자리표 오선의 4번 줄.'")
rep("t('Space 3 of the treble clef, one octave above Clara.', '높은음자리표의 3번 칸,", "t('Space 3 of the treble staff, one octave above Clara.', '높은음자리표 오선의 3번 칸,")
rep("t('Space 2 of the bass clef, one octave below Clara.', '낮은음자리표의 2번 칸,", "t('Space 2 of the bass staff, one octave below Clara.', '낮은음자리표 오선의 2번 칸,")
rep("<>The treble clef's five <b>lines</b>, from the bottom,", "<>The treble staff's five <b>lines</b>, from the bottom,")
rep("<>높은음자리표의 다섯 <b>줄</b>은 아래에서부터", "<>높은음자리표 오선의 다섯 <b>줄</b>은 아래에서부터")
rep("<>The bass clef's five <b>lines</b> are", "<>The bass staff's five <b>lines</b> are")
rep("<>낮은음자리표의 다섯 <b>줄</b>은", "<>낮은음자리표 오선의 다섯 <b>줄</b>은")
rep("Each saying works only in its own clef.</>", "Each saying works only on its own staff.</>")
rep("문장은 저마다 자기 음자리표에서만 써요.</>", "문장은 저마다 자기 오선에서만 써요.</>")
rep("<>오른손으로 높은음자리표의 네 음을 읽고 쳐요:", "<>오른손으로 높은음자리표 오선의 네 음을 읽고 쳐요:")
rep("<>왼손으로 낮은음자리표의 네 음을 읽고 쳐요:", "<>왼손으로 낮은음자리표 오선의 네 음을 읽고 쳐요:")
rep("<>Read and play the treble clef's four notes with the right hand:", "<>Read and play the four notes on the treble staff with the right hand:")
rep("<>Read and play the bass clef's four with the left hand:", "<>Read and play the four on the bass staff with the left hand:")
rep('how="All nine lines and spaces of the treble clef, mixed up.', 'how="All nine lines and spaces of the treble staff, mixed up.')
rep('how="All nine lines and spaces of the bass clef, mixed up.', 'how="All nine lines and spaces of the bass staff, mixed up.')
rep("This word travels through both clefs.", "This word travels across both staves.")
rep('watch="Using the treble clef\'s sayings in the bass clef.', 'watch="Using the treble sayings on the bass staff.')
# 12. Korean: 오선 wherever the English says staff (lines, spaces, top and bottom lines)
s2 = []
for L in s.split('\n'):
    if not L.lstrip().startswith('//'):
        L = re.sub(r'(높은|낮은)음자리표 (맨|첫째|둘째|셋째|넷째)', r'\1음자리표 오선 \2', L)
        L = re.sub(r'(높은|낮은)음자리표 <b>맨', r'\1음자리표 오선 <b>맨', L)
        L = re.sub(r'(높은|낮은)음자리표의 (다섯 줄|네 칸)', r'\1음자리표 오선의 \2', L)
        L = L.replace("'두 음이 자기만의 짧은 줄 위에 있는 높은음자리표:", "'두 음이 자기만의 짧은 줄 위에 있는 높은음자리표 오선:")
    s2.append(L)
s = '\n'.join(s2)
# 13. a natural Korean question
rep("높은음자리표, 낮은음자리표?", "높은음자리표? 낮은음자리표?", 3)
# 14-18. Korean grammar
rep("<><b>팔꿈치가 몸 바로 앞에</b>, 옆구리에서 주먹 하나만큼 떨어지게 의자를 앞뒤로 옮겨요.</>", "<><b>팔꿈치가 몸 바로 앞에</b> 오게, 옆구리에서 주먹 하나만큼 떨어지게 의자를 앞뒤로 옮겨요.</>")
rep("여섯 동작을 <b>이 순서대로</b>, 몸의 큰 부분부터 작은 부분까지.", "여섯 동작을 <b>이 순서대로</b> 해요: 몸의 큰 부분부터 작은 부분까지.")
rep("워크북에 따라 그리는 쪽이 있어요.", "따라 그리는 쪽은 워크북에 있어요.", 2)
rep("<b>F 줄 위의 점</b>에서 시작해", "<b>F 줄에 찍은 점</b>에서 시작해")
rep("빨리 읽는 사람은 매번 문장을 외우지 않아요.", "빨리 읽는 사람은 매번 문장을 처음부터 외우지 않아요.")
rep("<><b>가운데 도</b>에서 다음 C까지 흰건반 8개를 글자를 말하며 올라가요.", "<><b>가운데 도</b>에서 다음 C까지 흰건반 8개를 올라가며 글자를 말해요.")
rep("'음자리표 확인 먼저: 음 이름보다 음자리표를 먼저 말해요'", "'음자리표 확인 먼저: 음 이름 전에 음자리표를 말해요'")
rep("<b>둘째 줄</b>이 <b>여왕의 집</b>: 그 줄의 음은 모두 <b>G</b>예요.", "아래에서 <b>둘째 줄</b>이 <b>여왕의 집</b>이에요. 그 줄의 음은 모두 <b>G</b>예요.")
rep("<b>넷째 줄</b> 바로 위와 바로 아래에 있어요. 그 줄이 왕의 집: 그 줄의 음은 모두 <b>F</b>예요.", "아래에서 <b>넷째 줄</b> 바로 위와 바로 아래에 있어요. 그 줄이 왕의 집이에요. 그 줄의 음은 모두 <b>F</b>예요.")
# 19. the free wrist
rep("손목은 자유롭게: 손끝을 건반에 댄 채, 팔뚝 아래 <b>롤러</b>가 있듯 손이 위아래, 좌우로 흔들려요.", "손목은 자유롭게 둬요. 손끝을 건반에 댄 채, 팔뚝 아래 <b>롤러</b>가 있듯 손이 위아래, 좌우로 흔들려요.")
rep("A free wrist: tip on the key, the hand sways up and down and side to side, as if on a <b>roller</b> under the forearm.",
    "Keep the wrist free. With the tip on the key, the hand sways up and down and side to side, as if a <b>roller</b> sat under the forearm.")
# 20. tasks with a verb
rep("<>Right hand, from <b>middle C</b> up to <b>G</b>: C D E F G.", "<>With your right hand, walk up from <b>middle C</b> to <b>G</b>: C D E F G.")
rep("<>Left hand, from <b>middle C</b> down to <b>F</b>: C B A G F.", "<>With your left hand, walk down from <b>middle C</b> to <b>F</b>: C B A G F.")
# 21. the ledger line, by name
rep("line, space, line, space. Draw it <b>a little wider than the note</b>,", "line, space, line, space. Draw a ledger line <b>a little wider than the note</b>,")
# 22. the half step
rep("A <b>half step</b> is the smallest step on the piano: to the <b>very next key</b>, black or white. It is the key's <b>nearest neighbour</b>.",
    "A <b>half step</b> is the smallest step on the piano: from a key to its <b>nearest neighbour</b>, black or white.")
rep("<><b>반 걸음</b>은 피아노에서 가장 작은 걸음이에요: <b>바로 옆 건반</b>까지, 검은건반이든 흰건반이든. 그 건반의 <b>가장 가까운 이웃</b>이에요.",
    "<><b>반 걸음</b>은 피아노에서 가장 작은 걸음이에요: 한 건반에서 <b>가장 가까운 이웃</b> 건반까지, 검은건반이든 흰건반이든.")
# 23. counted from the bottom
rep("Its curl wraps the <b>second line</b>, the <b>Queen's house</b>:", "Its curl wraps the <b>second line</b> from the bottom, the <b>Queen's house</b>:")
rep("just above and below the <b>fourth line</b>. That line", "just above and below the <b>fourth line</b> from the bottom. That line")
# 24. small wording
rep("They count from the nearest <b>landmark</b>, usually a step or a skip.", "They count from the nearest <b>landmark</b>, usually a step or a skip away.")
rep("<b>Visiting the Queen</b>, write her just under the Queen's staff.", "<b>Visiting the Queen</b>, her note goes just under the Queen's staff.")
# 25. Clara: the name first, 'a little princess' after
rep("<b>C</b>: 작은 집 왼쪽 문의 꼬마 공주 <b>클라라(Clara)</b>.", "<b>C</b>: 작은 집 왼쪽 문의 <b>클라라(Clara)</b>, 꼬마 공주예요.")
# 26. the other spelling
rep("A ledger line is also spelled leger line (AMEB accepts both).", "Its other spelling is leger line.")

open(B + 't460c.src.html', 'w').write(s)

# the guide pages
def grep(p, pairs):
    g = open(B + p).read()
    for a, b in pairs:
        assert g.count(a) == 1, (p, a)
        g = g.replace(a, b)
    open(B + p, 'w').write(g)
grep('posture-hands.html', [("<li><b>A free wrist:</b> tip on the key, the hand sways up and down and side to side, as if on a roller under the forearm.</li>",
                             "<li><b>A free wrist:</b> with the fingertip on the key, the hand sways up and down and side to side, as if a roller sat under the forearm.</li>")])
grep('ledger-lines.html', [("lets each hand stay in its own staff.</p>", "lets each hand stay on its own staff.</p>"),
                           ("Writing it in each hand's own staff keeps", "Writing it on each hand's own staff keeps"),
                           ("<p>Draw it <b>a little wider than the note</b>,", "<p>Draw a ledger line <b>a little wider than the note</b>,")])
grep('tones.html', [("<p>A <b>half step</b> is the smallest step on the piano: to the <b>very next key</b>, black or white. It is the key's nearest neighbour.</p>",
                     "<p>A <b>half step</b> is the smallest step on the piano: from a key to its <b>nearest neighbour</b>, black or white.</p>")])
grep('note-names.html', [("then make the names fast, until", "then make the names come fast, until")])
print('ok')
