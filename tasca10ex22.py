#22. Definir una funció crear_repetits() que agafi un número enter i un caràcter i retorni el caràcter multiplicat pel número enter. Ex: crear_repetits(5, “a”), retorni “aaaaa”

def crear_repetits(f,t):
    return f*t

#programa principal
a = input("Introdueix un caracter: ")
b = int(input("Introdueix el numero de vegades que vols que es repeteixi el caracter: "))
print("El caracter {} repetit {} vegades es {}".format(a,b,crear_repetits(a,b)))

    
