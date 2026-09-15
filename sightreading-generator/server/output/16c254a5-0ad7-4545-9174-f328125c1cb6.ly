\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 3 — Reading" }
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
  \time 3/4
  g'4\mp c''4. d''8 |
  e''8 e''8 fis''8 g''4 a''8 |
  g''8 fis''2 g''8 |
  a''2 a''8 g''8 |
  b''8 a''8 a''4 a''8 g''8 |
  fis''8 fis''4 fis''8 e''8 d''8 |
  e''2 d''4 |
  d''8 c''4 b'8 c''8 d''8 |
  c''8 e''8 fis''4 b''8 a''8 |
  g''2 g''4 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 3/4
  g4. d'4. |
  c'4. g4. |
  g4. d'4. |
  d'4. a4. |
  g4. d'4. |
  d'4. a4. |
  c'4. g4. |
  g4. d'4. |
  c'4. g4. |
  g4. d'4. |
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
  \midi { \tempo 4 = 88 }
}
