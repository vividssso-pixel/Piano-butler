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
  \time 2/4
  R2 |
  a'4 b'4 |
  R2 |
  a'4. a'8 |
  \break
  c''8 d''8 d''4 |
  R2 |
  R2 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 2/4
  c4\f d4 |
  R2 |
  a8 g4. |
  R2 |
  \break
  R2 |
  a2 |
  a8 a4 a8 |
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
