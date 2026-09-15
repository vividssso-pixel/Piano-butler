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
  \tempo "Romanze"
  d''8.\mf e''16 d''4 e''4 e''4 |
  d''2 e''4. d''16( cis''16) |
  d''2 cis''4. g'8 |
  fis'4. g'8 fis'4 a'4 |
  \break
  R1 |
  d''4 cis''8 d''16 cis''16 g'4 fis'4 |
  r2 a'2 |
  b'4. cis''8 d''4 cis''4 |
  \break
  d''2 d''4. e''8 |
  d''4 r4 d''16( cis''16 d''8) cis''4 |
  b'4. cis''8 b'4. a'8 |
  b'4 cis''4 d''2 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  d2 fis2 |
  d2 fis2 |
  g2 b2 |
  d2 fis2 |
  \break
  e2 g2 |
  d2 fis2 |
  e2 g2 |
  g2 b2 |
  \break
  g2 b2 |
  g2 b2 |
  e2 g2 |
  d2 fis2 |
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
