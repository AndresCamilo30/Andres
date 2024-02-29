from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario: 
        #Aquí va el código del CDT
    """---------------------------------------------------------
    # Atributos
    ---------------------------------------------------------"""

    cedula = ""
    nombre = ""
    mesActual = 0

    """---------------------------------------------------------
    # Asociaciones
    ---------------------------------------------------------"""

    cuentaAhorros = CuentaAhorros()
    cuentaCorriente = CuentaCorriente()
    cdt = CDT()

    """---------------------------------------------------------
    # METODOS
    ---------------------------------------------------------"""
    
    def DarInteresMensual(self):
        #Aquí va el código del método
        return 0
    
    def ConsignarCuentaCorriente(self, valorConsignacion):
        self.cuentaCorriente.ConsignarValor(valorConsignacion)
    
    def CalcularSaldoTotal(self):
        saldoTotal = self.cuentaAhorros.saldo + self.cuentaCorriente.saldo
        return "El saldo total es de: " + saldoTotal
    
    def TransferirSaldoAhorrosaCorriente(self):
        self.cuentaCorriente.ConsignarValor(CuentaAhorros.ConsultarSaldo())
        self.cuentaAhorros.RetirarValor(CuentaAhorros.ConsultarSaldo())
        return "El saldo de la cuenta de ahorros ha sido transferido a la cuenta corriente."

    def ConsultarSaldoCorriente(self):
        saldo = self.cuentaCorriente.saldo
        return "El saldo de la cuenta corriente es de: " + saldo

    def RetirarTodoCuentaCorriente(self):
        total = self.CalcularSaldoTotal()
        self.cuentaCorriente.RetirarValor(self.cuentaCorriente.ConsultarSaldo())
        self.cuentaAhorros.RetirarValor(self.cuentaAhorros.ConsultarSaldo())
        return "Retiraste total: " + total

    def DuplicarAhorro(self):
        self.cuentaAhorros.ConsignarValor(self.cuentaAhorros.ConsultarSaldo())
        return "El nuevo saldo de la cuenta de ahorros es de: " + self.cuentaAhorros.ConsultarSaldo()


    
    #Crear asociaciones y crear dentro de la clase simulador bancario crear los metodos: ConsignarCuentaCorriente, 
    #CalcularSaldoTotal, Pasar saldo de ahorro a corriente

    #Tarea
    #crear metodos Consultar Saldo Corriente, Retirar Todo Cuenta Corriente, Duplicar Ahorro