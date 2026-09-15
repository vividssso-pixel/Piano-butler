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
  \tempo "Slow march"
  des''16([\f ees''8 f''8] ees''8[ f''16)] |
  f''4-. \tuplet 3/2 { ees''8( f''8 ees''8) } |
  f''8([ aes'16 bes'16)] f'4-. |
  ges'4-. c''16([ des''8 f'16)] |
  \break
  R2 |
  bes'4.-. bes'8 |
  c''16([ bes'16 c''16 ees''8] des''8[ ees''16)] |
  aes'4-. bes'8([ c''8)] |
  \break
  des''4-. c''4-. |
  des''4-. c''16([ aes'16 ges'16 f'16)] |
  f'8([ ges'8] ges'8[ f'8)] |
  ges'8.([ aes'16)] des''4-. |
  \bar "|."
}

bassLine = {
  \key des \major
  \time 2/4
  des4-. aes4-. |
  des4-. aes4-. |
  des4-. aes4-. |
  ges4-. des4-. |
  \break
  aes4-. ees4-. |
  ges4-. des4-. |
  aes4-. ees4-. |
  aes4-. ees4-. |
  \break
  des4-. aes4-. |
  des4-. aes4-. |
  des4-. aes4-. |
  des4-. aes4-. |
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
