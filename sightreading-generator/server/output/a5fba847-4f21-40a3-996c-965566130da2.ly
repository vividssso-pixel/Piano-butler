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
  d''16\p cis''16 d''8 e''4-. d''16( d''16 cis''8) b'4 |
  fis'4 fis'8( cis''8) b'2 |
  cis''2 b'8 g'8 a'16 b'16 cis''8 |
  b'4 d''16( e''16 d''8) a'4.-. g'8 |
  \break
  a'8 g'8 fis'4 g'2-. |
  fis'4. g'8 a'2-. |
  b'16 d''16 e''16 d''16 e''4-. d''4-. d''4-. |
  cis''4 d''2-. cis''8 b'16 cis''16 |
  \break
  d''4-. e''16 d''16 e''8 d''4. cis''16( a'16) |
  g'4-. g'4. a'8 g'4 |
  a'4 g'4 fis'8( g'16 fis'16) g'4 |
  b'4 cis''2 d''4 |
  \break
  cis''4 cis''4. d''8 cis''8 d''8 |
  cis''8 cis''8 b'4.-. a'8 b'16 cis''16 d''8 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  g4-. d4 g4 d4 |
  d4-. a4-. d4 a4-. |
  a4 e4 a4 e4 |
  g4-. d4 g4 d4-. |
  \break
  d4-. a4 d4-. a4 |
  d4-. a4 d4 a4-. |
  g4 d4 g4-. d4-. |
  a4-. e4-. a4-. e4-. |
  \break
  d4 a4 d4 a4-. |
  g4 d4 g4 d4-. |
  d4-. a4 d4-. a4 |
  g4 d4-. g4-. d4 |
  \break
  a4-. e4-. a4 e4 |
  d4 a4 d4 a4 |
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
