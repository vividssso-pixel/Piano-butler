\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 8 — Reading" }
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
  \time 9/8
  \tempo "Allegro giocoso"
  c''4\f d''8 f''8 e''8 d''8 e''8 f''4 |
  a'8 a'4 f'4 e'8( e'8 d''8 c''8) |
  d''8 c''4 d''4. f''4. |
  e''4. d''8 a'4 a'4 b'8 |
  \break
  a'8( b'8 c''8) d''4 c''8( d''8 e''8 d''8) |
  e''8( f''8 b'8 c''8 b'16 a'16 c''8) b'4. |
  c''4. c''8 d''4 d''4. |
  e''4 d''8 c''4. d''4. |
  \break
  c''8( d''8 e''16 d''16) c''4 c''8( b'8) c''4 |
  b'4 a'8 g'4 a'8 b'4 c''8 |
  b'4 c''8 c''8 d''8 f''16 e''16 f''4. |
  e''4. d''8 b'4 a'8 g'4 |
  \break
  a'4. g'8 f'4 e'8 g'4 |
  g'4 f'8( e'8 f'8 g'8 a'8 g'8 f'8) |
  a'8( b'16 c''16 d''8) e''4 d''8 b'4. |
  a'8 b'8 d''8 e''8 f''4 e''4. |
  \break
  d''8 d''16 e''16 f''8 e''4. d''8 b'4 |
  a'8 g'4 f'8 f'4 f'8 a'4 |
  g'4 g'8 a'8 g'4 b'8 c''8 a'8 |
  g'4. f'8 e'4 f'8 f'4 |
  \break
  f'4. e'4. f'4. |
  e'16( f'16 e'8 f'8 g'8) f'4 e'8 f'16 g'16 c''8 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 9/8
  c4. g4. e4. |
  e4. a4. e4. |
  f4. a4. d4. |
  e4. c4. e4. |
  \break
  d4. a4. f4. |
  e4. a4. e4. |
  a4. c4. f4. |
  g4. e4. g4. |
  \break
  c4. g4. e4. |
  d4. g4. d4. |
  a4. c4. f4. |
  d4. b4. d4. |
  \break
  c4. g4. e4. |
  g4. c4. g4. |
  f4. a4. d4. |
  a4. f4. a4. |
  \break
  g4. d4. b4. |
  a4. d4. a4. |
  b4. d4. g4. |
  g4. e4. g4. |
  \break
  d4. a4. f4. |
  g4. c4. g4. |
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
  \midi { \tempo 4. = 72 }
}
