#!/bin/python3

# Import required standard libraries
import math
import os
import random
import re
import sys

def rotLeft(a, d):
    """
    Performs a left rotation on an array by d positions.
    
    Args:
        a (list): Array to rotate
        d (int): Number of positions to rotate left
        
    Returns:
        list: Array after d left rotations
        
    Example:
        >>> rotLeft([1, 2, 3, 4, 5], 2)
        [3, 4, 5, 1, 2]
    """
    # Calculate effective rotation (handles cases where d > len(a))
    d1 = d % len(a)
    
    # Create new array by combining:
    # 1. Elements from d1 to end: a[d1:]
    # 2. Elements from start to d1: a[0:d1]
    # The * operator unpacks the slices into the new list
    return [*a[d1:], *a[0:d1]]


if __name__ == '__main__':
    # Open file for writing output (HackerRank specific)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read space-separated values for array size (n) and rotation count (d)
    nd = input().split()

    # Parse array size
    n = int(nd[0])

    # Parse number of left rotations
    d = int(nd[1])

    # Read space-separated integers and convert to list
    a = list(map(int, input().rstrip().split()))

    # Perform the left rotation
    result = rotLeft(a, d)

    # Convert result to space-separated string and write to output
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    # Close the output file
    fptr.close()
