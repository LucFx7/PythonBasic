"""Escriure un programa que calculi en quan s'hauria convertit el nostre capital al final dels anys.
Per això li hem de demanar a l’usuari que introdueixi la quantitat a sol·licitar 
(mínim 50000€ màxim 800000€), un interès (mínim 0.5% i màxim 13%) i el número d’anys (
    mínim 3 anys - màxim 40 anys).  La fórmula per calcular-ho és: Cfinal =
    Cinicial * (1 + interés/100) **  anys.  Ex. 10000€ a 4.5% d’interés a 20 anys s’ha de convertir 
    en 24117.14€
"""

Cinicial = float(input("Introdueix la quantitat inicial: "))
while Cinicial < 50000 or Cinicial > 800000:
    print("La quantitat inicial ha de ser entre 50000 i 800000")
    Cinicial = float(input("Introdueix la quantitat inicial: "))

interes = float(input("Introdueix l'interes anual: "))
while interes < 0.5 or interes > 13:
    print("L'interes anual ha de ser entre 0.5 i 13")
    interes = float(input("Introdueix l'interes anual: "))
    
anys = float(input("Introdueix el nombre d'anys: "))    
while anys < 3 or anys > 40:
    print("Els anys han de ser entre 3 i 40")
    anys = float(input("Introdueix el nombre d'anys: "))

Cfinal = round(Cinicial * (1 + interes/100) ** anys, 2)

print ( "{}€ a {}% d’interés a {} anys s’ha de convertir en {}€".format(Cinicial, interes, anys, Cfinal))