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
  \key bes \major
  \time 3/4
  bes'8_\markup { \italic "brightly" } c''4 bes'8 c''4 |
  d''4. ees''4 ees''8 |
  ees''4. d''8 ees''4 |
  R2. |
  R2. |
  R2. |
  bes'4 bes'8 bes'4 bes'8 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 3/4
  R2. |
  R2. |
  R2. |
  a8 g8 a4. g8 |
  f8 ees4 a4 g8 |
  a4 g8 f8 f4 |
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
