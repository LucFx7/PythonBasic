#Escriure un programa que converteixi el números binaris en enters.
def binari_a_decimal(b):
    a = b[::-1]
    c=0
    for i,e in enumerate(b):
        c+=int(e)*(2**i)
    return c
#Programa principal
a = input("Introduexi un número en binari: ")
print("El número {}-binari és {}-decimal".format(a,binari_a_decimal(a)))
