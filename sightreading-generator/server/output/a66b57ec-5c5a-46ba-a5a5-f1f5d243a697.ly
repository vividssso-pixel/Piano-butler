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
  \key cis \minor
  \time 4/4
  \tempo "Hymn"
  cis''4\(\f dis''4 e''2 |
  dis''4 cis''4 dis''2 |
  e''8( dis''8) cis''4. b'8 cis''16 dis''16 e''8 |
  dis''16 e''16 dis''8 cis''2 b'4 |
  \break
  a'4. gis'16 a'16 b'2\) |
  a'2\( b'4 e''8( dis''8) |
  cis''2 b'4 a'4 |
  a'2 gis'4 gis'4 |
  \break
  fis'2 e'2 |
  e'2 fis'8 gis'16 a'16 cis''4\) |
  \bar "|."
}

bassLine = {
  \key cis \minor
  \time 4/4
  <cis e gis>4 <cis e gis>4 <cis e gis>4 <cis e gis>4 |
  <gis bis' dis>4 <gis bis' dis>4 <gis bis' dis>4 <gis bis' dis>4 |
  <cis e gis>4 <cis e gis>4 <cis e gis>4 <cis e gis>4 |
  <gis bis' dis>4 <gis bis' dis>4 <gis bis' dis>4 <gis bis' dis>4 |
  \break
  <fis a cis>4 <fis a cis>4 <fis a cis>4 <fis a cis>4 |
  <gis bis' dis>4 <gis bis' dis>4 <gis bis' dis>4 <gis bis' dis>4 |
  <fis a cis>4 <fis a cis>4 <fis a cis>4 <fis a cis>4 |
  <gis bis' dis>4 <gis bis' dis>4 <gis bis' dis>4 <gis bis' dis>4 |
  \break
  <fis a cis>4 <fis a cis>4 <fis a cis>4 <fis a cis>4 |
  <cis e gis>4 <cis e gis>4 <cis e gis>4 <cis e gis>4 |
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
