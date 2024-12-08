"""Escriure un programa que mostri els dígits parells d’un número donat."""

num = int(input("Introdueix un nombre: "))

llista = []

for i in range(len(str(num))):    
    llista.append(int(str(num)[i]))

for i in llista:
    if i % 2 == 0:
        print("El dígit {} és parell".format(i))