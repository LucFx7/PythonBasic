"""Definir una funció  mostrar_majors_que() que donada una tupla de números enters, 
imprimeixi tots els superiors a un altre número donat. 
Per provar que funciona bé, escriure un programa que permeti 
introduir els valors enters de la tupla  i ens digui tots els que són majors de 18 anys.
"""

def mostrar_major_que(a,n):
    return [e for e in a if e > n]

#programa principal
print(mostrar_major_que([1,2,3,4,5,6,7,8,9],4))