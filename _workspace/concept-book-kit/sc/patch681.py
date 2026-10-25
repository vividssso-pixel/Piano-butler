import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build S (her 2026-10-25, option 1: two new rooms and the topics in turn): the Beginner floor in its new order -- the topics
# alternate and what must come first comes first (the tie in Time signatures before slur-or-tie in Dynamics; C position and the
# staff before Steps & skips). Two new rooms wait off the map until their chapters exist: Hand positions (5) and Listen and
# sing (6). Chapter numbers follow the new order everywhere (the books number from the map).
rep("""  { ids: ['posture-hands', 'first-steps', 'pulse', 'note-names', 'note-values', 'staff', 'whole-staff', 'time-signatures', 'reading-steps', 'dynamics', 'tones', 'pitch-range'], en: ['Beginner', 'Sitting well, the keys and their letters, a steady beat, note values, the staff and time signatures, the first tunes, loud and soft, half and whole steps, high and low.'], ko: ['Beginner', '바른 자세, 건반과 글자, 일정한 박, 음표 길이, 오선과 박자표, 첫 선율, 셈여림, 반음과 온음, 높고 낮은 소리.'] },""",
    """  { ids: ['posture-hands', 'first-steps', 'pulse', 'note-names', 'hand-positions', 'listen-sing', 'note-values', 'staff', 'reading-steps', 'whole-staff', 'time-signatures', 'dynamics', 'pitch-range', 'tones'], en: ['Beginner', 'Sitting and hands, the keys and their letters, beat and note values, listening and singing, the staff and the first tunes, loud and soft, high and low, half and whole steps.'], ko: ['Beginner', '자세와 손, 건반과 글자, 박과 음표 길이, 듣고 노래하기, 오선과 첫 선율, 셈여림, 높고 낮은 소리, 반음과 온음.'] },   // Build S: the topics in turn""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
