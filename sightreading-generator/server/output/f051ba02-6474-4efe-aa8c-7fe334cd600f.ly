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
  d''8\mf e''4 d''2 e''8 |
  e''4 d''2 e''4 |
  d''2 e''8 b'4 a'8 |
  a'2 b'8 d''4. |
  e''4 d''4 cis''4. b'8 |
  cis''8 b'4. a'2 |
  d''4 cis''4 d''8 cis''4 e''8 |
  d''4 e''8 d''2 b'8 |
  b'2 b'4. b'8 |
  cis''4. d''2 d''8 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  d1 |
  a1 |
  d1 |
  d1 |
  a1 |
  a1 |
  a1 |
  g1 |
  g1 |
  g1 |
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
