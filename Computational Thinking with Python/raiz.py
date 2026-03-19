import math

def calcular_raizes(a, b, c):
    # Calcula o delta
    delta = (b**2) - (4*a*c)
    
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Duas raizes reais: x1 = {x1}, x2 = {x2}")


    
a = 2
b = -8
c = 6
print(calcular_raizes(a, b, c))
