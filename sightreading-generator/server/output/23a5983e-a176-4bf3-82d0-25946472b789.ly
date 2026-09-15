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
  fis'8\mf g'8 a'2 a'8 g'8 |
  g'4 fis'4 e'8 d'4 d'8 |
  R1 |
  R1 |
  \break
  d'4 fis'2 e'4 |
  g'4 fis'4 e'4 fis'8 e'8 |
  R1 |
  d'2 fis'4. e'8 |
  \break
  a'4. b'8 cis''8 d''4 cis''8 |
  R1 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  R1 |
  R1 |
  a4 g8 d8 e4 d4 |
  e4 d4 e4. fis8 |
  \break
  R1 |
  R1 |
  a8 g4. fis8 e4 e8 |
  R1 |
  \break
  R1 |
  a8 fis4. e8 d4 d8 |
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
