class CuentaAhorros:
        #Aquí va el código de la cuenta de ahorros
    """---------------------------------------------------------
    #Atributos
    ---------------------------------------------------------"""
    saldo = 0
    interesMensual = 0

    def ConsultarSaldo(self):
        return self.saldo

    def ConsignarValor(self, valor):
        #Aquí va el código del método
        nSaldo = self.saldo + valor
        return nSaldo
    
    def RetirarValor(self, valor):
        #Aquí va el código del método
        nSaldo = self.saldo - valor
        return nSaldo