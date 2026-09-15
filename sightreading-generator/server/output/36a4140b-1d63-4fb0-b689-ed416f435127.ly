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
  \key c \major
  \time 3/4
  <c''\mf a'>4 <b' g'>8 <a' f'>8 <g' e'>4 |
  <b' g'>4. <c'' a'>8 <d'' b'>8 <e'' c''>8 |
  <b' g'>2 <c'' a'>4 |
  <e'' c''>4. <d'' b'>8 <c'' a'>4 |
  \break
  <b' g'>4. <c'' a'>8 <c'' a'>8 <d'' b'>8 |
  <e''^\markup { \italic "rall." } c''>4 <d'' b'>4. <d'' b'>8 |
  <d'' b'>4 <e'' c''>4 <b' g'>4 |
  <c'' a'>4. <c'' a'>8 <c'' a'>4 |
  \bar "|."
}

bassLine = {
  \key c \major
  \time 3/4
  c4. g4. |
  g4. d4. |
  g4. d4. |
  c4. g4. |
  \break
  g4. d4. |
  g4. d4. |
  g4. d4. |
  c4. g4. |
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
