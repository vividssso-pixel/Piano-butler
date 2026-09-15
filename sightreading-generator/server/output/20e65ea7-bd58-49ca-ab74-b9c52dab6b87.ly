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
  cis''2-.\p_\markup { \italic "gentle" } e''4-. |
  d''4-. cis''2-. |
  cis''2-. e''8( d''8) |
  e''2-. d''8( e''8) |
  \break
  d''4.-. e''8 d''4-. |
  e''8( d''8) d''2-. |
  cis''8( d''8) cis''2-. |
  cis''4-. cis''2-. |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 3/4
  a2.-. |
  d'2.-. |
  a2.-. |
  a2.-. |
  \break
  d'2.-. |
  d'2.-. |
  a2.-. |
  a2.-. |
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
