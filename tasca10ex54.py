"""Escriure un programa que ens mostri tots els números parells fins arribar a 100. 
Ex: 2, 4, 6 ...., 98, 100. Prova-la. Fer el mateix amb els números senars.
"""

def imprimirParells():
    for i in range(2, 101, 2):
        print(i)

def imprimirSenars():
    for i in range(1, 100, 2):
        print(i)

#Programa principal
imprimirSenars()