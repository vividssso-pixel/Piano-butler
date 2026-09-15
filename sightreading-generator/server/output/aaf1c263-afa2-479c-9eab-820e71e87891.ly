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
  \key b \minor
  \time 4/4
  b'8 cis''8 b'4 cis''2 |
  cis''4 b'2 cis''8 b'8 |
  cis''4 d''4 cis''2 |
  R1 |
  \break
  R1 |
  R1 |
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key b \minor
  \time 4/4
  R1 |
  R1 |
  R1 |
  a8 g8 a4 g2 |
  \break
  fis4 fis2 e8 e8 |
  d4 fis4 e2 |
  b,1 |
  e4 fis8 g8 fis8 e8 b,4 |
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
