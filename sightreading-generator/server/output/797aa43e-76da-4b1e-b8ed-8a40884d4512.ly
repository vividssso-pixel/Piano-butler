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
  \tempo "Not too fast"
  f''4\mf f''4 e''2 |
  d''2. d''4 |
  c''4 e''4 f''4 \tuplet 3/2 { e''8 d''8 e''8 } |
  d''2 e''4 d''4 |
  \break
  e''4 f''4 e''4 d''4 |
  e''4 f''4 e''4 f''4 |
  c''4 bes'4 a'4 bes'4 |
  c''4 d''4 f''2 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  R1 |
  R1 |
  c'2 e'2 |
  bes2 d'2 |
  \break
  c'2 e'2 |
  R1 |
  f2 a2 |
  f2 a2 |
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
