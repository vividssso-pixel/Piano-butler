\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 2 — Reading" }
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
  \time 3/4
  R2. |
  bes'4. bes'8 c''4 |
  c''4 bes'4. c''8 |
  d''4. bes'8 c''8 bes'8 |
  \break
  bes'2. |
  bes'4 bes'4 bes'8 bes'8 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 3/4
  bes,4_\markup { \italic "cheerfully" } d8 ees8 d4 |
  R2. |
  R2. |
  R2. |
  \break
  R2. |
  R2. |
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
  \midi { \tempo 4 = 84 }
}
