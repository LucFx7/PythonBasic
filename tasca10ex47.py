"""Definir una funció esta_ordenada() que donada una llista de números, ens indiqui si està 
ordenada en ordre ascendent, descendent o no està ordenada. Prova-la. Ex. esta_ordenada([3,2,1]) 
retorni està ordenada de forma descendent. esta_ordenada([4,5,6]) retorni està ordenada de forma 
ascendent i qualsevol altres cas retorni no està ordenada.
"""

def esta_ordenada(l):
    if l == sorted(l):
        return "ascendent"
    elif l == sorted(l, reverse=True):
        return "descendent"
    else:
        return "no ordenada"
    
#programa principl
print(esta_ordenada([5, 4, 2, 3, 1]))    