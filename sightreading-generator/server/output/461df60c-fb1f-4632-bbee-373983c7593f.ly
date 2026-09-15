\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 3 — Reading" }
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
  \key g \minor
  \time 4/4
  R1 |
  g'4\f g'2 c''4 |
  bes'2 r4 c''4 |
  R1 |
  \break
  c''2. bes'8( a'8) |
  R1^\markup { \italic "slowing" } |
  c''4 bes'2 c''4 |
  bes'4 a'2 g'4 |
  \bar "|."
}

bassLine = {
  \key g \minor
  \time 4/4
  g1 |
  c1 |
  g1 |
  d1 |
  \break
  c1 |
  d1 |
  c1 |
  g1 |
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
  \midi { \tempo 4 = 88 }
}
