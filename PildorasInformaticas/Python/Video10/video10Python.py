#!/usr/bin/env python3
"""
Condicional If

¿Qué es el flujo de ejecución del programa?
    .El orden con el cual se ejecutan sus instrucciones.
    .Programa esta formado por una gran cantidad de lineas de código y normalmente se ejecutan de
    arriba hacia abajo.

"""
if True:
    print("Siempre se ejecutara")

def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Desaprobado"
    return valoracion
    
print(evaluacion(3))
print(evaluacion(7))




