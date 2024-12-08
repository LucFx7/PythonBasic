"""Escriu un programa que ens indiqui tots els números primers entre 1 i 100 
i ens digui quants n’hi ha.
"""

def nombresPrimers(max):
    for num in range(2,max+1):    
        prime = True
        for i in range(2,num):
            if (num%i == 0):
                prime = False
        if prime:
            print(num)
#programa principal
nombresPrimers(100)