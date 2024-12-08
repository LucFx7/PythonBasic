"""Definir una funció index_paraula() on donada una llista ordenada de paraules, +
ens retorni l’índex on es troba una paraula determinada o -1 en cas que no hi sigui.
"""

def index_paraula(list, word):
    if word in list:
        return list.index(word)
    else:
        return -1
    
def crear_llista_fitxer(filename):
    llista = []
    wordsFile = open(filename, "r")
    for line in wordsFile:
        for word in line.split():
            llista.append(word.strip())
    wordsFile.close()
    return llista

print(index_paraula(crear_llista_fitxer("paper.txt"), "Hola"))