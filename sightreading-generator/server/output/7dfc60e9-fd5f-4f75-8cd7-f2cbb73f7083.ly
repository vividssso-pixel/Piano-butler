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
  \key a \major
  \time 4/4
  \tempo "Flowing"
  cis''4-.\mf d''8 b'8 a'4 b'4-. |
  cis''4-. b'4-. cis''2-. |
  d''16( a'16 a'8) d''4 cis''4-. b'8 cis''8 |
  d''4.-. cis''8 d''4. e''8 |
  \break
  d''8 e''8 b'4. a'16( b'16) a'4 |
  b'4 b'2-. \tuplet 3/2 { cis''8 b'8 cis''8 } |
  d''4-. cis''2-. b'4-. |
  a'2-. b'4-. a'4-. |
  \break
  b'8 cis''16 b'16 a'4 b'2 |
  d''4.-. cis''16 b'16 cis''16 d''16 cis''8 b'4-. |
  cis''4 d''4.-. cis''8 b'4 |
  cis''4-. b'2. |
  \break
  cis''8 b'16 a'16 b'4-. cis''2 |
  d''4. b'8 b'4 a'4-. |
  b'4 cis''4.-. e''8 d''4 |
  cis''4-. b'2 a'4 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 4/4
  a4-. e4 cis4-. e4-. |
  a4 e4 cis4 e4 |
  d4 a4-. fis4 a4 |
  d4-. a4 fis4 a4-. |
  \break
  d4-. a4-. fis4-. a4-. |
  e4 b4-. gis4 b4-. |
  b4-. fis4-. d4-. fis4-. |
  a4 e4 cis4-. e4-. |
  \break
  b4 fis4-. d4-. fis4-. |
  b4 fis4 d4-. fis4 |
  a4-. e4 cis4 e4 |
  a4-. e4 cis4-. e4-. |
  \break
  a4 e4 cis4 e4-. |
  b4 fis4 d4 fis4-. |
  e4-. b4-. gis4 b4 |
  a4 e4 cis4 e4 |
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
