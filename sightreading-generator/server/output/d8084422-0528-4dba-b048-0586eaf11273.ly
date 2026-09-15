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
  \key b \major
  \time 3/4
  \tempo "Valse lente"
  b'2\mf \tuplet 3/2 { b'8( cis''8 b'8) } |
  cis''2. |
  cis''2. |
  e''2 dis''4 |
  \break
  cis''2 b'16[ cis''16 cis''8] |
  e''2 dis''4 |
  dis''2. |
  cis''4. dis''8 e''4 |
  \break
  dis''2 cis''4 |
  b'2. |
  cis''4 cis''2 |
  cis''4 dis''4 cis''4 |
  \break
  b'4 dis''2 |
  e''2 cis''8([ dis''16 cis''16)] |
  cis''4 cis''2 |
  b'4. b'8 b'4 |
  \bar "|."
}

bassLine = {
  \key b \major
  \time 3/4
  b,4 fis4 fis4 |
  cis4 gis4 gis4 |
  fis4 cis4 cis4 |
  cis4 gis4 gis4 |
  \break
  fis4 cis4 cis4 |
  cis4 gis4 gis4 |
  b,4 fis4 fis4 |
  cis4 gis4 gis4 |
  \break
  b,4 fis4 fis4 |
  b,4 fis4 fis4 |
  cis4 gis4 gis4 |
  fis4 cis4 cis4 |
  \break
  b,4 fis4 fis4 |
  cis4 gis4 gis4 |
  fis4 cis4 cis4 |
  b,4 fis4 fis4 |
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
