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
  \key e \minor
  \time 2/4
  e''2\mf |
  e''4 d''4 |
  d''4 c''4 |
  b'4 a'8 b'8 |
  b'8 a'4. |
  b'2 |
  c''4. b'8 |
  a'2 |
  g'4. g'8 |
  a'8 b'8 e''4 |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 2/4
  e4 b4 |
  e4 b4 |
  b4 fis4 |
  e4 b4 |
  e4 b4 |
  e4 b4 |
  a4 e4 |
  a4 e4 |
  e4 b4 |
  a4 e4 |
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
