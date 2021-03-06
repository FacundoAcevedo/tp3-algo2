#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
    Todo lo que trate de operaciones con archivos
"""

##Importaciones
import os, csv, sys
from grafo import Grafo
from texto import texto
from constantes import *



##Funciones
def obtener_datos(ruta):
    """wrapper a la subfuncion de validacion"""
    return validar_archivo(ruta)

def validar_archivo(ruta):
    """Corrobora que el archivo exista, no este vacio, y se pueda abrir"""

    #Valido la existencia
    if not os.path.isfile(ruta):
        print msj_err_no_arc 
        return None, None, None
    #valido que no este vacio
    if not os.path.getsize(ruta):
        print msj_err_vac_arc 
        return None, None, None        

    #Intento abirirlo
    try:
        handler = open(ruta,"r")

        #Devuelvo los datos extraidos
        retorno =  _extraer_datos(handler)
        handler.close()
        return retorno
        
    except:
        print "Ocurrio un error al intentar abrir el archivo",sys.exc_info()[0]
        return None, None, None





def _extraer_datos(handler):
    """Recibe: archivo, Devuelve: 2 grafos
    Extrae los datos del archivo y los devuelve"""
    #variables
    fila = []
    nodos_cant = 0
    calles_cant = 0
    i = 0 #indice generico
    info_nodo = {} #donde guardo la informacion de los nodos

    grafo_nodos = Grafo()
    grafo_calles = Grafo()

    #Cargo el manejador de csv
    contenido_csv = csv.reader(handler, delimiter=",")
    #obtengo la primer linea, que me dice cuantos -NODOS- son
    fila = contenido_csv.next()
    nodos_cant = int(fila[0])
    #avanzo para obtener la primer fila de -NODOS-
    fila = contenido_csv.next()

    #obtengo los datos de los -NODOS-
    for i in range(nodos_cant-1):
        #guardo la info del nodo
        info_nodo[ int(fila[0]) ] = {'x': float(fila[1]), 'y': float(fila[2]), 'lon': float(fila[4]),'lat': float(fila[3])}
        #avanzo una posicion si no estoy en el ultimo -NODO-
        if i != nodos_cant:
            fila = contenido_csv.next()
    #obtengo la cantidad de -CALLES-
    fila = contenido_csv.next()
    calles_cant = int(fila[0])

    #avanzo para obtener la primer fila de -CALLES-
    fila = contenido_csv.next()
    #obtengo los datos de las -CALLES-
    for i in range(calles_cant-1):
        if int(int(fila[4])) not in grafo_nodos:
            grafo_nodos.agregar_vertice(int(fila[4]))
        if texto(fila[1]) not in grafo_calles:
            grafo_calles.agregar_vertice(texto(fila[1]))
        #Agrego las aristas
        grafo_nodos.agregar_arista(int(fila[4]),int(fila[5]),int(fila[2]))
        grafo_calles.agregar_arista(texto(fila[1]),int(fila[4]),int(fila[5]))
        #Cuando son mano unica
        if int(fila[3]) == 0:
            if int(fila[5]) not in grafo_nodos:
                grafo_nodos.agregar_vertice(int(fila[5]))
            grafo_nodos.agregar_arista(int(fila[5]),int(fila[4]),int(fila[2]))
        #devuelvo los grafos e info_nodo
        if i != calles_cant:
            fila = contenido_csv.next()
        
    return grafo_nodos, grafo_calles ,info_nodo


















##########################<EOF
