#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
    Funciones referidas al tratamiento de cadenas
"""




##Funciones

def texto(entrada):
	"""Recibe un tipo y lo transforma al estandar de texto que usamos
	en las busquedas, pasa todo a minusculas, reemplaza espacios por
	guiones bajos"""
	
	entrada = str(entrada)
	return entrada.lower().replace(" ", "_")
	
def partir_calle(entrada):
        """La calle viene con el siguiente formato:
        Calle1,Calle2
        asi que tengo que devolver una tupla con las dos calles"""
        separador = ","
        entrada = texto(entrada)
        indice = entrada.find(separador)
        if indice != -1:
                return entrada[:indice],entrada[indice+len(separador):]
        else:
                return -1




##########################<EOF
