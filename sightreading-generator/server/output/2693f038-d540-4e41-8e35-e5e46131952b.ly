\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 3 — Reading" }
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
  \key a \major
  \time 4/4
  R1 |
  a'8 b'8 a'4 a'4 b'4 |
  R1 |
  a'4 b'8 a'8 b'4 cis''8 d''8 |
  \break
  d''8 e''8 d''4 d''2 |
  R1 |
  R1 |
  a'8 a'8 b'4 a'4. b'8 |
  \break
  b'4 a'4 a'8 a'8 a'4 |
  a'4. a'8 a'4. a'8 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 4/4
  e4\p_\markup { \italic "sadly" } fis4 gis4 e8 d8 |
  R1 |
  a8 gis8 fis4 gis8 fis8 gis4 |
  R1 |
  \break
  R1 |
  a2 gis4 a4 |
  fis2 e4. fis8 |
  R1 |
  \break
  R1 |
  R1 |
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
  \midi { \tempo 4 = 88 }
}
