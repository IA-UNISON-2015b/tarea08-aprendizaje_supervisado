#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tarea8.py
------------

Archivo general para realizar las pruebas del uso del arboles de desicion. Identico al usado en Naive Bayes.

Se prueba en un conjunto de prueba de dimensión fija sobre cadenas de ADN. Para mayor
información sobre la base de datos, se puede consultar en

http://archive.ics.uci.edu/ml/datasets/Molecular+Biology+(Splice-junction+Gene+Sequences)

La base ya se trato, y se convirtieron los valores de genes a numeros enteros con el fin de
poder utilizar la base para varios métodos de clasificación (como redes neuronales).

La base de datos ya se repartió en una base de entrenamiento (dna.data) y otra base de prueba
(dna.test). Con el fin de probar la robustez de los algoritmos de aprendizaje ante ruido, se agregó
a la base otros atributos extra con valores asignados al azar (como si tuvieramos atributos extra con información no
significativa). Estos datos se encuentran en dna_noise.data y dna_noise.test respectivamente.


"""

__author__ = 'Luis Fernando Suarez Astiazaran'


import id3
#import cart
#import knn

def carga_archivo(archivo):
    """
    Cargar el archivo de datos a clasificar, devuelve

    - datos = [dato1, dato2, ..., datoE], la lista de E datos a clasificar
      donde dato1 = [dato1(1), ..., dato1(n)] son los n valores de los atributos
      de dato1.

    - clases = [clase1, clase2, ..., claseE] la clase a la que pertenece cada dato

    - atributos = [a1, a2, .., an] donde ai es una lista

      ai = [v1, ..., vm]

      con los m valores que puede tomar ai

    """

    datos, clases, atributos = [], [], []

    enlistado = open(archivo, 'rU').readlines()
    for linea in enlistado:
        renglon = [int(d.strip().strip('\n')) for d in linea.split(',')]
        datos.append(renglon[0: -1])
        clases.append(renglon[-1])
    atributos = [[1, 2, 3, 4] for _ in range(len(datos[0]))]
    return datos, clases, atributos


def error_clasif(c1, c2):
    """
    Encuentra el porcentaje de valores diferentes entre la lista c1 y la c2

    """
    acc = len([1 for i in range(len(c1)) if c1[i] != c2[i]])
    return 1.0 * acc / len(c1)


def pruebaID3():

    print "\nPrueba con la base de datos de DNA sin ruido"
    print "----------------------------------------------"

    datos, clases, atributos = carga_archivo("dna.data")
    clasificador = id3.ArbolDecision(atributos)

    clasificador.entrena(datos, clases)
    clases_estimadas = clasificador.reconoce(datos)
    error = error_clasif(clases, clases_estimadas)
    print "Error de estimación en los mismos datos: "+str(error*100)+" %"

    d_test, c_test, _ = carga_archivo("dna.test")
    c_e_test = clasificador.reconoce(d_test)
    e_test = error_clasif(c_test, c_e_test)
    print "Error de estimación en los datos de prueba: "+str(e_test*100)+" %\n"

    print "Y se generaron ", clasificador.numero_nodos, " nodos y ", clasificador.numero_hojas, " hojas."

    print "\nPrueba con la base de datos de DNA con ruido"
    print "----------------------------------------------"

    datos, clases, atributos = carga_archivo("dna_noise.data")
    clasificador_ruido = id3.ArbolDecision(atributos)

    clasificador_ruido.entrena(datos, clases)
    clases_estimadas = clasificador_ruido.reconoce(datos)
    error = error_clasif(clases, clases_estimadas)
    print "Error de estimación en los mismos datos: "+str(error*100)+" %"

    d_test, c_test, _ = carga_archivo("dna_noise.test")
    c_e_test = clasificador_ruido.reconoce(d_test)
    e_test = error_clasif(c_test, c_e_test)
    print "Error de estimación en los datos de prueba: "+str(e_test*100)+" %\n"

    print "Y se generaron ", clasificador_ruido.numero_nodos, " nodos y ", clasificador_ruido.numero_hojas, " hojas."


def pruebaCART():
    """
    ***************************************************************************************************************
    60 puntos
    ***************************************************************************************************************

    Desarrolla en un módulo llamado cart.py una clase para realizar clasificación utilizando un árbol tipo CART para
    atributos cualitativos, que utilice al menos 3 criterios de prepoda (los mismos vistos para el árbol ID3

"""

    print "\nPrueba con la base de datos de DNA sin ruido"
    print "----------------------------------------------"

    datos, clases, atributos = carga_archivo("dna.data")
    clasificador = cart.ArbolDecision(atributos)

    clasificador.entrena(datos, clases)
    clases_estimadas = clasificador.reconoce(datos)
    error = error_clasif(clases, clases_estimadas)
    print "Error de estimación en los mismos datos: "+str(error*100)+" %"

    d_test, c_test, _ = carga_archivo("dna.test")
    c_e_test = clasificador.reconoce(d_test)
    e_test = error_clasif(c_test, c_e_test)
    print "Error de estimación en los datos de prueba: "+str(e_test*100)+" %\n"

    print "Y se generaron ", clasificador.numero_nodos, " nodos y ", clasificador.numero_hojas, " hojas."

    print "\nPrueba con la base de datos de DNA con ruido"
    print "----------------------------------------------"

    datos, clases, atributos = carga_archivo("dna_noise.data")
    clasificador_ruido = cart.ArbolDecision(atributos)

    clasificador_ruido.entrena(datos, clases)
    clases_estimadas = clasificador_ruido.reconoce(datos)
    error = error_clasif(clases, clases_estimadas)
    print "Error de estimación en los mismos datos: "+str(error*100)+"%"

    d_test, c_test, _ = carga_archivo("dna_noise.test")
    c_e_test = clasificador_ruido.reconoce(d_test)
    e_test = error_clasif(c_test, c_e_test)
    print "Error de estimación en los datos de prueba: "+str(e_test*100)+"%\n"

    print "Y se generaron ", clasificador_ruido.numero_nodos, " nodos y ", clasificador_ruido.numero_hojas, " hojas."
    
    """

    Contesta las siguientes:
        + ¿Cual es la diferencia entre el árbol tipo CART y el ID3?
    el cart se caracteriza por realizar particiones tipo binarias y el id3 hace busqueda rapida desde la raiz hasta las hojas
        
        + ¿Cual es más eficiente?
        el cart es mas eficiente

        + ¿Cuanto nodos genera cada uno?
        429 y 425
        
        + ¿Cuantos nodos hoja genera cada uno?
        322 y 319
        
        + ¿Cual tiene el menor error en los datos de prueba?
        igual ya que se equilibran
        
        + ¿A que crees que se debe que hay errores de aprendizaje con los datos de entrenamiento?
        A que es la primera informacion que recibe el sistema y es limitada comparada con toda la informacion que requiere
        para ser un clasificador universal


    """
    pass

def pruebaKNN():
    """
    ***************************************************************************************************************
    40 puntos
    ***************************************************************************************************************

    Desarrolla en un modulo llamado knn.py una clase para realizar clasificación con k vecinos próximos. Recuerda que 
    los datos de entrenamiento se utilizan para encontrar los vecinos (osea que los datos de entrenamiento sin ruido
    con los datos de prueba sin ruido, y los datos de entrenamiento con ruido con los datos de prueba con ruido).
    

    Ahora aplica el método de los K vecinos más próximos, y resuelve la siguiente tabla

      Vecinos                error datos prueba                                 error datos prueba ruido
      ------------------------------------------------------------------------------------------------------
        1
        3
        5
        7
        9

    y contesta las siguientes preguntas:
    
        + ¿Que método da menos error entre knn, CART, Id3 y naive bayes en los datos sin ruido?
        + ¿Que método da menos error entre knn, CART, Id3 y naive bayes en los datos con ruido?
        + ¿Mejora al aumentar el número de vecinos? ¿Hasta cuantos vecinos?

    """
    pass


if __name__ == "__main__":
    pruebaID3()


