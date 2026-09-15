\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 6 — Reading" }
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
  \time 4/4
  \tempo "Risoluto"
  c''2-.\p d''4 e''8( f''8) |
  a'2.-. b'4 |
  c''8 c''8 c''4. d''8 e''8 f''8 |
  d''4.-. c''16( d''16) c''4 d''4 |
  \break
  c''4.-. b'8 c''4 c''8. d''16 |
  c''8 b'8 f'2-. g'4 |
  a'4 a'8 e''8 f''2-- |
  b'4.-. c''8 d''2-. |
  \break
  c''4 d''16 b'16 a'8 b'4. a'16 b'16 |
  c''4-. b'2 a'4-. |
  g'4-. a'4.-. b'8 c''4-. |
  d''4 c''4. d''8 b'8 a'8 |
  \break
  a'4-. b'2.-. |
  a'4-. g'8 f'8 a'4 b'4 |
  a'4.-. b'8 a'4 c''8 c''8 |
  b'8( c''16 b'16) c''4. c''8 c''4 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 4/4
  c4-. g4-. e4 g4-. |
  d4-. a4-. f4 a4 |
  c4 g4-. e4 g4-. |
  d4-. a4-. f4 a4 |
  \break
  c4 g4 e4-. g4-. |
  c4 g4 e4-. g4-. |
  d4-. a4 f4 a4 |
  g4-. d4 b4-. d4 |
  \break
  g4 d4 b4 d4-. |
  f4 c4 a4-. c4-. |
  g4 d4 b4-. d4 |
  g4-. d4 b4 d4 |
  \break
  d4 a4 f4-. a4 |
  d4 a4-. f4 a4 |
  f4-. c4 a4 c4-. |
  c4-. g4 e4-. g4 |
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
  \midi { \tempo 4 = 100 }
}
