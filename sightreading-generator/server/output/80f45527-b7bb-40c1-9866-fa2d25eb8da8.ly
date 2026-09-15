\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 2 — Reading" }
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
  \key f \major
  \time 4/4
  R1 |
  R1 |
  R1 |
  f'8 g'8 a'4 g'8 g'8 f'4 |
  \break
  g'4 f'2 f'8 f'8 |
  f'8 g'8 a'4. g'8 f'8 f'8 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 4/4
  c2_\markup { \italic "brightly" } d2 |
  e4. e8 bes,4 a,8 bes,8 |
  a,4. bes,8 bes,8 a,8 g,4 |
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
  \midi { \tempo 4 = 84 }
}
