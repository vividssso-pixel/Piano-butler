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
  \key g \major
  \time 2/4
  R2 |
  R2 |
  R2 |
  R2 |
  \break
  g'4 a'4 |
  b'4 d''8 c''8 |
  d''4 c''4 |
  d''8 d''8 d''4 |
  \break
  R2 |
  R2 |
  R2 |
  R2 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 2/4
  d4 c4 |
  a,4 g,8 a,8 |
  a,4 a,4 |
  g,8 a,8 g,4 |
  \break
  R2 |
  R2 |
  R2 |
  R2 |
  \break
  a4 g4 |
  fis4 e8 g8 |
  fis4 fis4 |
  g8 g8 g4 |
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
