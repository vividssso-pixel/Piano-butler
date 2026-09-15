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
  \time 4/4
  \tempo "Adagio"
  cis''2\f d''8( d''8 d''8 d''8) |
  cis''8 cis''8 cis''8 d''8 e''4 d''8( d''8) |
  r2 d''8( e''8 d''8 cis''8) |
  R1 |
  \break
  r2 d''2 |
  cis''4 d''8( cis''8 d''8 e''8) r4 |
  cis''2 d''4 cis''8( d''8) |
  cis''2 cis''4 cis''4 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 4/4
  d'1 |
  a1 |
  a1 |
  a1 |
  \break
  a1 |
  a1 |
  a1 |
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
  \midi { \tempo 4 = 88 }
}
