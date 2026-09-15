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
  \key d \major
  \time 3/4
  \tempo "Canon"
  d''4.\f e''8 d''4 |
  e''4 d''2 |
  d''2 e''8([ d''16 e''16)] |
  d''2 cis''4 |
  \break
  b'4. cis''8( d''8[ e''16 d''16)] |
  cis''2 d''4 |
  cis''4. b'8 a'4 |
  g'8[ a'8] g'4 g'4 |
  \break
  fis'8[ b'8] b'4 cis''4 |
  b'8[ fis'8] g'8[ a'8] d''4 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 3/4
  d2. |
  d,4. e,8 d,4 |
  e,4 d,2 |
  d,2 e,8 d,16 e,16 |
  \break
  d,2 cis4 |
  b,4. cis8 d,8 e,16 d,16 |
  cis2 d,4 |
  cis4. b,8 a,4 |
  \break
  g,8 a,8 g,4 g,4 |
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
  \midi { \tempo 4 = 96 }
}
