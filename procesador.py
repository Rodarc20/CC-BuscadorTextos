import os

command = input('Instruccion: ') # captura la linea
commands = command.split() # ver como dividir

carpeta = 'dataset'

while (command != 'exit') :
    print(commands)
    if (commands[0] == 'generar'):
        # limipia y generar la base de datos
        os.system('hdfs dfs -rm -r indice') #eliminando
        os.system('yarn jar /home/rodrigo/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -file /home/rodrigo/buscador/mapper-tf.py -mapper /home/rodrigo/buscador/mapper-tf.py -file /home/rodrigo/buscador/reducer-tf-idf.py -reducer /home/rodrigo/buscador/reducer-tf-idf.py -input %s/* -output indice' % (carpeta))

    elif (commands[0] == 'generardebugmap'):
        # limipia y generar la base de datos
        os.system('hdfs dfs -rm -r indice') #eliminando
        os.system('yarn jar /home/rodrigo/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -file /home/rodrigo/buscador/mapper-tf.py -mapper /home/rodrigo/buscador/mapper-tf.py -file /home/rodrigo/buscador/reducer-none.py -reducer /home/rodrigo/buscador/reducer-none.py -input %s/* -output indice' % (carpeta))

    elif (commands[0] == 'recuperar'):
        # recuperar la base de datos
        os.system('rm /home/rodrigo/buscador/part-00000')
        os.system('hdfs dfs -get indice/part-00000')

    elif (commands[0] == 'subirtodo'):
        os.system('hdfs dfs -rm -r %s' % (carpeta)) #eliminando
        os.system('hdfs dfs -mkdir %s' % (carpeta)) #creacndo carpeta
        os.system('hdfs dfs -put /home/rodrigo/libros/* %s' % (carpeta)) # subiendo los libros

    elif (commands[0] == 'subirarchivo'):
        os.system('hdfs dfs -put /home/rodrigo/libros/%s.txt %s' % (commands[1], carpeta)) # subiendo los libros
    elif (commands[0] == 'listado'):
        os.system('hdfs dfs -ls %s' % (carpeta))
        #os.system('ls -l')

    command = input('Instruccion: ') # captura la linea
    commands = command.split() # ver como dividir


print('Adios')

