#Definir una funció sumar_llista() i una funció multiplicar_llista() que sumin i multipliqueu, respectivament, tots els valors d’una llista. Prova-la amb diferents exemples. Ex: sumar_llista([1,2,3,4]) retorni 10.



def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a= input("introdueix un numero: ")
        if a!=".":
            l.append(int(a))
    return l

def sumar_llista(l):
    suma = 0
    for e in l:
        suma += e
    return suma

def multiplicar_llista(l):
    multiplicacio=1
    if 0 in l or len(l)==0:
        return 0
    else:
        for e in l:
            multiplicacio *= e
    return multiplicacio
    

#programa principal
l=llegir_llista()
print("La suma dels elements de las llista {} es {}".format(l, sumar_llista(l)))
print("La multiplicacio dels elements de la llista {} es {}".format(l, multiplicar_llista(l)))