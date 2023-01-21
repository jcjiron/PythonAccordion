def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1*num2

def dividir(num1, num2):
    return num1/num2


num1 = int(input("Introduce el numero 1: "))
num2 = int(input("Introduce el numero 2: "))
operacion = int(input("Introduce la operacion a realizar \n Suma (1), Resta (2), Multiplicacion (3) y Division (4): "))

if operacion == 1:
    print(suma(num1, num2))
elif operacion == 2:
    print(resta(num1, num2))
elif operacion == 3:
    print(multiplicar(num1, num2))
elif operacion == 4:
    try: 
        print(dividir(num1, num2))
    except ZeroDivisionError:
        print("Error, la division que has intentado realizar no es valida")
else :
    print("Error, operacion no valida")
    print("Las operaciones validas son: Suma (1), Resta (2), Multiplicacion (3) y Division (4)")


print("Operacion ejecutada")