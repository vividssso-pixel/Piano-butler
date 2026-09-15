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
  ees''8\(\p_\markup { \italic "lilting" } f''8 d''4 |
  c''2~ |
  c''4 d''8 c''8 |
  bes'4 aes'4\) |
  \break
  bes'8\( c''8 d''4 |
  c''8( d''8) ees''4 |
  d''4. ees''8 |
  ees''4 ees''4\) |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/4
  ees4 aes4 |
  aes4 aes4 |
  aes4 ees4 |
  ees4 bes4 |
  \break
  bes4 aes4 |
  aes4 bes4 |
  bes4 ees4 |
  ees4 ees4 |
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
