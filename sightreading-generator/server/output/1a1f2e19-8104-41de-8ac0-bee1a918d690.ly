\version "2.24.3"

\header {
  title = "Sight-Reading Excerpt"
  subtitle = "Grade 1 (Ember) — Technique"
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
}

melody = {
  \key a \minor
  \time 3/4
  d'8 c'2 d'8 |
  b'8 b'4 d'4 e'8 |
  f'8 e'4 e'4 f'8 |
  e'2 d'8 c'8 |
  b'4 c'2 |
  c'8 b'4 c'8 d'4 |
  b'4 d'2 |
}

bassLine = {
  \key a \minor
  \time 3/4
  d4. a'4. |
  e4. b'4. |
  d4. a'4. |
  a4. e4. |
  e4. b'4. |
  a4. e4. |
  e4. b'4. |
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
