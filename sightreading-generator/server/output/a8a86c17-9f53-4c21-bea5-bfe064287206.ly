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
  \key d \major
  \time 4/4
  \tempo "Espressivo"
  d''8(\f e''8) d''4\( cis''8( b'8) cis''4~ |
  cis''2 a'2 |
  b'4. a'8 b'4 a'4~ |
  a'4 g'8( b'8) b'4. b'8\) |
  \break
  cis''2\( d''2 |
  e''4 e''2 d''4 |
  d''2 d''4. e''8 |
  d''4 d''4 d''4. d''8\) |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  g4 g4 g4 g4 |
  g4 g4 g4 g4 |
  g4 g4 g4 g4 |
  g4 g4 a4 a4 |
  \break
  a4 a4 a4 a4 |
  a4 g4 e4 d4 |
  d4 d4 d4 d4 |
  d4 d4 d4 d4 |
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
