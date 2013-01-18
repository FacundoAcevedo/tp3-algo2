#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
"""Todo lo relacionado a la generacion del KML"""


class SexyKML(object):
    """Generador SexyKML"""
    def __init__(self,titulo, ruta_archivo = False):
        if ruta_archivo:
            self.ruta_archivo = ruta_archivo
        self.ruta = "rutas.kml"
        try:
            self.archivo = open("rutas.kml","w")
        except IOError:
            return None
        self.salida = []
        #Agrego la cabecera
        cadena = ""
        cadena +='<?xml version="1.0" encoding="UTF-8"?>\n'
        cadena +='<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        cadena += "<Document>\n\n\n"
        cadena += """<!-- Título del mapa -->\n"""
        cadena += """\t<name>"""+str(titulo)+"""</name>\n"""
        cadena += """<!-- Final Título -->\n"""
        
        self.salida.append(cadena)


        
    def agregar_comentario(self, comentario):
        """Agrega un comentario al archivo"""
        slef.salida.append("<!-- "+str(comentario)+" -->\n")
    
    def agregar_ruta(self, nombre, ruta):
        """Recibe un ruta con el sigueinte estilo:
        [(x,y),(x,y)...] y la devuelve de la menera x,y x,y x,y"""
        string = ""
        for elemento in ruta:
            string += str(elemento+" ")
            
        cadena = ""
        cadena += """<!-- Acá empieza una línea -->\n"""
        cadena += "\t<Placemark>\n"
        cadena += """\t\t<name>"""+str(nombre)+"""</name>\n"""
        cadena += """\t\t<LineString>\n"""
        cadena += """\t\t\t<coordinates>\n"""
        cadena += "\t\t\t\t"+string+"\n"
        cadena += """\t\t\t</coordinates>\n"""
        cadena += """\t\t</LineString>\n"""
        cadena += """\t</Placemark>\n"""
        if cadena not in self.salida:
                self.salida.append(cadena)
        
    
    def agregar_marcador(self, nombre, lat, lon):
        """Agrega un marcador"""
        cadena = ""
        cadena += """<!-- Acá empieza una línea -->\n"""
        cadena += "\t<Placemark>\n"
        cadena += """\t\t<name>"""+str(nombre)+"""</name>\n"""
        cadena += """\t\t<Point>\n"""
        cadena += """\t\t\t<coordinates>\n"""
        cadena += "\t\t\t\t"+str(lat)+","+str(lon)+"\n"
        cadena += """\t\t\t</coordinates>\n"""
        cadena += """\t\t</Point>\n"""
        cadena += """\t</Placemark>\n"""
        if cadena not in self.salida:
                self.salida.append(cadena)
        
    
    def finalizar(self):
        """Vuelca lo agregado y cierra el archivo"""
        self.salida.append("""</Document>\n</kml>""")
        try:
            self.archivo.writelines(self.salida)
            return True
        except IOError:
            return False
    
        
        
        
            
        




