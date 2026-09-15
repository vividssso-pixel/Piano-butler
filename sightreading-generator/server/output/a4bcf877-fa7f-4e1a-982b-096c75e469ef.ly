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
  \time 4/4
  \tempo "Moderato grazioso"
  f''4.\f ees''8 f''4 ees''8 ees''8 |
  f''2 c''4 bes'4 |
  c''8.( des''16) ges'4 f'2 |
  ges'2. ges'4 |
  \break
  f'2 des''2 |
  c''4 des''2 bes'4 |
  aes'2 \tuplet 3/2 { bes'8 aes'8 ges'8 } ges'4 |
  aes'2. des''4 |
  \break
  des''4. c''8 bes'2 |
  aes'2 ges'8.( aes'16) bes'4 |
  ees''4 des''2 ees''4 |
  des''2 des''4 des''4 |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 4/4
  des4 aes4 des4 aes4 |
  bes4 f4 bes4 f4 |
  ges4 des4 ges4 des4 |
  ges4 des4 ges4 des4 |
  \break
  des4 aes4 des4 aes4 |
  aes4 ees4 aes4 ees4 |
  des4 aes4 des4 aes4 |
  des4 aes4 des4 aes4 |
  \break
  ges4 des4 ges4 des4 |
  aes4 ees4 aes4 ees4 |
  aes4 ees4 aes4 ees4 |
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
  \midi { \tempo 4 = 100 }
}
