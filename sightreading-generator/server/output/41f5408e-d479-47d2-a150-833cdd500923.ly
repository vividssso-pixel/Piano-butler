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
  \key fis \minor
  \time 4/4
  \tempo "Allegretto"
  a'16(\mf e''8 e''8 d''16 e''8) a'4. b'8 |
  a'4 b'8( a'16 b'16 a'8 a'8) b'4 |
  cis''4 cis''8.( d''16) e''4 a'16( b'16 d''8) |
  e''16( cis''8 cis''8 e''16 d''8) d''4 e''4 |
  \break
  cis''2 d''4 e''8.( d''16) |
  b'2 a'4. b'16( cis''16) |
  e''4 d''2 cis''8.( d''16) |
  cis''4. b'16( cis''16 d''16 d''8 cis''8 cis''8 b'16) |
  \break
  a'8( b'16 cis''16) b'4. a'8( b'16 a'16 b'16 cis''16) |
  d''4. e''16( cis''8 d''8 cis''16) b'4 |
  a'4. b'16( cis''8 b'8 cis''8 b'8 cis''16) |
  d''8( e''16 d''16) e''4 d''4. cis''8 |
  \break
  b'4. a'8 b'4. a'8 |
  cis''4 b'8( cis''8 b'16 a'8 a'8 a'8 a'16) |
  \bar "|."
}

bassLine = {
  \key fis \minor
  \time 4/4
  fis4 cis'4 fis4 cis'4 |
  fis4 cis'4 fis4 cis'4 |
  fis4 cis'4 fis4 cis'4 |
  cis'4 gis4 cis'4 gis4 |
  \break
  cis'4 gis4 cis'4 gis4 |
  b4 fis4 b4 fis4 |
  cis'4 gis4 cis'4 gis4 |
  fis4 cis'4 fis4 cis'4 |
  \break
  fis4 cis'4 fis4 cis'4 |
  b4 fis4 b4 fis4 |
  fis4 cis'4 fis4 cis'4 |
  b4 fis4 b4 fis4 |
  \break
  b4 fis4 b4 fis4 |
  fis4 cis'4 fis4 cis'4 |
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
