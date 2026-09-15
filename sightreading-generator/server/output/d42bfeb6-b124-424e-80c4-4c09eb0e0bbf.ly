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
  \tempo "Sarabande"
  b'4\(\mp cis''4 b'4 |
  cis''2 b'8([ cis''8)] |
  cis''4 dis''4. e''8 |
  dis''2 e''4 |
  \break
  dis''2 cis''4 |
  dis''2 dis''16([ cis''8 cis''16)] |
  dis''2 e''8([ e''8)]\) |
  dis''4\( cis''2 |
  \break
  cis''2 b'4 |
  r2 dis''4 |
  cis''4. dis''8 dis''4 |
  e''4. dis''8( cis''8[ cis''16 b'16)] |
  \break
  b'2 dis''4 |
  e''4 e''4 e''4\) |
  \bar "|."
}

bassLine = {
  \key gis \minor
  \time 3/4
  gis4 <gis b dis'>2 |
  cis'4 <cis' e' gis>2 |
  cis'4 <cis' e' gis>2 |
  dis'4 <dis' fisis' ais>2 |
  \break
  gis4 <gis b dis'>2 |
  gis4 <gis b dis'>2 |
  dis'4 <dis' fisis' ais>2 |
  gis4 <gis b dis'>2 |
  \break
  cis'4 <cis' e' gis>2 |
  cis'4 <cis' e' gis>2 |
  dis'4 <dis' fisis' ais>2 |
  cis'4 <cis' e' gis>2 |
  \break
  gis4 <gis b dis'>2 |
  gis4 <gis b dis'>2 |
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
