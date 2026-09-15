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
  \time 4/4
  f'8 g'2 a'8 bes'8 a'8 |
  g'8 a'8 bes'2 a'4 |
  R1 |
  R1 |
  f'8 g'2 a'8 g'8 g'8 |
  a'8 g'8 f'2 f'4 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 4/4
  R1 |
  R1 |
  a8 f2 e8 f8 e8 |
  g8 a8 a2 g4 |
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
  \layout {}
  \midi { \tempo 4 = 80 }
}
