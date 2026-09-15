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
  \time 3/4
  \tempo "Flowing"
  f''2\p ges'4 |
  \tuplet 3/2 { aes'8 bes'8 aes'8 } bes'4 f''4 |
  ees''2 des''4 |
  ees''4. aes'8 ges'4 |
  \break
  aes'8([ ges'8)] c''4 des''4 |
  f''4. ees''8 des''4 |
  f''8([ ees''16 bes'16)] c''2 |
  bes'4 c''2 |
  \break
  bes'2 c''4 |
  bes'4. bes'16([ aes'16)] bes'4 |
  aes'16[ bes'16 aes'16 bes'16] aes'4 bes'8([ c''8)] |
  des''2. |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 3/4
  des4 aes4 f4 |
  aes4 des4 aes4 |
  ges4 bes4 ees4 |
  ees4 c4 ees4 |
  \break
  des4 aes4 f4 |
  aes4 des4 aes4 |
  des4 f4 bes4 |
  bes4 ges4 bes4 |
  \break
  ees4 bes4 ges4 |
  bes4 ees4 bes4 |
  c4 ees4 aes4 |
  aes4 f4 aes4 |
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
