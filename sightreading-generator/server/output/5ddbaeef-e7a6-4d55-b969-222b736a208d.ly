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
  \key gis \minor
  \time 3/4
  \tempo "Moderato grazioso"
  dis''2\mf e''8.[ dis''16] |
  ais'4 b'4 b'4 |
  cis''4 b'4 ais'8([ ais'16 dis''16)] |
  e''2 dis''8[ dis''8] |
  \break
  b'16[ ais'16 gis'8] ais'4. ais'16[ gis'16] |
  dis''4. e''8 dis''4 |
  e''2. |
  dis''2 e''4 |
  \break
  dis''2 b'4 |
  cis''4. cis''8 b'4 |
  cis''4 b'4 b'8[ cis''8] |
  b'4 cis''8([ dis''8] cis''16[ dis''16 e''8)] |
  \break
  dis''4 dis''4. e''8 |
  dis''8([ cis''8)] b'4 ais'4 |
  gis'8[ ais'8] gis'4. ais'16[ cis''16] |
  b'4 ais'4. b'8 |
  \break
  ais'2 gis'4 |
  gis'2. |
  \bar "|."
}

bassLine = {
  \key gis \minor
  \time 3/4
  gis2. |
  dis2 e8. dis16 |
  ais,4 b,4 b,4 |
  cis4 b,4 ais,8 ais,16 dis16 |
  \break
  e2 dis8 dis8 |
  b,16 ais,16 gis,8 ais,4. ais,16 gis,16 |
  dis4. e8 dis4 |
  e2. |
  \break
  dis2 e4 |
  dis2 b,4 |
  cis4. cis8 b,4 |
  cis4 b,4 b,8 cis8 |
  \break
  b,4 cis8 dis8 cis16 dis16 e8 |
  dis4 dis4. e8 |
  dis8 cis8 b,4 ais,4 |
  gis,8 ais,8 gis,4. ais,16 cis16 |
  \break
  b,4 ais,4. b,8 |
  gis2. |
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
