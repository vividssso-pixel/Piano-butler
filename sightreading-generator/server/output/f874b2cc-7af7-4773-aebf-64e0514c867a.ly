\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 2 — Reading" }
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
  R1 |
  R1 |
  d'8 e'8 d'2 e'8 fis'8 |
  R1 |
  \break
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  d4._\markup { \italic "loudly" } cis8 d4 d4 |
  a,4 b,2 a,8 g,8 |
  R1 |
  a4. g8 g4 fis4 |
  \break
  fis2 e4 d8 d8 |
  d4 e8 fis8 e8 d8 d4 |
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
  \midi { \tempo 4 = 84 }
}
