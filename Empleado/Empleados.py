from Fecha import Fecha

class Empleado:
    # Aqui va el codigo del empleado
    """------------------------------
    # Atributos ---------------------"""
    nombre=""
    apellido=""
    """---------------------------------
    # 1 = Masculino 2 = Femenino ---"""
    sexo=0 
    salario=0

    """------------------------------
    Asociaciones
    ---------------------------------"""

    fechaNacimiento = Fecha()
    fechaIngreso = Fecha()

    """------------------------------
    # Metodos
    --------------------------------"""
    def CambiarSalario(self, nuevoSalario):
        #Aquí va el código del método
        self.salario = nuevoSalario
        return self.salario

    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        #Aquí va el código del método
        return None

    def ConsultarSalario(self):
        #Aquí va el código dek método
        return self.salario

    def NombreCompleto(self):
        #Aquí va el código del método
        return self.nombre
    
    def ApellidoCompleto(self):
        #Aquí va el código del método
        return self.apellido
    
    def ConsultarSexo(self):
        #Aquí va el código del método
        return self.sexo
    
    def ConsultarNobreCompleto(self):
        #Aquí va el código del método
        return self.nombre + " " + self.apellido
    
    def CambiarNombre(self, nNombre):
        #Aquí va el código del método
        self.nombre = nNombre
        return self.nombre
    
    def CambiarApellido(self, nApellido):
        #Aquí va el código del método
        self.apellido = nApellido
        return "El nuevo apellido es " + self.apellido

    def DuplicarSalario(self):
        # Aquí va el código del método
        # Forma 1
        # self.salario = self.salario2
        # Forma 2 pro
        self.salario *= 2

    def CalcularSalarioAnual(self):
        # Aquí va el código del método
        # Forma 1
        salarioAnual = self.salario * 12
        return "El salario anual del Empleado es de: " + salarioAnual
        # Forma 2
        # return self.salario * 12
    
    def ConsultarDiaCumpleaños(self):
        return "El día de su cumpleaños es: " + self.fechaNacimiento.ConsultarDia
    
    def CalcularImpuestos(self):
        total = self.CalcularSalarioAnual()
        return (total * 19.5) / 100 # 19.5 es el porcentaje de impuesto 

        # Forma 2
        #return self.CalcularSalarioAnual() * 0.195

