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
  \tempo "Tempo comodo"
  d''4.\mf d''8 d''4 |
  a'8 g'8. a'4 b'8. |
  a'4. b'8. cis''8. |
  g'4. fis'8 g'8 a'8 |
  \break
  b'2 a'4 |
  b'8 b'4 cis''4 b'8 |
  cis''4 a'8 b'4 b'8 |
  cis''8. d''4. d''8. |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 3/4
  d4. a4. |
  d4. a4. |
  a4. e4. |
  g4. d4. |
  \break
  g4. d4. |
  g4. d4. |
  a4. e4. |
  a4. e4. |
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
