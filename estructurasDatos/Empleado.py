class Empleado:
    def _init_(self,pago,puesto_trabajo):
        self.salario = pago
        self.puesto_trabajo = puesto_trabajo

pago = int(input("El salario del empleado es: "))
puesto_trabajo = str(input("El empleado trabaja en el area de:"))