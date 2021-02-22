#!/bin/python3

import math
import os
import random
import re
import sys

def rotLeft(a, d):
    d1 = d % len(a)
    return [*a[d1:], *a[0:d1]]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
