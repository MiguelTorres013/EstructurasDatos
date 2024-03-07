class Persona:

    def init(self, edad, genero,saludo):
        self.edad = edad
        self.genero = genero

edad = int(input('Edad: '))
genero = str(input('Genero: '))


class Empleado(Persona):
    def init(self, pago, puesto_trabajo):
        self.pago = pago
        self.puesto_trabajo = puesto_trabajo


pago = int(input("El salario del empleado es: "))
puesto_trabajo = str(input("El empleado trabaja en el area de: "))


class Estudiante(Persona):
    def init(self, grado, escuela):
        self.grado = grado
        self.escuela = escuela


grado = input("El estudiante esta en el curso: ")
escuela = input("El estudiante estudia en: ")