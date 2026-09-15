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
  \key aes \major
  \time 4/4
  \tempo "Legato"
  c''2.\p cis''4 |
  dis''2 f''2~ |
  f''2 c''4 cis''4 |
  f''2. dis''4 |
  \break
  f''2. dis''4 |
  cis''4 c''4 dis''4 cis''4 |
  dis''4 dis''4 cis''2 |
  c''2 c''4 c''4 |
  \bar "|."
}

bassLine = {
  \key aes \major
  \time 4/4
  gis4 dis'4 gis4 dis'4 |
  gis4 dis'4 gis4 dis'4 |
  gis4 dis'4 gis4 dis'4 |
  cis'4 gis4 cis'4 gis4 |
  \break
  cis'4 gis4 cis'4 gis4 |
  cis'4 gis4 cis'4 gis4 |
  gis4 dis'4 gis4 dis'4 |
  gis4 dis'4 gis4 dis'4 |
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
