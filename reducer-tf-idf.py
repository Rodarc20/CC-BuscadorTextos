#!/usr/bin/env python3
"""reducer.py"""

#from operator import itemgetter
import sys
import math

dictionary = {}

numfiles = 14 

for line in sys.stdin:
    line = line.strip()

    word, info = line.split('\t', 1)
    filename, tf = info.split(',', 1)

    if word in dictionary:
        if filename in dictionary[word]:
            dictionary[word][filename] = dictionary[word][filename] + int(tf)
        else:
            dictionary[word][filename] = int(tf)
    else:
        dictionary[word] = {filename: int(tf)}


# el formato deberia ser word1 file1,tf-idf1:file2,tf-idf2
for word in dictionary:
    idf = math.log10(float(numfiles) / len(dictionary[word]))
    filestuples = []
    for filename in dictionary[word]:
        filestuples.append('%s,%s' % (filename, dictionary[word][filename]*idf))
    files = ':'.join(filestuples)
    print('%s\t%s' % (word, files))
