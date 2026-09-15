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
  \time 3/4
  \tempo "Daintily"
  d''2.\mf |
  e''4 d''4 e''4 |
  b'2. |
  a'4. b'8 b'4 |
  \break
  \tuplet 3/2 { a'8([ g'8] fis'8) } g'2 |
  fis'4 g'4 \tuplet 3/2 { g'8[ a'8] cis''8 } |
  d''4 e''4 d''4 |
  d''4 d''4 d''4 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 3/4
  d4 fis2 |
  r4 cis'2 |
  g4 r2 |
  a4 cis'2 |
  \break
  d4 r2 |
  d4 fis2 |
  d4 fis2 |
  d4 fis2 |
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
