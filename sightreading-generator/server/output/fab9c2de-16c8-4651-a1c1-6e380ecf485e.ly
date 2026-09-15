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
  \key g \minor
  \time 4/4
  g'8\p_\markup { \italic "lilting" } a'8 bes'8 c''8 bes'2 |
  a'8 d''8 c''2. |
  r2 a'4 bes'8 c''8 |
  r4 a'4 bes'2 |
  \break
  R1 |
  g'2. a'4 |
  a'8( a'8 d''8 d''8) d''2 |
  c''8( d''8 c''8 ees''8) d''4 c''8( g'8) |
  \bar "|."
}

bassLine = {
  \key g \minor
  \time 4/4
  g2 bes2 |
  r2 fis2 |
  g2 r2 |
  g2 bes2 |
  \break
  c2 r2 |
  c2 r2 |
  d2 fis2 |
  g2 bes2 |
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
