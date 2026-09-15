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
  \key g \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  \tempo "Moderato grazioso"
  b'2\mf d'4. e'16( c'16) |
  b2 c'4 d'4 |
  c'16( d'16) a'4 b'8 d''2 |
  e''4. d''16 a'16 g'2 |
  \break
  d''2. d''4 |
  e''8 d''4. \tuplet 3/2 { c''8( d''8 c''8) } d''4 |
  e''4 d''4 e''4. e''8 |
  d''4. e''8 c''4 d''4 |
  \break
  c''4. b'8 c''4 d''4 |
  e''16 d''16 e''4. c''4 d''4 |
  e''8 e''4 e''16 d''16 c''16 b'16 c''4 d''8 |
  e''16( d''16 b'8 b'8 d''8) e''4. c''8 |
  \break
  b'4 c''4 d''8( c''8 b'16 a'16 c''8) |
  b'16( d''16 e''16 d''16) e''4 c''4. d''16 c''16 |
  b'4 a'8 a'8 b'16 c''16 c''4 d''16 c''16 |
  b'16( a'16) b'4 a'8 g'16 fis'16 e'8 d'4 |
  \break
  c'16 c'16 b8 b16 b8 c'16 b4. c'8 |
  b4 c'16 d'16 e'8 g'2 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 2/2
  \set Timing.baseMoment = #(ly:make-moment 1/4)
  \set Timing.beatStructure = #'(1 1 1 1)
  g1 |
  b,2 d4. e16 c16 |
  b,2 c4 d4 |
  c16 d16 a,4 b,8 d2 |
  \break
  e4. d16 a,16 g,2 |
  d2. d4 |
  e8 d4. c4 d4 |
  e4 d4 e4. e8 |
  \break
  d4. e8 c4 d4 |
  c4. b,8 c4 d4 |
  e16 d16 e4. c4 d4 |
  e8 e4 e16 d16 c16 b,16 c4 d8 |
  \break
  e16 d16 b,8 b,8 d8 e4. c8 |
  b,4 c4 d8 c8 b,16 a,16 c8 |
  b,16 d16 e16 d16 e4 c4. d16 c16 |
  b,4 a,8 a,8 b,16 c16 c4 d16 c16 |
  \break
  b,16 a,16 b,4 a,8 g,16 fis16 e8 d4 |
  g1 |
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
