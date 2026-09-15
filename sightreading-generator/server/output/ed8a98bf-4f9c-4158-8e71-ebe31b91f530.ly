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
  \key c \minor
  \time 4/4
  ees''4\(\p d''4 c''8 d''8 r4 |
  c''4 aes'2. |
  g'8( f'8) f'4 g'2 |
  c''8( c''8) c''4 c''4 g'8 aes'8\) |
  \break
  g'2.\( r4 |
  f'4 g'4 g'2 |
  f'4 aes'8( g'8 aes'8 bes'8) aes'4 |
  f'4 g'2\) aes'8( c''8) |
  \bar "|."
}

bassLine = {
  \key c \minor
  \time 4/4
  c1 |
  f1 |
  g1 |
  R1 |
  \break
  c1 |
  c1 |
  f1 |
  c1 |
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
