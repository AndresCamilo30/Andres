from Punto import Punto
from Color import Color

class Triangulo:

    # Atributos
    punto1 = Punto()
    punto2 = Punto()
    punto3 = Punto()

    colorRelleno = Color()
    colorLinea = Color()

    # Asociaciones

    color= Color()
    punto= Punto()


    def DibujarTriangulo(self, x, y):
        self.punto1.UbicarPunto(x, y)
        self.punto2.UbicarPunto(x, y)
        self.punto3.UbicarPunto(x, y)

    

