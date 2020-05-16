import os
from operator import itemgetter

command = input('Instruccion: ') # captura la linea
commands = command.split() # ver como dividir

dictionary = {}

def print_res(resultado):
    for res in resultado:
        print('%s\t%s' % res)

while (command != 'exit') :
    print(commands)
    if (commands[0] == 'search'):
        # buscar el termino de busqueda en el diccionario crearo
        if commands[1] in dictionary:
            #print(sorted(dictionary[commands[1]], key=itemgetter(1), reverse=True)[:5])
            print_res(sorted(dictionary[commands[1]], key=itemgetter(1), reverse=True)[:5])
    elif (commands[0] == 'load'):
        #read file
        with open('part-00000') as file:
            for line in file:
                line.strip()
                word, info = line.split()
                docs = info.split(':')
                wordinfo = []
                for doc in docs:
                    filename, tf_idf = doc.split(',')
                    wordinfo.append((filename, float(tf_idf)))
                dictionary[word] = wordinfo
        #consutrccion del diccionario del diccionario o por tupla o array para hacer sort?
        #print(dictionary)
    command = input('Instruccion: ') # captura la linea
    commands = command.split() # ver como dividir

print('Adios')

