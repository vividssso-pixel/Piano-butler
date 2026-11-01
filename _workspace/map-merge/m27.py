p='drills.src.html'; s=open(p).read()
if 'REF_MOVEMENTS' in s: print('already'); raise SystemExit
old="function RefPeriods() {\n  const paper = React.useContext(RefPaper), y0 = 1400,"
assert s.count(old)==1
s=s.replace(old,"""// m27 (her 'there used to be more in between'): the movements and styles inside and between the six periods
const REF_MOVEMENTS = [
  ['Medieval', '중세', 'before 1400', '1400년 이전', 'plainchant: one line, sung; then the first music in parts', '그레고리오 성가: 한 선율을 노래; 그리고 첫 여러 성부 음악', 'Hildegard, Machaut', '힐데가르트, 마쇼', null],
  ['Galant (Rococo)', '갈랑트 (로코코)', 'c. 1730–1770', '약 1730–1770', 'light and ornamented, between the Baroque and the Classical', '가볍고 꾸밈이 많은, 바로크와 고전 사이', 'C. P. E. Bach, J. C. Bach', 'C. P. E. 바흐, J. C. 바흐', null],
  ['Late Romantic', '후기 낭만', 'c. 1850–1910', '약 1850–1910', 'huge orchestras, rich chromatic harmony', '거대한 오케스트라, 풍부한 반음계 화성', 'Wagner, Brahms, Mahler, Rachmaninoff', '바그너, 브람스, 말러, 라흐마니노프', 'composers'],
  ['Nationalism', '민족주의', 'c. 1850–1940', '약 1850–1940', 'the folk tunes and dances of one country', '한 나라의 민요와 춤', 'Grieg, Dvořák, Smetana, Mussorgsky', '그리그, 드보르자크, 스메타나, 무소륵스키', 'composers'],
  ['Impressionism', '인상주의', 'c. 1890–1920', '약 1890–1920', 'colour and mood: whole-tone and pentatonic scales, blurred with the pedal', '색채와 분위기: 온음음계와 5음음계, 페달로 흐리게', 'Debussy, Ravel', '드뷔시, 라벨', 'composers'],
  ['Ragtime and jazz', '래그타임과 재즈', 'from c. 1895', '약 1895년부터', 'a syncopated tune over a steady left hand; then swing and the blues', '꾸준한 왼손 위의 당김음 선율; 그리고 스윙과 블루스', 'Joplin, Gershwin', '조플린, 거슈윈', 'styles'],
  ['Expressionism, serialism', '표현주의, 음렬주의', 'c. 1908–1960', '약 1908–1960', 'no home key; later, the twelve notes in a fixed row', '으뜸조 없음; 그 뒤 열두 음을 정한 순서로', 'Schoenberg, Berg, Webern', '쇤베르크, 베르크, 베베른', 'composers'],
  ['Neoclassicism', '신고전주의', 'c. 1920–1950', '약 1920–1950', 'old forms and clear textures with new harmonies', '옛 형식과 맑은 짜임에 새 화성', 'Stravinsky, Prokofiev, Poulenc', '스트라빈스키, 프로코피예프, 풀랑크', 'composers'],
  ['Minimalism', '미니멀리즘', 'from the 1960s', '1960년대부터', 'short patterns repeated, changing slowly', '짧은 음형을 되풀이하며 천천히 바뀌어요', 'Riley, Reich, Glass', '라일리, 라이히, 글래스', 'composers'],
  ['Today', '오늘', 'now', '지금', 'many styles at once: film and game music, electronic, crossover', '여러 양식이 함께: 영화·게임 음악, 전자 음악, 크로스오버', 'Einaudi, Kats-Chernin', '에이나우디, 카츠-체르닌', null],
];
function RefPeriods({ part }) {
  const paper = React.useContext(RefPaper), y0 = 1400,""")
old="    {!paper && <RefNote>{t('♪ plays the Styles room’s example of each period.', '♪는 양식 방의 시대별 예를 들려줘요.')}</RefNote>}\n  </div>;\n}"
assert s.count(old)==1
s=s.replace(old,"""    {!paper && <RefNote>{t('♪ plays the Styles room’s example of each period.', '♪는 양식 방의 시대별 예를 들려줘요.')}</RefNote>}
    {part !== 'a' && <><RefLab>{t('In between: movements and styles', '그 사이: 사조와 양식')}</RefLab>
    <RefTable k="movements" cols="minmax(0,1fr) auto" rows={REF_MOVEMENTS.map(([en, ko, yen, yko, den, dko, wen, wko, room]) => [<div data-ref-movement={en}><b style={{fontWeight:800}}>{t(en, ko)}</b> <span style={{fontSize:12,fontWeight:800,color:BK.coral,whiteSpace:'nowrap'}}>{t(yen, yko)}</span>
      <div style={{fontSize:13}}>{t(den, dko)}</div><div style={{color:BK.muted,fontWeight:700,fontSize:12.5}}>{t(wen, wko)}</div></div>, <RefDoor room={room}/>])}/></>}
  </div>;
}""")
open(p,'w').write(s); print('ok')
