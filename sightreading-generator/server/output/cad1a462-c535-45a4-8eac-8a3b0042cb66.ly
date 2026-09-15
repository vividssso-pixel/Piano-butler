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
  \key a \major
  \time 4/4
  \tempo "Romanze"
  cis''2\(\f d''4 cis''4 |
  d''4. e''8 d''4 cis''4 |
  d''4. e''16 cis''16 d''8 cis''8 cis''4 |
  d''2 cis''8( cis''8 d''8 e''16 d''16) |
  \break
  cis''4. d''8 cis''2 |
  e''8.( d''16) e''2 d''4 |
  e''2 d''2\) |
  e''4\( d''4. cis''8 e''4 |
  \break
  d''4. cis''8 d''4 cis''16 d''16 d''8 |
  e''4 d''8 d''16 e''16 d''2 |
  e''4. d''8 cis''4 d''8 cis''16 cis''16 |
  d''4 cis''8( d''8) cis''4 d''4 |
  \break
  e''4 d''4 e''4. d''8 |
  cis''8.( cis''16) cis''2 cis''4\) |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 4/4
  a2 cis'2 |
  d'2 fis'2 |
  a2 cis'2 |
  d'2 fis'2 |
  \break
  a2 cis'2 |
  a2 cis'2 |
  e'2 gis'2 |
  a2 cis'2 |
  \break
  d'2 fis'2 |
  e'2 gis'2 |
  a2 cis'2 |
  d'2 fis'2 |
  \break
  e'2 gis'2 |
  a2 cis'2 |
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
