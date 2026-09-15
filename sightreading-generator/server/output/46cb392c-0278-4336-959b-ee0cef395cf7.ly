\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 5 — Reading" }
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
  \key bes \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Gigue"
  des''8\mp des''4 des''4. |
  ees''8( ees''8 f''8) ees''4 des''8 |
  des''4. ees''4. |
  f''16( ees''16 des''8 des''8) ees''4. |
  \break
  f''8( f''8 ees''16 des''16) des''4 ees''8 |
  f''4. ees''8( des''8 ees''8) |
  des''4. des''4 ees''8 |
  des''4. ees''4. |
  \break
  des''16( ees''16 des''8 f''8) r4 f''8 |
  ees''8 des''4 ees''8( des''8 ees''8) |
  f''8 ees''4 des''4 ees''8 |
  f''8 ees''4 des''8( des''8 des''8) |
  \bar "|."
}

bassLine = {
  \key bes \minor
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  bes4. f'4. |
  ees'4. bes4. |
  bes4. f'4. |
  bes4. f'4. |
  \break
  bes4. f'4. |
  bes4. f'4. |
  bes4. f'4. |
  bes4. f'4. |
  \break
  bes4. f'4. |
  ees'4. bes4. |
  bes4. f'4. |
  bes4. f'4. |
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
  \midi { \tempo 4. = 64 }
}
