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
  \time 2/4
  \tempo "Moderato, flowing"
  f''4\mp aes'4 |
  ges'4. aes'8 |
  f''4 ees''4 |
  r2 |
  \break
  aes'4. ges'16([ f'16)] |
  ges'4 bes'16([ aes'16 aes'16 des''16)] |
  c''4 bes'4 |
  ges'8[ f'16 c''16] des''4 |
  \break
  ees''16([ f''16 ees''8)] des''4 |
  des''8([ ees''16 ees''16)] des''4 |
  bes'8.[ aes'16] aes'4-. |
  ges'8[ f'8] ges'8[ aes'8] |
  \break
  ges'8[ aes'8] bes'4-. |
  des''2 |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 2/4
  des2-. |
  ees2 |
  des2 |
  ees2 |
  \break
  des2 |
  ges2 |
  aes2 |
  ges2 |
  \break
  aes2-. |
  des2 |
  des2 |
  ees2 |
  \break
  ees2 |
  des2 |
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
