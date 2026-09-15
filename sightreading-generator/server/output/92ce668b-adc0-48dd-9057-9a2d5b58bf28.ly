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
  f'4 g'4 a'4 b'4 |
  b'2 a'4 g'4 |
  a'2 g'4 b'4 |
  g'2 a'2 |
}

bassLine = {
  \key c \major
  \time 4/4
  f1 |
  g1 |
  f1 |
  c1 |
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
}
