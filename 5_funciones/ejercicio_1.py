from math import pi

def calcAreaTriangulo(base, altura):
    return round((base*altura)/2, 2)

def calcAreaCirculo(radio):
    return round(pi*(radio**2), 2)

print('Área de triángulo: ' + str(calcAreaTriangulo(4.3, 5.25))+ ' m²')
print('Área de círculo: ' + str(calcAreaCirculo(4.16))+' m²')