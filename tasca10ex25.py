#Definir una funció gran_llista() que donada una llista de número ens retorni el més gran. Ex: gran_llista([3, 4, 2, 3, 10]), retorni 10.

def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l
def gran_llista(l):
    return max(l)

#programa principal
a=llegir_llista()
print("El numero mes gran de la {} es {}".format(a,gran_llista(a)))

   