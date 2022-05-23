#!/usr/bin/env python3

def suma():
    num1 = 12  
    num2 = 13
    result = num1 + num2
    return result

valor = suma()
print(valor)

# Función con parámetros o argumentos
# Los argumentos o parametros de una función pueden ser de distintos tipos.
# Python siempre pasa los valores por referencia.
def suma_number(num1,num2):
    suma = num1 + num2
    return suma

suma1 = suma_number(12,12)
suma2 = suma_number(3,4)
suma3 = suma_number(12,1)

print(suma1)
print(suma2)
print(suma3)












