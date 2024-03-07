class Coche:
    def __init__(self, velocidad_inicial):
        self._velocidad = velocidad_inicial

    def acelerar(self, acelerar):
        self._velocidad += acelerar

    def frenar(self, frenar):
        if self._velocidad - frenar >= 0:
            self._velocidad -= frenar
        else:
            self._velocidad = 0

    def obtener_velocidad(self):
        return self._velocidad