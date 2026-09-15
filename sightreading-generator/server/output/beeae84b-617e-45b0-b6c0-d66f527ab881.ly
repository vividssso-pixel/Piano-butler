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
  \key d \major
  \time 4/4
  \tempo "Andante"
  d''4\pp e''2 d''4 |
  g'4 g'2. |
  a'2. g'16 fis'16 g'16 g'16 |
  g'4 a'4 b'2 |
  \break
  d''4 e''4 d''2 |
  d''4 b'4 cis''16 d''16 cis''16 d''16 e''4 |
  d''2 cis''4 d''4 |
  d''2. d''4 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  d1 |
  r1 |
  g1 |
  r1 |
  \break
  g1 |
  g1 |
  g1 |
  d1 |
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
