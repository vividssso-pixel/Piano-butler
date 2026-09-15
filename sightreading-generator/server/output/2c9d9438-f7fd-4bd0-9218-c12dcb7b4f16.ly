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
  \tempo "Allegretto"
  des''2\p ees''4. ees''16( des''16) |
  c''4 bes'4. ees''8 f''4 |
  r2 f''4 des''4 |
  ees''8( bes'8 c''8 bes'16 aes'16) r4 c''4 |
  \break
  des''8 des''8 ees''4 bes'2 |
  aes'4 ges'4 f'4. ges'8 |
  aes'2 ges'8 c''8 bes'4 |
  aes'4 ges'8.( f'16) ges'4 f'4 |
  \break
  ges'4 aes'2 r4 |
  aes'4. c''8 r4 c''8.( ees''16) |
  f''4. des''8 ees''4. f''8 |
  ees''4. c''8 c''2 |
  \break
  bes'8 aes'8 f'2 ges'4 |
  f'2 ges'8 aes'8 bes'8 des''8 |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 4/4
  des4 aes4 des4 aes4 |
  aes4 ees4 aes4 ees4 |
  des4 aes4 des4 aes4 |
  aes4 ees4 aes4 ees4 |
  \break
  ges4 des4 ges4 des4 |
  des4 aes4 des4 aes4 |
  aes4 ees4 aes4 ees4 |
  des4 aes4 des4 aes4 |
  \break
  ges4 des4 ges4 des4 |
  aes4 ees4 aes4 ees4 |
  des4 aes4 des4 aes4 |
  aes4 ees4 aes4 ees4 |
  \break
  ges4 des4 ges4 des4 |
  des4 aes4 des4 aes4 |
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
