#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
   Todo lo relacionado con la interaccion de la maquina y el usuario
"""

##Importaciones

from grafo import Grafo
from texto import *
from archivos import *


##Objetos


##Funciones

#~ Nota:
    #~ El ingreso de la interseccion se debe hacer separando las calles con
    #~ una coma ","

def ingresar_calles(grafo_calles):
    """Recibe las calles"""
    dupla= ()
    continuar = True
    
    print "Ingrese la interseccion con el siguiente formato:\n\
        Calle1,calle2"

    while continuar:
        calles = raw_input(":> ")
        dupla = partir_calle(calles)
        if dupa != -1:
            continuar = False
        else:
            existencia = verificar_existencia_calles(dupla, grafo_calles)
            if !exitencia:
                print "Las calles no se encuentran dentro del mapa cargado"
    return dupla


        
        
    
    
    





##########################<EOF
