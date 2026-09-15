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
  \time 3/4
  R2. |
  aes'2\p bes'8([ bes'8)] |
  R2. |
  aes'4 bes'4 aes'8([ c''8)] |
  \break
  c''8([ aes'8)] g'4 aes'8[ bes'8] |
  aes'4 g'4 aes'4 |
  aes'8[ bes'8] aes'8[ bes'8] c''4 |
  ees''2. |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 3/4
  ees2. |
  ees,8 bes,8 aes,4 g,4 |
  aes,2 bes,8 bes,8 |
  c8 d8 c2 |
  \break
  aes,4 bes,4 aes,8 c8 |
  c8 aes,8 g,4 aes,8 bes,8 |
  aes,4 g,4 aes,4 |
  ees2. |
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
