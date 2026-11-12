
// ---- Read & listen: the app's moving posture and hand drawings in the lens (her 12 Nov: "움직이는 것 다 끼워서") ----
// Three widgets, each the app's own drawing: the stool (side view, height and distance), the elbows (front view)
// and the hand (side view, the good shape and five faults). The narration sets the pose; the reader can press or drag.
(function () {
  const SIT = { good: [114, 100], low: [124, 100], high: [106, 100], close: [114, 124], far: [114, 90] };
  const SITL = { good: 'Just right', low: 'Stool too low', high: 'Stool too high', close: 'Too close', far: 'Too far' };
  const HANDS = ['good', 'flat', 'bridge', 'nail', 'low', 'high'];
  const FRONT = { good: 0.45, tight: 0.05, wings: 0.95 };
  const GOOD = [80, 55, 24, -3, -2];
  const W = {};   // kind -> state
  const chip = (on, txt, data, bad) => `<button type="button" class="pch${on ? ' on' : ''}" data-v="${data}">${bad ? '<span class="px">✗</span> ' : on && !bad ? '✓ ' : ''}${txt}</button>`;
  function anim(st, to, draw, ms = 520) {
    cancelAnimationFrame(st.raf); const from = st.v.slice(), t0 = performance.now();
    const step = (now) => { const k = Math.min(1, (now - t0) / ms), e = pEase(k); st.v = from.map((x, i) => x + (to[i] - x) * e); draw(); if (k < 1) st.raf = requestAnimationFrame(step); };
    st.raf = requestAnimationFrame(step);
  }
  function cycle(st, list, go) { clearInterval(st.cyc); let i = 0; go(list[0]); st.cyc = setInterval(() => { if (!st.el.isConnected) return clearInterval(st.cyc); i = (i + 1) % list.length; go(list[i]); }, 1900); }
  // the stool, from the side
  function mountSit(el) {
    const st = W.sit = { el, v: SIT.low.slice(), id: 'low' };
    el.innerHTML = `<div class="pchips">${Object.keys(SIT).map(k => chip(false, SITL[k], k, k !== 'good')).join('')}</div><div class="pdraw"></div>
<div class="psl"><label>Height<input type="range" min="0" max="30" data-s="h"></label><label>Distance<input type="range" min="0" max="44" data-s="d"></label></div><div class="pck"></div>`;
    const draw = () => {
      const [y, x] = st.v, p = sitPose376(y, x, false), cks = sitChecks376(p);
      el.querySelector('.pdraw').innerHTML = penSvg(penSitShapes(y, x, false, cks));
      el.querySelector('.pck').innerHTML = cks.map(c => `<div class="${c.ok ? 'ok' : 'no'}"><b>${c.ok ? '✓' : '✗'}</b> ${c.label}${c.ok ? '' : '<span>: ' + c.fix + '</span>'}</div>`).join('');
      el.querySelector('[data-s=h]').value = 130 - y; el.querySelector('[data-s=d]').value = 132 - x;
      el.querySelectorAll('.pch').forEach(b => b.classList.toggle('on', b.dataset.v === st.id));
    };
    st.draw = draw;
    el.querySelectorAll('.pch').forEach(b => b.onclick = () => { clearInterval(st.cyc); st.id = b.dataset.v; anim(st, SIT[st.id], draw); });
    el.querySelectorAll('input').forEach(r => r.oninput = () => { clearInterval(st.cyc); cancelAnimationFrame(st.raf); st.id = '';
      st.v = [130 - +el.querySelector('[data-s=h]').value, 132 - +el.querySelector('[data-s=d]').value]; draw(); });
    draw();
  }
  // the elbows, from the front
  function mountFront(el) {
    const st = W.front = { el, v: [0.05], id: 'tight' };
    el.innerHTML = `<div class="pdraw pfront"></div><div class="psl"><label>Elbows<input type="range" min="0" max="100" data-s="g"></label></div><div class="pck"></div>`;
    const draw = () => { const g = st.v[0], ok = g >= 0.3 && g <= 0.65;
      el.querySelector('.pdraw').innerHTML = penSvg(penFrontShapes(g, ok), { vb: [0, 20, 150, 146] });
      el.querySelector('.pck').innerHTML = `<div class="${ok ? 'ok' : 'no'}"><b>${ok ? '✓' : '✗'}</b> ${g < 0.3 ? 'Elbows stuck to the body' : g > 0.65 ? 'Chicken wings: elbows too far out' : 'Elbows a fist away from the body'}</div>`;
      el.querySelector('[data-s=g]').value = Math.round(g * 100); };
    st.draw = draw;
    el.querySelector('input').oninput = (e) => { clearInterval(st.cyc); cancelAnimationFrame(st.raf); st.v = [+e.target.value / 100]; draw(); };
    draw();
  }
  // the hand, from the side
  function mountHand(el) {
    const st = W.hand = { el, v: GOOD.slice(), id: 'good' };
    el.innerHTML = `<div class="pchips">${HANDS.map(k => chip(false, k === 'good' ? 'The good shape' : HAND_POSES[k].title, k, k !== 'good')).join('')}</div><div class="pdraw"></div><div class="pck"></div>`;
    const draw = () => {
      const r = penHandSide(st.v, { ball: st.id === 'good', nail: st.id === 'nail', halo: true });
      el.querySelector('.pdraw').innerHTML = penSvg(r.shapes, { vb: [34, 26, 258, 126] });
      const P = st.id === 'good' ? null : HAND_POSES[st.id];
      el.querySelector('.pck').innerHTML = P ? `<div class="no"><b>✗</b> ${P.title}<span>: ${P.see}</span></div>` : `<div class="ok"><b>✓</b> The good shape<span>: knuckles up like a bridge, the wrist level, playing on the fingertip.</span></div>`;
      el.querySelectorAll('.pch').forEach(b => b.classList.toggle('on', b.dataset.v === st.id));
    };
    st.draw = draw;
    el.querySelectorAll('.pch').forEach(b => b.onclick = () => { clearInterval(st.cyc); st.id = b.dataset.v; anim(st, st.id === 'good' ? GOOD : HAND_POSES[st.id].a, draw); });
    draw();
  }
  // finger numbers: the app's two hands from above, each finger lighting with its number (frames from the app)
  const FSEQ = [['3:1', 'Thumbs are 1'], ['3:right hand finger 2', 'Right hand, finger 2'], ['3:right hand finger 3', 'Right hand, finger 3'], ['3:right hand finger 4', 'Right hand, finger 4'], ['3:right hand finger 5', 'Right hand, finger 5'],
    ['3:left hand finger 2', 'Left hand, finger 2'], ['3:left hand finger 3', 'Left hand, finger 3'], ['3:left hand finger 4', 'Left hand, finger 4'], ['3:left hand finger 5', 'Left hand, finger 5']];
  function mountFing(el) {
    const st = W.fing = { el, i: 0 };
    el.innerHTML = `<div class="pchips">${[1, 2, 3, 4, 5].map(n => `<button type="button" class="pch" data-v="${n}">${n}</button>`).join('')}</div><div class="pdraw pfing"></div><div class="pck"></div>`;
    const draw = () => { const [k, lab] = FSEQ[st.i]; el.querySelector('.pdraw').innerHTML = (window.PEN_FING || {})[k] || '';
      el.querySelector('.pck').innerHTML = `<div class="ok"><b>${st.i === 0 ? 1 : (st.i - 1) % 4 + 2}</b> ${lab}</div>`; };
    st.draw = draw;
    el.querySelectorAll('.pch').forEach(b => b.onclick = () => { clearInterval(st.cyc); const n = +b.dataset.v, right = !(st.i >= 5 && n > 1); st.i = n === 1 ? 0 : (right ? n - 1 : n + 3); draw(); });
    draw();
  }
  const MOUNT = { sit: mountSit, front: mountFront, hand: mountHand, fing: mountFing };
  function go(kind, target) {
    const st = W[kind]; if (!st) return; clearInterval(st.cyc);
    if (kind === 'sit') {
      const one = (id) => { st.id = id; anim(st, SIT[id], st.draw); };
      if (target === 'cycle') cycle(st, ['low', 'good', 'high', 'good'], one); else if (SIT[target]) one(target);
    } else if (kind === 'hand') {
      const one = (id) => { st.id = id; anim(st, id === 'good' ? GOOD : HAND_POSES[id].a, st.draw); };
      if (target === 'cycle') cycle(st, ['good', 'flat', 'good', 'bridge', 'good', 'low'], one);
      else if (target === 'cycle-ex') cycle(st, ['flat', 'bridge', 'good'], one); else if (HANDS.includes(target)) one(target);
    } else if (kind === 'fing') {
      st.i = 0; st.draw(); st.cyc = setInterval(() => { if (!st.el.isConnected) return clearInterval(st.cyc); st.i = (st.i + 1) % FSEQ.length; st.draw(); }, 1100);
    } else if (kind === 'front') {
      const one = (id) => { st.id = id; anim(st, [FRONT[id]], st.draw); };
      if (target === 'cycle') cycle(st, ['tight', 'good', 'wings', 'good'], one); else if (FRONT[target] != null) one(target);
    }
  }
  window.PEN = { mount: (kind, el) => { Object.values(W).forEach(s => { clearInterval(s.cyc); cancelAnimationFrame(s.raf); }); MOUNT[kind](el); }, go };
})();
