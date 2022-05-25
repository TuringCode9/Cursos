#!/usr/bin/env python3

# Cada else debe ir acompañado de su correspondiente if.
edad = int(input("Digite su edad: "))
if edad > 0 and edad < 18:
    print("Es menor de edad")
elif edad >= 18 and edad < 100:
    print("Eres mayor de edad")
else:
    print("Edad incorrecta")


# Introducir una nota y evaluaremos si la nota es : Insuficiente,Suficiente,
nota_alum = int(input("Digite la nota: "))
if nota_alum < 5:
    print("Insuficiente")
elif nota_alum < 6:
    print("Suficiente")
elif nota_alum < 7:
    print("Bien")
elif nota_alum < 9:
    print("Notable")
else:
    print("Sobresaliente")

