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
  \key c \major
  \time 2/4
  \tempo "Espressivo"
  c''2\p |
  d''8( b'8) c''4 |
  d''2 |
  d''2 |
  \break
  e''4. d''8 |
  a'2 |
  b'2 |
  c''4 c''8 c''8 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 2/4
  c2 |
  g2 |
  g2 |
  g2 |
  \break
  c2 |
  f2 |
  g2 |
  c2 |
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
