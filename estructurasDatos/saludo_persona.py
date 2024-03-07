class Persona:
    def saludo(self):
     print("Hola, ¿Como estas?")

class Empleado(Persona):
    def saludo(self):
        super().saludo()
        print("Hola jefe")

class Estudiante(Persona):
    def saludo(self):
        super().saludo()
        print("Hola profesor")


persona = Persona()
persona.saludo()

empleado = Empleado()
empleado.saludo()

estudiante = Estudiante()
estudiante.saludo()