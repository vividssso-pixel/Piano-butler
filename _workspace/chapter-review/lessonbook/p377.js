// ── Phase 377: the chapter map becomes the Piano Butler's House (house376.jsx) ──
rep('function MusicMap({ onOpen, compact, noIntro }) {', read('house376.jsx').replace('__HOUSE_ICONS__', read('houseicons.json').trim()) + '\nfunction MusicMap({ onOpen, compact, noIntro }) {', '377 house code');
rep(`      <MusicMap onOpen={onOpen} noIntro/>`, `      <HouseMap onOpen={onOpen} noIntro/>`, '377 map home');
rep(`        <MusicMap onOpen={onOpenChapter} compact/>`, `        <HouseMap onOpen={onOpenChapter} compact/>`, '377 student page');
rep(`text={t('The whole road on one page. Tap a chapter to open it, or carry on with the button.', '전체 길이 한 장에 있어요. 챕터를 누르거나, 버튼을 눌러 이어서 해요.')}/>`,
  `text={t('The Piano Butler’s house: every floor is a stage, every room is a chapter, from the front door up to the attic. Tap a room to open it, or carry on with the button.', '피아노 버틀러의 집: 층마다 단계 하나, 방마다 챕터 하나, 현관에서 다락까지. 방을 누르거나, 버튼을 눌러 이어서 해요.')}/>`, '377 map intro');
