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
  \key ees \major
  \time 4/4
  \tempo "Daintily"
  ees''2.\mp ees''4 |
  d''2 ees''2 |
  ees''4 f''2 c''4 |
  bes'2 aes'2 |
  \break
  bes'4 aes'4 bes'4. c''8 |
  d''4 aes'2 g'4 |
  c''2 bes'4 c''4 |
  d''2. ees''4 |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 4/4
  ees2 bes2 |
  bes2 f2 |
  aes2 ees2 |
  R1 |
  \break
  ees2 bes2 |
  bes2 f2 |
  f2 c2 |
  ees2 bes2 |
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
  \midi { \tempo 4 = 92 }
}
