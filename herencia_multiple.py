class Clase1:
    def metodo1():
        print("Metodo uno")

class clase2:
    def metodo2():
        print("Metodo dos")

class Clase3(Clase1, clase2):
    def metodo3():
        print("Metodo tres")


instancia = (Clase3)

instancia.metodo1()
instancia.metodo2()
instancia.metodo3()