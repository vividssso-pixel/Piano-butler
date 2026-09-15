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
  \time 2/4
  \tempo "Canon"
  des''8.[\mf des''16] ees''4 |
  f''2 |
  ees''4 f''4 |
  des''8([ ees''8)] des''4 |
  \break
  des''16[ ees''16 des''16 ees''16] r4 |
  f''16[ f''16 des''8] ees''4 |
  f''4. f''16([ ees''16)] |
  f''2 |
  \break
  ees''4 des''4 |
  ees''16([ des''16 ees''16 des''16)] ees''4 |
  ees''16([ des''16 des''8)] ees''4 |
  f''4 ees''16[ f''16 ees''8] |
  \break
  des''4 ees''16[ des''16 ees''8] |
  f''4 ees''16[ des''16 des''16 des''16] |
  \bar "|."
}

bassLine = {
  \key bes \minor
  \time 2/4
  bes2 |
  des8. des16 ees4 |
  f2 |
  ees4 f4 |
  \break
  des8 ees8 des4 |
  des16 ees16 des16 ees16 f4 |
  f16 f16 des8 ees4 |
  f4. f16 ees16 |
  \break
  f2 |
  ees4 des4 |
  ees16 des16 ees16 des16 ees4 |
  ees16 des16 des8 ees4 |
  \break
  f4 ees16 f16 ees8 |
  bes2 |
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
