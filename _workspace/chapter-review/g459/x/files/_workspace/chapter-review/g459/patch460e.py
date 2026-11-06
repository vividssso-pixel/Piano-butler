# Phase 460e: the chapter 1 warm-up cards (book page 3 and the Toolbox), short and plain
B = '/home/claude/pbtest/g460/out/'
s = open(B + 't460c.src.html').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:100]); s = s.replace(old, new)
rep("t('Flop forward and let both arms hang heavy. Shake them loose, then float the hands up and set them gently on the keys.', '앞으로 털썩 숙여 두 팔을 무겁게 늘어뜨려요. 흔들어 힘을 빼고, 손을 둥실 올려 건반 위에 살포시 내려놓아요.')",
    "t('Flop forward, arms hanging heavy. Shake them loose. Float the hands up onto the keys.', '앞으로 털썩 숙여 팔을 무겁게 늘어뜨려요. 흔들어 힘을 빼요. 손을 둥실 올려 건반 위에 내려놓아요.')")
rep("t('Check the elbows are free, not stuck to your body: let them float out like wings, then back. Stop in the middle, a fist from your body.', '팔꿈치가 몸에 붙지 않고 자유로운지 확인해요: 날개처럼 둥실 벌렸다가 돌아와요. 몸에서 주먹 하나만큼 떨어진 가운데에서 멈춰요.')",
    "t('Elbows free, not stuck to your body. Float them out like wings, then back. Stop a fist from your body.', '팔꿈치는 몸에 붙이지 않고 자유롭게. 날개처럼 벌렸다가 돌아와요. 몸에서 주먹 하나만큼 떨어져 멈춰요.')")
rep("t('Now the whole arm: skate along the keys. The round hand rides on the arm to the next group of keys. The fingers ride, they don’t walk.', '이제 팔 전체로 건반 위를 스케이트 타듯 지나가요. 둥근 손은 팔을 타고 다음 건반 묶음으로 가요. 손가락은 걷지 않고 타고 가요.')",
    "t('Skate the whole arm along the keys. The round hand rides to the next group of keys. The fingers ride, they don’t walk.', '팔 전체로 건반 위를 스케이트 타듯 지나가요. 둥근 손은 팔을 타고 다음 건반 묶음으로 가요. 손가락은 걷지 않고 타고 가요.')")
rep("t('Check the bridge: your knuckles are a bridge a little car can drive over. Press one key slowly and hold for 3: the bridge stays up.', '다리를 확인해요: 손가락 마디는 작은 자동차가 지나갈 수 있는 다리예요. 건반 하나를 천천히 누르고 셋을 세는 동안 그대로: 다리는 무너지지 않아요.')",
    "t('Your knuckles are a bridge a little car can drive over. Press one key slowly and hold for 3: the bridge stays up.', '손가락 마디는 작은 자동차가 지나가는 다리예요. 건반 하나를 천천히 누르고 셋을 세요: 다리는 그대로예요.')")
rep("t('Check the wrist never sinks: as the key goes down, a balloon lifts the wrist straight back up to level. The fingertip stays on the key.', '손목이 가라앉지 않는지 확인해요: 건반이 내려가면 풍선이 손목을 바로 같은 높이까지 다시 들어 올려요. 손끝은 건반 위에 그대로 있어요.')",
    "t('The wrist never sinks: as the key goes down, a balloon lifts it back up to level. The fingertip stays on the key.', '손목은 가라앉지 않아요: 건반이 내려가면 풍선이 손목을 같은 높이로 다시 들어 올려요. 손끝은 건반 위에 그대로.')")
rep("{t('Spell and play', '단어 치기')}</b> — {t(", "{t('Spell and play', '단어 치기')}</b>: {t(")
rep("', saying each letter as you play it. Then make up a word of your own.', '. 치면서 글자를 하나씩 말하고, 나만의 단어도 만들어 봐요.')", "', saying each letter as you play it.', '. 치면서 글자를 하나씩 말해요.')")
open(B + 't460d.src.html', 'w').write(s)
print('ok')
