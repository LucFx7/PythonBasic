"""Definir una funció comptar_vocals() que donada una paraula, compti el número de vegades que apareix
cada vocal. Ex: comptar_vocals(“Ratapinyada”) retorni1 HI ha 4 a’s, 0 e’s, 1 i’s, 0 o’s i 0 u’s

"""

a = 0
e = 0
i = 0
o = 0
u = 0



def comptar_vocals(p):
    global a, e, i, o, u 
    for ee in p:
        if ee == "a":
            a +=1
        if ee == "e":
            e +=1
        if ee == "i":
            i +=1
        if ee == "o":
            o +=1
        if ee == "u":
            u +=1
    return "Hi ha {} a, {} e, {} i, {} o i {} u".format(a, e, i, o, u)

# Programa principal
p = "Python"
resultat = comptar_vocals(p)
print("La paraula '{}' té aquestes vocals: {}".format(p, resultat))

    