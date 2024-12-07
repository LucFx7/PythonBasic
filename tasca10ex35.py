"""Definir una funció es_de_traspas() donat un any, ens indiqui si és de traspàs o no. Un any 
és de traspàs si és divisible per 4, però no per 100 i també és divisible per 400.
"""
def es_de_traspas(any):
    if any % 4 == 0:
        if any % 100 == 0:
            if any % 400 == 0:
                print("l'any {} es de traspas.".format(any))
            else:
                print("l'any {} no es de traspas.".format(any))
        else:
            print("l'any {} es de traspas.".format(any))
    else:
        print("l'any {} no es de traspas.".format(any))
#programa principal
es_de_traspas(2024)