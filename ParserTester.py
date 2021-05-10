#!/usr/bin/env python3

import sys
from ChordParser import ChordParser

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
}

class ParserTester:
    def __init__(self):
        pass

    def begin_tests(self):
        parser = ChordParser()
        count = 0
        total_tests = len(tests)

        # go through each test and assert output is correct
        for input_, output_ in tests.items():
            res = parser.parse(input_)
            if (res != output_):
                print ('--------------------------------')
                print ('Test %i/%i failed.\ninput: %s\nexpected output: %s\ncurrent output: %s' % (count, total_tests, input_, output_, res))
                print ('--------------------------------')
                sys.exit(0)
            count += 1

        print ('--------------------------------')
        print ("%i/%i tests completed successfully!" % (count, total_tests))
        print ('--------------------------------')
        sys.exit(0)