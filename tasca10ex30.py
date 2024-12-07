"""Escriure un programa on donats l’any actual, i l’any de naixement i el nom de 4 persones, calculi els anys que farà cada un d’ells l’any actual i imprimeixi totes les dades tabulades per pantalla. Ex:
Any actual 2022
Nom			Data naixement	Anys que farà aquest any
Pere			2000			22
Maria			1999			23
Anna			2005			17"""


def taula(dato):
    print("Any actual", any_actual)
    print(f"{'Nom':<8}{'Naixement':<10}{'Edat':<4}")
    print("-"*30)
    for nom, naixement in dato:
        edat = any_actual - naixement
        print(f"{nom:<8}{naixement:<10}{edat:<4}")
        
        
 #Programa principal       
any_actual = 2024
personas = [
    ("Alex", 1999),
    ("Anna", 2009),
    ("Pere", 2001),
    ("Maria", 1975)
]

taula(personas)
