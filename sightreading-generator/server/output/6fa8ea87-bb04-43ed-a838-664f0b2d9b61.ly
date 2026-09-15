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
  \tempo "Dolce"
  f''2\mf e''4 f''4 |
  f''4 e''4 f''4 c''4 |
  bes'4 a'4 a'2 |
  e''2. f''4 |
  \break
  e''1 |
  d''1 |
  \tuplet 3/2 { c''8 bes'8 c''8 } bes'4 bes'2 |
  a'2 \tuplet 3/2 { c''8 d''8 e''8 } f''4 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  f2 c'2 |
  f2 c'2 |
  f2 c'2 |
  R1 |
  \break
  R1 |
  R1 |
  bes2 f2 |
  f2 c'2 |
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
