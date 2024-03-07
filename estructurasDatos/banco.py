class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    def depositar(self, monto):
        self._saldo += monto

    def retirar(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
        else:
            raise ValueError("Saldo insuficiente")

    def consultar_saldo(self):
        return self._saldo
