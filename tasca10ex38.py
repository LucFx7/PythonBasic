"""Escriure un programa que demani dues paraules i ens digui si rimen o no. Rimen quan coincideixen 
les 3 darreres lletres i rimen un poc quan coincideixen les 2 darreres, si no ens ha de dir que no 
rimen.
"""


paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

def Rima(paraula1, paraula2):
    if paraula1[-3:] == paraula2[-3:]:
        print("Les paraules rimen")
    elif paraula1[-2:] == paraula2[-2:]:
        print("Les paraules rimen un poc")
    elif paraula1[-1:] == paraula2[-1:]:
        print("Les paraules casi no rimen")
    else:
        print("Les paraules no rimen") 
        
Rima(paraula1, paraula2)