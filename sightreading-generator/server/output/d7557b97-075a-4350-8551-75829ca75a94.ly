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
  \time 2/4
  \tempo "Slow march"
  b'4\mf cis''8([ dis''8)] |
  dis''8([ dis''8] e''8[ e''8)] |
  e''8([ dis''16 e''16] dis''8[ dis''8)] |
  e''16([ dis''8 cis''8] dis''16[ dis''8)] |
  \break
  e''2 |
  dis''2 |
  R2 |
  e''2 |
  \break
  dis''16([ dis''16 dis''16 cis''16)] r4 |
  cis''4. dis''8 |
  cis''8([ dis''8)] e''4 |
  e''4 e''4 |
  \bar "|."
}

bassLine = {
  \key gis \minor
  \time 2/4
  gis4 dis'4 |
  gis4 dis'4 |
  gis4 dis'4 |
  gis4 dis'4 |
  \break
  cis'4 gis4 |
  dis'4 ais4 |
  cis'4 gis4 |
  cis'4 gis4 |
  \break
  gis4 dis'4 |
  cis'4 gis4 |
  cis'4 gis4 |
  gis4 dis'4 |
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
