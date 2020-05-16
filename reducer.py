#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

dictionary = {}

#aqui debo calcular el idf, teniendo en cuenta el numero de archivos
#deb ver ver cuando documentos tiene cada palabra del diccionario que reciba y dividir por el numero total
#luego agregar este valor al diccionario como una tercera clave
#ver como seria la segunda en estructura
#con esto ya tengo lo ncesario

# la salida luego sera recuperdada, quiza por python en el maestro y cargado a memoria, de acuerdo a la busqueda de termino, ire directo a la palabra y sumare los idf y los multiplicare por el idf
#aun que esto quiza lo pueda hacer en el reduce, cada documento de cada palabra tendra su tf y ademas tendra el tf-idf
#cunado en python quiera buscar una palabra, ire directo a este valor, es mas quiza el reduce no necesite los otros valores, solo este, es decir el tf se reemplazara por el tf-idf
#devolverlos ordenados de preferencia, no se si eso se pueda en un diccionario o en un set

for line in sys.stdin:
    line = line.strip()

    word, filename = line.split('\t', 1)
    if word in dictionary:
        #signfica que ya esta creada la entrada y el set al menos con un elemento
        dictionary[word].add(filename)
    else:
        #no esta creada la entrada, crear y darle un set con el nombre de archivo 
        dictionary[word] = {filename} #esto es un set

#imprimir el diccionario, y la lista de filenames, la pregunta es como deberia imprimirlo si quisiera leerlo en el siguiente mapper?
for word in dictionary:
    print('%s\t%s' % (word, dictionary[word]))
