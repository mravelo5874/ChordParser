#!/usr/bin/env python3

import sys
from ChordParser import ChordParser
from tests.triad_tests import triad_tests
from tests.seventh_tests import seventh_tests
from tests.slash_tests import slash_tests
from tests.chord_tests import chord_tests

class ParserTester:
    def __init__(self):
        pass

    def begin_tests(self):
        parser = ChordParser()

        # --------------------------------
        #   TRIAD TESTS
        # --------------------------------
        print ('--------------------------------')
        print ("Starting triad tests...")
        count = 0
        total_tests = len(triad_tests)

        # go through each test and assert output is correct
        for input_, output_ in triad_tests.items():
            res = parser.parse(input_)
            if (res != output_):
                print ('Test %i/%i failed.\ninput: %s\nexpected output: %s\ncurrent output: %s' % (count, total_tests, input_, output_, res))
                print ('--------------------------------')
                sys.exit(0)
            count += 1
        print ("%i/%i tests completed successfully!" % (count, total_tests))


        # --------------------------------
        #   SEVENTH TESTS
        # --------------------------------
        print ('--------------------------------')
        print ("Starting seventh tests...")
        count = 0
        total_tests = len(seventh_tests)

        # go through each test and assert output is correct
        for input_, output_ in seventh_tests.items():
            res = parser.parse(input_)
            if (res != output_):
                print ('Test %i/%i failed.\ninput: %s\nexpected output: %s\ncurrent output: %s' % (count, total_tests, input_, output_, res))
                print ('--------------------------------')
                sys.exit(0)
            count += 1
        print ("%i/%i tests completed successfully!" % (count, total_tests))


        # --------------------------------
        #   SLASH TESTS
        # --------------------------------
        print ('--------------------------------')
        print ("Starting slash tests...")
        count = 0
        total_tests = len(slash_tests)

        # go through each test and assert output is correct
        for input_, output_ in slash_tests.items():
            res = parser.parse(input_)
            if (res != output_):
                print ('Test %i/%i failed.\ninput: %s\nexpected output: %s\ncurrent output: %s' % (count, total_tests, input_, output_, res))
                print ('--------------------------------')
                sys.exit(0)
            count += 1
        print ("%i/%i tests completed successfully!" % (count, total_tests))


        # --------------------------------
        #   CHORD TESTS
        # --------------------------------
        print ('--------------------------------')
        print ("Starting chord tests...")
        count = 0
        total_tests = len(chord_tests)

        # go through each test and assert output is correct
        for input_, output_ in chord_tests.items():
            res = parser.parse(input_)
            res = parser.stack_to_notes(res)
            if (res != output_):
                print ('Test %i/%i failed.\ninput: %s\nexpected output: %s\ncurrent output: %s' % (count, total_tests, input_, output_, res))
                print ('--------------------------------')
                sys.exit(0)
            count += 1
        print ("%i/%i tests completed successfully!" % (count, total_tests))

        
        print ('--------------------------------')
        sys.exit(0)