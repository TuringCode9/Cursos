#!/usr/bin/env python3
"""
Las tuplas
   .Las tuplas son listas inmutables,no se pueden modificar su valor después de su creación.
      .No permiten añadir,eliminar y mover elementos(no append,extend,remove).
      .Si permiten extraer porciones,el resultado de la extracción es una nueva tupla.
      .Si permiten comprobar si un elemento se encuentra en la tupla.d
    
    ¿Qué utilidad o ventaja tiene respecto a la lista?
      .Más rapidas.
      .Menos espacio.
      .Fromatean strings.
      .Pueden usarse como claves en un diccionario(las listas no).

Sintaxis de una tupla
   miTupla = ("Daniel",True,"Aprendiendo")
   

"""

# Los parentesis en las tuplas son opcionales.
from __future__ import annotations


miTupla = ("Daniel",True,9,"Zai",9,False,9)
print(miTupla[0])

# Indices negativos en una tupla.
print(miTupla[-1])

# Convertir una tupla en una lista.
miLista1 = tuple(miTupla)
print(miLista1[:])

# Convertir una lista a tupla.
miTupla1 = list(miLista1)
print(miTupla1[:])

# Para comprobar si un elemento se encuentra dentro de una tupla.
print("Daniel" in miTupla1)

# count(elemento): Nos permite averiguar cuantos elementos se encuentran dentro de una tupla.
print(miTupla1.count(9))

# Función len():Nos permite averiguar la longitud de una tupla.
print(miTupla1)
print(len(miTupla1))

# Tuplas unitarias: Contienen un unico elemento.
miTuplaUnitaria = ("Daniel",)
print(len(miTuplaUnitaria))

# Empaquetado de tupla.
miTupla2 = ("Daniel",True,1998)
nombre,decision,anio = miTupla2
# Desenpaquetado de tupla.
print(nombre)
print(decision)
print(anio)

