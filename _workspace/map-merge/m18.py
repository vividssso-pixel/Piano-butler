p='drills.src.html'; s=open(p).read()
if 'm18' in s: print('already'); raise SystemExit
SUB = {
 'posture-hands':['Sit tall, round hands','바른 자세, 둥근 손'],'first-steps':['Black keys in twos and threes','검은건반 2개·3개'],'pulse':['Feel the steady beat','일정한 박 느끼기'],
 'note-names':['A to G on the keys','건반 위 A부터 G'],'hand-positions':['Middle C and C position','가운데 도와 C 자리'],'ear-prep':['Games for your ears','귀로 하는 놀이'],
 'note-values':['How long each note lasts','음표마다 길이'],'dynamics':['p, f and in between','p, f, 그 사이'],'staff':['Five lines, two clefs','다섯 줄, 두 음자리표'],
 'reading-steps':['Read by step and skip','걸음과 건너뛰기로 읽기'],'whole-staff':['Every note on the staff','오선 위 모든 음'],'time-signatures':['2/4, 3/4 and 4/4','2/4, 3/4, 4/4'],'tones':['Whole and half steps','온음과 반음'],
 'listen-sing':['Hear it, sing it back','듣고 따라 부르기'],'tempo':['How fast: the Italian words','빠르기와 이탈리아어'],'rhythm':['Quavers and dots','8분음표와 점음표'],'ledger-lines':['Notes above and below','오선 위아래의 음'],
 'scales':['How a scale is built','스케일의 짜임'],'scale-play':['Thumb under, smooth and even','엄지 넘기기, 고르게'],'minor-scales':['Natural and harmonic','자연단음계, 화성단음계'],'signs':['Repeats, pause, D.C.','도돌이표, 늘임표, D.C.'],
 'listen-write':['Home note, clap it back','으뜸음, 리듬 따라 치기'],'accidentals':['Sharps, flats, naturals','샵, 플랫, 제자리표'],'key-signatures':['The sharps or flats of a key','조의 샵과 플랫'],'terms':['Largo to presto','라르고부터 프레스토'],
 'six-eight':['Two big beats in threes','셋씩 묶인 두 큰 박'],'intervals':['From a 2nd to an octave','2도부터 옥타브까지'],'chords':['Triads; I, IV and V','3화음; I, IV, V'],'form':['AB, ABA, rondo','AB, ABA, 론도'],
 'listen-23':['Two notes together','동시에 울리는 두 음'],'melody':['Question and answer','묻고 답하는 프레이즈'],'scales-23':['Black-key starts, chromatic','검은건반 시작, 반음계'],'harmony-2':['Major, minor, perfect','장·단·완전 음정'],'rhythm-2':['Semiquavers and triplets','16분음표와 셋잇단'],
 'listen-3':['Name the interval','음정 이름 맞히기'],'melody-3':['Write a four-bar tune','네 마디 선율 쓰기'],'scales-3':['Contrary motion, new keys','반진행, 새 조'],'harmony-3':['Degree names, inversions','음의 이름, 자리바꿈'],'rhythm-3':['2/2, 3/8 and 9/8','2/2, 3/8, 9/8'],
 'listen-4':['Intervals and two parts','음정과 두 성부'],'scales-4':['Four octaves, arpeggios','4옥타브, 아르페지오'],'keys-4':['Up to six sharps or flats','샵·플랫 여섯 개까지'],'harmony-4':['The four cadences','네 가지 종지'],'rhythm-4':['Syncopation, 12/8','당김음, 12/8'],'melody-4':['A tune for a couplet','두 줄 시에 선율'],
 'listen-5':['Three intervals, triads','음정 셋, 3화음'],'scales-5':['Now with dynamics','셈여림을 넣어서'],'keys-5':['Every key, both minors','모든 조, 두 단음계'],'harmony-5':['The cadential 6-4','종지 6-4'],'melody-5':['A tune for a stanza','네 줄 시에 선율'],
 'listen-6':['Triads and inversions','3화음과 자리바꿈'],'scales-6':['The grand scale','그랜드 스케일'],'arps-6':['Inversions, dominant 7th','자리바꿈, 딸림7'],'harmony-6':['V7 and figured bass','V7과 숫자저음'],
 'listen-7':['Cadences, sing from memory','종지, 외워 부르기'],'scales-7':['Three against two','3 대 2'],'arps-7':['Chord walks, accompaniments','화음 진행, 반주형'],'pieces-78':['Form and style of your piece','내 곡의 형식과 스타일'],
 'listen-8':['All four cadences','네 가지 종지 모두'],'scales-8':['A third and a sixth apart','3도·6도 간격'],'arps-8':['I IV I6-4 V I','I IV I6-4 V I'],'pieces-8':['Your pieces, diploma depth','디플로마 깊이로 내 곡'],
 'piano-story':['Inside the piano','피아노 속 이야기'],'piano-story-8':['The piano through time','피아노의 역사'],'pitch-range':['High and low instruments','높은 악기, 낮은 악기'],'composers':['Baroque to today','바로크부터 오늘까지'],'styles':['Folk, jazz, blues, classical','민요, 재즈, 블루스, 클래식'],
}
import json
assert len(SUB)==67, len(SUB)
js="const CH_SUB = " + json.dumps(SUB, ensure_ascii=False).replace('], "', '],\n  "') + ";   // m18: one line, what you learn in the room (drafts, 1 Nov; hers to edit)\n"
comp = js + r'''const TH_SANS = "Inter, 'Pretendard', system-ui, sans-serif";
function thCleanLay(state, rooms, cmp) {   // m18: the clean room -- the number, the name in a bold sans, one line of what you learn
  const tz = cmp ? 11.5 : 14, sz = cmp ? 8.6 : 10.5, pad = cmp ? 7 : 9;
  const lines = {}, subs = {}; let ml = 1, sl = 1;
  rooms.forEach(([id, w]) => { const nm = CH_SHORT[id] || [id, ''], sb = CH_SUB[id];
    lines[id] = thWrap(t(nm[0], nm[1] || nm[0]), w - 2 * pad, tz, TH_SANS).slice(0, 2); ml = Math.max(ml, lines[id].length);
    subs[id] = sb ? thWrap(t(sb[0], sb[1]), w - 2 * pad, sz, TH_SANS).slice(0, 2) : []; sl = Math.max(sl, subs[id].length); });
  const sq = cmp ? 14 : 17, h = pad + sq + 5 + ml * tz * 1.12 + 4 + sl * sz * 1.3 + pad;
  return { clean: true, tz, sz, pad, sq, lines, subs, ml, sl, h: Math.ceil(h) };
}
function thRoomClean(view, state, id, x, y, w, h, fs, out, dimNew, lay, cmp) {
  const st = state[id], on = id === view.here, done = st === 'done', num = view.nums[id], { tz, sz, pad, sq } = lay;
  let s = '<rect x="' + pFix(x) + '" y="' + pFix(y) + '" width="' + pFix(w) + '" height="' + pFix(h) + '" fill="#fff" stroke-width="1"/>';
  if (on) s += '<rect x="' + pFix(x + 1.2) + '" y="' + pFix(y + 1.2) + '" width="' + pFix(w - 2.4) + '" height="' + pFix(h - 2.4) + '" fill="#fff3ee" stroke="' + ST.C + '" stroke-width="2.4"/>';
  const nfill = on ? ST.C : dimNew && st === 'new' ? ST.NEW : ST.N;
  s += stSquare(x + pad, y + pad, sq, num, done ? ST.G : null, cmp ? 9 : 11);
  let ty = y + pad + sq + 5 + tz * 0.9;
  (lay.lines[id] || []).forEach((ln, i) => { s += stT(x + pad, ty + i * tz * 1.12, ln, { size: tz, weight: 800, font: TH_SANS, fill: nfill, ls: '-0.01em' }); });
  ty += lay.ml * tz * 1.12 + 4 - tz * 0.9 + sz * 0.95;
  (lay.subs[id] || []).forEach((ln, i) => { s += stT(x + pad, ty + i * sz * 1.3, ln, { size: sz, weight: 500, font: TH_SANS, fill: '#5a5d92' }); });
  const thn = THEORY_ROOM[id];
  if (thn && UI_TEACHER) s += stT(x + w - pad, y + pad + sq * 0.72, 'T' + thn, { size: cmp ? 7.5 : 9, weight: 800, fill: '#8a8cb8', anchor: 'end' });   // her 1 Nov: the T marks for the teacher only
  const star = view.star && view.star[id];
  if (!done && !star && view.review && view.review.includes(id)) { const rw = cmp ? 34 : 44, rh = cmp ? 10 : 12, rx0 = x + w - rw - pad, ry0 = y + pad + (UI_TEACHER && thn ? sq + 2 : 2);
    s += '<rect x="' + pFix(rx0) + '" y="' + pFix(ry0) + '" width="' + rw + '" height="' + rh + '" rx="' + (rh / 2) + '" fill="#fff" stroke="' + ST.C + '" stroke-width="0.9"/>' + stT(rx0 + rw / 2, ry0 + rh - (cmp ? 2.4 : 2.8), t('review', '다시'), { size: cmp ? 7 : 8.4, weight: 800, fill: ST.C, anchor: 'middle' }); }
  if (star) s += '<path d="' + chkStarD(x + w - (cmp ? 9 : 12), y + h - (cmp ? 9 : 12), cmp ? 5.5 : 7.5) + '" fill="' + ST.G + '" stroke="#fff" stroke-width="0.8"/>';
  if (view.focus && thArea(id) !== view.focus) s += '<rect x="' + pFix(x + 1) + '" y="' + pFix(y + 1) + '" width="' + pFix(w - 2) + '" height="' + pFix(h - 2) + '" fill="#fff" opacity="0.78" stroke="none"/>';
  const nm = CH_SHORT[id] || [id, ''], sb = CH_SUB[id];
  const label = num + '. ' + t(nm[0], nm[1] || nm[0]) + (sb ? ': ' + t(sb[0], sb[1]) : '') + (done ? t(', done', ', 완료') : on ? t(', you are here', ', 지금 여기') : '') + (star ? t(', check passed', ', 체크 통과') : '');
  out.btns.push({ num, html: '<g data-chapter="' + id + '" data-status="' + st + '" data-here="' + (on ? '1' : '0') + '" data-clean="1" role="button" tabindex="0" aria-label="' + penEsc(label).replace(/"/g, '&quot;') + '" style="cursor:pointer"><rect x="' + pFix(x + 1) + '" y="' + pFix(y + 1) + '" width="' + pFix(w - 2) + '" height="' + pFix(h - 2) + '" fill="transparent"/></g>' });
  return s;
}
'''
a="function thRoom(view, state, id, x, y, w, h, fs, out, dimNew, lay, cmp) {"
assert s.count(a)==1
s=s.replace(a, comp + a + "\n  if (lay && lay.clean) return thRoomClean(view, state, id, x, y, w, h, fs, out, dimNew, lay, cmp);   // m18", 1)
old="    const rwOf = (j) => (L1 - L0) / at(j)[2], lay = thNames(state, st.ids.map((id, j) => [id, rwOf(j)]));\n    const rh = (cmp ? 45 + (fs.wp === 'drape' ? 7 : 0) : RH) + (lay.ml - 1) * 14,"
assert s.count(old)==1, 'lay'
s=s.replace(old,"    const rwOf = (j) => (L1 - L0) / at(j)[2], lay = o.print ? thNames(state, st.ids.map((id, j) => [id, rwOf(j)])) : thCleanLay(state, st.ids.map((id, j) => [id, rwOf(j)]), cmp);   // m18: the clean rooms on screen; paper keeps its pictures\n    const rh = lay.clean ? lay.h : (cmp ? 45 + (fs.wp === 'drape' ? 7 : 0) : RH) + (lay.ml - 1) * 14,")
open(p,'w').write(s); print('ok')
