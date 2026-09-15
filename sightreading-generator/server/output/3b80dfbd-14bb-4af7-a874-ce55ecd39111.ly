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
  \key a \minor
  \time 4/4
  \tempo "Adagio"
  r4\p d''8 e''8 d''2 |
  e''4 e''2 e''8 c''8 |
  c''8 e''8 d''8 e''8 d''2 |
  e''2 f''8( e''8 e''8 d''8) |
  \break
  e''4 e''2 d''8 c''8 |
  c''8( c''8 b'8 c''8) b'2 |
  b'4 a'8( a'8) b'4 a'8( b'8) |
  a'8( b'8) a'4 a'8( a'8) a'4 |
  \bar "|."
}

bassLine = {
  \key a \minor
  \time 4/4
  R1 |
  a1 |
  a1 |
  R1 |
  \break
  a1 |
  a1 |
  e1 |
  a1 |
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
