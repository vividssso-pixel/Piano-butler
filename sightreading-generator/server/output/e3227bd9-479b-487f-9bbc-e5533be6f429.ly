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
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Andante"
  f''2\pp e''4 f''4 |
  e''2 a'4 \tuplet 3/2 { bes'8 d''8 e''8 } |
  bes'4 c''4 d''4 d''4 |
  \tuplet 3/2 { e''8 d''8 c''8 } bes'4 c''2 |
  \break
  a'4 bes'4 d''2 |
  c''2. c''4 |
  d''4 e''4 f''4 f''4 |
  f''1 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  f1 |
  c'1 |
  bes1 |
  c'1 |
  \break
  f1 |
  f1 |
  bes1 |
  f1 |
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
