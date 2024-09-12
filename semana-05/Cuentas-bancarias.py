class Cuenta:
    def __init__(self, saldo, numero, nombre):
        self.saldo = saldo
        self.numero = numero
        self.nombre = nombre

    def depositar(self, importe):
        self.saldo += importe

    def extraer(self, importe):
        pass


class CajaDeAhorro(Cuenta):

    def __init__(self, saldo, numero, nombre):
        super().__init__(saldo, numero, nombre)

    def extraer(self, importe):
        if self.saldo < importe:
            return False
        else:
            self.saldo -= importe
            return True


class CuentaCorriente(Cuenta):

    def __init__(self, saldo, numero, nombre, acuerdo):
        super().__init__(saldo, numero, nombre)
        self.acuerdo = acuerdo

    def extraer(self, importe):
        if (self.saldo + self.acuerdo) < importe:
            return False
        else:
            self.saldo -= importe
            return True


def main():
    cc = CuentaCorriente(1000,
                         1234,
                         'Facundo Montenegro (CC)',
                         2000)

    ca = CajaDeAhorro(1000,
                      1234,
                      'Facundo Montenegro (CA)')

    print(cc.extraer(1500))
    print(ca.extraer(1500))


if __name__ == '__main__':
    main()
