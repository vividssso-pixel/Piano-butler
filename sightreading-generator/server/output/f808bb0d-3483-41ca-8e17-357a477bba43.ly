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
  c''4\mf des''2 \tuplet 3/2 { ees''8( f''8 ees''8) } |
  des''4 c''2 des''4 |
  ees''2 f''2 |
  ees''4. des''8 c''4. ees''8 |
  \break
  des''4 ees''4 f''2 |
  c''4 des''2. |
  c''16 des''16 ees''16 des''16 c''2. |
  c''2 c''4 c''4 |
  \bar "|."
}

bassLine = {
  \key aes \major
  \time 4/4
  aes2 ees'2 |
  R1 |
  aes2 ees'2 |
  R1 |
  \break
  des'2 aes2 |
  aes2 ees'2 |
  R1 |
  aes2 ees'2 |
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
