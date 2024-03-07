class Rectangulo:

    def _init_(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho

longitud = int(input("Longitud: "))
ancho = int(input("Ancho:"))

area = longitud*ancho
perimetro = (2*longitud) + (2*ancho)

print("El area es: ",area,"y el perimetro es:",perimetro)