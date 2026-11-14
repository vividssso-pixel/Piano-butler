# Her 14 Nov ("왕의 걱정이 뭐였지? 라는 물음표가 있으면 … 외우는 대신 자연스레 알게 되는 거"): one funny moment per chapter,
# taken from the Read & listen scripts (no new metaphors). (1) The Handbook prints it as a small speech bubble on the
# chapter's first page, so readers and listeners share the scene. (2) The Workbook's Learn page opens with a story
# question that sends the child back to it; the answer is in the answer key. Runs after wbfix.py (page numbers final).
import re, json, sys
sys.path.insert(0, '/tmp/claude-0/pk'); import pagemap as PM
H = '/mnt/user-data/outputs/house-rooms/'
J = json.load(open(H + 'workbook-pages.json')); OFF = J['off']
# key: (speaker, bubble, question, answer); bubble None = the moment is already printed
S = {
 'P1': ('Clara', 'Butler, what comes after G? H?', 'Clara guessed a letter that comes after G. Which letter did she guess?', 'H (there is no H: after G comes A again)'),
 'P2': ('The King', 'My clef’s two dots hug line four, like a pair of eyes.', 'What do the two dots on the King’s clef look like?', 'a pair of eyes (on either side of line 4, F)'),
 'P3': ('The King', 'Two guards at the castle gate, with Middle C between us.', 'The King’s F and the Queen’s G stand like two what at the castle gate?', 'guards (F and G, with Middle C between)'),
 'P4': ('The King', 'You have no idea. The dragons keep eating the cows’ grass.', 'Something in the King’s kingdom keeps eating the cows’ grass. What is it?', 'dragons (Great Big Dragons Fly Away; All Cows Eat Grass)'),
 'P5': ('The Queen', 'We take turns. Like sharing a bicycle.', 'Which note do the Queen and the King share, the way you would share a bicycle?', 'Middle C'),
 'P6': ('The Guest', 'Until the bar line, darling. That’s the front door.', 'The Guest in her sharp hat calls one thing in the music her front door. What is it?', 'the bar line'),
 'P7': ('The Butler', 'Here’s a riddle: Monday to Wednesday, how many days?', 'The Butler asked how many days from Monday to Wednesday. Clara said two. What is the right answer?', 'three (count the day you start on)'),
 'P8': ('The Queen', 'Perfect, like me.', 'Which word did the Queen use about herself, and about 4ths, 5ths and octaves?', 'perfect'),
 'T1': ('Clara', 'It’s beating. Steady, steady. Oh good, I’m alive.', 'What good news did Clara find with her hand on her heart?', 'she is alive: her heart beats steadily (a pulse)'),
 'T2': ('Clara', 'Who leaves pizza on the plate?', 'In the pizza story, who leaves their pizza on the plate?', 'rests'),
 'T3': ('The Butler', 'Two notes, but one sound. Two half-sandwiches are still one sandwich.', 'Which food showed Clara that two tied notes make one sound?', 'a sandwich (two halves, one sandwich)'),
 'T4': ('The Stationmaster', 'Tickets, please! I check the time signature at the start of the line.', 'On the Stationmaster’s train, what is each bar of music?', 'a carriage (the top number is its seats)'),
 'T5': ('Clara', 'Pine-ap-ple, pine-ap-ple. Now I want a fruit salad.', 'Which fruit did Clara chant as she stepped?', 'pineapple (three quavers in each beat)'),
 'T6': ('The Butler', 'A very small, polite dinosaur that arrives early.', 'The Butler says an upbeat is like a small, polite animal that arrives early. Which animal?', 'a dinosaur that arrives early (an upbeat)'),
 'T7': ('Clara', 'My foot is very easily distracted.', 'When Clara clapped between the beats, which part of her kept getting distracted?', 'her foot (it keeps the beat)'),
 'T8': ('Clara', 'Dad drives round the roundabout twice when he misses the turning.', 'What does Clara’s dad sometimes drive round twice?', 'the roundabout (a repeat)'),
 'E1': ('The Butler', 'This is pianissimo. Very soft, like a mouse in slippers.', 'The Butler says pianissimo is very soft, like a mouse in what?', 'slippers (pp)'),
 'E2': ('The Butler', 'Dots: short and detached, like popcorn popping.', 'Which snack do staccato dots sound like?', 'popcorn'),
 'E3': ('The Butler', 'Presto, very fast, like a squirrel who has had too much coffee.', 'The fastest speed word is a squirrel that has had too much of which drink?', 'coffee (Presto)'),
 'E4': ('Clara', 'The sound keeps going after my hands stop. Like a ghost clapping back.', 'When Clara clapped in the big school hall, who did she say clapped back?', 'a ghost (the sound rings on, like the right pedal)'),
 'E5': ('Clara', None, 'The Handbook says an ornament is like something you wear. What?', 'a necklace (or a hair clip)'),
 'S1': ('Clara', 'It sounds like a secret knock on a door.', 'Clara said the step pattern of a major scale sounds like a secret what?', 'a knock (T T S T T T S)'),
 'S2': ('Clara', 'Ooh. Same home, but it’s raining now.', 'C major turned into C minor: same home, but what was the weather doing?', 'raining'),
 'S3': ('The King', 'Father Charles was my cousin. He ended a great many battles. Mostly by falling asleep in them.', 'How did Father Charles end so many battles?', 'by falling asleep in them (Father Charles Goes Down And Ends Battle)'),
 'S4': ('The Doorkeeper', 'The last one in always holds the door for the key. Good manners.', 'The last sharp in the key signature holds the door for someone. Who?', 'the key (one key up from the last sharp)'),
 'S5': ('Clara', 'What is that giant clock on the page? Is it time for lunch?', 'Clara thought the circle of fifths was a giant clock. What did she hope it was time for?', 'lunch'),
 'H1': ('Clara', 'Like pressing lots of keys with my elbow?', 'Clara asked if pressing lots of keys with one part of her arm makes a chord. Which part?', 'her elbow (a real triad is play one, skip one)'),
 'H2': ('Clara', 'Sunny, rainy, spooky and dreamy!', 'Sunny, rainy, spooky and what? (the four kinds of triad)', 'dreamy (augmented)'),
 'H3': ('Clara', 'So that’s why so many songs only need three chords!', 'How many chords do so many songs need?', 'three (I, IV and V)'),
 'H4': ('Clara', 'It’s like a family taking turns to sit at the bottom of the bunk bed.', 'Inversions are like a family taking turns on which piece of furniture?', 'a bunk bed'),
 'H5': ('Clara', 'Mwa-ha-ha!', 'Which seventh chord made Clara laugh like a film villain?', 'the diminished seventh'),
 'H6': ('Clara', 'Open, floating, strong, warm, sparkly. It’s like a paint box!', 'Clara said the colour chords are like a box of what?', 'paints'),
 'H7': ('The Butler', 'Like a wedding cake for a giant.', 'A chord that keeps growing past the 7th is like a wedding cake for whom?', 'a giant'),
 'H8': ('Clara', None, 'The Handbook says a slash chord is like a cake standing on what?', 'a plate (the bass note)'),
 'M1': ('Clara', 'Sigh, then push. Like getting out of bed on a Monday.', 'Clara said the two kinds of guest note are like getting out of bed on which day?', 'Monday: first a sigh (down), then a push (up)'),
 'M2': ('Clara', 'Huh?! That one tricked me. I was already putting my coat on.', 'Which ending tricked Clara while she was putting her coat on?', 'the interrupted cadence (V–vi)'),
 'M3': ('Clara', 'Can I have drums?', 'When the Butler let Clara choose the band, which instrument did she ask for?', 'drums (not today: the chords are the band)'),
 'M4': ('Clara', 'Like everyone in town taking the same bus route?', 'Clara said chord progressions are like everyone in town taking the same what?', 'bus route'),
 'F1': ('Clara', 'Bye, Butler? That was a question.', 'Did Clara say goodbye as a statement or as a question?', 'as a question (a phrase can ask, and the next one answers)'),
 'F2': ('Clara', 'Like my mum making soup out of leftovers?', 'Thrifty composers are like Clara’s mum making what out of leftovers?', 'soup'),
 'F3': ('The Butler', 'Run your fingers over your jumper. Feel the threads?', 'The Butler asked Clara to feel the threads of something she was wearing. What?', 'her jumper (texture is how the threads of music are woven)'),
 'F4': ('Clara', 'Does it send a postcard?', 'When music goes on holiday to a new key, what did Clara want it to send?', 'a postcard'),
 'F6': ('The Queen', 'It is like wearing a ball gown to a picnic.', 'The Queen says pedalling Bach like Chopin is like wearing what to a picnic?', 'a ball gown'),
 'L1': ('Clara', 'The thumb is like a little tunnel under a bridge!', 'Clara said the thumb passing under the hand is like a little what under a bridge?', 'a tunnel'),
 'L2': ('The Butler', 'Nearly isn’t three, I’m afraid.', 'How many right in a row does the Butler want before you go faster?', 'three'),
 'L3': ('Clara', 'Like a pilot checking the plane before take-off!', 'Clara said the 30-second look before playing is like whom, checking before take-off?', 'a pilot'),
 'L4': ('Clara', 'I can’t play my ear. I’ve tried wiggling it.', 'What had Clara already tried doing with her ear?', 'wiggling it'),
 'L5': ('The Queen', 'When I forget a word, I simply carry on.', 'What does the Queen do when she forgets a word in a speech?', 'she simply carries on (keep the beat, never go back)'),
}
INLINE = {'H7'}   # pages with no room for a line of its own
CSS = ('.sbn{font:400 18px/1.2 "CV",cursive;font-style:normal;color:#26296b}.sbi{display:block;margin-top:5px;font:400 19px/1.25 "CV",cursive;color:#26296b}'
       '.sbi b{font:700 10.5px/1.2 "AH",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#e4572e;margin-right:8px}'
       '.sq{display:flex;gap:10px;align-items:baseline;margin:4px 0 6px;padding:5px 12px;background:#f6f4fb;border-radius:10px}'
       '.sq b{font:700 10.5px/1.2 "AH",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#e4572e;white-space:nowrap}'
       '.sq span{flex:1;font-size:13.5px;line-height:1.35}.sq em{display:inline-block;min-width:140px;border-bottom:1.5px solid #26296b;margin-left:6px;font-style:normal}'
       '.ansT td{font-size:12px;line-height:1.3}.sqr .sqi{display:flex;gap:8px;align-items:baseline;margin:3px 0;font-size:13.5px}.sqr .sqi em{flex:1;min-width:120px;border-bottom:1.5px solid #26296b}')
from playwright.sync_api import sync_playwright
def measure(files):
    out = {}
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for f in files:
            pg = b.new_page(viewport={'width': 900, 'height': 1300}); pg.goto('file://' + H + f + '.html'); pg.wait_for_timeout(2500)
            out[f] = pg.evaluate("""() => [...document.querySelectorAll('section')].map(s => { const ft = s.querySelector('.foot'), bd = s.querySelector('.body'); if (!ft || !bd) return -1;
                let mx = 0; for (const c of bd.querySelectorAll(':scope > *')) { const r = c.getBoundingClientRect(); if (r.height > 0) mx = Math.max(mx, r.bottom); }
                const sg = s.querySelector('.sign'); return Math.round((sg ? sg.getBoundingClientRect().top : ft.getBoundingClientRect().top) - mx); })""")
            pg.close()
        b.close()
    return out
def foot(sec):
    m = re.search(r'<div class="foot"><span>(\d+)</span>', sec) or re.search(r'class="foot[^"]*"[^>]*>\s*<span>(\d+)</span>', sec)
    return int(m.group(1)) if m else None
# (1) Handbook: the moment joins the chapter's opening paragraph (no new block, so the page flow is unchanged)
HB = ('handbook-pitch', 'handbook-time2', 'handbook-expression', 'handbook-scales', 'handbook-harmony', 'handbook-harmony2', 'handbook-shape', 'handbook-play')
first = {PM.pages_of(k)[0]: k for k in S}
nb = 0
for f in HB:
    s = open(H + f + '.html').read(); out = []
    for sec in re.split(r'(?=<section )', s):
        k = first.get(foot(sec))
        if k and S[k][1] and 'class="sbi"' not in sec:
            m = re.search(r'(<p class="lead">.*?)(</p>)', sec, re.S)
            if m: sec = sec[:m.end(1)] + (f' <i class="sbn">“{S[k][1].rstrip(".")},” says {S[k][0][0].lower() + S[k][0][1:] if S[k][0].startswith("The") else S[k][0]}.</i>' if k in INLINE else f'<span class="sbi"><b>{S[k][0]}</b>“{S[k][1]}”</span>') + sec[m.end(1):]; nb += 1
            else: print('no lead', f, k)
        out.append(sec)
    s = ''.join(out); s = s.replace('</style></head>', CSS + '</style></head>', 1) if '.sbi{' not in s else s
    open(H + f + '.html', 'w').write(s)
# (2) Workbook: the story question on the chapter page with room (Learn first), else in a Story round on the part's Review page
WB = {'P': ('workbook-pitch', 0), 'T': ('workbook-time2', 0), 'E': ('workbook-expression', 0), 'S': ('workbook-scales', 0), 'H': ('workbook-harmony', 0), 'M': ('workbook-harmony', 8), 'F': ('workbook-shape', 0), 'L': ('workbook-play', 0)}
FREE = measure(sorted(set(f for f, _ in WB.values())))
nq = 0; later = {}
def add_answer(pages, absn, text):
    for i, pg in enumerate(pages):
        row = re.search(rf'(<td>p\. {absn}</td><td>)(.*?)(</td>)', pg, re.S)
        if row: pages[i] = pg[:row.end(2)] + f' Story: {text.split(" (")[0]}.' + pg[row.end(2):]; return True
    print('no answer row', absn); return False
for f in sorted(set(f for f, _ in WB.values())):
    s = open(H + f + '.html').read(); secs = re.split(r'(?=<section\b)', s); head, pages = secs[0], secs[1:]; free = FREE[f]
    for pre, (ff, add) in WB.items():
        if ff != f: continue
        for k in sorted([k for k in S if k[0] == pre], key=lambda k: int(k[1:])):
            i = int(k[1:]) + add
            cand = [i - 1] if pre == 'S' else [2 * i - 2, 2 * i - 1]
            need = 66 if len(S[k][2]) > 78 else 56   # measured box heights plus a margin
            ok = [x for x in cand if x < len(pages) and free[x] >= need]
            if not ok: later.setdefault(f, []).append((k, foot(pages[cand[0]]))); continue
            x = ok[0]; free[x] -= need
            q = f'<div class="sq"><b>Remember the story?</b><span>{S[k][2]}<em></em></span></div>'
            m = re.search(r'<p class="rem2">.*?</p>', pages[x], re.S)
            pages[x] = pages[x][:m.end()] + q + pages[x][m.end():]; nq += 1
            add_answer(pages, foot(pages[x]), S[k][3])
    for k, pgn in later.get(f, []):
        r = [j for j, pg in enumerate(pages) if re.search(r'<div class="kick">[^<]*· Review</div>', pg)]
        if not r: print('no review page', f, k); continue
        j = r[0]
        if 'sqr"' not in pages[j]:
            n = len(re.findall(r'<span class="en">', pages[j])) + 1
            box = f'<div class="ex2 sqr"><div class="eh"><span class="en">{n}</span><b>Remember the stories?</b><span class="el">★<span class="so">★★</span></span></div><p class="how">Each story is in its chapter of the Handbook and in Read &amp; listen.</p></div>'
            pages[j] = re.sub(r'(</div>)(\s*<div class="sign">)', lambda m: box + m.group(1) + m.group(2), pages[j], count=1)
        pages[j] = pages[j].replace('Read &amp; listen.</p>', f'Read &amp; listen.</p><div class="sqi">{S[k][2]}<em></em></div>', 1) if False else re.sub(r'(<div class="ex2 sqr">.*?</p>)((?:<div class="sqi">.*?</div>)*)', lambda m: m.group(1) + m.group(2) + f'<div class="sqi"><span>{S[k][2]}</span><em></em></div>', pages[j], count=1, flags=re.S)
        add_answer(pages, foot(pages[j]), S[k][3]); nq += 1
    s = ''.join([head] + pages); s = s.replace('</style></head>', CSS + '</style></head>', 1) if '.sq{' not in s else s
    open(H + f + '.html', 'w').write(s)
print('storyrecall bubbles', nb, 'questions', nq, 'in story rounds', {f: [k for k, _ in v] for f, v in later.items()})
