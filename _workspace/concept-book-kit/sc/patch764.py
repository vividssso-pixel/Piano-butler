import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:100])
    s = s.replace(old, new)
# Build CS, part 1 (board call 3, her 21:18 'my metaphors'): the Home's Keys and staff speaks with her words, as the rooms do.
# The small house and the big house for the black-key groups and their doors; the turtle low and the bird high; Clara on
# middle C and Clara's ladder (its ledger line, where the staves fold); the Queen's G and the King's F. Wording follows the
# rooms (First steps, Note names, The whole staff, Ledger lines, Ear prep). Facts and counts are unchanged.
# kq-black
rep("""allLine: ['They come in groups of 2 and 3, always in the same order. Tap to listen.', '2개와 3개씩 모여 있고, 순서는 늘 같아요. 눌러 들어 보세요.']""",
    """allLine: ['They come in groups of 2 and 3, the small houses and the big houses, always in the same order. Tap to listen.', '2개와 3개씩 모여 있어요. 작은 집과 큰 집이고, 순서는 늘 같아요. 눌러 들어 보세요.']""")
rep("""['Two black keys stand side by side. Count them.', '검은건반 두 개가 나란히 서 있어요. 세어 보세요.']""",
    """['Two black keys stand side by side: a small house. Count them.', '검은건반 두 개가 나란히 서 있어요. 작은 집이에요. 세어 보세요.']""")
rep("""['Then comes a row of three.', '그다음에는 세 개가 줄지어 있어요.']""",
    """['Then comes a row of three: a big house.', '그다음에는 세 개가 줄지어 있어요. 큰 집이에요.']""")
rep("""['Tap along the keys. Left sounds low and right sounds high.', '건반을 눌러 보세요. 왼쪽은 낮은 소리, 오른쪽은 높은 소리예요.']""",
    """['Tap along the keys. Left is low, down with the turtle; right is high, up with the bird.', '건반을 눌러 보세요. 왼쪽은 낮은 소리, 거북이와 함께 아래로. 오른쪽은 높은 소리, 새와 함께 위로.']""")
rep("""yes: ['The higher sound came from the key further right.', '높은 소리는 더 오른쪽 건반에서 났어요.']""",
    """yes: ['The higher sound, the bird’s, came from the key further right.', '높은 소리, 새의 소리는 더 오른쪽 건반에서 났어요.']""")
rep("""'Groups of 2 and 3, and low and high.', '2개와 3개씩 모인 검은건반, 낮은 소리와 높은 소리.'""",
    """'The small and the big houses, the turtle and the bird.', '작은 집과 큰 집, 거북이와 새.'""")
# kq-houses
rep("""name: ['The group of 2', '2개 묶음'] }""", """name: ['The small house', '작은 집'] }""")
rep("""name: ['The group of 3', '3개 묶음'] }""", """name: ['The big house', '큰 집'] }""")
rep("""['Three white keys go with it: one on the left, one between, one on the right.', '흰건반 세 개가 딸려 있어요. 왼쪽, 사이, 오른쪽에 하나씩이에요.']""",
    """['Three white keys live here: one at each door and one inside.', '흰건반 세 개가 살아요. 양쪽 문에 하나씩, 집 안에 하나예요.']""")
rep("""['Four white keys go with it: one on the left, two between, one on the right.', '흰건반 네 개가 딸려 있어요. 왼쪽에 하나, 사이에 둘, 오른쪽에 하나예요.']""",
    """['Four white keys live here: one at each door and two inside.', '흰건반 네 개가 살아요. 양쪽 문에 하나씩, 집 안에 둘이에요.']""")
i = s.index('const KQ_DOOR = {'); j = s.index('};', i) + 2
s = s[:i] + """const KQ_DOOR = {   // Build CS: the doors of her small and big houses (the rooms' words: 'C is at the small house's left door, D is inside, E at the right door')
  C: [['C: the small house’s left door', 'C: 작은 집의 왼쪽 문'], ['It lives at the left door of the small house.', '작은 집의 왼쪽 문에 살아요.'], ['at the small house’s left door', '작은 집의 왼쪽 문'], ['left door', '왼쪽 문']],
  D: [['D: inside the small house', 'D: 작은 집 안'], ['It lives inside, between the two black keys.', '집 안, 두 검은건반 사이에 살아요.'], ['inside the small house', '작은 집 안'], ['inside', '안']],
  E: [['E: the small house’s right door', 'E: 작은 집의 오른쪽 문'], ['It lives at the right door of the small house.', '작은 집의 오른쪽 문에 살아요.'], ['at the small house’s right door', '작은 집의 오른쪽 문'], ['right door', '오른쪽 문']],
  F: [['F: the big house’s left door', 'F: 큰 집의 왼쪽 문'], ['It lives at the left door of the big house.', '큰 집의 왼쪽 문에 살아요.'], ['at the big house’s left door', '큰 집의 왼쪽 문'], ['left door', '왼쪽 문']],
  G: [['G: first inside the big house', 'G: 큰 집 안 첫째'], ['It lives inside, between the 1st and 2nd black keys.', '집 안, 첫째와 둘째 검은건반 사이에 살아요.'], ['between the big house’s 1st and 2nd black keys', '큰 집의 첫째와 둘째 검은건반 사이'], ['inside', '안']],
  A: [['A: second inside the big house', 'A: 큰 집 안 둘째'], ['It lives inside too, between the 2nd and 3rd black keys.', '역시 집 안, 둘째와 셋째 검은건반 사이에 살아요.'], ['between the big house’s 2nd and 3rd black keys', '큰 집의 둘째와 셋째 검은건반 사이'], ['inside', '안']],
  B: [['B: the big house’s right door', 'B: 큰 집의 오른쪽 문'], ['It lives at the right door of the big house.', '큰 집의 오른쪽 문에 살아요.'], ['at the big house’s right door', '큰 집의 오른쪽 문'], ['right door', '오른쪽 문']],
};""" + s[j:]
# the Korean questions built from the door words now read 'the key at ...' (…에 있는 흰건반)
rep("""prompt: ['Which letter is the white key ' + D[2][0] + '?', D[2][1] + '인 흰건반은 어떤 글자일까요?']""",
    """prompt: ['Which letter is the white key ' + D[2][0] + '?', D[2][1] + '에 있는 흰건반은 어떤 글자일까요?']""")
rep("""prompt: ['Tap every white key that is ' + D[2][0] + '.', D[2][1] + '인 흰건반을 모두 눌러 보세요.']""",
    """prompt: ['Tap every white key ' + D[2][0] + '.', D[2][1] + '에 있는 흰건반을 모두 눌러 보세요.']""")
rep("""prompt: ['Tap the white key that is ' + D[2][0] + '.', D[2][1] + '인 흰건반을 눌러 보세요.']""",
    """prompt: ['Tap the white key ' + D[2][0] + '.', D[2][1] + '에 있는 흰건반을 눌러 보세요.']""")
rep("""['Group of 2, group of 3, again and again, with the same seven letters. Tap the keys to hear them.', '2개 묶음, 3개 묶음이 되풀이되고 같은 일곱 글자가 돌아와요. 건반을 눌러 들어 보세요.']""",
    """['Small house, big house, again and again, with the same seven letters. Tap the keys to hear them.', '작은 집, 큰 집이 되풀이되고 같은 일곱 글자가 돌아와요. 건반을 눌러 들어 보세요.']""")
rep("""prompt: ['This white key sits by which group of black keys?', '이 흰건반은 어느 검은건반 묶음 옆에 있을까요?'], opts: [{ id: '2', label: () => t('The group of 2', '2개 묶음') }, { id: '3', label: () => t('The group of 3', '3개 묶음') }]""",
    """prompt: ['Which house does this white key live at?', '이 흰건반은 어느 집에 살까요?'], opts: [{ id: '2', label: () => t('The small house', '작은 집') }, { id: '3', label: () => t('The big house', '큰 집') }]""")
rep("""yes: ['Yes: ' + L + ' belongs to the group of ' + (small ? '2' : '3') + '.', '맞아요. ' + L + '은(는) ' + (small ? '2' : '3') + '개 묶음에 속해요.'], no: ['It is ' + L + ', which belongs to the group of ' + (small ? '2' : '3') + '.', kqYe(L) + '. ' + (small ? '2' : '3') + '개 묶음에 속해요.']""",
    """yes: ['Yes: ' + L + ' lives at the ' + (small ? 'small' : 'big') + ' house.', '맞아요. ' + L + '은(는) ' + (small ? '작은' : '큰') + ' 집에 살아요.'], no: ['It is ' + L + ', and it lives at the ' + (small ? 'small' : 'big') + ' house.', kqYe(L) + '. ' + (small ? '작은' : '큰') + ' 집에 살아요.']""")
rep("""'C D E around the group of 2, F G A B around the group of 3.', '2개 묶음 둘레의 C D E, 3개 묶음 둘레의 F G A B.'""",
    """'C D E at the small house, F G A B at the big house.', '작은 집의 C D E, 큰 집의 F G A B.'""")
rep("""allLine: ['Each white key is named by where it sits next to the black-key groups.', '흰건반은 검은건반 묶음 옆 어디에 있는지로 이름을 붙여요.']""",
    """allLine: ['Each white key is named by where it lives: at the small house or the big house, at a door or inside.', '흰건반은 어디에 사는지로 이름을 붙여요. 작은 집인지 큰 집인지, 문인지 집 안인지예요.']""")
# kq-names: Clara on middle C
rep("""['Each C sits just left of a group of 2, so every C has the same spot.', 'C는 2개 묶음 바로 왼쪽마다 있어서, 모든 C가 같은 자리에 있어요.']""",
    """['Each C lives at the left door of a small house, so every C has the same spot.', 'C는 작은 집마다 왼쪽 문에 살아서, 모든 C가 같은 자리에 있어요.']""")
rep("""['One C has a name of its own: the C in the middle of the keyboard.', 'C 하나는 이름이 따로 있어요. 건반 한가운데 있는 C예요.']""",
    """['One C has a name of its own: middle C, in the middle of the keyboard. Clara lives here.', 'C 하나는 이름이 따로 있어요. 건반 한가운데의 가운데 도예요. 클라라가 여기 살아요.']""")
rep("""['A group of 2 and a group of 3 make one pattern.""", """['A small house and a big house make one pattern.""")
rep("""'2개 묶음과 3개 묶음이 무늬 하나예요.""", """'작은 집과 큰 집이 무늬 하나예요.""")
rep("""['After B the next group of 2 begins, and C comes round again.""", """['After B the next small house begins, and C comes round again.""")
rep("""'B 다음에는 다음 2개 묶음이 시작되고, C가 다시 나와요.""", """'B 다음에는 다음 작은 집이 시작되고, C가 다시 나와요.""")
rep("""['That is not a C. A C sits just left of a group of 2 black keys.', '그건 C가 아니에요. C는 검은건반 2개 묶음 바로 왼쪽에 있어요.']""",
    """['That is not a C. A C lives at the left door of a small house.', '그건 C가 아니에요. C는 작은 집의 왼쪽 문에 살아요.']""")
rep("""y: ['Yes, the C in the middle of the keyboard.', '맞아요. 건반 한가운데의 C예요.']""",
    """y: ['Yes: middle C, Clara’s key, in the middle of the keyboard.', '맞아요. 클라라의 건반, 건반 한가운데의 가운데 도예요.']""")
rep("""t('C = middle C, the C near the middle of the keyboard', 'C = 가운데 도, 건반 한가운데 가까이의 C')""",
    """t('C = middle C, Clara’s key, near the middle of the keyboard', 'C = 가운데 도, 클라라의 건반, 건반 한가운데 가까이')""")
# the staff: Clara between the staves, Clara's ladder, the Queen's G and the King's F
rep("""['Piano music stacks them. Middle C sits between the two staves: the treble staff reads to the right of it, the bass staff to the left.', '피아노 악보는 둘을 겹쳐 써요. 가운데 도는 두 오선 사이에 있어요. 높은음자리 오선은 그 오른쪽, 낮은음자리 오선은 그 왼쪽을 읽어요.']""",
    """['Piano music stacks them. Clara, middle C, sits between the two staves: the treble staff reads to the right of her, the bass staff to the left.', '피아노 악보는 둘을 겹쳐 써요. 클라라, 가운데 도는 두 오선 사이에 있어요. 높은음자리 오선은 그 오른쪽, 낮은음자리 오선은 그 왼쪽을 읽어요.']""")
rep("""['Fold the two staves at middle C and the landmarks mirror each other: G and F, and the two Cs.', '두 오선을 가운데 도에서 접으면 기준 음이 서로 마주 봐요. G와 F, 그리고 두 C예요.']""",
    """['Fold the two staves at Clara’s ladder, middle C, and the landmarks mirror each other: the Queen’s G and the King’s F, and the two Cs.', '두 오선을 클라라의 발판, 가운데 도에서 접으면 기준 음이 서로 마주 봐요. 여왕의 G와 왕의 F, 그리고 두 C예요.']""")
rep("""['The two staves meet at middle C, on a short line of its own. It is the centre of the keyboard too.', '두 오선은 가운데 도에서 만나요. 자기만의 짧은 줄 위에 있고, 건반에서도 한가운데예요.']""",
    """['The two staves meet at middle C, on a short line of its own: Clara’s ladder. It is the centre of the keyboard too.', '두 오선은 가운데 도에서 만나요. 자기만의 짧은 줄, 클라라의 발판 위에 있고, 건반에서도 한가운데예요.']""")
rep("""['Fold at middle C. Treble G, 4 steps above, meets bass F, 4 steps below. On the keyboard they are 7 keys either side.', '가운데 도에서 접어요. 4걸음 위의 높은음자리 G와 4걸음 아래의 낮은음자리 F가 마주 봐요. 건반에서는 양쪽으로 7칸이에요.']""",
    """['Fold at Clara’s ladder. The Queen’s G, 4 steps above, lands on the King’s F, 4 steps below. On the keyboard they are 7 keys either side.', '클라라의 발판에서 접어요. 4걸음 위 여왕의 G가 4걸음 아래 왕의 F에 겹쳐요. 건반에서는 양쪽으로 7칸이에요.']""")
rep("""['When a note is too high or too low for the five lines, short extra lines are added: ledger lines.', '다섯 줄에 담기지 않는 높은 음이나 낮은 음에는 짧은 덧줄을 더해요.']""",
    """['When a note is too high or too low for the five lines, short extra lines are added: ledger lines, the ladders out of the staff.', '다섯 줄에 담기지 않는 높은 음이나 낮은 음에는 짧은 덧줄을 더해요. 오선 밖으로 나가는 발판이에요.']""")
rep("""['A short line below the lowest line.', '가장 아래 줄 밑의 짧은 줄이에요.']""",
    """['A short line below the lowest line: Clara’s ladder.', '가장 아래 줄 밑의 짧은 줄, 클라라의 발판이에요.']""")
rep("""['A short line above the top line. It is the same key.', '가장 위 줄 위의 짧은 줄이에요. 같은 건반이에요.']""",
    """['A short line above the top line: Clara’s ladder again, the same key.', '가장 위 줄 위의 짧은 줄, 역시 클라라의 발판이에요. 같은 건반이에요.']""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
