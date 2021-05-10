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
    'C+5':      [0, 14],

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
    'C#+5':     [1, 14],

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
    'Db+5':     [1, 14],

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
    'D+5':     [2, 14],

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
    'D#+5':     [3, 14],

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
    'Eb+5':     [3, 14],

    # D# diminished
    'Ebo':      [3, 15],
    'Ebdim':    [3, 15],
    'Ebmb5':    [3, 15],
    'Ebmo5':    [3, 15],
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
                print ('Test %i/%i failed.\ninput: %s\nexpected output: %s\ncurrent output: %s\n' % (count, total_tests, input_, output_, res))
                sys.exit(0)
            count += 1

        print ("%i/%i tests completed successfully!" % (count, total_tests))