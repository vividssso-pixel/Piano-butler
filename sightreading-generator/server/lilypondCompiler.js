// ---------------------------------------------------------------------------
// Compiles a LilyPond (.ly) source string to PDF, then rasterizes it to PNG
// for inline preview, per the build spec's step 7:
//   "Compile to PDF via LilyPond; rasterize to PNG via pdftoppm for inline
//    preview. Return both files to the frontend."
//
// 2026-08-27: the inline preview PNG is no longer a raster of the whole
// page (or even of the whole page cropped as one block) -- it's composed
// from two SEPARATELY cropped pieces, the title/subtitle and the music
// system, each independently centered on a shared canvas by
// composePreview.py. See that script's header comment for why: LilyPond's
// own title centers over the PAPER's line-width, which for a short
// excerpt is usually much wider than the actual music, so a single-crop
// raster left the title looking off-center over the staff. The full-page
// PDF (used for the Download PDF button and for print) is untouched by
// any of this -- only the inline PNG preview goes through the compose step.
//
// This same pass optionally also renders single-staff "right hand only" /
// "left hand only" preview images (see the `variants` param) for the
// hands-view toggle in the UI, reusing the exact same melody/bassLine defs
// as the full piece so the isolated view can never show different notes.
// ---------------------------------------------------------------------------

const fs = require('fs');
const os = require('os');
const path = require('path');
const { execFile } = require('child_process');

function run(cmd, args, opts = {}) {
  return new Promise((resolve, reject) => {
    execFile(cmd, args, { timeout: 30000, ...opts }, (err, stdout, stderr) => {
      if (err) {
        reject(new Error(`${cmd} failed: ${stderr || err.message}`));
        return;
      }
      resolve({ stdout, stderr });
    });
  });
}

// General MIDI soundfont installed via `fluid-soundfont-gm`. Used to render
// the LilyPond-generated .midi file to actual audio so a teacher/student can
// listen back and check the excerpt reads/sounds correctly, not just look at
// the notation.
const SOUNDFONT = '/usr/share/sounds/sf2/FluidR3_GM.sf2';

const COMPOSE_SCRIPT = path.join(__dirname, 'composePreview.py');
const PREVIEW_DPI = '200';

// Our own generator (server/generator/index.js) always writes title/
// subtitle as `\markup { ... "actual text" }` on a single line -- this is
// the signature that tells us it's safe to run the two-piece compose
// pipeline (we know exactly how to blank the header and how to pull the
// display text back out for the standalone header render). Arbitrary
// Explorer Bank uploads won't match this and fall back to a plain single-
// crop raster of the whole page instead.
function isOwnGeneratedFormat(lySource) {
  return /title\s*=\s*\\markup/.test(lySource);
}

// Pull the last "..."-quoted string off a `title = ...` / `subtitle = ...`
// line. Our header lines always have exactly two quoted strings (the font
// name, then the actual display text) -- the display text is always last.
function extractHeaderText(lySource, field) {
  const lineRe = new RegExp(`^\\s*${field}\\s*=.*$`, 'm');
  const lineMatch = lineRe.exec(lySource);
  if (!lineMatch) return null;
  const quotes = [...lineMatch[0].matchAll(/"([^"]*)"/g)];
  if (!quotes.length) return null;
  return quotes[quotes.length - 1][1];
}

// Blank out the title/subtitle header fields (keeping every other line,
// including \paper's font-tree setup, intact) so a crop of this source
// contains only the music -- no reserved header space.
function blankHeader(lySource) {
  return lySource
    .replace(/^(\s*)title\s*=.*$/m, '$1title = ""')
    .replace(/^(\s*)subtitle\s*=.*$/m, '$1subtitle = ""');
}

// Render a standalone title/subtitle block (no music at all) as a tightly
// cropped PNG. Uses the same minimal sans-serif styling as index.js's
// headerBlock() -- kept as a literal copy here rather than a shared import
// since this file intentionally has no dependency on the generator module
// (Explorer Bank uploads, which never go through the generator, still flow
// through this same compiler).
async function renderHeaderOnly(titleText, subtitleText, scratchDir) {
  const esc = (s) => s.replace(/\\/g, '\\\\').replace(/"/g, '\\"');
  const ly = `\\version "2.24.3"

\\paper {
  indent = 0
}

\\markup \\column {
  \\center-column {
    \\override #'(font-name . "Liberation Sans")
    \\fontsize #2 \\normal-text "${esc(titleText)}"
  }
  ${subtitleText ? `\\vspace #0.4
  \\center-column {
    \\override #'(font-name . "Liberation Sans")
    \\fontsize #-1 \\normal-text \\with-color #(x11-color 'gray40) "${esc(subtitleText)}"
  }` : ''}
}
`;
  return renderCroppedMarkupOrScore(ly, scratchDir, 'header');
}

// Compile+crop an arbitrary .ly source (either the header-only markup doc
// above, or a full score with a blanked header) and rasterize the cropped
// result to PNG. Returns the PNG path.
async function renderCroppedMarkupOrScore(ly, scratchDir, label) {
  const lyPath = path.join(scratchDir, `${label}.ly`);
  const croppedPdfPath = path.join(scratchDir, `${label}.cropped.pdf`);
  const pngPath = path.join(scratchDir, `${label}.png`);
  fs.writeFileSync(lyPath, ly, 'utf8');
  await run('lilypond', ['-dcrop', '-o', scratchDir, lyPath]);
  if (!fs.existsSync(croppedPdfPath)) {
    throw new Error(`LilyPond did not produce a cropped PDF for ${label}`);
  }
  await run('pdftoppm', ['-png', '-r', PREVIEW_DPI, '-singlefile', croppedPdfPath, path.join(scratchDir, label)]);
  if (!fs.existsSync(pngPath)) {
    throw new Error(`pdftoppm did not produce a PNG for ${label}`);
  }
  return pngPath;
}

// Build the composed (title-over-music, both independently centered)
// preview PNG for every requested view ('both', plus 'treble'/'bass' when
// variant sources are supplied), writing each final PNG into outDir as
// "<id>.png" (both) / "<id>.treble.png" / "<id>.bass.png".
async function buildComposedPreviews({ lySource, variants, outDir, id }) {
  const scratchDir = fs.mkdtempSync(path.join(os.tmpdir(), `lyprev-${id}-`));
  try {
    const titleText = extractHeaderText(lySource, 'title') || 'Sight-Reading Excerpt';
    const subtitleText = extractHeaderText(lySource, 'subtitle') || '';

    const views = { both: lySource };
    if (variants && variants.treble) views.treble = variants.treble;
    if (variants && variants.bass) views.bass = variants.bass;

    // The header render and every view's score render are all mutually
    // independent LilyPond compiles -- run them concurrently rather than
    // one after another. Each `lilypond` invocation has a fixed ~1-2s
    // startup cost regardless of how tiny the input is, so with up to 4
    // compiles per generate (header + both/treble/bass) doing them serially
    // was adding several seconds of pure wait for no reason.
    const viewNames = Object.keys(views);
    const [headerPng, ...scorePngs] = await Promise.all([
      renderHeaderOnly(titleText, subtitleText, scratchDir),
      ...viewNames.map((viewName) => renderCroppedMarkupOrScore(blankHeader(views[viewName]), scratchDir, `score-${viewName}`)),
    ]);

    const result = {};
    await Promise.all(
      viewNames.map(async (viewName, i) => {
        const finalPath = viewName === 'both' ? path.join(outDir, `${id}.png`) : path.join(outDir, `${id}.${viewName}.png`);
        await run('python3', [COMPOSE_SCRIPT, headerPng, scorePngs[i], finalPath]);
        result[viewName] = finalPath;
      })
    );
    return result;
  } finally {
    fs.rmSync(scratchDir, { recursive: true, force: true });
  }
}

// Fallback for content that isn't in our own generator's header format
// (Explorer Bank uploads): a single crop of the whole page, same approach
// as the previous (2026-08-27, pre-compose) fix -- still much tighter than
// rasterizing an entire uncropped page, just without the independent
// title/music centering the compose pipeline gives our own excerpts.
async function buildFallbackPreview({ lySource, outDir, id }) {
  const scratchDir = fs.mkdtempSync(path.join(os.tmpdir(), `lyprev-${id}-`));
  try {
    const scorePng = await renderCroppedMarkupOrScore(lySource, scratchDir, 'whole');
    const finalPath = path.join(outDir, `${id}.png`);
    fs.copyFileSync(scorePng, finalPath);
    return { both: finalPath };
  } finally {
    fs.rmSync(scratchDir, { recursive: true, force: true });
  }
}

/**
 * @param {string} lySource the full ("both hands") score -- also what's
 *   compiled for the downloadable PDF and the MIDI/mp3 audio.
 * @param {string} outDir directory to write <id>.ly/.pdf/.png/.mid/.mp3 into
 * @param {string} id base filename (no extension)
 * @param {{treble?: string, bass?: string}} [variants] optional single-
 *   staff LilyPond sources (right-hand-only / left-hand-only) for the
 *   hands-view toggle -- only meaningful when the piece actually has two
 *   staves. Each, if present, also gets a composed preview PNG written to
 *   "<id>.treble.png" / "<id>.bass.png".
 * @returns {Promise<{lyPath:string, pdfPath:string, pngPath:string, pngPathTreble:string|null, pngPathBass:string|null, midiPath:string|null, mp3Path:string|null}>}
 */
async function compileExcerpt(lySource, outDir, id, variants) {
  fs.mkdirSync(outDir, { recursive: true });
  const lyPath = path.join(outDir, `${id}.ly`);
  const pdfPath = path.join(outDir, `${id}.pdf`);
  const midiPath = path.join(outDir, `${id}.midi`);
  const wavPath = path.join(outDir, `${id}.wav`);
  const mp3Path = path.join(outDir, `${id}.mp3`);

  fs.writeFileSync(lyPath, lySource, 'utf8');

  // The normal (uncropped) full-page compile -- used for the Download PDF
  // button, the print page, and the MIDI/audio pipeline -- and the preview
  // PNG pipeline are entirely independent of each other (different output
  // files, different scratch dirs), so run them concurrently rather than
  // waiting for the full-page compile before starting on previews.
  const [, previews] = await Promise.all([
    run('lilypond', ['-o', outDir, lyPath]).then(() => {
      if (!fs.existsSync(pdfPath)) {
        throw new Error('LilyPond did not produce a PDF');
      }
    }),
    (async () => {
      try {
        if (isOwnGeneratedFormat(lySource)) {
          return await buildComposedPreviews({ lySource, variants, outDir, id });
        }
        return await buildFallbackPreview({ lySource, outDir, id });
      } catch (err) {
        // Never let a preview-image problem block an otherwise-working PDF
        // -- fall back to the simplest possible raster (whole page, no
        // crop) so the caller still gets SOME preview rather than a hard
        // failure. Needs the full-page PDF to exist first, so this
        // fallback path is awaited separately below rather than raced.
        console.error('Composed preview failed, falling back to plain raster:', err.message);
        return null;
      }
    })(),
  ]);

  let finalPreviews = previews;
  if (!finalPreviews) {
    await run('pdftoppm', ['-png', '-r', '150', '-singlefile', pdfPath, path.join(outDir, id)]);
    finalPreviews = { both: path.join(outDir, `${id}.png`) };
  }

  // Audio playback is best-effort: a \midi block is only emitted when the
  // .ly source includes one (see index.js), and fluidsynth/ffmpeg rendering
  // can fail independently of the notation itself compiling fine. Never let
  // an audio problem block the (already-working) PDF/PNG result.
  let mp3PathResult = null;
  if (fs.existsSync(midiPath)) {
    try {
      await run('fluidsynth', ['-ni', SOUNDFONT, midiPath, '-F', wavPath, '-r', '44100'], { timeout: 30000 });
      if (fs.existsSync(wavPath)) {
        await run('ffmpeg', ['-y', '-i', wavPath, '-codec:a', 'libmp3lame', '-qscale:a', '4', mp3Path], { timeout: 30000 });
        if (fs.existsSync(mp3Path)) {
          mp3PathResult = mp3Path;
        }
        fs.unlinkSync(wavPath);
      }
    } catch (err) {
      console.error('Audio render failed (non-fatal):', err.message);
    }
  }

  return {
    lyPath,
    pdfPath,
    pngPath: finalPreviews.both,
    pngPathTreble: finalPreviews.treble || null,
    pngPathBass: finalPreviews.bass || null,
    midiPath: fs.existsSync(midiPath) ? midiPath : null,
    mp3Path: mp3PathResult,
  };
}

module.exports = { compileExcerpt };
