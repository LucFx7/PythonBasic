"""Escriure un programa on li passem un número (mínim 1 i màxim 900000) i ens indiqui la quantitat 
de dígits que té.
"""
num = 0
while num < 1 or num > 999999999:
    num = int(input("Introdueix un nombre: "))

        
print("El nombre introduit te {} xifres".format(len(str(num))))