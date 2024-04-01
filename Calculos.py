# Problema 9

import Operaciones

def obtener_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("ValueError: Introduce un número válido.")

num1 = obtener_numero("Ingrese el primer número: ")
num2 = obtener_numero("Ingrese el segundo número: ")


print("Suma:", Operaciones.suma(num1, num2))
print("Resta:", Operaciones.resta(num1, num2))
print("Producto:", Operaciones.producto(num1, num2))
print("División:", Operaciones.division(num1, num2))
2
