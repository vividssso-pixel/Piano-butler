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
  \key des \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Moderato, flowing"
  f''8(\mf ees''8 ees''8) f''4 bes'8 |
  aes'8 f''4 ees''16( ges'16 f'8 f'8) |
  ges'8( f'8 ges'16 des''16) des''4 ees''8 |
  bes'4. c''4. |
  \break
  des''8( c''8 bes'8) des''4. |
  c''4 des''8 f''4. |
  ees''4. r4 ees''8 |
  des''16( ees''16 f''8 ees''8 des''8 c''8 bes'8) |
  \break
  aes'16( ges'16 aes'8 bes'8 ges'8) r4 |
  ges'4. ges'8 f'4 |
  ges'4 f'8 ges'4 aes'8 |
  bes'4 aes'8 ges'4 f'8 |
  \break
  ges'8( aes'8 bes'8) aes'4. |
  bes'4. c''8 des''4 |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  des4. aes4. |
  des4. aes4. |
  ges4. des4. |
  ges4. des4. |
  \break
  ges4. des4. |
  aes4. ees4. |
  aes4. ees4. |
  des4. aes4. |
  \break
  des4. aes4. |
  ges4. des4. |
  ges4. des4. |
  ges4. des4. |
  \break
  ges4. des4. |
  des4. aes4. |
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
