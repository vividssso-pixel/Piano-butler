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
  \time 4/4
  \tempo "Dolce"
  d''4\mf d''2. |
  g'2. fis'4 |
  g'2. d''4 |
  e''2 d''2 |
  \break
  cis''2 d''2 |
  b'2 cis''2 |
  a'4 g'4 fis'2 |
  g'4 a'4 d''2 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  R1 |
  R1 |
  g4 g4 a4 a4 |
  a4 a4 a4 a4 |
  \break
  R1 |
  g4 fis4 e4 r4 |
  d4 e4 fis4 g4 |
  d4 d4 d4 d4 |
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
