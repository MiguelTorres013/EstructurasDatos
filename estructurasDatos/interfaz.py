from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)

rectangulo = Rectangulo(7, 93)
print("Área del rectángulo: {rectangulo.calcularArea()}")
print("Perímetro del rectángulo: {rectangulo.calcularPerimetro()}")