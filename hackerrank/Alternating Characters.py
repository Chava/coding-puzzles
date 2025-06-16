#!/bin/python3

# Import required standard libraries
import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    """
    Determines the minimum number of deletions needed to create a string
    where no two adjacent characters are the same.
    
    Args:
        s (str): Input string containing only 'A' and 'B' characters
    
    Returns:
        int: The minimum number of characters that must be deleted
    """
    # List to store characters that should be kept
    modified = []
    
    # Iterate through each character in the input string
    for ch in s:
        if not modified:
            # If modified list is empty, add the first character
            modified.append(ch)
        else:
            # Get the last character we kept
            c = modified[-1]
            # Only keep current character if it's different from the previous one
            if ch != c:
                modified.append(ch)
    
    # Return the number of characters that need to be deleted
    # (difference between original and modified string lengths)
    return len(s) - len(modified)


if __name__ == '__main__':
    # Open file for writing output (HackerRank specific)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    q = int(input())

    # Process each test case
    for q_itr in range(q):
        # Read the input string
        s = input()

        # Calculate the result for current test case
        result = alternatingCharacters(s)

        # Write result to output file
        fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()