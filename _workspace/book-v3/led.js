// her 18 Nov ("덧줄이 생기는 걸 보여주고, 덮을 필요 없다는 걸 애니메이트"): the magic ladder and the no-lid trap, drawn moving
function ledOp(D, pts) { const ks = pts.map(p => (p[0] / D).toFixed(3)).join(';'), vs = pts.map(p => p[1]).join(';'); return `<animate attributeName="opacity" values="${vs}" keyTimes="${ks}" dur="${D}s" fill="freeze"/>`; }
function ledStaff() { let g = ''; for (let k = 0; k < 5; k++) g += `<line x1="40" x2="540" y1="${120 + k * 14}" y2="${120 + k * 14}" stroke="#26296b" stroke-width="1.6"/>`; return g + `<text x="44" y="180" font-size="82" fill="#26296b" font-family="serif">𝄞</text>`; }
function ledNote(x, y, c) { return `<ellipse cx="${x}" cy="${y}" rx="9" ry="6.4" transform="rotate(-20 ${x} ${y})" fill="${c || '#26296b'}"/>`; }
function drawLedLadder() {
  const key = 'ledladder'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const D = 7, ACC = '#e4572e', F = 'font-family="Atkinson Hyperlegible,sans-serif"';
  const steps = [['F', 200, 120, []], ['G', 265, 113, []], ['A', 330, 106, [106]], ['B', 395, 99, [106]], ['C', 460, 92, [106, 92]]];
  let g = ledStaff();
  steps.forEach(([n, x, y, rungs], i) => { const t = 0.4 + i * 0.9;
    g += `<g opacity="0">${ledOp(D, [[0, 0], [t, 0], [t + .3, 1], [D, 1]])}` + rungs.map(ry => `<line x1="${x - 16}" x2="${x + 16}" y1="${ry}" y2="${ry}" stroke="${ACC}" stroke-width="2.6"/>`).join('') + ledNote(x, y, i === steps.length - 1 ? ACC : null) + `<text x="${x}" y="${y > 110 ? 210 : 60}" text-anchor="middle" font-size="17" font-weight="700" fill="${rungs.length ? ACC : '#26296b'}" ${F}>${n}</text></g>`; });
  g += `<g opacity="0">${ledOp(D, [[0, 0], [4.6, 0], [5, 1], [D, 1]])}<text x="290" y="34" text-anchor="middle" font-size="16" font-weight="700" fill="${ACC}" ${F}>a rung appears only where the note needs one</text></g>`;
  lensShell(key, '♪ The magic ladder', `<svg viewBox="0 0 580 230" role="img" aria-label="A note climbs above the staff; ledger lines appear one at a time, only as far as the note goes">${g}</svg>`);
}
function drawLedLid() {
  const key = 'ledlid'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const D = 7, ACC = '#e4572e', GR = '#2e8a6e', F = 'font-family="Atkinson Hyperlegible,sans-serif"';
  let g = ledStaff() + ledNote(250, 113) + ledNote(400, 183) + `<text x="250" y="70" text-anchor="middle" font-size="17" font-weight="700" fill="#26296b" ${F}>G</text><text x="400" y="222" text-anchor="middle" font-size="17" font-weight="700" fill="#26296b" ${F}>D</text>`;
  const wrong = (x1, y, lab, ly) => `<line x1="${x1 - 17}" x2="${x1 + 17}" y1="${y}" y2="${y}" stroke="${ACC}" stroke-width="3"/><text x="${x1 + 26}" y="${ly}" font-size="16" font-weight="700" fill="${ACC}" ${F}>${lab}</text>`;
  g += `<g opacity="0">${ledOp(D, [[0, 0], [0.9, 0], [1.2, 1], [3.9, 1], [4.3, 0], [D, 0]])}${wrong(250, 104, 'a lid?', 100)}${wrong(400, 193, 'a stand?', 198)}</g>`;
  const X = (x, y) => `<path d="M${x - 14} ${y - 14}L${x + 14} ${y + 14}M${x + 14} ${y - 14}L${x - 14} ${y + 14}" stroke="${ACC}" stroke-width="4" stroke-linecap="round"/>`;
  g += `<g opacity="0">${ledOp(D, [[0, 0], [2.3, 0], [2.5, 1], [3.9, 1], [4.3, 0], [D, 0]])}${X(250, 104)}${X(400, 193)}</g>`;
  g += `<g opacity="0">${ledOp(D, [[0, 0], [4.3, 0], [4.8, 1], [D, 1]])}<text x="290" y="34" text-anchor="middle" font-size="17" font-weight="700" fill="${GR}" ${F}>✓ G sits on top, D hangs below: no line needed</text></g>`;
  lensShell(key, '♪ No lid, no stand', `<svg viewBox="0 0 580 235" role="img" aria-label="G sitting on top of the staff and D hanging below need no ledger line: a lid or a stand is crossed out">${g}</svg>`);
}
