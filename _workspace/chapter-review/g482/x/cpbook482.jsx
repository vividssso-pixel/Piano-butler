// ─── Phase 482: chapter 26, Composers through Time: its composers, the who's who of each period, and the Lesson Book
// (page 1 the timeline; pages 2 to 5 the periods; page 6 who lived when; page 7 the five checks) ───
const CPX_PAGES = [
  { era: 'baroque', ids: ['vivaldi', 'bach', 'handel', 'scarlatti'], from: 1670, to: 1770 },
  { era: 'classical', ids: ['haydn', 'clementi', 'mozart', 'beethoven'], from: 1725, to: 1840 },
  { era: 'romantic', ids: ['schubert', 'chopin', 'rschumann', 'liszt', 'cschumann', 'brahms', 'tchaikovsky'], from: 1790, to: 1910 },
  { era: 'modern', ids: ['debussy', 'joplin', 'bartok', 'prokofiev', 'kabalevsky', 'sculthorpe', 'williams', 'hisaishi'], from: 1855, to: MTL_NOW },
];
const CPX_IDS = CPX_PAGES.flatMap(p => p.ids);
// where each one lived, in short (a country, then a city), and one piece (from Phase 305's checked lists)
const CPX_FROM = { vivaldi: ['Italy', '이탈리아'], bach: ['Germany', '독일'], handel: ['Germany, then London', '독일, 그 후 런던'], scarlatti: ['Italy, then Lisbon and Madrid', '이탈리아, 그 후 리스본과 마드리드'],
  haydn: ['Austria', '오스트리아'], clementi: ['Italy, then London', '이탈리아, 그 후 런던'], mozart: ['Austria', '오스트리아'], beethoven: ['Germany, then Vienna', '독일, 그 후 빈'],
  schubert: ['Austria', '오스트리아'], chopin: ['Poland, then Paris', '폴란드, 그 후 파리'], rschumann: ['Germany', '독일'], liszt: ['Hungary', '헝가리'], cschumann: ['Germany', '독일'], brahms: ['Germany, then Vienna', '독일, 그 후 빈'], tchaikovsky: ['Russia', '러시아'],
  debussy: ['France', '프랑스'], joplin: ['USA', '미국'], bartok: ['Hungary', '헝가리'], prokofiev: ['Russia', '러시아'], kabalevsky: ['Russia', '러시아'], sculthorpe: ['Australia', '호주'], williams: ['USA', '미국'], hisaishi: ['Japan', '일본'] };
// Schubert's piece is from 1822 (Romantic years); Robert Schumann's is the set students play (and the one the app plays)
const CPX_PIECE = { vivaldi: ['The Four Seasons', '사계'], bach: ['The Well-Tempered Clavier', '평균율 클라비어곡집'], handel: ['Messiah', '메시아'], scarlatti: ['555 keyboard sonatas', '건반 소나타 555곡'],
  haydn: ['the “Surprise” Symphony', '“놀람” 교향곡'], clementi: ['Sonatinas, Op. 36', '소나티네 작품 36'], mozart: ['Eine kleine Nachtmusik', '아이네 클라이네 나흐트무지크'], beethoven: ['Für Elise', '엘리제를 위하여'],
  schubert: ['the “Unfinished” Symphony', '“미완성” 교향곡'], chopin: ['the “Minute” Waltz', '“강아지 왈츠”'], rschumann: ['Album for the Young, Op. 68', '어린이를 위한 앨범 작품 68'], liszt: ['“Liebestraum” No. 3', '“사랑의 꿈” 3번'], cschumann: ['Piano Concerto, Op. 7', '피아노 협주곡 작품 7'], brahms: ['Lullaby, Op. 49 No. 4', '자장가 작품 49-4'], tchaikovsky: ['The Nutcracker', '호두까기 인형'],
  debussy: ['“Clair de lune”', '“달빛”'], joplin: ['“The Entertainer”', '“엔터테이너”'], bartok: ['Mikrokosmos', '미크로코스모스'], prokofiev: ['Peter and the Wolf', '피터와 늑대'], kabalevsky: ['24 Pieces for Children', '어린이를 위한 24개의 소품'],
  sculthorpe: ['Kakadu', '카카두'], williams: ['Star Wars (film music)', '스타워즈(영화 음악)'], hisaishi: ['My Neighbor Totoro (film music)', '이웃집 토토로(영화 음악)'] };
const cpxYrs = (id) => { const [a, b] = mtlYears(id); return b > 2025 ? t(a + ' to today', a + '년부터 오늘날까지') : t(a + '–⁠' + b, a + '~⁠' + b); };
// Korean word pairs kept on one line
const cpxNbKo = (x) => typeof x !== 'string' ? x : chxNbKo(x).replace(/(바로크|고전주의|낭만주의) 시대/g, '$1 시대').replace(/(같은|한) (때|해|시기|세기)/g, '$1 $2')
  .replace(/그 후 /g, '그 후 ').replace(/작품 (\d+)/g, '작품 $1').replace(/건반 악기/g, '건반 악기').replace(/알베르티 베이스/g, '알베르티 베이스').replace(/어느 시대/g, '어느 시대')
  .replace(/곡 하나/g, '곡 하나').replace(/맨 (아래|위) 음/g, '맨 $1 음').replace(/듣는 곡/g, '듣는 곡').replace(/소나타 (\d+곡)/g, '소나타 $1').replace(/요\((\d+)챕터\)/g, '요⁠($1챕터)');
const cpxKoT = (x) => LANG === 'ko' ? cpxNbKo(x) : x;
const cpxItal = () => LANG === 'ko' ? 'normal' : 'italic';   // Hangul is never slanted

// the who's who of one period: each composer an entry (name and years; where; one piece). onTap makes each a button.
function CpxWho({ ids, onTap, sel, cols = 2, scr }) {
  return <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:scr ? '4px 16px' : '3px 22px',width:'100%',textAlign:'left'}}>
    {onTap && <style>{'.cpx-who:focus{outline:none}.cpx-who:focus-visible{outline:2px solid #e4572e;outline-offset:2px}'}</style>}
    {ids.map(id => { const c = cmpById(id), on = sel === id;
      const body = <><span style={{display:'block',fontSize:scr ? 15 : 14,fontWeight:900,color:on ? BK.coral : BK.ink,lineHeight:1.3,wordBreak:'keep-all'}}>{cmpT(c.name)} <span style={{fontWeight:700,fontSize:scr ? 13 : 12.5,color:on ? BK.coral : BK.muted,whiteSpace:'nowrap'}}>{mtlLife(c)}</span></span>
        <span style={{display:'block',fontSize:scr ? 13.5 : 12.5,color:BK.ink,lineHeight:1.35,wordBreak:'keep-all'}}>{cpxKoT(t(CPX_FROM[id][0], CPX_FROM[id][1]))} · <span style={{fontStyle:cpxItal()}}>{cpxKoT(t(CPX_PIECE[id][0], CPX_PIECE[id][1]))}</span></span></>;
      const line = { borderStyle:'solid', borderColor:'rgba(38,41,107,0.16)', borderWidth:'1px 0 0', borderRadius:0 };
      return onTap ? <button key={id} type="button" className="cpx-who" aria-pressed={on} onClick={() => onTap(id)} style={{...line,display:'flex',flexDirection:'column',justifyContent:'flex-start',alignItems:'stretch',minWidth:0,background:on ? 'rgba(228,87,46,0.07)' : 'transparent',textAlign:'left',font:'inherit',color:'inherit',cursor:'pointer',minHeight:44,padding:'5px 4px 3px',margin:0}}>{body}</button>
        : <div key={id} style={{...line,padding:'5px 0 3px',minWidth:0}}>{body}</div>; })}
  </div>;
}

function cpxLbPages(scr = false) {
  const ch = 'composers';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680, pad) => <LbPic h={h} pad={pad}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const X = (en, ko) => sscT(en, skgKo(cpxNbKo(ko)));
  const cap = (x, key = 'cap') => <div key={key} style={{textAlign:'center',fontSize:scr ? 14 : 13.5,fontWeight:800,color:BK.ink,margin:'2px auto 0',maxWidth:600,lineHeight:1.35,textWrap:'balance',wordBreak:'keep-all'}}>{cpxKoT(x)}</div>;
  const ch18 = bkChapterNo('piano-story'), ch27 = bkChapterNo('styles');
  const eraLabel = (k) => k === 3 ? t('Modern and Contemporary, 1900 to today', '근대와 현대, 1900년부터 오늘날까지') : cmpEraTag(CPX_PAGES[k].era) + ', ' + cpxYrs(CPX_PAGES[k].era);
  const lives = (ids) => ids.map(id => { const c = cmpById(id); return cmpT(c.name) + ', ' + mtlLife(c); }).join('; ');

  // p1 (macro first): the timeline of music, a lane per composer in the order they were born
  const p1 = <LbLive still={stack([<MusTimeline key="m" firstPiano stack fs={10.5} laneH={11.5} barH={7} guides label={t('The timeline of music, 1600 to today. Periods: Baroque 1600 to 1750, Classical 1750 to 1820, Romantic 1820 to 1900, Modern 1900 to 1950, Contemporary 1950 to today. Keyboards: the harpsichord, then the fortepiano from about 1770, then the piano from about 1830; the first piano in 1700. Composers: ' + CPX_IDS.length + ' lives in the order they were born, from Vivaldi, born 1678, to Hisaishi, born 1950. Sound and styles: chapter ' + ch27 + '.', '음악의 타임라인, 1600년부터 오늘날까지. 시대: 바로크 1600~1750, 고전주의 1750~1820, 낭만주의 1820~1900, 근대 1900~1950, 현대 1950~오늘날. 건반 악기: 하프시코드, 1770년쯤부터 포르테피아노, 1830년쯤부터 피아노. 첫 피아노는 1700년. 작곡가: 태어난 차례대로 ' + CPX_IDS.length + '명, 1678년에 태어난 비발디부터 1950년에 태어난 히사이시까지. 소리와 스타일은 ' + ch27 + '챕터.')}/>,
    cap(t('A composer’s period is when they wrote their music. The last two rows, sound and styles, are chapter ' + ch27 + '.', '작곡가의 시대는 곡을 쓴 때로 정해요. 아래 두 줄, 소리와 스타일은 ' + ch27 + '챕터에서 배워요.'))], 300, 6, 680, '10px 16px')} live={<MtlMapPad/>}/>;
  // p2 to p5: one period each: its stretch of the timeline, then its who's who
  const per = (k, capx) => { const P = CPX_PAGES[k];
    return stack([<MusTimeline key="t" big W={scr ? 680 : 590} from={P.from} to={P.to} rows={['era', 'keys', 'cmp']} ids={P.ids} firstPiano={k === 0} label={eraLabel(k) + ': ' + lives(P.ids) + '.'}/>,
      <CpxWho key="w" ids={P.ids}/>, cap(capx, 'c')], 360, 12); };
  const p2 = per(0, t('Bach, Handel and Scarlatti were all born in 1685. Their keyboard: the harpsichord.', '바흐, 헨델, 스카를라티는 모두 1685년에 태어났어요. 이들의 건반 악기는 하프시코드예요.'));
  const p3 = per(1, t('Haydn, Mozart and Beethoven all worked in Vienna. Their keyboard: the fortepiano.', '하이든, 모차르트, 베토벤은 모두 빈에서 활동했어요. 이들의 건반 악기는 포르테피아노예요.'));
  const p4 = per(2, t('Chopin and Robert Schumann were both born in 1810. Their keyboard: the piano.', '쇼팽과 로베르트 슈만은 둘 다 1810년에 태어났어요. 이들의 건반 악기는 피아노예요.'));
  const p5 = per(3, t('Five composers of the Modern period, three of the Contemporary period.', '근대의 작곡가 다섯 명, 현대의 작곡가 세 명.'));
  // p6: who lived when: Baroque to Romantic, a lane each, and a line down from 1785
  const p6ids = CPX_PAGES.slice(0, 3).flatMap(p => p.ids);
  const p6 = stack([<MusTimeline key="t" stack W={520} fs={11.5} laneH={19} barH={11} from={1670} to={1910} rows={['era', 'cmp']} ids={p6ids} year={1785} step={20} label={t('Fifteen lives from 1678 to 1897, Baroque to Romantic. A coral line down from 1785 crosses four of them: Haydn, Clementi, Mozart and Beethoven.', '1678년부터 1897년까지 열다섯 명의 생애, 바로크부터 낭만주의까지. 1785년에서 내려온 산호색 선이 네 명을 지나요: 하이든, 클레멘티, 모차르트, 베토벤.')}/>,
    cap(t('A line down from 1785 crosses four lives: Haydn, Clementi, Mozart and Beethoven were alive at the same time.', '1785년에서 내려온 선이 네 사람을 지나요: 하이든, 클레멘티, 모차르트, 베토벤은 같은 시기에 살았어요.'), 'c6')], 300, 12);

  // the check icons
  const R = (x, y, w, h, extra = '') => '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" ' + extra + '/>';
  const ic = {
    map: [{ k: 'raw', svg: [6, 24, 40, 56, 70].map((x, i, a) => R(x, 12, (a[i + 1] || 86) - x - 2, 14, 'fill="none" stroke="' + PEN_N + '" stroke-width="1.4"')).join('') + '<text x="46" y="38" text-anchor="middle" font-size="8" font-weight="800" fill="' + PEN_N + '">' + t('1600 → today', '1600 → 오늘날') + '</text>' }],
    keys: [{ k: 'raw', svg: [0, 1, 2, 3, 4, 5, 6].map(i => R(18 + i * 8, 8, 8, 24, 'fill="#fff" stroke="' + PEN_N + '" stroke-width="1.2"')).join('') + [0, 1, 3, 4, 5].map(i => R(23.5 + i * 8, 8, 5, 14, 'fill="' + PEN_N + '"')).join('') }],
    piece: [{ k: 'raw', svg: R(24, 4, 44, 32, 'fill="none" stroke="' + PEN_N + '" stroke-width="1.4"') + [12, 17, 22, 27].map(y => '<line x1="30" x2="62" y1="' + y + '" y2="' + y + '" stroke="' + PEN_N + '" stroke-width="0.8"/>').join('') + '<ellipse cx="44" cy="24" rx="3.6" ry="2.6" fill="' + PEN_C + '"/><line x1="47.3" x2="47.3" y1="24" y2="11" stroke="' + PEN_C + '" stroke-width="1.3"/>' }],
    alive: [{ k: 'raw', svg: [[4, 34, 10], [20, 62, 20], [38, 86, 30]].map(([a, b, y]) => R(a, y - 3, b - a, 6, 'rx="3" fill="' + (a < 46 && b > 46 ? PEN_C : PEN_N) + '"')).join('') + '<line x1="46" x2="46" y1="2" y2="38" stroke="' + PEN_C + '" stroke-width="1.8"/>' }],
    mine: [{ k: 'raw', svg: '<circle cx="30" cy="14" r="7" fill="none" stroke="' + PEN_N + '" stroke-width="1.5"/><path d="M17 36 Q30 20 43 36" fill="none" stroke="' + PEN_N + '" stroke-width="1.5"/><ellipse cx="62" cy="28" rx="4.2" ry="3" fill="' + PEN_C + '"/><line x1="66" x2="66" y1="28" y2="10" stroke="' + PEN_C + '" stroke-width="1.5"/><path d="M66 10 Q72 13 72 19" fill="none" stroke="' + PEN_C + '" stroke-width="1.5"/>' }],
  };
  const checksRows = [
    ['map', t('I can name the five periods in order, with their years', '다섯 시대의 이름과 연도를 차례대로 말할 수 있어요')],
    ['keys', t('I can name the keyboard of the Baroque, Classical and Romantic periods', '바로크, 고전주의, 낭만주의 시대의 건반 악기를 말할 수 있어요')],
    ['piece', t('I can name a composer and a piece from each period', '시대마다 작곡가 한 명과 그 작곡가의 곡 하나를 말할 수 있어요')],
    ['alive', t('I can find who was alive in a given year', '어느 해에 누가 살아 있었는지 찾을 수 있어요')],
    ['mine', t('I can say who wrote my piece, when they lived, and in which period', '내 곡을 누가 썼는지, 언제 살았는지, 어느 시대인지 말할 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(cpxNbKo(x))) : sscNbEn(x)]);
  const sayYears = (en, ko) => X(en + ' Say its composer and the years they lived.', ko + ' 작곡가 이름과, 그 작곡가가 언제부터 언제까지 살았는지 말해요.');

  const P = (k, kicker, era, pic, defs, steps, rem, pad) => <LbPage key={k} no={k} chId={ch} kicker={kicker} title={t(cmpEraTag(era) + ': ' + cpxYrs(era), cmpEraTag(era) + ': ' + cpxYrs(era))}>
    {live(pic, pad)}
    <LbDefs items={defs}/>
    <LbPiano steps={steps}/>
    <LbRemember>{rem}</LbRemember>
  </LbPage>;

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>곡을 쓰는 사람이 <b>작곡가</b>예요. 음악의 역사는 <b>시대</b>로 나눠요. 시대는 음악 양식이 비슷한 기간이에요.</> : <><b>Composers</b> write music. Music history is divided into <b>periods</b>: stretches of years whose music shares a style.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[cmpEraTag('baroque'), 2], [cmpEraTag('classical'), 3], [cmpEraTag('romantic'), 4], [t('Modern and Contemporary', '근대와 현대'), 5], [t('Who lived when', '누가 언제 살았을까'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',gap:8,fontSize:15,padding:'3px 0',borderBottom:'1px dotted rgba(38,41,107,0.3)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)',textWrap:'pretty'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    P(2, t('Step 1', '1단계'), 'baroque', p2, [
      [t('Baroque period', '바로크 시대'), X('The period from about 1600 to 1750.', '1600년쯤부터 1750년까지의 시대.')],
      [t('counterpoint', '대위법'), X('Two or more tunes at once, each as important as the other.', '두 개 이상의 선율을 똑같이 중요하게 동시에 엮는 것.')],
      [t('harpsichord', '하프시코드'), X('A keyboard whose strings are plucked. Pressing harder does not make it louder (chapter ' + ch18 + ').', '현을 뜯어 소리 내는 건반 악기. 세게 눌러도 소리가 커지지 않아요(' + ch18 + '챕터).')],
    ], [
      sayYears('Play a Baroque piece you know.', '아는 바로크 곡을 쳐요.'),
      X('Play a tune at one loudness, like a harpsichord. Then play it soft and loud, like a piano.', '선율을 하프시코드처럼 같은 세기로 쳐요. 그다음 피아노처럼 여리게, 세게 쳐요.'),
    ], X('Baroque: 1600 to 1750. Bach. The harpsichord.', '바로크: 1600~1750. 바흐. 하프시코드.'), <CpxPeriodPad k={0}/>),

    P(3, t('Step 2', '2단계'), 'classical', p3, [
      [t('Classical period', '고전주의 시대'), X('The period from about 1750 to 1820.', '1750년쯤부터 1820년까지의 시대.')],
      [t('fortepiano', '포르테피아노'), X('The early piano of Mozart’s time. It plays soft and loud (chapter ' + ch18 + ').', '모차르트 시대의 초기 피아노. 여리게도 세게도 칠 수 있어요(' + ch18 + '챕터).')],
      [t('Alberti bass', '알베르티 베이스'), X('A left-hand accompaniment that breaks a chord: lowest, highest, middle, highest.', '화음을 맨 아래 음, 맨 위 음, 가운데 음, 맨 위 음 순서로 펼쳐 치는 왼손 반주.')],
    ], [
      X('Play an Alberti bass on the chord of C: C G E G, again and again.', 'C 화음으로 알베르티 베이스를 쳐요: C G E G를 되풀이해요.'),
      sayYears('Play a Classical piece you know, such as a sonatina.', '소나티네처럼 아는 고전주의 곡을 쳐요.'),
    ], X('Classical: 1750 to 1820. Mozart. The fortepiano.', '고전주의: 1750~1820. 모차르트. 포르테피아노.'), <CpxPeriodPad k={1}/>),

    P(4, t('Step 3', '3단계'), 'romantic', p4, [
      [t('Romantic period', '낭만주의 시대'), X('The period from about 1820 to 1900.', '1820년쯤부터 1900년까지의 시대.')],
      [t('rubato', '루바토'), X('Time bent for feeling: a little faster, then a little slower.', '표현을 위해 빠르기를 조금 당겼다가 조금 늦추는 것.')],
      [t('virtuoso', '비르투오소'), X('A performer with dazzling skill, such as Liszt.', '리스트처럼 놀라운 기교를 가진 연주자.')],
    ], [
      X('Play a slow tune twice: once in strict time, once with a little rubato.', '느린 선율을 두 번 쳐요: 한 번은 일정한 빠르기로, 한 번은 루바토를 조금 넣어서.'),
      sayYears('Play a Romantic piece you know.', '아는 낭만주의 곡을 쳐요.'),
    ], X('Romantic: 1820 to 1900. Chopin. The piano.', '낭만주의: 1820~1900. 쇼팽. 피아노.'), <CpxPeriodPad k={2}/>),

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Modern and Contemporary', '근대와 현대')}>
      {live(p5, <CpxPeriodPad k={3}/>)}
      <LbDefs items={[
        [t('Modern period', '근대'), X('The period from about 1900 to 1950.', '1900년쯤부터 1950년까지의 시대.')],
        [t('Contemporary period', '현대'), X('The period from 1950 to today.', '1950년부터 오늘날까지의 시대.')],
        [t('Impressionism', '인상주의'), X('Music of soft colours and moods, from about 1890 to 1920: Debussy, Ravel.', '부드러운 색채와 분위기의 음악. 1890년쯤부터 1920년까지: 드뷔시, 라벨.')],
      ]}/>
      <LbPiano steps={[
        sayYears('Play a Modern or Contemporary piece you know.', '아는 근대나 현대 곡을 쳐요.'),
        X('Hold the sustaining pedal down and play soft notes high up. Let them blur, like an Impressionist painting.', '댐퍼 페달을 밟은 채 높은 음을 여리게 쳐요. 인상주의 그림처럼 소리가 번지게 해요.'),
      ]}/>
      <LbRemember>{X('Modern: 1900 to 1950. Contemporary: 1950 to today.', '근대: 1900~1950. 현대: 1950년부터 오늘날까지.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Who lived when', '누가 언제 살았을까')}>
      {live(p6, <CpxAlivePad/>)}
      <LbDefs items={[
        [t('contemporaries', '동시대인'), X('People who lived at the same time.', '같은 시기에 살았던 사람들.')],
      ]}/>
      <LbPiano steps={[
        X('On the timeline, find 1685. Who was born that year?', '타임라인에서 1685년을 찾아요. 그해에 누가 태어났나요?'),
        X('In 1792 Beethoven went to Vienna to study with Haydn. Find both on the timeline. Play Haydn’s “Surprise” tune (C C E E G G E), then Beethoven’s “Ode to Joy” (E E F G G F E D).'.replace(/\(([A-G ]+)\)/g, (m, x) => '(' + x.replace(/ /g, '\u00a0') + ')'), '1792년에 베토벤은 하이든에게 배우러 빈에 갔어요. 타임라인에서 두 사람을 찾아요. 하이든의 “놀람” 선율을 쳐요(C C E E G G E). 그다음 베토벤의 “환희의\u00a0송가”를 쳐요(E E F G G F E D).'.replace(/\(([A-G ]+)\)/g, (m, x) => '(' + x.replace(/ /g, '\u00a0') + ')')),
      ]}/>
      <LbRemember>{X('Contemporaries lived at the same time. A line down from one year finds them.', '동시대인은 같은 시기에 살았어요. 한 해에서 아래로 선을 그으면 찾을 수 있어요.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one on its page (1 to 6). The check-up on paper is in the Workbook.', '1~6쪽을 펴고 하나씩 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_cpx_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
    </LbPage>,
  ];
}
function ComposersLessonBook() { return <>{cpxLbPages(false)}</>; }
