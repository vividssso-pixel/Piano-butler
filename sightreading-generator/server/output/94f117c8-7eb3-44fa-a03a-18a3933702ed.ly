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
  \time 3/4
  b'4 cis''8 b'8 b'8 cis''8 |
  d''4 cis''4 b'8 d''8 |
  cis''4 d''8 d''8 d''4 |
  R2. |
  \break
  R2. |
  R2. |
  R2. |
  R2. |
  \bar "|."
}

bassLine = {
  \key b \minor
  \time 3/4
  R2. |
  R2. |
  R2. |
  a4 g8 e8 d8 e8 |
  \break
  d4 cis4 d8 e8 |
  d4 e8 fis8 e4 |
  b,2. |
  e4 d4 b,4 |
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
