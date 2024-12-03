def menu():
    op = 0
    while op < 1 or op > 9:
        print("Menu")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Binari")
        print("6. Octal")
        print("7. Decimal")
        print("8.Hexadecimal")
        print("9. Sortir")
        op = int(input("Introdueix una opcio: "))
    return op

def sumar():
    a = int(input("Introdueix el primer element: "))
    b = int(input("Introdueix el segon element: "))
    c = a + b
    print("El resultat de sumar {} + {} és {}".format(a, b, c))

def restar():
    a = int(input("Introdueix el primer element: "))
    b = int(input("Introdueix el segon element: "))
    c = a - b
    print("El resultat de restar {} - {} és {}".format(a, b, c))

def multiplicar():
    a = int(input("Introdueix el primer element: "))
    b = int(input("Introdueix el segon element: "))
    c = a * b
    print("El resultat de multiplicar {} * {} és {}".format(a, b, c))

def dividir():
    a = int(input("Introdueix el primer element: "))
    b = int(input("Introdueix el segon element: "))
    c = a / b
    print("El resultat de dividir {} / {} és {}".format(a, b, c))

def binari():
    a = int(input("Introdueix el número decimal: "))
    print("El número {} en binari és {}".format(a, bin(a)[2:]))

def octal():
    a = int(input("Introdueix el número decimal: "))
    print("El número {} en octal és {}".format(a, oct(a)[2:]))

def decimal():
    base = int(input("Introdueix la base (2 per binari, 8 per octal, 16 per hexadecimal): "))
    num = input("Introdueix el número en la base especificada: ")
    print("El número {} en decimal és {}".format(num, int(num, base)))

def hexadecimal():
    a = int(input("Introdueix el número decimal: "))
    print("El número {} en hexadecimal és {}".format(a, hex(a)[2:]))

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
            binari()
        case 6:
            octal()
        case 7:
            decimal()
        case 8:
            hexadecimal()
        case 9:
            print("Adéu")
            b = False
