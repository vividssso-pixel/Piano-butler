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
  \time 2/4
  \tempo "Allegretto"
  R2 |
  a'4 b'8 e''8 |
  R2 |
  a'4. b'8 |
  \break
  R2 |
  R2 |
  a'8 a'4. |
  a'4. a'8 |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 2/4
  cis4.\f d8 |
  R2 |
  a8 gis4 fis8 |
  R2 |
  \break
  a4 gis8 a8 |
  gis8 gis8 fis4 |
  R2 |
  R2 |
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
