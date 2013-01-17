#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
   Todo lo relacionado al uso de grafo y el grafo mismo
"""
from cola import Cola

#VARIABLE GLOBAL
#Si es necesario que la quite, avisame, solo la voy a usar para poder
#comparar con infinito, so no la tengo que declarar en todos lados
#no tarda en calcularo: real 0m0.039s
#~ infinito = 9999**999
infinito = float("inf")

class Vertice:
    def __init__(self,clave):
        """Crea el vertice"""
        self.clave = clave
        self.adyacentes = {} #Crea un diccionario de vertices adyacentes

    def agregar_vecino(self, vecino, peso):
        """Agrega vertices adyacentes propiamente al vertice"""
        self.adyacentes[vecino] = peso #Agrega el peso del vecino objeto

    #~ def __str__(self):
        #~ """Imprime los adyacentes del vertice"""
        #~ return str(self.clave) + ' --> ' + str([i.clave for i in self.adyacentes])

    def obtener_adyacentes(self):
        """Retorna los vertices adyacentes"""
        return self.adyacentes.keys()

    def obtener_lista_adyacentes(self):
        return [int(i.clave) for i in self.adyacentes]

    def obtener_clave(self):
        """Retorna un vertice que posee adyacentes"""
        return self.clave

    def obtener_peso(self,vecino):
        """Retona el peso de la arista"""
        return self.adyacentes[vecino]

class Grafo:
    def __init__(self):
        """Crea el grafo"""
        self.vertices = {} # clave es el nodo, valores es la clase vertices


    def __iter__(self):
        """ Crea un iterador en grafo"""
        return iter(self.vertices.values())

    def __str__(self):
        s = "\n::Conexiones::\n"
        for vertice, vecinos in self.vertices.iteritems():
            for elemento in vecinos.obtener_lista_adyacentes():
                s += str(vertice) +  " -> "  + str(elemento) + "\n"
        return s

    def __len__(self):
        return len(self.vertices)

    def agregar_vertice(self,clave):
        """Agrega un vertice a la clase grafo"""
        self.vertices[clave] = Vertice(clave) #crea un nuevo vertices

    def obtener_vertice(self,vertice):
        """Retorna el objeto clase vertice"""
        if vertice in self.vertices:
            return self.vertices[vertice] #retorna objeto
        else:
            return None

    def obtener_lista_vertices(self):
        """Retorna los vertices que componen el grafo"""
        return self.vertices.keys()

    def obtener_objetos_vertice(self):
        """Retorna todos los vertieces (OBJETOS)"""
        return self.vertices.values()

    def __contains__(self,n):
        """Retorna el vertice si se encuentra en el grafo"""
        return n in self.vertices

    def agregar_arista(self,vertice,vecino,peso):
        """Agrega un vertice adyacente al actual con su peso de arista"""
        if vertice not in self.vertices:
            self.agregar_vertice(vertice)
        if vecino not in self.vertices:
            self.agregar_vertice(vecino)
        self.vertices[vertice].agregar_vecino(self.vertices[vecino], peso)



def verificar_existencia_calles(calles, grafo):
    """Verifica que las calles recibidas (dupla) esten dendo del grafo"""
    verticeA = grafo.obtener_vertice(calles[0])
    verticeB = grafo.obtener_vertice(calles[1])

    if verticeA and verticeB:
        return True
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
        lat = str(info_nodos[vertice.clave]["latitud"])
        lon = str(info_nodos[vertice.clave]["longitud"])
        salida.append(lat+","+lon)
    
    return salida
        
        
