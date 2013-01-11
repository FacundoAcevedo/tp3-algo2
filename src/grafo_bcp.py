#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    Implementacion en python de un grafo
"""




##Objetos

class vertice:
	"""Define un nodo"""
	def __init__(self, N, X, Y, lat, lon):
		"""Inicializo un nodo"""
		self.n = N
		self.x = X
		self.y = Y
		self.lat = lat
		self.lon = lon
		self.adyacentes = {}
	
	def get_x(self):
		"Devuelve la coordenada x"
		return self.x
		
	def get_y(self):
		"Devuelve la coordenada y"
		return self.y
		
	def get_latitud(self):
		"Devuelve la latitud"
		return self.lat
		
	def get_longitud(self):
		"Devuelve la longitud"
		return self.lon
		

class grafo:
    """Define un grafo"""
    def __init__(self):
        self.grafo = {}

    def __get_iterador(self, obj):
        try:
            iterador = iter(obj)
        except TypeError:
            iterador = (obj, )
        return iterador

    def agregar_vertice(self, vertice):
        """
           agregar vertice al grafo
       """
        for i in self.__get_iterador(vertice):
            self.grafo[i] = set()

    def del_vertice(self, vertice):
        """
			Quita el vertice si esta en el grafo
       """
        vertice = set(self.__get_iterador(vertice))
        for i in vertice:
            if i in self.grafo:
                self.grafo.pop(i)
        for i in self.grafo.iterkeys():
            self.grafo[i] -= vertice

    def es_vertice(self, vertice):
        """
         True si el vertice pertenece al grafo, de otra manera
         False
       """
        if vertice in self.grafo:
            return True
        return False

    def agregar_arista(self, src, dest, noDirigido=True):
        """
           Agrega una arista desde el inicio hasta el final
           Or agregar aristas from the cartesian product of src cross dest
           Example: agregar_arista((1, 2, 3), (2, 3))
           agregar the aristas:
               (1, 2)
               (1, 3)
               (2, 3)
               (3, 2)
       """
        for s in self.__get_iterador(src):
            if s not in self.grafo:
                self.grafo[s] = set()
            for d in self.__get_iterador(dest):
                if s == d:
                    continue
                if d not in self.grafo:
                    self.grafo[d] = set()
                self.grafo[s].add(d)
                if noDirigido:
                    self.grafo[d].add(s)

    def delete_arista(self, src, dest):
        """
           Quita la arista 
           Or the aristas of the cartesian product of src cross dest
           Example: delete_arista((1, 2, 3), (2, 3))
           Will delete the aristas:
               (1, 2)
               (1, 3)
               (2, 3)
               (3, 2)
       """
        dest = set(self.__get_iterador(dest))
        src = set(self.__get_iterador(src))
        for i in src:
            if i in self.grafo:
                self.grafo[i] -= dest

    def get_arista(self, vertice):
        """
           Devuelve las aristas del vertice dado
       """
        return self.grafo[vertice]

    def walk(self, source, topdown=False):
        """
       Walk through the grafo:
           DFS(Deep First Search)if topdown = True
           Otherwise BFS(Breath First Search)
       """
        v = set()
        l = [source]
        if topdown:
            print "DFS:"
        else:
            print "BFS:"
        v.agregar(source)
        while l:
            nodo = l.pop()
            print nodo,
            for i in self.grafo[nodo]:
                if i not in v:
                    v.agregar(i)
                    if topdown:
                        l.append(i)
                    else:
                        l.insert(0, i)
        print ""

    def __str__(self):
        #Print the vertice
        s = "vertice -> aristas\n"
        for k, v in self.grafo.iteritems():
            s += "%-6s -> %s\n" % (k, v)
        return s

if __name__ == '__main__':
    grafo = grafo()
    grafo.agregar_arista(1, (2, 3))
    grafo.agregar_arista(2, (4, 5))
    grafo.agregar_arista(3, (6, 7))
    print grafo







##########################<EOF
