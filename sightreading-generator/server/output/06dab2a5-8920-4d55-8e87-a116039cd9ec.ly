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
  \key a \minor
  \time 4/4
  a'8\mp b'4 b'8 a'8 c''4 d''8 |
  R1 |
  R1 |
  a'8 c''2 d''8 f''8 g''8 |
  a''4 a''4. a''4 a''8 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 4/4
  R1 |
  g4 g4 e4 f4 |
  g4 d4. d8 e4 |
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
  \midi { \tempo 4 = 88 }
}
