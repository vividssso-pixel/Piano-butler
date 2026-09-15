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
  \key f \minor
  \time 3/4
  \tempo "Flowing"
  f''4.\p ees''8 des''4 |
  c''4 bes'4 c''4 |
  bes'2 bes'4 |
  aes'4. bes'8 des''4 |
  \break
  des''4 des''2 |
  c''4. bes'8 c''4 |
  e''4 f''4 des''8([ c''8)] |
  c''2 bes'4 |
  \break
  \tuplet 3/2 { aes'8 bes'8 c''8 } ees''4 des''4 |
  bes'4 c''8[ ees''16 f''16] f''4 |
  e''4. e''8 f''4 |
  des''4 ees''4 des''4 |
  \break
  e''4 des''4. c''8 |
  des''4 e''8.([ e''16)] e''4 |
  e''4 des''4. e''8 |
  \tuplet 3/2 { ees''8 des''8 des''8 } e''4 f''8( f''8) |
  \bar "|."
}

bassLine = {
  \key f \minor
  \time 3/4
  bes,2. |
  c2. |
  bes,2. |
  des2. |
  \break
  bes,2. |
  c2. |
  c2. |
  c2. |
  \break
  f,2. |
  bes,2. |
  c2. |
  bes,2. |
  \break
  c2. |
  c2. |
  c2. |
  f,2. |
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
