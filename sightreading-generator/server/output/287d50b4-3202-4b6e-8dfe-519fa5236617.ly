\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
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
  \key f \major
  \time 3/4
  \tempo "Dolce"
  f''2.\(\pp |
  e''2 d''16 c''16 a'16 a'16 |
  bes'4 c''2 |
  bes'4 bes'4 bes'4\) |
  \break
  a'2\( d''4 |
  e''4 d''2 |
  c''4 d''4 a'16 bes'16 c''16 d''16 |
  f''2.\) |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 3/4
  f2. |
  f2. |
  bes2. |
  bes2. |
  \break
  f2. |
  c'2. |
  f2. |
  f2. |
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
  \midi { \tempo 4 = 92 }
}
