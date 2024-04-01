from Problema3 import CIRCULO
from Problema4 import RECTANGULO

def calcular_area_circulo():
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        circulo = CIRCULO(radio)
        area = circulo.calcular_area()
        print("El área del círculo es:", area)
    except ValueError:
        print("Error: Ingrese un número válido para el radio del círculo.")

def calcular_area_rectangulo():
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        rectangulo = RECTANGULO(largo, ancho)
        area = rectangulo.calcular_area()
        print("El área del rectángulo es:", area)1
    except ValueError:
        print("Error: Ingrese números válidos para el largo y el ancho del rectángulo.")

def calcular_area_cuadrado():
    try:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado ** 2
        print("El área del cuadrado es:", area)
    except ValueError:
        print("Error: Ingrese un número válido para el lado del cuadrado.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    menu()
