import createVerovioModule from 'verovio/wasm';
import { VerovioToolkit } from 'verovio/esm';
import fs from 'fs';
const M = await createVerovioModule(); const tk = new VerovioToolkit(M);
const mei = `<?xml version="1.0" encoding="UTF-8"?><mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.0"><meiHead><fileDesc><titleStmt><title/></titleStmt><pubStmt/></fileDesc></meiHead><music><body><mdiv><score>
<scoreDef><staffGrp><staffDef n="1" lines="5" clef.shape="G" clef.line="2" meter.count="4" meter.unit="4"/></staffGrp></scoreDef><section>
<measure n="1"><staff n="1"><layer n="1"><note xml:id="a1" pname="c" oct="4" dur="4"/><note xml:id="a2" pname="d" oct="4" dur="4"/><note xml:id="a3" pname="e" oct="4" dur="4"/><note xml:id="a4" pname="f" oct="4" dur="4"/></layer></staff>
<dynam staff="1" startid="#a1" place="below">p</dynam><fing staff="1" startid="#a1" place="above">1</fing><slur xml:id="sl" startid="#a1" endid="#b1" curvedir="above"/></measure>
<measure n="2" right="end"><staff n="1"><layer n="1"><note xml:id="b1" pname="e" oct="4" dur="2"/><rest dur="2"/></layer></staff>
<fing staff="1" startid="#b1" place="above">3</fing><harm staff="1" startid="#b1" place="above">C</harm></measure>
</section></score></mdiv></body></music></mei>`;
tk.setOptions({ pageWidth: 1400, adjustPageHeight: true, adjustPageWidth: true, scale: 50, header: 'none', footer: 'none', svgViewBox: true, pageMarginTop: 40, pageMarginBottom: 100, pageMarginLeft: 10, pageMarginRight: 30, breaks: 'none', spacingLinear: 0.3, spacingNonLinear: 0.6, font: 'Leipzig', dynamDist: 3 });
tk.loadData(mei); let svg = tk.renderToSVG(1);
svg = svg.replace('<g id="b1" class="note">', '<g id="b1" class="note" fill="#e4572e" color="#e4572e" stroke="#e4572e">');
svg = svg.replace(/<g([^>]*class="dynam"[^>]*)>/, '<g$1 transform="translate(0,120)">');
fs.writeFileSync('/tmp/claude-0/pk/six/six.svg', svg); console.log(svg.length, (svg.match(/class="(dynam|fing|slur|harm)"/g) || []).length);
