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
  \key d \major
  \time 4/4
  \tempo "March"
  d''2\mp e''2 |
  a'4. b'8( b'16 cis''16 d''8) a'4 |
  a'2 g'16 a'16 b'8 cis''4 |
  R1 |
  \break
  cis''4 d''16 cis''16 d''16 e''16 d''4 e''8( d''8) |
  e''8 d''8 d''8 d''8 cis''4 b'4 |
  cis''4 d''16 e''16 d''8 e''2 |
  cis''4 d''4 cis''8 d''8 cis''4 |
  \break
  d''8. cis''16 d''4 d''4 cis''4 |
  b'8. b'16 cis''4. e''8 d''4 |
  cis''4 d''2 e''8. cis''16 |
  b'4 d''16 e''16 d''8 d''4 d''4 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  d,2 a,2 |
  d,2 a,2 |
  a,2 e,2 |
  e,2 b,2 |
  \break
  a,2 e,2 |
  g,2 d,2 |
  a,2 e,2 |
  a,2 e,2 |
  \break
  d,2 a,2 |
  e,2 b,2 |
  a,2 e,2 |
  d,2 a,2 |
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
