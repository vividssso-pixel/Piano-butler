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
  \time 4/4
  \tempo "Hymn"
  d''8.\mf cis''16 d''4. fis'8 g'4 |
  g'2 a'4 g'4 |
  fis'4 g'4. a'8 b'4 |
  a'4 b'4. a'8 b'4 |
  \break
  cis''4 d''2 e''8 d''8 |
  e''16( cis''8 b'8 cis''8 cis''8 d''8 e''8 d''8 cis''16) |
  cis''2 d''4 cis''4 |
  d''2 cis''16 b'8 cis''16 b'4 |
  \break
  a'4 g'2 a'8( b'8) |
  g'4. a'8 g'2 |
  fis'4 fis'4 g'2 |
  a'4. b'8 d''2 |
  \bar "|."
}

bassLine = {
  \key d \major
  \time 4/4
  <d fis a>4 <d fis a>4 <d fis a>4 <d fis a>4 |
  <g b d>4 <g b d>4 <g b d>4 <g b d>4 |
  <d fis a>4 <d fis a>4 <d fis a>4 <d fis a>4 |
  <d fis a>4 <d fis a>4 <d fis a>4 <d fis a>4 |
  \break
  <a cis' e>4 <a cis' e>4 <a cis' e>4 <a cis' e>4 |
  <a cis' e>4 <a cis' e>4 <a cis' e>4 <a cis' e>4 |
  <a cis' e>4 <a cis' e>4 <a cis' e>4 <a cis' e>4 |
  <g b d>4 <g b d>4 <g b d>4 <g b d>4 |
  \break
  <a cis' e>4 <a cis' e>4 <a cis' e>4 <a cis' e>4 |
  <g b d>4 <g b d>4 <g b d>4 <g b d>4 |
  <d fis a>4 <d fis a>4 <d fis a>4 <d fis a>4 |
  <d fis a>4 <d fis a>4 <d fis a>4 <d fis a>4 |
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
