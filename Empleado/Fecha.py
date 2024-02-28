class Fecha:
    #Aqui va todo el codigo de fecha
    """------------------------------
    # Atributos ---------------------"""
    dia=0
    mes=0
    anio=0

    def ConsultarDia(self):
        #Aquí va el código del método
        return self.dia
        
    def ConsultarMes(self):
        #Aquí va el código del método
        return self.mes
        
    def ConsultarAnio(self):
        return self.anio
        
    def ConsultarFecha(self):
        return self.dia + "/" + self.mes + "/" + self.anio