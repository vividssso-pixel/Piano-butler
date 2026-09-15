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
  \key gis \minor
  \time 3/4
  \tempo "Corrente"
  gis'4\(\p cis''4 b'8[ cis''8] |
  dis''4 cis''4 b'4 |
  cis''4 b'4 cis''4 |
  b'4. cis''8 b'4\) |
  \break
  ais'4.\( gis'8 cis''8[ b'8] |
  b'2 b'4 |
  gis'4 ais'4 gis'8([ ais'8)] |
  gis'4. gis'8 gis'4\) |
  \bar "|."
}

bassLine = {
  \key gis \minor
  \time 3/4
  cis4 e4 gis4 |
  gis4 e4 cis4 |
  cis4 e4 gis4 |
  gis4 gis4 gis4 |
  \break
  gis4 gis4 gis4 |
  gis4 gis4 gis4 |
  cis4 cis4 cis4 |
  gis4 gis4 gis4 |
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
