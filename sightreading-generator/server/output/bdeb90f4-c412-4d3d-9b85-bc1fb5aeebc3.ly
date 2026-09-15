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
  \time 4/4
  d''4\p_\markup { \italic "lilting" } ees''4 f''8( ees''8) f''4 |
  ees''8( f''8) r4 ees''2 |
  ees''4 f''8( d''8) ees''4 f''8 d''8 |
  ees''4 ees''4 d''4 ees''4 |
  \break
  f''4 r4 ees''8 f''8 ees''4 |
  R1^\markup { \italic "slowing" } |
  d''4 f''8 ees''8 r4 ees''4 |
  f''4 f''4 f''4 f''4 |
  \bar "|."
}

bassLine = {
  \key bes \major
  \time 4/4
  R1 |
  ees'4 d'4 c'4 bes4 |
  bes4 c'4 d'4 ees'4 |
  R1 |
  \break
  bes4 c'4 d'4 ees'4 |
  ees'4 ees'4 ees'4 ees'4 |
  ees'4 d'4 c'4 bes4 |
  bes4 bes4 bes4 bes4 |
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
