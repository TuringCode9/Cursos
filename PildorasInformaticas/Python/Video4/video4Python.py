#!/usr/bin/env python3

# Tipos operadores y variables.
"""
En Python vamos a manejar principalmente 3 tipos de datos:
1)Númericos
    1.1)Enteros
    1.2)Coma flotante
    1.3)Complejos
2)Textos
    .Los textos van entre comillas y estas pueden ser simples,dobles o triples.

3)Booleanos
    .Pueden tener 2 valores : True or False.



Operadores en Python
1)Aritmeticos
    .Suma                   -> +
    .Resta                  -> -
    .Multiplicación         -> *
    .División               -> /
    .Módulo                 -> %
    .Exponente              -> **
    .División Entera        -> //
2)Comparación
    .Igual que              -> ==
    .Diferente que          -> != 
    .Mayor que              -> >
    .Menor que              -> <
    .Mayor o igual que      -> <=
    .Menor o igual que      -> >=
3)Lógicos
    .AND
    .OR
    .NOT
4)Asignación
    .Igual                  ->  =
    .Incremento             -> +=
    .Decremento             -> -=
    .*=
    ./=
    .%=
    .**=
    .//=
5)Especiales
    .IS
    .IS NOT
    .IN
    .NOT IN


Varaible:
    .Espacio en la memoria de un ordenador(RAM) donde se almacenara un valor que podra cambiar 
    durante la ejecución del programa.

"""

# Módulo: Es el resto de una división.
num1 = int(input("Digite el número 1: "))
num2 = int(input("Digite el número 2: "))

modulo = num1 % num2
print(modulo)

# El tipo de variable lo establece el contenido.
# En Python absolutamente todo es un objeto.

# Función type():Nos devolvera el tipo de dato.
number = 13
number_decimal = 3.1416
name = "Daniel"
decision = True

print(type(number))
print(type(number_decimal))
print(type(name))
print(type(decision))


mensaje = """Mensaje 
con saltos de línea
en Python"""
print(mensaje)

numero1 = int(input("Introduce el número 1: "))
numero2 = int(input("Introduce el número 2: "))

if numero1 > numero2:
    print("Número 1 es mayor")
elif numero1 == numero2:
    print("Número 1 es igual al número 2")
else:
    print("Número 2 es mayor")
    






