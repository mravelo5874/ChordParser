#!/usr/bin/env python3

from ChordParser import ChordParser

def main():

    parser = ChordParser()

    # accept user input until user quits program
    print ("\nThis program parses chord names and denotes how to costruct it. Type \'exit\' to end the program.\n")
    while (True):
        user_input = input("Enter a chord: ")
        user_input = user_input.lower() # convert to lowercase to make parsing easier

        if (user_input == "exit"):
            break

        # send user input to the parser class
        result = parser.parse(user_input)

    # end program
    print ("ending program...")

if __name__ == "__main__":
    main()