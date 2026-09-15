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
  \key f \major
  \time 2/4
  f'2 |
  a'8 bes'4 a'8 |
  R2 |
  R2 |
  f'2 |
  f'8 f'4 f'8 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 2/4
  R2 |
  R2 |
  e2 |
  d8 d4 d8 |
  R2 |
  R2 |
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
  \layout {}
  \midi { \tempo 4 = 80 }
}
