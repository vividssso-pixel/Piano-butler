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
  ees''4.-.\(\mp_\markup { \italic "sweetly" } f''8 |
  c''4-. c''8( aes'8) |
  bes'4-. aes'4-. |
  g'4-. aes'4-.\) |
  \break
  bes'4-.\( c''4-. |
  bes'4-. aes'8( bes'8) |
  aes'8( c''8) d''4-. |
  ees''4.-. ees''8\) |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/4
  ees2 |
  aes2 |
  ees2 |
  ees2 |
  \break
  ees2 |
  ees2 |
  aes2 |
  ees2 |
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
