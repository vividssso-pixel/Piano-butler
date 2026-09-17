# ---------------------------------------------------------------------------
# 2026-09-15: written so this app can finally be deployed publicly (it was
# only ever run locally before this). Render's free Web Service tier is the
# deploy target Sohyun picked specifically to keep this at $0/month -- see
# server.js's 2026-09-15 comment for the Mission Bank removal this same
# decision drove (free tier disk is wiped on every redeploy/restart/
# spin-down, so nothing here should depend on the filesystem surviving).
#
# Why a plain Node buildpack won't work: server/lilypondCompiler.js shells
# out directly to several system binaries that a normal "npm install && npm
# start" host has no reason to have installed -- `lilypond` (the actual
# notation engraver), `pdftoppm` (poppler-utils, PDF->PNG rasterizing),
# `python3` + Pillow (composePreview.py's title/music image compositing),
# and `fluidsynth` + `ffmpeg` (best-effort MIDI->mp3 playback rendering,
# see compileExcerpt's audio step). This image installs all of them
# explicitly so the container has everything server.js expects, exactly
# the same set that's already present in this dev sandbox.
# ---------------------------------------------------------------------------

FROM node:20-bookworm-slim

# lilypond      -- notation engraving (.ly -> .pdf/.midi)
# poppler-utils -- pdftoppm (PDF -> PNG rasterizing, preview images)
# python3 + python3-pil -- composePreview.py (title/music PNG compositing)
# fluidsynth    -- renders the .midi to .wav for playback
# ffmpeg        -- .wav -> .mp3 for the browser <audio> player
# fluid-soundfont-gm -- provides /usr/share/sounds/sf2/FluidR3_GM.sf2,
#   the exact soundfont path lilypondCompiler.js's SOUNDFONT constant expects
# fonts-liberation -- provides the "Liberation Sans" family that the title/
#   subtitle/instrument-name markup blocks explicitly request via
#   \override #'(font-name . "Liberation Sans") -- without this package
#   installed, LilyPond silently falls back to whatever serif font
#   fontconfig resolves instead, which is why those labels rendered in a
#   mismatched serif font on the first deploy.
RUN apt-get update && apt-get install -y --no-install-recommends \
      lilypond \
      poppler-utils \
      python3 \
      python3-pil \
      fluidsynth \
      fluid-soundfont-gm \
      ffmpeg \
      fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Node deps first (separate layer) so a code-only change doesn't
# force a full npm install on every rebuild.
COPY package.json package-lock.json* ./
RUN npm install --omit=dev

COPY server ./server
COPY client ./client

# Render (and most PaaS hosts) injects PORT at runtime -- server.js already
# reads process.env.PORT with a local-dev fallback of 3000, so no change
# needed there.
ENV NODE_ENV=production
EXPOSE 3000

CMD ["node", "server/server.js"]
