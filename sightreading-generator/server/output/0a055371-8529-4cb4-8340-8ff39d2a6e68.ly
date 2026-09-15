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
  \key ees \major
  \time 2/4
  \tempo "Espressivo"
  ees''8\f f''8 d''4 |
  c''4 aes'4 |
  g'8 aes'8 bes'4 |
  aes'4. g'8 |
  \break
  aes'4 g'8 aes'8 |
  aes'4. g'8 |
  aes'2 |
  bes'4 ees''4 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/4
  <ees g bes>4 <ees g bes>4 |
  <aes c' ees>4 <aes c' ees>4 |
  <ees g bes>4 <ees g bes>4 |
  <aes c' ees>4 <aes c' ees>4 |
  \break
  <aes c' ees>4 <aes c' ees>4 |
  <aes c' ees>4 <aes c' ees>4 |
  <aes c' ees>4 <aes c' ees>4 |
  <ees g bes>4 <ees g bes>4 |
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
