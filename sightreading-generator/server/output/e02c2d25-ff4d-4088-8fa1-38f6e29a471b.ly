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
  \key c \major
  \time 2/2
  \tempo "Tempo comodo"
  c''4\p f'4 g'2 |
  c''8. b'4. c''8 d''8. e''8 |
  c''4 b'2 c''4 |
  b'2 c''4 d''4 |
  \break
  e''8 f''8. e''4 f''8 e''8. f''8 |
  c''4 d''4 e''4 d''8 e''8 |
  d''8 b'4 c''2 b'8 |
  c''8 b'2 c''8 c''8 c''8 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 2/2
  c4 g4 c4 g4 |
  c4 g4 c4 g4 |
  c4 g4 c4 g4 |
  g4 d4 g4 d4 |
  \break
  c4 g4 c4 g4 |
  c4 g4 c4 g4 |
  g4 d4 g4 d4 |
  c4 g4 c4 g4 |
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
