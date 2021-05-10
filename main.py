#!/usr/bin/env python3

import sys
from ChordParser import ChordParser
from ParserTester import ParserTester

def main():

    # unit testing
    if ('-test' in sys.argv):
        tester = ParserTester()
        tester.begin_tests()
        print ("ending program...")
        sys.exit(0)

    # accept user input until user quits program
    print ("\nThis program parses chord names and denotes how to costruct it. Type \'exit\' to end the program.\n")
    while (True):
        user_input = input("Enter a chord: ")
        user_input = user_input.replace(' ', '') # remove all spaces
        print('') # print extra line

        if (user_input == "exit"):
            break

        # send user input to the parser class
        parser = ChordParser()
        result = parser.parse(user_input)

        # print out result
        parser.translate_stack(result)

    # end program
    print ("ending program...")
    sys.exit(0)

if __name__ == "__main__":
    main()