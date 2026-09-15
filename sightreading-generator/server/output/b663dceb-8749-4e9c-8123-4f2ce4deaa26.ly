\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 1 — Reading" }
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
  \key d \major
  \time 4/4
  d'4 e'2 e'8 fis'8 |
  g'4 fis'8 g'8 a'8 fis'8 e'4 |
  R1 |
  R1 |
  \break
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  R1 |
  R1 |
  a4 g2 fis8 e8 |
  d4 e8 fis8 e8 fis8 g4 |
  \break
  d1 |
  g8 a8 g8 fis8 e4 d4 |
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
  \midi { \tempo 4 = 80 }
}
