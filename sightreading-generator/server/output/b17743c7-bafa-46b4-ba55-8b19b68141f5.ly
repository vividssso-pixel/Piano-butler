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
  \key b \minor
  \time 4/4
  b'2\f_\markup { \italic "playfully" } cis''8( cis''8 d''8 cis''8) |
  d''2 b'8( b'8) cis''4 |
  d''2 cis''4 b'8 cis''8 |
  r4 e''4 d''8 b'8 cis''8 cis''8 |
  \break
  R1 |
  d''2^\markup { \italic "slowing" } cis''8( b'8) r4 |
  R1 |
  b'4 b'2. |
  \bar "|."
}

bassLine = {
  \key b \minor
  \time 4/4
  b2 r2 |
  b2 d2 |
  b2 d2 |
  e2 g2 |
  \break
  e2 g2 |
  b2 d2 |
  b2 d2 |
  b2 d2 |
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
