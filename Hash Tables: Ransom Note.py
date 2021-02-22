#!/bin/python3

import math
import os
import random
import re
import sys


def checkMagazine(magazine, note):
    if len(note) == len(magazine) and list(sorted(note)) == list(sorted(magazine)):
        return "Yes"
    for n in note:
        if n not in magazine:
            return "No"
        else:
            magazine.remove(n)
    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
