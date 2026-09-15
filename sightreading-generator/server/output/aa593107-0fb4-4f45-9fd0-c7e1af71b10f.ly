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
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  \tempo "Moderato Pastorale"
  b'4.-.\p c''8 d''4-. |
  c''8 d''4-. e''8( d''8 d''16 d''16) |
  b'8 r4 b'8( c''16 d''16 c''8) |
  b'4-. c''8( d''8) c''4-. |
  \break
  d''8 e''4-. e''8( b'8 c''8) |
  d''4-. c''8 c''4-. c''8 |
  d''16( c''16 b'8 d''8 c''8 b'8 c''8) |
  R2. |
  \break
  c''4-. c''8( c''8) b'4-. |
  c''4.-. b'8 b'4-. |
  c''16( d''16 c''8 b'8) c''4-. b'8 |
  R2. |
  \break
  c''8( b'16 c''16 b'8) c''4.-. |
  b'4.-. b'8 b'4-. |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 6/8
  \set Timing.baseMoment = #(ly:make-moment 1/8)
  \set Timing.beatStructure = #'(3 3)
  g4. d'4. |
  b4. d'4. |
  g4. d'4. |
  b4. d'4. |
  \break
  g4. d'4. |
  e'4. g4. |
  g4. d'4. |
  b4. d'4. |
  \break
  c'4. g4. |
  e'4. g4. |
  c'4. g4. |
  e'4. g4. |
  \break
  c'4. g4. |
  b4. d'4. |
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
