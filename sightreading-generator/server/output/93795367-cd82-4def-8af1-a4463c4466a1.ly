\version "2.24.3"

\header {
  title = \markup { \override #'(font-name . "Liberation Sans") \fontsize #2 \normal-text "Sight-Reading Excerpt" }
  subtitle = \markup { \override #'(font-name . "Liberation Sans") \fontsize #-1 \normal-text \with-color #(x11-color 'gray40) "Grade 5 — Reading" }
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
  \tempo "Slow march"
  ees''4\f \tuplet 3/2 { f''8 ees''8 d''8 } |
  ees''4 f''8[ ees''16 d''16] |
  d''2 |
  ees''16([ f''16 ees''8)] f''4 |
  \break
  r2 |
  f''8[ ees''16 d''16] ees''4 |
  ees''16([ f''16 aes'8)] g'4 |
  \tuplet 3/2 { aes'8( g'8 bes'8 } aes'8 bes'8) |
  \break
  aes'4. g'8 |
  aes'8[ bes'8] c''8[ d''16 ees''16] |
  \bar "|."
}

bassLine = {
  \key ees \major
  \time 2/4
  ees,4 bes,4 |
  ees,4 bes,4 |
  bes,4 f,4 |
  ees,4 bes,4 |
  \break
  ees,4 bes,4 |
  bes,4 f,4 |
  ees,4 bes,4 |
  ees,4 bes,4 |
  \break
  aes,4 ees,4 |
  ees,4 bes,4 |
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
  \midi { \tempo 4 = 96 }
}
