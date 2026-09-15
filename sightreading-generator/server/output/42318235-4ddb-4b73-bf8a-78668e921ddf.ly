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
  \key ees \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Cheekily"
  ees''4\mp bes'4 c''4 \tuplet 3/2 { d''8 c''8 d''8 } |
  ees''2 f''4 ees''4 |
  f''2 ees''2 |
  d''4 g'4 aes'2 |
  \break
  aes'4 g'4 d''4 ees''4 |
  c''4 d''4 d''4 c''4 |
  bes'2. aes'4 |
  bes'2 c''4 ees''4 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  aes2 ees2 |
  R1 |
  bes2 f2 |
  bes2 f2 |
  \break
  aes2 ees2 |
  aes2 ees2 |
  bes2 f2 |
  ees2 bes2 |
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
