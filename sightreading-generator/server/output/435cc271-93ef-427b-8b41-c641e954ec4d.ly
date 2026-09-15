\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Preliminary (Spark) — Rhythm"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key a \minor
  \time 4/4
  d'4 c'4 b'4 c'4 |
  d'2 c'4 b'4 |
  c'2 d'2 |
  d'4 b'4 c'4 b'4 |
}

\score {
  \new Staff \with { instrumentName = "Piano" } {
    \clef treble
    \melody
  }
  \layout {}
}
