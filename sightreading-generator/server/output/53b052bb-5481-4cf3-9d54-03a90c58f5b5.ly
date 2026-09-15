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
  \time 3/4
  \tempo "Canon"
  e''4\p gis'16([ fis'8 gis'8] a'8[ bis''16)] |
  a'4 bis''4 a'8([ e''8)] |
  dis''2 cis''8([ bis''16 cis''16)] |
  dis''4. cis''16([ bis''8] fis'8[ gis'16)] |
  \break
  fis'8([ e'16 fis'16)] gis'4. a'16([ gis'16)] |
  a'8([ gis'8] a'16[ bis''16 cis''8)] cis''4 |
  bis''2 cis''8([ dis''16 cis''16)] |
  cis''8([ bis''8] a'8[ bis''8)] a'4 |
  \break
  bis''4. a'8 bis''4 |
  bis''16([ bis''8 cis''16] dis''16[ cis''8 cis''8] cis''8[ cis''16)] |
  \bar "|."
}

bassLine = {
  \key cis \minor
  \time 3/4
  cis2. |
  e,4 gis,16 fis,8 gis,8 a,8 bis16 |
  a,4 bis4 a,8 e,8 |
  dis,2 cis,8 bis16 cis,16 |
  \break
  dis,4. cis,16 bis8 fis,8 gis,16 |
  fis,8 e,16 fis,16 gis,4. a,16 gis,16 |
  a,8 gis,8 a,16 bis16 cis,8 cis,4 |
  bis2 cis,8 dis,16 cis,16 |
  \break
  cis,8 bis8 a,8 bis8 a,4 |
  cis2. |
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
