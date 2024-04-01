# Problema 3

import math

class CIRCULO:
    def __init__(self, radio):
        try:
            if radio <= 0:
                raise ValueError("El radio debe ser un número positivo.")
            self.radio = radio
        except ValueError as ve:
            print("Error:", ve)

    def calcular_area(self):
        try:
            area = math.pi * (self.radio ** 2)
            return area
        except AttributeError:
            print("AttributeError: Asegúrate de haber definido el radio correctamente.")

if __name__ == '__main__':
    try:
        radio = float(input("Introduce el radio del círculo: "))
        mi_circulo = CIRCULO(radio)
        print("El área del círculo es:", mi_circulo.calcular_area())
    except ValueError:
        print("ValueError: El radio debe ser un número real positivo.")
    except ZeroDivisionError:
        print("ZeroDivisionError: El radio no puede ser cero.")
    except KeyboardInterrupt:
        print("\nSe interrumpió la ejecución.")

