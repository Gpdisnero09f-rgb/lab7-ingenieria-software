import math

def _validar_entero(numero):
    if isinstance(numero, bool) or not isinstance(numero, int):
        raise TypeError("El parametro numero debe ser un entero.")
    return numero

def _tiene_divisor_impar(numero):
    limite = math.isqrt(numero) + 1
    return any(numero % divisor == 0 for divisor in range(3, limite, 2))

def es_primo(numero):
    valor = _validar_entero(numero)
    if valor < 2:
        return False
    if valor == 2:
        return True
    if valor % 2 == 0:
        return False
    return not _tiene_divisor_impar(valor)
