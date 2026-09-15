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
  \time 3/4
  \tempo "Waltz time"
  f''4\mf c''4 c''4 |
  e''4 f''2 |
  e''2 d''8 c''8 |
  f''2 e''4 |
  \break
  d''8 d''8 f''4 f''4 |
  e''8 d''8 c''2 |
  bes'4 c''4. d''8 |
  e''2 f''8 f''8 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 3/4
  f4 c'4 c'4 |
  c'4 g4 g4 |
  c'4 g4 g4 |
  f4 c'4 c'4 |
  \break
  bes4 f4 f4 |
  c'4 g4 g4 |
  bes4 f4 f4 |
  bes4 f4 f4 |
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
