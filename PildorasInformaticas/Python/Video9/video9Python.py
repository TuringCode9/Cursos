#!/usr/bin/env python3
"""
Los diccionarios

¿Qué son los diccionarios?
    .Estructuras de datos que nos permiten almacenar valores de diferente tipo(entero,cadenas de 
    de texto,decimales) e incluso listas y otros diccionarios.
    .La principal característica de los diccionarios es que los datos se almacenan asociados a una
    clave de tal forma que se crea una asociación de tipo clave:valor para cada elemento almacenado.
    .Los elementos almacenados no estan ordenados.El orden es indiferente a la hora de almacenar 
    información en un diccionario.

Sintaxis 
"""

# Clave : Valor
miDiccionario = {"Perú":"Lima","Colombia":"Bogota","Alemania":"Berlin","Francia":"Paris",
"España":"Madrid"}

print(miDiccionario["Francia"])
print(miDiccionario["Perú"])
print(miDiccionario["España"])

# Imprimir todo el diccionario.
print(miDiccionario)

# Agregar un elemento a un diccionario.
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)

# Modificando un valor de un diccionario.
miDiccionario["Italia"] = "Roma"
print(miDiccionario)

# Eliminar algún elemento de nuestro diccionario.
del miDiccionario["España"]
print(miDiccionario)

miDiccionario1 = {23:"Jordan","Mosqueteros":3}
print(miDiccionario1)

miTupla1 = ("Perú","Huánuco","Francia","Alemania")
miDiccionario2 = {miTupla1[0]:"Lima",miTupla1[1]:"Huánuco",miTupla1[2]:"París",miTupla1[3]:"Berlin"}
print(miDiccionario2)

# Acceder a un elemento en concreto.
print(miDiccionario2["Huánuco"])

# Un diccionario almacene en su interior una tupla.
miDiccionario3 = {23:"Jordan","Equipo":"Chicago","Nombre":"Michael",
"Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario3["Anillos"])

print(miDiccionario3.keys())
print(miDiccionario3.values())
print(len(miDiccionario3))
