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
  cis''2\p b'8 a'8 b'4 |
  R1 |
  R1 |
  a'4 cis''4 d''4 cis''4 |
  \break
  R1 |
  a'4 b'4 a'4 cis''8 d''8 |
  cis''8 d''8 cis''2 b'8 a'8 |
  a'4. a'8 a'4 a'4 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 4/4
  R1 |
  a8 fis8 gis4 a4 fis8 fis8 |
  gis4 fis4. e8 fis8 fis8 |
  R1 |
  \break
  a8 gis8 fis4 gis4 fis4 |
  R1 |
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
