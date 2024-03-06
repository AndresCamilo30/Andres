from Fecha import Fecha

class Empleado:
    # Aqui va el codigo del empleado
    """------------------------------
    # Atributos ---------------------"""
    nombre=""
    apellido=""
    #1er Punto
    nHijos = 0
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


    """--------------------------------------------------
    #SOLUCION TALLER
    -----------------------------------------------------"""
    
    #2do Punto
    def ConsultarNumeroDeHijos(self):
        return self.nHijos


    #3er Punto
    def CalcularAuxilioEducativo(self):
        salarioEmpleado = self.salario
        numeroDeHijos = self.ConsultarNumeroDeHijos()
        porcentaje = (salarioEmpleado * 5) / 100
        auxilioEducativo = porcentaje * numeroDeHijos
        return auxilioEducativo

    #4to Punto
    def CalcularAuxilioEducativo(self, porcentaje):
        salarioEmpleado = self.salario
        numeroDeHijos = self.ConsultarNumeroDeHijos()
        porcent = (salarioEmpleado * porcentaje) / 100
        auxilioEducativo = porcent * numeroDeHijos
        return auxilioEducativo

    #5to Punto
    def CalcularDiferenciaSalarial(self, salario2):
        diferenciaSalarial = self.salario - salario2
        return "La diferencia salarial con respecto al otro empleado es de: $" + diferenciaSalarial

    #6to Punto

    """
    En el curso he aprendido varios conceptos nuevos, entre los cuales están
    1. Clases y objetos
    2. Métodos y para qué sirve
    3. Atributos
    4. Asociaciones
    5. Requerimiento funcional
    6. Mundo del problema
    7. Requerimientos no funcionales

    Una dificultad que se me presentó al principio fué que los conceptos eran muy abstractos, 
    y se me complicaba un poco entenderlos, pero con algo de práctica y estudio esos conceptos se fueron
    reforzando.

    """