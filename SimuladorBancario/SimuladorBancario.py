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

    #1er Punto
    tipoCliente = ""

    """---------------------------------------------------------
    # Asociaciones
    ---------------------------------------------------------"""

    cuentaAhorros = CuentaAhorros()
    cuentaCorriente = CuentaCorriente()
    cdt = CDT()

    """---------------------------------------------------------
    # METODOS
    ---------------------------------------------------------"""

    def __init__(self, tipoCliente):
        #Iniciamos el tipo de cliente según el valor recibido por parametro
        self.tipoCliente = tipoCliente

    
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


    
"""----------------------------------------------
    SOLUCION TALLER
------------------------------------------------"""

    #3er Punto

    def CambiarTipoCliente(self, nTipoCliente):
        self.tipoCliente = nTipoCliente
        return "El tipo de cliente cambió a: " + nTipoCliente

