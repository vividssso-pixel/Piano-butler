\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 7 — Reading" }
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
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Tempo di Gavotte"
  des''4\mf ees''8( des''8 ces'8) des''4. |
  ees''16( ees''16) f''4 ees''16( ges'16) aes'4 f''8( ees''16 des''16) |
  ees''4 des''8( ces'8) des''4 ees''8( ees''16 f''16) |
  des''4 ees''8( des''16 ees''16) f''2 |
  \break
  des''16( ces'16) des''4. ees''2 |
  des''8( ees''8) f''4 aes'4. ges'8 |
  des''2. ces'8( des''8) |
  ees''4. aes'8 ges'4 aes'8( ges'16 aes'16) |
  \break
  bes'2 ces'8( bes'8 ces'8 bes'16 ces'16) |
  des''2 ees''8( f''16 ees''16 f''8 ees''8) |
  ees''4 des''8( ces'16 aes'16) ges'2 |
  ges'2 ges'2 |
  \break
  aes'16( ces'16 bes'8 aes'16 bes'8 ces'16) bes'4 bes'8( ces'8) |
  ces'2. ces'8( des''8) |
  ees''2 ees''16( f''16) ees''4. |
  f''2. ees''4 |
  \break
  des''8( ees''8 f''16 ees''16 des''8) des''2 |
  ees''2 ees''8 des''4 ees''8 |
  f''4 ees''16( f''16 ees''8) f''4. ees''8 |
  f''2. \tuplet 3/2 { ees''8( f''8 ees''8) } |
  \break
  des''4. ces'16( bes'16 aes'8 ges'8) ges'4 |
  ges'2. ges'4 |
  \bar "|."
}

bassLine = {
  \key ges \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  ges,4 des4 bes,4 des4 |
  aes,4 ees4 ces,4 ees4 |
  aes,4 ees4 ces,4 ees4 |
  des4 aes,4 f4 aes,4 |
  \break
  ges,4 des4 bes,4 des4 |
  des4 aes,4 f4 aes,4 |
  ges,4 des4 bes,4 des4 |
  aes,4 ees4 ces,4 ees4 |
  \break
  ges,4 des4 bes,4 des4 |
  des4 aes,4 f4 aes,4 |
  aes,4 ees4 ces,4 ees4 |
  ges,4 des4 bes,4 des4 |
  \break
  aes,4 ees4 ces,4 ees4 |
  aes,4 ees4 ces,4 ees4 |
  aes,4 ees4 ces,4 ees4 |
  des4 aes,4 f4 aes,4 |
  \break
  des4 aes,4 f4 aes,4 |
  aes,4 ees4 ces,4 ees4 |
  des4 aes,4 f4 aes,4 |
  des4 aes,4 f4 aes,4 |
  \break
  ges,4 des4 bes,4 des4 |
  ges,4 des4 bes,4 des4 |
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
  \midi { \tempo 4 = 104 }
}
