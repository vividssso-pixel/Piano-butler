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
  \key d \major
  \time 3/4
  d''4\p e''4. cis''8 |
  b'4 b'4. a'8 |
  g'2 fis'4~ |
  fis'4. fis'8 g'8 g'8 |
  \break
  g'2 fis'8( g'8) |
  fis'4 b'2 |
  a'2 d''4 |
  e''8 d''8 d''4. d''8 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 3/4
  d2. |
  g2. |
  g2. |
  g2. |
  \break
  g2. |
  d2. |
  d2. |
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
