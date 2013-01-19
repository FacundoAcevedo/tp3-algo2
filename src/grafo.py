#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
   Todo lo relacionado al uso de grafo y el grafo mismo
"""


from constantes import *
from texto import *


class Grafo:
    def __init__(self):
        """Inicializa el grafo"""
        self.vertices = {}


    def __iter__(self):
        """ Devuelve un iterador de los vertices"""
        return iter(self.vertices.values())

    def __str__(self):
        "Para printear..."
        s = "\n::Conexiones::\n"
        for vertice, vecinos in self.vertices.iteritems():
            for elemento in vecinos.obtener_lista_adyacentes():
                s += str(vertice) +  " -> "  + str(elemento) + "\n"
        return s
        
    def __contains__(self,vertice):
        """si el vertice esta en el grafo, debuelve True"""
        return vertice in self.vertices

    def __len__(self):
        "Cantidad de vertices"
        return len(self.vertices)

    def agregar_vertice(self,clave):
        """Agrega un vertice"""
        self.vertices[clave] = Vertice(clave) 

    def obtener_vertice(self,vertice):
        """Devuelve un objeto vertice"""
        if vertice in self.vertices:
            return self.vertices[vertice] 
        else:
            return None

    def obtener_lista_vertices(self):
        """Devuelve todos los vertices del grafo (str)"""
        return self.vertices.keys()

    def obtener_objetos_vertice(self):
        """Devuelve todos los vertieces (OBJETOS)"""
        return self.vertices.values()


    def agregar_arista(self,vertice,vecino,peso):
        """Agrega un vertice adyacente al actual con el peso"""
        if vertice not in self.vertices:
            self.agregar_vertice(vertice)
        if vecino not in self.vertices:
            self.agregar_vertice(vecino)
        self.vertices[vertice].agregar_vecino(self.vertices[vecino], peso)
    
class Vertice:
    def __init__(self,clave):
        """Inicializa el vertice"""
        self.clave = clave
        self.adyacentes = {} 

    def agregar_vecino(self, vecino, peso):
        """Agrega vertices adyacentes al vertice"""
        self.adyacentes[vecino] = peso 

    def __str__(self):
        """Imprime los adyacentes del vertice"""
        return str(self.clave) + ' --> ' + str([i.clave for i in self.adyacentes])

    def obtener_adyacentes(self):
        """Devuelve sus vertices adyacentes"""
        return self.adyacentes.keys()

    def obtener_lista_adyacentes(self):
        return [int(i.clave) for i in self.adyacentes]

    def obtener_clave(self):
        """Devuelve su 'nombre'"""
        return self.clave

    def obtener_peso(self,vecino):
        """Devuelve el peso de la arista"""
        return self.adyacentes[vecino]


def validar_calles(calles, grafo):
    """Verifica que las calles recibidas (dupla) esten dendo del grafo"""
    verticeA = grafo.obtener_vertice(calles[0])
    verticeB = grafo.obtener_vertice(calles[1])

    if verticeA and verticeB:
        #reviso que sea una haya interseccion
        for vertice in verticeA.obtener_adyacentes():
            if vertice in verticeB.obtener_adyacentes():
                return vertice
        #reviso desde el otro lado
        for vertice in verticeB.obtener_adyacentes():
            if vertice in verticeA.obtener_adyacentes():
                return vertice
    return False

def imprimir_distancia(distancia):
    """Recibe un diccionario e imprime las distancias de manera
    leible para los.. humanos"""
    salida = []

    for vertice, distancia in distancia.items():
        if distancia == infinito:
            distancia = "INF"
        cad = str(vertice.clave) + " - " +  str(distancia)
        salida.append(cad)
    salida.sort()
    for elemento in salida:
        print elemento


def procesar_ruta(ruta, vert_inicio, vert_fin):
    """Recibe una ruta (diccionario) el vertice inicial y el vertice
    final, devuelve una lista de los vertices(objeto) ordenados de
    de inicio a fin"""

    salida = []
    cadena =  ""
    aux = ruta[vert_fin]
    salida.append(vert_fin)

    try:
        for i in range(len(ruta)-2):
            salida.append(aux)
            aux = ruta[aux]
        salida.append(aux)
    except KeyError:
        #NO SOY UN PARCHE!!!!
        #Es por el primer/ultimo vertice
        pass

    salida.append(vert_inicio)

    salida.reverse()

    return salida


def imprimir_ruta(ruta, vert_inicio, vert_fin):
    """Imprime la ruta de manera legible"""
    salida = []
    i = 0
    cadena =  ""

    aux = ruta[vert_fin]
    salida.append(str(vert_fin.clave))

    try:
        for i in range(len(ruta)-2):

            salida.append(str(aux.clave))
            aux = ruta[aux]
        salida.append(str(aux.clave))

    except KeyError:
        #NO SOY UN PARCHE!!!!
        #Es por el primer/ultimo vertice
        pass
    salida.append(str(vert_inicio.clave))
    salida.reverse()
    for item in salida:
        cadena += item+"->"

    print cadena[:len(cadena)-2]





def dijkstra(grafo,nodo_inicial):
    """Algoritmo Dijkstra, genera los mejores caminos desde el nodo_inicial
    al resto de los nodos"""
    #basado en el de wikipedia y en los de:
    #https://code.activestate.com/recipes/119466-dijkstras-algorithm-for-shortest-paths/

    ruta = {}
    distancia = {}
    visto = {}

    for vertice in grafo.obtener_objetos_vertice():
        #Marco todos los vertices en distancia infinita y como no vistos
        distancia[vertice] = infinito
        visto[vertice] = False 
        if vertice in nodo_inicial.obtener_adyacentes():
            #Si son adyacentes al nodo_inicial, le cargo sus pesos
            distancia[vertice] = float(nodo_inicial.obtener_peso(vertice))
    
    #Remarco el nodo inicial a 0 y como visitado
    distancia[nodo_inicial] = 0
    visto[nodo_inicial]=True
    
    while False in visto.values():
        #mientras haya nodos no vistos, busco el vertice adyacente 
        #mas liviano (digamos...)
        vertice=_buscar_minimo(distancia,visto)
        visto[vertice] = True
        for elemento in vertice.obtener_adyacentes():
            #Busco el menor y lo agrego a la ruta
            if distancia[elemento] > distancia[vertice] + float(vertice.obtener_peso(elemento)):
                distancia[elemento] = distancia[vertice] + float(vertice.obtener_peso(elemento))
                ruta[elemento] = vertice

    return ruta

def _buscar_minimo(distancia,visitados):
    """Funcion PRIVADA, Busca el vertice mas cercano y menos pesado"""
    minimo = infinito
    vertice = object
    
    for elemento, estado in visitados.items():
        if distancia[elemento] <= minimo and estado == False:
            minimo=distancia[elemento]
            vertice=elemento
    return vertice

def parsear_ruta(ruta, info_nodos):
    """Recibe un ruta con el sigueinte estilo:
    [vert1,vart2,...] y la devuelve de la menera x,y x,y x,y"""
    salida = []
    for vertice in ruta:
        lat = str(info_nodos[vertice.clave]["lat"])
        lon = str(info_nodos[vertice.clave]["lon"])
        salida.append(lat+","+lon)    
    return salida
    
def viaje(grafo_nodos, A, nombreA, B, nombreB, info_nodos, kml):
    """Genera el recorrido y lo guarda en el kml"""
    verticeA = A[0]
    dir_verticeA = A[1]
    info_verticeA = A[2]
    
    verticeB = B[0]
    dir_verticeB = B[1]
    info_verticeB = B[2]
    
    print msj_dijkstra
    ruta = dijkstra(grafo_nodos, verticeA)

    ruta_procesada = procesar_ruta(ruta, verticeA, verticeB)
    ruta_parseada = parsear_ruta(ruta_procesada, info_nodos)
    #~ Genero el kml
    print msj_kml
    info_verticeA = info_nodos[verticeA.clave]
    info_verticeB = info_nodos[verticeB.clave]
    kml.agregar_marcador(texto(nombreA)+" "+dir_verticeA[0]+" y "+dir_verticeA[1], info_verticeA["latitud"], info_verticeA["longitud"])
    kml.agregar_marcador(texto(nombreB)+" "+dir_verticeB[0]+" y "+dir_verticeB[1], info_verticeB["latitud"], info_verticeB["longitud"])
    kml.agregar_ruta("Ruta "+texto(nombreA)+"->"+texto(nombreB), ruta_parseada)

                    
        
        
