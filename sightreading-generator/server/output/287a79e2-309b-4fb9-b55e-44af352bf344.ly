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
  \key aes \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Andante"
  c''1\(\mf |
  c''2 c''4 des''4 |
  des''2 ees''4 f''4 |
  ees''4 ees''4 ees''2\) |
  \break
  c''2\( des''4 c''4 |
  ees''4 des''4 f''2 |
  ees''4 des''4 c''2 |
  c''4 f''4 \tuplet 3/2 { ees''8( f''8 f''8) } f''4\) |
  \bar "|."
}

bassLine = {
  \key aes \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  aes2 c'2 |
  aes2 c'2 |
  des'2 f'2 |
  aes2 c'2 |
  \break
  aes2 c'2 |
  aes2 c'2 |
  aes2 c'2 |
  aes2 c'2 |
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
