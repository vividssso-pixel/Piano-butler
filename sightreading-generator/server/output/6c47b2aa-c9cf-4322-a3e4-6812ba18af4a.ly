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
  \time 4/4
  \tempo "Moderato, flowing"
  b'2\mf c''8( e''8) d''4 |
  c''4 e''4. d''8 e''4 |
  d''4 d''2 e''4 |
  c''2 c''4 b'16 c''16 e''8 |
  \break
  d''2 c''4 d''8 d''16 e''16 |
  c''2 \tuplet 3/2 { d''8 b'8 b'8 } c''4 |
  r2 b'4 c''8 b'16 c''16 |
  e''8 d''8 d''4 e''4. d''8 |
  \break
  c''4 b'4. c''16( b'16) c''4 |
  b'2 c''4. b'8 |
  b'4 e''8 d''16 e''16 d''4 c''4 |
  d''4 e''4 c''4 b'4 |
  \break
  c''2 b'4 c''4 |
  b'4. b'8 b'2 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 4/4
  g1 |
  b,2 c8 e8 d4 |
  c4 e4. d8 e4 |
  d4 d2 e4 |
  \break
  c2 c4 b,16 c16 e8 |
  d2 c4 d8 d16 e16 |
  c2 d4 c4 |
  c2 b,4 c8 b,16 c16 |
  \break
  e8 d8 d4 e4. d8 |
  c4 b,4. c16 b,16 c4 |
  b,2 c4. b,8 |
  b,4 e8 d16 e16 d4 c4 |
  \break
  d4 e4 c4 b,4 |
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
  \midi { \tempo 4 = 96 }
}
