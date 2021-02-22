#!/bin/python3

import math
import os
import random
import re
import sys

def make_dict(word):
    res = {}
    for ch in word:
        if res.get(ch):
            res[ch] += 1
        else:
            res[ch] = 1
    return res

def makeAnagram(a, b):
    dict_a = make_dict(a)
    dict_b = make_dict(b)
    for aa in dict_a:
        if dict_b.get(aa):
            dict_a[aa] = dict_a[aa] - dict_b[aa]
            del dict_b[aa]
    res = 0
    for k, v in dict_a.items():
        res +=abs(v)
    for k, v in dict_b.items():
        res +=v
    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()