#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
<<<<<<< HEAD
    Maneja todo lo relacionado al manejo de archivos.
=======
    Todo lo que trate de operaciones con archivos
>>>>>>> 50bed007fe9a537f8373c2fb25477cbfbe53d0ed
"""

##Importaciones

<<<<<<< HEAD
<<<<<<< HEAD
import csv
import os
=======
    import os, system, csv
>>>>>>> 50bed007fe9a537f8373c2fb25477cbfbe53d0ed



##Objetos
class Lista_calles(object):
    """Objeto encargado de leer los archivos csv y mantener una lista de
    los nodos y las calles"""

    def __init__(self):
		self.nodos = []
		self.calles = []
		self.cant_nodos = int
		self.cant_intersecciones = int
        pass

    def leer_archivo(self, nombre_fichero):
        """Levanta los datos del fichero, la estructura de directorios no debe
        variar"""
        #Variables
        salir = False
        lock = False
        
        #Obtengo la ruta
        ruta = os.path.join("..",nombre_fichero)
        
        #Intento abrir el archivo
        try:
			handler = open(ruta)
			cant_lineas = len(hander.readlines())
			close(handler)
			#Cargo el lector csv
			csv_fichero = csv.reader(open(ruta), delimiter=',')
		
		except IOError:
			raise IOError("Error al intentar abrir el fichero .csv")	
		
		#intento cargar todos los nodos y calles
		try:
			#while de los nodos
			while salir != True:
				for fila in csv_fichero:
					#Cargo la cantidad de nodos
					if (type(fila) is int):
						if lock == True:
							salir = True
							break
							
						lock = True
						self.cant_nodos = fila
					
				
						
						
						
			




=======
import os, system, csv



##Funciones
>>>>>>> 62c2f558afcef03c0aaabb6c711fd2f22dfb1b7d

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
