#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from grafo import *
from archivos import *
from texto import *
from interaccion import *
from sexykml import *
from constantes import *


def main():
    mapa_ok = False

    
    #~ Inicializo el kml
    kml = SexyKML("Pizeria Gerli, hoy Gerli, mañana... el mundo!")


    #Consigo los grafos
    while not mapa_ok:
        ruta_mapa = obtener_texto(msj_mapa)
        grafo_nodos, grafo_calles, info_nodos = obtener_datos(ruta_mapa)
        if grafo_nodos and grafo_calles and info_nodos:
            mapa_ok = True
    #Busco la pizeria
    dir_pizeria, vertice_pizeria = ingresar_calles(grafo_calles, msj_pizeria)
    
    #Debo obtener el vertice de grafo_nodos, por que los algoritmos se manejan 
    #con la posicion de memoria ( lo mismo con el cliente)
    vertice_pizeria = grafo_nodos.obtener_vertice(vertice_pizeria.clave)
    #Obtengo la info de la pizeria
    info_pizeria = info_nodos[vertice_pizeria.clave]
    #Agrego el marcador de la pizeria
    #~ kml.agregar_marcador("Pizeria", info_pizeria["latitud"], info_pizeria["longitud"])
    
    pizeria = (vertice_pizeria, dir_pizeria, info_pizeria)

    
    while True:
        #Bucle principal
        opcion = menu()
        if opcion == "3":
            #SALIR
            kml.finalizar()
            print msj_kml_finalizado
            return 0
        
        elif opcion == "1":
            #1)Generar ruta              
            #~ #Busco al cliente
            dir_cliente, vertice_cliente = ingresar_calles(grafo_calles, msj_cliente)
            vertice_cliente = grafo_nodos.obtener_vertice(vertice_cliente.clave)
            info_cliente = info_nodos[vertice_cliente.clave]
            cliente = (vertice_cliente, dir_cliente, info_cliente)
            #Verifico que sean distitnos el inicio del final
            if pizeria != cliente:
                print "Ida..."
                viaje(grafo_nodos, cliente, "Cliente", pizeria, "Pizeria", info_nodos, kml)
                print "Vuelta..."
                viaje(grafo_nodos, pizeria, "Pizeria", cliente, "Cliente", info_nodos, kml)

                print msj_kml_ok
            else:
                print msj_err_lugar               
        
        elif opcion == "2":
            #~ 2)Ruta e/puntos cualesquiera
            #~ #VerticeA
            dir_A, verticeA = ingresar_calles(grafo_calles, "Ingrese interseccion del vertice_A:")
            verticeA = grafo_nodos.obtener_vertice(verticeA.clave)
            #~ #VerticeB
            dir_B, verticeB = ingresar_calles(grafo_calles, "Ingrese interseccion del vertice_B:")
            verticeB = grafo_nodos.obtener_vertice(verticeB.clave)
            
            info_A = info_nodos[verticeA.clave]
            info_B = info_nodos[verticeB.clave]
            
            A = (verticeA, dir_A, info_A)
            B = (verticeB, dir_B, info_B)
            #Verifico que sean distitnos el inicio del final
            if A != B:
                print "Ida..."
                viaje(grafo_nodos, A, "VerticeA", B, "VerticeB", info_nodos, kml)
                #el regreso
                print "Vuelta..."
                viaje(grafo_nodos, B, "VerticeB", A, "VerticeA", info_nodos, kml)

                print msj_kml_ok
            else:
                print msj_err_lugar


if __name__ == '__main__':
	main()

