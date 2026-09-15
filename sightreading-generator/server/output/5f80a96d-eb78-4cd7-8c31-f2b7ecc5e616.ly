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
  d'4 e'4 f'4 e'4 |
  d'2 e'4 d'4 |
  c'4 d'4 c'2 |
  b'2 c'4 d'4 |
  e'2 f'2 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 4/4
  d1 |
  d1 |
  a1 |
  e1 |
  a1 |
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
