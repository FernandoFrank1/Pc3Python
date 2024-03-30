# Problema 1:

def Porcentajes(a):
    try:
        x, y = map(int, a.split('/'))
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            return Porcentajes(input("Ingrese una fracción nuevamente, donde X debe ser menor o igual a Y: "))

        porcentaje = (x / y) * 100
        if porcentaje < 1:
            return 'E'
        elif porcentaje > 99:
            return 'F'
        else:
            return str(round(porcentaje)) + '%'
        
    except ValueError:
        print("ValueError: Ingresar una fracción válida en el formato X/Y, donde X e Y son números enteros.")
        return Porcentajes(input("Ingrese una fracción nuevamente: "))
    
    except ZeroDivisionError:
        print("ZeroDivisionError: El denominador (Y) no puede ser cero.")
        return Porcentajes(input("Ingrese una fracción nuevamente: "))

if __name__ == '__main__':
    fraccion = input("Ingrese una fracción en el formato X/Y: ")
    resultado = Porcentajes(fraccion)
    print("Cantidad de combustible en el tanque:", resultado)