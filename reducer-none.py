#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys
import math

dictionary = {}

numfiles = 17 

for line in sys.stdin:
    line = line.strip()

    word, info = line.split('\t', 1)
    filename, tf = info.split(',', 1)
    print('%s\t%s,%s' % (word, filename, tf))

