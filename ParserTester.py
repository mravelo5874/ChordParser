#!/usr/bin/env python3

import sys
from ChordParser import ChordParser
from tests.triad_tests import triad_tests
from tests.seventh_tests import seventh_tests

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
        print ('--------------------------------')


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
        print ('--------------------------------')

        sys.exit(0)