\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Grade 4 (Blaze) — Reading"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key a \minor
  \time 3/4
  \tempo "Allegro"
  d'2\p g'4 |
  f'8. e'8. d'4 e'8 |
  d'4 d'4. c'8 |
  b'4. a'4. |
  a'2 c'4 |
  g'4 f'4 f'4 |
  g'8 a''4 g'4 g'8 |
  g'4 a''8 g'8. a''8 a''8 |
  g'4. f'4 g'8 |
  f'2 g'4 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 3/4
  d4 a'4 f4 |
  d4 a'4 f4 |
  d4 a'4 f4 |
  e4 b'4 g4 |
  a4 e4 c4 |
  e4 b'4 g4 |
  e4 b'4 g4 |
  e2.~ e16 |
  e4 b'4 g4 |
  d4 a'4 f4 |
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
  \midi { \tempo 4 = 92 }
}
