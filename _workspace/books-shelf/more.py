# Books - latest: the rest of what has been made goes on the top shelf too (her 27 Nov: "연습노트 만든 것까지 다 넣어줘").
# Adds four books after Handbook, Workbook, Music Box, Note Writer: Practice Diary (free), Games, Level books, More.
# Safe to run again: it replaces its own block (between the more-books markers) and its own top-shelf buttons.
import os,re,shutil,subprocess,glob,html
ROOT=os.path.expanduser('~/mnt/Piano Butler'); B=ROOT+'/Claude outputs/Books - latest'; TH=B+'/_thumbs'
def pages(f):
    try: return int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',f],capture_output=True,text=True).stdout).group(1))
    except Exception: return 0
def thumb(pdf,name):
    out=f'{TH}/{name}.jpg'
    if not os.path.exists(out) or os.path.getmtime(out)<os.path.getmtime(pdf):
        subprocess.run(['pdftoppm','-jpeg','-r','42','-f','1','-l','1','-singlefile',pdf,out[:-4]],capture_output=True)
    return f'_thumbs/{name}.jpg'
def put(src,dst):
    os.makedirs(os.path.dirname(dst),exist_ok=True)
    if not os.path.exists(dst) or os.path.getmtime(dst)<os.path.getmtime(src): shutil.copy2(src,dst)
E_=html.escape
def card(rel,topic,title,note,tid):
    f=B+'/'+rel; n=pages(f); t=thumb(f,tid)
    return (f'<div class="card"><a class="sheet" href="{E_(rel)}" target="_blank"><img src="{t}" alt="" loading="lazy"></a><div class="txt"><div class="topic">{E_(topic)}</div><h3>{E_(title)}</h3><p>{E_(note)}</p>\n'
            f'<div class="foot"><span class="meta">{n} page{"s" if n!=1 else ""}</span><a class="btn" href="{E_(rel)}" target="_blank">Open</a></div></div></div>')
def series(sid,title,sub,lead,cards):
    return f'<section class="series" id="s-{sid}" hidden><div class="ph"><h2>{E_(title)}</h2><span class="whole">{E_(sub)}</span></div><p class="lead" style="margin:10px 0 22px">{E_(lead)}</p><div class="grid">{"".join(cards)}</div></section>'
def nice(fn): return fn[:-4].replace('-',' ').capitalize()
# ---- files
put(ROOT+'/books/practice-diary.pdf',B+'/7 Practice diary/practice-diary.pdf')
games=sorted(glob.glob(ROOT+'/printables/pdf/*.pdf'))
for g in games:
    if os.path.basename(g)!='practice-diary.pdf': put(g,B+'/3 Activities and games/sheets/'+os.path.basename(g))
pd=[card('7 Practice diary/practice-diary.pdf','Free','Practice diary','A lesson record for the week: what to practise, ticks for each day, scales and theory pages.','pd-diary')]
ag=[card('3 Activities and games/rhythm-activities-games.pdf','Book','Rhythm activities and games','','ag-rhythm'),card('3 Activities and games/pitch-games.pdf','Book','Pitch games','','ag-pitch')]
for g in sorted(glob.glob(B+'/3 Activities and games/sheets/*.pdf')):
    fn=os.path.basename(g); ag.append(card('3 Activities and games/sheets/'+fn,'Free sheet',nice(fn),'','ags-'+fn[:-4]))
lb=[]
for key,nm in (('beginner','Beginner'),('prelim','Prelim'),('grade1','Grade 1'),('grade2','Grade 2')):
    f=f'5 Level books/levelbook-{key}-draft.pdf'
    if os.path.exists(B+'/'+f): lb.append(card(f,'Level book',nm,'Draft','lb-'+key))
films=sorted(glob.glob(B+'/5 Level books/*.mp4'))+sorted(glob.glob(B+'/5 Level books/films/*.mp4'))
filmlinks=''.join(f'<a href="{E_(os.path.relpath(f,B))}" target="_blank">{E_(nice(os.path.basename(f)))} (film)</a>' for f in films)
xx=[]
for f,topic,title,note,tid in (('Whole books (later)/scales-and-chords-book-1-letter-version.pdf','Book','Scales and Chords, Book 1','Pieces 0 to 12: major scales, harmonic minors, thirds, major and minor chords, I IV V. Ends with the letter to play. Waiting for your check.','xx-scalesL1'),
    ('Whole books (later)/scales-and-chords-book-2-letter-version.pdf','Book','Scales and Chords, Book 2','Pieces 13 to 22: natural and melodic minor, diminished, augmented, sevenths, words that are chords. Waiting for your check.','xx-scalesL2'),
    ('Whole books (later)/the-letter-on-one-page.pdf','Story','The letter, on one page','The story thread in one page: what it is, what each part gives back, three rules.','xx-story'),
    ('Whole books (later)/claras-letter-draft.pdf','Story','Clara’s Letter (for your decision)','The letter after each part, with its one moment. 12 pages.','xx-letterpack'),
    ('Where do I start - the Handbook check.pdf','Free','Where do I start? The Handbook check','A short check that points to the right part of the Handbook.','xx-check')):
    if os.path.exists(B+'/'+f): xx.append(card(f,topic,title,note,tid))
# her 27 Nov: "안쓰고 있는거 따로 모아서": everything made and no longer in use, in one place; nothing is deleted
old=[]
for f,topic,title,note,tid in (('Whole books (later)/scale-and-chord-book-draft.pdf','Replaced','Scales and Chords, Book 1 (Secret Files)','The first frame. Replaced by the letter version.','xx-scales'),
    ('Whole books (later)/scale-and-chord-book-2-draft.pdf','Replaced','Scales and Chords, Book 2 (Secret Files)','The first frame. Replaced by the letter version.','xx-scales2'),
    ('Whole books (later)/accompaniment-book-levels-1-3.pdf','Replaced','Accompaniment book, Levels 1 to 3','The Music Box grew out of this book.','xx-accomp'),
    ('Whole books (later)/music-box-songs-draft.pdf','Replaced','Music Box songs (first draft)','Before Music Box 1, 2 and 3.','old-mb0'),
    ('Whole books (later)/music-box-songs-1-12-draft.pdf','Replaced','Music Box songs 1 to 12 (draft)','Before Music Box 1, 2 and 3.','old-mb12'),
    ('Whole books (later)/music-box-songs-1-11-draft.pdf','Replaced','Music Box songs 1 to 11 (draft)','Before Music Box 1, 2 and 3.','old-mb11'),
    ('Whole books (later)/music-box-songs-1-9-draft.pdf','Replaced','Music Box songs 1 to 9 (draft)','Before Music Box 1, 2 and 3.','old-mb9')):
    if os.path.exists(B+'/'+f): old.append(card(f,topic,title,note,tid))
old+=[c.replace('<div class="topic">Level book</div>','<div class="topic">Paused</div>') for c in lb]
def door(href,title,what,state):
    return (f'<div class="card"><div class="txt" style="border:1.5px solid var(--navy);border-radius:10px;padding:16px 16px 14px;background:#fffefa"><div class="topic">{E_(state)}</div><h3>{E_(title)}</h3><p>{E_(what)}</p>'
            f'<div class="foot"><span class="meta">opens in the browser</span><a class="btn" href="{E_(href)}" target="_blank">Open</a></div></div></div>')
sc=[door('../../books/read/lesson.html#P1','The picture lesson','Clara and the Butler talk; a picture moves with every line. All parts.','In review · not linked on the site yet'),
    door('../../drills.html?view=home&pics=pitch','The Library picture books','82 short moving pictures, by part. No sound.','Live'),
    door('../../drills.html','The house (drills)','A room for every chapter: lesson, Workbook pages and drills.','Live'),
    door('../../musicbox.html','The Music Box (play along)','Listen, follow the lit notes, then play with the backing.','Live')]
web=''
STYLE=('<style>.shelf.top{grid-template-columns:repeat(5,minmax(0,1fr));gap:22px}@media (max-width:760px){.shelf.top{grid-template-columns:repeat(3,minmax(0,1fr))}}'
       '.st{display:inline-block;margin-top:5px;font:800 10.5px Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:2px 9px;align-self:flex-start}'
       '.st-ready{background:#2b6e56;color:#fff}.st-review{background:#fde3d8;color:#b8421f}.st-draft{background:#e4e6f3;color:#26296b}'
       '.legend{font-size:13px;color:var(--muted);margin:10px 0 0}.legend .st,.legend .now{margin:0 4px 0 12px}'
       '.st-old{background:#e9e6dc;color:#6b6259}.now{display:inline-block;margin-top:5px;font:800 10.5px Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:2px 9px;align-self:flex-start;background:#e4572e;color:#fff;font-style:normal}'
       '.book.top.isold{opacity:.62}.book.top.isold:hover{opacity:1}'
       '.nowbox{border:2px solid #26296b;border-radius:12px;background:#fffefa;padding:14px 20px;margin:14px 0 6px;max-width:860px}.nowbox>b{font:800 12px Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#e4572e}.nowbox ol{margin:6px 0 4px;padding-left:20px;font-size:15px;line-height:1.55;color:#26296b}.nowbox p{margin:0;font-size:13px;color:var(--muted)}</style>')
block=('<!--more-books:start-->'+series('pd','The Practice Diary','free · for every lesson','The lesson record book: one page a week.',pd)
       +series('ag','Activities and games',f'2 books · {len(ag)-2} free sheets','Games and activity sheets for rhythm and pitch.',ag)
       +series('xx','Scales and Chords, and more',f'{len(xx)} books','The two Scale and Chord books, the letter story on one page, and the Handbook check.',xx)
       +series('sc','On screen','4 doors · open in the browser','Everything that is used on a screen, not printed.',sc)
       +series('old','Older versions',f'{len(old)} items · not in use','Made earlier and not used now: replaced versions and paused drafts. Kept here so nothing is lost. Tell Claude which ones to delete.',old).replace('</section>',(f'<h3 style="margin:26px 0 8px">Level book films (paused)</h3><div class="nwl">{filmlinks}</div>' if filmlinks else '')+'</section>')+STYLE+'<!--more-books:end-->')
BOW=lambda c: f'<span class="bw"><svg viewBox="0 0 40 24" width="34" height="20"><path d="M2 3 L18 12 L2 21 Z" fill="none" stroke="{c}" stroke-width="2" stroke-linejoin="round"/><path d="M38 3 L22 12 L38 21 Z" fill="none" stroke="{c}" stroke-width="2" stroke-linejoin="round"/><circle cx="20" cy="12" r="2.6" fill="#e4572e"/></svg></span>'
def top(sid,cls,kick,title,blurb,cap,sub,size=''):
    ink='#26296b' if cls=='wb' else '#fffdf7'
    return (f'<button type="button" class="book top" data-series="{sid}" aria-expanded="false"><span class="cv {cls}"><span class="fr"><span class="se">The Piano Butler</span><span class="ki" style="color:{"#e4572e" if cls=="wb" else "#f4a9bb"}">{kick}</span>'
            f'<span class="ti"{size}>{title}</span><span class="dv"></span><span class="bl">{blurb}</span>{BOW(ink)}</span></span><span class="cap"><b>{cap}</b><span>{sub}</span></span></button>')
tops=('<!--more-tops:start-->'+top('pd','wb','Free','Diary','The lesson record: what to practise this week','The Practice Diary','free · tap to open')
      +top('ag','wb','Play','Games','Rhythm and pitch games, and the free sheets','Activities and games',f'{len(ag)} items · tap to open')
      +top('xx','hb','Technique','Scales &amp; Chords','Books 1 and 2, the letter story, the Handbook check','Scales and Chords, and more',f'{len(xx)} books · tap to open',' style="font-size:9cqw"')
      +top('sc','wb','On screen','Screen','The picture lesson, picture books, the house, the Music Box','On screen','4 doors · tap to open')
      +top('old','wb','Not in use','Older','Replaced versions and paused drafts, kept in one place','Older versions',f'{len(old)} items · tap to open').replace('class="book top"','class="book top isold"')+'<!--more-tops:end-->')
p=B+'/index.html'; s=open(p).read(); (os.path.exists(p+'.bak-more') or shutil.copy2(p,p+'.bak-more'))
s=re.sub(r'<!--more-books:start-->.*?<!--more-books:end-->','',s,flags=re.S); s=re.sub(r'<!--more-tops:start-->.*?<!--more-tops:end-->','',s,flags=re.S)
i=s.index('<section class="series" id="s-hb"'); j=s.rindex('</div>',0,i); assert s[:j].rstrip().endswith('</button>'), 'top shelf not where expected'
s=s[:j]+tops+s[j:]
# the chip rows that the new shelf books replace go; other rows (Music Box, next books) stay
for head in ('Where do I start?','New books','Level books (older drafts)','Activities and games'):
    s=re.sub(r'<div class="more"><b>'+re.escape(head)+r'</b>.*?</div>\n?','',s,count=1,flags=re.S)
k=s.find('<div class="more">')
if k<0: k=s.rindex('</div>',0,s.rindex('<script'))   # inside the page wrap
s=s[:k]+block+'\n'+s[k:]
STATE={'hb':('review','In review'),'wb':('review','In review'),'mb':('draft','Draft'),'nw':('review','In review'),'pd':('ready','Ready'),'ag':('ready','Ready'),'xx':('review','In review'),'sc':('review','Live · lesson in review'),'old':('old','Not in use')}
NOW={'hb':'Now · your review','sc':'Now · your review','wb':'Now · your review','xx':'Now · your check','mb':'Now · other window','nw':'Now · other window'}
s=re.sub(r'<i class="st st-[a-z]+">[^<]*</i>','',s); s=re.sub(r'<i class="now">[^<]*</i>','',s); s=re.sub(r'<p class="legend">.*?</p>','',s,flags=re.S); s=re.sub(r'<!--now:start-->.*?<!--now:end-->','',s,flags=re.S)
for sid,(cls,lab) in STATE.items():
    m=re.search(r'<button type="button" class="book top[a-z ]*" data-series="'+sid+r'".*?</button>',s,flags=re.S)
    if not m: continue
    b=m.group(0); q=b.rindex('</span></button>'); b2=b[:q]+f'<i class="st st-{cls}">{lab}</i>'+(f'<i class="now">{NOW[sid]}</i>' if sid in NOW else '')+b[q:]
    s=s.replace(b,b2,1)
LEG=('<!--now:start--><div class="nowbox"><b>Working on now</b><ol><li><b>Your review, part by part:</b> the Handbook beside the picture lesson (On screen), then the Workbook. Start with Pitch.</li><li><b>Scales and Chords, Books 1 and 2:</b> drafts finished, waiting for your check (this window).</li><li><b>Music Box 1, 2, 3:</b> being made (Music Box window).</li><li><b>Note Writer:</b> being made (Note Writer window).</li></ol><p>Everything else is finished, or put away under Older versions.</p></div><!--now:end-->'
     '<p class="legend"><i class="now">Now</i>being worked on<i class="st st-ready">Ready</i>finished<i class="st st-review">In review</i>built, being checked<i class="st st-draft">Draft</i>not finished<i class="st st-old">Not in use</i>put away</p>')
q=s.index('<div class="shelf top">'); s=s[:q]+LEG+s[q:]
open(p,'w').write(s); print('top books',len(re.findall(r'class="book top',s)),'| diary',len(pd),'| games',len(ag),'| more',len(xx),'| older',len(old),'| films',len(films))
