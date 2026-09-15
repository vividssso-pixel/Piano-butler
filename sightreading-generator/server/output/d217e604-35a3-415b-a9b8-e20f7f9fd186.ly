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
  \key bes \major
  \time 2/4
  \tempo "Moderato"
  d''8(\mf d''8) ees''4 |
  f''2 |
  ees''8( d''8) ees''4-. |
  ees''2 |
  \break
  d''2 |
  ees''8( d''8) ees''4-. |
  d''2 |
  d''4 d''4 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 2/4
  bes2 |
  bes2 |
  ees'2 |
  ees'2 |
  \break
  bes2 |
  ees'2 |
  bes2 |
  bes2 |
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
