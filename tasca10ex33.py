"""Variar l’exercici anterior, perquè enlloc de la lletra a,
sigui una lletra introduïda per teclat per l’usuari."""

def nums_que_comencen_per(n,l):
    Nom = [n for n in n if n[0] == l]
    quantitat = len(Nom)
    return Nom, quantitat

#programa principal
lletra = input("Introdueix la lletra per la qual han de començar els noms: ")
Nom, quantitat = nums_que_comencen_per(["Alex", "Maria", "Anna", "Albert"], lletra)
print("Noms que començen per {}: {}".format(lletra, Nom))
print("Quantitat de noms que començen per {}: {}".format(lletra, quantitat))
