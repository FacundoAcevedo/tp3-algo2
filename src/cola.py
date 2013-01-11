#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       cola.py

class Cola(object):
    "FIFO"
    def __init__(self):
        self.lista = []
        
    def agregar(self, item):
        "Agrega un elemento a la ultima posicion de la cola"
        self.lista.append(item)
    
    def quitar(self):
        "Devuelve el primer elemento de la cola"
        try:
            return self.lista.pop(0)
        except:
            raise ValueError("La lista esta vacia")
    
    def estaVacia(Self):
        if len(self.lista) == 0:
            return True
        else:
            return False
    def __len__(self):
        return len(self.lista)
