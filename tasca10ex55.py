"""Escriure un programa que sumi tots els números entre dos números donats, ambdós inclosos.
"""

def sumaEntre(num1, num2):
    suma = 0
    for i in range(num1, num2 + 1):
        suma += i
    return suma
#programa principal
print(sumaEntre(1, 20))