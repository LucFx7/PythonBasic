"""Definir una funció elements_parells() que donada una llista de paraules, 
només ens mostri les que estan en la posició parell. Prova-la
"""

def crear_llista_fitxer(filename):
    llista = []
    wordsFile = open(filename, "r")
    for line in wordsFile:
        for word in line.split():
            llista.append(word.strip())
    wordsFile.close()
    return llista

def elements_parells(llista):
    for i in range(0, len(llista), 2):
        print(llista[i])

print(elements_parells(crear_llista_fitxer("paper.txt")))