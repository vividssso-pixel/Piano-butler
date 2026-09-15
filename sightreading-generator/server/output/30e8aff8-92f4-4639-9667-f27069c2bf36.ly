\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
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
  \time 3/4
  \tempo "Moderato"
  d''4\pp e''4 d''4 |
  cis''4 b'4 a'4 |
  a'4 a'4 g'4 |
  a'4 g'2 |
  \break
  fis'16( g'16 fis'16 b'16) cis''4 b'4 |
  a'2 b'4 |
  cis''2 d''4 |
  d''2. |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 3/4
  d4 a4 d4 |
  a4 e4 a4 |
  a4 e4 a4 |
  a4 e4 a4 |
  \break
  d4 a4 d4 |
  d4 a4 d4 |
  a4 e4 a4 |
  d4 a4 d4 |
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
  \midi { \tempo 4 = 92 }
}
