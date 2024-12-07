"""Escriure un programa que si li introduïm un número menor de 100, mostri la suma dels quadrats 
dels números que estan separats entre sí per a quatres posicions. Ex: 80 --> 76**2 + 72**2 + 68**2 + 
... 
"""

resultat = 0

def quadrats(n):
    global resultat
    while n > 0:
        resultat += n**2
        n -= 4
        
quadrats(int(input("Quin nombre vols introduir? ")))
print("La suma dels quadrats dels nombres anteriors és: {}".format(resultat))