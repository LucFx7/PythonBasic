#17. Definir una funció que agafi un caràcter i retorni vertader si és una vocal i en cas contrari retorni fals. Prova-la amb diferents exemples.
def esvocal(x):
    return x.lower() in "aeiou"
#programa principal
a = "a"
while(a!="."):
    a = input("Escriu una lletra: ")
    if esvocal(a):
        print("La lletra {} és vocal".format(a))
    else:
        print("La lletra {} no és una vocal".format(a))
