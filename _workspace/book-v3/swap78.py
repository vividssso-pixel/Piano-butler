# Her 17-18 Nov ("두개 순서 바뀌어야할 듯", "톤 세미톤때 검은건반 흰건반의 연관성 미리 맛보기 하고 사인 알려주고 인터벌로"):
# Tones and semitones now comes before Sharps, flats and naturals (Pitch 7 and 8 swap; the keys P7/P8 follow the new
# numbers). Tones and semitones gives a first taste of how a black key sits between two white ones; the sharps chapter
# builds on the semitone. The Guest is explained as what she is (a sharp or flat written in the music, visiting one bar,
# her hat is the sign) and speaks only after the bar-line rule. Same page count.
import re, sys
S = sys.argv[1]
def rw(f, fn): p = f'{S}/{f}'; h = open(p).read(); h2 = fn(h); assert h2 != h, f; open(p, 'w').write(h2)
def rep(h, a, b, n=1): assert h.count(a) == n, (a[:80], h.count(a)); return h.replace(a, b)
SW = lambda h: h.replace('data-k="P7"', '@@P7@@').replace('data-k="P8"', 'data-k="P7"').replace('@@P7@@', 'data-k="P8"')
def pitch(h):
    secs = [(m.start(), m.end()) for m in re.finditer(r'<section\b.*?</section>', h, re.S)]
    get = lambda k: [h[a:b] for a, b in secs if h[a:b].startswith(f'<section class="pg mk" data-k="{k}"')]
    s7a, s7b = get('P7'); s8, = get('P8')
    a0 = h.index(s7a); b0 = h.index(s8) + len(s8)
    t = s8   # Tones and semitones: now chapter 7, p. 32
    t = rep(t, 'Part I · Pitch · 8', 'Part I · Pitch · 7'); t = rep(t, '<span>34</span></div></section>', '<span>32</span></div></section>')
    t = rep(t, 'Read &amp; listen › Pitch › 8', 'Read &amp; listen › Pitch › 7')
    t = rep(t, '>C♯ between: a tone<', '>a black key between: a tone<')
    t = rep(t, 'Everywhere else a black key sits between two white keys: one key between, a <b>tone</b>.</p>',
            'Everywhere else a black key sits between two white keys: one key between, a <b>tone</b>. And each black key is a semitone from <b>both</b> of its white neighbours, so it can take its name from either side: that is the next chapter.</p>')
    t = rep(t, 'Sharps, flats and naturals <span class="pref" data-k="P7">p.&nbsp;32</span>', 'Sharps, flats and naturals <span class="pref" data-k="P7">p.&nbsp;33</span>')
    a = s7a  # Sharps, flats and naturals: now chapter 8, pp. 33-34
    a = rep(a, 'Part I · Pitch · 7', 'Part I · Pitch · 8'); a = rep(a, '<span>32</span></div></section>', '<span>33</span></div></section>')
    a = rep(a, 'The black keys have no letters of their own. They borrow the names of their white neighbours, adding a sharp or a flat.',
            'The black keys have no letters of their own. Each one is a semitone from two white neighbours (p.&nbsp;32), and borrows a name from either, adding a sharp or a flat.')
    a = rep(a, '<span class="sbi"><b>The Guest</b>“Until the bar line, darling. That’s the front door.”</span>', '')
    b = s7b
    b = rep(b, 'Part I · Pitch · 7 · continued', 'Part I · Pitch · 8 · continued'); b = rep(b, '<span>33</span></div></section>', '<span>34</span></div></section>')
    b = rep(b, 'Read &amp; listen › Pitch › 7', 'Read &amp; listen › Pitch › 8')
    b = rep(b, 'A <b>semitone</b> is the smallest step on the piano: from one key to the very next, black or white (American books call it a <i>half step</i>).',
            'A <b>semitone</b> is the very next key (Tones and semitones, p.&nbsp;32).')
    b = rep(b, 'And a natural cancels a sharp just as it cancels a flat.</p>',
            'And a natural cancels a sharp just as it cancels a flat.</p>'
            '<p class="sm" style="margin-top:6px"><b>Think of it: the Guest.</b> A sharp or flat written in front of a note is a Guest who visits for one bar. '
            'The sign is her hat: ♯ lifts the note to the very next key on the right, ♭ lowers it to the very next key on the left. '
            'Every note on that line or space in the bar wears the hat too. At the bar line she leaves, and takes her hat with her; a natural ♮ takes it off sooner.</p>'
            '<span class="sbi"><b>The Guest</b>“Until the bar line, darling. That’s the front door.”</span>')
    b = rep(b, 'Tones and semitones <span class="pref" data-k="P8">p.&nbsp;34</span>', 'Tones and semitones <span class="pref" data-k="P8">p.&nbsp;32</span>')
    mid = h[h.index(s7a) + len(s7a) + len(s7b) if False else a0:b0]
    new = SW(t) + SW(a) + SW(b)
    pre, post = h[:a0], h[b0:]
    def others(x):   # other pages' links: P8 (tones) was p. 34 → 32 (now P7); P7 (sharps) p. 32 → 33 (now P8)
        x = x.replace('<span class="pref" data-k="P8">p.&nbsp;34</span>', '@@T@@').replace('<span class="pref" data-k="P7">p.&nbsp;32</span>', '@@S@@')
        return x.replace('@@T@@', '<span class="pref" data-k="P7">p.&nbsp;32</span>').replace('@@S@@', '<span class="pref" data-k="P8">p.&nbsp;33</span>')
    h = others(pre) + new + others(post)
    h = rep(h, '7 · Sharps, flats and naturals<br>8 · Tones and semitones', '7 · Tones and semitones<br>8 · Sharps, flats and naturals')
    return h
rw('pitch-pilot.html', pitch)
def front(h):
    h = rep(h, '<div class="tr ftr"><span>7 · Sharps, flats and naturals</span><span class="dots"></span><span>32</span></div><div class="tr ftr"><span>8 · Tones and semitones</span><span class="dots"></span><span>34</span></div>',
            '<div class="tr ftr"><span>7 · Tones and semitones</span><span class="dots"></span><span>32</span></div><div class="tr ftr"><span>8 · Sharps, flats and naturals</span><span class="dots"></span><span>33</span></div>')
    return SW(h)
rw('front.html', front)
def gloss(h):
    def fix(h, term, old, new):
        h2 = re.sub(r'(<b>' + re.escape(term) + r'</b>[^<]*<i>p\.&#8202;)' + old + r'(</i>)', r'\g<1>' + new + r'\g<2>', h, count=1)
        assert h2 != h, term; return h2
    for w in ('accidental', 'enharmonic', 'flat (♭)', 'natural (♮)', 'sharp (♯)'): h = fix(h, w, '32', '33')
    for w in ('semitone', 'tone'): h = fix(h, w, '34', '32')
    h = fix(h, 'interval', '34', '35')
    return SW(h)
rw('glossary.html', gloss)
rw('play-pilot.html', lambda h: rep(h, 'Sharps, flats and naturals, p.&nbsp;32', 'Sharps, flats and naturals, p.&nbsp;33'))
def wb(h):
    secs = [(m.start(), m.end()) for m in re.finditer(r'<section\b.*?</section>', h, re.S)]
    s7 = [(a, b) for a, b in secs if 'data-k="P7"' in h[a:a + 200]]; s8 = [(a, b) for a, b in secs if 'data-k="P8"' in h[a:a + 200]]
    assert len(s7) == 1 and len(s8) == 1 and s7[0][1] <= s8[0][0]
    A = h[s7[0][0]:s7[0][1]]; Bs = h[s8[0][0]:s8[0][1]]; gap = h[s7[0][1]:s8[0][0]]
    A = rep(A, 'HANDBOOK P. 32', 'HANDBOOK P. 33') if 'HANDBOOK P. 32' in A else A
    Bs = rep(Bs, 'HANDBOOK P. 34', 'HANDBOOK P. 32') if 'HANDBOOK P. 34' in Bs else Bs
    h = h[:s7[0][0]] + SW(Bs) + gap + SW(A) + h[s8[0][1]:]
    return h
rw('wb/pitch.html', wb)
print('swap done')
def wb2(h):
    rows = {n: re.search(r'<tr><td>p\. ?' + str(n) + r'</td><td>.*?</td></tr>', h).group(0) for n in (18, 19, 20)}
    body = lambda r: r[r.index('</td><td>') + 9:-10]
    new = {18: body(rows[20]), 19: body(rows[18]), 20: body(rows[19])}
    for n in (18, 19, 20): h = h.replace(rows[n], '@@R%d@@' % n)
    for n in (18, 19, 20): h = h.replace('@@R%d@@' % n, rows[n][:rows[n].index('</td><td>') + 9] + new[n] + '</td></tr>')
    a = re.search(r'<tr><td>sharps, flats and naturals</td>.*?</tr>', h).group(0); b = re.search(r'<tr><td>counting intervals; tones and semitones</td>.*?</tr>', h).group(0)
    cb = a[a.index('</td>') + 5:a.rindex('<td>')]
    T = lambda name, pg: '<tr><td>' + name + '</td>' + cb + '<td>p. ' + pg + '</td></tr>'
    h = h.replace(a + b, T('tones and semitones', '32') + T('sharps, flats and naturals', '33') + T('counting intervals', '35'))
    assert 'counting intervals</td>' in h
    return h
rw('wb/pitch.html', wb2)
print('workbook answers and progress done')
