#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
    pruebas
"""

##Importaciones
from grafo import Grafo, dijktra
from texto import *
from archivos import *


##Funciones

def probar(booleano,texto):
	if booleano:
		print "La preuba "+texto+": OK"
	if not booleano:
		print "La preuba "+texto+": ERROR"
	else:
		" -- ERROR TESTEANDO "+texto
		
def separador():
	print "\n    ## \n"
		
		
		
		
def prueba_grafo():
	#creo el grafo
	grafo = Grafo()
	
	# 1 -> 2 -> 3 -> 5
	#      ^    ^	este sera mi grafo de preubas
	#      4 <--|
	
	#agrego los nodos
	grafo.agregar_vertice(1)
	grafo.agregar_vertice(2)
	grafo.agregar_vertice(3)
	grafo.agregar_vertice(4)
	grafo.agregar_vertice(5)
	
	#agrego las aristas
	grafo.agregar_arista(1,2,0)
	grafo.agregar_arista(2,3,1)
	grafo.agregar_arista(3,5,0)
	grafo.agregar_arista(4,2,2)
	grafo.agregar_arista(4,3,3,True)
	
	dijktra(grafo,1)
	
	
	## La comparacion depende del orden osea que [1,2] es distinto a [2,1] OJO!
	probar(grafo.obtener_vertice(1).conseguir_lista_conexiones() == [2],\
	"Prueba_de_enlaces_1")
	probar(sorted(grafo.obtener_vertice(4).conseguir_lista_conexiones()) == [2,3],\
	"Prueba_de_enlaces_2")
	probar(sorted(grafo.obtener_vertice(3).conseguir_lista_conexiones()) == [4,5],\
	"Prueba_de_enlaces_3")
	probar(grafo.obtener_vertice(5).conseguir_lista_conexiones() == [],\
	"Prueba_de_enlaces_4")
	
	#~ print grafo
	separador()
	
	
	
def prueba_texto():
	probar( "a_b_c" == texto("A b C"), "texto_0")
	probar( "a_b c" != texto("A_B c"), "texto_1")
	probar( ("uno","dos") == partir_calle("uno,dos"), "partir_calle_0")
	probar( -1 == partir_calle("unodos"), "partir_calle_1")
	separador()

def prueba_cargar_archivo():
	ruta="../mapas/partido_gerli.csv"
	#devuelve dos grafos y la informacion de los nodos
	grafo_nodos, grafo_calles, info_nodo = obtener_datos(ruta)
	
	if grafo_nodos:
		probar(True, "Existe grafo_nodos")
	else:
		probar(False, "Existe grafo_nodos")
	if grafo_calles:
		probar(True, "Existe grafo_calles")
	else:
		probar(False, "Existe grafo_calles")
	if info_nodo:
		probar(True, "Existe info_nodo")
	else:
		probar(False, "Existe info_nodo")

	separador()

##Corro las pruebas
print ("::PRUEBAS::")
#~ prueba_texto()
#~ prueba_cargar_archivo()
prueba_grafo()

##########################<EOF
