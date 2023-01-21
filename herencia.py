
class Persona:
    def __init__(self, nombre, edad, apellido, sexo):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.sexo = sexo

    def datosPersonales(self):
        print("El nombre de la persona es: ", self.nombre)
        print("La edad de la persona es: ", self.edad)
        print("El apellido de la persona es ", self.apellido)
        print("El sexo de la persona es ", self.sexo)


miPersona = Persona("Juan", 28, "Jiron", "Masculino")
miPersona.datosPersonales()
print("============================")

class Empleado(Persona):
    def datosEmpleado(self, vacaciones, salario):
        print("Sus dias de vacaciones son: " + str(vacaciones))
        print("Su salario es: " +  str(salario))

miPersona2 = Empleado("Maria", 22, "Luna", "Femenino")
miPersona2.datosPersonales()
miPersona2.datosEmpleado(10, 20000)