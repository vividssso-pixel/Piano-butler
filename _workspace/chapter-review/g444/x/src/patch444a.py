#!/usr/bin/env python3
# Phase 444a: the black key is a hidden attic (her 16:04 '검은건반을 숨겨진 다락방처럼 내가 쓸 떄도 있고 d가 쓸때도 있고'):
# chapter 11's page 5, its moving part, the Teacher copy. New words carry no '--' (her 16:07).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit('found %d (want %d): %s' % (c, n, a[:100]))
    s = s.replace(a, b)
# page 5, the words
rep("""<><b>샤프 {tnSign('#')}</b>는 음을 <b>반 걸음 위로</b> 옮겨요 -- 오른쪽 바로 옆 건반으로. 그래서 C 바로 오른쪽 검은건반은 <b>C 샤프, C{tnSign('#')}</b>예요. <b>플랫 {tnSign('b')}</b>은 음을 <b>반 걸음 아래로</b> 옮겨요 -- 왼쪽 바로 옆 건반으로. 그래서 같은 검은건반을 D에서 보면 <b>D 플랫, D{tnSign('b')}</b>이에요. 건반 하나, 이름 둘: 클라라의 C에서 반 걸음 위, 강아지의 D에서 반 걸음 아래예요. 그런데 샤프나 플랫이 늘 검은건반인 건 아니에요: E에서 반 걸음 위는 흰건반 F라서, E 샤프는 F와 같은 건반이에요.</>""",
"""<><b>샤프 {tnSign('#')}</b>는 음을 <b>반 걸음 위로</b>, 오른쪽 바로 옆 건반으로 옮겨요. <b>플랫 {tnSign('b')}</b>은 음을 <b>반 걸음 아래로</b>, 왼쪽 바로 옆 건반으로 옮겨요. 검은건반은 두 방 사이의 <b>숨겨진 다락방</b> 같아요. 양옆 이웃이 같이 써요. 클라라가 C에서 쓰면 <b>C 샤프, C{tnSign('#')}</b>, 강아지가 D에서 쓰면 <b>D 플랫, D{tnSign('b')}</b>이에요. 다락방 하나, 이름 둘. 그런데 E와 F 사이에는 다락방이 없어요. E에서 반 걸음 위는 바로 옆집 흰건반 F라서, E 샤프는 F와 같은 건반이에요. 샤프나 플랫이 늘 검은건반인 건 아니에요.</>""")
rep("""<>The <b>sharp sign {tnSign('#')}</b> moves a note <b>up a half step</b> -- to the very next key on the right. So the black key just right of C is <b>C sharp, C{tnSign('#')}</b>. The <b>flat sign {tnSign('b')}</b> moves a note <b>down a half step</b> -- to the very next key on the left. So the same black key, seen from D, is <b>D flat, D{tnSign('b')}</b>. One key, two names: a half step up from Clara's C, and a half step down from the Dog's D. But a sharp or a flat is not always a black key: a half step up from E is the white key F, so E sharp is the same key as F.</>""",
"""<>The <b>sharp sign {tnSign('#')}</b> moves a note <b>up a half step</b>, to the very next key on the right. The <b>flat sign {tnSign('b')}</b> moves a note <b>down a half step</b>, to the very next key on the left. A black key is like a <b>hidden attic</b> between two rooms, shared by the neighbours on each side. When Clara uses it from C, it is <b>C sharp, C{tnSign('#')}</b>. When the Dog uses it from D, it is <b>D flat, D{tnSign('b')}</b>. One attic, two names. But between E and F there is no attic: a half step up from E is the white key F next door, so E sharp is the same key as F. A sharp or a flat is not always a black key.</>""")
rep("""<>C를 치고 C{tnSign('#')}를 쳐요 -- 반 걸음 위. D를 치고 D{tnSign('b')}을 쳐요 -- 반 걸음 아래. 같은 검은건반이에요!</>""",
    """<>C를 치고 C{tnSign('#')}를 쳐요: 반 걸음 위. D를 치고 D{tnSign('b')}을 쳐요: 반 걸음 아래. 같은 검은건반, 같은 다락방이에요!</>""")
rep("""<>Play C, then C{tnSign('#')} -- a half step up. Play D, then D{tnSign('b')} -- a half step down. The same black key!</>""",
    """<>Play C, then C{tnSign('#')}: a half step up. Play D, then D{tnSign('b')}: a half step down. The same black key, the same attic!</>""")
rep("""{t(' down a half step -- to the very next key, black or white.', '은 반 걸음 아래 -- 바로 옆 건반으로, 검은건반이든 흰건반이든.')}""",
    """{t(' down a half step: to the very next key, black or white.', '은 반 걸음 아래: 바로 옆 건반으로, 검은건반이든 흰건반이든.')}""")
rep("a navy one a half step down from D to D flat -- the same black key', ", "a navy one a half step down from D to D flat: the same black key, an attic the two neighbours share', ")
rep("남색 점선은 D에서 반 걸음 아래 D 플랫으로 -- 같은 검은건반'), 300)", "남색 점선은 D에서 반 걸음 아래 D 플랫으로: 같은 검은건반, 두 이웃이 같이 쓰는 다락방'), 300)")
# the moving part
rep("""{t('Tap a white key, then tap ♯ up or ♭ down: the sharp moves it a half step up, the flat a half step down -- to the very next key, black or white.', '흰건반을 누르고 ♯ 위로 또는 ♭ 아래로를 눌러요: 샤프는 반 걸음 위로, 플랫은 반 걸음 아래로 옮겨요 -- 바로 옆 건반으로, 검은건반이든 흰건반이든.')}""",
    """{t('Tap a white key, then tap ♯ up or ♭ down. The sharp moves it a half step up, the flat a half step down: to the very next key, black or white.', '흰건반을 누르고 ♯ 위로 또는 ♭ 아래로를 눌러요. 샤프는 반 걸음 위로, 플랫은 반 걸음 아래로 옮겨요: 바로 옆 건반으로, 검은건반이든 흰건반이든.')}""")
rep("""{!on ? t('Off the end of this keyboard -- pick another key.', '건반 끝을 벗어났어요 -- 다른 건반을 골라요.')""",
    """{!on ? t('Off the end of this keyboard. Pick another key.', '건반 끝을 벗어났어요. 다른 건반을 골라요.')""")
rep("""{t(' -- a half step ' + (up ? 'up' : 'down') + ' from ' + L + ', the black key on its ' + (up ? 'right' : 'left') + '. Its other name: ', ' -- ' + L + '에서 반 걸음 ' + (up ? '위' : '아래') + ', ' + (up ? '오른쪽' : '왼쪽') + ' 검은건반이에요. 다른 이름: ')}<b>{prettyNote(land.find(x => x !== name))}</b>.</>""",
    """{t(': a half step ' + (up ? 'up' : 'down') + ' from ' + L + ', into the attic on its ' + (up ? 'right' : 'left') + '. The neighbour on the other side calls it ', ': ' + L + '에서 반 걸음 ' + (up ? '위' : '아래') + ', ' + (up ? '오른쪽' : '왼쪽') + ' 다락방이에요. 반대쪽 이웃이 부르는 이름은 ')}<b>{prettyNote(land.find(x => x !== name))}</b>.</>""")
rep("""{t(' -- a half step ' + (up ? 'up' : 'down') + ' from ' + L + ' is the white key ' + land[0] + ': the same key. A ' + (up ? 'sharp' : 'flat') + ' is not always a black key.', ' -- ' + L + '에서 반 걸음 ' + (up ? '위' : '아래') + '는 흰건반 ' + land[0] + ': 같은 건반이에요. ' + (up ? '샤프가' : '플랫이') + ' 늘 검은건반인 건 아니에요.')}""",
    """{t(': no attic between ' + (up ? L + ' and ' + land[0] : land[0] + ' and ' + L) + ', so a half step ' + (up ? 'up' : 'down') + ' from ' + L + ' is the white key ' + land[0] + ' next door. The same key! A ' + (up ? 'sharp' : 'flat') + ' is not always a black key.', ': ' + (up ? L + '와 ' + land[0] : land[0] + '와 ' + L) + ' 사이엔 다락방이 없어서, ' + L + '에서 반 걸음 ' + (up ? '위' : '아래') + '는 바로 옆집 흰건반 ' + land[0] + '예요. 같은 건반! ' + (up ? '샤프가' : '플랫이') + ' 늘 검은건반인 건 아니에요.')}""")
# the Teacher copy
rep("""      say="“A half step up from C is C sharp; a half step down from D is D flat -- the same key.”"/>""",
    """      say="“A black key is a hidden attic two neighbours share: from C it is C sharp, from D it is D flat. No attic between E and F, so E sharp is F.”"/>""")
open(dst, 'w', encoding='utf-8').write(s); print('444a applied')
