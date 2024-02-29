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

    def ConsignarValor(valor):
        #Aquí va el código del método
        return valor
    
    def RetirarValor(self):
        #Aquí va el código del método
        return 0
    
    def DarInteresMensual(self):
        #Aquí va el código del método
        return 0
    
    def ConsignarCuentaCorriente(self, valorConsignacion):
        #self.cuentaCorriente.saldo += valorConsignacion
        self.cuentaCorriente.saldo += self.ConsignarValor(valorConsignacion)
        return "Usted ha consignado: " + valorConsignacion
    
    def CalcularSaldoTotal(self):
        saldoTotal = self.cuentaAhorros.saldo + self.cuentaCorriente.saldo
        return "El saldo total es de: " + saldoTotal
    
    def TransferirSaldoAhorrosaCorriente(self):
        self.cuentaCorriente.saldo += self.cuentaAhorros.saldo
        self.cuentaAhorros.saldo = 0
        return "El saldo de la cuenta de ahorros ha sido transferido a la cuenta corriente."

    def ConsultarSaldoCorriente(self):
        saldo = self.cuentaCorriente.saldo
        return "El saldo de la cuenta corriente es de: " + saldo

    def RetirarTodoCuentaCorriente(self):
        return 0

    def DuplicarAhorro(self):
        nuevoAhorro = self.cuentaAhorros.saldo * 2
        return "El nuevo saldo de la cuenta de ahorros es de: " + nuevoAhorro


    
    #Crear asociaciones y crear dentro de la clase simulador bancario crear los metodos: ConsignarCuentaCorriente, 
    #CalcularSaldoTotal, Pasar saldo de ahorro a corriente

    #Tarea
    #crear metodos Consultar Saldo Corriente, Retirar Todo Cuenta Corriente, Duplicar Ahorro