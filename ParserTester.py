#!/usr/bin/env python3

import sys
from ChordParser import ChordParser
from tests import tests

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