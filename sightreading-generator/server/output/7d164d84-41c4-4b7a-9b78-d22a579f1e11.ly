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
  \key g \major
  \time 2/4
  <b'\mp g'>4 <c'' a'>8 <b' g'>8 |
  <c'' a'>4. <d'' b'>8 |
  <c'' a'>4 <d'' b'>4 |
  <c'' a'>8 <d'' b'>8 <c'' a'>4 |
  \break
  <d'' b'>8 <e'' c''>8 <d'' b'>4 |
  <d'' b'>8 <d'' b'>8 <c'' a'>4 |
  <b' g'>8 <c'' a'>8 <d'' b'>4 |
  <e'' c''>8 <e'' c''>8 <e'' c''>4 |
  \bar "|."
}

bassLine = {
  \key g \major
  \time 2/4
  g4 d'4 |
  c'4 g4 |
  c'4 g4 |
  c'4 g4 |
  \break
  g4 d'4 |
  g4 d'4 |
  g4 d'4 |
  g4 d'4 |
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
