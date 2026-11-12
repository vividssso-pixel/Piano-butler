# Part III Scales and keys, chapters 1-5, rewritten 7 Nov to the Pitch rules (her): asking Examples (red ?), hops for sizes,
# strict order (nothing before it is taught), minors as changes to the major on the SAME note (her teaching order), relative minor
# only with key signatures, circle read as "right adds a sharp, left adds a flat". exec'd from pitch.py after pitch_new.py.
def wn(i, t, red=False): return ('w', i, t, red)
def bn(i, t, red=True): return ('b', i, t, red)
def qtag(fig): return f'<div style="display:flex;align-items:center;justify-content:center;gap:16px"><div style="flex:0 1 auto;min-width:0">{fig}</div><span style="flex:none;width:38px;height:38px;border-radius:50%;background:#e4572e;color:#fff;font:700 24px AH,Arial;display:flex;align-items:center;justify-content:center">?</span></div>'
def strip(seq, counts, q=None, col=RED):   # keys round the circle as a row of stepping stones; q = index shown as '?'
    o = ''
    for i, (k, c) in enumerate(zip(seq, counts)):
        isq = i == q
        o += (f'<div class="stone{" sq" if isq else ""}"><b>{k}</b><span>{"?" if isq else c}</span></div>' + ('<i>›</i>' if i < len(seq) - 1 else ''))
    return f'<div class="stones">{o}</div>'
css += """
.stones{display:flex;align-items:center;justify-content:center;gap:6px;margin:8px 0} .stones i{font-style:normal;font-size:22px;color:#c9c7da} .stone{border:2px solid #26296b;border-radius:10px;width:64px;padding:6px 0;text-align:center} .stone b{display:block;font-family:PF,serif;font-size:22px;color:#26296b} .stone span{font-size:12.5px;font-weight:700;color:#6d6f9c} .stone.sq{border-color:#e4572e;background:#fff3ee} .stone.sq span{color:#e4572e;font-size:16px}
"""
def hero_cmin():   # C major above, C natural minor below: notes 3, 6 and 7 each move one key left
    W, H = 46, 150
    maj = qkb('C', 8, W, H, nums=[wn(i, i + 1) for i in range(8)], scale=1.0)
    mn = qkb('C', 8, W, H, nums=[wn(0, 1), wn(1, 2), bn(1, 3), wn(3, 4), wn(4, 5), bn(4, 6), bn(5, 7), wn(7, 8)], scale=1.0)
    lab = lambda t, c: f'<div style="font-family:AH,Arial;font-weight:700;font-size:15px;color:{c};margin:4px 0">{t}</div>'
    return f'<div style="display:flex;flex-direction:column;align-items:center;gap:4px">{lab("C major", NAV)}{maj}{lab("C minor: 3, 6 and 7 move one key left", RED)}{mn}</div>'

# ---------- 1 Major scales ----------
P29 = ppage(f"""{head('Part I · Pitch · 8', 'Major scales', 'A <b>scale</b> climbs from a home note, the <b>key note</b>, to the next note with the same name, using every letter once. A <b>major</b> scale always takes the same steps, whatever note it starts on.')}
{hero(hero_stairs(), 'Tone, tone, semitone, tone, tone, tone, semitone')}
{rule('<b>T</b> = tone = <b>one key between</b>. <b>S</b> = semitone = <b>no key between</b>: the very next key, best friends. Every major scale: <b>T T S T T T S</b>.')}
{inaction('Where are the short steps?', qtag(kq('C', 8, 48, 104, nums=[wn(i, i + 1) for i in range(8)])), ['<b>Play C up to C</b> on the white keys, numbering the notes 1 to 8.', '<b>Between each pair,</b> look for a black key. A key between means a tone.', '<b>Which pairs have no black key</b> between them?'], 'Only <b>3–4</b> (E–F) and <b>7–8</b> (B–C): nothing between. Those are the two short steps of every major scale.')}
<!--SPLIT-->
{inaction('Build G major', kq('G', 8, 48, 104, nums=[wn(i, i + 1) for i in range(8) if i != 6], q=(6,)), ['<b>Write the letters</b> G to G: G A B C D E F G.', '<b>Check the top:</b> 6 to 7 must be T (one key between), 7 to 8 must be S (none between). E to F has nothing between.', '<b>Move the ? one key right.</b> What is it called now?'], 'The <b>?</b> becomes <b>F♯</b>. G major: G A B C D E F♯ G, one sharp.')}
{inaction('Build D major', kq('D', 8, 48, 104, nums=[wn(i, i + 1) for i in range(8) if i not in (2, 6)], q=(2, 6)), ['<b>Write the letters</b> D to D.', '<b>Check each step</b> against T T S T T T S: is there a key between?', '<b>Two steps are too short.</b> Move each ? one key right.'], 'D major: D E <b>F♯</b> G A B <b>C♯</b> D, two sharps.')}
{youknow('Joy to the World', ykfig('yk_joy', ('n1','n2','n3','n4','n5','n6','n7','n8'), 64), 'The first line is the <b class="co">C major scale</b>, top to bottom: C B A G F E D C.', 'Play C major down from the top C and sing “Joy to the world” over it.')}
<!--SPLIT-->
{inaction('Build F major', kq('F', 8, 48, 104, nums=[wn(i, i + 1) for i in range(8) if i != 3], q=(3,)), ['<b>Write the letters</b> F to F: F G A B C D E F.', '<b>Check 3 to 4:</b> it must be S, nothing between. A to B has a key between: too big.', '<b>Move the ? one key left.</b> What is it called now?'], 'The <b>?</b> becomes <b>B♭</b>. F major: F G A B♭ C D E F, one flat.')}
{inaction('Build A major', kq('A', 8, 48, 104, nums=[wn(i, i + 1) for i in range(8) if i not in (2, 5, 6)], q=(2, 5, 6)), ['<b>Write the letters</b> A to A.', '<b>Check each step:</b> two are too short and the top one is too big.', '<b>Move each ? one key right.</b>'], 'A major: A B <b>C♯</b> D E <b>F♯ G♯</b> A, three sharps.')}
{watch(['Using the same letter twice: every letter appears once (F♯ in G major, never G♭).', 'Forgetting the short step at the top: 7 to 8 never has a key between.'])}
{game('Spot the wrong note', qitems(['G A B C D E F G', 'D E F♯ G A B C D', 'F G A B C D E F'], 3), 'Each of these major scales has one note that breaks T T S T T T S. Which one, and what should it be?', '1 F should be F♯ · 2 C should be C♯ · 3 B should be B♭.')}
{try10(kbx('C', 8, 24, 70, label=True, shade={2: PINK, 3: PINK, 6: PINK, 7: PINK}, scale=1.0), 'One finger, C to C.', 'Play the white keys from C up to C and say “tone, tone, semitone, tone, tone, tone, semitone”. Feel the two short steps.')}
{foot('Minor scales p. {{S2}} · Keys and key signatures p. {{S3}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Scales')}""", 29)

# ---------- 2 Minor scales: the major on the same note, three notes lowered ----------
P29b = ppage(f"""{head('Part I · Pitch · 9', 'Minor scales', 'Play C major, then C minor: same home note, but the mood turns darker and more serious. Minor scales come in three versions, and all of them start from the major scale you already know.')}
{hero(hero_cmin(), 'The same home note · three notes one key lower')}
{rule('<b>Natural minor</b> = the major with 3, 6 and 7 lowered one key. <b>Harmonic minor</b> = the natural minor with 7 raised again. <b>Melodic minor</b> = going up, 6 and 7 raised; coming down, the natural minor.')}
{h3('A minor in three forms')}
{px('a_nat', 84, 'Natural: A major (F♯ C♯ G♯) with 3, 6 and 7 lowered: C, F and G. All white keys.')}
{px('a_har', 84, 'Harmonic: the 7th raised again, one key up: <b class="co">G♯</b>.')}
{px('a_mel', 84, 'Melodic: going up, 6 and 7 raised (<b class="co">F♯ G♯</b>); coming down, back to <b class="co">G F</b>.')}
<!--SPLIT-->
{inaction('Build C natural minor', kq('C', 8, 52, 120, nums=[wn(i, i + 1) for i in range(8) if i not in (2, 5, 6)], q=(2, 5, 6)), ['<b>Start from C major:</b> C D E F G A B C.', '<b>The ? keys are 3, 6 and 7.</b> Move each one key left.', '<b>Name the keys you land on.</b>'], 'C natural minor: C D <b>E♭</b> F G <b>A♭ B♭</b> C.')}
{inaction('Build A harmonic minor', ask(ykfig('a_nat', ('n7',), 88), ('n7',)), ['<b>Start from A natural minor:</b> A B C D E F G A, all white.', '<b>Take note 7</b> (the ?) and raise it one key.', '<b>Name it.</b>'], 'Note 7 becomes <b>G♯</b>: A harmonic minor is A B C D E F G♯ A.')}
{youknow('Greensleeves', ykfig('yk_green', ('n4','n7'), 76), 'A minor, with a <b class="co">G♯</b>: the raised 7th of the harmonic minor, leaning hard up to A.', 'Play it once with G♯, once with G: hear the pull disappear.')}
<!--SPLIT-->
{inaction('Build D natural minor', kq('D', 8, 52, 120, nums=[wn(0, 1), wn(1, 2), bn(2, '?'), wn(3, 4), wn(4, 5), wn(5, '?', True), bn(6, '?'), wn(7, 8)]), ['<b>This is D major.</b> The ? keys are notes 3, 6 and 7.', '<b>Move 3, 6 and 7</b> one key left each.', '<b>Name the new keys.</b>'], 'D natural minor: D E <b>F</b> G A <b>B♭ C</b> D.')}
{watch(['Lowering the wrong notes: only 3, 6 and 7 move.', 'Playing the melodic minor’s raised notes on the way down.'])}
{game('Which minor?', qitems(['nothing raised', 'the 7th raised', '6th and 7th raised going up, lowered coming down'], 3), 'Three forms of the minor scale. Name each one.', '1 natural · 2 harmonic · 3 melodic.')}
{try10(kbx('C', 8, 24, 70, label=True, shade={2: PINK, 5: PINK, 6: PINK}, scale=1.0), 'Major, then minor.', 'Play C major, then play it again with E, A and B one key lower. Same home, new colour: bright, then dark.')}
{foot('Major scales p. {{S1}} · Keys and key signatures p. {{S3}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Scales')}""", 30)

# ---------- 3 Keys and key signatures (reading them; the relative minor) ----------
keys4 = [['C major', 'none'], ['G major', '1♯: F♯'], ['D major', '2♯: F♯ C♯'], ['F major', '1♭: B♭']]
P30 = ppage(f"""{head('Part I · Pitch · 10', 'Keys and key signatures', 'Why write F♯ fifty times? The <b>key signature</b> at the start of each line says it once, for the whole piece. Its sharps or flats always line up in the same order.')}
{hero(pxh('hero_ks', ('n1', 'n4', 'n6'), 230), 'One sharp at the start: every F plays F♯')}
{two(px('sharps', 112, 'Sharps always come in this order: F C G D A E B.'), px('flats', 112, 'Flats: B E A D G C F, the sharps backwards.'))}
<p class="sm">To remember the order: <b>F</b>ather <b>C</b>harles <b>G</b>oes <b>D</b>own <b>A</b>nd <b>E</b>nds <b>B</b>attle; backwards for the flats: <b>B</b>attle <b>E</b>nds <b>A</b>nd <b>D</b>own <b>G</b>oes <b>C</b>harles’ <b>F</b>ather.</p>
{two(tbl(['Key you built', 'Key signature'], keys4, ['50%', '50%']), h3('One signature, two keys') + '<p>Every key signature also belongs to a <b>minor</b> key: the <b>relative minor</b>. To find it, go <b>down a minor 3rd</b>: 2 keys between, then land. C major and A minor share every note: all white keys.</p>', '1fr 1.2fr')}
<!--SPLIT-->
{inaction('Which notes are sharp?', qtag(px('ks_2s', 84)), ['<b>Count the sharps.</b>', '<b>Name them in order:</b> the first sharp is always F, then …', '<b>Which keys turn black</b> for the whole piece?'], 'Two sharps, <b>F♯ and C♯</b>: every F and every C in the piece, high or low.')}
{inaction('Find the relative minor of C major', kq('F', 8, 48, 120, tags={4: 'start'}, tagcol={4: NAV}, nums=[wn(3, 1, False), bn(2, 2, False)], q=(2,), shade={4: '#fbd0c2'}), ['<b>Start on C</b>, the key note.', '<b>Count 2 keys between, going down:</b> B is 1, B♭ is 2 …', '<b>The next key is the ?.</b>'], 'You land on <b>A</b>: the relative minor of C major is <b>A minor</b>.')}
{inaction('Find the relative minor of F major', kq('C', 8, 48, 120, tags={3: 'start'}, tagcol={3: NAV}, nums=[wn(2, 1, False), bn(1, 2, False)], q=(1,), shade={3: '#fbd0c2'}), ['<b>Start on F.</b>', '<b>Count 2 keys between, going down:</b> E is 1, E♭ is 2 …', '<b>The next key is the ?.</b>'], 'The <b>?</b> is <b>D</b>: D minor, which shares F major’s one flat, B♭.')}
<!--SPLIT-->
{youknow('Minuet in G', ykfig('yk_minuet2', ('n5',), 88), 'One sharp in the key signature: every F is <b class="co">F♯</b>, like the one just before the top G. One sharp, and the piece ends on G: <b>G major</b>.', 'Find every F in the piece and play it as F♯.')}
{inaction('Which notes are flat?', qtag(px('ks_3f', 84)), ['<b>Count the flats.</b>', '<b>Name them in order:</b> the first flat is always B, then …', '<b>Which keys turn black?</b>'], 'Three flats, <b>B♭ E♭ A♭</b>: every B, E and A in the piece.')}
{watch(['Writing a key signature in the wrong order: sharps always F C G D A E B.', 'Reading it once and forgetting it: glance at the key signature at the start of every line.'])}
{thinkt('A dress code on a party invitation: written once at the top, it applies to every guest all night. Only an accidental, a word to one guest, overrules it, and only until the bar line.')}
{game('Which comes next?', qitems(['sharps: F C G …', 'flats: B E …', 'the 1st flat', 'the 2nd sharp'], 4), 'Use the orders of sharps and flats.', '1 D · 2 A · 3 B♭ · 4 C♯.')}
{try10(px('sharps', 60), 'Say the sharps in order.', '“Father Charles Goes Down And Ends Battle”: F C G D A E B. Then backwards for the flats: B E A D G C F.')}
{foot('Major scales p. {{S1}} · Finding the key p. {{S4}} · The circle of fifths p. {{S5}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Keys')}""", 31)

# ---------- 4 Finding the key ----------
_fkkb = kbx('F', 6, 40, 120, label=True, shade={2: BLUE}, marks=[f'<text x="{x}" y="{y}" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="{c}">{t}</text>' for x, y, t, c in ((80, 62, '1', '#fff'), (60, 100, '2', NAV))] + ['<circle cx="40" cy="58" r="11" fill="#e4572e"/><text x="40" y="62" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="#fff">?</text>', '<text x="100" y="100" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" fill="#26296b">start</text>'], scale=1.0)
P31 = ppage(f"""{head('Part I · Pitch · 11', 'Finding the key', 'A key signature names two keys, a major and its relative minor. Two quick rules find the major; a minor 3rd down finds the minor; then the music itself tells you which of the two it is.')}
{hero(hero_findkey(), 'Sharps: the last sharp, then the very next key up. Three sharps: A major')}
<div class="fk"><div class="fkf">{px('ks_3f', 118)}</div><div><b>Flats: the second-last flat is the key.</b><br>B♭ E♭ A♭: the second-last is E♭, so <b class="co">E♭ major</b>. One flat alone is F major.</div></div>
<div class="fk"><div class="fkf">{_fkkb}</div><div><b>Major to minor: down a minor 3rd.</b><br>From A: 2 keys between, G♯ and G, then land on <b class="co">F♯</b>. Three sharps is A major <b>or</b> F♯ minor.</div></div>
<!--SPLIT-->
{inaction('Name the major key: sharps', qtag(px('ks_2s', 84)), ['<b>Find the last sharp,</b> the one furthest right.', '<b>Name it</b> (F first, then C …).', '<b>Go to the very next key up.</b> That is the key.'], 'The last sharp is C♯; the next key up is D: <b>D major</b>.')}
{inaction('Name the major key: flats', qtag(px('ks_2f', 84)), ['<b>Find the second-last flat.</b>', '<b>Name it</b> (B first, then E …).', '<b>That flat names the key.</b>'], 'B♭ E♭: the second-last is B♭: <b>B♭ major</b>.')}
{inaction('Major or minor?', qtag(ask(px('ex_key', 96), (), True)), ['<b>The key signature:</b> one sharp. Which major, and which minor a minor 3rd below it?', '<b>Look for a sharp that is not in the signature.</b> A minor key raises its 7th: whose 7th is it?', '<b>Look at the last note.</b>'], 'One sharp, D♯ clues, ending on E: <b>E minor</b>, not G major.')}
<!--SPLIT-->
{youknow('Für Elise (Beethoven)', ykfig('yk_elise2', ('n1','n9'), 76), 'No key signature, a <b class="co">G♯</b> as the clue, and the music keeps coming home to <b class="co">A</b>: <b>A minor</b>.', 'Play A, then G♯ A: hear the G♯ lean into home.')}
{h3('Minor keys and their clue notes')}
{tbl(['Minor key', 'Signature', 'Clue note (the raised 7th)'], [['A minor', 'none', '<b class="co">G♯</b>'], ['E minor', '1♯', '<b class="co">D♯</b>'], ['D minor', '1♭', '<b class="co">C♯</b>'], ['B minor', '2♯', '<b class="co">A♯</b>'], ['G minor', '2♭', '<b class="co">F♯</b>']], ['34%', '28%', '38%'])}
{inaction('Find a minor key from its clue', qtag(px('ks_2f', 72)), ['<b>Two flats:</b> B♭ major, or the minor a minor 3rd below it.', '<b>Count 2 keys between going down</b> from B♭: A, A♭ … and land. Which minor key is it, and what is its 7th note?', '<b>Raise that 7th</b>: if the piece is full of it, the key is minor.'], 'Two flats with F♯ clues: <b>G minor</b> (its 7th, F, raised to F♯).')}
{thinkt('Detective work: the key signature narrows it to two suspects; the clue note and the last note name the culprit.')}
{game('Name the major key', qitems(['2 sharps', '4 sharps', '1 flat', '3 flats'], 4), 'Sharps: the last sharp, the very next key up. Flats: the second-last flat (one flat alone is F).', '1 D · 2 E · 3 F · 4 E♭.')}
{try10(px('ks_3s', 64), 'Three sharps, stop, step up.', 'Say “F C G”, stop: the last one is G♯. The next key up is A. Three sharps is A major. Try it with two and four.')}
{howto('Find the key of a new piece', ['<b>The key signature:</b> name the major key, and its relative minor a minor 3rd below.', '<b>The clue notes:</b> look for the minor key’s raised 7th.', '<b>The last bass note:</b> pieces nearly always end on the key note.'])}
{foot('Keys and key signatures p. {{S3}} · The circle of fifths p. {{S5}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Keys')}""", 32)

# ---------- 5 The circle of fifths ----------
P32 = ppage(f"""{head('Part I · Pitch · 12', 'The circle of fifths', 'Twelve major keys sit around one clock face, with C at twelve o’clock. Learn to read this clock and you can name any key signature in seconds.')}
{hero(circle_hero(), 'Right: one more sharp · left: one more flat')}
{two(h3('How to read the clock') + '<p><b>Outer ring:</b> the major keys. <b>Inner ring:</b> their relative minors. <b>Outside the circle:</b> how many sharps or flats.</p>', h3('Neighbours are close') + '<p>Keys side by side share all but one note, so music moves between them easily: from C major to G major or F major, or to the relative minor.</p>')}
{rule('Each step right is a <b>5th up</b>: count the notes, C D E F G, and G is the next key round. That is why it is called the circle of <b>fifths</b>.')}
<!--SPLIT-->
{inaction('How many sharps in A major?', strip(['C', 'G', 'D', 'A'], ['none', '1♯', '2♯', '3♯'], q=3), ['<b>Start at C</b>, at the top: no sharps.', '<b>Go right</b> one step at a time: G, D …', '<b>Count the steps</b> to A.'], 'Three steps right: A major has <b>three sharps</b>, F♯ C♯ G♯.')}
{inaction('How many flats in E♭ major?', strip(['C', 'F', 'B♭', 'E♭'], ['none', '1♭', '2♭', '3♭'], q=3), ['<b>Start at C</b> again.', '<b>Go left:</b> F, B♭ …', '<b>Count the steps</b> to E♭.'], 'Three steps left: E♭ major has <b>three flats</b>, B♭ E♭ A♭.')}
{inaction('Why do G and D sound so close?', two(kq('G', 8, 34, 96, dots=(0, 1, 2, 3, 4, 5), bdots=(6,)), kq('D', 8, 34, 96, dots=(0, 1, 3, 4, 5), bdots=(2,), qb=(6,))), ['<b>G major</b> (left) and <b>D major</b> (right) are neighbours on the clock.', '<b>Compare their notes:</b> which letters are the same?', '<b>Which one letter changes?</b>'], 'Six notes are the same; only C becomes <b>C♯</b>. One step round the circle changes just one note.')}
<!--SPLIT-->
{h3('The first steps round the circle')}
{tbl(['Steps', 'Right (sharps)', 'Left (flats)'], [['1', 'G major: F♯', 'F major: B♭'], ['2', 'D major: F♯ C♯', 'B♭ major: B♭ E♭'], ['3', 'A major: F♯ C♯ G♯', 'E♭ major: B♭ E♭ A♭']], ['16%', '42%', '42%'])}
{inaction('Find the minor inside D', kq('A', 8, 48, 120, tags={3: 'start'}, tagcol={3: NAV}, nums=[bn(2, 1, False), wn(2, 2, False)], q=(1,), shade={3: '#fbd0c2'}), ['<b>Start on D</b>, on the outer ring.', '<b>Count 2 keys between, going down:</b> C♯ is 1, C is 2 …', '<b>The next key is the ?.</b> It sits on the inner ring, just inside D.'], 'The <b>?</b> is <b>B</b>: B minor, D major’s relative minor. Both have two sharps.')}
{watch(['Going the wrong way round: right adds sharps, left adds flats.', 'Forgetting the relative minors on the inner ring.'])}
{game('Neighbours on the clock', qitems(['right of D', 'left of C', 'opposite C', 'inside G'], 4), 'Right adds a sharp. Inside each major sits its relative minor.', '1 A · 2 F · 3 F♯ / G♭ · 4 E minor.')}
{try10(kq('C', 15, 20, 66, dots=(0, 4, 8, 12), scale=1.0), 'Walk the circle: C G D A.', 'Play each key note with one finger, a 5th up each time. You just walked three steps right round the circle.')}
{howto('Learn the circle by heart', ['<b>Right, out loud:</b> C G D A E B F♯.', '<b>Left:</b> C F B♭ E♭ A♭ D♭ G♭.', '<b>Check yourself:</b> the number of steps from C is the number of sharps or flats.'])}
{foot('Keys and key signatures p. {{S3}} · Finding the key p. {{S4}} · Chords: Harmony (later)', 'Workbook Pitch 5 · Online: Scale finder, Library › Related keys')}""", 33)
