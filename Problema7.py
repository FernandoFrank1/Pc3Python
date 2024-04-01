# Problema 7

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante IV"
        elif self.x == 0 and self.y != 0:
            return "Sobre eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre eje X"
        else:
            return "Sobre el origen"
    
    def vector(self, otro_punto):
        x_resultante = otro_punto.x - self.x
        y_resultante = otro_punto.y - self.y
        return Punto(x_resultante, y_resultante)
    
    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        print(f"La distancia entre {self} y {otro_punto} es: {distancia}")

x1 = int(input("Ingrese la coordenada X del primer punto: "))
y1 = int(input("Ingrese la coordenada Y del primer punto: "))
x2 = int(input("Ingrese la coordenada X del segundo punto: "))
y2 = int(input("Ingrese la coordenada Y del segundo punto: "))

p1 = Punto(x1, y1)
p2 = Punto(x2, y2)

print("Punto 1:", p1)
print("Punto 2:", p2)
print("Cuadrante Punto 1:", p1.cuadrante())
print("Cuadrante Punto 2:", p2.cuadrante())
print("Vector Punto 1 a Punto 2:", p1.vector(p2))
p1.distancia(p2)

