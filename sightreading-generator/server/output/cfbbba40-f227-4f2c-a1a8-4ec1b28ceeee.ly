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
  \tempo "Not too fast"
  ees''2.\p \tuplet 3/2 { ees''8( f''8 c''8) } |
  d''16 ees''16 f''16 ees''16 d''2. |
  c''2 bes'2 |
  f''4 ees''2 d''4 |
  \break
  ees''2 f''16( ees''16 ees''16 d''16) aes'4 |
  g'2 \tuplet 3/2 { aes'8 d''8 c''8 } bes'4 |
  bes'4 aes'2 bes'4 |
  c''4 ees''2. |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  aes2 ees2 |
  bes2 f2 |
  R1 |
  bes2 f2 |
  \break
  aes2 ees2 |
  ees2 bes2 |
  R1 |
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
