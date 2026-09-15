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
  a'2_\markup { \italic "brightly" } a'8 bes'8 c''4 |
  g'2 a'2 |
  R1 |
  R1 |
  f'4 f'2 g'4 |
  a'4 bes'8 a'4 bes'4. |
  c''8 c''4 d''4. e''8 f''8 |
  \bar "|."
}

bassLine = {
  \key f \major
  \time 4/4
  R1 |
  R1 |
  a4. g2 g8 |
  a8 e4. f8 g8 f4 |
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
  \layout {}
  \midi { \tempo 4 = 84 }
}
