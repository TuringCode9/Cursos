#!/usr/bin/env python3

"""
Funciones
¿Qué son las funciones?
    .Conjunto de línea de código agrupadas(bloque de código) que funcionan como una unidad
    realizando una tarea específica.
    .Las funciones de Python pueden devolver valores.
    .Las funciones en Python pueden tener parámetros o argumentos.
    .A las funciones también se les denominca métodos cuando se encuentran definidas dentro de 
    una clase.

¿Porqué creamos funciones dentro de un programa?
    .Reutilización de código(cuando sea necesario o si es necesario).

Sintaxis de una función en Python
    .def name_function():
        .Instrucciones de la función.
        .return (opcional) # Return -> Devolución de valores.
    
    .def name_function(parametros):
        .Instrucciones de la función.
        .return (opcional) # Return -> Devolución de valores.

Ejecución de una función:
    .name_function()
    .name_function(parametros)

Funciones Predefinidas: Se nos proporciona por el lenguaje de programación.
Funciones Propias     : Crear nuestras propias funciones para usarlo en el futuro.

"""
# Los programas en Python tenemos que guardarlo con extensión (.py).
def Sucesion_Fibonacci(n):
    """Sucesión de Fibonacci"""
    a,b =0,1
    numberFibonacci = []
    while a < n:
        numberFibonacci.append(a)
        a,b = b,a+b
    return numberFibonacci

result = Sucesion_Fibonacci(100)
print(result)

def mensaje(): # Declaración de la función
    print("Estamos aprenndiendo a programar en Python")
    print("Poco a poco iremos avanzando")
    print("Python scripting")

# Una función para ejecutarse tiene que ser llamado.
mensaje() # Llamada de la función








