class Coche():
    def __init__(self):
        self.marca="Audi"
        self.color="Rojo"
        self.__anio=2000
        self.enmarcha=False
        print(f"Se ha creado un auto marca {self.marca} color {self.color} anio {self.__anio}")

    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El cche se encuentra apagado"

    def __str__(self):
        return "Este auto es marca {}, de color {}, anio {} ".format(self.marca, self.color, self.__anio)

    def __del__(self):
        print(f'Se ha vendido el auto marca {self.marca} color {self.color} anio {self.__anio}')

miCoche = Coche()
print(miCoche.arrancar(True))
print(str(miCoche))
miCoche.__anio = 2010
print(str(miCoche))