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
  \time 3/4
  \tempo "Moderato"
  e''8(\mf b'8) a'4 b'16 a'16 cis''16 b'16 |
  a'4. b'16 cis''8 dis''8 cis''16 |
  b'2 a'8( gis'16 a'16~) |
  a'16 a'8 gis'8 a'16 b'8 cis''4 |
  \break
  b'4 e''4. dis''8 |
  dis''8 e''8 cis''4. dis''8~ |
  dis''4 dis''8 cis''8 a'4 |
  gis'16( b'8 a'16 b'8 cis''8) e''4 |
  \bar "|."
}

bassLine = {
  \key e \major
  \time 3/4
  e4. b4. |
  a4. e4. |
  e4. b4. |
  e4. b4. |
  \break
  e4. b4. |
  b4. fis4. |
  a4. e4. |
  e4. b4. |
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
