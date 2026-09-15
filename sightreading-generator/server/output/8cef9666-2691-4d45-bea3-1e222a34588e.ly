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
  \key d \major
  \time 4/4
  d'8\f cis''2 b'8 d''4 |
  e''2 cis''8 b'8 a'4 |
  g'4 a'4 g'4 g'8 a'8 |
  g'4. fis'2 a'8 |
  b'8 a'8 g'8 g'4 b'4. |
  a'4 b'4. g'8 a'4 |
  g'4 a'4 b'8 b'4 g'8 |
  a'4 g'4 a'8 b'4 d''8 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  d1 |
  a1 |
  g1 |
  g1 |
  g1 |
  d1 |
  g1 |
  d1 |
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
  \midi { \tempo 4 = 88 }
}
