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
    # Metodos
    --------------------------------"""
    def CambiarSalario(self, nuevoSalario):
        #Aquí va el código del método
        return 0

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
    
    def consultarSexo(self):
        #Aquí va el código del método
        return self.sexo