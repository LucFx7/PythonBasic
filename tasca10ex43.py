"""Escriure un programa que imprimeixi la taula de multiplicar d’un número donat (mínim 1 màxim 20).
"""

num = 0

while num < 1 or num > 20:
    num = int(input("Introdueix un nombre entre 1 i 20: "))

def taula_Multiplicar(num):
    for e in range(1, 11):
        print("{} * {} = {}".format(num, e, num*e))
        
taula_Multiplicar(num)