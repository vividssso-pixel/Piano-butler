\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Grade 2 (Flame) — Technique"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key a \minor
  \time 3/4
  d'8 c'2 b'8 |
  a'8 a'4 b'8 e'8 f'8 |
  f'4 e'2 |
  e'8 d'8 b'8 a'4. |
  c'2 b'8 c'8 |
  d'8 c'4 c'4 d'8 |
  a'2 b'8 c'8 |
  b'8 b'2 a'8 |
}

bassLine = {
  \key a \minor
  \time 3/4
  d4 a'4 d4 |
  a4 e4 a4 |
  d4 a'4 d4 |
  a4 e4 a4 |
  a4 e4 a4 |
  d4 a'4 d4 |
  a4 e4 a4 |
  e4 b'4 e4 |
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
