""""Definir una funció hi_ha_duplicats() que ens indiqui si una llista donada 
té qualque element duplicat o no, no s’ha de modificar la llista donada. 
Prova-la."""



def hi_ha_duplicats(l):
    if len(l) == len(set(l)):
        return "No hi ha duplicats"
    else:
        return "Hi ha duplicats"


print(hi_ha_duplicats([1,4,4,3,2,2,5,5,6,7,9]))