#! /usr/bin/env python
"""
This snippet create double of an integer or float
"""

__author__ = "O.A"
__author_email__ = "oa@live.com"

import sys

def doubler(number):
    """
    Given a number, double it and return the value
    """
    result = number * 2 
    return result
# Entry point of the program
if __name__ == '__main__':
    #Retrieve command line input
    try:
        input = float(sys.argv[1])
    except (IndexError, ValueError) as e:
        # Indicates no command line parameter was provided
        print("You must provide a number as a parameter to this script")
        print("Example: ")
        print(" python doubler.py 12")
        sys.exit(1)

    #Double the provided number and print output
    answer = doubler(input)
    print(answer)

