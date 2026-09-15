\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 3 — Reading" }
  tagline = ##f
}

\paper {
  indent = 0
  ragged-bottom = ##t
  ragged-right = ##t
  top-margin = 6\mm
  bottom-margin = 6\mm
  left-margin = 8\mm
  right-margin = 8\mm
}

melody = {
  \key g \major
  \time 4/4
  \tempo "Espressivo"
  R1 |
  g'4 a'2 b'8 a'8 |
  g'8 a'4 b'2 a'8 |
  R1 |
  \break
  g'2 b'8 c''8 a'4 |
  a'2 b'2 |
  R1 |
  R1 |
  \break
  g'4 g'2 g'4 |
  g'2 g'4 g'8 g'8 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 4/4
  d4\f_\markup { \italic "playfully" } e8 fis4 e4. |
  R1 |
  R1 |
  a2 a4 g8 fis8 |
  \break
  R1 |
  R1 |
  a8 fis8 g4 g4 a8 g8 |
  a8 g4 a4 g4 a8 |
  \break
  R1 |
  R1 |
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
  \layout {
    \context {
      \Score
      \override SpacingSpanner.uniform-stretching = ##t
    }
  }
  \midi { \tempo 4 = 88 }
}
