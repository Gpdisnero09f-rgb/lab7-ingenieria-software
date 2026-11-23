import math

def validar_dimension_positiva(valor, nombre_parametro):
    if valor <= 0:
        raise ValueError("Dimension invalida: " + nombre_parametro)

def calcular_area_rectangulo(base, altura):
    validar_dimension_positiva(base, "base")
    validar_dimension_positiva(altura, "altura")
    return base * altura

def calcular_area_triangulo(base, altura):
    validar_dimension_positiva(base, "base")
    validar_dimension_positiva(altura, "altura")
    return (base * altura) / 2.0

def calcular_area_circulo(radio):
    validar_dimension_positiva(radio, "radio")
    return math.pi * (radio ** 2)

if __name__ == "__main__":
    print("Area rectangulo (4x5):", round(calcular_area_rectangulo(4, 5), 2))
    print("Area triangulo (base=4, altura=6):", round(calcular_area_triangulo(4, 6), 2))
    print("Area circulo (radio=3):", round(calcular_area_circulo(3), 4))
