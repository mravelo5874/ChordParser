#!/usr/bin/env python3

# Tests are organized in a dictionary:
#   'input' : 'expected-output'

tests = {
# --------------------------------
#   C TRIADS
# --------------------------------
    # C major
    'Cmaj':     [0, 12],
    'CM':       [0, 12],
    'CΔ':       [0, 12],
    'C':        [0, 12],

    # C minor
    'Cm':       [0, 13],
    'C-':       [0, 13],
    'Cmin':     [0, 13],

    # C augmented
    'C+':       [0, 14],
    'Caug':     [0, 14],
    'CM#5':     [0, 14],
    'CM+5':     [0, 14],

    # C diminished
    'Co':       [0, 15],
    'Cdim':     [0, 15],
    'Cmb5':     [0, 15],
    'Cmo5':     [0, 15],
# --------------------------------
#   C# TRIADS
# --------------------------------
    # C# major
    'C#maj':    [1, 12],
    'C#M':      [1, 12],
    'C#Δ':      [1, 12],
    'C#':       [1, 12],

    # C# minor
    'C#m':      [1, 13],
    'C#-':      [1, 13],
    'C#min':    [1, 13],

    # C# augmented
    'C#+':      [1, 14],
    'C#aug':    [1, 14],
    'C#M#5':    [1, 14],
    'C#M+5':    [1, 14],

    # C# diminished
    'C#o':      [1, 15],
    'C#dim':    [1, 15],
    'C#mb5':    [1, 15],
    'C#mo5':    [1, 15],
# --------------------------------
#   Db TRIADS
# --------------------------------
    # Db major
    'Dbmaj':    [1, 12],
    'DbM':      [1, 12],
    'DbΔ':      [1, 12],
    'Db':       [1, 12],

    # Db minor
    'Dbm':      [1, 13],
    'Db-':      [1, 13],
    'Dbmin':    [1, 13],

    # Db augmented
    'Db+':      [1, 14],
    'Dbaug':    [1, 14],
    'DbM#5':    [1, 14],
    'DbM+5':     [1, 14],

    # Db diminished
    'Dbo':      [1, 15],
    'Dbdim':    [1, 15],
    'Dbmb5':    [1, 15],
    'Dbmo5':    [1, 15],
# --------------------------------
#   D TRIADS
# --------------------------------
    # D major
    'Dmaj':    [2, 12],
    'DM':      [2, 12],
    'DΔ':      [2, 12],
    'D':       [2, 12],

    # D minor
    'Dm':      [2, 13],
    'D-':      [2, 13],
    'Dmin':    [2, 13],

    # D augmented
    'D+':      [2, 14],
    'Daug':    [2, 14],
    'DM#5':    [2, 14],
    'DM+5':     [2, 14],

    # D diminished
    'Do':      [2, 15],
    'Ddim':    [2, 15],
    'Dmb5':    [2, 15],
    'Dmo5':    [2, 15],
# --------------------------------
#   D# TRIADS
# --------------------------------
    # D# major
    'D#maj':    [3, 12],
    'D#M':      [3, 12],
    'D#Δ':      [3, 12],
    'D#':       [3, 12],

    # D# minor
    'D#m':      [3, 13],
    'D#-':      [3, 13],
    'D#min':    [3, 13],

    # D# augmented
    'D#+':      [3, 14],
    'D#aug':    [3, 14],
    'D#M#5':    [3, 14],
    'D#M+5':     [3, 14],

    # D# diminished
    'D#o':      [3, 15],
    'D#dim':    [3, 15],
    'D#mb5':    [3, 15],
    'D#mo5':    [3, 15],
# --------------------------------
#   Eb TRIADS
# --------------------------------
    # Eb major
    'Ebmaj':    [3, 12],
    'EbM':      [3, 12],
    'EbΔ':      [3, 12],
    'Eb':       [3, 12],

    # Eb minor
    'Ebm':      [3, 13],
    'Eb-':      [3, 13],
    'Ebmin':    [3, 13],

    # Eb augmented
    'Eb+':      [3, 14],
    'Ebaug':    [3, 14],
    'EbM#5':    [3, 14],
    'EbM+5':     [3, 14],

    # Eb diminished
    'Ebo':      [3, 15],
    'Ebdim':    [3, 15],
    'Ebmb5':    [3, 15],
    'Ebmo5':    [3, 15],
# --------------------------------
#   E TRIADS
# --------------------------------
    # E major
    'Emaj':    [4, 12],
    'EM':      [4, 12],
    'EΔ':      [4, 12],
    'E':       [4, 12],

    # E minor
    'Em':      [4, 13],
    'E-':      [4, 13],
    'Emin':    [4, 13],

    # E augmented
    'E+':      [4, 14],
    'Eaug':    [4, 14],
    'EM#5':    [4, 14],
    'EM+5':     [4, 14],

    # E diminished
    'Eo':      [4, 15],
    'Edim':    [4, 15],
    'Emb5':    [4, 15],
    'Emo5':    [4, 15],
# --------------------------------
#   F TRIADS
# --------------------------------
    # F major
    'Fmaj':    [5, 12],
    'FM':      [5, 12],
    'FΔ':      [5, 12],
    'F':       [5, 12],

    # F minor
    'Fm':      [5, 13],
    'F-':      [5, 13],
    'Fmin':    [5, 13],

    # F augmented
    'F+':      [5, 14],
    'Faug':    [5, 14],
    'FM#5':    [5, 14],
    'FM+5':     [5, 14],

    # F diminished
    'Fo':      [5, 15],
    'Fdim':    [5, 15],
    'Fmb5':    [5, 15],
    'Fmo5':    [5, 15],
# --------------------------------
#   F# TRIADS
# --------------------------------
    # F# major
    'F#maj':    [6, 12],
    'F#M':      [6, 12],
    'F#Δ':      [6, 12],
    'F#':       [6, 12],

    # F# minor
    'F#m':      [6, 13],
    'F#-':      [6, 13],
    'F#min':    [6, 13],

    # F# augmented
    'F#+':      [6, 14],
    'F#aug':    [6, 14],
    'F#M#5':    [6, 14],
    'F#M+5':     [6, 14],

    # F# diminished
    'F#o':      [6, 15],
    'F#dim':    [6, 15],
    'F#mb5':    [6, 15],
    'F#mo5':    [6, 15],
# --------------------------------
#   Gb TRIADS
# --------------------------------
    # Gb major
    'Gbmaj':    [6, 12],
    'GbM':      [6, 12],
    'GbΔ':      [6, 12],
    'Gb':       [6, 12],

    # Gb minor
    'Gbm':      [6, 13],
    'Gb-':      [6, 13],
    'Gbmin':    [6, 13],

    # Gb augmented
    'Gb+':      [6, 14],
    'Gbaug':    [6, 14],
    'GbM#5':    [6, 14],
    'GbM+5':     [6, 14],

    # Gb diminished
    'Gbo':      [6, 15],
    'Gbdim':    [6, 15],
    'Gbmb5':    [6, 15],
    'Gbmo5':    [6, 15],
# --------------------------------
#   G TRIADS
# --------------------------------
    # G major
    'Gmaj':    [7, 12],
    'GM':      [7, 12],
    'GΔ':      [7, 12],
    'G':       [7, 12],

    # G minor
    'Gm':      [7, 13],
    'G-':      [7, 13],
    'Gmin':    [7, 13],

    # G augmented
    'G+':      [7, 14],
    'Gaug':    [7, 14],
    'GM#5':    [7, 14],
    'GM+5':     [7, 14],

    # G diminished
    'Go':      [7, 15],
    'Gdim':    [7, 15],
    'Gmb5':    [7, 15],
    'Gmo5':    [7, 15],
# --------------------------------
#   G# TRIADS
# --------------------------------
    # G# major
    'G#maj':    [8, 12],
    'G#M':      [8, 12],
    'G#Δ':      [8, 12],
    'G#':       [8, 12],

    # G# minor
    'G#m':      [8, 13],
    'G#-':      [8, 13],
    'G#min':    [8, 13],

    # G# augmented
    'G#+':      [8, 14],
    'G#aug':    [8, 14],
    'G#M#5':    [8, 14],
    'G#M+5':     [8, 14],

    # G# diminished
    'G#o':      [8, 15],
    'G#dim':    [8, 15],
    'G#mb5':    [8, 15],
    'G#mo5':    [8, 15],
# --------------------------------
#   Ab TRIADS
# --------------------------------
    # Ab major
    'Abmaj':    [8, 12],
    'AbM':      [8, 12],
    'AbΔ':      [8, 12],
    'Ab':       [8, 12],

    # Ab minor
    'Abm':      [8, 13],
    'Ab-':      [8, 13],
    'Abmin':    [8, 13],

    # Ab augmented
    'Ab+':      [8, 14],
    'Abaug':    [8, 14],
    'AbM#5':    [8, 14],
    'AbM+5':     [8, 14],

    # Ab diminished
    'Abo':      [8, 15],
    'Abdim':    [8, 15],
    'Abmb5':    [8, 15],
    'Abmo5':    [8, 15],
# --------------------------------
#   A TRIADS
# --------------------------------
    # A major
    'Amaj':    [9, 12],
    'AM':      [9, 12],
    'AΔ':      [9, 12],
    'A':       [9, 12],

    # A minor
    'Am':      [9, 13],
    'A-':      [9, 13],
    'Amin':    [9, 13],

    # A augmented
    'A+':      [9, 14],
    'Aaug':    [9, 14],
    'AM#5':    [9, 14],
    'AM+5':     [9, 14],

    # A diminished
    'Ao':      [9, 15],
    'Adim':    [9, 15],
    'Amb5':    [9, 15],
    'Amo5':    [9, 15],
# --------------------------------
#   A# TRIADS
# --------------------------------
    # A# major
    'A#maj':    [10, 12],
    'A#M':      [10, 12],
    'A#Δ':      [10, 12],
    'A#':       [10, 12],

    # A# minor
    'A#m':      [10, 13],
    'A#-':      [10, 13],
    'A#min':    [10, 13],

    # A# augmented
    'A#+':      [10, 14],
    'A#aug':    [10, 14],
    'A#M#5':    [10, 14],
    'A#M+5':     [10, 14],

    # A# diminished
    'A#o':      [10, 15],
    'A#dim':    [10, 15],
    'A#mb5':    [10, 15],
    'A#mo5':    [10, 15],
# --------------------------------
#   Bb TRIADS
# --------------------------------
    # Bb major
    'Bbmaj':    [10, 12],
    'BbM':      [10, 12],
    'BbΔ':      [10, 12],
    'Bb':       [10, 12],

    # Bb minor
    'Bbm':      [10, 13],
    'Bb-':      [10, 13],
    'Bbmin':    [10, 13],

    # Bb augmented
    'Bb+':      [10, 14],
    'Bbaug':    [10, 14],
    'BbM#5':    [10, 14],
    'BbM+5':     [10, 14],

    # Bb diminished
    'Bbo':      [10, 15],
    'Bbdim':    [10, 15],
    'Bbmb5':    [10, 15],
    'Bbmo5':    [10, 15],
# --------------------------------
#   B TRIADS
# --------------------------------
    # B major
    'Bmaj':    [11, 12],
    'BM':      [11, 12],
    'BΔ':      [11, 12],
    'B':       [11, 12],

    # B minor
    'Bm':      [11, 13],
    'B-':      [11, 13],
    'Bmin':    [11, 13],

    # B augmented
    'B+':      [11, 14],
    'Baug':    [11, 14],
    'BM#5':    [11, 14],
    'BM+5':     [11, 14],

    # B diminished
    'Bo':      [11, 15],
    'Bdim':    [11, 15],
    'Bmb5':    [11, 15],
    'Bmo5':    [11, 15],



# --------------------------------
#   C SEVENTHS
# --------------------------------
    # C dominant seventh
    'C7':       [0, 16],
    'Cdom7':    [0, 16],

    # C dominant flat seventh
    'C7b5':     [0, 17],
    'C7dim5':   [0, 17],

    # C major seventh
    'CM7':      [0, 18],
    'Cmaj7':    [0, 18],
    'CΔ7':      [0, 18],

    # C major seventh flat five
    'CM7b5':    [0, 19],
    'CΔ7b5':    [0, 19],

    # C minor-major seventh
    'CmM7':     [0, 20],
    'Cm#7':     [0, 20],
    'C-M7':     [0, 20],
    'C-Δ7':     [0, 20],
    'Cminmaj7':     [0, 20],
    'Cmin-maj7':    [0, 20],

    # C minor seventh
    'Cm7':      [0, 21],
    'C-7':      [0, 21],
    'Cmin7':    [0, 21],

    # C augmented-major seventh
    'C+M7':     [0, 22],
    'Caugmaj7':     [0, 22],
    'Caug-maj7':    [0, 22],
    'CM7#5':     [0, 22],
    'CM7+5':     [0, 22],
    'CΔ7#5':     [0, 22],
    'CΔ7+5':     [0, 22],

    # C augmented seventh
    'C+7':      [0, 23],
    'Caug7':    [0, 23],
    'C7#5':     [0, 23],
    'C7+5':     [0, 23],

    # C half-diminished seventh
    'Cø':       [0, 24],
    'Cø7':      [0, 24],
    'Cmin7dim5':    [0, 24],
    'Cm7b5':    [0, 24],
    'Cm7o5':    [0, 24],
    'C-7b5':    [0, 24],
    'C-7o5':    [0, 24],

    # C diminished seventh
    'Co7':       [0, 25],
    'Cdim7':     [0, 25],

    # C diminished major seventh
    'CmM7b5':     [0, 26],
    'C-Δ7b5':     [0, 26],
    'CoM7':       [0, 26],
# --------------------------------
#   C# SEVENTHS
# --------------------------------
    # C# dominant seventh
    'C#7':       [1, 16],
    'C#dom7':    [1, 16],

    # C# dominant flat seventh
    'C#7b5':     [1, 17],
    'C#7dim5':   [1, 17],

    # C# major seventh
    'C#M7':      [1, 18],
    'C#maj7':    [1, 18],
    'C#Δ7':      [1, 18],

    # C# major seventh flat five
    'C#M7b5':    [1, 19],
    'C#Δ7b5':    [1, 19],

    # C# minor-major seventh
    'C#mM7':     [1, 20],
    'C#m#7':     [1, 20],
    'C#-M7':     [1, 20],
    'C#-Δ7':     [1, 20],
    'C#minmaj7':     [1, 20],
    'C#min-maj7':    [1, 20],

    # C# minor seventh
    'C#m7':      [1, 21],
    'C#-7':      [1, 21],
    'C#min7':    [1, 21],

    # C# augmented-major seventh
    'C#+M7':     [1, 22],
    'C#augmaj7':     [1, 22],
    'C#aug-maj7':    [1, 22],
    'C#M7#5':     [1, 22],
    'C#M7+5':     [1, 22],
    'C#Δ7#5':     [1, 22],
    'C#Δ7+5':     [1, 22],

    # C# augmented seventh
    'C#+7':      [1, 23],
    'C#aug7':    [1, 23],
    'C#7#5':     [1, 23],
    'C#7+5':     [1, 23],

    # C# half-diminished seventh
    'C#ø':       [1, 24],
    'C#ø7':      [1, 24],
    'C#min7dim5':    [1, 24],
    'C#m7b5':    [1, 24],
    'C#m7o5':    [1, 24],
    'C#-7b5':    [1, 24],
    'C#-7o5':    [1, 24],

    # C# diminished seventh
    'C#o7':       [1, 25],
    'C#dim7':     [1, 25],

    # C# diminished major seventh
    'C#mM7b5':     [1, 26],
    'C#-Δ7b5':     [1, 26],
    'C#oM7':       [1, 26],
# --------------------------------
#   Db SEVENTHS
# --------------------------------
    # Db dominant seventh
    'Db7':       [1, 16],
    'Dbdom7':    [1, 16],

    # Db dominant flat seventh
    'Db7b5':     [1, 17],
    'Db7dim5':   [1, 17],

    # Db major seventh
    'DbM7':      [1, 18],
    'Dbmaj7':    [1, 18],
    'DbΔ7':      [1, 18],

    # Db major seventh flat five
    'DbM7b5':    [1, 19],
    'DbΔ7b5':    [1, 19],

    # Db minor-major seventh
    'DbmM7':     [1, 20],
    'Dbm#7':     [1, 20],
    'Db-M7':     [1, 20],
    'Db-Δ7':     [1, 20],
    'Dbminmaj7':     [1, 20],
    'Dbmin-maj7':    [1, 20],

    # Db minor seventh
    'Dbm7':      [1, 21],
    'Db-7':      [1, 21],
    'Dbmin7':    [1, 21],

    # Db augmented-major seventh
    'Db+M7':     [1, 22],
    'Dbaugmaj7':     [1, 22],
    'Dbaug-maj7':    [1, 22],
    'DbM7#5':     [1, 22],
    'DbM7+5':     [1, 22],
    'DbΔ7#5':     [1, 22],
    'DbΔ7+5':     [1, 22],

    # Db augmented seventh
    'Db+7':      [1, 23],
    'Dbaug7':    [1, 23],
    'Db7#5':     [1, 23],
    'Db7+5':     [1, 23],

    # Db half-diminished seventh
    'Dbø':       [1, 24],
    'Dbø7':      [1, 24],
    'Dbmin7dim5':    [1, 24],
    'Dbm7b5':    [1, 24],
    'Dbm7o5':    [1, 24],
    'Db-7b5':    [1, 24],
    'Db-7o5':    [1, 24],

    # Db diminished seventh
    'Dbo7':       [1, 25],
    'Dbdim7':     [1, 25],

    # Db diminished major seventh
    'DbmM7b5':     [1, 26],
    'Db-Δ7b5':     [1, 26],
    'DboM7':       [1, 26],
# --------------------------------
#   D SEVENTHS
# --------------------------------
    # D dominant seventh
    'D7':       [2, 16],
    'Ddom7':    [2, 16],

    # D dominant flat seventh
    'D7b5':     [2, 17],
    'D7dim5':   [2, 17],

    # D major seventh
    'DM7':      [2, 18],
    'Dmaj7':    [2, 18],
    'DΔ7':      [2, 18],

    # D major seventh flat five
    'DM7b5':    [2, 19],
    'DΔ7b5':    [2, 19],

    # D minor-major seventh
    'DmM7':     [2, 20],
    'Dm#7':     [2, 20],
    'D-M7':     [2, 20],
    'D-Δ7':     [2, 20],
    'Dminmaj7':     [2, 20],
    'Dmin-maj7':    [2, 20],

    # D minor seventh
    'Dm7':      [2, 21],
    'D-7':      [2, 21],
    'Dmin7':    [2, 21],

    # D augmented-major seventh
    'D+M7':     [2, 22],
    'Daugmaj7':     [2, 22],
    'Daug-maj7':    [2, 22],
    'DM7#5':     [2, 22],
    'DM7+5':     [2, 22],
    'DΔ7#5':     [2, 22],
    'DΔ7+5':     [2, 22],

    # D augmented seventh
    'D+7':      [2, 23],
    'Daug7':    [2, 23],
    'D7#5':     [2, 23],
    'D7+5':     [2, 23],

    # D half-diminished seventh
    'Dø':       [2, 24],
    'Dø7':      [2, 24],
    'Dmin7dim5':    [2, 24],
    'Dm7b5':    [2, 24],
    'Dm7o5':    [2, 24],
    'D-7b5':    [2, 24],
    'D-7o5':    [2, 24],

    # D diminished seventh
    'Do7':       [2, 25],
    'Ddim7':     [2, 25],

    # D diminished major seventh
    'DmM7b5':     [2, 26],
    'D-Δ7b5':     [2, 26],
    'DoM7':       [2, 26],
# --------------------------------
#   D# SEVENTHS
# --------------------------------
    # D# dominant seventh
    'D#7':       [3, 16],
    'D#dom7':    [3, 16],

    # D# dominant flat seventh
    'D#7b5':     [3, 17],
    'D#7dim5':   [3, 17],

    # D# major seventh
    'D#M7':      [3, 18],
    'D#maj7':    [3, 18],
    'D#Δ7':      [3, 18],

    # D# major seventh flat five
    'D#M7b5':    [3, 19],
    'D#Δ7b5':    [3, 19],

    # D# minor-major seventh
    'D#mM7':     [3, 20],
    'D#m#7':     [3, 20],
    'D#-M7':     [3, 20],
    'D#-Δ7':     [3, 20],
    'D#minmaj7':     [3, 20],
    'D#min-maj7':    [3, 20],

    # D# minor seventh
    'D#m7':      [3, 21],
    'D#-7':      [3, 21],
    'D#min7':    [3, 21],

    # D# augmented-major seventh
    'D#+M7':     [3, 22],
    'D#augmaj7':     [3, 22],
    'D#aug-maj7':    [3, 22],
    'D#M7#5':     [3, 22],
    'D#M7+5':     [3, 22],
    'D#Δ7#5':     [3, 22],
    'D#Δ7+5':     [3, 22],

    # D# augmented seventh
    'D#+7':      [3, 23],
    'D#aug7':    [3, 23],
    'D#7#5':     [3, 23],
    'D#7+5':     [3, 23],

    # D# half-diminished seventh
    'D#ø':       [3, 24],
    'D#ø7':      [3, 24],
    'D#min7dim5':    [3, 24],
    'D#m7b5':    [3, 24],
    'D#m7o5':    [3, 24],
    'D#-7b5':    [3, 24],
    'D#-7o5':    [3, 24],

    # D# diminished seventh
    'D#o7':       [3, 25],
    'D#dim7':     [3, 25],

    # D# diminished major seventh
    'D#mM7b5':     [3, 26],
    'D#-Δ7b5':     [3, 26],
    'D#oM7':       [3, 26],
# --------------------------------
#   Eb SEVENTHS
# --------------------------------
    # Eb dominant seventh
    'Eb7':       [3, 16],
    'Ebdom7':    [3, 16],

    # Eb dominant flat seventh
    'Eb7b5':     [3, 17],
    'Eb7dim5':   [3, 17],

    # Eb major seventh
    'EbM7':      [3, 18],
    'Ebmaj7':    [3, 18],
    'EbΔ7':      [3, 18],

    # Eb major seventh flat five
    'EbM7b5':    [3, 19],
    'EbΔ7b5':    [3, 19],

    # Eb minor-major seventh
    'EbmM7':     [3, 20],
    'Ebm#7':     [3, 20],
    'Eb-M7':     [3, 20],
    'Eb-Δ7':     [3, 20],
    'Ebminmaj7':     [3, 20],
    'Ebmin-maj7':    [3, 20],

    # Eb minor seventh
    'Ebm7':      [3, 21],
    'Eb-7':      [3, 21],
    'Ebmin7':    [3, 21],

    # Eb augmented-major seventh
    'Eb+M7':     [3, 22],
    'Ebaugmaj7':     [3, 22],
    'Ebaug-maj7':    [3, 22],
    'EbM7#5':     [3, 22],
    'EbM7+5':     [3, 22],
    'EbΔ7#5':     [3, 22],
    'EbΔ7+5':     [3, 22],

    # Eb augmented seventh
    'Eb+7':      [3, 23],
    'Ebaug7':    [3, 23],
    'Eb7#5':     [3, 23],
    'Eb7+5':     [3, 23],

    # Eb half-diminished seventh
    'Ebø':       [3, 24],
    'Ebø7':      [3, 24],
    'Ebmin7dim5':    [3, 24],
    'Ebm7b5':    [3, 24],
    'Ebm7o5':    [3, 24],
    'Eb-7b5':    [3, 24],
    'Eb-7o5':    [3, 24],

    # Eb diminished seventh
    'Ebo7':       [3, 25],
    'Ebdim7':     [3, 25],

    # Eb diminished major seventh
    'EbmM7b5':     [3, 26],
    'Eb-Δ7b5':     [3, 26],
    'EboM7':       [3, 26],
# --------------------------------
#   E SEVENTHS
# --------------------------------
    # E dominant seventh
    'E7':       [4, 16],
    'Edom7':    [4, 16],

    # E dominant flat seventh
    'E7b5':     [4, 17],
    'E7dim5':   [4, 17],

    # E major seventh
    'EM7':      [4, 18],
    'Emaj7':    [4, 18],
    'EΔ7':      [4, 18],

    # E major seventh flat five
    'EM7b5':    [4, 19],
    'EΔ7b5':    [4, 19],

    # E minor-major seventh
    'EmM7':     [4, 20],
    'Em#7':     [4, 20],
    'E-M7':     [4, 20],
    'E-Δ7':     [4, 20],
    'Eminmaj7':     [4, 20],
    'Emin-maj7':    [4, 20],

    # E minor seventh
    'Em7':      [4, 21],
    'E-7':      [4, 21],
    'Emin7':    [4, 21],

    # E augmented-major seventh
    'E+M7':     [4, 22],
    'Eaugmaj7':     [4, 22],
    'Eaug-maj7':    [4, 22],
    'EM7#5':     [4, 22],
    'EM7+5':     [4, 22],
    'EΔ7#5':     [4, 22],
    'EΔ7+5':     [4, 22],

    # E augmented seventh
    'E+7':      [4, 23],
    'Eaug7':    [4, 23],
    'E7#5':     [4, 23],
    'E7+5':     [4, 23],

    # E half-diminished seventh
    'Eø':       [4, 24],
    'Eø7':      [4, 24],
    'Emin7dim5':    [4, 24],
    'Em7b5':    [4, 24],
    'Em7o5':    [4, 24],
    'E-7b5':    [4, 24],
    'E-7o5':    [4, 24],

    # E diminished seventh
    'Eo7':       [4, 25],
    'Edim7':     [4, 25],

    # E diminished major seventh
    'EmM7b5':     [4, 26],
    'E-Δ7b5':     [4, 26],
    'EoM7':       [4, 26],
# --------------------------------
#   F SEVENTHS
# --------------------------------
    # F dominant seventh
    'F7':       [5, 16],
    'Fdom7':    [5, 16],

    # F dominant flat seventh
    'F7b5':     [5, 17],
    'F7dim5':   [5, 17],

    # F major seventh
    'FM7':      [5, 18],
    'Fmaj7':    [5, 18],
    'FΔ7':      [5, 18],

    # F major seventh flat five
    'FM7b5':    [5, 19],
    'FΔ7b5':    [5, 19],

    # F minor-major seventh
    'FmM7':     [5, 20],
    'Fm#7':     [5, 20],
    'F-M7':     [5, 20],
    'F-Δ7':     [5, 20],
    'Fminmaj7':     [5, 20],
    'Fmin-maj7':    [5, 20],

    # F minor seventh
    'Fm7':      [5, 21],
    'F-7':      [5, 21],
    'Fmin7':    [5, 21],

    # F augmented-major seventh
    'F+M7':     [5, 22],
    'Faugmaj7':     [5, 22],
    'Faug-maj7':    [5, 22],
    'FM7#5':     [5, 22],
    'FM7+5':     [5, 22],
    'FΔ7#5':     [5, 22],
    'FΔ7+5':     [5, 22],

    # F augmented seventh
    'F+7':      [5, 23],
    'Faug7':    [5, 23],
    'F7#5':     [5, 23],
    'F7+5':     [5, 23],

    # F half-diminished seventh
    'Fø':       [5, 24],
    'Fø7':      [5, 24],
    'Fmin7dim5':    [5, 24],
    'Fm7b5':    [5, 24],
    'Fm7o5':    [5, 24],
    'F-7b5':    [5, 24],
    'F-7o5':    [5, 24],

    # F diminished seventh
    'Fo7':       [5, 25],
    'Fdim7':     [5, 25],

    # F diminished major seventh
    'FmM7b5':     [5, 26],
    'F-Δ7b5':     [5, 26],
    'FoM7':       [5, 26],
# --------------------------------
#   F# SEVENTHS
# --------------------------------
    # F# dominant seventh
    'F#7':       [6, 16],
    'F#dom7':    [6, 16],

    # F# dominant flat seventh
    'F#7b5':     [6, 17],
    'F#7dim5':   [6, 17],

    # F# major seventh
    'F#M7':      [6, 18],
    'F#maj7':    [6, 18],
    'F#Δ7':      [6, 18],

    # F# major seventh flat five
    'F#M7b5':    [6, 19],
    'F#Δ7b5':    [6, 19],

    # F# minor-major seventh
    'F#mM7':     [6, 20],
    'F#m#7':     [6, 20],
    'F#-M7':     [6, 20],
    'F#-Δ7':     [6, 20],
    'F#minmaj7':     [6, 20],
    'F#min-maj7':    [6, 20],

    # F# minor seventh
    'F#m7':      [6, 21],
    'F#-7':      [6, 21],
    'F#min7':    [6, 21],

    # F# augmented-major seventh
    'F#+M7':     [6, 22],
    'F#augmaj7':     [6, 22],
    'F#aug-maj7':    [6, 22],
    'F#M7#5':     [6, 22],
    'F#M7+5':     [6, 22],
    'F#Δ7#5':     [6, 22],
    'F#Δ7+5':     [6, 22],

    # F# augmented seventh
    'F#+7':      [6, 23],
    'F#aug7':    [6, 23],
    'F#7#5':     [6, 23],
    'F#7+5':     [6, 23],

    # F# half-diminished seventh
    'F#ø':       [6, 24],
    'F#ø7':      [6, 24],
    'F#min7dim5':    [6, 24],
    'F#m7b5':    [6, 24],
    'F#m7o5':    [6, 24],
    'F#-7b5':    [6, 24],
    'F#-7o5':    [6, 24],

    # F# diminished seventh
    'F#o7':       [6, 25],
    'F#dim7':     [6, 25],

    # F# diminished major seventh
    'F#mM7b5':     [6, 26],
    'F#-Δ7b5':     [6, 26],
    'F#oM7':       [6, 26],
# --------------------------------
#   Gb SEVENTHS
# --------------------------------
    # Gb dominant seventh
    'Gb7':       [6, 16],
    'Gbdom7':    [6, 16],

    # Gb dominant flat seventh
    'Gb7b5':     [6, 17],
    'Gb7dim5':   [6, 17],

    # Gb major seventh
    'GbM7':      [6, 18],
    'Gbmaj7':    [6, 18],
    'GbΔ7':      [6, 18],

    # Gb major seventh flat five
    'GbM7b5':    [6, 19],
    'GbΔ7b5':    [6, 19],

    # Gb minor-major seventh
    'GbmM7':     [6, 20],
    'Gbm#7':     [6, 20],
    'Gb-M7':     [6, 20],
    'Gb-Δ7':     [6, 20],
    'Gbminmaj7':     [6, 20],
    'Gbmin-maj7':    [6, 20],

    # Gb minor seventh
    'Gbm7':      [6, 21],
    'Gb-7':      [6, 21],
    'Gbmin7':    [6, 21],

    # Gb augmented-major seventh
    'Gb+M7':     [6, 22],
    'Gbaugmaj7':     [6, 22],
    'Gbaug-maj7':    [6, 22],
    'GbM7#5':     [6, 22],
    'GbM7+5':     [6, 22],
    'GbΔ7#5':     [6, 22],
    'GbΔ7+5':     [6, 22],

    # Gb augmented seventh
    'Gb+7':      [6, 23],
    'Gbaug7':    [6, 23],
    'Gb7#5':     [6, 23],
    'Gb7+5':     [6, 23],

    # Gb half-diminished seventh
    'Gbø':       [6, 24],
    'Gbø7':      [6, 24],
    'Gbmin7dim5':    [6, 24],
    'Gbm7b5':    [6, 24],
    'Gbm7o5':    [6, 24],
    'Gb-7b5':    [6, 24],
    'Gb-7o5':    [6, 24],

    # Gb diminished seventh
    'Gbo7':       [6, 25],
    'Gbdim7':     [6, 25],

    # Gb diminished major seventh
    'GbmM7b5':     [6, 26],
    'Gb-Δ7b5':     [6, 26],
    'GboM7':       [6, 26],
# --------------------------------
#   G SEVENTHS
# --------------------------------
    # G dominant seventh
    'G7':       [7, 16],
    'Gdom7':    [7, 16],

    # G dominant flat seventh
    'G7b5':     [7, 17],
    'G7dim5':   [7, 17],

    # G major seventh
    'GM7':      [7, 18],
    'Gmaj7':    [7, 18],
    'GΔ7':      [7, 18],

    # G major seventh flat five
    'GM7b5':    [7, 19],
    'GΔ7b5':    [7, 19],

    # G minor-major seventh
    'GmM7':     [7, 20],
    'Gm#7':     [7, 20],
    'G-M7':     [7, 20],
    'G-Δ7':     [7, 20],
    'Gminmaj7':     [7, 20],
    'Gmin-maj7':    [7, 20],

    # G minor seventh
    'Gm7':      [7, 21],
    'G-7':      [7, 21],
    'Gmin7':    [7, 21],

    # G augmented-major seventh
    'G+M7':     [7, 22],
    'Gaugmaj7':     [7, 22],
    'Gaug-maj7':    [7, 22],
    'GM7#5':     [7, 22],
    'GM7+5':     [7, 22],
    'GΔ7#5':     [7, 22],
    'GΔ7+5':     [7, 22],

    # G augmented seventh
    'G+7':      [7, 23],
    'Gaug7':    [7, 23],
    'G7#5':     [7, 23],
    'G7+5':     [7, 23],

    # G half-diminished seventh
    'Gø':       [7, 24],
    'Gø7':      [7, 24],
    'Gmin7dim5':    [7, 24],
    'Gm7b5':    [7, 24],
    'Gm7o5':    [7, 24],
    'G-7b5':    [7, 24],
    'G-7o5':    [7, 24],

    # G diminished seventh
    'Go7':       [7, 25],
    'Gdim7':     [7, 25],

    # G diminished major seventh
    'GmM7b5':     [7, 26],
    'G-Δ7b5':     [7, 26],
    'GoM7':       [7, 26],
# --------------------------------
#   G# SEVENTHS
# --------------------------------
    # G# dominant seventh
    'G#7':       [8, 16],
    'G#dom7':    [8, 16],

    # G# dominant flat seventh
    'G#7b5':     [8, 17],
    'G#7dim5':   [8, 17],

    # G# major seventh
    'G#M7':      [8, 18],
    'G#maj7':    [8, 18],
    'G#Δ7':      [8, 18],

    # G# major seventh flat five
    'G#M7b5':    [8, 19],
    'G#Δ7b5':    [8, 19],

    # G# minor-major seventh
    'G#mM7':     [8, 20],
    'G#m#7':     [8, 20],
    'G#-M7':     [8, 20],
    'G#-Δ7':     [8, 20],
    'G#minmaj7':     [8, 20],
    'G#min-maj7':    [8, 20],

    # G# minor seventh
    'G#m7':      [8, 21],
    'G#-7':      [8, 21],
    'G#min7':    [8, 21],

    # G# augmented-major seventh
    'G#+M7':     [8, 22],
    'G#augmaj7':     [8, 22],
    'G#aug-maj7':    [8, 22],
    'G#M7#5':     [8, 22],
    'G#M7+5':     [8, 22],
    'G#Δ7#5':     [8, 22],
    'G#Δ7+5':     [8, 22],

    # G# augmented seventh
    'G#+7':      [8, 23],
    'G#aug7':    [8, 23],
    'G#7#5':     [8, 23],
    'G#7+5':     [8, 23],

    # G# half-diminished seventh
    'G#ø':       [8, 24],
    'G#ø7':      [8, 24],
    'G#min7dim5':    [8, 24],
    'G#m7b5':    [8, 24],
    'G#m7o5':    [8, 24],
    'G#-7b5':    [8, 24],
    'G#-7o5':    [8, 24],

    # G# diminished seventh
    'G#o7':       [8, 25],
    'G#dim7':     [8, 25],

    # G# diminished major seventh
    'G#mM7b5':     [8, 26],
    'G#-Δ7b5':     [8, 26],
    'G#oM7':       [8, 26],
# --------------------------------
#   Ab SEVENTHS
# --------------------------------
    # Ab dominant seventh
    'Ab7':       [8, 16],
    'Abdom7':    [8, 16],

    # Ab dominant flat seventh
    'Ab7b5':     [8, 17],
    'Ab7dim5':   [8, 17],

    # Ab major seventh
    'AbM7':      [8, 18],
    'Abmaj7':    [8, 18],
    'AbΔ7':      [8, 18],

    # Ab major seventh flat five
    'AbM7b5':    [8, 19],
    'AbΔ7b5':    [8, 19],

    # Ab minor-major seventh
    'AbmM7':     [8, 20],
    'Abm#7':     [8, 20],
    'Ab-M7':     [8, 20],
    'Ab-Δ7':     [8, 20],
    'Abminmaj7':     [8, 20],
    'Abmin-maj7':    [8, 20],

    # Ab minor seventh
    'Abm7':      [8, 21],
    'Ab-7':      [8, 21],
    'Abmin7':    [8, 21],

    # Ab augmented-major seventh
    'Ab+M7':     [8, 22],
    'Abaugmaj7':     [8, 22],
    'Abaug-maj7':    [8, 22],
    'AbM7#5':     [8, 22],
    'AbM7+5':     [8, 22],
    'AbΔ7#5':     [8, 22],
    'AbΔ7+5':     [8, 22],

    # Ab augmented seventh
    'Ab+7':      [8, 23],
    'Abaug7':    [8, 23],
    'Ab7#5':     [8, 23],
    'Ab7+5':     [8, 23],

    # Ab half-diminished seventh
    'Abø':       [8, 24],
    'Abø7':      [8, 24],
    'Abmin7dim5':    [8, 24],
    'Abm7b5':    [8, 24],
    'Abm7o5':    [8, 24],
    'Ab-7b5':    [8, 24],
    'Ab-7o5':    [8, 24],

    # Ab diminished seventh
    'Abo7':       [8, 25],
    'Abdim7':     [8, 25],

    # Ab diminished major seventh
    'AbmM7b5':     [8, 26],
    'Ab-Δ7b5':     [8, 26],
    'AboM7':       [8, 26],
# --------------------------------
#   A SEVENTHS
# --------------------------------
    # A dominant seventh
    'A7':       [9, 16],
    'Adom7':    [9, 16],

    # A dominant flat seventh
    'A7b5':     [9, 17],
    'A7dim5':   [9, 17],

    # A major seventh
    'AM7':      [9, 18],
    'Amaj7':    [9, 18],
    'AΔ7':      [9, 18],

    # A major seventh flat five
    'AM7b5':    [9, 19],
    'AΔ7b5':    [9, 19],

    # A minor-major seventh
    'AmM7':     [9, 20],
    'Am#7':     [9, 20],
    'A-M7':     [9, 20],
    'A-Δ7':     [9, 20],
    'Aminmaj7':     [9, 20],
    'Amin-maj7':    [9, 20],

    # A minor seventh
    'Am7':      [9, 21],
    'A-7':      [9, 21],
    'Amin7':    [9, 21],

    # A augmented-major seventh
    'A+M7':     [9, 22],
    'Aaugmaj7':     [9, 22],
    'Aaug-maj7':    [9, 22],
    'AM7#5':     [9, 22],
    'AM7+5':     [9, 22],
    'AΔ7#5':     [9, 22],
    'AΔ7+5':     [9, 22],

    # A augmented seventh
    'A+7':      [9, 23],
    'Aaug7':    [9, 23],
    'A7#5':     [9, 23],
    'A7+5':     [9, 23],

    # A half-diminished seventh
    'Aø':       [9, 24],
    'Aø7':      [9, 24],
    'Amin7dim5':    [9, 24],
    'Am7b5':    [9, 24],
    'Am7o5':    [9, 24],
    'A-7b5':    [9, 24],
    'A-7o5':    [9, 24],

    # A diminished seventh
    'Ao7':       [9, 25],
    'Adim7':     [9, 25],

    # A diminished major seventh
    'AmM7b5':     [9, 26],
    'A-Δ7b5':     [9, 26],
    'AoM7':       [9, 26],
# --------------------------------
#   A# SEVENTHS
# --------------------------------
    # A# dominant seventh
    'A#7':       [10, 16],
    'A#dom7':    [10, 16],

    # A# dominant flat seventh
    'A#7b5':     [10, 17],
    'A#7dim5':   [10, 17],

    # A# major seventh
    'A#M7':      [10, 18],
    'A#maj7':    [10, 18],
    'A#Δ7':      [10, 18],

    # A# major seventh flat five
    'A#M7b5':    [10, 19],
    'A#Δ7b5':    [10, 19],

    # A# minor-major seventh
    'A#mM7':     [10, 20],
    'A#m#7':     [10, 20],
    'A#-M7':     [10, 20],
    'A#-Δ7':     [10, 20],
    'A#minmaj7':     [10, 20],
    'A#min-maj7':    [10, 20],

    # A# minor seventh
    'A#m7':      [10, 21],
    'A#-7':      [10, 21],
    'A#min7':    [10, 21],

    # A# augmented-major seventh
    'A#+M7':     [10, 22],
    'A#augmaj7':     [10, 22],
    'A#aug-maj7':    [10, 22],
    'A#M7#5':     [10, 22],
    'A#M7+5':     [10, 22],
    'A#Δ7#5':     [10, 22],
    'A#Δ7+5':     [10, 22],

    # A# augmented seventh
    'A#+7':      [10, 23],
    'A#aug7':    [10, 23],
    'A#7#5':     [10, 23],
    'A#7+5':     [10, 23],

    # A# half-diminished seventh
    'A#ø':       [10, 24],
    'A#ø7':      [10, 24],
    'A#min7dim5':    [10, 24],
    'A#m7b5':    [10, 24],
    'A#m7o5':    [10, 24],
    'A#-7b5':    [10, 24],
    'A#-7o5':    [10, 24],

    # A# diminished seventh
    'A#o7':       [10, 25],
    'A#dim7':     [10, 25],

    # A# diminished major seventh
    'A#mM7b5':     [10, 26],
    'A#-Δ7b5':     [10, 26],
    'A#oM7':       [10, 26],
# --------------------------------
#   Bb SEVENTHS
# --------------------------------
    # Bb dominant seventh
    'Bb7':       [10, 16],
    'Bbdom7':    [10, 16],

    # Bb dominant flat seventh
    'Bb7b5':     [10, 17],
    'Bb7dim5':   [10, 17],

    # Bb major seventh
    'BbM7':      [10, 18],
    'Bbmaj7':    [10, 18],
    'BbΔ7':      [10, 18],

    # Bb major seventh flat five
    'BbM7b5':    [10, 19],
    'BbΔ7b5':    [10, 19],

    # Bb minor-major seventh
    'BbmM7':     [10, 20],
    'Bbm#7':     [10, 20],
    'Bb-M7':     [10, 20],
    'Bb-Δ7':     [10, 20],
    'Bbminmaj7':     [10, 20],
    'Bbmin-maj7':    [10, 20],

    # Bb minor seventh
    'Bbm7':      [10, 21],
    'Bb-7':      [10, 21],
    'Bbmin7':    [10, 21],

    # Bb augmented-major seventh
    'Bb+M7':     [10, 22],
    'Bbaugmaj7':     [10, 22],
    'Bbaug-maj7':    [10, 22],
    'BbM7#5':     [10, 22],
    'BbM7+5':     [10, 22],
    'BbΔ7#5':     [10, 22],
    'BbΔ7+5':     [10, 22],

    # Bb augmented seventh
    'Bb+7':      [10, 23],
    'Bbaug7':    [10, 23],
    'Bb7#5':     [10, 23],
    'Bb7+5':     [10, 23],

    # Bb half-diminished seventh
    'Bbø':       [10, 24],
    'Bbø7':      [10, 24],
    'Bbmin7dim5':    [10, 24],
    'Bbm7b5':    [10, 24],
    'Bbm7o5':    [10, 24],
    'Bb-7b5':    [10, 24],
    'Bb-7o5':    [10, 24],

    # Bb diminished seventh
    'Bbo7':       [10, 25],
    'Bbdim7':     [10, 25],

    # Bb diminished major seventh
    'BbmM7b5':     [10, 26],
    'Bb-Δ7b5':     [10, 26],
    'BboM7':       [10, 26],
# --------------------------------
#   B SEVENTHS
# --------------------------------
    # B dominant seventh
    'B7':       [11, 16],
    'Bdom7':    [11, 16],

    # B dominant flat seventh
    'B7b5':     [11, 17],
    'B7dim5':   [11, 17],

    # B major seventh
    'BM7':      [11, 18],
    'Bmaj7':    [11, 18],
    'BΔ7':      [11, 18],

    # B major seventh flat five
    'BM7b5':    [11, 19],
    'BΔ7b5':    [11, 19],

    # B minor-major seventh
    'BmM7':     [11, 20],
    'Bm#7':     [11, 20],
    'B-M7':     [11, 20],
    'B-Δ7':     [11, 20],
    'Bminmaj7':     [11, 20],
    'Bmin-maj7':    [11, 20],

    # B minor seventh
    'Bm7':      [11, 21],
    'B-7':      [11, 21],
    'Bmin7':    [11, 21],

    # B augmented-major seventh
    'B+M7':     [11, 22],
    'Baugmaj7':     [11, 22],
    'Baug-maj7':    [11, 22],
    'BM7#5':     [11, 22],
    'BM7+5':     [11, 22],
    'BΔ7#5':     [11, 22],
    'BΔ7+5':     [11, 22],

    # B augmented seventh
    'B+7':      [11, 23],
    'Baug7':    [11, 23],
    'B7#5':     [11, 23],
    'B7+5':     [11, 23],

    # B half-diminished seventh
    'Bø':       [11, 24],
    'Bø7':      [11, 24],
    'Bmin7dim5':    [11, 24],
    'Bm7b5':    [11, 24],
    'Bm7o5':    [11, 24],
    'B-7b5':    [11, 24],
    'B-7o5':    [11, 24],

    # B diminished seventh
    'Bo7':       [11, 25],
    'Bdim7':     [11, 25],

    # B diminished major seventh
    'BmM7b5':     [11, 26],
    'B-Δ7b5':     [11, 26],
    'BoM7':       [11, 26],
}