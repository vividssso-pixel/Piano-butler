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
  \key des \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Flowing"
  des''4\mp ees''8( des''8 c''8 c''8) |
  des''8 ees''8 f''8 ees''4.-. |
  aes'16 bes'16 c''8 ees''8 f''8 ees''8 des''8 |
  aes'4. aes'4 bes'8 |
  \break
  aes'4. aes'8 bes'4 |
  bes'4. bes'4. |
  aes'8 bes'4-. ges'4. |
  f'4.-. aes'8( bes'8 des''8) |
  \break
  ees''4 f''8 ees''4.-. |
  bes'4. aes'4. |
  bes'8 ges'8 aes'8 ges'8 ges'4 |
  f'4.-. ges'16( aes'16 bes'8 c''8) |
  \break
  c''4. des''4. |
  c''4. des''4-. c''8 |
  des''8 ees''8 des''8 c''8 des''4-. |
  c''4. des''8 ees''4-. |
  \break
  des''4 c''8( bes'8 c''8 bes'8) |
  aes'8 bes'8 aes'8 ges'4 ges'8 |
  aes'4-. ges'8 ges'4. |
  ges'8 ges'4 aes'8 bes'8 c''16 des''16 |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  des4. aes4. |
  des4. aes4. |
  aes4. ees4. |
  des4. aes4. |
  \break
  des4. aes4. |
  ees4. bes4. |
  aes4. ees4. |
  des4. aes4. |
  \break
  ees4. bes4. |
  aes4. ees4. |
  ees4. bes4. |
  des4. aes4. |
  \break
  aes4. ees4. |
  aes4. ees4. |
  des4. aes4. |
  aes4. ees4. |
  \break
  ges4. des4. |
  aes4. ees4. |
  des4. aes4. |
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
  \midi { \tempo 4. = 67 }
}
