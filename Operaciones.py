# Problema 9

def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("TypeError: Tipo de dato no válido.")

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        print("TypeError: Tipo de dato no válido.")

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        print("TypeError: Tipo de dato no válido.")

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("ZeroDivisionError: No es posible dividir entre cero.")
    except TypeError:
        print("TypeError: Tipo de dato no válido.")

