#!/bin/python3

# Import required standard libraries
import math
import os
import random
import re
import sys

def make_dict(word):
    """
    Creates a frequency dictionary of characters in the given word.
    
    Args:
        word (str): Input string to count character frequencies
        
    Returns:
        dict: Dictionary with characters as keys and their frequencies as values
        
    Example:
        >>> make_dict("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    res = {}
    for ch in word:
        if res.get(ch):
            # Increment count if character already exists
            res[ch] += 1
        else:
            # Initialize count for new character
            res[ch] = 1
    return res

def makeAnagram(a, b):
    """
    Calculates the minimum number of character deletions needed to make two strings anagrams.
    
    Args:
        a (str): First input string
        b (str): Second input string
        
    Returns:
        int: Minimum number of character deletions needed
        
    Example:
        >>> makeAnagram("cde", "abc")
        4  # Delete 'd','e' from first string and 'a','b' from second string
    """
    # Create frequency dictionaries for both strings
    dict_a = make_dict(a)
    dict_b = make_dict(b)
    
    # Process common characters between both strings
    for aa in dict_a:
        if dict_b.get(aa):
            # Calculate the difference in frequencies
            dict_a[aa] = dict_a[aa] - dict_b[aa]
            # Remove processed character from dict_b
            del dict_b[aa]
    
    # Calculate total deletions needed
    res = 0
    # Add absolute differences for characters in first string
    for k, v in dict_a.items():
        res += abs(v)
    # Add frequencies for remaining characters in second string
    for k, v in dict_b.items():
        res += v
    
    return res


if __name__ == '__main__':
    # Open file for writing output (HackerRank specific)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read first string
    a = input()

    # Read second string
    b = input()

    # Calculate minimum deletions needed
    res = makeAnagram(a, b)

    # Write result to output file
    fptr.write(str(res) + '\n')

    # Close the output file
    fptr.close()