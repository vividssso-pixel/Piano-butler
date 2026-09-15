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
  \key g \major
  \time 3/4
  \tempo "Minuet tempo"
  b'8\p c''4 d''4 e''8 |
  d''4 c''4. d''8 |
  c''4. d''8. d''8. |
  e''2 d''4 |
  e''8. d''8. c''4 b'8 |
  c''4 b'8. b'8. c''8 |
  d''4 e''8. d''8 d''8. |
  c''8 b'4 b'8 b'8 b'8 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 3/4
  g2. |
  g2. |
  c'2. |
  c'2. |
  c'2. |
  c'2. |
  g2. |
  c'2. |
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
