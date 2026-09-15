\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 7 — Reading" }
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
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Tempo di Gavotte"
  c''4\f d''8( e''16 e''16) d''4. c''16( b'16) |
  c''4 b'8( c''8) d''2 |
  b'16( c''16 c''8 d''16 c''8 b'16) f''4 f''8( f''8) |
  e''2 d''4 e''16( e''16 d''16 d''16) |
  \break
  c''8( b'8) a'4 b'4. b'8 |
  a'2 b'8( c''8 d''16 e''16 d''8) |
  c''2. e''16( d''16 c''16 b'16) |
  b'4 a'16( g'16 f'16 g'16) f'4 e'8( f'8) |
  \break
  e'2 g'4 f'4 |
  g'2 f'2 |
  e'8( f'8 g'16 f'16 e'8) f'4 \tuplet 3/2 { g'8( f'8 e'8) } |
  f'8 g'4 f'16( g'16) g'4 a'16( b'16 a'16 g'16) |
  \break
  g'8( f'8 e'8 f'8) g'2 |
  a'16( g'16) g'4. a'8( g'16 f'16 g'8 f'8) |
  g'2 f'16( e'16) f'4. |
  e'4. f'8 g'4. b'8 |
  \break
  c''16( d''16) b'4 a'16( f'16) g'4 f'4 |
  g'4 f'4 f'4. e'8 |
  f'2 g'2 |
  a'16( b'16) a'4 g'8( f'16 f'16) g'4 f'8 |
  \break
  e'2 e'4 f'8( g'16 f'16) |
  e'8 f'4. g'4 a'8( c''8) |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  c4 g4 e4 g4 |
  c4 g4 e4 g4 |
  f4 c4 a4 c4 |
  c4 g4 e4 g4 |
  \break
  f4 c4 a4 c4 |
  d4 a4 f4 a4 |
  c4 g4 e4 g4 |
  d4 a4 f4 a4 |
  \break
  c4 g4 e4 g4 |
  c4 g4 e4 g4 |
  c4 g4 e4 g4 |
  d4 a4 f4 a4 |
  \break
  c4 g4 e4 g4 |
  d4 a4 f4 a4 |
  c4 g4 e4 g4 |
  c4 g4 e4 g4 |
  \break
  f4 c4 a4 c4 |
  c4 g4 e4 g4 |
  d4 a4 f4 a4 |
  d4 a4 f4 a4 |
  \break
  c4 g4 e4 g4 |
  c4 g4 e4 g4 |
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
  \midi { \tempo 4 = 104 }
}
