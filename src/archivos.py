#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    Maneja todo lo relacionado al manejo de archivos.
"""

##Importaciones

import csv
import os



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
					
				
						
						
						
			






##Funciones






##########################<EOF
