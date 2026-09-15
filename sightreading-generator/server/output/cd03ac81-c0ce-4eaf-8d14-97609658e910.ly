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
  f'4 d'2 e'4 |
  d'2 e'2 |
  d'4 e'2 f'4 |
  f'4 g'4 a'4 g'4 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 4/4
  f1 |
  g1 |
  g1 |
  f1 |
  \bar "|."
}

\score {
  \new PianoStaff <<
    \new Staff = "right" {
      \clef treble
      \melody
    }
    \new Staff = "left" {
      \clef bass
      \bassLine
    }
  >>
  \layout {}
  \midi { \tempo 4 = 76 }
}
