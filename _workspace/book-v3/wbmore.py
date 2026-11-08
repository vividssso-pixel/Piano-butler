# The Piano Butler Workbook for Handbook Parts III Expression, VII Shape and style and VIII Playing and listening (her 8 Nov: B).
# Two pages per chapter (Learn, Use), then review, progress and answers, as in the other workbooks.
exec(open('/tmp/claude-0/pk/wbpitch.py').read())   # helpers, css, SIZEJS, firstdone (rewrites the Pitch workbooks, harmless)
EVS = json.load(open('/tmp/claude-0/pk/ex/eout.json'))
def sn(k, h=70): return '<figure class="vx px" style="border:0;background:none;box-shadow:none"><div class="vs">' + EVS[k].replace('<svg ', f'<svg style="width:100%;height:auto;max-height:{h}px" ', 1) + '</div></figure>'
_WBH.update({'Loud and soft': 'E1', 'Touch': 'E2', 'Speed words': 'E3', 'The pedals': 'E4',
             'Motifs and phrases': 'F1', 'Repetition and sequence': 'F2', 'Texture': 'F3', 'Changing key': 'F4', 'Form': 'F5', 'Styles through time': 'F6',
             'Fingering': 'L1', 'Practising well': 'L2', 'Listening': 'L4', 'Performing': 'L5'})
def wp3(inner, n, hb, lab):
    right = f'{lab} · HANDBOOK P. ' + PM.resolve('{{' + hb + '}}') if hb else lab
    return f'''<section class="pg"{' data-end="1"' if not hb else ''}><div class="top"><span>THE PIANO BUTLER WORKBOOK</span><span>{right}</span></div><div class="rule"></div><div class="body">{inner}</div>
<div class="sign"><span style="flex:0 0 240px">Date <i></i></span></div><div class="foot"><span>{n}</span></div></section>'''
def mk(part, lab):
    def t(kind, topic, title, rule, inner, n, hb): return wp3(f'<div class="kick">{part} · {topic} · {kind}</div><h1>{title}</h1><p class="rem2"><span>Remember</span><em style="font-style:normal">{rule}</em></p>{inner}', n, hb, lab)
    return t
def opt(t, o): return f'<div class="row"><b>{t}</b><span class="tf">{" &nbsp;·&nbsp; ".join(o)}</span></div>'
def D(x): return f'<b class="done2">{x}</b>'
def T4(rows, w=('34%', '66%'), head=('', '')): return tbl(list(head), rows, list(w), 'bld')
def tick_rows(items, n=4, cols=2): return f'<div class="ts6" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(f'<div><b>{t}</b>{ticks(n)}</div>' for t in items) + '</div>'
def lines(n=3): return '<div class="lines">' + '<span class="al"></span>' * n + '</div>'
def sent(items): return '<div class="sent">' + ''.join(f'<p>{x}</p>' for x in items) + '</div>'
def dsy(t, fs=22): return f'<span style="font-family:PF,serif;font-style:italic;font-weight:700;font-size:{fs}px">{t}</span>'
def explain(n, prompt): return ex(n, 'Explain it', 2, prompt, lines(3))
NOTE = '<p class="sm">“Play it”, “in your music”, listening and playing have no single answer to copy: check them at the piano with your teacher, or with the online lessons.</p>'
def review(part, lab, n, ansp, body): return wp3(f'<div class="kick">{part} · Review</div><h1>Review</h1><p class="rem2"><span>Ten minutes</span>No help, no piano. Mark it with the answers on page {ansp}.</p>{body}<div class="score">Score <span class="ab"></span> / 10</div>', n, None, lab)
def progress(part, lab, n, concepts): return wp3(f'''<div class="kick">{part} · Progress</div><h1>My progress</h1><p class="rem2"><span>How to use</span>Tick each column when it is true. Come back to this page every few weeks.</p>
{tbl(['Concept', 'I know it', 'I can write it', 'I can play it', 'Handbook'], [[c, '<span class="cb2"></span>', '<span class="cb2"></span>', '<span class="cb2"></span>', 'p.\u2009' + PM.resolve('{{' + k + '}}')] for c, k in concepts], ['36%', '15%', '17%', '17%', '15%'], 'prog')}
<div class="note2"><b>Teacher’s note</b><div class="lines"><span class="al"></span><span class="al"></span><span class="al"></span></div></div>''', n, None, lab)
def answers(part, lab, n, ans): return wp3(f'<div class="kick">{part} · Answers</div><h1>Answers</h1>{tbl(["Page", "Answers"], [[p, a] for p, a in ans], ["12%", "88%"], "ansT")}{NOTE}', n, None, lab)

# ======================= Expression =======================
te = mk('Expression', 'EXPRESSION')
EA1 = te('Learn', 'Loud and soft', 'Loud and soft', 'pp p mp mf f ff: from a whisper to a shout. <b>m</b> (mezzo) means half; a second letter means very.', f'''
{ex(1, 'Say it', 1, 'Write the Italian name and what it means. The first row is done.', T4([[dsy('p'), D('piano'), D('soft')]] + [[dsy(s), LINE, LINE] for s in ('mf', 'ff', 'mp', 'pp', 'f')], ('16%', '38%', '46%'), ('Sign', 'Name', 'Means')))}
{ex(2, 'Soft to loud', 1, 'Write these six signs in order, from the softest to the loudest: ' + ' &nbsp; '.join(dsy(s, 18) for s in ('mf', 'pp', 'f', 'p', 'ff', 'mp')) + '. The first is done.', '<div class="anrow">' + f'<span>{D("pp")}</span>' + ''.join(f'<span>{BOX}</span>' for _ in range(5)) + '</div>')}
{ex(3, 'Louder or softer?', 1, 'Does the music get louder or softer from the first sign to the second?', ''.join(opt(a, ('louder', 'softer')) for a in ('mp → mf', 'f → p', 'pp → mp', 'ff → mf', 'p → f')))}
{ex(4, 'Play it', 1, 'Play Middle C six times: pp, p, mp, mf, f, ff. Six different steps? Tick a circle each day.', ticks())}''', 1, 'E1')
EB1 = te('Use', 'Loud and soft', 'Loud and soft', 'A hairpin that opens grows louder (cresc.); one that closes fades (dim.).', f'''
{ex(1, 'Read the hairpins', 2, 'Look at the music and complete each sentence.', sn('e_tw_q', 66) + sent([f'It starts {BOX} (sign).', f'The loudest note is in bar {BOX}, marked {BOX}.', f'It ends {BOX} (sign).']))}
{ex(2, 'Signs and words', 1, 'Write what each one asks you to do. The first is done.', T4([['<i>cresc.</i>', D('getting louder, little by little')], ['<i>dim.</i>', LINE], [dsy('sfz', 18), LINE], [dsy('fp', 18), LINE], ['<i>subito p</i>', LINE]], ('30%', '70%'), ('Sign', 'What you do')))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('mf is louder than mp.', 'A crescendo also gets faster.', 'A dynamic lasts until the next one.', 'sfz makes one note suddenly strong.')))}
{ex(4, 'Play it', 1, 'Play C D E F G growing from p to f, then come down fading to p, without speeding up. Tick a circle each day.', ticks())}''', 2, 'E1+1')
EA2 = te('Learn', 'Touch', 'Touch: smooth, short, strong', 'Curve: join. Dot: short. Line: hold. Arrow: strong.', f'''
{ex(1, 'Name the mark', 1, 'Write the name and how to play it. The first row is done.', T4([['a dot', D('staccato'), D('short, let go early')]] + [[m, LINE, LINE] for m in ('a curve over different notes', 'a line', '&gt; (an arrow)', 'a wedge ▼')], ('30%', '28%', '42%'), ('Mark', 'Name', 'How')))}
{ex(2, 'Which notes are short?', 2, 'Look at the music and complete the sentences.', sn('a_mixq', 70) + sent([f'Bar 1 is played {BOX} (joined or short).', f'In bar 2, {BOX} notes have dots.', f'The last G has an {BOX}.']))}
{ex(3, 'Slur or tie?', 1, 'Circle slur or tie.', ''.join(opt(a, ('slur', 'tie')) for a in ('a curve over C D E', 'a curve joining G and G', 'a curve over E F', 'a curve joining two Bs')))}
{ex(4, 'Play it', 1, 'Hot Cross Buns: play E D C joined, then short and bouncy. Tick a circle each day.', ticks())}''', 3, 'E2')
EB2 = te('Use', 'Touch', 'Touch: smooth, short, strong', 'A two-note slur: drop into the first note, lift off the second.', f'''
{ex(1, 'Mood words', 1, 'Write what each word means. The first is done.', T4([['<i>dolce</i>', D('sweetly')]] + [[f'<i>{w}</i>', LINE] for w in ('cantabile', 'leggiero', 'espressivo', 'maestoso')], ('30%', '70%'), ('Word', 'Meaning')))}
{ex(2, 'Touch for the job', 2, 'Circle the touch that fits best.', ''.join(opt(a, ('legato', 'staccato', 'accent')) for a in ('a lullaby', 'a bouncing ball', 'a march, with strong beats', 'a singing tune')))}
{ex(3, 'Drop and lift', 1, 'Each pair has a two-note slur. Write drop or lift under each note. The first is done.', T4([['E–D', D('drop'), D('lift')], ['G–F', LINE, LINE], ['C–B', LINE, LINE]], ('30%', '35%', '35%'), ('Pair', 'Note 1', 'Note 2')))}
{ex(4, 'True or false?', 1, 'Circle T or F.', tfrows(('Staccato means loud.', 'A tenuto note is held its full length.', 'Lift your hand at the end of a slur.')))}
{ex(5, 'Play it', 1, 'Play one bar of a piece three ways: all legato, all staccato, then as written. Tick a circle each day.', ticks())}''', 4, 'E2+1')
EA3 = te('Learn', 'Speed words', 'Speed words', 'Largo, Adagio, Andante, Moderato, Allegro, Presto: slow to fast. ♩ = 60 is one beat a second.', f'''
{ex(1, 'Slow to fast', 1, 'Write these words in order, from the slowest to the fastest: Allegro, Largo, Andante, Presto, Adagio, Moderato. The first is done.', '<div class="anrow">' + f'<span>{D("Largo")}</span>' + ''.join(f'<span>{WL}</span>' for _ in range(5)) + '</div>')}
{ex(2, 'What does it mean?', 1, 'Write the meaning. The first is done.', T4([['<b>Andante</b>', D('at a walking pace')]] + [[f'<b>{w}</b>', LINE] for w in ('Allegro', 'Adagio', 'Presto', 'Moderato', 'Lento')], ('30%', '70%'), ('Word', 'Meaning')))}
{ex(3, 'Metronome maths', 2, 'Complete each sentence.', sent([f'At ♩ = 60 there is one beat every {BOX} second(s).', f'At ♩ = 120 there are {BOX} beats every second.', f'At ♩ = 30 there is one beat every {BOX} seconds.']))}
{ex(4, 'Play it', 1, 'Walk at Andante saying 1 2 3 4, then jog at Allegro. Then clap both. Tick a circle each day.', ticks())}''', 5, 'E3')
EB3 = te('Use', 'Speed words', 'Speed words', 'rit. and rall.: gradually slower. accel.: gradually faster. a tempo: back to the first speed.', f'''
{ex(1, 'Changing speed', 1, 'Write what each one asks. The first is done.', T4([['<i>rit.</i>', D('gradually slower')]] + [[f'<i>{w}</i>', LINE] for w in ('accel.', 'a tempo', 'rall.', 'poco a poco', 'più mosso')] + [['fermata (pause)', LINE]], ('34%', '66%'), ('Word or sign', 'What you do')))}
{ex(2, 'Read the map', 2, 'Look at the music and complete the sentences.', sn('t_atempo', 66) + sent([f'The music slows down in bar {BOX}.', f'The first speed comes back in bar {BOX}, at the words {LINE.replace("al", "al inl")}.']))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('Andante is very slow.', 'A fermata means hold the note longer.', 'meno mosso means faster.')))}
{ex(4, 'Play it', 1, 'Play C D E F G and slow down into the G (rit.), then play it again a tempo. Tick a circle each day.', ticks())}''', 6, 'E3+1')
EA4 = te('Learn', 'The pedals', 'The pedals', 'Ped.: right pedal down. ✻: up. Play first, then pedal.', f'''
{ex(1, 'Which pedal?', 1, 'Write which pedal and what your foot does. The first row is done.', T4([['<b>Ped.</b>', D('right'), D('down')]] + [[f'<b>{s}</b>', LINE, LINE] for s in ('✻', 'u.c.', 't.c.')], ('24%', '38%', '38%'), ('Sign', 'Pedal', 'Foot')))}
{ex(2, 'Read the pedal', 2, 'Look at the music and complete the sentences.', sn('p_pedq', 70) + sent([f'The pedal goes down on the first {BOX}.', f'It changes on the first note of bar {BOX}.', f'It comes up in bar {BOX}.']))}
{ex(3, 'Play first, then pedal', 2, 'Number the steps of a pedal change in order. The first is done.', T4([['play the new notes', D('1')], ['press the pedal down again', BOX], ['lift the pedal', BOX]], ('70%', '30%'), ('Step', 'Order')))}
{ex(4, 'Play it', 1, 'Play C E G together, press the pedal, take your hands off and listen. Lift the pedal. Tick a circle each day.', ticks())}''', 7, 'E4')
EB4 = te('Use', 'The pedals', 'The pedals', 'A new chord, a new pedal: play it, then change straight away.', f'''
{ex(1, 'Clean or muddy?', 2, 'Circle what you will hear.', ''.join(opt(a, ('clean', 'muddy', 'a gap')) for a in ('a change after every new chord', 'the pedal held from C-E-G into F-A-C', 'the pedal lifted before the new notes', 'a change just after the new notes')))}
{ex(2, 'Where do you change?', 2, 'Each bar has one group of notes. Write down, change or none for each bar. The first is done.', T4([['bar 1: C E G', D('down')], ['bar 2: C E G again', BOX], ['bar 3: F A C', BOX], ['bar 4: G B D', BOX], ['bar 5: G B D again', BOX]], ('60%', '40%'), ('Bar', 'Pedal')))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('Keep your heel on the floor.', 'u.c. is the right pedal.', 'Change the pedal at the same moment as the new chord.')))}
{ex(4, 'Play it', 1, 'Play C-E-G, F-A-C, G-B-D, C-E-G slowly with a change on each. Tick a circle each clean day.', ticks())}''', 8, 'E4+1')
EA5 = te('Learn', 'Ornaments', 'Ornaments', 'An ornament borrows the next-door notes: one letter up or one letter down.', f'''
{ex(1, 'Name the ornament', 1, 'Write the name of each one. The first is done.', T4([['tr', D('trill')]] + [[d, LINE] for d in ('a zigzag', 'a zigzag with a line through it', 'a lying-down S (~)', 'a tiny note with a slash', 'a tiny note without a slash')], ('48%', '52%'), ('Sign', 'Name')))}
{ex(2, 'Next-door notes', 1, 'Write the letter above and the letter below. The first row is done.', T4([['<b>D</b>', D('E'), D('C')]] + [[f'<b>{n}</b>', BOX, BOX] for n in ('G', 'A', 'F', 'B')], ('30%', '35%', '35%'), ('Main note', 'Above', 'Below')))}
{ex(3, 'Spell it out', 2, 'Write the notes you play. The first is done.', T4([['upper mordent on G', D('G A G')], ['lower mordent on A', LINE], ['turn on D', LINE], ['trill on E (four notes)', LINE]], ('50%', '50%'), ('Ornament', 'Notes')))}
{ex(4, 'Play it', 1, 'Play D and E with fingers 2 and 3, slowly, eight times, then a little faster. Tick a circle each day.', ticks())}''', 9, 'E5')
EB5 = te('Use', 'Ornaments', 'Ornaments', 'Slash: crushed in (acciaccatura). No slash: leans, taking half the time (appoggiatura).', f'''
{ex(1, 'Crushed or leaning?', 2, 'Circle the name.', ''.join(opt(a, ('acciaccatura', 'appoggiatura')) for a in ('a tiny note with a slash', 'a tiny note without a slash', 'played as fast as possible', 'takes half the main note’s time')))}
{ex(2, 'Above or below?', 1, 'Which next-door note does each use? Circle one.', ''.join(opt(a, ('above', 'below', 'both')) for a in ('trill', 'upper mordent', 'lower mordent', 'turn')))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('An ornament starts on the beat.', 'A trill uses the note below.', 'The main note still lands on time.')))}
{ex(4, 'Play it', 1, 'Play C D E F G with an upper mordent on each note, slowly. Tick a circle each day.', ticks())}
{explain(5, 'In your own words: how do you play an upper mordent on D, and where does it start?')}''', 10, 'E5+1')
ER = review('Expression', 'EXPRESSION', 11, 13, f'''
{ex(1, 'Name them', 1, 'Write what each one means.', T4([[dsy('mp'), LINE], ['<i>rit.</i>', LINE], ['<b>Ped.</b>', LINE], ['a dot over a note', LINE]], ('40%', '60%')))}
{ex(2, 'Complete it', 2, 'One word in each space.', sent([f'Andante means at a {BOX} pace.', f'A curve over different notes is a {BOX}.', f'A trill goes back and forth with the note {BOX}.']))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('ff is softer than f.', 'a tempo means back to the first speed.', 'Change the pedal before you play the new chord.')))}''')
EP = progress('Expression', 'EXPRESSION', 12, [('dynamics: pp to ff', 'E1'), ('crescendo and diminuendo', 'E1'), ('slurs, staccato, tenuto, accents', 'E2'), ('mood words', 'E2'), ('tempo words and the metronome', 'E3'), ('rit., accel., a tempo, fermata', 'E3'), ('the sustain pedal', 'E4'), ('ornaments', 'E5')])
EAN = answers('Expression', 'EXPRESSION', 13, [
    ('p. 1', 'Say it: mf mezzo-forte half loud · ff fortissimo very loud · mp mezzo-piano half soft · pp pianissimo very soft · f forte loud. Order: pp p mp mf f ff. Louder/softer: louder, softer, louder, softer, louder.'),
    ('p. 2', 'Hairpins: mp; bar 2, f; p. Signs: dim. getting softer · sfz one note suddenly strong · fp loud, then soft at once · subito p suddenly soft. T/F: T, F, T, T.'),
    ('p. 3', 'Marks: slur, join smoothly · tenuto, hold full length · accent, a stronger start · staccatissimo, very short. Short notes: joined; two; accent. Slur or tie: slur, tie, slur, tie.'),
    ('p. 4', 'Mood words: in a singing style · lightly · with feeling · majestically. Touch: legato, staccato, accent, legato. Drop and lift: drop, lift (every pair). T/F: F, T, T.'),
    ('p. 5', 'Order: Largo, Adagio, Andante, Moderato, Allegro, Presto. Meanings: fast and lively · slow, at ease · very fast · moderate · slow. Metronome: 1; 2; 2.'),
    ('p. 6', 'Changing speed: gradually faster · back to the speed before · gradually slower · little by little · more movement, faster · hold longer than written. Map: bar 1; bar 3, a tempo. T/F: F, T, F.'),
    ('p. 7', 'Pedals: right, up · left, down · left, up. Read the pedal: C; bar 2; bar 3. Order: play 1, lift 2, press down again 3.'),
    ('p. 8', 'Clean or muddy: clean, muddy, a gap, clean. Where: none, change, change, none. T/F: T, F, F.'),
    ('p. 9', 'Names: upper mordent, lower mordent, turn, acciaccatura, appoggiatura. Next door: G A F · A B G · F G E · B C A. Spell: A G A · E D C D · E F E F.'),
    ('p. 10', 'Crushed or leaning: acciaccatura, appoggiatura, acciaccatura, appoggiatura. Above or below: above, above, below, both. T/F: T, F, T.'),
    ('p. 11', 'half soft · gradually slower · right pedal down · short (staccato). walking; slur; above. F, T, F.')])
EFIRST = {'Louder or softer?': [('ring', 'louder')], 'Slur or tie?': [('ring', 'slur')], 'Touch for the job': [('ring', 'legato')], 'Clean or muddy?': [('ring', 'clean')],
          'Crushed or leaning?': [('ring', 'acciaccatura')], 'Above or below?': [('ring', 'above')], 'Read the hairpins': [('fill', 'mp')], 'Which notes are short?': [('fill', 'joined')],
          'Read the map': [('fill', '1')], 'Read the pedal': [('fill', 'C')], 'Metronome maths': [('fill', '1')]}

# ======================= Shape and style =======================
tf_ = mk('Shape and style', 'SHAPE AND STYLE')
FA1 = tf_('Learn', 'Motifs and phrases', 'Motifs and phrases', 'Most phrases are 4 bars. A question ends away from the home note; an answer comes home.', f'''
{ex(1, 'Question or answer?', 1, 'Each phrase is in C major. Circle question or answer from its last note.', ''.join(opt(f'ends on {n}', ('question', 'answer')) for n in ('D', 'C', 'G', 'B', 'C')))}
{ex(2, 'Count the phrases', 1, 'Each phrase is 4 bars long. Write how many phrases. The first is done.', T4([['8 bars', D('2')], ['12 bars', BOX], ['16 bars', BOX]], ('50%', '50%'), ('Tune', 'Phrases')))}
{ex(3, 'Find the motif', 2, 'Look at the music and complete the sentences.', sn('f_motq', 66) + sent([f'The motif has {BOX} notes.', f'It comes {BOX} times.', f'Each time it starts one {BOX} higher.']))}
{ex(4, 'Play it', 1, 'Sing Ode to Joy bars 1–4 and stop on the D (a question). Then sing the answer and land on C. Tick a circle each day.', ticks())}''', 1, 'F1')
FB1 = tf_('Use', 'Motifs and phrases', 'Motifs and phrases', 'A motif is short and comes back: listen for its rhythm and its shape.', f'''
{ex(1, 'Make a motif', 2, 'Move each motif up one step, then one step more. The first row is done.', T4([['C D E', D('D E F'), D('E F G')], ['C E D', LINE, LINE], ['G G E', LINE, LINE], ['E C D', LINE, LINE]], ('34%', '33%', '33%'), ('Motif', 'One step up', 'Two steps up')))}
{ex(2, 'Write an answer', 3, 'The question is C D E F | G. Write an answer of five notes that comes home to C.', '<div class="anrow">' + ''.join(f'<span>{BOX}</span>' for _ in range(4)) + f'<span>{D("C")}</span></div>')}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('A motif is usually 2 to 6 notes.', 'A question phrase ends on the home note.', 'Most phrases are 4 bars long.')))}
{ex(4, 'In your music', 2, 'In a piece you play, pencil a curve over each phrase. How many phrases are there, and how long is each?', sent([f'Phrases {BOX} &nbsp; Bars in each {BOX}']))}
{ex(5, 'Play it', 1, 'Play a piece and grow towards the high point of each phrase. Tick a circle each day.', ticks())}''', 2, 'F1+1')
FA2 = tf_('Learn', 'Repetition and sequence', 'Repetition and sequence', 'Repetition: the same notes again. Sequence: the same shape, higher or lower.', f'''
{ex(1, 'Repetition or sequence?', 1, 'Circle the right word.', ''.join(opt(a, ('repetition', 'sequence')) for a in ('C D E · C D E', 'C D E · D E F', 'G F E · F E D', 'A B C · A B C', 'E G · F A')))}
{ex(2, 'Continue the sequence', 2, 'Write the next group: the same shape, one step on. The first is done.', T4([['C D E · D E F', D('E F G')], ['C E D · D F E', LINE], ['G E · F D', LINE], ['C D C · D E D', LINE]], ('55%', '45%'), ('Pattern', 'Next')))}
{ex(3, 'Name it', 1, 'Circle the right word.', ''.join(opt(a, ('repetition', 'sequence', 'imitation', 'contrast')) for a in ('the left hand copies the right', 'a new rhythm', 'the same notes again')))}
{ex(4, 'Play it', 1, 'Play C D E, D E F, E F G, then come down: G F E, F E D, E D C. Tick a circle each day.', ticks())}''', 3, 'F2')
FB2 = tf_('Use', 'Repetition and sequence', 'Repetition and sequence', 'Imitation: another hand or voice copies the idea. Contrast: something new.', f'''
{ex(1, 'Map Frère Jacques', 2, 'Look at the music. Write how each bar relates to the one before. The first is done.', sn('f_frere', 80) + T4([['bar 2', D('repetition')], ['bar 3', LINE], ['bar 4', LINE]], ('40%', '60%'), ('Bar', 'Compared with the bar before')))}
{ex(2, 'A falling sequence', 2, 'Move each shape down one step, then one step more. The first is done.', T4([['G F E', D('F E D'), LINE], ['C B A', LINE, LINE], ['A G F', LINE, LINE]], ('34%', '33%', '33%'), ('Start', 'Next', 'Next')))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('A sequence moves to new notes.', 'Imitation needs two hands or voices.', 'Contrast means the same idea again.')))}
{ex(4, 'Play it', 1, 'Sing Frère Jacques as a round with a friend: they start when you reach bar 3. Tick a circle each day.', ticks())}''', 4, 'F2+1')
FA3 = tf_('Learn', 'Texture', 'Texture', 'Count the lines: one alone, a tune with chords, or tunes woven together.', f'''
{ex(1, 'Name the texture', 1, 'Circle the word.', ''.join(opt(a, ('monophonic', 'homophonic', 'polyphonic')) for a in ('one tune alone', 'a tune with block chords', 'two tunes at once', 'a tune over C G E G')))}
{ex(2, 'Block or broken?', 1, 'Write the notes of each chord, struck together (block) or one at a time, low–high–middle–high (Alberti). The first row is done.', T4([['<b>C</b>', D('C E G'), D('C G E G')], ['<b>F</b>', LINE, LINE], ['<b>G</b>', LINE, LINE]], ('20%', '40%', '40%'), ('Chord', 'Block', 'Alberti')))}
{ex(3, 'Which hand sings?', 2, 'Look at the music and complete the sentences.', sn('f_lh', 130) + sent([f'The tune is in the {BOX} hand.', f'The other hand plays {BOX} (chords or a tune).']))}
{ex(4, 'Play it', 1, 'Play Twinkle with the right hand and a C chord in the left, tune louder, chord softer. Tick a circle each day.', ticks())}''', 5, 'F3')
FB3 = tf_('Use', 'Texture', 'Texture', 'Melody and accompaniment: the tune sings, the accompaniment stays softer.', f'''
{ex(1, 'Three textures', 2, 'Play Mary Had a Little Lamb three ways and tick each one you can do.', tick_rows(('tune alone', 'tune and block chords', 'tune and Alberti bass'), 4, 1))}
{ex(2, 'True or false?', 1, 'Circle T or F.', tfrows(('Polyphonic music has two or more tunes at once.', 'An Alberti bass is one long note.', 'In melody and accompaniment, the tune is louder.')))}
{ex(3, 'In your music', 2, 'Choose two pieces you play. Name the texture of each and the hand that has the tune.', T4([[LINE, LINE, LINE], [LINE, LINE, LINE]], ('40%', '30%', '30%'), ('Piece', 'Texture', 'Tune in')))}
{ex(4, 'Listen', 1, 'Listen to a piece by Bach and one by Mozart. Which has two tunes woven together?', sent([f'Two tunes: {LINE.replace("al", "al inl")}']))}
{ex(5, 'Play it', 1, 'Play a piece you know with the tune louder than the accompaniment. Ask someone if they can hear the tune clearly. Tick a circle each day.', ticks())}''', 6, 'F3+1')
FA4 = tf_('Learn', 'Changing key', 'Changing key', 'A new sharp or flat that keeps coming back, then a cadence: a new key.', f'''
{ex(1, 'Which new key?', 2, 'Write the major key the music has moved to. The first is done.', T4([['C major', 'F♯ keeps appearing', D('G major')], ['C major', 'B♭ keeps appearing', LINE], ['G major', 'C♯ keeps appearing', LINE], ['F major', 'E♭ keeps appearing', LINE]], ('26%', '38%', '36%'), ('From', 'Signpost', 'New key')))}
{ex(2, 'Passing or new?', 2, 'Circle the right word.', ''.join(opt(a, ('passing', 'new key')) for a in ('one F♯, then F♮ again', 'F♯ in every bar, ending on G', 'one C♯ in a quick run', 'B♭ again and again, ending on F')))}
{ex(3, 'The nearest keys', 1, 'Write the key with one more sharp and the key with one more flat. The first row is done.', T4([['<b>C major</b>', D('G major'), D('F major')]] + [[f'<b>{k}</b>', LINE, LINE] for k in ('G major', 'F major', 'D major')], ('30%', '35%', '35%'), ('Key', 'One more sharp (or one less flat)', 'One more flat (or one less sharp)')))}
{ex(4, 'Play it', 1, 'Play the four bars on Handbook p.\u2009' + PM.resolve('{{F4}}') + ' twice: once with F♮, once with F♯. Hear the new home. Tick a circle each day.', ticks())}''', 7, 'F4')
FB4 = tf_('Use', 'Changing key', 'Changing key', 'Relative keys share a key signature: C major and A minor.', f'''
{ex(1, 'Relative keys', 1, 'Write the relative minor. The first is done.', T4([['C major', D('A minor')], ['G major', LINE], ['F major', LINE], ['D major', LINE]], ('50%', '50%'), ('Major', 'Relative minor')))}
{ex(2, 'True or false?', 1, 'Circle T or F.', tfrows(('One sharp in one bar always means a new key.', 'Most pieces end in the key they began in.', 'G major is one more sharp than C major.')))}
{ex(3, 'In your music', 3, 'Find a piece that changes key. Write the bar, the new note and the new key.', sent([f'Bar {BOX} &nbsp; new note {BOX} &nbsp; new key {LINE.replace("al", "al inl")}']))}
{ex(4, 'Play it', 1, 'Play the C major scale, then the G major scale: listen for the F♯. Tick a circle each day.', ticks())}
{explain(5, 'Explain how you can tell a real change of key from one passing sharp or flat.')}''', 8, 'F4+1')
FA5 = tf_('Learn', 'Form', 'Form', 'Same music, same letter. New music, the next letter.', f'''
{ex(1, 'Name the form', 1, 'Write the name of each form. The first is done.', T4([['A B', D('binary')], ['A B A', LINE], ['A B A C A', LINE], ['A A¹ A² A³', LINE], ['A A A (every verse)', LINE]], ('45%', '55%'), ('Letters', 'Form')))}
{ex(2, 'Letter the phrases', 2, 'Write a letter for each phrase. The first is done.', T4([['phrase 1: the first tune', D('A')], ['phrase 2: a new tune', BOX], ['phrase 3: the first tune again', BOX], ['phrase 4: another new tune', BOX], ['phrase 5: the first tune again', BOX]], ('70%', '30%'), ('Phrase', 'Letter')))}
{ex(3, 'Finish the map', 2, 'Write the missing letter.', T4([['rondo: A B A ? A', BOX], ['ternary: A B ?', BOX]], ('70%', '30%')))}''', 9, 'F5')
FB5 = tf_('Use', 'Form', 'Form', 'Binary AB · ternary ABA · rondo ABACA · variations A A¹ A².', f'''
{ex(1, 'Which form fits?', 2, 'Circle the form.', '<div class="opt5">' + ''.join(opt(a, ('binary', 'ternary', 'rondo', 'variations', 'strophic')) for a in ('a minuet in two halves', 'Für Elise', 'Twinkle, dressed 12 ways', 'a hymn, 4 verses')) + '</div>')}
{ex(2, 'Map a piece you play', 3, 'Write the bars of each section and its letter.', T4([[LINE, BOX], [LINE, BOX], [LINE, BOX], [LINE, BOX]], ('70%', '30%'), ('Bars', 'Letter')) + f'<p class="how">Its form: {LINE.replace("al", "al inl")}</p>')}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('A played twice is still A.', 'In a rondo, A comes back again and again.', 'Ternary has only two sections.')))}
{ex(4, 'Listen', 1, 'Listen to Für Elise and raise a hand each time you hear A. How many times do you hear A altogether, counting the start?', sent([f'I hear A {BOX} times.']))}''', 10, 'F5+1')
FA6 = tf_('Learn', 'Styles through time', 'Styles through time', 'Baroque 1600–1750 · Classical 1750–1820 · Romantic 1820–1900 · Modern 1900 to today.', f'''
{ex(1, 'Which period?', 1, 'Write the period. The first is done.', T4([['Bach', D('Baroque')]] + [[c, LINE] for c in ('Mozart', 'Chopin', 'Debussy', 'Handel', 'Haydn', 'Liszt')], ('45%', '55%'), ('Composer', 'Period')))}
{ex(2, 'Clues', 2, 'Circle the period each clue points to.', ''.join(opt(a, ('Baroque', 'Classical', 'Romantic', 'Modern')) for a in ('harpsichord, many trills', 'Alberti bass, tidy phrases', 'rubato, rich pedal', 'jazz rhythms, new scales')))}
{ex(3, 'Dates', 1, 'Write the years. The first is done.', T4([['Baroque', D('1600–1750')], ['Classical', LINE], ['Romantic', LINE], ['Modern', LINE]], ('50%', '50%'), ('Period', 'Years')))}''', 11, 'F6')
FB6 = tf_('Use', 'Styles through time', 'Styles through time', 'Play in style: the pedal, the time and the touch change with the period.', f'''
{ex(1, 'Playing in style', 2, 'Circle the pedal for each period.', ''.join(opt(a, ('little or none', 'light', 'rich')) for a in ('Baroque', 'Classical', 'Romantic')))}
{ex(2, 'True or false?', 1, 'Circle T or F.', tfrows(('Mozart wrote for the harpsichord only.', 'Romantic music often uses rubato.', 'Bach needs a lot of pedal.')))}
{ex(3, 'Your pieces', 2, 'Write three or four pieces you play, their composers and their periods.', T4([[LINE, LINE, LINE]] * 4, ('40%', '30%', '30%'), ('Piece', 'Composer', 'Period')))}
{ex(4, 'Listen', 1, 'Listen to one piece from each period. Tick each one.', tick_rows(('Baroque', 'Classical', 'Romantic', 'Modern'), 1, 2))}''', 12, 'F6+1')
FR = review('Shape and style', 'SHAPE AND STYLE', 13, 15, f'''
{ex(1, 'Name it', 1, 'Write the word.', T4([['the same shape, one step higher', LINE], ['a tune with chords underneath', LINE], ['A B A', LINE], ['Mozart’s period', LINE]], ('60%', '40%')))}
{ex(2, 'Complete it', 2, 'One word in each space.', sent([f'A phrase is usually {BOX} bars long.', f'An answer phrase ends on the {BOX} note.', f'From C major, an F♯ that keeps coming back leads to {BOX} major.']))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('Für Elise is a rondo.', 'Bach is a Romantic composer.', 'Polyphonic music has only one line.')))}''')
FP = progress('Shape and style', 'SHAPE AND STYLE', 14, [('motifs', 'F1'), ('phrases: question and answer', 'F1'), ('repetition, sequence, imitation', 'F2'), ('texture', 'F3'), ('changing key', 'F4'), ('form', 'F5'), ('the four periods', 'F6')])
FAN = answers('Shape and style', 'SHAPE AND STYLE', 15, [
    ('p. 1', 'Question or answer: question, answer, question, question, answer. Phrases: 3, 4. Motif: 3 notes; 3 times; step.'),
    ('p. 2', 'Motif: D F E, E G F · A A F, B B G · F D E, G E F. Answer: any five notes ending on C, for example G F E D C. T/F: T, F, T.'),
    ('p. 3', 'Repetition, sequence, sequence, repetition, sequence. Next: E G F · E C · E F E. Name it: imitation, contrast, repetition.'),
    ('p. 4', 'Frère Jacques: bar 3 contrast (new notes), bar 4 repetition. Falling: row 1 E D C · row 2 B A G, A G F · row 3 G F E, F E D. T/F: T, T, F.'),
    ('p. 5', 'Texture: monophonic, homophonic, polyphonic, homophonic. Block/Alberti: F A C, F C A C · G B D, G D B D. Which hand: left; chords.'),
    ('p. 6', 'T/F: T, F, T. Listen: usually the Bach piece (two tunes woven together).'),
    ('p. 7', 'New key: F major, D major, B♭ major. Passing or new: passing, new key, passing, new key. Nearest: G: D / C · F: C / B♭ · D: A / G.'),
    ('p. 8', 'Relative minors: E minor, D minor, B minor. T/F: F, T, T.'),
    ('p. 9', 'Forms: ternary, rondo, theme and variations, strophic. Letters: B, A, C, A. Missing: C; A.'),
    ('p. 10', 'Which form: binary, rondo, variations, strophic. T/F: T, T, F. Für Elise: 3 times.'),
    ('p. 11', 'Periods: Classical, Romantic, Modern, Baroque, Classical, Romantic. Clues: Baroque, Classical, Romantic, Modern. Dates: 1750–1820, 1820–1900, 1900 to today.'),
    ('p. 12', 'Pedal: little or none, light, rich. T/F: F, T, F.'),
    ('p. 13', 'sequence · homophonic (melody and accompaniment) · ternary · Classical. 4; home; G. T, F, F.')])
FFIRST = {'Question or answer?': [('ring', 'question')], 'Repetition or sequence?': [('ring', 'repetition')], 'Name it': [('ring', 'imitation')], 'Name the texture': [('ring', 'monophonic')],
          'Passing or new?': [('ring', 'passing')], 'Which form fits?': [('ring', 'binary')], 'Clues': [('ring', 'Baroque')], 'Playing in style': [('ring', 'little or none')],
          'Find the motif': [('fill', '3')], 'Which hand sings?': [('fill', 'left')]}

# ======================= Playing and listening =======================
tl = mk('Playing and listening', 'PLAYING AND LISTENING')
LA1 = tl('Learn', 'Fingering', 'Fingering', 'Thumbs are 1 in both hands, little fingers 5.', f'''
{ex(1, 'Finger numbers', 1, 'Write the number. The first is done.', T4([['thumb', D('1')], ['index finger', BOX], ['middle finger', BOX], ['ring finger', BOX], ['little finger', BOX]], ('60%', '40%'), ('Finger', 'Number')))}
{ex(2, 'Five-finger position', 1, 'Right-hand thumb on C, left-hand little finger on C: write the finger for each note. The first is done.', T4([['<b>right hand</b>', D('1'), BOX, BOX, BOX, BOX], ['<b>left hand</b>', BOX, BOX, BOX, BOX, BOX]], ('28%', '14.4%', '14.4%', '14.4%', '14.4%', '14.4%'), ('', 'C', 'D', 'E', 'F', 'G')))}
{ex(3, 'C major, right hand', 2, 'Write the fingering going up. The first three are done.', T4([['<b>finger</b>', D('1'), D('2'), D('3'), BOX, BOX, BOX, BOX, BOX]], ('16%',) + ('10.5%',) * 8, ('', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C')))}
{ex(4, 'Play it', 1, 'Play C D E F G up and down with each hand, saying the finger numbers. Tick a circle each day.', ticks())}''', 1, 'L1')
LB1 = tl('Use', 'Fingering', 'Fingering', 'Going up the right hand, the thumb passes under; coming down, finger 3 crosses over.', f'''
{ex(1, 'Under or over?', 2, 'Circle what happens.', ''.join(opt(a, ('thumb under', 'finger over')) for a in ('right hand going up, after finger 3', 'right hand coming down, after the thumb', 'left hand going up, after the thumb', 'left hand coming down, after finger 3')))}
{ex(2, 'C major, left hand', 2, 'Write the fingering going up. The first is done.', T4([['<b>finger</b>', D('5'), BOX, BOX, BOX, BOX, BOX, BOX, BOX]], ('16%',) + ('10.5%',) * 8, ('', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C')))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('The thumb is 1 only in the right hand.', 'Write your fingering in once and keep it.', 'The thumb should land heavily as it passes under.')))}
{ex(4, 'Play it', 1, 'Play the C major scale, one octave, each hand alone. Tick a circle each clean day.', ticks())}
{explain(5, 'Explain why it helps to write your fingering in and keep it.')}''', 2, 'L1+1')
LA2 = tl('Learn', 'Practising well', 'Practising well', 'Slow, small and correct; three correct times, then one notch faster.', f'''
{ex(1, 'The metronome ladder', 1, 'The Handbook’s ladder (p.\u2009' + PM.resolve('{{L2}}') + ') goes 60 66 72 80 88 96. Write the two missing steps. The first is done.', '<div class="anrow">' + ''.join(f'<span>{x}</span>' for x in ('60', '66', '72', D('80'), BOX)) + '</div>')}
{ex(2, 'Good habit?', 1, 'Circle helps or wastes time.', ''.join(opt(a, ('helps', 'wastes time')) for a in ('the hardest bar first', 'always from the top', 'faster to fix a slip', 'three correct, then faster', 'hands separately first')))}
{ex(3, 'My fifteen minutes', 2, 'Plan your practice: what will you do in each part?', T4([['2 min · warm up', LINE], ['5 min · hardest bars', LINE], ['5 min · join them', LINE], ['3 min · play it through', LINE]], ('40%', '60%'), ('Time', 'What')))}
{ex(4, 'True or false?', 1, 'Circle T or F.', tfrows(('Small chunks are easier to fix.', 'Practise only what you can already play.', 'Hands separately first, then together.')))}
{ex(5, 'Play it', 1, 'Choose one hard bar and climb the metronome ladder. Tick a circle each day.', ticks())}''', 3, 'L2')
LB2 = tl('Use', 'Practising well', 'Practising well', 'Write it down: what got better, and what to start with tomorrow.', f'''
{ex(1, 'Practice log', 2, 'Fill in a line after each practice.', T4([[LINE, LINE, LINE] for _ in range(5)], ('20%', '40%', '40%'), ('Day', 'Got better', 'Start with tomorrow')))}
{ex(2, 'True or false?', 1, 'Circle T or F.', tfrows(('Playing fast and wrong teaches the wrong notes.', 'One long practice beats several short ones.', 'Count aloud to keep the rhythm honest.')))}
{ex(3, 'Chunk it', 2, 'Choose a piece. Write the bars you will practise first, the hardest first.', sent([f'Bars {BOX} to {BOX}, then {BOX} to {BOX}']))}
{ex(4, 'Play it', 1, 'Practise for fifteen minutes with your plan from page 3. Tick a circle each day.', ticks())}
{explain(5, 'Explain why slow and correct is faster than fast and wrong.')}''', 4, 'L2+1')
LA3 = tl('Learn', 'Sight-reading', 'Sight-reading', 'Thirty seconds of looking, then keep the beat going whatever happens.', f'''
{ex(1, 'Scan this', 2, 'Look at the music for thirty seconds and complete the sentences.', sn('l_sr', 68) + sent([f'Key: {BOX} major. &nbsp; Time: {BOX} beats in a bar.', f'First note: {BOX}. &nbsp; Bar 2 is bar 1 one step {BOX}.']))}
{ex(2, 'Scan order', 1, 'Number the checks in the order of the scan. The first is done.', T4([['key', D('1')], ['time', BOX], ['first notes', BOX], ['rhythm', BOX], ['patterns', BOX], ['marks', BOX]], ('70%', '30%'), ('Check', 'Order')))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('Stop and fix every wrong note.', 'Choose a speed you can keep.', 'Read shapes, not single notes.')))}''', 5, 'L3')
LB3 = tl('Use', 'Sight-reading', 'Sight-reading', 'Look one bar ahead while you play.', f'''
{ex(1, 'Scan this too', 2, 'Look at the music and complete the sentences.', sn('l_sr2', 68) + sent([f'Key: {BOX} major. &nbsp; Time: {BOX} beats in a bar.', f'The F in bar 2 is played as {BOX}.']))}
{ex(2, 'Sight-reading log', 2, 'One new piece each day: scan, play once without stopping, then tick.', T4([[LINE, '<span class="cb2"></span>', '<span class="cb2"></span>'] for _ in range(5)], ('50%', '25%', '25%'), ('Piece', 'Scanned', 'No stops')))}
{ex(3, 'Read ahead', 1, 'Cover each bar with a card as you play it. Tick a circle each day.', ticks())}
{ex(4, 'True or false?', 1, 'Circle T or F.', tfrows(('A stop is heard more than a wrong note.', 'Look down at your hands while sight-reading.', 'Tap the trickiest rhythm before you start.')))}''', 6, 'L3+1')
LA4 = tl('Learn', 'Listening', 'Listening', 'Major sounds bright, minor darker: only the middle note of the chord moves.', f'''
{ex(1, 'Intervals by song', 1, 'Write a song that has each interval near its start. The first is done.', T4([['perfect 5th', D('Twinkle (2nd to 3rd note)')], ['major 2nd', LINE], ['major 3rd', LINE], ['perfect 4th', LINE], ['octave', LINE]], ('34%', '66%'), ('Interval', 'Song')))}
{ex(2, 'Finished or not?', 2, 'In C major: does the ending sound finished?', ''.join(opt(a, ('finished', 'not finished')) for a in ('G → C', 'C → G', 'F → C', 'Dm → G')))}
{ex(3, 'Bright or dark?', 1, 'Play each chord and circle what you hear.', ''.join(opt(a, ('bright', 'dark')) for a in ('C E G', 'C E♭ G', 'A C E', 'G B D')))}
{ex(4, 'Play it', 1, 'Play C E G and C E♭ G one after the other, then sing the middle note of each. Tick a circle each day.', ticks())}''', 7, 'L4')
LB4 = tl('Use', 'Listening', 'Listening', 'If you can sing it back, you can play it.', f'''
{ex(1, 'Clap it back', 1, 'A friend claps two bars; you clap them back. Tick each one you get right first time.', tick_rows(('rhythm 1', 'rhythm 2', 'rhythm 3', 'rhythm 4'), 1, 2))}
{ex(2, 'How many beats?', 2, 'Listen to four pieces. Clap along and write the beats in a bar.', T4([[LINE, BOX] for _ in range(4)], ('70%', '30%'), ('Piece', 'Beats')))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('Major and minor chords differ by the middle note.', 'A perfect cadence sounds unfinished.', 'Close your eyes to listen better.')))}
{ex(4, 'Sing it back', 1, 'A friend plays five notes; you sing them, then find them on the keys. Tick a circle each day.', ticks())}
{explain(5, 'Explain how you can hear whether a chord is major or minor.')}''', 8, 'L4+1')
LA5 = tl('Learn', 'Performing', 'Performing', 'Breathe, feel a bar of the beat, then begin. After a slip, catch the next beat.', f'''
{ex(1, 'The routine', 1, 'Number the steps in order. The first is done.', T4([['adjust the bench', D('1')], ['breathe out slowly', BOX], ['feel one bar of the beat', BOX], ['play the first note', BOX], ['stand and bow', BOX]], ('70%', '30%'), ('Step', 'Order')))}
{ex(2, 'After a slip', 2, 'Circle helps or does not help.', ''.join(opt(a, ('helps', 'does not help')) for a in ('keep the beat going', 'go back and fix it', 'rejoin at the next phrase', 'stop and say sorry')))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('Nerves mean you care.', 'Practise starting from three places.', 'The audience wants you to fail.')))}
{ex(4, 'Play it', 1, 'A one-minute concert: walk to the piano, sit, breathe, feel a bar, play eight bars, bow. Tick a circle each day.', ticks())}''', 9, 'L5')
LB5 = tl('Use', 'Performing', 'Performing', 'Play it once a day without stopping, as if someone were listening.', f'''
{ex(1, 'My concert plan', 2, 'Write your piece and three places you can start from.', T4([['piece', LINE], ['start 1 (bar)', BOX], ['start 2 (bar)', BOX], ['start 3 (bar)', BOX]], ('40%', '60%')))}
{ex(2, 'Run-throughs', 1, 'Play it through once a day without stopping. Tick a circle each day.', ticks(7))}
{ex(3, 'After the concert', 2, 'Write one thing that went well and one thing to practise next.', '<p class="how">Went well</p>' + lines(2) + '<p class="how">Practise next</p>' + lines(2))}
{explain(4, 'Explain what you will do if you slip in the middle of your piece.')}''', 10, 'L5+1')
LR = review('Playing and listening', 'PLAYING AND LISTENING', 11, 13, f'''
{ex(1, 'Name it', 1, 'Write the answer.', T4([['the finger number of the thumb', BOX], ['the finger for G, right hand, thumb on C', BOX], ['the step after ♩ = 72 on the ladder', BOX], ['a song that starts with a perfect 4th', LINE]], ('64%', '36%')))}
{ex(2, 'Complete it', 2, 'One word in each space.', sent([f'Practise the {BOX} bar first.', f'Before sight-reading, look at the key and the {BOX} signature.', f'After a slip, keep the {BOX} going.']))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('Going up, the right thumb passes under.', 'Minor chords usually sound brighter than major.', 'Speed up only after three correct times.')))}''')
LP = progress('Playing and listening', 'PLAYING AND LISTENING', 12, [('finger numbers', 'L1'), ('scale fingering', 'L1'), ('a practice plan', 'L2'), ('the metronome ladder', 'L2'), ('the thirty-second scan', 'L3'), ('intervals by song', 'L4'), ('major or minor by ear', 'L4'), ('a performance routine', 'L5')])
LAN = answers('Playing and listening', 'PLAYING AND LISTENING', 13, [
    ('p. 1', 'Numbers: 2, 3, 4, 5. Five-finger: right 1 2 3 4 5 · left 5 4 3 2 1. C major up: 1 2 3 1 2 3 4 5.'),
    ('p. 2', 'Under or over: thumb under, finger over, finger over, thumb under. Left hand up: 5 4 3 2 1 3 2 1. T/F: F, T, F.'),
    ('p. 3', 'Ladder: 80, 88. Habits: helps, wastes time, wastes time, helps, helps. T/F: T, F, T.'),
    ('p. 4', 'T/F: T, F, T.'),
    ('p. 5', 'Scan: G major, 4 beats; G; up. Order: key 1, time 2, first notes 3, rhythm 4, patterns 5, marks 6. T/F: F, T, T.'),
    ('p. 6', 'Scan: G major, 3 beats; F♯. T/F: T, F, T.'),
    ('p. 7', 'Songs (or any that fit): Frère Jacques · Oh When the Saints · Amazing Grace · Somewhere over the Rainbow. Endings: finished, not finished, finished, not finished. Bright/dark: bright, dark, dark, bright.'),
    ('p. 8', 'T/F: T, F, T.'),
    ('p. 9', 'Routine: breathe 2, beat 3, first note 4, bow 5. After a slip: helps, does not help, helps, does not help. T/F: T, T, F.'),
    ('p. 11', '1 · 5 · 80 · Amazing Grace. hardest; time; beat. T, F, T.')])
LFIRST = {'Under or over?': [('ring', 'thumb under')], 'Good habit?': [('ring', 'helps')], 'Finished or not?': [('ring', 'finished')], 'Bright or dark?': [('ring', 'bright')],
          'After a slip': [('ring', 'helps')], 'Scan this': [('fill', 'G')], 'Scan this too': [('fill', 'G')]}

css += '.opt5 .row b{flex:0 0 30%} .opt5 .tf{letter-spacing:0;white-space:nowrap;font-size:14px}'
def _write(fn, pages, first):
    pages = [re.sub(r'<div class="foot"><span>\d+</span>', f'<div class="foot"><span>{k + 1}</span>', p, count=1) for k, p in enumerate(pages)]
    h = _LG(firstdone.apply(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{"".join(pages)}{SIZEJS}</body></html>', first).replace('</style></head>', firstdone.CSS + '</style></head>', 1))
    h = re.sub(r'<div class="wbhd"><div><div class="kick">(.*?)</div>', r'<div class="kick">\1</div><div class="wbhd"><div>', h)   # review: the kicker runs full width above the picture
    h = re.sub(r'max-height:\d+px;max-width:\d+%"', 'width:46%;max-height:none;flex:0 0 46%"', h)
    open(f'/mnt/user-data/outputs/house-rooms/{fn}.html', 'w').write(h)
_write('workbook-expression', [EA1, EB1, EA2, EB2, EA3, EB3, EA4, EB4, EA5, EB5, ER, EP, EAN], EFIRST)
_write('workbook-shape', [FA1, FB1, FA2, FB2, FA3, FB3, FA4, FB4, FA5, FB5, FA6, FB6, FR, FP, FAN], FFIRST)
_write('workbook-play', [LA1, LB1, LA2, LB2, LA3, LB3, LA4, LB4, LA5, LB5, LR, LP, LAN], LFIRST)
print('ok wbmore')
