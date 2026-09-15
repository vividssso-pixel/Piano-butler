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
  \key a \major
  \time 2/2
  \tempo "Allegretto"
  cis''2\mf cis''16 d''4. cis''16 |
  cis''2 d''8( e''8) d''4 |
  e''2 e''4 d''16( cis''8.) |
  d''4. d''8 cis''2 |
  \break
  d''4. cis''8( d''8) cis''4. |
  d''2 cis''8( d''16) e''4 d''16 |
  e''8.( e''16) d''4. cis''8.( d''8 cis''16) |
  d''8. cis''4 cis''16 cis''4 cis''4 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 2/2
  a1 |
  cis2 cis16 d4. cis16 |
  cis2 d8 e8 d4 |
  e2 e4 d16 cis8. |
  \break
  d4. d8 cis2 |
  d4. cis8 d8 cis4. |
  d2 cis8 d16 e4 d16 |
  a1 |
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
