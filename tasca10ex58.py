"""Escriu un programa que, utlitzant, la sentència for mostri el següent:
	5 4 3 2 1
	4 3 2 1
	3 2 1
 	2 1
	1
"""

def sequnciaNombres(max):
    for i in range(max, 0, -1):
        for e in range(i, 0, -1):
            print(e, end=" ")
        print()
        
sequnciaNombres(5)