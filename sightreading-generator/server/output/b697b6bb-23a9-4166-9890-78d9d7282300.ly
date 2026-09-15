\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Preliminary — Reading" }
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
  #(define fonts
    (make-pango-font-tree "Liberation Sans" "Liberation Sans" "Liberation Mono" (/ staff-height pt 20)))
}

melody = {
  \key a \minor
  \time 4/4
  a'2 b'4 a'4 |
  b'4 c''4 d''4 c''4 |
  R1 |
  R1 |
  a'2 b'4 b'4 |
  c''4 b'4 a'4 a'4 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 4/4
  R1 |
  R1 |
  f2 e4 d4 |
  e4 d4 e4 f4 |
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
  \midi { \tempo 4 = 76 }
}
