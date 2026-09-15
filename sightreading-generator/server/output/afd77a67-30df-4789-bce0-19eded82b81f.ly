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
  \key fis \minor
  \time 3/4
  \tempo "Sarabande"
  a'4\mf a'16([ b'16 cis''8] d''8[ cis''8)] |
  b'16([ a'8 b'8] e''8[ d''8] cis''8[ a'16)] |
  b'4 a'4 b'4 |
  a'4 b'2 |
  \break
  cis''8([ b'8] b'8[ d''8)] e''4 |
  a'2 a'4 |
  cis''2 dis''4 |
  e''2 e''4 |
  \bar "|."
}

bassLine = {
  \key fis \minor
  \time 3/4
  fis4 <fis a cis'>2 |
  b4 <b d' fis>2 |
  b4 <b d' fis>2 |
  fis4 <fis a cis'>2 |
  \break
  b4 <b d' fis>2 |
  fis4 <fis a cis'>2 |
  fis4 <fis a cis'>2 |
  fis4 <fis a cis'>2 |
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
