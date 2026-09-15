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
  \key aes \major
  \time 3/4
  \tempo "Valse lente"
  ees''4\mp des''4 c''8[ des''8] |
  c''2. |
  des''8.([ bes'16)] c''2 |
  bes'4 aes'16[ bes'16 aes'8] bes'4 |
  \break
  bes'8[ aes'8] bes'4. aes'8 |
  bes'4 c''2 |
  c''2 des''8.([ c''16)] |
  des''16[ c''16 bes'8] c''4 des''4 |
  \break
  aes'4 bes'8[ bes'8] aes'4 |
  des''4 ees''4 f''16([ bes'16 c''8)] |
  des''4 c''4 \tuplet 3/2 { bes'8( c''8 c''8) } |
  des''4. ees''8 f''4 |
  \break
  ees''4. des''8 c''4 |
  bes'4 c''4 bes'4 |
  aes'2. |
  bes'4 aes'8[ c''8] bes'4 |
  \break
  bes'4. bes'8 aes'4 |
  bes'4 aes'4 aes'8([ aes'8)] |
  \bar "|."
}

bassLine = {
  \key aes \major
  \time 3/4
  aes,4 ees4 ees4 |
  aes,4 ees4 ees4 |
  bes,4 f4 f4 |
  ees4 bes,4 bes,4 |
  \break
  ees4 bes,4 bes,4 |
  ees4 bes,4 bes,4 |
  aes,4 ees4 ees4 |
  bes,4 f4 f4 |
  \break
  ees4 bes,4 bes,4 |
  bes,4 f4 f4 |
  bes,4 f4 f4 |
  bes,4 f4 f4 |
  \break
  aes,4 ees4 ees4 |
  bes,4 f4 f4 |
  aes,4 ees4 ees4 |
  bes,4 f4 f4 |
  \break
  ees4 bes,4 bes,4 |
  aes,4 ees4 ees4 |
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
