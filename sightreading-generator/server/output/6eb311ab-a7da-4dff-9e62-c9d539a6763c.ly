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
  \key c \major
  \time 4/4
  f'4 e'4 d'4 e'4 |
  d'4 e'2 f'4 |
  e'2 f'4 g'4 |
}

\score {
  \new Staff \with { instrumentName = "Piano" } {
    \clef treble
    \melody
  }
  \layout {}
}
