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
  \time 3/4
  \tempo "Sweetly"
  cis''4\f d''2~ |
  d''2. |
  e''2 cis''4 |
  d''2 cis''4~ |
  \break
  cis''16( d''16 cis''16 d''16) cis''2 |
  d''16( e''16 d''16 cis''16) d''4 cis''4 |
  cis''4 cis''2 |
  cis''2. |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 3/4
  a2. |
  a2. |
  a2. |
  d'2. |
  \break
  r2. |
  d'2. |
  a2. |
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
  \midi { \tempo 4 = 92 }
}
