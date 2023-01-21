class Perro:
    def hablar(self):
        print("Guau")

class Gato:
    def hablar(self):
        print("Miau")

def escucharMascota(animal):
    animal.hablar()

miMascota=Perro()
escucharMascota(miMascota)
