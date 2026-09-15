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
  f''8[\f ees''8] des''8[ c''8] f'4 |
  ges'8[ aes'8] bes'2 |
  c''2 des''4 |
  des''2 ees''4 |
  \break
  f''8[ ees''8] des''2 |
  ees''4 r2 |
  c''8([ bes'8)] bes'2 |
  c''2 bes'8[ aes'8] |
  \break
  f'2 ees'8[ ees'16 des'16] |
  ees'4. f'8 bes'4 |
  \bar "|."
}

bassLine = {
  \key bes \minor
  \time 3/4
  bes,4 f4 f4 |
  ees4 bes,4 bes,4 |
  f4 c4 c4 |
  bes,4 f4 f4 |
  \break
  bes,4 f4 f4 |
  ees4 bes,4 bes,4 |
  f4 c4 c4 |
  f4 c4 c4 |
  \break
  bes,4 f4 f4 |
  bes,4 f4 f4 |
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
