p='drills.src.html'; s=open(p).read()
def rep(o,n,c=1):
    global s
    assert s.count(o)==c,(s.count(o),o[:80]); s=s.replace(o,n)
# m50: the scales map checked against the Grade 5-8 technical list (2 Nov). The rooms were right; four map rows were short.
rep("[F.sim, S5_KEYS.map(nm), '♩ = 84 · ' + t('one scale, four ways', '한 스케일, 네 가지로')], [F.cm, cm(5), '♩ = 60'],",
    "[F.sim, S5_KEYS.map(nm), '♩ = 84 · ' + t('each three ways: p, f, louder up', '세 가지로: p, f, 올라가며 세게')], [t('Staccato', '스타카토'), ['Db', 'Bbmel'].map(nm), 'mf'], [F.cm, cm(5), '♩ = 60'],")
rep("[F.cm, cm(6), '♩ = 72'], [F.poly, [t('as a scale', '스케일로')], ''],",
    "[F.cm, cm(6), '♩ = 72'], [F.chr, ['F♯/G♭'], t('four octaves, three ways', '네 옥타브, 세 가지로')], [F.poly, [t('as an exercise', '연습곡으로')], ''],")
rep("[F.chr, S7_CH.map(x => x[0]), '♩ = 104 · ' + t('hands together', '양손 함께')],",
    "[F.chr, [...S7_CH.map(x => x[0]), t('E♭ (two octaves)', 'E♭ (두 옥타브)')], '♩ = 104 · ' + t('hands together', '양손 함께')],")
rep("[F.chr, [t('in sixes; in double minor thirds', '6도로; 겹단3도로')], '']] },",
    "[F.chr, ['E', 'A♯/B♭'], t('three octaves, in sixes', '세 옥타브, 여섯 음씩')], [t('Chromatic in double thirds', '겹3도 반음계'), ['C', 'E♭'], t('two octaves', '두 옥타브')]] },")
open(p,'w').write(s); print('ok')
# m50b: name the keys where the rows only said 'abbreviated', 'as a scale' or nothing
s=open(p).read()
rep("[F.grand, [t('abbreviated', '줄인 형태')], ''],", "[F.grand, ['Eb', 'Cmh'].map(k => SMAP_NAME(k, S6_GR)), t('abbreviated, four octaves', '줄인 형태, 네 옥타브')],")
rep("[F.poly, [t('as a scale', '스케일로')], ''], [F.cm, cm(7), '♩ = 80'],", "[F.poly, ['D major', 'B harmonic minor'], t('three octaves against two', '세 옥타브 대 두 옥타브')], [F.cm, cm(7), '♩ = 80'],")
rep("[F.poly, [t('two against three', '2 대 3')], ''], [F.apart, [], ''],", "[t('Two against three', '2 대 3'), ['E major'], ''], [F.apart, S8_GR_KEYS.map(k => SMAP_NAME(k, S6_GR)), t('four octaves', '네 옥타브')],")
open(p,'w').write(s); print('ok b')
