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
  \tempo "Andante"
  c''4.\p cis''16( cis''8 c''8 dis''8 cis''8 cis''16) |
  dis''4 f''8( dis''16 c''16 cis''8 dis''8) f''4 |
  dis''16 c''16 c''8 c''16 cis''8 dis''8 f''8 dis''8 f''8 dis''16~ |
  dis''4. dis''16( dis''16 dis''16 cis''16 c''8) cis''4 |
  \break
  c''16 c''8 cis''16 dis''4 f''8 dis''16 f''8 dis''16 f''8 |
  dis''8. cis''16 dis''4 cis''4. dis''8~ |
  dis''4 dis''4 f''8 dis''16 f''8 dis''16 f''8 |
  cis''8. c''16 cis''4 dis''16( cis''8 c''8 c''8 c''16) |
  \bar "|."
}

bassLine = {
  \key aes \major
  \time 4/4
  gis1 |
  gis1 |
  gis1 |
  gis1 |
  \break
  gis1 |
  gis1 |
  gis1 |
  gis1 |
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
