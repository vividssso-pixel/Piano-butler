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
  \time 3/4
  \tempo "Corrente"
  f''2\mp ees''8[ c''8] |
  des''4 bes'4. aes'8 |
  f''4 ees''4. des''8 |
  ges'8([ f'8)] ges'4 aes'8.([ bes'16)] |
  \break
  c''16([ bes'16 aes'8)] ges'4. f'16[ ges'16] |
  c''4 des''4 ees''4 |
  des''4. ees''8 f''4 |
  ees''4 des''8[ ees''8] des''16[ ees''16 des''8] |
  \break
  c''2 bes'4 |
  bes'4 c''8([ des''8)] des''4 |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 3/4
  des4 des4 des4 |
  des4 des4 des4 |
  des4 f4 ges4 |
  ges4 aes4 aes4 |
  \break
  aes4 aes4 aes4 |
  aes4 f4 des4 |
  des4 f4 aes4 |
  aes4 aes4 aes4 |
  \break
  aes4 aes4 ges4 |
  des4 des4 des4 |
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
