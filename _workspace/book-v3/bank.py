# The Piano Butler activity bank: standalone, tagged rhythm activities that can be mixed into any book later,
# with some marked as free printables. Output: a catalogue PDF (auto-paginated), a metadata JSON, and free one-page sheets.
import json
exec(open('/tmp/claude-0/pk/wbtime2.py').read())   # helpers: gcell, gin, tbl, bars, ticks, BOX, LINE, staff, FF, css, W ...
BS = json.load(open('/tmp/claude-0/vrv/bout.json')); W.update(BS)
def bx(k, h=72, cap=''):
    svg = BS[k].replace('<svg ', '<svg style="max-height:%dpx" ' % h, 1)
    return '<figure class="vx"><div class="vs">' + svg + '</div>' + ('<figcaption>' + cap + '</figcaption>' if cap else '') + '</figure>'
def tile(k, h=46): return f'<span class="tile">{gcell("n", k, h) if not k.startswith("r") else gcell("r", k[1:], h)}</span>'
TYPES = {'body': 'At the piano', 'puzzle': 'Puzzle', 'write': 'Write it', 'find': 'Find and fix', 'listen': 'Listen', 'make': 'Make your own', 'piece': 'Your music', 'challenge': 'Challenge'}
A = []
def act(id_, step, level, stars, typ, title, how, body, answer='', free=False):
    A.append(dict(id=id_, topic='Rhythm', step=step, level=level, stars=stars, type=typ, title=title, how=how, body=body, answer=answer, free=free))
STEPS = {1: 'Feel the beat', 2: 'Crotchets and crotchet rests', 3: 'Minims and semibreves'}

# ---------- Step 1 · Feel the beat ----------
act('R1-01', 1, 'Level 0', 1, 'body', 'Beat or rhythm?', 'Play any piece (or listen to one). Tap your foot on the beat and clap the rhythm of the tune. Then swap: clap the beat, tap the rhythm.',
    '<div class="tickrow"><span>Foot beat, hands rhythm</span>' + ticks(3) + '</div><div class="tickrow"><span>Hands beat, foot rhythm</span>' + ticks(3) + '</div>', free=True)
act('R1-02', 1, 'Level 0', 1, 'puzzle', 'Slow to fast', 'Number the metronome marks from the slowest (1) to the fastest (4).',
    '<div class="mm4">' + ''.join(f'<div><span class="mmk">{gin("n", "c")} = {v}</span>{BOX}</div>' for v in (120, 60, 92, 76)) + '</div>', '60, 76, 92, 120', free=True)
act('R1-03', 1, 'Level 0', 1, 'write', 'Strong beats', 'Each dot is one beat. Circle the strong beat in every bar; in 4/4, also underline the medium beat.', beats_row('2/4', 2) + beats_row('3/4', 3) + beats_row('4/4', 4), 'beat 1 of every bar; in 4/4 also beat 3')
act('R1-04', 1, 'Level 0', 2, 'listen', 'Two, three or four?', 'Someone plays a piece, or a march, a waltz and a song online. Count along and decide how many beats are in each bar.',
    tbl(['Music', 'Beats in a bar'], [[LINE, '2 · 3 · 4'], [LINE, '2 · 3 · 4'], [LINE, '2 · 3 · 4']], ['60%', '40%']))
act('R1-05', 1, 'Level 0', 2, 'challenge', 'Tempo ladder', 'Clap the line while counting aloud. Tick a step each time it is steady, then move the metronome up.',
    bx('b_lad', 66) + '<div class="lad">' + ''.join(f'<div><b>{gin("n", "c")} = {v}</b>{ticks(3)}</div>' for v in (60, 72, 84, 96, 108)) + '</div>', free=True)
act('R1-06', 1, 'Level 0', 1, 'body', 'Walk the beat', 'Set the metronome to ♩ = 80. Walk one step on every beat, saying the counts. Stop on beat 1 when someone says “freeze”.',
    '<div class="tickrow"><span>2/4 (left, right)</span>' + ticks(3) + '</div><div class="tickrow"><span>3/4 (a step and a sway)</span>' + ticks(3) + '</div><div class="tickrow"><span>4/4</span>' + ticks(3) + '</div>')

# ---------- Step 2 · Crotchets and crotchet rests ----------
words = [('tea', ['c']), ('cof-fee', ['q', 'q']), ('juice', ['c']), ('le-mon-ade', ['q', 'q', 'c'])]
act('R2-01', 2, 'Level 0', 1, 'write', 'Count it', 'Write a count in every box. Count the rests too: they are beats of silence.', bx('b_cnt1', 80), '1 2 3 4 · 1 2 3 4 (rests on 1 and 3)')
act('R2-02', 2, 'Level 0', 1, 'body', 'Clap and open', 'Clap on every crotchet; open your hands wide on every rest. Count aloud.', bx('b_cl1', 64) + bx('b_cl3', 64) + ticks(), free=True)
act('R2-03', 2, 'Level 0', 2, 'listen', 'Which did you hear?', 'Someone claps one rhythm from the row. Circle A, B or C. Then swap roles.', opts(('b_h1', 'b_h2', 'b_h3'), 54), '')
act('R2-04', 2, 'Level 0', 2, 'write', 'Finish with rests', 'Each bar is short. Complete it with crotchet rests (draw as many as you need).',
    grid([f'<div class="fc">{bx(k, 60)}<div class="add">rests {BOX}</div></div>' for k in ('b_fr1', 'b_fr2', 'b_fr3', 'b_fr4')], 4), '1 · 1 · 2 · 1 crotchet rests')
act('R2-05', 2, 'Level 0', 1, 'body', 'Rhythm echo', 'Someone claps one bar of crotchets and rests; you clap it straight back without a pause. Colour a square for every echo that is exactly right.',
    '<div class="sq10">' + '<i></i>' * 10 + '</div>', free=True)
act('R2-06', 2, 'Level 0', 2, 'make', 'Rest patterns', 'Make four different bars of 4/4 using crotchets and crotchet rests. No two the same. Clap each one.', staff('4/4', 4))
act('R2-07', 2, 'Level 0', 3, 'challenge', 'Two hands', 'Right hand plays the top line on one key, left hand the bottom line on another. Slowly, then faster.',
    bx('b_cl1', 60, 'right hand') + bx('b_cl2', 60, 'left hand') + ticks())

# ---------- Step 3 · Minims and semibreves ----------
act('R3-01', 3, 'Level 0', 1, 'write', 'Count it', 'Write a count in every box: the beat you play, then the beats you hold.', bx('b_cnt2', 84), '1–2 3 4 · 1–2–3–4 · 1 2–3 4')
act('R3-02', 3, 'Level 0', 1, 'puzzle', 'Balance the scales', 'Write one note on the right so both sides last the same.',
    '<div class="bal">' + ''.join(f'<div class="bl2"><span class="pan">{"".join(gin("n", k, 30) for k in L)}</span><span class="eq">=</span><span class="pan">{BOX}</span></div>' for L in (['c', 'c'], ['m', 'm'], ['m', 'c', 'c'], ['c', 'c', 'c', 'c'])) + '</div>',
    'minim · semibreve · semibreve · semibreve', free=True)
cards = ['sb', 'm', 'm', 'c', 'c', 'c', 'c', 'rc']
act('R3-03', 3, 'Level 0', 2, 'puzzle', 'Rhythm dominoes', 'Use the cards to fill one bar of 4/4 exactly (4 beats). How many different ways can you find? Write each way by drawing the notes.',
    '<div class="tiles">' + ''.join(tile(k) for k in cards) + '</div>' + '<div class="ways">' + ''.join(f'<div><span class="wn">{i}</span><span class="al"></span></div>' for i in range(1, 7)) + '</div>',
    'e.g. semibreve · two minims · minim + two crotchets · four crotchets · minim + crotchet + crotchet rest …', free=True)
hunt = [['m', 'm'], ['m', 'c'], ['sb'], ['c', 'c', 'm'], ['m', 'c', 'c', 'c'], ['c', 'm', 'c'], ['c', 'c', 'c'], ['sb', 'c'], ['c', 'c', 'c', 'c']]
act('R3-04', 3, 'Level 0', 2, 'puzzle', 'Full bar hunt', 'Colour every box that holds exactly four beats.',
    '<div class="hunt">' + ''.join('<div class="hb">' + ''.join(gin('n', k, 30) for k in b) + '</div>' for b in hunt) + '</div>', 'boxes 1, 3, 4, 6, 9', free=True)
act('R3-05', 3, 'Level 0', 2, 'find', 'Rhythm detective', 'Each line has one bar with the wrong number of beats. Circle it and fix it.', bx('b_det1', 66) + bx('b_det2', 66), 'line 1: bar 2 (5 beats) · line 2: bar 3 (3 beats)')
act('R3-06', 3, 'Level 0', 2, 'listen', 'Short or long?', 'Someone claps one rhythm from the row. Circle A, B or C.', opts(('b_h4', 'b_h5', 'b_h6'), 54))
act('R3-07', 3, 'Level 0', 3, 'make', 'Question and answer', 'The first two bars ask a question. Write two bars that answer it, ending on a long note. Play it on one key.', bx('b_qa', 64, 'question') + staff('4/4', 2))
act('R3-08', 3, 'Level 0', 1, 'piece', 'In your music', 'Find these in a piece you are learning.', piece(['a minim', 'a semibreve', 'a crotchet rest', 'a bar of four crotchets']))
act('R3-09', 3, 'Level 0', 1, 'body', 'Clap and count', 'Clap and count each line, holding your hands together through the long notes.', bx('b_m1', 64) + bx('b_m2', 64) + ticks(), free=True)

# ---------- render: catalogue (auto-paginated in the browser) ----------
def card(a, show_free=True):
    tags = f'<span class="tg">{STEPS[a["step"]]}</span><span class="tg">{a["level"]}</span><span class="tg">{TYPES[a["type"]]}</span>' + ('<span class="tg fr">Free printable</span>' if a['free'] and show_free else '') + f'<span class="tg id">{a["id"]}</span>'
    return f'''<div class="ex2 card"><div class="eh"><b>{a["title"]}</b><span class="el">{star(a["stars"])}</span></div><div class="tags">{tags}</div><p class="how">{a["how"]}</p>{a["body"]}</div>'''
blocks = []
for st in (1, 2, 3):
    blocks.append(f'<div class="sthead"><div class="kick">Rhythm · Step {st}</div><h2>{STEPS[st]}</h2></div>')
    blocks += [card(a) for a in A if a['step'] == st]
ansT = tbl(['Activity', 'Answer'], [[f'<b>{a["id"]}</b> {a["title"]}', a['answer']] for a in A if a['answer']], ['36%', '64%'], 'ansT')
blocks.append('<div class="sthead"><div class="kick">Rhythm · Steps 1–3</div><h2>Answers</h2></div>' + ansT)
HEAD = '<div class="top"><span>PIANO BUTLER · ACTIVITY BANK</span><span>RHYTHM</span></div><div class="rule"></div>'
JS = '''<script>
(function(){const src=document.getElementById('src'),out=document.getElementById('out');const kids=[...src.children];let n=0,pg,body;
function newPage(){n++;pg=document.createElement('section');pg.className='pg';pg.innerHTML=HEAD+'<div class="body"></div><div class="foot"><span>'+n+'</span></div>';out.appendChild(pg);body=pg.querySelector('.body');}
newPage();const LIM=1123-80;
kids.forEach(k=>{body.appendChild(k);if(body.getBoundingClientRect().bottom-pg.getBoundingClientRect().top>LIM && body.children.length>1){newPage();body.appendChild(k);}
 if(k.classList.contains('sthead')){}});
// keep a step heading with its first card
document.querySelectorAll('.pg .body').forEach(b=>{const l=b.lastElementChild;if(l&&l.classList.contains('sthead')){const nx=b.closest('.pg').nextElementSibling;if(nx)nx.querySelector('.body').prepend(l);}});
src.remove();})();
</script>'''.replace('HEAD+', json.dumps(HEAD) + '+')
css += f'''
.card{{margin-top:14px}} .tags{{display:flex;flex-wrap:wrap;gap:6px;margin:3px 0 2px}} .tg{{font-size:10.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:{MUTE};border-bottom:1px solid #d9d4c6}} .tg.fr{{color:{C};border-color:{C}}} .tg.id{{margin-left:auto;color:#b0b2cc}}
.sthead{{margin-top:22px}} .sthead:first-child{{margin-top:0}} .sthead h2{{font-family:'PF',Georgia,serif;font-size:30px;margin:2px 0 0}}
.tickrow{{display:flex;align-items:center;justify-content:space-between;border-bottom:.6px solid #e2ddd0;padding:6px 0;font-size:15px}} .tickrow .tk{{margin:0}}
.lad{{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:6px}} .lad>div{{border:1px solid #e2ddd0;background:#fff;padding:8px;text-align:center}} .lad b{{display:block;font-size:14px;margin-bottom:4px}} .lad .tk{{justify-content:center;gap:5px}} .lad .tk i{{width:18px;height:18px}}
.sq10{{display:grid;grid-template-columns:repeat(10,1fr);gap:8px}} .sq10 i{{aspect-ratio:1;border:1.6px solid {N_};display:block}}
.bal{{display:grid;grid-template-columns:1fr 1fr;gap:10px 30px}} .bl2{{display:flex;align-items:center;gap:14px;border-bottom:.6px solid #e2ddd0;padding:6px 0}} .pan{{flex:1;display:flex;justify-content:center;align-items:center;gap:4px;border-bottom:3px solid {N_};padding:4px 0;min-height:44px}} .eq{{font-weight:700;font-size:20px}}
.tiles{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:8px}} .tile{{width:58px;height:72px;border:1.6px solid {N_};border-radius:6px;background:#fff;display:flex;align-items:center;justify-content:center}}
.ways{{display:grid;grid-template-columns:1fr 1fr;gap:6px 24px}} .ways>div{{display:flex;align-items:flex-end;gap:8px}} .wn{{font-weight:700;color:{C}}} .ways .al{{flex:1;height:34px}}
.hunt{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}} .hb{{border:1.6px solid {N_};background:#fff;min-height:58px;display:flex;align-items:center;justify-content:center;gap:4px}}
'''
cat = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body><div id="out"></div><div id="src" style="width:678px">{"".join(blocks)}</div>{JS}</body></html>'
open('/mnt/user-data/outputs/house-rooms/activity-bank-rhythm.html', 'w').write(cat)
json.dump([{k: v for k, v in a.items() if k not in ('body',)} for a in A], open('/mnt/user-data/outputs/house-rooms/activity-bank-rhythm.json', 'w'), ensure_ascii=False, indent=1)

# ---------- free printables: one activity per sheet, with brand and a link ----------
for a in A:
    if a['id'] in ('R2-04', 'R3-05'): a['free'] = True
FREE = [a for a in A if a['free']]
GROUPS = [('Feel the beat', ['R1-01', 'R1-02', 'R1-05']), ('Crotchets and rests', ['R2-02', 'R2-04', 'R2-05']), ('Long notes', ['R3-02', 'R3-04', 'R3-09']), ('Rhythm puzzles', ['R3-03', 'R3-05'])]
BY = {a['id']: a for a in A}
def sheet(title, ids):
    acts = [BY[i] for i in ids]
    body = ''.join(f'''<div class="ex2 card"><div class="eh"><span class="en">{k + 1}</span><b>{a["title"]}</b><span class="el">{star(a["stars"])}</span></div><p class="how">{a["how"]}</p>{a["body"]}</div>''' for k, a in enumerate(acts))
    answers = ' · '.join(f'{k + 1}: {a["answer"]}' for k, a in enumerate(acts) if a['answer'])
    lvl = acts[0]['level']
    return f'''<section class="pg free"><div class="top"><span>PIANO BUTLER · FREE PRINTABLE</span><span>RHYTHM · {lvl.upper()}</span></div><div class="rule"></div>
<div class="body"><div class="kick">Free rhythm sheet</div><h1>{title}</h1>{body}{('<div class="fans"><span class="gl">Answers</span> ' + answers + '</div>') if answers else ''}</div>
<div class="ffoot"><span class="bw">{bowtie_svg}</span><span>More activities, the Handbook and the online rooms at <b>thepianobutler.com</b></span><span>Free for personal and classroom use. Share the link, not the file. © Piano Butler</span></div></section>'''
bowtie_svg = f'<svg viewBox="0 0 40 24" style="width:34px;height:20px"><path d="M2 3 L18 12 L2 21 Z" fill="none" stroke="{N_}" stroke-width="2" stroke-linejoin="round"/><path d="M38 3 L22 12 L38 21 Z" fill="none" stroke="{N_}" stroke-width="2" stroke-linejoin="round"/><circle cx="20" cy="12" r="2.6" fill="{C}"/></svg>'
fcss = css + f'''.fans{{margin-top:16px;font-size:11.5px;color:{MUTE};transform:rotate(180deg);text-align:right}} .free .card{{margin-top:16px}} .ffoot{{position:absolute;left:58px;right:58px;bottom:34px;display:flex;align-items:center;gap:12px;border-top:1.5px solid {N_};padding-top:10px;font-size:12px;color:#3d4080}} .ffoot span:last-child{{margin-left:auto;color:{MUTE};font-size:10.5px}}'''
open('/mnt/user-data/outputs/house-rooms/free-printables-rhythm.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{fcss}</style></head><body>{"".join(sheet(t, ids) for t, ids in GROUPS)}</body></html>')
print('ok', len(A), 'activities,', len(FREE), 'free')
