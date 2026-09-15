\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 6 — Reading" }
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
  \key ges \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Tarantella"
  ges'4.\mp ges'8 aes'4 |
  ces'8( bes'8 aes'8) bes'4. |
  ces'8( des''8 ees''8 bes'8) ces'4 |
  ees''8( f''8 f''8 ees''8 f''8 ees''8) |
  \break
  des''4. ees''4. |
  des''4. ees''16 des''16 des''8 ces'8 |
  des''8 ees''8 f''8 ees''8 ees''8 f''16 ces'16 |
  des''4 ees''8 f''16 ees''16 f''8 ees''8 |
  \break
  f''8 ees''4 ces'8( des''16 ees''16 des''8) |
  ees''8 f''4 ees''4. |
  f''8( ees''8 f''16 ees''16 f''8 ees''8 f''8) |
  ees''8 f''4 ees''8 des''4 |
  \break
  ees''8 des''4 ces'16 des''16 ees''8 f''8 |
  ees''4 f''8 ees''8 des''4 |
  ees''8 f''8 ees''8 des''8 ces'16 bes'16 ges'8 |
  aes'16 ges'16 aes'8 ges'8 ges'4 ges'8 |
  \bar "|."
}

bassLine = {
  \key ges \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  ges4. des4. |
  ces4. ees4. |
  aes4. ees4. |
  ces4. ees4. |
  \break
  des4. aes4. |
  bes4. des4. |
  aes4. ees4. |
  f4. aes4. |
  \break
  des4. aes4. |
  ces4. ees4. |
  des4. aes4. |
  ces4. ees4. |
  \break
  aes4. ees4. |
  ces4. ees4. |
  ces4. ges4. |
  bes4. des4. |
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
  \midi { \tempo 4. = 67 }
}
