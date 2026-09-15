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
  \time 4/4
  e''8\mf d''4. e''4. c''8 |
  c''4 b'4 e''4. d''8 |
  c''2 e''4. d''8 |
  c''2 d''4 c''4 |
  \break
  d''2 e''4. d''8 |
  e''2 e''4. e''8 |
  \bar "|."
}

bassLine = {
  \key e \minor
  \time 4/4
  a2 e2 |
  a2 e2 |
  a2 e2 |
  a2 e2 |
  \break
  b2 fis2 |
  e2 b2 |
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
