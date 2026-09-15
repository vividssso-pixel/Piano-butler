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
  \tempo "Daintily"
  ees''2\mp d''2 |
  ees''2 f''4 ees''4 |
  d''4 ees''4 d''4 c''4 |
  aes'4 bes'4 c''2 |
  \break
  aes'4 g'4 aes'2 |
  aes'2 c''4 bes'4~ |
  bes'4 aes'4 \tuplet 3/2 { g'8( c''8 d''8) } c''4 |
  d''2 ees''4 ees''4 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  ees1 |
  ees1 |
  bes1 |
  aes1 |
  \break
  aes1 |
  R1 |
  aes1 |
  ees1 |
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
