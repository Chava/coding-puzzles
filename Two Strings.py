#!/bin/python3

# Import required standard libraries
import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    """
    Determines if two strings share any common substring (even a single character).
    
    Args:
        s1 (str): First input string
        s2 (str): Second input string
    
    Returns:
        str: 'YES' if the strings share any common substring, 'NO' otherwise
    
    Example:
        >>> twoStrings('hello', 'world')
        'YES'  # because both strings share 'l' and 'o'
        >>> twoStrings('hi', 'bye')
        'NO'   # no characters in common
    """
    # Convert both strings to sets of characters and find their intersection
    # Using set intersection is more efficient than checking every substring
    return 'YES' if set(s1) & set(s2) else 'NO'


if __name__ == '__main__':
    # Open file for writing output (HackerRank specific)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    q = int(input())

    # Process each test case
    for q_itr in range(q):
        # Read the first string
        s1 = input()

        # Read the second string
        s2 = input()

        # Check if strings share any common substring
        result = twoStrings(s1, s2)

        # Write result to output file
        fptr.write(result + '\n')

    # Close the output file
    fptr.close()
