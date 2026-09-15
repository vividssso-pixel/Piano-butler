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
  \time 3/4
  \tempo "Allegretto"
  d''2\mp d''4 |
  ees''4 d''4 ees''4 |
  d''2 \tuplet 3/2 { ees''8 f''8 ees''8 } |
  d''2. |
  \break
  ees''2 f''4 |
  f''2. |
  d''2. |
  d''4 d''4 d''4 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 3/4
  bes4 d'4 ees'4 |
  ees'4 d'4 bes4 |
  bes4 bes4 bes4 |
  bes4 d'4 r4 |
  \break
  ees'4 d'4 bes4 |
  bes4 bes4 bes4 |
  R2. |
  bes4 bes4 bes4 |
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
