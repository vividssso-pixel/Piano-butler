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
  \key aes \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Allegretto"
  aes'2-.\f ees''4 f''8 f''8 |
  f''2 c''4. des''8 |
  c''16 des''16 bes'16 c''16 c''4 des''4 des''4 |
  ees''4 des''8( c''16 c''16) bes'2-. |
  \break
  c''8 des''4.-. ees''4 c''16 bes'16 c''16 bes'16 |
  aes'2-. bes'16 aes'16 bes'16 aes'16 bes'4 |
  aes'4 c''4 bes'4 des''16 c''16 des''8 |
  c''2.-. bes'8 bes'16 c''16 |
  \break
  des''4. c''8( bes'8) aes'4 bes'8 |
  bes'4 aes'4 bes'4-. aes'16( bes'16 c''16 bes'16) |
  c''8 bes'4 aes'16 c''16 bes'4 aes'16 bes'16 c''8 |
  bes'16 c''16 bes'8 aes'16 aes'8 aes'16 aes'4. aes'8 |
  \bar "|."
}

bassLine = {
  \key aes \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  des4 aes4 f4 aes4-. |
  des4-. aes4-. f4 aes4-. |
  aes4 ees4 c4 ees4 |
  aes4 ees4 c4-. ees4 |
  \break
  aes4 ees4 c4-. ees4 |
  des4-. aes4 f4 aes4 |
  des4 aes4 f4 aes4-. |
  aes4 ees4 c4 ees4 |
  \break
  bes4-. f4 des4-. f4 |
  ees4 bes4 g4-. bes4 |
  aes4 ees4 c4-. ees4 |
  aes4 ees4-. c4 ees4-. |
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
  \midi { \tempo 4 = 100 }
}
