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
  \key bes \major
  \time 4/4
  \tempo "Cheekily"
  d''2\f ees''4. f''8~ |
  f''2 f''2 |
  ees''2 ees''2 |
  f''4. ees''8( d''16 ees''16 d''16 ees''16) d''4 |
  \break
  ees''4. d''8 ees''2 |
  \tuplet 3/2 { f''8 ees''8 d''8 } d''4 ees''4 f''4 |
  ees''16 ees''16 f''16 ees''16 d''2 d''16 d''16 ees''16 d''16 |
  ees''4. d''8 d''4. d''8 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 4/4
  bes4 c'4 d'4 ees'4 |
  R1 |
  ees'4 d'4 c'4 bes4 |
  bes4 c'4 d'4 ees'4 |
  \break
  ees'4 d'4 c'4 bes4 |
  bes4 bes4 bes4 bes4 |
  bes4 bes4 bes4 bes4 |
  bes4 bes4 bes4 bes4 |
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
