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
  \key ees \minor
  \time 2/4
  \tempo "Allegretto"
  ees''8([\pp des''8)] ces'4 |
  d''8([ d''8] \tuplet 3/2 { ees''8 f''8 aes'8) } |
  ges'4 aes'4 |
  ees''8([ des''16 des''16)] ees''4 |
  \break
  d''2 |
  ces'2 |
  d''2 |
  ees''16([ des''16 ees''8)] des''4 |
  \break
  ces'4 des''4 |
  ees''4 f''16([ ces'16 bes'8)] |
  d''4 ees''16([ d''16 ees''16 ees''16)] |
  f''16([ f''16 aes'8)] aes'4 |
  \break
  aes'4 des''8.([ ces'16)] |
  bes'4 ces'4 |
  d''16([ f''16 ees''8)] d''4 |
  ees''8([ des''16 ces'16)] bes'4 |
  \break
  ces'4. ces'8 |
  bes'4 aes'16([ bes'16 ces'16 ees''16)] |
  \bar "|."
}

bassLine = {
  \key ees \minor
  \time 2/4
  aes4 ees4 |
  bes4 f4 |
  ees4 bes4 |
  ees4 bes4 |
  \break
  bes4 f4 |
  aes4 ees4 |
  bes4 f4 |
  ees4 bes4 |
  \break
  aes4 ees4 |
  aes4 ees4 |
  bes4 f4 |
  bes4 f4 |
  \break
  aes4 ees4 |
  bes4 f4 |
  bes4 f4 |
  ees4 bes4 |
  \break
  aes4 ees4 |
  ees4 bes4 |
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
