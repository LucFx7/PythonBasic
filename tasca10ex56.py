"""Escriure un programa que, utilitzant, la sentència for mostri el següent:
*
**
***
**
*
"""


def dibuixPunts(max):
    for i in range(1, max+1):
        print("*" * i)
    for i in range(max-1, 0, -1):
        print("*" * i)


#programa principal
dibuixPunts(3)