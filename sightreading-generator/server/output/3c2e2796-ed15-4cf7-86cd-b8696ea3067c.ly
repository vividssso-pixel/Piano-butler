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
  \time 9/8
  \tempo "Canon"
  cis''4\mf d''8 e''4. d''8( e''16 d''16 cis''8) |
  d''8 cis''4 d''8( e''8 e''16 d''16 e''8 cis''8 d''8) |
  cis''4. d''8( cis''8 d''8) d''4 e''8 |
  d''4. cis''8( cis''8 d''16 d''16 cis''8) r4 |
  \break
  cis''8( d''8 e''8 d''8) e''4 d''4. |
  cis''4. cis''4. e''8( d''16 cis''16 cis''8) |
  d''4. e''8( d''16 e''16 d''8) e''4. |
  d''4 cis''8( d''8 cis''8 d''8) e''4. |
  \break
  e''8 d''4 cis''4 e''8( d''8 cis''16 d''16 cis''8) |
  d''8 e''4 e''4 cis''8 d''4 d''8 |
  e''8( d''8 cis''8) d''4. cis''4 d''8 |
  e''4. d''8( cis''16 d''16 cis''8) d''4 e''8 |
  \break
  d''4. d''4. e''8( d''8 d''8) |
  d''4. cis''8 cis''4 cis''4. |
  \bar "|."
}

bassLine = {
  \key a \major
  \time 9/8
  a1~ a8 |
  cis4 d8 e4. d8 e16 d16 cis8 |
  d8 cis4 d8 e8 e16 d16 e8 cis8 d8 |
  cis4. d8 cis8 d8 d4 e8 |
  \break
  d4. cis8 cis8 d16 d16 cis8 d4 |
  cis8 d8 e8 d8 e4 d4. |
  cis4. cis4. e8 d16 cis16 cis8 |
  d4. e8 d16 e16 d8 e4. |
  \break
  d4 cis8 d8 cis8 d8 e4. |
  e8 d4 cis4 e8 d8 cis16 d16 cis8 |
  d8 e4 e4 cis8 d4 d8 |
  e8 d8 cis8 d4. cis4 d8 |
  \break
  e4. d8 cis16 d16 cis8 d4 e8 |
  a1~ a8 |
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
  \midi { \tempo 4. = 64 }
}
