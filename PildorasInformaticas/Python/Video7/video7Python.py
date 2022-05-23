#!/usr/bin/env python3
    
"""
La lista
   .Estructura de datos que nos permiten almacenar gran cantidad de 
   valores(equivalentes a los arrays en otros lenguajes de programación.)
   .En Python las listas pueden guardar diferentes tipo de valores
   (en otros lenguajes no ocurre esto con los arrays).
   .Se puede expandir dinamicamente añadiendo nuevos elementos
   (otra novedad despecto a los arrays en otros lenguajes).

Sintaxis de una lista en Python
   nombreLista = [elemen1,elemen2,elemen,...]
   .¿Qué es un índice de la lista?
      .Los índices de una lista comienzan desde cero.
      .elemen1 -> 0
    
"""
miLista  = ["Daniel",3.1416,"María","Pepe","Marta","Antonio"]
print(miLista[:])

# Acceder a un elemento concreto de la lista.
print(miLista[1]) # Me imprimira María.

# Indices negativos: Empieza a contar desde el final,lo hace desde -1.
print(miLista[-1])

# Rebanadas de la lista.
print(miLista[0:2]) # El 0 es inclusivo es 2 es exclusive.
print(miLista[:2])
print(miLista[1:])

# append(): Agrega un elemento al final de la lista.
miLista.append("Daniel")
miLista.append("Hola")
print(miLista[:])

# Agregar un elemento de la lista en un índice especifico.
miLista.insert(1,"Zai")
print(miLista[:])

# Agregar varios elementos a una lista.
miLista.extend(["Jirafa",True,3])
print(miLista[:])

# Para saber en que índice se encuentra un elemento de una lista.
# En caso existan elementos repetidos siempre nos dara el primer elemento que encuentre.
print(miLista[:])
print(miLista.index("Zai"))


# Comprobar si un elemento se encuentra dentro de una lista,nos devolver True o False.
print("Pepe" in miLista[:])
print("Dan" in miLista[:])

# Las listas en Python pueden almacenar distintos tipos de datos.
miNewLista = ["Daniel",True,False,12,12.45]
print(miNewLista[:])

# Eliminar elementos de una lista.
miNewLista.remove(True)
print(miNewLista[:])

# Eliminar el último elemento de una lista.
print(miNewLista[:])
miNewLista.pop()
print(miNewLista[:])

# Unios de listas.
lista1 = ["Daniel","Jorge",True]
lista2 = ["Jorge",12,False]
lista3 = lista1 + lista2
print(lista3[:])

# Múltiplicación de listas.
lista1_mult = lista1 * 3
print(lista1_mult)

