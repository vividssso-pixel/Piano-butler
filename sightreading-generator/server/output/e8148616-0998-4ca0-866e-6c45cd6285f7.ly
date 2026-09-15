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
  \key bes \major
  \time 2/4
  bes'2\mp |
  ees''8 ees''8 ees''8 f''8 |
  f''4. ees''8 |
  f''2 |
  ees''8 f''4. |
  f''2 |
  d''4 ees''4 |
  d''8 c''4 bes'8 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 2/4
  bes4 f'4 |
  ees'4 bes4 |
  bes4 f'4 |
  bes4 f'4 |
  ees'4 bes4 |
  bes4 f'4 |
  bes4 f'4 |
  bes4 f'4 |
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
