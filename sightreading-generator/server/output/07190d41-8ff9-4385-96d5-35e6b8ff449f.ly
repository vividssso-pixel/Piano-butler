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
  \key bes \minor
  \time 3/4
  \tempo "Canon"
  des''4\f ees''2 |
  ees''8[ des''8] des''4 ees''4 |
  des''8.([ ees''16)] ees''4 des''16[ ees''16 f''16 ees''16] |
  f''8([ ees''16 ees''16)] f''2 |
  \break
  ees''16[ des''16 des''8] r2 |
  des''4 des''8([ des''8] ees''8[ des''8)] |
  ees''4. ees''16([ des''16)] des''4 |
  des''4 des''2 |
  \bar "|."
}

bassLine = {
  \key bes \minor
  \time 3/4
  bes2. |
  des4 ees2 |
  ees8 des8 des4 ees4 |
  des8. ees16 ees4 des16 ees16 f16 ees16 |
  \break
  f8 ees16 ees16 f2 |
  ees16 des16 des8 ees2 |
  des4 des8 des8 ees8 des8 |
  bes2. |
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
