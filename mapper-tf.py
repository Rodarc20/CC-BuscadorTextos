#!/usr/bin/env python3
"""mapper.py"""

import sys
import os
import re
#from stop_words import get_stop_words

#stop_words = get_stop_words('en')
regex = re.compile('[^a-zA-Z0-9]')
file_name = os.getenv('mapreduce_map_input_file')
file_name = file_name.split('/')[-1]

palabras = {}

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        word = regex.sub('', word)
        if word != '':
            if word in palabras:
                palabras[word] = palabras[word]+ 1
            else:
                palabras[word] = 1 

for word in palabras:
    print('%s\t%s,%s' % (word, file_name, palabras[word]))
