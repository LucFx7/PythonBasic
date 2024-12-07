"""Definir una funció nums_que_comencen_per() que donat una llista de noms, 
ens digui quants comencen per la lletra a.
"""
def nums_que_comencen_per(n,l):
    Nom = [n for n in n if n[0] == l]
    quantitat = len(Nom)
    return Nom, quantitat

#programa principal
Nom, quantitat = nums_que_comencen_per(["Alex", "Maria", "Anna", "Albert"], "A")
print("Noms que començen per 'A': {}".format(Nom))
print("Quantitat de noms que començen per 'A': {}".format(quantitat))
