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
  d'4 fis'2 g'4 |
  b'4 cis''8 d''8 cis''8 b'8 cis''4 |
  R1 |
  \break
  R1 |
  R1 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  b,4_\markup { \italic "soft" } a,4 a,4 a,8 a,8 |
  R1 |
  R1 |
  a8 g8 g4 fis4 e8 fis8 |
  \break
  g8 a8 g8 a8 e4 fis4 |
  e4 d4 d2 |
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
