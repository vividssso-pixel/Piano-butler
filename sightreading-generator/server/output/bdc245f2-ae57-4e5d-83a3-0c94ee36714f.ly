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
  \key d \minor
  \time 3/4
  d''4\p d''8([ c''8] g'8[ a'8)] |
  g'4 c''8[ bes'8] a'8[ bes'8] |
  d''2 e''4 |
  d''4 d''2 |
  \break
  cis''8([ cis''8] bes'8[ a'8)] bes'4 |
  a'2. |
  g'8[ g'8] f'8[ g'8] f'4 |
  f'8([ g'8] a'8[ bes'8)] d''4 |
  \bar "|."
}

bassLine = {
  \key d \minor
  \time 3/4
  R2. |
  g2. |
  g2. |
  g2. |
  \break
  a2. |
  d2. |
  g2. |
  d2. |
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
