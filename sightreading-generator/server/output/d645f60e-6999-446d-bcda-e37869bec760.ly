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
  \time 2/4
  \tempo "Moderato, flowing"
  cis''4\mp cis''4 |
  dis''8.[ e''16] dis''4 |
  e''8[ dis''8] e''8[ dis''16 e''16] |
  dis''2 |
  \break
  cis''2 |
  e''8[ dis''16 cis''16] b'4 |
  cis''2 |
  e'8([ fis'16 gis'16)] cis''4 |
  \bar "|."
}

bassLine = {
  \key cis \minor
  \time 2/4
  cis4 gis4 |
  gis4 dis4 |
  cis4 gis4 |
  gis4 dis4 |
  \break
  cis4 gis4 |
  cis4 gis4 |
  cis4 gis4 |
  cis4 gis4 |
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
