def calc(t, a, b):
    if t == 1:
        return a * b
    elif t == 2:
        return (a * b) / 2
    elif t == 3:
        return 3.14159 * a * a
    else:
        return 0

print("Rectangulo 4x5:", calc(1, 4, 5))
print("Triangulo base 4 alt 6:", calc(2, 4, 6))
print("Circulo radio 3:", calc(3, 3, 0))
