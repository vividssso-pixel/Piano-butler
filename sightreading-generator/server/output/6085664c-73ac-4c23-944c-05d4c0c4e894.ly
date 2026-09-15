\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 4 — Reading" }
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
  \time 3/4
  \tempo "Allegro"
  d''8\p e''4. d''4 |
  cis''4 cis''4 b'4 |
  e''2 d''4 |
  b'8. cis''4. d''8. |
  cis''8 cis''8 b'4 cis''4 |
  b'4. cis''8 b'8 g'8 |
  fis'4. g'8 fis'8 fis'8 |
  g'4 a'4 d''4 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 3/4
  d2. |
  a2. |
  a2. |
  g2. |
  a2. |
  g2. |
  d2. |
  g2. |
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
  \midi { \tempo 4 = 92 }
}
