"""Definir una funció llista_20_elements() que retorni una llista de 20 elements 
creats aleatòriament entre 1 i 100. Provar amb la funció anterior si 
s’han generat elements duplicats o no.
"""

import random


def llista_20_elements():
    llista = [random.randint(1, 100) for _ in range(20)]
    return llista


def hi_ha_duplicats(l):
    if len(l) == len(set(l)):
        return "No hi ha duplicats"
    else:
        return "Hi ha duplicats"



llista = llista_20_elements()
print("Llista generada:", llista)


if hi_ha_duplicats(llista):
    print("Hi ha elements duplicats a la llista.")
else:
    print("No hi ha elements duplicats a la llista.")
