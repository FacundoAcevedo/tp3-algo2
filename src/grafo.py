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
infinito = 9999**999

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
        nuevo_vertice= Vertice(clave) #crea un nuevo vertices
        self.vertices[clave] = nuevo_vertice
        #return nuevo_vertice

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
    
def procesar_ruta(ruta, vert_inicio, vert_fin):
    """Recibe una ruta (diccionario) el vertice inicial y el vertice
    final, devuelve una lista de los vertices(objeto) ordenados de
    de inicio a fin"""
    
    salida = []
    cadena =  ""
    aux = ruta[vert_fin]
    salida.append(vert_fin)

    for i in range(len(ruta)-2):
        salida.append(aux)
        aux = ruta[aux]
    salida.append(aux)
    salida.append(vert_inicio)
    
    salida.reverse()
    
    return salida

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

def imprimir_ruta(ruta, vert_inicio, vert_fin):
    """Imprime la ruta de manera legible"""
    salida = []
    
    cadena =  ""
    
    aux = ruta[vert_fin]
    salida.append(str(vert_fin.clave))


    for i in range(len(ruta)-2):
        salida.append(str(aux.clave))
        aux = ruta[aux]
    salida.append(str(aux.clave))
    salida.append(str(vert_inicio.clave))
    
    salida.reverse()
    for item in salida:
        cadena += item+"->"
        
    return cadena[:len(cadena)-2]
    
            
        
    
        
        
    

    
def dijkstra(grafo, vertice_inicial): ##Reimplementacion con hash...
    """Devuelve una cola de los nodos a visitar
    vertice_inicial es un objeto vertice"""
    cola = Cola()
    #~ infinito = 6*(10**23)
    distancia = {}
    visto = {}
    ruta = {}
    
    if not isinstance(vertice_inicial, Vertice):
        return 0
    
    #~ Marco todo como distancia infinito y no visitado
    for objeto_vertice in grafo.obtener_objetos_vertice():
        distancia[objeto_vertice] = infinito
        visto[objeto_vertice] = False
    
    
    for vertice in grafo.obtener_objetos_vertice():
        #~ Reviso que sean vecinos
        #~ if vertice_inicial not in vertice.adyacentes:
        if vertice not in vertice_inicial.adyacentes:
            distancia[vertice] = infinito
        else:
            #~ distancia[vertice] = vertice.obtener_peso(vertice_inicial)
            distancia[vertice] = vertice_inicial.obtener_peso(vertice)
            
    distancia[vertice_inicial] = 0
    visto[vertice_inicial] = True
    
    #~ Mientras haya un vertice sin visistar
    #~ while False in visto.values():
    for vertice_visitar,estado in sorted(visto.items()):
        if estado is False:
            #~ imprimir_distancia(distancia)
            #lo marco como visitado
            visto[vertice_visitar] = True            
      
            for vertice in vertice_visitar.obtener_adyacentes():
                if distancia[vertice] > (distancia[vertice_visitar] + vertice_visitar.obtener_peso(vertice)):                    
                    distancia[vertice] = distancia[vertice_visitar] + vertice_visitar.obtener_peso(vertice)
                    ruta[vertice] = vertice_visitar
                
    return ruta
        
#####################################################################################    
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


#~ def dijktra(grafo, vertice_inicial):
    #~ """Devuelve una cola de los nodos a visitar"""
    #~ cola = Cola()
    #~ infinito = -1 #-1 esta lejos de infinito, depende de donde lo mires
    #~ distancia = []
    #~ visto = []
    #~ 
    #~ Marco todo como distancia infinito y no visitado
    #~ for indice in range(len(grafo)+1): #el +1 es parche, Revisar por que se sale de rango
        #~ distancia.append(infinito)
        #~ visto.append(False)
    #~ 
    #~ 
    #~ for vertice in grafo.obtener_objetos_vertice():
        #~ Reviso que sean vecinos
        #~ if vertice_inicial not in vertice.adyacentes:
            #~ distancia[vertice.obtener_clave()] = infinito
        #~ else:
            #~ distancia[vertice.obtener_clave()] = vertice.obtener_peso(vertice_inicial)
            #~ 
    #~ distancia[vertice_inicial] = 0
    #~ visto[vertice_inicial] = True
    #~ 
    #~ Mientras haya un vertice sin visistar
    #~ while False in visto:
        #~ Busco en la lista el primero no visitado
        #~ vertice_visitar = visto.index(False)
        #~ Lo visito
        #~ visto[vertice_visitar] = True
        #~ print vertice_visitar
        #~ 
        #~ Obtengo el objeto
        #~ vertice_visitar =  grafo.obtener_vertice(vertice_visitar)
        #~ 
        #~ 
        #~ for vertice in vertice_visitar.obtener_adyacentes():
            #~ if distancia[vertice.obtener_clave()] > distancia[vertice_visitar.obtener_clave()] + vertice.obtener_peso(vertice_visitar):
                #~ distancia[vertice.obtener_clave()] = distancia[vertice_visitar.obtener_clave()] + vertice.obtener_peso(vertice_visitar)
            
    #~ print distancia
    


