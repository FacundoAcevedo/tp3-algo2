#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
   Todo lo relacionado al uso de grafo y el grafo mismo
"""
from cola import Cola

class Vertice:
    def __init__(self,clave):
        """Crea el vertice"""
        self.clave =clave
        self.adyacentes = {} #Crea un diccionario de vertices adyacentes

    def agregar_vecino(self,vecino,peso):
        """Agrega vertices adyacentes propiamente al vertice"""
        self.adyacentes[vecino] = peso #Agrega el peso del vecino objeto

    def __str__(self):
        """Imprime los adyacentes del vertice"""
        return str(self.clave) + ' --> ' + str([i.clave for i in self.adyacentes])

    def conseguir_conexiones(self):
        """Retorna los vertices adyacentes"""
        return self.adyacentes.keys()
    
    def conseguir_lista_conexiones(self):
        return [int(i.clave) for i in self.adyacentes]

    def conseguir_clave(self):
        """Retorna un vertice que posee adyacentes"""
        return self.clave

    def conseguir_peso(self,vecino):
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
            for elemento in vecinos.conseguir_lista_conexiones():
                s += str(vertice) +  " -> "  + str(elemento) + "\n"
        return s        
        
    def __len__(self):
        return len(self.vertices)

    def agregar_vertice(self,clave):    
        """Agrega un vertice a la clase grafo"""
        nuevo_vertice= Vertice(clave) #crea un nuevo vertices
        self.vertices[clave] = nuevo_vertice
        #return nuevo_vertice

    def obtener_vertice(self,vertice):
        """Retorna el objeto clase vertice"""
        if vertice in self.vertices:
            return self.vertices[vertice] #retorna objeto
        else:
            return None
            
    def obtener_vertices(self):
        """Retorna los vertices que componen el grafo"""
        return self.vertices.keys()

    def __contains__(self,n):
        """Retorna el vertice si se encuentra en el grafo"""
        return n in self.vertices
    
    def cantidad_vertices(self):
        return len(self.vertices)

    def agregar_arista(self,vertice,vecino,peso, dirigido = False):
        """Agrega un vertice adyacente al actual con su peso de arista"""
        if vertice not in self.vertices:
            nv = self.agregar_vertice(vertice)
        if vecino not in self.vertices:
            nv = self.agregar_vertice(vecino)
        self.vertices[vertice].agregar_vecino(self.vertices[vecino], peso)
        if dirigido:
            self.agregar_arista(vecino,vertice,peso,False)



def verificar_existencia_calles(calles, grafo):
    """Verifica que las calles recibidas (dupla) esten dendo del grafo"""
    verticeA = grafo.obtener_vertice(calles[0])
    verticeB = grafo.obtener_vertice(calles[1])
    
    if verticeA and verticeB:
        return True
    return False
    
def dijktra(grafo, vertice_inicial):
    """Devuelve una colo de los nodos a visitar"""
    cola = Cola()
    infinito = -1 #-1 esta lejos de infinito, depende de donde lo mires
    distancia = []
    visto = []
    
    #~ Marco todo como distancia infinito y no visitado
    for indice in range(len(grafo)-1):
        distancia.append(infinito)
        visto.append(False)
    
    
    for vertice in grafo.obtener_vertices():
        #~ Reviso que sean vecinos
        if vertice_inicial not in vertice.adyacentes:  #VER ACA
            distancia[vertice.conseguir_clave()] = infinito
        else:
            distancia[vertice.conseguir_clave()] = vertice.conseguir_peso(vertice_inicial)
            
    distancia[vertice_inicial] = 0
    visto[vertice_inicial] = True
    
    #~ Mientras haya un vertice sin visistar
    while False in visto:
        #~ Busco en la lista el primero no visitado
        vertice_visitar = visto.index(False)
        #~ Lo visito
        visto[a_visitar] = True
        #~ Obtengo el objeto
        vertice_visitar =  grafo.obtener_vertice(vertice_visitar)
        
        for vertice in vertice_visitar.conseguir_conexiones():
            if distancia[vertice.conseguir_clave()] > distancia[vertice_visitar.conseguir_clave()] + vertice.conseguir_peso(vertice_visitar):
                distancia[vertice.conseguir_clave()] = distancia[vertice_visitar.conseguir_clave()] + vertice.conseguir_peso(vertice_visitar)
            
    print distancia
        
        
    
    
#~ función Dijkstra (Grafo G, nodo_salida s)
  #~ //Usaremos un vector para guardar las distancias del nodo salida al resto entero distancia[n] 
  #~ //Inicializamos el vector con distancias iniciales booleano visto[n] 
  #~ //vector de boleanos para controlar los vertices de los que ya tenemos la distancia mínima
  #~ para cada w ∈ V[G] hacer
     #~ Si (no existe arista entre s y w) entonces
         #~ distancia[w] = Infinito //puedes marcar la casilla con un -1 por ejemplo
     #~ Si_no
         #~ distancia[w] = peso (s, w)
     #~ fin si 
  #~ fin para
  #~ distancia[s] = 0
  #~ visto[s] = cierto
  #~ //n es el número de vertices que tiene el Grafo
  #~ mientras que (no_esten_vistos_todos) hacer 
     #~ vertice = coger_el_minimo_del_vector distancia y que no este visto;
     #~ visto[vertice] = cierto;
     #~ para cada w ∈ sucesores (G, vertice) hacer  # SUPONGO QUE VECINOS
         #~ si distancia[w]>distancia[vertice]+peso (vertice, w) entonces
            #~ distancia[w] = distancia[vertice]+peso (vertice, w)
         #~ fin si
     #~ fin para 
  #~ fin mientras
#~ fin función


