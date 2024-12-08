"""Definir una funció eliminarcapicua() que donada una llista, elimini el primer i el darrer
element de la llista i ens retorni una nova llista sense aquest dos elements. Prova-la
"""

def eliminarcapicua(l):
    l.remove(l[0])
    l.remove(l[-1])
    return l

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(eliminarcapicua(l))