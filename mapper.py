#!/usr/bin/env python3
"""mapper.py"""

import sys
import os
import re
from stop_words import get_stop_words

stop_words = get_stop_words('en')
regex = re.compile('[^a-zA-Z0-9]')
#file_name = os.getenv('map_input_file')
file_name = os.getenv('mapreduce_map_input_file')

# necesito un diccionario de palabras
palabras = {}

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        word = regex.sub('', word)
        #verificar que no este en el stopwords
        if not word in stop_words:

            if word in palabras:
                palabras[word][filename] = palabras[word][filename] + 1
            else:
                #no esta creada la entrada, crear y darle un set con el nombre de archivo 
                palabras[word] = {filename: 1} #esto es un diccionario
            # las palabras son agregas al diccionario, con el nombre del archivo para la primera vez, y un contador en 1, en las repeticiones de la palabra este contador ira aumentando
            #esto quiza sea una tupla, para que luego sea usado facilmente en el reducer, ver como o quiza un set
for word in 
#no neesito el dicionario, solo el contador de palabras, de este archivo, al final en el print yo puedo generar las tuplas de salida manualmente, ya que el archivo siempre es el mismo, y el paso intermedio al reduce solo lo ordenara, al inicio dl reduce debo simplemente hacer la agregacion. ahi si usare el diccionario que he planteado aqui
print('%s\t%s' % (word, file_name))
