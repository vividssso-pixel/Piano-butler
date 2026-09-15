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
  \time 4/4
  \tempo "Romanze"
  f''2\(\p des''8 c''8 c''4 |
  des''8 c''8 des''4 ees''2 |
  aes'4 bes'4 ees''16 f''8 bes'16 c''8 bes'8 |
  aes'8( ees''8 des''8 ees''8) f''4. ees''8\) |
  \break
  des''2\( c''8( des''8) c''4 |
  bes'8 aes'8 bes'4. ees''16 f''8 ees''8 f''16 |
  ees''2 f''2 |
  ees''8( des''8) des''4 des''2\) |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 4/4
  des2 f2 |
  des2 f2 |
  aes2 c'2 |
  aes2 c'2 |
  \break
  des2 f2 |
  des2 f2 |
  aes2 c'2 |
  des2 f2 |
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
  \midi { \tempo 4 = 96 }
}
