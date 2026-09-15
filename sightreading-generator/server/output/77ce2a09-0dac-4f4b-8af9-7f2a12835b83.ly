\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Preliminary (Spark) — Reading"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key a \minor
  \time 4/4
  d'2 c'4 d'4 |
  d'4 f'4 g'2 |
}

\score {
  \new Staff \with { instrumentName = "Piano" } {
    \clef treble
    \melody
  }
  \layout {}
}
