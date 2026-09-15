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
  \tempo "Waltz"
  des''4\(\f des''4 ees''8.([ des''16)] |
  ees''16([ ees''8 f''8] des''8[ ees''8] f''8[ des''16)] |
  ees''8([ f''8)] ees''2 |
  f''2 ees''4 |
  \break
  f''8([ des''8] ees''16[ ees''8 ees''8] des''8[ ees''16)]\) |
  des''2\( ees''8([ des''8)] |
  ees''8([ des''8)] ees''4. des''8 |
  ees''4 ees''2 |
  \break
  des''8([ ees''8] f''8[ f''16 ees''8] f''8[ f''16)] |
  f''2 f''4\) |
  \bar "|."
}

bassLine = {
  \key bes \minor
  \time 3/4
  bes4 f'4 f'4 |
  bes4 f'4 f'4 |
  ees'4 bes4 bes4 |
  f'4 c'4 c'4 |
  \break
  bes4 f'4 f'4 |
  bes4 f'4 f'4 |
  ees'4 bes4 bes4 |
  ees'4 bes4 bes4 |
  \break
  bes4 f'4 f'4 |
  bes4 f'4 f'4 |
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
