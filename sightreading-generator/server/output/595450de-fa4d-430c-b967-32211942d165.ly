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
  cis''8.([\f b'16)] a'4 gis'8[ b'16 a'16] |
  gis'4. gis'8( a'8[ bis''8)] |
  a'2 e''4 |
  dis''8[ cis''8] bis''8[ e'8] fis'4 |
  \break
  dis''4. e''8 cis''8[ b'16 cis''16] |
  e''4. dis''8 dis''16[ e''16 dis''8] |
  cis''16[ dis''16 cis''8] dis''4 cis''4 |
  dis''16[ e''16 dis''16 e''16] dis''4. cis''16([ bis''16)] |
  \break
  a'4. gis'8 e'4 |
  fis'2 gis'8[ fis'8] |
  e'4 fis'4. gis'8 |
  a'2 cis''4 |
  \bar "|."
}

bassLine = {
  \key cis \minor
  \time 3/4
  fis2. |
  cis,8. b,16 a,4 gis,8 b,16 a,16 |
  gis,4. gis,8 a,8 b,8 |
  a,2 e,4 |
  \break
  dis,8 cis,8 b,8 e,8 fis,4 |
  dis,4. e,8 cis,8 b,16 cis,16 |
  e,4. dis,8 dis,16 e,16 dis,8 |
  cis,16 dis,16 cis,8 dis,4 cis,4 |
  \break
  dis,16 e,16 dis,16 e,16 dis,4. cis,16 b,16 |
  a,4. gis,8 e,4 |
  fis,2 gis,8 fis,8 |
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
