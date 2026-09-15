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
  \time 4/4
  \tempo "Cheekily"
  f''4\f e''2 e''4 |
  f''4 e''4 d''4 c''4 |
  bes'4 a'2. |
  c''2 c''4 c''4 |
  \break
  f''4 e''2 d''4 |
  c''4 bes'4 bes'2 |
  bes'2. c''4 |
  d''2. f''4 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 4/4
  f1 |
  f,4 e2 e4 |
  f,4 e4 d4 c4 |
  bes,4 a,2. |
  \break
  c2 c4 c4 |
  f,4 e2 d4 |
  c4 bes,4 bes,2 |
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
