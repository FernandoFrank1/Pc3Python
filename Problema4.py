# Problema 4

class RECTANGULO:
    def __init__(self, largo, ancho):
        if largo < 0 or ancho < 0:
            raise ValueError("ValueError: El largo y el ancho deben ser mayores que cero.")
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        try:
            area = self.largo * self.ancho
            return area
        except TypeError:
            print("TypeError: Los valores de largo y ancho deben ser números.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None


if __name__ == '__main__':
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        if largo < 0 or ancho < 0:
            print("Error: El largo y el ancho deben ser mayores que cero.")
        else:
            rectangulo = RECTANGULO(largo, ancho)
            area = rectangulo.calcular_area()
            if area is not None:
                print(f"El área del rectángulo es: {area}")
    except ValueError:
        print("ValueError: Ingrese un número válido para el largo y el ancho.")

