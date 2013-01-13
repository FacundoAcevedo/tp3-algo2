#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
    pruebas
"""

##Importaciones
from grafo import Grafo, dijkstra, imprimir_distancia, imprimir_ruta
from texto import *
from archivos import *




##Funciones

def probar(booleano,texto):
	if booleano:
		print "La prueba "+texto+": OK"
	if not booleano:
		print "La prueba "+texto+": ERROR"
	else:
		" -- ERROR TESTEANDO "+texto
		
def separador():
	print "\n    ## \n"
		
		
		
		
def prueba_grafo():
	#creo el grafo
	grafo = Grafo()
        
        #~ +-----> 2 <----> 3 +-
        #~ +       ^        ^  |     
        #~ 1       |        |  |->5--->6
        #~ ^       |        |     +
        #~ |       |        |     |
        #~ |       +-->4 <--+     |
        #~ |                      |
        #~ +----------------------+
	 
	#agrego los nodos
	grafo.agregar_vertice(1)
	grafo.agregar_vertice(2)
	grafo.agregar_vertice(3)
	grafo.agregar_vertice(4)
	grafo.agregar_vertice(5)
        grafo.agregar_vertice(6)
	
	#agrego las aristas
	grafo.agregar_arista(1,2,1)
	grafo.agregar_arista(2,3,1,True)
	grafo.agregar_arista(3,5,1)
	grafo.agregar_arista(4,2,1,True)
	grafo.agregar_arista(4,3,1,True)
        grafo.agregar_arista(5,1,1)
        grafo.agregar_arista(5,6,1)
        
	vert_inicio = grafo.obtener_vertice(1)
        vert_fin = grafo.obtener_vertice(6)
	ruta = dijkstra(grafo, vert_inicio)
        print imprimir_ruta(ruta, vert_inicio, vert_fin)
        
        
	#~ imprimir_distancia(distancia)
	
	## La comparacion depende del orden osea que [1,2] es distinto a [2,1] OJO!
	probar(grafo.obtener_vertice(1).obtener_lista_adyacentes() == [2],\
	"Prueba_de_enlaces_1")
	probar(sorted(grafo.obtener_vertice(4).obtener_lista_adyacentes()) == [2,3],\
	"Prueba_de_enlaces_2")
	probar(sorted(grafo.obtener_vertice(3).obtener_lista_adyacentes()) == [2,4,5],\
	"Prueba_de_enlaces_3")
	probar(sorted(grafo.obtener_vertice(5).obtener_lista_adyacentes()) == [1,6],\
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
