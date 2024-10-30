def menu():
    op = 0
    while op<1 or op>5:
        print("Menu")
        print("1. Sumar")
        print("2. restar")
        print("3. multiplicar")
        print("4. dividir")
        print("5. Sortir")
        op = int(input("Introdueix una opcio: "))
    return op
def sumar():
    a = int(input("introdueix el primer element: "))
    b = int(input("introdueix el segon element: "))
    c = a + b
    print("el resultat de sumar {} + {} es {}".format(a, b, c))
def restar():
    a = int(input("introdueix el primer elemen: t"))
    b = int(input("introdueix el segon element: "))
    c = a - b
    print("el resultat de restar {} + {} es {}".format(a, b, c))
def multiplicar():
    a = int(input("introdueix el primer element: "))
    b = int(input("introdueix el segon element: "))
    c = a * b
    print("el resultat de multiplicar {} + {} es {}".format(a, b, c))
def dividir():
    a = int(input("introdueix el primer element: "))
    b = int(input("introdueix el segon element: "))
    c = a / b
    print("el resultat de dividir {} + {} es {}".format(a, b, c))

b = True
while b:
    op = menu()
    match(op):
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
        case 5:
            print ("Adeu")
            b = False
       
            
