from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser positivas.")
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser positivas.")
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura) / 2.0

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser positivo.")
        self.radio = radio
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Trapecio(FiguraGeometrica):
    def __init__(self, base_mayor, base_menor, altura):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Las bases y la altura deben ser positivas.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2.0

class CalculadoraAreas:
    def area_total(self, figuras):
        return sum(figura.calcular_area() for figura in figuras)

class ReporteAreasConsola:
    def mostrar_detalle(self, figuras, calculadora):
        for figura in figuras:
            print("-", type(figura).__name__, "area:", round(figura.calcular_area(), 4))
        print("Area total acumulada:", round(calculadora.area_total(figuras), 4))

if __name__ == "__main__":
    figuras_base = [Rectangulo(4, 5), Triangulo(4, 6), Circulo(3)]
    calc = CalculadoraAreas()
    rep = ReporteAreasConsola()
    print("Escenario 1 (Iniciales):")
    rep.mostrar_detalle(figuras_base, calc)
    figuras_ext = [*figuras_base, Trapecio(8, 4, 5)]
    print("Escenario 2 (Con Trapecio - OCP):")
    rep.mostrar_detalle(figuras_ext, calc)
