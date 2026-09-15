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
  \key g \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Tempo di Gavotte"
  g'4\mp a'8( b'16 c''16) d''4 e''16( d''16 e''8) |
  g'4 a'16( b'16 a'16 b'16) a'2 |
  b'8( a'8 d''8 c''8) d''4 e''16( d''16 c''8) |
  b'8 a'4 c''16( d''16) e''4 b'4 |
  \break
  c''16( b'16) c''4 d''8 d''4 a'4 |
  b'2 c''8( b'8 c''8 d''16 e''16) |
  d''8( c''8) b'4 g'4. a'16( b'16) |
  c''4 b'4 a'4. b'16( c''16) |
  \break
  c''4 d''4 d''8( e''8) d''4 |
  b'4 a'16( b'16 c''8) d''4 d''8( e''16 e''16) |
  d''4. e''16( d''16) c''4. e''8 |
  d''4 e''8( d''16 c''16) d''4. d''8 |
  \break
  e''4 d''8( b'8 c''8) b'4 a'8 |
  a'8 g'4. a'2 |
  b'8( a'16 g'16) a'4 g'4 a'4 |
  g'16( a'16) g'4 a'8( b'16 a'16 g'8) g'4 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  g,4 d4 g,4 d4 |
  g,4 d4 g,4 d4 |
  g,4 d4 g,4 d4 |
  e4 b,4 e4 b,4 |
  \break
  a,4 e4 a,4 e4 |
  g,4 d4 g,4 d4 |
  g,4 d4 g,4 d4 |
  a,4 e4 a,4 e4 |
  \break
  d4 a,4 d4 a,4 |
  g,4 d4 g,4 d4 |
  g,4 d4 g,4 d4 |
  g,4 d4 g,4 d4 |
  \break
  a,4 e4 a,4 e4 |
  d4 a,4 d4 a,4 |
  g,4 d4 g,4 d4 |
  g,4 d4 g,4 d4 |
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
