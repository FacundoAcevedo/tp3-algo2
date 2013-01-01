#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    Todo lo que trate de operaciones con archivos
"""

##Importaciones

import os, system, csv



##Funciones

def _csv_reader(contenido):
    """Recibe:cadena, Devuelve: manejador csv
    Interpreta lo que recive, y devuelve un manejador"""

    lector=reader(contenido, delimiter=";")
    return lector

def _extraer_datos(ruta):
    """Recibe: cadena, Devuelve: cadena,entero
    Extrae los datos del archivo, cierra el archivo y los devuelve"""
    #variables
    handler=file #manejador de archivos
    contenido=[]
    linea=""

    #codigo
    try:
        handler=open(ruta,"r")
        for linea in handler.readlines():
            if linea!="\n": # por si hay lineas en blanco en un archivo
                            #hace que funcione aunque este mal el
                            #formato
                contenido.append(linea)
        handler.close()
        return contenido
    except:
        print "[E] Ocurrio algun error, el fichero puede no existir\
o no se tienen los permisos de lectura"
        if len(argv)>1: #varia segun la menera en la qeu fue ejecutado
            exit(1)
        else:
            return False, None

def desmenuzar(contenido):
    """Recive una lista de lineas que representan el archivo a
    interpretar como csv, se lo interpreta y devuelve dos listas
    una de nodos y otra de calles (objetos c/u"""
    yeah!







##########################<EOF
