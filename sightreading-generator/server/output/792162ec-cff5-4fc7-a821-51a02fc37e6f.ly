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
  \tempo "Gently rocking"
  des''4.\p ees''8 f''4 |
  ees''8( ees''8 f''8) ees''4. |
  f''8( aes'16 ges'16 aes'8) bes'4 f'8 |
  ges'4. aes'8 aes'4 |
  \break
  aes'8( ges'8 f'16 bes'16) c''4. |
  r4 aes'8( bes'8 c''8 c''8) |
  des''8( c''8 ees''8 des''8 ees''8 f''8) |
  f''16( ees''16 f''8 bes'8) c''4 f''8 |
  \break
  f''4. des''4. |
  ees''8( c''8 bes'16 c''16 aes'8 bes'8 des''16 des''16) |
  des''8( c''8 des''8) ees''4. |
  ees''8( f''8 ees''8) des''4 c''8 |
  \break
  bes'4. c''8 bes'4 |
  aes'4 bes'8( c''8) des''4 |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  des4. aes4. |
  c'4. ees4. |
  des4. aes4. |
  f4. aes4. |
  \break
  des4. aes4. |
  bes4. des4. |
  aes4. ees4. |
  f4. aes4. |
  \break
  des4. aes4. |
  c'4. ees4. |
  des4. aes4. |
  c'4. ees4. |
  \break
  ges4. des4. |
  f4. aes4. |
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
