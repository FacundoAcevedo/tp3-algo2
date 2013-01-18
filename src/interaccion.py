#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
   Todo lo relacionado con la interaccion de la maquina y el usuario
"""

##Importaciones

from grafo import *
from texto import *
from archivos import *


##Objetos


##Funciones

#~ Nota:
    #~ El ingreso de la interseccion se debe hacer separando las calles con
    #~ una coma ","

def ingresar_calles(grafo_calles, mensaje):
    """Recibe las calles"""
    dupla= ()
    continuar = True
    print "\nIngrese la interseccion con el siguiente formato:\n\
        calle1,calle2\n"
    if mensaje:
        print mensaje.upper()
    while continuar:
        calles = raw_input(":> ")
        dupla = partir_calle(calles)
        if dupla == -1:
            print "Formato no valido\n"
        else:
            vertice = validar_calles(dupla, grafo_calles)
            continuar = False
            if not vertice:
                continuar = True
                print "Las calles no se encuentran dentro del mapa cargado o no intersectan."
    return dupla, vertice

def menu():
	
	opt=""
	opciones=["1","2","3"]
	while True:	
		print r"""
          sSSSSs   .S_sSSs      sSSs  
         d%%%%SP  .SS~YS%%b    d%%SP  
        d%S'      S%S   `S%b  d%S'    
        S%S       S%S    S%S  S%|     
        S&S       S%S    d*S  S&S     
        S&S       S&S   .S*S  Y&Ss    
        S&S       S&S_sdSSS   `S&&S   
        S&S sSSs  S&S~YSSY      `S*S  
        S*b `S%%  S*S            l*S  
        S*S   S%  S*S           .S*P  
         SS_sSSS  S*S         sSS*S   
          Y~YSSY  S*S         YSS'    
                  SP                  
                  Y    De Gerli al MUNDO!
 """.center(50)
		print r"""
        1)Generar ruta
        2)Ruta e/puntos cualesquiera -Consigna Opcional-
        3)Salir
		""".center(50)
		opt=raw_input(":>")
		
		
		if opt in opciones:
			return opt
		else:
			print "Esa opcion no esta disponible!"

def obtener_texto(mensaje):
    while True:
        print mensaje
        entrada = raw_input(":>")
        if entrada:
            return entrada


    
        
        
    
    
    





##########################<EOF
