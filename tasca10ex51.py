"""Definir una funció crear_llista_fitxer() on llegeixi un fitxer i transformi cada paraula 
llegida en un element de la llista. Prova-la.
"""

def crear_llista_fitxer(filename):
    llista = []
    wordsFile = open(filename, "r")
    for line in wordsFile:
        for word in line.split():
            llista.append(word.strip())
    wordsFile.close()
    return llista

print(crear_llista_fitxer("paper.txt"))