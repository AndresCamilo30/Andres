class CuentaCorriente:
        #Aquí va el código del CDT
    """---------------------------------------------------------
    #Atributos
    ---------------------------------------------------------"""
    saldo = 0

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