"""Definir una funció elimina_duplicats() que donada una llista ens retorni
una nova llista sense elements duplicats."""

import random


def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]


def hi_ha_duplicats(llista):
    return "Hi ha duplicats" if len(llista) != len(set(llista)) else "No hi ha duplicats"


def elimina_duplicats(numlist):
    return list(set(numlist))

llista = llista_20_elements()
print("Llista generada:", llista)


llista_sense_duplicats = elimina_duplicats(llista)
print("La llista original {} i despres de eliminar els duplicats {}".format(llista, llista_sense_duplicats))

