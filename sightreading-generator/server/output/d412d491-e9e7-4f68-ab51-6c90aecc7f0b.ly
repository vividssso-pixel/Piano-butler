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
  \time 3/4
  d''4\f d''4 f''8([ ees''8)] |
  d''2 ees''4 |
  ees''8([ f''8)] ees''4 d''4 |
  ees''8([ ees''8] d''8[ ees''8)] d''4 |
  \break
  ees''8([ f''8] ees''8[ d''8)] ees''4 |
  f''2 ees''4 |
  f''2 ees''8[ ees''8] |
  d''4 d''4 d''4 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 3/4
  bes2. |
  bes2. |
  ees'2. |
  ees'2. |
  \break
  ees'2. |
  f'2. |
  R2. |
  bes2. |
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
