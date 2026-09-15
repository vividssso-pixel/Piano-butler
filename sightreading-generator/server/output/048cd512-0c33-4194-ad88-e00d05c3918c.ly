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
  \key a \major
  \time 3/4
  cis''4-.\mp_\markup { \italic "sweetly" } d''8 cis''8 d''4-. |
  e''4-. d''4-. d''4-. |
  e''4-. d''8 cis''8 d''4-. |
  e''2-. d''8 e''8 |
  \break
  d''4-. e''8 d''8 e''4-. |
  d''2-. e''8 d''8 |
  cis''8 d''8 cis''2-. |
  cis''4-. cis''2-. |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 3/4
  a2. |
  cis4 d8 cis8 d4 |
  e4 d4 d4 |
  e4 d8 cis8 d4 |
  \break
  e2 d8 e8 |
  d4 e8 d8 e4 |
  d2 e8 d8 |
  a2. |
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
  \midi { \tempo 4 = 88 }
}
