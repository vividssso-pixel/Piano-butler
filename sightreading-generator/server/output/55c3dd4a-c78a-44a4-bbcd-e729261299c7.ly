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
  \tempo "Allegretto"
  f''4.\mf ees''8 |
  f''8.[ ees''16] f''4 |
  ees''4 bes'4 |
  aes'8([ ges'8)] f'4 |
  \break
  ges'8([ c''8)] c''4 |
  bes'2 |
  c''8[ bes'8] r4 |
  des''8.[ des''16] des''4 |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 2/4
  des4 aes4 |
  des4 aes4 |
  aes4 ees4 |
  des4 aes4 |
  \break
  ges4 des4 |
  ges4 des4 |
  aes4 ees4 |
  des4 aes4 |
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
