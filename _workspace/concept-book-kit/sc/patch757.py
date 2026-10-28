import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CL (call 21, her 09:38: major chords in capitals, minor in small letters, as the app writes them): the last places
# that still wrote minor chords in capitals. Student-facing: the Grade 4 chords check. Teacher notes: written the app's way,
# the syllabus's capitals named where they are quoted.
rep("t('I name the chords on I, II, IV, V and VI in four parts', '네 성부의 I, II, IV, V, VI 화음 이름을 말해요')",
    "t('I name the chords I, ii, IV, V and vi (i, iv, V and VI in a minor key) in four parts', '네 성부의 I, ii, IV, V, vi 화음(단조에서는 i, iv, V, VI) 이름을 말해요')")
rep("t('First inversions (Ib, IIb, IVb, Vb, VIb): the 3rd in the bass.", "t('First inversions (Ib, iib, IVb, Vb, vib; the syllabus writes IIb and VIb): the 3rd in the bass.")
rep("'첫째 자리바꿈(Ib, IIb, IVb, Vb, VIb): 3음이 베이스.", "'첫째 자리바꿈(Ib, iib, IVb, Vb, vib; 실라버스는 IIb, VIb로 적어요): 3음이 베이스.")
rep("interrupted V–VI (the 3rd of VI doubled).", "interrupted V–vi (V–VI in a minor key, the 3rd of VI doubled).")
rep("거짓종지 V–VI(VI의 3음을 겹쳐요).", "거짓종지 V–vi(단조에서는 V–VI, VI의 3음을 겹쳐요).")
rep("t('Theory of Music Grade 4 harmony, one step each: the chords on I, II, IV, V and VI, root position", "t('Theory of Music Grade 4 harmony, one step each: the chords I, ii, IV, V and vi (i, iv, V and VI in a minor key), root position")
rep("'이론 4급 화성을 한 단계씩: I, II, IV, V, VI 화음, 기본 위치", "'이론 4급 화성을 한 단계씩: I, ii, IV, V, vi 화음(단조에서는 i, iv, V, VI), 기본 위치")
rep("t('Theory of Music Grade 5 harmony vocabulary: I II IV V VI (II in major keys only), Ib IIb IVb Vb VIb VIIb, and Ic as a cadential 6-4. VIIb is new: the leading-note chord in first inversion, usually between I and Ib (I–VIIb–Ib, the bass rising by step).",
    "t('Theory of Music Grade 5 harmony vocabulary, as the syllabus prints it: I II IV V VI (II in major keys only), Ib IIb IVb Vb VIb VIIb, and Ic as a cadential 6-4. vii°b (the syllabus: VIIb) is new: the leading-note chord in first inversion, usually between I and Ib (I–vii°b–Ib, the bass rising by step).")
rep("'이론 5급 화성의 어휘: I II IV V VI(II는 장조만), Ib IIb IVb Vb VIb VIIb, 그리고 종지의 6-4인 Ic. VIIb가 새로워요: 이끎음 위 화음의 첫째 자리바꿈, 흔히 I과 Ib 사이(I–VIIb–Ib, 베이스가 한 음씩 올라가요).",
    "'이론 5급 화성의 어휘(실라버스 표기): I II IV V VI(II는 장조만), Ib IIb IVb Vb VIb VIIb, 그리고 종지의 6-4인 Ic. vii°b(실라버스: VIIb)가 새로워요: 이끎음 위 화음의 첫째 자리바꿈, 흔히 I과 Ib 사이(I–vii°b–Ib, 베이스가 한 음씩 올라가요).")
rep("Before V: IIb, IV, IVb or Ic in a major key; IIb, IV, IVb, VI or Ic in a minor key (only II in root position is major keys only).",
    "Before V: iib, IV, IVb or Ic in a major key; ii°b, iv, ivb, VI or ic in a minor key (the syllabus writes IIb, IV, IVb, VI, Ic for both; only II in root position is major keys only).")
rep("V 앞에: 장조에서는 IIb, IV, IVb, Ic; 단조에서는 IIb, IV, IVb, VI, Ic(근음 자리의 II만 장조 전용).",
    "V 앞에: 장조에서는 iib, IV, IVb, Ic; 단조에서는 ii°b, iv, ivb, VI, ic(실라버스는 둘 다 IIb, IV, IVb, VI, Ic로 적어요; 근음 자리의 II만 장조 전용).")
rep("Its harmony vocabulary, major and minor keys: I II III IV V VI and their first inversions;", "Its harmony vocabulary, major and minor keys, as the syllabus prints it: I II III IV V VI and their first inversions;")
rep("화성 어휘, 장조와 단조: I II III IV V VI과 첫째 자리바꿈;", "화성 어휘, 장조와 단조(실라버스 표기): I II III IV V VI과 첫째 자리바꿈;")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
