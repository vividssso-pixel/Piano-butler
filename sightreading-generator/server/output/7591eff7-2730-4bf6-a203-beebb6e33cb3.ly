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
  \time 3/4
  f'8_\markup { \italic "soft" } g'8 a'4 g'4 |
  f'4 g'4 a'8 c''8 |
  R2. |
  f'4. g'8 a'4 |
  g'8 f'4. f'4 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 3/4
  R2. |
  R2. |
  a4 g2 |
  R2. |
  R2. |
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
  \layout {}
  \midi { \tempo 4 = 84 }
}
