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
  \time 4/4
  \tempo "Daintily"
  ees''4.\(\pp f''8 ees''4 f''16 c''16 d''16 ees''16 |
  c''4 c''2 aes'4 |
  g'2 c''2~ |
  c''2. c''4\) |
  \break
  d''4\( c''4 c''4. ees''8 |
  f''2. ees''4 |
  d''16 c''16 aes'16 g'16 bes'2. |
  c''4 d''4 ees''4. ees''8\) |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  aes,2 ees,2 |
  aes,2 ees,2 |
  R1 |
  bes,2 f,2 |
  \break
  aes,2 ees,2 |
  bes,2 f,2 |
  bes,2 f,2 |
  ees,2 bes,2 |
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
