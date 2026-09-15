\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
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
  \key e \major
  \time 2/2
  \tempo "Cantabile"
  e''4.\mp cis''16 b'4 a'8( cis''16 cis''16 dis''16) |
  e''4 a'8( gis'16) b'4 cis''4 b'16 |
  b'8( cis''8) gis'4. a'8 b'4 |
  b'8. cis''4. dis''8 b'4 a'16 |
  \break
  gis'8( dis''16) cis''4 gis'4 a'8( b'16 gis'16 a'16) |
  gis'8 a'4. a'8.( gis'16) gis'4 |
  a'8( b'8.) cis''4. dis''16 dis''4 |
  dis''8 dis''4 e''8 e''4. e''16( e''16) |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 2/2
  a2 e2 |
  e2 b2 |
  e2 b2 |
  b2 fis2 |
  \break
  e2 b2 |
  e2 b2 |
  a2 e2 |
  e2 b2 |
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
  \midi { \tempo 4 = 92 }
}
