p='drills.src.html'; s=open(p).read()
def rep(o,n,c=1):
    global s
    assert s.count(o)==c,(s.count(o),o[:80]); s=s.replace(o,n)
# 1. Dynamics comes after the staff is read (its workbook reads and plays notes on the staff): after Line and Space Names
rep("'ear-prep', 'note-values', 'dynamics', 'staff', 'reading-steps', 'whole-staff', 'time-signatures', 'tones'], en: ['Beginner',",
    "'ear-prep', 'note-values', 'staff', 'reading-steps', 'whole-staff', 'dynamics', 'time-signatures', 'tones'], en: ['Beginner',")   # m52
rep("'0b': [['dynamics', 'staff'], ['reading-steps', 'whole-staff'], ['time-signatures', 'tones']]", "'0b': [['staff', 'reading-steps'], ['whole-staff', 'dynamics'], ['time-signatures', 'tones']]")
# 2. the bass clef's dots never touch the time signature
rep("""    if (k === 'ts') { [[it[1], Y(low + 6)], [4, Y(low + 2)]].forEach(([n, y]) => out.push('<text x="' + pFix(x + 8) + '" """,
    """    if (k === 'ts') { const bx = clef === 'bass' ? 7 : 0; x += bx;   /* m52: room after the bass clef's two dots */ [[it[1], Y(low + 6)], [4, Y(low + 2)]].forEach(([n, y]) => out.push('<text x="' + pFix(x + 8) + '" """)
# 3. the paper check-up says what a dashed box is
rep("{bkSec('E', 'Write the count under every heart, the rests too.')}", "{bkSec('E', 'Write the count under every heart, the rests too: a dashed box is a rest.')}")
# 4. the medium heart on beat 3 of 4/4 is explained
rep('Then right hand, finger 3 on G: play it, beat 1 a little louder.">', 'Then right hand, finger 3 on G: play it, beat 1 a little louder (the big heart), beat 3 a touch louder too (the middle heart).">')
open(p,'w').write(s); print('ok')
