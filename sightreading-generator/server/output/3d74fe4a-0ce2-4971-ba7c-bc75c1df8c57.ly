\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 5 — Reading" }
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
  \key g \major
  \time 9/8
  \tempo "Moderato, flowing"
  b'8\mp c''8 b'8 c''8 c''4 d''4 e''8 |
  R1*9/8 |
  d''8 e''16 b'16 c''8 e''8 e''4 d''8 c''4 |
  d''8 c''4 b'8( c''8 d''8 e''8) d''4 |
  \break
  b'4 b'8 c''4 b'8 c''8 d''8 c''16 b'16 |
  c''8 b'4 c''4 d''8( d''8 e''16 d''16 c''8) |
  c''4 d''8 e''4 d''8 d''4. |
  c''4 d''8( c''8) b'4 c''16 c''16 d''8 e''8 |
  \break
  d''8 r4 e''8( d''8 e''8) d''4. |
  d''4. c''8 b'4 c''4. |
  b'4 b'8 c''4 b'8( c''8 b'8 c''8) |
  d''4. b'4 c''8 c''4 d''8 |
  \break
  c''4 b'8 c''8 b'8 c''8 b'8 c''8 d''8 |
  d''4. d''16 b'16 c''8 d''8 e''8 e''8 e''8 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 9/8
  g4. d'4. g4. |
  g4. d'4. g4. |
  c'4. g4. c'4. |
  g4. d'4. g4. |
  \break
  g4. d'4. g4. |
  c'4. g4. c'4. |
  d'4. a4. d'4. |
  c'4. g4. c'4. |
  \break
  d'4. a4. d'4. |
  g4. d'4. g4. |
  g4. d'4. g4. |
  g4. d'4. g4. |
  \break
  c'4. g4. c'4. |
  g4. d'4. g4. |
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
  \midi { \tempo 4. = 64 }
}
