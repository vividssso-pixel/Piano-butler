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
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Dolce"
  d''8(\mp ees''8 d''8) ees''4. |
  d''4. ees''8 d''4 |
  ees''4 f''8 ees''8 d''16 ees''16 d''8 |
  ees''4. d''4. |
  \break
  ees''4 ees''8 d''4. |
  f''8 ees''8 f''8 ees''4. |
  f''8 f''8 ees''8 f''8 f''8 f''8 |
  f''4. f''4. |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  bes2. |
  d8 ees8 d8 ees4. |
  d4. ees8 d4 |
  ees4 f8 ees8 d16 ees16 d8 |
  \break
  ees4. d4. |
  ees4 ees8 d4. |
  f8 ees8 f8 ees4. |
  bes2. |
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
  \midi { \tempo 4. = 61 }
}
